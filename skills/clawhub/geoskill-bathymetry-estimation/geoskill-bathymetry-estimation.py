#!/usr/bin/env python3
"""bathymetry-estimation — 遥感水深反演

从蓝、绿波段的底质反射信号反演浅海 / 湖泊水深，实现两种经典经验算法：

- **Stumpf 对数比值法**：``depth = m0 + m1 * ln(R_blue / R_green)``。
  清洁水体中蓝光衰减慢、绿光衰减快，蓝/绿比值随水深单调增大，
  取对数后与水深近似线性（Stumpf et al. 2003）。
- **Lyzenga 线性变换**：``depth = c0 + c1*ln(R_blue) + c2*ln(R_green)``，
  由多波段对数反射率的线性组合拟合水深（Lyzenga 1978 简化形式）。

两种方法的系数均可由实测校准点（``--calibration-points`` CSV，列为
blue,green,depth）经最小二乘拟合；合成模式下自动从真值水深采样生成校准点，
并给出 RMSE / MAE / R² 精度评估。

数据源：本地多波段 GeoTIFF（含蓝、绿波段）；或 ``--synthetic`` / 仅给
``--bbox`` 时离线生成按 Beer–Lambert 衰减的蓝绿反射率影像。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python bathymetry-estimation.py --bbox 116 39 117 40 --method stumpf
    python bathymetry-estimation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
    python bathymetry-estimation.py --input scene.tif --calibration-points calib.csv

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
SKILL_NAME = "bathymetry-estimation"

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


BLUE_IDX = 0
GREEN_IDX = 1
NODATA = -9999.0


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
def stumpf_depth(blue: np.ndarray, green: np.ndarray,
                 m0: float, m1: float, detect_floor: float = 0.02) -> np.ndarray:
    """Stumpf 对数比值水深：depth = m0 + m1 * ln(R_blue / R_green)。

    蓝或绿反射率低于 detect_floor（底质信号淹没在噪声中、水深不可反演）
    的像元返回 NODATA。
    """
    blue = blue.astype(np.float64)
    green = green.astype(np.float64)
    valid = (blue > detect_floor) & (green > detect_floor)
    depth = np.full(blue.shape, NODATA, dtype=np.float32)
    ratio = np.clip(blue[valid] / green[valid], 1e-6, None)
    depth[valid] = (m0 + m1 * np.log(ratio)).astype(np.float32)
    return depth


def lyzenga_depth(blue: np.ndarray, green: np.ndarray,
                  c0: float, c1: float, c2: float, detect_floor: float = 0.02) -> np.ndarray:
    """Lyzenga 线性变换水深：depth = c0 + c1*ln(R_blue) + c2*ln(R_green)。

    反射率低于 detect_floor 的像元（底质不可见）返回 NODATA。
    """
    blue = blue.astype(np.float64)
    green = green.astype(np.float64)
    valid = (blue > detect_floor) & (green > detect_floor)
    depth = np.full(blue.shape, NODATA, dtype=np.float32)
    depth[valid] = (c0 + c1 * np.log(blue[valid])
                    + c2 * np.log(green[valid])).astype(np.float32)
    return depth


def fit_stumpf(blue_s: np.ndarray, green_s: np.ndarray,
               depth_s: np.ndarray, eps: float = 1e-4) -> Tuple[float, float]:
    """由校准样本最小二乘拟合 Stumpf 系数 (m0, m1)。"""
    blue_s = np.asarray(blue_s, dtype=np.float64).ravel()
    green_s = np.asarray(green_s, dtype=np.float64).ravel()
    depth_s = np.asarray(depth_s, dtype=np.float64).ravel()
    valid = (blue_s > eps) & (green_s > eps)
    if valid.sum() < 2:
        raise ValidationError("need at least 2 valid calibration samples for Stumpf")
    x = np.log(blue_s[valid] / green_s[valid])
    A = np.column_stack([np.ones_like(x), x])
    coef, *_ = np.linalg.lstsq(A, depth_s[valid], rcond=None)
    return float(coef[0]), float(coef[1])


def fit_lyzenga(blue_s: np.ndarray, green_s: np.ndarray,
                depth_s: np.ndarray, eps: float = 1e-4) -> Tuple[float, float, float]:
    """由校准样本最小二乘拟合 Lyzenga 系数 (c0, c1, c2)。"""
    blue_s = np.asarray(blue_s, dtype=np.float64).ravel()
    green_s = np.asarray(green_s, dtype=np.float64).ravel()
    depth_s = np.asarray(depth_s, dtype=np.float64).ravel()
    valid = (blue_s > eps) & (green_s > eps)
    if valid.sum() < 3:
        raise ValidationError("need at least 3 valid calibration samples for Lyzenga")
    A = np.column_stack([np.ones_like(blue_s[valid]),
                         np.log(blue_s[valid]),
                         np.log(green_s[valid])])
    coef, *_ = np.linalg.lstsq(A, depth_s[valid], rcond=None)
    return float(coef[0]), float(coef[1]), float(coef[2])


def accuracy_metrics(estimated: np.ndarray, truth: np.ndarray) -> Dict[str, float]:
    """在有效（非 NODATA）像元上计算 RMSE / MAE / R²。"""
    valid = (estimated > NODATA / 2) & np.isfinite(estimated) & np.isfinite(truth)
    if valid.sum() == 0:
        return {"rmse": float("nan"), "mae": float("nan"),
                "r2": float("nan"), "n_valid": 0}
    e = estimated[valid].astype(np.float64)
    t = truth[valid].astype(np.float64)
    resid = e - t
    rmse = float(np.sqrt(np.mean(resid ** 2)))
    mae = float(np.mean(np.abs(resid)))
    ss_res = float(np.sum(resid ** 2))
    ss_tot = float(np.sum((t - np.mean(t)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 1e-9 else float("nan")
    return {"rmse": round(rmse, 4), "mae": round(mae, 4),
            "r2": round(r2, 6), "n_valid": int(valid.sum())}


def estimate_bathymetry(
    cube: np.ndarray,
    method: str = "stumpf",
    blue_index: int = BLUE_IDX,
    green_index: int = GREEN_IDX,
    calib_blue: Optional[np.ndarray] = None,
    calib_green: Optional[np.ndarray] = None,
    calib_depth: Optional[np.ndarray] = None,
    max_depth: float = 40.0,
    detect_floor: float = 0.02,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """统一入口：反演水深并返回 (depth (H,W), params_dict)。

    若提供校准样本则拟合系数，否则使用默认物理系数。反演结果裁剪到
    [0, max_depth]。
    """
    if cube.ndim != 3:
        raise ValidationError("cube must be multiband (bands, H, W)")
    nb = cube.shape[0]
    if max(blue_index, green_index) >= nb:
        raise ValidationError(
            f"band index out of range: blue={blue_index} green={green_index} "
            f"but cube has {nb} bands",
        )
    blue = cube[blue_index]
    green = cube[green_index]

    has_calib = (calib_blue is not None and calib_green is not None
                 and calib_depth is not None)

    if method == "stumpf":
        if has_calib:
            m0, m1 = fit_stumpf(calib_blue, calib_green, calib_depth)
        else:
            m0, m1 = -2.0, 12.0   # 默认经验系数
        depth = stumpf_depth(blue, green, m0, m1, detect_floor=detect_floor)
        coeffs = {"m0": round(m0, 6), "m1": round(m1, 6)}
    elif method == "lyzenga":
        if has_calib:
            c0, c1, c2 = fit_lyzenga(calib_blue, calib_green, calib_depth)
        else:
            c0, c1, c2 = 5.0, -6.0, 4.0
        depth = lyzenga_depth(blue, green, c0, c1, c2, detect_floor=detect_floor)
        coeffs = {"c0": round(c0, 6), "c1": round(c1, 6), "c2": round(c2, 6)}
    else:
        raise UsageError(f"unknown method '{method}'. Choose stumpf|lyzenga",
                         method=method)

    # 裁剪有效水深到 [0, max_depth]
    valid = depth > NODATA / 2
    depth[valid] = np.clip(depth[valid], 0.0, max_depth)

    params = {
        "method": method,
        "blue_index": blue_index,
        "green_index": green_index,
        "coefficients": coeffs,
        "calibrated": bool(has_calib),
        "n_calibration": int(len(calib_depth)) if has_calib else 0,
        "max_depth": max_depth,
        "water_pixels": int(valid.sum()),
        "mean_depth": round(float(np.nanmean(depth[valid])), 4) if valid.any() else None,
    }
    return depth.astype(np.float32), params


# ---------------------------------------------------------------------------
# 合成数据：Beer–Lambert 衰减的蓝绿反射率 + 真值水深
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    max_depth: float = 20.0,
    k_blue: float = 0.12,
    k_green: float = 0.28,
    albedo_blue: float = 0.50,
    albedo_green: float = 0.40,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 (4, H, W) 反射率立方体（蓝 绿 红 近红外）与真值水深 (H,W)。

    水深场为平滑斜坡（0→max_depth）。底质反射按 Beer–Lambert 衰减：
    R = albedo * exp(-2 * k * depth)，绿光衰减系数大于蓝光，
    使蓝/绿比值随水深单调增大（Stumpf 可精确恢复）。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yn = yy.astype(np.float64) / max(height - 1, 1)
    xn = xx.astype(np.float64) / max(width - 1, 1)

    depth = max_depth * np.clip(0.7 * xn + 0.3 * yn, 0.0, 1.0)

    blue = albedo_blue * np.exp(-2.0 * k_blue * depth)
    green = albedo_green * np.exp(-2.0 * k_green * depth)
    blue = blue + rng.normal(0, 0.003, size=blue.shape)
    green = green + rng.normal(0, 0.003, size=green.shape)

    cube = np.zeros((4, height, width), dtype=np.float32)
    cube[0] = np.clip(blue, 1e-4, 1.0).astype(np.float32)
    cube[1] = np.clip(green, 1e-4, 1.0).astype(np.float32)
    cube[2] = np.clip(0.3 * green, 1e-4, 1.0).astype(np.float32)   # 红（强吸收）
    cube[3] = np.clip(0.02 * np.ones_like(green), 1e-4, 1.0).astype(np.float32)  # NIR

    info = {
        "bbox": bbox, "width": width, "height": height,
        "max_depth": max_depth, "k_blue": k_blue, "k_green": k_green,
        "mean_true_depth": round(float(np.mean(depth)), 4),
    }
    return cube, depth.astype(np.float32), info


def sample_calibration(cube: np.ndarray, truth_depth: np.ndarray,
                       blue_index: int, green_index: int,
                       n: int = 200, seed: int = 1,
                       detect_floor: float = 0.02) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """从可反演水体（蓝绿反射率均高于 detect_floor）中随机采样校准点，
    返回 (blue, green, depth) 样本数组。"""
    rng = np.random.default_rng(seed)
    blue_band = cube[blue_index]
    green_band = cube[green_index]
    candidates = np.argwhere((blue_band > detect_floor) & (green_band > detect_floor))
    if len(candidates) == 0:
        raise ValidationError("no detectable water pixels available for calibration")
    k = min(n, len(candidates))
    sel = rng.choice(len(candidates), size=k, replace=False)
    rows = candidates[sel, 0]
    cols = candidates[sel, 1]
    return (cube[blue_index, rows, cols].astype(np.float64),
            cube[green_index, rows, cols].astype(np.float64),
            truth_depth[rows, cols].astype(np.float64))


def read_calibration_csv(path: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """读取校准 CSV（列：blue,green,depth；可含表头）。"""
    if not os.path.exists(path):
        raise UsageError(f"calibration file not found: {path}", path=path)
    rows: List[List[float]] = []
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            parts = [p for p in line.replace(";", ",").split(",") if p.strip()]
            try:
                vals = [float(x) for x in parts]
            except ValueError:
                if i == 0:
                    continue  # 跳过表头
                raise ValidationError(f"non-numeric calibration row {i + 1}: {line}")
            if len(vals) < 3:
                raise ValidationError(f"calibration row {i + 1} needs 3 columns: {line}")
            rows.append(vals[:3])
    if len(rows) < 2:
        raise ValidationError("calibration CSV needs at least 2 data rows")
    arr = np.asarray(rows, dtype=np.float64)
    return arr[:, 0], arr[:, 1], arr[:, 2]


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
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


def write_geotiff(path, array, bbox, dtype="float32", nodata=NODATA):
    import rasterio
    from rasterio.transform import from_bounds
    if array.ndim == 2:
        array = array[np.newaxis, ...]
    nb, h, w = array.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(array[b].astype(dtype), b + 1)


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
            "calibration_points": getattr(args, "calibration_points", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
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

    truth_depth: Optional[np.ndarray] = None
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, truth_depth, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    # ---- validation (BEFORE os.makedirs to avoid empty output dirs) ----
    if bbox is None:
        raise UsageError("could not determine bbox")
    validate_bbox(bbox, ctx="bbox")
    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if args.input and not args.synthetic:
        valid_count = int(np.sum(np.isfinite(cube)))
        if valid_count == 0:
            raise ValidationError(
                f"input raster has no valid (non-NoData) pixels: {args.input}"
            )
    os.makedirs(output_dir, exist_ok=True)

    # 校准样本：优先 CSV，其次合成模式自动采样
    calib = (None, None, None)
    if args.calibration_points:
        calib = read_calibration_csv(args.calibration_points)
    elif truth_depth is not None:
        calib = sample_calibration(cube, truth_depth,
                                   args.blue_index, args.green_index)

    depth, params = estimate_bathymetry(
        cube, method=args.method,
        blue_index=args.blue_index, green_index=args.green_index,
        calib_blue=calib[0], calib_green=calib[1], calib_depth=calib[2],
        max_depth=args.max_depth,
    )

    # 精度评估（有真值时）
    acc = None
    if truth_depth is not None:
        acc = accuracy_metrics(depth, truth_depth)
        params["accuracy"] = acc

    out_tif = os.path.join(output_dir, "bathymetry.tif")
    write_geotiff(out_tif, depth, bbox)

    acc_path = os.path.join(output_dir, "accuracy.json")
    with open(acc_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {"source": source_note, "method": args.method}
    qa.update({k: params[k] for k in
               ("water_pixels", "mean_depth", "calibrated", "n_calibration")})
    if acc is not None:
        qa.update(acc)
    if synth_info is not None:
        qa["mean_true_depth"] = synth_info["mean_true_depth"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": acc_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  calibrated: {params['calibrated']}")
        print(f"[{SKILL_NAME}] water pixels: {params['water_pixels']}")
        print(f"[{SKILL_NAME}] mean depth: {params['mean_depth']}")
        if acc is not None:
            print(f"[{SKILL_NAME}] RMSE: {acc['rmse']}  R2: {acc['r2']}")
        print(f"[{SKILL_NAME}] depth raster: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Estimate water depth from blue/green bands (Stumpf / Lyzenga).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multiband GeoTIFF (needs blue & green bands)")
    p.add_argument("--method", default="stumpf", choices=["stumpf", "lyzenga"],
                   help="retrieval method (default: stumpf)")
    p.add_argument("--blue-index", type=int, default=BLUE_IDX,
                   help="0-based band index for blue (default: 0)")
    p.add_argument("--green-index", type=int, default=GREEN_IDX,
                   help="0-based band index for green (default: 1)")
    p.add_argument("--calibration-points", default=None,
                   help="CSV of calibration samples: columns blue,green,depth")
    p.add_argument("--max-depth", type=float, default=40.0,
                   help="clip retrieved depth to this maximum in meters (default: 40)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic bathymetric scene (offline)")
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
