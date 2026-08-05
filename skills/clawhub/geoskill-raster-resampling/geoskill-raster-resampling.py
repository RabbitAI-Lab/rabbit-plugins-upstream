#!/usr/bin/env python3
"""raster-resampling — 栅格重采样

用纯 numpy 实现三种经典重采样方法，改变栅格分辨率（像元尺寸）：

- **nearest**（最近邻）：取最近的输入像元值，保持原始取值，适合分类栅格。
- **bilinear**（双线性）：2x2 邻域距离加权，对线性场精确，适合连续数据。
- **cubic**（三次卷积，Keys 1981，a=-0.5）：4x4 邻域卷积，边缘更锐利。

地理范围（bbox）保持不变，仅改变像元网格密度；输出 transform 由 bbox 与
新尺寸重新推算。支持 nodata：插值时若邻域含 nodata 则输出 nodata。

数据源：本地 GeoTIFF（``--input``），或 ``--synthetic`` 模式生成 64x64 的
线性坡面 + 分类块测试栅格（离线）。

隐私声明 / Privacy：
- 默认完全离线运行，``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python raster-resampling.py --input dem.tif --method bilinear --scale 0.5
    python raster-resampling.py --bbox 116 39 117 40 --synthetic --method cubic --output-dir ./out

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
SKILL_NAME = "raster-resampling"

METHODS = {"nearest", "bilinear", "cubic"}

# ---- 共享核心库（本地 vendored，随脚本目录一起分发）----
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
# 核心算法：重采样核函数与坐标映射
# ---------------------------------------------------------------------------
def cubic_kernel(x: float, a: float = -0.5) -> float:
    """Keys 三次卷积核。|x|<=1 与 1<|x|<2 分段。"""
    ax = abs(x)
    if ax <= 1.0:
        return (a + 2.0) * ax ** 3 - (a + 3.0) * ax ** 2 + 1.0
    if ax < 2.0:
        return a * ax ** 3 - 5.0 * a * ax ** 2 + 8.0 * a * ax - 4.0 * a
    return 0.0


def _out_shape(in_h: int, in_w: int, scale: float) -> Tuple[int, int]:
    out_h = max(1, int(round(in_h * scale)))
    out_w = max(1, int(round(in_w * scale)))
    return out_h, out_w


def _map_coords(out_h: int, out_w: int, in_h: int, in_w: int) -> Tuple[np.ndarray, np.ndarray]:
    """输出像元中心 → 输入连续坐标（像元中心对齐）。"""
    oy = np.arange(out_h, dtype=np.float64)
    ox = np.arange(out_w, dtype=np.float64)
    iy = (oy + 0.5) * (in_h / out_h) - 0.5
    ix = (ox + 0.5) * (in_w / out_w) - 0.5
    return iy, ix


def resample_nearest(band: np.ndarray, out_h: int, out_w: int,
                     nodata: Optional[float] = None) -> np.ndarray:
    in_h, in_w = band.shape
    iy, ix = _map_coords(out_h, out_w, in_h, in_w)
    sy = np.clip(np.round(iy).astype(int), 0, in_h - 1)
    sx = np.clip(np.round(ix).astype(int), 0, in_w - 1)
    return band[np.ix_(sy, sx)].astype(np.float32)


def resample_bilinear(band: np.ndarray, out_h: int, out_w: int,
                      nodata: Optional[float] = None,
                      mask: Optional[np.ndarray] = None) -> np.ndarray:
    """Bilinear resample.

    If both ``mask`` (a boolean array, True = NoData) and ``nodata`` are
    provided, the output is set to ``nodata`` whenever any of the 4 source
    pixels in the bilinear stencil is NoData (GDAL semantics).
    """
    in_h, in_w = band.shape
    iy, ix = _map_coords(out_h, out_w, in_h, in_w)
    y0 = np.floor(iy).astype(int)
    x0 = np.floor(ix).astype(int)
    wy = iy - y0
    wx = ix - x0
    y0c = np.clip(y0, 0, in_h - 1)
    y1c = np.clip(y0 + 1, 0, in_h - 1)
    x0c = np.clip(x0, 0, in_w - 1)
    x1c = np.clip(x0 + 1, 0, in_w - 1)

    Iyy = band[np.ix_(y0c, x0c)]
    Iy1 = band[np.ix_(y0c, x1c)]
    I1y = band[np.ix_(y1c, x0c)]
    I11 = band[np.ix_(y1c, x1c)]
    wy2 = wy[:, None]
    wx2 = wx[None, :]
    out = (Iyy * (1 - wy2) * (1 - wx2)
           + Iy1 * (1 - wy2) * wx2
           + I1y * wy2 * (1 - wx2)
           + I11 * wy2 * wx2)

    if mask is not None and nodata is not None:
        M00 = mask[np.ix_(y0c, x0c)]
        M01 = mask[np.ix_(y0c, x1c)]
        M10 = mask[np.ix_(y1c, x0c)]
        M11 = mask[np.ix_(y1c, x1c)]
        any_nd = M00 | M01 | M10 | M11
        out = np.where(any_nd, np.float32(nodata), out).astype(np.float32)
    return out.astype(np.float32)


def resample_cubic(band: np.ndarray, out_h: int, out_w: int,
                   nodata: Optional[float] = None, a: float = -0.5,
                   mask: Optional[np.ndarray] = None) -> np.ndarray:
    """Cubic (Keys 1981, a=-0.5) resample on a 4x4 source stencil.

    If both ``mask`` and ``nodata`` are provided, the output is set to
    ``nodata`` whenever any of the 16 source pixels in the cubic stencil is
    NoData (GDAL semantics).
    """
    in_h, in_w = band.shape
    iy, ix = _map_coords(out_h, out_w, in_h, in_w)
    out = np.empty((out_h, out_w), dtype=np.float32)
    out_mask = np.zeros((out_h, out_w), dtype=bool) if (mask is not None and nodata is not None) else None
    y_base = np.floor(iy).astype(int)
    x_base = np.floor(ix).astype(int)
    fy = iy - y_base
    fx = ix - x_base
    for oy in range(out_h):
        wy = np.array([cubic_kernel(fy[oy] - m, a) for m in (-1, 0, 1, 2)])
        sy = np.clip(y_base[oy] + np.array([-1, 0, 1, 2]), 0, in_h - 1)
        for ox in range(out_w):
            wx = np.array([cubic_kernel(fx[ox] - m, a) for m in (-1, 0, 1, 2)])
            sx = np.clip(x_base[ox] + np.array([-1, 0, 1, 2]), 0, in_w - 1)
            patch = band[np.ix_(sy, sx)]
            val = float(wy @ patch @ wx)
            out[oy, ox] = val
            if out_mask is not None:
                patch_mask = mask[np.ix_(sy, sx)]
                if patch_mask.any():
                    out_mask[oy, ox] = True
    if out_mask is not None:
        out = np.where(out_mask, np.float32(nodata), out).astype(np.float32)
    return out


def resample_band(band: np.ndarray, scale: float, method: str,
                  nodata: Optional[float] = None) -> np.ndarray:
    """按 scale 改变分辨率，返回重采样后的单波段。"""
    if method not in METHODS:
        raise UsageError(f"unknown method '{method}'. Choose from: {sorted(METHODS)}")
    if scale <= 0:
        raise UsageError("scale must be > 0")
    in_h, in_w = band.shape
    out_h, out_w = _out_shape(in_h, in_w, scale)

    work = band.astype(np.float64)
    mask: Optional[np.ndarray] = None
    if nodata is not None:
        mask = np.isclose(work, nodata)
        if method == "nearest":
            # nearest: take source value as-is; if source is nodata, output is nodata
            res = resample_nearest(work, out_h, out_w)
            if mask is not None:
                iy, ix = _map_coords(out_h, out_w, in_h, in_w)
                sy = np.clip(np.round(iy).astype(int), 0, in_h - 1)
                sx = np.clip(np.round(ix).astype(int), 0, in_w - 1)
                src_mask = mask[np.ix_(sy, sx)]
                res = np.where(src_mask, np.float32(nodata), res).astype(np.float32)
            return res.astype(np.float32)
        # bilinear/cubic: pass mask to propagate; fill work with 0 for math
        work = np.where(mask, 0.0, work)

    if method == "nearest":
        return resample_nearest(work, out_h, out_w)
    if method == "bilinear":
        return resample_bilinear(work, out_h, out_w, nodata=nodata, mask=mask)
    return resample_cubic(work, out_h, out_w, nodata=nodata, mask=mask)


def resample_cube(cube: np.ndarray, scale: float, method: str,
                  nodata: Optional[float] = None) -> np.ndarray:
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb = cube.shape[0]
    bands = [resample_band(cube[b], scale, method, nodata) for b in range(nb)]
    return np.stack(bands, axis=0)


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> None:
    """Validate geographic bbox [W, S, E, N] for ordering, sign, and 180°/90° limits."""
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise ValidationError(
            f"--bbox requires 4 floats [W S E N], got {bbox!r}", bbox=list(bbox),
        )
    w, s, e, n = [float(v) for v in bbox]
    import math
    for name, v in (("W", w), ("S", s), ("E", e), ("N", n)):
        if not math.isfinite(v):
            raise ValidationError(
                f"--bbox {name}={v} is not finite", bbox=list(bbox),
            )
    if w >= e:
        raise ValidationError(
            f"--bbox requires W < E (got W={w}, E={e}); "
            f"antimeridian crossing (W>E) is not supported — split into two bboxes",
            bbox=list(bbox), w=float(w), e=float(e),
        )
    if s >= n:
        raise ValidationError(
            f"--bbox requires S < N (got S={s}, N={n})", bbox=list(bbox),
        )
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"--bbox longitudes out of [-180, 180]: W={w}, E={e}", bbox=list(bbox),
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"--bbox latitudes out of [-90, 90]: S={s}, N={n}", bbox=list(bbox),
        )


# ---------------------------------------------------------------------------
# 合成数据：线性坡面 + 分类块（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], size: int = 64) -> Tuple[np.ndarray, Dict[str, Any]]:
    """单波段：左半为行列线性坡面，右半为分类整数块。"""
    yy, xx = np.mgrid[0:size, 0:size].astype(np.float64)
    ramp = (xx + yy)  # 线性平面，双线性/三次应能精确重构
    classes = ((xx // 8).astype(int) % 4) * 10.0
    band = np.where(xx < size / 2, ramp, classes)
    cube = band.astype(np.float32)[np.newaxis, ...]
    info = {"bbox": bbox, "size": size, "min": float(band.min()), "max": float(band.max())}
    return cube, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0) -> None:
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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """Read input GeoTIFF. Raises ValidationError if the entire raster is NoData."""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
        if nodata is not None and np.isclose(cube, nodata).all():
            raise ValidationError(
                "input raster is entirely NoData — no pixels to resample",
                path=path,
            )
    return cube, bbox, nodata


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
    bbox: Optional[List[float]],
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
            "method": getattr(args, "method", None),
            "scale": getattr(args, "scale", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
            "bbox": bbox,
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

    if args.input and not args.synthetic:
        cube, file_bbox, nodata = read_geotiff(args.input)
        if bbox is not None:
            validate_bbox(bbox)
        else:
            validate_bbox(file_bbox)
            bbox = file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        cube, _info = generate_synthetic(bbox, size=args.size)
        nodata = -9999.0
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    in_shape = cube.shape[1:]
    resampled = resample_cube(cube, args.scale, args.method, nodata)
    out_shape = resampled.shape[1:]

    out_tif = os.path.join(output_dir, "resampled.tif")
    write_geotiff(out_tif, resampled, bbox, nodata=nodata if nodata is not None else -9999.0)

    qa = {
        "source": source_note,
        "method": args.method,
        "scale": args.scale,
        "input_shape": [int(in_shape[0]), int(in_shape[1])],
        "output_shape": [int(out_shape[0]), int(out_shape[1])],
        "in_min": float(np.nanmin(cube)),
        "in_max": float(np.nanmax(cube)),
        "out_min": float(np.nanmin(resampled)),
        "out_max": float(np.nanmax(resampled)),
    }
    outputs = [{"path": out_tif, "kind": "raster", "crs_epsg": 4326,
                "bbox_wgs84": bbox, "band_count": int(resampled.shape[0])}]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  scale: {args.scale}")
        print(f"[{SKILL_NAME}] shape: {in_shape} -> {out_shape}")
        print(f"[{SKILL_NAME}] value range: [{qa['out_min']:.3f}, {qa['out_max']:.3f}]")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Resample raster resolution with nearest/bilinear/cubic convolution.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF raster")
    p.add_argument("--method", default="bilinear", choices=sorted(METHODS),
                   help="resampling method (default: bilinear)")
    p.add_argument("--scale", type=float, default=0.5,
                   help="resolution scale factor, e.g. 0.5 halves, 2.0 doubles (default: 0.5)")
    p.add_argument("--size", type=int, default=64,
                   help="synthetic raster size in pixels (default: 64)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate synthetic test raster (offline)")
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
