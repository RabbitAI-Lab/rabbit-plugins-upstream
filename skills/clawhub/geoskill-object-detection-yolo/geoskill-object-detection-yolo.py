#!/usr/bin/env python3
"""object-detection-yolo — 遥感目标检测

在遥感影像上检测感兴趣目标（如建筑、车辆、船只等明亮/高对比地物），
输出带地理坐标的检测框 GeoJSON。

本 skill 是 YOLO/深度目标检测器的**离线 numpy 等价实现**：
不依赖 torch/ultralytics，而用可验证的经典流程复现"检测"的核心逻辑——

1. **滑窗扫描**：在影像上以固定窗口 + 步长滑动；
2. **目标性打分**：对每个窗口计算"显著性"（局部均值相对全图的 z-score，
   可选 HOG 梯度能量），超过阈值的窗口记为候选检测；
3. **非极大值抑制 NMS**：按 IoU 去除重叠冗余框，保留最高分；
4. **地理编码**：把像元框经仿射变换转成 WGS-84 经纬度框，写 GeoJSON。

数据源：本地单/多波段 GeoTIFF（取首波段作为强度），或 ``--synthetic``
生成含若干明亮方形目标的模拟影像用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python object-detection-yolo.py --input scene.tif --output-dir ./out
    python object-detection-yolo.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "object-detection-yolo"

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
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox, source: str = "bbox") -> None:
    """校验 EPSG:4326 经纬度 bbox：W<=E、S<=N、超经纬度→ValidationError(6)。
    跨 180° 经线（|E-W| > 360）→ValidationError 并附"拆分为两侧"提示。
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(
            f"{source} must be [W, S, E, N] with 4 floats, got {bbox!r}",
            bbox=bbox,
        )
    w, s, e, n = bbox
    if not all(isinstance(v, (int, float)) and np.isfinite(v) for v in (w, s, e, n)):
        raise ValidationError(
            f"{source} contains non-finite values: {bbox!r}", bbox=bbox,
        )
    if w < -180.0 or e > 180.0 or s < -90.0 or n > 90.0:
        raise ValidationError(
            f"{source} out of WGS-84 range (lon∈[-180,180], lat∈[-90,90]): {bbox!r}",
            bbox=bbox,
        )
    if w > e:
        raise ValidationError(
            f"{source} has W>E ({w} > {e}); cross-dateline not supported. "
            f"Split into two bboxes (e.g. [{w}, {s}, 180, {n}] and [-180, {s}, {e}, {n}]) "
            f"and run separately.",
            bbox=bbox,
        )
    if s > n:
        raise ValidationError(
            f"{source} has S>N ({s} > {n}); latitude must increase northward", bbox=bbox,
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"{source} too small (Δlon={e - w}, Δlat={n - s}); must be > 1e-9 degrees",
            bbox=bbox,
        )


