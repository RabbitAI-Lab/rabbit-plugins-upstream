#!/usr/bin/env python3
"""sar-crop-classification — SAR农作物分类

基于多时相 SAR 后向散射时序的逐像元农作物分类。不同作物因物候（播种、
插秧、抽穗、成熟）不同而在 σ⁰ 时序上呈现可分特征——例如水稻插秧期淹水
导致后向散射极低，随后营养生长使 σ⁰ 快速上升；冬小麦前高后低；玉米在
盛夏出现峰值。流程：

1. **特征提取**：逐像元构建特征向量——各时相 σ⁰ 值 + 时序统计
   （mean/std/amplitude/cv）+ 物候峰值时刻（argmax/T）。
2. **随机森林分类**：``sklearn.ensemble.RandomForestClassifier``。
   合成模式用真值标签做有监督训练（分层抽样训练/测试分割）；真实输入
   无标签时用 KMeans 生成伪标签自训练（无监督辅助）。
3. **精度评估**：混淆矩阵 + 总体精度（合成模式在留出测试集上评估）。

数据源：本地多时相 σ⁰ GeoTIFF（各波段为一个时相），或使用 ``--synthetic``
生成水稻/小麦/玉米三类、各具特征时序曲线的场景（含乘性/加性噪声）。

隐私声明 / Privacy：
- 默认完全离线运行，不发起任何网络请求。
- ``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python sar-crop-classification.py --input ts.tif --n-dates 6
    python sar-crop-classification.py --bbox 116 39 117 40 --synthetic --n-dates 8

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
SKILL_NAME = "sar-crop-classification"

CLASS_NAMES = ["rice", "wheat", "corn"]

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
def temporal_features(cube: np.ndarray) -> Tuple[np.ndarray, List[str]]:
    """逐像元时序特征提取。

    输入 (T, H, W)，返回 (features (H*W, T+5), feature_names)。
    特征：各时相 σ⁰ + [mean, std, amplitude, cv, peak_time]。
    """
    cube = np.asarray(cube, dtype=np.float32)
    if cube.ndim != 3:
        raise ValidationError(
            f"time-series cube must be 3-D (T,H,W), got shape {cube.shape}",
            shape=list(cube.shape),
        )
    t, h, w = cube.shape
    eps = 1e-9
    flat = cube.reshape(t, h * w).T  # (N, T)

    mean = flat.mean(axis=1, keepdims=True)
    std = flat.std(axis=1, keepdims=True)
    amplitude = (flat.max(axis=1) - flat.min(axis=1))[:, None]
    cv = std / np.maximum(np.abs(mean), eps)
    peak_time = (np.argmax(flat, axis=1).astype(np.float32) / max(t - 1, 1))[:, None]

    feats = np.concatenate([flat, mean, std, amplitude, cv, peak_time], axis=1)
    names = [f"t{i}" for i in range(t)] + ["mean", "std", "amplitude", "cv", "peak_time"]
    return feats.astype(np.float32), names


def confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray, n_classes: int) -> np.ndarray:
    """混淆矩阵 (n_classes, n_classes)，行=真值，列=预测。"""
    cm = np.zeros((n_classes, n_classes), dtype=np.int64)
    for yt, yp in zip(np.asarray(y_true).ravel(), np.asarray(y_pred).ravel()):
        if 0 <= int(yt) < n_classes and 0 <= int(yp) < n_classes:
            cm[int(yt), int(yp)] += 1
    return cm


def overall_accuracy(cm: np.ndarray) -> float:
    """总体精度 = 对角线之和 / 总数。"""
    total = int(cm.sum())
    if total == 0:
        return 0.0
    return float(np.trace(cm) / total)


def classify_supervised(
    features: np.ndarray,
    labels: np.ndarray,
    train_mask: np.ndarray,
    n_classes: int,
    n_estimators: int = 50,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """有监督随机森林分类。

    features (N, F)，labels (N,)，train_mask (N,) bool。
    返回 (predictions (N,), confusion_on_test, report)。
    """
    from sklearn.ensemble import RandomForestClassifier

    features = np.asarray(features, dtype=np.float32)
    labels = np.asarray(labels).astype(np.int64).ravel()
    train_mask = np.asarray(train_mask, dtype=bool).ravel()
    if features.shape[0] != labels.shape[0]:
        raise ValidationError(
            f"features/labels length mismatch: {features.shape[0]} vs {labels.shape[0]}",
        )
    if train_mask.sum() == 0 or (~train_mask).sum() == 0:
        raise ValidationError("need both training and test samples",
                              train=int(train_mask.sum()), test=int((~train_mask).sum()))

    clf = RandomForestClassifier(
        n_estimators=n_estimators, random_state=seed, n_jobs=1,
    )
    clf.fit(features[train_mask], labels[train_mask])
    pred = clf.predict(features).astype(np.int64)

    cm = confusion_matrix(labels[~train_mask], pred[~train_mask], n_classes)
    acc = overall_accuracy(cm)
    report = {
        "mode": "supervised",
        "n_train": int(train_mask.sum()),
        "n_test": int((~train_mask).sum()),
        "overall_accuracy": acc,
        "n_estimators": int(n_estimators),
    }
    return pred, cm, report


def classify_unsupervised(
    features: np.ndarray,
    n_classes: int,
    n_estimators: int = 50,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """无监督辅助：KMeans 伪标签 + 随机森林自训练。

    用于真实输入（无真值标签）。返回 (predictions, agreement_matrix, report)，
    agreement_matrix 为 RF 预测对 KMeans 伪标签的一致性矩阵。
    对 NaN 像素做"剔除 → 训练 → 预测 + 回填"三步处理，保持 NaN 输出。
    """
    from sklearn.cluster import KMeans
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.impute import SimpleImputer

    features = np.asarray(features, dtype=np.float32)
    # NaN-safe：剔除有 NaN 的行（来自 NoData 块），训练后再回填
    nan_mask = np.isnan(features).any(axis=1)
    n_nan = int(nan_mask.sum())
    pred_full = np.zeros(features.shape[0], dtype=np.int64)
    cm = np.zeros((n_classes, n_classes), dtype=np.int64)
    acc = 0.0
    if (~nan_mask).sum() >= n_classes:
        X_valid = features[~nan_mask]
        km = KMeans(n_clusters=n_classes, random_state=seed, n_init=4)
        pseudo = km.fit_predict(X_valid).astype(np.int64)
        clf = RandomForestClassifier(
            n_estimators=n_estimators, random_state=seed, n_jobs=1,
        )
        clf.fit(X_valid, pseudo)
        pred_valid = clf.predict(X_valid).astype(np.int64)
        # 对全图（含 NaN）也预测；NaN 行的预测通过 imputer 填充均值
        if n_nan > 0:
            imputer = SimpleImputer(strategy="mean")
            imputer.fit(X_valid)
            X_full_imputed = imputer.transform(features)
            pred_full = clf.predict(X_full_imputed).astype(np.int64)
        else:
            pred_full = clf.predict(features).astype(np.int64)
        cm = confusion_matrix(pseudo, pred_valid, n_classes)
        acc = overall_accuracy(cm)
    report = {
        "mode": "unsupervised_kmeans",
        "n_samples": int(features.shape[0]),
        "n_skipped_nan": n_nan,
        "overall_accuracy": acc,
        "n_estimators": int(n_estimators),
    }
    return pred_full, cm, report


# ---------------------------------------------------------------------------
# 合成数据：水稻/小麦/玉米 三类时序曲线 + 噪声
# ---------------------------------------------------------------------------
def _class_curves(n_dates: int) -> np.ndarray:
    """三类作物的 σ⁰ 时序曲线 (n_classes, T)，线性强度。"""
    t = np.linspace(0.0, 1.0, n_dates, dtype=np.float32)
    # 水稻：插秧淹水低后向 → 营养生长快速上升（logistic）
    rice = 0.004 + 0.09 / (1.0 + np.exp(-(t - 0.45) * 10.0))
    # 冬小麦：前期高、成熟期下降
    wheat = 0.07 - 0.045 * t + 0.005 * np.sin(2.0 * np.pi * t)
    # 玉米：基值低、盛夏峰值（高斯）
    corn = 0.015 + 0.085 * np.exp(-(((t - 0.55) / 0.22) ** 2))
    return np.stack([rice, wheat, corn], axis=0).astype(np.float32)


def generate_synthetic(
    bbox: List[float],
    n_dates: int = 6,
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 (T, H, W) σ⁰ 立方体 + (H, W) 真值标签（0/1/2 = 水稻/小麦/玉米）。

    三类按横向条带分布，各自施加特征时序曲线 + 乘性/加性噪声。
    返回 (cube, truth_labels, info)。
    """
    if n_dates < 3:
        raise UsageError(f"--n-dates must be >= 3, got {n_dates}", n_dates=int(n_dates))
    rng = np.random.default_rng(seed)
    curves = _class_curves(n_dates)  # (3, T)

    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xn = xx / max(width - 1, 1)
    # 三类地块（条带 + 斜向边界，避免完全竖直）
    yn = yy / max(height - 1, 1)
    boundary = xn + 0.15 * (yn - 0.5)
    truth = np.zeros((height, width), dtype=np.int64)
    truth[boundary >= 1.0 / 3.0] = 1
    truth[boundary >= 2.0 / 3.0] = 2

    cube = np.empty((n_dates, height, width), dtype=np.float32)
    for i in range(n_dates):
        base = curves[truth.ravel(), i].reshape(height, width)
        sig = base * np.exp(rng.normal(0.0, 0.12, size=(height, width))).astype(np.float32)
        sig = sig + rng.normal(0.0, 0.0015, size=(height, width)).astype(np.float32)
        cube[i] = np.clip(sig, 1e-5, None)

    dates = [
        (_dt.date(2024, 4, 1) + _dt.timedelta(days=15 * i)).isoformat()
        for i in range(n_dates)
    ]
    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "n_dates": int(n_dates),
        "class_names": list(CLASS_NAMES),
        "class_curves": curves.tolist(),
        "dates": dates,
        "truth_class_fractions": [float((truth == c).mean()) for c in range(len(CLASS_NAMES))],
    }
    return cube, truth, info


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


