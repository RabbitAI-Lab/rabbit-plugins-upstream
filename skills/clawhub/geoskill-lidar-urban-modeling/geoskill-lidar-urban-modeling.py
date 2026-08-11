#!/usr/bin/env python3
"""lidar-urban-modeling — LiDAR 城市三维建模

从 LiDAR 点云提取城市建筑物的二维轮廓与三维体量：

1. **地面估计**：把点云栅格化为最低高程面（或低分位数面），再用渐进
   形态学滤波（PMF，Zhang et al. 2003 简化版）逐级开运算削去建筑/
   植被突起，得到裸地 DTM；
2. **nDSM**：最高高程面 DSM 减 DTM，得到归一化数字表面模型
   （non-ground height）；
3. **建筑提取**：阈值 nDSM ≥ min_height + 8 连通域标记 + 最小面积过滤；
4. **矢量化与建模**：rasterio.features.shapes 逐连通域提取多边形轮廓，
   每栋赋高度（区域内 nDSM 最大/均值）、底面积与体积（平均高 × 面积）。

数据源：本地点云（.npy / .csv / .txt xyz，建议投影或局部米制坐标），
或 ``--synthetic`` 生成平面地形 + 若干矩形建筑的模拟点云（离线）。

隐私声明 / Privacy：
- 完全离线运行，不访问任何网络服务。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python lidar-urban-modeling.py --input cloud.npy --min-height 3
    python lidar-urban-modeling.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "lidar-urban-modeling"

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
# 输入验证
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate WGS-84 bbox: W<E, S<N, lon∈[-180,180], lat∈[-90,90], nonzero area.

    Raises ValidationError (rc=6) on failure with a human-readable message.
    Bbox that crosses the antimeridian is rejected with a hint to split.
    """
    if bbox is None:
        raise ValidationError("bbox is required (--bbox or derive from --input)")
    if len(bbox) != 4:
        raise ValidationError(f"bbox must have 4 elements [W S E N], got {len(bbox)}")
    W, S, E, N = bbox
    if not all(np.isfinite([W, S, E, N])):
        raise ValidationError(f"bbox must be finite, got {[W, S, E, N]}")
    if W >= E:
        raise ValidationError(
            f"bbox invalid: minLon (W={W}) must be < maxLon (E={E})",
            west=W, east=E,
        )
    if S >= N:
        raise ValidationError(
            f"bbox invalid: minLat (S={S}) must be < maxLat (N={N})",
            south=S, north=N,
        )
    if W < -180 or E > 180:
        raise ValidationError(
            f"bbox longitude out of range [-180, 180]: W={W}, E={E}. "
            f"If the bbox crosses the antimeridian, split into two requests.",
            west=W, east=E,
        )
    if S < -90 or N > 90:
        raise ValidationError(
            f"bbox latitude out of range [-90, 90]: S={S}, N={N}",
            south=S, north=N,
        )
    if (E - W) * (N - S) <= 0:
        raise ValidationError(f"bbox has zero area: W={W}, E={E}, S={S}, N={N}")
    return None


def validate_params(args) -> None:
    """Validate numeric parameters: --min-height>0, --min-area>0, --cell-size>0."""
    for name, lo in (("min_height", 0.0), ("min_area", 0.0), ("cell_size", 0.0)):
        v = getattr(args, name)
        if not np.isfinite(v):
            raise ValidationError(f"--{name.replace('_', '-')} must be finite, got {v}")
        if v <= lo:
            raise ValidationError(f"--{name.replace('_', '-')} must be > {lo}, got {v}")
    return None


# ---------------------------------------------------------------------------
# 栅格化
# ---------------------------------------------------------------------------
def grid_extent(points: np.ndarray, cell_size: float
                ) -> Tuple[float, float, int, int]:
    """返回 (xmin, ymax, width, height)；行 0 = 最北（north-up）。"""
    xmin = float(points[:, 0].min())
    ymin = float(points[:, 1].min())
    xmax = float(points[:, 0].max())
    ymax = float(points[:, 1].max())
    w = max(1, int(np.ceil((xmax - xmin) / cell_size)))
    h = max(1, int(np.ceil((ymax - ymin) / cell_size)))
    return xmin, ymax, w, h


def cell_indices(points: np.ndarray, extent: Tuple[float, float, int, int],
                 cell_size: float) -> Tuple[np.ndarray, np.ndarray]:
    xmin, ymax, w, h = extent
    xi = np.clip(((points[:, 0] - xmin) / cell_size).astype(int), 0, w - 1)
    yi = np.clip(((ymax - points[:, 1]) / cell_size).astype(int), 0, h - 1)
    return xi, yi


