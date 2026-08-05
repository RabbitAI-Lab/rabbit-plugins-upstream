#!/usr/bin/env python3
"""edge-detection-lineament — 边缘检测与线性构造提取

对栅格影像执行边缘检测，并可选地用概率 Hough 变换提取线性构造
（lineament），用于地质构造解译、断裂带识别、海岸线/道路提取。

算法：
- **Canny**：多尺度（高斯平滑 + 梯度 + 非极大值抑制 + 双阈值滞后跟踪），
  ``skimage.feature.canny``；
- **Sobel**：Sobel 梯度幅值 + 单阈值二值化，``scipy.ndimage.sobel``；
- **概率 Hough 变换**（``skimage.transform.probabilistic_hough_line``）
  从边缘图中提取线段，再把像元坐标转换为地理坐标输出 GeoJSON。

输出：边缘栅格 GeoTIFF（二值 0/1）+ 线性构造 GeoJSON（LineString 线段集合）。

数据源：本地 GeoTIFF（默认用第 1 波段），或使用 ``--synthetic`` 生成
含线性边缘（断层/道路）的模拟影像用于离线验证。

隐私声明 / Privacy：
- 默认离线运行，仅在显式 ``--place`` 解析地名时才会访问 Nominatim/Open-Meteo。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python edge-detection-lineament.py --input scene.tif --method canny --threshold 0.1
    python edge-detection-lineament.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "edge-detection-lineament"

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
# 校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate geographic bbox. raise ValidationError on any structural issue."""
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            "bbox must be 4 floats [W, S, E, N]", bbox=str(bbox))
    w, s, e, n = [float(v) for v in bbox]
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError("bbox has non-finite values", bbox=bbox)
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0
            and -90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            "bbox out of WGS84 range (lon∈[-180,180], lat∈[-90,90])",
            bbox=bbox)
    if w >= e:
        raise ValidationError(
            f"bbox west ({w}) must be < east ({e}); "
            "this skill does not support anti-meridian crossing — split into two calls",
            bbox=bbox)
    if s >= n:
        raise ValidationError(
            f"bbox south ({s}) must be < north ({n})", bbox=bbox)
    span_lon = e - w
    span_lat = n - s
    if span_lon < 1e-5 or span_lat < 1e-5:
        raise ValidationError(
            f"bbox too small (lon span={span_lon:.7f}, lat span={span_lat:.7f}); "
            "both dimensions must be > 1e-5°", bbox=bbox)


def validate_method_params(method: str, threshold: float, min_length: int,
                           line_gap: int, hough_threshold: int) -> None:
    """Validate method-specific CLI parameters (CLI errors → UsageError rc=2)."""
    if method not in ("canny", "sobel"):
        raise UsageError(f"unknown method '{method}'; choose canny|sobel",
                         method=method)
    if not (0.0 < float(threshold) < 1.0):
        raise UsageError(
            f"--threshold must be in (0, 1); got {threshold}",
            threshold=threshold)
    if int(min_length) < 2:
        raise UsageError(
            f"--min-length must be >= 2 pixels; got {min_length}",
            min_length=min_length)
    if int(line_gap) < 0:
        raise UsageError(
            f"--line-gap must be >= 0; got {line_gap}", line_gap=line_gap)
    if int(hough_threshold) < 1:
        raise UsageError(
            f"--hough-threshold must be >= 1; got {hough_threshold}",
            hough_threshold=hough_threshold)


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def normalize01(band: np.ndarray) -> np.ndarray:
    """把波段线性归一化到 [0, 1]（NaN 置 0）。"""
    valid = band[np.isfinite(band)]
    if valid.size == 0:
        return np.zeros(band.shape, dtype=np.float64)
    bmin, bmax = float(valid.min()), float(valid.max())
    if bmax - bmin < 1e-12:
        return np.zeros(band.shape, dtype=np.float64)
    out = (band - bmin) / (bmax - bmin)
    return np.nan_to_num(out, nan=0.0).astype(np.float64)


def detect_edges(
    band: np.ndarray,
    method: str = "canny",
    threshold: float = 0.1,
    sigma: float = 1.0,
) -> np.ndarray:
    """边缘检测，返回二值边缘栅格 (H, W) float32（1=边缘，0=非边缘）。

    method:
      - "canny": skimage.feature.canny，threshold 作为低阈值，高阈值=2×低阈值；
      - "sobel": scipy.ndimage.sobel 梯度幅值归一化后阈值化。
    """
    img = normalize01(band)

    if method == "canny":
        from skimage.feature import canny
        low = float(np.clip(threshold, 1e-3, 0.9))
        high = float(np.clip(low * 2.0, low, 1.0))
        edges = canny(img, sigma=sigma, low_threshold=low, high_threshold=high)
        return edges.astype(np.float32)

    if method == "sobel":
        from scipy.ndimage import sobel
        gx = sobel(img, axis=1)
        gy = sobel(img, axis=0)
        mag = np.hypot(gx, gy)
        mmax = float(mag.max())
        if mmax < 1e-12:
            return np.zeros(img.shape, dtype=np.float32)
        mag = mag / mmax
        edges = mag >= float(np.clip(threshold, 0.0, 1.0))
        return edges.astype(np.float32)

    raise UsageError(f"unknown method '{method}'. Choose canny or sobel",
                     method=method)


