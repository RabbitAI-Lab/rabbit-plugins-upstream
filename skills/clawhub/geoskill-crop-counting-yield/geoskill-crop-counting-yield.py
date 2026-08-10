#!/usr/bin/env python3
"""crop-counting-yield — 作物计数与产量估算

基于高分辨率冠层高度/植被指数栅格，用局部峰值检测定位单株，分水岭分割
 delineate 冠幅，统计株数密度，并用经验模型估算产量。

核心算法
--------
- **冠层峰值检测**：scipy.ndimage 局部最大值（min_distance 去重）定位单株中心。
- **分水岭分割**：以峰值为种子，对冠层梯度做分水岭，划分单株冠幅。
- **产量估算**：yield = a * density * mean_vigor + b（经验线性模型）。

数据源：本地 CHM/NDVI 栅格或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线，``--synthetic`` 完全无网络，本地处理不上传。

Usage:
    python crop-counting-yield.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "crop-counting-yield"

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, DependencyError, to_exit_code,
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

    class DependencyError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=3, kind="EDepend", **k)

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
def detect_peaks(canopy: np.ndarray, min_distance: int = 3, threshold_abs: float = 0.1) -> np.ndarray:
    """局部峰值检测，返回 (N, 2) 的 [row, col] 坐标。"""
    try:
        from skimage.feature import peak_local_max
    except ImportError:
        try:
            from scipy.ndimage import maximum_filter
        except ImportError as exc:  # pragma: no cover
            raise DependencyError("scipy or scikit-image required for peak detection") from exc
        # scipy fallback: local max via maximum_filter
        canopy = np.asarray(canopy, dtype=np.float32)
        local_max = maximum_filter(canopy, size=min_distance * 2 + 1)
        peaks_mask = (canopy == local_max) & (canopy > threshold_abs)
        coords = np.argwhere(peaks_mask)
        return coords

    canopy = np.asarray(canopy, dtype=np.float32)
    coords = peak_local_max(
        canopy, min_distance=min_distance, threshold_abs=threshold_abs,
        exclude_border=False,
    )
    return coords


def watershed_segment(canopy: np.ndarray, peaks: np.ndarray) -> np.ndarray:
    """以 peaks 为种子做分水岭分割，返回标签图。"""
    try:
        from scipy.ndimage import label as ndlabel, distance_transform_edt
        from skimage.segmentation import watershed
    except ImportError:
        # pure scipy fallback: connected components on thresholded canopy
        from scipy.ndimage import label as ndlabel
        canopy = np.asarray(canopy, dtype=np.float32)
        binary = canopy > 0.1
        labels, _ = ndlabel(binary)
        return labels.astype(np.int32)

    canopy = np.asarray(canopy, dtype=np.float32)
    # markers from peaks
    markers = np.zeros(canopy.shape, dtype=np.int32)
    for i, (r, c) in enumerate(peaks):
        markers[r, c] = i + 1
    # gradient-like surface: invert canopy so basins are at peaks
    surface = -canopy
    labels = watershed(surface, markers=markers, mask=canopy > 0.05)
    return labels.astype(np.int32)


def count_and_stats(canopy: np.ndarray, min_distance: int = 3,
                    pixel_area_m2: float = 1.0) -> Dict[str, Any]:
    """统计株数、密度、平均冠幅。"""
    peaks = detect_peaks(canopy, min_distance=min_distance)
    n = len(peaks)
    labels = watershed_segment(canopy, peaks)
    area_px = canopy.size
    density = n / max(area_px * pixel_area_m2, 1e-9)  # plants/m2

    # mean crown area from labels
    unique = np.unique(labels)
    unique = unique[unique > 0]
    crown_areas = []
    for u in unique:
        crown_areas.append(np.sum(labels == u))
    mean_crown_px = float(np.mean(crown_areas)) if crown_areas else 0.0
    mean_vigor = float(np.nanmean(canopy[canopy > 0.05])) if np.any(canopy > 0.05) else 0.0

    return {
        "count": int(n),
        "density": float(density),
        "mean_crown_px": mean_crown_px,
        "mean_vigor": mean_vigor,
        "peaks": peaks,
        "labels": labels,
    }


def estimate_yield(density: float, mean_vigor: float, area_ha: float = 1.0,
                   a: float = 8000.0, b: float = 500.0) -> float:
    """经验产量模型：yield (kg/ha) = a * density * mean_vigor + b。"""
    if density < 0 or mean_vigor < 0:
        raise ValidationError("density and mean_vigor must be >= 0")
    return float(a * density * mean_vigor + b)


def process_canopy(canopy: np.ndarray, min_distance: int = 3,
                   pixel_area_m2: float = 1.0, area_ha: float = 1.0) -> Dict[str, Any]:
    """主流程：峰值检测 + 分水岭 + 产量估算。"""
    canopy = np.asarray(canopy, dtype=np.float32)
    if canopy.ndim != 2:
        raise ValidationError("canopy must be 2D")
    stats = count_and_stats(canopy, min_distance=min_distance, pixel_area_m2=pixel_area_m2)
    yld = estimate_yield(stats["density"], stats["mean_vigor"], area_ha=area_ha)
    stats["yield_kg_ha"] = yld
    return stats


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64,
                       n_plants: int = 25, seed: int = 42):
    """生成含 n_plants 个高斯冠层的 CHM 栅格。"""
    rng = np.random.default_rng(seed)
    canopy = np.full((height, width), 0.02, dtype=np.float32)  # bare soil baseline

    # 随机放置 n_plants 个冠层
    positions = []
    for _ in range(n_plants):
        r = rng.integers(5, height - 5)
        c = rng.integers(5, width - 5)
        positions.append((r, c))
        amp = rng.uniform(0.5, 0.9)
        sigma = rng.uniform(2.0, 3.5)
        yy, xx = np.mgrid[0:height, 0:width]
        g = amp * np.exp(-((yy - r) ** 2 + (xx - c) ** 2) / (2 * sigma ** 2))
        canopy += g.astype(np.float32)

    canopy = np.clip(canopy, 0.0, 1.0).astype(np.float32)
    info = {
        "bbox": bbox, "width": width, "height": height,
        "n_plants_true": n_plants, "positions": positions,
    }
    return canopy, info


# ---------------------------------------------------------------------------
# 输入校验：bbox（共用同 animated-map-series 模板）
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> None:
    """Validate a [W, S, E, N] bbox in WGS-84.

    Raises ValidationError (exit 6) for:
      - wrong length
      - non-finite values
      - longitude out of [-180, 180]
      - latitude  out of [-90, 90]
      - W >= E (would make a non-positive-width raster)
      - S >= N
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(
            f"bbox must have 4 floats [W S E N], got {bbox!r}",
        )
    w, s, e, n = bbox
    vals = [w, s, e, n]
    if not all(np.isfinite(vals)):
        raise ValidationError(f"bbox contains non-finite values: {vals}")
    if not (-180.0 <= w <= 180.0) or not (-180.0 <= e <= 180.0):
        raise ValidationError(
            f"longitude out of [-180, 180]: W={w}, E={e}",
        )
    if not (-90.0 <= s <= 90.0) or not (-90.0 <= n <= 90.0):
        raise ValidationError(
            f"latitude out of [-90, 90]: S={s}, N={n}",
        )
    if w >= e:
        raise ValidationError(
            f"bbox W must be < E (W={w}, E={e}); cross-180 not supported; "
            f"split into two bboxes at the dateline",
        )
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N (S={s}, N={n})",
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox extent too small (W={w}, E={e}, S={s}, N={n})",
        )


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
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
    """Read a multiband GeoTIFF, returning (cube, bbox) with NoData→NaN."""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=True).astype(np.float32)
        cube = np.ma.filled(cube, np.nan)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


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
        inputs={"input": getattr(args, "input", None), "method": getattr(args, "method", None),
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
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        canopy = cube[0] if cube.ndim == 3 else cube
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        canopy, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    # 校验（先于 makedirs）
    if canopy.size == 0:
        raise ValidationError("input raster is empty")
    if bbox is not None:
        validate_bbox(bbox)
    if not np.any(np.isfinite(canopy)):
        raise ValidationError(
            "input canopy has no valid (finite) pixels (all NoData or NaN)",
        )

    # 现在 makedirs
    os.makedirs(output_dir, exist_ok=True)

    res = process_canopy(canopy, min_distance=args.min_distance,
                         pixel_area_m2=args.pixel_area, area_ha=args.area_ha)

    # 写出冠层栅格
    canopy_tif = os.path.join(output_dir, "canopy.tif")
    write_geotiff(canopy_tif, canopy, bbox)

    # 写出分割标签
    labels_tif = os.path.join(output_dir, "plant_labels.tif")
    write_geotiff(labels_tif, res["labels"].astype(np.float32), bbox)

    # 统计 JSON
    stats_json = os.path.join(output_dir, "count_yield_stats.json")
    stats_out = {k: v for k, v in res.items() if k not in ("peaks", "labels")}
    stats_out["peaks_count"] = int(len(res["peaks"]))
    with open(stats_json, "w", encoding="utf-8") as f:
        json.dump(stats_out, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "method": args.method,
          "count": res["count"], "density": res["density"],
          "yield_kg_ha": res["yield_kg_ha"]}
    if synth_info is not None:
        qa["synthetic"] = {"n_plants_true": synth_info["n_plants_true"]}

    outputs = [
        {"path": canopy_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": labels_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_json, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] plants: {res['count']}  density: {res['density']:.4f} plants/m2")
        print(f"[{SKILL_NAME}] yield: {res['yield_kg_ha']:.1f} kg/ha")
        print(f"[{SKILL_NAME}] output: {canopy_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Crop counting via canopy peak detection and watershed, with empirical yield estimation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input canopy/CHM GeoTIFF (single band)")
    p.add_argument("--method", default="peak-watershed", choices=["peak-watershed", "peak-only"],
                   help="counting method (default: peak-watershed)")
    p.add_argument("--min-distance", type=int, default=3,
                   help="minimum distance between peaks in pixels (default: 3)")
    p.add_argument("--pixel-area", type=float, default=1.0,
                   help="pixel area in m2 (default: 1.0)")
    p.add_argument("--area-ha", type=float, default=1.0,
                   help="field area in hectares for yield scaling (default: 1.0)")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic scene (offline)")
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
