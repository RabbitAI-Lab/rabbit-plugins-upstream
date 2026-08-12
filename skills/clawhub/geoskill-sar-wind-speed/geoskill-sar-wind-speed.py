#!/usr/bin/env python3
"""sar-wind-speed — SAR海面风场反演

从 SAR 后向散射系数 σ⁰ 反演海面风速。实现简化的 CMOD（C-band Model）经验
地球物理模型函数：

    σ⁰_dB(U, φ, θ) = [a0 + a1·θ] + [s0 + s1·θ]·U·M(φ)

其中 U 为 10 m 高度风速 (m/s)，θ 为入射角 (°)，φ 为风向与雷达视线（方位向）
夹角，M(φ) = 1 + m1·cosφ + m2·cos2φ 为方位向调制函数（迎风 > 侧风 > 顺风）。
a0,a1,s0,s1,m1,m2 依 CMOD5 / CMOD7 取不同的经验系数。

反演：给定风向外推方位调制后，σ⁰_dB 对 U 单调递增，用二分法在 [U_min, U_max]
数值求根（向量化迭代），逐像元恢复风速。

数据源：本地 σ⁰（dB）GeoTIFF，或 ``--synthetic`` 生成的空间变化风场经 CMOD 正演
得到的模拟 σ⁰ 场景（含观测噪声），用于离线验证反演精度。

隐私声明 / Privacy：
- 默认离线运行，仅在显式解析地名时才访问网络。
- ``--synthetic`` 模式完全无网络。所有处理在本地完成，不上传任何用户数据。

Usage:
    python sar-wind-speed.py --bbox 121 30 122 31 --wind-dir 45 --cmod cmod5 --synthetic
    python sar-wind-speed.py --input sigma0.tif --wind-dir 90 --output-dir ./out

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
SKILL_NAME = "sar-wind-speed"

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


# ---------------------------------------------------------------------------
# CMOD 经验系数（简化标定值）：
#   σ⁰_dB = (a0 + a1·θ) + (s0 + s1·θ)·U·M(φ)
#   M(φ) = 1 + m1·cosφ + m2·cos2φ
# ---------------------------------------------------------------------------
CMOD_COEFS: Dict[str, Dict[str, float]] = {
    "cmod5": {"a0": -12.0, "a1": -0.120, "s0": 0.850, "s1": -0.006,
              "m1": 0.25, "m2": 0.10},
    "cmod7": {"a0": -12.3, "a1": -0.123, "s0": 0.840, "s1": -0.006,
              "m1": 0.27, "m2": 0.11},
}

U_MIN = 0.0
U_MAX = 45.0


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法：CMOD 正演 + 二分反演
# ---------------------------------------------------------------------------
def azimuth_modulation(rel_wind_dir_deg: np.ndarray, m1: float, m2: float) -> np.ndarray:
    """方位向调制 M(φ) = 1 + m1·cosφ + m2·cos2φ。"""
    phi = np.deg2rad(np.asarray(rel_wind_dir_deg, dtype=np.float64))
    return 1.0 + m1 * np.cos(phi) + m2 * np.cos(2.0 * phi)


def cmod_sigma0_db(
    wind_speed: np.ndarray, rel_wind_dir_deg: float, incidence_deg: float,
    model: str = "cmod5",
) -> np.ndarray:
    """CMOD 正演：由风速、相对风向、入射角计算 σ⁰ (dB)。"""
    if model not in CMOD_COEFS:
        raise UsageError(f"unknown cmod model '{model}', choose from {sorted(CMOD_COEFS)}")
    if not 0.0 <= incidence_deg <= 70.0:
        raise ValidationError(f"incidence angle must be in [0,70], got {incidence_deg}")
    c = CMOD_COEFS[model]
    base = c["a0"] + c["a1"] * incidence_deg
    slope = c["s0"] + c["s1"] * incidence_deg
    mod = azimuth_modulation(rel_wind_dir_deg, c["m1"], c["m2"])
    u = np.asarray(wind_speed, dtype=np.float64)
    return base + slope * u * mod


def cmod_invert_wind(
    sigma0_db: np.ndarray, rel_wind_dir_deg: float, incidence_deg: float,
    model: str = "cmod5", u_min: float = U_MIN, u_max: float = U_MAX,
    n_iter: int = 60,
) -> np.ndarray:
    """二分法数值反演风速（向量化）。σ⁰_dB 对 U 单调递增，保证收敛。

    低于/高于可反演范围的像元分别截断到 u_min / u_max。
    """
    if u_min >= u_max:
        raise ValidationError(f"need u_min < u_max, got {u_min},{u_max}")
    target = np.asarray(sigma0_db, dtype=np.float64)
    lo = np.full(target.shape, u_min, dtype=np.float64)
    hi = np.full(target.shape, u_max, dtype=np.float64)
    for _ in range(n_iter):
        mid = 0.5 * (lo + hi)
        fwd = cmod_sigma0_db(mid, rel_wind_dir_deg, incidence_deg, model)
        too_low = fwd < target  # 正演偏小 → 风速应增大
        lo = np.where(too_low, mid, lo)
        hi = np.where(too_low, hi, mid)
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------------------
# 合成数据：空间变化风场 → CMOD 正演 σ⁰
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float], width: int = 64, height: int = 64,
    wind_dir: float = 45.0, incidence_deg: float = 40.0,
    model: str = "cmod5", radar_azimuth: float = 0.0,
    noise_db: float = 0.25, seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成空间变化风速场，经 CMOD 正演为 σ⁰_dB（含观测噪声）。

    返回 (sigma0_db (H,W), info)，info 含真值风速场 wind_truth。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float64) / max(width - 1, 1)
    yn = yy.astype(np.float64) / max(height - 1, 1)

    # 真值风速场：基准 + 东西梯度 + 经向波动 + 纹理噪声
    wind = (7.0 + 5.0 * xn + 2.5 * np.sin(2.0 * np.pi * yn)
            + rng.normal(0.0, 0.4, size=(height, width)))
    wind = np.clip(wind, 1.0, 30.0)

    rel = wind_dir - radar_azimuth
    sigma0 = cmod_sigma0_db(wind, rel, incidence_deg, model)
    sigma0 = sigma0 + rng.normal(0.0, noise_db, size=(height, width))

    info = {
        "bbox": bbox, "width": width, "height": height,
        "wind_dir_deg": wind_dir, "incidence_deg": incidence_deg,
        "radar_azimuth_deg": radar_azimuth, "model": model,
        "noise_db": noise_db,
        "wind_truth_mean": float(wind.mean()),
        "wind_truth_std": float(wind.std()),
        "wind_truth": wind.astype(np.float32),
    }
    return sigma0.astype(np.float32), info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, array: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0) -> None:
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
        arr = src.read(1).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return arr, bbox


def read_geotiff_full(path: str) -> Tuple[np.ndarray, List[float], float]:
    """Read single-band GeoTIFF, replace nodata with NaN, validate n_valid_pixels.

    Returns (array_with_nan, bbox, nodata). Raises ValidationError if all pixels are
    NoData. nodata may be None if file has no nodata tag.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        arr = src.read(1).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None and np.isfinite(nodata):
        arr = np.where(arr == nodata, np.nan, arr)
    n_valid = int(np.sum(np.isfinite(arr)))
    if n_valid == 0:
        raise ValidationError(
            f"input raster has no valid pixels (all {arr.size} are NoData={nodata})"
        )
    return arr, bbox, nodata


