#!/usr/bin/env python3
"""instance-segmentation — 实例分割

在遥感影像上把每个独立目标（建筑、地块、树冠、池塘等）分割为**独立实例**，
并为每个实例提取属性（面积、质心、边界框、平均亮度），输出实例标注 GeoJSON。

本 skill 是 Mask R-CNN 等实例分割网络的**离线 numpy 等价实现**：
不依赖 torch/tensorflow，而用可验证的经典流程复现"实例分割"的核心逻辑——

1. **前景分离**：对强度影像做阈值分割（全局阈值或 Otsu 自动阈值）；
2. **连通域标记**：用 scipy.ndimage.label 做 4/8 邻接连通域标记，
   每个连通域就是一个实例（等价于网络输出的逐实例掩膜）；
3. **实例属性提取**：用 regionprops 思路逐实例计算面积、质心、bbox、均值亮度；
4. **地理编码**：把每个实例的像素 bbox 转成 WGS-84 地理框，写 GeoJSON。

数据源：本地单/多波段 GeoTIFF（取首波段），或 ``--synthetic`` 生成含若干
分离明亮斑块的模拟影像。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python instance-segmentation.py --input scene.tif --output-dir ./out
    python instance-segmentation.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "instance-segmentation"

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
# Input validation (P0/P1)
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate a [W, S, E, N] bbox. Raises ValidationError on bad order, range,
    zero-area, or crossing the 180° meridian.
    """
    try:
        w, s, e, n = [float(v) for v in bbox]
    except Exception:
        raise ValidationError(f"bbox must be 4 floats, got {bbox!r}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"longitude out of range [-180, 180]: W={w}, E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"latitude out of range [-90, 90]: S={s}, N={n}")
    if w >= e:
        raise ValidationError(
            f"bbox requires W < E (got W={w}, E={e}); check --bbox order")
    if s >= n:
        raise ValidationError(
            f"bbox requires S < N (got S={s}, N={n}); check --bbox order")
    if e - w > 360.0 or n - s > 180.0:
        raise ValidationError(
            f"bbox span too large (dx={e - w}, dy={n - s})")
    if w > 180.0 or e > 180.0 or w < -180.0 or e < -180.0:
        raise ValidationError(
            f"bbox crosses 180° meridian; please split into two sub-bboxes")


def validate_cli_params(min_area: int, threshold) -> None:
    """Validate CLI parameter ranges. Raises ValidationError on bad input."""
    if int(min_area) < 1:
        raise ValidationError(
            f"--min-area must be >= 1, got {min_area}")
    if threshold is not None and not (0.0 <= float(threshold) <= 1.0):
        # Allow absolute thresholds (intensity) too — but reject negative.
        try:
            tv = float(threshold)
        except Exception:
            raise ValidationError(f"--threshold must be a number, got {threshold!r}")
        if tv < 0.0:
            raise ValidationError(
                f"--threshold must be non-negative, got {threshold}")


