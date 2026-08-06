#!/usr/bin/env python3
"""pasture-quality-assessment — 草地质量评估

综合三项指标评估草地质量：
- **植被覆盖度**（FVC，由 NDVI 像元分解得到）；
- **物候特征**（生长季起止、峰值时间与幅度）；
- **退化指数**（多年 NDVI 线性趋势斜率，负斜率=退化）。
融合为质量指数并分级。

核心算法
--------
- FVC = (NDVI − NDVIsoil) / (NDVIveg − NDVIsoil)，裁剪 [0,1]。
- 物候：以振幅阈值为生长季边界，argmax 为峰值。
- 退化：对逐像元多年 NDVI 做一阶线性拟合，斜率为退化速率。

数据源：本地 NDVI 时序/多年栅格或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线，``--synthetic`` 完全无网络，本地处理不上传。

Usage:
    python pasture-quality-assessment.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "pasture-quality-assessment"

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, DependencyError, to_exit_code,
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

    class DependencyError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=3, kind="EDepend", **k)

    class ProcessError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=7, kind="EProcess", **k)

    def to_exit_code(exc):
        return getattr(exc, "code", 7)

    OutputManifest = None
    OutputFile = None


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float], source: str = "bbox") -> None:
    """Validate geographic bbox: W<=E, S<=N, lon/lat in range, min area.

    Cross-dateline (W>E) is a ValidationError with a hint to split.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(f"{source}: expected 4 floats [W S E N], got {bbox!r}")
    try:
        w, s, e, n = (float(v) for v in bbox)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"{source}: non-numeric bbox values: {bbox!r}") from exc
    for v, name in ((w, "W"), (s, "S"), (e, "E"), (n, "N")):
        if not (v == v):  # NaN
            raise ValidationError(f"{source}: bbox contains NaN at {name}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"{source}: lon out of [-180,180]: W={w} E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"{source}: lat out of [-90,90]: S={s} N={n}")
    if w > e:
        raise ValidationError(
            f"{source}: W ({w}) > E ({e}); cross-dateline bboxes are not supported. "
            "Split into two bboxes on each side of the 180\u00b0 meridian and run separately."
        )
    if s > n:
        raise ValidationError(f"{source}: S ({s}) > N ({n})")
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"{source}: bbox too small (dlon={e - w}, dlat={n - s}); need > 1e-9 degrees"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def fractional_cover(ndvi: np.ndarray, ndvi_soil: float = 0.10,
                     ndvi_veg: float = 0.70) -> np.ndarray:
    """植被覆盖度 FVC = (NDVI − NDVIsoil)/(NDVIveg − NDVIsoil)，[0,1]。"""
    if ndvi_veg <= ndvi_soil:
        raise ValidationError("ndvi_veg must exceed ndvi_soil")
    ndvi = np.asarray(ndvi, dtype=np.float32)
    fvc = (ndvi - ndvi_soil) / (ndvi_veg - ndvi_soil)
    return np.clip(fvc, 0.0, 1.0).astype(np.float32)


def phenology_metrics(series: np.ndarray, threshold_frac: float = 0.2) -> Dict[str, float]:
    """从一维 NDVI 物候序列提取生长季与峰值特征。

    返回 peak_index/peak_value/base/amplitude/season_start/season_end/season_length。
    """
    s = np.asarray(series, dtype=np.float32).ravel()
    if s.size < 3:
        raise ValidationError("need >=3 time steps for phenology")
    base = float(np.min(s))
    peak_value = float(np.max(s))
    amplitude = peak_value - base
    peak_index = int(np.argmax(s))
    if amplitude <= 1e-6:
        return {"peak_index": peak_index, "peak_value": peak_value, "base": base,
                "amplitude": 0.0, "season_start": int(0), "season_end": int(s.size - 1),
                "season_length": int(s.size - 1)}
    threshold = base + threshold_frac * amplitude
    above = np.where(s >= threshold)[0]
    season_start = int(above[0])
    season_end = int(above[-1])
    return {
        "peak_index": peak_index,
        "peak_value": peak_value,
        "base": base,
        "amplitude": float(amplitude),
        "season_start": season_start,
        "season_end": season_end,
        "season_length": int(season_end - season_start),
    }


def degradation_slope(annual_ndvi: np.ndarray) -> np.ndarray:
    """对 (years, H, W) 多年 NDVI 逐像元做一阶线性拟合，返回斜率 (H,W)。

    正斜率=改善，负斜率=退化。x 轴为年份序号。
    """
    annual_ndvi = np.asarray(annual_ndvi, dtype=np.float32)
    if annual_ndvi.ndim != 3 or annual_ndvi.shape[0] < 2:
        raise ValidationError("annual_ndvi must be (years>=2, H, W)")
    years = annual_ndvi.shape[0]
    x = np.arange(years, dtype=np.float32)
    x_mean = x.mean()
    denom = np.sum((x - x_mean) ** 2)
    y_mean = annual_ndvi.mean(axis=0)
    # slope = sum((x-xm)(y-ym)) / sum((x-xm)^2)
    num = np.sum((x[:, None, None] - x_mean) * (annual_ndvi - y_mean[None, :, :]), axis=0)
    slope = num / denom
    return slope.astype(np.float32)


