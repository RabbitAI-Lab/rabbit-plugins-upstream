#!/usr/bin/env python3
"""viewshed-analysis — 视域分析

基于 DEM 的视域（可视性）分析。对每个观察点，沿径向逐像元判断视线（line of
sight）是否被地形遮挡，并叠加地球曲率与大气折射修正。支持多观察点叠加，
输出可视次数栅格与二值可视栅格。

数据源：本地 DEM GeoTIFF，或 --synthetic 生成模拟地形。

隐私声明 / Privacy：
- 默认离线运行，不发起任何网络请求。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python viewshed-analysis.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "viewshed-analysis"

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


EARTH_RADIUS_M = 6371000.0
# 等效地球半径系数（大气折射 k≈0.13 → 有效半径系数 ~ 1/(1-k)）
REFRACTION_COEF = 0.13


def validate_bbox(bbox):
    """Validate WGS-84 bbox. Returns (W, S, E, N) as floats.

    Rules:
      - 4 numeric values
      - -180 <= W, E <= 180; -90 <= S, N <= 90
      - W < E (no crossing of antimeridian; split into two bboxes if needed)
      - S < N
      - width / height strictly positive
    Raises ValidationError (exit 6) on any failure.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(f"bbox must be 4 floats [W S E N], got: {bbox}")
    w, s, e, n = (float(v) for v in bbox)
    for label, val, lo, hi in (("W", w, -180.0, 180.0), ("E", e, -180.0, 180.0),
                               ("S", s, -90.0, 90.0), ("N", n, -90.0, 90.0)):
        if val < lo or val > hi:
            raise ValidationError(
                f"bbox {label}={val} out of range [{lo}, {hi}]; got bbox={bbox}"
            )
    if w >= e:
        raise ValidationError(
            f"bbox W={w} must be < E={e} (no antimeridian crossing; "
            f"if needed, split into two bboxes)"
        )
    if s >= n:
        raise ValidationError(
            f"bbox S={s} must be < N={n}"
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero or negative area: width={e - w:.3e}, height={n - s:.3e}"
        )
    return w, s, e, n


def validate_observer_height(h):
    """Observer height must be a finite non-negative float (meters)."""
    try:
        f = float(h)
    except (TypeError, ValueError):
        raise ValidationError(f"observer-height must be numeric, got: {h!r}")
    if f != f or f in (float("inf"), float("-inf")):
        raise ValidationError(f"observer-height must be finite, got: {f}")
    if f < 0:
        raise ValidationError(
            f"observer-height must be >= 0 (meters above ground), got: {f}"
        )
    return f


def validate_grid_size(g):
    """Grid size must be a positive integer."""
    try:
        n = int(g)
    except (TypeError, ValueError):
        raise ValidationError(f"grid-size must be an integer, got: {g!r}")
    if n < 4:
        raise ValidationError(f"grid-size must be >= 4, got: {n}")
    return n


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def curvature_correction(distance_m: np.ndarray, k: float = REFRACTION_COEF) -> np.ndarray:
    """地球曲率 + 大气折射的高度修正（米）。

    drop = d^2 / (2 * R_eff)，R_eff = R / (1 - k)。
    从目标高程中减去该值以模拟视线下降。
    """
    R_eff = EARTH_RADIUS_M / (1.0 - k)
    return (distance_m ** 2) / (2.0 * R_eff)


