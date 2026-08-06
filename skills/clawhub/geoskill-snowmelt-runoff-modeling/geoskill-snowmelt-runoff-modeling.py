#!/usr/bin/env python3
"""snowmelt-runoff-modeling — 融雪径流模拟

度日因子法（Degree-Day Factor, DDF）融雪径流模拟。核心公式：

    M = DDF × max(0, T − T_base)

其中 M 为日融雪量（mm/day，以水当量计），DDF 为度日因子（mm·°C⁻¹·day⁻¹），
T 为日平均气温，T_base 为融化临界温度（默认 0 °C）。气温经高程递减率
（lapse rate，默认 6 °C/km）下垫到每个像元，因此高海拔更冷、融雪更慢。

逐日循环：对每个有积雪的像元计算潜在融雪量，实际融雪受剩余积雪（SWE，雪水
当量）限制（不能融超），累积形成逐像元径流深栅格；全流域平均得逐日径流过程线，
并统计积雪面积随时间的递减曲线（snow-cover depletion curve）。

数据源：本地 DEM GeoTIFF（EPSG:4326），配合合成气温时序与初始积雪；或
``--synthetic`` 生成含高程带、春季升温过程的完整模拟数据集用于离线测试。

隐私声明 / Privacy：
- 默认完全离线运行，不发起任何网络请求。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python snowmelt-runoff-modeling.py --input dem.tif --ddf 4.0
    python snowmelt-runoff-modeling.py --bbox 116 39 117 40 --ddf 4.0 --synthetic --output-dir ./out

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
SKILL_NAME = "snowmelt-runoff-modeling"

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


def validate_bbox(bbox) -> None:
    """Validate bbox: W<E, S<N, lon in [-180,180], lat in [-90,90]."""
    if bbox is None or len(bbox) != 4:
        raise UsageError("bbox must be 4 floats: W S E N")
    w, s, e, n = [float(x) for x in bbox]
    if w >= e:
        raise ValidationError(
            f"invalid bbox: W >= E ({w} >= {e}); cross-180° bboxes not supported, "
            f"split the request into two halves")
    if s >= n:
        raise ValidationError(f"invalid bbox: S >= N ({s} >= {n})")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"invalid bbox: longitude out of [-180,180]: [{w}, {e}]")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"invalid bbox: latitude out of [-90,90]: [{s}, {n}]")
    if abs(e - w) < 1e-9 or abs(n - s) < 1e-9:
        raise ValidationError(f"invalid bbox: zero-area ({w},{s},{e},{n})")


def validate_ddf(value: float) -> float:
    """Validate --ddf > 0 (mm·°C⁻¹·day⁻¹); return float."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        raise ValidationError(f"ddf must be a number, got {value!r}")
    if v <= 0.0:
        raise ValidationError(f"ddf must be > 0 (mm per °C per day), got {v}")
    return v


def validate_n_days(value: int) -> int:
    """Validate --n-days >= 1; return int."""
    try:
        v = int(value)
    except (TypeError, ValueError):
        raise ValidationError(f"n-days must be an integer, got {value!r}")
    if v < 1:
        raise ValidationError(f"n-days must be >= 1, got {v}")
    return v


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def degree_day_melt(temp: np.ndarray, ddf: float, t_base: float = 0.0) -> np.ndarray:
    """度日因子融雪量：M = DDF × max(0, T − T_base)（mm/day）。

    temp 可为标量或数组（像元气温）。
    """
    return float(ddf) * np.maximum(0.0, np.asarray(temp, dtype=np.float64) - t_base)


def air_temp_at_elevation(
    t_ref: float, dem: np.ndarray, elev_ref: float, lapse: float = 0.006
) -> np.ndarray:
    """高程递减率下垫气温：T = T_ref − lapse × (elev − elev_ref)。

    lapse 单位 °C/m（默认 0.006 = 6 °C/km）。
    """
    return t_ref - float(lapse) * (np.asarray(dem, dtype=np.float64) - elev_ref)


