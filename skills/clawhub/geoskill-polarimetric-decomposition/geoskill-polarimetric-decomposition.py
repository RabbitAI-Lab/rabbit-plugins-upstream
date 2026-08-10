#!/usr/bin/env python3
"""polarimetric-decomposition — 极化SAR分解

对全极化 SAR 数据执行极化目标分解，提取散射物理信息。实现两类主流方法：

- **Cloude-Pottier（H/A/α，特征分解）**：对每个像元的 3×3 相干矩阵 T3 做
  Hermitian 特征分解（``np.linalg.eigh``），得到三个特征值 λ1≥λ2≥λ3，进而计算
  - 熵 H = −Σ pᵢ·log₃(pᵢ)，pᵢ = λᵢ/Σλ，表征散射随机性，H∈[0,1]；
  - 各向异性 A = (λ2−λ3)/(λ2+λ3)，衡量次要散射机制的相对权重；
  - 散射角 α = Σ pᵢ·αᵢ，αᵢ = arccos(|eᵢ[0]|)，区分表面(α≈0-30°)、
    体散射(α≈40-60°)与二面角散射(α≈90°)。
- **Freeman-Durden 三分量（简化）**：从 |Shh|²、|Svv|²、|Shv|² 三通道
  求解表面散射 Ps、二面角散射 Pd 与体散射 Pv（Pv ≈ 2·|Shv|²，剩余能量按
  HH/VV 不对称性分配到 Ps、Pd）。

输入约定：
- Cloude / H/A/α：输入 GeoTIFF 需含 9 个波段，按 T3 上三角编码
  [T11, T22, T33, Re T12, Im T12, Re T13, Im T13, Re T23, Im T23]（对角为实数）。
- Freeman：输入 GeoTIFF 需含 3 个波段 [|Shh|², |Svv|², |Shv|²]。
使用 ``--synthetic`` 可生成物理一致的模拟极化场景（表面/体/二面角三分区），离线测试。

隐私声明 / Privacy：
- 默认离线运行，仅在显式解析地名时才访问网络。
- ``--synthetic`` 模式完全无网络。所有处理在本地完成，不上传任何用户数据。

Usage:
    python polarimetric-decomposition.py --bbox 116 39 117 40 --method cloude --output-dir ./out
    python polarimetric-decomposition.py --input T3.tif --method ha_alpha --output-dir ./out

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
SKILL_NAME = "polarimetric-decomposition"

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
# Validation helpers
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float], source: str = "bbox") -> None:
    """Validate geographic bbox: W<=E, S<=N, lon/lat in range, min area.

    Cross-dateline (W>E) is a ValidationError with a hint to split.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(f"{source}: expected 4 floats [W S E N], got {bbox!r}")
    try:
        w, s, e, n = (float(v) for v in bbox)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"{source}: non-numeric bbox values: {bbox!r}") from exc
    for v, name in ((w, "W"), (s, "S"), (e, "E"), (n, "N")):
        if not (v == v):
            raise ValidationError(f"{source}: bbox contains NaN at {name}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"{source}: lon out of [-180,180]: W={w} E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"{source}: lat out of [-90,90]: S={s} N={n}")
    if w > e:
        raise ValidationError(
            f"{source}: W ({w}) > E ({e}); cross-dateline bboxes are not supported. "
            "Split into two bboxes on each side of the 180\u00b0 meridian and run separately."
        )
    if s > n:
        raise ValidationError(f"{source}: S ({s}) > N ({n})")
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"{source}: bbox too small (dlon={e - w}, dlat={n - s}); need > 1e-9 degrees"
        )


