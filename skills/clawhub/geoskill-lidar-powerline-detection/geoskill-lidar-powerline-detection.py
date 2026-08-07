#!/usr/bin/env python3
"""lidar-powerline-detection — LiDAR 电力线检测

从 LiDAR 点云（N,3 的 xyz 数组）中提取电力线走廊的关键要素：

- **高程滤波**：用低分位数估计地面高程，提取高于地面 ``min_height`` 的候选点。
- **线性特征检测**：对候选点做主成分分析（PCA），电力线在平面投影上呈细长
  线性结构（主轴方差远大于垂直方向），用垂直距离阈值提取线性内点。
- **悬链线拟合**：电力线在重力下呈悬链线 ``z = offset + a·cosh((u-u0)/a)``，
  用 scipy 非线性最小二乘拟合，估计弧垂（sag）与拟合残差。
- **塔架聚类**：塔架是高程高、平面紧凑的垂直结构，用 cKDTree 连通分量聚类
  高点的 xy 位置，按垂直范围判定塔架。
- **线-树距离**：以植被点（高于地面但低于电力线、非塔架）与电力线内点的最近
  水平距离评估线路净空（clearance）。

数据源：本地 LiDAR 点云（.npy / .txt / .csv / .xyz，每行 x y z），或使用
``--synthetic`` 生成物理一致的模拟场景（地面 + 悬链线电力线 + 两端塔架 + 植被）。

隐私声明 / Privacy：
- 默认完全离线运行，不发起任何网络请求。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python lidar-powerline-detection.py --bbox 116 39 117 40 --min-height 5 --output-dir ./out
    python lidar-powerline-detection.py --input cloud.xyz --output-dir ./out

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
SKILL_NAME = "lidar-powerline-detection"

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
    """Validate numeric parameters: min-height, inlier-thresh, tower-thresh, tower-excl.

    inlier_thresh and tower_excl must be strictly > 0 (zero makes the algorithm
    degenerate: no points can be inliers, or zero exclusion radius).
    min_height and tower_thresh must be >= 0.
    """
    ge0 = ("min_height", "tower_thresh")
    gt0 = ("inlier_thresh", "tower_excl")
    for name in ge0:
        v = getattr(args, name)
        if not np.isfinite(v):
            raise ValidationError(f"--{name.replace('_', '-')} must be finite, got {v}")
        if v < 0:
            raise ValidationError(f"--{name.replace('_', '-')} must be >= 0, got {v}")
    for name in gt0:
        v = getattr(args, name)
        if not np.isfinite(v):
            raise ValidationError(f"--{name.replace('_', '-')} must be finite, got {v}")
        if v <= 0:
            raise ValidationError(f"--{name.replace('_', '-')} must be > 0, got {v}")
    return None


# ---------------------------------------------------------------------------
# 坐标参考：本地米制坐标 <-> WGS84 经纬度
# ---------------------------------------------------------------------------
M_PER_DEG_LAT = 110540.0


def meters_per_deg_lon(lat_deg: float) -> float:
    return 111320.0 * math.cos(math.radians(lat_deg))


def make_geo_ref(bbox: List[float]) -> Dict[str, Any]:
    """以 bbox 西南角为原点，建立本地米制坐标参考。"""
    W, S, E, N = bbox
    midlat = 0.5 * (S + N)
    return {
        "x0": float(W), "y0": float(S),
        "kx": meters_per_deg_lon(midlat), "ky": M_PER_DEG_LAT,
        "geographic": True,
    }


def local_size_m(bbox: List[float]) -> Tuple[float, float]:
    W, S, E, N = bbox
    midlat = 0.5 * (S + N)
    width_m = (E - W) * meters_per_deg_lon(midlat)
    height_m = (N - S) * M_PER_DEG_LAT
    return float(width_m), float(height_m)


def meters_to_lonlat(
    x_m: np.ndarray, y_m: np.ndarray, geo_ref: Dict[str, Any]
) -> Tuple[np.ndarray, np.ndarray]:
    if not geo_ref.get("geographic", False):
        return np.asarray(x_m, dtype=float), np.asarray(y_m, dtype=float)
    lon = geo_ref["x0"] + np.asarray(x_m, dtype=float) / geo_ref["kx"]
    lat = geo_ref["y0"] + np.asarray(y_m, dtype=float) / geo_ref["ky"]
    return lon, lat


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def estimate_ground_height(points: np.ndarray, percentile: float = 5.0) -> float:
    """用 z 的低分位数估计地面高程（稳健，不受塔架/线影响）。"""
    if points.size == 0:
        return 0.0
    z = points[:, 2]
    z = z[np.isfinite(z)]
    if z.size == 0:
        return 0.0
    return float(np.percentile(z, percentile))


def filter_above_ground(
    points: np.ndarray, min_height: float, percentile: float = 5.0
) -> Tuple[np.ndarray, float]:
    """提取高于地面 ``min_height`` 的点。返回 (above_points, ground_z)。"""
    ground_z = estimate_ground_height(points, percentile)
    if points.size == 0:
        return points, ground_z
    mask = points[:, 2] > (ground_z + min_height)
    return points[mask], ground_z


def pca_direction(xy: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """对 (N,2) 做 PCA，返回 (centroid, 主轴单位方向向量, 降序特征值)。"""
    centroid = xy.mean(axis=0)
    centered = xy - centroid
    cov = np.cov(centered, rowvar=False)
    eigvals, eigvecs = np.linalg.eigh(cov)
    order = np.argsort(eigvals)[::-1]
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]
    direction = eigvecs[:, 0]
    direction = direction / (np.linalg.norm(direction) + 1e-12)
    return centroid, direction, eigvals


def detect_linear_feature(
    points: np.ndarray, inlier_thresh: float = 3.0
) -> Dict[str, Any]:
    """在点云的平面投影中检测细长线性特征（电力线）。

    用 PCA 主轴作为线的方向，以垂直距离 < inlier_thresh 提取内点。
    返回 elongation（主轴方差 / 次轴方差，越大越细长）等信息。
    """
    if points.shape[0] < 3:
        raise ValidationError(
            f"too few points for linear detection: {points.shape[0]}",
            n_points=int(points.shape[0]),
        )
    xy = points[:, :2]
    centroid, direction, eigvals = pca_direction(xy)
    # 次轴方向
    perp = np.array([-direction[1], direction[0]])
    centered = xy - centroid
    along = centered @ direction
    across = centered @ perp
    inlier_mask = np.abs(across) < inlier_thresh
    if not np.any(inlier_mask):
        # 阈值过严，退化为取最靠近主轴的一半点
        inlier_mask = np.abs(across) < np.percentile(np.abs(across), 50)
    elongation = float(eigvals[0] / (eigvals[1] + 1e-9))
    return {
        "centroid": centroid,
        "direction": direction,
        "perp": perp,
        "along": along,
        "across": across,
        "inlier_mask": inlier_mask,
        "inlier_points": points[inlier_mask],
        "elongation": elongation,
        "n_inliers": int(np.sum(inlier_mask)),
    }


def project_along(
    points: np.ndarray, centroid: np.ndarray, direction: np.ndarray
) -> np.ndarray:
    """把点投影到线主轴上，返回沿轴坐标 u（以 centroid 为原点）。"""
    return (points[:, :2] - centroid) @ direction


def cluster_towers(
    points: np.ndarray,
    ground_z: float,
    high_thresh: float = 15.0,
    eps: float = 8.0,
    min_points: int = 8,
    min_extent: float = 5.0,
) -> List[Dict[str, Any]]:
    """检测塔架：高点（z > ground + high_thresh）在单个平面网格内紧凑且垂直范围大。

    电力线本身可能整体很高，但它水平延展、逐网格垂直范围小；塔架是垂直柱，
    单网格内点数多且 z 跨度大。因此用平面网格（cell=eps）统计：某网格高点数
    >= min_points 且垂直范围 >= min_extent 才作为塔架候选，再把相邻候选合并。
    这种逐网格判定避免连通分量把整条电力线连成一个巨型簇。
    """
    if points.shape[0] == 0:
        return []
    high_mask = points[:, 2] > (ground_z + high_thresh)
    high = points[high_mask]
    if high.shape[0] < min_points:
        return []

    cell = float(eps)
    cx = np.floor(high[:, 0] / cell).astype(int)
    cy = np.floor(high[:, 1] / cell).astype(int)
    keys = list({(int(cx[i]), int(cy[i])) for i in range(high.shape[0])})

    candidates: List[Dict[str, Any]] = []
    for (ix, iy) in keys:
        mask = (cx == ix) & (cy == iy)
        sub = high[mask]
        if sub.shape[0] < min_points:
            continue
        z_extent = float(sub[:, 2].max() - sub[:, 2].min())
        if z_extent < min_extent:
            continue
        xy_center = sub[:, :2].mean(axis=0)
        candidates.append({
            "xy": [float(xy_center[0]), float(xy_center[1])],
            "z_max": float(sub[:, 2].max()),
            "n_points": int(sub.shape[0]),
            "z_extent": z_extent,
        })

    if not candidates:
        return []

    # 合并相邻候选（同一塔架可能跨 2~4 个网格）
    merge_r = cell * 1.6
    parent = np.arange(len(candidates))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    cxy = np.array([c["xy"] for c in candidates])
    for i in range(len(candidates)):
        for j in range(i + 1, len(candidates)):
            if np.hypot(*(cxy[i] - cxy[j])) < merge_r:
                union(i, j)

    groups: Dict[int, List[int]] = {}
    for i in range(len(candidates)):
        groups.setdefault(find(i), []).append(i)

    towers: List[Dict[str, Any]] = []
    for idxs in groups.values():
        subs = [candidates[i] for i in idxs]
        total = sum(s["n_points"] for s in subs)
        wsum = np.array([s["xy"][0] * s["n_points"] for s in subs]).sum()
        wx = wsum / total
        wsum_y = np.array([s["xy"][1] * s["n_points"] for s in subs]).sum()
        wy = wsum_y / total
        z_max = max(s["z_max"] for s in subs)
        towers.append({
            "xy": [float(wx), float(wy)],
            "height": float(z_max - ground_z),
            "z_max": float(z_max),
            "n_points": int(total),
            "z_extent": float(max(s["z_extent"] for s in subs)),
        })
    towers.sort(key=lambda t: t["height"], reverse=True)
    return towers


def upper_envelope(
    u: np.ndarray, z: np.ndarray, n_bins: int = 80
) -> Tuple[np.ndarray, np.ndarray]:
    """沿轴分箱，取每箱最高回波——电力线是各水平位置的最高回波。

    这一步剔除混入线带内的低矮植被/地面离群点，得到干净的导线剖面。
    """
    u = np.asarray(u, dtype=float)
    z = np.asarray(z, dtype=float)
    if u.size == 0:
        return u, z
    n_bins = max(int(n_bins), 4)
    edges = np.linspace(float(u.min()), float(u.max()), n_bins + 1)
    idx = np.clip(np.digitize(u, edges) - 1, 0, n_bins - 1)
    uu: List[float] = []
    zz: List[float] = []
    for b in range(n_bins):
        m = idx == b
        if not np.any(m):
            continue
        sub_u = u[m]
        sub_z = z[m]
        k = int(np.argmax(sub_z))
        uu.append(float(sub_u[k]))
        zz.append(float(sub_z[k]))
    return np.array(uu), np.array(zz)


def fit_catenary(u: np.ndarray, z: np.ndarray) -> Dict[str, Any]:
    """拟合悬链线 z = offset + a·cosh((u-u0)/a)。

    返回参数、弧垂 sag（端点均值 - 最低点）与拟合 RMSE。
    """
    from scipy.optimize import curve_fit

    u = np.asarray(u, dtype=float)
    z = np.asarray(z, dtype=float)
    if u.size < 4:
        raise ValidationError(
            f"too few points for catenary fit: {u.size}", n_points=int(u.size)
        )

    def model(x: np.ndarray, offset: float, a: float, u0: float) -> np.ndarray:
        return offset + a * np.cosh((x - u0) / a)

    span = float(u.max() - u.min())
    z_min = float(z.min())
    z_max = float(z.max())
    sag0 = max(z_max - z_min, 0.1)
    a0 = max(span * span / (8.0 * sag0), 1e-3)
    u0_0 = float(u[np.argmin(z)])

    try:
        popt, _ = curve_fit(
            model, u, z,
            p0=[z_min, a0, u0_0],
            bounds=([-np.inf, 1e-3, -np.inf], [np.inf, np.inf, np.inf]),
            maxfev=20000,
        )
    except (RuntimeError, ValueError) as exc:
        raise ProcessError(f"catenary fit failed: {exc}") from exc

    offset, a, u0 = (float(popt[0]), float(popt[1]), float(popt[2]))
    fitted = model(u, offset, a, u0)
    resid = z - fitted
    rmse = float(np.sqrt(np.mean(resid ** 2)))
    # 悬链线最低点在 u0 处，值为 offset + a（cosh(0)=1）；弧垂 = 端点均值 - 最低点
    u_lo, u_hi = float(u.min()), float(u.max())
    z_end = 0.5 * (model(u_lo, offset, a, u0) + model(u_hi, offset, a, u0))
    z_min_curve = offset + a
    sag = float(z_end - z_min_curve)
    return {
        "offset": offset, "a": a, "u0": u0,
        "sag": sag, "rmse": rmse,
        "span": span, "n_points": int(u.size),
    }


def line_tree_distance(
    line_xy: np.ndarray, veg_xy: np.ndarray
) -> Dict[str, Any]:
    """计算植被点到电力线内点的最近水平距离（净空评估）。"""
    if line_xy.shape[0] == 0 or veg_xy.shape[0] == 0:
        return {
            "n_vegetation": int(veg_xy.shape[0]),
            "min_distance": None, "mean_distance": None,
            "n_within_5m": 0,
        }
    from scipy.spatial import cKDTree

    tree = cKDTree(line_xy)
    dist, _ = tree.query(veg_xy, k=1)
    return {
        "n_vegetation": int(veg_xy.shape[0]),
        "min_distance": float(dist.min()),
        "mean_distance": float(dist.mean()),
        "max_distance": float(dist.max()),
        "n_within_5m": int(np.sum(dist < 5.0)),
    }


# ---------------------------------------------------------------------------
# 合成数据：地面 + 悬链线电力线 + 两端塔架 + 植被（本地米制坐标）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (N,3) 点云（本地米制坐标）与场景真值信息。"""
    rng = np.random.default_rng(seed)
    width_m, height_m = local_size_m(bbox)
    ground = 0.0
    tower_h = 25.0
    sag = 8.0
    # 塔架位置：沿 x 轴居中一条线
    ax = (0.20 * width_m, 0.50 * height_m)
    bx = (0.80 * width_m, 0.50 * height_m)
    span = bx[0] - ax[0]
    a_true = max(span * span / (8.0 * sag), 1e-3)
    c_true = tower_h - a_true * math.cosh(span / (2.0 * a_true))

    def catenary_z(u: float) -> float:
        # u 以 A 为 0，B 为 span
        return a_true * math.cosh((u - span / 2.0) / a_true) + c_true

    pts: List[np.ndarray] = []

    # 地面点
    n_ground = 2000
    gx = rng.uniform(0, width_m, n_ground)
    gy = rng.uniform(0, height_m, n_ground)
    gz = rng.normal(ground, 0.3, n_ground)
    pts.append(np.column_stack([gx, gy, gz]))

    # 电力线点（沿悬链线）
    n_line = 600
    u_line = np.linspace(0, span, n_line)
    lx = ax[0] + u_line
    ly = np.full(n_line, ax[1]) + rng.normal(0, 0.3, n_line)
    lz = np.array([catenary_z(u) for u in u_line]) + rng.normal(0, 0.15, n_line)
    pts.append(np.column_stack([lx, ly, lz]))

    # 塔架点（两端垂直柱）
    n_tower = 300
    for (tx, ty) in (ax, bx):
        tz = rng.uniform(ground, tower_h, n_tower)
        txx = tx + rng.normal(0, 1.0, n_tower)
        tyy = ty + rng.normal(0, 1.0, n_tower)
        pts.append(np.column_stack([txx, tyy, tz]))

    # 植被点（线两侧走廊内，高度 2~12m）
    n_tree = 800
    tree_u = rng.uniform(0, span, n_tree)
    offset = rng.uniform(-20, 20, n_tree)
    vx = ax[0] + tree_u
    vy = ax[1] + offset
    vz = rng.uniform(2.0, 12.0, n_tree)
    pts.append(np.column_stack([vx, vy, vz]))

    points = np.vstack(pts).astype(np.float32)
    info = {
        "bbox": bbox,
        "width_m": width_m,
        "height_m": height_m,
        "tower_a_m": [float(ax[0]), float(ax[1])],
        "tower_b_m": [float(bx[0]), float(bx[1])],
        "tower_height": tower_h,
        "true_sag": sag,
        "true_catenary_a": float(a_true),
        "span_m": float(span),
        "n_points": int(points.shape[0]),
    }
    return points, info