def read_geotiff_full(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """扩展版 read：同时返回 nodata 值（若无则为 None）。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
        if nodata is not None:
            nodata = float(nodata)
    return cube, bbox, nodata


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Optional[List[float]]) -> List[float]:
    """校验地理 bbox 合法性，失败抛 ValidationError（exit 6）。"""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats [W S E N]")
    try:
        w, s, e, n = [float(x) for x in bbox]
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox entries must be numeric: {exc}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"latitude out of [-90,90]: S={s}, N={n}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"longitude out of [-180,180]: W={w}, E={e}")
    if s >= n:
        raise ValidationError(
            f"S >= N (S={s}, N={n}); bbox inverted (S must be < N)"
        )
    if w >= e:
        raise ValidationError(
            f"W >= E (W={w}, E={e}); cross-180° bbox not supported. "
            f"Split into two non-antipodal bboxes."
        )
    if (e - w) < 0.001 or (n - s) < 0.001:
        raise ValidationError(
            f"bbox too small ({(e-w):.6f}°×{(n-s):.6f}°); min span is 0.001°"
        )
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# 面积统计
# ---------------------------------------------------------------------------
def class_area_stats(
    labels: np.ndarray,
    class_names: List[str],
    bbox: List[float],
) -> List[Dict[str, Any]]:
    """逐类像元数 / 占比 / 面积（km²）。"""
    h, w = labels.shape
    lat_mid = 0.5 * (bbox[1] + bbox[3])
    px_w_m = (bbox[2] - bbox[0]) / max(w, 1) * 111320.0 * np.cos(np.deg2rad(lat_mid))
    px_h_m = (bbox[3] - bbox[1]) / max(h, 1) * 110540.0
    px_area_m2 = px_w_m * px_h_m
    total = int(labels.size)
    out = []
    for c, name in enumerate(class_names):
        px = int((labels == c).sum())
        out.append({
            "class_id": c,
            "class_name": name,
            "pixels": px,
            "fraction": float(px / total) if total else 0.0,
            "area_km2": float(px * px_area_m2 / 1e6),
        })
    return out


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
    input_nodata: Optional[float] = None,
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
            "n_classes": getattr(args, "n_classes", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
            "input_nodata": input_nodata,
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
    n_classes = args.n_classes

    # 校验 CLI 参数（前置）
    if args.n_dates < 3:
        raise ValidationError(
            f"--n-dates must be >= 3 (got {args.n_dates})"
        )
    if args.n_classes < 2:
        raise ValidationError(
            f"--n-classes must be >= 2 (got {args.n_classes})"
        )
    if args.n_estimators < 1:
        raise ValidationError(
            f"--n-estimators must be >= 1 (got {args.n_estimators})"
        )

    # 1) 获取时序立方体
    synth_info: Optional[Dict[str, Any]] = None
    truth: Optional[np.ndarray] = None
    input_nodata: Optional[float] = None
    n_valid_pixels: Optional[int] = None
    if args.input and not args.synthetic:
        cube, file_bbox, src_nodata = read_geotiff_full(args.input)
        input_nodata = src_nodata
        if bbox is not None:
            bbox = validate_bbox(bbox)
        else:
            bbox = validate_bbox(file_bbox)
        # NoData 处理
        if src_nodata is not None:
            n_total = int(cube[0].size)
            n_nd = int(np.count_nonzero(cube[0] == src_nodata))
            n_valid_pixels = n_total - n_nd
            if n_valid_pixels == 0:
                raise ValidationError(
                    f"input raster has no valid pixels "
                    f"(all {n_nd}/{n_total} are NoData={src_nodata})",
                    path=args.input, nodata=src_nodata,
                )
            cube = np.where(cube == src_nodata, np.nan, cube).astype(np.float32)
        else:
            n_valid_pixels = int(cube[0].size)
        source_note = args.input
        class_names = [f"cluster_{c}" for c in range(n_classes)]
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        cube, truth, synth_info = generate_synthetic(bbox, n_dates=args.n_dates)
        n_classes = len(CLASS_NAMES)
        class_names = list(CLASS_NAMES)
        n_valid_pixels = int(cube[0].size)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.shape[0] < 3:
        raise ValidationError(
            f"need >= 3 dates, got {cube.shape[0]}", dates=int(cube.shape[0]),
        )

    # 校验通过后再建输出目录
    os.makedirs(output_dir, exist_ok=True)

    h, w = cube.shape[1], cube.shape[2]

    # 2) 特征提取
    features, feat_names = temporal_features(cube)

    # 3) 分类
    rng = np.random.default_rng(42)
    if truth is not None:
        train_mask = rng.random(h * w) < 0.35
        pred, cm, report = classify_supervised(
            features, truth.ravel(), train_mask, n_classes,
            n_estimators=args.n_estimators,
        )
    else:
        pred, cm, report = classify_unsupervised(
            features, n_classes, n_estimators=args.n_estimators,
        )

    label_map = pred.reshape(h, w).astype(np.float32)

    # 4) 写出产物
    out_tif = os.path.join(output_dir, "crop_classification.tif")
    write_geotiff(out_tif, label_map, bbox, nodata=-1.0)

    area = class_area_stats(label_map.astype(np.int64), class_names, bbox)
    area_path = os.path.join(output_dir, "crop_area_stats.json")
    with open(area_path, "w", encoding="utf-8") as f:
        json.dump({"class_names": class_names, "classes": area,
                   "pixel_area_m2": area[0]["area_km2"] * 1e6 / max(area[0]["pixels"], 1)},
                  f, ensure_ascii=False, indent=2)

    cm_payload = {
        "class_names": class_names,
        "confusion_matrix": cm.tolist(),
        "overall_accuracy": report["overall_accuracy"],
        "mode": report["mode"],
        "feature_names": feat_names,
        "report": report,
    }
    cm_path = os.path.join(output_dir, "confusion_matrix.json")
    with open(cm_path, "w", encoding="utf-8") as f:
        json.dump(cm_payload, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "mode": report["mode"],
        "n_dates": int(cube.shape[0]),
        "n_classes": int(n_classes),
        "n_features": int(features.shape[1]),
        "n_valid_pixels": int(n_valid_pixels) if n_valid_pixels is not None else None,
        "input_nodata": input_nodata,
        "overall_accuracy": report["overall_accuracy"],
    }
    if synth_info is not None:
        qa["synthetic_truth_class_fractions"] = synth_info["truth_class_fractions"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": area_path, "kind": "json"},
        {"path": cm_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox,
                              input_nodata=input_nodata)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mode: {report['mode']}  n_dates: {cube.shape[0]}  classes: {class_names}")
        print(f"[{SKILL_NAME}] features: {features.shape[1]}  overall accuracy: {report['overall_accuracy']:.3f}")
        for row in area:
            print(f"[{SKILL_NAME}]   {row['class_name']}: {row['fraction']:.3f} "
                  f"({row['area_km2']:.4f} km2)")
        print(f"[{SKILL_NAME}] classification: {out_tif}")
        print(f"[{SKILL_NAME}] area stats:   {area_path}")
        print(f"[{SKILL_NAME}] confusion:    {cm_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="SAR crop classification from multi-temporal backscatter time series.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="multi-temporal backscatter GeoTIFF (band per date)")
    p.add_argument("--n-dates", type=int, default=6,
                   help="number of acquisition dates (synthetic, default: 6)")
    p.add_argument("--n-classes", type=int, default=3,
                   help="number of classes for unsupervised mode (default: 3)")
    p.add_argument("--n-estimators", type=int, default=50,
                   help="Random Forest trees (default: 50)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic scene (offline)")
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
