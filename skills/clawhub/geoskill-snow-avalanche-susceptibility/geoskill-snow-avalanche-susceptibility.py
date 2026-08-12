#!/usr/bin/env python3
"""snow-avalanche-susceptibility — 雪崩易发性评估

融合地形与积雪/气象因子评估雪崩易发性：

- **坡度**：雪崩集中发生在 30–45°（峰值 ~38°），用高斯型坡度因子刻画
- **坡向**：北半球背风(偏北)坡积雪更厚、更易发
- **地形粗糙度**：光滑坡面更易滑动
- **积雪深度**：越厚越易发（饱和递增）
- **温度**：接近 0°C 的湿雪层最不稳定

各因子归一到 [0,1] 后加权求和得易发性指数（[0,1]），再分级。

数据源：本地多波段 GeoTIFF（band1=坡度°、band2=坡向°、band3=雪深m、band4=温度°C），
或 ``--synthetic`` 生成山地场景。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python snow-avalanche-susceptibility.py --input terrain.tif
    python snow-avalanche-susceptibility.py --bbox 90 30 91 31 --synthetic --output-dir ./out

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
SKILL_NAME = "snow-avalanche-susceptibility"

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


def validate_roughness(value: float) -> float:
    """Validate --roughness in [0,1]; return float."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        raise ValidationError(f"roughness must be a number, got {value!r}")
    if not (0.0 <= v <= 1.0):
        raise ValidationError(f"roughness must be in [0,1], got {v}")
    return v


# ---------------------------------------------------------------------------
# 核心算法：各因子（均输出 [0,1]）
# ---------------------------------------------------------------------------
def slope_factor(slope_deg: np.ndarray, peak: float = 38.0, width: float = 12.0) -> np.ndarray:
    """坡度因子：高斯型，峰值 ~38°（30–45° 高发），过缓或过陡都降低。"""
    s = np.asarray(slope_deg, dtype=np.float64)
    return np.exp(-((s - peak) / width) ** 2).astype(np.float32)


def aspect_factor(aspect_deg: np.ndarray) -> np.ndarray:
    """坡向因子：北半球偏北(背风)坡更高。aspect 自北顺时针，北=1、南=0。"""
    a = np.deg2rad(np.asarray(aspect_deg, dtype=np.float64))
    return (0.5 + 0.5 * np.cos(a)).astype(np.float32)


def roughness_factor(roughness: np.ndarray) -> np.ndarray:
    """粗糙度因子：越光滑(roughness→0)越易发。roughness 假定已在 [0,1]。"""
    r = np.clip(np.asarray(roughness, dtype=np.float64), 0.0, 1.0)
    return (1.0 - r).astype(np.float32)


def snow_factor(depth_m: np.ndarray, scale: float = 1.0) -> np.ndarray:
    """积雪因子：随雪深饱和递增（1 - exp(-d/scale)）。"""
    d = np.clip(np.asarray(depth_m, dtype=np.float64), 0.0, None)
    return (1.0 - np.exp(-d / float(scale))).astype(np.float32)


def temperature_factor(temp_c: np.ndarray, center: float = 0.0, width: float = 8.0) -> np.ndarray:
    """温度因子：接近 0°C 的湿雪最不稳定（高斯峰值在 center）。"""
    t = np.asarray(temp_c, dtype=np.float64)
    return np.exp(-((t - center) / width) ** 2).astype(np.float32)


def susceptibility_from_factors(slope_f: np.ndarray, aspect_f: np.ndarray, roughness_f: np.ndarray,
                                snow_f: np.ndarray, temp_f: np.ndarray,
                                weights: Tuple[float, ...] = (0.30, 0.15, 0.10, 0.30, 0.15)) -> np.ndarray:
    """对五个 [0,1] 因子加权求和 → 易发性指数 [0,1]。对每个因子单调不减。"""
    w = np.asarray(weights, dtype=np.float64)
    if np.any(w < 0) or w.sum() <= 1e-12:
        raise ValidationError("weights must be non-negative with positive sum")
    parts = [np.clip(np.asarray(x, dtype=np.float64), 0, 1) for x in
             (slope_f, aspect_f, roughness_f, snow_f, temp_f)]
    acc = sum(float(w[i]) * parts[i] for i in range(5))
    return np.clip(acc / w.sum(), 0.0, 1.0).astype(np.float32)


def avalanche_susceptibility(slope_deg: np.ndarray, aspect_deg: np.ndarray, roughness: np.ndarray,
                             snow_depth: np.ndarray, temperature: np.ndarray,
                             weights: Tuple[float, ...] = (0.30, 0.15, 0.10, 0.30, 0.15)) -> np.ndarray:
    """从物理输入计算雪崩易发性指数（[0,1]）。"""
    if not (slope_deg.shape == aspect_deg.shape == roughness.shape == snow_depth.shape == temperature.shape):
        raise ValidationError("input layer shape mismatch")
    return susceptibility_from_factors(
        slope_factor(slope_deg), aspect_factor(aspect_deg), roughness_factor(roughness),
        snow_factor(snow_depth), temperature_factor(temperature), weights,
    )


def classify_susceptibility(s: np.ndarray, breaks: Tuple[float, ...] = (0.25, 0.5, 0.75)) -> np.ndarray:
    """易发性分级：0=low,1=moderate,2=high,3=very_high。"""
    return np.digitize(np.asarray(s, dtype=np.float64), list(breaks)).astype(np.int16)


