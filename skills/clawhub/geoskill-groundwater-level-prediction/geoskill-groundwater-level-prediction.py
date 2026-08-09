#!/usr/bin/env python3
"""groundwater-level-prediction — 地下水位预测

基于历史地下水位时序与驱动因子（降水补给、开采量），用多元回归或随机森林
预测未来若干步的水位，并把预测水位空间插值成栅格。核心内容：

- **时序分解**：滑动平均提取趋势项、按周期叠加提取季节项、剩余为残差。
- **驱动回归 / 随机森林**：以降水（含滞后补给项）、开采量、季节项、趋势项
  为特征，拟合水位响应，外推未来 ``--predict-steps`` 个月。
- **空间插值**：把井点预测水位用反距离加权（IDW）插值为区域栅格。
- **不确定性**：时间留出法估计 RMSE，并给出预测—真值相关系数（合成模式）。

数据源：本地多时相水位 GeoTIFF（band = 月份快照），或 ``--synthetic`` 生成
物理一致的井点时序 + 驱动因子用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，无网络访问。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python groundwater-level-prediction.py --bbox 116 39 117 40 --predict-steps 6
    python groundwater-level-prediction.py --bbox 116 39 117 40 --method rf --synthetic

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
SKILL_NAME = "groundwater-level-prediction"

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


def validate_predict_steps(steps):
    """--predict-steps must be a positive integer."""
    try:
        steps = int(steps)
    except (TypeError, ValueError):
        raise UsageError(f"--predict-steps must be an integer, got {steps!r}")
    if steps < 1:
        raise UsageError(f"--predict-steps must be >= 1, got {steps}")
    return steps


def validate_period(period):
    """--period must be >= 2 (otherwise seasonality is undefined)."""
    try:
        period = int(period)
    except (TypeError, ValueError):
        raise UsageError(f"--period must be an integer, got {period!r}")
    if period < 2:
        raise UsageError(f"--period must be >= 2, got {period}")
    return period


# ---------------------------------------------------------------------------
# 核心算法 1：时序分解（趋势 + 季节 + 残差）
# ---------------------------------------------------------------------------
def moving_average_trend(series: np.ndarray, window: int = 12) -> np.ndarray:
    """居中滑动平均提取趋势项。

    边界用最近的有效均值填充，保证输出与输入等长。
    """
    s = np.asarray(series, dtype=np.float64)
    n = s.size
    if n == 0:
        return s.copy()
    window = max(1, min(int(window), n))
    kernel = np.ones(window) / float(window)
    # full 卷积后裁剪回原长（居中对齐）
    conv = np.convolve(s, kernel, mode="full")
    start = (window - 1) // 2
    trend = conv[start:start + n]
    # 边界裁剪不足处用端点值填充
    if trend.size < n:
        trend = np.pad(trend, (0, n - trend.size), mode="edge")
    return trend.astype(np.float64)


def seasonal_component(detrended: np.ndarray, period: int = 12) -> np.ndarray:
    """对去趋势序列按周期位置取均值，得到长度等于 ``period`` 的季节项，
    并平铺回原长度。季节项去均值（总和为 0）。"""
    d = np.asarray(detrended, dtype=np.float64)
    n = d.size
    period = max(1, int(period))
    cycle = np.zeros(period, dtype=np.float64)
    counts = np.zeros(period, dtype=np.float64)
    for i in range(n):
        cycle[i % period] += d[i]
        counts[i % period] += 1.0
    cycle = np.where(counts > 0, cycle / np.maximum(counts, 1.0), 0.0)
    cycle = cycle - cycle.mean()  # 去均值，避免吸收趋势
    return np.tile(cycle, int(np.ceil(n / period)))[:n]


def decompose_series(
    series: np.ndarray, period: int = 12, window: int = 12,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """加性时序分解：series = trend + seasonal + residual。"""
    s = np.asarray(series, dtype=np.float64)
    trend = moving_average_trend(s, window=window)
    seasonal = seasonal_component(s - trend, period=period)
    residual = s - trend - seasonal
    return trend, seasonal, residual


# ---------------------------------------------------------------------------
# 核心算法 2：驱动因子特征矩阵 + 回归/随机森林预测
# ---------------------------------------------------------------------------
def build_feature_matrix(
    precip: np.ndarray,
    pumping: np.ndarray,
    period: int = 12,
    n_lag: int = 2,
) -> Tuple[np.ndarray, np.ndarray]:
    """由降水/开采量序列构建特征矩阵。

    特征列：[precip, precip_lag1, ..., precip_lagN, pumping, sin, cos, trend_norm]。
    返回 (X, valid_index)：仅包含 t >= n_lag 的有效行及其全局时间下标。
    """
    precip = np.asarray(precip, dtype=np.float64)
    pumping = np.asarray(pumping, dtype=np.float64)
    T = precip.size
    if pumping.size != T:
        raise ValidationError(
            "precip and pumping length mismatch",
            precip=int(T), pumping=int(pumping.size),
        )
    n_lag = max(0, int(n_lag))
    idx = np.arange(n_lag, T)
    if idx.size == 0:
        raise ValidationError("time series too short for the requested lag", n_lag=n_lag, T=int(T))
    cols: List[np.ndarray] = [precip[idx]]
    for lag in range(1, n_lag + 1):
        cols.append(precip[idx - lag])
    cols.append(pumping[idx])
    cols.append(np.sin(2.0 * np.pi * idx / float(period)))
    cols.append(np.cos(2.0 * np.pi * idx / float(period)))
    cols.append(idx / float(max(T - 1, 1)))  # 归一化趋势项
    X = np.stack(cols, axis=1)
    return X, idx


def fit_predict_drivers(
    level_hist: np.ndarray,
    precip_hist: np.ndarray,
    pumping_hist: np.ndarray,
    precip_fut: np.ndarray,
    pumping_fut: np.ndarray,
    period: int = 12,
    n_lag: int = 2,
    method: str = "linear",
    holdout_frac: float = 0.2,
    seed: int = 42,
) -> Dict[str, Any]:
    """对单点水位时序拟合驱动模型并外推未来。

    使用扩展序列（历史 + 未来驱动）构建一致的特征矩阵：训练用历史行，
    预测用未来行。时间留出法估计验证 RMSE。返回包含预测、RMSE、拟合优度的 dict。
    """
    level_hist = np.asarray(level_hist, dtype=np.float64)
    precip_hist = np.asarray(precip_hist, dtype=np.float64)
    pumping_hist = np.asarray(pumping_hist, dtype=np.float64)
    precip_fut = np.asarray(precip_fut, dtype=np.float64)
    pumping_fut = np.asarray(pumping_fut, dtype=np.float64)
    predict_steps = int(precip_fut.size)
    if pumping_fut.size != predict_steps:
        raise ValidationError("future precip/pumping length mismatch")
    if level_hist.size != precip_hist.size:
        raise ValidationError("history level/precip length mismatch")

    precip_ext = np.concatenate([precip_hist, precip_fut])
    pumping_ext = np.concatenate([pumping_hist, pumping_fut])
    T_hist = precip_hist.size

    X_full, global_idx = build_feature_matrix(precip_ext, pumping_ext, period, n_lag)
    # 行对应的全局时间下标 global_idx；训练行 < T_hist，预测行 >= T_hist
    train_row = global_idx < T_hist
    fut_row = global_idx >= T_hist

    X_hist = X_full[train_row]
    y_hist = level_hist[global_idx[train_row]]
    X_fut = X_full[fut_row]

    if X_hist.shape[0] < 3:
        raise ValidationError("not enough history samples to fit", rows=int(X_hist.shape[0]))

    # 时间留出法验证
    n_train = max(1, int(round(X_hist.shape[0] * (1.0 - holdout_frac))))
    n_train = min(n_train, X_hist.shape[0])
    X_tr, y_tr = X_hist[:n_train], y_hist[:n_train]
    X_va, y_va = X_hist[n_train:], y_hist[n_train:]

    pred_va = _fit_and_predict(X_tr, y_tr, X_va, method, seed)
    if y_va.size > 0:
        rmse_val = float(np.sqrt(np.mean((pred_va - y_va) ** 2)))
    else:
        rmse_val = float("nan")

    # 用全部历史重拟合，外推未来
    pred_fut = _fit_and_predict(X_hist, y_hist, X_fut, method, seed)

    # 拟合优度（历史内样本 R^2）
    fitted_hist = _fit_and_predict(X_hist, y_hist, X_hist, method, seed)
    ss_res = float(np.sum((y_hist - fitted_hist) ** 2))
    ss_tot = float(np.sum((y_hist - y_hist.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 1e-12 else 0.0

    return {
        "predicted_future": pred_fut.astype(np.float64),
        "rmse_validation": rmse_val,
        "r2_history": float(r2),
        "n_history": int(X_hist.shape[0]),
        "predict_steps": predict_steps,
        "method": method,
    }


def _fit_and_predict(
    X_tr: np.ndarray, y_tr: np.ndarray, X_pred: np.ndarray, method: str, seed: int,
) -> np.ndarray:
    """统一的拟合 + 预测入口（线性 / 随机森林）。"""
    if method == "linear":
        # 带截距的最小二乘
        A = np.hstack([X_tr, np.ones((X_tr.shape[0], 1))])
        coef, *_ = np.linalg.lstsq(A, y_tr, rcond=None)
        Ap = np.hstack([X_pred, np.ones((X_pred.shape[0], 1))])
        return Ap @ coef
    if method == "rf":
        try:
            from sklearn.ensemble import RandomForestRegressor
        except ImportError as exc:  # pragma: no cover
            raise ProcessError("scikit-learn is required for method='rf'") from exc
        rf = RandomForestRegressor(
            n_estimators=80, max_depth=8, random_state=seed, n_jobs=1,
        )
        rf.fit(X_tr, y_tr)
        return rf.predict(X_pred)
    raise UsageError(f"unknown method '{method}'. Choose from: linear, rf", method=method)


# ---------------------------------------------------------------------------
# 核心算法 3：反距离加权空间插值（IDW）
# ---------------------------------------------------------------------------
def idw_interpolate(
    points_xy: np.ndarray,
    values: np.ndarray,
    grid_shape: Tuple[int, int],
    bbox: List[float],
    power: float = 2.0,
) -> np.ndarray:
    """把离散点值用 IDW 插值到规则栅格（地理坐标）。

    points_xy: (n, 2) 坐标 (x=lon, y=lat)；values: (n,)；
    grid_shape: (H, W)；bbox: [W, S, E, N]。返回 (H, W)。
    落在点上的像元直接取该点值（避免除零）。
    """
    pts = np.asarray(points_xy, dtype=np.float64)
    vals = np.asarray(values, dtype=np.float64)
    if pts.ndim != 2 or pts.shape[1] != 2:
        raise ValidationError("points_xy must have shape (n, 2)")
    if pts.shape[0] != vals.size:
        raise ValidationError("points and values count mismatch")
    if pts.shape[0] == 0:
        raise ValidationError("no points to interpolate")

    H, W = int(grid_shape[0]), int(grid_shape[1])
    w, s, e, n = bbox
    xs = np.linspace(w, e, W)
    ys = np.linspace(n, s, H)  # 行从上（北）到下（南）
    gx, gy = np.meshgrid(xs, ys)
    grid = np.stack([gx.ravel(), gy.ravel()], axis=1)  # (HW, 2)

    diff = grid[:, None, :] - pts[None, :, :]  # (HW, n, 2)
    dist = np.sqrt(np.sum(diff ** 2, axis=2))  # (HW, n)
    eps = 1e-12
    on_point = dist < eps
    weights = np.where(on_point, 0.0, 1.0 / np.power(np.maximum(dist, eps), power))
    # 若像元正好落在某点上，直接取该点值
    hit = np.any(on_point, axis=1)
    wsum = weights.sum(axis=1)
    interp = (weights * vals[None, :]).sum(axis=1) / np.where(wsum > 0, wsum, 1.0)
    if np.any(hit):
        nearest = np.argmin(dist[hit], axis=1)
        interp[hit] = vals[nearest]
    return interp.reshape(H, W).astype(np.float32)


# ---------------------------------------------------------------------------
# 合成数据：物理一致的井点水位时序 + 驱动因子
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    n_history: int = 60,
    predict_steps: int = 6,
    n_wells: int = 16,
    period: int = 12,
    grid_shape: Tuple[int, int] = (48, 48),
    seed: int = 42,
) -> Dict[str, Any]:
    """生成受降水（正）与开采（负）驱动、带季节性与长期下降趋势的井点水位。

    返回 dict：井位、历史水位、历史/未来驱动、未来真值水位、栅格信息等。
    """
    rng = np.random.default_rng(seed)
    w, s, e, n = bbox
    # 井位（地理坐标）
    xs = rng.uniform(w + 0.05 * (e - w), e - 0.05 * (e - w), n_wells)
    ys = rng.uniform(s + 0.05 * (n - s), n - 0.05 * (n - s), n_wells)
    points = np.stack([xs, ys], axis=1)

    T = n_history + predict_steps
    t = np.arange(T, dtype=np.float64)
    # 降水：夏季高（峰在 ~第 6 月）+ 噪声
    precip = 70.0 + 55.0 * np.sin(2.0 * np.pi * (t - 3.0) / period) + rng.normal(0, 12.0, T)
    precip = np.clip(precip, 1.0, None)
    # 开采量：春季/旱季高 + 缓慢上升趋势 + 噪声
    pumping = 30.0 + 0.12 * t + 12.0 * np.cos(2.0 * np.pi * (t - 1.0) / period) + rng.normal(0, 3.0, T)
    pumping = np.clip(pumping, 1.0, None)

    precip_mean = precip[:n_history].mean()
    pumping_mean = pumping[:n_history].mean()

    # 每口井的空间基准水位（区域渐变）
    xn = (xs - w) / max(e - w, 1e-9)
    yn = (ys - s) / max(n - s, 1e-9)
    base = 35.0 + 8.0 * xn - 5.0 * yn  # 水位高程 (m)

    decline = 0.03      # 长期下降速率 (m/月)
    beta_p = 0.020      # 降水补给响应 (m/mm)
    beta_q = 0.015      # 开采响应 (m/单位开采)
    seasonal_amp = 0.4  # 独立季节波动 (m)

    levels = np.zeros((n_wells, T), dtype=np.float64)
    for i in range(n_wells):
        level = (
            base[i]
            - decline * t
            + beta_p * (precip - precip_mean)
            - beta_q * (pumping - pumping_mean)
            + seasonal_amp * np.sin(2.0 * np.pi * t / period + 0.5)
            + rng.normal(0, 0.15, T)
        )
        levels[i] = level

    return {
        "bbox": list(bbox),
        "points": points,
        "n_wells": n_wells,
        "n_history": n_history,
        "predict_steps": predict_steps,
        "period": period,
        "grid_shape": tuple(int(x) for x in grid_shape),
        "levels": levels,                       # (n_wells, T) 全部真值
        "levels_hist": levels[:, :n_history],   # (n_wells, n_history)
        "levels_fut_truth": levels[:, n_history:],  # (n_wells, predict_steps)
        "precip_hist": precip[:n_history],
        "pumping_hist": pumping[:n_history],
        "precip_fut": precip[n_history:],
        "pumping_fut": pumping[n_history:],
        "base_levels": base,
    }


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str, cube: np.ndarray, bbox: List[float], nodata: float = -9999.0,
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
    """Read a multi-temporal water-level GeoTIFF. Returns (cube, bbox).

    NoData values declared in the file are replaced with NaN in the returned
    cube. Callers should treat any NaN as a non-finite observation.
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


