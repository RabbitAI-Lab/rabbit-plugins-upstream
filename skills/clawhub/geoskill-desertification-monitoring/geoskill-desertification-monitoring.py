#!/usr/bin/env python3
"""desertification-monitoring — 荒漠化监测

融合多期 NDVI 趋势、反照率（albedo）与植被稀缺度，综合评分并对荒漠化程度
分级（稳定 / 轻度 / 中度 / 重度）。

- **NDVI 趋势**：对每个像元的 NDVI 时间序列估计趋势斜率，支持 Sen's slope
  （稳健中位数斜率）与最小二乘线性回归斜率。负斜率代表植被退化。
- **反照率**：可见光波段（蓝/绿/红）均值。裸土/沙漠反照率高，植被低。
- **植被稀缺度**：由平均 NDVI 反映，低 NDVI 指示稀疏植被/裸地。

融合得分 score = 0.4×scarcity + 0.35×bare + 0.25×decline，再阈值化为四个等级。

数据源：本地多期 GeoTIFF（波段 = 各期 NDVI，可选末波段为反照率），
或 ``--synthetic`` 生成含退化趋势的物理一致模拟序列（离线）。

隐私声明 / Privacy：默认离线，不访问网络，所有处理本地完成。

Usage:
    python desertification-monitoring.py --input ndvi_series.tif --n-dates 6 --output-dir ./out
    python desertification-monitoring.py --bbox 100 40 101 41 --synthetic --n-dates 6 --output-dir ./out

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
SKILL_NAME = "desertification-monitoring"

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


# ---- 评分参数 ----
ALB_LO = 0.15               # 反照率隶属度下界
ALB_HI = 0.35               # 反照率隶属度上界
NDVI_SPARSE_LO = 0.15       # 植被稀缺度 NDVI 下界
NDVI_SPARSE_HI = 0.50       # 植被稀缺度 NDVI 上界
W_SCARCITY = 0.40
W_BARE = 0.35
W_DECLINE = 0.25

# ---- 分级阈值 ----
GRADE_MILD = 0.30
GRADE_MODERATE = 0.50
GRADE_SEVERE = 0.70
GRADE_NAMES = ["stable", "mild", "moderate", "severe"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 校验：bbox / 参数
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """P0: bbox 合法性前置校验。"""
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            f"bbox must be a 4-element [W S E N]; got {bbox!r}"
        )
    try:
        w, s, e, n = [float(v) for v in bbox]
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox values must be numeric; got {bbox!r}") from exc
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range [-180, 180]: W={w}, E={e}"
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range [-90, 90]: S={s}, N={n}"
        )
    if w >= e:
        if w > 0 and e < 0 and (e - w) > -360:
            raise ValidationError(
                f"bbox W ({w}) >= E ({e}); cross-180° antimeridian is not "
                f"supported — split into two extents"
            )
        raise ValidationError(f"bbox W ({w}) must be < E ({e})")
    if s >= n:
        raise ValidationError(f"bbox S ({s}) must be < N ({n})")
    area = (e - w) * (n - s)
    if area <= 0:
        raise ValidationError(f"bbox area must be > 0; got {area}")


def validate_synthetic_params(n_dates: int) -> None:
    if not isinstance(n_dates, int) or n_dates < 2:
        raise UsageError(f"--n-dates must be >= 2 (Sen's slope needs >=2 dates); got {n_dates}")


def _ramp(x: np.ndarray, lo: float, hi: float) -> np.ndarray:
    if hi <= lo:
        return (x > lo).astype(np.float32)
    return np.clip((x - lo) / (hi - lo), 0.0, 1.0).astype(np.float32)


# ---------------------------------------------------------------------------
# 趋势斜率
# ---------------------------------------------------------------------------
def sens_slope(cube: np.ndarray, times: Optional[np.ndarray] = None) -> np.ndarray:
    """Sen's slope 稳健估计：所有像元对斜率 (x_j−x_i)/(t_j−t_i) 的中位数。

    输入 cube 形状 (n_dates, H, W)，返回 (H, W) 斜率栅格。
    """
    n = cube.shape[0]
    if n < 2:
        raise ValidationError(f"Sen's slope needs >=2 dates, got {n}", n_dates=int(n))
    if times is None:
        times = np.arange(n, dtype=np.float64)
    times = np.asarray(times, dtype=np.float64)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            dt = times[j] - times[i]
            if dt == 0:
                continue
            pairs.append((cube[j] - cube[i]) / dt)
    stack = np.stack(pairs, axis=0)
    return np.median(stack, axis=0).astype(np.float32)


def linear_slope(cube: np.ndarray, times: Optional[np.ndarray] = None) -> np.ndarray:
    """最小二乘线性回归斜率（每像元）。"""
    n = cube.shape[0]
    if n < 2:
        raise ValidationError(f"linear slope needs >=2 dates, got {n}", n_dates=int(n))
    if times is None:
        times = np.arange(n, dtype=np.float64)
    t = np.asarray(times, dtype=np.float64)
    t = t - t.mean()
    denom = float((t ** 2).sum())
    y = cube - cube.mean(axis=0, keepdims=True)
    slope = (t[:, None, None] * y).sum(axis=0) / denom
    return slope.astype(np.float32)


def trend_slope(cube: np.ndarray, times: Optional[np.ndarray] = None,
                method: str = "sens") -> np.ndarray:
    if method == "sens":
        return sens_slope(cube, times)
    if method == "linear":
        return linear_slope(cube, times)
    raise UsageError(f"unknown trend method '{method}'", method=method)


# ---------------------------------------------------------------------------
# 荒漠化评分与分级
# ---------------------------------------------------------------------------
def desertification_score(
    ndvi_series: np.ndarray,
    albedo: np.ndarray,
    method: str = "sens",
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """融合 NDVI 趋势 + 反照率 + 植被稀缺度，计算荒漠化得分 [0,1]。

    返回 (score, slope, components)。
    """
    n = ndvi_series.shape[0]
    slope = trend_slope(ndvi_series, method=method)
    mean_ndvi = ndvi_series.mean(axis=0)

    # 相对退化：斜率×时长 / 均值，取负并裁剪到 [0,1]
    rel_decline = -slope * (n - 1) / np.clip(mean_ndvi, 0.05, None)
    decline = np.clip(rel_decline, 0.0, 1.0).astype(np.float32)

    scarcity = 1.0 - _ramp(mean_ndvi, NDVI_SPARSE_LO, NDVI_SPARSE_HI)
    bare = _ramp(albedo.astype(np.float32), ALB_LO, ALB_HI)

    score = (W_SCARCITY * scarcity + W_BARE * bare + W_DECLINE * decline).astype(np.float32)
    score = np.clip(score, 0.0, 1.0)
    components = {
        "mean_decline": float(np.mean(decline)),
        "mean_scarcity": float(np.mean(scarcity)),
        "mean_bare": float(np.mean(bare)),
        "mean_slope": float(np.mean(slope)),
    }
    return score, slope, components


def classify_desertification(score: np.ndarray) -> np.ndarray:
    """得分 → 等级 (0=stable, 1=mild, 2=moderate, 3=severe)。"""
    grade = np.zeros(score.shape, dtype=np.uint8)
    grade[score >= GRADE_MILD] = 1
    grade[score >= GRADE_MODERATE] = 2
    grade[score >= GRADE_SEVERE] = 3
    return grade


def grade_areas(grade: np.ndarray, pixel_area_m2: float) -> Dict[str, Any]:
    """各等级像元数与面积。"""
    out: Dict[str, Any] = {}
    for g, name in enumerate(GRADE_NAMES):
        px = int((grade == g).sum())
        out[name] = {
            "pixels": px,
            "area_m2": px * pixel_area_m2,
            "area_ha": px * pixel_area_m2 / 10000.0,
            "fraction": float(px) / grade.size,
        }
    return out


# ---------------------------------------------------------------------------
# 输入拆分
# ---------------------------------------------------------------------------
def split_inputs(cube: np.ndarray, n_dates: int) -> Tuple[np.ndarray, np.ndarray, bool]:
    """把输入立方体拆成 (ndvi_series, albedo, albedo_explicit)。

    - nb == n_dates+1：前 n_dates 为 NDVI 序列，末波段为反照率；
    - nb >= n_dates：前 n_dates 为 NDVI 序列，反照率用 (1−mean_ndvi) 代理。
    """
    if cube.ndim != 3:
        raise ValidationError(f"expected 3D cube, got shape {cube.shape}", shape=str(cube.shape))
    nb = cube.shape[0]
    if nb < n_dates:
        raise ValidationError(
            f"need >= {n_dates} bands for {n_dates} dates, got {nb}",
            bands=int(nb), n_dates=int(n_dates),
        )
    ndvi = cube[:n_dates].astype(np.float32)
    if nb == n_dates + 1:
        albedo = cube[n_dates].astype(np.float32)
        explicit = True
    else:
        albedo = (1.0 - ndvi.mean(axis=0)).astype(np.float32)
        explicit = False
    return ndvi, albedo, explicit


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic_series(
    bbox: List[float],
    n_dates: int = 6,
    width: int = 128,
    height: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成荒漠化合成场景。

    布局（自上而下）：稳定草地、退化斑块（NDVI 由 0.55 降至 0.10）、
    稳定沙漠（低 NDVI、高反照率）、轻度退化斑块。
    返回 (ndvi_series, albedo, degrading_truth_mask, info)。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yyn = yy.astype(np.float32) / max(height - 1, 1)

    times = np.arange(n_dates, dtype=np.float32)
    frac = times / max(n_dates - 1, 1)  # 0..1

    ndvi = np.zeros((n_dates, height, width), dtype=np.float32)
    albedo = np.full((height, width), 0.12, dtype=np.float32)

    # 默认：稳定草地 NDVI 0.6
    base = np.full((height, width), 0.60, dtype=np.float32)

    # 退化斑块：中部横带，NDVI 0.55 -> 0.10
    degrade_band = (yyn > 0.30) & (yyn < 0.50)
    degrade_start, degrade_end = 0.55, 0.10

    # 稳定沙漠：下部，NDVI 0.10
    desert = yyn > 0.72

    # 轻度退化：0.55 -> 0.42
    mild_band = (yyn > 0.55) & (yyn < 0.68)

    for k in range(n_dates):
        layer = base.copy()
        layer[degrade_band] = degrade_start + (degrade_end - degrade_start) * frac[k]
        layer[desert] = 0.10
        layer[mild_band] = 0.55 + (0.42 - 0.55) * frac[k]
        layer = layer + rng.normal(0, 0.004, size=layer.shape).astype(np.float32)
        ndvi[k] = np.clip(layer, 0.0, 1.0)

    albedo[degrade_band] = 0.34
    albedo[desert] = 0.38
    albedo[mild_band] = 0.20
    albedo = np.clip(albedo + rng.normal(0, 0.004, size=albedo.shape).astype(np.float32), 0, 1)

    truth_degrading = degrade_band.astype(np.uint8)
    info = {
        "bbox": bbox, "width": width, "height": height, "n_dates": n_dates,
        "degrading_px": int(truth_degrading.sum()),
        "injected_slope_degrading": float((degrade_end - degrade_start) / max(n_dates - 1, 1)),
    }
    return ndvi, albedo, truth_degrading, info


def build_cube(ndvi_series: np.ndarray, albedo: np.ndarray) -> np.ndarray:
    """打包为 (n_dates+1, H, W) 立方体：NDVI 序列 + 末波段反照率。"""
    return np.concatenate([ndvi_series, albedo[np.newaxis, ...]], axis=0).astype(np.float32)


def pixel_area_m2(bbox: List[float], height: int, width: int) -> float:
    lat0 = (bbox[1] + bbox[3]) / 2.0
    x_m = (bbox[2] - bbox[0]) * 111320.0 * np.cos(np.deg2rad(lat0)) / max(width, 1)
    y_m = (bbox[3] - bbox[1]) * 110540.0 / max(height, 1)
    return float(abs(x_m * y_m))


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """读 GeoTIFF，返回 (cube, bbox)。P0: NoData 替换为 NaN（保持 test 兼容 2-tuple）。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=False).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    return cube, bbox


