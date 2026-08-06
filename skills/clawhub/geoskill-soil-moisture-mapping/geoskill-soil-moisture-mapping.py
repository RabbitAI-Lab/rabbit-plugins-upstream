#!/usr/bin/env python3
"""soil-moisture-mapping — 土壤湿度制图

用热惯量法（表观热惯量 ATI 与土壤含水量的经验关系）与 SAR Dubois 后向散射
模型反演表层土壤体积含水量，并划分干旱等级。

核心算法
--------
- **热惯量法**：表观热惯量 ATI = (1 - 反照率) / 昼夜温差；含水量越高热惯量
  越大，用 mv = mv_max * (1 - exp(-ATI * scale)) 的经验关系估算。
- **SAR Dubois 模型**（Dubois et al. 1995 简化）：
  σ°_vv = 10^A · (cosθ)^-1.47 · mv^1.09 · 10^(-0.028·ks·tanθ)
  其中 A = -2.75 + 0.0287·f(GHz)。对 mv 解析反演。
- **干旱等级**：按体积含水量阈值分 0（无旱）~3（重旱）。

数据源：本地多源栅格（热红外 + SAR）或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线，``--synthetic`` 完全无网络，本地处理不上传。

Usage:
    python soil-moisture-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "soil-moisture-mapping"

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


# Dubois 模型默认几何/频率参数
DEFAULT_INCIDENCE_DEG = 40.0
DEFAULT_FREQ_GHZ = 5.405  # Sentinel-1 C 波段
DEFAULT_KS = 0.8          # 均方根粗糙度 (无量纲 ks = k*sigma_h)


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


def validate_bbox(bbox) -> None:
    """Validate bbox: W<E, S<N, lon in [-180,180], lat in [-90,90]."""
    if bbox is None or len(bbox) != 4:
        raise UsageError("bbox must be 4 floats: W S E N")
    w, s, e, n = [float(x) for x in bbox]
    if w >= e:
        raise ValidationError(
            f"invalid bbox: W >= E ({w} >= {e}); cross-180° bboxes not supported, "
            f"split the request into two halves")
    if s >= n:
        raise ValidationError(f"invalid bbox: S >= N ({s} >= {n})")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"invalid bbox: longitude out of [-180,180]: [{w}, {e}]")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"invalid bbox: latitude out of [-90,90]: [{s}, {n}]")
    if abs(e - w) < 1e-9 or abs(n - s) < 1e-9:
        raise ValidationError(f"invalid bbox: zero-area ({w},{s},{e},{n})")


def validate_sar_params(incidence: float, freq: float, ks: float) -> None:
    """Validate SAR model params: 0 < incidence < 90°, freq > 0, ks > 0."""
    try:
        incidence_f = float(incidence)
        freq_f = float(freq)
        ks_f = float(ks)
    except (TypeError, ValueError):
        raise ValidationError("incidence/freq/ks must be numbers")
    if not (0.0 < incidence_f < 90.0):
        raise ValidationError(
            f"incidence angle must be in (0,90) degrees, got {incidence_f}")
    if freq_f <= 0.0:
        raise ValidationError(f"freq must be > 0 (GHz), got {freq_f}")
    if ks_f <= 0.0:
        raise ValidationError(f"ks (surface roughness) must be > 0, got {ks_f}")


# ---------------------------------------------------------------------------
# 核心算法：热惯量法
# ---------------------------------------------------------------------------
def apparent_thermal_inertia(albedo: np.ndarray, t_day: np.ndarray, t_night: np.ndarray,
                             eps: float = 1.0) -> np.ndarray:
    """表观热惯量 ATI = (1 - albedo) / (T_day - T_night + eps)。

    昼夜温差越小、吸收辐射越多（低反照率），ATI 越大，通常对应更高含水量。
    """
    albedo = np.asarray(albedo, dtype=np.float32)
    dt = np.asarray(t_day, dtype=np.float32) - np.asarray(t_night, dtype=np.float32)
    dt = np.clip(dt, 0.0, None) + eps
    ati = (1.0 - np.clip(albedo, 0.0, 1.0)) / dt
    return ati.astype(np.float32)


def thermal_inertia_moisture(ati: np.ndarray, mv_max: float = 0.45, scale: float = 8.0) -> np.ndarray:
    """由 ATI 经验估算体积含水量 mv = mv_max * (1 - exp(-ATI*scale))。"""
    ati = np.clip(np.asarray(ati, dtype=np.float32), 0.0, None)
    if mv_max <= 0 or scale <= 0:
        raise ValidationError("mv_max and scale must be > 0")
    mv = mv_max * (1.0 - np.exp(-ati * scale))
    return np.clip(mv, 0.0, mv_max).astype(np.float32)


# ---------------------------------------------------------------------------
# 核心算法：SAR Dubois 模型
# ---------------------------------------------------------------------------
def dubois_forward(mv: np.ndarray, ks: float = DEFAULT_KS,
                   incidence_deg: float = DEFAULT_INCIDENCE_DEG,
                   freq_ghz: float = DEFAULT_FREQ_GHZ) -> np.ndarray:
    """Dubois 前向：σ°_vv（线性）= 10^A · cosθ^-1.47 · mv^1.09 · 10^(-0.028·ks·tanθ)。"""
    mv = np.clip(np.asarray(mv, dtype=np.float32), 1e-4, None)
    theta = np.deg2rad(incidence_deg)
    A = -2.75 + 0.0287 * freq_ghz
    geom = (np.cos(theta) ** -1.47) * (10.0 ** (-0.028 * ks * np.tan(theta)))
    sigma = (10.0 ** A) * geom * (mv ** 1.09)
    return sigma.astype(np.float32)


def dubois_invert(sigma_vv: np.ndarray, ks: float = DEFAULT_KS,
                  incidence_deg: float = DEFAULT_INCIDENCE_DEG,
                  freq_ghz: float = DEFAULT_FREQ_GHZ) -> np.ndarray:
    """Dubois 解析反演含水量 mv。"""
    sigma_vv = np.clip(np.asarray(sigma_vv, dtype=np.float32), 1e-9, None)
    theta = np.deg2rad(incidence_deg)
    A = -2.75 + 0.0287 * freq_ghz
    geom = (np.cos(theta) ** -1.47) * (10.0 ** (-0.028 * ks * np.tan(theta)))
    mv = (sigma_vv / ((10.0 ** A) * geom)) ** (1.0 / 1.09)
    return np.clip(mv, 0.0, 0.65).astype(np.float32)


def linear_to_db(sigma: np.ndarray) -> np.ndarray:
    return (10.0 * np.log10(np.clip(np.asarray(sigma, dtype=np.float32), 1e-9, None))).astype(np.float32)


# ---------------------------------------------------------------------------
# 干旱等级
# ---------------------------------------------------------------------------
def drought_grade(mv: np.ndarray, thresholds: Tuple[float, float, float] = (0.30, 0.20, 0.10)) -> np.ndarray:
    """体积含水量阈值分级：0=无旱, 1=轻旱, 2=中旱, 3=重旱。"""
    mv = np.asarray(mv, dtype=np.float32)
    t_hi, t_mid, t_lo = thresholds
    out = np.full(mv.shape, 3, dtype=np.int32)
    out[mv >= t_lo] = 2
    out[mv >= t_mid] = 1
    out[mv >= t_hi] = 0
    return out


def estimate_moisture(albedo: np.ndarray, t_day: np.ndarray, t_night: np.ndarray,
                      sigma_vv: np.ndarray, method: str = "combined",
                      incidence_deg: float = DEFAULT_INCIDENCE_DEG,
                      freq_ghz: float = DEFAULT_FREQ_GHZ, ks: float = DEFAULT_KS) -> Dict[str, Any]:
    """主估算。method ∈ {thermal-inertia, dubois-sar, combined}。"""
    mv_ti = thermal_inertia_moisture(apparent_thermal_inertia(albedo, t_day, t_night))
    mv_sar = dubois_invert(sigma_vv, ks=ks, incidence_deg=incidence_deg, freq_ghz=freq_ghz)

    if method == "thermal-inertia":
        mv = mv_ti
    elif method == "dubois-sar":
        mv = mv_sar
    elif method == "combined":
        mv = (0.5 * mv_ti + 0.5 * mv_sar).astype(np.float32)
    else:
        raise UsageError(f"unknown method '{method}'", method=method)

    grade = drought_grade(mv)
    return {
        "mv": mv,
        "mv_ti": mv_ti,
        "mv_sar": mv_sar,
        "grade": grade,
        "stats": {
            "mean_mv": float(np.nanmean(mv)),
            "mean_mv_ti": float(np.nanmean(mv_ti)),
            "mean_mv_sar": float(np.nanmean(mv_sar)),
            "grade_hist": {str(i): int(np.sum(grade == i)) for i in range(4)},
        },
    }


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64, seed: int = 42):
    """波段顺序 [albedo, T_day_K, T_night_K, sigma_vv_linear, sigma_vh_linear]。

    场景：左侧湿润（低 ATI 温差、高后向散射），右侧干燥。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1)

    # 真值含水量：左湿右干
    mv_true = np.clip(0.40 - 0.30 * xx, 0.05, 0.45).astype(np.float32)

    albedo = np.clip(0.15 + 0.15 * xx + rng.normal(0, 0.01, (height, width)), 0.05, 0.4).astype(np.float32)
    # 湿土昼夜温差小，干土温差大
    dt_amp = 6.0 + 12.0 * xx  # 6K (湿) -> 18K (干)
    t_night = np.full((height, width), 288.0, dtype=np.float32)
    t_day = (t_night + dt_amp).astype(np.float32)

    # SAR 后向散射由 Dubois 前向生成（湿土后向散射更强）
    sigma_vv = dubois_forward(mv_true)
    sigma_vh = (sigma_vv * 0.25).astype(np.float32)
    sigma_vv = sigma_vv * (1.0 + rng.normal(0, 0.03, sigma_vv.shape)).astype(np.float32)

    cube = np.stack([albedo, t_day, t_night, sigma_vv, sigma_vh], axis=0).astype(np.float32)
    info = {
        "bbox": bbox, "width": width, "height": height,
        "band_order": ["albedo", "T_day_K", "T_night_K", "sigma_vv", "sigma_vh"],
        "incidence_deg": DEFAULT_INCIDENCE_DEG, "freq_ghz": DEFAULT_FREQ_GHZ, "ks": DEFAULT_KS,
        "mean_mv_true": float(mv_true.mean()),
    }
    return cube, {"info": info, "mv_true": mv_true}


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
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == nodata, np.nan, cube).astype(np.float32)
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
    bbox = list(args.bbox) if args.bbox else None

    # --- Upfront validation (BEFORE makedirs; rc=6 for bad data, rc=2 for bad CLI) ---
    if args.bbox is not None:
        validate_bbox(args.bbox)
    validate_sar_params(args.incidence, args.freq, args.ks)

    synth_info: Optional[Dict[str, Any]] = None
    incidence, freq, ks = args.incidence, args.freq, args.ks
    valid = None
    n_total, n_valid = 0, 0
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            validate_bbox(bbox)
        source_note = args.input
        n_total = int(cube.shape[1] * cube.shape[2])
        if cube.ndim != 3:
            raise ValidationError("input raster must be multiband (bands, H, W)")
        valid = np.isfinite(cube).all(axis=0)
        n_valid = int(np.count_nonzero(valid))
        if n_valid == 0:
            raise ValidationError("input raster has no valid pixels (all NoData)")
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, packed = generate_synthetic(bbox)
        synth_info = packed["info"]
        source_note = "synthetic"
        n_total = int(cube.shape[1] * cube.shape[2])
        n_valid = n_total

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.shape[0] < 5:
        raise ValidationError("input needs >=5 bands [albedo, T_day, T_night, sigma_vv, sigma_vh]")

    albedo, t_day, t_night, sigma_vv = cube[0], cube[1], cube[2], cube[3]
    res = estimate_moisture(albedo, t_day, t_night, sigma_vv, method=args.method,
                            incidence_deg=incidence, freq_ghz=freq, ks=ks)

    if valid is not None:
        # NoData 像素屏蔽：mv 置 NaN（写出时转 -9999），grade 置 -1 哨兵
        res["mv"] = np.where(valid, res["mv"], np.nan)
        res["mv_ti"] = np.where(valid, res["mv_ti"], np.nan)
        res["mv_sar"] = np.where(valid, res["mv_sar"], np.nan)
        res["grade"] = np.where(valid, res["grade"], -1)
        # 统计口径与输出一致：屏蔽像元不计入干旱分级
        res["stats"]["grade_hist"] = {str(i): int(np.sum(res["grade"] == i))
                                      for i in range(4)}

    # --- Output dir (only after all upfront validation passes) ---
    os.makedirs(output_dir, exist_ok=True)

    mv_tif = os.path.join(output_dir, "soil_moisture.tif")
    mv_out = np.where(np.isfinite(res["mv"]), res["mv"], -9999.0).astype(np.float32)
    write_geotiff(mv_tif, mv_out, bbox)
    grade_tif = os.path.join(output_dir, "drought_grade.tif")
    write_geotiff(grade_tif, res["grade"].astype(np.float32), bbox, nodata=-1.0)
    comp_tif = os.path.join(output_dir, "moisture_components.tif")
    comp = np.stack([res["mv_ti"], res["mv_sar"]], 0)
    comp = np.where(np.isfinite(comp), comp, -9999.0).astype(np.float32)
    write_geotiff(comp_tif, comp, bbox)

    qa = {"source": source_note, "method": args.method,
          "input_nodata": -9999.0, "n_valid_pixels": n_valid, "n_total_pixels": n_total,
          "mean_mv": res["stats"]["mean_mv"],
          "grade_hist": res["stats"]["grade_hist"]}
    if synth_info is not None:
        qa["synthetic"] = synth_info

    outputs = [
        {"path": mv_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": grade_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": comp_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 2},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  method: {args.method}")
        print(f"[{SKILL_NAME}] mean soil moisture: {qa['mean_mv']:.4f} (volumetric)")
        print(f"[{SKILL_NAME}] drought grades: {qa['grade_hist']}")
        print(f"[{SKILL_NAME}] output: {mv_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Soil moisture mapping via thermal inertia and the SAR Dubois model with drought grading.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF [albedo, T_day, T_night, sigma_vv, sigma_vh]")
    p.add_argument("--method", default="combined",
                   choices=["thermal-inertia", "dubois-sar", "combined"],
                   help="estimation method (default: combined)")
    p.add_argument("--incidence", type=float, default=DEFAULT_INCIDENCE_DEG,
                   help="SAR incidence angle in degrees (default: 40)")
    p.add_argument("--freq", type=float, default=DEFAULT_FREQ_GHZ,
                   help="SAR frequency in GHz (default: 5.405 C-band)")
    p.add_argument("--ks", type=float, default=DEFAULT_KS,
                   help="surface roughness ks (default: 0.8)")
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