def extract_lineaments(
    edge_mask: np.ndarray,
    min_length: int = 15,
    line_gap: int = 5,
    threshold: int = 10,
) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """概率 Hough 变换提取线段（像元坐标）。

    返回 [((x0, y0), (x1, y1)), ...]，坐标为 (col, row)。
    """
    from skimage.transform import probabilistic_hough_line

    mask = (edge_mask > 0).astype(np.uint8)
    if mask.sum() == 0:
        return []
    lines = probabilistic_hough_line(
        mask, threshold=threshold,
        line_length=min_length, line_gap=line_gap,
    )
    return [((int(p0[0]), int(p0[1])), (int(p1[0]), int(p1[1])))
            for p0, p1 in lines]


def pixel_to_geo(
    px: int, py: int, width: int, height: int, bbox: List[float],
) -> Tuple[float, float]:
    """像元 (col, row) 中心 → 地理坐标 (lon, lat)。bbox = [W, S, E, N]。"""
    lon = bbox[0] + (px + 0.5) / width * (bbox[2] - bbox[0])
    lat = bbox[3] - (py + 0.5) / height * (bbox[3] - bbox[1])
    return lon, lat


def build_lineaments_gdf(
    lines: List[Tuple[Tuple[int, int], Tuple[int, int]]],
    width: int, height: int, bbox: List[float],
):
    """把像元线段转为 geopandas GeoDataFrame（WGS84 / shapely LineString）。"""
    import geopandas as gpd
    from shapely.geometry import LineString

    records, geoms = [], []
    for idx, (p0, p1) in enumerate(lines):
        lon0, lat0 = pixel_to_geo(p0[0], p0[1], width, height, bbox)
        lon1, lat1 = pixel_to_geo(p1[0], p1[1], width, height, bbox)
        geoms.append(LineString([(lon0, lat0), (lon1, lat1)]))
        records.append({
            "id": idx,
            "length_px": round(float(np.hypot(p1[0] - p0[0], p1[1] - p0[1])), 3),
            "x0": p0[0], "y0": p0[1], "x1": p1[0], "y1": p1[1],
        })
    if records:
        gdf = gpd.GeoDataFrame(records, geometry=geoms, crs="EPSG:4326")
    else:
        gdf = gpd.GeoDataFrame(
            {"id": [], "length_px": [], "x0": [], "y0": [], "x1": [], "y1": []},
            geometry=[], crs="EPSG:4326",
        )
    return gdf


def write_lineaments_geojson(path: str, gdf) -> int:
    """把 GeoDataFrame 写成 GeoJSON，返回要素数量。"""
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    gdf.to_file(path, driver="GeoJSON")
    return int(len(gdf))


def edge_stats(edge_mask: np.ndarray) -> Dict[str, Any]:
    n_edge = int((edge_mask > 0).sum())
    n_total = int(edge_mask.size)
    return {
        "n_edge_pixels": n_edge,
        "n_total_pixels": n_total,
        "edge_density": float(n_edge / n_total) if n_total else 0.0,
    }