def fill_nan_nearest(grid: np.ndarray) -> np.ndarray:
    from scipy.ndimage import distance_transform_edt
    mask = np.isnan(grid)
    if not mask.any():
        return grid.copy()
    if mask.all():
        return np.zeros_like(grid)
    _, idx = distance_transform_edt(mask, return_indices=True)
    return grid[tuple(idx)]


def rasterize_min_surface(points: np.ndarray, extent, cell_size: float) -> np.ndarray:
    xmin, ymax, w, h = extent
    xi, yi = cell_indices(points, extent, cell_size)
    surf = np.full((h, w), np.inf, dtype=np.float64)
    np.minimum.at(surf, (yi, xi), points[:, 2])
    surf[np.isinf(surf)] = np.nan
    return surf


def rasterize_max_surface(points: np.ndarray, extent, cell_size: float) -> np.ndarray:
    xmin, ymax, w, h = extent
    xi, yi = cell_indices(points, extent, cell_size)
    surf = np.full((h, w), -np.inf, dtype=np.float64)
    np.maximum.at(surf, (yi, xi), points[:, 2])
    surf[np.isneginf(surf)] = np.nan
    return surf


def rasterize_percentile_surface(points: np.ndarray, extent, cell_size: float,
                                 pct: float = 10.0) -> np.ndarray:
    """逐格网像元的 z 值低分位数面（比最低面对噪声更稳健）。"""
    xmin, ymax, w, h = extent
    xi, yi = cell_indices(points, extent, cell_size)
    flat_idx = yi * w + xi
    order = np.argsort(flat_idx, kind="stable")
    srt_idx = flat_idx[order]
    srt_z = points[order, 2]
    bounds = np.searchsorted(srt_idx, np.arange(w * h + 1))
    surf = np.full((h, w), np.nan, dtype=np.float64)
    flat = surf.ravel()
    for k in range(w * h):
        a, b = bounds[k], bounds[k + 1]
        if b > a:
            flat[k] = np.percentile(srt_z[a:b], pct)
    return surf


# ---------------------------------------------------------------------------
# 核心算法：地面估计（PMF 渐进形态学滤波）
# ---------------------------------------------------------------------------
def grey_opening(grid: np.ndarray, size: int) -> np.ndarray:
    """灰度开运算（先腐蚀后膨胀）：去除比结构元素小的正向突起。"""
    from scipy.ndimage import grey_erosion, grey_dilation
    return grey_dilation(grey_erosion(grid, size=size), size=size)