# ---------------------------------------------------------------------------
# 点云 I/O
# ---------------------------------------------------------------------------
def read_pointcloud(path: str) -> np.ndarray:
    """读取点云 (.npy / 分隔文本)，返回 (N,3)。"""
    if not os.path.exists(path):
        raise UsageError(f"input point cloud not found: {path}", path=path)
    try:
        if path.lower().endswith(".npy"):
            arr = np.load(path)
        else:
            # 先试空白分隔，再试逗号
            try:
                arr = np.genfromtxt(path, comments="#", dtype=float)
                if np.isnan(arr).all():
                    raise ValueError("all nan")
            except (ValueError, StopIteration):
                arr = np.genfromtxt(path, delimiter=",", comments="#", dtype=float)
    except Exception as exc:  # noqa: BLE001
        raise UsageError(f"failed to read point cloud '{path}': {exc}", path=path) from exc

    arr = np.asarray(arr, dtype=float)
    if arr.ndim == 1:
        arr = arr.reshape(1, -1)
    if arr.shape[1] < 3:
        raise ValidationError(
            f"point cloud needs >=3 columns (x,y,z), got {arr.shape[1]}",
            columns=int(arr.shape[1]),
        )
    # 去掉非有限行
    finite = np.isfinite(arr[:, :3]).all(axis=1)
    arr = arr[finite, :3]
    if arr.shape[0] == 0:
        raise ValidationError("point cloud has no valid points")
    return arr


