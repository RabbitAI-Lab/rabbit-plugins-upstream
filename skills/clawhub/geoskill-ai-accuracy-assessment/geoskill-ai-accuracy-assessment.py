#!/usr/bin/env python3
"""ai-accuracy-assessment — AI 模型精度评估

对分类/分割模型的预测结果做全面精度评估：混淆矩阵、总体精度 OA、
逐类 Precision/Recall/F1、平均交并比 mIoU、Cohen's Kappa，以及
空间精度图（局部窗口内的正确率），输出评估报告 JSON 与精度栅格。

本 skill 是模型评测流水线的**离线 numpy 等价实现**：
所有指标均由 numpy 直接计算，可逐项单元测试验证，无任何黑盒依赖——

1. **混淆矩阵**：行为真值、列为预测（NoData 像元不参与统计）；
2. **全局指标**：OA = 对角和/总数；mIoU = 各类 IoU 均值，
   IoU_c = TP / (行和 + 列和 - TP)；Kappa = (po - pe) / (1 - pe)；
3. **逐类指标**：Precision = TP/列和，Recall = TP/行和，F1 为其调和平均；
4. **空间精度图**：用滑动窗口平均 (pred == truth) 的 0/1 图，
   揭示误差的空间分布（哪里错得多）；NoData 区域输出 nodata。

输入校验：标签必须是非负整数类别号（连续值栅格 → exit 6）；
pred/truth 必须同 CRS 且地理范围一致；全 NoData → exit 6；
bbox 不支持跨 180° 经线。

数据源：预测/真值标签栅格（``--input`` + ``--truth``，或单文件双波段），
或 ``--synthetic`` 生成含已知误差块的模拟数据。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python ai-accuracy-assessment.py --input pred.tif --truth ref.tif --output-dir ./out
    python ai-accuracy-assessment.py --bbox 116 39 117 40 --synthetic --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import math
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "ai-accuracy-assessment"
NODATA_OUT = -9999.0

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, DependencyError, ValidationError, ProcessError, to_exit_code,
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
        def __init__(self, m, **k): super().__init__(m, code=3, kind="EDepend", **k)

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
# 校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> List[float]:
    """校验 bbox：有限、在值域内、W<=E（不支持跨 180°）、S<=N、非退化。"""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must have 4 values: W S E N")
    try:
        w, s, e, n = (float(v) for v in bbox)
    except (TypeError, ValueError):
        raise ValidationError(f"bbox values must be numeric, got {bbox!r}")
    for v, name in ((w, "W"), (s, "S"), (e, "E"), (n, "N")):
        if not math.isfinite(v):
            raise ValidationError(f"bbox {name} is not finite: {v}")
    if not (-180.0 <= w <= 180.0) or not (-180.0 <= e <= 180.0):
        raise ValidationError(f"longitude out of range [-180, 180]: W={w}, E={e}")
    if not (-90.0 <= s <= 90.0) or not (-90.0 <= n <= 90.0):
        raise ValidationError(f"latitude out of range [-90, 90]: S={s}, N={n}")
    if w > e:
        raise ValidationError(
            f"bbox crosses the antimeridian (W={w} > E={e}); "
            "this skill does not wrap around 180° — split the request into two bboxes")
    if s > n:
        raise ValidationError(f"bbox has S > N (S={s}, N={n})")
    if w == e or s == n:
        raise ValidationError(f"bbox is degenerate (zero width or height): {bbox}")
    return [w, s, e, n]


def validate_labels(arr: np.ndarray, name: str) -> None:
    """标签值域校验：必须是有限的、非负的整数值类别号。"""
    if not np.all(np.isfinite(arr)):
        raise ValidationError(f"{name} contains non-finite values (NaN/Inf)")
    rounded = np.round(arr)
    if not np.allclose(arr, rounded, atol=1e-4):
        raise ValidationError(
            f"{name} must contain integer class IDs; found non-integer values "
            "(is this a probability/continuous raster instead of labels?)")
    if np.any(rounded < 0):
        raise ValidationError(f"{name} contains negative class labels")
    if rounded.max() > 1_000_000:
        raise ValidationError(
            f"{name} has implausibly large class IDs (max={int(rounded.max())}); "
            "is this really a label raster?")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def confusion_matrix(pred: np.ndarray, truth: np.ndarray,
                     labels: Optional[np.ndarray] = None) -> Tuple[np.ndarray, np.ndarray]:
    """构建混淆矩阵（行=真值，列=预测）。返回 (cm, labels)。"""
    pred = np.asarray(pred).ravel().astype(np.int64)
    truth = np.asarray(truth).ravel().astype(np.int64)
    if pred.size != truth.size:
        raise ValidationError("pred and truth size mismatch",
                              pred=int(pred.size), truth=int(truth.size))
    if pred.size == 0:
        raise ValidationError("pred/truth is empty")
    if labels is None:
        labels = np.unique(np.concatenate([pred, truth]))
    idx = {int(l): i for i, l in enumerate(labels)}
    k = len(labels)
    cm = np.zeros((k, k), dtype=np.int64)
    for t, p in zip(truth, pred):
        if int(t) in idx and int(p) in idx:
            cm[idx[int(t)], idx[int(p)]] += 1
    return cm, labels


def overall_accuracy(cm: np.ndarray) -> float:
    """总体精度 OA = 对角线之和 / 总数。"""
    cm = np.asarray(cm, dtype=np.float64)
    total = cm.sum()
    if total <= 0:
        return 0.0
    return float(np.trace(cm) / total)


def per_class_metrics(cm: np.ndarray) -> List[Dict[str, float]]:
    """逐类 Precision / Recall / F1 / support。"""
    cm = np.asarray(cm, dtype=np.float64)
    out: List[Dict[str, float]] = []
    row_sum = cm.sum(axis=1)
    col_sum = cm.sum(axis=0)
    for c in range(cm.shape[0]):
        tp = cm[c, c]
        precision = tp / col_sum[c] if col_sum[c] > 0 else 0.0
        recall = tp / row_sum[c] if row_sum[c] > 0 else 0.0
        f1 = (2 * precision * recall / (precision + recall)
              if (precision + recall) > 0 else 0.0)
        out.append({
            "class": int(c),
            "precision": float(precision),
            "recall": float(recall),
            "f1": float(f1),
            "support": float(row_sum[c]),
        })
    return out


def mean_iou(cm: np.ndarray) -> Tuple[float, List[float]]:
    """平均交并比 mIoU 与逐类 IoU。IoU_c = TP / (行和 + 列和 - TP)。"""
    cm = np.asarray(cm, dtype=np.float64)
    row_sum = cm.sum(axis=1)
    col_sum = cm.sum(axis=0)
    ious: List[float] = []
    for c in range(cm.shape[0]):
        tp = cm[c, c]
        union = row_sum[c] + col_sum[c] - tp
        ious.append(float(tp / union) if union > 0 else 0.0)
    return float(np.mean(ious)), ious


def cohens_kappa(cm: np.ndarray) -> float:
    """Cohen's Kappa = (po - pe) / (1 - pe)。"""
    cm = np.asarray(cm, dtype=np.float64)
    total = cm.sum()
    if total <= 0:
        return 0.0
    po = float(np.trace(cm) / total)
    row_sum = cm.sum(axis=1)
    col_sum = cm.sum(axis=0)
    pe = float(np.sum(row_sum * col_sum) / (total * total))
    if abs(1.0 - pe) < 1e-12:
        return 1.0
    return float((po - pe) / (1.0 - pe))


