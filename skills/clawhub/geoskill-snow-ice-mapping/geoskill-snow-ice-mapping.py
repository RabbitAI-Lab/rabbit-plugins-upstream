#!/usr/bin/env python3
"""snow-ice-mapping — 积雪/冰体遥感制图

利用归一化雪指数 NDSI 提取积雪 / 冰体覆盖范围，并可叠加亮温阈值进一步
剔除低温误判：

- **NDSI** = (Green − SWIR) / (Green + SWIR)。雪在绿光波段高反射、短波红外
  强吸收，NDSI 显著偏高；``NDSI > --ndsi-threshold``（默认 0.4）判为雪。
- **温度阈值（可选）**：若提供亮温，叠加 ``温度 < --temp-threshold`` 约束，
  排除高反射但温暖的云/裸岩。

输出二值积雪栅格 GeoTIFF（1=雪 / 0=无雪）与面积统计 JSON（像元数、覆盖
比例、估算面积 km²）。

数据源：本地多波段 GeoTIFF（含绿光与短波红外波段）；或 ``--synthetic`` /
仅给 ``--bbox`` 时离线生成含雪区（高绿低 SWIR）的模拟影像。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python snow-ice-mapping.py --bbox 116 39 117 40 --ndsi-threshold 0.4
    python snow-ice-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out
    python snow-ice-mapping.py --input scene.tif --green-index 1 --swir-index 4

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
SKILL_NAME = "snow-ice-mapping"

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


# 经纬度 → 米的近似换算常数
M_PER_DEG_LAT = 110540.0
M_PER_DEG_LON_EQ = 111320.0


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


def validate_ndsi_threshold(value: float) -> float:
    """Validate --ndsi-threshold in [-1,1]; return float."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        raise ValidationError(f"ndsi-threshold must be a number, got {value!r}")
    if not (-1.0 <= v <= 1.0):
        raise ValidationError(f"ndsi-threshold must be in [-1,1], got {v}")
    return v


def validate_band_index(value: int, name: str) -> int:
    """Validate band index >= 0; return int."""
    try:
        v = int(value)
    except (TypeError, ValueError):
        raise ValidationError(f"{name} must be an integer, got {value!r}")
    if v < 0:
        raise ValidationError(f"{name} must be >= 0 (got {v}); negative indices "
                              f"would silently wrap to the last band")
    return v


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def compute_ndsi(green: np.ndarray, swir: np.ndarray) -> np.ndarray:
    """NDSI = (Green − SWIR) / (Green + SWIR)，值域 [-1, 1]。

    分母接近 0 处（极暗像元）返回 0，避免除零；任一波段为 NaN 的像元
    传播 NaN（不参与统计，也不被当作雪）。
    """
    green = green.astype(np.float32)
    swir = swir.astype(np.float32)
    denom = green + swir
    with np.errstate(divide="ignore", invalid="ignore"):
        ndsi = np.where(np.abs(denom) > 1e-6, (green - swir) / denom, 0.0)
    ndsi = np.where(np.isnan(green) | np.isnan(swir), np.nan, ndsi)
    return np.clip(ndsi, -1.0, 1.0).astype(np.float32)


