#!/usr/bin/env python3
"""urban-sprawl-analysis — 城市蔓延分析

从多期城市边界（二值栅格，1=建成区，0=非建成区）量化城市蔓延的形态
指标时序：

1. **紧凑度（circularity）**：4πA/P²，越接近 1 形态越紧凑（圆形）。
2. **分形维数（fractal dimension）**：由周长-面积关系
   D = 2·ln(P/4)/ln(A) 估计，越接近 2 边界越复杂。
3. **重心迁移**：逐期建成区质心坐标及相邻期重心位移（km）。
4. **扩张面积/速率**：相邻期新增像元、净增面积（km²）与增长率。

结果输出为蔓延指标时序 JSON、重心轨迹 JSON，以及用 geopandas/shapely
矢量化的多期城市边界 GeoJSON。合成模式生成逐渐向外（偏东）扩张的
多期城市斑块，完全离线。

数据源：本地多波段二值 GeoTIFF（每波段一期），或 ``--synthetic`` 合成序列。

隐私声明 / Privacy：
- 默认离线运行，不访问任何网络服务。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python urban-sprawl-analysis.py --input urban_multidate.tif --n-dates 4
    python urban-sprawl-analysis.py --bbox 116 39 117 40 --n-dates 4 --output-dir ./out

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
SKILL_NAME = "urban-sprawl-analysis"

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


def validate_bbox(bbox: Optional[List[float]]) -> List[float]:
    """Validate a [W, S, E, N] bbox in EPSG:4326.

    Rules:
      - W < E, S < N (non-degenerate)
      - lon ∈ [-180, 180], lat ∈ [-90, 90]
      - bbox area (in degree^2) must be > 0
      - cannot cross the 180° meridian (split into two if needed)
    """
    if bbox is None:
        raise ValidationError("bbox is required (provide --bbox or --input)")
    if len(bbox) != 4:
        raise ValidationError(f"bbox must have 4 floats, got {len(bbox)}")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox lon out of range [-180, 180]: W={w} E={e}",
            bbox=bbox,
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox lat out of range [-90, 90]: S={s} N={n}",
            bbox=bbox,
        )
    if w >= e:
        raise ValidationError(
            f"bbox W must be < E (got W={w} E={e}); cross-180° not supported, "
            f"split into two bboxes and merge results manually",
            bbox=bbox,
        )
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N (got S={s} N={n})",
            bbox=bbox,
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox area too small: dlon={e - w}, dlat={n - s}",
            bbox=bbox,
        )
    return [w, s, e, n]


def _pixel_geometry(bbox: List[float], shape: Tuple[int, int]) -> Dict[str, float]:
    """由 bbox 与 (H, W) 计算像元几何（km 与 deg）。"""
    h, w = shape
    lat_mid = (bbox[1] + bbox[3]) / 2.0
    deg_px_x = (bbox[2] - bbox[0]) / max(w, 1)
    deg_px_y = (bbox[3] - bbox[1]) / max(h, 1)
    km_px_x = deg_px_x * 111.32 * math.cos(math.radians(lat_mid))
    km_px_y = deg_px_y * 110.57
    return {
        "deg_px_x": deg_px_x, "deg_px_y": deg_px_y,
        "km_px_x": km_px_x, "km_px_y": km_px_y,
        "km_px_area": km_px_x * km_px_y,
        "km_px_mean": 0.5 * (km_px_x + km_px_y),
        "lat_mid": lat_mid,
    }


# ---------------------------------------------------------------------------
# 核心算法：单期形态指标
# ---------------------------------------------------------------------------
def perimeter_pixels(binary: np.ndarray) -> int:
    """统计建成区边界像元数（4-邻域侵蚀后取差集）。"""
    from scipy.ndimage import binary_erosion
    b = np.asarray(binary).astype(bool)
    if not b.any():
        return 0
    cross = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=bool)
    eroded = binary_erosion(b, structure=cross, border_value=0)
    edge = b & (~eroded)
    return int(edge.sum())


def compactness(area_px: float, perimeter_px: float) -> float:
    """圆形紧凑度 4πA/P²，裁剪到 [0, 1]（栅格阶梯边界可能使原值 >1）。"""
    if perimeter_px <= 0 or area_px <= 0:
        return 0.0
    val = (4.0 * math.pi * area_px) / (perimeter_px * perimeter_px)
    return float(min(max(val, 0.0), 1.0))


def fractal_dimension(area_px: float, perimeter_px: float) -> float:
    """分形维数 D = 2·ln(P/4)/ln(A)，裁剪到 [1, 2]。"""
    if area_px <= 1.0 or perimeter_px <= 4.0:
        return 1.0
    val = 2.0 * math.log(perimeter_px / 4.0) / math.log(area_px)
    return float(min(max(val, 1.0), 2.0))


def centroid_lonlat(binary: np.ndarray, bbox: List[float]) -> Optional[List[float]]:
    """建成区质心的 [lon, lat]（栅格第 0 行对应北边界）。无建成区返回 None。"""
    b = np.asarray(binary).astype(bool)
    if not b.any():
        return None
    rows, cols = np.where(b)
    h, w = b.shape
    deg_px_x = (bbox[2] - bbox[0]) / max(w, 1)
    deg_px_y = (bbox[3] - bbox[1]) / max(h, 1)
    c_col = float(cols.mean())
    c_row = float(rows.mean())
    lon = bbox[0] + (c_col + 0.5) * deg_px_x
    lat = bbox[3] - (c_row + 0.5) * deg_px_y
    return [float(lon), float(lat)]


def urban_metrics(binary: np.ndarray, bbox: List[float]) -> Dict[str, Any]:
    """单期城市形态指标。"""
    binary = np.asarray(binary)
    if binary.ndim != 2:
        raise ValidationError(
            f"each date must be a 2-D raster, got ndim={binary.ndim}",
            ndim=int(binary.ndim),
        )
    geom = _pixel_geometry(bbox, binary.shape)
    n_px = int((binary > 0).sum())
    if n_px == 0:
        return {
            "present": False, "urban_pixels": 0, "urban_area_km2": 0.0,
            "perimeter_pixels": 0, "perimeter_km": 0.0,
            "compactness": 0.0, "fractal_dimension": 0.0,
            "centroid": None,
        }
    perim_px = perimeter_pixels(binary)
    area_km2 = n_px * geom["km_px_area"]
    perim_km = perim_px * geom["km_px_mean"]
    return {
        "present": True,
        "urban_pixels": n_px,
        "urban_area_km2": float(area_km2),
        "perimeter_pixels": perim_px,
        "perimeter_km": float(perim_km),
        "compactness": compactness(n_px, perim_px),
        "fractal_dimension": fractal_dimension(n_px, perim_px),
        "centroid": centroid_lonlat(binary, bbox),
    }


def centroid_distance_km(c1: List[float], c2: List[float]) -> float:
    """两经纬度点之间的平面近似距离（km）。"""
    if c1 is None or c2 is None:
        return 0.0
    lat_mid = (c1[1] + c2[1]) / 2.0
    dx = (c2[0] - c1[0]) * 111.32 * math.cos(math.radians(lat_mid))
    dy = (c2[1] - c1[1]) * 110.57
    return float(math.hypot(dx, dy))


def sprawl_time_series(
    stack: np.ndarray,
    bbox: List[float],
    start_year: int = 2000,
    interval_years: int = 5,
) -> Dict[str, Any]:
    """多期蔓延指标时序。

    参数 stack: (n_dates, H, W) 二值栅格。
    返回逐期指标 + 相邻期变化（新增/损失像元、净增面积、增长率、重心位移）。
    """
    if stack.ndim != 3:
        raise ValidationError(
            f"stack must be 3-D (n_dates,H,W), got ndim={stack.ndim}",
            ndim=int(stack.ndim),
        )
    n = stack.shape[0]
    geom = _pixel_geometry(bbox, stack.shape[1:])
    dates: List[Dict[str, Any]] = []
    changes: List[Dict[str, Any]] = []

    prev_bin = None
    prev_metrics = None
    for i in range(n):
        b = (stack[i] > 0).astype(np.int32)
        m = urban_metrics(b, bbox)
        m["date_index"] = i
        m["year"] = int(start_year + i * interval_years)
        dates.append(m)

        if i > 0:
            cur = b.astype(bool)
            prev = prev_bin.astype(bool)
            new_px = int((cur & (~prev)).sum())
            lost_px = int((prev & (~cur)).sum())
            net_px = new_px - lost_px
            prev_area = prev_metrics["urban_area_km2"]
            growth_rate = (net_px * geom["km_px_area"]) / prev_area if prev_area > 0 else 0.0
            changes.append({
                "from_year": int(start_year + (i - 1) * interval_years),
                "to_year": m["year"],
                "new_pixels": new_px,
                "lost_pixels": lost_px,
                "net_pixels": net_px,
                "new_area_km2": new_px * geom["km_px_area"],
                "net_area_km2": net_px * geom["km_px_area"],
                "growth_rate": float(growth_rate),
                "centroid_shift_km": centroid_distance_km(
                    prev_metrics["centroid"], m["centroid"]),
            })
        prev_bin = b
        prev_metrics = m

    total_new = sum(c["new_pixels"] for c in changes)
    total_net = sum(c["net_pixels"] for c in changes)
    first_c = dates[0]["centroid"]
    last_c = dates[-1]["centroid"]
    summary = {
        "n_dates": n,
        "interval_years": int(interval_years),
        "total_new_pixels": int(total_new),
        "total_net_pixels": int(total_net),
        "total_new_area_km2": total_new * geom["km_px_area"],
        "total_net_area_km2": total_net * geom["km_px_area"],
        "net_expansion_detected": total_net > 0,
        "first_centroid": first_c,
        "last_centroid": last_c,
        "total_centroid_shift_km": centroid_distance_km(first_c, last_c),
    }
    return {"dates": dates, "changes": changes, "summary": summary}


# ---------------------------------------------------------------------------
# 合成数据：逐渐偏东扩张的多期城市斑块（离线）
# ---------------------------------------------------------------------------
def generate_synthetic_series(
    bbox: List[float],
    n_dates: int = 4,
    width: int = 96,
    height: int = 96,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (n_dates, H, W) 二值城市序列，面积逐期递增且重心东移。"""
    n_dates = max(int(n_dates), 2)
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)

    cx0 = width * 0.42
    cy0 = height * 0.55
    r0 = 0.10 * min(width, height)

    stack = np.zeros((n_dates, height, width), dtype=np.int32)
    counts = []
    for i in range(n_dates):
        r = r0 * (1.0 + 0.35 * i)
        main = ((xx - cx0) ** 2 + (yy - cy0) ** 2) <= r * r
        # 偏东副瓣：随期数增大，使重心向东迁移
        lobe_r = 0.45 * r * (i / max(n_dates - 1, 1))
        lobe_cx = cx0 + r * 1.15
        lobe = ((xx - lobe_cx) ** 2 + (yy - cy0) ** 2) <= lobe_r * lobe_r
        city = (main | lobe)
        # 少量随机边缘扰动，增加边界复杂度（保持单调：只加不减）
        noise = rng.random(city.shape) < 0.004
        city = city | (noise & (np.roll(city, 1, axis=0) | np.roll(city, 1, axis=1)))
        stack[i] = city.astype(np.int32)
        counts.append(int(city.sum()))

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "n_dates": n_dates,
        "urban_pixels_per_date": counts,
        "monotonic_growth": all(counts[i + 1] >= counts[i]
                                for i in range(len(counts) - 1)),
    }
    return stack, info


