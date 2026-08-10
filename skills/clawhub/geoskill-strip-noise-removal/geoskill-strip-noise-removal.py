#!/usr/bin/env python3
"""strip-noise-removal — 条带噪声去除

去除多光谱 / 热红外影像中的条带噪声（Landsat 7 SLC-off、MODIS 探测器退化等），
实现两种经典算法：

- **矩匹配 (moment matching)**：逐列（或逐行）将均值和标准差归一化到全图统计量。
  对加性 + 乘性条带均有效，是最常用的快速去条带方法。
- **加权线性回归 (weighted linear regression)**：对每个条带列拟合
  ``y_stripe = a * y_ref + b``，用无条带参考列做回归基准，最小化条带与参考的差异。
  对非均匀条带（如渐变型退化）效果优于矩匹配。

数据源：本地多波段 GeoTIFF；或 ``--synthetic`` / 仅给 ``--bbox`` 时离线生成
含可控条带（加性偏移 + 乘性增益 + 随机坏线）的模拟影像。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python strip-noise-removal.py --bbox 116 39 117 40 --synthetic
    python strip-noise-removal.py --input scene.tif --direction vertical --method moment
    python strip-noise-removal.py --input scene.tif --direction horizontal --method regression

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
SKILL_NAME = "strip-noise-removal"

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
# 核心算法
# ---------------------------------------------------------------------------
def moment_matching(
    band: np.ndarray,
    direction: str = "vertical",
    mask: Optional[np.ndarray] = None,
) -> np.ndarray:
    """矩匹配去条带：逐列（vertical）或逐行（horizontal）归一化。

    对每个条带单元 k：
        y_corrected = (y - mean_k) / std_k * global_std + global_mean

    mask: 与 band 同形状，0 表示无效像元（不参与统计，不修正）。
    """
    band = band.astype(np.float64)
    h, w = band.shape

    if direction not in ("vertical", "horizontal"):
        raise UsageError(f"direction must be 'vertical' or 'horizontal', got '{direction}'")

    if mask is None:
        mask = np.ones_like(band, dtype=bool)
    else:
        mask = mask.astype(bool)

    # 全局统计量
    valid = band[mask]
    if valid.size == 0:
        return band.astype(np.float32)
    global_mean = float(np.mean(valid))
    global_std = float(np.std(valid))
    if global_std < 1e-9:
        return band.astype(np.float32)

    result = band.copy()

    if direction == "vertical":
        # 逐列处理
        for c in range(w):
            col_mask = mask[:, c]
            if not col_mask.any():
                continue
            col = band[:, c][col_mask]
            m, s = float(np.mean(col)), float(np.std(col))
            if s < 1e-9:
                result[:, c] = global_mean
            else:
                corrected = (band[:, c] - m) / s * global_std + global_mean
                result[:, c] = np.where(mask[:, c], corrected, band[:, c])
    else:  # horizontal
        # 逐行处理
        for r in range(h):
            row_mask = mask[r, :]
            if not row_mask.any():
                continue
            row = band[r, :][row_mask]
            m, s = float(np.mean(row)), float(np.std(row))
            if s < 1e-9:
                result[r, :] = global_mean
            else:
                corrected = (band[r, :] - m) / s * global_std + global_mean
                result[r, :] = np.where(mask[r, :], corrected, band[r, :])

    return result.astype(np.float32)


def weighted_regression(
    band: np.ndarray,
    direction: str = "vertical",
    mask: Optional[np.ndarray] = None,
    ref_fraction: float = 0.3,
) -> np.ndarray:
    """加权线性回归去条带：以无条带参考区域为基准做逐列/行回归。

    对每个条带单元 k，取参考区域（全图最中间 ref_fraction 比例的列/行）
    的均值作为 y_ref，拟合 y_k = a * y_ref + b，然后校正。
    """
    band = band.astype(np.float64)
    h, w = band.shape

    if direction not in ("vertical", "horizontal"):
        raise UsageError(f"direction must be 'vertical' or 'horizontal', got '{direction}'")

    if mask is None:
        mask = np.ones_like(band, dtype=bool)
    else:
        mask = mask.astype(bool)

    result = band.copy()

    if direction == "vertical":
        # 参考列：中间 ref_fraction 比例
        n_ref = max(1, int(w * ref_fraction))
        c_start = (w - n_ref) // 2
        ref_cols = band[:, c_start:c_start + n_ref]
        ref_mask = mask[:, c_start:c_start + n_ref]
        y_ref = np.nanmean(np.where(ref_mask, ref_cols, np.nan), axis=1)

        for c in range(w):
            col_mask = mask[:, c]
            if not col_mask.any():
                continue
            y_k = band[:, c]
            valid = col_mask & np.isfinite(y_ref)
            if valid.sum() < 2:
                continue
            x, y = y_ref[valid], y_k[valid]
            # 拟合 y_k = a*x + b
            A = np.column_stack([x, np.ones_like(x)])
            coef, *_ = np.linalg.lstsq(A, y, rcond=None)
            a, b = float(coef[0]), float(coef[1])
            # 校正：y_corrected = (y_k - b) / a  → 回归到参考尺度
            if abs(a) > 1e-9:
                corrected = (band[:, c] - b) / a
                result[:, c] = np.where(mask[:, c], corrected, band[:, c])

    else:  # horizontal
        n_ref = max(1, int(h * ref_fraction))
        r_start = (h - n_ref) // 2
        ref_rows = band[r_start:r_start + n_ref, :]
        ref_mask = mask[r_start:r_start + n_ref, :]
        y_ref = np.nanmean(np.where(ref_mask, ref_rows, np.nan), axis=0)

        for r in range(h):
            row_mask = mask[r, :]
            if not row_mask.any():
                continue
            y_k = band[r, :]
            valid = row_mask & np.isfinite(y_ref)
            if valid.sum() < 2:
                continue
            x, y = y_ref[valid], y_k[valid]
            A = np.column_stack([x, np.ones_like(x)])
            coef, *_ = np.linalg.lstsq(A, y, rcond=None)
            a, b = float(coef[0]), float(coef[1])
            if abs(a) > 1e-9:
                corrected = (band[r, :] - b) / a
                result[r, :] = np.where(mask[r, :], corrected, band[r, :])

    return result.astype(np.float32)


def destripe(
    cube: np.ndarray,
    direction: str = "vertical",
    method: str = "moment",
    mask: Optional[np.ndarray] = None,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """对多波段立方体逐波段去条带。返回 (corrected_cube, params_dict)。"""
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape

    if mask is not None and mask.ndim == 2:
        mask = np.broadcast_to(mask, cube.shape).copy()

    result = np.zeros_like(cube, dtype=np.float32)
    for b in range(nb):
        band_mask = mask[b] if mask is not None else None
        if method == "moment":
            result[b] = moment_matching(cube[b], direction, band_mask)
        elif method == "regression":
            result[b] = weighted_regression(cube[b], direction, band_mask)
        else:
            raise UsageError(f"unknown method '{method}'. Choose moment|regression")

    params = {
        "method": method,
        "direction": direction,
        "n_bands": nb,
        "shape": [h, w],
    }
    return result, params


def compute_stripe_index(band: np.ndarray, direction: str = "vertical") -> float:
    """条带指数（striping index）：逐列/行均值的标准差 / 全图标准差。

    越接近 0 条带越弱，用于量化去条带前后效果。
    """
    valid = band[np.isfinite(band)]
    if valid.size == 0:
        return 0.0
    global_std = float(np.std(valid))
    if global_std < 1e-9:
        return 0.0
    if direction == "vertical":
        line_means = np.nanmean(np.where(np.isfinite(band), band, np.nan), axis=0)
    else:
        line_means = np.nanmean(np.where(np.isfinite(band), band, np.nan), axis=1)
    line_means = line_means[np.isfinite(line_means)]
    if line_means.size == 0:
        return 0.0
    return float(np.std(line_means) / global_std)


# ---------------------------------------------------------------------------
# 合成数据：含可控条带 + 可选 gap mask
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    n_bands: int = 4,
    stripe_amplitude: float = 0.15,
    stripe_type: str = "additive",  # additive | multiplicative | mixed
    n_dead_lines: int = 0,
    gap_fraction: float = 0.0,
    seed: int = 42,
) -> Tuple[np.ndarray, Optional[np.ndarray], Dict[str, Any]]:
    """生成 (bands, H, W) 反射率立方体 + 可选 gap mask（0=gap, 1=valid）。

    条带注入方式：
    - additive：逐列加 N(0, amplitude) 偏移
    - multiplicative：逐列乘 N(1, amplitude) 增益
    - mixed：两者各半
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yn = yy.astype(np.float64) / max(height - 1, 1)
    xn = xx.astype(np.float64) / max(width - 1, 1)

    cube = np.zeros((n_bands, height, width), dtype=np.float64)
    base_means = [0.12, 0.15, 0.18, 0.35]
    for b in range(n_bands):
        surf = base_means[b % len(base_means)] * (
            0.6 + 0.3 * np.sin(4 * np.pi * xn) + 0.1 * np.cos(3 * np.pi * yn))
        surf = np.clip(surf, 0.02, 0.9)
        surf = surf + rng.normal(0, 0.01, size=surf.shape)
        cube[b] = surf

    # 注入条带
    for b in range(n_bands):
        if stripe_type == "additive":
            offsets = rng.normal(0, stripe_amplitude, size=width)
            cube[b] += offsets[np.newaxis, :]
        elif stripe_type == "multiplicative":
            gains = rng.normal(1.0, stripe_amplitude, size=width)
            cube[b] *= gains[np.newaxis, :]
        elif stripe_type == "mixed":
            offsets = rng.normal(0, stripe_amplitude * 0.5, size=width)
            gains = rng.normal(1.0, stripe_amplitude * 0.5, size=width)
            cube[b] = cube[b] * gains[np.newaxis, :] + offsets[np.newaxis, :]

    # 坏线
    if n_dead_lines > 0:
        dead = rng.choice(width, size=min(n_dead_lines, width), replace=False)
        cube[:, :, dead] = 0.0

    # gap mask
    mask = None
    if gap_fraction > 0:
        mask = np.ones((n_bands, height, width), dtype=np.float32)
        gap_mask = rng.random((height, width)) < gap_fraction
        mask[:, gap_mask] = 0.0

    cube = np.clip(cube, 0.0, 1.0).astype(np.float32)
    info = {
        "bbox": bbox, "width": width, "height": height,
        "n_bands": n_bands,
        "stripe_amplitude": stripe_amplitude,
        "stripe_type": stripe_type,
        "n_dead_lines": n_dead_lines,
        "gap_fraction": gap_fraction,
    }
    return cube, mask, info


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
    return cube, bbox


