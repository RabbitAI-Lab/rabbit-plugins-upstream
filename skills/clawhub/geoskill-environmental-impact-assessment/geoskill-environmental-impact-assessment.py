#!/usr/bin/env python3
"""environmental-impact-assessment — 环境影响评价

多因子叠加 + 影响预测 + 累积效应 → 影响等级。

- 单因子影响：每个压力因子（污染/土地利用变化/噪声等）归一化到 [0, 1]，
  乘以敏感度权重，
- 加权叠加：综合影响指数 I = Σ(wi × fi) / Σwi，
- 累积效应：多项目叠加 C = 1 - Π(1 - Ii)（独立概率叠加，避免简单相加溢出），
- 影响等级：按阈值分为可忽略/轻微/中等/显著/严重 5 级。

数据源：--synthetic 生成多压力因子栅格；--input 读取多波段压力栅格。

隐私声明 / Privacy：
- 完全离线运行。

Usage:
    python environmental-impact-assessment.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "environmental-impact-assessment"

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
# 校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate geographic bbox. raise ValidationError on any structural issue."""
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            "bbox must be 4 floats [W, S, E, N]", bbox=str(bbox))
    w, s, e, n = [float(v) for v in bbox]
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError("bbox has non-finite values", bbox=bbox)
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0
            and -90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            "bbox out of WGS84 range (lon∈[-180,180], lat∈[-90,90])",
            bbox=bbox)
    if w >= e:
        raise ValidationError(
            f"bbox west ({w}) must be < east ({e}); "
            "this skill does not support anti-meridian crossing — split into two calls",
            bbox=bbox)
    if s >= n:
        raise ValidationError(
            f"bbox south ({s}) must be < north ({n})", bbox=bbox)
    span_lon = e - w
    span_lat = n - s
    if span_lon < 1e-5 or span_lat < 1e-5:
        raise ValidationError(
            f"bbox too small (lon span={span_lon:.7f}, lat span={span_lat:.7f}); "
            "both dimensions must be > 1e-5°", bbox=bbox)


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
DEFAULT_WEIGHTS = [0.30, 0.25, 0.25, 0.20]  # 4 个压力因子的敏感度权重
FACTOR_NAMES = ["pollution", "land_change", "noise", "fragmentation"]
GRADE_THRESHOLDS = [0.1, 0.3, 0.5, 0.7]
GRADE_NAMES = ["negligible", "minor", "moderate", "significant", "severe"]


def normalize_factor(arr: np.ndarray) -> np.ndarray:
    """压力因子 min-max 归一化到 [0, 1]；恒值返回 0。"""
    a = arr.astype(np.float64)
    finite = a[np.isfinite(a)]
    if finite.size == 0:
        return np.zeros_like(a, dtype=np.float32)
    lo, hi = float(np.min(finite)), float(np.max(finite))
    if hi - lo < 1e-9:
        return np.zeros_like(a, dtype=np.float32)
    return np.clip((a - lo) / (hi - lo), 0.0, 1.0).astype(np.float32)


def weighted_overlay(factors: np.ndarray, weights: List[float]) -> np.ndarray:
    """加权叠加：I = Σ(wi × fi) / Σwi。factors shape=(n_factors, H, W)。"""
    n = factors.shape[0]
    w = np.asarray(weights[:n], dtype=np.float64)
    if w.sum() <= 0:
        raise UsageError("weights must sum to a positive value", weights=list(weights))
    return (np.tensordot(w, factors, axes=(0, 0)) / w.sum()).astype(np.float32)


def cumulative_impact(impacts: np.ndarray) -> np.ndarray:
    """累积效应：C = 1 - Π(1 - Ii)，独立概率叠加。impacts shape=(n_projects, H, W)。"""
    clipped = np.clip(impacts, 0.0, 1.0)
    survival = np.prod(1.0 - clipped, axis=0)
    return (1.0 - survival).astype(np.float32)


def impact_grade(index: np.ndarray) -> np.ndarray:
    """综合影响指数 → 等级（0-4），阈值见 GRADE_THRESHOLDS。"""
    grade = np.zeros(index.shape, dtype=np.int8)
    grade[index >= GRADE_THRESHOLDS[0]] = 1
    grade[index >= GRADE_THRESHOLDS[1]] = 2
    grade[index >= GRADE_THRESHOLDS[2]] = 3
    grade[index >= GRADE_THRESHOLDS[3]] = 4
    return grade


