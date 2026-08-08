#!/usr/bin/env python3
"""farmland-productivity — 农田生产力评估

基于 NDVI 时序积分估算累积生物量（生长季内 NDVI 对时间的积分正比于光合累积），
叠加气候校正因子（降水/温度距平）得到相对生产力指数。

核心算法
--------
- **NDVI 时序积分**：梯形法对生长季 NDVI 积分，得到累积植被指数（∝ 生物量）。
- **气候校正**：用降水/温度距平构造乘性校正因子（≈1 表示常年）。
- **生产力指数**：PI = 积分 × 气候因子，再对参考值归一到 [0,1]。

数据源：本地 NDVI 时序栅格（多波段=多时相）或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线，``--synthetic`` 完全无网络，本地处理不上传。

Usage:
    python farmland-productivity.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "farmland-productivity"

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
# Input validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate a [W, S, E, N] geographic bbox.

    Raises ValidationError (exit 6) on:
      - non-finite values
      - longitude/latitude out of range
      - W >= E (no antimeridian wrap-around)
      - S >= N
      - zero-area bbox
    """
    w, s, e, n = bbox
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError(
            f"bbox contains non-finite values: W={w} S={s} E={e} N={n}",
            bbox=list(bbox),
        )
    if abs(w) > 180.0 or abs(e) > 180.0:
        raise ValidationError(
            f"bbox longitude out of range: W={w} E={e} (must be in [-180, 180])",
            bbox=list(bbox),
        )
    if abs(s) > 90.0 or abs(n) > 90.0:
        raise ValidationError(
            f"bbox latitude out of range: S={s} N={n} (must be in [-90, 90])",
            bbox=list(bbox),
        )
    if w >= e:
        raise ValidationError(
            f"bbox reversed: W ({w}) must be < E ({e}). "
            f"For antimeridian-crossing bboxes, split into W..180 and -180..E.",
            bbox=list(bbox),
        )
    if s >= n:
        raise ValidationError(
            f"bbox reversed: S ({s}) must be < N ({n})", bbox=list(bbox)
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero area: W={w} S={s} E={e} N={n}", bbox=list(bbox)
        )


def read_geotiff_with_nodata(path: str):
    """Read a multi-band GeoTIFF, replacing NoData with NaN.

    Returns (cube_float32, bbox_WSEN, n_valid_pixel_steps).
    """
    cube, bbox = read_geotiff(path)
    import rasterio
    with rasterio.open(path) as src:
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == nodata, np.nan, cube).astype(np.float32)
    n_valid = int(np.sum(np.isfinite(cube)))
    return cube, bbox, n_valid


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def ndvi_integral(ndvi_series: np.ndarray, dt_days: float = 16.0) -> np.ndarray:
    """对 (T, H, W) NDVI 时序沿时间轴做梯形积分，返回 (H, W) 累积量。

    单位：NDVI·day，正比于生长季累积光合生物量。
    """
    ndvi_series = np.asarray(ndvi_series, dtype=np.float32)
    if ndvi_series.ndim != 3:
        raise ValidationError("ndvi_series must be (T, H, W)")
    if ndvi_series.shape[0] < 2:
        raise ValidationError("need >=2 time steps for integration")
    if dt_days <= 0:
        raise ValidationError("dt_days must be > 0")
    # NaN-safe trapezoidal integration along time axis. np.trapz is
    # available in numpy 1.x; np.trapezoid is numpy 2.0+ only.
    if hasattr(np, "trapezoid"):
        integ = np.trapezoid(ndvi_series, dx=dt_days, axis=0)
    else:
        integ = np.trapz(ndvi_series, dx=dt_days, axis=0)
    return integ.astype(np.float32)


def climate_correction_factor(precip_anomaly_pct: float, temp_anomaly_c: float,
                              precip_sensitivity: float = 0.004,
                              temp_sensitivity: float = 0.03) -> float:
    """气候校正乘性因子：正降水距平增产，正温度距平（热胁迫）减产。

    factor = 1 + precip_sensitivity*precip_pct − temp_sensitivity*temp_c，
    裁剪到 [0.5, 1.5] 避免极端值。
    """
    f = 1.0 + precip_sensitivity * float(precip_anomaly_pct) - temp_sensitivity * float(temp_anomaly_c)
    return float(np.clip(f, 0.5, 1.5))


def productivity_index(integral: np.ndarray, climate_factor: float = 1.0,
                       ref_integral: Optional[float] = None) -> np.ndarray:
    """生产力指数 PI = integral × climate_factor，按参考积分归一到 [0,1]。"""
    integral = np.asarray(integral, dtype=np.float32)
    if climate_factor <= 0:
        raise ValidationError("climate_factor must be > 0")
    scaled = integral * climate_factor
    if ref_integral is None:
        ref = float(np.nanpercentile(scaled, 95)) if scaled.size else 1.0
        ref = max(ref, 1e-6)
    else:
        if ref_integral <= 0:
            raise ValidationError("ref_integral must be > 0")
        ref = float(ref_integral)
    pi = scaled / ref
    return np.clip(pi, 0.0, 1.0).astype(np.float32)


def grade_productivity(pi: np.ndarray) -> np.ndarray:
    """生产力分级：0=低, 1=中低, 2=中高, 3=高。"""
    pi = np.asarray(pi, dtype=np.float32)
    out = np.zeros(pi.shape, dtype=np.int32)
    out[pi >= 0.4] = 1
    out[pi >= 0.6] = 2
    out[pi >= 0.8] = 3
    return out