def validate_window_params(win_size: int, step: int) -> None:
    """校验滑窗/步长参数：win_size ≥ 2（< 2 物理无意义），step ≥ 1。"""
    if win_size is None or not isinstance(win_size, int) or win_size < 2:
        raise ValidationError(
            f"--win-size must be a positive integer >= 2 (got {win_size!r})",
            win_size=win_size,
        )
    if step is None or not isinstance(step, int) or step < 1:
        raise ValidationError(
            f"--step must be a positive integer >= 1 (got {step!r})",
            step=step,
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def iou(box_a: np.ndarray, box_b: np.ndarray) -> float:
    """计算两个 [x1, y1, x2, y2] 框的交并比 (IoU)。"""
    a = np.asarray(box_a, dtype=np.float64)
    b = np.asarray(box_b, dtype=np.float64)
    ix1 = max(a[0], b[0])
    iy1 = max(a[1], b[1])
    ix2 = min(a[2], b[2])
    iy2 = min(a[3], b[3])
    iw = max(0.0, ix2 - ix1)
    ih = max(0.0, iy2 - iy1)
    inter = iw * ih
    area_a = max(0.0, a[2] - a[0]) * max(0.0, a[3] - a[1])
    area_b = max(0.0, b[2] - b[0]) * max(0.0, b[3] - b[1])
    union = area_a + area_b - inter
    if union <= 0.0:
        return 0.0
    return float(inter / union)


def nms(
    boxes: np.ndarray,
    scores: np.ndarray,
    iou_thresh: float = 0.5,
) -> np.ndarray:
    """非极大值抑制。

    参数
    ----
    boxes : (N, 4) 数组，每行 [x1, y1, x2, y2]
    scores : (N,) 数组，检测置信度
    iou_thresh : 当两个保留框的 IoU 超过该阈值时，丢弃低分框

    返回保留下来的框的索引（按分数从高到低排序）。
    """
    boxes = np.asarray(boxes, dtype=np.float64)
    scores = np.asarray(scores, dtype=np.float64)
    if boxes.size == 0:
        return np.empty((0,), dtype=np.int64)
    order = np.argsort(-scores)
    keep: List[int] = []
    while order.size > 0:
        i = int(order[0])
        keep.append(i)
        if order.size == 1:
            break
        rest = order[1:]
        survivors: List[int] = []
        for j in rest:
            if iou(boxes[i], boxes[j]) < iou_thresh:
                survivors.append(int(j))
        order = np.asarray(survivors, dtype=np.int64)
    return np.asarray(keep, dtype=np.int64)


def hog_energy(patch: np.ndarray) -> float:
    """简化的 HOG 梯度能量：Sobel 梯度幅值的均值。

    用于刻画窗口内的"结构/边缘丰富程度"，是 HOG 特征的轻量等价。
    """
    p = np.asarray(patch, dtype=np.float64)
    if p.size == 0:
        return 0.0
    kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float64)
    ky = kx.T
    from scipy.signal import convolve2d
    gx = convolve2d(p, kx, mode="same", boundary="symm")
    gy = convolve2d(p, ky, mode="same", boundary="symm")
    mag = np.sqrt(gx * gx + gy * gy)
    return float(np.mean(mag))


def window_score(
    patch: np.ndarray,
    global_mean: float,
    global_std: float,
    feature: str = "intensity",
) -> float:
    """对单个滑窗打分。

    feature="intensity" 用局部均值的 z-score（适合检测明亮目标）；
    feature="hog" 用梯度能量（适合检测结构丰富的目标）。
    """
    p = np.asarray(patch, dtype=np.float64)
    if p.size == 0:
        return 0.0
    if feature == "hog":
        return hog_energy(p)
    std = global_std if global_std > 1e-9 else 1.0
    return float((np.mean(p) - global_mean) / std)


def sliding_window_detect(
    image: np.ndarray,
    win_size: int = 16,
    step: int = 8,
    score_thresh: float = 1.5,
    feature: str = "intensity",
) -> Tuple[np.ndarray, np.ndarray]:
    """在 2D 影像上滑窗扫描，返回 (候选框, 分数)。

    框为像素坐标 [x1, y1, x2, y2]（x=列, y=行）。
    """
    img = np.asarray(image, dtype=np.float64)
    if img.ndim != 2:
        raise ValidationError("sliding_window_detect expects a 2D image", shape=list(img.shape))
    h, w = img.shape
    if win_size > h or win_size > w:
        raise ValidationError(
            f"window size {win_size} larger than image ({w}x{h})",
            win_size=int(win_size), image=[int(w), int(h)],
        )
    finite = img[np.isfinite(img)]
    global_mean = float(np.mean(finite)) if finite.size else 0.0
    global_std = float(np.std(finite)) if finite.size else 1.0

    boxes: List[List[float]] = []
    scores: List[float] = []
    for y in range(0, h - win_size + 1, step):
        for x in range(0, w - win_size + 1, step):
            patch = img[y:y + win_size, x:x + win_size]
            s = window_score(patch, global_mean, global_std, feature)
            if s >= score_thresh:
                boxes.append([x, y, x + win_size, y + win_size])
                scores.append(s)
    return np.asarray(boxes, dtype=np.float64), np.asarray(scores, dtype=np.float64)


