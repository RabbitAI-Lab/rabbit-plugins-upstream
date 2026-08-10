#!/usr/bin/env python3
"""sar-ship-detection — SAR船舶检测

在单极化 SAR 强度影像上检测海上船舶目标。核心流程：

1. **CFAR 恒虚警检测**：在滑动窗口内，用保护带（guard）之外的背景单元估计局部
   杂波功率，自适应设定检测门限，从而在不同海况下保持恒定虚警率。
   - **CA-CFAR**（单元平均）：门限 = α·μ_bg，α = N·(Pfa^(−1/N) − 1)，
     源于指数分布杂波下虚警率 Pfa 与门限倍数的解析关系；N 为背景单元数。
   - **OS-CFAR**（有序统计）：对背景单元排序，取第 k 个次序统计量作为杂波估计，
     对多目标/杂波边缘更稳健。
2. **形态学聚类**：对超门限像元做连通域标记（scipy.ndimage.label），
   提取每个目标的面积、质心、峰值强度与外接框。

数据源：本地单波段 SAR 强度 GeoTIFF，或 ``--synthetic`` 生成的模拟海面场景
（低 σ⁰ 平滑海面背景 + 指数分布散斑 + 若干高亮船舶点目标）。

隐私声明 / Privacy：
- 默认离线运行，仅在显式解析地名时才访问网络。
- ``--synthetic`` 模式完全无网络。所有处理在本地完成，不上传任何用户数据。

Usage:
    python sar-ship-detection.py --bbox 121 30 122 31 --synthetic --cfar ca --pfa 1e-4
    python sar-ship-detection.py --input sar.tif --cfar os --output-dir ./out

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
SKILL_NAME = "sar-ship-detection"

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
# 核心算法 1：CFAR 门限
# ---------------------------------------------------------------------------
def ca_cfar_alpha(pfa: float, n_background: int) -> float:
    """CA-CFAR 门限倍数：α = N·(Pfa^(−1/N) − 1)。

    指数分布杂波下，单元平均估计的虚警率与门限倍数满足
    Pfa = (1 + α/N)^(−N)，反解即得上式。
    """
    if not 0.0 < pfa < 1.0:
        raise ValidationError(f"pfa must be in (0,1), got {pfa}")
    if n_background < 1:
        raise ValidationError(f"n_background must be >=1, got {n_background}")
    return float(n_background * (pfa ** (-1.0 / n_background) - 1.0))


def _window_sums(image: np.ndarray, size: int) -> np.ndarray:
    """返回每个像元 size×size 窗口内的和（内部像元精确；边界用反射填充）。"""
    from scipy.ndimage import uniform_filter
    mean = uniform_filter(image.astype(np.float64), size=size, mode="reflect")
    return mean * (size * size)


def cfar_detect(
    image: np.ndarray,
    guard: int = 2,
    background: int = 5,
    pfa: float = 1e-4,
    method: str = "ca",
    os_rank: Optional[float] = None,
) -> Dict[str, np.ndarray]:
    """对 2D 强度影像执行 CFAR 检测。

    返回 dict：detections (bool)、threshold、noise_estimate（均与 image 同形）。
    边界 margin=guard+background 内的像元不参与检测。
    """
    if guard < 0 or background < 1:
        raise ValidationError(f"need guard>=0 and background>=1, got {guard},{background}")
    if method not in ("ca", "os"):
        raise UsageError(f"unknown cfar method '{method}'")
    h, w = image.shape
    margin = guard + background
    if h <= 2 * margin + 1 or w <= 2 * margin + 1:
        raise ValidationError(
            f"image {h}x{w} too small for guard={guard} background={background}",
        )

    img = image.astype(np.float64)
    outer_size = 2 * margin + 1
    guard_size = 2 * guard + 1
    n_background = outer_size * outer_size - guard_size * guard_size

    detections = np.zeros((h, w), dtype=bool)
    threshold = np.zeros((h, w), dtype=np.float64)
    noise = np.zeros((h, w), dtype=np.float64)

    iy0, iy1 = margin, h - margin
    ix0, ix1 = margin, w - margin

    if method == "ca":
        alpha = ca_cfar_alpha(pfa, n_background)
        outer_sum = _window_sums(img, outer_size)
        guard_sum = _window_sums(img, guard_size)
        bg_mean = (outer_sum - guard_sum) / n_background
        thr = alpha * bg_mean
        noise[iy0:iy1, ix0:ix1] = bg_mean[iy0:iy1, ix0:ix1]
        threshold[iy0:iy1, ix0:ix1] = thr[iy0:iy1, ix0:ix1]
        detections[iy0:iy1, ix0:ix1] = img[iy0:iy1, ix0:ix1] > thr[iy0:iy1, ix0:ix1]
    else:  # os
        from numpy.lib.stride_tricks import sliding_window_view
        rank = os_rank if os_rank is not None else 0.75
        if not 0.0 < rank < 1.0:
            raise ValidationError(f"os_rank must be in (0,1), got {rank}")
        # OS 门限倍数：用指数分布次序统计量的期望近似放大
        k = max(1, int(round(rank * n_background)))
        pad = margin
        padded = np.pad(img, pad, mode="reflect")
        windows = sliding_window_view(padded, (outer_size, outer_size))  # (h, w, os, os)
        # 构造背景掩膜（外窗内、保护带外）
        yy, xx = np.mgrid[0:outer_size, 0:outer_size]
        cy = cx = margin
        bg_mask = ~((np.abs(yy - cy) <= guard) & (np.abs(xx - cx) <= guard))
        bg_cells = windows[:, :, bg_mask]  # (h, w, n_background)
        bg_sorted = np.sort(bg_cells, axis=-1)
        os_val = bg_sorted[..., k - 1]
        # 指数分布第 k 次序统计量期望 ≈ μ·Σ_{i=N-k+1}^{N} 1/i；据此归一到 μ 再乘 α
        harmonic = float(np.sum(1.0 / np.arange(n_background - k + 1, n_background + 1)))
        mu_est = os_val / max(harmonic, 1e-9)
        alpha = ca_cfar_alpha(pfa, n_background)
        thr = alpha * mu_est
        noise[iy0:iy1, ix0:ix1] = mu_est[iy0:iy1, ix0:ix1]
        threshold[iy0:iy1, ix0:ix1] = thr[iy0:iy1, ix0:ix1]
        detections[iy0:iy1, ix0:ix1] = img[iy0:iy1, ix0:ix1] > thr[iy0:iy1, ix0:ix1]

    return {"detections": detections, "threshold": threshold, "noise_estimate": noise}


# ---------------------------------------------------------------------------
# 核心算法 2：连通域聚类与属性提取
# ---------------------------------------------------------------------------
def cluster_detections(
    detections: np.ndarray, image: np.ndarray, min_area: int = 1,
) -> List[Dict[str, Any]]:
    """对检测掩膜做连通域标记，提取每个目标的属性（像素坐标）。

    返回按峰值强度降序的属性列表：area_px、centroid (row,col)、peak、bbox。
    """
    from scipy.ndimage import label
    if detections.ndim != 2:
        raise ValidationError(f"detections must be 2D, got {detections.shape}")
    lbl, n = label(detections.astype(np.uint8))
    targets: List[Dict[str, Any]] = []
    if n == 0:
        return targets
    for i in range(1, n + 1):
        ys, xs = np.where(lbl == i)
        area = int(ys.size)
        if area < min_area:
            continue
        peak_idx = int(np.argmax(image[ys, xs]))
        targets.append({
            "id": int(i),
            "area_px": area,
            "centroid_row": float(ys.mean()),
            "centroid_col": float(xs.mean()),
            "peak_row": int(ys[peak_idx]),
            "peak_col": int(xs[peak_idx]),
            "peak_intensity": float(image[ys[peak_idx], xs[peak_idx]]),
            "bbox_px": [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())],
        })
    targets.sort(key=lambda t: t["peak_intensity"], reverse=True)
    for rank, t in enumerate(targets):
        t["rank"] = rank
    return targets


def pixel_to_lonlat(row: int, col: int, bbox: List[float], h: int, w: int) -> Tuple[float, float]:
    """像素 (row,col) → (lon, lat)。bbox=[W,S,E,N]，row 从北向南增大。"""
    lon = bbox[0] + (col + 0.5) / w * (bbox[2] - bbox[0])
    lat = bbox[3] - (row + 0.5) / h * (bbox[3] - bbox[1])
    return lon, lat


def targets_to_geodataframe(targets, bbox, h, w):
    """把目标属性转成 GeoDataFrame：点几何（质心）+ 外接框 Polygon。"""
    import geopandas as gpd
    from shapely.geometry import Point, Polygon

    rows = []
    geoms = []
    for t in targets:
        lon, lat = pixel_to_lonlat(t["centroid_row"], t["centroid_col"], bbox, h, w)
        x0, y0, x1, y1 = t["bbox_px"]
        lon0, lat_top = pixel_to_lonlat(y0, x0, bbox, h, w)
        lon1, lat_bot = pixel_to_lonlat(y1, x1, bbox, h, w)
        bx0, bx1 = sorted((lon0, lon1))
        by0, by1 = sorted((lat_bot, lat_top))
        rows.append({
            "id": t["id"], "rank": t["rank"], "area_px": t["area_px"],
            "peak_intensity": t["peak_intensity"],
            "centroid_lon": lon, "centroid_lat": lat,
            "bbox": [bx0, by0, bx1, by1],
        })
        geoms.append(Point(lon, lat))
    gdf = gpd.GeoDataFrame(rows, geometry=geoms, crs="EPSG:4326")
    return gdf


# ---------------------------------------------------------------------------
# 合成数据：海面背景 + 船舶点目标
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 96,
    height: int = 96,
    n_ships: int = 6,
    clutter_sigma0: float = 0.0025,
    ship_contrast: float = 60.0,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (H, W) SAR 强度场景：指数分布海面散斑 + 若干高亮船舶。

    返回 (image, info)，info 含注入船舶的像素位置真值。
    """
    rng = np.random.default_rng(seed)
    # 海面杂波：指数分布（SAR 强度散斑的经典模型），均值 = clutter_sigma0
    sea = rng.exponential(scale=clutter_sigma0, size=(height, width)).astype(np.float64)
    # 轻微空间平滑，模拟相关杂波
    from scipy.ndimage import gaussian_filter
    sea = gaussian_filter(sea, sigma=0.6)

    margin = 14
    ys = rng.integers(margin, height - margin, size=n_ships)
    xs = rng.integers(margin, width - margin, size=n_ships)
    # 保证船舶彼此分离，避免连通域合并
    ships: List[Tuple[int, int, float]] = []
    for y, x in zip(ys, xs):
        too_close = any(abs(y - sy) < 8 and abs(x - sx) < 8 for sy, sx, _ in ships)
        if too_close:
            continue
        amp = clutter_sigma0 * ship_contrast * rng.uniform(0.8, 1.3)
        ships.append((int(y), int(x), float(amp)))

    image = sea.copy()
    for y, x, amp in ships:
        image[y, x] += amp
        image[y - 1, x] += amp * 0.4
        image[y + 1, x] += amp * 0.4
        image[y, x - 1] += amp * 0.4
        image[y, x + 1] += amp * 0.4

    truth = [{"row": y, "col": x, "amp": a} for y, x, a in ships]
    info = {
        "bbox": bbox, "width": width, "height": height,
        "n_ships_injected": len(ships), "ships_truth_px": truth,
        "clutter_sigma0": clutter_sigma0, "ship_contrast": ship_contrast,
    }
    return image.astype(np.float32), info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, array: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if array.ndim == 2:
        array = array[np.newaxis, ...]
    nb, h, w = array.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(array[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        arr = src.read(1).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return arr, bbox


def read_geotiff_full(path: str) -> Tuple[np.ndarray, List[float], float]:
    """Read single-band GeoTIFF, replace nodata with NaN, validate n_valid_pixels.

    Returns (array_with_nan, bbox, nodata). Raises ValidationError if all pixels are
    NoData. nodata may be None if file has no nodata tag.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        arr = src.read(1).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None and np.isfinite(nodata):
        arr = np.where(arr == nodata, np.nan, arr)
    n_valid = int(np.sum(np.isfinite(arr)))
    if n_valid == 0:
        raise ValidationError(
            f"input raster has no valid pixels (all {arr.size} are NoData={nodata})"
        )
    return arr, bbox, nodata


def validate_bbox(bbox: List[float]) -> None:
    """Validate bbox = [W, S, E, N]. Raise ValidationError on W>=E, S>=N, out-of-range,
    or cross-180° antipodal bbox."""
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise ValidationError(f"bbox must be 4 floats [W S E N], got {bbox}")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"longitude out of range [-180,180]: W={w}, E={e}"
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"latitude out of range [-90,90]: S={s}, N={n}"
        )
    if w >= e:
        if abs(e - (-180.0)) < 1e-9 and w > 0:
            raise ValidationError(
                f"cross-180° bbox not supported (W={w}, E={e}); "
                f"split into two non-antipodal bboxes"
            )
        raise ValidationError(f"W must be < E, got W={w}, E={e}")
    if s >= n:
        raise ValidationError(f"S must be < N, got S={s}, N={n}")
    if (e - w) < 0.001 or (n - s) < 0.001:
        raise ValidationError(
            f"bbox too small (<0.001°), got W={w},S={s},E={e},N={n}"
        )


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
            "cfar": getattr(args, "cfar", None),
            "pfa": getattr(args, "pfa", None),
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
    input_nodata: Optional[float] = None
    n_valid_pixels: Optional[int] = None

    if args.input and not args.synthetic:
        # Validate bbox first (if user passed --bbox)
        if bbox is not None:
            validate_bbox(bbox)
        image, file_bbox, input_nodata = read_geotiff_full(args.input)
        bbox = bbox if bbox is not None else file_bbox
        n_valid_pixels = int(np.sum(np.isfinite(image)))
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        image, synth_info = generate_synthetic(bbox)
        n_valid_pixels = int(image.size)
        source_note = "synthetic"

    if image.size == 0:
        raise ValidationError("input raster is empty")

    # Now safe to create output dir
    os.makedirs(output_dir, exist_ok=True)

    # 检测
    res = cfar_detect(image, guard=args.guard, background=args.background,
                      pfa=args.pfa, method=args.cfar)
    detections = res["detections"]
    targets = cluster_detections(detections, image, min_area=args.min_area)
    h, w = image.shape

    # 矢量产物
    gdf = targets_to_geodataframe(targets, bbox, h, w)
    geojson_path = os.path.join(output_dir, "ships.geojson")
    gdf.to_file(geojson_path, driver="GeoJSON")

    # 检测掩膜栅格
    mask_path = os.path.join(output_dir, "detection_mask.tif")
    write_geotiff(mask_path, detections.astype(np.float32), bbox)

    # 属性表 + 计数
    attrs_path = os.path.join(output_dir, "ship_attributes.json")
    with open(attrs_path, "w", encoding="utf-8") as f:
        json.dump({"n_detected": len(targets), "targets": targets}, f,
                  ensure_ascii=False, indent=2)

    count = {
        "n_detected": len(targets),
        "cfar_method": args.cfar,
        "pfa": args.pfa,
        "guard": args.guard,
        "background": args.background,
        "n_background_cells": (2 * (args.guard + args.background) + 1) ** 2
        - (2 * args.guard + 1) ** 2,
    }
    if synth_info is not None:
        count["n_ships_injected"] = synth_info["n_ships_injected"]
    count_path = os.path.join(output_dir, "detection_count.json")
    with open(count_path, "w", encoding="utf-8") as f:
        json.dump(count, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note, "cfar": args.cfar, "pfa": args.pfa,
        "n_detected": len(targets),
        "detection_rate_px": float(detections.mean()),
        "n_valid_pixels": n_valid_pixels,
        "input_nodata": input_nodata,
    }
    if synth_info is not None:
        qa["n_ships_injected"] = synth_info["n_ships_injected"]
        qa["detection_vs_truth"] = (
            f"{len(targets)}/{synth_info['n_ships_injected']}"
        )

    outputs = [
        {"path": geojson_path, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": len(targets)},
        {"path": mask_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": attrs_path, "kind": "json"},
        {"path": count_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] CFAR: {args.cfar}  pfa={args.pfa}  "
              f"guard={args.guard}  background={args.background}")
        print(f"[{SKILL_NAME}] ships detected: {len(targets)}")
        print(f"[{SKILL_NAME}] vector: {geojson_path}")
        print(f"[{SKILL_NAME}] mask:   {mask_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="SAR ship detection with CA/OS-CFAR and connected-component clustering.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input single-band SAR intensity GeoTIFF")
    p.add_argument("--cfar", default="ca", choices=["ca", "os"],
                   help="CFAR detector (default: ca)")
    p.add_argument("--pfa", type=float, default=1e-4,
                   help="probability of false alarm (default: 1e-4)")
    p.add_argument("--guard", type=int, default=2,
                   help="guard window half-size in pixels (default: 2)")
    p.add_argument("--background", type=int, default=5,
                   help="background window half-size in pixels (default: 5)")
    p.add_argument("--min-area", type=int, default=1,
                   help="minimum cluster area in pixels (default: 1)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic sea-surface scene with ships (offline)")
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