# ---------------------------------------------------------------------------
# T3 编码 <-> 复相干矩阵 互转
# 波段顺序：[T11, T22, T33, Re T12, Im T12, Re T13, Im T13, Re T23, Im T23]
# 对角元为实数（Hermitian 矩阵性质）。
# ---------------------------------------------------------------------------
def bands_to_T3(cube: np.ndarray) -> np.ndarray:
    """把 (9, H, W) 实数波段堆栈重建为 (H, W, 3, 3) 复 Hermitian 矩阵 T3。"""
    if cube.ndim != 3 or cube.shape[0] != 9:
        raise ValidationError(
            f"Cloude/H-A/alpha requires 9 input bands (T3 encoding), got {cube.shape[0] if cube.ndim == 3 else cube.ndim}",
        )
    T11, T22, T33 = cube[0], cube[1], cube[2]
    h, w = T11.shape
    T = np.zeros((h, w, 3, 3), dtype=np.complex128)
    T[..., 0, 0] = T11
    T[..., 1, 1] = T22
    T[..., 2, 2] = T33
    T12 = cube[3] + 1j * cube[4]
    T13 = cube[5] + 1j * cube[6]
    T23 = cube[7] + 1j * cube[8]
    T[..., 0, 1] = T12
    T[..., 1, 0] = np.conj(T12)
    T[..., 0, 2] = T13
    T[..., 2, 0] = np.conj(T13)
    T[..., 1, 2] = T23
    T[..., 2, 1] = np.conj(T23)
    return T


def T3_to_bands(T: np.ndarray) -> np.ndarray:
    """把 (H, W, 3, 3) 复 T3 压成 (9, H, W) 实数波段堆栈（bands_to_T3 的逆）。"""
    h, w = T.shape[0], T.shape[1]
    out = np.zeros((9, h, w), dtype=np.float32)
    out[0] = T[..., 0, 0].real
    out[1] = T[..., 1, 1].real
    out[2] = T[..., 2, 2].real
    out[3] = T[..., 0, 1].real
    out[4] = T[..., 0, 1].imag
    out[5] = T[..., 0, 2].real
    out[6] = T[..., 0, 2].imag
    out[7] = T[..., 1, 2].real
    out[8] = T[..., 1, 2].imag
    return out