def spatial_accuracy_map(pred: np.ndarray, truth: np.ndarray, window: int = 7,
                         valid_mask: Optional[np.ndarray] = None) -> np.ndarray:
    """局部精度图：窗口内 (pred == truth) 的比例，范围 [0, 1]。

    提供 valid_mask 时，NoData 像元不参与窗口统计；无有效像元的窗口输出 NaN。
    """
    try:
        from scipy.ndimage import uniform_filter
    except ImportError as exc:
        raise DependencyError(f"scipy is required for the spatial accuracy map: {exc}")
    pred = np.asarray(pred)
    truth = np.asarray(truth)
    if pred.shape != truth.shape:
        raise ValidationError("pred/truth shape mismatch",
                              pred=list(pred.shape), truth=list(truth.shape))
    if window < 1:
        raise UsageError("window must be >= 1", window=int(window))
    if valid_mask is None:
        correct = (pred == truth).astype(np.float64)
        if window == 1:
            return correct
        return uniform_filter(correct, size=window, mode="nearest")
    vm = np.asarray(valid_mask, dtype=bool)
    if vm.shape != pred.shape:
        raise ValidationError("valid_mask shape mismatch")
    correct = ((pred == truth) & vm).astype(np.float64)
    if window == 1:
        return np.where(vm, correct, np.nan)
    sum_correct = uniform_filter(correct, size=window, mode="nearest")
    sum_valid = uniform_filter(vm.astype(np.float64), size=window, mode="nearest")
    with np.errstate(invalid="ignore", divide="ignore"):
        acc = np.where(sum_valid > 0, sum_correct / sum_valid, np.nan)
    return acc


