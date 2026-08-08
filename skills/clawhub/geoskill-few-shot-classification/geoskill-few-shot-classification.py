#!/usr/bin/env python3
"""few-shot-classification — 小样本遥感分类

用极少量标注样本（每类 1~5 个）对遥感影像做分类：以"原型网络"思想，
把每类支持样本的特征均值作为类原型，查询像元按最近原型分类。

本 skill 是 Prototypical Networks 少样本学习的**离线 numpy 等价实现**：
不依赖 torch/tensorflow，而用可验证的流程复现其核心机制——

1. **特征提取**：逐像元光谱特征（波段值），并用支持集统计量标准化；
2. **原型计算**：每个类的原型 = 该类支持样本特征的均值（网络嵌入空间的类中心）；
3. **最近原型分类**：查询像元到各原型取欧氏距离最小者为其类别，
   并用 softmax(-距离) 给出概率（等价于原型网络的度量分类头）；
4. **少样本回合 (episode)**：从标注中抽取 support/query 划分，
   在 query 上评估精度，验证小样本泛化能力。

数据源：本地多波段 GeoTIFF（真实模式用 KMeans 伪标签选支持样本），
或 ``--synthetic`` 生成含真值的三类场景做有监督少样本评估。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python few-shot-classification.py --input scene.tif --n-classes 3 --output-dir ./out
    python few-shot-classification.py --bbox 116 39 117 40 --synthetic --n-shot 3 --output-dir ./out

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
SKILL_NAME = "few-shot-classification"

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
# Input validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate a [W, S, E, N] geographic bbox.

    Raises ValidationError (exit 6) on:
      - non-finite values
      - longitude/latitude out of range
      - W >= E (no antimeridian wrap-around)
      - S >= N
      - zero-area bbox
    """
    w, s, e, n = bbox
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError(
            f"bbox contains non-finite values: W={w} S={s} E={e} N={n}",
            bbox=list(bbox),
        )
    if abs(w) > 180.0 or abs(e) > 180.0:
        raise ValidationError(
            f"bbox longitude out of range: W={w} E={e} (must be in [-180, 180])",
            bbox=list(bbox),
        )
    if abs(s) > 90.0 or abs(n) > 90.0:
        raise ValidationError(
            f"bbox latitude out of range: S={s} N={n} (must be in [-90, 90])",
            bbox=list(bbox),
        )
    if w >= e:
        raise ValidationError(
            f"bbox reversed: W ({w}) must be < E ({e}). "
            f"For antimeridian-crossing bboxes, split into W..180 and -180..E.",
            bbox=list(bbox),
        )
    if s >= n:
        raise ValidationError(
            f"bbox reversed: S ({s}) must be < N ({n})", bbox=list(bbox)
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero area: W={w} S={s} E={e} N={n}", bbox=list(bbox)
        )


def read_geotiff_with_nodata(path: str):
    """Read a multi-band GeoTIFF, replacing NoData with NaN.

    Returns (cube_float32, bbox_WSEN, n_valid_pixel_steps).
    """
    cube, bbox = read_geotiff(path)
    import rasterio
    with rasterio.open(path) as src:
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == nodata, np.nan, cube).astype(np.float32)
    n_valid = int(np.sum(np.isfinite(cube)))
    return cube, bbox, n_valid


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def pixel_features(cube: np.ndarray) -> Tuple[np.ndarray, int, int, int]:
    """(bands, H, W) -> (H*W, bands) 逐像元特征，及维度信息。"""
    cube = np.asarray(cube, dtype=np.float64)
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    if cube.ndim != 3:
        raise ValidationError("cube must be (bands, H, W)", shape=list(cube.shape))
    nb, h, w = cube.shape
    feats = np.moveaxis(cube, 0, -1).reshape(h * w, nb)
    return feats, nb, h, w


def compute_prototypes(features: np.ndarray, labels: np.ndarray,
                       classes: Optional[np.ndarray] = None) -> Tuple[np.ndarray, np.ndarray]:
    """每个类的原型 = 该类样本特征的均值。

    返回 (prototypes[K, F], classes[K])。某类无样本时报错。
    """
    features = np.asarray(features, dtype=np.float64)
    labels = np.asarray(labels).ravel()
    if features.shape[0] != labels.size:
        raise ValidationError("features/labels length mismatch")
    if classes is None:
        classes = np.unique(labels)
    protos: List[np.ndarray] = []
    for c in classes:
        mask = labels == c
        if not np.any(mask):
            raise UsageError(f"class {int(c)} has no support samples", cls=int(c))
        protos.append(features[mask].mean(axis=0))
    return np.stack(protos, axis=0), np.asarray(classes)


def euclidean_distances(x: np.ndarray, prototypes: np.ndarray) -> np.ndarray:
    """计算 x (M, F) 到 prototypes (K, F) 的欧氏距离矩阵 (M, K)。"""
    x = np.asarray(x, dtype=np.float64)
    prototypes = np.asarray(prototypes, dtype=np.float64)
    diff = x[:, None, :] - prototypes[None, :, :]
    return np.sqrt(np.sum(diff * diff, axis=2))


