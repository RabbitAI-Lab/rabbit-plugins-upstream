#!/usr/bin/env python3
"""land-degradation-assessment — 土地退化评估（SDG 15.3.1）

按照联合国 SDG 指标 15.3.1（土地退化零增长，LDN）的方法论，用三个子指标
综合评估土地退化状态：

- **土地生产力（productivity）**：用 NDVI 时间序列的 Sen's slope 非参数趋势
  估计器（Sen 1968）逐像元拟合，斜率显著为负 → 生产力下降 → 退化。
- **土地覆盖变化（cover）**：对比两期 LULC 分类，依据各地类的生态质量评分
  构建转移矩阵，质量下降型转移 → 退化。
- **土壤有机碳（carbon，可选）**：对比两期 SOC 储量，相对下降超阈值 → 退化。

三个子指标按 SDG 报告规则合成：任一子指标退化 → 退化；否则任一改善 → 改善；
其余 → 稳定。输出退化分级栅格（-1=退化 / 0=稳定 / +1=改善）+ SDG 报告。

数据源：本地多期 NDVI 栅格（``--input`` 多波段）或两期 LULC + SOC；
``--synthetic`` 生成物理一致的模拟场景（含注入的退化/改善真值区）用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python land-degradation-assessment.py --bbox 116 39 117 40 --n-dates 6 --output-dir ./out
    python land-degradation-assessment.py --input ndvi_stack.tif --output-dir ./out

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
SKILL_NAME = "land-degradation-assessment"

# ---------------------------------------------------------------------------
# Input validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate geographic bbox: W<E, S<N, lat in [-90,90], lon in [-180,180]."""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be [W, S, E, N] with 4 floats")
    w, s, e, n = [float(x) for x in bbox]
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError("bbox contains non-finite values")
    if w < -180.0 or e > 180.0 or s < -90.0 or n > 90.0:
        raise ValidationError(
            f"bbox out of range: lon=[{w},{e}] must be in [-180,180], lat=[{s},{n}] in [-90,90]")
    if w >= e:
        raise ValidationError(
            f"bbox W must be < E; got W={w}, E={e} (likely reversed; this skill does not support wrapping around 180°)")
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N; got S={s}, N={n} (likely reversed)")
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(f"bbox has zero area: W={w}, E={e}, S={s}, N={n}")


def read_geotiff_with_nodata(path: str):
    """Read multiband GeoTIFF, replacing NoData with NaN; return (cube, bbox)."""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nd = src.nodata
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    if nd is not None and np.isfinite(float(nd)):
        cube = np.where(cube == float(nd), np.nan, cube).astype(np.float32)
    return cube, bbox

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


# ---------------------------------------------------------------------------
# 地类生态质量评分（1-5，越高越健康），用于 LULC 转移矩阵的退化判定
# 编码：1=森林 2=草地 3=耕地 4=裸地/退化地 5=建设用地 6=水体
# ---------------------------------------------------------------------------
LULC_CLASSES: Dict[int, str] = {
    1: "forest",
    2: "grassland",
    3: "cropland",
    4: "bare_degraded",
    5: "urban",
    6: "water",
}
LULC_QUALITY: Dict[int, int] = {
    1: 5,  # 森林最健康
    2: 4,
    3: 3,
    6: 3,
    5: 2,
    4: 1,  # 裸地/退化地最差
}

# SDG 分级编码
DEGRADED = -1
STABLE = 0
IMPROVED = 1
CLASS_NAMES = {DEGRADED: "degraded", STABLE: "stable", IMPROVED: "improved"}


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def sens_slope(series: np.ndarray, times: np.ndarray) -> np.ndarray:
    """逐像元 Sen's slope 非参数趋势估计（Sen 1968）。

    参数
    ----
    series : (n_dates, H, W) 的 NDVI 时间序列
    times  : (n_dates,) 的时间坐标（如年份）

    返回
    ----
    (H, W) 的斜率栅格，取所有两两点斜率 (y_j-y_i)/(t_j-t_i) 的中位数。
    对异常值稳健，不假设正态分布，是 LDN 生产力指标的推荐方法。
    """
    series = np.asarray(series, dtype=np.float64)
    times = np.asarray(times, dtype=np.float64)
    n = int(times.size)
    if series.shape[0] != n:
        raise ValidationError(
            f"series has {series.shape[0]} dates but times has {n} entries")
    if n < 2:
        raise ValidationError("need at least 2 dates to estimate a trend")

    pair_slopes: List[np.ndarray] = []
    for i in range(n):
        for j in range(i + 1, n):
            dt = times[j] - times[i]
            if dt == 0:
                continue
            diff = series[j] - series[i]
            # NaN/Inf propagate; nanmedian handles per-pixel
            pair_slopes.append(diff / dt)
    if not pair_slopes:
        return np.zeros(series.shape[1:], dtype=np.float64)
    stack = np.stack(pair_slopes, axis=0)
    return np.nanmedian(stack, axis=0)


