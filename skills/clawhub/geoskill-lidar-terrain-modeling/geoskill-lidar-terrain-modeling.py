#!/usr/bin/env python3
"""lidar-terrain-modeling — LiDAR 精细地形建模

从 LiDAR 点云（N,3 的 xyz 数组）构建数字高程模型（DEM/DTM）并派生地形因子：

- **栅格化插值**：把离散点云插值到规则网格。
  - ``idw``：反距离加权（Inverse Distance Weighting），用 cKDTree 取 k 近邻，
    权重 1/d^p，稳健、无空洞。
  - ``tin``：不规则三角网，scipy.spatial.Delaunay 三角化 + 线性插值，凸包外
    用最近邻填补。
- **坡度 / 坡向**：用 numpy.gradient 计算 dz/dx、dz/dy，
  坡度 = arctan(√(gx²+gy²))，坡向为最陡下降方向的罗盘角（北=0，顺时针）。

数据源：本地 LiDAR 点云（.npy/.txt/.csv/.xyz，每行 x y z），或使用 ``--synthetic``
生成平滑正弦叠加地形的模拟点云（含解析真值，用于精度评估）。

隐私声明 / Privacy：默认完全离线，不发起网络请求，所有处理本地完成。

Usage:
    python lidar-terrain-modeling.py --bbox 116 39 117 40 --resolution 1.0 --method idw --output-dir ./out
    python lidar-terrain-modeling.py --input cloud.xyz --method tin --output-dir ./out

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
SKILL_NAME = "lidar-terrain-modeling"

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
MAX_DIM = 160  # 合成/栅格化网格单边上限（保证测试快速）


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
    """Validate numeric parameters: --resolution>0."""
    if not np.isfinite(args.resolution):
        raise ValidationError(f"--resolution must be finite, got {args.resolution}")
    if args.resolution <= 0:
        raise ValidationError(f"--resolution must be > 0 meters, got {args.resolution}")
    return None


def meters_per_deg_lon(lat_deg: float) -> float:
    return 111320.0 * math.cos(math.radians(lat_deg))


def local_size_m(bbox: List[float]) -> Tuple[float, float, float]:
    """返回 (width_m, height_m, midlat)。"""
    W, S, E, N = bbox
    midlat = 0.5 * (S + N)
    width_m = (E - W) * meters_per_deg_lon(midlat)
    height_m = (N - S) * M_PER_DEG_LAT
    return float(width_m), float(height_m), float(midlat)


def grid_dims(
    bbox: List[float], resolution: float, max_dim: int = MAX_DIM
) -> Tuple[int, int, float, float]:
    """计算网格维度与实际分辨率，超限时放大分辨率以封顶网格尺寸。"""
    width_m, height_m, _ = local_size_m(bbox)
    res = max(float(resolution), 1e-3)
    n_cols = max(2, int(round(width_m / res)))
    n_rows = max(2, int(round(height_m / res)))
    longest = max(n_cols, n_rows)
    if longest > max_dim:
        scale = longest / float(max_dim)
        n_cols = max(2, int(round(n_cols / scale)))
        n_rows = max(2, int(round(n_rows / scale)))
    res_x = width_m / n_cols
    res_y = height_m / n_rows
    return n_cols, n_rows, float(res_x), float(res_y)


def grid_nodes(
    bbox: List[float], n_cols: int, n_rows: int
) -> Tuple[np.ndarray, np.ndarray, float, float]:
    """返回网格中心坐标 (xs 向东, ys 向北 row0=北) 与分辨率。"""
    width_m, height_m, _ = local_size_m(bbox)
    res_x = width_m / n_cols
    res_y = height_m / n_rows
    xs = (np.arange(n_cols) + 0.5) * res_x
    ys = height_m - (np.arange(n_rows) + 0.5) * res_y  # row0 在北
    return xs, ys, res_x, res_y


# ---------------------------------------------------------------------------
# 解析地形（合成真值）
# ---------------------------------------------------------------------------
def terrain_z(
    x_m: np.ndarray, y_m: np.ndarray, width_m: float, height_m: float
) -> np.ndarray:
    """平滑正弦叠加地形，解析可求值，便于精度评估。"""
    x = np.asarray(x_m, dtype=float)
    y = np.asarray(y_m, dtype=float)
    z = (
        100.0
        + 20.0 * np.sin(2 * np.pi * 2 * x / max(width_m, 1e-6))
        + 15.0 * np.cos(2 * np.pi * 3 * y / max(height_m, 1e-6))
        + 10.0 * np.sin(2 * np.pi * (x + y) / max(width_m, 1e-6))
    )
    return z


# ---------------------------------------------------------------------------
# 插值：IDW / TIN
# ---------------------------------------------------------------------------
def idw_interpolate(
    points: np.ndarray, nodes_xy: np.ndarray, k: int = 12, power: float = 2.0
) -> np.ndarray:
    """反距离加权插值：对每个网格节点取 k 近邻加权平均。"""
    from scipy.spatial import cKDTree

    if points.shape[0] < k:
        k = max(1, points.shape[0])
    tree = cKDTree(points[:, :2])
    d, idx = tree.query(nodes_xy, k=k)
    if k == 1:
        d = d[:, None]
        idx = idx[:, None]
    z = points[idx, 2]
    eps = 1e-9
    w = 1.0 / (d ** power + eps)
    out = np.sum(w * z, axis=1) / np.sum(w, axis=1)
    # 与样本点几乎重合时直接取该点高程
    coincident = d[:, 0] < 1e-6
    if np.any(coincident):
        out[coincident] = points[idx[coincident, 0], 2]
    return out


def tin_interpolate(points: np.ndarray, nodes_xy: np.ndarray) -> np.ndarray:
    """TIN 线性插值（Delaunay），凸包外用最近邻填补。"""
    from scipy.spatial import Delaunay
    from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator

    tri = Delaunay(points[:, :2])
    interp = LinearNDInterpolator(tri, points[:, 2])
    out = interp(nodes_xy)
    nan_mask = np.isnan(out)
    if np.any(nan_mask):
        nearest = NearestNDInterpolator(points[:, :2], points[:, 2])
        out[nan_mask] = nearest(nodes_xy[nan_mask])
    return out


def rasterize(
    points: np.ndarray, bbox: List[float], resolution: float, method: str = "idw"
) -> Tuple[np.ndarray, int, int, float, float]:
    """把点云栅格化为 DEM。返回 (dem[n_rows,n_cols], n_cols, n_rows, res_x, res_y)。"""
    if points.shape[0] < 3:
        raise ValidationError(
            f"too few points to rasterize: {points.shape[0]}", n_points=int(points.shape[0])
        )
    n_cols, n_rows, res_x, res_y = grid_dims(bbox, resolution)
    xs, ys, _, _ = grid_nodes(bbox, n_cols, n_rows)
    XX, YY = np.meshgrid(xs, ys)
    nodes = np.column_stack([XX.ravel(), YY.ravel()])

    if method == "tin":
        dem_flat = tin_interpolate(points, nodes)
    elif method == "idw":
        dem_flat = idw_interpolate(points, nodes)
    else:
        raise UsageError(f"unknown method '{method}'", method=method)

    dem = dem_flat.reshape(n_rows, n_cols).astype(np.float32)
    return dem, n_cols, n_rows, res_x, res_y


def slope_aspect(
    dem: np.ndarray, res_x: float, res_y: float
) -> Tuple[np.ndarray, np.ndarray]:
    """由 DEM 计算坡度(度)与坡向(度，罗盘角，北=0 顺时针，平地=-1)。

    dem row0 = 北，行号向南增大；列号向东增大。
    """
    # gy: 对北坐标的导数 = -(对行号的导数)，因为行号向南增大
    d_row, d_col = np.gradient(dem.astype(float), res_y, res_x)
    gx = d_col                 # dz/d(east)
    gy = -d_row                # dz/d(north)
    slope_rad = np.arctan(np.hypot(gx, gy))
    slope_deg = np.degrees(slope_rad).astype(np.float32)

    aspect = np.degrees(np.arctan2(-gx, -gy))   # 最陡下降方向罗盘角
    aspect = (aspect + 360.0) % 360.0
    flat = slope_deg < 1e-3
    aspect = aspect.astype(np.float32)
    aspect[flat] = -1.0
    return slope_deg, aspect


# ---------------------------------------------------------------------------
# 合成点云
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float], resolution: float, seed: int = 42
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (N,3) 点云（本地米制），采样解析地形 + 噪声。"""
    rng = np.random.default_rng(seed)
    width_m, height_m, midlat = local_size_m(bbox)
    n_cols, n_rows, res_x, res_y = grid_dims(bbox, resolution)
    n_points = int(min(25000, max(6000, n_cols * n_rows)))
    x = rng.uniform(0, width_m, n_points)
    y = rng.uniform(0, height_m, n_points)
    z = terrain_z(x, y, width_m, height_m) + rng.normal(0, 0.05, n_points)
    points = np.column_stack([x, y, z]).astype(np.float32)
    info = {
        "bbox": bbox, "width_m": width_m, "height_m": height_m,
        "n_points": n_points, "grid": [n_cols, n_rows],
        "res": [res_x, res_y],
        "terrain_relief_m": float(np.ptp(terrain_z(
            np.array([0, width_m / 4]),
            np.array([0, height_m / 4]),
            width_m, height_m))),
    }
    return points, info


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
    """把经纬度点云转为以 bbox 西南角为原点的本地米制。若已是米制则原样返回。"""
    minx, maxx = points[:, 0].min(), points[:, 0].max()
    miny, maxy = points[:, 1].min(), points[:, 1].max()
    geographic = abs(minx) <= 180 and abs(maxx) <= 180 and abs(miny) <= 90 \
        and abs(maxy) <= 90 and (maxx - minx) < 90 and (maxy - miny) < 90
    if not geographic:
        return points
    midlat = 0.5 * (miny + maxy)
    kx = meters_per_deg_lon(midlat)
    ky = M_PER_DEG_LAT
    out = points.copy()
    out[:, 0] = (points[:, 0] - bbox[0]) * kx
    out[:, 1] = (points[:, 1] - bbox[1]) * ky
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


