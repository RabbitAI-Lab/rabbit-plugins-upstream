#!/usr/bin/env python3
"""urban-population-estimation — 城市人口估算

从建筑体积、夜光和土地利用权重估算人口密度空间分布。核心算法：

- **建筑体积**：volume = 足迹面积 × 建筑高度。
- **居住权重**：raw_weight = volume × 居住率 × 夜光强度 × LULC 权重。
  夜光校正：夜光越亮，人类活动越强，权重越高。
  LULC 权重：仅居住/商业用地承载人口，水体/植被权重为 0。
- **人口分配（守恒）**：density = weight / Σweight × total_population / pixel_area。
  关键性质：Σ(density × pixel_area) = total_population（人口总量严格守恒）。

数据源：本地建筑高度 + 夜光 + LULC GeoTIFF，或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络。

Usage:
    python urban-population-estimation.py --input height.tif --nightlight nl.tif --lulc lulc.tif
    python urban-population-estimation.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "urban-population-estimation"

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
    """Validate numeric parameters (population conservation + pixel geometry)."""
    if float(args.total_population) < 0:
        raise ValidationError(
            f"--total-population must be >= 0 (got {args.total_population})",
            total_population=args.total_population,
        )
    if float(args.pixel_size) <= 0:
        raise ValidationError(
            f"--pixel-size must be > 0 m (got {args.pixel_size})",
            pixel_size=args.pixel_size,
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------

def building_volume(footprint_area: np.ndarray, height: np.ndarray) -> np.ndarray:
    """建筑体积 = 足迹面积 × 高度（m³）。"""
    a = np.clip(np.asarray(footprint_area, dtype=np.float32), 0.0, None)
    h = np.clip(np.asarray(height, dtype=np.float32), 0.0, None)
    return (a * h).astype(np.float32)


def nightlight_weight(nightlight: np.ndarray) -> np.ndarray:
    """夜光校正权重：归一化到 [0.1, 1]，避免零权重抹掉有人区。

    weight = 0.1 + 0.9 × norm(nightlight)，norm 按全局最大值。
    """
    nl = np.clip(np.asarray(nightlight, dtype=np.float32), 0.0, None)
    mx = float(np.nanmax(nl)) if nl.size > 0 else 1.0
    if mx < 1e-8:
        return np.full_like(nl, 0.5, dtype=np.float32)
    norm = nl / mx
    return (0.1 + 0.9 * norm).astype(np.float32)


# LULC 权重表：类别码 → 人口承载权重
LULC_WEIGHTS: Dict[int, float] = {
    0: 0.0,   # 无数据 / 水体
    1: 0.0,   # 水体
    2: 1.0,   # 居住用地
    3: 0.8,   # 商业/工业
    4: 0.1,   # 交通
    5: 0.0,   # 植被
    6: 0.0,   # 裸地
}


def lulc_weight(lulc: np.ndarray, table: Dict[int, float] = LULC_WEIGHTS) -> np.ndarray:
    """LULC 类别 → 人口承载权重（查表）。未知类别取 0.5。"""
    arr = np.asarray(lulc)
    out = np.full(arr.shape, 0.5, dtype=np.float32)
    for code, w in table.items():
        out[arr == code] = w
    return out.astype(np.float32)


def allocate_population(
    weight: np.ndarray,
    total_population: float,
    pixel_area: float,
) -> np.ndarray:
    """人口密度分配（人/单位面积），严格守恒总量。

    density = weight / Σweight × total_population / pixel_area。
    性质：Σ(density × pixel_area) = total_population。
    weight 全零时返回均匀分布以保守恒。
    """
    w = np.clip(np.asarray(weight, dtype=np.float64), 0.0, None)
    total_w = float(w.sum())
    n = w.size
    if total_w < 1e-12:
        w = np.ones_like(w)
        total_w = float(n)
    frac = w / total_w
    density = frac * float(total_population) / float(pixel_area)
    return density.astype(np.float64)


# ---------------------------------------------------------------------------
# 合成数据：建筑高度 + 夜光 + LULC
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height_px: int = 128,
    total_population: float = 100000.0,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成建筑高度、夜光、LULC。

    左半区：高密度居住区（高建筑、亮夜光、LULC=2）。
    右半区：水体/植被（零建筑、暗夜光、LULC=1/5），几乎无人口。
    """
    rng = np.random.default_rng(seed)
    height = np.zeros((height_px, width), dtype=np.float32)
    nightlight = np.zeros((height_px, width), dtype=np.float32)
    lulc = np.zeros((height_px, width), dtype=np.int32)

    mid = width // 2
    # 左半区：居住
    height[:, :mid] = rng.uniform(10, 50, (height_px, mid)).astype(np.float32)
    nightlight[:, :mid] = rng.uniform(0.5, 1.0, (height_px, mid)).astype(np.float32)
    lulc[:, :mid] = 2

    # 右半区：上半水体，下半植被
    nightlight[:, mid:] = rng.uniform(0.0, 0.05, (height_px, width - mid)).astype(np.float32)
    lulc[:height_px // 2, mid:] = 1   # 水体
    lulc[height_px // 2:, mid:] = 5   # 植被

    info = {
        "bbox": bbox, "width": width, "height": height_px,
        "total_population": total_population,
    }
    return height, nightlight, lulc, info


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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], float]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        res = float(src.res[0]) if src.res else 1.0
    return cube, bbox, res


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
            "nightlight": getattr(args, "nightlight", None),
            "lulc": getattr(args, "lulc", None),
            "total_population": getattr(args, "total_population", 100000.0),
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
    pixel_area = args.pixel_size ** 2

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox, res = read_geotiff(args.input)
        height = cube[0]
        bbox = bbox if bbox is not None else file_bbox
        bbox = validate_bbox(bbox)
        if res > 0:
            pixel_area = res ** 2
        if args.nightlight:
            nl_cube, _, _ = read_geotiff(args.nightlight)
            nightlight = nl_cube[0]
        else:
            nightlight = np.ones_like(height) * 0.5
        if args.lulc:
            lc_cube, _, _ = read_geotiff(args.lulc)
            lulc = lc_cube[0].astype(np.int32)
        else:
            lulc = np.full_like(height, 2, dtype=np.int32)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        height, nightlight, lulc, synth_info = generate_synthetic(
            bbox, total_population=args.total_population)
        source_note = "synthetic"

    if height.size == 0:
        raise ValidationError("input raster is empty")

    # 校验通过后再创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 2) 体积 → 权重 → 人口分配
    footprint_area = (height > 0).astype(np.float32) * pixel_area
    volume = building_volume(footprint_area, height)
    nl_w = nightlight_weight(nightlight)
    lc_w = lulc_weight(lulc)
    weight = volume * nl_w * lc_w

    density = allocate_population(weight, args.total_population, pixel_area)
    density_f32 = density.astype(np.float32)

    # 守恒校验
    estimated_total = float(np.sum(density) * pixel_area)

    # 3) 写出
    out_tif = os.path.join(output_dir, "population_density.tif")
    write_geotiff(out_tif, density_f32, bbox)

    stats = {
        "target_population": args.total_population,
        "estimated_total_population": estimated_total,
        "conservation_error": abs(estimated_total - args.total_population),
        "mean_density": float(np.mean(density)),
        "max_density": float(np.max(density)),
        "pixel_area_m2": pixel_area,
    }
    stats_path = os.path.join(output_dir, "population_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {"source": source_note}
    qa.update(stats)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] target population: {args.total_population:.0f}")
        print(f"[{SKILL_NAME}] estimated total: {estimated_total:.1f} (error: {stats['conservation_error']:.2e})")
        print(f"[{SKILL_NAME}] mean density: {stats['mean_density']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Urban population estimation with volume, nightlight and LULC weights.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input building height GeoTIFF")
    p.add_argument("--nightlight", help="nightlight GeoTIFF")
    p.add_argument("--lulc", help="land use / land cover GeoTIFF (integer codes)")
    p.add_argument("--total-population", type=float, default=100000.0,
                   help="total population to distribute (default: 100000)")
    p.add_argument("--pixel-size", type=float, default=10.0,
                   help="pixel size in meters (default: 10)")
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
