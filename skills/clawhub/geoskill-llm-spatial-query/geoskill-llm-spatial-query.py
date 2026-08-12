#!/usr/bin/env python3
"""llm-spatial-query — LLM 空间查询

用一句自然语言（如"筛选面积大于 50 且在范围内的地块，取值最高的前 3 个"）
对矢量图层做空间 + 属性查询，输出命中的要素 GeoJSON 与查询计划。

本 skill 是 LLM/NL2GeoSQL 空间问答系统的**离线 numpy 等价实现**：
不依赖大模型/网络，而用可验证的规则流程复现"自然语言 -> 结构化查询 -> 执行"——

1. **意图解析**：用正则规则从文本抽取属性过滤条件（字段 + 比较符 + 数值）、
   空间范围意图（"在范围内" -> bbox 相交过滤）与排序/Top-N（等价槽位填充）；
2. **查询计划**：把解析结果组织成结构化 query plan（字段/算子/值/空间/Top-N）；
3. **执行**：用 geopandas/shapely 执行属性过滤、bbox 空间相交与排序，输出结果。

数据源：本地矢量文件（GeoJSON/Shapefile，经 geopandas 读取），或 ``--synthetic``
生成规则地块网格图层用于离线演示。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python llm-spatial-query.py --input parcels.geojson --query "面积大于50" --output-dir ./out
    python llm-spatial-query.py --bbox 116 39 117 40 --synthetic --query "前3个" --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "llm-spatial-query"

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
# Validation helpers
# ---------------------------------------------------------------------------
def validate_bbox(bbox, allow_antimeridian: bool = False):
    """Validate geographic bbox. Returns bbox as list[float] on success.

    Cross-180° (W > E) is rejected with a hint unless ``allow_antimeridian``.
    """
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            f"bbox must be 4 floats [W S E N], got {bbox!r}")
    w, s, e, n = (float(x) for x in bbox)
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0
            and -90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox out of range (-180..180 lon, -90..90 lat): [{w}, {s}, {e}, {n}]")
    if w == e or s == n:
        raise ValidationError(
            f"bbox has zero area: W==E ({w}) or S==N ({s}); "
            f"got [{w}, {s}, {e}, {n}]")
    if s > n:
        raise ValidationError(
            f"bbox S>N (south > north): [{w}, {s}, {e}, {n}]")
    if w > e:
        if not allow_antimeridian:
            raise ValidationError(
                f"bbox crosses antimeridian (W>E: {w}>{e}); "
                f"split into two bboxes and merge results manually")
        return [w, s, e, n]
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# 核心算法：自然语言 -> 结构化查询计划
# ---------------------------------------------------------------------------
FIELD_ALIASES: Dict[str, str] = {
    "面积": "area_km2", "area": "area_km2",
    "值": "value", "value": "value", "数值": "value",
    "人口": "population", "population": "population",
}

# (关键词, 规范算子)；长词在前，避免 "大于" 被 ">" 误匹配
OP_KEYWORDS: List[Tuple[str, str]] = [
    ("大于等于", ">="), ("大于", ">"), ("超过", ">"), ("高于", ">"),
    ("＞=", ">="), ("＞", ">"), (">=", ">="), (">", ">"),
    ("小于等于", "<="), ("小于", "<"), ("低于", "<"),
    ("＜=", "<="), ("＜", "<"), ("<=", "<="), ("<", "<"),
    ("等于", "=="), ("=", "=="),
]

_FIELD_ALT = "|".join(re.escape(k) for k in sorted(FIELD_ALIASES, key=len, reverse=True))
_OP_ALT = "|".join(re.escape(op) for op, _ in OP_KEYWORDS)
_FILTER_RE = re.compile(rf"({_FIELD_ALT})\s*({_OP_ALT})\s*([0-9]+(?:\.[0-9]+)?)")
_TOPN_RE = re.compile(r"(?:前|top)\s*([0-9]+)", re.IGNORECASE)


def normalize_op(token: str) -> str:
    """把算子关键词归一化为规范算子。"""
    for kw, op in OP_KEYWORDS:
        if token == kw:
            return op
    return token


def parse_spatial_query(text: str) -> Dict[str, Any]:
    """解析自然语言查询 -> 查询计划。

    返回 {filters:[{field, op, value}], spatial:'all'|'bbox',
          top_n:int|None, sort_field:str|None}。
    """
    if not text or not text.strip():
        raise UsageError("query text is empty")
    low = text.lower()
    filters: List[Dict[str, Any]] = []
    for m in _FILTER_RE.finditer(text):
        field = FIELD_ALIASES[m.group(1)]
        op = normalize_op(m.group(2))
        value = float(m.group(3))
        filters.append({"field": field, "op": op, "value": value})

    spatial = "bbox" if ("范围内" in text or "区域内" in text or "在范围" in low) else "all"

    top_n = None
    mt = _TOPN_RE.search(text)
    if mt:
        top_n = int(mt.group(1))

    sort_field = "value" if (top_n is not None or "最高" in text or "最大" in text) else None

    return {
        "filters": filters,
        "spatial": spatial,
        "top_n": top_n,
        "sort_field": sort_field,
    }


# ---------------------------------------------------------------------------
# 查询执行（geopandas / shapely）
# ---------------------------------------------------------------------------
def apply_attribute_filter(gdf, field: str, op: str, value: float):
    """对 GeoDataFrame 应用单个属性过滤；字段不存在时原样返回。"""
    if field not in gdf.columns:
        return gdf
    col = gdf[field]
    if op == ">":
        return gdf[col > value]
    if op == ">=":
        return gdf[col >= value]
    if op == "<":
        return gdf[col < value]
    if op == "<=":
        return gdf[col <= value]
    if op == "==":
        return gdf[col == value]
    raise UsageError(f"unsupported operator '{op}'", op=op)


def query_by_bbox(gdf, bbox: List[float]):
    """保留与 bbox 相交的要素。"""
    from shapely.geometry import box
    if gdf.crs is None:
        raise ValidationError("input layer has no CRS; cannot do bbox query")
    bbox_poly = box(bbox[0], bbox[1], bbox[2], bbox[3])
    mask = gdf.geometry.intersects(bbox_poly)
    return gdf[mask]


def run_spatial_query(gdf, plan: Dict[str, Any], bbox: Optional[List[float]] = None):
    """按查询计划执行：空间过滤 -> 属性过滤 -> 排序/Top-N。"""
    result = gdf
    if plan.get("spatial") == "bbox":
        if bbox is None:
            raise UsageError("query asks for bbox filter but no --bbox provided")
        result = query_by_bbox(result, bbox)
    for flt in plan.get("filters", []):
        result = apply_attribute_filter(result, flt["field"], flt["op"], flt["value"])
    sort_field = plan.get("sort_field")
    if sort_field and sort_field in result.columns:
        result = result.sort_values(sort_field, ascending=False)
    top_n = plan.get("top_n")
    if top_n is not None:
        result = result.head(top_n)
    return result


def results_to_geojson(gdf) -> Dict[str, Any]:
    """GeoDataFrame -> GeoJSON FeatureCollection dict。"""
    return json.loads(gdf.to_json())


# ---------------------------------------------------------------------------
# 合成矢量图层：规则地块网格 + 属性
# ---------------------------------------------------------------------------
def build_synthetic_dataset(bbox: List[float], n: int = 9, seed: int = 42):
    """生成 n 个网格地块多边形（带 area_km2/value/population/category 属性）。"""
    import geopandas as gpd
    from shapely.geometry import box
    rng = np.random.default_rng(seed)
    w, s, e, n_bound = bbox
    cols = int(np.ceil(np.sqrt(n)))
    rows = int(np.ceil(n / cols))
    dw = (e - w) / cols
    dh = (n_bound - s) / rows
    categories = ["农田", "建设用地", "水体", "林地"]
    feats = []
    idx = 0
    for r in range(rows):
        for c in range(cols):
            if idx >= n:
                break
            x0 = w + c * dw
            y0 = s + r * dh
            poly = box(x0, y0, x0 + dw, y0 + dh)
            area_km2 = float(poly.area) * (111.0 ** 2)  # 度² -> 近似 km²
            feats.append({
                "id": int(idx),
                "name": f"地块{idx}",
                "area_km2": round(area_km2, 3),
                "value": round(float(rng.uniform(0, 100)), 2),
                "population": int(rng.integers(0, 5000)),
                "category": categories[int(idx) % len(categories)],
                "geometry": poly,
            })
            idx += 1
    gdf = gpd.GeoDataFrame(feats, crs="EPSG:4326")
    return gdf


# ---------------------------------------------------------------------------
# GeoTIFF I/O（保留以满足契约；本 skill 主用矢量 I/O）
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
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_vector(path: str):
    import geopandas as gpd
    if not os.path.exists(path):
        raise UsageError(f"input vector not found: {path}", path=path)
    return gpd.read_file(path)


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
    query_text = args.query or "全部要素"

    # ---- Validate bbox and params early ----
    if bbox is not None:
        bbox = validate_bbox(bbox)
    if not args.synthetic:
        if args.n_features is not None and args.n_features != 9:
            # Only meaningful in synthetic mode; warn but don't reject for now.
            pass
    else:
        if args.n_features is None or args.n_features < 1:
            raise ValidationError(
                f"--n-features must be >= 1 in synthetic mode (got {args.n_features})")
        if args.seed is None or args.seed < 0:
            raise ValidationError(
                f"--seed must be a non-negative integer (got {args.seed})")
    # Plan parsing: validate empty query up front so it errors before --input check
    plan = parse_spatial_query(query_text)

    if args.input and not args.synthetic:
        gdf = read_vector(args.input)
        if bbox is None and gdf.crs is not None:
            tb = gdf.total_bounds
            bbox = [float(tb[0]), float(tb[1]), float(tb[2]), float(tb[3])]
        elif bbox is None and gdf.crs is None:
            raise ValidationError(
                "input layer has no CRS and no --bbox provided; cannot determine spatial extent")
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <vector>")
        gdf = build_synthetic_dataset(bbox, n=args.n_features, seed=args.seed)
        source_note = "synthetic"

    if len(gdf) == 0:
        # Don't create output_dir if input is empty
        raise ValidationError("input layer has no features")

    # ---- Now safe to create output directory ----
    os.makedirs(output_dir, exist_ok=True)

    result = run_spatial_query(gdf, plan, bbox=bbox)
    geojson = results_to_geojson(result)

    res_path = os.path.join(output_dir, "query_result.geojson")
    with open(res_path, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    plan_path = os.path.join(output_dir, "query_plan.json")
    with open(plan_path, "w", encoding="utf-8") as f:
        json.dump({"query": query_text, "plan": plan}, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_input_features": int(len(gdf)),
        "n_matched": int(len(result)),
        "n_filters": len(plan["filters"]),
        "spatial": plan["spatial"],
        "top_n": plan["top_n"],
    }
    outputs = [
        {"path": res_path, "kind": "vector", "crs_epsg": 4326, "bbox_wgs84": bbox},
        {"path": plan_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] query: {query_text}")
        print(f"[{SKILL_NAME}] plan: {plan}")
        print(f"[{SKILL_NAME}] matched {len(result)}/{len(gdf)} features")
        print(f"[{SKILL_NAME}] result: {res_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="LLM-style spatial query (NL rule parsing + geopandas, offline equivalent).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input vector file (GeoJSON/Shapefile)")
    p.add_argument("--query", default="", help="natural-language query")
    p.add_argument("--n-features", type=int, default=9, help="number of synthetic parcels")
    p.add_argument("--seed", type=int, default=42, help="seed for synthetic dataset")
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
