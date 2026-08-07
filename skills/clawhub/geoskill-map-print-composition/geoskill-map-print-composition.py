#!/usr/bin/env python3
"""map-print-composition — 地图打印合成

面向印刷 / 出版的高分辨率地图合成：把彩色地形层与 Horn 山体阴影层做
**乘法混合**（shaded relief），可再叠加任意 RGB 图层（alpha 合成），最终
输出带地理配准的 RGB GeoTIFF 与矢量 PDF。

数据源：本地 DEM GeoTIFF（可另给 ``--overlay`` RGB 图层），或 ``--synthetic``
生成模拟 DEM 用于离线测试。

隐私声明 / Privacy：完全离线；所有处理本地完成，不上传用户数据。

Usage:
    python map-print-composition.py --input dem.tif --dpi 300 --azimuth 315
    python map-print-composition.py --bbox 116 39 117 40 --synthetic --altitude 40

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
SKILL_NAME = "map-print-composition"

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


CMAPS = ["terrain", "viridis", "magma", "inferno", "plasma", "gray", "YlGn", "turbo"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法：Horn 山体阴影（同 hillshade-visualization）
# ---------------------------------------------------------------------------
def horn_hillshade(dem: np.ndarray, azimuth: float = 315.0, altitude: float = 45.0,
                   cellsize: float = 1.0, z_factor: float = 1.0) -> np.ndarray:
    z = dem.astype(np.float32) * float(z_factor)
    # NaN-aware: build a 0/1 valid mask and use it to mark NoData pixels
    valid = np.isfinite(z).astype(np.float32)
    z_filled = np.where(np.isfinite(z), z, 0.0).astype(np.float32)
    zp = np.pad(z_filled, 1, mode="edge")
    z1, z2, z3 = zp[:-2, :-2], zp[:-2, 1:-1], zp[:-2, 2:]
    z4, z6 = zp[1:-1, :-2], zp[1:-1, 2:]
    z7, z8, z9 = zp[2:, :-2], zp[2:, 1:-1], zp[2:, 2:]
    dzdx = ((z3 + 2 * z6 + z9) - (z1 + 2 * z4 + z7)) / (8.0 * cellsize)
    dzdy = ((z7 + 2 * z8 + z9) - (z1 + 2 * z2 + z3)) / (8.0 * cellsize)
    slope = np.arctan(np.sqrt(dzdx ** 2 + dzdy ** 2))
    aspect = np.arctan2(dzdy, -dzdx)
    az_rad = np.deg2rad(360.0 - float(azimuth) + 90.0)
    alt_rad = np.deg2rad(altitude)
    hs = (np.sin(alt_rad) * np.cos(slope)
          + np.cos(alt_rad) * np.sin(slope) * np.cos(az_rad - aspect))
    # Mark NoData pixels (center or any neighbor NoData) as hs=NaN
    valid_p = np.pad(valid, 1, mode="edge")
    any_nan = 1.0 - (
        valid_p[:-2, :-2] * valid_p[:-2, 1:-1] * valid_p[:-2, 2:]
        * valid_p[1:-1, :-2] * valid_p[1:-1, 2:]
        * valid_p[2:, :-2] * valid_p[2:, 1:-1] * valid_p[2:, 2:]
    )
    hs = np.where(any_nan > 0, np.nan, hs)
    return np.clip(np.nan_to_num(hs, nan=0.0), 0.0, 1.0).astype(np.float32)


# ---------------------------------------------------------------------------
# 核心算法：图层合成
# ---------------------------------------------------------------------------
def alpha_composite(base: np.ndarray, overlay: np.ndarray, alpha: float) -> np.ndarray:
    """RGB 图层 alpha 合成：out = base*(1-a) + overlay*a。

    base/overlay 均为 [0,1] 的 (H, W, 3)。alpha 裁剪到 [0,1]。
    """
    a = float(np.clip(alpha, 0.0, 1.0))
    out = np.asarray(base, dtype=np.float64) * (1.0 - a) \
        + np.asarray(overlay, dtype=np.float64) * a
    return np.clip(out, 0.0, 1.0).astype(np.float32)


def hillshade_blend(rgb: np.ndarray, hillshade: np.ndarray, ambient: float = 0.0) -> np.ndarray:
    """shaded relief 乘法混合：out = rgb * (ambient + (1-ambient)*hs)。

    hs=1 → 原色；hs=0 → 环境光底色（默认黑）。
    """
    hs = np.clip(np.asarray(hillshade, dtype=np.float64), 0.0, 1.0)
    amb = float(np.clip(ambient, 0.0, 1.0))
    factor = (amb + (1.0 - amb) * hs)[..., np.newaxis]
    return np.clip(np.asarray(rgb, dtype=np.float64) * factor, 0.0, 1.0).astype(np.float32)


def dem_to_color(dem: np.ndarray, cmap_name: str) -> np.ndarray:
    """DEM 归一化后经 colormap 转 [0,1] RGB。"""
    import matplotlib
    if cmap_name not in CMAPS:
        raise UsageError(f"unknown cmap '{cmap_name}'. Choose: {CMAPS}", cmap=cmap_name)
    v = dem.astype(np.float64)
    # NaN-safe normalization: use nanmin/nanmax so NoData pixels are excluded
    # from the range; render NoData pixels as black (0,0,0) in the output.
    valid_mask = np.isfinite(v)
    if not valid_mask.any():
        # All NoData (shouldn't reach here due to upstream check)
        return np.zeros(v.shape + (3,), dtype=np.float32)
    vmin, vmax = float(np.nanmin(v)), float(np.nanmax(v))
    norm = (v - vmin) / (vmax - vmin) if vmax > vmin else np.zeros_like(v)
    norm = np.where(valid_mask, norm, 0.0)
    norm = np.clip(norm, 0.0, 1.0)
    return matplotlib.colormaps[cmap_name](norm)[..., :3].astype(np.float32)


def to_uint8_rgb(rgb01: np.ndarray) -> np.ndarray:
    return (np.clip(rgb01, 0.0, 1.0) * 255.0).round().astype(np.uint8)


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 128, height: int = 128,
                       seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1); yy /= max(height - 1, 1)
    peak = 1400.0 * np.exp(-(((xx - 0.62) ** 2 + (yy - 0.55) ** 2) / 0.02))
    ridge = 500.0 * np.exp(-(((yy - 0.3) ** 2) / 0.008))
    base = 120.0 + 160.0 * xx
    noise = rng.normal(0, 6.0, size=(height, width)).astype(np.float32)
    dem = (base + peak + ridge + noise).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "min_elev": float(dem.min()), "max_elev": float(dem.max()),
            "kind": "synthetic-dem"}
    return dem, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（RGB uint8 打印栅格 + float 输入）
# ---------------------------------------------------------------------------
def write_geotiff_rgb(path: str, rgb_u8: np.ndarray, bbox: List[float]) -> None:
    """写 3 波段 uint8 RGB GeoTIFF。"""
    import rasterio
    from rasterio.transform import from_bounds
    if rgb_u8.ndim != 3 or rgb_u8.shape[2] != 3:
        raise ValidationError("write_geotiff_rgb expects (H, W, 3) uint8")
    h, w, _ = rgb_u8.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {"driver": "GTiff", "height": h, "width": w, "count": 3,
               "dtype": "uint8", "crs": "EPSG:4326", "transform": transform,
               "compress": "deflate"}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(3):
            dst.write(rgb_u8[..., b].astype("uint8"), b + 1)


def write_geotiff(path, cube, bbox, nodata=-9999.0):
    import rasterio
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
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    # NoData → NaN for downstream NaN-safe ops
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    return cube, bbox


def validate_bbox(bbox) -> None:
    """Validate bbox as (W, S, E, N); raise ValidationError on bad input.

    Rules (WGS-84):
        * 4 floats
        * W < E, S < N (zero-area or reversed bbox rejected)
        * -180 <= W, E <= 180; -90 <= S, N <= 90
        * bbox spans <1e-4 deg on either axis rejected (effectively zero area)
    Cross-180° is reported as a hint to split, but rejected for clarity.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats (W, S, E, N)", bbox=bbox)
    W, S, E, N = [float(x) for x in bbox]
    if not (-180.0 <= W <= 180.0 and -180.0 <= E <= 180.0):
        raise ValidationError(
            f"longitude out of range: W={W}, E={E} must be in [-180, 180]",
            bbox=bbox,
        )
    if not (-90.0 <= S <= 90.0 and -90.0 <= N <= 90.0):
        raise ValidationError(
            f"latitude out of range: S={S}, N={N} must be in [-90, 90]",
            bbox=bbox,
        )
    if W >= E:
        raise ValidationError(
            f"bbox has W >= E (W={W}, E={E}); please use W < E. "
            f"For cross-180° regions, split into two bboxes.",
            bbox=bbox,
        )
    if S >= N:
        raise ValidationError(
            f"bbox has S >= N (S={S}, N={N}); please use S < N.",
            bbox=bbox,
        )
    if (E - W) < 1e-4 or (N - S) < 1e-4:
        raise ValidationError(
            f"bbox span too small: width={E - W}, height={N - S}; must be >= 1e-4 deg",
            bbox=bbox,
        )


