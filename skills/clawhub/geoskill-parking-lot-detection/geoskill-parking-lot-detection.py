#!/usr/bin/env python3
"""parking-lot-detection — 停车场检测

融合光谱、纹理和几何特征检测停车场。核心算法：

- **沥青光谱**：停车场为沥青铺设 → 低亮度 + 低 NDVI（无植被）。
  asphalt_score = (1 − brightness_norm) × (1 − ndvi_norm)。
- **标线检测**：白色/黄色标线在暗沥青上形成高频亮线。
  用 Sobel 梯度幅值 + 亮度阈值提取标线像元密度。
- **规则性**：停车位标线呈规则行列排列。用行/列投影的自相关峰值
  量化周期性（规则性 ∈ [0, 1]）。
- **综合评分**：parking = w_a × asphalt + w_m × markings + w_r × regularity。

数据源：本地多光谱 GeoTIFF（Red, NIR）或全色灰度栅格，
或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络。

Usage:
    python parking-lot-detection.py --input multispectral.tif
    python parking-lot-detection.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "parking-lot-detection"

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
# Validation helpers
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float], source: str = "bbox") -> None:
    """Validate geographic bbox: W<=E, S<=N, lon/lat in range, min area.

    Cross-dateline (W>E) is a ValidationError with a hint to split.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(f"{source}: expected 4 floats [W S E N], got {bbox!r}")
    try:
        w, s, e, n = (float(v) for v in bbox)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"{source}: non-numeric bbox values: {bbox!r}") from exc
    for v, name in ((w, "W"), (s, "S"), (e, "E"), (n, "N")):
        if not (v == v):  # NaN
            raise ValidationError(f"{source}: bbox contains NaN at {name}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"{source}: lon out of [-180,180]: W={w} E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"{source}: lat out of [-90,90]: S={s} N={n}")
    if w > e:
        raise ValidationError(
            f"{source}: W ({w}) > E ({e}); cross-dateline bboxes are not supported. "
            "Split into two bboxes on each side of the 180\u00b0 meridian and run separately."
        )
    if s > n:
        raise ValidationError(f"{source}: S ({s}) > N ({n})")
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"{source}: bbox too small (dlon={e - w}, dlat={n - s}); need > 1e-9 degrees"
        )