# ---------------------------------------------------------------------------
# 核心算法 1：Cloude-Pottier H/A/α 特征分解
# ---------------------------------------------------------------------------
def cloude_pottier(T: np.ndarray) -> Dict[str, np.ndarray]:
    """对 (H, W, 3, 3) 相干矩阵做 Cloude-Pottier 分解。

    返回 dict，含 H（熵）、A（各向异性）、alpha/beta/delta/gamma（角度，度）
    以及三个特征值 lambda1/2/3。H∈[0,1]，alpha∈[0,90]。
    """
    if T.ndim != 4 or T.shape[-2:] != (3, 3):
        raise ValidationError(f"expected (H,W,3,3) coherency matrix, got {T.shape}")

    # NaN safety: if any of the 9 input bands is NaN at a given pixel, the
    # reconstructed T3 is not PSD, eigh returns NaN/garbage, and entropy
    # becomes NaN/-Inf. We identify such pixels *before* the eigh and
    # substitute the T3 with a benign diagonal so the result is well-defined
    # (we then zero-out the outputs at those pixels at the end).
    nan_mask = ~np.isfinite(T).all(axis=(-2, -1))  # (H, W)
    if nan_mask.any():
        n_clean = int((~nan_mask).sum())
        if n_clean < 1:
            raise ValidationError(
                f"need at least 1 valid (non-NoData) pixel for Cloude-Pottier; got {n_clean}"
            )
        T_safe = np.where(nan_mask[..., np.newaxis, np.newaxis],
                          np.eye(3, dtype=T.dtype)[np.newaxis, np.newaxis, :, :] * 1e-12,
                          T)
    else:
        T_safe = T

    # eigh 返回升序特征值，需翻转为降序 λ1≥λ2≥λ3
    evals, evecs = np.linalg.eigh(T_safe)
    evals = np.clip(evals[..., ::-1], 0.0, None)
    evecs = evecs[..., ::-1]

    span = evals.sum(axis=-1)
    span_safe = np.where(span > 0, span, 1.0)
    p = evals / span_safe[..., np.newaxis]  # (H,W,3)

    # 熵 H = -Σ p_i log3(p_i)，处理 p_i=0 → 0·log0 = 0
    log3p = np.where(p > 0, np.log(np.where(p > 0, p, 1.0)) / np.log(3.0), 0.0)
    entropy = -np.sum(p * log3p, axis=-1)
    entropy = np.where(span > 0, entropy, 0.0)

    l1, l2, l3 = evals[..., 0], evals[..., 1], evals[..., 2]
    denom = l2 + l3
    anisotropy = np.divide(l2 - l3, denom, out=np.zeros_like(denom), where=denom > 0)

    # 散射角 α_i = arccos(|e_i[0]|)，加权平均
    alpha_i = np.arccos(np.clip(np.abs(evecs[..., 0, :]), 0.0, 1.0))  # (H,W,3) 弧度
    beta_i = np.arccos(np.clip(np.abs(evecs[..., 1, :]), 0.0, 1.0))
    delta_i = np.angle(evecs[..., 0, :] * np.conj(evecs[..., 1, :]))
    gamma_i = np.angle(evecs[..., 0, :] * np.conj(evecs[..., 2, :]))

    alpha = np.sum(p * alpha_i, axis=-1)
    beta = np.sum(p * beta_i, axis=-1)
    delta = np.sum(p * delta_i, axis=-1)
    gamma = np.sum(p * gamma_i, axis=-1)

    deg = 180.0 / np.pi
    out = {
        "entropy": entropy.astype(np.float32),
        "anisotropy": anisotropy.astype(np.float32),
        "alpha": (alpha * deg).astype(np.float32),
        "beta": (beta * deg).astype(np.float32),
        "delta": (delta * deg).astype(np.float32),
        "gamma": (gamma * deg).astype(np.float32),
        "lambda1": l1.astype(np.float32),
        "lambda2": l2.astype(np.float32),
        "lambda3": l3.astype(np.float32),
    }
    # Zero out NoData pixels in the output arrays
    if nan_mask.any():
        mask_f = nan_mask.astype(np.float32)
        for k, v in out.items():
            out[k] = v * (1.0 - mask_f)
    out["n_valid_pixels"] = int((~nan_mask).sum())
    return out


# ---------------------------------------------------------------------------
# 核心算法 2：Freeman-Durden 三分量（简化求解）
# ---------------------------------------------------------------------------
def freeman_three_component(
    c11: np.ndarray, c22: np.ndarray, c33: np.ndarray,
) -> Dict[str, np.ndarray]:
    """从 |Shh|²(C11)、|Svv|²(C22)、|Shv|²(C33) 求解三分量散射功率。

    简化模型：
    - 体散射 Pv = 2·C33（交叉极化主要来自体散射）；
    - 扣除体散射贡献后，HH 剩余记为表面散射 Ps；
    - VV 相对 HH 的剩余（二面角使 VV 增强）记为二面角散射 Pd。
    返回 Ps（surface）、Pd（double-bounce）、Pv（volume）与总功率 span。
    """
    c11 = np.asarray(c11, dtype=np.float32)
    c22 = np.asarray(c22, dtype=np.float32)
    c33 = np.asarray(c33, dtype=np.float32)
    # NaN safety: a NoData pixel in any of the three channels forces the
    # three components and span to 0 there, so the per-pixel fraction
    # statistics remain on the valid data.
    nan_mask = ~(np.isfinite(c11) & np.isfinite(c22) & np.isfinite(c33))
    n_valid = int((~nan_mask).sum())
    if n_valid < 1:
        raise ValidationError(
            f"need at least 1 valid (non-NoData) pixel for Freeman-Durden; got {n_valid}"
        )
    c11s = np.where(nan_mask, 0.0, c11)
    c22s = np.where(nan_mask, 0.0, c22)
    c33s = np.where(nan_mask, 0.0, c33)
    pv = 2.0 * np.maximum(c33s, 0.0)
    res_hh = np.maximum(c11s - pv / 2.0, 0.0)
    res_vv = np.maximum(c22s - pv / 2.0, 0.0)
    pd = np.maximum(res_vv - res_hh, 0.0)
    ps = res_hh
    span = ps + pd + pv
    return {
        "Ps": ps.astype(np.float32),
        "Pd": pd.astype(np.float32),
        "Pv": pv.astype(np.float32),
        "span": span.astype(np.float32),
        "n_valid_pixels": n_valid,
    }


