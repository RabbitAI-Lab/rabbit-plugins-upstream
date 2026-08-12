#!/usr/bin/env python3
"""lake-area-change — 湖泊面积变化

基于多时相多光谱影像的水体指数（NDWI / MNDWI）阈值法提取湖泊水体，重建湖泊
面积时间序列，并用线性拟合量化面积变化趋势：

- **NDWI**（McFeeters 1996）= (Green − NIR) / (Green + NIR)
- **MNDWI**（Xu 2006）= (Green − SWIR) / (Green + SWIR)，对建筑 / 裸地更鲁棒
- **水体提取**：指数 ≥ 阈值的像元判为水体。
- **面积时序**：每期水体像元数 × 像元面积。
- **趋势分析**：对面积时序做一元线性拟合，斜率 + 相对变化率判定萎缩 / 扩张 / 稳定。

数据源：本地多时相水体指数栅格（每波段一期），或 ``--synthetic`` 生成面积随时
间单调变化（萎缩 / 扩张 / 稳定）的模拟湖泊用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python lake-area-change.py --input ndwi_stack.tif --output-dir ./out
    python lake-area-change.py --bbox 116 39 117 40 --n-dates 5 --synthetic --output-dir ./out

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
SKILL_NAME = "lake-area-change"

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


def validate_threshold(threshold: float) -> None:
    """NDWI/MNDWI threshold should be in [-1, 1]."""
    if not np.isfinite(threshold):
        raise ValidationError(f"--threshold must be finite, got {threshold}")
    if threshold < -1.0 or threshold > 1.0:
        raise ValidationError(
            f"--threshold must be in [-1, 1] (NDWI range); got {threshold}")


def read_geotiff_with_nodata(path: str):
    """Read multiband GeoTIFF, replacing NoData with NaN; return (cube, bbox, valid_mask, nodata)."""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nd = src.nodata
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    valid_mask = None
    if nd is not None:
        try:
            nd_finite = np.isfinite(float(nd))
        except (TypeError, ValueError):
            nd_finite = False
        if nd_finite:
            valid_mask = cube != float(nd)
        else:
            valid_mask = np.ones(cube.shape, dtype=bool)
    else:
        valid_mask = np.isfinite(cube)
    cube = np.where(valid_mask, cube, np.nan).astype(np.float32)
    return cube, bbox, valid_mask

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


# 趋势判定的相对变化率阈值（%/期）
TREND_EPS_PCT = 1.0


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def compute_index(green: np.ndarray, other: np.ndarray) -> np.ndarray:
    """归一化差值水体指数通式：(green − other) / (green + other)。

    NDWI 传 other=NIR，MNDWI 传 other=SWIR。分母近 0 处返回 0。
    """
    green = np.asarray(green, dtype=np.float64)
    other = np.asarray(other, dtype=np.float64)
    denom = green + other
    out = np.zeros_like(green, dtype=np.float64)
    valid = np.abs(denom) > 1e-6
    out[valid] = (green[valid] - other[valid]) / denom[valid]
    return np.clip(out, -1.0, 1.0)


def extract_water(index: np.ndarray, threshold: float = 0.0) -> np.ndarray:
    """阈值法水体掩膜：index ≥ threshold 为水体。"""
    index = np.asarray(index, dtype=np.float64)
    return index >= threshold


def lake_area_km2(mask: np.ndarray, cell_area_m2: float) -> float:
    """水体像元数 × 像元面积 → 湖泊面积（km²）。"""
    return float(np.count_nonzero(mask)) * float(cell_area_m2) / 1e6


def fit_trend(
    areas: np.ndarray, times: Optional[np.ndarray] = None
) -> Dict[str, Any]:
    """对面积时序做一元线性拟合，返回斜率、截距、R²、相对变化率与趋势类别。"""
    areas = np.asarray(areas, dtype=np.float64)
    n = areas.size
    if n < 2:
        raise UsageError("at least 2 dates are required for a trend fit", n=int(n))
    if times is None:
        times = np.arange(n, dtype=np.float64)
    times = np.asarray(times, dtype=np.float64)
    slope, intercept = np.polyfit(times, areas, 1)
    pred = slope * times + intercept
    ss_res = float(np.sum((areas - pred) ** 2))
    ss_tot = float(np.sum((areas - areas.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 1e-12 else 1.0
    mean_area = float(areas.mean())
    pct_per_step = 100.0 * slope / mean_area if mean_area > 1e-9 else 0.0
    if pct_per_step < -TREND_EPS_PCT:
        trend = "shrinking"
    elif pct_per_step > TREND_EPS_PCT:
        trend = "expanding"
    else:
        trend = "stable"
    total_change_pct = 100.0 * (areas[-1] - areas[0]) / areas[0] if areas[0] > 1e-9 else 0.0
    return {
        "slope_per_step": round(float(slope), 6),
        "intercept": round(float(intercept), 6),
        "r_squared": round(float(r2), 4),
        "mean_area_km2": round(mean_area, 6),
        "pct_change_per_step": round(float(pct_per_step), 4),
        "total_change_pct": round(float(total_change_pct), 4),
        "trend": trend,
    }


def polygonize_water(
    mask: np.ndarray, bbox: List[float], date_index: int, area_km2: float
) -> List[Dict[str, Any]]:
    """把单期水体掩膜矢量化为 GeoJSON feature（可能多个多边形）。"""
    from rasterio.features import shapes
    from rasterio.transform import from_bounds

    mask = np.asarray(mask)
    h, w = mask.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    mask_u8 = mask.astype(np.uint8)
    feats: List[Dict[str, Any]] = []
    for geom, val in shapes(mask_u8, mask=mask_u8.astype(bool), transform=transform):
        feats.append({
            "type": "Feature",
            "geometry": geom,
            "properties": {
                "date_index": int(date_index),
                "area_km2": round(float(area_km2), 6),
            },
        })
    return feats


# ---------------------------------------------------------------------------
# 合成数据：面积随时间单调变化的模拟湖泊（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    n_dates: int = 5,
    width: int = 96,
    height: int = 96,
    trend: str = "shrinking",
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成多时相 NDWI/MNDWI 水体指数立方体（n_dates, H, W）。

    湖泊为中部椭圆，面积按 trend 随时间线性缩放（shrinking 缩到一半，
    expanding 扩到 1.5 倍，stable 不变）。返回 (index_cube, info)。
    """
    if n_dates < 2:
        raise UsageError("--n-dates must be >= 2", n_dates=int(n_dates))
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yn = yy.astype(np.float64) / max(height - 1, 1)
    xn = xx.astype(np.float64) / max(width - 1, 1)

    cx, cy = 0.5, 0.5
    a0, b0 = 0.18, 0.22  # 初始椭圆半轴（归一化）
    if trend == "shrinking":
        factors = np.linspace(1.0, 0.5, n_dates)
    elif trend == "expanding":
        factors = np.linspace(1.0, 1.5, n_dates)
    elif trend == "stable":
        factors = np.ones(n_dates)
    else:
        raise UsageError(f"unknown trend '{trend}'", trend=trend)

    # 地物反射率（绿 / 近红外 / 短波）
    green_land, green_water = 0.10, 0.06
    nir_land, nir_water = 0.42, 0.015
    swir_land, swir_water = 0.22, 0.010

    cube = np.zeros((n_dates, height, width), dtype=np.float32)
    true_areas_km2: List[float] = []

    lat0 = 0.5 * (bbox[1] + bbox[3])
    dx = (bbox[2] - bbox[0]) * 111320.0 * np.cos(np.deg2rad(lat0)) / width
    dy = (bbox[3] - bbox[1]) * 110540.0 / height
    cell_area_m2 = float(dx * dy)

    for i, f in enumerate(factors):
        a, b = a0 * f, b0 * f
        dist = ((xn - cx) / a) ** 2 + ((yn - cy) / b) ** 2
        water = dist < 1.0
        green = np.where(water, green_water, green_land) + rng.normal(0, 0.008, (height, width))
        nir = np.where(water, nir_water, nir_land) + rng.normal(0, 0.01, (height, width))
        green = np.clip(green, 0.001, None)
        nir = np.clip(nir, 0.001, None)
        idx = compute_index(green, nir)  # NDWI
        cube[i] = idx.astype(np.float32)
        true_areas_km2.append(lake_area_km2(extract_water(idx, 0.0), cell_area_m2))

    info = {
        "bbox": bbox, "width": width, "height": height, "n_dates": n_dates,
        "trend": trend, "cell_area_m2": cell_area_m2,
        "factors": [round(float(x), 4) for x in factors],
        "true_areas_km2": [round(x, 6) for x in true_areas_km2],
    }
    return cube, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0
) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if array.ndim == 2:
        array = array[np.newaxis, ...]
    nb, h, w = array.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(array[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], float]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        h, w = cube.shape[-2], cube.shape[-1]
        lat0 = 0.5 * (b.bottom + b.top)
        dx = (b.right - b.left) * 111320.0 * np.cos(np.deg2rad(lat0)) / w
        dy = (b.top - b.bottom) * 110540.0 / h
        cell_area_m2 = float(dx * dy)
        nd = src.nodata
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    # NaN out NoData so downstream NaN-safe stats are used
    if nd is not None and np.isfinite(float(nd)):
        cube = np.where(cube == float(nd), np.nan, cube).astype(np.float32)
    return cube, bbox, cell_area_m2