# ---------------------------------------------------------------------------
# PDF 版式（matplotlib）
# ---------------------------------------------------------------------------
def render_pdf(path: str, rgb_u8: np.ndarray, bbox: List[float], title: str,
               dpi: int) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(8, 6), dpi=min(dpi, 300))
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.88])
    ax.imshow(rgb_u8, extent=[bbox[0], bbox[2], bbox[1], bbox[3]], origin="upper")
    ax.set_title(title)
    ax.set_xlabel("Longitude"); ax.set_ylabel("Latitude")
    fig.savefig(path, format="pdf", dpi=min(dpi, 300))
    plt.close(fig)


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
                "cmap": getattr(args, "cmap", None),
                "dpi": getattr(args, "dpi", None),
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
    bbox = list(args.bbox) if args.bbox else None

    synth_info: Optional[Dict[str, Any]] = None
    n_valid_pixels = 0
    input_nodata = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is None:
            raise ValidationError("could not determine bbox from input")
        validate_bbox(bbox)
        dem = cube[0]
        valid_mask = np.isfinite(dem)
        n_valid_pixels = int(valid_mask.sum())
        input_nodata = "NaN-replaced (src.nodata in cube)"
        if n_valid_pixels == 0:
            raise ValidationError(
                "input raster is entirely NoData (no valid pixels); nothing to render",
                path=args.input, n_total_pixels=int(dem.size),
            )
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        dem, synth_info = generate_synthetic(bbox)
        n_valid_pixels = int(dem.size)  # synthetic has no NoData
        source_note = "synthetic"

    if dem.size == 0:
        raise ValidationError("input raster is empty")
    if bbox is None:
        raise UsageError("could not determine bbox")

    # Now that we know inputs are valid, ensure output dir
    os.makedirs(output_dir, exist_ok=True)

    # 1) 彩色地形层
    color_rgb = dem_to_color(dem, args.cmap)
    # 2) 山体阴影乘法混合
    hs = horn_hillshade(dem, azimuth=args.azimuth, altitude=args.altitude,
                        z_factor=args.zfactor)
    shaded = hillshade_blend(color_rgb, hs, ambient=args.ambient)
    composed = shaded

    # 3) 可选叠加图层（alpha 合成）
    if args.overlay and not args.synthetic:
        ov_cube, _ = read_geotiff(args.overlay)
        ov = ov_cube[:3]
        if ov.shape[0] < 3:
            ov = np.repeat(ov[:1], 3, axis=0)
        v = ov.astype(np.float64)
        vmin, vmax = float(np.nanmin(v)), float(np.nanmax(v))
        ov_norm = (v - vmin) / (vmax - vmin) if vmax > vmin else np.zeros_like(v)
        ov_norm = np.clip(np.nan_to_num(ov_norm, nan=0.0), 0.0, 1.0)
        ov_rgb = np.transpose(ov_norm, (1, 2, 0))
        if ov_rgb.shape[:2] != composed.shape[:2]:
            raise ValidationError("overlay raster size does not match base raster")
        composed = alpha_composite(composed, ov_rgb, args.overlay_alpha)

    rgb_u8 = to_uint8_rgb(composed)

    # 输出：RGB GeoTIFF + PDF
    tif_path = os.path.join(output_dir, "print_map.tif")
    write_geotiff_rgb(tif_path, rgb_u8, bbox)
    pdf_path = os.path.join(output_dir, "print_map.pdf")
    render_pdf(pdf_path, rgb_u8, bbox, args.title, args.dpi)

    meta = {"source": source_note, "cmap": args.cmap, "dpi": args.dpi,
            "azimuth": args.azimuth, "altitude": args.altitude,
            "zfactor": args.zfactor, "ambient": args.ambient,
            "overlay": args.overlay, "overlay_alpha": args.overlay_alpha,
            "bbox": bbox, "shape": [int(rgb_u8.shape[0]), int(rgb_u8.shape[1])],
            "rgb_mean": [float(np.mean(rgb_u8[..., i])) for i in range(3)],
            "hillshade_mean": float(np.mean(hs)) if np.all(np.isfinite(hs)) else float(np.nanmean(hs)),
            "n_valid_pixels": n_valid_pixels,
            "n_total_pixels": int(dem.size),
            "input_nodata_handling": input_nodata,
            "generated_at": _utc_now()}
    if synth_info is not None:
        meta["synthetic"] = synth_info
    meta_path = os.path.join(output_dir, "print_meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "cmap": args.cmap, "dpi": args.dpi,
          "hillshade_mean": meta["hillshade_mean"],
          "rgb_mean": meta["rgb_mean"], "bbox": bbox,
          "n_valid_pixels": n_valid_pixels,
          "n_total_pixels": int(dem.size),
          "input_nodata_handling": input_nodata}
    outputs = [
        {"path": tif_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 3},
        {"path": pdf_path, "kind": "text"},
        {"path": meta_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  cmap: {args.cmap}  dpi: {args.dpi}")
        print(f"[{SKILL_NAME}] light: az={args.azimuth} alt={args.altitude}  hs mean: {meta['hillshade_mean']:.3f}")
        print(f"[{SKILL_NAME}] tif: {tif_path}")
        print(f"[{SKILL_NAME}] pdf: {pdf_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Compose print-ready maps: shaded-relief blend, layer alpha compositing, RGB GeoTIFF + PDF.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input DEM GeoTIFF")
    p.add_argument("--overlay", help="optional overlay GeoTIFF (alpha-composited)")
    p.add_argument("--overlay-alpha", type=float, default=0.4,
                   help="overlay alpha 0..1 (default: 0.4)")
    p.add_argument("--cmap", default="terrain", choices=CMAPS)
    p.add_argument("--azimuth", type=float, default=315.0)
    p.add_argument("--altitude", type=float, default=45.0)
    p.add_argument("--zfactor", type=float, default=1.0)
    p.add_argument("--ambient", type=float, default=0.05,
                   help="ambient light 0..1 (default: 0.05)")
    p.add_argument("--dpi", type=int, default=150, help="print dpi (default: 150)")
    p.add_argument("--title", default="Print Map")
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
