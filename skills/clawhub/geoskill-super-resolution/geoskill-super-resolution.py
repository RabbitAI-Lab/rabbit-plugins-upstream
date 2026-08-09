#!/usr/bin/env python3
"""super-resolution — 影像超分辨率重建

用双三次（bicubic）插值把低分辨率影像放大 2× / 4×，提升空间分辨率。双三次
插值以 4×4 邻域加权拟合三次曲面，相比最近邻/双线性能更好地保留边缘与纹理，
是轻量、无训练、可离线运行的经典超分基线。

- **scale 2 / 4**：空间放大倍数。
- **method bicubic**：scipy.ndimage.zoom(order=3) 实现的三次卷积插值。

质量评估：在 ``--synthetic`` 模式下，脚本先生成高分辨率"真值"再下采样为低
分辨率输入，超分后与真值比较，给出 PSNR（dB）作为重建质量参考。

数据源：本地低分辨率 GeoTIFF（``--input``），或使用 ``--synthetic`` / 仅
``--bbox`` 自动生成模拟数据用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python super-resolution.py --input lowres.tif --scale 2
    python super-resolution.py --bbox 116 39 117 40 --synthetic --scale 4 --output-dir ./out

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
SKILL_NAME = "super-resolution"

# ---- 复用共享核心库（本地 vendored，随脚本目录一起分发）----
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
# Input validation (bbox / params)
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Any) -> None:
    """Validate a W,S,E,N geographic bbox. Raises ValidationError on bad input.

    Rules:
      - Must be a sequence of 4 numbers.
      - Longitude W, E in [-180, 180]; latitude S, N in [-90, 90].
      - S < N (south below north).
      - W < E *unless* the bbox crosses the antimeridian (W near +180 and E near -180)
        — such cases are rejected with a hint to split into two bboxes.
      - Extent (E-W) and (N-S) must be ≥ 1e-4 degrees (avoid zero-area).
    """
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            f"bbox must be [W,S,E,N] (4 floats), got {bbox!r}",
            bbox=list(bbox) if hasattr(bbox, "__iter__") else None,
        )
    W, S, E, N = bbox
    for v, name in [(W, "W"), (S, "S"), (E, "E"), (N, "N")]:
        try:
            fv = float(v)
        except (TypeError, ValueError):
            raise ValidationError(
                f"bbox {name}={v!r} is not a finite number", bbox=list(bbox),
            )
        if not np.isfinite(fv):
            raise ValidationError(
                f"bbox {name}={v!r} is not a finite number", bbox=list(bbox),
            )
    if not (-180.0 <= float(W) <= 180.0 and -180.0 <= float(E) <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range [-180,180]: W={W}, E={E}", bbox=list(bbox),
        )
    if not (-90.0 <= float(S) <= 90.0 and -90.0 <= float(N) <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range [-90,90]: S={S}, N={N}", bbox=list(bbox),
        )
    if float(W) >= float(E) and not (float(W) > 170.0 and float(E) < -170.0):
        raise ValidationError(
            f"bbox has W >= E ({W} >= {E}); crossing the antimeridian "
            f"(W near +180, E near -180) is not supported. "
            f"Pass a bbox with W < E (e.g. split into two bboxes).",
            bbox=list(bbox),
        )
    if float(W) > 170.0 and float(E) < -170.0:
        # explicit antimeridian crossing — reject with hint
        raise ValidationError(
            f"bbox crosses the antimeridian (W={W}, E={E}); not supported. "
            f"Split into two bboxes: [{W}, {S}, 180.0, {N}] and [-180.0, {S}, {E}, {N}].",
            bbox=list(bbox),
        )
    if float(S) >= float(N):
        raise ValidationError(
            f"bbox has S >= N ({S} >= {N}); south must be strictly less than north.",
            bbox=list(bbox),
        )
    if (float(E) - float(W)) < 1e-4 or (float(N) - float(S)) < 1e-4:
        raise ValidationError(
            f"bbox is too small (extent < 1e-4 degrees): W={W},S={S},E={E},N={N}.",
            bbox=list(bbox),
        )


def validate_params(scale: int, method: str) -> None:
    """Cross-check CLI params that argparse choices already constrain."""
    if scale not in (2, 4):
        raise ValidationError(f"scale must be 2 or 4, got {scale}", scale=int(scale))
    if method != "bicubic":
        raise ValidationError(
            f"unknown method '{method}'. Only 'bicubic' is supported.", method=method,
        )


# ---------------------------------------------------------------------------
# 核心算法：双三次超分 + PSNR
# ---------------------------------------------------------------------------
def bicubic_upscale(cube: np.ndarray, scale: int) -> np.ndarray:
    """把 cube (bands, h, w) 双三次放大 scale 倍 → (bands, h*scale, w*scale)。"""
    from scipy.ndimage import zoom

    if scale not in (2, 4):
        raise UsageError(f"scale must be 2 or 4, got {scale}", scale=int(scale))
    cube = np.asarray(cube, dtype=np.float64)
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    if cube.ndim != 3:
        raise ValidationError(f"cube must be 2-D/3-D, got ndim={cube.ndim}")
    zoomed = zoom(cube, (1.0, float(scale), float(scale)), order=3, mode="nearest")
    return zoomed.astype(np.float32)


def downsample(cube: np.ndarray, scale: int) -> np.ndarray:
    """把 cube (bands, H, W) 下采样 scale 倍（双线性），用于构造低分辨率输入。"""
    from scipy.ndimage import zoom

    cube = np.asarray(cube, dtype=np.float64)
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    z = zoom(cube, (1.0, 1.0 / scale, 1.0 / scale), order=1, mode="nearest")
    return z.astype(np.float32)


def psnr(a: np.ndarray, b: np.ndarray, max_val: float = 1.0) -> float:
    """峰值信噪比 (dB)。a、b 形状相同。完全相等返回 inf。"""
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    if a.shape != b.shape:
        raise ValidationError(
            f"psnr shape mismatch: {a.shape} vs {b.shape}",
            shape_a=list(a.shape), shape_b=list(b.shape),
        )
    mse = float(np.mean((a - b) ** 2))
    if mse <= 0:
        return float("inf")
    return float(10.0 * np.log10((max_val ** 2) / mse))


def super_resolve(
    cube: np.ndarray,
    scale: int = 2,
    method: str = "bicubic",
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """超分辨率主入口。返回 (upscaled_cube, params)。"""
    if method != "bicubic":
        raise UsageError(
            f"unknown method '{method}'. Only 'bicubic' is supported.", method=method,
        )
    upscaled = bicubic_upscale(cube, scale)
    params = {
        "method": method,
        "scale": int(scale),
        "input_shape": list(np.asarray(cube).shape),
        "output_shape": list(upscaled.shape),
    }
    return upscaled, params


# ---------------------------------------------------------------------------
# 合成数据：高分辨率真值 + 低分辨率输入（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    scale: int = 2,
    bands: int = 3,
    base: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成高分辨率真值影像并下采样为低分辨率输入。

    返回 (lowres_cube (bands, base/scale, base/scale),
          truth_cube (bands, base, base), info)。
    """
    rng = np.random.default_rng(seed)
    if base % scale != 0:
        raise ValidationError(f"base ({base}) must be divisible by scale ({scale})")

    yy, xx = np.mgrid[0:base, 0:base]
    yn = yy.astype(np.float32) / max(base - 1, 1)
    xn = xx.astype(np.float32) / max(base - 1, 1)

    truth = np.zeros((bands, base, base), dtype=np.float32)
    for b in range(bands):
        grad = 0.2 + 0.4 * xn + 0.25 * yn
        blob = 0.25 * np.exp(-(((xn - 0.4) ** 2 + (yn - 0.6) ** 2) / 0.02))
        ripple = 0.05 * np.sin(2 * np.pi * 6 * xn) * np.cos(2 * np.pi * 5 * yn)
        noise = rng.normal(0, 0.005, size=(base, base)).astype(np.float32)
        val = grad + blob + ripple + noise + 0.03 * b
        truth[b] = np.clip(val, 0.0, 1.0)

    lowres = downsample(truth, scale)

    info = {
        "bbox": list(bbox),
        "scale": int(scale),
        "bands": bands,
        "truth_shape": list(truth.shape),
        "lowres_shape": list(lowres.shape),
    }
    return lowres, truth, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
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
            "scale": getattr(args, "scale", None),
            "method": getattr(args, "method", None),
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

    # ---- Validate CLI / params up front (no filesystem side effects yet) ----
    validate_params(args.scale, args.method)

    bbox = list(args.bbox) if args.bbox else None
    truth: Optional[np.ndarray] = None

    if args.input and not args.synthetic:
        lowres, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        # Only validate user-supplied bbox; the file bbox comes from the raster
        # header which is implicitly valid (otherwise rasterio would have failed).
        if args.bbox is not None:
            validate_bbox(bbox)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        lowres, truth, _info = generate_synthetic(bbox, scale=args.scale)
        source_note = "synthetic"

    if lowres.size == 0:
        raise ValidationError("input raster is empty")

    # ---- All validation passed — safe to create output directory ----
    os.makedirs(output_dir, exist_ok=True)

    upscaled, params = super_resolve(lowres, scale=args.scale, method=args.method)

    out_tif = os.path.join(output_dir, "super_resolved.tif")
    write_geotiff(out_tif, upscaled, bbox)

    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "scale": int(args.scale),
        "input_shape": list(lowres.shape),
        "output_shape": list(upscaled.shape),
        "mean_value_per_band": [float(np.mean(upscaled[b])) for b in range(upscaled.shape[0])],
    }
    if truth is not None:
        # 真值与超分结果同尺寸，逐波段 PSNR
        qa["psnr_db_per_band"] = [
            psnr(upscaled[b], truth[b], max_val=1.0) for b in range(upscaled.shape[0])
        ]
        qa["psnr_db_overall"] = psnr(upscaled, truth, max_val=1.0)

    qa_path = os.path.join(output_dir, "qa.json")
    with open(qa_path, "w", encoding="utf-8") as f:
        json.dump(qa, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(upscaled.shape[0])},
        {"path": qa_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  scale: {args.scale}")
        print(f"[{SKILL_NAME}] shape: {list(lowres.shape)} -> {list(upscaled.shape)}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        print(f"[{SKILL_NAME}] qa: {qa_path}")
        if "psnr_db_overall" in qa:
            print(f"[{SKILL_NAME}] PSNR vs truth: {qa['psnr_db_overall']:.2f} dB")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Bicubic super-resolution (2x/4x) with PSNR quality assessment.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input low-resolution GeoTIFF")
    p.add_argument("--scale", type=int, default=2, choices=[2, 4],
                   help="upscale factor (default: 2)")
    p.add_argument("--method", default="bicubic", choices=["bicubic"],
                   help="super-resolution method (default: bicubic)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic low/high-res pair (offline)")
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
