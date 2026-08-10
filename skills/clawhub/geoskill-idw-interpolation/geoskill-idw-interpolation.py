#!/usr/bin/env python3
"""idw-interpolation — 反距离权重插值

对离散采样点执行反距离权重（Inverse Distance Weighting, IDW）空间插值，
生成连续栅格表面。支持幂参数调节、搜索半径限制和最近邻域搜索。

数据源：本地 GeoTIFF 点采样栅格，或使用 --synthetic 生成模拟采样点。

隐私声明 / Privacy：
- 默认离线运行，不发起任何网络请求。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python idw-interpolation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
    python idw-interpolation.py --input points.tif --power 2 --output-dir ./out

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
SKILL_NAME = "idw-interpolation"


# ---------------------------------------------------------------------------
# 校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate geographic bbox. Raise ValidationError -> exit 6.

    Rules:
        - 4 floats, W<S, W<=E, S<=N,  -180<=W,E<=180,  -90<=S,N<=90
        - width/height > 1e-9 (non-degenerate)
    Anti-meridian wrap (W>E) is not supported: clearly error out, do not silently
    wrap or produce garbage.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats [W S E N]")
    try:
        W, S, E, N = [float(v) for v in bbox]
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox values must be numeric: {bbox}") from exc
    if not (-180.0 <= W <= 180.0 and -180.0 <= E <= 180.0):
        raise ValidationError(f"bbox lon out of range [-180,180]: W={W} E={E}")
    if not (-90.0 <= S <= 90.0 and -90.0 <= N <= 90.0):
        raise ValidationError(f"bbox lat out of range [-90,90]: S={S} N={N}")
    if W >= E:
        raise ValidationError(
            f"bbox W>=E ({W}>={E}); crossing 180° not supported, please split"
        )
    if S >= N:
        raise ValidationError(f"bbox S>=N ({S}>={N})")
    if (E - W) < 1e-9 or (N - S) < 1e-9:
        raise ValidationError("bbox has zero or negative area")


def validate_idw_params(power, neighbors) -> None:
    """Validate IDW parameter ranges. Raise ValidationError -> exit 6."""
    if power is None:
        raise ValidationError("--power is required")
    try:
        power = float(power)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"--power must be numeric: {power}") from exc
    if not (power > 0.0):
        raise ValidationError(f"--power must be > 0 (got {power})")
    if neighbors is not None:
        try:
            neighbors = int(neighbors)
        except (TypeError, ValueError) as exc:
            raise ValidationError(f"--neighbors must be int: {neighbors}") from exc
        if neighbors < 1:
            raise ValidationError(f"--neighbors must be >= 1 (got {neighbors})")


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
# 核心算法
# ---------------------------------------------------------------------------
def idw_interpolate(
    points_xy: np.ndarray,
    values: np.ndarray,
    grid_x: np.ndarray,
    grid_y: np.ndarray,
    power: float = 2.0,
    max_distance: Optional[float] = None,
    n_neighbors: Optional[int] = None,
) -> np.ndarray:
    """IDW 插值核心。

    Parameters
    ----------
    points_xy : (N, 2) 已知点坐标
    values : (N,) 已知点值
    grid_x, grid_y : (H, W) 目标网格坐标
    power : 距离幂参数
    max_distance : 搜索半径（None 表示不限）
    n_neighbors : 最近邻个数（None 表示使用全部）

    Returns
    -------
    (H, W) 插值结果
    """
    if points_xy.shape[0] == 0:
        raise ValidationError("no input points for interpolation")
    if points_xy.shape[0] != values.shape[0]:
        raise ValidationError("points and values length mismatch")

    h, w = grid_x.shape
    result = np.zeros((h, w), dtype=np.float64)

    pts_flat_x = grid_x.ravel()
    pts_flat_y = grid_y.ravel()
    n_pts = pts_flat_x.shape[0]

    for i in range(n_pts):
        dx = points_xy[:, 0] - pts_flat_x[i]
        dy = points_xy[:, 1] - pts_flat_y[i]
        dist = np.sqrt(dx * dx + dy * dy)

        # 搜索半径过滤
        if max_distance is not None:
            mask = dist <= max_distance
            if not np.any(mask):
                # 无邻域点时使用最近点
                mask = np.zeros_like(dist, dtype=bool)
                mask[np.argmin(dist)] = True
        else:
            mask = np.ones(len(dist), dtype=bool)

        # 最近邻过滤
        if n_neighbors is not None:
            valid_idx = np.where(mask)[0]
            if len(valid_idx) > n_neighbors:
                sub_dist = dist[valid_idx]
                top_k = np.argsort(sub_dist)[:n_neighbors]
                new_mask = np.zeros_like(mask)
                new_mask[valid_idx[top_k]] = True
                mask = new_mask

        d = dist[mask]
        v = values[mask]

        # 精确命中（距离为0）
        zero_mask = d < 1e-12
        if np.any(zero_mask):
            result.flat[i] = v[zero_mask][0]
        else:
            weights = 1.0 / np.power(d, power)
            result.flat[i] = np.sum(weights * v) / np.sum(weights)

    return result


def idw_grid_vectorized(
    points_xy: np.ndarray,
    values: np.ndarray,
    grid_x: np.ndarray,
    grid_y: np.ndarray,
    power: float = 2.0,
    n_neighbors: Optional[int] = None,
) -> np.ndarray:
    """向量化 IDW（无搜索半径限制时更快）。"""
    if points_xy.shape[0] == 0:
        raise ValidationError("no input points for interpolation")

    h, w = grid_x.shape
    n = points_xy.shape[0]
    gx = grid_x.ravel()
    gy = grid_y.ravel()
    m = gx.shape[0]

    # (m, n) 距离矩阵
    dx = gx[:, None] - points_xy[:, 0][None, :]
    dy = gy[:, None] - points_xy[:, 1][None, :]
    dist = np.sqrt(dx * dx + dy * dy)

    if n_neighbors is not None and n_neighbors < n:
        # 只保留 k 个最近邻
        idx = np.argpartition(dist, n_neighbors, axis=1)[:, :n_neighbors]
        mask = np.zeros((m, n), dtype=bool)
        mask[np.arange(m)[:, None], idx] = True
        dist_masked = np.where(mask, dist, np.inf)
    else:
        dist_masked = dist

    # 精确命中处理
    exact = dist_masked < 1e-12
    has_exact = exact.any(axis=1)

    with np.errstate(divide="ignore"):
        weights = np.where(dist_masked > 1e-12, 1.0 / np.power(dist_masked, power), 0.0)
    # 对精确命中的行，只保留精确点权重
    for row in np.where(has_exact)[0]:
        weights[row, :] = 0.0
        weights[row, exact[row]] = 1.0

    w_sum = weights.sum(axis=1)
    w_sum = np.where(w_sum < 1e-30, 1.0, w_sum)
    result = (weights * values[None, :]).sum(axis=1) / w_sum

    return result.reshape(h, w)


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    n_points: int = 50,
    grid_size: int = 64,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成合成采样点和目标网格。

    Returns: (points_xy, values, grid_x, grid_y, info)
    """
    rng = np.random.default_rng(seed)
    w, s, e, n = bbox
    # 随机采样点
    px = rng.uniform(w, e, n_points)
    py = rng.uniform(s, n, n_points)
    points_xy = np.column_stack([px, py])
    # 值：用简单空间趋势 + 噪声
    values = 2.0 * (px - w) / max(e - w, 1e-9) + 3.0 * (py - s) / max(n - s, 1e-9)
    values = values + rng.normal(0, 0.1, n_points)

    # 目标网格
    gx_1d = np.linspace(w, e, grid_size)
    gy_1d = np.linspace(n, s, grid_size)  # 从北到南
    grid_x, grid_y = np.meshgrid(gx_1d, gy_1d)

    info = {
        "n_points": n_points,
        "grid_size": grid_size,
        "value_range": [float(values.min()), float(values.max())],
    }
    return points_xy, values, grid_x, grid_y, info


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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """Read a raster; return (data, bbox, nodata). nodata is None if unset.

    Replaces raster's declared nodata values with NaN for clean downstream
    masking.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        data = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None and np.isfinite(nodata):
        for i in range(data.shape[0]):
            band = data[i]
            data[i] = np.where(band == nodata, np.nan, band)
    return data, bbox, nodata


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

    # Validate bbox and parameters BEFORE creating output directory.
    if bbox is not None:
        validate_bbox(bbox)
    validate_idw_params(args.power, args.neighbors)

    os.makedirs(output_dir, exist_ok=True)

    if args.input and not args.synthetic:
        data, file_bbox, file_nodata = read_geotiff(args.input)
        # If user didn't pass --bbox, use file's bbox; otherwise validate the
        # provided bbox (we already did). For input mode, sanity check that
        # the file bbox itself is sane.
        if bbox is None:
            validate_bbox(file_bbox)
            bbox = file_bbox
        # 从栅格中提取非 nodata 点作为采样
        h, w = data.shape[-2], data.shape[-1]
        band = data[0] if data.ndim == 3 else data
        yy, xx = np.mgrid[0:h, 0:w]
        # 坐标转换
        from rasterio.transform import from_bounds
        t = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
        xs = t.c * xx + t.a * yy + t.a * 0.5 + t.c * 0.5
        ys = t.f * yy + t.d * xx + t.d * 0.5 + t.f * 0.5
        # data has been NaN'd for declared nodata; also exclude non-finite.
        valid = np.isfinite(band)
        if not np.any(valid):
            raise ValidationError(
                f"no valid (non-nodata) pixels in input raster "
                f"(nodata={file_nodata})"
            )
        points_xy = np.column_stack([xs[valid], ys[valid]])
        values = band[valid].astype(np.float64)
        grid_x_1d = np.linspace(bbox[0], bbox[2], w)
        grid_y_1d = np.linspace(bbox[3], bbox[1], h)
        grid_x, grid_y = np.meshgrid(grid_x_1d, grid_y_1d)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        points_xy, values, grid_x, grid_y, _ = generate_synthetic(bbox)
        source_note = "synthetic"

    if points_xy.shape[0] == 0:
        raise ValidationError("no valid data points found")

    result = idw_grid_vectorized(
        points_xy, values, grid_x, grid_y,
        power=args.power,
        n_neighbors=args.neighbors,
    )

    out_tif = os.path.join(output_dir, "idw_result.tif")
    write_geotiff(out_tif, result, bbox)

    qa = {
        "source": source_note,
        "n_points": int(points_xy.shape[0]),
        "power": args.power,
        "n_neighbors": args.neighbors,
        "result_min": float(result.min()),
        "result_max": float(result.max()),
        "result_mean": float(result.mean()),
    }
    if args.input and not args.synthetic:
        qa["input_nodata"] = file_nodata
    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] points: {points_xy.shape[0]}  power: {args.power}")
        print(f"[{SKILL_NAME}] result range: [{result.min():.4f}, {result.max():.4f}]")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Inverse Distance Weighting (IDW) spatial interpolation.",
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF raster")
    p.add_argument("--power", type=float, default=2.0, help="IDW power parameter (default: 2)")
    p.add_argument("--neighbors", type=int, default=None,
                   help="number of nearest neighbors (default: all)")
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
