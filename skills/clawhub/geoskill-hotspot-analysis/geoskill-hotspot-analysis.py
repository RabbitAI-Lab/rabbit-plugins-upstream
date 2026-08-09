#!/usr/bin/env python3
"""hotspot-analysis — 热点分析

基于 Getis-Ord Gi* 统计量识别统计显著的热点（高值聚集）与冷点（低值聚集），
叠加核密度估计（KDE）与多尺度分析。输出 Gi* z 得分栅格、核密度栅格和显著性分级。

数据源：本地 GeoTIFF 栅格 / 点事件，或 --synthetic 生成模拟场。

隐私声明 / Privacy：
- 默认离线运行，不发起任何网络请求。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python hotspot-analysis.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "hotspot-analysis"

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
def distance_band_weights(coords: np.ndarray, bandwidth: float) -> np.ndarray:
    """距离带二元权重矩阵（含自身），未行标准化。"""
    from scipy.spatial import cKDTree
    n = coords.shape[0]
    tree = cKDTree(coords)
    W = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        idx = tree.query_ball_point(coords[i], bandwidth)
        W[i, idx] = 1.0
    return W


def gi_star_zscores(x: np.ndarray, W: np.ndarray) -> np.ndarray:
    """Getis-Ord Gi* z 得分（W 应含自身权重 w_ii）。

    Gi*_i = (sum_j w_ij x_j - Xbar * sum_j w_ij) /
            {S * [n sum_j w_ij^2 - (sum_j w_ij)^2] / (n-1)}^0.5
    """
    x = np.asarray(x, dtype=np.float64).ravel()
    n = x.shape[0]
    xbar = x.mean()
    S = np.sqrt((x ** 2).sum() / n - xbar ** 2)
    S = max(S, 1e-12)
    row_sum = W.sum(1)
    row_sq = (W ** 2).sum(1)
    num = W @ x - xbar * row_sum
    with np.errstate(invalid="ignore"):
        denom_term = (n * row_sq - row_sum ** 2) / max(n - 1, 1)
    denom_term = np.clip(denom_term, 0.0, None)
    den = S * np.sqrt(denom_term)
    den = np.where(den < 1e-12, 1e-12, den)
    return num / den


def classify_significance(z: np.ndarray, alpha: float = 0.05) -> np.ndarray:
    """将 z 得分分级为显著性类别。

    返回整型栅格：
    +3 热点 99% (z>2.58), +2 热点 95% (z>1.96), +1 热点 90% (z>1.65),
    0 不显著, -1/-2/-3 对应冷点。
    """
    from scipy.stats import norm
    zcrit = {3: norm.ppf(1 - 0.01 / 2), 2: norm.ppf(1 - 0.05 / 2), 1: norm.ppf(1 - 0.10 / 2)}
    out = np.zeros(z.shape, dtype=np.int32)
    out[z > zcrit[1]] = 1
    out[z > zcrit[2]] = 2
    out[z > zcrit[3]] = 3
    out[z < -zcrit[1]] = -1
    out[z < -zcrit[2]] = -2
    out[z < -zcrit[3]] = -3
    return out


def kernel_density(points_xy: np.ndarray, grid_x: np.ndarray, grid_y: np.ndarray,
                   bandwidth: float, weights: Optional[np.ndarray] = None) -> np.ndarray:
    """高斯核密度估计（2D）。

    Parameters
    ----------
    points_xy : (N, 2)
    grid_x, grid_y : (H, W)
    bandwidth : 核带宽
    weights : (N,) 可选点权重

    Returns (H, W) 密度栅格。
    """
    if points_xy.shape[0] == 0:
        raise ValidationError("no points for KDE")
    if weights is None:
        weights = np.ones(points_xy.shape[0])
    h, w = grid_x.shape
    gx = grid_x.ravel()
    gy = grid_y.ravel()
    m = gx.shape[0]
    density = np.zeros(m)
    norm_const = 1.0 / (2.0 * np.pi * bandwidth ** 2)
    for i in range(points_xy.shape[0]):
        dx = gx - points_xy[i, 0]
        dy = gy - points_xy[i, 1]
        k = np.exp(-(dx ** 2 + dy ** 2) / (2.0 * bandwidth ** 2))
        density += weights[i] * k
    density *= norm_const
    return density.reshape(h, w)


def multiscale_gi(x: np.ndarray, coords: np.ndarray,
                  bandwidths: List[float]) -> Dict[str, np.ndarray]:
    """多尺度 Gi*：在多个距离带尺度上计算 z 得分。"""
    result = {}
    for bw in bandwidths:
        W = distance_band_weights(coords, bw)
        z = gi_star_zscores(x, W)
        result[f"bw_{bw:.4f}"] = z
    return result


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], grid_size: int = 24, n_events: int = 300,
                       seed: int = 42) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成带热点的合成事件点和权重场。

    Returns (field (H,W), points_xy (N,2), info)。
    """
    rng = np.random.default_rng(seed)
    w, s, e, n = bbox
    # 场：两个高斯热点 + 背景
    yy, xx = np.mgrid[0:grid_size, 0:grid_size]
    yyf = yy / grid_size
    xxf = xx / grid_size
    field = (3.0 * np.exp(-((xxf - 0.3) ** 2 + (yyf - 0.3) ** 2) / 0.02)
             + 2.0 * np.exp(-((xxf - 0.7) ** 2 + (yyf - 0.7) ** 2) / 0.02)
             + rng.normal(0.2, 0.05, (grid_size, grid_size)))
    # 事件点：向热点聚集
    pts = []
    hot_centers = np.array([[w + 0.3 * (e - w), s + 0.7 * (n - s)],
                            [w + 0.7 * (e - w), s + 0.3 * (n - s)]])
    for _ in range(n_events):
        if rng.random() < 0.7:
            c = hot_centers[rng.integers(0, 2)]
            pt = c + rng.normal(0, 0.03 * max(e - w, n - s), 2)
        else:
            pt = rng.uniform([w, s], [e, n])
        pts.append(pt)
    points_xy = np.array(pts)
    info = {"grid_size": grid_size, "n_events": n_events}
    return field, points_xy, info


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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """Read a GeoTIFF and replace NoData values with NaN in-place.

    Returns (data (band,h,w) float32, bbox [W,S,E,N], nodata_value_or_None).
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
        data = np.where(data == nodata, np.nan, data)
    return data, bbox, nodata


def validate_bbox(bbox: Optional[List[float]], allow_none: bool = False) -> List[float]:
    """Validate a W,S,E,N bbox. Cross-180 / out-of-range / W>=E / S>=N -> ValidationError."""
    if bbox is None:
        if allow_none:
            return None  # type: ignore[return-value]
        raise ValidationError("bbox is required")
    if len(bbox) != 4:
        raise ValidationError(f"bbox must have 4 floats, got {len(bbox)}")
    w, s, e, n = bbox
    for v, name in zip([w, s, e, n], ["W", "S", "E", "N"]):
        if not isinstance(v, (int, float)) or not (-1e9 < v < 1e9):
            raise ValidationError(f"bbox {name}={v!r} not a finite number")
    if w == e or s == n:
        raise ValidationError(f"bbox has zero area: W={w} E={e} S={s} N={n}")
    if not (-180.0 <= w <= 180.0) or not (-180.0 <= e <= 180.0):
        raise ValidationError(f"bbox lon out of [-180,180]: W={w} E={e}")
    if not (-90.0 <= s <= 90.0) or not (-90.0 <= n <= 90.0):
        raise ValidationError(f"bbox lat out of [-90,90]: S={s} N={n}")
    if w > e:
        # Cross-dateline: W>170 (eastern) AND E<-170 (western) is wraparound
        if not (w > 170.0 and e < -170.0):
            raise ValidationError(
                f"bbox has W>E (minLon > maxLon): W={w} E={e} — "
                f"if crossing the dateline, split into two bboxes (e.g. "
                f"[{w}, {s}, 180, {n}] and [-180, {s}, {e}, {n}])"
            )
        # otherwise it IS a cross-dateline bbox, which this skill does not yet support
        raise ValidationError(
            f"bbox crosses the 180° dateline (W={w} E={e}); "
            f"split into two non-wrapping bboxes ([{w}, {s}, 180, {n}] and "
            f"[-180, {s}, {e}, {n}]) and run separately"
        )
    if s > n:
        raise ValidationError(f"bbox has S>N (minLat > maxLat): S={s} N={n}")
    return [float(w), float(s), float(e), float(n)]


def validate_params(bandwidth: float) -> float:
    """Validate optional CLI parameters. 0 means auto (allowed)."""
    if bandwidth is None:
        return 0.0
    if bandwidth < 0:
        raise ValidationError(f"--bandwidth must be >= 0 (0 = auto), got {bandwidth}")
    return float(bandwidth)


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

    # ---- 1. 参数验证 (前置：失败不创建 output_dir) ----
    bbox = list(args.bbox) if args.bbox else None
    if bbox is not None:
        bbox = validate_bbox(bbox)
    args.bandwidth = validate_params(getattr(args, "bandwidth", 0.0))

    # ---- 2. 数据获取 ----
    input_nodata: Optional[float] = None
    n_valid_input: int = 0
    n_total_input: int = 0

    if args.input and not args.synthetic:
        data, file_bbox, input_nodata = read_geotiff(args.input)
        # user bbox overrides file bbox
        bbox = bbox if bbox is not None else file_bbox
        bbox = validate_bbox(bbox)
        field_raw = data[0] if data.ndim == 3 else data
        # NaN mask BEFORE any further computation
        valid_mask = np.isfinite(field_raw)
        n_valid_input = int(valid_mask.sum())
        n_total_input = int(field_raw.size)
        if n_valid_input == 0:
            raise ValidationError(
                f"input raster has no valid (non-NoData) pixels "
                f"(nodata={input_nodata}, total={n_total_input})"
            )
        # fill NaN with 0 only for KDE/percentile (Gi* will be re-masked in QA)
        field_filled = np.where(valid_mask, field_raw, 0.0).astype(np.float64)
        h, w = field_filled.shape
        # 采样事件点（高值像元）
        from rasterio.transform import from_bounds
        t = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
        # use only valid pixels for the percentile threshold
        thr = float(np.percentile(field_filled[valid_mask], 80))
        rows, cols = np.where((field_filled >= thr) & valid_mask)
        if len(rows) > 0:
            xs = t.c * cols + t.a * rows + t.a * 0.5 + t.c * 0.5
            ys = t.f * rows + t.d * cols + t.d * 0.5 + t.f * 0.5
            points_xy = np.column_stack([xs, ys])
        else:
            points_xy = np.empty((0, 2))
        # Gi* still computes over filled field; mark NoData output later
        field = field_filled
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        field, points_xy, _ = generate_synthetic(bbox, grid_size=args.grid_size)
        source_note = "synthetic"
        n_valid_input = int(field.size)
        n_total_input = int(field.size)

    # ---- 3. 校验通过后创建 output_dir ----
    os.makedirs(output_dir, exist_ok=True)

    if field.size < 4:
        raise ValidationError("raster too small")
    gs = args.grid_size
    if field.shape[0] != gs or field.shape[1] != gs:
        from scipy.ndimage import zoom
        field = zoom(field, (gs / field.shape[0], gs / field.shape[1]), order=1)

    # Gi*：用像元中心坐标 + 距离带权重
    h, w = field.shape
    gx = np.linspace(bbox[0], bbox[2], w)
    gy = np.linspace(bbox[3], bbox[1], h)
    gxx, gyy = np.meshgrid(gx, gy)
    coords = np.column_stack([gxx.ravel(), gyy.ravel()])
    x = field.ravel()
    bw = args.bandwidth if args.bandwidth > 0 else (bbox[2] - bbox[0]) / gs * 1.5
    W = distance_band_weights(coords, bw)
    z = gi_star_zscores(x, W)
    z_grid = z.reshape(h, w)
    sig = classify_significance(z).reshape(h, w)

    # 核密度
    kde = np.zeros((h, w))
    if points_xy.shape[0] > 0:
        kde_bw = bw
        kde = kernel_density(points_xy, gxx, gyy, kde_bw)

    # NoData-aware output: zero out Gi* / KDE for input NoData pixels
    if args.input and not args.synthetic and input_nodata is not None:
        z_grid = np.where(valid_mask, z_grid, np.nan).astype(np.float32)
        sig = np.where(valid_mask, sig, 0).astype(np.int32)  # 0 = not significant (sentinel)
        kde = np.where(valid_mask, kde, np.nan).astype(np.float32)

    out_z = os.path.join(output_dir, "gi_star_zscore.tif")
    write_geotiff(out_z, np.nan_to_num(z_grid, nan=-9999.0), bbox, nodata=-9999.0)
    out_sig = os.path.join(output_dir, "hotspot_significance.tif")
    write_geotiff(out_sig, sig.astype(np.float32), bbox, nodata=0.0)
    out_kde = os.path.join(output_dir, "kernel_density.tif")
    write_geotiff(out_kde, np.nan_to_num(kde, nan=-9999.0), bbox, nodata=-9999.0)

    # 显著性统计（只对有效像元计数）
    if args.input and not args.synthetic and input_nodata is not None:
        sig_for_count = sig[valid_mask] if valid_mask.shape == sig.shape else sig
    else:
        sig_for_count = sig
    uniq, counts = np.unique(sig_for_count, return_counts=True)
    sig_summary = {int(u): int(c) for u, c in zip(uniq, counts)}
    # z range from valid pixels only
    z_for_range = z_grid[np.isfinite(z_grid)] if z_grid.dtype == np.float32 else z_grid
    z_max = float(z_for_range.max()) if z_for_range.size else float("nan")
    z_min = float(z_for_range.min()) if z_for_range.size else float("nan")
    stats_path = os.path.join(output_dir, "hotspot_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump({"significance_counts": sig_summary, "bandwidth": bw,
                   "z_max": z_max, "z_min": z_min,
                   "n_valid_pixels": int(sig_for_count.size)},
                  f, ensure_ascii=False, indent=2)

    qa = {
        "source": source_note,
        "n_cells": int(x.size),
        "n_valid_pixels": int(n_valid_input),
        "n_total_pixels": int(n_total_input),
        "input_nodata": input_nodata,
        "bandwidth": float(bw),
        "hotspot_cells_95": int(sig_summary.get(2, 0) + sig_summary.get(3, 0)),
        "coldspot_cells_95": int(sig_summary.get(-2, 0) + sig_summary.get(-3, 0)),
        "z_max": z_max,
        "z_min": z_min,
    }
    outputs = [
        {"path": out_z, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1, "nodata": -9999.0},
        {"path": out_sig, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1, "nodata": 0.0},
        {"path": out_kde, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1, "nodata": -9999.0},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] bandwidth: {bw:.4f}")
        print(f"[{SKILL_NAME}] z range: [{z_min:.2f}, {z_max:.2f}]")
        print(f"[{SKILL_NAME}] hotspots(95%): {qa['hotspot_cells_95']}  coldspots(95%): {qa['coldspot_cells_95']}")
        print(f"[{SKILL_NAME}] output: {out_z}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Hotspot analysis: Getis-Ord Gi*, kernel density, multi-scale significance.",
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF raster")
    p.add_argument("--grid-size", type=int, default=24, help="working grid size (default: 24)")
    p.add_argument("--bandwidth", type=float, default=0.0,
                   help="distance bandwidth (0=auto, default: 0)")
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