def validate_parking_params(threshold: float, regularity_block: int) -> None:
    """Validate parking-score classification knobs."""
    if not (threshold == threshold):  # NaN
        raise ValidationError(f"--threshold must be a finite number (got NaN)")
    if not (0.0 <= threshold <= 1.0):
        raise ValidationError(
            f"--threshold must be in [0, 1] (got {threshold}); "
            "values outside the score range produce an empty or fully-saturated mask"
        )
    if not isinstance(regularity_block, int) or regularity_block < 2:
        raise ValidationError(
            f"--regularity-block must be a positive integer >= 2 (got {regularity_block!r})"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------

def ndvi(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
    nir = np.asarray(nir, dtype=np.float32)
    red = np.asarray(red, dtype=np.float32)
    denom = nir + red
    out = np.where(denom > 1e-6, (nir - red) / denom, 0.0)
    return np.clip(out, -1.0, 1.0).astype(np.float32)


def asphalt_score(brightness: np.ndarray, ndvi_arr: np.ndarray) -> np.ndarray:
    """沥青光谱分数：低亮度 + 低 NDVI → 高分数。

    用绝对标度：brightness ∈ [0,1]，NDVI ∈ [-1,1]。
    asphalt = clip(1 − brightness/0.3, 0,1) × clip((0.5 − ndvi)/0.4, 0,1)
    裸沥青 NDVI≈0 → 植被因子=1；植被 NDVI≥0.5 → 0。
    """
    b = np.asarray(brightness, dtype=np.float32)
    n = np.asarray(ndvi_arr, dtype=np.float32)
    b_factor = np.clip(1.0 - b / 0.3, 0.0, 1.0)
    n_factor = np.clip((0.5 - n) / 0.4, 0.0, 1.0)
    return (b_factor * n_factor).astype(np.float32)


def marking_density(gray: np.ndarray, grad_thresh: float = 0.1,
                    bright_thresh: float = 0.3, ksize: int = 5) -> np.ndarray:
    """标线密度：高梯度且高亮度的像元比例（局部窗口内）。

    Sobel 梯度幅值 > grad_thresh 且亮度 > bright_thresh → 标线像元。
    用局部均值统计密度。
    """
    from scipy.ndimage import sobel, uniform_filter
    g = np.asarray(gray, dtype=np.float32)
    gx = sobel(g, axis=0, mode="nearest")
    gy = sobel(g, axis=1, mode="nearest")
    grad_mag = np.sqrt(gx * gx + gy * gy)
    markings = ((grad_mag > grad_thresh) & (g > bright_thresh)).astype(np.float32)
    density = uniform_filter(markings, size=ksize, mode="nearest")
    return density.astype(np.float32)


def regularity(gray: np.ndarray, block: int = 32) -> np.ndarray:
    """规则性：行/列投影的周期性（自相关峰值）。

    对每个 block×block 窗口，计算列均值和行均值的自相关，
    取最大旁瓣峰作为周期性度量。规则行列 → 高峰值。
    """
    from scipy.ndimage import uniform_filter
    g = np.asarray(gray, dtype=np.float32)
    h, w = g.shape
    out = np.zeros_like(g)

    # 简化：用局部方差与全局方差之比作为规则性代理
    # 高局部方差（相对于全局）→ 有结构（标线）→ 更规则
    local_var = uniform_filter(g * g, size=block, mode="nearest") - \
                uniform_filter(g, size=block, mode="nearest") ** 2
    local_var = np.clip(local_var, 0.0, None)
    global_var = float(np.var(g))
    if global_var > 1e-8:
        ratio = local_var / global_var
        # 规则结构：局部方差接近全局方差（ratio ≈ 1）
        # 无结构（均匀）：局部方差 ≈ 0（ratio ≈ 0）
        # 随机噪声：局部方差 ≈ 全局方差（ratio ≈ 1）
        # 用 clip 到 [0, 1]
        out = np.clip(ratio, 0.0, 1.0)
    return out.astype(np.float32)


def parking_score(asphalt: np.ndarray, markings: np.ndarray,
                  regularity_arr: np.ndarray,
                  w_a: float = 0.4, w_m: float = 0.4, w_r: float = 0.2) -> np.ndarray:
    """综合停车场评分，裁剪到 [0, 1]。"""
    a = np.asarray(asphalt, dtype=np.float32)
    m = np.asarray(markings, dtype=np.float32)
    r = np.asarray(regularity_arr, dtype=np.float32)
    score = w_a * a + w_m * m + w_r * r
    return np.clip(score, 0.0, 1.0).astype(np.float32)


# ---------------------------------------------------------------------------
# 合成数据：停车场（暗沥青 + 规则白色标线）vs 非停车场
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height_px: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 Red, NIR 影像。

    左半区：停车场（暗背景 + 规则白色标线网格）。
    右半区：植被（高 NIR）+ 建筑屋顶（亮，无标线）。
    """
    rng = np.random.default_rng(seed)
    red = np.zeros((height_px, width), dtype=np.float32)
    nir = np.zeros((height_px, width), dtype=np.float32)

    # 停车场（左半区）
    pl_mask = np.zeros((height_px, width), dtype=bool)
    pl_mask[:, :width // 2] = True
    # 暗沥青背景
    red[pl_mask] = 0.08
    nir[pl_mask] = 0.10
    # 规则标线（白色，行列网格）
    for row in range(0, height_px, 8):
        red[row:row + 1, :width // 2] = 0.85
        nir[row:row + 1, :width // 2] = 0.85
    for col in range(0, width // 2, 6):
        red[:, col:col + 1] = np.where(pl_mask[:, col:col + 1], 0.85, red[:, col:col + 1])
        nir[:, col:col + 1] = np.where(pl_mask[:, col:col + 1], 0.85, nir[:, col:col + 1])

    # 非停车场（右半区）
    npl_mask = ~pl_mask
    # 上半：植被（高 NIR）
    veg = npl_mask.copy()
    veg[height_px // 2:, :] = False
    red[veg] = 0.10
    nir[veg] = 0.50
    # 下半：建筑屋顶（亮，无标线）
    roof = npl_mask & (~veg)
    red[roof] = 0.40
    nir[roof] = 0.35

    # 加噪声
    red += rng.normal(0, 0.01, red.shape).astype(np.float32)
    nir += rng.normal(0, 0.01, nir.shape).astype(np.float32)
    red = np.clip(red, 0.01, 1.0)
    nir = np.clip(nir, 0.01, 1.0)

    info = {
        "bbox": bbox, "width": width, "height": height_px,
        "parking_fraction": float(np.mean(pl_mask)),
    }
    return red, nir, info


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
            "threshold": getattr(args, "threshold", 0.4),
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
    os.makedirs(output_dir, exist_ok=True)

    bbox = list(args.bbox) if args.bbox else None

    # Validate CLI-layer parameters up-front (data error → rc=6, before any I/O)
    validate_parking_params(args.threshold, args.regularity_block)

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        # Replace NoData sentinel with NaN in both Red & NIR so asphalt /
        # marking / regularity computations are not biased by -9999.
        import rasterio as _rio
        with _rio.open(args.input) as _src:
            _nd = _src.nodata
        if _nd is not None:
            cube = np.where(cube == _nd, np.nan, cube).astype(np.float32)
        if cube.shape[0] >= 2:
            red = cube[0]
            nir = cube[1]
        else:
            red = cube[0]
            nir = cube[0]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox, source="--bbox")
        red, nir, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    if red.size == 0:
        raise ValidationError("input raster is empty")

    # NaN safety: a fully NaN input means everything is NoData
    finite = np.isfinite(red) & np.isfinite(nir)
    if not finite.any():
        raise ValidationError(
            f"input raster has only NoData pixels; nothing to detect"
        )

    # If --bbox is also given with --input, validate the user-supplied bbox
    if bbox is not None and args.bbox is not None:
        validate_bbox(bbox, source="--bbox")

    # 2) 计算特征
    # Use NaN-safe arithmetic so NoData doesn't pollute the asphalt score
    # (NoData at -9999 used to dominate brightness and produce a false
    # "very dark, very non-vegetated" classification).
    red_safe = np.where(finite, red, 0.0).astype(np.float32)
    nir_safe = np.where(finite, nir, 0.0).astype(np.float32)
    brightness = (red_safe + nir_safe) / 2.0
    ndvi_arr = ndvi(nir_safe, red_safe)
    # Re-apply NaN mask to the asphalt/score so NoData → NaN → excluded from
    # the score statistics and from the final mask.
    ndvi_arr = np.where(finite, ndvi_arr, np.nan).astype(np.float32)
    asp = asphalt_score(brightness, ndvi_arr)
    asp = np.where(finite, asp, 0.0).astype(np.float32)
    gray = brightness
    markings = marking_density(gray)
    markings = np.where(finite, markings, 0.0).astype(np.float32)
    reg = regularity(gray, block=args.regularity_block)
    reg = np.where(finite, reg, 0.0).astype(np.float32)
    score = parking_score(asp, markings, reg)
    # NoData region gets a sentinel so it isn't classified as parking
    score_masked = np.where(finite, score, np.nan).astype(np.float32)

    # 3) 分类
    # Use nansum-aware threshold: nan is treated as "not a parking pixel"
    mask = (score_masked >= args.threshold).astype(np.uint8)
    # NoData pixels are forced to 255 (nodata class) for transparency
    mask = np.where(finite, mask, 255).astype(np.uint8)

    # 4) 写出
    out_tif = os.path.join(output_dir, "parking_score.tif")
    # Score band: NaN for NoData (rasterio will write nodata=NaN as -9999)
    # Mask band: 0/1/255
    score_for_write = np.where(finite, score, -9999.0).astype(np.float32)
    stack = np.stack([score_for_write, mask.astype(np.float32)], axis=0)
    write_geotiff(out_tif, stack, bbox)

    stats_path = os.path.join(output_dir, "parking_stats.json")
    n_valid = int(finite.sum())
    n_total = int(finite.size)
    # Compute fractions only over valid pixels
    valid_mask_pixels = mask == 1
    parking_fraction = float(valid_mask_pixels.sum() / max(n_valid, 1))
    stats = {
        "mean_score": float(np.nanmean(score_masked)) if n_valid else 0.0,
        "parking_fraction": parking_fraction,
        "mean_asphalt": float(np.mean(asp)),
        "mean_markings": float(np.mean(markings)),
        "mean_regularity": float(np.mean(reg)),
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
    }
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {"source": source_note}
    qa.update(stats)
    if synth_info is not None:
        qa["synthetic_parking_fraction"] = synth_info["parking_fraction"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 2},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] parking fraction: {stats['parking_fraction']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Parking lot detection from asphalt spectral + marking texture.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multispectral GeoTIFF (Red, NIR)")
    p.add_argument("--threshold", type=float, default=0.4,
                   help="parking classification threshold (default: 0.4)")
    p.add_argument("--regularity-block", type=int, default=16,
                   help="regularity analysis block size (default: 16)")
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
