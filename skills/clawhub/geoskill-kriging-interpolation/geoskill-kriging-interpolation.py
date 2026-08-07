#!/usr/bin/env python3
"""kriging-interpolation — 克里金空间插值

对离散采样点执行普通克里金（Ordinary Kriging）空间插值。流程：
1. 计算经验半变异函数（experimental semivariogram）
2. 拟合球状模型（spherical model：nugget / sill / range）
3. 逐像元建立并求解克里金方程组（含 Lagrange 乘子）
4. leave-one-out 交叉验证（RMSE / ME）

数据源：本地 GeoTIFF 栅格采样，或 --synthetic 生成模拟点。

隐私声明 / Privacy：
- 默认离线运行，不发起任何网络请求。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python kriging-interpolation.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "kriging-interpolation"

# ---- 共享库（带 fallback）----
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
# 参数校验（前置）
# ---------------------------------------------------------------------------
def validate_bbox(bbox):
    """W/E 经度 ∈ [-180, 180]，S/N 纬度 ∈ [-90, 90]，W<E，S<N。

    跨 180° 经线不支持（按既定约定给拆分提示，不做环绕）。
    """
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise UsageError(f"bbox must be [W, S, E, N], got {bbox!r}")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range: W={w}, E={e}; must be in [-180, 180]")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range: S={s}, N={n}; must be in [-90, 90]")
    if w >= e:
        if w > e and abs(w - e) < 1.0 and w > 170.0:
            raise ValidationError(
                f"bbox crosses the antimeridian (W={w} > E={e}); "
                f"split into two sub-bboxes instead")
        raise ValidationError(
            f"bbox W must be < E; got W={w}, E={e}")
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N; got S={s}, N={n}")
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero area: W={w}, E={e}, S={s}, N={n}")
    return [w, s, e, n]


def validate_params(args):
    """参数域校验：--grid-size >= 2、--max-points >= 3、--n-lags >= 2。"""
    if args.grid_size < 2:
        raise ValidationError(
            f"--grid-size must be >= 2; got {args.grid_size}")
    if args.max_points < 3:
        raise ValidationError(
            f"--max-points must be >= 3 (need at least 3 points for kriging); got {args.max_points}")
    if args.n_lags < 2:
        raise ValidationError(
            f"--n-lags must be >= 2; got {args.n_lags}")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def empirical_semivariogram(
    coords: np.ndarray, values: np.ndarray, n_lags: int = 12,
    max_dist: Optional[float] = None,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """计算经验半变异函数。

    Returns (lag_centers, semivariance, pair_counts)。
    gamma(h) = 1/(2N) * sum (z_i - z_j)^2
    """
    n = coords.shape[0]
    if n < 2:
        raise ValidationError("need at least 2 points for semivariogram")
    if max_dist is None:
        # 取最大点对距离的一半作为有效范围
        dmax = np.sqrt(((coords[:, None, :] - coords[None, :, :]) ** 2).sum(-1)).max()
        max_dist = dmax * 0.5
    edges = np.linspace(0, max_dist, n_lags + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    gamma = np.zeros(n_lags)
    counts = np.zeros(n_lags, dtype=int)

    for i in range(n):
        d = np.sqrt(((coords[i + 1:] - coords[i]) ** 2).sum(-1))
        dz2 = (values[i + 1:] - values[i]) ** 2
        idx = np.searchsorted(edges, d, side="right") - 1
        valid = (idx >= 0) & (idx < n_lags)
        for j in np.where(valid)[0]:
            k = idx[j]
            gamma[k] += dz2[j]
            counts[k] += 1
    with np.errstate(invalid="ignore", divide="ignore"):
        gamma = np.where(counts > 0, gamma / (2.0 * counts), np.nan)
    return centers, gamma, counts


def spherical_model(h: np.ndarray, nugget: float, sill: float, rng: float) -> np.ndarray:
    """球状半变异模型。"""
    h = np.asarray(h, dtype=np.float64)
    out = np.full(h.shape, sill, dtype=np.float64)
    mask = (h > 0) & (h < rng)
    hr = h[mask] / rng
    out[mask] = nugget + (sill - nugget) * (1.5 * hr - 0.5 * hr ** 3)
    out[h <= 0] = 0.0
    out[h >= rng] = sill
    return out


def fit_semivariogram(
    lags: np.ndarray, gamma: np.ndarray,
) -> Dict[str, float]:
    """用最小二乘拟合球状模型参数 (nugget, sill, range)。"""
    valid = np.isfinite(gamma) & (lags > 0)
    if valid.sum() < 2:
        # 退化：用经验值兜底
        g = gamma[np.isfinite(gamma)]
        sill = float(g.max()) if g.size else 1.0
        return {"nugget": 0.0, "sill": max(sill, 1e-9), "range": float(lags.max())}
    x = lags[valid]
    y = gamma[valid]
    nugget0 = max(float(y.min()), 0.0)
    sill0 = float(y.max())
    range0 = float(x[np.argmax(y >= sill0 * 0.95)]) if np.any(y >= sill0 * 0.95) else float(x.max())
    range0 = max(range0, x.min() + 1e-9)

    from scipy.optimize import least_squares

    def resid(p):
        nug, sil, rng = p
        return spherical_model(x, nug, sil, rng) - y

    res = least_squares(
        resid, [nugget0, sill0, range0],
        bounds=([0.0, 1e-9, 1e-9], [sill0 * 2 + 1e-3, sill0 * 3 + 1e-3, x.max() * 3]),
        max_nfev=200,
    )
    nugget, sill, vrange = res.x
    return {"nugget": float(nugget), "sill": float(sill), "range": float(vrange)}


def ordinary_kriging(
    coords: np.ndarray, values: np.ndarray, target: np.ndarray,
    nugget: float, sill: float, vrange: float,
) -> Tuple[np.ndarray, np.ndarray]:
    """普通克里金插值。

    Parameters
    ----------
    coords : (N, 2)
    values : (N,)
    target : (M, 2) 预测点

    Returns (z_pred (M,), variance (M,))。
    """
    n = coords.shape[0]
    # 构建 (n+1)x(n+1) 克里金矩阵
    d = np.sqrt(((coords[:, None, :] - coords[None, :, :]) ** 2).sum(-1))
    A = np.zeros((n + 1, n + 1))
    A[:n, :n] = spherical_model(d, nugget, sill, vrange)
    A[n, :n] = 1.0
    A[:n, n] = 1.0
    A[n, n] = 0.0
    # 数值稳定：对角微扰
    A[:n, :n][np.diag_indices(n)] += 1e-10
    A_inv = np.linalg.pinv(A)

    m = target.shape[0]
    z_pred = np.zeros(m)
    variance = np.zeros(m)
    dt = np.sqrt(((target[:, None, :] - coords[None, :, :]) ** 2).sum(-1))
    C = spherical_model(dt, nugget, sill, vrange)  # (m, n)
    for i in range(m):
        b = np.zeros(n + 1)
        b[:n] = C[i]
        b[n] = 1.0
        w = A_inv @ b
        z_pred[i] = w[:n] @ values
        variance[i] = max(float(w @ b), 0.0)
    return z_pred, variance


def cross_validate(
    coords: np.ndarray, values: np.ndarray, nugget: float, sill: float, vrange: float,
) -> Dict[str, float]:
    """Leave-one-out 交叉验证，返回 RMSE / ME。"""
    n = coords.shape[0]
    errors = np.zeros(n)
    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        pred, _ = ordinary_kriging(
            coords[mask], values[mask], coords[i:i + 1], nugget, sill, vrange,
        )
        errors[i] = pred[0] - values[i]
    rmse = float(np.sqrt(np.mean(errors ** 2)))
    me = float(np.mean(errors))
    return {"rmse": rmse, "mean_error": me, "n": n}


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float], n_points: int = 40, seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成具有空间相关性的合成采样点（高斯随机场近似）。"""
    rng = np.random.default_rng(seed)
    w, s, e, n = bbox
    px = rng.uniform(w, e, n_points)
    py = rng.uniform(s, n, n_points)
    coords = np.column_stack([px, py])
    # 空间趋势 + 平滑随机场
    trend = (px - w) / max(e - w, 1e-9) + (py - s) / max(n - s, 1e-9)
    field = np.zeros(n_points)
    centers = rng.uniform([w, s], [e, n], (3, 2))
    for c in centers:
        field += np.exp(-((coords - c) ** 2).sum(-1) / (0.1 * max(e - w, n - s) ** 2))
    values = trend + 0.5 * field + rng.normal(0, 0.05, n_points)
    info = {"n_points": n_points, "value_range": [float(values.min()), float(values.max())]}
    return coords, values, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
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
        data = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return data, bbox


