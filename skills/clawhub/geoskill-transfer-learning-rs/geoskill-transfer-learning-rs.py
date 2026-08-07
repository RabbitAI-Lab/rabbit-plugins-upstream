#!/usr/bin/env python3
"""transfer-learning-rs — 遥感迁移学习

用一个"冻结的特征提取器"（预训练主干的离线等价）从遥感影像抽取特征，
再在其上"微调"一个轻量分类头，并在独立验证集上评估精度。

本 skill 是深度迁移学习（预训练 backbone + fine-tune head）的**离线 numpy 等价实现**：
不依赖 torch/tensorflow，而用可验证的流程复现其核心范式——

1. **特征提取（冻结主干）**：对每个波段施加固定的滤波 bank（原始光谱 +
   Sobel 梯度幅值 + 局部均值纹理），拼成逐像元特征向量。滤波器是确定的，
   等价于"在源域预训练后冻结、不再更新"的卷积主干；
2. **微调分类头**：特征标准化后，用 sklearn 逻辑回归/随机森林拟合少量标注样本
   （等价于只训练网络末端的分类头）；
3. **精度评估**：在划出的验证集上计算总体精度 OA，并与"仅用原始光谱（不迁移）"
   的基线对比，验证迁移特征的价值。

数据源：本地多波段 GeoTIFF（真实模式做无监督特征聚类），或 ``--synthetic``
生成含真值标签的三分类场景用于有监督迁移评估。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python transfer-learning-rs.py --input scene.tif --n-classes 4 --output-dir ./out
    python transfer-learning-rs.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "transfer-learning-rs"

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
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox, *, allow_antimeridian_cross: bool = False) -> None:
    """校验 bbox=[W,S,E,N]（EPSG:4326 度）。"""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must have 4 floats [W S E N]")
    w, s, e, n = [float(v) for v in bbox]
    if not (all(np.isfinite([w, s, e, n]))):
        raise ValidationError("bbox contains non-finite values")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError("bbox lon out of [-180, 180]")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError("bbox lat out of [-90, 90]")
    if w >= e:
        if not allow_antimeridian_cross:
            raise ValidationError(
                f"bbox W>=E ({w} >= {e}); cross-180° not supported, "
                f"split into two bboxes if needed"
            )
        raise ValidationError(f"bbox W>=E ({w} >= {e})")
    if s >= n:
        raise ValidationError(f"bbox S>=N ({s} >= {n})")
    if (e - w) < 1e-4 or (n - s) < 1e-4:
        raise ValidationError(
            f"bbox too small (dx={e - w}, dy={n - s}); need >= 1e-4 degrees"
        )


def validate_params(args: argparse.Namespace) -> None:
    """校验 CLI 参数物理合理性 → ValidationError 触发 rc=6。"""
    if not (0.0 < args.train_frac < 1.0):
        raise ValidationError(
            f"--train-frac must be in (0, 1) (got {args.train_frac})"
        )
    if args.n_classes < 2:
        raise ValidationError(
            f"--n-classes must be >= 2 (got {args.n_classes})"
        )
    if args.n_classes > 256:
        raise ValidationError(
            f"--n-classes {args.n_classes} is unrealistically large (> 256)"
        )
    if args.seed < 0 or args.seed > 2**31 - 1:
        raise ValidationError(
            f"--seed must be in [0, 2^31-1] (got {args.seed})"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def _gradient_magnitude(band: np.ndarray) -> np.ndarray:
    from scipy.signal import convolve2d
    kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float64)
    gx = convolve2d(band, kx, mode="same", boundary="symm")
    gy = convolve2d(band, kx.T, mode="same", boundary="symm")
    return np.sqrt(gx * gx + gy * gy)


def build_features(cube: np.ndarray, use_transfer: bool = True) -> np.ndarray:
    """逐像元特征提取。

    use_transfer=False：仅原始光谱 (N, bands)。
    use_transfer=True：原始光谱 + 梯度幅值 + 局部均值纹理 (N, 3*bands)，
    等价于把冻结主干输出的多通道特征图展平。
    """
    from scipy.ndimage import uniform_filter
    cube = np.asarray(cube, dtype=np.float64)
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    if cube.ndim != 3:
        raise ValidationError("cube must be (bands, H, W)", shape=list(cube.shape))
    nb, h, w = cube.shape
    channels: List[np.ndarray] = [cube]
    if use_transfer:
        grad = np.stack([_gradient_magnitude(cube[b]) for b in range(nb)], axis=0)
        lmean = np.stack([uniform_filter(cube[b], size=3) for b in range(nb)], axis=0)
        channels.extend([grad, lmean])
    stack = np.concatenate(channels, axis=0)  # (F, H, W)
    feats = np.moveaxis(stack, 0, -1).reshape(h * w, stack.shape[0])
    return feats


def standardize(x_train: np.ndarray, x_test: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """用训练集统计量标准化训练/测试特征（防止数据泄漏）。"""
    mu = x_train.mean(axis=0)
    sigma = x_train.std(axis=0)
    sigma = np.where(sigma < 1e-9, 1.0, sigma)
    return (x_train - mu) / sigma, (x_test - mu) / sigma, mu, sigma


def finetune_classifier(x_train: np.ndarray, y_train: np.ndarray, model: str = "logreg"):
    """在特征上训练分类头。"""
    if model == "logreg":
        from sklearn.linear_model import LogisticRegression
        clf = LogisticRegression(max_iter=2000)
    elif model == "rf":
        from sklearn.ensemble import RandomForestClassifier
        clf = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=1)
    else:
        raise UsageError(f"unknown model '{model}'. Choose from: logreg, rf", model=model)
    clf.fit(x_train, y_train)
    return clf


def overall_accuracy(pred: np.ndarray, truth: np.ndarray) -> float:
    pred = np.asarray(pred).ravel()
    truth = np.asarray(truth).ravel()
    if pred.size != truth.size or pred.size == 0:
        raise ValidationError("pred/truth size mismatch or empty")
    return float(np.mean(pred == truth))


def split_indices(n: int, train_frac: float, seed: int = 42) -> Tuple[np.ndarray, np.ndarray]:
    """随机划分训练/验证索引。"""
    if not 0.0 < train_frac < 1.0:
        raise UsageError("train_frac must be in (0, 1)", train_frac=float(train_frac))
    rng = np.random.default_rng(seed)
    idx = rng.permutation(n)
    n_train = max(1, int(round(n * train_frac)))
    n_train = min(n_train, n - 1)  # 至少留 1 个验证样本
    return idx[:n_train], idx[n_train:]


def transfer_learn(
    cube: np.ndarray,
    truth: np.ndarray,
    train_frac: float = 0.6,
    use_transfer: bool = True,
    model: str = "logreg",
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """完整迁移学习流程：特征 -> 划分 -> 标准化 -> 微调 -> 评估。

    返回 (full_label_map[H, W], info)。info 含验证精度等。
    """
    cube = np.asarray(cube, dtype=np.float64)
    truth = np.asarray(truth).ravel()
    nb, h, w = (cube if cube.ndim == 3 else cube[np.newaxis, ...]).shape
    if truth.size != h * w:
        raise ValidationError("truth size does not match H*W",
                              truth=int(truth.size), hw=int(h * w))

    feats = build_features(cube, use_transfer=use_transfer)
    train_idx, test_idx = split_indices(feats.shape[0], train_frac, seed)

    x_tr, x_te, mu, sigma = standardize(feats[train_idx], feats[test_idx])
    y_tr = truth[train_idx]
    y_te = truth[test_idx]

    clf = finetune_classifier(x_tr, y_tr, model=model)
    acc = overall_accuracy(clf.predict(x_te), y_te)

    # 全图预测
    x_all = (feats - mu) / sigma
    full_pred = np.asarray(clf.predict(x_all)).reshape(h, w)

    info = {
        "use_transfer": bool(use_transfer),
        "model": model,
        "n_features": int(feats.shape[1]),
        "n_train": int(train_idx.size),
        "n_test": int(test_idx.size),
        "validation_accuracy": acc,
    }
    return full_pred, info


def cluster_features(cube: np.ndarray, n_classes: int, seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    """真实输入（无标签）模式：迁移特征 + KMeans 无监督聚类。"""
    from sklearn.cluster import KMeans
    cube = np.asarray(cube, dtype=np.float64)
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    feats = build_features(cube, use_transfer=True)
    km = KMeans(n_clusters=n_classes, n_init=10, random_state=seed)
    labels = km.fit_predict(feats).reshape(h, w)
    info = {"n_classes": int(n_classes), "n_features": int(feats.shape[1])}
    return labels, info


# ---------------------------------------------------------------------------
# 合成数据：3 类（光谱 + 纹理差异）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    n_bands: int = 4,
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 3 类场景 + 真值标签。类别在光谱与纹理上都有差异。"""
    rng = np.random.default_rng(seed)
    truth = np.zeros((height, width), dtype=np.int64)
    truth[:, :width // 3] = 0
    truth[:, width // 3:2 * width // 3] = 1
    truth[:, 2 * width // 3:] = 2

    cube = np.zeros((n_bands, height, width), dtype=np.float32)
    mask2 = truth == 2
    n2 = int(mask2.sum())
    for b in range(n_bands):
        layer = np.zeros((height, width), dtype=np.float64)
        layer[truth == 0] = 0.2 + 0.05 * b
        layer[truth == 1] = 0.5 + 0.05 * b
        layer[mask2] = 0.8 + 0.05 * b
        # 类别 2 叠加高频纹理（梯度特征更易区分）
        layer[mask2] += rng.normal(0, 0.08, size=n2)
        layer += rng.normal(0, 0.02, layer.shape)
        cube[b] = np.clip(layer, 0, 1).astype(np.float32)

    info = {"bbox": bbox, "n_bands": n_bands, "width": width, "height": height}
    return cube, truth, info


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
        nd = src.nodata
        if nd is not None and np.isfinite(nd):
            cube = np.where(cube == nd, np.nan, cube).astype(np.float32)
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
            "model": getattr(args, "model", None),
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

    # 1) 参数与 bbox 校验（先做，不创建任何目录）
    validate_params(args)

    bbox = list(args.bbox) if args.bbox else None
    synth_truth: Optional[np.ndarray] = None

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
        label_map, info = cluster_features(cube, n_classes=args.n_classes, seed=args.seed)
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        cube, synth_truth, _ = generate_synthetic(bbox, seed=args.seed)
        source_note = "synthetic"
        label_map, info = transfer_learn(
            cube, synth_truth, train_frac=args.train_frac,
            use_transfer=True, model=args.model, seed=args.seed,
        )
        # 基线：不迁移（仅原始光谱）
        _, info_raw = transfer_learn(
            cube, synth_truth, train_frac=args.train_frac,
            use_transfer=False, model=args.model, seed=args.seed,
        )
        info["validation_accuracy_raw"] = info_raw["validation_accuracy"]
        info["transfer_gain"] = info["validation_accuracy"] - info_raw["validation_accuracy"]

    # input 模式也要校验 bbox（防止 file_bbox 异常）
    if bbox is not None:
        validate_bbox(bbox)

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    # 全 NaN 检查（NoData -> NaN 后）
    n_total = int(cube.size)
    n_valid = int(np.sum(np.isfinite(cube)))
    if n_valid == 0:
        raise ValidationError(
            f"input raster has no valid pixels (n_valid=0, n_total={n_total})"
        )

    # 所有校验通过 → 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    out_tif = os.path.join(output_dir, "classification.tif")
    write_geotiff(out_tif, label_map.astype(np.float32), bbox)

    report_path = os.path.join(output_dir, "accuracy_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_total_pixels": n_total,
        "n_valid_pixels": n_valid,
        "input_nodata_handling": "NoData->NaN",
        "device": "cpu+numpy/sklearn (offline equivalent; "
                  "transfer learning conceptual model)",
    }
    qa.update(info)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        if "validation_accuracy" in info:
            print(f"[{SKILL_NAME}] transfer OA: {info['validation_accuracy']:.3f}")
            if "validation_accuracy_raw" in info:
                print(f"[{SKILL_NAME}] raw OA:     {info['validation_accuracy_raw']:.3f}  "
                      f"gain: {info['transfer_gain']:+.3f}")
        else:
            print(f"[{SKILL_NAME}] clusters: {info['n_classes']}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Remote-sensing transfer learning (frozen filter-bank features + fine-tuned head).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multispectral GeoTIFF (unsupervised feature clustering)")
    p.add_argument("--n-classes", type=int, default=3, help="clusters for unsupervised mode")
    p.add_argument("--train-frac", type=float, default=0.6, help="training fraction")
    p.add_argument("--model", default="logreg", choices=["logreg", "rf"],
                   help="classifier head (default: logreg)")
    p.add_argument("--seed", type=int, default=42, help="random seed")
    p.add_argument("--synthetic", action="store_true", help="generate a synthetic scene (offline)")
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
