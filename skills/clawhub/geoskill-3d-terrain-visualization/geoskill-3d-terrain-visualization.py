#!/usr/bin/env python3
"""3d-terrain-visualization — 三维地形可视化

把 DEM（可叠加影像色彩）渲染成带光照的三维地形效果图，并生成一个自包含的
HTML 查看器（CSS 3D 透视 + 可拖动旋转 / 垂直夸张滑块）。光照用 Lambertian
漫反射模型：逐像元由 DEM 梯度求法向量，再与太阳方向做点积。

单位口径（重要）：DEM 梯度按 **米制水平距离** 计算。EPSG:4326（度）输入
的水平像元尺寸会自动换算为米（≈111320·cos(φ) m/度），与 GDAL gdaldem
hillshade 对度单位 DEM 的 scale/zfactor 约定一致；投影坐标输入会先重投影
到 EPSG:4326。NoData 像元不参与梯度/统计，输出中以 nodata 标记。

数据源：本地 DEM GeoTIFF（可选 --input-rgb 叠加影像），或 ``--synthetic``
生成模拟 DEM。

隐私声明 / Privacy：
- 默认离线生成；HTML 仅在浏览器端本地渲染。
- ``--synthetic`` 模式完全无网络。所有处理本地完成，不上传数据。

Usage:
    python 3d-terrain-visualization.py --input dem.tif --exaggeration 2.5
    python 3d-terrain-visualization.py --bbox 116 39 117 40 --synthetic

License: MIT
"""
from __future__ import annotations

import argparse
import base64
import datetime as _dt
import io
import json
import math
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "3d-terrain-visualization"

# 赤道处 1 度的米制长度（与 ESRI z-factor 约定 1/0.00000898 ≈ 111320 一致；
# Snyder 1987 PP1395 给出椭球精确公式，此处球面近似误差 <1%）
M_PER_DEG_EQUATOR = 111320.0
SHADE_NODATA = -9999.0

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, DependencyError, ValidationError, ProcessError,
        to_exit_code,
    )
    from _geoskill_core.manifest import OutputManifest, OutputFile
except ImportError:  # pragma: no cover
    class GeoSkillError(Exception):
        def __init__(self, message: str, code: int = 7, kind: str = "EGeo", **kw):
            super().__init__(message)
            self.message, self.code, self.kind = message, code, kind

    class UsageError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=2, kind="EUsage", **k)

    class DependencyError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=3, kind="EDepend", **k)

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
# 校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> List[float]:
    """校验 bbox：有限、在值域内、W<=E（不支持跨 180°）、S<=N、非退化。"""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must have 4 values: W S E N")
    try:
        w, s, e, n = (float(v) for v in bbox)
    except (TypeError, ValueError):
        raise ValidationError(f"bbox values must be numeric, got {bbox!r}")
    for v, name in ((w, "W"), (s, "S"), (e, "E"), (n, "N")):
        if not math.isfinite(v):
            raise ValidationError(f"bbox {name} is not finite: {v}")
    if not (-180.0 <= w <= 180.0) or not (-180.0 <= e <= 180.0):
        raise ValidationError(f"longitude out of range [-180, 180]: W={w}, E={e}")
    if not (-90.0 <= s <= 90.0) or not (-90.0 <= n <= 90.0):
        raise ValidationError(f"latitude out of range [-90, 90]: S={s}, N={n}")
    if w > e:
        raise ValidationError(
            f"bbox crosses the antimeridian (W={w} > E={e}); "
            "this skill does not wrap around 180° — split the request into two bboxes")
    if s > n:
        raise ValidationError(f"bbox has S > N (S={s}, N={n})")
    if w == e or s == n:
        raise ValidationError(f"bbox is degenerate (zero width or height): {bbox}")
    return [w, s, e, n]


