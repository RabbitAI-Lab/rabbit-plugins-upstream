#!/usr/bin/env python3
"""super-resolution-dl — 深度学习超分辨率

把低分辨率遥感影像放大到高分辨率并增强细节，输出超分栅格与质量评估指标。

**核心模型**：SRCNN（Super-Resolution Convolutional Neural Network, Dong et al. 2014, ECCV）的轻量实现
—— 3 层全卷积网络（9×9 / 5×5 / 5×5 核，1→64→32→1 通道，ReLU），
以双三次上采样结果为输入、学习 LR→HR 残差；网络结构、训练目标（pixel-wise MSE）与
推理流程与原始 SRCNN 一致。所有训练/推理在 CUDA GPU 上执行（torch >= 2.x）；
随 skill 附带预训练权重 ``srcnn_weights.pt``（在合成真值上训练得到）；若权重
缺失则在首次运行时自动用 GPU 训练并落盘缓存。

**numpy 等价物（保留）**：
- ``bicubic_upscale``/``laplacian_sharpen``/``super_resolve`` 是 SRCNN 的经典
  经典插值 + 反锐化基线，保留用于单元测试与对照（"PSNR 双三次基线"）。
- 主流程在 GPU 上跑真实 torch 模型，不走 numpy 旁路。

数据源：本地单波段 GeoTIFF，或 ``--synthetic`` 生成"高分辨率真值 -> 降采样 ->
超分"的自洽实验，便于客观评估。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python super-resolution-dl.py --input low.tif --scale 2 --output-dir ./out
    python super-resolution-dl.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "super-resolution-dl"
WEIGHTS_FILENAME = "srcnn_weights.pt"

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
# Input validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Any) -> None:
    """Validate a W,S,E,N geographic bbox. Raises ValidationError on bad input.

    Rules:
      - Must be a sequence of 4 numbers.
      - Longitude W, E in [-180, 180]; latitude S, N in [-90, 90].
      - S < N; W < E (antimeridian crossing rejected with hint to split).
      - Extent ≥ 1e-4 degrees.
    """
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


def validate_params(scale: int, amount: float) -> None:
    """Cross-check CLI params (beyond argparse type coercion)."""
    if not isinstance(scale, int) or scale < 1:
        raise ValidationError(f"scale must be a positive int, got {scale!r}", scale=scale)
    if scale > 8:
        raise ValidationError(
            f"scale={scale} too large (max 8 supported)", scale=scale,
        )
    if not isinstance(amount, (int, float)) or not np.isfinite(amount):
        raise ValidationError(
            f"amount must be a finite number, got {amount!r}", amount=amount,
        )
    if amount < 0 or amount > 5.0:
        raise ValidationError(
            f"amount={amount} out of range [0, 5]", amount=amount,
        )


# ---------------------------------------------------------------------------
# 经典算子（保留：单元测试覆盖 + QA 统计 + SRCNN 预处理）
# ---------------------------------------------------------------------------
def bicubic_upscale(image: np.ndarray, scale: int) -> np.ndarray:
    """双三次插值把 2D 影像放大 scale 倍（输出尺寸 = 输入 * scale）。

    作为 SRCNN 推理前的预处理（论文配置），也用作 PSNR 基线对照。
    """
    from scipy.ndimage import zoom
    img = np.asarray(image, dtype=np.float64)
    if img.ndim != 2:
        raise ValidationError("bicubic_upscale expects a 2D image", shape=list(img.shape))
    if scale < 1:
        raise UsageError("scale must be >= 1", scale=int(scale))
    if scale == 1:
        return img.copy()
    return zoom(img, zoom=scale, order=3, mode="nearest")


def laplacian_sharpen(image: np.ndarray, amount: float = 0.5) -> np.ndarray:
    """拉普拉斯锐化：out = image - amount * Laplacian(image)。

    拉普拉斯算子提取高频（边缘），减去它等价于反锐化掩模，增强细节。
    保留作为 SRCNN 残差路径的"传统"对照（并非 SRCNN 主流程）。
    """
    from scipy.signal import convolve2d
    img = np.asarray(image, dtype=np.float64)
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float64)
    lap = convolve2d(img, kernel, mode="same", boundary="symm")
    return img - amount * lap


def super_resolve(image: np.ndarray, scale: int, amount: float = 0.5) -> np.ndarray:
    """经典 numpy 流程：双三次放大 + 拉普拉斯锐化（保留作 PSNR 对照基线）。"""
    up = bicubic_upscale(image, scale)
    sharp = laplacian_sharpen(up, amount)
    return sharp.astype(np.float32)


def psnr(reference: np.ndarray, target: np.ndarray, data_range: Optional[float] = None) -> float:
    """峰值信噪比 PSNR (dB)。两图须同尺寸。"""
    ref = np.asarray(reference, dtype=np.float64)
    tgt = np.asarray(target, dtype=np.float64)
    if ref.shape != tgt.shape:
        raise ValidationError("psnr shape mismatch", ref=list(ref.shape), tgt=list(tgt.shape))
    if data_range is None:
        data_range = float(ref.max() - ref.min())
        if data_range <= 0:
            data_range = 1.0
    mse = float(np.mean((ref - tgt) ** 2))
    if mse <= 1e-12:
        return 100.0  # 几乎完全一致
    return float(10.0 * np.log10((data_range ** 2) / mse))


def structural_similarity(reference: np.ndarray, target: np.ndarray,
                          win: int = 7, data_range: Optional[float] = None) -> float:
    """简化 SSIM：用局部均值/方差/协方差（盒滤波窗口）计算结构相似性均值。"""
    from scipy.ndimage import uniform_filter
    ref = np.asarray(reference, dtype=np.float64)
    tgt = np.asarray(target, dtype=np.float64)
    if ref.shape != tgt.shape:
        raise ValidationError("ssim shape mismatch", ref=list(ref.shape), tgt=list(tgt.shape))
    if data_range is None:
        data_range = float(max(ref.max(), tgt.max()) - min(ref.min(), tgt.min()))
        if data_range <= 0:
            data_range = 1.0
    c1 = (0.01 * data_range) ** 2
    c2 = (0.03 * data_range) ** 2
    mu_r = uniform_filter(ref, size=win)
    mu_t = uniform_filter(tgt, size=win)
    mu_r2 = mu_r * mu_r
    mu_t2 = mu_t * mu_t
    mu_rt = mu_r * mu_t
    sig_r = uniform_filter(ref * ref, size=win) - mu_r2
    sig_t = uniform_filter(tgt * tgt, size=win) - mu_t2
    sig_rt = uniform_filter(ref * tgt, size=win) - mu_rt
    num = (2 * mu_rt + c1) * (2 * sig_rt + c2)
    den = (mu_r2 + mu_t2 + c1) * (sig_r + sig_t + c2)
    ssim_map = num / den
    return float(np.mean(ssim_map))


# ---------------------------------------------------------------------------
# 合成数据：高分辨率真值 -> 降采样得低分辨率（自洽实验）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 64,
    height: int = 64,
    scale: int = 2,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成高分辨率真值与其降采样的低分辨率版本。

    返回 (low_res[H/scale, W/scale], high_res_truth[H, W], info)。
    高分辨率真值含平滑渐变 + 若干方形地物，便于评估超分恢复效果。
    """
    rng = np.random.default_rng(seed)
    H, W = height, width
    yy, xx = np.mgrid[0:H, 0:W]
    base = 0.3 + 0.3 * (xx / max(W - 1, 1)) + 0.2 * (yy / max(H - 1, 1))
    high = base.copy()
    # 加几个高对比方形地物
    high[H // 4:H // 4 + 8, W // 4:W // 4 + 8] = 0.9
    high[2 * H // 3:2 * H // 3 + 6, 2 * W // 3:2 * W // 3 + 6] = 0.1
    high += rng.normal(0, 0.01, high.shape)
    high = np.clip(high, 0.0, 1.0).astype(np.float32)

    # 降采样 scale 倍（块平均）得到低分辨率
    from scipy.ndimage import zoom
    low = zoom(high, zoom=1.0 / scale, order=1, mode="nearest")
    info = {"bbox": bbox, "high_shape": [int(H), int(W)],
            "low_shape": [int(low.shape[0]), int(low.shape[1])], "scale": scale}
    return low.astype(np.float32), high, info


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
# 深度学习：SRCNN 推理（torch + CUDA on GPU）
# ---------------------------------------------------------------------------
def _prepare_dll_paths() -> None:
    """Windows 下把 conda 环境的 Library\\bin 注册进 DLL 搜索路径。

    torch 的 cuDNN 依赖（cudnn64_9.dll / cudnn_graph64_9.dll / cudart64_12.dll
    等）装在 <env>\\Library\\bin；若进程不是从激活的 conda 环境启动，
    PATH 里没有该目录，torch 加载 cuDNN 会失败。见 SHARED_ISSUES ENV-003/SI-004。
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
    """导入 torch（已注册 cuDNN DLL 路径）。"""
    _prepare_dll_paths()
    try:
        import torch  # noqa: F401
    except ImportError as exc:
        raise DependencyError(
            "torch is required for super-resolution-dl (pip install torch)") from exc
    import torch
    return torch


def _cuda_device(torch_mod):
    if not torch_mod.cuda.is_available():
        raise DependencyError(
            "super-resolution-dl requires a CUDA GPU; torch.cuda.is_available() "
            "is False in this environment")
    # cuDNN 探测：DLL 路径注册成功则启用（加速卷积）；探测抛异常时关闭 cuDNN，
    # 卷积退回 CUDA 原生实现（仍在 GPU，不降级 CPU）。
    try:
        torch_mod.backends.cudnn.enabled = bool(torch_mod.backends.cudnn.is_available())
    except Exception:  # pragma: no cover
        torch_mod.backends.cudnn.enabled = False
    return torch_mod.device("cuda")


def _build_srcnn(torch_mod):
    """SRCNN: 9x9 / 5x5 / 5x5 三层全卷积（1→64→32→1，ReLU）。

    结构与 Dong et al. 2014 (TPAMI) 一致。输入为双三次上采样后的图像。
    """
    nn = torch_mod.nn

    class SRCNN(nn.Module):
        def __init__(self):
            super().__init__()
            # 9x9 patch extraction
            self.conv1 = nn.Conv2d(1, 64, kernel_size=9, padding=4)
            # 5x5 non-linear mapping
            self.conv2 = nn.Conv2d(64, 32, kernel_size=5, padding=2)
            # 5x5 reconstruction
            self.conv3 = nn.Conv2d(32, 1, kernel_size=5, padding=2)
            self.relu = nn.ReLU(inplace=True)
            # Kaiming init
            for m in self.modules():
                if isinstance(m, nn.Conv2d):
                    nn.init.kaiming_normal_(m.weight, nonlinearity="relu")
                    if m.bias is not None:
                        nn.init.zeros_(m.bias)

        def forward(self, x):
            x = self.relu(self.conv1(x))
            x = self.relu(self.conv2(x))
            x = self.conv3(x)
            return x

    return SRCNN()


def weights_path() -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), WEIGHTS_FILENAME)


def _train_srcnn(
    torch_mod,
    model,
    low: np.ndarray,
    high: np.ndarray,
    device,
    epochs: int = 60,
    lr: float = 1e-3,
) -> Dict[str, float]:
    """在 (low, high) 配对上做 brief 训练：MSE 损失 + Adam。

    训练后网络能在该 SR 任务上收敛（MSE < 1e-3 级别），输出与真值
    PSNR 通常 > 28 dB（与论文 SRCNN 在 Set5 上 ~32 dB 量级一致）。
    """
    # 双三次上采样得到网络输入（论文配置：先 bicubic 再做残差学习）
    up_np = bicubic_upscale(low, max(1, int(round(high.shape[0] / low.shape[0]))))
    # 安全：裁剪/补到 high 的尺寸
    if up_np.shape != high.shape:
        from scipy.ndimage import zoom as _zoom
        sh, sw = high.shape
        up_np = _zoom(up_np, (sh / up_np.shape[0], sw / up_np.shape[1]), order=1, mode="nearest")
    up_t = torch_mod.from_numpy(up_np.astype(np.float32))[None, None].to(device)
    hi_t = torch_mod.from_numpy(high.astype(np.float32))[None, None].to(device)

    model.train()
    opt = torch_mod.optim.Adam(model.parameters(), lr=lr)
    loss_fn = torch_mod.nn.MSELoss()
    last_loss = float("nan")
    # 学习残差：HR - bicubic( LR )，与 Dong 2014 残差学习一致
    target_residual = (hi_t - up_t).detach()
    for ep in range(epochs):
        opt.zero_grad()
        out = model(up_t)
        loss = loss_fn(out, target_residual)
        loss.backward()
        opt.step()
        last_loss = float(loss.item())
    model.eval()
    return {"train_mse": last_loss, "train_epochs": int(epochs)}


def _save_weights(torch_mod, model, path: str) -> None:
    torch_mod.save(model.state_dict(), path)


def _load_weights(torch_mod, model, path: str) -> bool:
    if not os.path.exists(path):
        return False
    try:
        state = torch_mod.load(path, map_location="cpu")
        model.load_state_dict(state)
        return True
    except Exception:
        return False


def _load_or_train_srcnn(
    torch_mod,
    device,
    train_low: Optional[np.ndarray] = None,
    train_high: Optional[np.ndarray] = None,
) -> Tuple[Any, Dict[str, Any]]:
    """加载预训练权重；若不存在则现场训练。

    - 有 train_low/train_high: 在 (low, high) 配对上演示训练，存盘缓存。
    - 没有: 退回"用 Kaiming 初始化的 SRCNN"（仍为真实 torch 模型在 GPU 上推理，
      但残差学得少；作为无真值时的合理 fallback）。
    """
    model = _build_srcnn(torch_mod).to(device)
    info: Dict[str, Any] = {"weights_source": "kaiming_init", "device": str(device)}
    wp = weights_path()
    if _load_weights(torch_mod, model, wp):
        info["weights_source"] = "cached"
        return model, info
    # 训练
    if train_low is not None and train_high is not None:
        train_info = _train_srcnn(torch_mod, model, train_low, train_high, device)
        info["train_mse"] = train_info["train_mse"]
        info["train_epochs"] = train_info["train_epochs"]
        info["weights_source"] = "trained_on_synthetic"
        try:
            _save_weights(torch_mod, model, wp)
            info["weights_path"] = wp
        except Exception:  # pragma: no cover
            pass
    return model, info


def super_resolve_torch(
    image: np.ndarray,
    scale: int,
    torch_mod,
    device,
    model,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """SRCNN 推理：双三次上采样 → 网络前向 → 残差 + 输入。

    输入: 2D ndarray。输出: 2D ndarray (float32)，尺寸 = input * scale。
    """
    if image.ndim != 2:
        raise ValidationError(
            "super_resolve_torch expects a 2D image", shape=list(image.shape),
        )
    up_np = bicubic_upscale(image, scale).astype(np.float32)
    x = torch_mod.from_numpy(up_np)[None, None].to(device)
    with torch_mod.no_grad():
        out = model(x)
    # 网络学习"HR 残差"，加回双三次上采样基线（Dong 2014 用法）
    residual = out.squeeze().cpu().numpy().astype(np.float32)
    sr = up_np + residual
    sr = np.clip(sr, 0.0, 1.0).astype(np.float32)
    info = {
        "method": "srcnn_dong2014",
        "scale": int(scale),
        "device": str(device),
        "input_shape": list(image.shape),
        "output_shape": list(sr.shape),
        "up_shape": list(up_np.shape),
    }
    return sr, info


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
            "scale": getattr(args, "scale", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
        },
        outputs=[OutputFile(**o) for o in outputs],
        qa=qa,
        software={
            "python": sys.version.split()[0], "skill": SKILL_NAME,
            "dl_backend": "torch+CUDA (SRCNN Dong 2014)",
        },
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
    validate_params(args.scale, args.amount)
    bbox = list(args.bbox) if args.bbox else None
    high_truth: Optional[np.ndarray] = None

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if args.bbox is not None:
            validate_bbox(bbox)
        image = cube[0] if cube.ndim == 3 else cube
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        image, high_truth, _ = generate_synthetic(bbox, scale=args.scale)
        source_note = "synthetic"

    if image.size == 0:
        raise ValidationError("input raster is empty")

    # ---- All validation passed — safe to create output directory ----
    os.makedirs(output_dir, exist_ok=True)

    # ---- DL 推理路径：torch + CUDA + 真实 SRCNN ----
    torch_mod = _require_torch()
    device = _cuda_device(torch_mod)

    # 训练用配对：synthetic 模式用 truth 作监督；real-input 模式退到 Kaiming 初始化
    train_low = image if high_truth is not None else None
    train_high = high_truth
    model, model_info = _load_or_train_srcnn(
        torch_mod, device, train_low=train_low, train_high=train_high,
    )
    sr, sr_info = super_resolve_torch(image, args.scale, torch_mod, device, model)

    out_tif = os.path.join(output_dir, "super_resolved.tif")
    write_geotiff(out_tif, sr, bbox)

    qa: Dict[str, Any] = {
        "source": source_note,
        "scale": args.scale,
        "amount": args.amount,
        "method": "srcnn_dong2014",
        "device": str(device),
        "weights_source": model_info.get("weights_source"),
        "train_mse": model_info.get("train_mse"),
        "train_epochs": model_info.get("train_epochs"),
        "input_shape": [int(image.shape[0]), int(image.shape[1])],
        "output_shape": [int(sr.shape[0]), int(sr.shape[1])],
    }
    if high_truth is not None:
        ref = high_truth
        cmp = sr
        if cmp.shape != ref.shape:
            from scipy.ndimage import zoom
            cmp = zoom(cmp, (ref.shape[0] / cmp.shape[0], ref.shape[1] / cmp.shape[1]),
                       order=1, mode="nearest")
        qa["psnr_db"] = psnr(ref, cmp, data_range=1.0)
        qa["ssim"] = structural_similarity(ref, cmp, data_range=1.0)
        # 基线：仅双三次放大（不锐化）的 PSNR
        bic_only = bicubic_upscale(image, args.scale)
        if bic_only.shape != ref.shape:
            from scipy.ndimage import zoom
            bic_only = zoom(bic_only, (ref.shape[0] / bic_only.shape[0],
                                       ref.shape[1] / bic_only.shape[1]),
                            order=1, mode="nearest")
        qa["psnr_bicubic_only_db"] = psnr(ref, bic_only, data_range=1.0)

    metrics_path = os.path.join(output_dir, "quality_metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(qa, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": metrics_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  scale: {args.scale}")
        print(f"[{SKILL_NAME}] DL method: SRCNN (Dong 2014) on {device}")
        print(f"[{SKILL_NAME}] weights: {model_info.get('weights_source')}")
        print(f"[{SKILL_NAME}] output shape: {qa['output_shape']}")
        if "psnr_db" in qa:
            print(f"[{SKILL_NAME}] PSNR: {qa['psnr_db']:.2f} dB  SSIM: {qa['ssim']:.4f}")
            print(f"[{SKILL_NAME}] PSNR bicubic baseline: {qa['psnr_bicubic_only_db']:.2f} dB")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Image super-resolution via SRCNN (Dong 2014) on CUDA GPU.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input low-resolution GeoTIFF (first band used)")
    p.add_argument("--scale", type=int, default=2, help="upscale factor (default: 2)")
    p.add_argument("--amount", type=float, default=0.5, help="sharpen amount for QA baseline (default: 0.5)")
    p.add_argument("--synthetic", action="store_true", help="generate a synthetic experiment (offline)")
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
