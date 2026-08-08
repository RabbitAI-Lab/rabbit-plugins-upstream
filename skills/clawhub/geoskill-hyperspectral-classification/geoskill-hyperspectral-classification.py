#!/usr/bin/env python3
"""hyperspectral-classification — 高光谱监督分类

对高光谱影像立方体 (bands, H, W) 执行监督分类。流程：

1. **训练样本**：合成模式自动从真值标签分层采样；真实数据模式先用
   KMeans 聚类生成伪标签作为训练依据（无标注时的工程近似）。
2. **PCA 降维**：在训练样本上拟合 PCA，压缩上百个波段到少量主成分，
   降低维度灾难并加速分类器。
3. **分类器**：RandomForest (``rf``) 或 SVM (``svm``) 逐像元预测类别。

输出分类图 GeoTIFF、精度报告 JSON（含混淆矩阵与总体精度）。

数据源：本地高光谱 GeoTIFF（多波段），或 ``--synthetic`` 生成含 N 类
特征光谱曲线的模拟立方体用于离线测试。

隐私声明 / Privacy：
- 完全离线运行，不访问任何网络服务。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python hyperspectral-classification.py --input hyper.tif --method rf
    python hyperspectral-classification.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "hyperspectral-classification"

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
# 核心算法
# ---------------------------------------------------------------------------
def class_spectra(n_classes: int, n_bands: int, seed: int = 1) -> np.ndarray:
    """生成 n_classes 条相互区分度高的特征光谱曲线 (n_classes, n_bands)。

    每条曲线由不同的基线、斜率、高斯吸收特征位置和纹波频率组合而成，
    模拟真实矿物 / 植被端元在光谱维上的差异。取值裁剪到 [0.01, 1]。
    """
    if n_classes < 1:
        raise UsageError("n_classes must be >= 1", n_classes=n_classes)
    if n_bands < 2:
        raise UsageError("n_bands must be >= 2", n_bands=n_bands)
    x = np.linspace(0.0, 1.0, n_bands)
    spectra = np.zeros((n_classes, n_bands), dtype=np.float64)
    for c in range(n_classes):
        base = 0.20 + 0.18 * (c / max(n_classes - 1, 1))
        slope = ((c % 3) - 1) * 0.20 * x
        center = (c + 0.5) / n_classes
        absorp = 0.25 * np.exp(-((x - center) ** 2) / (2.0 * 0.03 ** 2))
        ripple = 0.03 * np.sin(2.0 * np.pi * (c + 1) * x)
        spectra[c] = base + slope - absorp + ripple
    return np.clip(spectra, 0.01, 1.0)


def generate_label_map(height: int, width: int, n_classes: int,
                       rng: np.random.Generator) -> np.ndarray:
    """用随机种子点的 Voronoi 剖分生成自然斑块状的真值标签图 (H, W)。"""
    cy = rng.uniform(0.0, height, n_classes)
    cx = rng.uniform(0.0, width, n_classes)
    yy, xx = np.mgrid[0:height, 0:width]
    yy = yy.astype(np.float64)[..., np.newaxis]
    xx = xx.astype(np.float64)[..., np.newaxis]
    d2 = (yy - cy) ** 2 + (xx - cx) ** 2  # (H, W, n_classes)
    return np.argmin(d2, axis=-1).astype(np.int32)


def generate_synthetic(bbox: List[float], n_bands: int = 30, n_classes: int = 4,
                       width: int = 64, height: int = 64, seed: int = 42,
                       noise: float = 0.02) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 (bands, H, W) 高光谱立方体 + 真值标签图。

    每个像元光谱 = 所属类别特征曲线 × (1 + 乘性噪声) + 加性噪声。
    返回 (cube, labels, info)。
    """
    rng = np.random.default_rng(seed)
    labels = generate_label_map(height, width, n_classes, rng)
    spectra = class_spectra(n_classes, n_bands, seed=seed + 1)
    cube = np.zeros((n_bands, height, width), dtype=np.float32)
    for c in range(n_classes):
        mask = labels == c
        count = int(mask.sum())
        if count == 0:
            continue
        mult = 1.0 + rng.normal(0.0, noise, (n_bands, count))
        add = rng.normal(0.0, noise * 0.5, (n_bands, count))
        cube[:, mask] = (spectra[c][:, np.newaxis] * mult + add).astype(np.float32)
    cube = np.clip(cube, 0.0, 1.0)
    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "n_bands": n_bands,
        "n_classes": n_classes,
        "noise": noise,
        "class_pixel_counts": {int(c): int((labels == c).sum()) for c in range(n_classes)},
    }
    return cube, labels, info


