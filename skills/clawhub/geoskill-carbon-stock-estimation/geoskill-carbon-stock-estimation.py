#!/usr/bin/env python3
"""carbon-stock-estimation — 碳储量估算

基于异速生长方程（allometric equation）与土壤碳密度数据估算区域碳储量。

- 地上生物量（AGB）：由 NDVI 经幂律异速方程估算（AGB = scale × NDVI^power），
- 地下生物量（BGB）：AGB × 根茎比，
- 土壤有机碳（SOC）：植被类型查表 × 像元面积 × 深度因子，
- 总碳储量 = AGB × 含碳系数 × (1 + 根茎比) + SOC。

含碳系数取 IPCC 默认 0.47（干生物量中碳占比）。

数据源：本地 GeoTIFF（band1=NDVI 或生物量代理），或 --synthetic 离线模拟。

隐私声明 / Privacy：
- 默认离线运行，--synthetic 完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python carbon-stock-estimation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
    python carbon-stock-estimation.py --input ndvi.tif --output-dir ./out

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
SKILL_NAME = "carbon-stock-estimation"

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
CARBON_FRACTION = 0.47   # IPCC 默认：干生物量含碳比例
ROOT_SHOOT_RATIO = 0.30  # 通用根茎比
SOC_DENSITY: Dict[str, float] = {
    "forest": 60.0, "grassland": 45.0, "cropland": 35.0, "bare": 15.0, "water": 0.0,
}
CLASS_NAMES = ["forest", "grassland", "cropland", "bare", "water"]


def agb_from_ndvi(ndvi: np.ndarray, scale: float = 200.0, power: float = 2.0) -> np.ndarray:
    """幂律异速方程：AGB (Mg/ha) = scale × max(NDVI, 0)^power。"""
    return (scale * np.clip(ndvi, 0.0, None) ** power).astype(np.float32)


def carbon_from_biomass(biomass: np.ndarray, carbon_fraction: float = CARBON_FRACTION) -> np.ndarray:
    """生物量 → 碳：C = biomass × CF。"""
    return (biomass * carbon_fraction).astype(np.float32)


def classify_lulc_carbon(ndvi: np.ndarray) -> np.ndarray:
    codes = np.full(ndvi.shape, 3, dtype=np.int8)  # bare
    codes[ndvi >= 0.55] = 0
    codes[(ndvi >= 0.35) & (ndvi < 0.55)] = 1
    codes[(ndvi >= 0.15) & (ndvi < 0.35)] = 2
    codes[ndvi < 0.0] = 4
    return codes


def soil_carbon(lulc_codes: np.ndarray, pixel_area_ha: float,
                soc_density: Optional[Dict[str, float]] = None,
                depth_factor: float = 1.0) -> np.ndarray:
    """土壤有机碳（Mg C / pixel）= 类型碳密度 × 面积 × 深度因子。"""
    if soc_density is None:
        soc_density = SOC_DENSITY
    soc = np.zeros(lulc_codes.shape, dtype=np.float32)
    for ci, cname in enumerate(CLASS_NAMES):
        soc[lulc_codes == ci] = soc_density.get(cname, 20.0) * pixel_area_ha * depth_factor
    return soc


def total_carbon(agb_carbon: np.ndarray, root_shoot_ratio: float = ROOT_SHOOT_RATIO,
                 soc: Optional[np.ndarray] = None) -> np.ndarray:
    """总碳 = 地上碳×(1+根茎比) + 土壤碳。"""
    total = agb_carbon * (1.0 + root_shoot_ratio)
    if soc is not None:
        total = total + soc
    return total.astype(np.float32)


def generate_synthetic_carbon(bbox: List[float], width: int = 128, height: int = 128,
                              seed: int = 42) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy /= max(height - 1, 1)
    xx /= max(width - 1, 1)
    ndvi = (0.05 + 0.70 * xx + 0.15 * np.sin(5 * np.pi * yy)
            + rng.normal(0, 0.03, (height, width))).astype(np.float32)
    ndvi = np.clip(ndvi, -0.1, 0.95)
    codes = classify_lulc_carbon(ndvi)
    info = {"bbox": bbox, "width": width, "height": height}
    return ndvi, codes, info


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
    """读取栅格，返回 (cube, bbox)。保持既有签名。"""
    cube, bbox, _ = read_geotiff_masked(path)
    return cube, bbox


def read_geotiff_masked(path: str) -> Tuple[np.ndarray, List[float], np.ndarray]:
    """读取栅格，返回 (cube, bbox, valid_mask)；nodata 像元在 mask 中为 False。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        try:
            mask = src.read_masks(1) > 0
        except Exception:
            mask = np.ones(cube.shape[1:], dtype=bool)
        nd = src.nodata
    if nd is not None:
        for k in range(cube.shape[0]):
            mask &= ~np.isclose(cube[k], nd)
    cube = np.where(mask[None], cube, 0.0).astype(np.float32)
    return cube, bbox, mask