def validate_params(args: argparse.Namespace) -> None:
    """输入参数值域校验（越界 → ValidationError → exit 6）。"""
    exag, az, alt, amb = args.exaggeration, args.azimuth, args.altitude, args.ambient
    for v, name in ((exag, "exaggeration"), (az, "azimuth"), (alt, "altitude"), (amb, "ambient")):
        if not math.isfinite(float(v)):
            raise ValidationError(f"--{name} must be finite, got {v}")
    if exag <= 0:
        raise ValidationError(f"--exaggeration must be > 0, got {exag}")
    if not (0.0 <= az < 360.0):
        raise ValidationError(f"--azimuth must be in [0, 360), got {az}")
    if not (0.0 <= alt <= 90.0):
        raise ValidationError(f"--altitude must be in [0, 90] degrees, got {alt}")
    if not (0.0 <= amb <= 1.0):
        raise ValidationError(f"--ambient must be in [0, 1], got {amb}")
    if args.cellsize is not None:
        if not math.isfinite(args.cellsize) or args.cellsize <= 0:
            raise ValidationError(f"--cellsize must be > 0 (metres), got {args.cellsize}")


def cellsize_meters(bbox: List[float], height: int, width: int) -> float:
    """由 WGS84 bbox 与栅格尺寸估算水平像元尺寸（米），取 x/y 均值。"""
    w, s, e, n = bbox
    lat_c = 0.5 * (s + n)
    m_per_deg = M_PER_DEG_EQUATOR * math.cos(math.radians(lat_c))
    dx = (e - w) / max(width, 1) * m_per_deg
    dy = (n - s) / max(height, 1) * m_per_deg
    return 0.5 * (dx + dy)


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def dem_normals(
    dem: np.ndarray, cellsize: float = 1.0, zfactor: float = 1.0
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """由 DEM 中心差分梯度求逐像元单位法向量 (nx, ny, nz)。

    坐标约定：x 沿列（东），y 沿行，z 向上。
    平面 z = a*x + b*y 的法向量为 (-a, -b, 1)/‖·‖（可用解析解校验）。
    zfactor 用于垂直夸张（放大高程相对水平距离的影响）。
    cellsize 与 z 必须同为米制（见 process() 的单位换算）。
    """
    z = dem.astype(np.float32) * zfactor
    gy, gx = np.gradient(z, cellsize, cellsize, edge_order=2)
    nx = -gx
    ny = -gy
    nz = np.ones_like(z)
    norm = np.sqrt(nx * nx + ny * ny + nz * nz)
    norm = np.where(norm < 1e-12, 1.0, norm)
    return (nx / norm, ny / norm, nz / norm)


def light_vector(azimuth_deg: float, altitude_deg: float) -> Tuple[float, float, float]:
    """太阳方向单位向量（从地表指向太阳）。

    azimuth：方位角，北=0°、东=90°（在 x=东、y=北坐标系），与 ESRI Hillshade
    及 GDAL gdaldem hillshade 的 azimuth 约定一致。
    altitude：高度角，地平=0°、天顶=90°。
    """
    az = np.deg2rad(azimuth_deg)
    alt = np.deg2rad(altitude_deg)
    lx = float(np.cos(alt) * np.sin(az))   # east
    ly = float(np.cos(alt) * np.cos(az))   # north
    lz = float(np.sin(alt))                # up
    return lx, ly, lz


def lambertian_shade(
    nx: np.ndarray, ny: np.ndarray, nz: np.ndarray,
    lx: float, ly: float, lz: float,
) -> np.ndarray:
    """Lambertian 漫反射：shade = max(N·L, 0)，返回 [0, 1]。"""
    dot = nx * lx + ny * ly + nz * lz
    return np.clip(dot, 0.0, 1.0).astype(np.float32)


def shade_color_overlay(rgb01: np.ndarray, shade: np.ndarray, ambient: float = 0.15) -> np.ndarray:
    """把光照叠加到 [0,1] RGB 上：out = rgb * (ambient + (1-ambient)*shade)。"""
    factor = (ambient + (1.0 - ambient) * shade)[..., np.newaxis]
    out = rgb01 * factor
    return np.clip(out, 0.0, 1.0)


def encode_png_bytes(rgb_u8: np.ndarray) -> bytes:
    try:
        from PIL import Image
    except ImportError as exc:
        raise DependencyError(f"pillow is required for PNG encoding: {exc}")
    img = Image.fromarray(rgb_u8, "RGB")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def terrain_rgb(dem01: np.ndarray) -> np.ndarray:
    """用 terrain colormap 把 [0,1] DEM 映射为 [0,1] RGB。"""
    try:
        import matplotlib
    except ImportError as exc:
        raise DependencyError(f"matplotlib is required for the terrain colormap: {exc}")
    cmap = matplotlib.colormaps["terrain"]
    return cmap(np.clip(dem01, 0.0, 1.0))[..., :3].astype(np.float32)


def build_viewer_html(image_b64: str, meta: Dict[str, Any]) -> str:
    """生成 CSS 3D 透视查看器 HTML。"""
    meta_json = json.dumps(meta, ensure_ascii=False)
    title = meta.get("title", "3D Terrain")
    exag = meta.get("exaggeration", 1.0)
    return f"""<!DOCTYPE html>
<html lang="zh"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<style>
html,body{{height:100%;margin:0;background:#0b1020;color:#eee;font-family:sans-serif;overflow:hidden}}
#stage{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;perspective:1200px}}
#tile{{width:70vmin;height:70vmin;background-size:cover;background-position:center;
transform-style:preserve-3d;box-shadow:0 40px 80px rgba(0,0,0,.6);
transform:rotateX(55deg) rotateZ(0deg) scale(1)}}
#ui{{position:absolute;top:10px;left:10px;background:rgba(0,0,0,.5);padding:10px 14px;border-radius:8px}}
label{{display:block;margin:6px 0 2px;font-size:12px}}
</style></head>
<body>
<div id="stage"><div id="tile"></div></div>
<div id="ui"><b>{title}</b>
<label>垂直夸张 exaggeration <span id="ev">{exag:.1f}</span></label>
<input id="exag" type="range" min="0.5" max="6" step="0.1" value="{exag}"/>
<label>俯仰 tilt <span id="tv">55</span>°</label>
<input id="tilt" type="range" min="0" max="85" step="1" value="55"/>
<label>旋转 rotate <span id="rv">0</span>°</label>
<input id="rot" type="range" min="0" max="360" step="1" value="0"/>
</div>
<script>
var META = {meta_json};
var tile = document.getElementById('tile');
tile.style.backgroundImage = 'data:image/png;base64,{image_b64}';
var exag = document.getElementById('exag'), tilt = document.getElementById('tilt'), rot = document.getElementById('rot');
function apply(){{
  var e = parseFloat(exag.value), t = parseFloat(tilt.value), r = parseFloat(rot.value);
  document.getElementById('ev').textContent = e.toFixed(1);
  document.getElementById('tv').textContent = t.toFixed(0);
  document.getElementById('rv').textContent = r.toFixed(0);
  tile.style.transform = 'rotateX('+t+'deg) rotateZ('+r+'deg) scaleZ('+e+')';
}}
exag.oninput = apply; tilt.oninput = apply; rot.oninput = apply; apply();
</script></body></html>
"""


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float], width: int = 128, height: int = 128, seed: int = 42
) -> Tuple[np.ndarray, Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy /= max(height - 1, 1); xx /= max(width - 1, 1)
    ridge = 800.0 * np.exp(-(((xx - 0.5) ** 2) / 0.01)) * (0.5 + 0.5 * np.sin(6.0 * yy))
    peak = 1500.0 * np.exp(-(((xx - 0.3) ** 2 + (yy - 0.7) ** 2) / 0.015))
    base = 100.0 + 80.0 * yy
    noise = rng.normal(0, 5.0, size=(height, width)).astype(np.float32)
    dem = (base + ridge + peak + noise).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "min_elev": float(dem.min()), "max_elev": float(dem.max()),
            "kind": "synthetic-dem"}
    return dem, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def _import_rasterio():
    try:
        import rasterio
        return rasterio
    except ImportError as exc:
        raise DependencyError(f"rasterio is required for GeoTIFF I/O: {exc}")