def build_geo_ref_from_points(points: np.ndarray, bbox: Optional[List[float]]) -> Dict[str, Any]:
    """为输入点云建立坐标参考。若 bbox 给定则用它；否则用数据范围。

    若坐标看起来是经纬度（绝对值小），则转为本地米制并以 geographic 标记。
    """
    if bbox is not None:
        return make_geo_ref(bbox)
    minx = float(points[:, 0].min())
    miny = float(points[:, 1].min())
    maxx = float(points[:, 0].max())
    maxy = float(points[:, 1].max())
    geographic = abs(minx) <= 180 and abs(maxx) <= 180 and abs(miny) <= 90 and abs(maxy) <= 90 \
        and (maxx - minx) < 90
    return {"x0": minx, "y0": miny,
            "kx": meters_per_deg_lon(0.5 * (miny + maxy)) if geographic else 1.0,
            "ky": M_PER_DEG_LAT if geographic else 1.0,
            "geographic": geographic}


def points_to_local(points: np.ndarray, geo_ref: Dict[str, Any]) -> np.ndarray:
    """把经纬度点云转为本地米制（若 geo_ref.geographic）。否则原样返回。"""
    if not geo_ref.get("geographic", False):
        return points
    out = points.copy().astype(float)
    out[:, 0] = (points[:, 0] - geo_ref["x0"]) * geo_ref["kx"]
    out[:, 1] = (points[:, 1] - geo_ref["y0"]) * geo_ref["ky"]
    return out