# ---------------------------------------------------------------------------
# 主管线
# ---------------------------------------------------------------------------
def run_model(
    index_cube: np.ndarray, cell_area_m2: float, bbox: List[float],
    threshold: float = 0.0,
) -> Dict[str, Any]:
    """逐期提取水体 → 面积时序 → 趋势拟合 → 边界矢量化。"""
    index_cube = np.asarray(index_cube, dtype=np.float64)
    if index_cube.ndim == 2:
        index_cube = index_cube[np.newaxis, ...]
    n_dates = index_cube.shape[0]
    if n_dates < 2:
        raise UsageError("at least 2 dates (bands) are required", n_dates=int(n_dates))

    areas: List[float] = []
    feats: List[Dict[str, Any]] = []
    water_fracs: List[float] = []
    n_valid_total = 0
    for i in range(n_dates):
        idx = index_cube[i]
        finite = np.isfinite(idx)
        n_valid = int(finite.sum())
        if n_valid == 0:
            raise ValidationError(
                f"date {i} has no valid pixels (all NoData/NaN)")
        n_valid_total += n_valid
        # Treat NaN as not water
        idx_safe = np.where(finite, idx, -np.inf)
        mask = extract_water(idx_safe, threshold)
        area = lake_area_km2(mask, cell_area_m2)
        areas.append(area)
        water_fracs.append(float(mask.sum()) / n_valid)
        # Vectorize only the valid portion (NaN cells are not water)
        feats.extend(polygonize_water(mask, bbox, date_index=i, area_km2=area))

    trend = fit_trend(np.array(areas))
    return {
        "n_dates": n_dates,
        "threshold": float(threshold),
        "cell_area_m2": cell_area_m2,
        "areas_km2": [round(a, 6) for a in areas],
        "water_fraction": [round(x, 6) for x in water_fracs],
        "trend": trend,
        "features": feats,
        "n_valid_pixels_total": n_valid_total,
    }


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
            "bbox": bbox,
            "synthetic": bool(getattr(args, "synthetic", False)),
            "n_dates": getattr(args, "n_dates", None),
            "index_method": getattr(args, "index_method", None),
            "threshold": getattr(args, "threshold", None),
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
    validate_threshold(args.threshold)
    if args.n_dates is not None and args.n_dates < 2:
        raise ValidationError(
            f"--n-dates must be >= 2 for trend analysis, got {args.n_dates}")
    if args.width is not None and args.width < 1:
        raise ValidationError(f"--width must be >= 1, got {args.width}")
    if args.height is not None and args.height < 1:
        raise ValidationError(f"--height must be >= 1, got {args.height}")

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox, cell_area_m2 = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        index_cube = cube
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        index_cube, synth_info = generate_synthetic(
            bbox, n_dates=args.n_dates, width=args.width, height=args.height,
            trend=args.trend,
        )
        cell_area_m2 = synth_info["cell_area_m2"]
        source_note = "synthetic"

    if bbox is not None:
        try:
            validate_bbox(bbox)
        except ValidationError:
            if args.input and not args.synthetic:
                pass
            else:
                raise

    if index_cube.size == 0:
        raise ValidationError("input raster is empty")
    # Reject if no band has any valid pixel
    if not np.any(np.isfinite(index_cube)):
        raise ValidationError(
            "input raster has no valid pixels (entirely NoData/NaN)")

    os.makedirs(output_dir, exist_ok=True)

    try:
        result = run_model(index_cube, cell_area_m2, bbox, threshold=args.threshold)
    except GeoSkillError:
        raise
    except Exception as exc:  # noqa: BLE001
        raise ProcessError(f"lake area change analysis failed: {exc}") from exc

    # 写出产物
    out_tif = os.path.join(output_dir, "water_index.tif")
    write_geotiff(out_tif, index_cube, bbox)

    boundaries_geojson = os.path.join(output_dir, "lake_boundaries.geojson")
    with open(boundaries_geojson, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": result["features"]},
                  f, ensure_ascii=False, indent=2)

    timeseries_path = os.path.join(output_dir, "area_timeseries.json")
    timeseries_payload = {
        "n_dates": result["n_dates"],
        "threshold": result["threshold"],
        "index_method": args.index_method,
        "cell_area_m2": result["cell_area_m2"],
        "date_index": list(range(result["n_dates"])),
        "areas_km2": result["areas_km2"],
        "water_fraction": result["water_fraction"],
        "trend": result["trend"],
    }
    with open(timeseries_path, "w", encoding="utf-8") as f:
        json.dump(timeseries_payload, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_dates": result["n_dates"],
        "index_method": args.index_method,
        "areas_km2": result["areas_km2"],
        "trend": result["trend"]["trend"],
        "slope_per_step": result["trend"]["slope_per_step"],
        "total_change_pct": result["trend"]["total_change_pct"],
        "r_squared": result["trend"]["r_squared"],
        "n_boundary_features": len(result["features"]),
        "n_valid_pixels_total": result.get("n_valid_pixels_total", 0),
    }
    if synth_info is not None:
        qa["synthetic_true_trend"] = synth_info["trend"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(index_cube.shape[0])},
        {"path": boundaries_geojson, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": len(result["features"])},
        {"path": timeseries_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  index: {args.index_method}")
        print(f"[{SKILL_NAME}] dates: {result['n_dates']}  threshold: {args.threshold}")
        print(f"[{SKILL_NAME}] areas (km²): {[round(a,3) for a in result['areas_km2']]}")
        print(f"[{SKILL_NAME}] trend: {result['trend']['trend']}  "
              f"slope={result['trend']['slope_per_step']:.4f} km²/step  "
              f"total={result['trend']['total_change_pct']:.1f}%  R²={result['trend']['r_squared']:.3f}")
        print(f"[{SKILL_NAME}] output: {boundaries_geojson}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Multi-temporal NDWI/MNDWI lake water extraction, area time series and trend analysis.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="multi-band GeoTIFF, one water-index band per date")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic multi-temporal lake scene (offline)")
    p.add_argument("--width", type=int, default=96, help="synthetic raster width (default 96)")
    p.add_argument("--height", type=int, default=96, help="synthetic raster height (default 96)")
    p.add_argument("--n-dates", type=int, default=5,
                   help="number of synthetic dates (default 5)")
    p.add_argument("--index-method", default="ndwi", choices=["ndwi", "mndwi"],
                   help="water index method (default ndwi)")
    p.add_argument("--threshold", type=float, default=0.0,
                   help="water index threshold (default 0.0)")
    p.add_argument("--trend", default="shrinking",
                   choices=["shrinking", "expanding", "stable"],
                   help="synthetic lake trend (default shrinking)")
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
