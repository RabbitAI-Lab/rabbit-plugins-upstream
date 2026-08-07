#!/usr/bin/env python3
"""ecosystem-services-valuation — 生态系统服务评估

基于「当量因子法」（谢高地等, 2008/2015）与简化 InVEST 思路评估四类生态系统
服务价值：供给服务、调节服务、支持服务、文化服务。

- 从 NDVI 反演 LULC（林地/草地/耕地/水体/建设用地），
- 按单位面积当量因子表计算各服务价值密度（元/ha/yr），
- 输出各服务价值栅格与总量 JSON。

数据源：本地 GeoTIFF（band1=NDVI 或红光/近红外），或 --synthetic 离线模拟。

隐私声明 / Privacy：
- 默认离线运行，--synthetic 完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python ecosystem-services-valuation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
    python ecosystem-services-valuation.py --input ndvi.tif --output-dir ./out

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
SKILL_NAME = "ecosystem-services-valuation"

# ---- 复用共享核心库（本地 vendored，随脚本目录一起分发）----
try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, to_exit_code,
    )
    from _geoskill_core.manifest import OutputManifest, OutputFile
except ImportError:  # pragma: no cover - fallback minimal definitions
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
# Input validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> None:
    """Validate a [W, S, E, N] geographic bbox (exit 6 on failure)."""
    w, s, e, n = bbox
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError(
            f"bbox contains non-finite values: W={w} S={s} E={e} N={n}",
            bbox=list(bbox),
        )
    if abs(w) > 180.0 or abs(e) > 180.0:
        raise ValidationError(
            f"bbox longitude out of range: W={w} E={e} (must be in [-180, 180])",
            bbox=list(bbox),
        )
    if abs(s) > 90.0 or abs(n) > 90.0:
        raise ValidationError(
            f"bbox latitude out of range: S={s} N={n} (must be in [-90, 90])",
            bbox=list(bbox),
        )
    if w >= e:
        raise ValidationError(
            f"bbox reversed: W ({w}) must be < E ({e}). "
            f"For antimeridian-crossing bboxes, split into W..180 and -180..E.",
            bbox=list(bbox),
        )
    if s >= n:
        raise ValidationError(
            f"bbox reversed: S ({s}) must be < N ({n})", bbox=list(bbox)
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero area: W={w} S={s} E={e} N={n}", bbox=list(bbox)
        )


def read_geotiff_with_nodata(
    path: str,
) -> Tuple[np.ndarray, List[float], int]:
    """Read multi-band GeoTIFF replacing NoData with NaN; report n_valid."""
    cube, bbox = read_geotiff(path)
    import rasterio
    with rasterio.open(path) as src:
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == nodata, np.nan, cube).astype(np.float32)
    n_valid = int(np.sum(np.any(np.isfinite(cube), axis=0)))
    return cube, bbox, n_valid


# ---------------------------------------------------------------------------
# 当量因子表（谢高地等 2015，单位：当量/ha；1 当量 ≈ 全国均值粮食产值）
# 格式：{LULC类别: (供给, 调节, 支持, 文化)}
# ---------------------------------------------------------------------------
EQUIV_FACTOR_TABLE: Dict[str, Tuple[float, float, float, float]] = {
    "forest":    (2.01, 6.30, 3.02, 0.78),
    "grassland": (1.20, 3.80, 2.10, 0.35),
    "cropland":  (2.30, 1.40, 1.80, 0.10),
    "water":     (0.80, 5.20, 2.50, 1.80),
    "built":     (0.00, 0.10, 0.05, 0.01),
}
SERVICE_NAMES = ["provisioning", "regulating", "supporting", "cultural"]
LULC_CLASSES = list(EQUIV_FACTOR_TABLE.keys())
EQUIV_UNIT_VALUE = 3000.0  # 1 个当量对应元/ha/yr（全国均值参考）


def classify_lulc(ndvi: np.ndarray) -> np.ndarray:
    """从 NDVI 阈值分类 LULC，返回整型编码栅格（0=forest..4=built）。"""
    codes = np.zeros(ndvi.shape, dtype=np.int8)
    codes[ndvi < -0.05] = 3                        # water
    codes[(ndvi >= -0.05) & (ndvi < 0.15)] = 4     # built / bare
    codes[(ndvi >= 0.15) & (ndvi < 0.35)] = 2      # cropland
    codes[(ndvi >= 0.35) & (ndvi < 0.55)] = 1      # grassland
    codes[ndvi >= 0.55] = 0                        # forest
    return codes


def compute_service_values(
    codes: np.ndarray,
    pixel_area_ha: float,
    unit_value: float = EQUIV_UNIT_VALUE,
) -> np.ndarray:
    """计算各服务价值栅格（元/yr/pixel）。返回 shape=(4, H, W)。"""
    h, w = codes.shape
    values = np.zeros((4, h, w), dtype=np.float32)
    for ci, cls_name in enumerate(LULC_CLASSES):
        mask = codes == ci
        factors = EQUIV_FACTOR_TABLE[cls_name]
        for si in range(4):
            values[si][mask] = factors[si] * unit_value * pixel_area_ha
    return values


def generate_synthetic_esv(
    bbox: List[float], width: int = 128, height: int = 128, seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy /= max(height - 1, 1)
    xx /= max(width - 1, 1)
    ndvi = (
        0.10 + 0.55 * xx + 0.20 * np.sin(4 * np.pi * yy)
        + rng.normal(0, 0.04, (height, width))
    ).astype(np.float32)
    ndvi = np.clip(ndvi, -0.2, 0.9)
    ndvi[(xx < 0.25) & (yy < 0.25)] = -0.15  # 水体
    info = {"bbox": bbox, "width": width, "height": height}
    return ndvi, info


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
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
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
    # validate bbox shape up front (before any disk I/O or makedirs)
    if bbox is not None:
        validate_bbox(bbox)

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input raster not found: {args.input}", path=args.input)
        cube, file_bbox, n_valid = read_geotiff_with_nodata(args.input)
        if bbox is None:
            bbox = file_bbox
            validate_bbox(bbox)
        if cube.shape[0] < 1:
            raise ValidationError("input raster has no bands")
        if n_valid == 0:
            raise ValidationError(
                "input raster has no valid (non-NoData) pixels",
                n_bands=int(cube.shape[0]),
            )
        ndvi = cube[0]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        ndvi, synth_info = generate_synthetic_esv(bbox)
        source_note = "synthetic"
        n_valid = int(np.sum(np.isfinite(ndvi)))

    if ndvi.size == 0:
        raise ValidationError("input raster is empty")

    h, w = ndvi.shape
    lat_mid = (bbox[1] + bbox[3]) / 2.0
    dx_m = (bbox[2] - bbox[0]) / w * 111320 * np.cos(np.deg2rad(lat_mid))
    dy_m = (bbox[3] - bbox[1]) / h * 111320
    pixel_area_ha = (dx_m * dy_m) / 10000.0

    # NoData handling: pixels with NoData should not be classified as any LULC.
    # Replace remaining NoData (NaN) with a sentinel that classify_lulc() treats
    # as "no service" (built, which has near-zero equivalent factors). The
    # ``classify_lulc`` thresholds are checked in order, and NDVI = NaN fails
    # every comparison → code remains 0 (forest). We must explicitly handle
    # this: NaN pixels are forced to "built" so the service value is essentially
    # zero and properly distinguished from real forest.
    if not np.all(np.isfinite(ndvi)):
        # Mask out NaN pixels before classification; we'll set them to code=4
        # (built) post-hoc so they contribute ~0 to service totals.
        nan_mask = ~np.isfinite(ndvi)
        ndvi_for_class = np.where(nan_mask, 0.05, ndvi).astype(np.float32)  # 0.05 → built
    else:
        nan_mask = np.zeros_like(ndvi, dtype=bool)
        ndvi_for_class = ndvi

    codes = classify_lulc(ndvi_for_class)
    # Force NaN pixels to "built" (code 4) explicitly
    if nan_mask.any():
        codes[nan_mask] = 4

    values = compute_service_values(codes, pixel_area_ha)

    # create output dir only after all validations have passed
    os.makedirs(output_dir, exist_ok=True)

    outputs = []
    service_totals: Dict[str, float] = {}
    for si, sname in enumerate(SERVICE_NAMES):
        out_path = os.path.join(output_dir, f"value_{sname}.tif")
        write_geotiff(out_path, values[si], bbox)
        service_totals[sname] = float(np.sum(values[si]))
        outputs.append({"path": out_path, "kind": "raster", "crs_epsg": 4326,
                        "bbox_wgs84": bbox, "band_count": 1})

    total_all = sum(service_totals.values())
    n_total = int(codes.size)
    params = {
        "pixel_area_ha": pixel_area_ha,
        "equiv_unit_value": EQUIV_UNIT_VALUE,
        "service_totals_yr": service_totals,
        "total_ecosystem_value_yr": total_all,
        "lulc_class_counts": {LULC_CLASSES[i]: int(np.sum(codes == i)) for i in range(5)},
    }
    params_path = os.path.join(output_dir, "service_value_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)
    outputs.append({"path": params_path, "kind": "json"})

    qa: Dict[str, Any] = {
        "source": source_note,
        "pixel_area_ha": round(pixel_area_ha, 4),
        "service_totals_yr": service_totals,
        "total_ecosystem_value_yr": total_all,
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
    }
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        for sn in SERVICE_NAMES:
            print(f"[{SKILL_NAME}] {sn}: {service_totals[sn]:,.0f} 元/yr")
        print(f"[{SKILL_NAME}] total: {total_all:,.0f} 元/yr")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Ecosystem services valuation via equivalent-factor method.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF (band1=NDVI or reflectance)")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic NDVI scene (offline)")
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