def read_geotiff(path):
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        arr = src.read(1).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return arr, bbox


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
            "method": getattr(args, "method", None),
            "resolution": getattr(args, "resolution", None),
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
        if bbox is None:
            bbox = [float(pts_raw[:, 0].min()), float(pts_raw[:, 1].min()),
                    float(pts_raw[:, 0].max()), float(pts_raw[:, 1].max())]
        points = points_to_local_meters(pts_raw, bbox)
        source_note = args.input
    else:
        validate_bbox(bbox)
        points, synth_info = generate_synthetic(bbox, args.resolution)
        source_note = "synthetic"

    # ---- 3. 全部验证已通过，创建输出目录 ----
    os.makedirs(output_dir, exist_ok=True)

    dem, n_cols, n_rows, res_x, res_y = rasterize(
        points, bbox, args.resolution, method=args.method
    )
    slope, aspect = slope_aspect(dem, res_x, res_y)

    # 输出
    dem_path = os.path.join(output_dir, "dem.tif")
    write_geotiff(dem_path, dem, bbox)
    slope_path = os.path.join(output_dir, "slope.tif")
    write_geotiff(slope_path, slope, bbox, nodata=-1.0)
    aspect_path = os.path.join(output_dir, "aspect.tif")
    write_geotiff(aspect_path, aspect, bbox, nodata=-1.0)

    stats = {
        "source": source_note, "method": args.method,
        "resolution_m": [res_x, res_y], "grid": [int(n_cols), int(n_rows)],
        "n_points": int(points.shape[0]),
        "dem": {
            "min": float(np.min(dem)), "max": float(np.max(dem)),
            "mean": float(np.mean(dem)), "std": float(np.std(dem)),
        },
        "slope_deg": {
            "mean": float(np.mean(slope)), "max": float(np.max(slope)),
        },
    }
    # 合成模式：DEM 与解析真值的 RMSE
    if synth_info is not None:
        xs, ys, _, _ = grid_nodes(bbox, n_cols, n_rows)
        XX, YY = np.meshgrid(xs, ys)
        truth = terrain_z(XX, YY, synth_info["width_m"], synth_info["height_m"])
        rmse = float(np.sqrt(np.mean((dem - truth) ** 2)))
        stats["dem_rmse_vs_truth_m"] = rmse

    stats_path = os.path.join(output_dir, "terrain_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note, "method": args.method,
        "grid": [int(n_cols), int(n_rows)],
        "dem_mean": float(np.mean(dem)),
        "slope_mean_deg": float(np.mean(slope)),
        "slope_max_deg": float(np.max(slope)),
    }
    if "dem_rmse_vs_truth_m" in stats:
        qa["dem_rmse_vs_truth_m"] = stats["dem_rmse_vs_truth_m"]

    outputs = [
        {"path": dem_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "resolution_m": res_x},
        {"path": slope_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "resolution_m": res_x},
        {"path": aspect_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "resolution_m": res_x},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  method: {args.method}")
        print(f"[{SKILL_NAME}] grid: {n_cols}x{n_rows}  res: {res_x:.2f}x{res_y:.2f} m")
        print(f"[{SKILL_NAME}] DEM: min={stats['dem']['min']:.2f} max={stats['dem']['max']:.2f} mean={stats['dem']['mean']:.2f}")
        print(f"[{SKILL_NAME}] slope: mean={stats['slope_deg']['mean']:.2f}° max={stats['slope_deg']['max']:.2f}°")
        if "dem_rmse_vs_truth_m" in stats:
            print(f"[{SKILL_NAME}] DEM RMSE vs truth: {stats['dem_rmse_vs_truth_m']:.4f} m")
        print(f"[{SKILL_NAME}] output: {dem_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="LiDAR terrain modeling: point cloud to DEM (IDW/TIN) with slope and aspect.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input LiDAR point cloud (.npy/.txt/.csv/.xyz, x y z per row)")
    p.add_argument("--resolution", type=float, default=1.0,
                   help="output DEM cell size in meters (default: 1.0; capped by grid limit)")
    p.add_argument("--method", default="idw", choices=["idw", "tin"],
                   help="interpolation method (default: idw)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic terrain point cloud (offline)")
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
