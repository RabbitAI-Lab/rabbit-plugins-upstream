#!/usr/bin/env python3
"""water-purification-mapping — 水源涵养/净化功能制图

基于简化 InVEST 水量平衡模型 + 水质净化代理估算水源涵养量与养分截留。

- 产水量（water yield）：Budyko 风格水量平衡 Y = P - AET，
  其中 AET/P 由干燥指数 φ = ET0/P 与土壤水分参数 ω 参数化，
- 水源涵养量（retention）：产水量 × 植被截留系数（LULC 依赖），
- 水质净化（nutrient retention）：植被/土壤对 N/P 的截留率 × 负荷。

数据源：--synthetic 生成降雨/ET0/土壤/NDVI 栅格；--input 读取多波段输入。

隐私声明 / Privacy：
- 完全离线运行。

Usage:
    python water-purification-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "water-purification-mapping"

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


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def water_yield(precip: np.ndarray, et0: np.ndarray, awc: np.ndarray,
                omega: float = 1.5) -> np.ndarray:
    """Budyko 风格产水量（mm/yr）：Y = P - AET。

    AET/P = 1 + φ - (1 + φ^ω)^(1/ω)，φ = ET0/P（干燥指数）。
    """
    p_safe = np.maximum(precip, 1.0)
    phi = np.clip(et0 / p_safe, 0.0, 10.0)
    omega_safe = max(omega, 0.5)
    aet_ratio = 1.0 + phi - np.power(1.0 + np.power(phi, omega_safe), 1.0 / omega_safe)
    aet = aet_ratio * p_safe
    y = p_safe - aet
    return np.clip(y, 0.0, None).astype(np.float32)


def retention_factor(ndvi: np.ndarray, r_max: float = 0.85) -> np.ndarray:
    """植被截留系数 [0, r_max]：NDVI 高 → 截留强。"""
    ndvi_pos = np.clip(ndvi, 0.0, 1.0)
    return (r_max * ndvi_pos / (ndvi_pos + 0.2)).astype(np.float32)


def water_retention(yield_mm: np.ndarray, ndvi: np.ndarray) -> np.ndarray:
    """水源涵养量（mm/yr）= 产水量 × 截留系数。"""
    return (yield_mm * retention_factor(ndvi)).astype(np.float32)


def nutrient_retention(load_kg_ha: np.ndarray, ndvi: np.ndarray,
                       efficiency: float = 0.65) -> np.ndarray:
    """养分截留量（kg/ha/yr）= 负荷 × 截留效率（NDVI 调制）。"""
    ndvi_pos = np.clip(ndvi, 0.0, 1.0)
    eff = efficiency * ndvi_pos / (ndvi_pos + 0.3)
    return (load_kg_ha * eff).astype(np.float32)


def generate_synthetic_water(bbox: List[float], width: int = 128, height: int = 128,
                             seed: int = 42) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy /= max(height - 1, 1)
    xx /= max(width - 1, 1)
    precip = 500.0 + 600.0 * yy + rng.normal(0, 30, (height, width))
    et0 = 700.0 - 200.0 * yy + rng.normal(0, 20, (height, width))
    awc = 0.10 + 0.15 * xx + rng.normal(0, 0.01, (height, width))
    ndvi = 0.10 + 0.65 * xx + rng.normal(0, 0.04, (height, width))
    ndvi = np.clip(ndvi, 0.0, 0.9)
    n_load = 50.0 + 30.0 * (1.0 - xx) + rng.normal(0, 5, (height, width))
    return {
        "precip": precip.astype(np.float32), "et0": np.clip(et0, 100, 2000).astype(np.float32),
        "awc": np.clip(awc, 0.05, 0.4).astype(np.float32),
        "ndvi": ndvi.astype(np.float32), "n_load": np.clip(n_load, 0, 300).astype(np.float32),
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
    return cube, bbox


# ---------------------------------------------------------------------------
# 参数校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Optional[List[float]]) -> List[float]:
    """校验 [W, S, E, N]：W<E、S<N、范围合法；跨 180°给拆分提示。"""
    if bbox is None or len(bbox) != 4:
        raise UsageError(
            "bbox must be 4 floats [W S E N], got: " + repr(bbox),
            bbox=bbox,
        )
    w, s, e, n = bbox
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError(
            f"bbox must contain finite floats, got {bbox}", bbox=bbox)
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of [-180, 180]: W={w} E={e}", bbox=bbox)
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of [-90, 90]: S={s} N={n}", bbox=bbox)
    if s >= n:
        raise ValidationError(
            f"bbox South >= North: S={s} N={n}", bbox=bbox)
    # 跨 180°经线不直接支持
    if w > e:
        raise ValidationError(
            f"bbox crosses the 180° meridian (W={w} > E={e}); "
            f"please split the extent or wrap longitudes manually",
            bbox=bbox)
    if abs(e - w) < 1e-9 or abs(n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero area: W={w} E={e} S={s} N={n}", bbox=bbox)
    return [float(w), float(s), float(e), float(n)]


def validate_omega(omega: float) -> float:
    """Budyko ω 必须为正（实现中已用 max(omega, 0.5) 兜底，但负值物理无意义）。"""
    try:
        v = float(omega)
    except (TypeError, ValueError):
        raise ValidationError(f"omega must be a number, got {omega!r}")
    if not np.isfinite(v):
        raise ValidationError(f"omega must be finite, got {v}")
    if v <= 0.0:
        raise ValidationError(
            f"omega must be > 0 (Budyko parameter), got {v}", omega=v)
    return v


def read_geotiff_with_nodata(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """读 GeoTIFF 并把 nodata 标记的像元替换为 NaN；同时返回原 nodata。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    return cube, bbox, nodata


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
            "omega": getattr(args, "omega", None),
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
    omega = validate_omega(args.omega)

    bbox_in = list(args.bbox) if args.bbox else None

    if args.input and not args.synthetic:
        cube, file_bbox, _nd = read_geotiff_with_nodata(args.input)
        if cube.shape[0] < 5:
            raise ValidationError(
                f"input needs 5 bands (precip, et0, awc, ndvi, n_load), got {cube.shape[0]}")
        if bbox_in is not None:
            bbox = validate_bbox(bbox_in)
        else:
            bbox = validate_bbox(file_bbox)
        if cube.size == 0:
            raise ValidationError("input raster is empty")
        precip, et0, awc, ndvi, n_load = cube[0], cube[1], cube[2], cube[3], cube[4]
        n_valid_per_band = [int(np.isfinite(b).sum()) for b in (precip, et0, awc, ndvi, n_load)]
        n_total = int(precip.size)
        if any(v == 0 for v in n_valid_per_band):
            raise ValidationError(
                "input raster has a band with all NoData/NaN",
                n_valid_per_band=n_valid_per_band)
        source_note = args.input
    else:
        bbox = validate_bbox(bbox_in)
        s = generate_synthetic_water(bbox)
        precip, et0, awc, ndvi, n_load = s["precip"], s["et0"], s["awc"], s["ndvi"], s["n_load"]
        n_valid_per_band = [int(b.size) for b in (precip, et0, awc, ndvi, n_load)]
        n_total = int(precip.size)
        source_note = "synthetic"

    # 校验通过后再创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 核心计算（核心算子已 NaN-safe；这里直接复用）
    wy = water_yield(precip, et0, awc, omega=omega)
    wr = water_retention(wy, ndvi)
    nr = nutrient_retention(n_load, ndvi)

    wy_path = os.path.join(output_dir, "water_yield.tif")
    wr_path = os.path.join(output_dir, "water_retention.tif")
    nr_path = os.path.join(output_dir, "nutrient_retention.tif")
    write_geotiff(wy_path, wy, bbox)
    write_geotiff(wr_path, wr, bbox)
    write_geotiff(nr_path, nr, bbox)

    # 统计：仅基于有效像元
    def _nan_stat(arr: np.ndarray, fn) -> float:
        v = arr[np.isfinite(arr)]
        return float(fn(v)) if v.size else 0.0

    mean_wy = _nan_stat(wy, np.mean)
    mean_wr = _nan_stat(wr, np.mean)
    mean_nr = _nan_stat(nr, np.mean)
    total_wy = _nan_stat(wy, np.sum)
    total_nr = _nan_stat(nr, np.sum)

    params = {
        "omega": omega,
        "mean_water_yield_mm": mean_wy,
        "mean_water_retention_mm": mean_wr,
        "mean_nutrient_retention_kg_ha": mean_nr,
        "total_water_yield_mm_sum": total_wy,
        "total_nutrient_retention_kg_ha_sum": total_nr,
    }
    params_path = os.path.join(output_dir, "water_purification_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": wy_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": wr_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": nr_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    qa: Dict[str, Any] = {
        "source": source_note,
        "mean_water_yield_mm": mean_wy,
        "mean_water_retention_mm": mean_wr,
        "mean_nutrient_retention_kg_ha": mean_nr,
        "n_total_pixels": n_total,
        "n_valid_per_band": n_valid_per_band,
    }
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean water yield: {qa['mean_water_yield_mm']:.1f} mm/yr")
        print(f"[{SKILL_NAME}] mean retention: {qa['mean_water_retention_mm']:.1f} mm/yr")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Water purification and retention mapping via simplified InVEST water balance.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input 5-band GeoTIFF (precip, et0, awc, ndvi, n_load)")
    p.add_argument("--omega", type=float, default=1.5,
                   help="Budyko omega parameter (default: 1.5)")
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
