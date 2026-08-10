#!/usr/bin/env python3
"""lulc-accuracy-assessment — 土地覆盖分类精度评估

将分类栅格与参考样本（带真实标签的验证点）对比，构建混淆矩阵并计算一套
标准精度指标：

- **OA**（Overall Accuracy，总体精度）= 对角线之和 / 总样本数
- **Kappa**（Cohen's kappa 系数）= (Po - Pe) / (1 - Pe)，校正随机一致性
- **PA**（Producer's Accuracy，生产者精度）= 对角 / 行和（参考视角，漏分）
- **UA**（User's Accuracy，用户精度）= 对角 / 列和（用户视角，错分）
- **F1** = 2·PA·UA / (PA + UA)，每个类别的调和平均

合成模式下用**分层随机抽样**（stratified random sampling）从真值栅格按类别
均匀抽取验证点，分类栅格 = 真值 + 注入的误分类，因此 OA < 1、Kappa > 0。

数据源：本地 2 波段栅格（band1=分类, band2=参考标签，``--input``）；
``--synthetic`` 生成分类 + 真值 + 验证点用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python lulc-accuracy-assessment.py --bbox 116 39 117 40 --n-points 200 --output-dir ./out
    python lulc-accuracy-assessment.py --input classified_ref.tif --output-dir ./out

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
SKILL_NAME = "lulc-accuracy-assessment"

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


CLASS_NAMES: Dict[int, str] = {
    1: "forest",
    2: "grassland",
    3: "cropland",
    4: "water",
    5: "urban",
}


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------
def validate_bbox(bbox, allow_antimeridian: bool = False):
    """Validate geographic bbox. Returns bbox as list[float] on success.

    Cross-180° (W > E) is rejected with a hint unless ``allow_antimeridian``.
    """
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            f"bbox must be 4 floats [W S E N], got {bbox!r}")
    w, s, e, n = (float(x) for x in bbox)
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0
            and -90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox out of range (-180..180 lon, -90..90 lat): [{w}, {s}, {e}, {n}]")
    if w == e or s == n:
        raise ValidationError(
            f"bbox has zero area: W==E ({w}) or S==N ({s}); "
            f"got [{w}, {s}, {e}, {n}]")
    if s > n:
        raise ValidationError(
            f"bbox S>N (south > north): [{w}, {s}, {e}, {n}]")
    if w > e:
        if not allow_antimeridian:
            raise ValidationError(
                f"bbox crosses antimeridian (W>E: {w}>{e}); "
                f"split into two bboxes and merge results manually")
        return [w, s, e, n]
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# 核心算法：混淆矩阵 + 精度指标
# ---------------------------------------------------------------------------
def build_confusion_matrix(
    reference: np.ndarray,
    predicted: np.ndarray,
    labels: List[int],
) -> np.ndarray:
    """构建混淆矩阵，行=参考（真实），列=预测（分类），元素为样本计数。"""
    ref = np.asarray(reference).ravel()
    pred = np.asarray(predicted).ravel()
    if ref.size != pred.size:
        raise ValidationError("reference and predicted must have equal length")
    labels = list(labels)
    n = len(labels)
    code = {int(l): i for i, l in enumerate(labels)}
    cm = np.zeros((n, n), dtype=np.int64)
    for r, p in zip(ref, pred):
        ri = code.get(int(r))
        pi = code.get(int(p))
        if ri is not None and pi is not None:
            cm[ri, pi] += 1
    return cm


def overall_accuracy(cm: np.ndarray) -> float:
    total = cm.sum()
    if total == 0:
        return 0.0
    return float(np.trace(cm) / total)


def kappa_coefficient(cm: np.ndarray) -> float:
    """Cohen's kappa：(Po - Pe) / (1 - Pe)。"""
    total = float(cm.sum())
    if total == 0:
        return 0.0
    po = float(np.trace(cm)) / total
    row_sum = cm.sum(axis=1).astype(np.float64)
    col_sum = cm.sum(axis=0).astype(np.float64)
    pe = float((row_sum * col_sum).sum()) / (total * total)
    if abs(1.0 - pe) < 1e-12:
        return 1.0 if po >= 1.0 else 0.0
    return (po - pe) / (1.0 - pe)


