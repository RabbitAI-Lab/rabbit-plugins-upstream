#!/usr/bin/env python3
"""tsunami-inundation-mapping — 海啸淹没制图

基于 DEM 的 bathtub 淹没建模，并加入水文连通约束（只有与海岸连通的低洼区
才会被淹），输出淹没范围、水深、海啸到达时间与建议撤离区。

模型：

    淹没掩膜   = {DEM < 水位} ∩ {与海岸种子区 8-连通}
    水深       = max(水位 - DEM, 0)  （仅淹没像元）
    到达时间   = 到海岸种子区的欧氏距离 × 像元尺寸 / 波速
    撤离区     = 未淹没但高程 < 水位 + 安全余量 的临界地带

数据源：本地 DEM GeoTIFF（单波段，单位 m），或 ``--synthetic`` 生成海岸地形。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python tsunami-inundation-mapping.py --input dem.tif --water-level 15
    python tsunami-inundation-mapping.py --bbox 120 30 121 31 --synthetic --output-dir ./out

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
SKILL_NAME = "tsunami-inundation-mapping"

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
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox, *, allow_antimeridian_cross: bool = False) -> None:
    """校验 bbox=[W,S,E,N]（EPSG:4326 度）。"""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must have 4 floats [W S E N]")
    w, s, e, n = [float(v) for v in bbox]
    if not (all(np.isfinite([w, s, e, n]))):
        raise ValidationError("bbox contains non-finite values")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError("bbox lon out of [-180, 180]")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError("bbox lat out of [-90, 90]")
    if w >= e:
        if not allow_antimeridian_cross:
            raise ValidationError(
                f"bbox W>=E ({w} >= {e}); cross-180° not supported"
            )
        raise ValidationError(f"bbox W>=E ({w} >= {e})")
    if s >= n:
        raise ValidationError(f"bbox S>=N ({s} >= {n})")
    if (e - w) < 1e-4 or (n - s) < 1e-4:
        raise ValidationError(
            f"bbox too small (dx={e - w}, dy={n - s}); need >= 1e-4 degrees"
        )


def validate_params(args: argparse.Namespace) -> None:
    """校验 CLI 参数物理合理性 → ValidationError 触发 rc=6。"""
    if not (np.isfinite(args.water_level)):
        raise ValidationError(
            f"--water-level must be finite (got {args.water_level})"
        )
    if args.water_level < -100.0 or args.water_level > 200.0:
        raise ValidationError(
            f"--water-level {args.water_level} m is unrealistic "
            f"(expected -100 to 200 m for tsunami)"
        )
    if not (args.wave_speed > 0 and np.isfinite(args.wave_speed)):
        raise ValidationError(
            f"--wave-speed must be > 0 and finite (got {args.wave_speed})"
        )
    if args.wave_speed < 0.1 or args.wave_speed > 100.0:
        raise ValidationError(
            f"--wave-speed {args.wave_speed} m/s is unrealistic "
            f"(shallow-water tsunami celerity ~ 3-50 m/s)"
        )
    if args.cell_size is not None:
        if not (args.cell_size > 0 and np.isfinite(args.cell_size)):
            raise ValidationError(
                f"--cell-size must be > 0 and finite (got {args.cell_size})"
            )
        if args.cell_size > 1e6:
            raise ValidationError(
                f"--cell-size {args.cell_size} m is unrealistically large"
            )
    if not (args.evac_margin >= 0 and np.isfinite(args.evac_margin)):
        raise ValidationError(
            f"--evac-margin must be >= 0 and finite (got {args.evac_margin})"
        )
    if args.evac_margin > 100.0:
        raise ValidationError(
            f"--evac-margin {args.evac_margin} m is unrealistically large"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def bathtub_mask(dem: np.ndarray, water_level: float) -> np.ndarray:
    """Bathtub：高程低于水位的像元视为潜在淹没。NaN 视为无效（False）。"""
    d = np.asarray(dem, dtype=np.float64)
    if not np.all(np.isfinite(d)):
        # NaN -> +inf，使 NaN 永远不 < water_level（=False）
        d = np.where(np.isfinite(d), d, np.inf)
    return d < float(water_level)


def connected_to_ocean(wet: np.ndarray, seed_mask: Optional[np.ndarray] = None) -> np.ndarray:
    """水文连通约束：只保留与海岸种子区 8-连通的淹没像元。

    孤立的内陆洼地（即便高程低于水位）因与海洋不连通而不被淹没。
    """
    from scipy.ndimage import label
    wet = np.asarray(wet, dtype=bool)
    if seed_mask is None:
        seed_mask = np.zeros_like(wet)
        seed_mask[:, 0] = True  # 默认西侧列为海岸
    struct = np.ones((3, 3), dtype=int)
    labels, _n = label(wet, structure=struct)
    seed_labels = set(np.unique(labels[seed_mask & wet]).tolist())
    seed_labels.discard(0)
    if not seed_labels:
        return np.zeros_like(wet)
    return np.isin(labels, list(seed_labels))


def inundation(dem: np.ndarray, water_level: float,
               seed_mask: Optional[np.ndarray] = None) -> np.ndarray:
    """完整淹没范围 = bathtub ∩ 海岸连通。"""
    wet = bathtub_mask(dem, water_level)
    return connected_to_ocean(wet, seed_mask)


def water_depth(dem: np.ndarray, water_level: float, inund: np.ndarray) -> np.ndarray:
    """淹没水深（m）：水位 - 高程，非淹没区为 0，恒非负。"""
    d = (float(water_level) - np.asarray(dem, dtype=np.float64))
    d = np.where(inund, np.clip(d, 0.0, None), 0.0)
    return d.astype(np.float32)


def arrival_time(inund: np.ndarray, seed_mask: Optional[np.ndarray] = None,
                 cell_size: float = 30.0, wave_speed: float = 5.0) -> np.ndarray:
    """海啸到达时间（s）：到海岸种子区的欧氏距离 × 像元尺寸 / 波速。

    距离越远到达越晚；非淹没区为 0。波速可近似浅水波速 sqrt(g·h)。
    """
    from scipy.ndimage import distance_transform_edt
    inund = np.asarray(inund, dtype=bool)
    if seed_mask is None:
        seed_mask = np.zeros_like(inund)
        seed_mask[:, 0] = True
    src = seed_mask & inund
    if not src.any():
        return np.zeros(inund.shape, dtype=np.float32)
    dist_cells = distance_transform_edt(~src)
    t = dist_cells * float(cell_size) / float(wave_speed)
    t = np.where(inund, t, 0.0)
    return t.astype(np.float32)


def evacuation_zone(dem: np.ndarray, inund: np.ndarray, water_level: float,
                    margin: float = 5.0) -> np.ndarray:
    """撤离区：未被淹没但高程 < 水位 + 安全余量 的临界低地（需提前撤离）。

    与淹没区互斥（保证是干地）。
    """
    dem = np.asarray(dem, dtype=np.float64)
    dry_low = (~np.asarray(inund, dtype=bool)) & (dem < float(water_level) + float(margin))
    return dry_low.astype(bool)


# ---------------------------------------------------------------------------
# 合成数据：海岸地形（西低东高 + 山脊 + 孤立内陆洼地）
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64,
                       seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float64) / max(width - 1, 1)
    yn = yy.astype(np.float64) / max(height - 1, 1)
    # 基础地形：从海岸(西,0m)向东抬升到 ~40m
    dem = xn * 40.0
    # 一道南北向山脊（中部隆起）
    dem += 15.0 * np.exp(-((xn - 0.55) ** 2) / (2 * 0.05 ** 2))
    # 孤立内陆洼地（山脊以东的高原上的坑，不与海连通）
    basin = 12.0 * np.exp(-(((xn - 0.8) ** 2 + (yn - 0.5) ** 2)) / (2 * 0.06 ** 2))
    dem -= basin
    dem += rng.normal(0, 0.3, dem.shape)
    dem = np.clip(dem, -2.0, None).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "min_elev": float(dem.min()), "max_elev": float(dem.max())}
    return dem, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0, dtype: str = "float32") -> None:
    import rasterio
    from rasterio.transform import from_bounds
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {"driver": "GTiff", "height": h, "width": w, "count": nb,
               "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
               "nodata": nodata, "compress": "deflate"}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype(dtype), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], float]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        nd = src.nodata
        if nd is not None and np.isfinite(nd):
            cube = np.where(cube == nd, np.nan, cube).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        res = float(src.res[0]) if src.res and src.res[0] else 30.0
    return cube, bbox, res


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir: str, inputs: Dict[str, Any], outputs: List[Dict[str, Any]],
                   qa: Dict[str, Any], started_at: str, exit_code: int) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs=inputs, outputs=[OutputFile(**o) for o in outputs], qa=qa,
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

    # 1) 参数与 bbox 校验（先做，不创建任何目录）
    validate_params(args)

    bbox = list(args.bbox) if args.bbox else None

    if args.input and not args.synthetic:
        cube, file_bbox, res = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        dem = cube[0]
        cell_size = args.cell_size or res
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <dem>")
        validate_bbox(bbox)
        dem, _info = generate_synthetic(bbox)
        # 像元尺寸 ≈ 区域跨度 / 像元数（米，粗略纬度换算）
        span_m = (bbox[2] - bbox[0]) * 111320.0 * np.cos(np.deg2rad(np.mean([bbox[1], bbox[3]])))
        cell_size = args.cell_size or max(span_m / 64.0, 1.0)
        source_note = "synthetic"

    # input 模式也要校验 bbox
    if bbox is not None:
        validate_bbox(bbox)

    if dem.size == 0:
        raise ValidationError("DEM is empty")

    # 全 NaN 检查（NoData -> NaN 后）
    n_total = int(dem.size)
    n_valid = int(np.sum(np.isfinite(dem)))
    if n_valid == 0:
        raise ValidationError(
            f"DEM has no valid pixels (n_valid=0, n_total={n_total})"
        )

    # 所有校验通过 → 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    seed = np.zeros(dem.shape, dtype=bool)
    seed[:, 0] = True
    inund = inundation(dem, args.water_level, seed)
    depth = water_depth(dem, args.water_level, inund)
    arr = arrival_time(inund, seed, cell_size=cell_size, wave_speed=args.wave_speed)
    evac = evacuation_zone(dem, inund, args.water_level, margin=args.evac_margin)

    inund_tif = os.path.join(output_dir, "inundation.tif")
    write_geotiff(inund_tif, inund.astype("int16"), bbox, nodata=-1, dtype="int16")
    depth_tif = os.path.join(output_dir, "water_depth.tif")
    write_geotiff(depth_tif, depth, bbox)
    arr_tif = os.path.join(output_dir, "arrival_time.tif")
    write_geotiff(arr_tif, arr, bbox)
    evac_tif = os.path.join(output_dir, "evacuation_zone.tif")
    write_geotiff(evac_tif, evac.astype("int16"), bbox, nodata=-1, dtype="int16")

    area_px = int(np.count_nonzero(inund))
    px_area_m2 = float(cell_size) ** 2
    params = {"source": source_note, "water_level": args.water_level,
              "wave_speed": args.wave_speed, "cell_size": float(cell_size),
              "evac_margin": args.evac_margin}
    params_path = os.path.join(output_dir, "tsunami_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "water_level": args.water_level,
        "inundated_pixels": area_px,
        "inundated_area_km2": area_px * px_area_m2 / 1e6,
        "max_depth_m": float(depth.max()) if depth.size else 0.0,
        "mean_depth_m": float(depth[inund].mean()) if area_px and inund.any() else 0.0,
        "max_arrival_s": float(arr.max()) if arr.size else 0.0,
        "evacuation_pixels": int(np.count_nonzero(evac)),
        "n_total_pixels": n_total,
        "n_valid_pixels": n_valid,
        "input_nodata_handling": "NoData->NaN",
    }
    outputs = [
        {"path": inund_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": depth_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": arr_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": evac_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, {"input": args.input, "bbox": bbox,
                              "water_level": args.water_level, "synthetic": bool(args.synthetic)},
                              outputs, qa, started_at, 0)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] water level: {args.water_level} m")
        print(f"[{SKILL_NAME}] inundated: {qa['inundated_area_km2']:.3f} km2  max depth: {qa['max_depth_m']:.2f} m")
        print(f"[{SKILL_NAME}] outputs: {output_dir}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Tsunami inundation mapping (bathtub + hydrological connectivity).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input DEM GeoTIFF (single band, meters)")
    p.add_argument("--water-level", type=float, default=10.0, help="tsunami water level (m, default: 10)")
    p.add_argument("--wave-speed", type=float, default=5.0, help="wave celerity (m/s, default: 5)")
    p.add_argument("--cell-size", type=float, default=None, help="pixel size in meters (auto if omitted)")
    p.add_argument("--evac-margin", type=float, default=5.0, help="evacuation safety margin (m, default: 5)")
    p.add_argument("--synthetic", action="store_true")
    p.add_argument("--output-dir", default="./output")
    p.add_argument("--quiet", action="store_true")
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