def quality_index(cover: np.ndarray, degradation_slope_arr: np.ndarray,
                  slope_scale: float = 0.05) -> np.ndarray:
    """质量指数 = 覆盖度与趋势分的加权融合，[0,1]。

    趋势分 = clip(0.5 + slope/slope_scale, 0, 1)：正斜率加分，负斜率扣分。
    """
    cover = np.clip(np.asarray(cover, dtype=np.float32), 0.0, 1.0)
    slope = np.asarray(degradation_slope_arr, dtype=np.float32)
    trend_score = np.clip(0.5 + slope / slope_scale, 0.0, 1.0)
    q = 0.6 * cover + 0.4 * trend_score
    return np.clip(q, 0.0, 1.0).astype(np.float32)


def grade_quality(q: np.ndarray) -> np.ndarray:
    """质量分级：0=差, 1=中, 2=良, 3=优。"""
    q = np.asarray(q, dtype=np.float32)
    out = np.zeros(q.shape, dtype=np.int32)
    out[q >= 0.4] = 1
    out[q >= 0.6] = 2
    out[q >= 0.8] = 3
    return out


def assess_pasture(current_ndvi: np.ndarray, annual_ndvi: np.ndarray,
                   phenology_series: Optional[np.ndarray] = None) -> Dict[str, Any]:
    """主流程：覆盖度 + 退化趋势 + 物候 → 质量指数与分级。"""
    current_ndvi = np.asarray(current_ndvi, dtype=np.float32)
    if current_ndvi.ndim != 2:
        raise ValidationError("current_ndvi must be 2D (H, W)")
    # NaN safety: an all-NaN current_ndvi means NoData everywhere; we
    # have already validated that *some* finite pixels exist, but be
    # defensive at the function level too.
    if not np.isfinite(current_ndvi).any():
        raise ValidationError("current_ndvi has no finite (non-NoData) pixels")
    cover = fractional_cover(current_ndvi)
    slope = degradation_slope(annual_ndvi)
    q = quality_index(cover, slope)
    grade = grade_quality(q)
    if phenology_series is None:
        # NaN-aware per-year spatial mean: skip the -9999 NoData pixels.
        # nanmean raises RuntimeWarning on all-NaN slices; treat those as 0.
        with np.errstate(invalid="ignore"):
            annual_means = np.nanmean(annual_ndvi, axis=(1, 2))
        annual_means = np.where(np.isfinite(annual_means), annual_means, 0.0)
        phenology_series = annual_means
    elif not np.isfinite(phenology_series).all():
        # If caller passed a series with NaN, replace NaN with the finite mean
        finite_v = phenology_series[np.isfinite(phenology_series)]
        if finite_v.size:
            phenology_series = np.where(
                np.isfinite(phenology_series),
                phenology_series,
                float(finite_v.mean()),
            )
        else:
            raise ValidationError("phenology_series has no finite values")
    phen = phenology_metrics(phenology_series)
    # NaN-aware stats
    valid_cover = cover[np.isfinite(cover)]
    valid_slope = slope[np.isfinite(slope)]
    valid_q = q[np.isfinite(q)]
    return {
        "cover": cover, "degradation_slope": slope, "quality_index": q,
        "grade": grade, "phenology": phen,
        "stats": {
            "mean_cover": float(np.mean(valid_cover)) if valid_cover.size else 0.0,
            "mean_slope": float(np.mean(valid_slope)) if valid_slope.size else 0.0,
            "mean_quality": float(np.mean(valid_q)) if valid_q.size else 0.0,
            "degrading_fraction": float(np.mean(valid_slope < -0.005)) if valid_slope.size else 0.0,
            "grade_hist": {str(i): int(np.sum(grade == i)) for i in range(4)},
        },
    }


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 40, height: int = 40,
                       n_years: int = 8, seed: int = 42):
    """左侧优质草地（高覆盖、改善趋势），右侧退化草地（低覆盖、下降趋势）。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1)
    # 当前 NDVI：左高右低
    current_ndvi = np.clip(0.72 - 0.50 * xx + rng.normal(0, 0.02, (height, width)), 0.05, 0.9)
    # 多年序列：左侧逐年改善(+0.01/yr)，右侧退化(-0.02/yr)
    trend = (0.01 - 0.03 * xx)  # (H,W) 每年变化
    annual = np.zeros((n_years, height, width), dtype=np.float32)
    base_year = current_ndvi - trend * (n_years // 2)
    for y in range(n_years):
        annual[y] = np.clip(base_year + trend * y + rng.normal(0, 0.01, (height, width)), 0.05, 0.95)
    # 物候序列（空间平均），高斯生长季
    t = np.linspace(0, 1, 12)
    phenology = (0.15 + 0.55 * np.exp(-((t - 0.55) ** 2) / (2 * 0.13 ** 2))).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height, "n_years": n_years,
            "n_phenology_steps": 12}
    aux = {"current_ndvi": current_ndvi.astype(np.float32), "annual": annual,
           "phenology": phenology}
    return current_ndvi.astype(np.float32), {"info": info, "aux": aux}


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
        inputs={"input": getattr(args, "input", None), "method": getattr(args, "method", None),
                "synthetic": bool(getattr(args, "synthetic", False))},
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
    os.makedirs(output_dir, exist_ok=True)
    bbox = list(args.bbox) if args.bbox else None

    synth_info: Optional[Dict[str, Any]] = None
    phenology_series: Optional[np.ndarray] = None
    nodata: Optional[float] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)  # bands = 年度 NDVI（最后波段=当前）
        bbox = bbox if bbox is not None else file_bbox
        if cube.ndim != 3 or cube.shape[0] < 2:
            raise ValidationError("input needs >=2 bands as multi-year NDVI")
        # Replace NoData sentinel with NaN across the whole cube so the
        # per-year spatial mean (used as phenology series) and the per-pixel
        # current NDVI / annual slope all ignore NoData pixels instead of
        # being dragged by the −9999 sentinel.
        import rasterio as _rio
        with _rio.open(args.input) as _src:
            nodata = _src.nodata
        if nodata is not None:
            cube = np.where(cube == nodata, np.nan, cube).astype(np.float32)
        # If everything is NaN, fail fast
        finite = np.isfinite(cube)
        if not finite.any():
            raise ValidationError(
                f"input raster '{args.input}' contains only NoData pixels; nothing to assess"
            )
        annual = cube
        current_ndvi = cube[-1]
        # Build a per-year spatial mean over *valid* pixels (NaN-aware)
        # to keep the phenology series on the real NDVI scale.
        annual_means = np.nanmean(cube, axis=(1, 2))
        if np.all(~np.isfinite(annual_means)):
            raise ValidationError(
                f"input raster '{args.input}' has no valid (non-NoData) pixels per year; "
                "cannot compute phenology"
            )
        phenology_series = annual_means
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox, source="--bbox")
        _, packed = generate_synthetic(bbox)
        current_ndvi = packed["aux"]["current_ndvi"]
        annual = packed["aux"]["annual"]
        phenology_series = packed["aux"]["phenology"]
        synth_info = packed["info"]
        source_note = "synthetic"

    if current_ndvi.size == 0:
        raise ValidationError("input raster is empty")

    # If --bbox is also given with --input, validate the user-supplied bbox
    if bbox is not None and args.bbox is not None:
        validate_bbox(bbox, source="--bbox")

    res = assess_pasture(current_ndvi, annual, phenology_series=phenology_series)

    quality_tif = os.path.join(output_dir, "pasture_quality.tif")
    write_geotiff(quality_tif, res["quality_index"], bbox)
    cover_tif = os.path.join(output_dir, "fractional_cover.tif")
    write_geotiff(cover_tif, res["cover"], bbox)
    slope_tif = os.path.join(output_dir, "degradation_slope.tif")
    write_geotiff(slope_tif, res["degradation_slope"], bbox)

    phen_json = os.path.join(output_dir, "phenology.json")
    with open(phen_json, "w", encoding="utf-8") as f:
        json.dump(res["phenology"], f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "method": args.method,
          "mean_cover": res["stats"]["mean_cover"], "mean_quality": res["stats"]["mean_quality"],
          "mean_slope": res["stats"]["mean_slope"],
          "degrading_fraction": res["stats"]["degrading_fraction"],
          "grade_hist": res["stats"]["grade_hist"]}
    if synth_info is not None:
        qa["synthetic"] = synth_info

    outputs = [
        {"path": quality_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": cover_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": slope_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": phen_json, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean cover: {qa['mean_cover']:.4f}  mean quality: {qa['mean_quality']:.4f}")
        print(f"[{SKILL_NAME}] mean slope: {qa['mean_slope']:.5f}/yr  degrading frac: {qa['degrading_fraction']:.3f}")
        print(f"[{SKILL_NAME}] phenology peak step: {res['phenology']['peak_index']}")
        print(f"[{SKILL_NAME}] output: {quality_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Pasture quality assessment from NDVI cover, phenology and degradation trend.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multi-year NDVI GeoTIFF (bands = years, last = current)")
    p.add_argument("--method", default="full", choices=["full", "cover-only"],
                   help="assessment method (default: full)")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic scene (offline)")
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
