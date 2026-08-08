#!/usr/bin/env python3
"""lidar-coastal-erosion — LiDAR 海岸侵蚀分析

基于两期 LiDAR 点云 / DSM 量化海岸侵蚀与堆积：

- **两期 DSM 差分**：分别把 t1、t2 点云栅格化为 DSM（IDW），相减得变化量，
  负值 = 侵蚀（地表降低），正值 = 堆积。
- **海岸线提取**：对每期 DSM 按高程阈值（默认 0，即平均海平面）逐沿岸列求
  零交叉并亚像元插值，得到海岸线位置折线。
- **EPR（端点变化率，End Point Rate）**：逐断面两期海岸线的水平距离差除以
  时间间隔，得到海岸后退/前进速率（m/yr）。

数据源：本地 LiDAR 点云（.npy/.txt/.csv/.xyz，每行 x y z），或使用 ``--synthetic``
生成两期海岸地形（t2 海岸线向陆后退，产生侵蚀）。

隐私声明 / Privacy：默认完全离线，不发起网络请求，所有处理本地完成。

Usage:
    python lidar-coastal-erosion.py --bbox 116 39 117 40 --output-dir ./out
    python lidar-coastal-erosion.py --input cloud_t1.xyz --dt 10 --output-dir ./out

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
SKILL_NAME = "lidar-coastal-erosion"

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


M_PER_DEG_LAT = 110540.0
MAX_DIM = 140


# ---------------------------------------------------------------------------
# 输入验证
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate WGS-84 bbox: W<E, S<N, lon∈[-180,180], lat∈[-90,90], nonzero area.

    Raises ValidationError (rc=6) on failure with a human-readable message.
    Bbox that crosses the antimeridian (E>180 after normalisation) is rejected
    with a hint to split into two requests — we do not auto-unwrap.
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
    """Validate numeric parameters: --dt>0, --resolution>0."""
    if not np.isfinite(args.dt):
        raise ValidationError(f"--dt must be finite, got {args.dt}")
    if args.dt <= 0:
        raise ValidationError(f"--dt must be > 0 years, got {args.dt}")
    if not np.isfinite(args.resolution):
        raise ValidationError(f"--resolution must be finite, got {args.resolution}")
    if args.resolution <= 0:
        raise ValidationError(f"--resolution must be > 0 meters, got {args.resolution}")
    return None


def meters_per_deg_lon(lat_deg: float) -> float:
    return 111320.0 * math.cos(math.radians(lat_deg))


def local_size_m(bbox: List[float]) -> Tuple[float, float, float]:
    W, S, E, N = bbox
    midlat = 0.5 * (S + N)
    width_m = (E - W) * meters_per_deg_lon(midlat)
    height_m = (N - S) * M_PER_DEG_LAT
    return float(width_m), float(height_m), float(midlat)


def grid_dims(bbox: List[float], resolution: float,
              max_dim: int = MAX_DIM) -> Tuple[int, int, float, float]:
    width_m, height_m, _ = local_size_m(bbox)
    res = max(float(resolution), 1e-3)
    n_cols = max(4, int(round(width_m / res)))
    n_rows = max(4, int(round(height_m / res)))
    longest = max(n_cols, n_rows)
    if longest > max_dim:
        scale = longest / float(max_dim)
        n_cols = max(4, int(round(n_cols / scale)))
        n_rows = max(4, int(round(n_rows / scale)))
    return n_cols, n_rows, float(width_m / n_cols), float(height_m / n_rows)


def grid_center_coords(bbox: List[float], n_cols: int, n_rows: int
                       ) -> Tuple[np.ndarray, np.ndarray]:
    """网格中心本地米制坐标：xs 向东，ys 向北（row0=北）。"""
    width_m, height_m, _ = local_size_m(bbox)
    xs = (np.arange(n_cols) + 0.5) * (width_m / n_cols)
    ys = height_m - (np.arange(n_rows) + 0.5) * (height_m / n_rows)
    return xs, ys


def local_to_lonlat(x_m: np.ndarray, y_m: np.ndarray,
                    bbox: List[float]) -> Tuple[np.ndarray, np.ndarray]:
    W, S, E, N = bbox
    width_m, height_m, midlat = local_size_m(bbox)
    lon = W + np.asarray(x_m, dtype=float) / width_m * (E - W)
    lat = S + np.asarray(y_m, dtype=float) / height_m * (N - S)
    return lon, lat


# ---------------------------------------------------------------------------
# 海岸地形模型（解析真值）
# ---------------------------------------------------------------------------
def coastline_x(x_c0: float, amp: float, y: np.ndarray, height_m: float) -> np.ndarray:
    """沿岸方向（y）的海岸线位置（含正弦起伏）。"""
    return x_c0 + amp * np.sin(2 * np.pi * np.asarray(y, dtype=float) / max(height_m, 1e-6))


def terrain_elevation(
    x: np.ndarray, y: np.ndarray, x_c0: float, width_m: float, height_m: float,
    relief: float = 12.0, trans_frac: float = 0.03, amp_frac: float = 0.03,
) -> np.ndarray:
    """海岸地形高程：陆地在小 x 侧（正高程），海在大 x 侧（负高程）。

    elev = -relief * tanh((x - x_c(y)) / w)，海岸线（elev=0）位于 x_c(y)。
    x_c0 越小海岸线越靠陆（侵蚀后退）。
    """
    w = max(trans_frac * width_m, 1e-3)
    amp = amp_frac * width_m
    xc = coastline_x(x_c0, amp, y, height_m)
    return -relief * np.tanh((np.asarray(x, dtype=float) - xc) / w)


# ---------------------------------------------------------------------------
# 点云栅格化（IDW）
# ---------------------------------------------------------------------------
def idw_rasterize(points: np.ndarray, nodes_xy: np.ndarray,
                  k: int = 12, power: float = 2.0) -> np.ndarray:
    from scipy.spatial import cKDTree

    k = min(k, points.shape[0])
    tree = cKDTree(points[:, :2])
    d, idx = tree.query(nodes_xy, k=k)
    if k == 1:
        d = d[:, None]
        idx = idx[:, None]
    z = points[idx, 2]
    w = 1.0 / (d ** power + 1e-9)
    out = np.sum(w * z, axis=1) / np.sum(w, axis=1)
    coincident = d[:, 0] < 1e-6
    if np.any(coincident):
        out[coincident] = points[idx[coincident, 0], 2]
    return out


def points_to_dsm(points: np.ndarray, bbox: List[float],
                  resolution: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float, float]:
    """点云 → DSM 栅格。返回 (dsm[n_rows,n_cols], xs, ys, res_x, res_y)。"""
    n_cols, n_rows, res_x, res_y = grid_dims(bbox, resolution)
    xs, ys = grid_center_coords(bbox, n_cols, n_rows)
    XX, YY = np.meshgrid(xs, ys)
    nodes = np.column_stack([XX.ravel(), YY.ravel()])
    dsm = idw_rasterize(points, nodes).reshape(n_rows, n_cols).astype(np.float32)
    return dsm, xs, ys, res_x, res_y


# ---------------------------------------------------------------------------
# 海岸线提取（逐列高程阈值零交叉 + 亚像元插值）
# ---------------------------------------------------------------------------
def extract_coastline(
    dsm: np.ndarray, xs: np.ndarray, ys: np.ndarray, threshold: float = 0.0
) -> Tuple[np.ndarray, np.ndarray]:
    """逐沿岸行（row）求海岸线 x 位置（陆 elev>阈 → 海 elev<阈 的零交叉）。

    返回 (xc[n_rows], y_valid=ys)；无交叉的行 xc=NaN。
    """
    n_rows = dsm.shape[0]
    xc = np.full(n_rows, np.nan, dtype=float)
    s = dsm - threshold
    for r in range(n_rows):
        row = s[r, :]
        # 找从 + (陆) 到 - (海) 的首个交叉（x 增大方向）
        cross = np.where((row[:-1] >= 0) & (row[1:] < 0))[0]
        if cross.size == 0:
            continue
        i = int(cross[0])
        denom = row[i] - row[i + 1]
        if abs(denom) < 1e-9:
            f = 0.5
        else:
            f = row[i] / denom
        xc[r] = xs[i] + f * (xs[i + 1] - xs[i])
    return xc, ys


def coastline_feature(xc: np.ndarray, ys: np.ndarray, bbox: List[float],
                      epoch: str, threshold: float) -> Dict[str, Any]:
    """把海岸线数组转为 GeoJSON LineString 要素（剔除 NaN 行）。"""
    valid = np.isfinite(xc)
    lon, lat = local_to_lonlat(xc[valid], ys[valid], bbox)
    coords = [[float(lon[i]), float(lat[i])] for i in range(lon.size)]
    return {
        "type": "Feature",
        "geometry": {"type": "LineString", "coordinates": coords},
        "properties": {
            "epoch": epoch,
            "threshold": threshold,
            "n_points": int(valid.sum()),
        },
    }


# ---------------------------------------------------------------------------
# EPR 端点变化率
# ---------------------------------------------------------------------------
def compute_epr(
    xc_t1: np.ndarray, xc_t2: np.ndarray, dt_years: float
) -> Dict[str, Any]:
    """逐断面海岸线变化与 EPR。

    后退距离 = xc_t1 - xc_t2（x 向海增大，向陆减小；正 = 向陆后退 = 侵蚀）。
    EPR = 距离 / dt (m/yr)。
    """
    valid = np.isfinite(xc_t1) & np.isfinite(xc_t2)
    if not np.any(valid):
        raise ValidationError("no overlapping coastline transects for EPR")
    retreat = xc_t1[valid] - xc_t2[valid]   # 正 = 向陆后退
    dt = max(float(dt_years), 1e-6)
    epr = retreat / dt
    return {
        "n_transects": int(valid.sum()),
        "mean_retreat_m": float(np.mean(retreat)),
        "max_retreat_m": float(np.max(retreat)),
        "min_retreat_m": float(np.min(retreat)),
        "mean_epr_m_per_yr": float(np.mean(epr)),
        "max_epr_m_per_yr": float(np.max(epr)),
        "frac_eroding": float(np.mean(retreat > 0)),
        "dt_years": float(dt_years),
    }


def erosion_volume(diff: np.ndarray, res_x: float, res_y: float) -> Dict[str, Any]:
    """统计侵蚀/堆积体积（m³）。diff<0 为侵蚀。"""
    cell_area = res_x * res_y
    erosion = np.where(diff < 0, -diff, 0.0)
    accretion = np.where(diff > 0, diff, 0.0)
    return {
        "erosion_volume_m3": float(np.sum(erosion) * cell_area),
        "accretion_volume_m3": float(np.sum(accretion) * cell_area),
        "net_volume_m3": float(np.sum(diff) * cell_area),
        "max_erosion_depth_m": float(-np.min(diff)) if np.any(diff < 0) else 0.0,
        "max_accretion_height_m": float(np.max(diff)) if np.any(diff > 0) else 0.0,
        "mean_change_m": float(np.mean(diff)),
        "n_erosion_cells": int(np.sum(diff < 0)),
        "n_accretion_cells": int(np.sum(diff > 0)),
    }


# ---------------------------------------------------------------------------
# 合成点云（两期）
# ---------------------------------------------------------------------------
def generate_synthetic_points(
    bbox: List[float], x_c0_frac: float, resolution: float,
    n_points: int, rng: np.random.Generator,
    relief: float = 12.0, trans_frac: float = 0.03, amp_frac: float = 0.03,
) -> np.ndarray:
    width_m, height_m, _ = local_size_m(bbox)
    x = rng.uniform(0, width_m, n_points)
    y = rng.uniform(0, height_m, n_points)
    z = terrain_elevation(x, y, x_c0_frac * width_m, width_m, height_m,
                          relief, trans_frac, amp_frac)
    z = z + rng.normal(0, 0.05, n_points)
    return np.column_stack([x, y, z]).astype(np.float32)


def generate_synthetic(
    bbox: List[float], resolution: float, seed: int = 42
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成两期点云：t1 海岸线在 0.55*width，t2 后退到 0.50*width（侵蚀）。"""
    rng = np.random.default_rng(seed)
    width_m, height_m, _ = local_size_m(bbox)
    n_cols, n_rows, res_x, res_y = grid_dims(bbox, resolution)
    n_points = int(min(25000, max(8000, n_cols * n_rows)))
    pts_t1 = generate_synthetic_points(bbox, 0.55, resolution, n_points,
                                       np.random.default_rng(seed))
    pts_t2 = generate_synthetic_points(bbox, 0.50, resolution, n_points,
                                       np.random.default_rng(seed + 1))
    info = {
        "bbox": bbox, "width_m": width_m, "height_m": height_m,
        "n_points": n_points, "grid": [n_cols, n_rows],
        "xc_t1_frac": 0.55, "xc_t2_frac": 0.50,
        "true_retreat_m": 0.05 * width_m,
        "relief_m": 12.0,
    }
    return pts_t1, pts_t2, info