def classify_indicator(
    value: np.ndarray,
    degrade_thresh: float,
    improve_thresh: float,
) -> np.ndarray:
    """把连续指标值离散成 SDG 三分类。

    value < degrade_thresh → 退化 (-1)
    value > improve_thresh → 改善 (+1)
    其余 → 稳定 (0)

    degrade_thresh 应为负值，improve_thresh 应为正值。
    """
    value = np.asarray(value)
    out = np.full(value.shape, STABLE, dtype=np.int8)
    out[value < degrade_thresh] = DEGRADED
    out[value > improve_thresh] = IMPROVED
    return out


def transition_matrix(
    lulc1: np.ndarray,
    lulc2: np.ndarray,
    n_classes: int,
) -> np.ndarray:
    """两期 LULC 的转移矩阵（行=期初类别，列=期末类别，像元计数）。"""
    if lulc1.shape != lulc2.shape:
        raise ValidationError("lulc1 and lulc2 must have the same shape")
    a = np.asarray(lulc1).astype(np.int64).ravel()
    b = np.asarray(lulc2).astype(np.int64).ravel()
    if a.min() < 0 or b.min() < 0:
        raise ValidationError("LULC class codes must be >= 0")
    idx = a * n_classes + b
    mat = np.bincount(idx, minlength=n_classes * n_classes)
    return mat.reshape(n_classes, n_classes)


def lulc_quality(lulc: np.ndarray) -> np.ndarray:
    """把 LULC 分类栅格映射为逐像元生态质量评分。"""
    out = np.zeros(np.asarray(lulc).shape, dtype=np.float64)
    for code, score in LULC_QUALITY.items():
        out[lulc == code] = score
    return out


def lulc_change_indicator(
    lulc1: np.ndarray,
    lulc2: np.ndarray,
) -> np.ndarray:
    """依据地类质量评分的变化给出覆盖子指标（质量分差）。"""
    return lulc_quality(lulc2) - lulc_quality(lulc1)


def soc_relative_change(soc1: np.ndarray, soc2: np.ndarray) -> np.ndarray:
    """土壤有机碳相对变化 (soc2-soc1)/soc1，soc1 为 0 处记 0。"""
    s1 = np.asarray(soc1, dtype=np.float64)
    s2 = np.asarray(soc2, dtype=np.float64)
    denom = np.where(np.abs(s1) > 1e-9, s1, 1.0)
    rel = (s2 - s1) / denom
    return np.where(np.abs(s1) > 1e-9, rel, 0.0)


def combine_sdg(
    productivity: np.ndarray,
    cover: Optional[np.ndarray] = None,
    carbon: Optional[np.ndarray] = None,
) -> np.ndarray:
    """SDG 15.3.1 合成规则：任一子指标退化 → 退化；否则任一改善 → 改善；其余稳定。

    每个子指标数组元素 ∈ {-1, 0, +1}。cover / carbon 可选（None 时跳过）。
    """
    shape = productivity.shape
    degraded = productivity < 0
    improved = productivity > 0
    for arr in (cover, carbon):
        if arr is None:
            continue
        degraded = degraded | (arr < 0)
        improved = improved | (arr > 0)
    combined = np.full(shape, STABLE, dtype=np.int8)
    combined[degraded] = DEGRADED
    combined[improved & ~degraded] = IMPROVED
    return combined