def assess(pred: np.ndarray, truth: np.ndarray, window: int = 7,
           valid_mask: Optional[np.ndarray] = None) -> Dict[str, Any]:
    """完整精度评估：全局指标 + 逐类指标 + 空间精度图。"""
    if valid_mask is None:
        p_flat, t_flat = np.asarray(pred), np.asarray(truth)
        n_valid = int(p_flat.size)
    else:
        vm = np.asarray(valid_mask, dtype=bool)
        p_flat, t_flat = np.asarray(pred)[vm], np.asarray(truth)[vm]
        n_valid = int(vm.sum())
    cm, labels = confusion_matrix(p_flat, t_flat)
    miou, ious = mean_iou(cm)
    per_cls = per_class_metrics(cm)
    for c, iou_val in enumerate(ious):
        per_cls[c]["iou"] = iou_val
    acc_map = spatial_accuracy_map(pred, truth, window, valid_mask)
    return {
        "labels": [int(l) for l in labels],
        "confusion_matrix": cm.tolist(),
        "overall_accuracy": overall_accuracy(cm),
        "mean_iou": miou,
        "cohens_kappa": cohens_kappa(cm),
        "macro_f1": float(np.mean([m["f1"] for m in per_cls])) if per_cls else 0.0,
        "per_class": per_cls,
        "accuracy_map": acc_map,
        "n_pixels": n_valid,
    }


