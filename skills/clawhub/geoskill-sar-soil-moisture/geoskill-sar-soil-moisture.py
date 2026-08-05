#!/usr/bin/env python3
"""sar-soil-moisture — SAR土壤湿度反演

从 SAR 后向散射系数 σ⁰ 反演裸土地表土壤体积含水量 mv (m³/m³)。实现两类简化
半经验物理模型（Dubois / Oh 的标定形式）：

    σ⁰_dB(mv, ks, θ) = A(θ) + B(θ)·(k·s) + C(θ)·mv

其中 θ 为入射角，k = 2π/λ 为雷达波数（默认 C 波段 λ=5.6 cm），s 为地表 RMS
高度（粗糙度），ks = k·s 为归一化粗糙度。A 为入射角相关的基准项、B 为粗糙度
敏感项、C(θ) ∝ cos²θ 为湿度敏感项（随入射角增大而降低）。Dubois 与 Oh 采用
不同的经验标定系数。

反演：σ⁰_dB 对 mv 单调线性，给定入射角与粗糙度 ks 即可解析求解
    mv = (σ⁰_dB − A(θ) − B(θ)·ks) / C(θ)
并裁剪到物理有效范围 [MV_MIN, MV_MAX] = [0.01, 0.60] m³/m³。

数据源：本地 σ⁰ (dB) GeoTIFF，或 ``--synthetic`` 生成的空间变化土壤湿度场与粗糙度
场经模型正演的模拟场景（含观测噪声），用于离线验证反演精度。

隐私声明 / Privacy：
- 默认离线运行，仅在显式解析地名时才访问网络。
- ``--synthetic`` 模式完全无网络。所有处理在本地完成，不上传任何用户数据。

Usage:
    python sar-soil-moisture.py --bbox 116 39 117 40 --incidence-angle 40 --model dubois --synthetic
    python sar-soil-moisture.py --input sigma0.tif --model oh --output-dir ./out

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
SKILL_NAME = "sar-soil-moisture"

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
# 模型系数（简化标定形式）：
#   σ⁰_dB = (a0 + a1·θ) + (b0 + b1·θ)·ks + c0·cos²θ·mv
# ---------------------------------------------------------------------------
MODEL_COEFS: Dict[str, Dict[str, float]] = {
    "dubois": {"a0": -12.0, "a1": -0.050, "b0": 2.00, "b1": -0.004, "c0": 25.0},
    "oh":     {"a0": -13.0, "a1": -0.045, "b0": 2.30, "b1": -0.005, "c0": 22.0},
}

WAVELENGTH_M = 0.056  # C 波段约 5.6 cm
MV_MIN = 0.01
MV_MAX = 0.60


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法：半经验正演 + 解析反演
# ---------------------------------------------------------------------------
def radar_wavenumber(wavelength_m: float = WAVELENGTH_M) -> float:
    """雷达波数 k = 2π/λ (rad/m)。"""
    if wavelength_m <= 0:
        raise ValidationError(f"wavelength must be >0, got {wavelength_m}")
    return float(2.0 * np.pi / wavelength_m)


def _model_terms(incidence_deg: float, model: str) -> Tuple[float, float, float]:
    """返回 (A, B, C) 三项系数：A 基准、B 粗糙度敏感、C 湿度敏感。"""
    if model not in MODEL_COEFS:
        raise UsageError(f"unknown model '{model}', choose from {sorted(MODEL_COEFS)}")
    if not 0.0 <= incidence_deg <= 70.0:
        raise ValidationError(f"incidence angle must be in [0,70], got {incidence_deg}")
    c = MODEL_COEFS[model]
    theta = float(incidence_deg)
    A = c["a0"] + c["a1"] * theta
    B = c["b0"] + c["b1"] * theta
    C = c["c0"] * (np.cos(np.deg2rad(theta)) ** 2)
    return float(A), float(B), float(C)


def backscatter_db(
    mv: np.ndarray, ks: np.ndarray, incidence_deg: float, model: str = "dubois",
) -> np.ndarray:
    """半经验模型正演：由土壤湿度 mv、归一化粗糙度 ks、入射角计算 σ⁰ (dB)。"""
    A, B, C = _model_terms(incidence_deg, model)
    mv_a = np.asarray(mv, dtype=np.float64)
    ks_a = np.asarray(ks, dtype=np.float64)
    return A + B * ks_a + C * mv_a


def invert_soil_moisture(
    sigma0_db: np.ndarray, ks: np.ndarray, incidence_deg: float,
    model: str = "dubois", mv_min: float = MV_MIN, mv_max: float = MV_MAX,
) -> np.ndarray:
    """解析反演土壤湿度 mv (m³/m³)，并裁剪到 [mv_min, mv_max]。"""
    if mv_min >= mv_max:
        raise ValidationError(f"need mv_min < mv_max, got {mv_min},{mv_max}")
    A, B, C = _model_terms(incidence_deg, model)
    if C <= 0:
        raise ProcessError(f"non-positive moisture sensitivity C={C}")
    sigma0 = np.asarray(sigma0_db, dtype=np.float64)
    ks_a = np.asarray(ks, dtype=np.float64)
    mv = (sigma0 - A - B * ks_a) / C
    return np.clip(mv, mv_min, mv_max)


# ---------------------------------------------------------------------------
# 合成数据：土壤湿度场 + 粗糙度场 → 模型正演 σ⁰
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float], width: int = 64, height: int = 64,
    incidence_deg: float = 40.0, model: str = "dubois",
    wavelength_m: float = WAVELENGTH_M, noise_db: float = 0.3, seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成空间变化土壤湿度场与粗糙度场，经模型正演为 σ⁰_dB（含噪声）。

    返回 (sigma0_db (H,W), info)，info 含真值 mv_truth、roughness_s、ks_truth。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float64) / max(width - 1, 1)
    yn = yy.astype(np.float64) / max(height - 1, 1)

    # 真值土壤湿度 (m³/m³)：基准 + 空间梯度 + 波动 + 纹理
    mv = (0.18 + 0.14 * xn + 0.05 * np.sin(2.0 * np.pi * yn)
          + rng.normal(0.0, 0.02, size=(height, width)))
    mv = np.clip(mv, 0.03, 0.50)

    # 真值地表 RMS 高度 s (m)
    s = (0.012 + 0.008 * yn + rng.normal(0.0, 0.0015, size=(height, width)))
    s = np.clip(s, 0.005, 0.030)

    k = radar_wavenumber(wavelength_m)
    ks = k * s
    sigma0 = backscatter_db(mv, ks, incidence_deg, model)
    sigma0 = sigma0 + rng.normal(0.0, noise_db, size=(height, width))

    info = {
        "bbox": bbox, "width": width, "height": height,
        "incidence_deg": incidence_deg, "model": model,
        "wavelength_m": wavelength_m, "noise_db": noise_db,
        "mv_truth": mv.astype(np.float32),
        "roughness_s": s.astype(np.float32),
        "ks_truth": ks.astype(np.float32),
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
            "model": getattr(args, "model", None),
            "incidence_angle": getattr(args, "incidence_angle", None),
            "roughness_ks": getattr(args, "roughness_ks", None),
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
            bbox, incidence_deg=args.incidence_angle, model=args.model,
        )
        n_valid_pixels = int(sigma0.size)
        source_note = "synthetic"

    if sigma0.size == 0:
        raise ValidationError("input raster is empty")

    # Now safe to create output dir
    os.makedirs(output_dir, exist_ok=True)

    # 反演所用粗糙度：合成模式用真值 ks 场；真实模式用标量 --roughness-ks
    if synth_info is not None:
        ks_used = synth_info["ks_truth"]
    else:
        ks_used = float(args.roughness_ks)

    mv = invert_soil_moisture(sigma0, ks_used, args.incidence_angle, model=args.model)
    mv = mv.astype(np.float32)

    out_tif = os.path.join(output_dir, "soil_moisture.tif")
    write_geotiff(out_tif, mv, bbox)

    qa: Dict[str, Any] = {
        "source": source_note, "model": args.model,
        "incidence_deg": args.incidence_angle,
        "mv_mean": float(mv.mean()),
        "mv_std": float(mv.std()),
        "mv_range": [float(mv.min()), float(mv.max())],
        "in_physical_range": bool(mv.min() >= MV_MIN - 1e-6 and mv.max() <= MV_MAX + 1e-6),
        "n_valid_pixels": n_valid_pixels,
        "input_nodata": input_nodata,
    }
    truth = None
    if synth_info is not None:
        truth = synth_info["mv_truth"]
        rmse = float(np.sqrt(np.mean((mv - truth) ** 2)))
        corr = float(np.corrcoef(mv.ravel(), truth.ravel())[0, 1])
        bias = float(np.mean(mv - truth))
        qa["mv_truth_mean"] = float(truth.mean())
        qa["rmse_m3m3"] = rmse
        qa["bias_m3m3"] = bias
        qa["correlation"] = corr

    A, B, C = _model_terms(args.incidence_angle, args.model)
    stats = {
        "model": args.model,
        "coefficients": MODEL_COEFS[args.model],
        "incidence_deg": args.incidence_angle,
        "wavelength_m": WAVELENGTH_M,
        "radar_wavenumber": radar_wavenumber(WAVELENGTH_M),
        "terms": {"A_baseline": A, "B_roughness": B, "C_moisture": C},
        "mv_clip_range": [MV_MIN, MV_MAX],
        "statistics": {
            "mv_mean": qa["mv_mean"], "mv_std": qa["mv_std"], "mv_range": qa["mv_range"],
        },
    }
    if truth is not None:
        stats["validation"] = {"rmse": qa["rmse_m3m3"], "bias": qa["bias_m3m3"],
                               "correlation": qa["correlation"]}
    stats_path = os.path.join(output_dir, "soil_moisture_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] model: {args.model}  incidence: {args.incidence_angle}°")
        print(f"[{SKILL_NAME}] retrieved mean mv: {qa['mv_mean']:.4f} m³/m³")
        if truth is not None:
            print(f"[{SKILL_NAME}] RMSE={qa['rmse_m3m3']:.4f}  corr={qa['correlation']:.3f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="SAR bare-soil moisture retrieval using simplified Dubois/Oh semi-empirical models.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input sigma0 (dB) GeoTIFF")
    p.add_argument("--incidence-angle", type=float, default=40.0,
                   help="radar incidence angle in degrees (default: 40)")
    p.add_argument("--model", default="dubois", choices=["dubois", "oh"],
                   help="semi-empirical model (default: dubois)")
    p.add_argument("--roughness-ks", type=float, default=1.5,
                   help="normalized roughness ks for real-input mode (default: 1.5)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic soil-moisture scene (offline)")
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