def read_geotiff_nodata(path: str) -> Optional[float]:
    """从 GeoTIFF 读 nodata 值（独立函数）。"""
    import rasterio
    with rasterio.open(path) as src:
        return src.nodata


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(
    output_dir: str, args: argparse.Namespace, outputs: List[Dict[str, Any]],
    qa: Dict[str, Any], started_at: str, exit_code: int, bbox: List[float],
) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None), "synthetic": bool(getattr(args, "synthetic", False))},
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

    # ---- 前置校验：参数 + bbox（必须先于 os.makedirs）----
    validate_params(args)
    if bbox is not None:
        bbox = validate_bbox(bbox)

    if args.input and not args.synthetic:
        data, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            bbox = validate_bbox(bbox)
        band = data[0] if data.ndim == 3 else data
        h, w = band.shape
        from rasterio.transform import from_bounds
        t = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
        cols, rows = np.meshgrid(np.arange(w), np.arange(h))
        xs = t.c * cols + t.a * rows + t.a * 0.5 + t.c * 0.5
        ys = t.f * rows + t.d * cols + t.d * 0.5 + t.f * 0.5
        # NoData 处理：用 src.nodata 替换为 NaN，全 NoData -> rc=6
        src_nodata = read_geotiff_nodata(args.input)
        if src_nodata is not None:
            band = np.where(band == src_nodata, np.nan, band).astype(np.float32)
        valid = np.isfinite(band)
        if not valid.any():
            raise ValidationError("all input pixels are NoData")
        coords = np.column_stack([xs[valid], ys[valid]])
        values = band[valid].astype(np.float64)
        # 降采样以控制计算量
        if coords.shape[0] > args.max_points:
            idx = np.random.default_rng(0).choice(coords.shape[0], args.max_points, replace=False)
            coords, values = coords[idx], values[idx]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        coords, values, _ = generate_synthetic(bbox, n_points=args.max_points)
        source_note = "synthetic"

    if coords.shape[0] < 3:
        raise ValidationError("need at least 3 points for kriging")

    # ---- 校验通过后再创建输出目录（避免失败时留空目录）----
    os.makedirs(output_dir, exist_ok=True)

    # 1) 经验半变异函数 + 拟合
    lags, gamma, counts = empirical_semivariogram(coords, values, n_lags=args.n_lags)
    params = fit_semivariogram(lags, gamma)
    nugget, sill, vrange = params["nugget"], params["sill"], params["range"]

    # 2) 目标网格
    gs = args.grid_size
    gx = np.linspace(bbox[0], bbox[2], gs)
    gy = np.linspace(bbox[3], bbox[1], gs)
    gx2, gy2 = np.meshgrid(gx, gy)
    target = np.column_stack([gx2.ravel(), gy2.ravel()])

    # 3) 克里金插值
    z_pred, variance = ordinary_kriging(coords, values, target, nugget, sill, vrange)
    z_grid = z_pred.reshape(gs, gs)
    var_grid = variance.reshape(gs, gs)

    # 4) 交叉验证
    cv = cross_validate(coords, values, nugget, sill, vrange)

    out_tif = os.path.join(output_dir, "kriging_result.tif")
    write_geotiff(out_tif, z_grid, bbox)
    var_tif = os.path.join(output_dir, "kriging_variance.tif")
    write_geotiff(var_tif, var_grid, bbox)
    params_path = os.path.join(output_dir, "variogram_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump({"variogram": params, "cross_validation": cv,
                   "lags": lags.tolist(), "gamma": [None if not np.isfinite(g) else float(g) for g in gamma]},
                  f, ensure_ascii=False, indent=2)

    qa = {
        "source": source_note,
        "n_points": int(coords.shape[0]),
        "variogram": params,
        "cross_validation": cv,
        "result_min": float(z_grid.min()),
        "result_max": float(z_grid.max()),
        "result_mean": float(z_grid.mean()),
    }
    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": var_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] variogram: nugget={nugget:.4f} sill={sill:.4f} range={vrange:.4f}")
        print(f"[{SKILL_NAME}] CV RMSE={cv['rmse']:.4f} ME={cv['mean_error']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Ordinary Kriging interpolation with semivariogram fitting and cross-validation.",
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF raster")
    p.add_argument("--grid-size", type=int, default=48, help="output grid size (default: 48)")
    p.add_argument("--max-points", type=int, default=40, help="max sample points (default: 40)")
    p.add_argument("--n-lags", type=int, default=12, help="number of variogram lags (default: 12)")
    p.add_argument("--synthetic", action="store_true", help="use synthetic data")
    p.add_argument("--output-dir", default="./output", help="output directory")
    p.add_argument("--quiet", action="store_true", help="suppress output")
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