def pmf_ground_surface(grid: np.ndarray, cell_size: float, dh_base: float = 0.5,
                       max_slope: float = 0.15,
                       max_window_cells: Optional[int] = None) -> np.ndarray:
    """渐进形态学滤波估计裸地面。

    窗口逐级增大（3, 7, 15, 31...）；每级高程差阈值
    dh = dh_base + max_slope × 窗口宽度(米)，随地物尺度放宽，
    逐级削去灌木、乔木、建筑等突起而不破坏平缓地形。
    """
    surface = grid.copy()
    if max_window_cells is None:
        max_window_cells = max(3, (min(grid.shape) // 2) * 2 + 1)
    half = 1
    while 2 * half + 1 <= max_window_cells:
        size = 2 * half + 1
        dh = dh_base + max_slope * size * cell_size
        opened = grey_opening(surface, size=size)
        diff = surface - opened
        mask = diff > dh
        surface[mask] = opened[mask]
        half = 2 * half + 1
    return surface


def estimate_ground_surface(points: np.ndarray, extent, cell_size: float,
                            method: str = "min") -> np.ndarray:
    """地面面估计：min=最低高程面+PMF；percentile=10%分位数面+PMF。"""
    if method == "min":
        base = rasterize_min_surface(points, extent, cell_size)
    elif method == "percentile":
        base = rasterize_percentile_surface(points, extent, cell_size, pct=10.0)
    else:
        raise UsageError(f"unknown ground method '{method}'. Choose from: min, percentile",
                         method=method)
    return pmf_ground_surface(fill_nan_nearest(base), cell_size)


def compute_ndsm(points: np.ndarray, extent, cell_size: float,
                 ground_method: str = "min"
                 ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """返回 (ndsm, dsm, dtm)；nDSM = DSM − DTM，裁剪到 ≥ 0。"""
    dsm = fill_nan_nearest(rasterize_max_surface(points, extent, cell_size))
    dtm = estimate_ground_surface(points, extent, cell_size, ground_method)
    ndsm = np.clip(dsm - dtm, 0.0, None)
    return ndsm, dsm, dtm


# ---------------------------------------------------------------------------
# 核心算法：建筑提取与矢量化
# ---------------------------------------------------------------------------
def extract_buildings(ndsm: np.ndarray, extent: Tuple[float, float, int, int],
                      cell_size: float, min_height: float = 3.0,
                      min_area_m2: float = 15.0) -> List[Dict[str, Any]]:
    """阈值 + 8 连通域标记 + 最小面积过滤，逐栋量测栅格统计。

    返回建筑列表，每项含连通域掩膜 ``mask``、面积、最大/平均高度、
    体积（平均高 × 面积）与局部米制质心坐标。
    """
    from scipy.ndimage import label
    xmin, ymax = extent[0], extent[1]
    structure = np.ones((3, 3), dtype=bool)  # 8 连通
    lbl, n = label(ndsm >= min_height, structure=structure)
    cell_area = cell_size * cell_size
    buildings: List[Dict[str, Any]] = []
    for i in range(1, n + 1):
        comp = lbl == i
        n_cells = int(comp.sum())
        area = n_cells * cell_area
        if area < min_area_m2:
            continue
        z = ndsm[comp]
        height_max = float(z.max())
        height_mean = float(z.mean())
        rows, cols = np.where(comp)
        cy_row = float(rows.mean())
        cx_col = float(cols.mean())
        buildings.append({
            "mask": comp,
            "area_m2": float(area),
            "height_max": height_max,
            "height_mean": height_mean,
            "volume_m3": float(height_mean * area),
            "centroid_x": float(xmin + (cx_col + 0.5) * cell_size),
            "centroid_y": float(ymax - (cy_row + 0.5) * cell_size),
            "n_cells": n_cells,
        })
    buildings.sort(key=lambda b: -b["height_max"])
    for bid, b in enumerate(buildings):
        b["building_id"] = bid
    return buildings


def vectorize_buildings(buildings: List[Dict[str, Any]],
                        extent: Tuple[float, float, int, int],
                        cell_size: float) -> List[Any]:
    """逐连通域栅格转矢量（rasterio.features.shapes），返回与输入平行的
    shapely 几何列表（局部米制坐标，north-up）。"""
    from rasterio.features import shapes
    from rasterio.transform import from_origin
    from shapely.geometry import shape
    from shapely.ops import unary_union

    xmin, ymax = extent[0], extent[1]
    transform = from_origin(xmin, ymax, cell_size, cell_size)
    geoms: List[Any] = []
    for b in buildings:
        arr = b["mask"].astype(np.uint8)
        polys = [shape(g) for g, v in shapes(arr, transform=transform) if v == 1]
        if not polys:  # pragma: no cover - 连通域必有像元
            polys = []
        geom = unary_union(polys) if len(polys) != 1 else polys[0]
        geoms.append(geom)
    return geoms


def remap_geom_to_geo(geom: Any, work_bbox: List[float], geo_bbox: List[float]) -> Any:
    """把局部米制几何线性映射到地理 bbox（合成模式展示用）。"""
    from shapely.ops import transform as shp_transform
    wx0, wy0, wx1, wy1 = work_bbox
    gx0, gy0, gx1, gy1 = geo_bbox
    sx = (gx1 - gx0) / max(wx1 - wx0, 1e-9)
    sy = (gy1 - gy0) / max(wy1 - wy0, 1e-9)
    return shp_transform(lambda x, y: (gx0 + (x - wx0) * sx,
                                       gy0 + (y - wy0) * sy), geom)


# ---------------------------------------------------------------------------
# 合成数据：平面地形 + 矩形建筑（局部米制坐标）
# ---------------------------------------------------------------------------
def synthetic_terrain(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """平缓倾斜地形（m）：0.015x + 0.01y。"""
    return 0.015 * x + 0.01 * y


def generate_synthetic(bbox: List[float], cell_size: float = 1.0, seed: int = 42,
                       extent_m: float = 96.0, n_buildings: int = 8,
                       n_ground: int = 4500
                       ) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (N, 3) 点云；info['buildings'] 为注入真值
    [{x_min, y_min, x_max, y_max, cx, cy, height, width, depth, area_m2}]。

    建筑 = 平屋顶长方体：屋顶 0.5 m 网格点（平行于地形），四立面
    （内缩 0.1 m）均匀撒点至地面；建筑足迹内部不生成地面点
    （激光雷达无法穿透建筑）。
    """
    rng = np.random.default_rng(seed)
    pts: List[np.ndarray] = []

    buildings: List[Dict[str, float]] = []
    placed: List[Tuple[float, float, float, float]] = []  # (xmin, ymin, xmax, ymax)
    attempts = 0
    while len(buildings) < n_buildings and attempts < 400:
        attempts += 1
        w = float(rng.uniform(8.0, 18.0))
        d = float(rng.uniform(8.0, 18.0))
        h = float(rng.uniform(6.0, 25.0))
        x0 = float(rng.uniform(3.0, extent_m - w - 3.0))
        y0 = float(rng.uniform(3.0, extent_m - d - 3.0))
        x1, y1 = x0 + w, y0 + d
        margin = 4.0
        if any(not (x1 + margin < px0 or x0 - margin > px1 or
                    y1 + margin < py0 or y0 - margin > py1)
               for px0, py0, px1, py1 in placed):
            continue
        placed.append((x0, y0, x1, y1))
        buildings.append({
            "x_min": x0, "y_min": y0, "x_max": x1, "y_max": y1,
            "cx": x0 + w / 2.0, "cy": y0 + d / 2.0,
            "height": h, "width": w, "depth": d, "area_m2": w * d,
        })

    # 地面点：剔除落入建筑足迹内部的（建筑遮挡，无地面回波）
    gx = rng.uniform(0.0, extent_m, n_ground)
    gy = rng.uniform(0.0, extent_m, n_ground)
    inside = np.zeros(n_ground, dtype=bool)
    for b in buildings:
        inside |= ((gx >= b["x_min"]) & (gx <= b["x_max"])
                   & (gy >= b["y_min"]) & (gy <= b["y_max"]))
    gz = synthetic_terrain(gx[~inside], gy[~inside]) + rng.normal(0.0, 0.03, int((~inside).sum()))
    pts.append(np.column_stack([gx[~inside], gy[~inside], gz]))

    for b in buildings:
        x0, y0, x1, y1, h = (b["x_min"], b["y_min"], b["x_max"], b["y_max"],
                             b["height"])
        w, d = b["width"], b["depth"]

        # 屋顶：0.5 m 网格 + 抖动，顶面平行于地形（nDSM ≈ h）
        step = max(cell_size / 2.0, 0.4)
        rx = np.arange(x0 + step / 2.0, x1, step)
        ry = np.arange(y0 + step / 2.0, y1, step)
        rxx, ryy = np.meshgrid(rx, ry)
        rxx = rxx.ravel() + rng.uniform(-0.15, 0.15, rxx.size)
        ryy = ryy.ravel() + rng.uniform(-0.15, 0.15, ryy.size)
        rzz = synthetic_terrain(rxx, ryy) + h + rng.normal(0.0, 0.03, rxx.size)
        pts.append(np.column_stack([rxx, ryy, rzz]))

        # 四立面（内缩 0.1 m）：从地面到屋顶均匀撒点
        inset = 0.1
        per_wall = 150
        for edge in range(4):
            t = rng.uniform(0.0, 1.0, per_wall)
            zfrac = rng.uniform(0.0, 1.0, per_wall)
            if edge == 0:      # 南墙
                wxp = x0 + t * w
                wyp = np.full(per_wall, y0 + inset)
            elif edge == 1:    # 北墙
                wxp = x0 + t * w
                wyp = np.full(per_wall, y1 - inset)
            elif edge == 2:    # 西墙
                wxp = np.full(per_wall, x0 + inset)
                wyp = y0 + t * d
            else:              # 东墙
                wxp = np.full(per_wall, x1 - inset)
                wyp = y0 + t * d
            base = synthetic_terrain(wxp, wyp)
            wzp = base + zfrac * h + rng.normal(0.0, 0.02, per_wall)
            pts.append(np.column_stack([wxp, wyp, wzp]))

    points = np.vstack(pts).astype(np.float64)
    info = {
        "bbox": bbox,
        "extent_m": extent_m,
        "cell_size": cell_size,
        "n_points": int(points.shape[0]),
        "n_buildings_true": len(buildings),
        "buildings": buildings,
    }
    return points, info


# ---------------------------------------------------------------------------
# 点云 / 栅格 I/O
# ---------------------------------------------------------------------------
def read_points(path: str) -> np.ndarray:
    if not os.path.exists(path):
        raise UsageError(f"input point cloud not found: {path}", path=path)
    if path.lower().endswith(".npy"):
        arr = np.load(path)
    else:
        try:
            arr = np.loadtxt(path, delimiter=",", ndmin=2)
        except ValueError:
            arr = np.loadtxt(path, ndmin=2)
    arr = np.asarray(arr, dtype=np.float64)
    if arr.ndim != 2 or arr.shape[1] < 3:
        raise ValidationError("point cloud must have at least 3 columns (x, y, z)",
                              shape=list(arr.shape))
    return arr[:, :3]


def write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0) -> None:
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


def write_buildings_geojson(path: str, buildings: List[Dict[str, Any]],
                            geoms: List[Any]) -> None:
    """用 geopandas 写出建筑轮廓 GeoJSON（Polygon/MultiPolygon + 高度/体积属性）。"""
    import geopandas as gpd

    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    rows = [{
        "building_id": int(b["building_id"]),
        "height_max_m": round(float(b["height_max"]), 3),
        "height_mean_m": round(float(b["height_mean"]), 3),
        "area_m2": round(float(b["area_m2"]), 2),
        "volume_m3": round(float(b["volume_m3"]), 2),
    } for b in buildings]
    if rows:
        gdf = gpd.GeoDataFrame(rows, geometry=list(geoms), crs="EPSG:4326")
        gdf.to_file(path, driver="GeoJSON")
    else:
        # 空结果：直接写合法的空 FeatureCollection
        doc = {"type": "FeatureCollection", "name": "buildings",
               "crs": {"type": "name",
                       "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
               "features": []}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)


# ---------------------------------------------------------------------------
# 精度评估（合成真值匹配）
# ---------------------------------------------------------------------------
def match_buildings(detected: List[Dict[str, Any]], truth: List[Dict[str, Any]],
                    max_dist: float = 8.0
                    ) -> Tuple[List[Tuple[int, int]], float, float]:
    """最近邻质心匹配检测建筑与真值建筑。

    返回 (配对, 高度 RMSE, 相对面积误差 RMS)。
    """
    pairs: List[Tuple[int, int]] = []
    used: set = set()
    for di, d in enumerate(detected):
        best_j, best_d = -1, max_dist
        for tj, t in enumerate(truth):
            if tj in used:
                continue
            dist = float(np.hypot(d["centroid_x"] - t["cx"],
                                  d["centroid_y"] - t["cy"]))
            if dist < best_d:
                best_j, best_d = tj, dist
        if best_j >= 0:
            pairs.append((di, best_j))
            used.add(best_j)
    if pairs:
        h_err = np.array([detected[di]["height_max"] - truth[tj]["height"]
                          for di, tj in pairs])
        a_rel = np.array([(detected[di]["area_m2"] - truth[tj]["area_m2"])
                          / max(truth[tj]["area_m2"], 1e-6) for di, tj in pairs])
        h_rmse = float(np.sqrt(np.mean(h_err ** 2)))
        a_rrmse = float(np.sqrt(np.mean(a_rel ** 2)))
    else:
        h_rmse = a_rrmse = float("nan")
    return pairs, h_rmse, a_rrmse


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir: str, args: argparse.Namespace,
                   outputs: List[Dict[str, Any]], qa: Dict[str, Any],
                   started_at: str, exit_code: int, bbox: List[float]) -> Optional[str]:
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
            "min_height": getattr(args, "min_height", None),
            "min_area": getattr(args, "min_area", None),
            "cell_size": getattr(args, "cell_size", None),
            "ground_method": getattr(args, "ground_method", None),
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

    # ---- 1. 参数与路径验证（先于任何 makedirs / 数据读取）----
    if args.input is None and bbox is None:
        raise UsageError("provide --bbox (synthetic mode) or --input <point cloud>")
    if args.input:
        if not os.path.exists(args.input):
            raise UsageError(f"input point cloud not found: {args.input}", path=args.input)
    validate_params(args)

    # ---- 2. 读取输入（可能推导 bbox）----
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        points = read_points(args.input)
        if bbox is None:
            bbox = [float(points[:, 0].min()), float(points[:, 1].min()),
                    float(points[:, 0].max()), float(points[:, 1].max())]
        coord_is_geo = True
        source_note = args.input
    else:
        validate_bbox(bbox)
        points, synth_info = generate_synthetic(bbox, cell_size=args.cell_size)
        coord_is_geo = False
        source_note = "synthetic"

    if points.shape[0] == 0:
        raise ValidationError("point cloud is empty")
    if not np.all(np.isfinite(points)):
        raise ValidationError("point cloud contains non-finite coordinates")

    # ---- 3. 全部验证已通过，创建输出目录 ----
    os.makedirs(output_dir, exist_ok=True)

    extent = grid_extent(points, args.cell_size)
    ndsm, dsm, dtm = compute_ndsm(points, extent, args.cell_size, args.ground_method)
    buildings = extract_buildings(ndsm, extent, args.cell_size,
                                  args.min_height, args.min_area)
    geoms = vectorize_buildings(buildings, extent, args.cell_size)

    # 合成模式：局部米制轮廓映射到地理 bbox 展示
    work_bbox = [extent[0], extent[1] - extent[3] * args.cell_size,
                 extent[0] + extent[2] * args.cell_size, extent[1]]
    if not coord_is_geo:
        geoms = [remap_geom_to_geo(g, work_bbox, bbox) for g in geoms]

    heights = [b["height_max"] for b in buildings]
    stats: Dict[str, Any] = {
        "source": source_note,
        "cell_size": args.cell_size,
        "ground_method": args.ground_method,
        "min_height_filter": args.min_height,
        "min_area_filter_m2": args.min_area,
        "n_buildings_detected": len(buildings),
        "mean_height_max": float(np.mean(heights)) if heights else 0.0,
        "max_height": float(np.max(heights)) if heights else 0.0,
        "total_footprint_m2": float(sum(b["area_m2"] for b in buildings)),
        "total_volume_m3": float(sum(b["volume_m3"] for b in buildings)),
    }
    if synth_info is not None:
        pairs, h_rmse, a_rrmse = match_buildings(buildings, synth_info["buildings"])
        stats["n_buildings_true"] = synth_info["n_buildings_true"]
        stats["n_matched"] = len(pairs)
        stats["detection_rate"] = len(pairs) / max(synth_info["n_buildings_true"], 1)
        stats["height_rmse_m"] = h_rmse
        stats["area_relative_rrmse"] = a_rrmse

    # 写出产物
    ndsm_path = os.path.join(output_dir, "ndsm.tif")
    write_geotiff(ndsm_path, ndsm.astype(np.float32), bbox, nodata=-1.0)

    buildings_path = os.path.join(output_dir, "buildings.geojson")
    write_buildings_geojson(buildings_path, buildings, geoms)

    stats_path = os.path.join(output_dir, "stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_buildings_detected": len(buildings),
        "mean_height_max": stats["mean_height_max"],
        "max_height": stats["max_height"],
        "total_volume_m3": stats["total_volume_m3"],
        "detection_rate": stats.get("detection_rate"),
        "height_rmse_m": stats.get("height_rmse_m"),
    }
    outputs = [
        {"path": ndsm_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": buildings_path, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": len(buildings)},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] ground method: {args.ground_method}  "
              f"min_height={args.min_height} m")
        print(f"[{SKILL_NAME}] buildings detected: {len(buildings)}")
        if heights:
            print(f"[{SKILL_NAME}] height: mean={stats['mean_height_max']:.2f}  "
                  f"max={stats['max_height']:.2f} m")
            print(f"[{SKILL_NAME}] total volume: {stats['total_volume_m3']:.0f} m3")
        if "detection_rate" in stats:
            print(f"[{SKILL_NAME}] detection rate: {stats['detection_rate']:.2f}  "
                  f"height RMSE: {stats['height_rmse_m']:.3f} m")
        print(f"[{SKILL_NAME}] output: {ndsm_path}")
        print(f"[{SKILL_NAME}] output: {buildings_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="LiDAR urban 3D modeling: nDSM, building footprints, heights & volumes.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input point cloud (.npy or .csv/.txt xyz)")
    p.add_argument("--min-height", type=float, default=3.0,
                   help="minimum building height in nDSM meters (default: 3.0)")
    p.add_argument("--min-area", type=float, default=15.0,
                   help="minimum footprint area in m2 (default: 15.0)")
    p.add_argument("--cell-size", type=float, default=1.0,
                   help="rasterization cell size in point-cloud units (default: 1.0)")
    p.add_argument("--ground-method", default="min", choices=["min", "percentile"],
                   help="ground surface estimation (default: min)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic urban scene (offline)")
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
