#!/usr/bin/env python3
"""water-table-mapping — 地下水位空间制图

由离散监测井点（x, y, 水位）经空间插值生成区域地下水位栅格与埋深栅格。
核心内容：

- **IDW（反距离加权）**：像元值 = Σ(value_i / d_i^p) / Σ(1 / d_i^p)，稳健快速。
- **简化普通克里金（Ordinary Kriging）**：指数型变异函数，求解带无偏约束的
  克里金方程组，给出最优线性无偏估计（BLUE）。
- **地形约束**：地下水位不得高于地表高程（水位 = min(水位, DEM)）。
- **留一法交叉验证**：逐点剔除、用其余点插值，统计 RMSE / MAE / R²。

输入：本地 CSV（列含 x/lon, y/lat, level/water_level）+ 可选 DEM；或
``--synthetic`` 生成带空间渐变与噪声的井点 + 真值场用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，无网络访问。``--synthetic`` 完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python water-table-mapping.py --bbox 116 39 117 40 --synthetic --method idw
    python water-table-mapping.py --bbox 116 39 117 40 --method kriging --synthetic

License: MIT
"""
from __future__ import annotations

import argparse
import csv
import datetime as _dt
import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "water-table-mapping"

# ---- 复用共享核心库（本地 vendored）----
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
# 核心算法 1：变异函数与 IDW 插值
# ---------------------------------------------------------------------------
def exponential_variogram(h: np.ndarray, sill: float, range_a: float, nugget: float = 0.0) -> np.ndarray:
    """指数型变异函数 γ(h) = nugget + sill·(1 − exp(−3h/range))。"""
    h = np.asarray(h, dtype=np.float64)
    range_a = max(float(range_a), 1e-9)
    return nugget + sill * (1.0 - np.exp(-3.0 * h / range_a))


