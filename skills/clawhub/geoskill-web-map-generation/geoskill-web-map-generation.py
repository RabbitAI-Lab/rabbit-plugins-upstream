#!/usr/bin/env python3
"""web-map-generation — 交互式Web地图生成

把 GeoTIFF 栅格（或合成栅格）渲染成带地理配准的 PNG 瓦片，并嵌入一个
自包含的 Leaflet 交互式 HTML 地图。支持百分位拉伸 / min-max 拉伸与
多种 matplotlib 配色方案。

数据源：本地 GeoTIFF（单波段或多波段），或 ``--synthetic`` 生成物理一致的
模拟 DEM 用于离线测试。

隐私声明 / Privacy：
- 默认离线生成 HTML；Leaflet 底图瓦片仅在浏览器打开时按需加载（可断网查看叠加层）。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python web-map-generation.py --input dem.tif --cmap terrain --output-dir ./out
    python web-map-generation.py --bbox 116 39 117 40 --synthetic --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import base64
import datetime as _dt
import io
import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "web-map-generation"

# ---- 复用共享核心库（本地 vendored，随脚本目录一起分发）----
try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, to_exit_code,
    )
    from _geoskill_core.manifest import OutputManifest, OutputFile
except ImportError:  # pragma: no cover - fallback minimal definitions
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


CMAPS = ["viridis", "terrain", "gray", "magma", "inferno", "plasma", "turbo", "jet"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def percentile_stretch(
    band: np.ndarray, lo_pct: float = 2.0, hi_pct: float = 98.0
) -> Tuple[np.ndarray, float, float]:
    """百分位线性拉伸到 [0, 1]。

    用有效像元的低/高分位数作为拉伸端点，避免极值拉低对比度。
    返回 (stretched_01, lo_val, hi_val)。常数栅格返回全 0。
    """
    valid = band[np.isfinite(band)]
    if valid.size == 0:
        return np.zeros_like(band, dtype=np.float32), 0.0, 0.0
    lo = float(np.percentile(valid, lo_pct))
    hi = float(np.percentile(valid, hi_pct))
    if hi <= lo:
        return np.zeros_like(band, dtype=np.float32), lo, hi
    out = (band.astype(np.float32) - lo) / (hi - lo)
    out = np.clip(np.nan_to_num(out, nan=0.0), 0.0, 1.0)
    return out, lo, hi


def minmax_stretch(band: np.ndarray) -> Tuple[np.ndarray, float, float]:
    """min-max 线性拉伸到 [0, 1]。"""
    valid = band[np.isfinite(band)]
    if valid.size == 0:
        return np.zeros_like(band, dtype=np.float32), 0.0, 0.0
    lo = float(np.nanmin(valid))
    hi = float(np.nanmax(valid))
    if hi <= lo:
        return np.zeros_like(band, dtype=np.float32), lo, hi
    out = (band.astype(np.float32) - lo) / (hi - lo)
    out = np.clip(np.nan_to_num(out, nan=0.0), 0.0, 1.0)
    return out, lo, hi


def apply_colormap(gray01: np.ndarray, cmap_name: str) -> np.ndarray:
    """把 [0,1] 灰度映射为 (H, W, 3) uint8 RGB。"""
    import matplotlib
    if cmap_name not in CMAPS:
        raise UsageError(f"unknown cmap '{cmap_name}'. Choose from: {CMAPS}", cmap=cmap_name)
    cmap = matplotlib.colormaps[cmap_name]
    rgba = cmap(np.clip(gray01, 0.0, 1.0))  # (H,W,4) float
    rgb = rgba[..., :3]
    return (rgb * 255.0).round().astype(np.uint8)


def encode_png_bytes(rgb_u8: np.ndarray) -> bytes:
    """把 (H, W, 3) uint8 编码为 PNG 字节流。"""
    from PIL import Image
    if rgb_u8.ndim != 3 or rgb_u8.shape[2] != 3:
        raise ValidationError("encode_png_bytes expects (H, W, 3) uint8 array")
    img = Image.fromarray(rgb_u8, "RGB")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def leaflet_bounds(bbox: List[float]) -> str:
    """把 [W,S,E,N] 转成 Leaflet ImageOverlay 的 [[S,W],[N,E]] JS 字面量。"""
    w, s, e, n = bbox
    return f"[[{s}, {w}], [{n}, {e}]]"


def build_leaflet_html(
    bbox: List[float],
    image_b64: str,
    title: str,
    opacity: float,
    cmap_name: str,
    meta: Dict[str, Any],
) -> str:
    """生成自包含的 Leaflet HTML 字符串（叠加层用 data URI 内嵌）。"""
    bounds = leaflet_bounds(bbox)
    w, s, e, n = bbox
    cx, cy = (w + e) / 2.0, (s + n) / 2.0
    op = float(np.clip(opacity, 0.0, 1.0))
    meta_json = json.dumps(meta, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>html,body,#map{{height:100%;margin:0}}#info{{position:absolute;top:8px;right:8px;
background:rgba(255,255,255,.9);padding:8px 12px;font:12px/1.5 sans-serif;
border-radius:6px;max-width:280px;z-index:1000}}</style>
</head>
<body>
<div id="map"></div>
<div id="info"><b>{title}</b><br/>colormap: {cmap_name}<br/>opacity: {op:.2f}</div>
<script>
var map = L.map('map').setView([{cy}, {cx}], 9);
L.tileLayer('https://tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png',
  {{maxZoom: 19, attribution: '&copy; OpenStreetMap'}}).addTo(map);
var overlay = L.imageOverlay('data:image/png;base64,{image_b64}', {bounds},
  {{opacity: {op}, interactive: true}}).addTo(map);
map.fitBounds({bounds});
var META = {meta_json};
overlay.on('click', function(e){{
  L.popup().setLatLng(e.latlng)
    .setContent('lon: '+e.latlng.lng.toFixed(4)+'<br/>lat: '+e.latlng.lat.toFixed(4))
    .openOn(map);
}});
</script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# 合成数据：物理一致的模拟 DEM（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float], width: int = 128, height: int = 128, seed: int = 42
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成一个单波段 DEM（米），含一个高斯山丘 + 一条河谷 + 噪声。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy = yy / max(height - 1, 1)
    xx = xx / max(width - 1, 1)
    # 主山丘
    peak = 1200.0 * np.exp(-(((xx - 0.65) ** 2 + (yy - 0.6) ** 2) / 0.02))
    # 河谷（沿对角线下切）
    valley = -250.0 * np.exp(-(((xx - yy) ** 2) / 0.004))
    base = 200.0 + 150.0 * xx
    noise = rng.normal(0, 8.0, size=(height, width)).astype(np.float32)
    dem = (base + peak + valley + noise).astype(np.float32)
    info = {
        "bbox": bbox, "width": width, "height": height,
        "min_elev": float(dem.min()), "max_elev": float(dem.max()),
        "mean_elev": float(dem.mean()), "kind": "synthetic-dem",
    }
    return dem, info


# ---------------------------------------------------------------------------
# 参数校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Optional[List[float]]) -> List[float]:
    """校验 [W, S, E, N]：W<E、S<N、范围合法；跨 180°给拆分提示。"""
    if bbox is None or len(bbox) != 4:
        raise UsageError(
            "bbox must be 4 floats [W S E N], got: " + repr(bbox),
            bbox=bbox,
        )
    w, s, e, n = bbox
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError(
            f"bbox must contain finite floats, got {bbox}", bbox=bbox)
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of [-180, 180]: W={w} E={e}", bbox=bbox)
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of [-90, 90]: S={s} N={n}", bbox=bbox)
    if s >= n:
        raise ValidationError(
            f"bbox South >= North: S={s} N={n}", bbox=bbox)
    if w > e:
        raise ValidationError(
            f"bbox crosses the 180° meridian (W={w} > E={e}); "
            f"please split the extent or wrap longitudes manually",
            bbox=bbox)
    if abs(e - w) < 1e-9 or abs(n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero area: W={w} E={e} S={s} N={n}", bbox=bbox)
    return [float(w), float(s), float(e), float(n)]


def validate_percentiles(lo: float, hi: float) -> Tuple[float, float]:
    """百分位 lo/hi ∈ [0, 100] 且 lo < hi。"""
    try:
        lo_v = float(lo)
        hi_v = float(hi)
    except (TypeError, ValueError):
        raise ValidationError(
            f"lo-pct/hi-pct must be numbers, got lo={lo!r} hi={hi!r}")
    if not (np.isfinite(lo_v) and np.isfinite(hi_v)):
        raise ValidationError(
            f"lo-pct/hi-pct must be finite, got lo={lo_v} hi={hi_v}")
    if not (0.0 <= lo_v <= 100.0 and 0.0 <= hi_v <= 100.0):
        raise ValidationError(
            f"lo-pct/hi-pct must be in [0, 100], got lo={lo_v} hi={hi_v}")
    if lo_v >= hi_v:
        raise ValidationError(
            f"lo-pct must be < hi-pct (got lo={lo_v} hi={hi_v}); "
            f"inverted percentiles yield empty/degenerate stretch",
            lo_pct=lo_v, hi_pct=hi_v)
    return lo_v, hi_v


def validate_opacity(op: float) -> float:
    """不透明度 ∈ [0, 1]。"""
    try:
        v = float(op)
    except (TypeError, ValueError):
        raise ValidationError(f"opacity must be number, got {op!r}")
    if not np.isfinite(v):
        raise ValidationError(f"opacity must be finite, got {v}")
    if not (0.0 <= v <= 1.0):
        raise ValidationError(
            f"opacity must be in [0, 1], got {v}", opacity=v)
    return v


def read_band_with_nodata(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """读单波段 GeoTIFF 并把 nodata 标记的像元替换为 NaN；同时返回原 nodata。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    return cube, bbox, nodata


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str, cube: np.ndarray, bbox: List[float], nodata: float = -9999.0
) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(
    output_dir: str, args: argparse.Namespace, outputs: List[Dict[str, Any]],
    qa: Dict[str, Any], started_at: str, exit_code: int, bbox: List[float],
) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "cmap": getattr(args, "cmap", None),
            "stretch": getattr(args, "stretch", None),
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

    # 前置校验
    lo_pct, hi_pct = validate_percentiles(args.lo_pct, args.hi_pct)
    opacity = validate_opacity(args.opacity)
    bbox_in = list(args.bbox) if args.bbox else None

    # 1) 获取数据：给了 --input 就读真实栅格；否则走合成模式。
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox, _nd = read_band_with_nodata(args.input)
        if bbox_in is not None:
            bbox = validate_bbox(bbox_in)
        else:
            bbox = validate_bbox(file_bbox)
        source_note = args.input
    else:
        bbox = validate_bbox(bbox_in)
        dem, synth_info = generate_synthetic(bbox)
        cube = dem[np.newaxis, ...]
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    band = cube[0]
    n_valid = int(np.isfinite(band).sum())
    n_total = int(band.size)
    if n_valid == 0:
        raise ValidationError(
            f"input raster has no valid pixels (all NoData/NaN), "
            f"n_total={n_total}", n_total=n_total)

    # 校验通过后再创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 2) 拉伸 + 配色
    if args.stretch == "minmax":
        gray01, lo, hi = minmax_stretch(band)
    else:
        gray01, lo, hi = percentile_stretch(band, lo_pct, hi_pct)
    rgb = apply_colormap(gray01, args.cmap)
    png_bytes = encode_png_bytes(rgb)
    image_b64 = base64.b64encode(png_bytes).decode("ascii")

    # 3) 写出产物
    meta = {
        "source": source_note,
        "cmap": args.cmap,
        "stretch": args.stretch,
        "stretch_lo": lo,
        "stretch_hi": hi,
        "bbox": bbox,
        "shape": [int(band.shape[0]), int(band.shape[1])],
        "value_min": float(np.nanmin(band)),
        "value_max": float(np.nanmax(band)),
        "value_mean": float(np.nanmean(band)),
        "generated_at": _utc_now(),
    }
    if synth_info is not None:
        meta["synthetic"] = synth_info

    html = build_leaflet_html(bbox, image_b64, args.title, opacity, args.cmap, meta)
    html_path = os.path.join(output_dir, "web_map.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    # 可验证产物：渲染后的 [0,1] 栅格 GeoTIFF
    out_tif = os.path.join(output_dir, "rendered.tif")
    write_geotiff(out_tif, gray01.astype(np.float32), bbox)

    meta_path = os.path.join(output_dir, "map_metadata.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    qa = {
        "source": source_note,
        "cmap": args.cmap,
        "stretch": args.stretch,
        "html_bytes": len(html),
        "png_bytes": len(png_bytes),
        "rendered_mean": float(np.mean(gray01)),
        "n_total_pixels": n_total,
        "n_valid_pixels": n_valid,
        "bbox": bbox,
    }
    outputs = [
        {"path": html_path, "kind": "text"},
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": meta_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] cmap: {args.cmap}  stretch: {args.stretch}  range: [{lo:.2f}, {hi:.2f}]")
        print(f"[{SKILL_NAME}] html:  {html_path}")
        print(f"[{SKILL_NAME}] raster: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Generate an interactive Leaflet web map from a raster.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF raster")
    p.add_argument("--cmap", default="terrain", choices=CMAPS,
                   help="matplotlib colormap (default: terrain)")
    p.add_argument("--stretch", default="percentile", choices=["percentile", "minmax"],
                   help="contrast stretch method (default: percentile)")
    p.add_argument("--lo-pct", type=float, default=2.0,
                   help="low percentile for percentile stretch (default: 2)")
    p.add_argument("--hi-pct", type=float, default=98.0,
                   help="high percentile for percentile stretch (default: 98)")
    p.add_argument("--opacity", type=float, default=0.8,
                   help="overlay opacity 0..1 (default: 0.8)")
    p.add_argument("--title", default="Web Map", help="map title")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic DEM (offline)")
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
