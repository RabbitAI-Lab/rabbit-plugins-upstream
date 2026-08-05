#!/usr/bin/env python3
"""hillshade-visualization — 山体阴影可视化

用 Horn (1981) 算法计算山体阴影，支持**多方向合成**（多个方位角按权重加权，
突出不同走向的地形纹理）、垂直夸张系数与地形色彩叠加。

数据源：本地 DEM GeoTIFF，或 ``--synthetic`` 生成物理一致的模拟 DEM 用于离线测试。

隐私声明 / Privacy：完全离线；所有处理本地完成，不上传用户数据。

Usage:
    python hillshade-visualization.py --input dem.tif --zfactor 3 --altitude 45
    python hillshade-visualization.py --bbox 116 39 117 40 --synthetic --azimuths 315 270

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import io
import json
import os
import sys
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "hillshade-visualization"

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


CMAPS = ["terrain", "viridis", "gray", "magma", "inferno", "plasma", "turbo"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox):
    """Validate a geographic bbox [W, S, E, N] in EPSG:4326.

    Rules (consistent across the project):
      - W < E (no antimeridian wrap; user must split the request)
      - S < N
      - -180 <= W, E <= 180
      - -90 <= S, N <= 90
    Returns the bbox on success; raises ValidationError on failure.
    """
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError("bbox must be a sequence of 4 floats [W S E N]")
    w, s, e, n = [float(v) for v in bbox]
    if not (w < e):
        raise ValidationError(
            f"bbox W={w} must be < E={e} (antimeridian wrap not supported; "
            f"split your request into two boxes if needed)")
    if not (s < n):
        raise ValidationError(f"bbox S={s} must be < N={n}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox lon must be in [-180, 180], got W={w}, E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox lat must be in [-90, 90], got S={s}, N={n}")
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# 核心算法：Horn 山体阴影
# ---------------------------------------------------------------------------
def horn_hillshade(
    dem: np.ndarray, azimuth: float = 315.0, altitude: float = 45.0,
    cellsize: float = 1.0, z_factor: float = 1.0,
) -> np.ndarray:
    """Horn (1981) 单方向山体阴影，返回 [0, 1]。

    3x3 邻域差分：
        dz/dx = ((z3+2z6+z9) - (z1+2z4+z7)) / (8*cellsize)
        dz/dy = ((z7+2z8+z9) - (z1+2z2+z3)) / (8*cellsize)
        slope = atan(sqrt(dzdx^2+dzdy^2)),  aspect = atan2(dzdy, -dzdx)
        hs = sin(alt)cos(slope) + cos(alt)sin(slope)cos(az_rad - aspect)
    其中 az_rad = deg2rad(360 - azimuth + 90)（ESRI 约定）。
    平坦栅格 → hs = sin(altitude) 常数。
    """
    if altitude < 0 or altitude > 90:
        raise UsageError("altitude must be in [0, 90] degrees", altitude=altitude)
    z = dem.astype(np.float32) * float(z_factor)
    zp = np.pad(z, 1, mode="edge")
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
    return np.clip(hs, 0.0, 1.0).astype(np.float32)


def multidirectional_hillshade(
    dem: np.ndarray, azimuths: Sequence[float] = (315.0, 270.0, 360.0, 45.0),
    weights: Optional[Sequence[float]] = None, altitude: float = 45.0,
    cellsize: float = 1.0, z_factor: float = 1.0,
) -> Tuple[np.ndarray, List[float]]:
    """多方向山体阴影：各方位角 hillshade 的加权和（权重自动归一化）。

    返回 (combined, normalized_weights)。
    """
    azs = [float(a) for a in azimuths]
    if not azs:
        raise UsageError("at least one azimuth is required")
    if weights is None:
        w = np.ones(len(azs), dtype=float)
    else:
        w = np.asarray([float(x) for x in weights], dtype=float)
        if w.size != len(azs):
            raise UsageError(
                f"weights length ({w.size}) must match azimuths ({len(azs)})")
        if np.any(w < 0) or w.sum() <= 0:
            raise UsageError("weights must be non-negative and sum > 0")
    w = w / w.sum()
    combined = np.zeros_like(dem, dtype=np.float64)
    for az, wi in zip(azs, w):
        combined += wi * horn_hillshade(dem, azimuth=az, altitude=altitude,
                                        cellsize=cellsize, z_factor=z_factor)
    return np.clip(combined, 0.0, 1.0).astype(np.float32), [float(x) for x in w]


def normalize01(band: np.ndarray) -> np.ndarray:
    v = band.astype(np.float64)
    vmin, vmax = float(np.nanmin(v)), float(np.nanmax(v))
    if vmax <= vmin:
        return np.zeros_like(v, dtype=np.float32)
    return ((v - vmin) / (vmax - vmin)).astype(np.float32)


def color_overlay(dem_norm: np.ndarray, hillshade: np.ndarray,
                  cmap_name: str, ambient: float = 0.2) -> np.ndarray:
    """地形色彩 × 光照：rgb = cmap(dem_norm) * (ambient + (1-ambient)*hs)。

    返回 (H, W, 3) uint8。hs=1 → 全亮基色；hs=0 → 仅环境光。
    """
    import matplotlib
    if cmap_name not in CMAPS:
        raise UsageError(f"unknown cmap '{cmap_name}'. Choose: {CMAPS}", cmap=cmap_name)
    ambient = float(np.clip(ambient, 0.0, 1.0))
    base = matplotlib.colormaps[cmap_name](np.clip(dem_norm, 0.0, 1.0))[..., :3]
    factor = ambient + (1.0 - ambient) * np.clip(hillshade, 0.0, 1.0)
    rgb = base * factor[..., np.newaxis]
    return (np.clip(rgb, 0.0, 1.0) * 255.0).round().astype(np.uint8)


def encode_png_bytes(rgb_u8: np.ndarray) -> bytes:
    from PIL import Image
    buf = io.BytesIO()
    Image.fromarray(rgb_u8, "RGB").save(buf, format="PNG")
    return buf.getvalue()


# ---------------------------------------------------------------------------
# 合成数据：多山脊 DEM
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float], width: int = 128, height: int = 128, seed: int = 42
) -> Tuple[np.ndarray, Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1); yy /= max(height - 1, 1)
    ridges = (900.0 * np.exp(-(((xx - 0.3) ** 2) / 0.008))
              + 700.0 * np.exp(-(((xx - 0.7) ** 2) / 0.012))
              + 500.0 * np.exp(-(((yy - 0.5) ** 2) / 0.01)))
    base = 150.0 + 120.0 * xx
    noise = rng.normal(0, 5.0, size=(height, width)).astype(np.float32)
    dem = (base + ridges + noise).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "min_elev": float(dem.min()), "max_elev": float(dem.max()),
            "kind": "synthetic-dem"}
    return dem, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
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
    """Read a DEM GeoTIFF. Returns (cube, bbox).

    NoData values declared in the file are replaced with NaN. The cube may
    be (1, H, W) (single-band DEM) or (H, W) for a single-band input.
    """
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
    return cube, bbox


def finite_pixel_mask(dem: np.ndarray) -> np.ndarray:
    """Per-pixel mask: True iff the elevation is finite (not NaN/inf)."""
    return np.isfinite(np.asarray(dem))


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
                "azimuths": getattr(args, "azimuths", None),
                "zfactor": getattr(args, "zfactor", None),
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

    # --- pre-flight validation (BEFORE making output dir) -----------------
    bbox = list(args.bbox) if args.bbox else None

    synth_info: Optional[Dict[str, Any]] = None
    cellsize = args.cellsize
    input_nodata_value: Optional[float] = None
    n_valid = 0
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        # Capture the declared NoData value for the qa/manifest.
        import rasterio as _rio
        with _rio.open(args.input) as _src:
            input_nodata_value = _src.nodata
        if bbox is not None:
            bbox = validate_bbox(bbox)
        else:
            bbox = validate_bbox(file_bbox)
        if cube.ndim != 3 or cube.shape[0] != 1:
            raise ValidationError(
                f"input must be a single-band DEM (1, H, W); got shape={cube.shape}",
                bands=int(cube.shape[0]) if cube.ndim == 3 else 0)
        dem = cube[0]
        if dem.size == 0:
            raise ValidationError("input raster is empty")
        valid = finite_pixel_mask(dem)
        n_valid = int(valid.sum())
        if n_valid == 0:
            raise ValidationError(
                f"input raster has no valid pixels "
                f"(all values are nodata={input_nodata_value})")
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        dem, synth_info = generate_synthetic(bbox)
        n_valid = int(dem.size)
        source_note = "synthetic"

    if bbox is None:
        raise UsageError("could not determine bbox")

    # All checks passed → now create the output dir.
    os.makedirs(output_dir, exist_ok=True)

    hs, norm_w = multidirectional_hillshade(
        dem, azimuths=args.azimuths, weights=args.weights,
        altitude=args.altitude, cellsize=cellsize, z_factor=args.zfactor)

    # 色彩叠加 PNG
    dem_norm = normalize01(dem)
    rgb = color_overlay(dem_norm, hs, args.cmap, ambient=args.ambient)
    png_bytes = encode_png_bytes(rgb)
    png_path = os.path.join(output_dir, "color_shaded.png")
    with open(png_path, "wb") as f:
        f.write(png_bytes)

    # 可验证产物：hillshade GeoTIFF + 元数据
    out_tif = os.path.join(output_dir, "hillshade.tif")
    write_geotiff(out_tif, hs.astype(np.float32), bbox)
    meta = {"source": source_note, "azimuths": list(args.azimuths),
            "weights": norm_w, "altitude": args.altitude,
            "zfactor": args.zfactor, "cellsize": cellsize, "cmap": args.cmap,
            "ambient": args.ambient, "bbox": bbox,
            "hillshade_mean": float(np.mean(hs)), "hillshade_std": float(np.std(hs)),
            "shape": [int(dem.shape[0]), int(dem.shape[1])], "generated_at": _utc_now()}
    if synth_info is not None:
        meta["synthetic"] = synth_info
    meta_path = os.path.join(output_dir, "hillshade_meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "azimuths": list(args.azimuths),
          "weights": norm_w, "altitude": args.altitude, "zfactor": args.zfactor,
          "hillshade_mean": meta["hillshade_mean"], "bbox": bbox,
          "n_valid_pixels": n_valid}
    if input_nodata_value is not None:
        qa["input_nodata"] = input_nodata_value
    outputs = [
        {"path": png_path, "kind": "text"},
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": meta_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] azimuths: {list(args.azimuths)}  weights: {[round(w,3) for w in norm_w]}")
        print(f"[{SKILL_NAME}] altitude: {args.altitude}  zfactor: {args.zfactor}")
        print(f"[{SKILL_NAME}] hillshade mean: {meta['hillshade_mean']:.3f}")
        print(f"[{SKILL_NAME}] png: {png_path}  tif: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Multi-directional Horn hillshade with vertical exaggeration and color overlay.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input DEM GeoTIFF")
    p.add_argument("--azimuths", nargs="+", type=float,
                   default=[315.0, 270.0, 360.0, 45.0],
                   help="light azimuths in degrees (default: 315 270 360 45)")
    p.add_argument("--weights", nargs="+", type=float, default=None,
                   help="weights per azimuth (default: equal)")
    p.add_argument("--altitude", type=float, default=45.0,
                   help="light altitude degrees (default: 45)")
    p.add_argument("--zfactor", type=float, default=1.0,
                   help="vertical exaggeration factor (default: 1)")
    p.add_argument("--cellsize", type=float, default=1.0,
                   help="horizontal cell size (default: 1)")
    p.add_argument("--cmap", default="terrain", choices=CMAPS)
    p.add_argument("--ambient", type=float, default=0.2,
                   help="ambient light 0..1 (default: 0.2)")
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
