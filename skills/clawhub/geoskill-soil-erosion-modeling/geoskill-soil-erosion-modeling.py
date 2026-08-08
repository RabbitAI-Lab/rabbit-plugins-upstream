#!/usr/bin/env python3
"""soil-erosion-modeling — 土壤侵蚀建模

基于 RUSLE（Revised Universal Soil Loss Equation）估算土壤侵蚀模数
（t·ha⁻¹·yr⁻¹）：

    A = R × K × L × S × C × P

- R（降雨侵蚀力，MJ·mm·ha⁻¹·h⁻¹·yr⁻¹）：由年均降雨与强度估算，
- K（土壤可蚀性）：按质地查表，
- L·S（坡长-坡度因子）：由 DEM 坡度/汇流累积计算，
- C（植被覆盖管理因子）：由 NDVI 反演，取值 [0.01, 1]，
- P（水保措施因子）：等高耕作/梯田等，取值 [0, 1]。

数据源：--synthetic 生成降雨/DEM/NDVI/土壤栅格；--input 读取多波段输入。

隐私声明 / Privacy：
- 完全离线运行。

Usage:
    python soil-erosion-modeling.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "soil-erosion-modeling"

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


def validate_cell_size(value: float) -> float:
    """Validate --cell-size > 0 (meters); return float."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        raise ValidationError(f"cell-size must be a number, got {value!r}")
    if v <= 0.0:
        raise ValidationError(f"cell-size must be > 0 (meters), got {v}")
    return v


# ---------------------------------------------------------------------------
# RUSLE 因子
# ---------------------------------------------------------------------------
def r_factor(annual_precip_mm: np.ndarray, intensity_coeff: float = 0.35) -> np.ndarray:
    """降雨侵蚀力 R ≈ 年均降雨 × 强度系数（简化，MJ·mm·ha⁻¹·h⁻¹·yr⁻¹）。"""
    return (np.clip(annual_precip_mm, 0.0, None) * intensity_coeff).astype(np.float32)


def k_factor(soil_texture_code: np.ndarray) -> np.ndarray:
    """土壤可蚀性 K：0=砂土 1=壤土 2=黏土 3=粉砂 → 查表。"""
    table = np.array([0.05, 0.32, 0.25, 0.42], dtype=np.float32)
    idx = np.clip(soil_texture_code.astype(np.int8), 0, 3)
    return table[idx]


def ls_factor(slope_deg: np.ndarray, flow_accum: np.ndarray,
              cell_size: float = 30.0) -> np.ndarray:
    """坡长-坡度因子 LS（Moore & Burch 简化式）。

    LS = (flow_accum × cell / 22.13)^0.4 × (sin(slope)/0.0896)^1.3
    """
    m = np.power(np.maximum(flow_accum, 1.0) * cell_size / 22.13, 0.4)
    sin_s = np.sin(np.deg2rad(np.clip(slope_deg, 0.0, 90.0)))
    s = np.power(np.maximum(sin_s, 1e-4) / 0.0896, 1.3)
    return (m * s).astype(np.float32)


def c_factor(ndvi: np.ndarray, c_min: float = 0.01) -> np.ndarray:
    """植被覆盖管理因子 C：NDVI 高 → 植被覆盖好 → C 小。
    C = c_min + (1 - c_min) × exp(-2.5 × max(NDVI, 0))。"""
    ndvi_pos = np.clip(ndvi, 0.0, 1.0)
    return (c_min + (1.0 - c_min) * np.exp(-2.5 * ndvi_pos)).astype(np.float32)


def p_factor(practice_code: np.ndarray) -> np.ndarray:
    """水保措施因子 P：0=无措施 1=等高耕作 2=梯田 → 查表。"""
    table = np.array([1.0, 0.55, 0.25], dtype=np.float32)
    idx = np.clip(practice_code.astype(np.int8), 0, 2)
    return table[idx]


def rusle(r: np.ndarray, k: np.ndarray, ls: np.ndarray,
          c: np.ndarray, p: np.ndarray) -> np.ndarray:
    """侵蚀模数 A = R × K × LS × C × P（t·ha⁻¹·yr⁻¹）。"""
    return (r * k * ls * c * p).astype(np.float32)


def erosion_grade(a: np.ndarray) -> np.ndarray:
    """侵蚀强度分级（0-4）：微度/轻度/中度/强烈/极强烈。"""
    grade = np.zeros(a.shape, dtype=np.int8)
    grade[a >= 500] = 1
    grade[a >= 2500] = 2
    grade[a >= 5000] = 3
    grade[a >= 8000] = 4
    return grade