def finite_pixel_mask(cube: np.ndarray) -> np.ndarray:
    """Per-pixel mask: True iff every time-step is finite (not NaN/inf)."""
    return np.isfinite(np.asarray(cube)).all(axis=0)


def forecast_cube_seasonal_trend(
    cube: np.ndarray, predict_steps: int, period: int = 12,
) -> np.ndarray:
    """对多时相栅格（bands = 时间）逐像元做季节-趋势外推预测。

    用于 --input 路径（无外部驱动因子）：对每个像元时序分解，外推趋势并叠加
    季节项。返回 (predict_steps, H, W)。
    """
    if cube.ndim != 3:
        raise ValidationError("input cube must be 3D (time, H, W)")
    T, H, W = cube.shape
    flat = cube.reshape(T, -1).astype(np.float64)  # (T, npix)
    npix = flat.shape[1]
    out = np.zeros((predict_steps, npix), dtype=np.float64)
    for p in range(npix):
        series = flat[:, p]
        trend, seasonal, _ = decompose_series(series, period=period)
        # 趋势用末段斜率线性外推
        seg = min(period, T)
        slope = (trend[-1] - trend[-seg]) / max(seg - 1, 1)
        period_cyc = seasonal_component(series - trend, period=period)
        cyc = np.resize(period_cyc, period)
        for k in range(predict_steps):
            fut_t = T + k
            out[k, p] = trend[-1] + slope * (k + 1) + cyc[fut_t % period]
    return out.reshape(predict_steps, H, W).astype(np.float32)


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
        skill=SKILL_NAME,
        skill_version=VERSION,
        command=cmd,
        started_at=started_at,
        finished_at=_utc_now(),
        exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "method": getattr(args, "method", None),
            "predict_steps": getattr(args, "predict_steps", None),
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

    # --- pre-flight validation (BEFORE making output dir) -----------------
    bbox = list(args.bbox) if args.bbox else None
    predict_steps = validate_predict_steps(args.predict_steps)
    period = validate_period(args.period)

    # --- pre-flight validation: choose branch and validate inputs ---------
    synth_info: Optional[Dict[str, Any]] = None
    qa: Dict[str, Any] = {"method": args.method, "predict_steps": predict_steps,
                          "period": period}
    outputs: List[Dict[str, Any]] = []

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        if bbox is not None:
            bbox = validate_bbox(bbox)
        else:
            bbox = validate_bbox(file_bbox)
        if cube.shape[0] < 3:
            raise ValidationError("input raster needs >= 3 time bands", bands=int(cube.shape[0]))
        if cube.size == 0:
            raise ValidationError("input raster is empty")
        valid = finite_pixel_mask(cube)
        n_valid = int(valid.sum())
        if n_valid == 0:
            raise ValidationError(
                "input raster has no valid pixels (all values are nodata)")
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        # Validate bbox again in case caller supplied a degenerate one
        # (generate_synthetic itself doesn't re-check, but caller may).

    # All checks passed → now create the output dir.
    os.makedirs(output_dir, exist_ok=True)

    if args.input and not args.synthetic:
        # 真实栅格路径：多时相水位 cube（bands = 月份快照）→ 季节-趋势外推
        # (validation already done above; qa is enriched here)
        qa["source"] = args.input
        qa["n_valid_pixels"] = n_valid
        qa["n_time_bands"] = int(cube.shape[0])
        qa["grid_shape"] = [int(cube.shape[1]), int(cube.shape[2])]

        pred_cube = forecast_cube_seasonal_trend(cube, predict_steps, period=period)

        # 预测最末步栅格（保留 NaN，由 rasterio 写为 nodata）
        out_tif = os.path.join(output_dir, "predicted_level.tif")
        write_geotiff(out_tif, pred_cube[-1], bbox)
        outputs.append({"path": out_tif, "kind": "raster", "crs_epsg": 4326,
                        "bbox_wgs84": bbox, "band_count": 1})

        # 空间均值预测曲线（NaN-safe）
        cube_finite = np.where(np.isfinite(cube), cube, np.nan)
        hist_curve = [float(np.nanmean(cube_finite[t])) for t in range(cube.shape[0])]
        fut_curve = [float(np.nanmean(pred_cube[k])) for k in range(predict_steps)]
        curve = {"history_mean_level": hist_curve, "predicted_mean_level": fut_curve}
        qa["overall_predicted_mean"] = (
            float(np.nanmean(pred_cube)) if np.isfinite(pred_cube).any() else 0.0)
    else:
        # 合成路径：井点时序 + 驱动因子回归/RF
        # (validation already done above)
        synth_info = generate_synthetic(bbox, predict_steps=predict_steps, period=period)
        qa["source"] = "synthetic"
        qa["n_wells"] = synth_info["n_wells"]

        levels_hist = synth_info["levels_hist"]
        levels_fut_truth = synth_info["levels_fut_truth"]
        n_wells = synth_info["n_wells"]
        preds = np.zeros((n_wells, predict_steps), dtype=np.float64)
        rmses = np.zeros(n_wells, dtype=np.float64)
        for i in range(n_wells):
            res = fit_predict_drivers(
                levels_hist[i], synth_info["precip_hist"], synth_info["pumping_hist"],
                synth_info["precip_fut"], synth_info["pumping_fut"],
                period=period, method=args.method, seed=args.seed,
            )
            preds[i] = res["predicted_future"]
            rmses[i] = res["rmse_validation"]

        # 预测—真值相关系数与 RMSE
        p = preds.ravel()
        truth = levels_fut_truth.ravel()
        corr = float(np.corrcoef(p, truth)[0, 1]) if p.size > 1 else float("nan")
        rmse_truth = float(np.sqrt(np.mean((p - truth) ** 2)))
        qa["prediction_truth_correlation"] = corr
        qa["rmse_vs_truth"] = rmse_truth
        qa["rmse_validation_mean"] = float(np.nanmean(rmses))

        # 空间插值栅格：预测最末步水位 IDW 到区域
        pred_last = preds[:, -1]
        grid_shape = synth_info["grid_shape"]
        level_raster = idw_interpolate(
            synth_info["points"], pred_last, grid_shape, bbox, power=2.0,
        )
        out_tif = os.path.join(output_dir, "predicted_level.tif")
        write_geotiff(out_tif, level_raster, bbox)
        outputs.append({"path": out_tif, "kind": "raster", "crs_epsg": 4326,
                        "bbox_wgs84": bbox, "band_count": 1})

        # 预测曲线 JSON（空间均值）
        hist_curve = [float(np.mean(levels_hist[:, t])) for t in range(levels_hist.shape[1])]
        pred_curve = [float(np.mean(preds[:, k])) for k in range(predict_steps)]
        obs_curve = [float(np.mean(levels_fut_truth[:, k])) for k in range(predict_steps)]
        curve = {
            "history_mean_level": hist_curve,
            "predicted_mean_level": pred_curve,
            "observed_future_mean_level": obs_curve,
            "per_well_rmse_validation": [float(x) for x in rmses],
        }
        qa["overall_predicted_mean"] = float(np.mean(preds))

    # All checks passed → now create the output dir.
    os.makedirs(output_dir, exist_ok=True)

    curve_path = os.path.join(output_dir, "prediction_curve.json")
    curve["method"] = args.method
    curve["predict_steps"] = predict_steps
    curve["period"] = period
    with open(curve_path, "w", encoding="utf-8") as f:
        json.dump(curve, f, ensure_ascii=False, indent=2)
    outputs.append({"path": curve_path, "kind": "json"})

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {qa['source']}  method: {args.method}")
        print(f"[{SKILL_NAME}] predict_steps: {predict_steps}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        print(f"[{SKILL_NAME}] curve:  {curve_path}")
        if "prediction_truth_correlation" in qa:
            print(f"[{SKILL_NAME}] corr(pred,truth): {qa['prediction_truth_correlation']:.4f}"
                  f"  rmse_truth: {qa['rmse_vs_truth']:.4f}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Groundwater level prediction from driver-based regression / random forest.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multi-temporal water-level GeoTIFF (bands = months)")
    p.add_argument("--method", default="linear", choices=["linear", "rf"],
                   help="prediction method (default: linear)")
    p.add_argument("--predict-steps", type=int, default=6,
                   help="number of future steps to predict (default: 6)")
    p.add_argument("--period", type=int, default=12,
                   help="seasonal period in steps (default: 12)")
    p.add_argument("--seed", type=int, default=42, help="random seed (default: 42)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate physics-consistent synthetic well series (offline)")
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