def viewshed_single(
    dem: np.ndarray,
    observer_rc: Tuple[int, int],
    observer_height: float = 2.0,
    cell_size_m: float = 30.0,
    curvature: bool = True,
    k: float = REFRACTION_COEF,
) -> np.ndarray:
    """单观察点视域分析（基于最大仰角递推）。

    Parameters
    ----------
    dem : (H, W) 高程栅格（米）
    observer_rc : (row, col) 观察点像元
    observer_height : 观察点离地高度（米）
    cell_size_m : 像元地面尺寸（米）
    curvature : 是否做地球曲率/折射修正

    Returns (H, W) bool 可视栅格。
    """
    h, w = dem.shape
    orow, ocol = observer_rc
    if not (0 <= orow < h and 0 <= ocol < w):
        raise ValidationError(f"observer {observer_rc} out of raster bounds")
    z_obs = dem[orow, ocol] + observer_height
    visible = np.zeros((h, w), dtype=bool)
    visible[orow, ocol] = True

    # 沿 8 个主方向 + 细分射线扫描，逐像元判断
    # 采用逐像元仰角法：从观察点向外遍历每个像元，计算到观察点的最大仰角
    rows, cols = np.mgrid[0:h, 0:w]
    dr = rows - orow
    dc = cols - ocol
    dist_cells = np.sqrt(dr ** 2 + dc ** 2)
    dist_m = dist_cells * cell_size_m

    # 视线仰角（考虑曲率修正后的目标高程）
    target_z = dem.astype(np.float64)
    if curvature:
        target_z = target_z - curvature_correction(dist_m, k)
    dz = target_z - z_obs
    with np.errstate(divide="ignore", invalid="ignore"):
        angle = np.arctan2(dz, np.where(dist_m > 0, dist_m, 1.0))
    angle[orow, ocol] = -np.inf

    # 逐射线追踪：按角度分 bin，每个 bin 内按距离排序递推最大仰角
    theta = np.arctan2(dr, dc)
    n_bins = max(int(2 * np.pi * max(h, w)), 64)
    bins = np.linspace(-np.pi, np.pi, n_bins + 1)
    bin_idx = np.clip(np.digitize(theta.ravel(), bins) - 1, 0, n_bins - 1)
    flat_dist = dist_cells.ravel()
    flat_angle = angle.ravel()

    visible_flat = np.zeros(h * w, dtype=bool)
    visible_flat[orow * w + ocol] = True
    order_all = np.argsort(flat_dist, kind="stable")
    for b in range(n_bins):
        idx = order_all[bin_idx[order_all] == b]
        if idx.size == 0:
            continue
        max_ang = -np.inf
        for p in idx:
            if flat_dist[p] < 0.5:
                visible_flat[p] = True
                continue
            if flat_angle[p] > max_ang:
                visible_flat[p] = True
                max_ang = flat_angle[p]
    return visible_flat.reshape(h, w)