def generate_synthetic_erosion(bbox: List[float], width: int = 128, height: int = 128,
                               seed: int = 42) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy /= max(height - 1, 1)
    xx /= max(width - 1, 1)
    precip = 400.0 + 800.0 * yy + rng.normal(0, 30, (height, width))
    slope = 2.0 + 25.0 * xx + rng.normal(0, 2, (height, width))
    ndvi = 0.10 + 0.60 * (1.0 - xx) + rng.normal(0, 0.04, (height, width))
    ndvi = np.clip(ndvi, 0.0, 0.9)
    soil = (rng.integers(0, 4, (height, width))).astype(np.int8)
    practice = (rng.integers(0, 3, (height, width))).astype(np.int8)
    flow_accum = 1.0 + 50.0 * xx + rng.exponential(5, (height, width))
    return {
        "precip": precip.astype(np.float32), "slope": np.clip(slope, 0, 60).astype(np.float32),
        "ndvi": ndvi.astype(np.float32), "soil": soil, "practice": practice,
        "flow_accum": flow_accum.astype(np.float32),
        "bbox": bbox, "width": width, "height": height,
    }


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
    profile = {"driver": "GTiff", "height": h, "width": w, "count": nb,
               "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
               "nodata": nodata, "compress": "deflate"}
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
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "cell_size": getattr(args, "cell_size", None),
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

    # --- Upfront validation (BEFORE makedirs; rc=6 for bad data, rc=2 for bad CLI) ---
    if args.bbox is not None:
        validate_bbox(args.bbox)
    validate_cell_size(args.cell_size)

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            validate_bbox(bbox)
        # 期望 6 波段：precip, slope, ndvi, soil, practice, flow_accum
        if cube.shape[0] < 6:
            raise ValidationError(
                f"input needs 6 bands (precip, slope, ndvi, soil, practice, flow_accum), got {cube.shape[0]}")
        if cube.ndim != 3:
            raise ValidationError("input raster must be multiband (bands, H, W)")
        precip, slope, ndvi = cube[0], cube[1], cube[2]
        # soil/practice 为整数码；NoData(NaN) 像素先填占位值避免 int8 转换失败，
        # 最终侵蚀结果处统一按无效像素屏蔽
        valid = (np.isfinite(cube[:6]).all(axis=0))
        n_total = int(cube.shape[1] * cube.shape[2])
        n_valid = int(np.count_nonzero(valid))
        if n_valid == 0:
            raise ValidationError("input raster has no valid pixels (all NoData)")
        soil = np.where(np.isnan(cube[3]), 1.0, cube[3]).astype(np.int8)
        practice = np.where(np.isnan(cube[4]), 1.0, cube[4]).astype(np.int8)
        flow_accum = cube[5]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        s = generate_synthetic_erosion(bbox)
        precip, slope, ndvi = s["precip"], s["slope"], s["ndvi"]
        soil, practice, flow_accum = s["soil"], s["practice"], s["flow_accum"]
        source_note = "synthetic"
        n_total = int(precip.size)
        n_valid = n_total

    if precip.size == 0:
        raise ValidationError("input raster is empty")

    r = r_factor(precip)
    k = k_factor(soil)
    ls = ls_factor(slope, flow_accum, cell_size=args.cell_size)
    c = c_factor(ndvi)
    p = p_factor(practice)
    a = rusle(r, k, ls, c, p)
    if source_note != "synthetic":
        a = np.where(valid, a, np.nan)
    grade = erosion_grade(a)

    # --- Output dir (only after all upfront validation passes) ---
    os.makedirs(output_dir, exist_ok=True)

    erosion_path = os.path.join(output_dir, "erosion_modulus.tif")
    grade_path = os.path.join(output_dir, "erosion_grade.tif")
    a_out = np.where(np.isfinite(a), a, -9999.0).astype(np.float32)
    grade_out = np.where(np.isfinite(a), grade.astype(np.float32), -9999.0).astype(np.float32)
    write_geotiff(erosion_path, a_out, bbox)
    write_geotiff(grade_path, grade_out, bbox)

    params = {
        "cell_size_m": args.cell_size,
        "mean_erosion_t_ha_yr": float(np.nanmean(a)) if n_valid else 0.0,
        "max_erosion_t_ha_yr": float(np.nanmax(a)) if n_valid else 0.0,
        "mean_R": float(np.nanmean(r)), "mean_K": float(np.nanmean(k)),
        "mean_LS": float(np.nanmean(ls)), "mean_C": float(np.nanmean(c)),
        "mean_P": float(np.nanmean(p)),
        "grade_pixel_counts": {str(i): int(np.sum(grade == i)) for i in range(5)},
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
    }
    params_path = os.path.join(output_dir, "rusle_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": erosion_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": grade_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    qa: Dict[str, Any] = {
        "source": source_note,
        "input_nodata": -9999.0,
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
        "mean_erosion_t_ha_yr": params["mean_erosion_t_ha_yr"],
        "max_erosion_t_ha_yr": params["max_erosion_t_ha_yr"],
    }
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean erosion: {qa['mean_erosion_t_ha_yr']:.1f} t·ha⁻¹·yr⁻¹")
        print(f"[{SKILL_NAME}] max erosion:  {qa['max_erosion_t_ha_yr']:.1f} t·ha⁻¹·yr⁻¹")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Soil erosion modeling via RUSLE (R K LS C P).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input 6-band GeoTIFF (precip,slope,ndvi,soil,practice,flow)")
    p.add_argument("--cell-size", type=float, default=30.0, help="cell size in meters (default: 30)")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic inputs (offline)")
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
