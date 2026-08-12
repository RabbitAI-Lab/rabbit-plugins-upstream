#!/usr/bin/env python3
"""urban-microclimate — 城市微气候分析

从地表温度、植被、不透水面和建筑形态分析城市微气候。核心算法：

- **地表温度 LST 建模**：LST = base + α×ISA − β×NDVI。
  不透水面（ISA）加热、植被（NDVI）降温，符合地表能量平衡物理。
- **热岛强度 UHII**：UHII = LST − LST_rural（郊区参考温度）。
  关键性质：UHII 与 ISA 正相关（ISA 越高，热岛越强）。
- **通风指数**：VI = SVF × (1 − building_density)。
  建筑密度越高、天空可视因子越低 → 通风越差。值域 [0, 1]。

数据源：本地多源栅格（LST/ISA/NDVI/建筑密度/SVF），
或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络。

Usage:
    python urban-microclimate.py --input lst.tif --isa isa.tif --ndvi ndvi.tif
    python urban-microclimate.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "urban-microclimate"

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
    """Validate numeric parameters (physics + algebra constraints)."""
    if float(args.alpha) < 0:
        raise ValidationError(
            f"--alpha must be >= 0 (ISA heating coefficient, got {args.alpha})",
            alpha=args.alpha,
        )
    if float(args.beta) < 0:
        raise ValidationError(
            f"--beta must be >= 0 (NDVI cooling coefficient, got {args.beta})",
            beta=args.beta,
        )
    if not (-100.0 <= float(args.rural_temp) <= 80.0):
        raise ValidationError(
            f"--rural-temp must be in [-100, 80] °C (got {args.rural_temp})",
            rural_temp=args.rural_temp,
        )
    if not (-100.0 <= float(args.base_temp) <= 80.0):
        raise ValidationError(
            f"--base-temp must be in [-100, 80] °C (got {args.base_temp})",
            base_temp=args.base_temp,
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------

def model_lst(
    isa: np.ndarray,
    ndvi: np.ndarray,
    base_temp: float = 25.0,
    alpha: float = 10.0,
    beta: float = 6.0,
) -> np.ndarray:
    """地表温度建模：LST = base + α×ISA − β×NDVI（℃）。

    ISA ∈ [0,1]（不透水面比例），NDVI ∈ [-1,1]。
    α>0（ISA 加热），β>0（NDVI 蒸散降温）。
    """
    i = np.clip(np.asarray(isa, dtype=np.float32), 0.0, 1.0)
    n = np.asarray(ndvi, dtype=np.float32)
    lst = base_temp + alpha * i - beta * n
    return lst.astype(np.float32)


def heat_island_intensity(lst: np.ndarray, rural_reference: float) -> np.ndarray:
    """热岛强度 UHII = LST − LST_rural（℃）。可为负（冷岛）。"""
    lst = np.asarray(lst, dtype=np.float32)
    return (lst - float(rural_reference)).astype(np.float32)


def ventilation_index(building_density: np.ndarray, svf: np.ndarray) -> np.ndarray:
    """通风指数 VI = SVF × (1 − building_density)，值域 [0, 1]。

    SVF ∈ [0,1]（天空可视因子），density ∈ [0,1]。
    密度高 + SVF 低 → 通风差。
    """
    d = np.clip(np.asarray(building_density, dtype=np.float32), 0.0, 1.0)
    s = np.clip(np.asarray(svf, dtype=np.float32), 0.0, 1.0)
    return (s * (1.0 - d)).astype(np.float32)


def correlation(a: np.ndarray, b: np.ndarray) -> float:
    """皮尔逊相关系数（忽略 NaN）。"""
    x = np.asarray(a, dtype=np.float64).ravel()
    y = np.asarray(b, dtype=np.float64).ravel()
    finite = np.isfinite(x) & np.isfinite(y)
    x, y = x[finite], y[finite]
    if x.size < 2:
        return 0.0
    xm, ym = x.mean(), y.mean()
    denom = np.sqrt(np.sum((x - xm) ** 2) * np.sum((y - ym) ** 2))
    if denom < 1e-12:
        return 0.0
    return float(np.sum((x - xm) * (y - ym)) / denom)


# ---------------------------------------------------------------------------
# 合成数据：ISA 从中心向外递减，NDVI 相反，建筑密度中心高
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height_px: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 ISA, NDVI, building_density, SVF。

    城市中心 ISA 高、NDVI 低、密度高、SVF 低（深峡谷）；
    郊区相反。构成清晰的热岛梯度。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height_px, 0:width].astype(np.float32)
    cx, cy = width / 2.0, height_px / 2.0
    dist = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    dist_norm = dist / dist.max()

    isa = np.clip(1.0 - dist_norm + rng.normal(0, 0.03, dist.shape), 0.0, 1.0)
    ndvi = np.clip(0.6 * dist_norm - 0.1 + rng.normal(0, 0.03, dist.shape), -0.1, 0.8)
    building_density = np.clip(0.8 * (1.0 - dist_norm), 0.0, 1.0)
    svf = np.clip(0.3 + 0.6 * dist_norm, 0.0, 1.0)

    isa = isa.astype(np.float32)
    ndvi = ndvi.astype(np.float32)
    building_density = building_density.astype(np.float32)
    svf = svf.astype(np.float32)

    info = {
        "bbox": bbox, "width": width, "height": height_px,
    }
    return isa, ndvi, building_density, svf, info


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
            "rural_temp": getattr(args, "rural_temp", 22.0),
            "alpha": getattr(args, "alpha", 10.0),
            "beta": getattr(args, "beta", 6.0),
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
        if cube.shape[0] < 4:
            raise ValidationError("input must have 4 bands: ISA, NDVI, building_density, SVF")
        isa = cube[0]
        ndvi = cube[1]
        building_density = cube[2]
        svf = cube[3]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        isa, ndvi, building_density, svf, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    if isa.size == 0:
        raise ValidationError("input raster is empty")

    # 校验通过后再创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 2) LST 建模 → 热岛强度 → 通风指数
    lst = model_lst(isa, ndvi, base_temp=args.base_temp,
                    alpha=args.alpha, beta=args.beta)
    uhii = heat_island_intensity(lst, args.rural_temp)
    vi = ventilation_index(building_density, svf)

    # 3) UHII 与 ISA 的相关性（核心物理验证）
    corr_uhi_isa = correlation(uhii, isa)

    # 4) 写出（band1=LST, band2=UHII, band3=VI）
    out_tif = os.path.join(output_dir, "microclimate.tif")
    stack = np.stack([lst, uhii, vi], axis=0)
    write_geotiff(out_tif, stack, bbox)

    stats = {
        "mean_lst_c": float(np.mean(lst)),
        "mean_uhii_c": float(np.mean(uhii)),
        "max_uhii_c": float(np.max(uhii)),
        "mean_ventilation_index": float(np.mean(vi)),
        "correlation_uhii_isa": corr_uhi_isa,
        "rural_reference_c": args.rural_temp,
    }
    stats_path = os.path.join(output_dir, "microclimate_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {"source": source_note}
    qa.update(stats)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 3},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean LST: {stats['mean_lst_c']:.2f} C")
        print(f"[{SKILL_NAME}] mean UHII: {stats['mean_uhii_c']:.2f} C (max {stats['max_uhii_c']:.2f})")
        print(f"[{SKILL_NAME}] corr(UHII, ISA): {corr_uhi_isa:.3f}")
        print(f"[{SKILL_NAME}] mean ventilation index: {stats['mean_ventilation_index']:.3f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Urban microclimate: heat island intensity and ventilation index.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF with 4 bands: ISA, NDVI, density, SVF")
    p.add_argument("--base-temp", type=float, default=25.0,
                   help="base temperature in Celsius (default: 25)")
    p.add_argument("--alpha", type=float, default=10.0,
                   help="ISA heating coefficient (default: 10)")
    p.add_argument("--beta", type=float, default=6.0,
                   help="NDVI cooling coefficient (default: 6)")
    p.add_argument("--rural-temp", type=float, default=22.0,
                   help="rural reference LST in Celsius (default: 22)")
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