# ---------------------------------------------------------------------------
# 矢量化：多期城市边界 → GeoJSON（geopandas + shapely + rasterio.features）
# ---------------------------------------------------------------------------
def vectorize_series(stack: np.ndarray, bbox: List[float],
                     start_year: int = 2000,
                     interval_years: int = 5) -> Any:
    """把每期建成区栅格矢量化为多边形，返回带 date 属性的 GeoDataFrame。"""
    import geopandas as gpd
    import rasterio
    import rasterio.features
    from rasterio.transform import from_bounds
    from shapely.geometry import shape

    n, h, w = stack.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    records: List[Dict[str, Any]] = []
    for i in range(n):
        b = (stack[i] > 0).astype(np.uint8)
        polys = rasterio.features.shapes(b, mask=b.astype(bool), transform=transform)
        for geom, val in polys:
            if val != 1:
                continue
            records.append({
                "date_index": i,
                "year": int(start_year + i * interval_years),
                "geometry": shape(geom),
            })
    if not records:
        # 保证输出一个空但带 schema 的 GeoDataFrame
        return gpd.GeoDataFrame(
            {"date_index": [], "year": []}, geometry=[], crs="EPSG:4326")
    return gpd.GeoDataFrame(records, geometry="geometry", crs="EPSG:4326")


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