def assess_productivity(ndvi_series: np.ndarray, dt_days: float = 16.0,
                        precip_anomaly_pct: float = 0.0,
                        temp_anomaly_c: float = 0.0) -> Dict[str, Any]:
    """主流程：积分 → 气候校正 → 生产力指数与分级。"""
    integral = ndvi_integral(ndvi_series, dt_days)
    cf = climate_correction_factor(precip_anomaly_pct, temp_anomaly_c)
    pi = productivity_index(integral, climate_factor=cf)
    grade = grade_productivity(pi)
    return {
        "integral": integral,
        "climate_factor": cf,
        "productivity_index": pi,
        "grade": grade,
        "stats": {
            "mean_integral": float(np.nanmean(integral)),
            "climate_factor": float(cf),
            "mean_pi": float(np.nanmean(pi)),
            "grade_hist": {str(i): int(np.sum(grade == i)) for i in range(4)},
        },
    }


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 32, height: int = 32,
                       n_steps: int = 12, seed: int = 42):
    """生成 (T, H, W) NDVI 时序：左侧高产（高振幅物候），右侧低产。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1)
    # 生长季物候曲线（高斯型）
    t = np.linspace(0, 1, n_steps)
    phenology = np.exp(-((t - 0.5) ** 2) / (2 * 0.15 ** 2))  # (T,)
    # 空间振幅：左高右低
    amplitude = (0.85 - 0.55 * xx)[np.newaxis, :, :]  # (1,H,W)
    base = 0.12
    series = base + amplitude * phenology[:, np.newaxis, np.newaxis]
    series = series + rng.normal(0, 0.02, series.shape)
    series = np.clip(series, 0.0, 1.0).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height, "n_steps": n_steps,
            "dt_days": 16.0, "phenology": "gaussian"}
    return series, info


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
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None), "method": getattr(args, "method", None),
                "dt_days": getattr(args, "dt_days", None), "synthetic": bool(getattr(args, "synthetic", False))},
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
    if bbox is not None:
        validate_bbox(bbox)
    if args.dt_days is not None and args.dt_days <= 0:
        raise ValidationError(
            f"--dt-days must be > 0, got {args.dt_days}", dt_days=args.dt_days
        )

    synth_info: Optional[Dict[str, Any]] = None
    n_valid = 0
    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input raster not found: {args.input}", path=args.input)
        cube, file_bbox, n_valid = read_geotiff_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        validate_bbox(bbox)
        series = cube
        dt_days = args.dt_days
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        series, synth_info = generate_synthetic(bbox)
        dt_days = synth_info["dt_days"]
        source_note = "synthetic"
        n_valid = int(np.sum(np.isfinite(series)))

    if series.size == 0:
        raise ValidationError("input raster is empty")
    if series.ndim != 3 or series.shape[0] < 2:
        raise ValidationError("input needs >=2 bands as an NDVI time series")
    if n_valid == 0:
        raise ValidationError(
            "input raster has no valid (non-NoData) pixel steps",
            shape=tuple(series.shape),
        )

    res = assess_productivity(series, dt_days=dt_days,
                              precip_anomaly_pct=args.precip_anomaly,
                              temp_anomaly_c=args.temp_anomaly)

    # Only create output dir after all validations have passed
    os.makedirs(output_dir, exist_ok=True)

    pi_tif = os.path.join(output_dir, "productivity_index.tif")
    write_geotiff(pi_tif, res["productivity_index"], bbox)
    integral_tif = os.path.join(output_dir, "ndvi_integral.tif")
    write_geotiff(integral_tif, res["integral"], bbox)
    grade_tif = os.path.join(output_dir, "productivity_grade.tif")
    write_geotiff(grade_tif, res["grade"].astype(np.float32), bbox)

    n_total_pixel_steps = int(series.shape[0] * series.shape[1] * series.shape[2])
    qa = {
        "source": source_note, "method": args.method, "mean_pi": res["stats"]["mean_pi"],
        "mean_integral": res["stats"]["mean_integral"], "climate_factor": res["stats"]["climate_factor"],
        "grade_hist": res["stats"]["grade_hist"],
        "n_valid_pixel_steps": n_valid, "n_total_pixel_steps": n_total_pixel_steps,
    }
    if synth_info is not None:
        qa["synthetic"] = {k: v for k, v in synth_info.items() if k != "bbox"}

    outputs = [
        {"path": pi_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": integral_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": grade_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean integral: {qa['mean_integral']:.2f} NDVI·day")
        print(f"[{SKILL_NAME}] climate factor: {qa['climate_factor']:.3f}  mean PI: {qa['mean_pi']:.4f}")
        print(f"[{SKILL_NAME}] output: {pi_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Farmland productivity from NDVI time-series integration with climate correction.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input NDVI time-series GeoTIFF (bands = time steps)")
    p.add_argument("--method", default="integral", choices=["integral", "climate-corrected"],
                   help="productivity method (default: integral)")
    p.add_argument("--dt-days", dest="dt_days", type=float, default=16.0,
                   help="time step in days between bands (default: 16)")
    p.add_argument("--precip-anomaly", dest="precip_anomaly", type=float, default=0.0,
                   help="precipitation anomaly percent vs normal (default: 0)")
    p.add_argument("--temp-anomaly", dest="temp_anomaly", type=float, default=0.0,
                   help="temperature anomaly in Celsius vs normal (default: 0)")
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
