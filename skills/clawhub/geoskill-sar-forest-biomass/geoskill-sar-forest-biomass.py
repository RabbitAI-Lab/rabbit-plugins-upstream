#!/usr/bin/env python3
"""sar-forest-biomass — SAR森林生物量估算

从 SAR 后向散射系数 σ⁰ 估算森林地上生物量 AGB（above-ground biomass, t/ha）。
实现两类经验关系：

- **线性模型**：σ⁰_dB = m·AGB + c，反演 AGB = (σ⁰_dB − c)/m。适用于低生物量、
  未饱和区间。
- **饱和模型**：σ⁰_lin = −(1/k)·ln(1 − AGB/AGB_sat)，即 AGB = AGB_sat·(1−e^(−k·σ⁰_lin))。
  刻画 SAR 后向散射随生物量增加趋于饱和的物理特征（高 AGB 区敏感度下降）。

支持 ``--calibration`` 提供地面样本 CSV（列 ``sigma0,agb``，σ⁰ 单位 dB）：
- 线性：最小二乘拟合 AGB = a·σ⁰ + b；
- 饱和：非线性最小二乘（scipy curve_fit）拟合 AGB_sat、k。
无标定文件时使用按波段（C / L）内置的默认系数（L 波段穿透性强，AGB_sat 更高）。

数据源：本地 σ⁰ (dB) GeoTIFF，或 ``--synthetic`` 生成的空间变化 AGB 场经模型正演的
模拟场景（含观测噪声），用于离线验证估算精度。

隐私声明 / Privacy：
- 默认离线运行，仅在显式解析地名时才访问网络。
- ``--synthetic`` 模式完全无网络。所有处理在本地完成，不上传任何用户数据。

Usage:
    python sar-forest-biomass.py --bbox 110 22 111 23 --band l --synthetic --output-dir ./out
    python sar-forest-biomass.py --input sigma0.tif --band c --calibration samples.csv --output-dir ./out

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
SKILL_NAME = "sar-forest-biomass"

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
# 默认系数：按 (band, model) 组织
#   linear:     σ⁰_dB = m·AGB + c
#   saturation: σ⁰_lin = -(1/k)·ln(1 - AGB/AGB_sat)
# L 波段穿透性强，饱和生物量 AGB_sat 更高。
# ---------------------------------------------------------------------------
DEFAULT_COEFS: Dict[Tuple[str, str], Dict[str, float]] = {
    ("c", "linear"): {"m": 0.033, "c": -15.0},
    ("c", "saturation"): {"agb_sat": 250.0, "k": 1.5},
    ("l", "linear"): {"m": 0.028, "c": -14.0},
    ("l", "saturation"): {"agb_sat": 450.0, "k": 1.0},
}
AGB_MAX = 500.0


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法：σ⁰ <-> AGB 正演/反演
# ---------------------------------------------------------------------------
def forward_sigma0_db(agb: np.ndarray, model: str, coefs: Dict[str, float]) -> np.ndarray:
    """由 AGB (t/ha) 正演 σ⁰ (dB)。"""
    agb = np.asarray(agb, dtype=np.float64)
    if model == "linear":
        return coefs["m"] * agb + coefs["c"]
    if model == "saturation":
        agb_sat = coefs["agb_sat"]
        k = coefs["k"]
        ratio = np.clip(1.0 - agb / agb_sat, 1e-6, None)
        sigma0_lin = -(1.0 / k) * np.log(ratio)
        return 10.0 * np.log10(sigma0_lin)
    raise UsageError(f"unknown model '{model}', choose linear|saturation")


def invert_biomass(
    sigma0_db: np.ndarray, model: str, coefs: Dict[str, float],
    agb_max: float = AGB_MAX,
) -> np.ndarray:
    """由 σ⁰ (dB) 反演 AGB (t/ha)，裁剪到 [0, agb_max]。"""
    if agb_max <= 0:
        raise ValidationError(f"agb_max must be >0, got {agb_max}")
    sigma0_db = np.asarray(sigma0_db, dtype=np.float64)
    if model == "linear":
        if coefs["m"] == 0:
            raise ProcessError("linear model slope m is zero")
        agb = (sigma0_db - coefs["c"]) / coefs["m"]
    elif model == "saturation":
        agb_sat = coefs["agb_sat"]
        k = coefs["k"]
        sigma0_lin = np.power(10.0, sigma0_db / 10.0)
        agb = agb_sat * (1.0 - np.exp(-k * sigma0_lin))
    else:
        raise UsageError(f"unknown model '{model}', choose linear|saturation")
    return np.clip(agb, 0.0, agb_max)


# ---------------------------------------------------------------------------
# 标定：由地面样本拟合系数
# ---------------------------------------------------------------------------
def calibrate_linear(sigma0_db: np.ndarray, agb: np.ndarray) -> Dict[str, float]:
    """最小二乘拟合线性反演式 AGB = a·σ⁰ + b，返回正演系数 {m, c}。"""
    a, b = np.polyfit(np.asarray(sigma0_db, float).ravel(),
                      np.asarray(agb, float).ravel(), 1)
    if a == 0:
        raise ProcessError("degenerate calibration: zero slope")
    return {"m": float(1.0 / a), "c": float(-b / a)}


def calibrate_saturation(sigma0_db: np.ndarray, agb: np.ndarray) -> Dict[str, float]:
    """非线性最小二乘拟合饱和式 AGB = AGB_sat·(1 − e^(−k·σ⁰_lin))。"""
    from scipy.optimize import curve_fit

    sigma0_lin = np.power(10.0, np.asarray(sigma0_db, float).ravel() / 10.0)
    y = np.asarray(agb, float).ravel()

    def f(s, agb_sat, k):
        return agb_sat * (1.0 - np.exp(-k * s))

    p0 = [float(np.percentile(y, 95)) * 1.2 + 1.0, 1.0]
    popt, _ = curve_fit(f, sigma0_lin, y, p0=p0, maxfev=20000,
                        bounds=([1.0, 1e-4], [1e5, 1e3]))
    return {"agb_sat": float(popt[0]), "k": float(popt[1])}


def load_calibration_csv(path: str) -> Tuple[np.ndarray, np.ndarray]:
    """读取标定 CSV（列 sigma0,agb），返回 (sigma0_db, agb)。"""
    import pandas as pd
    if not os.path.exists(path):
        raise UsageError(f"calibration file not found: {path}", path=path)
    df = pd.read_csv(path)
    cols = {c.strip().lower(): c for c in df.columns}
    if "sigma0" not in cols or "agb" not in cols:
        raise ValidationError(
            f"calibration CSV must have columns 'sigma0' and 'agb', got {list(df.columns)}",
        )
    s = df[cols["sigma0"]].to_numpy(float)
    a = df[cols["agb"]].to_numpy(float)
    mask = np.isfinite(s) & np.isfinite(a)
    if mask.sum() < 3:
        raise ValidationError("calibration needs at least 3 valid samples")
    return s[mask], a[mask]


# ---------------------------------------------------------------------------
# 合成数据：AGB 场 → 模型正演 σ⁰
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float], width: int = 64, height: int = 64,
    band: str = "c", model: str = "saturation", noise_db: float = 0.4,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成空间变化 AGB 场，经 (band, model) 默认系数正演为 σ⁰_dB（含噪声）。

    返回 (sigma0_db (H,W), info)，info 含真值 agb_truth 与所用系数。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float64) / max(width - 1, 1)
    yn = yy.astype(np.float64) / max(height - 1, 1)

    coefs = DEFAULT_COEFS[(band, model)]
    agb_cap = min(0.8 * coefs.get("agb_sat", 300.0), 300.0) if model == "saturation" else 250.0
    agb = (25.0 + (agb_cap - 40.0) * xn + 25.0 * np.sin(2.0 * np.pi * yn)
           + rng.normal(0.0, 8.0, size=(height, width)))
    agb = np.clip(agb, 5.0, agb_cap)

    sigma0 = forward_sigma0_db(agb, model, coefs)
    sigma0 = sigma0 + rng.normal(0.0, noise_db, size=(height, width))

    info = {
        "bbox": bbox, "width": width, "height": height,
        "band": band, "model": model, "noise_db": noise_db,
        "coefs": coefs,
        "agb_truth": agb.astype(np.float32),
        "agb_truth_mean": float(agb.mean()),
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


def read_geotiff_full(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """扩展版 read：同时返回 nodata 值（若无则为 None）。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        arr = src.read(1).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
        if nodata is not None:
            nodata = float(nodata)
    return arr, bbox, nodata


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Optional[List[float]]) -> List[float]:
    """校验地理 bbox 合法性，失败抛 ValidationError（exit 6）。"""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats [W S E N]")
    try:
        w, s, e, n = [float(x) for x in bbox]
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox entries must be numeric: {exc}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"latitude out of [-90,90]: S={s}, N={n}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"longitude out of [-180,180]: W={w}, E={e}")
    if s >= n:
        raise ValidationError(
            f"S >= N (S={s}, N={n}); bbox inverted (S must be < N)"
        )
    if w >= e:
        raise ValidationError(
            f"W >= E (W={w}, E={e}); cross-180° bbox not supported. "
            f"Split into two non-antipodal bboxes."
        )
    if (e - w) < 0.001 or (n - s) < 0.001:
        raise ValidationError(
            f"bbox too small ({(e-w):.6f}°×{(n-s):.6f}°); min span is 0.001°"
        )
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox,
                   input_nodata=None):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "band": getattr(args, "band", None),
            "model": getattr(args, "model", None),
            "calibration": getattr(args, "calibration", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
            "input_nodata": input_nodata,
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
        sigma0, file_bbox, src_nodata = read_geotiff_full(args.input)
        input_nodata = src_nodata
        if bbox is not None:
            bbox = validate_bbox(bbox)
        else:
            bbox = validate_bbox(file_bbox)
        # NoData 处理
        if src_nodata is not None:
            n_total = int(sigma0.size)
            n_nd = int(np.count_nonzero(sigma0 == src_nodata))
            n_valid_pixels = n_total - n_nd
            if n_valid_pixels == 0:
                raise ValidationError(
                    f"input raster has no valid pixels "
                    f"(all {n_nd}/{n_total} are NoData={src_nodata})",
                    path=args.input, nodata=src_nodata,
                )
            sigma0 = np.where(sigma0 == src_nodata, np.nan, sigma0).astype(np.float32)
        else:
            n_valid_pixels = int(sigma0.size)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        sigma0, synth_info = generate_synthetic(bbox, band=args.band, model=args.model)
        n_valid_pixels = int(sigma0.size)
        source_note = "synthetic"

    if sigma0.size == 0:
        raise ValidationError("input raster is empty")

    # 校验通过后再建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 系数：标定优先，否则用 (band, model) 默认
    calibrated = False
    if args.calibration:
        cal_s, cal_a = load_calibration_csv(args.calibration)
        if args.model == "linear":
            coefs = calibrate_linear(cal_s, cal_a)
        else:
            coefs = calibrate_saturation(cal_s, cal_a)
        calibrated = True
    else:
        coefs = DEFAULT_COEFS[(args.band, args.model)]

    agb = invert_biomass(sigma0, args.model, coefs, agb_max=AGB_MAX).astype(np.float32)
    # 保留 NoData 块为 NaN（仅对部分 NoData 情况；全 NoData 已被前置校验拒收）
    if input_nodata is not None and np.any(np.isnan(agb)):
        # invert_biomass 已对 NaN 显式返回 NaN（np.log(np.nan)=nan）
        pass  # NaN-safe 已内置于 np 算子

    out_tif = os.path.join(output_dir, "forest_biomass.tif")
    write_geotiff(out_tif, agb, bbox)

    qa: Dict[str, Any] = {
        "source": source_note, "band": args.band, "model": args.model,
        "calibrated": calibrated,
        "agb_mean_tha": float(np.nanmean(agb)) if np.any(np.isfinite(agb)) else 0.0,
        "agb_std_tha": float(np.nanstd(agb)) if np.any(np.isfinite(agb)) else 0.0,
        "agb_range_tha": [float(np.nanmin(agb)) if np.any(np.isfinite(agb)) else 0.0,
                           float(np.nanmax(agb)) if np.any(np.isfinite(agb)) else 0.0],
        "n_valid_pixels": int(n_valid_pixels) if n_valid_pixels is not None else None,
        "input_nodata": input_nodata,
    }
    truth = None
    if synth_info is not None:
        truth = synth_info["agb_truth"]
        rmse = float(np.sqrt(np.mean((agb - truth) ** 2)))
        corr = float(np.corrcoef(agb.ravel(), truth.ravel())[0, 1])
        bias = float(np.mean(agb - truth))
        rel_rmse = rmse / max(float(truth.mean()), 1e-6)
        qa["agb_truth_mean_tha"] = float(truth.mean())
        qa["rmse_tha"] = rmse
        qa["bias_tha"] = bias
        qa["correlation"] = corr
        qa["relative_rmse"] = rel_rmse

    report = {
        "band": args.band, "model": args.model,
        "coefficients": coefs, "calibrated": calibrated,
        "agb_max_tha": AGB_MAX,
        "statistics": {
            "agb_mean_tha": qa["agb_mean_tha"],
            "agb_std_tha": qa["agb_std_tha"],
            "agb_range_tha": qa["agb_range_tha"],
        },
    }
    if truth is not None:
        report["validation"] = {
            "rmse_tha": qa["rmse_tha"], "bias_tha": qa["bias_tha"],
            "correlation": qa["correlation"], "relative_rmse": qa["relative_rmse"],
        }
    report_path = os.path.join(output_dir, "biomass_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox,
                              input_nodata=input_nodata)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] band: {args.band}  model: {args.model}  calibrated: {calibrated}")
        print(f"[{SKILL_NAME}] mean AGB: {qa['agb_mean_tha']:.2f} t/ha")
        if truth is not None:
            print(f"[{SKILL_NAME}] RMSE={qa['rmse_tha']:.2f} t/ha  corr={qa['correlation']:.3f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="SAR forest above-ground biomass estimation from sigma0 using linear/saturation models.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input sigma0 (dB) GeoTIFF")
    p.add_argument("--band", default="c", choices=["c", "l"],
                   help="SAR frequency band (default: c)")
    p.add_argument("--model", default="saturation", choices=["linear", "saturation"],
                   help="sigma0-AGB model (default: saturation)")
    p.add_argument("--calibration",
                   help="optional CSV with columns 'sigma0','agb' for coefficient fitting")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic forest biomass scene (offline)")
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