def read_binary_stack(path: str) -> Tuple[np.ndarray, List[float]]:
    """读取多波段栅格作为 (n_dates,H,W) 二值序列。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read()
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return (cube > 0).astype(np.int32), bbox


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
            "n_dates": getattr(args, "n_dates", None),
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

    # 1) 获取多期城市二值序列
    #    通用契约：给了 --input 就读真实栅格；否则（含 --synthetic）走合成。
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        stack, file_bbox = read_binary_stack(args.input)
        bbox = bbox if bbox is not None else file_bbox
        bbox = validate_bbox(bbox)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        stack, synth_info = generate_synthetic_series(
            bbox, n_dates=args.n_dates,
        )
        source_note = "synthetic"

    if stack.size == 0:
        raise ValidationError("input raster is empty")

    # 校验通过后再创建输出目录（避免失败路径残留空目录）
    os.makedirs(output_dir, exist_ok=True)

    # 2) 蔓延指标时序
    ts = sprawl_time_series(
        stack, bbox, start_year=args.start_year,
        interval_years=args.interval_years,
    )

    # 3) 写出产物
    metrics_path = os.path.join(output_dir, "sprawl_metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(ts, f, ensure_ascii=False, indent=2)

    centroid_path = os.path.join(output_dir, "centroid_trajectory.json")
    traj = {
        "trajectory": [
            {"year": d["year"], "centroid": d["centroid"]} for d in ts["dates"]
        ],
        "total_shift_km": ts["summary"]["total_centroid_shift_km"],
    }
    with open(centroid_path, "w", encoding="utf-8") as f:
        json.dump(traj, f, ensure_ascii=False, indent=2)

    gdf = vectorize_series(
        stack, bbox, start_year=args.start_year,
        interval_years=args.interval_years,
    )
    geojson_path = os.path.join(output_dir, "urban_footprint.geojson")
    gdf.to_file(geojson_path, driver="GeoJSON")

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_dates": ts["summary"]["n_dates"],
        "net_expansion_detected": ts["summary"]["net_expansion_detected"],
        "total_net_area_km2": ts["summary"]["total_net_area_km2"],
        "total_centroid_shift_km": ts["summary"]["total_centroid_shift_km"],
        "n_polygons": int(len(gdf)),
    }
    if synth_info is not None:
        qa["synthetic_pixels_per_date"] = synth_info["urban_pixels_per_date"]

    outputs = [
        {"path": metrics_path, "kind": "json"},
        {"path": centroid_path, "kind": "json"},
        {"path": geojson_path, "kind": "vector", "crs_epsg": 4326,
         "feature_count": int(len(gdf))},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] dates: {ts['summary']['n_dates']}")
        print(f"[{SKILL_NAME}] net expansion: "
              f"{ts['summary']['total_net_area_km2']:.4f} km² "
              f"(detected={ts['summary']['net_expansion_detected']})")
        print(f"[{SKILL_NAME}] centroid shift: "
              f"{ts['summary']['total_centroid_shift_km']:.4f} km")
        print(f"[{SKILL_NAME}] metrics: {metrics_path}")
        print(f"[{SKILL_NAME}] footprint: {geojson_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Quantify urban sprawl morphology from multi-date binary urban rasters.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="multi-band binary GeoTIFF (one band per date)")
    p.add_argument("--n-dates", type=int, default=4,
                   help="number of dates for synthetic mode, >=2 (default: 4)")
    p.add_argument("--start-year", type=int, default=2000,
                   help="first date year (default: 2000)")
    p.add_argument("--interval-years", type=int, default=5,
                   help="years between dates (default: 5)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate an expanding synthetic city series (offline)")
    p.add_argument("--output-dir", default="./output", help="output directory")
    p.add_argument("--quiet", action="store_true", help="suppress console output")
    p.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.n_dates < 2:
            raise UsageError(f"--n-dates must be >=2, got {args.n_dates}",
                             n_dates=int(args.n_dates))
        if args.interval_years < 1:
            raise UsageError(f"--interval-years must be >=1, got {args.interval_years}",
                             interval_years=int(args.interval_years))
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