def producers_accuracy(cm: np.ndarray) -> np.ndarray:
    """生产者精度（逐类）= 对角 / 行和；行和为 0 记 0。"""
    row_sum = cm.sum(axis=1).astype(np.float64)
    diag = np.diag(cm).astype(np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        pa = np.where(row_sum > 0, diag / row_sum, 0.0)
    return pa


def users_accuracy(cm: np.ndarray) -> np.ndarray:
    """用户精度（逐类）= 对角 / 列和；列和为 0 记 0。"""
    col_sum = cm.sum(axis=0).astype(np.float64)
    diag = np.diag(cm).astype(np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        ua = np.where(col_sum > 0, diag / col_sum, 0.0)
    return ua


def f1_scores(pa: np.ndarray, ua: np.ndarray) -> np.ndarray:
    """逐类 F1 = 2·PA·UA / (PA+UA)；分母为 0 记 0。"""
    denom = pa + ua
    with np.errstate(divide="ignore", invalid="ignore"):
        f1 = np.where(denom > 0, 2.0 * pa * ua / denom, 0.0)
    return f1


def accuracy_metrics(
    cm: np.ndarray,
    labels: List[int],
) -> Dict[str, Any]:
    """从混淆矩阵汇总全套精度指标。"""
    pa = producers_accuracy(cm)
    ua = users_accuracy(cm)
    f1 = f1_scores(pa, ua)
    per_class = []
    for i, lab in enumerate(labels):
        per_class.append({
            "class": int(lab),
            "name": CLASS_NAMES.get(int(lab), f"class_{lab}"),
            "producers_accuracy": float(pa[i]),
            "users_accuracy": float(ua[i]),
            "f1": float(f1[i]),
            "reference_count": int(cm.sum(axis=1)[i]),
            "predicted_count": int(cm.sum(axis=0)[i]),
        })
    return {
        "overall_accuracy": overall_accuracy(cm),
        "kappa": kappa_coefficient(cm),
        "total_samples": int(cm.sum()),
        "per_class": per_class,
    }


def stratified_sample(
    truth_raster: np.ndarray,
    n_points: int,
    rng: np.random.Generator,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """分层随机抽样：按类别均匀抽取验证点。

    返回 (rows, cols, labels)，每类约抽 n_points/n_classes 个，
    在该类的像元中均匀随机选取，返回其真实标签。
    """
    labels = np.unique(truth_raster)
    n_classes = labels.size
    if n_classes == 0:
        raise ValidationError("truth raster has no valid classes")
    per = max(1, n_points // n_classes)

    rows: List[int] = []
    cols: List[int] = []
    labs: List[int] = []
    for lab in labels:
        ys, xs = np.where(truth_raster == lab)
        if ys.size == 0:
            continue
        k = min(per, ys.size)
        chosen = rng.choice(ys.size, size=k, replace=False)
        rows.extend(ys[chosen].tolist())
        cols.extend(xs[chosen].tolist())
        labs.extend([int(lab)] * k)
    return (np.asarray(rows, dtype=np.int64),
            np.asarray(cols, dtype=np.int64),
            np.asarray(labs, dtype=np.int64))


# ---------------------------------------------------------------------------
# 合成数据：真值栅格 + 含误差的分类栅格
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    n_points: int = 200,
    width: int = 64,
    height: int = 64,
    error_rate: float = 0.18,
    seed: int = 42,
) -> Dict[str, Any]:
    """生成真值栅格（按象限分 4-5 类）+ 含随机误分类的分类栅格。

    分类栅格 = 真值复制后，随机翻转约 error_rate 比例的像元到其它类别，
    模拟真实分类误差，使总体精度约 1-error_rate。
    """
    rng = np.random.default_rng(seed)
    truth = np.zeros((height, width), dtype=np.int64)
    mid_r, mid_c = height // 2, width // 2
    truth[:mid_r, :mid_c] = 1   # forest
    truth[:mid_r, mid_c:] = 2   # grassland
    truth[mid_r:, :mid_c] = 3   # cropland
    truth[mid_r:, mid_c:] = 4   # water
    # 在右下嵌入一小块 urban
    truth[mid_r + mid_r // 4:, mid_c + mid_c // 4:] = 5

    classified = truth.copy()
    flip = rng.random((height, width)) < error_rate
    classes = np.array(sorted(CLASS_NAMES.keys()), dtype=np.int64)
    for y, x in zip(*np.where(flip)):
        alts = classes[classes != truth[y, x]]
        classified[y, x] = rng.choice(alts)

    rows, cols, ref_labels = stratified_sample(truth, n_points, rng)
    pred_labels = classified[rows, cols]

    return {
        "bbox": list(bbox),
        "width": width,
        "height": height,
        "n_points": int(rows.size),
        "truth": truth.astype(np.int32),
        "classified": classified.astype(np.int32),
        "rows": rows,
        "cols": cols,
        "reference": ref_labels,
        "predicted": pred_labels,
        "error_rate": error_rate,
    }


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


# ---------------------------------------------------------------------------
# HTML 报告
# ---------------------------------------------------------------------------
def render_html_report(
    cm: np.ndarray,
    labels: List[int],
    metrics: Dict[str, Any],
) -> str:
    head = ("<!DOCTYPE html><html><head><meta charset='utf-8'>"
            f"<title>{SKILL_NAME} report</title>"
            "<style>body{font-family:sans-serif;margin:24px}"
            "table{border-collapse:collapse;margin:12px 0}"
            "td,th{border:1px solid #999;padding:4px 10px;text-align:center}"
            "th{background:#eef}</style></head><body>")
    parts = [head, f"<h1>{SKILL_NAME}</h1>"]
    parts.append(f"<p>Overall Accuracy: <b>{metrics['overall_accuracy']:.4f}</b></p>")
    parts.append(f"<p>Kappa: <b>{metrics['kappa']:.4f}</b></p>")
    parts.append(f"<p>Total samples: {metrics['total_samples']}</p>")

    parts.append("<h2>Confusion Matrix (rows=reference, cols=predicted)</h2>")
    names = [CLASS_NAMES.get(int(l), str(l)) for l in labels]
    parts.append("<table><tr><th></th>" +
                 "".join(f"<th>{n}</th>" for n in names) + "</tr>")
    for i, lab in enumerate(labels):
        row = "".join(f"<td>{cm[i, j]}</td>" for j in range(len(labels)))
        parts.append(f"<tr><th>{names[i]}</th>{row}</tr>")
    parts.append("</table>")

    parts.append("<h2>Per-class metrics</h2>")
    parts.append("<table><tr><th>class</th><th>PA</th><th>UA</th><th>F1</th></tr>")
    for pc in metrics["per_class"]:
        parts.append(
            f"<tr><td>{pc['name']}</td><td>{pc['producers_accuracy']:.3f}</td>"
            f"<td>{pc['users_accuracy']:.3f}</td><td>{pc['f1']:.3f}</td></tr>")
    parts.append("</table></body></html>")
    return "".join(parts)


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
            "n_points": getattr(args, "n_points", None),
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
    bbox = list(args.bbox) if args.bbox else None
    synth_info: Optional[Dict[str, Any]] = None

    # ---- Validate bbox and params early ----
    if bbox is not None:
        bbox = validate_bbox(bbox)
    if args.n_points is not None and args.n_points < 1:
        raise ValidationError(
            f"--n-points must be >= 1 in synthetic mode (got {args.n_points})")

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        if bbox is None:
            bbox = validate_bbox(file_bbox)
        if cube.ndim != 3 or cube.shape[0] < 2:
            raise ValidationError(
                "input raster must have 2 bands: band1=classification, band2=reference")
        classified = np.rint(cube[0]).astype(np.int64)
        reference = np.rint(cube[1]).astype(np.int64)
        pred = classified.ravel()
        ref = reference.ravel()
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        synth = generate_synthetic(bbox, n_points=args.n_points)
        synth_info = synth
        ref = synth["reference"]
        pred = synth["predicted"]
        # 也写出分类栅格作为产物
        out_cls = os.path.join(output_dir, "classified.tif")
        write_geotiff(out_cls, synth["classified"].astype(np.float32), bbox)
        source_note = "synthetic"

    if ref.size == 0:
        # Don't create output_dir; surface clear error.
        raise ValidationError("no samples to evaluate")

    # ---- Now safe to create output directory ----
    os.makedirs(output_dir, exist_ok=True)

    labels = sorted(set(np.unique(ref).tolist()) | set(np.unique(pred).tolist()))
    cm = build_confusion_matrix(ref, pred, labels)
    metrics = accuracy_metrics(cm, labels)

    cm_path = os.path.join(output_dir, "confusion_matrix.json")
    with open(cm_path, "w", encoding="utf-8") as f:
        json.dump({"labels": [int(l) for l in labels],
                   "class_names": {str(l): CLASS_NAMES.get(int(l), str(l)) for l in labels},
                   "matrix": cm.tolist()},
                  f, ensure_ascii=False, indent=2)

    metrics_path = os.path.join(output_dir, "accuracy_metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2, default=str)

    html_path = os.path.join(output_dir, "accuracy_report.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(render_html_report(cm, labels, metrics))

    qa: Dict[str, Any] = {
        "source": source_note,
        "overall_accuracy": metrics["overall_accuracy"],
        "kappa": metrics["kappa"],
        "total_samples": metrics["total_samples"],
        "n_classes": len(labels),
    }
    if synth_info is not None:
        qa["injected_error_rate"] = synth_info["error_rate"]

    outputs = [
        {"path": cm_path, "kind": "json"},
        {"path": metrics_path, "kind": "json"},
        {"path": html_path, "kind": "text"},
    ]
    if args.input is None or args.synthetic:
        outputs.append({"path": os.path.join(output_dir, "classified.tif"),
                        "kind": "raster", "crs_epsg": 4326,
                        "bbox_wgs84": bbox, "band_count": 1})

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] samples: {metrics['total_samples']}  classes: {len(labels)}")
        print(f"[{SKILL_NAME}] OA: {metrics['overall_accuracy']:.4f}  "
              f"Kappa: {metrics['kappa']:.4f}")
        print(f"[{SKILL_NAME}] report: {html_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="LULC classification accuracy assessment (confusion matrix, OA/Kappa/PA/UA/F1).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="2-band GeoTIFF: band1=classification, band2=reference")
    p.add_argument("--n-points", type=int, default=200, dest="n_points",
                   help="number of stratified validation points (synthetic mode, default: 200)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic classified scene (offline)")
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