def assess_degradation(
    ndvi_series: np.ndarray,
    times: np.ndarray,
    lulc1: Optional[np.ndarray] = None,
    lulc2: Optional[np.ndarray] = None,
    soc1: Optional[np.ndarray] = None,
    soc2: Optional[np.ndarray] = None,
    prod_degrade: float = -0.005,
    prod_improve: float = 0.005,
    cover_degrade: float = -0.5,
    cover_improve: float = 0.5,
    soc_degrade: float = -0.10,
    soc_improve: float = 0.10,
) -> Dict[str, Any]:
    """完整 SDG 三指标评估，返回分级栅格 + 中间产物 + 统计。"""
    slope = sens_slope(ndvi_series, times)
    productivity = classify_indicator(slope, prod_degrade, prod_improve)

    cover = None
    tmat = None
    if lulc1 is not None and lulc2 is not None:
        cover_val = lulc_change_indicator(lulc1, lulc2)
        cover = classify_indicator(cover_val, cover_degrade, cover_improve)
        n_classes = max(len(LULC_CLASSES),
                        int(np.nanmax([lulc1, lulc2])) + 1)
        tmat = transition_matrix(lulc1, lulc2, n_classes)

    carbon = None
    soc_rel = None
    if soc1 is not None and soc2 is not None:
        soc_rel = soc_relative_change(soc1, soc2)
        carbon = classify_indicator(soc_rel, soc_degrade, soc_improve)

    combined = combine_sdg(productivity, cover, carbon)

    total = combined.size
    counts = {
        "degraded": int(np.sum(combined == DEGRADED)),
        "stable": int(np.sum(combined == STABLE)),
        "improved": int(np.sum(combined == IMPROVED)),
    }
    fractions = {k: v / total for k, v in counts.items()}

    result: Dict[str, Any] = {
        "degradation": combined,
        "productivity_slope": slope.astype(np.float32),
        "productivity_class": productivity,
        "cover_class": cover,
        "carbon_class": carbon,
        "soc_relative_change": (soc_rel.astype(np.float32)
                                 if soc_rel is not None else None),
        "transition_matrix": (tmat.tolist() if tmat is not None else None),
        "counts": counts,
        "fractions": fractions,
        "n_dates": int(ndvi_series.shape[0]),
    }
    return result


