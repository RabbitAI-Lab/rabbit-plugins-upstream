#!/usr/bin/env python3
"""impervious-surface-trend — 不透水面变化趋势

对多期不透水面比例（ISA，取值 0-1）做逐像元时间趋势拟合，量化城市化强度
与方向：

- **linear**（线性）：最小二乘拟合 ISA ~ a + b·t，斜率 b（ISA/年）即年增量。
- **exponential**（指数）：拟合 ln(ISA) ~ a + b·t，斜率 b（1/年）即相对增长率，
  适合刻画低基数区域的快速扩张。

增长热点用「斜率 > 均值 + k·标准差 且斜率为正」识别，对应高速城市化区域。

数据源：本地多期 ISA GeoTIFF（``--input``）或 ``--synthetic`` 生成含注入增长
趋势的模拟场景（离线）。

隐私声明 / Privacy：
- 默认离线运行，完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python impervious-surface-trend.py --bbox 116 39 117 40 --n-dates 5 --output-dir ./out
    python impervious-surface-trend.py --bbox 116 39 117 40 --trend exponential --output-dir ./out
    python impervious-surface-trend.py --input isa_stack.tif --trend linear --output-dir ./out

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
SKILL_NAME = "impervious-surface-trend"

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


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# Input validation (P0/P1)
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate a [W, S, E, N] bbox. Raises ValidationError on bad order, range,
    zero-area, or crossing the 180° meridian.
    """
    try:
        w, s, e, n = [float(v) for v in bbox]
    except Exception:
        raise ValidationError(f"bbox must be 4 floats, got {bbox!r}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"longitude out of range [-180, 180]: W={w}, E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"latitude out of range [-90, 90]: S={s}, N={n}")
    if w >= e:
        raise ValidationError(
            f"bbox requires W < E (got W={w}, E={e}); check --bbox order")
    if s >= n:
        raise ValidationError(
            f"bbox requires S < N (got S={s}, N={n}); check --bbox order")
    if e - w > 360.0 or n - s > 180.0:
        raise ValidationError(
            f"bbox span too large (dx={e - w}, dy={n - s})")
    # Cross-180° is not supported: treat it as a hard error.
    if w > 180.0 or e > 180.0 or w < -180.0 or e < -180.0:
        raise ValidationError(
            f"bbox crosses 180° meridian; please split into two sub-bboxes")


def validate_synthetic_params(n_dates: int) -> None:
    """Validate synthetic-mode parameters. Raises ValidationError on bad input."""
    if n_dates < 2:
        raise ValidationError(
            f"--n-dates must be >= 2 to fit a trend, got {n_dates}")