def viewshed_multi(
    dem: np.ndarray,
    observers: List[Tuple[int, int]],
    observer_height: float = 2.0,
    cell_size_m: float = 30.0,
    curvature: bool = True,
) -> Tuple[np.ndarray, np.ndarray]:
    """多观察点叠加。

    Returns (count_grid 可视次数, visible_any 二值可视)。
    """
    h, w = dem.shape
    count = np.zeros((h, w), dtype=np.int32)
    for obs in observers:
        vis = viewshed_single(dem, obs, observer_height, cell_size_m, curvature)
        count += vis.astype(np.int32)
    return count, count > 0


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], grid_size: int = 48, seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成合成 DEM：一个中央山峰 + 起伏地形。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:grid_size, 0:grid_size]
    yyf = yy / grid_size
    xxf = xx / grid_size
    # 中央山峰
    peak = 800.0 * np.exp(-((xxf - 0.5) ** 2 + (yyf - 0.5) ** 2) / 0.05)
    # 缓起伏背景
    bg = 200.0 + 100.0 * np.sin(xxf * 6.0) * np.cos(yyf * 5.0)
    noise = rng.normal(0, 5, (grid_size, grid_size))
    dem = (peak + bg + noise).astype(np.float32)
    info = {"grid_size": grid_size, "elev_range": [float(dem.min()), float(dem.max())]}
    return dem, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if array.ndim == 2:
        array = array[np.newaxis, ...]
    if array.ndim != 3:
        raise ValidationError("write_geotiff expects a 2D or 3D array")
    nb, hh, ww = array.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], ww, hh)
    profile = {
        "driver": "GTiff", "height": hh, "width": ww, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(array[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], np.ndarray]:
    """Read a single-band DEM raster, replacing NoData with NaN.

    Returns (array_2D, bbox, valid_mask).  All values identified as NoData
    (either by the file's nodata metadata or by NaN in the data) become NaN
    in the array and False in the mask.  If the raster has multiple bands, the
    first band is used.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        if src.count < 1:
            raise ValidationError(f"input raster has 0 bands: {path}")
        data = src.read(1).astype(np.float64)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    valid_mask = np.isfinite(data)
    if nodata is not None:
        try:
            valid_mask &= (data != float(nodata))
        except (TypeError, ValueError):
            pass
    data = np.where(valid_mask, data, np.nan).astype(np.float32)
    return data, bbox, valid_mask


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

    # ---- P0/P1: validate bbox, grid-size, observer-height BEFORE mkdir ----
    if bbox is not None:
        bbox = list(validate_bbox(bbox))
    args.grid_size = validate_grid_size(args.grid_size)
    args.observer_height = validate_observer_height(args.observer_height)

    os.makedirs(output_dir, exist_ok=True)

    if args.input and not args.synthetic:
        data, file_bbox, valid_mask = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            # Also validate file bbox (so --input without --bbox is checked too)
            bbox = list(validate_bbox(bbox))
        dem = data
        n_valid_pixels = int(valid_mask.sum())
        if n_valid_pixels < 9:
            raise ValidationError(
                f"input DEM has insufficient valid pixels: {n_valid_pixels}; "
                f"need at least 9 (3x3)"
            )
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        dem, _ = generate_synthetic(bbox, grid_size=args.grid_size)
        n_valid_pixels = int(np.isfinite(dem).sum()) if np.issubdtype(dem.dtype, np.floating) else dem.size
        source_note = "synthetic"

    if dem.size < 9:
        raise ValidationError("DEM too small for viewshed")
    gs = args.grid_size
    if dem.shape[0] != gs or dem.shape[1] != gs:
        from scipy.ndimage import zoom
        dem = zoom(dem, (gs / dem.shape[0], gs / dem.shape[1]), order=1).astype(np.float32)

    h, w = dem.shape
    # 像元地面尺寸（近似，按纬度缩放经度方向）
    lat0 = (bbox[1] + bbox[3]) / 2.0
    dx_m = (bbox[2] - bbox[0]) * 111320.0 * np.cos(np.deg2rad(lat0)) / w
    dy_m = (bbox[3] - bbox[1]) * 110540.0 / h
    cell_size_m = float(np.sqrt(dx_m * dy_m))

    # 观察点：默认中心 + 四角内侧
    observers = _parse_observers(args.observers, h, w)

    count, visible_any = viewshed_multi(
        dem, observers, observer_height=args.observer_height,
        cell_size_m=cell_size_m, curvature=args.curvature,
    )
    pct = 100.0 * visible_any.mean()

    out_vis = os.path.join(output_dir, "viewshed.tif")
    write_geotiff(out_vis, visible_any.astype(np.float32), bbox)
    out_cnt = os.path.join(output_dir, "viewshed_count.tif")
    write_geotiff(out_cnt, count.astype(np.float32), bbox)
    stats_path = os.path.join(output_dir, "viewshed_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump({"n_observers": len(observers), "visible_pct": float(pct),
                   "cell_size_m": cell_size_m, "curvature": bool(args.curvature)},
                  f, ensure_ascii=False, indent=2)

    qa = {
        "source": source_note,
        "n_observers": len(observers),
        "visible_pct": float(pct),
        "cell_size_m": cell_size_m,
    }
    outputs = [
        {"path": out_vis, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_cnt, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] observers: {len(observers)}  cell: {cell_size_m:.1f} m")
        print(f"[{SKILL_NAME}] visible area: {pct:.1f}%")
        print(f"[{SKILL_NAME}] output: {out_vis}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def _parse_observers(spec: Optional[str], h: int, w: int) -> List[Tuple[int, int]]:
    """解析观察点。格式 'row,col;row,col' 或 None（用默认布局）。"""
    if not spec:
        return [(h // 2, w // 2), (h // 4, w // 4), (3 * h // 4, 3 * w // 4)]
    obs = []
    for part in spec.split(";"):
        part = part.strip()
        if not part:
            continue
        r, c = part.split(",")
        obs.append((int(r), int(c)))
    if not obs:
        raise UsageError("no valid observers in --observers")
    for r, c in obs:
        if not (0 <= r < h and 0 <= c < w):
            raise UsageError(f"observer ({r},{c}) out of bounds for grid {h}x{w}")
    return obs


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="DEM-based viewshed analysis with curvature correction and multi-observer overlay.",
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input DEM GeoTIFF")
    p.add_argument("--grid-size", type=int, default=48, help="working grid size (default: 48)")
    p.add_argument("--observer-height", type=float, default=2.0, help="observer height (m, default: 2)")
    p.add_argument("--observers", default=None, help="observers as 'row,col;row,col' (default: auto)")
    p.add_argument("--curvature", action="store_true", help="apply earth curvature + refraction correction")
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