def sample_pixels(cube: np.ndarray, labels: np.ndarray, train_frac: float = 0.7,
                  n_per_class: int = 200, seed: int = 0,
                  valid_mask: Optional[np.ndarray] = None
                  ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """分层采样训练 / 测试像元。返回 (X_train, y_train, X_test, y_test)。

    valid_mask (H, W) if provided drops NoData pixels from sampling.
    """
    rng = np.random.default_rng(seed)
    nb, h, w = cube.shape
    X = cube.reshape(nb, -1).T.astype(np.float64)
    y = labels.reshape(-1)
    if valid_mask is not None:
        valid_flat = valid_mask.reshape(-1)
    else:
        valid_flat = np.ones(y.size, dtype=bool)
    train_idx: List[np.ndarray] = []
    test_idx: List[np.ndarray] = []
    for c in np.unique(labels):
        idx_all = np.where((y == c) & valid_flat)[0]
        if idx_all.size == 0:
            continue
        rng.shuffle(idx_all)
        idx = idx_all[: min(n_per_class, idx_all.size)]
        split = max(1, int(idx.size * train_frac))
        train_idx.append(idx[:split])
        if idx.size > split:
            test_idx.append(idx[split:])
    if not train_idx:
        raise ValidationError("no training samples after masking NoData")
    X_train, y_train = X[np.concatenate(train_idx)], y[np.concatenate(train_idx)]
    if test_idx:
        ti = np.concatenate(test_idx)
        X_test, y_test = X[ti], y[ti]
    else:
        X_test, y_test = X_train[:0], y_train[:0]
    return X_train, y_train, X_test, y_test


def train_classifier(X_train: np.ndarray, y_train: np.ndarray, method: str = "rf",
                     n_components: Optional[int] = None, seed: int = 42):
    """在训练样本上拟合 PCA + 分类器，返回 (model, pca)。"""
    from sklearn.decomposition import PCA
    if method == "rf":
        from sklearn.ensemble import RandomForestClassifier
    elif method == "svm":
        from sklearn.svm import SVC
    else:
        raise UsageError(f"unknown method '{method}'. Choose from: rf, svm", method=method)
    if X_train.shape[0] < 2:
        raise ValidationError("too few training samples", n_samples=int(X_train.shape[0]))
    n_comp = n_components or min(X_train.shape[1], 10, X_train.shape[0])
    pca = PCA(n_components=n_comp)
    Xp = pca.fit_transform(X_train)
    if method == "rf":
        model = RandomForestClassifier(n_estimators=60, random_state=seed, n_jobs=1)
    else:
        model = SVC(kernel="rbf", random_state=seed)
    model.fit(Xp, y_train)
    return model, pca


def classify_cube(cube: np.ndarray, model, pca,
                  valid_mask: Optional[np.ndarray] = None) -> np.ndarray:
    """用训练好的 PCA + 分类器对整幅立方体逐像元预测，返回标签图 (H, W)。

    valid_mask (H, W) if provided, NaN pixels are filled with per-band
    training-set mean (estimated from cube[valid_mask]) for inference and
    the returned label is -1 at those positions.
    """
    nb, h, w = cube.shape
    X = cube.reshape(nb, -1).T.astype(np.float64)
    if np.isnan(X).any():
        if valid_mask is None:
            valid_mask = np.all(np.isfinite(cube), axis=0)
        valid_flat = valid_mask.reshape(-1)
        if valid_flat.any():
            Xv = X[valid_flat]
            finite_v = np.all(np.isfinite(Xv), axis=1)
            if finite_v.any():
                fill = np.nanmean(Xv[finite_v], axis=0)
            else:
                fill = np.zeros(nb)
        else:
            fill = np.zeros(nb)
        X = np.where(np.isnan(X), fill, X)
    Xp = pca.transform(X)
    pred = model.predict(Xp)
    out = pred.reshape(h, w).astype(np.int32)
    if valid_mask is not None:
        out = np.where(valid_mask, out, -1).astype(np.int32)
    return out


def pseudo_labels(cube: np.ndarray, n_classes: int, seed: int = 42,
                  valid_mask: Optional[np.ndarray] = None) -> np.ndarray:
    """真实数据无标注时用 KMeans 聚类生成伪标签 (H, W)。

    valid_mask (H, W) drops NoData pixels from clustering.
    """
    from sklearn.cluster import KMeans
    nb, h, w = cube.shape
    X = cube.reshape(nb, -1).T.astype(np.float64)
    if valid_mask is not None:
        valid_flat = valid_mask.reshape(-1)
        Xv = X[valid_flat]
    else:
        Xv = X
        valid_flat = np.ones(X.shape[0], dtype=bool)
    if Xv.shape[0] < max(n_classes, 1):
        raise ValidationError(
            f"too few valid pixels for KMeans: {int(Xv.shape[0])} valid vs n_classes={n_classes}"
        )
    # Drop any remaining NaN rows defensively (KMeans rejects NaN)
    finite_rows = np.all(np.isfinite(Xv), axis=1)
    if not finite_rows.all():
        Xv = Xv[finite_rows]
        # also shrink the index mapping
        valid_indices = np.where(valid_flat)[0]
        valid_indices = valid_indices[finite_rows]
        valid_flat = np.zeros(X.shape[0], dtype=bool)
        valid_flat[valid_indices] = True
    if Xv.shape[0] < max(n_classes, 1):
        raise ValidationError(
            f"too few finite valid pixels for KMeans: {int(Xv.shape[0])} finite vs n_classes={n_classes}"
        )
    n_clusters = min(n_classes, Xv.shape[0])
    km = KMeans(n_clusters=n_clusters, random_state=seed, n_init=4)
    lab_v = km.fit_predict(Xv)
    lab = np.full(X.shape[0], -1, dtype=np.int32)
    lab[valid_flat] = lab_v
    return lab.reshape(h, w).astype(np.int32)


def confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """计算混淆矩阵，返回 (cm, classes)。cm[i, j] = 真值 i 被预测为 j 的数量。"""
    classes = np.unique(np.concatenate([y_true, y_pred]))
    idx = {int(c): i for i, c in enumerate(classes)}
    cm = np.zeros((classes.size, classes.size), dtype=np.int64)
    for t, p in zip(y_true.astype(int), y_pred.astype(int)):
        cm[idx[t], idx[p]] += 1
    return cm, classes


def overall_accuracy(cm: np.ndarray) -> float:
    """总体精度 = 对角线之和 / 总数。"""
    total = int(cm.sum())
    if total == 0:
        return 0.0
    return float(np.trace(cm)) / float(total)


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
    """Read multi-band GeoTIFF. Returns (cube (bands,H,W) float32, bbox [W,S,E,N])."""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_with_nodata(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """Read multi-band GeoTIFF and replace NoData pixels with NaN in-place.

    A pixel is NoData if ANY band equals the nodata sentinel. Returns
    (cube (bands, H, W) float32, bbox [W,S,E,N], nodata_value_or_None).
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None and np.isfinite(nodata):
        bad_mask = np.any(cube == nodata, axis=0)
        cube[:, bad_mask] = np.nan
    return cube, bbox, nodata


def validate_bbox(bbox: Optional[List[float]], allow_none: bool = False) -> List[float]:
    """Validate a W,S,E,N bbox. Cross-180 / out-of-range / W>=E / S>=N -> ValidationError."""
    if bbox is None:
        if allow_none:
            return None  # type: ignore[return-value]
        raise ValidationError("bbox is required")
    if len(bbox) != 4:
        raise ValidationError(f"bbox must have 4 floats, got {len(bbox)}")
    w, s, e, n = bbox
    for v, name in zip([w, s, e, n], ["W", "S", "E", "N"]):
        if not isinstance(v, (int, float)) or not (-1e9 < v < 1e9):
            raise ValidationError(f"bbox {name}={v!r} not a finite number")
    if w == e or s == n:
        raise ValidationError(f"bbox has zero area: W={w} E={e} S={s} N={n}")
    if not (-180.0 <= w <= 180.0) or not (-180.0 <= e <= 180.0):
        raise ValidationError(f"bbox lon out of [-180,180]: W={w} E={e}")
    if not (-90.0 <= s <= 90.0) or not (-90.0 <= n <= 90.0):
        raise ValidationError(f"bbox lat out of [-90,90]: S={s} N={n}")
    if w > e:
        if not (w > 170.0 and e < -170.0):
            raise ValidationError(
                f"bbox has W>E (minLon > maxLon): W={w} E={e} — "
                f"if crossing the dateline, split into two bboxes (e.g. "
                f"[{w}, {s}, 180, {n}] and [-180, {s}, {e}, {n}])"
            )
        raise ValidationError(
            f"bbox crosses the 180° dateline (W={w} E={e}); "
            f"split into two non-wrapping bboxes ([{w}, {s}, 180, {n}] and "
            f"[-180, {s}, {e}, {n}]) and run separately"
        )
    if s > n:
        raise ValidationError(f"bbox has S>N (minLat > maxLat): S={s} N={n}")
    return [float(w), float(s), float(e), float(n)]


def validate_synthetic_params(n_bands: int, n_classes: int) -> Tuple[int, int]:
    """Validate synthetic-cube parameters. Returns (n_bands, n_classes)."""
    if n_bands is None or n_bands < 2:
        raise ValidationError(f"--n-bands must be >= 2, got {n_bands}")
    if n_classes is None or n_classes < 1:
        raise ValidationError(f"--n-classes must be >= 1, got {n_classes}")
    return int(n_bands), int(n_classes)


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir: str, args: argparse.Namespace,
                   outputs: List[Dict[str, Any]], qa: Dict[str, Any],
                   started_at: str, exit_code: int, bbox: List[float]) -> Optional[str]:
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
            "n_bands": getattr(args, "n_bands", None),
            "n_classes": getattr(args, "n_classes", None),
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

    # ---- 1. 参数验证 (前置：失败不创建 output_dir) ----
    bbox = list(args.bbox) if args.bbox else None
    if bbox is not None:
        bbox = validate_bbox(bbox)
    n_bands, n_classes = validate_synthetic_params(args.n_bands, args.n_classes)

    # ---- 2. 数据获取 ----
    synth_info: Optional[Dict[str, Any]] = None
    truth_labels: Optional[np.ndarray] = None
    input_nodata: Optional[float] = None
    valid_mask: Optional[np.ndarray] = None
    n_valid_input: int = 0
    n_total_input: int = 0

    if args.input and not args.synthetic:
        cube, file_bbox, input_nodata = read_geotiff_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        bbox = validate_bbox(bbox)
        valid_mask = np.all(np.isfinite(cube), axis=0)  # 2D mask: True where all bands finite
        n_valid_input = int(valid_mask.sum())
        n_total_input = int(cube.shape[1] * cube.shape[2])
        if n_valid_input == 0:
            raise ValidationError(
                f"input cube has no valid (non-NoData) pixels "
                f"(nodata={input_nodata}, total={n_total_input})"
            )
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, truth_labels, synth_info = generate_synthetic(
            bbox, n_bands=n_bands, n_classes=n_classes,
        )
        source_note = "synthetic"
        n_valid_input = int(cube.size)
        n_total_input = int(cube.shape[1] * cube.shape[2])

    # ---- 3. 校验通过后创建 output_dir ----
    os.makedirs(output_dir, exist_ok=True)

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.ndim != 3 or cube.shape[0] < 2:
        raise ValidationError("input must be a multi-band cube (bands, H, W)",
                              shape=list(cube.shape))

    # 2) 训练样本标签：合成用真值，真实数据用 KMeans 伪标签（仅 valid 像元）
    if truth_labels is None:
        labels = pseudo_labels(cube, n_classes, seed=42, valid_mask=valid_mask)
        label_source = "kmeans-pseudo"
    else:
        labels = truth_labels
        label_source = "synthetic-truth"

    # 3) 采样 + 训练 + 预测 (NaN-safe: 跳过 NoData 像元)
    X_train, y_train, X_test, y_test = sample_pixels(
        cube, labels, seed=7, valid_mask=valid_mask,
    )
    model, pca = train_classifier(X_train, y_train, method=args.method)
    class_map = classify_cube(cube, model, pca, valid_mask=valid_mask)

    # 4) 精度评估（测试集）
    accuracy: Dict[str, Any] = {"label_source": label_source, "method": args.method}
    if y_test.size > 0:
        # NaN-safe predict on test
        finite_test = np.all(np.isfinite(X_test), axis=1)
        if finite_test.any():
            Xte = np.where(np.isfinite(X_test), X_test, 0.0)
            pred_te = model.predict(pca.transform(Xte))
            # restore NaN in X_test for ground-truth? ground truth is from labels, finite OK
            cm, classes = confusion_matrix(y_test[finite_test], pred_te[finite_test])
            oa = overall_accuracy(cm)
            accuracy["overall_accuracy"] = oa
            accuracy["n_test_pixels"] = int(finite_test.sum())
            accuracy["confusion_matrix"] = cm.tolist()
            accuracy["classes"] = [int(c) for c in classes]
        else:
            oa = float("nan")
            accuracy["overall_accuracy"] = None
    else:
        oa = float("nan")
        accuracy["overall_accuracy"] = None

    # 5) 写出产物
    out_tif = os.path.join(output_dir, "classification.tif")
    write_geotiff(out_tif, class_map.astype(np.float32), bbox, nodata=-1.0)

    accuracy_path = os.path.join(output_dir, "accuracy.json")
    with open(accuracy_path, "w", encoding="utf-8") as f:
        json.dump(accuracy, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "label_source": label_source,
        "n_bands": int(cube.shape[0]),
        "n_classes_detected": int(np.unique(class_map[class_map >= 0]).size) if (class_map >= 0).any() else 0,
        "overall_accuracy": accuracy.get("overall_accuracy"),
        "n_valid_pixels": int(n_valid_input),
        "n_total_pixels": int(n_total_input),
        "input_nodata": input_nodata,
    }
    if synth_info is not None:
        qa["synthetic_class_pixel_counts"] = synth_info["class_pixel_counts"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "nodata": -1.0},
        {"path": accuracy_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  bands: {cube.shape[0]}  shape: {cube.shape[1:]}")
        print(f"[{SKILL_NAME}] classes detected: {qa['n_classes_detected']}")
        if accuracy.get("overall_accuracy") is not None:
            print(f"[{SKILL_NAME}] overall accuracy: {accuracy['overall_accuracy']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Hyperspectral supervised classification (PCA + RF / SVM).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input hyperspectral GeoTIFF (bands, H, W)")
    p.add_argument("--method", default="rf", choices=["rf", "svm"],
                   help="classifier: random forest (rf) or support vector machine (svm)")
    p.add_argument("--n-bands", type=int, default=30,
                   help="synthetic cube band count (default: 30)")
    p.add_argument("--n-classes", type=int, default=4,
                   help="number of land-cover classes (default: 4)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic hyperspectral scene (offline)")
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
