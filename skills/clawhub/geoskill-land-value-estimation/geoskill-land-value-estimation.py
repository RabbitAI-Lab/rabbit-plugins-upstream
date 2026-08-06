#!/usr/bin/env python3
"""land-value-estimation — 土地价值估算

用特征价格（Hedonic）模型估算土地价值的空间分布。核心算法：

- **可达性**：到城市中心（或 CBD）的距离衰减，
  accessibility = exp(−distance / decay)。越靠近中心，可达性越高。
- **POI 密度**：兴趣点（设施）密度的局部核密度，设施越多价值越高。
- **绿地邻近性**：到绿地的距离衰减，靠近绿地价值越高。
- **Hedonic 模型**：value = β0 + β_acc × accessibility + β_poi × poi + β_green × green。
  系数可通过 ``--coef-*`` 指定，或用少量样本（合成模式内置）做线性回归标定。

数据源：本地多波段栅格（band1=到中心距离, band2=POI密度, band3=绿地距离），
或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络。

Usage:
    python land-value-estimation.py --input features.tif
    python land-value-estimation.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "land-value-estimation"

# ---------------------------------------------------------------------------
# Input validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate geographic bbox: W<E, S<N, lat in [-90,90], lon in [-180,180]."""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be [W, S, E, N] with 4 floats")
    w, s, e, n = [float(x) for x in bbox]
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError("bbox contains non-finite values")
    if w < -180.0 or e > 180.0 or s < -90.0 or n > 90.0:
        raise ValidationError(
            f"bbox out of range: lon=[{w},{e}] must be in [-180,180], lat=[{s},{n}] in [-90,90]")
    if w >= e:
        raise ValidationError(
            f"bbox W must be < E; got W={w}, E={e} (likely reversed; this skill does not support wrapping around 180°)")
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N; got S={s}, N={n} (likely reversed)")
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(f"bbox has zero area: W={w}, E={e}, S={s}, N={n}")


def validate_params(args) -> None:
    """Validate --decay/--coef-* values."""
    if not np.isfinite(args.decay):
        raise ValidationError(f"--decay must be finite, got {args.decay}")
    if args.decay <= 0:
        raise ValidationError(
            f"--decay must be > 0 (distance decay scale in pixels); got {args.decay}")
    for name in ("intercept", "coef_acc", "coef_poi", "coef_green"):
        v = getattr(args, name)
        if not np.isfinite(v):
            raise ValidationError(f"--{name.replace('_', '-')} must be finite, got {v}")


def read_geotiff_with_nodata(path: str):
    """Read multiband GeoTIFF, replacing NoData with NaN; return (cube, bbox)."""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nd = src.nodata
    if nd is not None and np.isfinite(float(nd)):
        cube = np.where(cube == float(nd), np.nan, cube).astype(np.float32)
    return cube, bbox

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


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------

def accessibility(distance: np.ndarray, decay: float = 1000.0) -> np.ndarray:
    """可达性 = exp(−distance / decay)，值域 (0, 1]。

    distance=0 → 1；distance→∞ → 0。decay 为衰减尺度（同 distance 单位）。
    """
    d = np.clip(np.asarray(distance, dtype=np.float32), 0.0, None)
    return np.exp(-d / max(float(decay), 1e-6)).astype(np.float32)


def hedonic_value(
    accessibility_arr: np.ndarray,
    poi_density: np.ndarray,
    green_proximity: np.ndarray,
    intercept: float = 1000.0,
    coef_acc: float = 5000.0,
    coef_poi: float = 2000.0,
    coef_green: float = 1500.0,
) -> np.ndarray:
    """Hedonic 特征价格：value = β0 + Σ βi × feature_i。

    线性可加，价值 ≥ 0（裁剪）。
    """
    a = np.asarray(accessibility_arr, dtype=np.float32)
    p = np.asarray(poi_density, dtype=np.float32)
    g = np.asarray(green_proximity, dtype=np.float32)
    value = (intercept
             + coef_acc * a
             + coef_poi * p
             + coef_green * g)
    return np.clip(value, 0.0, None).astype(np.float32)


def calibrate_coefficients(
    features: np.ndarray,
    observed_values: np.ndarray,
) -> np.ndarray:
    """用最小二乘标定 Hedonic 系数（含截距）。

    features: (n_samples, n_features)；observed_values: (n_samples,)。
    返回 [intercept, coef_1, ..., coef_n]。
    """
    X = np.asarray(features, dtype=np.float64)
    y = np.asarray(observed_values, dtype=np.float64)
    ones = np.ones((X.shape[0], 1), dtype=np.float64)
    Xb = np.hstack([ones, X])
    coef, *_ = np.linalg.lstsq(Xb, y, rcond=None)
    return coef