# ---------------------------------------------------------------------------
# 合成数据：真值条带 + 已知误差块
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 64,
    height: int = 64,
    error_frac: float = 0.08,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """返回 (pred, truth, info)。

    真值是 3 条竖直类别条带；预测 = 真值 + 一块系统性错分方块 +
    散布的随机错分，便于验证空间精度图能定位误差。
    """
    rng = np.random.default_rng(seed)
    truth = np.zeros((height, width), dtype=np.int64)
    truth[:, width // 3:2 * width // 3] = 1
    truth[:, 2 * width // 3:] = 2

    pred = truth.copy()
    # 系统性误差块：中心区域把类别 1 错分为 0
    y0, y1 = height // 4, 3 * height // 4
    x0, x1 = 3 * width // 8, 5 * width // 8
    block = (pred[y0:y1, x0:x1] == 1)
    pred[y0:y1, x0:x1][block] = 0
    # 随机散布误差
    n_rand = int(error_frac * pred.size)
    flat_idx = rng.choice(pred.size, size=n_rand, replace=False)
    yy, xx = np.unravel_index(flat_idx, pred.shape)
    pred[yy, xx] = (truth[yy, xx] + rng.integers(1, 3, size=n_rand)) % 3

    info = {
        "bbox": bbox, "width": width, "height": height,
        "error_block_px": [x0, y0, x1, y1],
    }
    return pred, truth, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def _import_rasterio():
    try:
        import rasterio
        return rasterio
    except ImportError as exc:
        raise DependencyError(f"rasterio is required for GeoTIFF I/O: {exc}")


def write_geotiff(path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
    rasterio = _import_rasterio()
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
    """读取 GeoTIFF，返回 (cube, bbox)。保留原签名（单元测试依赖）。"""
    rasterio = _import_rasterio()
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_labels(path: str) -> Tuple[np.ndarray, List[float], Optional[float], Any, Any]:
    """读取标签栅格全量元数据：(cube, bbox, nodata, crs, transform)。"""
    rasterio = _import_rasterio()
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    try:
        with rasterio.open(path) as src:
            cube = src.read().astype(np.float32)
            b = src.bounds
            bbox = [b.left, b.bottom, b.right, b.top]
            nodata = src.nodata
            crs = src.crs
            transform = src.transform
    except Exception as exc:
        raise ValidationError(f"cannot read input raster '{path}': {exc}")
    return cube, bbox, nodata, crs, transform


def reproject_labels_to_wgs84(cube: np.ndarray, nodata: Optional[float],
                              src_transform, src_crs) -> Tuple[np.ndarray, List[float]]:
    """把投影坐标系的标签栅格重投影到 EPSG:4326（最近邻，保类别）。"""
    _import_rasterio()
    from rasterio.warp import calculate_default_transform, reproject, Resampling
    from rasterio.transform import array_bounds
    nb, h, w = cube.shape
    left, bottom, right, top = array_bounds(h, w, src_transform)
    dst_transform, dst_w, dst_h = calculate_default_transform(
        src_crs, "EPSG:4326", w, h, left, bottom, right, top)
    dst_nodata = float(nodata) if nodata is not None else -9999.0
    dst = np.full((nb, dst_h, dst_w), dst_nodata, dtype=np.float32)
    for b in range(nb):
        reproject(
            source=cube[b], destination=dst[b],
            src_transform=src_transform, src_crs=src_crs,
            dst_transform=dst_transform, dst_crs="EPSG:4326",
            src_nodata=nodata if nodata is not None else None,
            dst_nodata=dst_nodata,
            resampling=Resampling.nearest,
        )
    l2, b2, r2, t2 = array_bounds(dst_h, dst_w, dst_transform)
    return dst, [l2, b2, r2, t2]


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
            "truth": getattr(args, "truth", None),
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
def _check_grid_alignment(bbox_a: List[float], bbox_b: List[float],
                          shape_a: Tuple[int, ...], shape_b: Tuple[int, ...]) -> None:
    """pred/truth 地理配准一致性检查（同形状 + 同范围）。"""
    if tuple(shape_a[-2:]) != tuple(shape_b[-2:]):
        raise ValidationError("pred/truth grid shape mismatch",
                              pred=list(shape_a), truth=list(shape_b))
    tol_x = abs(bbox_a[2] - bbox_a[0]) / max(shape_a[-1], 1) * 0.5 + 1e-9
    tol_y = abs(bbox_a[3] - bbox_a[1]) / max(shape_a[-2], 1) * 0.5 + 1e-9
    for i in range(4):
        tol = tol_x if i in (0, 2) else tol_y
        if abs(bbox_a[i] - bbox_b[i]) > tol:
            raise ValidationError(
                f"pred and truth are not geographically aligned "
                f"(bounds differ at index {i}: {bbox_a[i]} vs {bbox_b[i]}); "
                "compare only co-registered rasters")


def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    bbox = list(args.bbox) if args.bbox else None

    if args.truth and not args.input:
        raise UsageError("--truth requires --input")

    if args.input and not args.synthetic:
        cube, file_bbox, pred_nodata, pred_crs, pred_transform = read_labels(args.input)
        if pred_crs is None:
            raise ValidationError(
                "input raster has no coordinate reference system (CRS) defined")
        # 双波段 [pred, truth] 或 --truth 单波段
        if args.truth:
            truth_cube, truth_bbox, truth_nodata, truth_crs, truth_transform = \
                read_labels(args.truth)
            if truth_crs is None:
                raise ValidationError(
                    "truth raster has no coordinate reference system (CRS) defined")
            if pred_crs != truth_crs:
                raise ValidationError(
                    f"pred/truth CRS mismatch: {pred_crs} vs {truth_crs}")
            if pred_crs.is_projected:
                # 投影坐标 → 重投影到 WGS84（最近邻，保类别）
                cube, file_bbox = reproject_labels_to_wgs84(
                    cube, pred_nodata, pred_transform, pred_crs)
                truth_cube, truth_bbox = reproject_labels_to_wgs84(
                    truth_cube, truth_nodata, truth_transform, truth_crs)
            pred_raw = cube[0]
            truth_raw = truth_cube[0]
        elif cube.shape[0] >= 2:
            if pred_crs.is_projected:
                cube, file_bbox = reproject_labels_to_wgs84(
                    cube, pred_nodata, pred_transform, pred_crs)
            pred_raw = cube[0]
            truth_raw = cube[1]
            truth_bbox, truth_nodata = file_bbox, pred_nodata
        else:
            raise ValidationError(
                "need truth labels: provide --truth <raster> or a 2-band input "
                "[band1=pred, band2=truth]")
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        pred_i, truth_i, _ = generate_synthetic(bbox, seed=args.seed)
        pred_raw = pred_i.astype(np.float32)
        truth_raw = truth_i.astype(np.float32)
        truth_bbox = bbox
        pred_nodata = truth_nodata = None
        source_note = "synthetic"

    bbox = validate_bbox(bbox)

    if pred_raw.size == 0 or truth_raw.size == 0:
        raise ValidationError("input is empty")
    if args.input and not args.synthetic and args.truth:
        _check_grid_alignment(file_bbox, truth_bbox, pred_raw.shape, truth_raw.shape)
    if pred_raw.shape != truth_raw.shape:
        raise ValidationError("pred/truth shape mismatch",
                              pred=list(pred_raw.shape), truth=list(truth_raw.shape))

    # NoData / NaN 掩码：无效像元不参与任何统计
    valid = np.isfinite(pred_raw) & np.isfinite(truth_raw)
    if pred_nodata is not None:
        valid &= (pred_raw != np.float32(pred_nodata))
    if truth_nodata is not None:
        valid &= (truth_raw != np.float32(truth_nodata))
    if not valid.any():
        raise ValidationError("pred/truth are entirely NoData — nothing to assess")

    pred_v = pred_raw[valid]
    truth_v = truth_raw[valid]
    # 标签值域校验（整数类别号）
    validate_labels(pred_v, "pred labels")
    validate_labels(truth_v, "truth labels")

    pred = np.round(pred_raw).astype(np.int64)
    truth = np.round(truth_raw).astype(np.int64)

    report = assess(pred, truth, window=args.window, valid_mask=valid)
    acc_map = report.pop("accuracy_map")
    report["n_pixels_total"] = int(pred_raw.size)
    report["valid_pixel_fraction"] = float(valid.mean())

    report_path = os.path.join(output_dir, "accuracy_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    # 空间精度图：NaN（无有效像元的窗口）输出为 nodata
    acc_out = np.where(np.isnan(acc_map), NODATA_OUT, acc_map).astype(np.float32)
    acc_tif = os.path.join(output_dir, "spatial_accuracy.tif")
    write_geotiff(acc_tif, acc_out, bbox, nodata=NODATA_OUT)

    qa: Dict[str, Any] = {
        "source": source_note,
        "overall_accuracy": report["overall_accuracy"],
        "mean_iou": report["mean_iou"],
        "cohens_kappa": report["cohens_kappa"],
        "macro_f1": report["macro_f1"],
        "n_pixels": report["n_pixels"],
        "valid_pixel_fraction": report["valid_pixel_fraction"],
    }
    outputs = [
        {"path": report_path, "kind": "json"},
        {"path": acc_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] OA: {report['overall_accuracy']:.4f}  "
              f"mIoU: {report['mean_iou']:.4f}  Kappa: {report['cohens_kappa']:.4f}")
        print(f"[{SKILL_NAME}] valid pixels: {report['n_pixels']}/{report['n_pixels_total']} "
              f"({report['valid_pixel_fraction'] * 100:.1f}%)")
        print(f"[{SKILL_NAME}] report: {report_path}")
        print(f"[{SKILL_NAME}] spatial accuracy: {acc_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="AI model accuracy assessment (OA/mIoU/F1/Kappa + spatial accuracy map).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="prediction labels GeoTIFF (or 2-band [pred, truth])")
    p.add_argument("--truth", help="ground-truth labels GeoTIFF (optional with --input)")
    p.add_argument("--window", type=int, default=7, help="spatial accuracy window size (>=1)")
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
