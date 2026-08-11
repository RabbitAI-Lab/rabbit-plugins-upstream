#!/usr/bin/env python3
"""informal-settlement-detection — 非正规聚居区检测

融合纹理不规则性、建筑形态和光谱混合来检测非正规聚居区（城中村/棚户区）。
核心算法：

- **纹理不规则性**：用局部标准差（灰度共生矩阵的简化替代）量化空间无序程度。
  非正规聚居区通常纹理混乱、对比度高、无规则几何。
- **建筑密度**：高密度是必要条件（非正规聚居区往往建筑拥挤）。
- **光谱混合分类**：利用 NDVI（低植被）和亮度（低反射率）辅助分类。
- **综合评分**：加权融合 → 阈值分割 → 非正规 vs 正规。

数据源：本地多光谱 GeoTIFF（至少 Red, NIR）+ 建筑足迹栅格，
或使用 ``--synthetic`` 生成物理一致的模拟场景用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python informal-settlement-detection.py --input multispectral.tif --footprints fp.tif
    python informal-settlement-detection.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "informal-settlement-detection"

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
# Input validation (P0/P1)
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate a [W, S, E, N] bbox. Raises ValidationError on bad order, range,
    zero-area, or crossing the 180° meridian.
    """
    try:
        w, s, e, n = [float(v) for v in bbox]
    except Exception:
        raise ValidationError(f"bbox must be 4 floats, got {bbox!r}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"longitude out of range [-180, 180]: W={w}, E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"latitude out of range [-90, 90]: S={s}, N={n}")
    if w >= e:
        raise ValidationError(
            f"bbox requires W < E (got W={w}, E={e}); check --bbox order")
    if s >= n:
        raise ValidationError(
            f"bbox requires S < N (got S={s}, N={n}); check --bbox order")
    if e - w > 360.0 or n - s > 180.0:
        raise ValidationError(
            f"bbox span too large (dx={e - w}, dy={n - s})")
    if w > 180.0 or e > 180.0 or w < -180.0 or e < -180.0:
        raise ValidationError(
            f"bbox crosses 180° meridian; please split into two sub-bboxes")


def validate_cli_params(threshold: float, kernel_size: int) -> None:
    """Validate CLI parameter ranges. Raises ValidationError on bad input."""
    if not (0.0 <= float(threshold) <= 1.0):
        raise ValidationError(
            f"--threshold must be in [0, 1], got {threshold}")
    if int(kernel_size) < 1:
        raise ValidationError(
            f"--kernel-size must be >= 1, got {kernel_size}")
    if int(kernel_size) % 2 == 0:
        # scipy.ndimage.uniform_filter requires odd size for symmetric behavior
        # — many skills auto-bump; here we strictly reject to keep semantics clear.
        raise ValidationError(
            f"--kernel-size must be odd, got {kernel_size}")


