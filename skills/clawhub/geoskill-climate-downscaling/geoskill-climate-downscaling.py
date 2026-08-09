#!/usr/bin/env python3
"""climate-downscaling — 气候降尺度（统计降尺度）

将粗分辨率气候变量（温度/降水）降尺度到高分辨率，方法为地形回归 + 残差
空间插值（statistical downscaling）：

1. 由高分辨率 DEM 计算预测因子：高程（elevation）与坡度（slope）。
2. 将 DEM/真值块平均到粗分辨率格点，作为回归样本。
3. 用多元线性回归（scikit-learn LinearRegression）建立
   气候变量 ~ 高程 + 坡度 的关系（温度场景下高程系数即递减率 lapse rate）。
4. 将回归模型外推到高分辨率格网；粗格点残差经 scipy 线性插值回到高分辨率。
5. 降尺度结果 = 高分辨率回归预测 + 高分辨率插值残差。

验证：降尺度结果与真值的相关系数、RMSE，以及高程递减率符号。

数据源：本地多波段 GeoTIFF（band1=高分辨率 DEM，band2=待降尺度真值，
band3+=粗分辨率气候场），或 ``--synthetic`` 生成"温度随高程递减"场景（离线）。

隐私声明 / Privacy：默认离线，``--synthetic`` 完全无网络，所有处理本地完成。

Usage:
    python climate-downscaling.py --bbox 100 26 104 30 --output-dir ./out
    python climate-downscaling.py --bbox 100 26 104 30 --synthetic --output-dir ./out
    python climate-downscaling.py --input dem_truth.tif --output-dir ./out

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
SKILL_NAME = "climate-downscaling"

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


def validate_bbox(bbox, ctx: str = "bbox") -> None:
    """Validate a (W, S, E, N) bbox: 4 floats, lon/lat ranges, W<E, S<N.

    Antimeridian crossing (W > E) is NOT supported; raises ValidationError
    suggesting the user split the bbox.
    """
    if bbox is None or len(bbox) != 4:
        raise UsageError(f"{ctx}: expected 4 floats (W S E N); got {bbox!r}")
    try:
        w, s, e, n = [float(v) for v in bbox]
    except (TypeError, ValueError):
        raise UsageError(f"{ctx}: bbox values must be numeric; got {bbox!r}")
    if not (all(np.isfinite([w, s, e, n]))):
        raise ValidationError(f"{ctx}: bbox values must be finite; got {bbox!r}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"{ctx}: longitude out of range (got W={w} E={e}); expected -180..180"
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"{ctx}: latitude out of range (got S={s} N={n}); expected -90..90"
        )
    if w >= e:
        raise ValidationError(
            f"{ctx}: requires W < E (got W={w} E={e}); "
            f"antimeridian crossing is not supported — split the bbox into two."
        )
    if s >= n:
        raise ValidationError(f"{ctx}: requires S < N (got S={s} N={n})")
    if (e - w) < 1e-6 or (n - s) < 1e-6:
        raise ValidationError(
            f"{ctx}: bbox extent too small ({(e - w):.2e} x {(n - s):.2e} deg); "
            f"need at least ~1e-6 deg in each direction"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def slope_from_dem(dem: np.ndarray, res_m: float = 90.0) -> np.ndarray:
    """由 DEM 计算坡度（度）。res_m 为像元尺寸（米）。"""
    gy, gx = np.gradient(dem.astype(np.float64), res_m)
    return np.rad2deg(np.arctan(np.sqrt(gx ** 2 + gy ** 2)))


def block_average(arr: np.ndarray, ch: int, cw: int) -> np.ndarray:
    """将 (H, W) 块平均为 (H//ch, W//cw) 的粗格网（丢弃余边）。"""
    if arr.ndim != 2:
        raise ValidationError(f"block_average expects 2D, got ndim={arr.ndim}")
    H, W = arr.shape
    oh, ow = H // ch, W // cw
    if oh < 1 or ow < 1:
        raise ValidationError(
            f"block size ({ch},{cw}) too large for array ({H},{W})")
    trimmed = arr[:oh * ch, :ow * cw]
    return trimmed.reshape(oh, ch, ow, cw).mean(axis=(1, 3))


def fit_downscaling_regression(
    X_coarse: np.ndarray,
    y_coarse: np.ndarray,
):
    """多元线性回归：y ~ X（预测因子矩阵）。返回 (model, coefs, intercept)。"""
    from sklearn.linear_model import LinearRegression
    X = np.asarray(X_coarse, dtype=np.float64)
    y = np.asarray(y_coarse, dtype=np.float64)
    if X.ndim != 2:
        raise ValidationError(f"X must be 2D (n_samples,n_features), got {X.shape}")
    if X.shape[0] != y.shape[0]:
        raise ValidationError("X and y sample count mismatch")
    if X.shape[0] < X.shape[1] + 1:
        raise ValidationError(
            f"too few samples ({X.shape[0]}) for {X.shape[1]} features")
    model = LinearRegression()
    model.fit(X, y)
    return model, [float(c) for c in model.coef_], float(model.intercept_)


def interpolate_residual(residual: np.ndarray, target_shape: Tuple[int, int]) -> np.ndarray:
    """将粗格点残差线性插值回高分辨率 (H, W)。"""
    from scipy.interpolate import griddata
    ch, cw = residual.shape
    th, tw = target_shape
    if ch < 2 or cw < 2:
        # 太粗无法插值：直接平铺均值
        return np.full((th, tw), float(np.mean(residual)))
    gy, gx = np.mgrid[0:ch, 0:cw]
    # 映射到目标网格坐标空间
    sy = (ch - 1) / max(th - 1, 1)
    sx = (cw - 1) / max(tw - 1, 1)
    ty, tx = np.mgrid[0:th, 0:tw]
    pts = np.stack([ty.ravel() * sy, tx.ravel() * sx], axis=1)
    coarse_pts = np.stack([gy.ravel(), gx.ravel()], axis=1)
    vals = residual.ravel()
    out = griddata(coarse_pts, vals, pts, method="linear")
    nan_mask = np.isnan(out)
    if nan_mask.any():
        nearest = griddata(coarse_pts, vals, pts, method="nearest")
        out[nan_mask] = nearest[nan_mask]
    return out.reshape(th, tw)


def downscale(
    dem_hr: np.ndarray,
    slope_hr: np.ndarray,
    truth_hr: np.ndarray,
    coarse: int = 8,
) -> Dict[str, Any]:
    """完整统计降尺度。返回降尺度栅格 + 回归系数 + 验证指标。"""
    dem_hr = np.asarray(dem_hr, dtype=np.float64)
    slope_hr = np.asarray(slope_hr, dtype=np.float64)
    truth_hr = np.asarray(truth_hr, dtype=np.float64)
    H, W = dem_hr.shape
    if slope_hr.shape != (H, W) or truth_hr.shape != (H, W):
        raise ValidationError("dem/slope/truth shape mismatch")

    # 1) 块平均到粗分辨率格点
    dem_c = block_average(dem_hr, coarse, coarse)
    slope_c = block_average(slope_hr, coarse, coarse)
    truth_c = block_average(truth_hr, coarse, coarse)
    oh, ow = dem_c.shape

    X_c = np.column_stack([dem_c.ravel(), slope_c.ravel()])
    y_c = truth_c.ravel()

    # 2) 回归
    model, coefs, intercept = fit_downscaling_regression(X_c, y_c)

    # 3) 高分辨率回归预测
    X_hr = np.column_stack([dem_hr.ravel(), slope_hr.ravel()])
    reg_hr = model.predict(X_hr).reshape(H, W)

    # 4) 粗格点残差 → 高分辨率插值
    resid_c = truth_c - model.predict(X_c).reshape(oh, ow)
    resid_hr = interpolate_residual(resid_c, (H, W))

    # 5) 降尺度结果
    downscaled = reg_hr + resid_hr

    # 验证
    corr = float(np.corrcoef(downscaled.ravel(), truth_hr.ravel())[0, 1])
    rmse = float(np.sqrt(np.mean((downscaled - truth_hr) ** 2)))
    coarse_up = np.repeat(np.repeat(truth_c, coarse, axis=0), coarse, axis=1)
    coarse_up = coarse_up[:H, :W]
    rmse_coarse = float(np.sqrt(np.mean((coarse_up - truth_hr) ** 2)))
    valid = np.isfinite(downscaled)
    lapse = float(np.polyfit(dem_hr[valid].ravel(), downscaled[valid].ravel(), 1)[0])

    return {
        "downscaled": downscaled.astype(np.float32),
        "regression": reg_hr.astype(np.float32),
        "residual": resid_hr.astype(np.float32),
        "coefs": {"elevation": coefs[0], "slope": coefs[1]},
        "intercept": intercept,
        "coarse_shape": [oh, ow],
        "correlation": corr,
        "rmse": rmse,
        "rmse_coarse_baseline": rmse_coarse,
        "lapse_rate_per_m": lapse,
    }


# ---------------------------------------------------------------------------
# 合成数据：温度随高程递减场景（离线）
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], target_size: int = 64,
                       coarse: int = 8, seed: int = 42) -> Dict[str, Any]:
    """生成高分辨率 DEM、坡度、温度真值（含高程递减 + 平滑空间异常）与粗分辨率温度场。"""
    rng = np.random.default_rng(seed)
    H = W = int(target_size)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float64)
    yy = yy / max(H - 1, 1)
    xx = xx / max(W - 1, 1)

    # 高分辨率 DEM：西高东低 + 两座山丘 + 轻噪声
    dem = (500.0 + 1800.0 * (1.0 - xx)
           + 600.0 * np.exp(-(((xx - 0.3) ** 2 + (yy - 0.4) ** 2) / 0.03))
           + 450.0 * np.exp(-(((xx - 0.7) ** 2 + (yy - 0.7) ** 2) / 0.02))
           + rng.normal(0, 15.0, (H, W)))
    dem = np.clip(dem, 0.0, None)
    slope = slope_from_dem(dem, res_m=90.0)

    # 平滑空间异常（非地形可解释的部分）
    anomaly = (2.0 * np.sin(2 * np.pi * xx) * np.cos(np.pi * yy))
    lapse_true = -0.006  # ℃/m
    truth = 24.0 + lapse_true * dem + anomaly + rng.normal(0, 0.2, (H, W))

    # 粗分辨率温度场：高分辨率真值的块平均（模拟粗分辨率观测）
    truth_coarse = block_average(truth, coarse, coarse)

    info = {
        "bbox": bbox, "target_size": H, "coarse": coarse, "seed": seed,
        "true_lapse_rate_per_m": lapse_true,
        "dem_range_m": [float(dem.min()), float(dem.max())],
    }
    return {
        "dem": dem.astype(np.float32),
        "slope": slope.astype(np.float32),
        "truth": truth.astype(np.float32),
        "truth_coarse": truth_coarse.astype(np.float32),
        "info": info,
    }


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
    """Read multi-band GeoTIFF → (cube (nb, H, W) float32, bbox [W, S, E, N]).

    NoData values (from raster profile) are converted to NaN so the caller
    can mask them out via ``np.isfinite``.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        nodata = src.nodata
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    if nodata is not None:
        nd = float(nodata)
        cube = np.where(cube == nd, np.nan, cube)
    return cube, bbox


def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
            "target_resolution": getattr(args, "target_resolution", None),
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

    # target_resolution → 输出网格尺寸（像元数）
    target_size = max(int(args.target_resolution), 16)
    coarse = max(target_size // 8, 4)

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if cube.shape[0] < 3:
            raise ValidationError(
                "input raster must have >=3 bands (DEM, truth, coarse_climate); "
                f"got {cube.shape[0]}", bands=int(cube.shape[0]))
        dem_hr = cube[0].astype(np.float64)
        slope_hr = slope_from_dem(dem_hr)
        truth_hr = cube[1].astype(np.float64)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        met = generate_synthetic(bbox, target_size=target_size, coarse=coarse)
        dem_hr = met["dem"].astype(np.float64)
        slope_hr = met["slope"].astype(np.float64)
        truth_hr = met["truth"].astype(np.float64)
        synth_info = met["info"]
        source_note = "synthetic"

    # ---- validation (BEFORE os.makedirs to avoid empty output dirs) ----
    if bbox is None:
        raise UsageError("could not determine bbox")
    validate_bbox(bbox, ctx="bbox")
    if dem_hr.size == 0:
        raise ValidationError("DEM is empty")
    if args.input and not args.synthetic:
        valid_count = int(np.sum(np.isfinite(cube)))
        if valid_count == 0:
            raise ValidationError(
                f"input raster has no valid (non-NoData) pixels: {args.input}"
            )
    os.makedirs(output_dir, exist_ok=True)

    res = downscale(dem_hr, slope_hr, truth_hr, coarse=coarse)

    out_tif = os.path.join(output_dir, "downscaled.tif")
    write_geotiff(out_tif, res["downscaled"], bbox)

    diag_tif = os.path.join(output_dir, "downscaling_components.tif")
    stack = np.stack([res["regression"], res["residual"]], axis=0)
    write_geotiff(diag_tif, stack, bbox)

    report = {
        "source": source_note,
        "coarse_shape": res["coarse_shape"],
        "coefs": res["coefs"],
        "intercept": res["intercept"],
        "correlation": res["correlation"],
        "rmse": res["rmse"],
        "rmse_coarse_baseline": res["rmse_coarse_baseline"],
        "lapse_rate_per_m": res["lapse_rate_per_m"],
    }
    report_path = os.path.join(output_dir, "validation_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "correlation": res["correlation"],
        "rmse": res["rmse"],
        "rmse_coarse_baseline": res["rmse_coarse_baseline"],
        "lapse_rate_per_m": res["lapse_rate_per_m"],
        "elevation_coef": res["coefs"]["elevation"],
    }
    if synth_info is not None:
        qa["true_lapse_rate_per_m"] = synth_info["true_lapse_rate_per_m"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": diag_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 2},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] coarse grid: {res['coarse_shape']}  target: {dem_hr.shape}")
        print(f"[{SKILL_NAME}] elevation coef: {res['coefs']['elevation']:.5f}  "
              f"intercept: {res['intercept']:.3f}")
        print(f"[{SKILL_NAME}] corr: {res['correlation']:.4f}  rmse: {res['rmse']:.4f}  "
              f"(coarse baseline rmse: {res['rmse_coarse_baseline']:.4f})")
        print(f"[{SKILL_NAME}] lapse rate: {res['lapse_rate_per_m']:.5f} /m")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Statistical climate downscaling: terrain regression + residual interpolation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF (band1=DEM, band2=truth, band3=coarse climate)")
    p.add_argument("--target-resolution", type=int, default=64,
                   help="target fine-grid size in pixels (default: 64)")
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