# ---------------------------------------------------------------------------
# 合成数据：物理一致的场景 + 注入的退化/改善真值
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    n_dates: int = 6,
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Dict[str, Any]:
    """生成多期 NDVI 时序 + 两期 LULC + 两期 SOC，内含一个退化块和一个改善块。

    退化块：NDVI 逐年下降、森林→裸地、SOC 下降。
    改善块：NDVI 逐年上升、裸地→草地、SOC 上升。
    背景：稳定的草地/耕地，含少量随机噪声。
    """
    rng = np.random.default_rng(seed)
    times = np.arange(n_dates, dtype=np.float64)

    base = rng.uniform(0.45, 0.65, size=(height, width)).astype(np.float64)
    noise = rng.normal(0.0, 0.003, size=(n_dates, height, width))

    # 退化块（左上）与改善块（右下）
    deg = np.zeros((height, width), dtype=bool)
    imp = np.zeros((height, width), dtype=bool)
    deg[8:24, 8:24] = True
    imp[40:56, 40:56] = True

    ndvi = np.zeros((n_dates, height, width), dtype=np.float64)
    deg_trend = -0.05  # 每年下降 0.05
    imp_trend = +0.04  # 每年上升 0.04
    for t in range(n_dates):
        layer = base.copy()
        layer[deg] += deg_trend * times[t]
        layer[imp] += imp_trend * times[t]
        ndvi[t] = np.clip(layer + noise[t], 0.0, 1.0)

    # 两期 LULC：背景草地(2)，退化块 森林(1)->裸地(4)，改善块 裸地(4)->草地(2)
    lulc1 = np.full((height, width), 2, dtype=np.int32)
    lulc2 = np.full((height, width), 2, dtype=np.int32)
    lulc1[deg] = 1  # 期初森林
    lulc2[deg] = 4  # 期末退化为裸地
    lulc1[imp] = 4  # 期初裸地
    lulc2[imp] = 2  # 期末恢复为草地

    # 两期 SOC (kg/m²)：退化块下降 30%，改善块上升 25%，背景稳定
    soc1 = rng.uniform(3.0, 5.0, size=(height, width)).astype(np.float64)
    soc2 = soc1.copy() + rng.normal(0.0, 0.05, size=(height, width))
    soc2[deg] = soc1[deg] * 0.70
    soc2[imp] = soc1[imp] * 1.25

    truth = np.full((height, width), STABLE, dtype=np.int8)
    truth[deg] = DEGRADED
    truth[imp] = IMPROVED

    return {
        "bbox": list(bbox),
        "width": width,
        "height": height,
        "n_dates": n_dates,
        "times": times,
        "ndvi": ndvi.astype(np.float32),
        "lulc1": lulc1,
        "lulc2": lulc2,
        "soc1": soc1.astype(np.float32),
        "soc2": soc2.astype(np.float32),
        "truth": truth,
        "deg_mask": deg,
        "imp_mask": imp,
    }


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    cube: np.ndarray,
    bbox: List[float],
    nodata: float = -9999.0,
) -> None:
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
        nd = src.nodata
    if nd is not None and np.isfinite(float(nd)):
        cube = np.where(cube == float(nd), np.nan, cube).astype(np.float32)
    return cube, bbox


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
    bbox: List[float],
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
            "n_dates": getattr(args, "n_dates", None),
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
    if args.n_dates is not None and args.n_dates < 2:
        raise ValidationError(
            f"--n-dates must be >= 2 for trend analysis, got {args.n_dates}")

    synth_info: Optional[Dict[str, Any]] = None
    truth: Optional[np.ndarray] = None

    if args.input and not args.synthetic:
        ndvi, file_bbox = read_geotiff(args.input)
        if ndvi.ndim != 3 or ndvi.shape[0] < 2:
            raise ValidationError(
                "input raster must be a multiband (n_dates >= 2) NDVI stack")
        bbox = bbox if bbox is not None else file_bbox
        times = np.arange(ndvi.shape[0], dtype=np.float64)
        lulc1 = lulc2 = soc1 = soc2 = None
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        synth = generate_synthetic(bbox, n_dates=args.n_dates)
        ndvi = synth["ndvi"]
        times = synth["times"]
        lulc1, lulc2 = synth["lulc1"], synth["lulc2"]
        soc1, soc2 = synth["soc1"], synth["soc2"]
        truth = synth["truth"]
        synth_info = synth
        source_note = "synthetic"

    if ndvi.size == 0:
        raise ValidationError("input data is empty")
    # Reject if no date has any valid pixel
    if not np.any(np.isfinite(ndvi)):
        raise ValidationError(
            "input NDVI stack has no valid pixels (entirely NoData/NaN)")

    os.makedirs(output_dir, exist_ok=True)

    res = assess_degradation(
        ndvi, times,
        lulc1=lulc1, lulc2=lulc2, soc1=soc1, soc2=soc2,
    )

    deg_raster = res["degradation"].astype(np.float32)
    slope_raster = res["productivity_slope"]

    out_deg = os.path.join(output_dir, "degradation.tif")
    out_slope = os.path.join(output_dir, "productivity_slope.tif")
    write_geotiff(out_deg, deg_raster, bbox)
    write_geotiff(out_slope, slope_raster, bbox)

    # SDG 报告
    report: Dict[str, Any] = {
        "skill": SKILL_NAME,
        "method": "SDG 15.3.1 LDN three sub-indicators",
        "n_dates": res["n_dates"],
        "indicators_used": {
            "productivity": True,
            "cover": res["cover_class"] is not None,
            "carbon": res["carbon_class"] is not None,
        },
        "counts": res["counts"],
        "fractions": res["fractions"],
        "transition_matrix": res["transition_matrix"],
        "lulc_classes": {str(k): v for k, v in LULC_CLASSES.items()},
        "class_legend": CLASS_NAMES,
    }
    report_path = os.path.join(output_dir, "sdg_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2, default=str)

    # QA：含与注入真值的一致性（合成模式）
    n_valid = int(np.sum(np.isfinite(slope_raster)))
    qa: Dict[str, Any] = {
        "source": source_note,
        "degraded_fraction": res["fractions"]["degraded"],
        "stable_fraction": res["fractions"]["stable"],
        "improved_fraction": res["fractions"]["improved"],
        "mean_productivity_slope": (float(np.nanmean(slope_raster))
                                     if n_valid else 0.0),
        "n_valid_pixels": n_valid,
        "n_total_pixels": int(slope_raster.size),
    }
    if truth is not None:
        agree = float(np.mean(res["degradation"] == truth))
        qa["synthetic_agreement"] = agree

    outputs = [
        {"path": out_deg, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_slope, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": report_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] dates: {res['n_dates']}  shape: {deg_raster.shape}")
        print(f"[{SKILL_NAME}] degraded: {res['fractions']['degraded']:.3f}  "
              f"stable: {res['fractions']['stable']:.3f}  "
              f"improved: {res['fractions']['improved']:.3f}")
        if truth is not None:
            print(f"[{SKILL_NAME}] synthetic agreement: {qa['synthetic_agreement']:.3f}")
        print(f"[{SKILL_NAME}] output: {out_deg}")
        print(f"[{SKILL_NAME}] report: {report_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="SDG 15.3.1 land degradation assessment (productivity / cover / carbon).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="multiband NDVI time-series GeoTIFF (>= 2 bands)")
    p.add_argument("--n-dates", type=int, default=6, dest="n_dates",
                   help="number of time steps in synthetic mode (default: 6)")
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