# ---------------------------------------------------------------------------
# 合成数据：物理一致的模拟极化场景（离线测试）
# ---------------------------------------------------------------------------
def _gram_schmidt_unitary(e1: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """构造以 e1 为第一列的 3×3 酉矩阵（复 Gram-Schmidt）。"""
    e1 = e1 / np.linalg.norm(e1)
    V = np.zeros((3, 3), dtype=np.complex128)
    V[:, 0] = e1
    for j in (1, 2):
        v = rng.normal(size=3) + 1j * rng.normal(size=3)
        for k in range(j):
            v = v - V[:, k] * np.vdot(V[:, k], v)
        n = np.linalg.norm(v)
        if n < 1e-9:  # 退化时回退到坐标基
            v = np.zeros(3, dtype=np.complex128)
            v[j] = 1.0
            for k in range(j):
                v = v - V[:, k] * np.vdot(V[:, k], v)
            n = np.linalg.norm(v)
        V[:, j] = v / n
    return V


def _scatter_vector(alpha_deg: float, beta_deg: float, gamma_deg: float) -> np.ndarray:
    """由 (α, β, γ) 构造 Pauli 基下的单位散射向量。"""
    a = np.deg2rad(alpha_deg)
    b = np.deg2rad(beta_deg)
    g = np.deg2rad(gamma_deg)
    return np.array([
        np.cos(a),
        np.sin(a) * np.cos(b) * np.exp(1j * g),
        np.sin(a) * np.sin(b) * np.exp(1j * g),
    ], dtype=np.complex128)


def _make_T(e1: np.ndarray, eigvals: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """以 e1 为主特征向量、eigvals（降序）为特征值构造 3×3 Hermitian PSD 矩阵。"""
    V = _gram_schmidt_unitary(e1, rng)
    return (V * eigvals) @ V.conj().T


def generate_synthetic_T3(
    bbox: List[float], width: int = 64, height: int = 64, seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (9, H, W) 的 T3 编码场景：左=表面散射，中=体散射，右=二面角散射。

    每区有指定的主散射角 α 与特征值分布，从而得到物理可分的 H/α。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float32) / max(width - 1, 1)

    # 三分区散射机制：(alpha_deg, beta, gamma, [l1,l2,l3])
    zones = [
        (12.0, 30.0, 10.0, np.array([1.00, 0.08, 0.03])),   # 表面：低熵、低 α
        (50.0, 45.0, 60.0, np.array([1.00, 0.92, 0.85])),   # 体散射：高熵、中 α
        (82.0, 20.0, 90.0, np.array([1.00, 0.15, 0.05])),   # 二面角：低熵、高 α
    ]
    T = np.zeros((height, width, 3, 3), dtype=np.complex128)
    zone_map = np.zeros((height, width), dtype=np.int32)
    for y in range(height):
        for x in range(width):
            z = 0 if xn[y, x] < 1.0 / 3.0 else (1 if xn[y, x] < 2.0 / 3.0 else 2)
            zone_map[y, x] = z
            a, b, g, base = zones[z]
            eig = base * (1.0 + 0.05 * rng.standard_normal())
            eig = np.sort(np.abs(eig))[::-1]
            e1 = _scatter_vector(a, b, g)
            T[y, x] = _make_T(e1, eig, rng)

    cube = T3_to_bands(T)
    truth = {
        "zone_0_surface_alpha_deg": zones[0][0],
        "zone_1_volume_alpha_deg": zones[1][0],
        "zone_2_double_alpha_deg": zones[2][0],
        "zone_alpha_mean_deg": float(np.mean([z[0] for z in zones])),
    }
    info = {"bbox": bbox, "width": width, "height": height, "encoding": "T3-9band",
            "truth": truth}
    return cube, info


def generate_synthetic_C3(
    bbox: List[float], width: int = 64, height: int = 64, seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (3, H, W) 的 [|Shh|², |Svv|², |Shv|²] 场景，三分区对应不同散射机制。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float32) / max(width - 1, 1)

    # (|Shh|², |Svv|², |Shv|²) 典型值
    zones = [
        (1.00, 0.30, 0.04),  # 表面：HH 主导
        (0.80, 0.80, 0.50),  # 体散射：HV 高、HH≈VV
        (0.50, 1.30, 0.04),  # 二面角：VV 增强
    ]
    c11 = np.zeros((height, width), dtype=np.float32)
    c22 = np.zeros((height, width), dtype=np.float32)
    c33 = np.zeros((height, width), dtype=np.float32)
    for y in range(height):
        for x in range(width):
            z = 0 if xn[y, x] < 1.0 / 3.0 else (1 if xn[y, x] < 2.0 / 3.0 else 2)
            hh, vv, hv = zones[z]
            mul = np.exp(0.05 * rng.standard_normal())
            c11[y, x] = hh * mul
            c22[y, x] = vv * mul
            c33[y, x] = hv * mul

    cube = np.stack([c11, c22, c33], axis=0)
    info = {"bbox": bbox, "width": width, "height": height, "encoding": "C3-3band",
            "truth": {"zones_shh_svv_shv": [list(z) for z in zones]}}
    return cube, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0) -> None:
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
        skill=SKILL_NAME,
        skill_version=VERSION,
        command=cmd,
        started_at=started_at,
        finished_at=_utc_now(),
        exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "method": getattr(args, "method", None),
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
    os.makedirs(output_dir, exist_ok=True)

    bbox = list(args.bbox) if args.bbox else None
    method = args.method
    need_T3 = method in ("cloude", "ha_alpha")

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
        expected = 9 if need_T3 else 3
        if cube.ndim != 3 or cube.shape[0] != expected:
            raise ValidationError(
                f"method '{method}' needs {expected} bands, input has "
                f"{cube.shape[0] if cube.ndim == 3 else 1}",
            )
        # Replace NoData sentinel with NaN across the cube so the T3
        # eigendecomposition / Freeman split does not see -9999 as a real
        # coherence value (it would otherwise produce negative eigenvalues and
        # corrupt the entropy/alpha statistics).
        import rasterio as _rio
        with _rio.open(args.input) as _src:
            _nd = _src.nodata
        if _nd is not None:
            cube = np.where(cube == _nd, np.nan, cube).astype(np.float32)
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox, source="--bbox")
        if need_T3:
            cube, synth_info = generate_synthetic_T3(bbox)
        else:
            cube, synth_info = generate_synthetic_C3(bbox)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    # If --bbox is also given with --input, validate the user-supplied bbox
    if bbox is not None and args.bbox is not None:
        validate_bbox(bbox, source="--bbox")

    # 分解
    if need_T3:
        T = bands_to_T3(cube)
        decomp = cloude_pottier(T)
        out_cube = np.stack(
            [decomp["entropy"], decomp["anisotropy"], decomp["alpha"]], axis=0,
        ).astype(np.float32)
        band_names = ["entropy_H", "anisotropy_A", "alpha_deg"]
        # NaN-aware statistics
        valid_e = decomp["entropy"][np.isfinite(decomp["entropy"])]
        valid_a = decomp["alpha"][np.isfinite(decomp["alpha"])]
        valid_an = decomp["anisotropy"][np.isfinite(decomp["anisotropy"])]
        stats = {
            "entropy_mean": float(np.mean(valid_e)) if valid_e.size else 0.0,
            "entropy_range": [float(np.min(valid_e)) if valid_e.size else 0.0,
                              float(np.max(valid_e)) if valid_e.size else 0.0],
            "anisotropy_mean": float(np.mean(valid_an)) if valid_an.size else 0.0,
            "alpha_mean_deg": float(np.mean(valid_a)) if valid_a.size else 0.0,
            "alpha_range_deg": [float(np.min(valid_a)) if valid_a.size else 0.0,
                                float(np.max(valid_a)) if valid_a.size else 0.0],
        }
        qa = {
            "source": source_note, "method": method,
            "n_bands_out": 3, "band_names": band_names,
            "entropy_mean": stats["entropy_mean"],
            "alpha_mean_deg": stats["alpha_mean_deg"],
            "entropy_in_range": bool(0.0 <= stats["entropy_mean"] <= 1.0),
            "alpha_in_range": bool(0.0 <= stats["alpha_mean_deg"] <= 90.0),
            "n_valid_pixels": int(decomp.get("n_valid_pixels", 0)),
        }
        out_name = "cloude_H_A_alpha.tif"
    else:
        free = freeman_three_component(cube[0], cube[1], cube[2])
        out_cube = np.stack([free["Ps"], free["Pd"], free["Pv"]], axis=0).astype(np.float32)
        band_names = ["Ps_surface", "Pd_double", "Pv_volume"]
        total = float(np.sum(free["span"])) or 1.0
        stats = {
            "Ps_sum": float(np.sum(free["Ps"])),
            "Pd_sum": float(np.sum(free["Pd"])),
            "Pv_sum": float(np.sum(free["Pv"])),
            "span_sum": float(np.sum(free["span"])),
            "Ps_fraction": float(np.sum(free["Ps"]) / total),
            "Pd_fraction": float(np.sum(free["Pd"]) / total),
            "Pv_fraction": float(np.sum(free["Pv"]) / total),
        }
        qa = {
            "source": source_note, "method": method,
            "n_bands_out": 3, "band_names": band_names,
            "Ps_fraction": stats["Ps_fraction"],
            "Pd_fraction": stats["Pd_fraction"],
            "Pv_fraction": stats["Pv_fraction"],
            "n_valid_pixels": int(free.get("n_valid_pixels", 0)),
        }
        out_name = "freeman_three_component.tif"

    # 写出产物
    out_tif = os.path.join(output_dir, out_name)
    write_geotiff(out_tif, out_cube, bbox)

    stats_out = {"method": method, "band_names": band_names, "statistics": stats}
    if synth_info is not None:
        stats_out["synthetic_truth"] = synth_info.get("truth")
    stats_path = os.path.join(output_dir, "decomposition_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats_out, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(out_cube.shape[0])},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {method}  output bands: {band_names}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        print(f"[{SKILL_NAME}] stats:  {stats_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
        if need_T3:
            print(f"[{SKILL_NAME}] mean H={stats['entropy_mean']:.3f}  "
                  f"alpha={stats['alpha_mean_deg']:.1f}°")
        else:
            print(f"[{SKILL_NAME}] Ps/Pd/Pv fractions = "
                  f"{stats['Ps_fraction']:.2f}/{stats['Pd_fraction']:.2f}/{stats['Pv_fraction']:.2f}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Polarimetric SAR decomposition: Cloude-Pottier H/A/alpha and Freeman three-component.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input polarimetric GeoTIFF (T3 9-band or C3 3-band)")
    p.add_argument("--method", default="cloude", choices=["cloude", "freeman", "ha_alpha"],
                   help="decomposition method (default: cloude)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic polarimetric scene (offline)")
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