# ---------------------------------------------------------------------------
# 合成数据：含线性边缘（断层/道路）的影像（离线验证）
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float],
    width: int = 96,
    height: int = 96,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (1, H, W) 影像：背景渐变 + 若干条线性亮边（模拟断层/道路）。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xxn = xx.astype(np.float64) / max(width - 1, 1)
    yyn = yy.astype(np.float64) / max(height - 1, 1)

    img = 0.2 + 0.2 * xxn + rng.normal(0, 0.02, (height, width))

    # 几条直线（对角 + 水平），用高斯剖面形成清晰边缘
    def line_field(x0, y0, x1, y1, sigma=1.5):
        # 到线段所在直线的距离
        dx, dy = x1 - x0, y1 - y0
        norm = np.hypot(dx, dy)
        if norm < 1e-9:
            return np.zeros((height, width))
        dist = np.abs(dy * xx - dx * yy + x1 * y0 - y1 * x0) / norm
        return np.exp(-(dist ** 2) / (2 * sigma ** 2))

    img += 0.6 * line_field(0, 0, width - 1, height - 1)          # 对角线
    img += 0.6 * line_field(0, height // 3, width - 1, height // 3)  # 水平线
    img += 0.6 * line_field(width // 4, 0, width // 4, height - 1)   # 垂直线

    img = np.clip(img, 0.0, 1.0).astype(np.float32)
    cube = img[np.newaxis, ...]
    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "n_true_lines": 3,
    }
    return cube, info


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
    """Read GeoTIFF → (cube, bbox). NoData == profile.nodata 保留原值。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_with_nodata(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """Read GeoTIFF → (cube, bbox, nodata_or_None)。

    凡与 ``profile['nodata']`` 严格相等的像元都会被替换为 NaN（避免污染边缘/梯度计算）。
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=False).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None and np.isfinite(nodata):
        cube = np.where(cube == float(nodata), np.nan, cube)
    return cube, bbox, nodata


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
            "method": getattr(args, "method", None),
            "threshold": getattr(args, "threshold", None),
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

    # ---- 0) CLI 参数前置校验（错误→rc=2）----
    validate_method_params(
        method=args.method,
        threshold=args.threshold,
        min_length=args.min_length,
        line_gap=args.line_gap,
        hough_threshold=args.hough_threshold,
    )

    bbox = list(args.bbox) if args.bbox else None
    if bbox is not None:
        validate_bbox(bbox)

    # 1) 获取数据立方体（通用契约）
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox, src_nodata = read_geotiff_with_nodata(args.input)
        # 始终校验 bbox（CLI 覆盖或 file_bbox 都需要再过一遍）
        bbox = bbox if bbox is not None else file_bbox
        validate_bbox(bbox)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, synth_info = generate_synthetic_cube(bbox)
        source_note = "synthetic"
        src_nodata = None

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    band = cube[0]
    h, w = band.shape

    # ---- 1.5) NoData / 全无效校验 ----
    n_valid_pixels = int(np.isfinite(band).sum())
    n_total_pixels = int(band.size)
    if n_valid_pixels == 0:
        raise ValidationError(
            "input has no finite (non-NoData) pixels after NoData masking; "
            "all values are NaN/nodata — refusing to produce a fake edge map",
            n_total_pixels=n_total_pixels, input_nodata=src_nodata)

    # ---- 通过校验后再创建输出目录 ----
    os.makedirs(output_dir, exist_ok=True)

    # 2) 边缘检测（normalize01 内部用 isfinite mask，已对 NoData 安全）
    edges = detect_edges(band, method=args.method, threshold=args.threshold)

    edge_tif = os.path.join(output_dir, "edges.tif")
    write_geotiff(edge_tif, edges, bbox)

    # 3) Hough 提取线性构造
    lines = extract_lineaments(
        edges, min_length=args.min_length,
        line_gap=args.line_gap, threshold=args.hough_threshold,
    )
    gdf = build_lineaments_gdf(lines, w, h, bbox)
    line_path = os.path.join(output_dir, "lineaments.geojson")
    n_feat = write_lineaments_geojson(line_path, gdf)

    st = edge_stats(edges)
    lengths = list(gdf["length_px"]) if n_feat else []
    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "threshold": args.threshold,
        "edge_density": st["edge_density"],
        "n_edge_pixels": st["n_edge_pixels"],
        "n_lineaments": len(lines),
        "mean_lineament_length_px": float(np.mean(lengths)) if lengths else 0.0,
        "n_valid_pixels": n_valid_pixels,
        "n_total_pixels": n_total_pixels,
        "valid_pixel_ratio": float(n_valid_pixels / n_total_pixels) if n_total_pixels else 0.0,
        "input_nodata": src_nodata,
    }
    if synth_info is not None:
        qa["synthetic_true_lines"] = synth_info["n_true_lines"]

    outputs = [
        {"path": edge_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1,
         "nodata": -9999.0, "feature_count": None},
        {"path": line_path, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": int(n_feat)},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  threshold: {args.threshold}")
        print(f"[{SKILL_NAME}] edge density: {st['edge_density']:.4f}")
        print(f"[{SKILL_NAME}] lineaments: {len(lines)}")
        print(f"[{SKILL_NAME}] valid pixels: {n_valid_pixels}/{n_total_pixels} "
              f"({qa['valid_pixel_ratio']:.2%})")
        print(f"[{SKILL_NAME}] output: {edge_tif}")
        print(f"[{SKILL_NAME}] lineaments: {line_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Edge detection (Canny/Sobel) + probabilistic Hough lineament extraction.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF (uses band 1)")
    p.add_argument("--method", default="canny", choices=["canny", "sobel"],
                   help="edge detection method (default: canny)")
    p.add_argument("--threshold", type=float, default=0.1,
                   help="edge threshold: Canny low-threshold or Sobel magnitude cut (default: 0.1)")
    p.add_argument("--min-length", type=int, default=15,
                   help="minimum lineament length in pixels for Hough (default: 15)")
    p.add_argument("--line-gap", type=int, default=5,
                   help="max gap to bridge between line segments (default: 5)")
    p.add_argument("--hough-threshold", type=int, default=10,
                   help="Hough accumulator threshold (default: 10)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic scene with linear edges (offline)")
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