def read_nodata(path: str) -> Optional[float]:
    """从 GeoTIFF 文件读 nodata 值（不读数据）。用于记录到 qa。"""
    import rasterio
    with rasterio.open(path) as src:
        return src.nodata


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
            "synthetic": bool(getattr(args, "synthetic", False)),
            "n_dates": int(getattr(args, "n_dates", 6)),
            "method": getattr(args, "method", "sens"),
        },
        outputs=[OutputFile(**o) for o in outputs], qa=qa,
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

    # 0) 参数前置校验（P0/P1）
    if args.synthetic or not args.input:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        validate_synthetic_params(int(args.n_dates))

    synth_info: Optional[Dict[str, Any]] = None
    truth_deg: Optional[np.ndarray] = None
    input_nodata: Optional[float] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        input_nodata = read_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        ndvi, albedo, explicit = split_inputs(cube, args.n_dates)
        source_note = args.input
    else:
        ndvi, albedo, truth_deg, synth_info = generate_synthetic_series(
            bbox, n_dates=args.n_dates)
        explicit = True
        source_note = "synthetic"

    if ndvi.size == 0:
        raise ValidationError("input raster is empty")

    # 1) bbox + NoData 校验（前置，确保无效输入不创建 output 目录）
    if bbox is not None:
        validate_bbox(bbox)
    n_valid = int(np.count_nonzero(np.isfinite(ndvi)))
    if n_valid == 0:
        raise ValidationError(
            "input NDVI series has no valid pixels (all NoData/NaN); nothing to analyze"
        )

    # 2) 所有校验通过后才创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    h, w = ndvi.shape[1], ndvi.shape[2]
    px_area = pixel_area_m2(bbox, h, w)

    score, slope, components = desertification_score(ndvi, albedo, method=args.method)
    grade = classify_desertification(score)
    areas = grade_areas(grade, px_area)

    # 写出
    grade_tif = os.path.join(output_dir, "desertification_grade.tif")
    write_geotiff(grade_tif, grade.astype(np.float32), bbox)

    trend_tif = os.path.join(output_dir, "ndvi_trend.tif")
    write_geotiff(trend_tif, slope, bbox)

    score_tif = os.path.join(output_dir, "desertification_score.tif")
    write_geotiff(score_tif, score, bbox)

    stats = {
        "n_dates": int(ndvi.shape[0]),
        "method": args.method,
        "pixel_area_m2": px_area,
        "albedo_explicit": bool(explicit),
        "grade_areas": areas,
        "components": components,
        "input_nodata": input_nodata,
        "n_valid_pixels": n_valid,
    }
    stats_path = os.path.join(output_dir, "desertification_area.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "n_valid_pixels": n_valid,
        "input_nodata": input_nodata,
        "mean_slope": components["mean_slope"],
        "severe_fraction": areas["severe"]["fraction"],
    }
    if synth_info is not None and truth_deg is not None:
        # 退化区趋势检测一致性：真值退化区平均斜率应显著为负
        # 用 np.nanmean 兼容 partial NaN
        mean_slope_deg = float(np.nanmean(slope[truth_deg.astype(bool)]))
        qa["synthetic_degrading_mean_slope"] = mean_slope_deg
        # 退化区应被分为中度或重度
        deg_grade = grade[truth_deg.astype(bool)]
        qa["synthetic_degrading_frac_high_grade"] = float((deg_grade >= 2).mean())

    outputs = [
        {"path": grade_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": trend_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": score_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] dates: {ndvi.shape[0]}  method: {args.method}  shape: {ndvi.shape[1:]}")
        print(f"[{SKILL_NAME}] mean slope: {components['mean_slope']:.5f}")
        for name in GRADE_NAMES:
            print(f"[{SKILL_NAME}]   {name:>8}: {areas[name]['pixels']:>6} px  "
                  f"{areas[name]['area_ha']:.1f} ha")
        print(f"[{SKILL_NAME}] output: {grade_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Desertification monitoring from NDVI trend, albedo and vegetation scarcity.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multi-temporal GeoTIFF (bands=dates [+albedo])")
    p.add_argument("--n-dates", type=int, default=6,
                   help="number of time steps (default: 6)")
    p.add_argument("--method", default="sens", choices=["sens", "linear"],
                   help="trend estimator (default: sens)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic series (offline)")
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