# ---------------------------------------------------------------------------
# 合成数据：山地地形 + 积雪 + 温度
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64,
                       seed: int = 42) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float64) / max(width - 1, 1)
    yn = yy.astype(np.float64) / max(height - 1, 1)
    # 坡度：中部陡(~40°)，两侧缓
    slope = 40.0 * np.exp(-((xn - 0.5) ** 2) / (2 * 0.2 ** 2)) + 5.0
    slope = np.clip(slope + rng.normal(0, 2, slope.shape), 0, 60)
    # 坡向：偏北为主
    aspect = np.clip(360.0 * yn + rng.normal(0, 20, slope.shape), 0, 360)
    # 粗糙度
    roughness = np.clip(0.3 + 0.4 * xn + rng.normal(0, 0.05, slope.shape), 0, 1)
    # 雪深：高程/北坡更厚
    snow = np.clip(2.0 * (1 - xn) + 1.5 * slope / 40.0 + rng.normal(0, 0.1, slope.shape), 0, 5)
    # 温度：随“高程”(坡度代理)递减
    temp = -2.0 - 8.0 * (slope / 60.0) + rng.normal(0, 0.5, slope.shape)
    layers = {"slope": slope.astype(np.float32), "aspect": aspect.astype(np.float32),
              "roughness": roughness.astype(np.float32), "snow_depth": snow.astype(np.float32),
              "temperature": temp.astype(np.float32)}
    info = {"bbox": bbox, "width": width, "height": height, "max_slope": float(slope.max())}
    return layers, info


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
    bbox = list(args.bbox) if args.bbox else None

    # --- Upfront validation (BEFORE makedirs; rc=6 for bad data, rc=2 for bad CLI) ---
    if args.bbox is not None:
        validate_bbox(args.bbox)
    # Validate roughness regardless of mode so the rc=6 path is testable without --input
    validate_roughness(args.roughness)

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            validate_bbox(bbox)
        if cube.shape[0] < 4:
            raise ValidationError("input needs >=4 bands (slope, aspect, snow_depth, temperature)")
        slope, aspect, snow, temp = cube[0], cube[1], cube[2], cube[3]
        # NoData -> NaN: any of slope/aspect/snow/temp that have -9999 should be NaN
        slope = np.where(np.isfinite(slope), slope, np.nan).astype(np.float32)
        aspect = np.where(np.isfinite(aspect), aspect, np.nan).astype(np.float32)
        snow = np.where(np.isfinite(snow), snow, np.nan).astype(np.float32)
        temp = np.where(np.isfinite(temp), temp, np.nan).astype(np.float32)
        roughness = np.full(slope.shape, float(args.roughness), dtype=np.float32)
        # Check if all input is NoData -> exit 6
        total_pix = int(slope.size)
        n_valid = int(np.count_nonzero(
            np.isfinite(slope) & np.isfinite(aspect) & np.isfinite(snow) & np.isfinite(temp)
        ))
        if n_valid == 0:
            raise ValidationError("input raster has no valid pixels (all NoData)")
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        layers, _info = generate_synthetic(bbox)
        slope, aspect, snow, temp = layers["slope"], layers["aspect"], layers["snow_depth"], layers["temperature"]
        roughness = layers["roughness"]
        total_pix = int(slope.size)
        n_valid = total_pix
        source_note = "synthetic"

    sus = avalanche_susceptibility(slope, aspect, roughness, snow, temp)
    level = classify_susceptibility(sus)

    # --- Output dir (only after all upfront validation passes) ---
    os.makedirs(output_dir, exist_ok=True)

    sus_tif = os.path.join(output_dir, "susceptibility.tif")
    write_geotiff(sus_tif, sus, bbox)
    lvl_tif = os.path.join(output_dir, "susceptibility_level.tif")
    write_geotiff(lvl_tif, level.astype("int16"), bbox, nodata=-1, dtype="int16")

    params = {"source": source_note, "weights": [0.30, 0.15, 0.10, 0.30, 0.15]}
    params_path = os.path.join(output_dir, "avalanche_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    # NaN-safe statistics
    sus_valid = sus[np.isfinite(sus)]
    n_valid_sus = int(sus_valid.size)
    if n_valid_sus == 0:
        mean_s, max_s = 0.0, 0.0
    else:
        mean_s = float(sus_valid.mean())
        max_s = float(sus_valid.max())
    qa: Dict[str, Any] = {
        "source": source_note,
        "input_nodata": -9999.0,
        "n_valid_pixels": n_valid,
        "n_total_pixels": total_pix,
        "mean_susceptibility": mean_s,
        "max_susceptibility": max_s,
        "very_high_fraction": float(np.mean(level == 3)),
        "high_plus_fraction": float(np.mean(level >= 2)),
    }
    outputs = [
        {"path": sus_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": lvl_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, {"input": args.input, "bbox": bbox, "synthetic": bool(args.synthetic)},
                              outputs, qa, started_at, 0)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean susceptibility: {qa['mean_susceptibility']:.4f}  max: {qa['max_susceptibility']:.4f}")
        print(f"[{SKILL_NAME}] high+ fraction: {qa['high_plus_fraction']:.3f}")
        print(f"[{SKILL_NAME}] outputs: {output_dir}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Snow avalanche susceptibility (slope/aspect/roughness + snow + temperature).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoTIFF (band1=slope deg, band2=aspect deg, band3=snow depth m, band4=temp C)")
    p.add_argument("--roughness", type=float, default=0.3, help="terrain roughness 0-1 for real-input mode (default: 0.3)")
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