def detect_objects(
    image: np.ndarray,
    win_size: int = 16,
    step: int = 8,
    score_thresh: float = 1.5,
    iou_thresh: float = 0.5,
    feature: str = "intensity",
) -> Tuple[np.ndarray, np.ndarray]:
    """完整检测流程：滑窗打分 + NMS。返回 (保留框, 保留分数)。"""
    boxes, scores = sliding_window_detect(
        image, win_size, step, score_thresh, feature
    )
    if boxes.size == 0:
        return boxes, scores
    keep = nms(boxes, scores, iou_thresh)
    return boxes[keep], scores[keep]


def pixel_box_to_geo(
    box: np.ndarray,
    bbox: List[float],
    img_w: int,
    img_h: int,
) -> List[float]:
    """把像素框 [x1, y1, x2, y2] 转成地理框 [minLon, minLat, maxLon, maxLat]。

    采用简单的线性仿射：列 -> 经度，行 -> 纬度（行向下增大，纬度递减）。
    """
    w, s, e, n = bbox
    x1, y1, x2, y2 = [float(v) for v in box]
    lon1 = w + (x1 / img_w) * (e - w)
    lon2 = w + (x2 / img_w) * (e - w)
    lat1 = n - (y1 / img_h) * (n - s)  # 上边（y 小）纬度大
    lat2 = n - (y2 / img_h) * (n - s)  # 下边（y 大）纬度小
    return [min(lon1, lon2), min(lat1, lat2), max(lon1, lon2), max(lat1, lat2)]


def boxes_to_geojson(
    boxes: np.ndarray,
    scores: np.ndarray,
    bbox: List[float],
    img_w: int,
    img_h: int,
) -> Dict[str, Any]:
    """把检测框打包成 GeoJSON FeatureCollection（WGS-84 多边形）。"""
    features: List[Dict[str, Any]] = []
    for idx, (box, sc) in enumerate(zip(boxes, scores)):
        gminx, gminy, gmaxx, gmaxy = pixel_box_to_geo(box, bbox, img_w, img_h)
        ring = [
            [gminx, gminy], [gmaxx, gminy], [gmaxx, gmaxy],
            [gminx, gmaxy], [gminx, gminy],
        ]
        features.append({
            "type": "Feature",
            "id": int(idx),
            "properties": {
                "object_id": int(idx),
                "score": float(sc),
                "pixel_box": [float(v) for v in box],
            },
            "geometry": {"type": "Polygon", "coordinates": [ring]},
        })
    return {"type": "FeatureCollection", "features": features}


