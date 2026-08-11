#!/usr/bin/env python3
"""ai-time-series-forecast — AI 时序预测

对遥感时序数据（逐像元 NDVI/温度/后向散射等）做趋势与自回归建模，
执行多步预测并在留出时段上验证精度。

本 skill 是 LSTM/Transformer 时序预测网络的**离线 numpy 等价实现**：
不依赖深度学习框架，而用可验证的经典模型复现"拟合 -> 多步外推 -> 验证"——

1. **线性/多项式拟合**：最小二乘拟合时间趋势（线性或 d 次多项式）；
2. **自回归 AR(p)**：用最近 p 个观测的线性组合预测下一时刻（lstsq 求系数），
   多步预测逐步迭代外推；
3. **留出验证**：末尾 horizon 个时刻作为测试集，报告 MAE / RMSE；
4. **逐像元外推**：对 (T, H, W) 立方体逐像元预测，输出未来各步栅格。

数据源：本地多波段 GeoTIFF（各波段视为时间步），或 ``--synthetic`` 生成
含趋势 + 季节项 + 噪声的模拟时序立方体。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python ai-time-series-forecast.py --input series.tif --method linear --horizon 4 --output-dir ./out
    python ai-time-series-forecast.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "ai-time-series-forecast"

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, DependencyError, ValidationError, ProcessError,
        to_exit_code,
    )
    from _geoskill_core.manifest import OutputManifest, OutputFile
except ImportError:  # pragma: no cover
    class GeoSkillError(Exception):
        def __init__(self, message: str, code: int = 7, kind: str = "EGeo", **kw):
            super().__init__(message)
            self.message, self.code, self.kind = message, code, kind

    class UsageError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=2, kind="EUsage", **k)

    class DependencyError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=3, kind="EDep", **k)

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
# bbox validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox, *, allow_antimeridian: bool = False) -> List[float]:
    """校验 bbox: [W, S, E, N]。

    - 必须为 4 个 float
    - 经度 ∈ [-180, 180]、纬度 ∈ [-90, 90]
    - 必须 W < E 且 S < N（跨 180 经线按设计不支持）
    """
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise UsageError("bbox must be 4 floats [W S E N]", bbox=list(bbox) if bbox else None)
    try:
        w, s, e, n = (float(v) for v in bbox)
    except (TypeError, ValueError) as exc:
        raise UsageError("bbox entries must be numeric", bbox=list(bbox)) from exc
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError("bbox longitude out of range [-180, 180]", w=w, e=e)
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError("bbox latitude out of range [-90, 90]", s=s, n=n)
    if not (w < e):
        if allow_antimeridian and w > 0 and e < 0:
            pass
        else:
            raise ValidationError(
                "bbox requires W < E (got W={:.6f} E={:.6f}); "
                "antimeridian crossing is not supported".format(w, e),
                w=w, e=e)
    if not (s < n):
        raise ValidationError(
            "bbox requires S < N (got S={:.6f} N={:.6f})".format(s, n),
            s=s, n=n)
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# Torch + cuDNN 环境（DL skill 必需）：本 skill 是 LSTM 时序预测网络，
# 原实现为"离线 numpy 等价实现"，本版本替换为真 torch LSTM（GPU 训练/推理）。
# ---------------------------------------------------------------------------
def _prepare_dll_paths() -> None:
    """Windows 下把 conda 环境的 Library\\bin 注册进 DLL 搜索路径。

    torch 的 cuDNN 依赖（cudnn64_9.dll / cudnn_graph64_9.dll / cudart64_12.dll
    等）装在 <env>\\Library\\bin；若进程不是从激活的 conda 环境启动，
    PATH 里没有该目录，torch 加载 cuDNN 会失败（崩进程）。
    """
    if os.name != "nt":
        return
    lib_bin = os.path.join(sys.prefix, "Library", "bin")
    if not os.path.isdir(lib_bin):
        return
    if lib_bin not in os.environ.get("PATH", ""):
        os.environ["PATH"] = lib_bin + os.pathsep + os.environ.get("PATH", "")
    try:
        os.add_dll_directory(lib_bin)
    except (OSError, AttributeError):
        pass


def _require_torch():
    _prepare_dll_paths()
    try:
        import torch  # noqa: F401
    except ImportError as exc:
        raise DependencyError(
            "torch is required for ai-time-series-forecast (pip install torch)") from exc
    import torch
    return torch


def _cuda_device(torch_mod):
    if not torch_mod.cuda.is_available():
        raise DependencyError(
            "ai-time-series-forecast requires a CUDA GPU; torch.cuda.is_available() "
            "is False in this environment")
    try:
        torch_mod.backends.cudnn.enabled = bool(torch_mod.backends.cudnn.is_available())
    except Exception:  # pragma: no cover
        torch_mod.backends.cudnn.enabled = False
    return torch_mod.device("cuda")


# ---------------------------------------------------------------------------
# 深度学习核心：单层 LSTM 时序预测器（many-to-one）
# 训练目标：给定一个固定长度的输入窗口，预测紧接的下一个值；
# 多步预测通过把上一步输出反馈回窗口尾端、迭代外推实现。
# 单元测试可与经典线性/AR/poly 模型独立运行。
# ---------------------------------------------------------------------------
WEIGHTS_FILENAME = "ts_lstm_weights.pt"


def _build_lstm(torch_mod, hidden: int = 16):
    nn = torch_mod.nn

    class LSTMForecaster(nn.Module):
        def __init__(self, hidden_size: int = 16):
            super().__init__()
            self.hidden_size = hidden_size
            self.lstm = nn.LSTM(input_size=1, hidden_size=hidden_size,
                                num_layers=1, batch_first=True)
            self.head = nn.Linear(hidden_size, 1)

        def forward(self, x):
            # x: (B, T, 1)
            out, _ = self.lstm(x)
            return self.head(out[:, -1, :])  # (B, 1)

    return LSTMForecaster(hidden)


def _train_lstm_model(
    torch_mod, train_cube: np.ndarray, device, *,
    window: int = 8, hidden: int = 16, epochs: int = 15,
    batch: int = 128, lr: float = 2e-3, seed: int = 42,
) -> Tuple[Any, Dict[str, Any]]:
    """在合成 train_cube (T, H, W) 上训练一个全局共享 LSTM。

    构建滑窗样本：每个像素、每个 t>=window 取 X = train[t-window:t]，Y = train[t]。
    """
    T, H, W = train_cube.shape
    if T < window + 1:
        raise ValidationError(
            f"need at least window+1={window + 1} time steps for training, got T={T}",
            T=int(T), window=int(window))
    flat = train_cube.reshape(T, H * W)
    # 构造 (n_samples, window, 1) X 与 (n_samples, 1) Y
    n_samples = (T - window) * (H * W)
    X = np.empty((n_samples, window, 1), dtype=np.float32)
    Y = np.empty((n_samples, 1), dtype=np.float32)
    k = 0
    for t in range(window, T):
        win = flat[t - window:t].T  # (N, window)
        tgt = flat[t].T  # (N,)
        for j in range(H * W):
            X[k, :, 0] = win[j]
            Y[k, 0] = tgt[j]
            k += 1

    Xt = torch_mod.from_numpy(X).to(device)
    Yt = torch_mod.from_numpy(Y).to(device)

    torch_mod.manual_seed(seed)
    model = _build_lstm(torch_mod, hidden=hidden).to(device)
    opt = torch_mod.optim.Adam(model.parameters(), lr=lr)
    crit = torch_mod.nn.MSELoss()
    model.train()
    n = Xt.shape[0]
    steps = 0
    for _ in range(epochs):
        idx = torch_mod.randperm(n, device=device)
        for s in range(0, n, batch):
            bi = idx[s:s + batch]
            opt.zero_grad()
            pred = model(Xt[bi])
            loss = crit(pred, Yt[bi])
            loss.backward()
            opt.step()
            steps += 1
    return model, {
        "window": int(window),
        "hidden": int(hidden),
        "epochs": int(epochs),
        "batch": int(batch),
        "lr": float(lr),
        "n_params": int(sum(p.numel() for p in model.parameters())),
        "n_train_samples": int(n),
        "steps": int(steps),
        "trained_at": _utc_now(),
        "framework": f"torch {torch_mod.__version__} / {torch_mod.cuda.get_device_name(0)}",
    }


def weights_path() -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), WEIGHTS_FILENAME)


_LSTM_CACHE: Dict[str, Any] = {}


def _ensure_lstm(window: int, hidden: int, device) -> Tuple[Any, Dict[str, Any]]:
    """加载随附 LSTM 权重；缺失则在 GPU 上训练并落盘。"""
    cache_key = f"w{window}_h{hidden}_{device}"
    if cache_key in _LSTM_CACHE:
        return _LSTM_CACHE[cache_key]["model"], _LSTM_CACHE[cache_key]["meta"]
    torch_mod = _require_torch()
    path = weights_path()
    if os.path.exists(path):
        ck = torch_mod.load(path, map_location="cpu")
        model = _build_lstm(torch_mod, hidden=ck.get("hidden", hidden))
        model.load_state_dict(ck["state_dict"])
        meta = dict(ck.get("meta", {}))
        meta["weights"] = os.path.basename(path)
    else:
        # 缺权重：在调用现场训练（process 内做）
        return None, None  # signal: need training data
    model = model.to(device).eval()
    _LSTM_CACHE[cache_key] = {"model": model, "meta": meta}
    return model, meta


def _save_lstm_weights(model, meta: Dict[str, Any]) -> None:
    torch_mod = _require_torch()
    path = weights_path()
    torch_mod.save({"state_dict": model.state_dict(),
                    "meta": meta,
                    "window": meta.get("window", 8),
                    "hidden": meta.get("hidden", 16)},
                   path)


def _lstm_train_and_forecast(
    cube: np.ndarray, device, *,
    horizon: int, window: int = 8, hidden: int = 16, epochs: int = 15,
    batch: int = 128, lr: float = 2e-3, seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """LSTM 训练 + 推理：返回 (forecast[horizon, H, W], pixel_rmse[H, W], meta)。"""
    torch_mod = _require_torch()
    cube = np.asarray(cube, dtype=np.float32)
    if cube.ndim != 3:
        raise ValidationError("cube must be (T, H, W)", shape=list(cube.shape))
    T, H, W = cube.shape
    if T <= horizon + 2:
        raise ValidationError(
            f"need T > horizon + 2, got T={T}, horizon={horizon}",
            T=int(T), horizon=int(horizon))
    if horizon < 1:
        raise UsageError("horizon must be >= 1", horizon=int(horizon))
    if window < 1:
        raise UsageError("window must be >= 1", window=int(window))
    if T <= window:
        raise ValidationError(
            f"need T > window (got T={T}, window={window})", T=int(T), window=int(window))

    train_part = cube[:T - horizon]
    test_part = cube[T - horizon:]

    # 优先用随附权重；缺则训练并落盘
    model, meta = _ensure_lstm(window, hidden, device)
    if model is None:
        model, meta = _train_lstm_model(
            torch_mod, train_part, device, window=window, hidden=hidden,
            epochs=epochs, batch=batch, lr=lr, seed=seed,
        )
        meta["weights"] = "trained-on-the-fly (weights file missing)"
        try:
            _save_lstm_weights(model, meta)
        except Exception:  # pragma: no cover
            pass

    model.eval()
    fc = np.zeros((horizon, H, W), dtype=np.float32)
    history = cube[:T - horizon].copy()  # (T-h, H, W)
    with torch_mod.no_grad():
        for k in range(horizon):
            win = history[-window:].reshape(window, H * W).T[:, :, None]  # (N, W, 1)
            x_t = torch_mod.from_numpy(win).to(device).float()
            y_pred = model(x_t).cpu().numpy().reshape(H, W)
            fc[k] = y_pred
            history = np.concatenate([history, y_pred[None]], axis=0)
    err = fc - test_part
    rmse = np.sqrt((err * err).mean(axis=0))
    # 训练 holdout 指标（若 meta 来自权重文件，meta 中有 n_train_samples 字段）
    meta_out = dict(meta)
    meta_out["horizon"] = int(horizon)
    meta_out["device"] = str(device)
    meta_out["backend"] = "torch lstm (many-to-one, recursive)"
    return fc, rmse, meta_out


def _lstm_forecast_series(
    y: np.ndarray, device, *,
    window: int = 8, hidden: int = 16, epochs: int = 15,
    batch: int = 128, lr: float = 2e-3, seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """对单条序列的 LSTM 训练 + 预测。返回 (forecast[horizon], meta)。

    训练：序列前 80% 滑窗；预测：剩余 20% 长度作为 horizon 迭代外推。
    """
    torch_mod = _require_torch()
    y = np.asarray(y, dtype=np.float64).ravel()
    n = y.size
    if n < window + 2:
        raise ValidationError(
            f"need at least window+2={window + 2} samples", n=int(n), window=int(window))
    horizon = max(1, n // 5)
    if n <= horizon + 2:
        raise ValidationError(
            f"series too short for horizon {horizon}", n=int(n), horizon=int(horizon))

    train = y[:n - horizon].astype(np.float32)
    test = y[n - horizon:]

    # 单条序列训练：sliding windows over train
    n_train = train.size
    if n_train <= window:
        raise ValidationError(
            f"need train > window (got n_train={n_train}, window={window})",
            n_train=int(n_train), window=int(window))
    n_samples = n_train - window
    X = np.empty((n_samples, window, 1), dtype=np.float32)
    Y = np.empty((n_samples, 1), dtype=np.float32)
    for i in range(n_samples):
        X[i, :, 0] = train[i:i + window]
        Y[i, 0] = train[i + window]
    Xt = torch_mod.from_numpy(X).to(device)
    Yt = torch_mod.from_numpy(Y).to(device)

    torch_mod.manual_seed(seed)
    model = _build_lstm(torch_mod, hidden=hidden).to(device)
    opt = torch_mod.optim.Adam(model.parameters(), lr=lr)
    crit = torch_mod.nn.MSELoss()
    model.train()
    for _ in range(epochs):
        idx = torch_mod.randperm(n_samples, device=device)
        for s in range(0, n_samples, batch):
            bi = idx[s:s + batch]
            opt.zero_grad()
            pred = model(Xt[bi])
            loss = crit(pred, Yt[bi])
            loss.backward()
            opt.step()
    model.eval()
    fc: List[float] = []
    history = train.copy()
    with torch_mod.no_grad():
        for _ in range(horizon):
            win = history[-window:].reshape(window, 1)[:, :, None]
            x_t = torch_mod.from_numpy(win).to(device).float()
            y_pred = model(x_t).cpu().numpy().ravel()[0]
            fc.append(float(y_pred))
            history = np.concatenate([history, np.array([y_pred], dtype=np.float32)], axis=0)
    fc_arr = np.asarray(fc, dtype=np.float64)
    meta = {
        "method": "lstm",
        "window": int(window), "hidden": int(hidden), "epochs": int(epochs),
        "n_params": int(sum(p.numel() for p in model.parameters())),
        "framework": f"torch {torch_mod.__version__} / {torch_mod.cuda.get_device_name(0)}",
    }
    return fc_arr, {"horizon": int(horizon), "test": test, "meta": meta}


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def fit_linear(t: np.ndarray, y: np.ndarray) -> Tuple[float, float]:
    """最小二乘线性拟合 y = slope*t + intercept。返回 (slope, intercept)。"""
    t = np.asarray(t, dtype=np.float64).ravel()
    y = np.asarray(y, dtype=np.float64).ravel()
    if t.size != y.size or t.size < 2:
        raise ValidationError("fit_linear needs >= 2 matching points",
                              n_t=int(t.size), n_y=int(y.size))
    tm = t.mean()
    ym = y.mean()
    denom = float(np.sum((t - tm) ** 2))
    if denom <= 1e-12:
        raise ValidationError("t values are degenerate (no variance)")
    slope = float(np.sum((t - tm) * (y - ym)) / denom)
    intercept = float(ym - slope * tm)
    return slope, intercept


def fit_polynomial(t: np.ndarray, y: np.ndarray, degree: int) -> np.ndarray:
    """d 次多项式拟合，返回系数（最高次在前，np.polyfit 约定）。"""
    t = np.asarray(t, dtype=np.float64).ravel()
    y = np.asarray(y, dtype=np.float64).ravel()
    if degree < 1:
        raise UsageError("degree must be >= 1", degree=int(degree))
    if t.size != y.size or t.size <= degree:
        raise ValidationError(
            f"fit_polynomial needs > {degree} points", n=int(t.size), degree=int(degree))
    return np.polyfit(t, y, degree)


def eval_polynomial(coeffs: np.ndarray, t: np.ndarray) -> np.ndarray:
    return np.polyval(np.asarray(coeffs, dtype=np.float64), np.asarray(t, dtype=np.float64))


def fit_ar(y: np.ndarray, order: int) -> np.ndarray:
    """AR(p) 系数拟合：y_t = c[0]*y_{t-1} + ... + c[p-1]*y_{t-p}。

    用最小二乘（设计矩阵为滞后窗）求解，返回 (p,) 系数。
    """
    y = np.asarray(y, dtype=np.float64).ravel()
    if order < 1:
        raise UsageError("order must be >= 1", order=int(order))
    if y.size <= order + 1:
        raise ValidationError(
            f"fit_ar needs > {order + 1} samples", n=int(y.size), order=int(order))
    n = y.size
    X = np.empty((n - order, order), dtype=np.float64)
    Y = np.empty(n - order, dtype=np.float64)
    for i, t in enumerate(range(order, n)):
        X[i] = y[t - order:t][::-1]   # [y_{t-1}, ..., y_{t-p}]
        Y[i] = y[t]
    coefs, _, _, _ = np.linalg.lstsq(X, Y, rcond=None)
    return coefs


def forecast_ar(y_history: np.ndarray, coefs: np.ndarray, steps: int) -> np.ndarray:
    """AR 多步预测：迭代外推 steps 步。"""
    y = list(np.asarray(y_history, dtype=np.float64).ravel())
    p = len(coefs)
    if len(y) < p:
        raise ValidationError("history shorter than AR order",
                              history=len(y), order=int(p))
    if steps < 1:
        raise UsageError("steps must be >= 1", steps=int(steps))
    out: List[float] = []
    for _ in range(steps):
        window = np.array(y[-p:][::-1], dtype=np.float64)
        nxt = float(np.dot(coefs, window))
        out.append(nxt)
        y.append(nxt)
    return np.asarray(out, dtype=np.float64)


def evaluate_forecast(forecast: np.ndarray, actual: np.ndarray) -> Dict[str, float]:
    """预测 vs 实际：MAE / RMSE（样本数一致）。"""
    f = np.asarray(forecast, dtype=np.float64).ravel()
    a = np.asarray(actual, dtype=np.float64).ravel()
    if f.size != a.size or f.size == 0:
        raise ValidationError("forecast/actual size mismatch or empty",
                              forecast=int(f.size), actual=int(a.size))
    err = f - a
    return {
        "mae": float(np.mean(np.abs(err))),
        "rmse": float(np.sqrt(np.mean(err * err))),
        "n": int(f.size),
    }


def forecast_series(
    y: np.ndarray,
    method: str = "linear",
    horizon: int = 4,
    degree: int = 2,
    order: int = 2,
) -> Dict[str, Any]:
    """单序列完整流程：末尾 horizon 留出 -> 拟合 -> 多步预测 -> 评估。"""
    y = np.asarray(y, dtype=np.float64).ravel()
    if horizon < 1:
        raise UsageError("horizon must be >= 1", horizon=int(horizon))
    n = y.size
    if n <= horizon + 2:
        raise ValidationError(
            f"series too short for horizon {horizon}", n=int(n), horizon=int(horizon))
    train, test = y[:n - horizon], y[n - horizon:]
    t_train = np.arange(train.size, dtype=np.float64)
    t_future = np.arange(train.size, train.size + horizon, dtype=np.float64)

    if method == "linear":
        slope, intercept = fit_linear(t_train, train)
        fc = slope * t_future + intercept
        model_params = {"slope": slope, "intercept": intercept}
    elif method == "poly":
        coeffs = fit_polynomial(t_train, train, degree)
        fc = eval_polynomial(coeffs, t_future)
        model_params = {"coefficients": coeffs.tolist()}
    elif method == "ar":
        coefs = fit_ar(train, order)
        fc = forecast_ar(train, coefs, horizon)
        model_params = {"ar_coefficients": coefs.tolist()}
    else:
        raise UsageError(f"unknown method '{method}'. Choose from: linear, poly, ar",
                         method=method)

    metrics = evaluate_forecast(fc, test)
    return {
        "method": method,
        "horizon": int(horizon),
        "train_len": int(train.size),
        "forecast": np.asarray(fc, dtype=np.float64),
        "actual": test,
        "metrics": metrics,
        "model_params": model_params,
    }


def forecast_cube(
    cube: np.ndarray,
    method: str = "linear",
    horizon: int = 4,
    degree: int = 2,
    order: int = 2,
    device=None,
) -> Tuple[np.ndarray, np.ndarray]:
    """逐像元时序预测。cube (T, H, W)。

    返回 (forecast_steps[horizon, H, W], pixel_rmse[H, W])——
    预测用前 T-horizon 步拟合，并与留出的末尾 horizon 步比较得到 RMSE。

    method='lstm' 时调用 torch LSTM；其它方法（linear/poly/ar）为可解释经典模型。
    """
    cube = np.asarray(cube, dtype=np.float64)
    if cube.ndim != 3:
        raise ValidationError("cube must be (T, H, W)", shape=list(cube.shape))
    T, H, W = cube.shape
    if horizon < 1 or T <= horizon + 2:
        raise ValidationError(
            f"need T > horizon + 2, got T={T}, horizon={horizon}",
            T=int(T), horizon=int(horizon))

    if method == "lstm":
        torch_mod = _require_torch()
        if device is None:
            device = _cuda_device(torch_mod)
        fc, rmse, _meta = _lstm_train_and_forecast(
            cube.astype(np.float32), device, horizon=horizon,
            window=min(8, max(1, T - horizon - 1)),
            hidden=16, epochs=12, batch=128, lr=2e-3,
        )
        return fc, rmse

    pix = cube.reshape(T, H * W)
    n_train = T - horizon
    train = pix[:n_train]
    test = pix[n_train:]
    t_train = np.arange(n_train, dtype=np.float64)
    t_future = np.arange(n_train, T, dtype=np.float64)

    if method == "linear":
        tm = t_train.mean()
        denom = float(np.sum((t_train - tm) ** 2))
        ym = train.mean(axis=0)
        slope = ((t_train - tm)[:, None] * (train - ym[None, :])).sum(axis=0) / denom
        intercept = ym - slope * tm
        fc = slope[None, :] * t_future[:, None] + intercept[None, :]
    elif method == "poly":
        coeffs = np.polyfit(t_train, train, degree)  # (deg+1, N)
        fc = np.zeros((horizon, H * W))
        for i, tf in enumerate(t_future):
            fc[i] = np.polyval(coeffs, tf)
    elif method == "ar":
        fc = np.zeros((horizon, H * W))
        for j in range(H * W):
            coefs = fit_ar(train[:, j], order)
            fc[:, j] = forecast_ar(train[:, j], coefs, horizon)
    else:
        raise UsageError(
            f"unknown method '{method}'. Choose from: lstm, linear, poly, ar",
            method=method)

    err = fc - test
    pixel_rmse = np.sqrt((err * err).mean(axis=0)).reshape(H, W)
    return fc.reshape(horizon, H, W), pixel_rmse


# ---------------------------------------------------------------------------
# 合成数据：趋势 + 季节 + 噪声的时序立方体
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    n_steps: int = 24,
    width: int = 48,
    height: int = 48,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (T, H, W) 的 NDVI 式时序：缓升趋势 + 年周期 + 噪声，值域 [0, 1]。"""
    rng = np.random.default_rng(seed)
    t = np.arange(n_steps, dtype=np.float64)
    yy, xx = np.mgrid[0:height, 0:width]
    base = 0.35 + 0.2 * (xx / max(width - 1, 1))
    trend = 0.004 * t[:, None, None] * (1.0 + 0.5 * (yy / max(height - 1, 1)))[None, :, :]
    season = 0.1 * np.sin(2 * np.pi * t / 12.0)[:, None, None]
    noise = rng.normal(0, 0.02, size=(n_steps, height, width))
    cube = base[None, :, :] + trend + season + noise
    cube = np.clip(cube, 0.0, 1.0).astype(np.float32)
    info = {"bbox": bbox, "n_steps": n_steps, "width": width, "height": height}
    return cube, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    arr = np.asarray(array, dtype=np.float32)
    if arr.ndim == 2:
        arr = arr[np.newaxis, ...]
    nb, h, w = arr.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(arr[b].astype("float32"), b + 1)


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
        inputs={
            "input": getattr(args, "input", None),
            "method": getattr(args, "method", None),
            "horizon": getattr(args, "horizon", None),
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

    # 1) bbox 校验（先于任何 IO）
    bbox = list(args.bbox) if args.bbox else None
    if bbox is not None:
        bbox = validate_bbox(bbox)

    # 2) horizon / n_steps 校验
    if args.horizon is None or int(args.horizon) < 1:
        raise ValidationError(
            f"horizon must be >= 1 (got {args.horizon})", horizon=args.horizon)
    if args.n_steps is not None and int(args.n_steps) < 3:
        raise ValidationError(
            f"n-steps must be >= 3 (got {args.n_steps})", n_steps=args.n_steps)
    if args.degree is not None and int(args.degree) < 1:
        raise UsageError(f"degree must be >= 1 (got {args.degree})", degree=args.degree)
    if args.order is not None and int(args.order) < 1:
        raise UsageError(f"order must be >= 1 (got {args.order})", order=args.order)

    os.makedirs(output_dir, exist_ok=True)

    # 3) 读取 / 生成
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)  # 波段 = 时间步
        bbox = bbox if bbox is not None else validate_bbox(file_bbox)
        series_cube = cube  # (bands=T, H, W)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        series_cube, _ = generate_synthetic(bbox, n_steps=args.n_steps, seed=args.seed)
        source_note = "synthetic"

    if series_cube.size == 0:
        raise ValidationError("input raster is empty")
    if series_cube.ndim == 2:
        series_cube = series_cube[np.newaxis, ...]
    # rasterio 约定 (bands, H, W)，bands = T
    T = series_cube.shape[0]
    if T <= args.horizon + 2:
        raise ValidationError(
            f"need more time steps: T={T} must exceed horizon+2={args.horizon + 2}")

    # 4) 预测（lstm 方法：torch + CUDA；其它：numpy 经典）
    lstm_meta: Dict[str, Any] = {}
    if args.method == "lstm":
        torch_mod = _require_torch()
        device = _cuda_device(torch_mod)
    else:
        device = None  # type: ignore[assignment]

    fc_steps, pixel_rmse = forecast_cube(
        series_cube, method=args.method, horizon=args.horizon,
        degree=args.degree, order=args.order, device=device,
    )

    fc_tif = os.path.join(output_dir, "forecast.tif")
    write_geotiff(fc_tif, fc_steps, bbox)
    rmse_tif = os.path.join(output_dir, "validation_rmse.tif")
    write_geotiff(rmse_tif, pixel_rmse.astype(np.float32), bbox)

    # 中心像元：从立方体预测中提取（避免另起小样本训练）
    h_mid, w_mid = series_cube.shape[1] // 2, series_cube.shape[2] // 2
    center_series = series_cube[:, h_mid, w_mid].astype(np.float64)
    if args.method == "lstm":
        # 直接用全局 cube-level 预测在中心像元位置上的结果
        fc_center = np.asarray(fc_steps[:, h_mid, w_mid], dtype=np.float64)
        actual_center = center_series[-args.horizon:].astype(np.float64)
        if actual_center.size < args.horizon:
            actual_center = np.concatenate([
                actual_center,
                np.full(args.horizon - actual_center.size, actual_center[-1], dtype=np.float64),
            ])
        center_result = {
            "forecast": fc_center,
            "actual": actual_center,
            "metrics": evaluate_forecast(fc_center, actual_center),
            "model_params": {"lstm": "global_cube_lstm_hidden16"},
        }
    else:
        center_result = forecast_series(
            center_series, method=args.method, horizon=args.horizon,
            degree=args.degree, order=args.order,
        )
    report = {
        "method": args.method,
        "horizon": args.horizon,
        "n_steps": int(T),
        "mean_pixel_rmse": float(np.mean(pixel_rmse)),
        "max_pixel_rmse": float(np.max(pixel_rmse)),
        "center_pixel": {
            "forecast": [float(x) for x in np.asarray(center_result["forecast"]).ravel().tolist()],
            "actual": [float(x) for x in np.asarray(center_result["actual"]).ravel().tolist()],
            "metrics": center_result["metrics"],
        },
    }
    report_path = os.path.join(output_dir, "forecast_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "horizon": args.horizon,
        "n_steps": int(T),
        "mean_pixel_rmse": report["mean_pixel_rmse"],
        "center_pixel_mae": center_result["metrics"]["mae"],
    }
    if args.method == "lstm":
        qa["backend"] = "torch lstm (many-to-one, recursive)"
        qa["device"] = str(device)

    outputs = [
        {"path": fc_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(args.horizon)},
        {"path": rmse_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  method: {args.method}  "
              f"steps: {T} -> +{args.horizon}")
        print(f"[{SKILL_NAME}] mean pixel RMSE (holdout): {report['mean_pixel_rmse']:.4f}")
        print(f"[{SKILL_NAME}] forecast: {fc_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Time-series forecasting (linear/poly/AR fit + multi-step forecast + validation).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF whose bands are time steps")
    p.add_argument("--method", default="lstm",
                   choices=["lstm", "linear", "poly", "ar"],
                   help="forecast method (default: lstm — torch LSTM on GPU; "
                        "linear/poly/ar are interpretable numpy baselines)")
    p.add_argument("--horizon", type=int, default=4, help="forecast steps (default: 4)")
    p.add_argument("--degree", type=int, default=2, help="polynomial degree (method=poly)")
    p.add_argument("--order", type=int, default=2, help="AR order (method=ar)")
    p.add_argument("--n-steps", type=int, default=24, help="synthetic series length")
    p.add_argument("--seed", type=int, default=42, help="seed for synthetic data")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic series (offline)")
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
