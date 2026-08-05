#!/usr/bin/env python3
"""text-to-map-nlp — 自然语言生成地图

用一句自然语言描述（如"生成北京的植被指数地图"）自动生成一张专题地图：
解析意图 -> 选择图层类型与配色 -> 渲染带地理范围的地图 PNG + GeoJSON 边界。

本 skill 是 LLM/NL2Map 系统的**离线 numpy 等价实现**：
不依赖大模型/网络，而用可验证的规则流程复现"自然语言 -> 地图参数 -> 渲染"——

1. **关键词解析**：从文本中按关键词规则提取图层类型（植被/高程/灯光/水体/温度/
   地物）、配色方案、地名与标题（等价于 NLP 意图识别 + 槽位填充）；
2. **图层合成**：按图层类型生成物理一致的模拟栅格（离线，无需真实数据）；
3. **地图渲染**：用 matplotlib 把栅格按 bbox 地理范围渲染成带色条/标题的 PNG，
   并输出 bbox 边界 GeoJSON。

数据源：本地 GeoTIFF（``--input`` 直接作为图层），或 ``--synthetic``/默认 bbox
合成图层。``--query`` 控制图层类型与地图标题。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python text-to-map-nlp.py --query "上海夜间灯光" --bbox 121 31 122 32 --output-dir ./out
    python text-to-map-nlp.py --bbox 116 39 117 40 --synthetic --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "text-to-map-nlp"

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, to_exit_code,
    )
    from _geoskill_core.manifest import OutputManifest, OutputFile
except ImportError:  # pragma: no cover
    class GeoSkillError(Exception):
        def __init__(self, message: str, code: int = 7, kind: str = "EGeo", **kw):
            super().__init__(message)
            self.message, self.code, self.kind = message, code, kind

    class UsageError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=2, kind="EUsage", **k)

    class ValidationError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=6, kind="EValidate", **k)

    class ProcessError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=7, kind="EProcess", **k)

    def to_exit_code(exc):
        return getattr(exc, "code", 7)

    OutputManifest = None
    OutputFile = None


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# bbox validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Optional[List[float]], *, kind: str = "bbox") -> List[float]:
    """校验 W<S<E<N、lat∈[-90,90]、lon∈[-180,180]，跨 180° 单独报错提示拆分。

    返回规范化后的 [W, S, E, N]。失败抛 ValidationError (rc=6)。
    """
    if bbox is None:
        raise ValidationError(f"{kind} is required")
    if len(bbox) != 4:
        raise ValidationError(f"{kind} must have 4 floats [W S E N], got {len(bbox)}",
                              bbox=list(bbox))
    w, s, e, n = (float(x) for x in bbox)
    if not (all(np.isfinite(v) for v in (w, s, e, n))):
        raise ValidationError(f"{kind} contains non-finite values", bbox=[w, s, e, n])
    if w == e or s == n:
        raise ValidationError(f"{kind} has zero area: W==E or S==N", bbox=[w, s, e, n])
    # 跨 180° 经线单独给提示（不支持环绕）
    if w > e:
        raise ValidationError(
            f"{kind} crosses the 180° meridian (W={w} > E={e}); "
            "please split into two sub-bboxes or shift longitudes",
            bbox=[w, s, e, n],
        )
    if s > n:
        raise ValidationError(f"{kind} has S > N (S={s} > N={n})", bbox=[w, s, e, n])
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"{kind} latitude out of range [-90, 90]: S={s}, N={n}",
            bbox=[w, s, e, n],
        )
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"{kind} longitude out of range [-180, 180]: W={w}, E={e}",
            bbox=[w, s, e, n],
        )
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# 核心算法：自然语言 -> 地图参数（关键词规则解析）
# ---------------------------------------------------------------------------
# 图层类型定义：关键词、默认配色、中文名称
LAYER_SPECS: Dict[str, Dict[str, Any]] = {
    "ndvi": {"cmap": "RdYlGn", "cn": "植被指数 NDVI",
             "keywords": ["ndvi", "植被", "vegetation", "绿化", "作物", "crop"]},
    "elevation": {"cmap": "terrain", "cn": "高程 Elevation",
                  "keywords": ["高程", "地形", "dem", "elevation", "海拔", "山"]},
    "nightlights": {"cmap": "magma", "cn": "夜间灯光 Night Lights",
                    "keywords": ["夜间灯光", "灯光", "nightlight", "night light", "夜光", "照明"]},
    "water": {"cmap": "Blues", "cn": "水体 Water",
              "keywords": ["水体", "水", "water", "湖泊", "湖", "河流", "河"]},
    "temperature": {"cmap": "inferno", "cn": "地表温度 LST",
                    "keywords": ["温度", "temperature", "热", "heat", "lst", "高温"]},
    "landcover": {"cmap": "tab20", "cn": "土地利用 Land Cover",
                  "keywords": ["土地利用", "地物", "landcover", "land cover", "土地覆盖", "分类"]},
}

PLACE_KEYWORDS: Dict[str, str] = {
    "北京": "北京", "beijing": "北京",
    "上海": "上海", "shanghai": "上海",
    "广州": "广州", "guangzhou": "广州",
    "深圳": "深圳", "shenzhen": "深圳",
    "成都": "成都", "chengdu": "成都",
}


def detect_layer(text: str) -> str:
    """从文本中按关键词匹配图层类型，未命中返回默认 'ndvi'。"""
    low = text.lower()
    best_layer = "ndvi"
    best_hits = 0
    for layer, spec in LAYER_SPECS.items():
        hits = sum(1 for kw in spec["keywords"] if kw.lower() in low)
        if hits > best_hits:
            best_hits = hits
            best_layer = layer
    return best_layer


def detect_place(text: str) -> Optional[str]:
    """从文本中识别地名（小词典），未命中返回 None。"""
    low = text.lower()
    for kw, name in PLACE_KEYWORDS.items():
        if kw in low:
            return name
    return None


def parse_query(text: str, layer_override: str = "auto") -> Dict[str, Any]:
    """解析自然语言查询 -> 地图参数字典。

    返回 {layer, cmap, layer_cn, place, title, query}。
    layer_override != 'auto' 时强制使用该图层类型。
    """
    if not text or not text.strip():
        raise UsageError("query text is empty")
    layer = detect_layer(text) if layer_override == "auto" else layer_override
    if layer not in LAYER_SPECS:
        raise UsageError(
            f"unknown layer '{layer}'. Choose from: {sorted(LAYER_SPECS)}",
            layer=layer,
        )
    spec = LAYER_SPECS[layer]
    place = detect_place(text)
    title = f"{place + ' ' if place else ''}{spec['cn']}"
    return {
        "layer": layer,
        "cmap": spec["cmap"],
        "layer_cn": spec["cn"],
        "place": place,
        "title": title.strip(),
        "query": text,
    }


# ---------------------------------------------------------------------------
# 图层合成（离线，物理一致）
# ---------------------------------------------------------------------------
def synthetic_layer(layer: str, width: int = 128, height: int = 128,
                    seed: int = 42) -> np.ndarray:
    """按图层类型生成模拟栅格。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    u = xx.astype(np.float64) / max(width - 1, 1)
    v = yy.astype(np.float64) / max(height - 1, 1)

    if layer == "ndvi":
        arr = 0.3 + 0.4 * np.sin(np.pi * u) * np.cos(np.pi * v)
        arr += rng.normal(0, 0.03, arr.shape)
        return np.clip(arr, 0.0, 1.0).astype(np.float32)
    if layer == "elevation":
        arr = 1500 + 1200 * np.sin(2 * np.pi * u) * np.sin(2 * np.pi * v)
        arr += rng.normal(0, 50, arr.shape)
        return np.clip(arr, 0.0, 4000.0).astype(np.float32)
    if layer == "nightlights":
        arr = rng.exponential(0.05, (height, width))
        # 若干城市亮核
        for _ in range(5):
            cy, cx = rng.integers(0, height), rng.integers(0, width)
            d2 = (yy - cy) ** 2 + (xx - cx) ** 2
            arr += 5.0 * np.exp(-d2 / (2 * 8.0 ** 2))
        return arr.astype(np.float32)
    if layer == "water":
        field = np.sin(3 * np.pi * u) + np.cos(3 * np.pi * v)
        prob = 1.0 / (1.0 + np.exp(-2 * field))
        return prob.astype(np.float32)
    if layer == "temperature":
        arr = 15 + 20 * v + 5 * np.sin(4 * np.pi * u)
        arr += rng.normal(0, 1.0, arr.shape)
        return np.clip(arr, -10.0, 50.0).astype(np.float32)
    if layer == "landcover":
        # 最近邻随机种子 -> 类别斑块（0..4）
        n_cls = 5
        seeds_y = rng.integers(0, height, n_cls)
        seeds_x = rng.integers(0, width, n_cls)
        labels = np.zeros((height, width), dtype=np.float32)
        best = np.full((height, width), np.inf)
        for c in range(n_cls):
            d2 = (yy - seeds_y[c]) ** 2 + (xx - seeds_x[c]) ** 2
            mask = d2 < best
            labels[mask] = c
            best[mask] = d2[mask]
        return labels
    raise UsageError(f"unknown layer '{layer}'. Choose from: {sorted(LAYER_SPECS)}", layer=layer)


