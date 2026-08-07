#!/usr/bin/env python3
"""urban-growth-boundary — 城市增长边界

从历史扩张与多源约束划定城市增长边界。核心算法：

- **扩张速率**：relative_rate = (area_t2 − area_t1) / area_t1 / years
  （相对年均增长率）。
- **扩张方向/趋势**：用两期建成区差值（新增像元）的空间分布表征
  扩张趋势场（expansion_tendency）。
- **约束因子**：地形坡度、耕地、生态保护区各产生一个惩罚 ∈ [0, 1]，
  惩罚越大越不宜扩张。
- **增长适宜性**：suitability = tendency × Π(1 − w_i × penalty_i)，∈ [0, 1]。
- **增长边界**：适宜性高于阈值的连片区域外缘即城市增长边界（UGB）。

数据源：本地双期建成区 + 约束栅格，或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络。

Usage:
    python urban-growth-boundary.py --input built_t2.tif --built-t1 built_t1.tif
    python urban-growth-boundary.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "urban-growth-boundary"

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
# 校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Optional[List[float]]) -> List[float]:
    """Validate a [W, S, E, N] bbox in EPSG:4326.

    Rules:
      - W < E, S < N (non-degenerate)
      - lon ∈ [-180, 180], lat ∈ [-90, 90]
      - bbox area (in degree^2) must be > 0
      - cannot cross the 180° meridian (split into two if needed)

    Returns the validated bbox. Raises ValidationError on failure.
    """
    if bbox is None:
        raise ValidationError("bbox is required (provide --bbox or --input)")
    if len(bbox) != 4:
        raise ValidationError(f"bbox must have 4 floats, got {len(bbox)}")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox lon out of range [-180, 180]: W={w} E={e}",
            bbox=bbox,
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox lat out of range [-90, 90]: S={s} N={n}",
            bbox=bbox,
        )
    if w >= e:
        raise ValidationError(
            f"bbox W must be < E (got W={w} E={e}); cross-180° not supported, "
            f"split into two bboxes and merge results manually",
            bbox=bbox,
        )
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N (got S={s} N={n})",
            bbox=bbox,
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox area too small: dlon={e - w}, dlat={n - s}",
            bbox=bbox,
        )
    return [w, s, e, n]


def validate_params(args: argparse.Namespace) -> None:
    """Validate numeric parameters that argparse does not range-check."""
    if not (0.0 <= float(args.threshold) <= 1.0):
        raise ValidationError(
            f"--threshold must be in [0, 1] (got {args.threshold})",
            threshold=args.threshold,
        )
    if float(args.years) <= 0:
        raise ValidationError(
            f"--years must be > 0 (got {args.years})",
            years=args.years,
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------

def expansion_rate(area_t1: float, area_t2: float, years: float) -> float:
    """相对年均扩张速率 = (A2 − A1) / A1 / years。

    A1 ≤ 0 或 years ≤ 0 时返回 0。
    """
    if area_t1 <= 0 or years <= 0:
        return 0.0
    return float(area_t2 - area_t1) / float(area_t1) / float(years)


def expansion_tendency(built_t1: np.ndarray, built_t2: np.ndarray,
                       smooth: int = 5) -> np.ndarray:
    """扩张趋势场：新增建成区（t2 − t1）经平滑后的空间分布，归一化到 [0, 1]。"""
    from scipy.ndimage import uniform_filter
    b1 = (np.asarray(built_t1, dtype=np.float32) > 0).astype(np.float32)
    b2 = (np.asarray(built_t2, dtype=np.float32) > 0).astype(np.float32)
    growth = np.clip(b2 - b1, 0.0, 1.0)
    tend = uniform_filter(growth, size=smooth, mode="nearest")
    mx = float(tend.max())
    if mx > 1e-8:
        tend = tend / mx
    return tend.astype(np.float32)


def constraint_penalty(
    slope: np.ndarray,
    cropland: np.ndarray,
    ecological: np.ndarray,
    w_slope: float = 0.4,
    w_crop: float = 0.3,
    w_eco: float = 0.3,
) -> np.ndarray:
    """综合约束惩罚 = Σ w_i × penalty_i，∈ [0, 1]。

    各因子已是 [0, 1] 的惩罚强度（坡度陡/耕地多/生态敏感 → 高）。
    """
    s = np.clip(np.asarray(slope, dtype=np.float32), 0.0, 1.0)
    c = np.clip(np.asarray(cropland, dtype=np.float32), 0.0, 1.0)
    e = np.clip(np.asarray(ecological, dtype=np.float32), 0.0, 1.0)
    penalty = w_slope * s + w_crop * c + w_eco * e
    return np.clip(penalty, 0.0, 1.0).astype(np.float32)


def growth_suitability(tendency: np.ndarray, penalty: np.ndarray) -> np.ndarray:
    """增长适宜性 = tendency × (1 − penalty)，∈ [0, 1]。"""
    t = np.clip(np.asarray(tendency, dtype=np.float32), 0.0, 1.0)
    p = np.clip(np.asarray(penalty, dtype=np.float32), 0.0, 1.0)
    return (t * (1.0 - p)).astype(np.float32)


def slope_from_dem(dem: np.ndarray, pixel_size: float = 1.0) -> np.ndarray:
    """坡度（归一化到 [0,1]）：gradient 幅值 / (1 + 幅值)。"""
    dem = np.asarray(dem, dtype=np.float32)
    gy, gx = np.gradient(dem, pixel_size, edge_order=1)
    mag = np.sqrt(gx * gx + gy * gy)
    norm = mag / (1.0 + mag)
    return norm.astype(np.float32)


# ---------------------------------------------------------------------------
# 合成数据：双期建成区 + 约束（坡度/耕地/生态）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height_px: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 built_t1, built_t2, slope, cropland, ecological。

    城市中心建成区随时间向外（尤其向东）扩张；
    北部为陡坡，南部为耕地，西部为生态保护区（约束）。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height_px, 0:width].astype(np.float32)
    cx, cy = width * 0.45, height_px * 0.5

    # t1：较小的核心建成区
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    built_t1 = (d < width * 0.15).astype(np.float32)
    # t2：向东扩张更多
    dx = (xx - cx) * 0.7
    d2 = np.sqrt(dx ** 2 + (yy - cy) ** 2)
    built_t2 = (d2 < width * 0.28).astype(np.float32)

    # 约束：北部陡坡、南部耕地、西部生态
    slope = np.clip((height_px - yy) / height_px, 0.0, 1.0)  # 北高
    slope = np.where(yy < height_px * 0.25, 0.9, 0.1)
    cropland = np.where(yy > height_px * 0.75, 0.9, 0.1)
    ecological = np.where(xx < width * 0.2, 0.9, 0.1)

    info = {
        "bbox": bbox, "width": width, "height": height_px,
    }
    return built_t1, built_t2, slope, cropland, ecological, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    cube: np.ndarray,
    bbox: List[float],
    nodata: float = -9999.0,
) -> None:
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
def write_manifest(
    output_dir: str,
    args: argparse.Namespace,
    outputs: List[Dict[str, Any]],
    qa: Dict[str, Any],
    started_at: str,
    exit_code: int,
    bbox: List[float],
) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME,
        skill_version=VERSION,
        command=cmd,
        started_at=started_at,
        finished_at=_utc_now(),
        exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "built_t1": getattr(args, "built_t1", None),
            "years": getattr(args, "years", 10.0),
            "threshold": getattr(args, "threshold", 0.3),
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

    # 1) 参数校验（前置：避免无效输入污染 output_dir）
    validate_params(args)

    bbox = list(args.bbox) if args.bbox else None

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        bbox = validate_bbox(bbox)
        built_t2 = (cube[0] > 0).astype(np.float32)
        if args.built_t1:
            t1_cube, _ = read_geotiff(args.built_t1)
            built_t1 = (t1_cube[0] > 0).astype(np.float32)
        else:
            from scipy.ndimage import binary_erosion
            built_t1 = binary_erosion(built_t2 > 0, iterations=3).astype(np.float32)
        slope = np.full_like(built_t2, 0.2)
        cropland = np.full_like(built_t2, 0.2)
        ecological = np.full_like(built_t2, 0.1)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        built_t1, built_t2, slope, cropland, ecological, synth_info = \
            generate_synthetic(bbox)
        source_note = "synthetic"

    if built_t2.size == 0:
        raise ValidationError("input raster is empty")

    # 校验通过后再创建输出目录（避免失败路径留下空目录）
    os.makedirs(output_dir, exist_ok=True)

    # 2) 扩张速率 + 趋势 + 约束 + 适宜性
    area_t1 = float((built_t1 > 0).sum())
    area_t2 = float((built_t2 > 0).sum())
    rate = expansion_rate(area_t1, area_t2, args.years)
    tendency = expansion_tendency(built_t1, built_t2)
    penalty = constraint_penalty(slope, cropland, ecological)
    suitability = growth_suitability(tendency, penalty)

    boundary = (suitability >= args.threshold).astype(np.uint8)

    # 3) 写出
    out_tif = os.path.join(output_dir, "growth_suitability.tif")
    stack = np.stack([suitability, boundary.astype(np.float32)], axis=0)
    write_geotiff(out_tif, stack, bbox)

    stats = {
        "area_t1_px": area_t1,
        "area_t2_px": area_t2,
        "expansion_rate_per_year": rate,
        "mean_suitability": float(np.mean(suitability)),
        "boundary_fraction": float(np.mean(boundary)),
        "years": args.years,
        "threshold": args.threshold,
    }
    stats_path = os.path.join(output_dir, "growth_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {"source": source_note}
    qa.update(stats)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 2},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] expansion rate: {rate:.4f}/yr")
        print(f"[{SKILL_NAME}] mean suitability: {stats['mean_suitability']:.3f}")
        print(f"[{SKILL_NAME}] boundary fraction: {stats['boundary_fraction']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Urban growth boundary from expansion history and constraints.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input built-up area GeoTIFF (epoch t2)")
    p.add_argument("--built-t1", help="earlier built-up area GeoTIFF (epoch t1)")
    p.add_argument("--years", type=float, default=10.0,
                   help="years between epochs (default: 10)")
    p.add_argument("--threshold", type=float, default=0.3,
                   help="suitability threshold for growth boundary (default: 0.3)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic scene (offline)")
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