def write_geotiff(path, cube, bbox, nodata=-9999.0):
    rasterio = _import_rasterio()
    from rasterio.transform import from_bounds
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {"driver": "GTiff", "height": h, "width": w, "count": nb,
               "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
               "nodata": nodata, "compress": "deflate"}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype("float32"), b + 1)


def read_geotiff(path):
    """读取 GeoTIFF，返回 (cube, bbox, res)。保留原签名（单元测试依赖）。"""
    rasterio = _import_rasterio()
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        res = abs(src.transform.a)
    return cube, bbox, res


def read_dem(path):
    """读取 DEM 全量元数据：(cube, bbox, res, nodata, crs, transform)。"""
    rasterio = _import_rasterio()
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    try:
        with rasterio.open(path) as src:
            cube = src.read().astype(np.float32)
            b = src.bounds
            bbox = [b.left, b.bottom, b.right, b.top]
            res = abs(src.transform.a)
            nodata = src.nodata
            crs = src.crs
            transform = src.transform
    except Exception as exc:
        raise ValidationError(f"cannot read input raster '{path}': {exc}")
    return cube, bbox, res, nodata, crs, transform


def reproject_dem_to_wgs84(dem: np.ndarray, nodata: Optional[float],
                           src_transform, src_crs) -> Tuple[np.ndarray, List[float], float]:
    """把投影坐标系的 DEM 重投影到 EPSG:4326（双线性），返回 (dem, bbox, res_deg)。"""
    _import_rasterio()
    from rasterio.warp import calculate_default_transform, reproject, Resampling
    from rasterio.transform import array_bounds
    h, w = dem.shape
    left, bottom, right, top = array_bounds(h, w, src_transform)
    dst_transform, dst_w, dst_h = calculate_default_transform(
        src_crs, "EPSG:4326", w, h, left, bottom, right, top)
    dst_nodata = float(nodata) if nodata is not None else float("nan")
    dst = np.full((dst_h, dst_w), dst_nodata, dtype=np.float32)
    reproject(
        source=np.nan_to_num(dem, nan=dst_nodata if nodata is not None else 0.0),
        destination=dst,
        src_transform=src_transform, src_crs=src_crs,
        dst_transform=dst_transform, dst_crs="EPSG:4326",
        src_nodata=nodata if nodata is not None else None,
        dst_nodata=dst_nodata,
        resampling=Resampling.bilinear,
    )
    l2, b2, r2, t2 = array_bounds(dst_h, dst_w, dst_transform)
    return dst, [l2, b2, r2, t2], abs(dst_transform.a)


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
        inputs={"input": getattr(args, "input", None),
                "exaggeration": getattr(args, "exaggeration", None),
                "synthetic": bool(getattr(args, "synthetic", False))},
        outputs=[OutputFile(**o) for o in outputs], qa=qa,
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
    os.makedirs(output_dir, exist_ok=True)

    # 值域校验（越界 → exit 6）
    validate_params(args)

    bbox = list(args.bbox) if args.bbox else None
    synth_info: Optional[Dict[str, Any]] = None
    nodata_in: Optional[float] = None

    if args.input and not args.synthetic:
        cube, file_bbox, file_res, nodata_in, crs, transform = read_dem(args.input)
        if cube.size == 0:
            raise ValidationError("input raster is empty")
        if crs is None:
            raise ValidationError(
                "input raster has no coordinate reference system (CRS) defined; "
                "cannot determine georeferencing — provide a CRS-tagged DEM")
        dem = cube[0]
        if crs.is_geographic:
            data_bbox = file_bbox
        else:
            dem, data_bbox, _res = reproject_dem_to_wgs84(dem, nodata_in, transform, crs)
        bbox = bbox if bbox is not None else data_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        dem, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    bbox = validate_bbox(bbox)
    if dem.size == 0:
        raise ValidationError("input raster is empty")
    h, w = dem.shape
    if h < 3 or w < 3:
        raise ValidationError(
            f"input raster too small for gradient computation ({h}x{w}); need >= 3x3 pixels")

    # 水平像元尺寸（米）：用户显式 --cellsize 按米解释，否则由 bbox/栅格尺寸推导
    cellsize_m = float(args.cellsize) if args.cellsize is not None else cellsize_meters(bbox, h, w)

    # NoData / NaN 掩码：无效像元不参与梯度与统计
    valid = np.isfinite(dem)
    if nodata_in is not None:
        valid &= (dem != np.float32(nodata_in))
    if not valid.any():
        raise ValidationError("input raster is entirely NoData — nothing to render")
    if not valid.all():
        # 用有效像元均值填充无效像元（仅用于梯度计算，输出仍标记 nodata）
        dem = np.where(valid, dem, float(dem[valid].mean())).astype(np.float32)

    zfactor = float(args.exaggeration)  # 纯垂直夸张系数，作用于 z 后再除以米制 cellsize
    nx, ny, nz = dem_normals(dem, cellsize=cellsize_m, zfactor=zfactor)
    lx, ly, lz = light_vector(args.azimuth, args.altitude)
    shade = lambertian_shade(nx, ny, nz, lx, ly, lz)

    # DEM 归一化（仅统计有效像元）→ terrain 色彩 → 光照叠加
    dmin, dmax = float(dem[valid].min()), float(dem[valid].max())
    dem01 = (dem - dmin) / (dmax - dmin) if dmax > dmin else np.zeros_like(dem)
    dem01 = np.clip(dem01, 0.0, 1.0)
    base_rgb = terrain_rgb(dem01)
    shaded_rgb = shade_color_overlay(base_rgb, shade, ambient=args.ambient)
    if not valid.all():
        shaded_rgb[~valid] = 0.0
        shade = np.where(valid, shade, SHADE_NODATA).astype(np.float32)
    rgb_u8 = (shaded_rgb * 255.0).round().astype(np.uint8)
    png_bytes = encode_png_bytes(rgb_u8)
    image_b64 = base64.b64encode(png_bytes).decode("ascii")

    meta = {
        "title": args.title, "source": source_note,
        "exaggeration": args.exaggeration, "zfactor": zfactor,
        "cellsize_m": cellsize_m, "azimuth": args.azimuth, "altitude": args.altitude,
        "ambient": args.ambient, "bbox": bbox,
        "shape": [int(h), int(w)],
        "elev_min": dmin, "elev_max": dmax, "generated_at": _utc_now(),
    }
    if synth_info is not None:
        meta["synthetic"] = synth_info

    html = build_viewer_html(image_b64, meta)
    html_path = os.path.join(output_dir, "terrain_3d.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    # 可验证产物：山体阴影栅格 + JSON
    out_tif = os.path.join(output_dir, "shaded_relief.tif")
    write_geotiff(out_tif, shade.astype(np.float32), bbox, nodata=SHADE_NODATA)
    meta_path = os.path.join(output_dir, "terrain_3d.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "exaggeration": args.exaggeration,
          "azimuth": args.azimuth, "altitude": args.altitude,
          "shade_mean": float(np.mean(shade[valid])) if valid.all() else float(shade[valid].mean()),
          "valid_fraction": float(valid.mean()),
          "png_bytes": len(png_bytes), "bbox": bbox}
    outputs = [
        {"path": html_path, "kind": "text"},
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": meta_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] exaggeration: {args.exaggeration}  zfactor: {zfactor:.4f}  cellsize_m: {cellsize_m:.2f}")
        print(f"[{SKILL_NAME}] light: az={args.azimuth} alt={args.altitude}  mean shade: {qa['shade_mean']:.3f}")
        print(f"[{SKILL_NAME}] html: {html_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Render DEM into a lit 3D terrain image with an interactive HTML viewer.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input DEM GeoTIFF")
    p.add_argument("--exaggeration", type=float, default=2.0,
                   help="vertical exaggeration factor (default: 2.0)")
    p.add_argument("--azimuth", type=float, default=315.0,
                   help="sun azimuth degrees, north=0 east=90 (default: 315)")
    p.add_argument("--altitude", type=float, default=45.0,
                   help="sun altitude degrees above horizon (default: 45)")
    p.add_argument("--ambient", type=float, default=0.15,
                   help="ambient light 0..1 (default: 0.15)")
    p.add_argument("--cellsize", type=float, default=None,
                   help="horizontal cell size in metres; auto-derived from bbox/CRS "
                        "when omitted (default: auto)")
    p.add_argument("--title", default="3D Terrain", help="viewer title")
    p.add_argument("--synthetic", action="store_true")
    p.add_argument("--output-dir", default="./output")
    p.add_argument("--quiet", action="store_true")
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