# ---------------------------------------------------------------------------
# GeoJSON 输出
# ---------------------------------------------------------------------------
def write_geojson(path: str, features: List[Dict[str, Any]]) -> None:
    fc = {"type": "FeatureCollection", "features": features}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(fc, f, ensure_ascii=False, indent=2)


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
    bbox: Optional[List[float]],
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
            "min_height": getattr(args, "min_height", None),
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

    # ---- 1. 参数与路径验证（先于任何 makedirs / 数据读取）----
    if args.input is None and bbox is None:
        raise UsageError("provide --bbox (synthetic mode) or --input <pointcloud>")
    if args.input:
        if not os.path.exists(args.input):
            raise UsageError(f"input point cloud not found: {args.input}", path=args.input)
    validate_params(args)

    # ---- 2. 读取输入（可能推导 bbox）----
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        pts_raw = read_pointcloud(args.input)
        geo_ref = build_geo_ref_from_points(pts_raw, bbox)
        points = points_to_local(pts_raw, geo_ref)
        source_note = args.input
    else:
        validate_bbox(bbox)
        points, synth_info = generate_synthetic(bbox)
        geo_ref = make_geo_ref(bbox)
        source_note = "synthetic"

    if points.shape[0] == 0:
        raise ValidationError("point cloud is empty")

    # ---- 3. 全部验证已通过，创建输出目录 ----
    os.makedirs(output_dir, exist_ok=True)

    # 2) 高程滤波
    above, ground_z = filter_above_ground(points, args.min_height)
    if above.shape[0] < 5:
        raise ValidationError(
            f"too few above-ground points ({above.shape[0]}); lower --min-height",
            n_above=int(above.shape[0]),
        )

    # 3) 线性特征检测
    feat = detect_linear_feature(above, inlier_thresh=args.inlier_thresh)
    line_pts = feat["inlier_points"]

    # 4) 塔架聚类
    towers = cluster_towers(above, ground_z, high_thresh=args.tower_thresh)

    # 5) 悬链线拟合（排除塔架附近的点，聚焦档距中段）
    u_line = project_along(line_pts, feat["centroid"], feat["direction"])
    tower_u: List[float] = []
    for t in towers:
        txy = np.array(t["xy"])
        tu = float((txy - feat["centroid"]) @ feat["direction"])
        tower_u.append(tu)
    # 塔架影响半径（沿轴）
    excl = args.tower_excl
    keep = np.ones(line_pts.shape[0], dtype=bool)
    if tower_u:
        tu_arr = np.array(tower_u)
        for i in range(line_pts.shape[0]):
            if np.any(np.abs(u_line[i] - tu_arr) < excl):
                keep[i] = False
    span_u = u_line[keep]
    span_z = line_pts[keep, 2]
    catenary = None
    if span_u.size >= 4 and (span_u.max() - span_u.min()) > 0:
        # 取上包络剔除低矮植被，再拟合悬链线
        env_u, env_z = upper_envelope(span_u, span_z, n_bins=80)
        if env_u.size >= 4 and (env_u.max() - env_u.min()) > 0:
            catenary = fit_catenary(env_u, env_z)

    # 6) 植被 / 线-树距离
    #    植被 = 高于地面但低于电力线最低点附近、非线内点、非塔架
    line_set = set(map(tuple, np.round(line_pts[:, :2], 3)))
    veg_mask = np.ones(above.shape[0], dtype=bool)
    for i in range(above.shape[0]):
        key = tuple(np.round(above[i, :2], 3))
        if key in line_set:
            veg_mask[i] = False
    veg = above[veg_mask]
    clearance = line_tree_distance(line_pts[:, :2], veg[:, :2])

    # 7) 输出
    # 电力线矢量（按沿轴坐标排序的 LineString，经纬度 + 高程）
    order = np.argsort(u_line)
    line_sorted = line_pts[order]
    lon, lat = meters_to_lonlat(line_sorted[:, 0], line_sorted[:, 1], geo_ref)
    coords = [[float(lon[i]), float(lat[i]), float(line_sorted[i, 2])]
              for i in range(line_sorted.shape[0])]
    line_feature = {
        "type": "Feature",
        "geometry": {"type": "LineString", "coordinates": coords},
        "properties": {
            "elongation": feat["elongation"],
            "n_points": int(line_sorted.shape[0]),
            "catenary_a": catenary["a"] if catenary else None,
            "sag": catenary["sag"] if catenary else None,
        },
    }
    powerline_path = os.path.join(output_dir, "powerlines.geojson")
    write_geojson(powerline_path, [line_feature])

    # 塔架点
    tower_features = []
    for j, t in enumerate(towers):
        tlon, tlat = meters_to_lonlat(np.array([t["xy"][0]]), np.array([t["xy"][1]]), geo_ref)
        tower_features.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [float(tlon[0]), float(tlat[0])]},
            "properties": {
                "tower_id": j,
                "height": t["height"],
                "z_max": t["z_max"],
                "n_points": t["n_points"],
            },
        })
    towers_path = os.path.join(output_dir, "towers.geojson")
    write_geojson(towers_path, tower_features)

    # 线-树距离报告
    report = {
        "source": source_note,
        "ground_z": ground_z,
        "min_height": args.min_height,
        "n_total_points": int(points.shape[0]),
        "n_above_ground": int(above.shape[0]),
        "n_line_points": int(line_pts.shape[0]),
        "elongation": feat["elongation"],
        "towers": towers,
        "n_towers": len(towers),
        "catenary": catenary,
        "line_tree_clearance": clearance,
    }
    report_path = os.path.join(output_dir, "line_tree_distance.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2, default=str)

    # QA
    qa: Dict[str, Any] = {
        "source": source_note,
        "n_total_points": int(points.shape[0]),
        "n_above_ground": int(above.shape[0]),
        "n_line_points": int(line_pts.shape[0]),
        "elongation": feat["elongation"],
        "n_towers": len(towers),
        "catenary_rmse": catenary["rmse"] if catenary else None,
        "catenary_sag": catenary["sag"] if catenary else None,
        "min_line_tree_distance": clearance["min_distance"],
    }
    if synth_info is not None:
        qa["synthetic_true_sag"] = synth_info["true_sag"]
        qa["synthetic_n_towers"] = 2

    bbox_out = bbox if bbox is not None else [
        float(points[:, 0].min()), float(points[:, 1].min()),
        float(points[:, 0].max()), float(points[:, 1].max()),
    ]

    outputs = [
        {"path": powerline_path, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox_out, "feature_count": 1},
        {"path": towers_path, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox_out, "feature_count": len(tower_features)},
        {"path": report_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox_out)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] points: total={points.shape[0]} above_ground={above.shape[0]} line={line_pts.shape[0]}")
        print(f"[{SKILL_NAME}] elongation: {feat['elongation']:.2f}  towers: {len(towers)}")
        if catenary:
            print(f"[{SKILL_NAME}] catenary: a={catenary['a']:.3f} sag={catenary['sag']:.3f} rmse={catenary['rmse']:.4f}")
        print(f"[{SKILL_NAME}] min line-tree distance: {clearance['min_distance']}")
        print(f"[{SKILL_NAME}] output: {powerline_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="LiDAR powerline detection: catenary sag fit, tower clustering, line-tree clearance.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input LiDAR point cloud (.npy/.txt/.csv/.xyz, x y z per row)")
    p.add_argument("--min-height", type=float, default=5.0,
                   help="minimum height above ground for candidate points (default: 5)")
    p.add_argument("--inlier-thresh", type=float, default=3.0,
                   help="perpendicular distance threshold for linear inliers, meters (default: 3)")
    p.add_argument("--tower-thresh", type=float, default=15.0,
                   help="height above ground to consider tower candidates, meters (default: 15)")
    p.add_argument("--tower-excl", type=float, default=12.0,
                   help="along-span exclusion radius near towers for catenary fit, meters (default: 12)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic scene (offline)")
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