def read_geotiff_with_nodata(path: str):
    """Read a multiband raster and return (data, bbox, nodata).

    data is np.float32 with shape (nb, H, W). Values equal to the source
    nodata (if any) are replaced with NaN so downstream NaN-safe ops
    ignore them.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [float(b.left), float(b.bottom), float(b.right), float(b.top)]
        nd = src.nodata
    if nd is not None:
        cube = np.where(cube == nd, np.nan, cube)
    return cube, bbox, nd


def count_valid_pixels(cube: np.ndarray) -> int:
    """Number of pixels that are finite (i.e. not NaN, not inf) across all
    bands per location, then summed over valid locations.
    """
    if cube.ndim == 3:
        valid_loc = np.all(np.isfinite(cube), axis=0)
    else:
        valid_loc = np.isfinite(cube)
    return int(valid_loc.sum())


# ---------------------------------------------------------------------------
# 核心算法：逐像元趋势拟合
# ---------------------------------------------------------------------------
def linear_trend(cube: np.ndarray, times: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """逐像元线性最小二乘拟合 y = a + b·t。

    参数
    ----
    cube  : (n_dates, H, W) — NaN locations are masked per-pixel
    times : (n_dates,)

    返回 (slope, intercept)，形状均为 (H, W)。NaN locations stay NaN.
    b = Σ(t-t̄)(y-ȳ) / Σ(t-t̄)²
    """
    cube = np.asarray(cube, dtype=np.float64)
    times = np.asarray(times, dtype=np.float64)
    if cube.shape[0] != times.size:
        raise ValidationError(
            f"cube has {cube.shape[0]} dates but times has {times.size}")
    if times.size < 2:
        raise ValidationError("need at least 2 dates to fit a trend")

    t = times - times.mean()
    denom = float((t ** 2).sum())
    if denom <= 0:
        raise ValidationError("time coordinates must not all be identical")
    # Per-pixel mask of finite (valid) observations.
    finite = np.isfinite(cube)
    n_valid = finite.sum(axis=0)
    safe = n_valid >= 2
    # Replace NaN with 0 for subtraction; they will be masked by n_valid.
    y_safe = np.where(finite, cube, 0.0)
    y_mean = y_safe.sum(axis=0) / np.where(safe, n_valid, 1)
    y = np.where(finite, cube - y_mean[np.newaxis, :, :], 0.0)
    slope = (t[:, None, None] * y).sum(axis=0) / denom
    intercept = y_mean - slope * times.mean()
    # Restore NaN where we don't have enough valid observations.
    slope = np.where(safe, slope, np.nan)
    intercept = np.where(safe, intercept, np.nan)
    return slope, intercept


def exponential_trend(
    cube: np.ndarray,
    times: np.ndarray,
    eps: float = 1e-3,
) -> Tuple[np.ndarray, np.ndarray]:
    """逐像元指数拟合 ln(y) = a + b·t，返回 (b, a)。

    b 为相对增长率（1/时间单位）。ISA 先裁剪到 [eps, 1] 再取对数，避免 log(0)。
    NaN locations are preserved as NaN in the result.
    """
    cube = np.asarray(cube, dtype=np.float64)
    nan_mask = ~np.isfinite(cube)
    logy = np.log(np.clip(np.where(nan_mask, eps, cube), eps, 1.0))
    logy = np.where(nan_mask, np.nan, logy)
    return linear_trend(logy, times)


def detect_hotspots(
    slope: np.ndarray,
    k: float = 1.0,
    positive_only: bool = True,
) -> Tuple[np.ndarray, float]:
    """识别增长热点：slope > mean + k·std（且可选 slope > 0）。

    NaN locations are ignored (they are not flagged as hotspots). If every
    pixel is NaN, returns an all-False mask with threshold 0.
    """
    slope = np.asarray(slope, dtype=np.float64)
    finite = np.isfinite(slope)
    if not finite.any():
        return np.zeros(slope.shape, dtype=bool), 0.0
    s_mean = float(np.nanmean(slope))
    s_std = float(np.nanstd(slope))
    thr = s_mean + k * s_std
    hot = (slope > thr) & finite
    if positive_only:
        hot = hot & (slope > 0)
    return hot, thr


def fit_trend(
    cube: np.ndarray,
    times: np.ndarray,
    method: str = "linear",
) -> Dict[str, Any]:
    """按 method 拟合趋势，返回斜率栅格 + 诊断。"""
    if method == "linear":
        slope, intercept = linear_trend(cube, times)
    elif method == "exponential":
        slope, intercept = exponential_trend(cube, times)
    else:
        raise UsageError(f"unknown trend method '{method}'")

    hot, thr = detect_hotspots(slope)
    # NaN-safe stats.
    finite_slope = np.isfinite(slope)
    finite_cube = np.isfinite(cube)
    if finite_slope.any():
        mean_slope = float(np.nanmean(slope))
        max_slope = float(np.nanmax(slope))
        min_slope = float(np.nanmin(slope))
        std_slope = float(np.nanstd(slope))
        pos_frac = float(np.mean(slope[finite_slope] > 0))
    else:
        mean_slope = max_slope = min_slope = std_slope = pos_frac = 0.0
    if finite_cube.any():
        mean_isa = float(np.nanmean(cube))
    else:
        mean_isa = 0.0
    n_valid_pixels = int(finite_slope.sum())
    stats = {
        "method": method,
        "n_dates": int(cube.shape[0]),
        "n_valid_pixels": n_valid_pixels,
        "mean_slope": mean_slope,
        "max_slope": max_slope,
        "min_slope": min_slope,
        "std_slope": std_slope,
        "positive_fraction": pos_frac,
        "hotspot_threshold": thr,
        "hotspot_fraction": float(np.mean(hot)),
        "mean_isa": mean_isa,
        # 年均 ISA 相对增长率（用平均 ISA 归一化，便于横向比较）
        "mean_relative_growth": (mean_slope / mean_isa
                                  if mean_isa > 1e-9 else 0.0),
    }
    return {
        "slope": slope.astype(np.float32),
        "intercept": intercept.astype(np.float32),
        "hotspots": hot.astype(np.uint8),
        "stats": stats,
    }


# ---------------------------------------------------------------------------
# 合成数据：多期 ISA，注入已知增长趋势
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    n_dates: int = 5,
    trend: str = "linear",
    width: int = 64,
    height: int = 64,
    noise_std: float = 0.003,
    seed: int = 42,
) -> Dict[str, Any]:
    """生成 (n_dates, H, W) 的 ISA 时序，含一个强增长块和一个中等增长块。

    linear:     ISA = clip(base + slope_map·t + noise, 0, 1)
    exponential: ISA = clip(base · exp(rate_map·t) + noise, 0, 1)
    强增长块 [8:24, 8:24]，中等增长块 [40:56, 40:56]，背景近似稳定。
    """
    rng = np.random.default_rng(seed)
    times = np.arange(n_dates, dtype=np.float64)

    base = rng.uniform(0.10, 0.18, size=(height, width))
    grow = np.zeros((height, width), dtype=bool)
    med = np.zeros((height, width), dtype=bool)
    grow[8:24, 8:24] = True
    med[40:56, 40:56] = True

    if trend == "linear":
        slope_map = np.full((height, width), 0.002)   # 背景微增
        slope_map[grow] = 0.05                        # 强增长
        slope_map[med] = 0.02                         # 中等增长
        injected = {"strong": 0.05, "medium": 0.02, "background": 0.002}
        cube = np.zeros((n_dates, height, width), dtype=np.float64)
        for ti, t in enumerate(times):
            cube[ti] = base + slope_map * t
    else:  # exponential
        rate_map = np.full((height, width), 0.005)
        rate_map[grow] = 0.15
        rate_map[med] = 0.06
        injected = {"strong": 0.15, "medium": 0.06, "background": 0.005}
        cube = np.zeros((n_dates, height, width), dtype=np.float64)
        for ti, t in enumerate(times):
            cube[ti] = base * np.exp(rate_map * t)

    cube += rng.normal(0.0, noise_std, size=cube.shape)
    cube = np.clip(cube, 0.0, 1.0).astype(np.float32)

    return {
        "bbox": list(bbox),
        "width": width,
        "height": height,
        "n_dates": n_dates,
        "trend": trend,
        "times": times,
        "cube": cube,
        "grow_mask": grow,
        "med_mask": med,
        "injected": injected,
    }


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
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
            "n_dates": getattr(args, "n_dates", None),
            "trend": getattr(args, "trend", None),
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
    synth_info: Optional[Dict[str, Any]] = None

    # --- Phase 1: parameter validation (no side effects) ---
    if args.input and not args.synthetic:
        cube, file_bbox, _src_nd = read_geotiff_with_nodata(args.input)
        if cube.ndim != 3 or cube.shape[0] < 2:
            raise ValidationError(
                "input raster must be a multiband (n_dates >= 2) ISA stack")
        bbox = bbox if bbox is not None else file_bbox
        times = np.arange(cube.shape[0], dtype=np.float64)
        source_note = args.input
        src_nd = _src_nd
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        validate_synthetic_params(args.n_dates)
        synth = generate_synthetic(bbox, n_dates=args.n_dates, trend=args.trend)
        cube = synth["cube"]
        times = synth["times"]
        synth_info = synth
        source_note = "synthetic"
        src_nd = None
        # In synthetic mode, validate the bbox that will be used.
        bbox = validate_and_collapse_bbox(bbox)

    if cube.size == 0:
        raise ValidationError("input data is empty")

    # Validate bbox post-decision (covers input mode too).
    validate_bbox(bbox)

    n_valid = count_valid_pixels(cube)
    if n_valid == 0:
        raise ValidationError(
            "input raster has no valid pixels (all NoData / NaN)")

    # --- Phase 2: create output dir (only after validation passes) ---
    os.makedirs(output_dir, exist_ok=True)

    res = fit_trend(cube, times, method=args.trend)
    slope = res["slope"]
    hot = res["hotspots"]
    stats = res["stats"]

    out_slope = os.path.join(output_dir, "trend_slope.tif")
    out_hot = os.path.join(output_dir, "hotspots.tif")
    # Slope / hotspots: replace NaN with -9999 for the raster nodata
    slope_to_write = np.where(np.isfinite(slope), slope, -9999.0)
    hot_to_write = np.where(np.isfinite(slope), hot, 255).astype(np.float32)
    write_geotiff(out_slope, slope_to_write, bbox)
    write_geotiff(out_hot, hot_to_write, bbox)

    stats_path = os.path.join(output_dir, "growth_statistics.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2, default=str)

    n_total = int(cube.shape[1] * cube.shape[2]) if cube.ndim >= 2 else 0
    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.trend,
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
        "input_nodata": src_nd,
        "mean_slope": stats["mean_slope"],
        "positive_fraction": stats["positive_fraction"],
        "hotspot_fraction": stats["hotspot_fraction"],
    }
    if synth_info is not None:
        grow = synth_info["grow_mask"]
        # NaN-safe averages over the synthetic block.
        grow_slope = slope[grow]
        finite_grow = np.isfinite(grow_slope)
        qa["synthetic_strong_block_mean_slope"] = (
            float(np.nanmean(grow_slope)) if finite_grow.any() else 0.0)
        qa["synthetic_injected"] = synth_info["injected"]
        qa["synthetic_hotspot_recall"] = (
            float(np.mean(hot[grow])) if grow.any() else 0.0)

    outputs = [
        {"path": out_slope, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_hot, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.trend}  dates: {stats['n_dates']}")
        print(f"[{SKILL_NAME}] mean slope: {stats['mean_slope']:.5f}  "
              f"positive: {stats['positive_fraction']:.3f}")
        print(f"[{SKILL_NAME}] hotspot fraction: {stats['hotspot_fraction']:.3f}")
        print(f"[{SKILL_NAME}] output: {out_slope}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def validate_and_collapse_bbox(bbox):
    """Helper used in synthetic mode: returns the bbox unchanged after validation."""
    validate_bbox(bbox)
    return bbox


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Per-pixel impervious surface trend (linear / exponential) and growth hotspots.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="multiband ISA fraction GeoTIFF (>= 2 bands, values 0-1)")
    p.add_argument("--n-dates", type=int, default=5, dest="n_dates",
                   help="number of time steps in synthetic mode (default: 5)")
    p.add_argument("--trend", default="linear", choices=["linear", "exponential"],
                   help="trend model (default: linear)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic ISA time series (offline)")
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
