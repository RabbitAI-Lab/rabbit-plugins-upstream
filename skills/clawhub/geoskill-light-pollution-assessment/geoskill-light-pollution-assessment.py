#!/usr/bin/env python3
"""light-pollution-assessment — 光污染评估

基于 VIIRS 夜间灯光辐射值评估光污染等级及其生态影响。

- 光污染等级：将平均辐射值（nW·cm⁻²·sr⁻¹）按阈值分为 0–5 级，
  0 = 原始暗夜，5 = 极端光污染（城市核心区），
- 生态影响指数：对数响应模型 I = log10(1 + k·radiance)，
  反映人造光对夜行生物节律的干扰程度（0–1 归一化），
- 可选输出天空辉光代理（简化：辐射值 × 散射系数）。

数据源：--synthetic 生成城市梯度夜光；--input 读取 VIIRS 年平均辐射栅格。

隐私声明 / Privacy：
- 完全离线运行。

Usage:
    python light-pollution-assessment.py --bbox 116 39 117 40 --synthetic --output-dir ./out
    python light-pollution-assessment.py --input viirs.tif --output-dir ./out

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
SKILL_NAME = "light-pollution-assessment"

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
# 光污染等级阈值（nW·cm⁻²·sr⁻¹，参考 Falchi et al. 2016 光污染分级）
# ---------------------------------------------------------------------------
GRADE_THRESHOLDS = [0.25, 1.0, 4.0, 15.0, 50.0]
GRADE_NAMES = ["pristine", "low", "moderate", "high", "severe", "extreme"]
ECOLOGICAL_K = 0.10  # 生态影响对数模型系数


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------
def validate_bbox(bbox, allow_antimeridian: bool = False):
    """Validate geographic bbox.

    Returns bbox as list[float] on success; raises ValidationError on any issue.
    Cross-180° (W > E) is rejected with a hint unless ``allow_antimeridian``.
    """
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            f"bbox must be 4 floats [W S E N], got {bbox!r}")
    w, s, e, n = (float(x) for x in bbox)
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0
            and -90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox out of range (-180..180 lon, -90..90 lat): [{w}, {s}, {e}, {n}]")
    if w == e or s == n:
        raise ValidationError(
            f"bbox has zero area: W==E ({w}) or S==N ({s}); "
            f"got [{w}, {s}, {e}, {n}]")
    if s > n:
        raise ValidationError(
            f"bbox S>N (south > north): [{w}, {s}, {e}, {n}]")
    if w > e:
        if not allow_antimeridian:
            raise ValidationError(
                f"bbox crosses antimeridian (W>E: {w}>{e}); "
                f"split into two bboxes and merge results manually")
        return [w, s, e, n]
    return [w, s, e, n]


def radiance_to_grade(radiance: np.ndarray) -> np.ndarray:
    """辐射值 → 光污染等级（0-5），阈值见 GRADE_THRESHOLDS。

    NoData (NaN) 像素保持 grade=0（与 ``radiance < GRADE_THRESHOLDS[0]`` 一致），
    由 NoData 掩码通过 ``np.where`` 写回。统计时仅基于有效像素。
    """
    valid = np.isfinite(radiance)
    grade = np.zeros(radiance.shape, dtype=np.int8)
    grade[valid & (radiance >= GRADE_THRESHOLDS[0])] = 1
    grade[valid & (radiance >= GRADE_THRESHOLDS[1])] = 2
    grade[valid & (radiance >= GRADE_THRESHOLDS[2])] = 3
    grade[valid & (radiance >= GRADE_THRESHOLDS[3])] = 4
    grade[valid & (radiance >= GRADE_THRESHOLDS[4])] = 5
    return grade


def ecological_impact_index(radiance: np.ndarray, k: float = ECOLOGICAL_K) -> np.ndarray:
    """生态影响指数 I = log10(1 + k·radiance) / log10(1 + k·Rmax)，归一化 [0, 1]。
    Rmax 参考 200 nW（极端城市）。

    NoData (NaN) 像素 → NaN 输出（写回 -9999 由调用方在保存时处理）。
    """
    rmax = 200.0
    norm = np.log10(1.0 + k * rmax)
    out = np.full(radiance.shape, np.nan, dtype=np.float32)
    valid = np.isfinite(radiance)
    raw = np.log10(1.0 + k * np.clip(radiance[valid], 0.0, None))
    out[valid] = np.clip(raw / norm, 0.0, 1.0).astype(np.float32)
    return out


def skyglow_proxy(radiance: np.ndarray, scatter_coeff: float = 0.05) -> np.ndarray:
    """天空辉光代理（简化）= radiance × scatter_coeff；NoData 像素输出 NaN。"""
    out = np.full(radiance.shape, np.nan, dtype=np.float32)
    valid = np.isfinite(radiance)
    out[valid] = (radiance[valid] * scatter_coeff).astype(np.float32)
    return out


def generate_synthetic_light(bbox: List[float], width: int = 128, height: int = 128,
                             seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    """城市梯度夜光：中心高，向外衰减。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy /= max(height - 1, 1)
    xx /= max(width - 1, 1)
    cx, cy = 0.5, 0.5
    dist = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    radiance = 80.0 * np.exp(-3.0 * dist) + rng.exponential(2.0, (height, width))
    radiance = radiance.astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height}
    return radiance, info


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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], float]:
    """读取 GeoTIFF；NoData 像素替换为 NaN，返回 (cube, bbox, nodata_or_None)。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=False).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    # Sentinel-based NoData → NaN
    if nodata is not None and np.isfinite(float(nodata)):
        nd = float(nodata)
        cube = np.where(cube == nd, np.nan, cube).astype(np.float32)
    return cube, bbox, nodata


def read_nodata(path: str) -> Optional[float]:
    """Read only the NoData value (or None if not set)."""
    import rasterio
    if not os.path.exists(path):
        return None
    with rasterio.open(path) as src:
        return src.nodata


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
    input_nodata: Optional[float] = None

    # ---- Validate bbox early (synthetic path) ----
    if bbox is not None:
        bbox = validate_bbox(bbox)

    # ---- Load data first (validate input) ----
    if args.input and not args.synthetic:
        cube, file_bbox, input_nodata = read_geotiff(args.input)
        if bbox is None:
            bbox = validate_bbox(file_bbox)
        else:
            bbox = validate_bbox(bbox)
        if cube.size == 0 or cube.shape[0] == 0:
            raise ValidationError(f"input raster is empty: {args.input}")
        radiance = cube[0]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        radiance, _ = generate_synthetic_light(bbox)
        source_note = "synthetic"

    # ---- NoData check on real input ----
    n_valid = int(np.sum(np.isfinite(radiance)))
    n_total = int(radiance.size)
    if n_valid == 0:
        # Cleanup partial output_dir is unnecessary (we haven't created it yet)
        raise ValidationError(
            f"input has no valid pixels (n_total={n_total}, n_valid=0); "
            f"refusing to produce a meaningless grade/eco raster"
        )

    # ---- Now safe to create output directory ----
    os.makedirs(output_dir, exist_ok=True)

    grade = radiance_to_grade(radiance)
    eco_index = ecological_impact_index(radiance)
    skyglow = skyglow_proxy(radiance)

    grade_path = os.path.join(output_dir, "light_pollution_grade.tif")
    eco_path = os.path.join(output_dir, "ecological_impact.tif")
    sky_path = os.path.join(output_dir, "skyglow_proxy.tif")
    # Write with NaN -> -9999 sentinel so downstream tools can recognize NoData
    write_geotiff(grade_path, grade.astype(np.float32), bbox, nodata=-9999.0)
    write_geotiff(eco_path, np.where(np.isfinite(eco_index), eco_index, -9999.0).astype(np.float32), bbox, nodata=-9999.0)
    write_geotiff(sky_path, np.where(np.isfinite(skyglow), skyglow, -9999.0).astype(np.float32), bbox, nodata=-9999.0)

    # Grade counts: only valid pixels count; NoData is implicit grade=0 in our scheme
    grade_counts = {GRADE_NAMES[i]: int(np.sum(grade[1] == i)) if False else int(np.sum(grade == i)) for i in range(6)}
    # Reduce spurious double-write: keep only valid-pixel stats for the eco / radiance / skyglow means
    valid_radiance = radiance[np.isfinite(radiance)]
    params = {
        "grade_thresholds": GRADE_THRESHOLDS,
        "grade_names": GRADE_NAMES,
        "grade_pixel_counts": grade_counts,
        "mean_radiance": float(valid_radiance.mean()) if valid_radiance.size else float("nan"),
        "max_radiance": float(valid_radiance.max()) if valid_radiance.size else float("nan"),
        "mean_ecological_impact": float(np.nanmean(eco_index)) if np.any(np.isfinite(eco_index)) else float("nan"),
        "mean_skyglow": float(np.nanmean(skyglow)) if np.any(np.isfinite(skyglow)) else float("nan"),
    }
    params_path = os.path.join(output_dir, "light_pollution_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": grade_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": eco_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": sky_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    qa: Dict[str, Any] = {
        "source": source_note,
        "mean_radiance": params["mean_radiance"],
        "max_radiance": params["max_radiance"],
        "mean_ecological_impact": params["mean_ecological_impact"],
        "mean_skyglow": params["mean_skyglow"],
        "grade_pixel_counts": grade_counts,
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
        "input_nodata": input_nodata,
    }
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean radiance: {qa['mean_radiance']:.2f} nW·cm⁻²·sr⁻¹")
        print(f"[{SKILL_NAME}] mean eco-impact: {qa['mean_ecological_impact']:.3f}")
        print(f"[{SKILL_NAME}] grade counts: {grade_counts}")
        print(f"[{SKILL_NAME}] valid pixels: {n_valid}/{n_total}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Light pollution assessment from VIIRS night-time lights.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input VIIRS radiance GeoTIFF")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic nightlight (offline)")
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
