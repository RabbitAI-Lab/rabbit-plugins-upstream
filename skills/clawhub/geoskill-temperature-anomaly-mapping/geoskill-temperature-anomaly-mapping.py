#!/usr/bin/env python3
"""temperature-anomaly-mapping — 温度异常制图

计算**温度距平**（anomaly）并制图：

- **距平** = 当期温度 − 气候态（多年同期均值）。按季节相位（如月份）把
  时间序列分组，组内多年平均即该相位的气候态（climatology）。
- **标准化距平** = 距平 / 同期标准差，消除量纲、可比对不同季节/区域的异常强度。
- **异常等级**：按标准化距平阈值划分 严重暖异常 / 暖异常 / 正常 / 冷异常 /
  严重冷异常（±1σ、±2σ 分界），输出整数编码等级栅格。

数据源：本地多期 GeoTIFF（每波段 = 一个时间步，按年×月排列），或
``--synthetic`` 生成含气候态 + 注入暖异常的模拟温度序列用于离线验证。

隐私声明 / Privacy：
- 默认完全离线运行，``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python temperature-anomaly-mapping.py --bbox 116 39 117 40 --n-dates 12 --n-years 5
    python temperature-anomaly-mapping.py --input temp_monthly.tif --n-dates 12

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
SKILL_NAME = "temperature-anomaly-mapping"

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


# 异常等级编码（整数）与名称
ANOMALY_CLASSES: Dict[int, str] = {
    2: "extreme_warm",
    1: "warm",
    0: "normal",
    -1: "cold",
    -2: "extreme_cold",
}


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# Input validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Any) -> None:
    """Validate a W,S,E,N geographic bbox. Raises ValidationError on bad input."""
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            f"bbox must be [W,S,E,N] (4 floats), got {bbox!r}",
            bbox=list(bbox) if hasattr(bbox, "__iter__") else None,
        )
    W, S, E, N = bbox
    for v, name in [(W, "W"), (S, "S"), (E, "E"), (N, "N")]:
        try:
            fv = float(v)
        except (TypeError, ValueError):
            raise ValidationError(
                f"bbox {name}={v!r} is not a finite number", bbox=list(bbox),
            )
        if not np.isfinite(fv):
            raise ValidationError(
                f"bbox {name}={v!r} is not a finite number", bbox=list(bbox),
            )
    if not (-180.0 <= float(W) <= 180.0 and -180.0 <= float(E) <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range [-180,180]: W={W}, E={E}", bbox=list(bbox),
        )
    if not (-90.0 <= float(S) <= 90.0 and -90.0 <= float(N) <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range [-90,90]: S={S}, N={N}", bbox=list(bbox),
        )
    if float(W) >= float(E) and not (float(W) > 170.0 and float(E) < -170.0):
        raise ValidationError(
            f"bbox has W >= E ({W} >= {E}); crossing the antimeridian "
            f"(W near +180, E near -180) is not supported. "
            f"Pass a bbox with W < E (e.g. split into two bboxes).",
            bbox=list(bbox),
        )
    if float(W) > 170.0 and float(E) < -170.0:
        raise ValidationError(
            f"bbox crosses the antimeridian (W={W}, E={E}); not supported. "
            f"Split into two bboxes: [{W}, {S}, 180.0, {N}] and [-180.0, {S}, {E}, {N}].",
            bbox=list(bbox),
        )
    if float(S) >= float(N):
        raise ValidationError(
            f"bbox has S >= N ({S} >= {N}); south must be strictly less than north.",
            bbox=list(bbox),
        )
    if (float(E) - float(W)) < 1e-4 or (float(N) - float(S)) < 1e-4:
        raise ValidationError(
            f"bbox is too small (extent < 1e-4 degrees): W={W},S={S},E={E},N={N}.",
            bbox=list(bbox),
        )


def validate_params(n_dates: int, n_years: int) -> None:
    """Cross-check CLI params beyond argparse type coercion."""
    if not isinstance(n_dates, int) or n_dates < 1:
        raise ValidationError(
            f"n-dates must be a positive int (>= 1), got {n_dates!r}", n_dates=n_dates,
        )
    if n_dates > 366:
        raise ValidationError(
            f"n-dates {n_dates} implausibly large (max 366 = daily)", n_dates=n_dates,
        )
    if not isinstance(n_years, int) or n_years < 1:
        raise ValidationError(
            f"n-years must be a positive int (>= 1), got {n_years!r}", n_years=n_years,
        )
    if n_years > 200:
        raise ValidationError(
            f"n-years {n_years} implausibly large (max 200)", n_years=n_years,
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def compute_climatology(cube: np.ndarray, period: int) -> np.ndarray:
    """逐相位（季节）气候态：把时间维按 k %% period 分组，组内多年平均。

    返回与 cube 同形状的 (n, H, W) 气候态立方体，clim[k] = 相位 k%%period 的
    逐像元多年平均。period<=1 或 period>=n 时退化为整段时间均值。
    """
    if cube.ndim != 3:
        raise ValidationError(
            f"cube must be 3-D (n, H, W), got {cube.shape}", shape=tuple(cube.shape))
    n = cube.shape[0]
    if period < 1:
        raise ValidationError(f"period must be >= 1, got {period}", period=int(period))
    clim = np.zeros_like(cube, dtype=np.float32)
    if period >= n:
        mean_all = cube.mean(axis=0)
        for k in range(n):
            clim[k] = mean_all
        return clim
    for phase in range(period):
        idx = np.arange(phase, n, period)
        phase_mean = cube[idx].mean(axis=0)
        for k in idx:
            clim[k] = phase_mean
    return clim


def anomaly_cube(cube: np.ndarray, period: int) -> Tuple[np.ndarray, np.ndarray]:
    """距平 = 当期 − 气候态。返回 (anomaly, climatology)，均 (n, H, W)。"""
    clim = compute_climatology(cube, period)
    return (cube - clim).astype(np.float32), clim


def standardized_anomaly(
    cube: np.ndarray, period: int, eps: float = 1e-6
) -> np.ndarray:
    """标准化距平：逐相位距平除以该相位多年标准差（带 eps 下限）。"""
    if cube.ndim != 3:
        raise ValidationError(
            f"cube must be 3-D (n, H, W), got {cube.shape}", shape=tuple(cube.shape))
    n = cube.shape[0]
    anom, _ = anomaly_cube(cube, period)
    z = np.zeros_like(anom)
    if period >= n:
        std = cube.std(axis=0)
        z = anom / np.maximum(std, eps)
        return z.astype(np.float32)
    for phase in range(period):
        idx = np.arange(phase, n, period)
        if idx.size < 2:
            std = np.full(cube.shape[1:], eps, dtype=np.float32)
        else:
            std = cube[idx].std(axis=0)
        z[idx] = anom[idx] / np.maximum(std, eps)[None, :, :]
    return z.astype(np.float32)


def classify_anomaly(
    z: np.ndarray, sigma1: float = 1.0, sigma2: float = 2.0
) -> np.ndarray:
    """按标准化距平阈值划分异常等级，返回整数编码栅格。

    编码：2=严重暖异常(z≥σ2), 1=暖异常(σ1≤z<σ2), 0=正常,
    -1=冷异常, -2=严重冷异常(z≤-σ2)。输入可为任意形状。
    """
    z = np.asarray(z, dtype=np.float32)
    cls = np.zeros(z.shape, dtype=np.int16)
    cls[z >= sigma2] = 2
    cls[(z >= sigma1) & (z < sigma2)] = 1
    cls[(z <= -sigma2)] = -2
    cls[(z <= -sigma1) & (z > -sigma2)] = -1
    return cls


# ---------------------------------------------------------------------------
# 合成数据：气候态 + 年际噪声 + 注入暖异常
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float],
    n_dates: int = 12,
    n_years: int = 5,
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (n_dates*n_years, H, W) 月温度序列。

    气候态 = 空间基线 + 季节循环；叠加年际随机噪声。在最后一年最后一个
    相位于北部区域注入 +7°C 暖异常，供检测验证。
    """
    rng = np.random.default_rng(seed)
    total = n_dates * n_years
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy_n = yy / max(height - 1, 1)
    baseline = 15.0 + 5.0 * (1.0 - yy_n)          # 南暖北冷
    seasonal_amp = 12.0
    cube = np.zeros((total, height, width), dtype=np.float32)
    for y in range(n_years):
        for m in range(n_dates):
            k = y * n_dates + m
            seasonal = seasonal_amp * np.cos(2 * np.pi * (m) / n_dates)
            noise = rng.normal(0, 1.0, (height, width)).astype(np.float32)
            cube[k] = baseline + seasonal + noise
    # 注入暖异常：最后一年最后相位，北部区域 (rows 0:H//3)
    inj_year = n_years - 1
    inj_month = n_dates - 1
    inj_k = inj_year * n_dates + inj_month
    y0, y1 = 0, height // 3
    x0, x1 = 0, width
    cube[inj_k, y0:y1, x0:x1] += 7.0
    info = {
        "bbox": bbox, "width": width, "height": height,
        "n_dates": n_dates, "n_years": n_years, "total_frames": total,
        "injected": {
            "type": "warm_anomaly", "frame_index": int(inj_k),
            "y_range": [y0, y1], "x_range": [x0, x1], "magnitude": 7.0,
        },
    }
    return cube, info


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
            "n_years": getattr(args, "n_years", None),
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

    # ---- Validate CLI / params up front (no filesystem side effects yet) ----
    validate_params(args.n_dates, args.n_years)
    bbox = list(args.bbox) if args.bbox else None

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if args.bbox is not None:
            validate_bbox(bbox)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        cube, synth_info = generate_synthetic_cube(
            bbox, n_dates=args.n_dates, n_years=args.n_years,
        )
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.ndim != 3:
        raise ValidationError(
            f"input must be a time-series cube (n, H, W), got {cube.shape}",
            shape=tuple(cube.shape),
        )

    period = args.n_dates if args.n_dates >= 1 else 12

    # ---- All validation passed — safe to create output directory ----
    os.makedirs(output_dir, exist_ok=True)

    # 1) 距平 + 标准化距平
    anom, clim = anomaly_cube(cube, period)
    z = standardized_anomaly(cube, period)

    # 2) 最新一期的异常制图
    last_anom = anom[-1]
    last_z = z[-1]
    last_class = classify_anomaly(last_z)

    # 写出产物
    anom_tif = os.path.join(output_dir, "anomaly.tif")
    write_geotiff(anom_tif, np.stack([last_anom, last_z], axis=0), bbox)

    class_tif = os.path.join(output_dir, "anomaly_class.tif")
    write_geotiff(class_tif, last_class.astype(np.float32), bbox)

    # 3) 时序 JSON：逐期空间平均距平 + 最新等级占比
    unique, counts = np.unique(last_class, return_counts=True)
    class_frac = {ANOMALY_CLASSES.get(int(u), str(int(u))):
                  float(c / last_class.size) for u, c in zip(unique, counts)}
    ts_payload = {
        "source": source_note,
        "period": period,
        "n_frames": int(cube.shape[0]),
        "shape": [int(cube.shape[1]), int(cube.shape[2])],
        "mean_anomaly_per_frame": [float(anom[k].mean()) for k in range(cube.shape[0])],
        "mean_std_anomaly_per_frame": [float(z[k].mean()) for k in range(cube.shape[0])],
        "latest_frame_class_fractions": class_frac,
        "class_codes": {str(k): v for k, v in ANOMALY_CLASSES.items()},
    }
    if synth_info is not None:
        ts_payload["synthetic_injected"] = synth_info["injected"]
    ts_path = os.path.join(output_dir, "timeseries.json")
    with open(ts_path, "w", encoding="utf-8") as f:
        json.dump(ts_payload, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "period": period,
        "n_frames": int(cube.shape[0]),
        "latest_mean_anomaly": float(last_anom.mean()),
        "latest_mean_std_anomaly": float(last_z.mean()),
        "latest_warm_fraction": float(np.mean(last_class >= 1)),
        "latest_cold_fraction": float(np.mean(last_class <= -1)),
    }

    outputs = [
        {"path": anom_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 2},
        {"path": class_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": ts_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] frames: {cube.shape[0]}  period: {period}")
        print(f"[{SKILL_NAME}] latest mean anomaly: {qa['latest_mean_anomaly']:.3f} K")
        print(f"[{SKILL_NAME}] latest warm fraction: {qa['latest_warm_fraction']:.3f}")
        print(f"[{SKILL_NAME}] output: {anom_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Temperature anomaly mapping: anomaly, standardized anomaly, classes.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multi-band time-series GeoTIFF (band=time step)")
    p.add_argument("--n-dates", type=int, default=12,
                   help="time steps per year / climatology period (default: 12)")
    p.add_argument("--n-years", type=int, default=5,
                   help="number of years for synthetic mode (default: 5)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic temperature series with a warm anomaly")
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