def simulate_snowmelt(
    dem: np.ndarray,
    temp_series: np.ndarray,
    swe_init: np.ndarray,
    ddf: float = 4.0,
    t_base: float = 0.0,
    lapse: float = 0.006,
    elev_ref: Optional[float] = None,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """逐日度日因子融雪径流模拟。

    参数：
        dem         (H, W) 高程 (m)
        temp_series (n_days,) 参考高程日平均气温 (°C)
        swe_init    (H, W) 初始雪水当量 (mm)
        ddf         度日因子 (mm·°C⁻¹·day⁻¹)
        t_base      融化临界温度 (°C)
        lapse       气温递减率 (°C/m)
        elev_ref    参考高程（默认取 DEM 均值）

    返回 (runoff_daily, snow_area_curve, runoff_depth)：
        runoff_daily    (n_days,) 流域平均逐日径流深 (mm/day)
        snow_area_curve (n_days,) 逐日积雪面积比例 (0–1)
        runoff_depth    (H, W) 累积径流深栅格 (mm)
    """
    dem = np.asarray(dem, dtype=np.float64)
    swe_init = np.asarray(swe_init, dtype=np.float64)
    temp_series = np.asarray(temp_series, dtype=np.float64)
    if dem.ndim != 2 or swe_init.ndim != 2:
        raise ValidationError("DEM and initial SWE must be 2D arrays")
    if dem.shape != swe_init.shape:
        raise ValidationError(
            f"DEM shape {dem.shape} != SWE shape {swe_init.shape}"
        )
    if temp_series.ndim != 1:
        raise ValidationError("temp_series must be 1D")

    if elev_ref is None:
        elev_ref = float(np.nanmean(dem))

    h, w = dem.shape
    valid = np.isfinite(dem) & np.isfinite(swe_init)
    n_pix = int(np.count_nonzero(valid))
    if n_pix == 0:
        raise ValidationError("DEM has no valid pixels (all NoData)")
    # 无效像元视为无雪、无融雪（不传播 NaN）
    swe = np.clip(np.where(valid, swe_init, 0.0), 0.0, None).copy()
    swe_start = swe.copy()
    n_days = temp_series.size

    runoff_daily = np.zeros(n_days, dtype=np.float64)
    snow_area = np.zeros(n_days, dtype=np.float64)

    for t in range(n_days):
        temp_field = air_temp_at_elevation(temp_series[t], dem, elev_ref, lapse)
        potential_melt = degree_day_melt(temp_field, ddf, t_base)
        potential_melt = np.where(valid, potential_melt, 0.0)
        actual_melt = np.minimum(potential_melt, swe)  # 不能融超剩余雪量
        swe = swe - actual_melt
        runoff_daily[t] = float(np.sum(actual_melt) / n_pix)
        snow_area[t] = float(np.count_nonzero(swe > 1e-6) / n_pix)

    runoff_depth = np.where(valid, (swe_start - swe).astype(np.float32), np.nan)
    return runoff_daily, snow_area, runoff_depth


def snowmelt_stats(
    runoff_daily: np.ndarray,
    snow_area: np.ndarray,
    runoff_depth: np.ndarray,
    swe_init: np.ndarray,
) -> Dict[str, Any]:
    """汇总融雪径流统计量（对无效像元 NaN-safe）。"""
    cum = np.cumsum(runoff_daily)
    peak_day = int(np.argmax(runoff_daily)) if runoff_daily.size else 0
    swe_final = np.clip(np.asarray(swe_init, np.float64), 0, None) - runoff_depth
    return {
        "n_days": int(runoff_daily.size),
        "total_runoff_mm": float(cum[-1]) if cum.size else 0.0,
        "peak_runoff_mm_day": float(np.max(runoff_daily)) if runoff_daily.size else 0.0,
        "peak_day": peak_day,
        "initial_swe_mm_mean": float(np.nanmean(swe_init)) if swe_init.size else 0.0,
        "final_swe_mm_mean": float(np.nanmean(np.clip(swe_final, 0, None))),
        "initial_snow_area_fraction": float(snow_area[0]) if snow_area.size else 0.0,
        "final_snow_area_fraction": float(snow_area[-1]) if snow_area.size else 0.0,
        "runoff_depth_mm_mean": float(np.nanmean(runoff_depth)) if runoff_depth.size else 0.0,
    }


# ---------------------------------------------------------------------------
# 合成数据：高程带 + 春季升温 + 初始积雪（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    n_days: int = 60,
    ddf: float = 4.0,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 (dem, temp_series, swe_init, info)。

    DEM：500–3000 m 高程梯度（西北高、东南低）。
    气温：春季升温，参考高程日均温从约 −5 °C 升至 +12 °C。
    初始积雪：随高程增加（高海拔雪多，低海拔无雪）。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yy = yy.astype(np.float32) / max(height - 1, 1)
    xx = xx.astype(np.float32) / max(width - 1, 1)

    dem = 500.0 + 2500.0 * (1.0 - (0.5 * xx + 0.5 * yy))
    dem = dem + rng.normal(0, 30, size=dem.shape).astype(np.float32)
    dem = dem.astype(np.float32)

    # 春季升温（含日际波动）
    frac = np.arange(n_days, dtype=np.float64) / max(n_days - 1, 1)
    temp_series = -5.0 + 17.0 * frac + rng.normal(0, 1.5, size=n_days)

    # 初始积雪：高程 > 900 m 才有雪，随高程线性增加到 ~350 mm
    swe_init = np.clip((dem - 900.0) / 2100.0 * 350.0, 0.0, 400.0)
    swe_init = swe_init.astype(np.float32)

    info = {
        "bbox": bbox, "width": width, "height": height, "n_days": n_days,
        "dem_min": float(np.min(dem)), "dem_max": float(np.max(dem)),
        "temp_start": float(temp_series[0]), "temp_end": float(temp_series[-1]),
        "swe_init_mean": float(np.mean(swe_init)),
    }
    return dem, temp_series, swe_init, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    cube: np.ndarray,
    bbox: List[float],
    nodata: float = -9999.0,
    dtype: str = "float32",
) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype(dtype), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        data = src.read(1).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None:
        data = np.where(data == nodata, np.nan, data).astype(np.float32)
    return data, bbox


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
            "ddf": getattr(args, "ddf", None),
            "t_base": getattr(args, "t_base", None),
            "n_days": getattr(args, "n_days", None),
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

    # --- Upfront validation (BEFORE makedirs; rc=6 for bad data, rc=2 for bad CLI) ---
    if args.bbox is not None:
        validate_bbox(args.bbox)
    validate_ddf(args.ddf)
    validate_n_days(args.n_days)

    # 1) 获取 DEM + 气温 + 初始积雪
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        dem, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            validate_bbox(bbox)
        # 真实模式：合成气温时序与初始积雪（随高程）
        _, temp_series, swe_init, synth_info = generate_synthetic(
            bbox, width=dem.shape[1], height=dem.shape[0], n_days=args.n_days,
        )
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        dem, temp_series, swe_init, synth_info = generate_synthetic(
            bbox, n_days=args.n_days,
        )
        source_note = "synthetic"

    if dem.size == 0:
        raise ValidationError("input DEM is empty")
    n_total = int(dem.size)
    n_valid = int(np.count_nonzero(np.isfinite(dem)))
    if n_valid == 0:
        raise ValidationError("input DEM has no valid pixels (all NoData)")

    # 2) 融雪径流模拟
    runoff_daily, snow_area, runoff_depth = simulate_snowmelt(
        dem, temp_series, swe_init, ddf=args.ddf, t_base=args.t_base,
    )
    stats = snowmelt_stats(runoff_daily, snow_area, runoff_depth, swe_init)

    # --- Output dir (only after all upfront validation passes) ---
    os.makedirs(output_dir, exist_ok=True)

    # 3) 写出产物（NoData 像素重写为 -9999.0 哨兵）
    depth_tif = os.path.join(output_dir, "runoff_depth.tif")
    depth_out = np.where(np.isfinite(runoff_depth), runoff_depth, -9999.0).astype(np.float32)
    write_geotiff(depth_tif, depth_out, bbox)

    series_path = os.path.join(output_dir, "runoff_time_series.json")
    series = {
        "ddf": args.ddf,
        "t_base": args.t_base,
        "n_days": int(args.n_days),
        "runoff_daily_mm": [float(x) for x in runoff_daily],
        "snow_area_fraction": [float(x) for x in snow_area],
        "cumulative_runoff_mm": [float(x) for x in np.cumsum(runoff_daily)],
        "temperature_series_C": [float(x) for x in temp_series],
        "stats": stats,
    }
    with open(series_path, "w", encoding="utf-8") as f:
        json.dump(series, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "ddf": args.ddf,
        "input_nodata": -9999.0,
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
        "total_runoff_mm": stats["total_runoff_mm"],
        "peak_runoff_mm_day": stats["peak_runoff_mm_day"],
        "peak_day": stats["peak_day"],
        "initial_snow_area_fraction": stats["initial_snow_area_fraction"],
        "final_snow_area_fraction": stats["final_snow_area_fraction"],
    }
    if synth_info is not None:
        qa["synthetic_dem_max"] = synth_info["dem_max"]

    outputs = [
        {"path": depth_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": series_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  DDF: {args.ddf}")
        print(f"[{SKILL_NAME}] total runoff: {stats['total_runoff_mm']:.1f} mm  peak: {stats['peak_runoff_mm_day']:.2f} mm/day @ day {stats['peak_day']}")
        print(f"[{SKILL_NAME}] snow area: {stats['initial_snow_area_fraction']*100:.1f}% → {stats['final_snow_area_fraction']*100:.1f}%")
        print(f"[{SKILL_NAME}] runoff depth raster: {depth_tif}")
        print(f"[{SKILL_NAME}] time series: {series_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Degree-day-factor snowmelt runoff modeling with snow-cover depletion.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input DEM GeoTIFF (EPSG:4326)")
    p.add_argument("--ddf", type=float, default=4.0,
                   help="degree-day factor in mm/°C/day (default: 4.0)")
    p.add_argument("--t-base", type=float, default=0.0,
                   help="melt threshold temperature in °C (default: 0.0)")
    p.add_argument("--n-days", type=int, default=60,
                   help="number of simulation days (default: 60)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic dataset (offline)")
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