def read_geotiff_with_nodata(path: str):
    """Read a raster and return (data, bbox, nodata).

    Values equal to the source nodata (if any) are replaced with NaN.
    For 3D multiband input, only the first band is used downstream — we
    still replace NoData across all bands for the validity check.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [float(b.left), float(b.bottom), float(b.right), float(b.top)]
        nd = src.nodata
    if nd is not None:
        cube = np.where(cube == nd, np.nan, cube)
    return cube, bbox, nd


def count_valid_pixels(image: np.ndarray) -> int:
    """Number of locations that are finite (not NaN / inf)."""
    return int(np.isfinite(image).sum())


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def otsu_threshold(values: np.ndarray, n_bins: int = 256) -> float:
    """Otsu 自动阈值：最大化类间方差，把像元分成前景/背景两类。"""
    v = np.asarray(values, dtype=np.float64)
    v = v[np.isfinite(v)]
    if v.size == 0:
        return 0.0
    hist, edges = np.histogram(v, bins=n_bins)
    centers = 0.5 * (edges[:-1] + edges[1:])
    hist = hist.astype(np.float64)
    total = hist.sum()
    if total <= 0:
        return float(v.mean())
    weight_bg = np.cumsum(hist)
    weight_fg = total - weight_bg
    mean_bg_sum = np.cumsum(hist * centers)
    mean_bg = np.divide(mean_bg_sum, weight_bg, out=np.zeros_like(mean_bg_sum),
                        where=weight_bg > 0)
    mean_fg = np.divide(mean_bg_sum[-1] - mean_bg_sum, weight_fg,
                        out=np.zeros_like(weight_fg), where=weight_fg > 0)
    between = weight_bg * weight_fg * (mean_bg - mean_fg) ** 2
    # 双峰之间类间方差常为平台（gap 内无样本），取平台中点作为阈值更稳健
    peak = float(np.max(between))
    peak_idx = np.where(between >= peak - 1e-9)[0]
    idx = int(peak_idx[len(peak_idx) // 2])
    return float(centers[idx])


def threshold_segment(image: np.ndarray, thresh: Optional[float] = None) -> np.ndarray:
    """阈值分割成二值前景掩膜 (bool)。thresh=None 时用 Otsu 自动阈值。

    NaN locations are kept as False in the output mask (they are not foreground).
    """
    img = np.asarray(image, dtype=np.float64)
    if img.ndim != 2:
        raise ValidationError("threshold_segment expects a 2D image", shape=list(img.shape))
    if thresh is None:
        thresh = otsu_threshold(img)
    finite = np.isfinite(img)
    mask = (img > thresh) & finite
    return mask


def label_instances(mask: np.ndarray, connectivity: int = 8) -> Tuple[np.ndarray, int]:
    """连通域标记。返回 (label_map[H, W], n_instances)。

    connectivity=4 用十字结构元，8 用方形结构元。
    """
    from scipy.ndimage import label
    mask = np.asarray(mask).astype(bool)
    if connectivity == 4:
        struct = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=bool)
    elif connectivity == 8:
        struct = np.ones((3, 3), dtype=bool)
    else:
        raise UsageError("connectivity must be 4 or 8", connectivity=int(connectivity))
    labels, n = label(mask, structure=struct)
    return labels.astype(np.int32), int(n)


def instance_properties(
    label_map: np.ndarray,
    image: np.ndarray,
    min_area: int = 1,
) -> List[Dict[str, Any]]:
    """逐实例提取属性：面积、质心 (row, col)、像素 bbox、平均亮度。"""
    label_map = np.asarray(label_map, dtype=np.int32)
    image = np.asarray(image, dtype=np.float64)
    ids = [i for i in np.unique(label_map) if i != 0]
    props: List[Dict[str, Any]] = []
    for lab in ids:
        ys, xs = np.where(label_map == lab)
        area = int(ys.size)
        if area < min_area:
            continue
        props.append({
            "instance_id": int(lab),
            "area_px": area,
            "centroid_row": float(np.mean(ys)),
            "centroid_col": float(np.mean(xs)),
            "bbox_px": [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1],
            "mean_intensity": float(np.mean(image[ys, xs])),
        })
    props.sort(key=lambda d: d["area_px"], reverse=True)
    return props


def pixel_box_to_geo(box: List[float], bbox: List[float], img_w: int, img_h: int) -> List[float]:
    w, s, e, n = bbox
    x1, y1, x2, y2 = [float(v) for v in box]
    lon1 = w + (x1 / img_w) * (e - w)
    lon2 = w + (x2 / img_w) * (e - w)
    lat1 = n - (y1 / img_h) * (n - s)
    lat2 = n - (y2 / img_h) * (n - s)
    return [min(lon1, lon2), min(lat1, lat2), max(lon1, lon2), max(lat1, lat2)]


def instances_to_geojson(
    props: List[Dict[str, Any]], bbox: List[float], img_w: int, img_h: int
) -> Dict[str, Any]:
    """把实例属性打包成 GeoJSON FeatureCollection（bbox 多边形 + 属性）。"""
    features: List[Dict[str, Any]] = []
    for idx, p in enumerate(props):
        gminx, gminy, gmaxx, gmaxy = pixel_box_to_geo(p["bbox_px"], bbox, img_w, img_h)
        ring = [[gminx, gminy], [gmaxx, gminy], [gmaxx, gmaxy],
                [gminx, gmaxy], [gminx, gminy]]
        features.append({
            "type": "Feature",
            "id": int(idx),
            "properties": {
                "instance_id": p["instance_id"],
                "area_px": p["area_px"],
                "mean_intensity": round(p["mean_intensity"], 4),
                "centroid_col": round(p["centroid_col"], 3),
                "centroid_row": round(p["centroid_row"], 3),
            },
            "geometry": {"type": "Polygon", "coordinates": [ring]},
        })
    return {"type": "FeatureCollection", "features": features}


def segment_instances(
    image: np.ndarray,
    thresh: Optional[float] = None,
    connectivity: int = 8,
    min_area: int = 1,
) -> Tuple[np.ndarray, List[Dict[str, Any]], Dict[str, Any]]:
    """完整实例分割流程：阈值 -> 连通域 -> 属性。

    返回 (label_map[H, W], props, info)。
    """
    mask = threshold_segment(image, thresh)
    label_map, n_raw = label_instances(mask, connectivity)
    props = instance_properties(label_map, image, min_area=min_area)
    # 过滤小实例后重新编号 label_map（保留的实例 1..K）
    filtered = np.zeros_like(label_map)
    for new_id, p in enumerate(props, start=1):
        filtered[label_map == p["instance_id"]] = new_id
        p["instance_id"] = new_id
    info = {
        "n_raw_components": int(n_raw),
        "n_instances": int(len(props)),
        "threshold": float(thresh) if thresh is not None else "otsu",
        "connectivity": int(connectivity),
        "min_area": int(min_area),
    }
    return filtered, props, info


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    n_blobs: int = 5,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成暗背景 + 若干分离明亮方形/圆形斑块（每个是一个实例）。"""
    rng = np.random.default_rng(seed)
    img = rng.normal(15.0, 2.0, size=(height, width)).astype(np.float32)
    truth_centers: List[List[int]] = []
    # 均匀网格放置斑块，保证互相分离
    cols = int(np.ceil(np.sqrt(n_blobs)))
    rows = int(np.ceil(n_blobs / cols))
    cell_w = width // cols
    cell_h = height // rows
    r = max(3, min(cell_w, cell_h) // 4)
    placed = 0
    for ri in range(rows):
        for ci in range(cols):
            if placed >= n_blobs:
                break
            cy = ri * cell_h + cell_h // 2
            cx = ci * cell_w + cell_w // 2
            yy, xx = np.mgrid[0:height, 0:width]
            disk = ((yy - cy) ** 2 + (xx - cx) ** 2) <= r * r
            img[disk] += 100.0
            truth_centers.append([int(cy), int(cx)])
            placed += 1
    info = {"bbox": bbox, "width": width, "height": height,
            "n_blobs": n_blobs, "truth_centers": truth_centers}
    return img, info


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
            "connectivity": getattr(args, "connectivity", None),
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
    src_nd = None

    if args.input and not args.synthetic:
        cube, file_bbox, _src_nd = read_geotiff_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        image = cube[0] if cube.ndim == 3 else cube
        source_note = args.input
        src_nd = _src_nd
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        image, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    # Parameter validation (BEFORE side-effect makedirs).
    if bbox is not None:
        validate_bbox(bbox)
    validate_cli_params(args.min_area, args.threshold)

    if image.size == 0:
        raise ValidationError("input raster is empty")

    # Reject all-NoData input.
    n_valid = count_valid_pixels(image)
    if n_valid == 0:
        raise ValidationError(
            "input raster has no valid pixels (all NoData / NaN); cannot segment")

    label_map, props, info = segment_instances(
        image, thresh=args.threshold, connectivity=args.connectivity,
        min_area=args.min_area,
    )
    h, w = image.shape
    geojson = instances_to_geojson(props, bbox, w, h)

    # Side effects begin only after all validation passes.
    os.makedirs(output_dir, exist_ok=True)

    inst_path = os.path.join(output_dir, "instances.geojson")
    with open(inst_path, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    label_tif = os.path.join(output_dir, "instance_labels.tif")
    # NaN locations in the input → label=0 in the raster
    write_geotiff(label_tif, label_map.astype(np.float32), bbox)

    n_total = int(image.size)
    qa: Dict[str, Any] = {
        "source": source_note,
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
        "input_nodata": src_nd,
        "n_instances": int(len(props)),
        "n_raw_components": info["n_raw_components"],
        "threshold": info["threshold"],
        "mean_area_px": float(np.mean([p["area_px"] for p in props])) if props else 0.0,
    }
    if synth_info is not None:
        qa["synthetic_n_blobs"] = synth_info["n_blobs"]

    outputs = [
        {"path": inst_path, "kind": "vector", "crs_epsg": 4326, "bbox_wgs84": bbox},
        {"path": label_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] instances: {len(props)} (raw {info['n_raw_components']})")
        print(f"[{SKILL_NAME}] geojson: {inst_path}")
        print(f"[{SKILL_NAME}] labels: {label_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Instance segmentation (threshold + connected components + region props).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF (first band used)")
    p.add_argument("--threshold", type=float, default=None,
                   help="foreground threshold (default: Otsu auto)")
    p.add_argument("--connectivity", type=int, default=8, choices=[4, 8],
                   help="connected-component connectivity (default: 8)")
    p.add_argument("--min-area", type=int, default=1, help="drop instances smaller than this (px)")
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