# ---------------------------------------------------------------------------
# 合成数据：含若干明亮方形目标的模拟影像（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    n_targets: int = 4,
    target_size: int = 12,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成暗背景 + 若干明亮方形目标的影像。

    返回 (image[H, W], info)。真值目标框（像素坐标）记录在 info 里。
    """
    rng = np.random.default_rng(seed)
    img = rng.normal(20.0, 3.0, size=(height, width)).astype(np.float32)
    truth_boxes: List[List[int]] = []
    pad = target_size + 2
    ys = np.linspace(pad, height - pad - target_size, n_targets).astype(int)
    xs = np.linspace(pad, width - pad - target_size, n_targets).astype(int)
    for k in range(n_targets):
        y = int(ys[k])
        x = int(xs[k])
        img[y:y + target_size, x:x + target_size] += 120.0
        truth_boxes.append([x, y, x + target_size, y + target_size])
    info = {
        "bbox": bbox, "width": width, "height": height,
        "n_targets": n_targets, "truth_boxes": truth_boxes,
    }
    return img, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    arr = np.asarray(array, dtype=np.float32)
    if arr.ndim == 2:
        arr = arr[np.newaxis, ...]
    # NaN → nodata（GeoTIFF 物理写盘前必须把 NaN 替换为 sentinel，否则 rasterio 写 -inf 异常）
    arr = np.where(np.isnan(arr), np.float32(nodata), arr)
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
            dst.write(arr[b], b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """读 GeoTIFF，返回 (cube[C, H, W] float32, bbox) — band0 的 NoData 标记 → NaN。
    NaN 在滑窗均值/HOG 梯度中自然传播，使含 NoData 的窗口不进入候选（s<score_thresh 为 False）。
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nd = src.nodata
        if nd is not None and np.isfinite(nd) and cube.shape[0] >= 1:
            cube[0][cube[0] == float(nd)] = np.nan
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
            "feature": getattr(args, "feature", None),
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
    synth_info: Optional[Dict[str, Any]] = None

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        image = cube[0] if cube.ndim == 3 else cube
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox, source="--bbox")
        image, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    if bbox is not None:
        # 即便 --input 路径也要校验（输入数据本身可能越界/颠倒）
        validate_bbox(bbox, source="bbox from --input")

    if image.size == 0:
        raise ValidationError("input raster is empty")

    # 输入栅格全 NoData 校验
    finite_mask = np.isfinite(image)
    if not finite_mask.any():
        raise ValidationError(
            "input raster has no valid (non-NoData) pixels",
            shape=list(image.shape),
        )

    validate_window_params(args.win_size, args.step)

    boxes, scores = detect_objects(
        image,
        win_size=args.win_size,
        step=args.step,
        score_thresh=args.score_thresh,
        iou_thresh=args.iou_thresh,
        feature=args.feature,
    )
    h, w = image.shape
    geojson = boxes_to_geojson(boxes, scores, bbox, w, h)

    det_path = os.path.join(output_dir, "detections.geojson")
    with open(det_path, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    # score_map：初始为 nodata（保留输入 NoData 标记），有效像元处写入检测得分
    score_map = np.full(image.shape, -9999.0, dtype=np.float32)
    score_map[finite_mask] = 0.0  # 有效像元默认 0（无检测）
    for box, sc in zip(boxes, scores):
        x1, y1, x2, y2 = [int(round(v)) for v in box]
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(w, x2), min(h, y2)
        if x2 > x1 and y2 > y1:
            score_map[y1:y2, x1:x2] = np.maximum(
                score_map[y1:y2, x1:x2], float(sc)
            )
    score_path = os.path.join(output_dir, "score_map.tif")
    write_geotiff(score_path, score_map, bbox)

    qa: Dict[str, Any] = {
        "source": source_note,
        "feature": args.feature,
        "n_detections": int(len(boxes)),
        "n_valid_pixels": int(finite_mask.sum()),
        "n_total_pixels": int(finite_mask.size),
        "mean_score": float(np.mean(scores)) if len(scores) else 0.0,
        "max_score": float(np.max(scores)) if len(scores) else 0.0,
    }
    if synth_info is not None:
        qa["synthetic_n_targets"] = synth_info["n_targets"]

    outputs = [
        {"path": det_path, "kind": "vector", "crs_epsg": 4326, "bbox_wgs84": bbox},
        {"path": score_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] detections: {len(boxes)}  feature: {args.feature}")
        print(f"[{SKILL_NAME}] valid pixels: {qa['n_valid_pixels']}/{qa['n_total_pixels']}")
        print(f"[{SKILL_NAME}] geojson: {det_path}")
        print(f"[{SKILL_NAME}] score map: {score_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Remote-sensing object detection (sliding window + NMS, offline numpy equivalent).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF (first band used as intensity)")
    p.add_argument("--feature", default="intensity", choices=["intensity", "hog"],
                   help="window scoring feature (default: intensity)")
    p.add_argument("--win-size", type=int, default=16, help="sliding window size in pixels")
    p.add_argument("--step", type=int, default=8, help="sliding step in pixels")
    p.add_argument("--score-thresh", type=float, default=1.5, help="min window score to be a candidate")
    p.add_argument("--iou-thresh", type=float, default=0.5, help="NMS IoU threshold")
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