# ---------------------------------------------------------------------------
# 地图渲染（matplotlib，Agg 离线后端）
# ---------------------------------------------------------------------------
def render_map(array: np.ndarray, bbox: List[float], cmap: str, title: str,
               out_path: str, dpi: int = 100) -> str:
    """把栅格按 bbox 地理范围渲染成带色条/标题的 PNG。"""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    arr = np.asarray(array)
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(arr, cmap=cmap,
                   extent=[bbox[0], bbox[2], bbox[1], bbox[3]],
                   origin="upper", aspect="auto")
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    ax.set_title(title)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    fig.savefig(out_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    return out_path


def bbox_to_geojson(bbox: List[float], properties: Dict[str, Any]) -> Dict[str, Any]:
    """生成 bbox 边界多边形 GeoJSON FeatureCollection。"""
    w, s, e, n = bbox
    ring = [[w, s], [e, s], [e, n], [w, n], [w, s]]
    return {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "properties": properties,
            "geometry": {"type": "Polygon", "coordinates": [ring]},
        }],
    }


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    arr = np.asarray(array, dtype=np.float32)
    if arr.ndim == 2:
        arr = arr[np.newaxis, ...]
    nb, h, w = arr.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(arr[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """读 GeoTIFF；NoData 像素替换为 NaN 后返回 (cube, bbox)。

    同步通过模块级函数 _LAST_READ_META 暴露元数据，供 process() 在调用后读取。
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [float(b.left), float(b.bottom), float(b.right), float(b.top)]
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    n_valid = int(np.count_nonzero(np.isfinite(cube)))
    n_total = int(cube.size)
    globals()["_LAST_READ_META"] = {
        "nodata": nodata, "n_valid_pixels": n_valid, "n_total_pixels": n_total,
    }
    return cube, bbox


def get_last_read_meta() -> Dict[str, Any]:
    return globals().get("_LAST_READ_META", {"nodata": None,
                                              "n_valid_pixels": 0,
                                              "n_total_pixels": 0})


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "query": getattr(args, "query", None),
            "layer": getattr(args, "layer", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
        },
        outputs=[OutputFile(**o) for o in outputs],
        qa=qa,
        software={"python": sys.version.split()[0], "skill": SKILL_NAME},
    )
    path = os.path.join(output_dir, "output-manifest.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(man.to_dict(), f, ensure_ascii=False, indent=2, default=str)
    return path


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir
    bbox = list(args.bbox) if args.bbox else None
    query_text = args.query or "遥感专题地图"
    params = parse_query(query_text, layer_override=args.layer)

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        in_meta = get_last_read_meta()
        # 用户给了 --bbox 就用它（并校验）；否则用文件自带 bbox
        if bbox is not None:
            bbox = validate_bbox(bbox, kind="--bbox")
        else:
            bbox = validate_bbox(file_bbox, kind="--input file bbox")
        if in_meta["n_valid_pixels"] == 0:
            raise ValidationError(
                f"input raster has no valid pixels (all NoData={in_meta['nodata']})",
                path=args.input, n_total_pixels=in_meta["n_total_pixels"],
            )
        layer_data = cube[0] if cube.ndim == 3 else cube
        source_note = args.input
    else:
        # synthetic 模式必须给 --bbox；缺失是用户错误而非数据错误 → UsageError
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox, kind="--bbox")
        layer_data = synthetic_layer(params["layer"])
        source_note = "synthetic"

    if layer_data.size == 0:
        raise ValidationError("layer raster is empty")

    # 校验通过后再建目录（失败时不留空目录）
    os.makedirs(output_dir, exist_ok=True)

    png_path = os.path.join(output_dir, "map.png")
    render_map(layer_data, bbox, params["cmap"], params["title"], png_path)

    tif_path = os.path.join(output_dir, "layer.tif")
    write_geotiff(tif_path, layer_data.astype(np.float32), bbox)

    geo_path = os.path.join(output_dir, "footprint.geojson")
    footprint = bbox_to_geojson(bbox, {"layer": params["layer"], "title": params["title"]})
    with open(geo_path, "w", encoding="utf-8") as f:
        json.dump(footprint, f, ensure_ascii=False, indent=2)

    params_path = os.path.join(output_dir, "parsed_query.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "layer": params["layer"],
        "cmap": params["cmap"],
        "place": params["place"],
        "title": params["title"],
        "raster_min": float(np.nanmin(layer_data)),
        "raster_max": float(np.nanmax(layer_data)),
        "n_valid_pixels": int(np.count_nonzero(np.isfinite(layer_data))),
        "n_total_pixels": int(layer_data.size),
    }
    if args.input and not args.synthetic:
        qa["input_nodata"] = in_meta["nodata"]
        qa["input_n_valid_pixels"] = in_meta["n_valid_pixels"]
        qa["input_n_total_pixels"] = in_meta["n_total_pixels"]
    outputs = [
        {"path": png_path, "kind": "image"},
        {"path": tif_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": geo_path, "kind": "vector", "crs_epsg": 4326, "bbox_wgs84": bbox},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] query: {query_text}")
        print(f"[{SKILL_NAME}] parsed: layer={params['layer']}  place={params['place']}  cmap={params['cmap']}")
        print(f"[{SKILL_NAME}] title: {params['title']}")
        print(f"[{SKILL_NAME}] map: {png_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Natural-language to map (keyword parsing + matplotlib rendering, offline equivalent).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF used directly as the map layer")
    p.add_argument("--query", default="", help="natural-language description of the desired map")
    p.add_argument("--layer", default="auto",
                   choices=["auto"] + sorted(LAYER_SPECS.keys()),
                   help="force a layer type (default: auto-detect from query)")
    p.add_argument("--synthetic", action="store_true", help="generate a synthetic layer (offline)")
    p.add_argument("--output-dir", default="./output", help="output directory")
    p.add_argument("--quiet", action="store_true", help="suppress console output")
    p.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return process(args)
    except GeoSkillError as exc:
        print(f"[{SKILL_NAME}] ERROR [{exc.kind}] {exc.message}", file=sys.stderr)
        return exc.code
    except KeyboardInterrupt:
        return 130
    except Exception as exc:  # noqa: BLE001
        print(f"[{SKILL_NAME}] ERROR {exc}", file=sys.stderr)
        return to_exit_code(exc)


if __name__ == "__main__":
    sys.exit(main())
