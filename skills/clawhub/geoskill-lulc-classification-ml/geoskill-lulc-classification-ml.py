#!/usr/bin/env python3
"""lulc-classification-ml — 机器学习土地覆被分类

对多光谱影像执行逐像元监督分类。流程：

1. **特征工程**：以 6 波段反射率为基础，派生 NDVI 与灰度共生/局部方差纹理
   特征，构成逐像元特征向量。
2. **分类器**：RandomForest（``rf``）或梯度提升（``xgboost`` 选项，使用
   scikit-learn 的 ``GradientBoostingClassifier`` 作为离线可用的等价实现）
   逐像元训练与预测。
3. **后处理**：可选的 3×3 众数滤波（``scipy.ndimage``）去除盐噪。
4. **精度评估**：留出验证集上计算总体精度（OA）、Kappa 与混淆矩阵。

合成模式自动生成带标签训练样本（各类地物具有可区分的特征光谱），
完全离线、无网络。

数据源：本地多光谱 GeoTIFF，或 ``--synthetic`` 生成的物理一致模拟影像。

隐私声明 / Privacy：
- 默认离线运行，不访问任何网络服务。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python lulc-classification-ml.py --input scene.tif --n-classes 5 --method rf
    python lulc-classification-ml.py --bbox 116 39 117 40 --n-classes 5 --output-dir ./out

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
SKILL_NAME = "lulc-classification-ml"

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


# ---------------------------------------------------------------------------
# 地物类别定义（6 波段反射率：蓝 绿 红 近红外 短波1 短波2 + 纹理强度）
# 数值为典型地表反射率量级，公开领域知识。
# ---------------------------------------------------------------------------
CLASS_NAMES = ["water", "vegetation", "cropland", "built_up", "bare_soil"]

# 每类在 [blue, green, red, nir, swir1, swir2] 上的中心反射率
CLASS_SPECTRA: Dict[str, List[float]] = {
    "water":      [0.06, 0.05, 0.03, 0.01, 0.005, 0.001],
    "vegetation": [0.03, 0.09, 0.04, 0.48, 0.18, 0.10],
    "cropland":   [0.06, 0.13, 0.11, 0.34, 0.22, 0.15],
    "built_up":   [0.13, 0.15, 0.17, 0.21, 0.25, 0.27],
    "bare_soil":  [0.11, 0.16, 0.21, 0.27, 0.31, 0.33],
}
# 各类纹理强度（局部方差量级）：建成区/裸地纹理强，水体平滑
CLASS_TEXTURE: Dict[str, float] = {
    "water": 0.002,
    "vegetation": 0.03,
    "cropland": 0.05,
    "built_up": 0.08,
    "bare_soil": 0.04,
}


def validate_bbox(bbox) -> None:
    """校验 bbox 是 W<E、S<N、lon∈[-180,180]、lat∈[-90,90]、非零面积。
    跨 180° 经线必须拆成两个子 bbox。"""
    if bbox is None:
        raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range [-180, 180]: W={w}, E={e}",
            bbox=list(bbox),
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range [-90, 90]: S={s}, N={n}",
            bbox=list(bbox),
        )
    if w >= e:
        if w == e:
            raise ValidationError(
                f"bbox has zero width: W==E=={w} (degenerate AOI)",
                bbox=list(bbox),
            )
        raise ValidationError(
            f"bbox is reversed (W={w} >= E={e}); need W < E. "
            f"For datelines that cross 180° (e.g. 179.5 -> -179.5), "
            f"split into two sub-bboxes and run the skill on each separately.",
            bbox=list(bbox),
        )
    if s >= n:
        raise ValidationError(
            f"bbox is reversed (S={s} >= N={n}); need S < N",
            bbox=list(bbox),
        )


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 特征工程
# ---------------------------------------------------------------------------
def compute_ndvi(red: np.ndarray, nir: np.ndarray) -> np.ndarray:
    """归一化植被指数 NDVI = (NIR - RED) / (NIR + RED)，范围 [-1, 1]。"""
    denom = (nir + red).astype(np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        ndvi = np.where(np.abs(denom) < 1e-8, 0.0, (nir - red) / denom)
    return np.clip(ndvi, -1.0, 1.0).astype(np.float32)


def local_variance(arr: np.ndarray, win: int = 3) -> np.ndarray:
    """滑动窗口局部方差，作为纹理特征。

    用均值滤波 E[x] 与 E[x^2] 计算 Var = E[x^2] - E[x]^2。
    """
    from scipy.ndimage import uniform_filter
    a = arr.astype(np.float64)
    m = uniform_filter(a, size=win, mode="reflect")
    m2 = uniform_filter(a * a, size=win, mode="reflect")
    var = m2 - m * m
    return np.clip(var, 0.0, None).astype(np.float32)


def build_features(cube: np.ndarray) -> Tuple[np.ndarray, List[str]]:
    """由 (bands, H, W) 反射率立方体构造逐像元特征矩阵。

    特征顺序：6 个反射率波段 + NDVI + 近红外波段局部方差纹理。
    返回 (features (N, F), feature_names)。
    """
    if cube.ndim != 3 or cube.shape[0] < 4:
        raise ValidationError(
            f"need a (bands,H,W) cube with >=4 bands, got shape {cube.shape}",
            shape=list(cube.shape),
        )
    nb, h, w = cube.shape
    bands = [cube[b].astype(np.float32).ravel() for b in range(min(nb, 6))]
    # 不足 6 波段时补零，保证特征维度稳定
    while len(bands) < 6:
        bands.append(np.zeros(h * w, dtype=np.float32))

    red = cube[2].astype(np.float32) if nb > 2 else np.zeros((h, w), np.float32)
    nir = cube[3].astype(np.float32) if nb > 3 else np.zeros((h, w), np.float32)
    ndvi = compute_ndvi(red, nir).ravel()
    texture = local_variance(nir).ravel()

    feats = np.stack(bands + [ndvi, texture], axis=1).astype(np.float32)
    names = [f"band{b}" for b in range(6)] + ["ndvi", "texture_nir"]
    return feats, names


# ---------------------------------------------------------------------------
# 分类器
# ---------------------------------------------------------------------------
def _make_classifier(method: str, seed: int):
    """构造分类器。

    - ``rf``：RandomForestClassifier。
    - ``xgboost``：离线等价实现，使用 sklearn GradientBoostingClassifier
      （若安装了 xgboost 包亦可无缝替换，但本 skill 不强依赖）。
    """
    if method == "rf":
        from sklearn.ensemble import RandomForestClassifier
        return RandomForestClassifier(
            n_estimators=60, max_depth=None, min_samples_leaf=2,
            n_jobs=1, random_state=seed,
        )
    if method == "xgboost":
        from sklearn.ensemble import GradientBoostingClassifier
        return GradientBoostingClassifier(
            n_estimators=60, max_depth=3, learning_rate=0.15,
            random_state=seed,
        )
    raise UsageError(
        f"unknown method '{method}'. Choose from: ['rf', 'xgboost']",
        method=method,
    )


def confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray,
                     labels: List[int]) -> np.ndarray:
    """逐类混淆矩阵 (len(labels), len(labels))，行=真实，列=预测。"""
    idx = {lab: i for i, lab in enumerate(labels)}
    mat = np.zeros((len(labels), len(labels)), dtype=np.int64)
    for t, p in zip(y_true.ravel(), y_pred.ravel()):
        if t in idx and p in idx:
            mat[idx[int(t)], idx[int(p)]] += 1
    return mat


def accuracy_from_confusion(cm: np.ndarray) -> Dict[str, Any]:
    """由混淆矩阵计算总体精度 OA、Kappa 与逐类生产/用户精度。"""
    total = int(cm.sum())
    if total == 0:
        return {"overall_accuracy": 0.0, "kappa": 0.0,
                "per_class": [], "total_samples": 0}
    correct = int(np.trace(cm))
    oa = correct / total
    row_sum = cm.sum(axis=1).astype(np.float64)
    col_sum = cm.sum(axis=0).astype(np.float64)
    expected = float((row_sum * col_sum).sum()) / total
    kappa = (correct - expected) / (total - expected) if (total - expected) != 0 else 0.0
    per_class = []
    for i in range(cm.shape[0]):
        pa = cm[i, i] / row_sum[i] if row_sum[i] > 0 else 0.0
        ua = cm[i, i] / col_sum[i] if col_sum[i] > 0 else 0.0
        per_class.append({
            "class_index": i,
            "class_name": CLASS_NAMES[i] if i < len(CLASS_NAMES) else f"class_{i}",
            "producer_accuracy": float(pa),
            "user_accuracy": float(ua),
            "support": int(row_sum[i]),
        })
    return {
        "overall_accuracy": float(oa),
        "kappa": float(kappa),
        "per_class": per_class,
        "total_samples": total,
    }


def majority_filter(label_map: np.ndarray, win: int = 3) -> np.ndarray:
    """3×3（默认）众数滤波去除分类盐噪。

    对每个像元取其邻域内出现最多的类别；边界用反射填充。
    """
    from scipy.ndimage import generic_filter

    def _mode(vals):
        vals = vals.astype(np.int64)
        uniq, counts = np.unique(vals, return_counts=True)
        return uniq[np.argmax(counts)]

    if label_map.size == 0:
        return label_map
    return generic_filter(label_map.astype(np.int32), _mode,
                          size=win, mode="reflect").astype(np.int32)


def classify_pixels(
    cube: np.ndarray,
    labels: np.ndarray,
    method: str = "rf",
    test_fraction: float = 0.25,
    apply_filter: bool = True,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """逐像元监督分类主入口。

    参数：
        cube   : (bands, H, W) 反射率立方体
        labels : (H, W) 整数训练标签（与 cube 空间对齐）
        method : 'rf' 或 'xgboost'
        test_fraction : 留出验证比例
        apply_filter  : 是否对结果做众数滤波

    返回 (label_map (H,W) int32, accuracy_dict)。
    """
    if cube.ndim != 3:
        raise ValidationError(f"cube must be 3-D (bands,H,W), got ndim={cube.ndim}")
    _, h, w = cube.shape
    if labels.shape != (h, w):
        raise ValidationError(
            f"labels shape {labels.shape} != image shape {(h, w)}",
            labels_shape=list(labels.shape), image_shape=[h, w],
        )

    feats, feat_names = build_features(cube)
    y = labels.ravel().astype(np.int64)
    class_labels = sorted({int(v) for v in np.unique(y)})
    if len(class_labels) < 2:
        raise ValidationError(
            f"need >=2 classes for classification, found {len(class_labels)}",
            classes=class_labels,
        )

    # 分层训练/验证切分
    rng = np.random.default_rng(seed)
    n = feats.shape[0]
    perm = rng.permutation(n)
    n_test = max(1, int(round(n * test_fraction)))
    test_idx = perm[:n_test]
    train_idx = perm[n_test:]

    clf = _make_classifier(method, seed)
    clf.fit(feats[train_idx], y[train_idx])

    pred_test = clf.predict(feats[test_idx])
    cm = confusion_matrix(y[test_idx], pred_test, class_labels)
    acc = accuracy_from_confusion(cm)
    acc["method"] = method
    acc["feature_names"] = feat_names
    acc["class_labels"] = [int(c) for c in class_labels]
    acc["confusion_matrix"] = cm.tolist()
    acc["n_train"] = int(train_idx.size)
    acc["n_test"] = int(test_idx.size)

    # 全图预测
    pred_all = clf.predict(feats).reshape(h, w).astype(np.int32)
    if apply_filter:
        pred_all = majority_filter(pred_all)

    return pred_all, acc


def class_area_stats(label_map: np.ndarray, bbox: List[float]) -> Dict[str, Any]:
    """统计各类像元数与面积（平面近似，单位 km²）。"""
    w_deg = bbox[2] - bbox[0]
    h_deg = bbox[3] - bbox[1]
    lat_mid = (bbox[1] + bbox[3]) / 2.0
    # 每度经度 ≈ 111.32 * cos(lat) km，每度纬度 ≈ 110.57 km
    km_per_deg_lon = 111.32 * np.cos(np.deg2rad(lat_mid))
    km_per_deg_lat = 110.57
    total_area_km2 = float(w_deg * km_per_deg_lon * h_deg * km_per_deg_lat)

    h, w = label_map.shape
    px_area_km2 = total_area_km2 / max(h * w, 1)
    stats = []
    total_px = int(label_map.size)
    for cls in sorted({int(v) for v in np.unique(label_map)}):
        cnt = int((label_map == cls).sum())
        stats.append({
            "class_index": int(cls),
            "class_name": CLASS_NAMES[cls] if 0 <= cls < len(CLASS_NAMES) else f"class_{cls}",
            "pixel_count": cnt,
            "fraction": cnt / total_px if total_px else 0.0,
            "area_km2": cnt * px_area_km2,
        })
    return {
        "total_pixels": total_px,
        "total_area_km2": total_area_km2,
        "pixel_area_km2": px_area_km2,
        "classes": stats,
    }


# ---------------------------------------------------------------------------
# 合成数据：带标签的多光谱场景（离线）
# ---------------------------------------------------------------------------
def generate_synthetic_scene(
    bbox: List[float],
    n_classes: int = 5,
    width: int = 96,
    height: int = 96,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 (bands,H,W) 反射率立方体 + (H,W) 整数真值标签。

    用一组倾斜条带 + 圆形斑块构造空间分区，每区赋一类地物光谱，
    并叠加高斯噪声，保证类别可分但又非平凡。
    """
    n_classes = int(np.clip(n_classes, 2, len(CLASS_NAMES)))
    rng = np.random.default_rng(seed)
    names = CLASS_NAMES[:n_classes]

    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yn = yy / max(height - 1, 1)
    xn = xx / max(width - 1, 1)

    label = np.zeros((height, width), dtype=np.int32)
    # 用两个斜向梯度把画面切成 n_classes 个条带
    g = (xn * 0.6 + yn * 0.4)
    edges = np.linspace(0.0, 1.0, n_classes + 1)
    for i in range(n_classes):
        m = (g >= edges[i]) & (g < edges[i + 1] + (1e-6 if i == n_classes - 1 else 0.0))
        label[m] = i
    # 在右上叠加一个圆形斑块，强制出现第 0 类（水体）的紧凑区域
    cy, cx = int(height * 0.7), int(width * 0.75)
    rr = ((yy - cy) ** 2 + (xx - cx) ** 2) < (min(height, width) * 0.12) ** 2
    label[rr] = 0

    nb = 6
    cube = np.zeros((nb, height, width), dtype=np.float32)
    for ci, cname in enumerate(names):
        mask = label == ci
        spec = CLASS_SPECTRA[cname]
        tex_amp = CLASS_TEXTURE[cname]
        for b in range(nb):
            base = spec[b]
            noise = rng.normal(0.0, 0.012 + tex_amp, size=(height, width))
            cube[b][mask] = (base + noise[mask]).astype(np.float32)

    cube = np.clip(cube, 0.0, 1.0).astype(np.float32)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "n_classes": n_classes,
        "class_names": names,
        "class_pixel_counts": {
            names[i]: int((label == i).sum()) for i in range(n_classes)
        },
    }
    return cube, label, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    array: np.ndarray,
    bbox: List[float],
    dtype: str = "int32",
    nodata: Optional[float] = None,
) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    arr = array
    if arr.ndim == 2:
        arr = arr[np.newaxis, ...]
    nb, h, w = arr.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(arr[b].astype(dtype), b + 1)


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
            "n_classes": getattr(args, "n_classes", None),
            "method": getattr(args, "method", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
            "bbox": bbox,
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

    # 1) 获取数据 + 训练标签
    #    通用契约：给了 --input 就读真实栅格；否则（含显式 --synthetic）走合成模式。
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        validate_bbox(bbox)
        # 真实模式无外部标签：用反射率 + NDVI 的简单阈值做伪标签引导训练
        labels = auto_pseudo_labels(cube, args.n_classes)
        source_note = args.input
    else:
        validate_bbox(bbox)
        cube, labels, synth_info = generate_synthetic_scene(
            bbox, n_classes=args.n_classes,
        )
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    # 校验通过后再建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 2) 分类
    label_map, acc = classify_pixels(
        cube, labels, method=args.method,
        test_fraction=args.test_fraction,
        apply_filter=not args.no_filter,
        seed=args.seed,
    )

    # 3) 面积统计
    area = class_area_stats(label_map, bbox)

    # 4) 写出产物
    out_tif = os.path.join(output_dir, "lulc_classified.tif")
    write_geotiff(out_tif, label_map, bbox, dtype="int32", nodata=-1)

    acc_path = os.path.join(output_dir, "accuracy.json")
    with open(acc_path, "w", encoding="utf-8") as f:
        json.dump(acc, f, ensure_ascii=False, indent=2)

    area_path = os.path.join(output_dir, "area_stats.json")
    with open(area_path, "w", encoding="utf-8") as f:
        json.dump(area, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "n_classes": int(args.n_classes),
        "overall_accuracy": acc["overall_accuracy"],
        "kappa": acc["kappa"],
        "filter_applied": not args.no_filter,
        "class_names": CLASS_NAMES[:args.n_classes],
    }
    if synth_info is not None:
        qa["synthetic_class_pixel_counts"] = synth_info["class_pixel_counts"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "nodata": -1},
        {"path": acc_path, "kind": "json"},
        {"path": area_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  n_classes: {args.n_classes}")
        print(f"[{SKILL_NAME}] shape: {label_map.shape}")
        print(f"[{SKILL_NAME}] overall accuracy: {acc['overall_accuracy']:.4f}  "
              f"kappa: {acc['kappa']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        print(f"[{SKILL_NAME}] accuracy: {acc_path}")
        print(f"[{SKILL_NAME}] area stats: {area_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def auto_pseudo_labels(cube: np.ndarray, n_classes: int) -> np.ndarray:
    """真实模式的伪标签：用 NDVI 分层 + KMeans 聚类生成训练标签。

    仅用于在缺少外部样本时引导监督分类（真实工作流应替换为人工标注）。
    """
    from sklearn.cluster import KMeans
    nb, h, w = cube.shape
    red = cube[2] if nb > 2 else np.zeros((h, w), np.float32)
    nir = cube[3] if nb > 3 else np.zeros((h, w), np.float32)
    ndvi = compute_ndvi(red, nir)
    feats, _ = build_features(cube)
    k = int(np.clip(n_classes, 2, len(CLASS_NAMES)))
    km = KMeans(n_clusters=k, random_state=0, n_init=4)
    lab = km.fit_predict(feats).reshape(h, w).astype(np.int32)
    # 依据各类平均 NDVI 重排标签，使 0=低 NDVI（偏水/裸），高端=高 NDVI（植被）
    order = sorted(range(k), key=lambda c: float(ndvi[lab == c].mean())
                   if (lab == c).any() else 0.0)
    remap = {old: new for new, old in enumerate(order)}
    out = np.vectorize(remap.get)(lab).astype(np.int32)
    return out


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Per-pixel ML land cover classification (RandomForest / gradient boosting).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multispectral GeoTIFF (surface reflectance)")
    p.add_argument("--n-classes", type=int, default=5,
                   help="number of land cover classes, 2-5 (default: 5)")
    p.add_argument("--method", default="rf", choices=["rf", "xgboost"],
                   help="classifier: rf=RandomForest, xgboost=gradient boosting (default: rf)")
    p.add_argument("--test-fraction", type=float, default=0.25,
                   help="held-out validation fraction (default: 0.25)")
    p.add_argument("--no-filter", action="store_true",
                   help="disable 3x3 majority filter post-processing")
    p.add_argument("--seed", type=int, default=42, help="random seed (default: 42)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent labeled scene (offline)")
    p.add_argument("--output-dir", default="./output", help="output directory")
    p.add_argument("--quiet", action="store_true", help="suppress console output")
    p.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.n_classes < 2 or args.n_classes > len(CLASS_NAMES):
            raise UsageError(
                f"--n-classes must be in [2, {len(CLASS_NAMES)}], got {args.n_classes}",
                n_classes=int(args.n_classes),
            )
        if not (0.0 < args.test_fraction < 1.0):
            raise UsageError(
                f"--test-fraction must be in (0, 1), got {args.test_fraction}",
                test_fraction=float(args.test_fraction),
            )
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