def read_geotiff_with_nodata(path: str):
    """Read a multiband raster and return (data, bbox, nodata).

    Values equal to the source nodata (if any) are replaced with NaN.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [float(b.left), float(b.bottom), float(b.right), float(b.top)]
        nd = src.nodata
    if nd is not None:
        cube = np.where(cube == nd, np.nan, cube)
    return cube, bbox, nd


def count_valid_pixels(cube: np.ndarray) -> int:
    """Number of locations where ALL bands are finite (i.e. not NaN/inf)."""
    if cube.ndim == 3:
        valid_loc = np.all(np.isfinite(cube), axis=0)
    else:
        valid_loc = np.isfinite(cube)
    return int(valid_loc.sum())


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------

def local_std(gray: np.ndarray, size: int = 5) -> np.ndarray:
    """局部标准差（纹理不规则性代理）。用 nearest 边界避免边缘虚假方差。

    NaN-aware: NaN/inf 输入像元在窗口求和时按 0 处理，未被 finite 掩码覆盖的
    像元在方差归一化时也按 0 处理（避免污染）。输出对原始 NaN 像元仍为 NaN。
    """
    from scipy.ndimage import uniform_filter
    g = np.asarray(gray, dtype=np.float32)
    finite = np.isfinite(g).astype(np.float32)
    g_safe = np.where(np.isfinite(g), g, 0.0).astype(np.float32)
    sum_w = uniform_filter(finite, size=size, mode="nearest")
    sum_g = uniform_filter(g_safe, size=size, mode="nearest")
    sum_g2 = uniform_filter(g_safe * g_safe, size=size, mode="nearest")
    safe = sum_w > 0
    mean = np.divide(sum_g, sum_w, out=np.zeros_like(sum_g), where=safe)
    mean2 = np.divide(sum_g2, sum_w, out=np.zeros_like(sum_g2), where=safe)
    var = np.maximum(mean2 - mean * mean, 0.0)
    out = np.sqrt(var).astype(np.float32)
    # Mark original NaN locations as NaN in the output.
    out = np.where(np.isfinite(g), out, np.nan)
    return out


def ndvi(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
    nir = np.asarray(nir, dtype=np.float32)
    red = np.asarray(red, dtype=np.float32)
    denom = nir + red
    out = np.where(denom > 1e-6, (nir - red) / denom, 0.0)
    return np.clip(out, -1.0, 1.0).astype(np.float32)


def informal_score(
    texture: np.ndarray,
    density: np.ndarray,
    ndvi_arr: np.ndarray,
    w_tex: float = 0.5,
    w_den: float = 0.3,
    w_ndvi: float = 0.2,
    tex_scale: float = 0.3,
    ndvi_high: float = 0.3,
    ndvi_low: float = -0.1,
) -> np.ndarray:
    """综合评分（绝对物理标度）：高纹理 + 高密度 + 低 NDVI → 高非正规概率。

    - texture_norm = clip(texture / tex_scale, 0, 1)   粗糙度相对参考上限
    - density 已在 [0, 1]
    - bareness = clip((ndvi_high - ndvi) / (ndvi_high - ndvi_low), 0, 1)
      低植被 → 高 bareness

    Score = w_tex * texture_norm + w_den * density + w_ndvi * bareness，裁剪到 [0, 1]。
    """
    tex = np.asarray(texture, dtype=np.float32)
    den = np.asarray(density, dtype=np.float32)
    ndvi_a = np.asarray(ndvi_arr, dtype=np.float32)

    texture_norm = np.clip(tex / max(tex_scale, 1e-6), 0.0, 1.0)
    den_norm = np.clip(den, 0.0, 1.0)
    span = max(ndvi_high - ndvi_low, 1e-6)
    bareness = np.clip((ndvi_high - ndvi_a) / span, 0.0, 1.0)

    score = w_tex * texture_norm + w_den * den_norm + w_ndvi * bareness
    return np.clip(score, 0.0, 1.0).astype(np.float32)


def classify_informal(score: np.ndarray, threshold: float = 0.5) -> np.ndarray:
    return (score >= threshold).astype(np.uint8)


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height_px: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成模拟多光谱影像（Red, NIR）+ 建筑足迹。

    模拟两种城区：
    - 左半区：非正规聚居区（高噪声纹理、高密度、低 NDVI）
    - 右半区：正规城区（平滑纹理、中密度、中 NDVI）
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height_px, 0:width]

    # Red band: informal (bright, noisy), formal (darker, smooth)
    red = np.zeros((height_px, width), dtype=np.float32)
    nir = np.zeros((height_px, width), dtype=np.float32)
    fp = np.zeros((height_px, width), dtype=np.float32)

    # Informal half (left): high brightness noise, low NIR
    mask_inf = xx < width // 2
    red[mask_inf] = rng.uniform(0.15, 0.35, mask_inf.sum()).astype(np.float32)
    red[mask_inf] += rng.normal(0, 0.05, mask_inf.sum()).astype(np.float32)
    nir[mask_inf] = rng.uniform(0.10, 0.20, mask_inf.sum()).astype(np.float32)
    fp[mask_inf] = (rng.random(mask_inf.sum()) > 0.3).astype(np.float32)

    # Formal half (right): smoother, higher NIR (vegetation)
    mask_formal = ~mask_inf
    red[mask_formal] = rng.uniform(0.08, 0.15, mask_formal.sum()).astype(np.float32)
    nir[mask_formal] = rng.uniform(0.25, 0.45, mask_formal.sum()).astype(np.float32)
    fp[mask_formal] = (rng.random(mask_formal.sum()) > 0.6).astype(np.float32)

    red = np.clip(red, 0.01, 1.0)
    nir = np.clip(nir, 0.01, 1.0)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height_px,
        "informal_fraction": float(np.mean(mask_inf)),
    }
    return red, nir, fp, info


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
            "footprints": getattr(args, "footprints", None),
            "threshold": getattr(args, "threshold", 0.5),
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

    # 1) 获取数据
    synth_info: Optional[Dict[str, Any]] = None
    src_nd = None
    if args.input and not args.synthetic:
        cube, file_bbox, _src_nd = read_geotiff_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if cube.shape[0] < 2:
            raise ValidationError("input must have at least 2 bands (Red, NIR)")
        red = cube[0]
        nir = cube[1]
        if args.footprints:
            fp_cube, _, _ = read_geotiff_with_nodata(args.footprints)
            fp = fp_cube[0]
        else:
            fp = np.ones_like(red) * 0.5
        source_note = args.input
        src_nd = _src_nd
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        red, nir, fp, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    # Parameter validation (BEFORE side-effect makedirs).
    if bbox is not None:
        validate_bbox(bbox)
    validate_cli_params(args.threshold, args.kernel_size)

    if red.size == 0:
        raise ValidationError("input raster is empty")

    # 2) 计算纹理、NDVI、密度
    gray = (red + nir) / 2.0
    texture = local_std(gray, size=args.kernel_size)
    ndvi_arr = ndvi(nir, red)
    from scipy.ndimage import uniform_filter
    density = uniform_filter(fp, size=args.kernel_size, mode="constant")
    density = np.clip(density, 0.0, 1.0)

    # 3) 综合评分 + 分类
    score = informal_score(texture, density, ndvi_arr)
    mask = classify_informal(score, threshold=args.threshold)

    # Check NoData propagation — at least one valid pixel must remain.
    n_valid = count_valid_pixels(np.stack([score, mask.astype(np.float32)], axis=0))
    if n_valid == 0:
        raise ValidationError(
            "input has no valid pixels (all NoData / NaN); nothing to score")

    # 4) Side effects begin only after all validation passes.
    os.makedirs(output_dir, exist_ok=True)

    out_tif = os.path.join(output_dir, "informal_score.tif")
    # NaN locations → -9999 (nodata) in the raster
    score_to_write = np.where(np.isfinite(score), score, -9999.0)
    mask_to_write = np.where(np.isfinite(score), mask, 255).astype(np.float32)
    stack = np.stack([score_to_write, mask_to_write], axis=0)
    write_geotiff(out_tif, stack, bbox)

    stats_path = os.path.join(output_dir, "informal_stats.json")
    finite_score = np.isfinite(score)
    stats = {
        "mean_score": float(np.nanmean(score)) if finite_score.any() else 0.0,
        "informal_fraction": (
            float(np.mean(mask[finite_score])) if finite_score.any() else 0.0
        ),
        "threshold": args.threshold,
    }
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    n_total = int(score.size)
    qa: Dict[str, Any] = {
        "source": source_note,
        "n_valid_pixels": int(finite_score.sum()),
        "n_total_pixels": n_total,
        "input_nodata": src_nd,
        "mean_score": stats["mean_score"],
        "informal_fraction": stats["informal_fraction"],
    }
    if synth_info is not None:
        qa["synthetic_informal_fraction"] = synth_info["informal_fraction"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 2},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] informal fraction: {stats['informal_fraction']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Informal settlement detection from texture, density and spectral mixing.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multispectral GeoTIFF (Red, NIR bands)")
    p.add_argument("--footprints", help="building footprint GeoTIFF (binary 0/1)")
    p.add_argument("--threshold", type=float, default=0.5,
                   help="classification threshold (default: 0.5)")
    p.add_argument("--kernel-size", type=int, default=5,
                   help="texture kernel size (default: 5)")
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