def validate_bbox(bbox: List[float]) -> List[float]:
    """校验 bbox [W, S, E, N]；不合法抛 ValidationError（exit 6）。"""
    try:
        w, s, e, n = (float(v) for v in bbox)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox values must be numeric: {bbox}") from exc
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"bbox longitude out of range [-180, 180]: W={w}, E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"bbox latitude out of range [-90, 90]: S={s}, N={n}")
    if w > e:
        raise ValidationError(
            f"bbox W ({w}) > E ({e}); antimeridian-crossing bbox is not supported — "
            "split the request into two bboxes on either side of +/-180")
    if s > n:
        raise ValidationError(f"bbox S ({s}) > N ({n})")
    return [w, s, e, n]


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
            "scale": getattr(args, "scale", None),
            "power": getattr(args, "power", None),
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
    os.makedirs(output_dir, exist_ok=True)
    bbox = list(args.bbox) if args.bbox else None

    if args.scale <= 0 or args.power <= 0:
        raise ValidationError("allometry parameters must be positive",
                              scale=args.scale, power=args.power)

    valid: Optional[np.ndarray] = None
    if args.input and not args.synthetic:
        cube, file_bbox, mask = read_geotiff_masked(args.input)
        bbox = validate_bbox(bbox if bbox is not None else file_bbox)
        ndvi = cube[0]
        if ndvi.size == 0:
            raise ValidationError("input raster is empty")
        valid = mask
        if not bool(valid.any()):
            raise ValidationError("input raster contains no valid (non-NoData) pixels")
        vals = ndvi[valid]
        if float(np.percentile(vals, 99)) > 1.5:
            raise ValidationError(
                "band 1 does not look like NDVI (values outside [-1, 1]); "
                "provide an NDVI raster as band 1")
        ndvi = np.where(valid, ndvi, 0.0).astype(np.float32)
        codes = classify_lulc_carbon(ndvi)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        ndvi, codes, _ = generate_synthetic_carbon(bbox)
        source_note = "synthetic"

    h, w = ndvi.shape
    lat_mid = (bbox[1] + bbox[3]) / 2.0
    dx_m = (bbox[2] - bbox[0]) / w * 111320 * np.cos(np.deg2rad(lat_mid))
    dy_m = (bbox[3] - bbox[1]) / h * 111320
    pixel_area_ha = (dx_m * dy_m) / 10000.0

    agb = agb_from_ndvi(ndvi, scale=args.scale, power=args.power)      # Mg/ha（密度）
    agb_c = carbon_from_biomass(agb) * pixel_area_ha                   # Mg C/像元（储量）
    soc = soil_carbon(codes, pixel_area_ha)                            # Mg C/像元（储量）
    tc = total_carbon(agb_c, soc=soc)                                  # Mg C/像元（储量）

    if valid is not None:
        fill = np.full_like(agb_c, -9999.0)
        agb_c = np.where(valid, agb_c, fill).astype(np.float32)
        soc = np.where(valid, soc, fill).astype(np.float32)
        tc = np.where(valid, tc, fill).astype(np.float32)
        agg = valid
    else:
        agg = np.ones((h, w), dtype=bool)

    agb_path = os.path.join(output_dir, "agb_carbon.tif")
    soc_path = os.path.join(output_dir, "soil_carbon.tif")
    tc_path = os.path.join(output_dir, "total_carbon.tif")
    write_geotiff(agb_path, agb_c, bbox)
    write_geotiff(soc_path, soc, bbox)
    write_geotiff(tc_path, tc, bbox)

    params = {
        "carbon_fraction": CARBON_FRACTION, "root_shoot_ratio": ROOT_SHOOT_RATIO,
        "scale": args.scale, "power": args.power, "pixel_area_ha": pixel_area_ha,
        "valid_pixel_fraction": float(np.mean(agg)),
        "mean_agb_carbon_density_Mg_per_ha": float(np.mean(agb_c[agg])) / pixel_area_ha,
        "total_agb_carbon_Mg": float(np.sum(agb_c[agg])),
        "total_soc_Mg": float(np.sum(soc[agg])),
        "total_carbon_Mg": float(np.sum(tc[agg])),
    }
    params_path = os.path.join(output_dir, "carbon_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": agb_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": soc_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": tc_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    qa: Dict[str, Any] = {
        "source": source_note,
        "total_carbon_Mg": params["total_carbon_Mg"],
        "agb_carbon_Mg": params["total_agb_carbon_Mg"],
        "soc_Mg": params["total_soc_Mg"],
    }
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] total C: {params['total_carbon_Mg']:,.1f} Mg")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Carbon stock estimation from biomass allometry and soil carbon density.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF (band1=NDVI or biomass proxy)")
    p.add_argument("--scale", type=float, default=200.0, help="AGB allometry scale (default: 200)")
    p.add_argument("--power", type=float, default=2.0, help="AGB allometry power (default: 2.0)")
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
