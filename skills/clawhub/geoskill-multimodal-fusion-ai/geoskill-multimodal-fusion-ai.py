#!/usr/bin/env python3
"""multimodal-fusion-ai — 多模态遥感 AI 融合

把多个异源遥感数据（如光学 / SAR / DEM / 热红外）标准化到可比尺度后加权融合，
并在融合特征上做联合分类，输出融合栅格与分类图。

本 skill 是多模态深度学习融合网络（多分支 CNN/Transformer）的**离线 numpy 等价实现**：
不依赖 torch/tensorflow，而用可验证的流程复现"对齐 -> 融合 -> 联合解译"——

1. **多源标准化**：逐源 min-max 缩放到 [0, 1]（或 z-score），消除量纲差异
   （等价于网络各分支的 BatchNorm 对齐）；
2. **加权融合**：按用户权重或自动权重（逆噪声方差，噪声小的源权重大，
   等价于对同一场景的独立噪声观测做最优加权平均）做加权平均；
3. **联合分类**：在融合图上用 KMeans 逐像元聚类（等价于融合特征上的分类头）；
4. **质量评估**：合成模式下与真值比较融合降噪效果与分类精度。

数据源：本地多波段 GeoTIFF（各波段视为一个模态），或 ``--synthetic`` 生成
多源观测同一场景的模拟数据。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python multimodal-fusion-ai.py --input multi.tif --weights 0.6,0.4 --output-dir ./out
    python multimodal-fusion-ai.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "multimodal-fusion-ai"

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, to_exit_code,
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
def standardize_layer(layer: np.ndarray, method: str = "minmax") -> np.ndarray:
    """单源标准化。

    minmax：缩放到 [0, 1]（常数层返回全 0）。
    zscore：零均值单位方差（常数层返回全 0）。
    """
    x = np.asarray(layer, dtype=np.float64)
    if method == "minmax":
        lo, hi = float(np.nanmin(x)), float(np.nanmax(x))
        if hi <= lo:
            return np.zeros_like(x)
        return (x - lo) / (hi - lo)
    if method == "zscore":
        mu = float(np.nanmean(x))
        sd = float(np.nanstd(x))
        if sd <= 1e-12:
            return np.zeros_like(x)
        return (x - mu) / sd
    raise UsageError(f"unknown norm method '{method}'. Choose from: minmax, zscore",
                     method=method)


def standardize_layers(layers: List[np.ndarray], method: str = "minmax") -> List[np.ndarray]:
    """对多个源逐一标准化（形状须一致）。"""
    if not layers:
        raise ValidationError("no layers to standardize")
    shapes = {np.asarray(l).shape for l in layers}
    if len(shapes) != 1:
        raise ValidationError("all layers must share the same shape",
                              shapes=[list(s) for s in shapes])
    return [standardize_layer(l, method) for l in layers]


def estimate_noise(layer: np.ndarray) -> float:
    """稳健噪声估计：拉普拉斯响应的 MAD（中位数绝对偏差）。

    对噪声方差 sigma^2，Laplacian 响应的标准差为 sigma*sqrt(20)
    （核平方和 = 20）；用 MAD/0.6745 还原，边缘等少数大值不影响中位数。
    """
    from scipy.signal import convolve2d
    x = np.asarray(layer, dtype=np.float64)
    if x.ndim != 2 or x.size == 0:
        return 0.0
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float64)
    lap = convolve2d(x, kernel, mode="valid")
    if lap.size == 0:
        return 0.0
    mad = float(np.median(np.abs(lap - np.median(lap))))
    return 1.4826 * mad / np.sqrt(20.0)


def auto_weights(layers: List[np.ndarray]) -> np.ndarray:
    """噪声自适应权重：估计各源噪声水平，按逆噪声方差加权（归一化和为 1）。

    这是"对同一场景的独立噪声观测取加权平均"的最优融合规则：
    噪声小的源权重高。所有源噪声都为 0 时退化为等权。
    """
    if not layers:
        raise ValidationError("no layers for auto weights")
    noises = np.array([estimate_noise(np.asarray(l, dtype=np.float64)) for l in layers])
    if noises.max() <= 1e-12:
        return np.full(len(layers), 1.0 / len(layers))
    # 下限保护：零噪声源给极大权重（同时避免除零）
    safe = np.clip(noises, 1e-6, None)
    inv = 1.0 / (safe * safe)
    return inv / inv.sum()


def parse_weights(text: str, n: int) -> np.ndarray:
    """解析逗号分隔权重字符串，校验数量与合法性。"""
    if not text or not text.strip():
        raise UsageError("weights string is empty")
    try:
        vals = [float(v) for v in text.split(",")]
    except ValueError as exc:
        raise UsageError(f"weights must be comma-separated numbers: {text}") from exc
    if len(vals) != n:
        raise UsageError(f"weights count {len(vals)} != number of layers {n}",
                         weights=len(vals), layers=int(n))
    arr = np.asarray(vals, dtype=np.float64)
    if np.any(arr < 0):
        raise UsageError("weights must be non-negative")
    if arr.sum() <= 0:
        raise UsageError("weights must not all be zero")
    return arr / arr.sum()


def affine_residual_std(x: np.ndarray, ref: np.ndarray) -> float:
    """扣除最优线性偏差 (a*ref + b) 后的残差标准差。

    标准化会因噪声极值拉伸范围而引入全局线性偏差；先最小二乘拟合
    x ≈ a*ref + b 再取残差，得到的才是纯粹的"噪声水平"，
    用于公平比较不同源/融合结果的降噪效果。
    """
    x = np.asarray(x, dtype=np.float64).ravel()
    ref = np.asarray(ref, dtype=np.float64).ravel()
    if x.size != ref.size or x.size < 3:
        raise ValidationError("affine_residual_std needs >= 3 matching samples",
                              x=int(x.size), ref=int(ref.size))
    A = np.column_stack([ref, np.ones_like(ref)])
    coef, _, _, _ = np.linalg.lstsq(A, x, rcond=None)
    resid = x - A @ coef
    return float(np.sqrt(np.mean(resid * resid)))


def fuse_weighted(layers: List[np.ndarray], weights: np.ndarray) -> np.ndarray:
    """加权平均融合（建议先用 standardize_layers 对齐量纲）。"""
    if not layers:
        raise ValidationError("no layers to fuse")
    weights = np.asarray(weights, dtype=np.float64).ravel()
    if weights.size != len(layers):
        raise ValidationError("weights/layers count mismatch",
                              weights=int(weights.size), layers=int(len(layers)))
    if weights.sum() <= 0:
        raise ValidationError("weights must sum to a positive value")
    w = weights / weights.sum()
    stack = np.stack([np.asarray(l, dtype=np.float64) for l in layers], axis=0)
    return np.tensordot(w, stack, axes=(0, 0))


def joint_classify(image: np.ndarray, n_classes: int, seed: int = 42) -> np.ndarray:
    """在融合图上逐像元 KMeans 联合分类，返回 (H, W) 标签图。"""
    from sklearn.cluster import KMeans
    img = np.asarray(image, dtype=np.float64)
    if img.ndim != 2:
        raise ValidationError("joint_classify expects a 2D fused image", shape=list(img.shape))
    if n_classes < 1:
        raise UsageError("n_classes must be >= 1", n_classes=int(n_classes))
    km = KMeans(n_clusters=n_classes, n_init=10, random_state=seed)
    labels = km.fit_predict(img.reshape(-1, 1))
    return labels.reshape(img.shape)


def fuse_and_classify(layers: List[np.ndarray], weights: Optional[np.ndarray],
                      n_classes: int, norm: str = "minmax",
                      seed: int = 42) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """完整流程：标准化 -> 加权融合 -> 联合分类。返回 (fused, labels, info)。"""
    std_layers = standardize_layers(layers, method=norm)
    if weights is None:
        # 在标准化（同尺度）后的层上估计噪声，权重才对实际融合最优
        weights = auto_weights(std_layers)
    weights = np.asarray(weights, dtype=np.float64).ravel()
    if weights.size != len(layers):
        raise ValidationError("weights/layers count mismatch")
    weights = weights / weights.sum()
    fused = fuse_weighted(std_layers, weights)
    labels = joint_classify(fused, n_classes, seed=seed)
    info = {
        "n_layers": int(len(layers)),
        "norm": norm,
        "weights": weights.tolist(),
        "fused_min": float(np.nanmin(fused)),
        "fused_max": float(np.nanmax(fused)),
        "n_classes": int(n_classes),
    }
    return fused, labels, info


# ---------------------------------------------------------------------------
# 合成数据：多源观测同一场景（不同量纲 + 噪声）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Tuple[List[np.ndarray], np.ndarray, Dict[str, Any]]:
    """生成观测同一三类场景的两个模态 + 真值标签。

    两个模态观测同一地表信号，但量纲不同、噪声独立：
    - 模态 1（光学式）：反射率 [0, 1]；
    - 模态 2（SAR 式）：不同尺度（*100 + 20）的后向散射量。
    两者叠加幅度相同（真值单位下 ±0.04）的独立均匀噪声——
    这样标准化后偏差剖面一致，加权平均能严格降低噪声方差，
    使"融合优于任一单源"成为可验证的数学事实。
    """
    rng = np.random.default_rng(seed)
    truth = np.zeros((height, width), dtype=np.int64)
    truth[:, :width // 3] = 0
    truth[:, width // 3:2 * width // 3] = 1
    truth[:, 2 * width // 3:] = 2
    base = np.where(truth == 0, 0.2, np.where(truth == 1, 0.5, 0.8)).astype(np.float64)

    optical = base + rng.uniform(-0.04, 0.04, base.shape)
    optical = np.clip(optical, 0.0, 1.0)

    # SAR 式：不同量纲（真值单位下的噪声幅度与光学一致）
    sar = 100.0 * base + 20.0 + rng.uniform(-4.0, 4.0, base.shape)

    info = {"bbox": bbox, "width": width, "height": height,
            "modalities": ["optical", "sar"]}
    return [optical.astype(np.float32), sar.astype(np.float32)], truth, info


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
            "weights": getattr(args, "weights", None),
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
# 输入校验（前置；统一 exit code = 6 ValidationError）
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Any) -> List[float]:
    """W<E、S<N、坐标超范围、零面积 → ValidationError。"""
    if not bbox or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats [W S E N]", bbox=bbox)
    W, S, E, N = [float(x) for x in bbox]
    if not (all(np.isfinite([W, S, E, N]))):
        raise ValidationError("bbox must be finite", bbox=[W, S, E, N])
    if not (-180.0 <= W <= 180.0 and -180.0 <= E <= 180.0):
        raise ValidationError("longitude out of [-180, 180]", W=W, E=E)
    if not (-90.0 <= S <= 90.0 and -90.0 <= N <= 90.0):
        raise ValidationError("latitude out of [-90, 90]", S=S, N=N)
    if W >= E:
        raise ValidationError(
            f"bbox W must be < E (W={W}, E={E})", W=W, E=E)
    if S >= N:
        raise ValidationError(
            f"bbox S must be < N (S={S}, N={N})", S=S, N=N)
    if (E - W) * (N - S) <= 0.0:
        raise ValidationError("bbox area is zero or negative", area=(E - W) * (N - S))
    return [W, S, E, N]


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir
    bbox = list(args.bbox) if args.bbox else None
    truth: Optional[np.ndarray] = None

    # 校验前置（input 模式：bbox 可选；synthetic 模式：bbox 必填）
    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input raster not found: {args.input}", path=args.input)
        if bbox is not None:
            bbox = validate_bbox(bbox)
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)

    os.makedirs(output_dir, exist_ok=True)

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        layers = [cube[b] for b in range(cube.shape[0])]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        layers, truth, _ = generate_synthetic(bbox, seed=args.seed)
        source_note = "synthetic"

    if len(layers) < 2:
        raise ValidationError("multimodal fusion needs at least 2 input bands/layers")

    weights = parse_weights(args.weights, len(layers)) if args.weights else None
    fused, labels, info = fuse_and_classify(
        layers, weights, n_classes=args.n_classes, norm=args.norm, seed=args.seed)

    fused_tif = os.path.join(output_dir, "fused.tif")
    write_geotiff(fused_tif, fused.astype(np.float32), bbox)
    class_tif = os.path.join(output_dir, "classification.tif")
    write_geotiff(class_tif, labels.astype(np.float32), bbox)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_layers": info["n_layers"],
        "norm": info["norm"],
        "weights": info["weights"],
        "n_classes": info["n_classes"],
    }
    if truth is not None:
        # 融合降噪评估：扣除线性偏差后的残差噪声水平（见 affine_residual_std）
        truth_std = standardize_layer(truth.astype(np.float64), "minmax")
        std_layers = standardize_layers(layers, method="minmax")
        src_noise = [affine_residual_std(s, truth_std) for s in std_layers]
        fused_noise = affine_residual_std(fused, truth_std)
        qa["source_noise_std"] = src_noise
        qa["fused_noise_std"] = fused_noise
        qa["noise_improves"] = bool(fused_noise < min(src_noise))

    report_path = os.path.join(output_dir, "fusion_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(qa, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": fused_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": class_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  layers: {info['n_layers']}  "
              f"weights: {[round(w, 3) for w in info['weights']]}")
        if "fused_noise_std" in qa:
            print(f"[{SKILL_NAME}] source noise: {[round(m, 5) for m in qa['source_noise_std']]}")
            print(f"[{SKILL_NAME}] fused noise:  {qa['fused_noise_std']:.5f}  "
                  f"improves: {qa['noise_improves']}")
        print(f"[{SKILL_NAME}] fused: {fused_tif}  classes: {class_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Multimodal remote-sensing fusion (standardize + weighted fuse + joint classify).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multiband GeoTIFF (each band = one modality)")
    p.add_argument("--weights", default="",
                   help="comma-separated fusion weights (default: auto by std)")
    p.add_argument("--n-classes", type=int, default=3, help="classes for joint classification")
    p.add_argument("--norm", default="minmax", choices=["minmax", "zscore"],
                   help="per-source standardization (default: minmax)")
    p.add_argument("--seed", type=int, default=42, help="seed for synthetic data")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic data (offline)")
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