def prototype_probabilities(distances: np.ndarray) -> np.ndarray:
    """softmax(-distance) -> 每个查询对各类的概率 (M, K)，逐行和为 1。"""
    d = np.asarray(distances, dtype=np.float64)
    logits = -d
    logits = logits - logits.max(axis=1, keepdims=True)
    e = np.exp(logits)
    return e / e.sum(axis=1, keepdims=True)


def classify(query: np.ndarray, prototypes: np.ndarray,
             classes: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """最近原型分类。返回 (预测类别, 概率矩阵)。"""
    d = euclidean_distances(query, prototypes)
    probs = prototype_probabilities(d)
    idx = np.argmin(d, axis=1)
    return np.asarray(classes)[idx], probs


def standardize_fit_transform(features: np.ndarray, support_idx: np.ndarray
                              ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """用支持集统计量标准化全部特征（防止泄漏）。"""
    mu = features[support_idx].mean(axis=0)
    sigma = features[support_idx].std(axis=0)
    sigma = np.where(sigma < 1e-9, 1.0, sigma)
    return (features - mu) / sigma, mu, sigma


def few_shot_episode(
    features: np.ndarray,
    labels: np.ndarray,
    n_shot: int,
    seed: int = 42,
) -> Dict[str, Any]:
    """少样本回合：每类抽 n_shot 个支持样本，其余为查询，评估精度。

    返回 {accuracy, n_query, n_classes, n_shot, prototypes}。
    """
    features = np.asarray(features, dtype=np.float64)
    labels = np.asarray(labels).ravel()
    classes = np.unique(labels)
    if n_shot < 1:
        raise UsageError("n_shot must be >= 1", n_shot=int(n_shot))

    rng = np.random.default_rng(seed)
    support_idx: List[int] = []
    query_idx: List[int] = []
    for c in classes:
        idx_c = np.where(labels == c)[0]
        if idx_c.size < n_shot + 1:
            raise ValidationError(
                f"class {int(c)} has only {idx_c.size} samples, need >= {n_shot + 1}",
                cls=int(c), have=int(idx_c.size), need=int(n_shot + 1))
        perm = rng.permutation(idx_c)
        support_idx.extend(perm[:n_shot].tolist())
        query_idx.extend(perm[n_shot:].tolist())
    support_idx = np.array(support_idx, dtype=np.int64)
    query_idx = np.array(query_idx, dtype=np.int64)

    feats_std, _, _ = standardize_fit_transform(features, support_idx)
    prototypes, _ = compute_prototypes(feats_std[support_idx], labels[support_idx], classes)
    pred, probs = classify(feats_std[query_idx], prototypes, classes)
    acc = float(np.mean(pred == labels[query_idx]))
    return {
        "accuracy": acc,
        "n_shot": int(n_shot),
        "n_query": int(query_idx.size),
        "n_classes": int(len(classes)),
        "n_support": int(support_idx.size),
        "mean_confidence": float(np.mean(np.max(probs, axis=1))),
    }


def classify_image(cube: np.ndarray, support_features: np.ndarray,
                   support_labels: np.ndarray) -> np.ndarray:
    """用支持集训练原型，对整幅影像逐像元分类，返回 label_map[H, W]。

    NoData/NaN 像元（任何波段含 NaN）返回 -1 作为 nodata 哨兵。
    """
    feats, nb, h, w = pixel_features(cube)
    # 支持集特征拼接到全体前部以复用标准化
    combined = np.vstack([support_features, feats])
    sup_idx = np.arange(support_features.shape[0])
    combined_std, mu, sigma = standardize_fit_transform(combined, sup_idx)
    sup_std = combined_std[:support_features.shape[0]]
    pix_std = combined_std[support_features.shape[0]:]
    prototypes, classes = compute_prototypes(sup_std, np.asarray(support_labels).ravel())
    # Identify which pixels have any NaN (NoData) — they cannot be classified
    valid_pix = np.all(np.isfinite(pix_std), axis=1)
    pred, _ = classify(pix_std[valid_pix], prototypes, classes)
    label_map = np.full(pix_std.shape[0], -1, dtype=np.int64)
    label_map[valid_pix] = pred
    return label_map.reshape(h, w)


# ---------------------------------------------------------------------------
# 合成数据：3 类光谱可分场景
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    n_bands: int = 4,
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    truth = np.zeros((height, width), dtype=np.int64)
    truth[:, :width // 3] = 0
    truth[:, width // 3:2 * width // 3] = 1
    truth[:, 2 * width // 3:] = 2
    cube = np.zeros((n_bands, height, width), dtype=np.float32)
    for b in range(n_bands):
        layer = np.zeros((height, width), dtype=np.float64)
        layer[truth == 0] = 0.2 + 0.05 * b
        layer[truth == 1] = 0.5 + 0.05 * b
        layer[truth == 2] = 0.8 + 0.05 * b
        layer += rng.normal(0, 0.03, layer.shape)
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
            "n_shot": getattr(args, "n_shot", None),
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
def _pseudo_support(feats, n_classes, n_shot, seed):
    """真实模式：KMeans 伪标签，每簇取 n_shot 个作为支持样本。

    NaN 像素被排除（KMeans 不接受 NaN 输入）。
    """
    from sklearn.cluster import KMeans
    finite_mask = np.all(np.isfinite(feats), axis=1)
    feats_valid = feats[finite_mask]
    if feats_valid.shape[0] < n_classes:
        raise ValidationError(
            f"not enough valid (non-NoData) pixels for KMeans: "
            f"have {feats_valid.shape[0]}, need >= n_classes={n_classes}",
            n_valid=int(feats_valid.shape[0]),
        )
    km = KMeans(n_clusters=n_classes, n_init=10, random_state=seed)
    sub_labels = km.fit_predict(feats_valid)
    # Map back to original indices
    valid_indices = np.where(finite_mask)[0]
    support_idx: List[int] = []
    rng = np.random.default_rng(seed)
    for c in range(n_classes):
        idx_c = valid_indices[sub_labels == c]
        if idx_c.size == 0:
            continue
        take = idx_c[rng.permutation(idx_c.size)[:n_shot]]
        support_idx.extend(take.tolist())
    # Build support labels by re-mapping the support indices to their KMeans labels
    sub_label_map = dict(zip(valid_indices.tolist(), sub_labels.tolist()))
    sup_labels = np.array([sub_label_map[int(i)] for i in support_idx], dtype=np.int64)
    return np.array(support_idx, dtype=np.int64), sup_labels


def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir
    bbox = list(args.bbox) if args.bbox else None
    if bbox is not None:
        validate_bbox(bbox)
    if args.n_classes < 1:
        raise ValidationError(
            f"--n-classes must be >= 1, got {args.n_classes}", n_classes=args.n_classes
        )
    if args.n_shot < 1:
        raise ValidationError(
            f"--n-shot must be >= 1, got {args.n_shot}", n_shot=args.n_shot
        )

    episode: Optional[Dict[str, Any]] = None
    n_valid = 0
    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input raster not found: {args.input}", path=args.input)
        cube, file_bbox, n_valid = read_geotiff_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        validate_bbox(bbox)
        feats, nb, h, w = pixel_features(cube)
        sup_idx, sup_labels = _pseudo_support(feats, args.n_classes, args.n_shot, args.seed)
        label_map = classify_image(cube, feats[sup_idx], sup_labels)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, truth, _ = generate_synthetic(bbox, seed=args.seed)
        feats, nb, h, w = pixel_features(cube)
        episode = few_shot_episode(feats, truth.ravel(), n_shot=args.n_shot, seed=args.seed)
        # 用每类 n_shot 个支持样本对整幅分类
        rng = np.random.default_rng(args.seed)
        sup_idx: List[int] = []
        for c in np.unique(truth):
            idx_c = np.where(truth.ravel() == c)[0]
            sup_idx.extend(rng.permutation(idx_c)[:args.n_shot].tolist())
        sup_idx_arr = np.array(sup_idx, dtype=np.int64)
        label_map = classify_image(cube, feats[sup_idx_arr], truth.ravel()[sup_idx_arr])
        source_note = "synthetic"
        n_valid = int(np.sum(np.isfinite(cube)))

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if n_valid == 0:
        raise ValidationError(
            "input raster has no valid (non-NoData) pixel steps",
            shape=list(cube.shape),
        )

    # Only create output dir after all validations have passed
    os.makedirs(output_dir, exist_ok=True)

    out_tif = os.path.join(output_dir, "classification.tif")
    write_geotiff(out_tif, label_map.astype(np.float32), bbox)

    report = {
        "n_shot": args.n_shot,
        "n_classes": args.n_classes,
        "n_classes_found": int(len(np.unique(label_map))),
    }
    if episode is not None:
        report["episode"] = episode
    report_path = os.path.join(output_dir, "few_shot_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    n_total_pixel_steps = int(cube.shape[0] * cube.shape[1] * cube.shape[2])
    qa: Dict[str, Any] = {
        "source": source_note, "n_shot": args.n_shot,
        "n_valid_pixel_steps": n_valid, "n_total_pixel_steps": n_total_pixel_steps,
    }
    if episode is not None:
        qa["episode_accuracy"] = episode["accuracy"]
        qa["mean_confidence"] = episode["mean_confidence"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  n_shot: {args.n_shot}")
        if episode is not None:
            print(f"[{SKILL_NAME}] episode accuracy: {episode['accuracy']:.3f}  "
                  f"confidence: {episode['mean_confidence']:.3f}")
        print(f"[{SKILL_NAME}] classes found: {report['n_classes_found']}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Few-shot remote-sensing classification (prototypical nearest-centroid).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multispectral GeoTIFF (pseudo few-shot mode)")
    p.add_argument("--n-classes", type=int, default=3, help="number of classes")
    p.add_argument("--n-shot", type=int, default=3, help="support samples per class")
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