def _pairwise_distances(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """两组点间欧氏距离矩阵 (na, nb)。"""
    return np.sqrt(((a[:, None, :] - b[None, :, :]) ** 2).sum(axis=2))


def idw_interpolate(
    points: np.ndarray, values: np.ndarray, targets: np.ndarray, power: float = 2.0,
) -> np.ndarray:
    """反距离加权插值。points (n,2), values (n,), targets (m,2) → (m,)。

    若目标点与某已知点重合，直接取该点值（避免除零）。
    """
    pts = np.asarray(points, dtype=np.float64)
    vals = np.asarray(values, dtype=np.float64)
    tgt = np.asarray(targets, dtype=np.float64)
    if pts.shape[0] != vals.size:
        raise ValidationError("points/values count mismatch")
    if pts.shape[0] == 0:
        raise ValidationError("no points to interpolate")
    d = _pairwise_distances(tgt, pts)  # (m, n)
    eps = 1e-12
    on_point = d < eps
    w = np.where(on_point, 0.0, 1.0 / np.power(np.maximum(d, eps), power))
    wsum = w.sum(axis=1)
    out = (w * vals[None, :]).sum(axis=1) / np.where(wsum > 0, wsum, 1.0)
    hit = np.any(on_point, axis=1)
    if np.any(hit):
        nearest = np.argmin(d[hit], axis=1)
        out[hit] = vals[nearest]
    return out.astype(np.float64)


# ---------------------------------------------------------------------------
# 核心算法 2：简化普通克里金
# ---------------------------------------------------------------------------
def fit_variogram_params(
    points: np.ndarray, values: np.ndarray, n_bins: int = 10,
) -> Tuple[float, float]:
    """由点对半方差粗略估计变异函数的 sill 与 range。

    返回 (sill, range)。sill 取实验半方差的高分位值，range 取达到 ~95% sill
    的滞后距离（不足则用最大滞后的 1/3）。
    """
    pts = np.asarray(points, dtype=np.float64)
    vals = np.asarray(values, dtype=np.float64)
    n = pts.shape[0]
    if n < 4:
        return float(np.var(vals) + 1e-9), 1.0
    d = _pairwise_distances(pts, pts)
    iu = np.triu_indices(n, k=1)
    dists = d[iu]
    half_sq = 0.5 * (vals[:, None] - vals[None, :]) ** 2
    semivar = half_sq[iu]
    if dists.size == 0 or dists.max() <= 0:
        return float(np.var(vals) + 1e-9), 1.0
    max_d = float(dists.max())
    edges = np.linspace(0.0, max_d, n_bins + 1)
    gamma = []
    centers = []
    for k in range(n_bins):
        mask = (dists >= edges[k]) & (dists < edges[k + 1])
        if mask.any():
            gamma.append(float(semivar[mask].mean()))
            centers.append(0.5 * (edges[k] + edges[k + 1]))
    if not gamma:
        return float(np.var(vals) + 1e-9), max_d / 3.0
    gamma = np.array(gamma)
    centers = np.array(centers)
    sill = float(np.percentile(gamma, 90)) + 1e-9
    # range：首次达到 0.95·sill 的滞后
    reached = centers[gamma >= 0.95 * sill]
    range_a = float(reached[0]) if reached.size else max_d / 3.0
    return sill, max(range_a, 1e-6)


def ordinary_kriging(
    points: np.ndarray, values: np.ndarray, targets: np.ndarray,
    sill: float, range_a: float, nugget: float = 0.0,
) -> np.ndarray:
    """简化普通克里金（指数变异函数，带无偏约束）。

    求解 (n+1)×(n+1) 克里金方程组得到每个目标点的最优权重。
    points (n,2), values (n,), targets (m,2) → (m,)。
    """
    pts = np.asarray(points, dtype=np.float64)
    vals = np.asarray(values, dtype=np.float64)
    tgt = np.asarray(targets, dtype=np.float64)
    n = pts.shape[0]
    if n == 0:
        raise ValidationError("no points to krig")
    if pts.shape[0] != vals.size:
        raise ValidationError("points/values count mismatch")

    # 数据点间协方差矩阵 C = sill - γ
    d_nn = _pairwise_distances(pts, pts)
    C = sill - exponential_variogram(d_nn, sill, range_a, nugget)
    # 增广矩阵（无偏约束 λ）
    A = np.ones((n + 1, n + 1), dtype=np.float64)
    A[:n, :n] = C
    A[n, n] = 0.0
    # 数值稳定：对角微扰
    A[:n, :n] += np.eye(n) * (sill * 1e-8 + 1e-9)

    d_tn = _pairwise_distances(tgt, pts)  # (m, n)
    c0 = sill - exponential_variogram(d_tn, sill, range_a, nugget)  # (m, n)
    m = tgt.shape[0]
    b = np.ones((n + 1, m), dtype=np.float64)
    b[:n, :] = c0.T
    try:
        w = np.linalg.solve(A, b)  # (n+1, m)
    except np.linalg.LinAlgError as exc:
        raise ProcessError("kriging system singular") from exc
    est = vals @ w[:n, :]
    return est.astype(np.float64)


# ---------------------------------------------------------------------------
# 核心算法 3：留一法交叉验证
# ---------------------------------------------------------------------------
def interpolate_at(
    train_pts: np.ndarray, train_vals: np.ndarray, targets: np.ndarray,
    method: str, sill: float, range_a: float, power: float = 2.0,
) -> np.ndarray:
    if method == "idw":
        return idw_interpolate(train_pts, train_vals, targets, power=power)
    if method == "kriging":
        return ordinary_kriging(train_pts, train_vals, targets, sill, range_a)
    raise UsageError(f"unknown method '{method}'. Choose from: idw, kriging", method=method)


def leave_one_out_cv(
    points: np.ndarray, values: np.ndarray, method: str, power: float = 2.0,
) -> Dict[str, float]:
    """留一法交叉验证，返回 RMSE / MAE / R²。"""
    pts = np.asarray(points, dtype=np.float64)
    vals = np.asarray(values, dtype=np.float64)
    n = pts.shape[0]
    if n < 3:
        raise ValidationError("need >= 3 points for leave-one-out CV")
    sill, range_a = fit_variogram_params(pts, vals)
    pred = np.zeros(n, dtype=np.float64)
    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        pred[i] = interpolate_at(pts[mask], vals[mask], pts[i:i + 1], method, sill, range_a)[0]
    err = pred - vals
    rmse = float(np.sqrt(np.mean(err ** 2)))
    mae = float(np.mean(np.abs(err)))
    ss_res = float(np.sum(err ** 2))
    ss_tot = float(np.sum((vals - vals.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 1e-12 else 0.0
    return {"rmse": rmse, "mae": mae, "r2": r2, "n_points": int(n), "method": method,
            "sill": sill, "range": range_a}


# ---------------------------------------------------------------------------
# 合成数据：井点（空间渐变 + 噪声）+ 真值场 + DEM
# ---------------------------------------------------------------------------
def truth_field(bbox: List[float], grid_shape: Tuple[int, int]) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """真值地下水位场（平面渐变 + 轻微弯曲）与对应 DEM（水位之上）。

    返回 (level_field, dem_field, xs, ys 的 mesh)。level < dem 处处成立。
    """
    H, W = int(grid_shape[0]), int(grid_shape[1])
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float64)
    xxn = xx / max(W - 1, 1)
    yyn = yy / max(H - 1, 1)
    # 地下水位：从西北（高）向东南（低）渐变
    level = 45.0 - 12.0 * xxn - 8.0 * yyn + 1.5 * np.sin(3.0 * np.pi * xxn)
    # 地表 DEM：水位之上，起伏更大
    dem = level + 6.0 + 4.0 * xxn + 2.0 * np.sin(2.0 * np.pi * yyn)
    return level.astype(np.float32), dem.astype(np.float32)


def generate_synthetic(
    bbox: List[float], n_wells: int = 40, grid_shape: Tuple[int, int] = (64, 64),
    noise: float = 0.3, seed: int = 42,
) -> Dict[str, Any]:
    """在真值场上随机布井并加观测噪声，得到井点水位样本。"""
    rng = np.random.default_rng(seed)
    H, W = grid_shape
    level_field, dem_field = truth_field(bbox, grid_shape)
    w, s, e, n = bbox
    xs = rng.uniform(w, e, n_wells)
    ys = rng.uniform(s, n, n_wells)
    # 从真值场采样井点水位（双线性近似：最近像元）
    col = np.clip(((xs - w) / max(e - w, 1e-9) * (W - 1)).round().astype(int), 0, W - 1)
    row = np.clip(((n - ys) / max(n - s, 1e-9) * (H - 1)).round().astype(int), 0, H - 1)
    levels = level_field[row, col] + rng.normal(0, noise, n_wells)
    points = np.stack([xs, ys], axis=1)
    return {
        "bbox": list(bbox),
        "grid_shape": (H, W),
        "points": points,
        "levels": levels.astype(np.float64),
        "level_field": level_field,
        "dem": dem_field,
    }


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
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


def _grid_targets(bbox: List[float], grid_shape: Tuple[int, int]) -> np.ndarray:
    H, W = grid_shape
    w, s, e, n = bbox
    xs = np.linspace(w, e, W)
    ys = np.linspace(n, s, H)
    gx, gy = np.meshgrid(xs, ys)
    return np.stack([gx.ravel(), gy.ravel()], axis=1)


# ---------------------------------------------------------------------------
# 井点 CSV 读取
# ---------------------------------------------------------------------------
_LEVEL_KEYS = ("level", "water_level", "head", "gwl", "value", "z")
_X_KEYS = ("x", "lon", "lng", "longitude", "easting")
_Y_KEYS = ("y", "lat", "latitude", "northing")


def read_wells_csv(path: str) -> Tuple[np.ndarray, np.ndarray]:
    """读取井点 CSV，自动识别坐标列与水位列。返回 (points (n,2), values (n,))。"""
    if not os.path.exists(path):
        raise UsageError(f"input CSV not found: {path}", path=path)
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = [c.strip().lower() for c in (reader.fieldnames or [])]
        xk = next((c for c in fields if c in _X_KEYS), None)
        yk = next((c for c in fields if c in _Y_KEYS), None)
        lk = next((c for c in fields if c in _LEVEL_KEYS), None)
        if not (xk and yk and lk):
            raise ValidationError(
                "CSV must contain x/y/level columns",
                columns=fields,
            )
        # 映射回原始列名
        orig = {c.strip().lower(): c for c in reader.fieldnames}
        pts, vals = [], []
        for row in reader:
            try:
                x = float(row[orig[xk]])
                y = float(row[orig[yk]])
                v = float(row[orig[lk]])
            except (TypeError, ValueError, KeyError):
                continue
            if np.isfinite(x) and np.isfinite(y) and np.isfinite(v):
                pts.append([x, y])
                vals.append(v)
    if not pts:
        raise ValidationError("no valid well rows parsed from CSV")
    return np.array(pts, dtype=np.float64), np.array(vals, dtype=np.float64)


# ---------------------------------------------------------------------------
# 参数校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Optional[List[float]]) -> List[float]:
    """校验 [W, S, E, N]：W<E、S<N、范围合法；跨 180°给拆分提示。"""
    if bbox is None or len(bbox) != 4:
        raise UsageError(
            "bbox must be 4 floats [W S E N], got: " + repr(bbox),
            bbox=bbox,
        )
    w, s, e, n = bbox
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError(
            f"bbox must contain finite floats, got {bbox}", bbox=bbox)
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of [-180, 180]: W={w} E={e}", bbox=bbox)
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of [-90, 90]: S={s} N={n}", bbox=bbox)
    if s >= n:
        raise ValidationError(
            f"bbox South >= North: S={s} N={n}", bbox=bbox)
    if w > e:
        raise ValidationError(
            f"bbox crosses the 180° meridian (W={w} > E={e}); "
            f"please split the extent or wrap longitudes manually",
            bbox=bbox)
    if abs(e - w) < 1e-9 or abs(n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero area: W={w} E={e} S={s} N={n}", bbox=bbox)
    return [float(w), float(s), float(e), float(n)]


def validate_grid_size(n: int) -> int:
    """输出网格大小 NxN 必须 >= 2（1x1 退化为单点；0x0 写出空栅格）。"""
    try:
        v = int(n)
    except (TypeError, ValueError):
        raise ValidationError(f"grid-size must be int, got {n!r}")
    if v < 2:
        raise ValidationError(
            f"grid-size must be >= 2 (got {v}); use 0/1 produces degenerate output",
            grid_size=v)
    return v


def validate_n_wells(n: int) -> int:
    """井点数必须 >= 3（CV / IDW 最小有效样本）。"""
    try:
        v = int(n)
    except (TypeError, ValueError):
        raise ValidationError(f"n-wells must be int, got {n!r}")
    if v < 3:
        raise ValidationError(
            f"n-wells must be >= 3 (leave-one-out CV requirement), got {v}",
            n_wells=v)
    return v


def validate_power(p: float) -> float:
    """IDW 幂次必须 > 0（p<=0 权重定义退化）。"""
    try:
        v = float(p)
    except (TypeError, ValueError):
        raise ValidationError(f"power must be number, got {p!r}")
    if not np.isfinite(v):
        raise ValidationError(f"power must be finite, got {v}")
    if v <= 0.0:
        raise ValidationError(f"power must be > 0 (IDW exponent), got {v}", power=v)
    return v


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "method": getattr(args, "method", None),
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

    # 前置校验
    grid_size = validate_grid_size(args.grid_size)
    n_wells = validate_n_wells(args.n_wells)
    power = validate_power(args.power)
    bbox_in = list(args.bbox) if args.bbox else None
    grid_shape = (grid_size, grid_size)

    dem = None
    truth = None
    if args.input and not args.synthetic:
        points, values = read_wells_csv(args.input)
        source_note = args.input
        # CSV 模式：bbox 仅在显式给出时校验；否则从点云边界推断
        if bbox_in is not None:
            bbox = validate_bbox(bbox_in)
        else:
            bbox = validate_bbox([
                float(points[:, 0].min()), float(points[:, 1].min()),
                float(points[:, 0].max()), float(points[:, 1].max()),
            ])
    else:
        bbox = validate_bbox(bbox_in)
        synth = generate_synthetic(bbox, n_wells=n_wells, grid_shape=grid_shape, seed=args.seed)
        points = synth["points"]
        values = synth["levels"]
        dem = synth["dem"]
        truth = synth["level_field"]
        source_note = "synthetic"

    if points.shape[0] < 3:
        raise ValidationError("need >= 3 wells", n=int(points.shape[0]))

    # 校验通过后再创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 交叉验证
    cv = leave_one_out_cv(points, values, args.method, power=power)

    # 全场插值
    sill, range_a = cv["sill"], cv["range"]
    targets = _grid_targets(bbox, grid_shape)
    level_flat = interpolate_at(points, values, targets, args.method, sill, range_a, power)
    level_grid = level_flat.reshape(grid_shape).astype(np.float32)

    # 地形约束：水位 ≤ DEM
    if dem is not None and dem.shape == level_grid.shape:
        level_grid = np.minimum(level_grid, dem).astype(np.float32)

    # 埋深 = DEM − 水位（无 DEM 时用栅格自身最大值近似地表，给出相对埋深）
    if dem is not None and dem.shape == level_grid.shape:
        depth_grid = (dem - level_grid).astype(np.float32)
    else:
        surface = np.full_like(level_grid, float(np.nanmax(level_grid) + 5.0))
        depth_grid = (surface - level_grid).astype(np.float32)
    depth_grid = np.clip(depth_grid, 0.0, None)

    # 与真值对比（合成模式）
    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "n_wells": int(points.shape[0]),
        "cv_rmse": cv["rmse"],
        "cv_mae": cv["mae"],
        "cv_r2": cv["r2"],
        "mean_water_level": float(np.mean(level_grid)),
        "mean_depth_to_water": float(np.mean(depth_grid)),
    }
    if truth is not None and truth.shape == level_grid.shape:
        err = level_grid - truth
        qa["truth_rmse"] = float(np.sqrt(np.mean(err ** 2)))
        corr = float(np.corrcoef(level_grid.ravel(), truth.ravel())[0, 1])
        qa["truth_correlation"] = corr

    # 输出
    out_level = os.path.join(output_dir, "water_table.tif")
    write_geotiff(out_level, level_grid, bbox)
    out_depth = os.path.join(output_dir, "depth_to_water.tif")
    write_geotiff(out_depth, depth_grid, bbox)

    report = {"cross_validation": cv, "qa": qa, "bbox": bbox, "grid_shape": list(grid_shape)}
    report_path = os.path.join(output_dir, "interpolation_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": out_level, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_depth, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  method: {args.method}  wells: {points.shape[0]}")
        print(f"[{SKILL_NAME}] CV RMSE: {cv['rmse']:.4f}  R²: {cv['r2']:.4f}")
        if "truth_rmse" in qa:
            print(f"[{SKILL_NAME}] truth RMSE: {qa['truth_rmse']:.4f}  corr: {qa['truth_correlation']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_level}  {out_depth}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Spatial water-table mapping from wells via IDW / ordinary kriging.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input wells CSV (columns: x/lon, y/lat, level)")
    p.add_argument("--method", default="idw", choices=["idw", "kriging"],
                   help="interpolation method (default: idw)")
    p.add_argument("--power", type=float, default=2.0, help="IDW power (default: 2)")
    p.add_argument("--n-wells", type=int, default=40, help="synthetic well count (default: 40)")
    p.add_argument("--grid-size", type=int, default=64, help="output grid size N×N (default: 64)")
    p.add_argument("--seed", type=int, default=42, help="random seed (default: 42)")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic wells (offline)")
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