def generate_synthetic_eia(bbox: List[float], width: int = 128, height: int = 128,
                           seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (4, H, W) 压力因子栈：城市梯度 + 工业点源 + 交通走廊 + 破碎化斑块。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy /= max(height - 1, 1)
    xx /= max(width - 1, 1)

    pollution = 60.0 * np.exp(-4.0 * ((xx - 0.6) ** 2 + (yy - 0.4) ** 2)) \
        + rng.normal(0, 3, (height, width))
    land_change = 0.5 * xx + 0.3 * yy + rng.normal(0, 0.05, (height, width))
    noise = 50.0 * np.exp(-np.abs(yy - 0.5) / 0.1) + rng.normal(0, 3, (height, width))
    fragmentation = (rng.random((height, width)) < (0.3 * (1.0 - xx))).astype(np.float32)

    factors = np.stack([
        np.clip(pollution, 0, None),
        np.clip(land_change, 0, 1),
        np.clip(noise, 0, None),
        fragmentation,
    ], axis=0).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height, "factors": FACTOR_NAMES}
    return factors, info


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
    """Read GeoTIFF → (cube, bbox). NoData == profile.nodata 保留原值。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_with_nodata(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """Read GeoTIFF → (cube, bbox, nodata_or_None)。NoData → NaN。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=False).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None and np.isfinite(nodata):
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
    if bbox is not None:
        validate_bbox(bbox)

    src_nodata = None
    if args.input and not args.synthetic:
        factors, file_bbox, src_nodata = read_geotiff_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        validate_bbox(bbox)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        factors, _ = generate_synthetic_eia(bbox)
        source_note = "synthetic"

    if factors.size == 0:
        raise ValidationError("input raster is empty")

    # ---- NoData / 全无效校验 ----
    # 各因子的"valid 像元"按所有波段的交集计算；任一因子在该像元为 NaN 即视为缺测
    valid_mask = np.all(np.isfinite(factors), axis=0)
    n_valid = int(valid_mask.sum())
    n_total = int(factors.shape[1] * factors.shape[2])
    if n_valid == 0:
        raise ValidationError(
            "input has no finite (non-NoData) pixels across all factor bands; "
            "cannot compute impact index over an empty domain",
            n_total_pixels=n_total, input_nodata=src_nodata)
    # 把 NoData 像元置 0（参与 min-max 归一化时被自动排除 → 不影响 valid 像素的结果）
    factors = np.where(np.isfinite(factors), factors, 0.0)

    # ---- 通过校验后再创建输出目录 ----
    os.makedirs(output_dir, exist_ok=True)

    # 逐因子归一化 → 加权叠加
    norm = np.stack([normalize_factor(factors[i]) for i in range(factors.shape[0])], axis=0)
    impact_index = weighted_overlay(norm, DEFAULT_WEIGHTS)

    # 累积效应：把 4 个因子视为 4 个独立影响源叠加
    cumulative = cumulative_impact(norm)
    final_index = np.clip(0.5 * impact_index + 0.5 * cumulative, 0.0, 1.0).astype(np.float32)
    # NoData 像元在输出中显式置 0（与 nodata=-9999 区分需另开 NoData 通道；本 skill
    # 维持单波段 float32 输出，NaN 已被 0 填充，故用 grade=0 标记）
    final_index[~valid_mask] = 0.0
    grade = impact_grade(final_index)
    grade[~valid_mask] = 0

    index_path = os.path.join(output_dir, "impact_index.tif")
    grade_path = os.path.join(output_dir, "impact_grade.tif")
    write_geotiff(index_path, final_index, bbox)
    write_geotiff(grade_path, grade.astype(np.float32), bbox)

    # 仅在 valid 像素上统计
    if n_valid > 0:
        grade_counts = {GRADE_NAMES[i]: int(np.sum(grade[valid_mask] == i)) for i in range(5)}
        mean_impact = float(np.mean(final_index[valid_mask]))
        max_impact = float(np.max(final_index[valid_mask]))
        mean_cum = float(np.mean(cumulative[valid_mask]))
    else:
        grade_counts = {n: 0 for n in GRADE_NAMES}
        mean_impact = 0.0
        max_impact = 0.0
        mean_cum = 0.0

    params = {
        "weights": dict(zip(FACTOR_NAMES, DEFAULT_WEIGHTS)),
        "grade_thresholds": GRADE_THRESHOLDS,
        "grade_names": GRADE_NAMES,
        "mean_impact_index": mean_impact,
        "max_impact_index": max_impact,
        "mean_cumulative": mean_cum,
        "grade_pixel_counts": grade_counts,
    }
    params_path = os.path.join(output_dir, "eia_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": index_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1, "nodata": -9999.0},
        {"path": grade_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1, "nodata": -9999.0},
        {"path": params_path, "kind": "json"},
    ]
    qa: Dict[str, Any] = {
        "source": source_note,
        "mean_impact_index": mean_impact,
        "max_impact_index": max_impact,
        "grade_pixel_counts": grade_counts,
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
        "valid_pixel_ratio": float(n_valid / n_total) if n_total else 0.0,
        "input_nodata": src_nodata,
    }
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean impact: {qa['mean_impact_index']:.3f}  max: {qa['max_impact_index']:.3f}")
        print(f"[{SKILL_NAME}] valid pixels: {n_valid}/{n_total} "
              f"({qa['valid_pixel_ratio']:.2%})")
        print(f"[{SKILL_NAME}] grade counts: {grade_counts}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Environmental impact assessment via multi-factor overlay and cumulative effects.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multi-band GeoTIFF (each band = pressure factor)")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic pressure stack (offline)")
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