# ---------------------------------------------------------------------------
# 合成数据：到中心距离 + POI 密度 + 绿地距离
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height_px: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成三个特征栅格：到中心距离、POI 密度、到绿地距离。

    城市中心在影像中心：距离从中心向外递增；POI 密度中心高、边缘低；
    绿地在右下角一块，绿地距离从该块向外递增。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height_px, 0:width].astype(np.float32)
    cx, cy = width / 2.0, height_px / 2.0

    dist_center = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    poi_density = np.exp(-dist_center / (width / 4.0))

    # 绿地斑块（右下角）
    gx, gy = width * 0.8, height_px * 0.8
    dist_green = np.sqrt((xx - gx) ** 2 + (yy - gy) ** 2)

    info = {
        "bbox": bbox, "width": width, "height": height_px,
        "center": [cx, cy],
    }
    return dist_center, poi_density, dist_green, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    cube: np.ndarray,
    bbox: List[float],
    nodata: float = -9999.0,
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
        nd = src.nodata
    if nd is not None and np.isfinite(float(nd)):
        cube = np.where(cube == float(nd), np.nan, cube).astype(np.float32)
    return cube, bbox


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(
    output_dir: str,
    args: argparse.Namespace,
    outputs: List[Dict[str, Any]],
    qa: Dict[str, Any],
    started_at: str,
    exit_code: int,
    bbox: List[float],
) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME,
        skill_version=VERSION,
        command=cmd,
        started_at=started_at,
        finished_at=_utc_now(),
        exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "decay": getattr(args, "decay", 30.0),
            "intercept": getattr(args, "intercept", 1000.0),
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
    validate_params(args)

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if cube.shape[0] < 3:
            raise ValidationError("input must have 3 bands: dist_center, poi_density, dist_green")
        dist_center = cube[0]
        poi_density = cube[1]
        dist_green = cube[2]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        dist_center, poi_density, dist_green, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    if dist_center.size == 0:
        raise ValidationError("input raster is empty")
    if not np.any(np.isfinite(np.stack([dist_center, poi_density, dist_green], axis=0))):
        raise ValidationError(
            "input raster has no valid pixels (entirely NoData/NaN)")

    os.makedirs(output_dir, exist_ok=True)

    # 2) 特征 → 可达性/绿地邻近性 → Hedonic 价值
    acc = accessibility(dist_center, decay=args.decay)
    green_prox = accessibility(dist_green, decay=args.decay)
    value = hedonic_value(
        acc, poi_density, green_prox,
        intercept=args.intercept,
        coef_acc=args.coef_acc,
        coef_poi=args.coef_poi,
        coef_green=args.coef_green,
    )

    out_tif = os.path.join(output_dir, "land_value.tif")
    write_geotiff(out_tif, value, bbox)

    coefs = {
        "intercept": args.intercept,
        "coef_accessibility": args.coef_acc,
        "coef_poi": args.coef_poi,
        "coef_green": args.coef_green,
        "decay": args.decay,
    }
    coefs_path = os.path.join(output_dir, "hedonic_coefficients.json")
    with open(coefs_path, "w", encoding="utf-8") as f:
        json.dump(coefs, f, ensure_ascii=False, indent=2)

    stats = {
        "mean_value": float(np.mean(value)),
        "max_value": float(np.max(value)),
        "min_value": float(np.min(value)),
        "mean_accessibility": float(np.mean(acc)),
    }
    stats_path = os.path.join(output_dir, "value_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {"source": source_note}
    qa.update(stats)
    qa["n_valid_pixels"] = int(value.size)
    qa["n_total_pixels"] = int(value.size)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": coefs_path, "kind": "json"},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean land value: {stats['mean_value']:.1f}")
        print(f"[{SKILL_NAME}] value range: [{stats['min_value']:.1f}, {stats['max_value']:.1f}]")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Land value estimation via hedonic pricing and accessibility.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF with 3 bands: dist_center, poi, dist_green")
    p.add_argument("--decay", type=float, default=30.0,
                   help="distance decay scale in pixels (default: 30)")
    p.add_argument("--intercept", type=float, default=1000.0,
                   help="hedonic intercept (default: 1000)")
    p.add_argument("--coef-acc", type=float, default=5000.0,
                   help="accessibility coefficient (default: 5000)")
    p.add_argument("--coef-poi", type=float, default=2000.0,
                   help="POI density coefficient (default: 2000)")
    p.add_argument("--coef-green", type=float, default=1500.0,
                   help="green proximity coefficient (default: 1500)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic scene (offline)")
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