def read_geotiff_full(path: str) -> Tuple[np.ndarray, List[float], int, Optional[float]]:
    """Read GeoTIFF + replace NoData sentinel with NaN; return (cube, bbox, n_valid, input_nodata).

    If *all* pixels are NoData in every band, raises ``ValidationError`` (rc=6).
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=False).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        input_nodata = src.nodata
    if input_nodata is not None:
        cube = np.where(cube == float(input_nodata), np.nan, cube).astype(np.float32)
    valid_mask = np.isfinite(cube)
    n_valid = int(valid_mask.sum())
    if n_valid == 0:
        nodata_str = f"={input_nodata}" if input_nodata is not None else "(none)"
        raise ValidationError(
            f"input raster has no valid pixels (all are NoData{nodata_str})",
            path=path, input_nodata=input_nodata,
        )
    return cube, bbox, n_valid, input_nodata


def validate_bbox(bbox):
    """Validate EPSG:4326 bbox: W<E, S<N, lon/lat ranges, no crossing antimeridian,
    span > 1e-4°. Raises ``ValidationError`` (rc=6)."""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be [W, S, E, N] with 4 floats")
    W, S, E, N = [float(v) for v in bbox]
    if W < -180.0 or E > 180.0 or S < -90.0 or N > 90.0:
        raise ValidationError(
            f"bbox out of WGS-84 range: W={W} S={S} E={E} N={N} "
            "(must satisfy -180<=lon<=180, -90<=lat<=90)",
            bbox=bbox,
        )
    if W >= E:
        if W > 0 and E < 0 and (W - E) < 360.0:
            raise ValidationError(
                f"bbox crosses 180° antimeridian (W={W}, E={E}); "
                "split into two non-antipodal sub-bboxes",
                bbox=bbox,
            )
        raise ValidationError(
            f"bbox has W>=E (W={W}, E={E}); expected W<E in WGS-84 order",
            bbox=bbox,
        )
    if S >= N:
        raise ValidationError(
            f"bbox has S>=N (S={S}, N={N}); expected S<N in WGS-84 order",
            bbox=bbox,
        )
    if (E - W) < 1e-4 or (N - S) < 1e-4:
        raise ValidationError(
            f"bbox is too small (lon-span={E - W:.6f}, lat-span={N - S:.6f}); "
            "need at least 1e-4° on each axis",
            bbox=bbox,
        )
    return [W, S, E, N]


def write_geotiff(path, array, bbox, dtype="float32", nodata=-9999.0):
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
            "direction": getattr(args, "direction", None),
            "method": getattr(args, "method", None),
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

    # 1) bbox validation FIRST (before makedirs)
    if args.input and not args.synthetic:
        if bbox is not None:
            bbox = validate_bbox(bbox)
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)

    n_valid_pixels = None
    input_nodata = None
    synth_info: Optional[Dict[str, Any]] = None
    mask = None
    if args.input and not args.synthetic:
        cube, file_bbox, n_valid_pixels, input_nodata = read_geotiff_full(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            bbox = validate_bbox(bbox)
        source_note = args.input
    else:
        cube, mask, synth_info = generate_synthetic(
            bbox,
            stripe_amplitude=args.stripe_amp,
            stripe_type=args.stripe_type,
            n_dead_lines=args.dead_lines,
            gap_fraction=args.gap_frac,
        )
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    # 去条带前统计
    stripe_before = [round(compute_stripe_index(cube[b], args.direction), 6)
                     for b in range(cube.shape[0])]

    # 执行去条带
    corrected, params = destripe(cube, direction=args.direction, method=args.method,
                                  mask=mask)

    # 去条带后统计
    stripe_after = [round(compute_stripe_index(corrected[b], args.direction), 6)
                    for b in range(corrected.shape[0])]

    # 2) ALL checks passed → safe to makedirs
    os.makedirs(output_dir, exist_ok=True)

    # 输出 GeoTIFF
    out_tif = os.path.join(output_dir, "destriped.tif")
    write_geotiff(out_tif, corrected, bbox)

    # 输出 mask（如果有）
    if mask is not None:
        mask_path = os.path.join(output_dir, "gap_mask.tif")
        write_geotiff(mask_path, mask, bbox, dtype="uint8", nodata=255)

    # 输出统计 JSON
    stats = {
        "method": args.method,
        "direction": args.direction,
        "stripe_index_before": stripe_before,
        "stripe_index_after": stripe_after,
        "mean_stripe_reduction": round(float(np.mean(
            [max(0, b - a) for b, a in zip(stripe_before, stripe_after)])), 6),
    }
    stats_path = os.path.join(output_dir, "destripe_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "direction": args.direction,
        "n_bands": int(cube.shape[0]),
        "mean_stripe_before": round(float(np.mean(stripe_before)), 6),
        "mean_stripe_after": round(float(np.mean(stripe_after)), 6),
        "n_valid_pixels": n_valid_pixels,
        "input_nodata": input_nodata,
    }
    if synth_info is not None:
        qa["synthetic_params"] = {
            k: synth_info[k] for k in
            ("stripe_amplitude", "stripe_type", "n_dead_lines", "gap_fraction")
        }

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(cube.shape[0])},
        {"path": stats_path, "kind": "json"},
    ]
    if mask is not None:
        outputs.append({"path": mask_path, "kind": "raster", "crs_epsg": 4326,
                        "bbox_wgs84": bbox, "band_count": int(cube.shape[0])})

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  direction: {args.direction}")
        print(f"[{SKILL_NAME}] bands: {cube.shape[0]}")
        print(f"[{SKILL_NAME}] mean stripe index before: {qa['mean_stripe_before']}")
        print(f"[{SKILL_NAME}] mean stripe index after:  {qa['mean_stripe_after']}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        print(f"[{SKILL_NAME}] stats: {stats_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Destriping for multispectral imagery (moment matching / regression).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multiband GeoTIFF")
    p.add_argument("--direction", default="vertical", choices=["vertical", "horizontal"],
                   help="stripe direction (default: vertical)")
    p.add_argument("--method", default="moment", choices=["moment", "regression"],
                   help="destriping method (default: moment)")
    # synthetic controls
    p.add_argument("--stripe-amp", type=float, default=0.15,
                   help="synthetic stripe amplitude (default: 0.15)")
    p.add_argument("--stripe-type", default="additive",
                   choices=["additive", "multiplicative", "mixed"],
                   help="synthetic stripe type (default: additive)")
    p.add_argument("--dead-lines", type=int, default=0,
                   help="synthetic number of dead lines (default: 0)")
    p.add_argument("--gap-frac", type=float, default=0.0,
                   help="synthetic gap fraction for mask testing (default: 0)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic striped scene (offline)")
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