# ---------------------------------------------------------------------------
# 点云 I/O
# ---------------------------------------------------------------------------
def read_pointcloud(path: str) -> np.ndarray:
    if not os.path.exists(path):
        raise UsageError(f"input point cloud not found: {path}", path=path)
    try:
        if path.lower().endswith(".npy"):
            arr = np.load(path)
        else:
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
            f"point cloud needs >=3 columns, got {arr.shape[1]}", columns=int(arr.shape[1])
        )
    finite = np.isfinite(arr[:, :3]).all(axis=1)
    arr = arr[finite, :3]
    if arr.shape[0] == 0:
        raise ValidationError("point cloud has no valid points")
    return arr


def points_to_local_meters(points: np.ndarray, bbox: List[float]) -> np.ndarray:
    minx, maxx = points[:, 0].min(), points[:, 0].max()
    miny, maxy = points[:, 1].min(), points[:, 1].max()
    geographic = abs(minx) <= 180 and abs(maxx) <= 180 and abs(miny) <= 90 \
        and abs(maxy) <= 90 and (maxx - minx) < 90 and (maxy - miny) < 90
    if not geographic:
        return points
    midlat = 0.5 * (miny + maxy)
    out = points.copy()
    out[:, 0] = (points[:, 0] - bbox[0]) * meters_per_deg_lon(midlat)
    out[:, 1] = (points[:, 1] - bbox[1]) * M_PER_DEG_LAT
    return out


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path, array, bbox, nodata=-9999.0):
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
            "dt_years": getattr(args, "dt", None),
            "threshold": getattr(args, "threshold", None),
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

    # ---- 1. 参数验证（先于任何 makedirs / 数据读取）----
    if args.input is None and bbox is None:
        raise UsageError("provide --bbox (synthetic mode) or --input <pointcloud>")
    if args.input:
        # input path must exist
        if not os.path.exists(args.input):
            raise UsageError(f"input point cloud not found: {args.input}", path=args.input)
    validate_params(args)
    # bbox is validated only after we know it (or after deriving from input)

    # ---- 2. 读取输入（可能推导 bbox）----
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        pts_t1_raw = read_pointcloud(args.input)
        if bbox is None:
            bbox = [float(pts_t1_raw[:, 0].min()), float(pts_t1_raw[:, 1].min()),
                    float(pts_t1_raw[:, 0].max()), float(pts_t1_raw[:, 1].max())]
        # Now validate the bbox (user-provided or derived)
        validate_bbox(bbox)
        pts_t1 = points_to_local_meters(pts_t1_raw, bbox)
        # t2：以输入范围建模一个向陆后退的海岸（单期输入 → 模型化变化）
        width_m, height_m, _ = local_size_m(bbox)
        rng = np.random.default_rng(0)
        n_cols, n_rows, _, _ = grid_dims(bbox, args.resolution)
        n_pts = int(min(25000, max(8000, n_cols * n_rows)))
        pts_t2 = generate_synthetic_points(bbox, 0.50, args.resolution, n_pts,
                                           np.random.default_rng(1))
        source_note = args.input
    else:
        validate_bbox(bbox)
        pts_t1, pts_t2, synth_info = generate_synthetic(bbox, args.resolution)
        source_note = "synthetic"

    # ---- 3. 全部验证已通过，创建输出目录 ----
    os.makedirs(output_dir, exist_ok=True)

    # 两期 DSM
    dsm_t1, xs, ys, res_x, res_y = points_to_dsm(pts_t1, bbox, args.resolution)
    dsm_t2, _, _, _, _ = points_to_dsm(pts_t2, bbox, args.resolution)
    diff = (dsm_t2 - dsm_t1).astype(np.float32)   # 负 = 侵蚀

    # 海岸线
    xc_t1, _ = extract_coastline(dsm_t1, xs, ys, threshold=args.threshold)
    xc_t2, _ = extract_coastline(dsm_t2, xs, ys, threshold=args.threshold)
    epr = compute_epr(xc_t1, xc_t2, args.dt)
    vol = erosion_volume(diff, res_x, res_y)

    # 输出
    diff_path = os.path.join(output_dir, "elevation_change.tif")
    write_geotiff(diff_path, diff, bbox)

    feat_t1 = coastline_feature(xc_t1, ys, bbox, "t1", args.threshold)
    feat_t2 = coastline_feature(xc_t2, ys, bbox, "t2", args.threshold)
    change_path = os.path.join(output_dir, "coastline_change.geojson")
    with open(change_path, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": [feat_t1, feat_t2]},
                  f, ensure_ascii=False, indent=2)

    rates = {
        "source": source_note,
        "dt_years": args.dt,
        "threshold": args.threshold,
        "grid": [int(dsm_t1.shape[1]), int(dsm_t1.shape[0])],
        "resolution_m": [res_x, res_y],
        "epr": epr,
        "volume": vol,
    }
    if synth_info is not None:
        rates["synthetic_true_retreat_m"] = synth_info["true_retreat_m"]
    rates_path = os.path.join(output_dir, "erosion_rates.json")
    with open(rates_path, "w", encoding="utf-8") as f:
        json.dump(rates, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_diff_pixels": int(diff.size),
        "n_erosion_pixels": int(np.sum(diff < 0)),
        "n_accretion_pixels": int(np.sum(diff > 0)),
        "n_unchanged_pixels": int(np.sum(diff == 0)),
        "n_valid_transects": int(epr["n_transects"]),
        "mean_retreat_m": epr["mean_retreat_m"],
        "mean_epr_m_per_yr": epr["mean_epr_m_per_yr"],
        "erosion_volume_m3": vol["erosion_volume_m3"],
        "net_volume_m3": vol["net_volume_m3"],
        "frac_eroding": epr["frac_eroding"],
    }
    if synth_info is not None:
        qa["synthetic_true_retreat_m"] = synth_info["true_retreat_m"]

    outputs = [
        {"path": diff_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "resolution_m": res_x},
        {"path": change_path, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": 2},
        {"path": rates_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  dt: {args.dt} yr")
        print(f"[{SKILL_NAME}] grid: {dsm_t1.shape[1]}x{dsm_t1.shape[0]}  res: {res_x:.2f}x{res_y:.2f} m")
        print(f"[{SKILL_NAME}] mean retreat: {epr['mean_retreat_m']:.2f} m  mean EPR: {epr['mean_epr_m_per_yr']:.3f} m/yr")
        print(f"[{SKILL_NAME}] erosion vol: {vol['erosion_volume_m3']:.0f} m³  net vol: {vol['net_volume_m3']:.0f} m³")
        print(f"[{SKILL_NAME}] output: {diff_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="LiDAR coastal erosion: two-epoch DSM differencing, coastline extraction, EPR rates.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input LiDAR point cloud for epoch t1 (.npy/.txt/.csv/.xyz)")
    p.add_argument("--dt", type=float, default=10.0,
                   help="time interval between epochs in years (default: 10)")
    p.add_argument("--threshold", type=float, default=0.0,
                   help="elevation threshold for coastline (default: 0 = mean sea level)")
    p.add_argument("--resolution", type=float, default=1.0,
                   help="DSM cell size in meters (default: 1.0; capped by grid limit)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate two synthetic coastal epochs (offline)")
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