def validate_bbox(bbox: List[float]) -> None:
    """Validate bbox = [W, S, E, N]. Raise ValidationError on W>=E, S>=N, out-of-range,
    or cross-180° antipodal bbox."""
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise ValidationError(f"bbox must be 4 floats [W S E N], got {bbox}")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"longitude out of range [-180,180]: W={w}, E={e}"
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"latitude out of range [-90,90]: S={s}, N={n}"
        )
    if w >= e:
        if abs(e - (-180.0)) < 1e-9 and w > 0:
            raise ValidationError(
                f"cross-180° bbox not supported (W={w}, E={e}); "
                f"split into two non-antipodal bboxes"
            )
        raise ValidationError(f"W must be < E, got W={w}, E={e}")
    if s >= n:
        raise ValidationError(f"S must be < N, got S={s}, N={n}")
    if (e - w) < 0.001 or (n - s) < 0.001:
        raise ValidationError(
            f"bbox too small (<0.001°), got W={w},S={s},E={e},N={n}"
        )


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
            "cmod": getattr(args, "cmod", None),
            "wind_dir": getattr(args, "wind_dir", None),
            "incidence_angle": getattr(args, "incidence_angle", None),
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
    synth_info: Optional[Dict[str, Any]] = None
    input_nodata: Optional[float] = None
    n_valid_pixels: Optional[int] = None

    if args.input and not args.synthetic:
        if bbox is not None:
            validate_bbox(bbox)
        sigma0, file_bbox, input_nodata = read_geotiff_full(args.input)
        bbox = bbox if bbox is not None else file_bbox
        n_valid_pixels = int(np.sum(np.isfinite(sigma0)))
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        sigma0, synth_info = generate_synthetic(
            bbox, wind_dir=args.wind_dir, incidence_deg=args.incidence_angle,
            model=args.cmod, radar_azimuth=args.radar_azimuth,
        )
        n_valid_pixels = int(sigma0.size)
        source_note = "synthetic"

    if sigma0.size == 0:
        raise ValidationError("input raster is empty")

    # Now safe to create output dir
    os.makedirs(output_dir, exist_ok=True)

    rel = args.wind_dir - args.radar_azimuth
    wind = cmod_invert_wind(sigma0, rel, args.incidence_angle, model=args.cmod)
    wind = wind.astype(np.float32)

    out_tif = os.path.join(output_dir, "wind_speed.tif")
    write_geotiff(out_tif, wind, bbox)

    # QA：合成模式下评估反演精度
    qa: Dict[str, Any] = {
        "source": source_note, "model": args.cmod,
        "wind_dir_deg": args.wind_dir, "incidence_deg": args.incidence_angle,
        "retrieved_mean_ms": float(np.nanmean(wind)),
        "retrieved_std_ms": float(np.nanstd(wind)),
        "retrieved_range_ms": [float(np.nanmin(wind)), float(np.nanmax(wind))],
        "n_valid_pixels": n_valid_pixels,
        "input_nodata": input_nodata,
    }
    truth = None
    if synth_info is not None:
        truth = synth_info["wind_truth"]
        rmse = float(np.sqrt(np.mean((wind - truth) ** 2)))
        corr = float(np.corrcoef(wind.ravel(), truth.ravel())[0, 1])
        bias = float(np.mean(wind - truth))
        qa["truth_mean_ms"] = float(truth.mean())
        qa["rmse_ms"] = rmse
        qa["bias_ms"] = bias
        qa["correlation"] = corr

    c = CMOD_COEFS[args.cmod]
    params = {
        "model": args.cmod,
        "coefficients": c,
        "wind_dir_deg": args.wind_dir,
        "radar_azimuth_deg": args.radar_azimuth,
        "incidence_deg": args.incidence_angle,
        "u_range_ms": [U_MIN, U_MAX],
        "azimuth_modulation": float(azimuth_modulation(rel, c["m1"], c["m2"])),
    }
    params_path = os.path.join(output_dir, "retrieval_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] model: {args.cmod}  wind_dir: {args.wind_dir}°  "
              f"incidence: {args.incidence_angle}°")
        print(f"[{SKILL_NAME}] retrieved mean wind: {qa['retrieved_mean_ms']:.2f} m/s")
        if truth is not None:
            print(f"[{SKILL_NAME}] RMSE={qa['rmse_ms']:.3f} m/s  corr={qa['correlation']:.3f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="SAR sea-surface wind speed retrieval using simplified CMOD geophysical model.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input sigma0 (dB) GeoTIFF")
    p.add_argument("--wind-dir", type=float, default=45.0,
                   help="meteorological wind direction in degrees (default: 45)")
    p.add_argument("--radar-azimuth", type=float, default=0.0,
                   help="radar look/azimuth direction in degrees (default: 0)")
    p.add_argument("--incidence-angle", type=float, default=40.0,
                   help="radar incidence angle in degrees (default: 40)")
    p.add_argument("--cmod", default="cmod5", choices=["cmod5", "cmod7"],
                   help="CMOD model variant (default: cmod5)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic wind field + sigma0 scene (offline)")
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