def detect_snow(
    cube: np.ndarray,
    green_index: int = 1,
    swir_index: int = 4,
    ndsi_threshold: float = 0.4,
    temperature: Optional[np.ndarray] = None,
    temp_threshold: Optional[float] = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """检测积雪。返回 (snow_mask bool (H,W), ndsi (H,W))。

    若提供 temperature 且 temp_threshold 不为 None，则叠加温度约束
    （亮温低于阈值才判为雪）。
    """
    if cube.ndim == 2:
        raise ValidationError("cube must be multiband (bands, H, W) for NDSI")
    nb = cube.shape[0]
    if green_index < 0 or swir_index < 0:
        raise ValidationError(
            f"band index must be >= 0: green={green_index} swir={swir_index}")
    if green_index >= nb or swir_index >= nb:
        raise ValidationError(
            f"band index out of range: green={green_index} swir={swir_index} "
            f"but cube has {nb} bands",
            green_index=int(green_index), swir_index=int(swir_index), bands=int(nb),
        )
    green = cube[green_index]
    swir = cube[swir_index]
    ndsi = compute_ndsi(green, swir)
    snow = ndsi > ndsi_threshold

    if temperature is not None and temp_threshold is not None:
        snow = snow & (temperature < temp_threshold)
    return snow, ndsi


def pixel_area_km2(bbox: List[float], height: int, width: int) -> float:
    """估算单个像元的地表面积（km²），用 bbox 中心纬度修正经度收缩。"""
    w, s, e, n = bbox
    mid_lat = (s + n) / 2.0
    dx_m = (e - w) * M_PER_DEG_LON_EQ * np.cos(np.deg2rad(mid_lat)) / max(width, 1)
    dy_m = (n - s) * M_PER_DEG_LAT / max(height, 1)
    return float(abs(dx_m * dy_m) / 1e6)


def snow_area_stats(snow_mask: np.ndarray, bbox: List[float]) -> Dict[str, Any]:
    """统计积雪像元数、覆盖率与估算面积。"""
    h, w = snow_mask.shape
    n_snow = int(np.count_nonzero(snow_mask))
    npx = h * w
    px_km2 = pixel_area_km2(bbox, h, w)
    return {
        "snow_pixels": n_snow,
        "total_pixels": int(npx),
        "snow_fraction": round(n_snow / npx, 6),
        "pixel_area_km2": round(px_km2, 6),
        "snow_area_km2": round(n_snow * px_km2, 4),
        "total_area_km2": round(npx * px_km2, 4),
    }


# ---------------------------------------------------------------------------
# 合成数据：含雪区的模拟影像
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    bands: int = 6,
    green_index: int = 1,
    swir_index: int = 4,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any], np.ndarray]:
    """生成 (bands, H, W) 反射率影像 + 亮温 (H,W)，含一块高 NDSI 雪区。

    地物：背景为植被/土壤（绿低 SWIR 高，NDSI<0），雪区（绿高 SWIR 低，
    NDSI~0.78）。亮温：雪冷（~258K），背景暖（~290K）。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yy = yy.astype(np.float32) / max(height - 1, 1)
    xx = xx.astype(np.float32) / max(width - 1, 1)

    # 雪区：右上三角
    snow_mask = ((xx + yy) > 1.2)
    truth = snow_mask.astype(np.uint8)

    # 逐波段基准反射率（6 波段：蓝绿红红边NIR SWIR）
    green_bg, green_snow = 0.10, 0.80
    swir_bg, swir_snow = 0.30, 0.10

    cube = np.zeros((bands, height, width), dtype=np.float32)
    for b in range(bands):
        if b == green_index:
            layer = np.where(snow_mask, green_snow, green_bg)
        elif b == swir_index:
            layer = np.where(snow_mask, swir_snow, swir_bg)
        else:
            layer = np.where(snow_mask, 0.7, 0.15)
        layer = layer.astype(np.float32)
        layer = layer + rng.normal(0, 0.01, size=layer.shape).astype(np.float32)
        cube[b] = np.clip(layer, 0.0, 1.0)

    # 亮温：雪冷、背景暖
    temperature = np.where(snow_mask, 258.0, 290.0).astype(np.float32)
    temperature = temperature + rng.normal(0, 1.0, size=temperature.shape).astype(np.float32)

    info = {
        "bbox": bbox, "width": width, "height": height, "bands": bands,
        "green_index": green_index, "swir_index": swir_index,
        "truth_snow_fraction": round(float(np.count_nonzero(snow_mask)) / (height * width), 6),
    }
    return cube, temperature, info, truth


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
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


def write_geotiff(path, array, bbox, dtype="uint8", nodata=255):
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
            "ndsi_threshold": getattr(args, "ndsi_threshold", None),
            "green_index": getattr(args, "green_index", None),
            "swir_index": getattr(args, "swir_index", None),
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

    # --- Upfront validation (BEFORE makedirs; rc=6 for bad data, rc=2 for bad CLI) ---
    if args.bbox is not None:
        validate_bbox(args.bbox)
    validate_ndsi_threshold(args.ndsi_threshold)
    validate_band_index(args.green_index, "--green-index")
    validate_band_index(args.swir_index, "--swir-index")

    temperature: Optional[np.ndarray] = None
    synth_info: Optional[Dict[str, Any]] = None
    total_pix = 0
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            validate_bbox(bbox)
        if cube.ndim != 3:
            raise ValidationError("input raster must be multiband (bands, H, W)")
        source_note = args.input
        total_pix = int(cube.shape[1] * cube.shape[2])
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, temperature, synth_info, _truth = generate_synthetic(
            bbox, green_index=args.green_index, swir_index=args.swir_index,
        )
        source_note = "synthetic"
        total_pix = int(cube.shape[1] * cube.shape[2])

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    # NoData（已转为 NaN）像素不参与检测；全 NoData → exit 6
    n_valid = int(np.count_nonzero(np.isfinite(cube).all(axis=0)))
    if n_valid == 0:
        raise ValidationError("input raster has no valid pixels (all NoData)")

    # 温度阈值：仅在有温度数据（合成模式）时生效
    temp = temperature if temperature is not None else None
    snow, ndsi = detect_snow(
        cube, green_index=args.green_index, swir_index=args.swir_index,
        ndsi_threshold=args.ndsi_threshold,
        temperature=temp, temp_threshold=args.temp_threshold,
    )

    # --- Output dir (only after all upfront validation passes) ---
    os.makedirs(output_dir, exist_ok=True)

    snow_u8 = snow.astype(np.uint8)
    out_tif = os.path.join(output_dir, "snow_cover.tif")
    write_geotiff(out_tif, snow_u8, bbox, dtype="uint8", nodata=255)

    # NDSI 连续产品（便于检查）
    ndsi_tif = os.path.join(output_dir, "ndsi.tif")
    write_geotiff(ndsi_tif, ndsi, bbox, dtype="float32", nodata=-9999.0)

    stats = snow_area_stats(snow, bbox)
    stats.update({
        "ndsi_threshold": args.ndsi_threshold,
        "green_index": args.green_index,
        "swir_index": args.swir_index,
        "temp_threshold": args.temp_threshold,
        "mean_ndsi": round(float(np.nanmean(ndsi)), 4),
    })
    stats_path = os.path.join(output_dir, "snow_area_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "input_nodata": -9999.0,
        "n_valid_pixels": n_valid,
        "n_total_pixels": total_pix,
    }
    qa.update(stats)
    if synth_info is not None:
        qa["truth_snow_fraction"] = synth_info["truth_snow_fraction"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": ndsi_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] snow fraction: {stats['snow_fraction']:.4f}")
        print(f"[{SKILL_NAME}] snow area:     {stats['snow_area_km2']:.2f} km2")
        print(f"[{SKILL_NAME}] mean NDSI:     {stats['mean_ndsi']:.4f}")
        print(f"[{SKILL_NAME}] snow raster: {out_tif}")
        print(f"[{SKILL_NAME}] stats: {stats_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Map snow/ice cover using the NDSI index and optional temperature threshold.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multiband GeoTIFF (reflectance)")
    p.add_argument("--green-index", type=int, default=1,
                   help="0-based band index for green (default: 1)")
    p.add_argument("--swir-index", type=int, default=4,
                   help="0-based band index for SWIR (default: 4)")
    p.add_argument("--ndsi-threshold", type=float, default=0.4,
                   help="NDSI threshold for snow (default: 0.4)")
    p.add_argument("--temp-threshold", type=float, default=None,
                   help="optional brightness-temperature upper bound (K) for snow")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic scene with a snow region (offline)")
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
