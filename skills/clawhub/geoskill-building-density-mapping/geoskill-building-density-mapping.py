#!/usr/bin/env python3
"""building-density-mapping — 建筑密度制图

从建筑足迹栅格估计建筑密度（建筑覆盖率）和容积率（FAR, Floor Area Ratio）。
核心算法：

- **建筑密度**：以建筑足迹二值栅格为输入，用方形核对每个像元做局部均值
  卷积（kernel density estimation），得到 [0,1] 的连续密度场。
- **容积率 (FAR)**：FAR = 建筑密度 × (建筑高度 / 标准层高)。标准层高默认
  3.0 m，可通过 ``--floor-height`` 调整。

数据源：本地建筑足迹 GeoTIFF（二值：1=建筑，0=非建筑）+ 建筑高度栅格，
或使用 ``--synthetic`` 生成物理一致的模拟数据用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python building-density-mapping.py --input footprints.tif --heights heights.tif
    python building-density-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "building-density-mapping"

# ---- 复用共享核心库（本地 vendored，随脚本目录一起分发）----
try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, DependencyError, ValidationError, ProcessError,
        to_exit_code,
    )
    from _geoskill_core.manifest import OutputManifest, OutputFile
except ImportError:  # pragma: no cover - fallback minimal definitions
    class GeoSkillError(Exception):
        def __init__(self, message: str, code: int = 7, kind: str = "EGeo", **kw):
            super().__init__(message)
            self.message, self.code, self.kind = message, code, kind

    class UsageError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=2, kind="EUsage", **k)

    class DependencyError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=3, kind="EDependency", **k)

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


def validate_bbox(bbox, ctx: str = "bbox") -> None:
    """Validate a (W, S, E, N) bbox: 4 floats, lon/lat ranges, W<E, S<N.

    Antimeridian crossing (W > E) is NOT supported; raises ValidationError
    suggesting the user split the bbox.
    """
    if bbox is None or len(bbox) != 4:
        raise UsageError(f"{ctx}: expected 4 floats (W S E N); got {bbox!r}")
    try:
        w, s, e, n = [float(v) for v in bbox]
    except (TypeError, ValueError):
        raise UsageError(f"{ctx}: bbox values must be numeric; got {bbox!r}")
    if not (all(np.isfinite([w, s, e, n]))):
        raise ValidationError(f"{ctx}: bbox values must be finite; got {bbox!r}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"{ctx}: longitude out of range (got W={w} E={e}); expected -180..180"
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"{ctx}: latitude out of range (got S={s} N={n}); expected -90..90"
        )
    if w >= e:
        raise ValidationError(
            f"{ctx}: requires W < E (got W={w} E={e}); "
            f"antimeridian crossing is not supported — split the bbox into two."
        )
    if s >= n:
        raise ValidationError(f"{ctx}: requires S < N (got S={s} N={n})")
    if (e - w) < 1e-6 or (n - s) < 1e-6:
        raise ValidationError(
            f"{ctx}: bbox extent too small ({(e - w):.2e} x {(n - s):.2e} deg); "
            f"need at least ~1e-6 deg in each direction"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------

def compute_density(footprint: np.ndarray, kernel_size: int = 5) -> np.ndarray:
    """建筑密度：方形核均值卷积。

    Parameters
    ----------
    footprint : 2D array, 建筑足迹（1=建筑，0=非建筑）
    kernel_size : 方形核边长（>= 1）

    Returns
    -------
    density : 2D float32 array, 值域 [0, 1]
    """
    if not isinstance(kernel_size, (int, np.integer)) or kernel_size < 1:
        raise ValidationError(
            f"kernel_size must be an integer >= 1; got {kernel_size!r}"
        )
    try:
        from scipy.ndimage import uniform_filter
    except ImportError as exc:
        raise DependencyError(
            f"scipy is required for compute_density: {exc}"
        ) from exc
    fp = np.asarray(footprint, dtype=np.float32)
    fp = np.clip(fp, 0.0, 1.0)
    density = uniform_filter(fp, size=kernel_size, mode="constant", cval=0.0)
    return np.clip(density, 0.0, 1.0).astype(np.float32)


def compute_far(
    density: np.ndarray,
    height: np.ndarray,
    floor_height: float = 3.0,
) -> np.ndarray:
    """容积率 FAR = 建筑密度 × (建筑高度 / 标准层高)。

    Parameters
    ----------
    density : 2D float32 [0, 1]
    height : 2D float32, 建筑高度 (m)
    floor_height : 标准层高 (m), 默认 3.0, 必须 > 0

    Returns
    -------
    far : 2D float32, ≥ 0
    """
    if not np.isfinite(floor_height) or floor_height <= 0.0:
        raise ValidationError(
            f"floor_height must be a positive finite number; got {floor_height!r}"
        )
    d = np.asarray(density, dtype=np.float32)
    h = np.asarray(height, dtype=np.float32)
    h = np.clip(h, 0.0, None)
    floors = h / float(floor_height)
    far = d * floors
    return far.astype(np.float32)


# ---------------------------------------------------------------------------
# 合成数据：物理一致的模拟场景（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height_px: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成模拟建筑足迹 + 建筑高度。

    模拟一个城市街区：随机放置若干矩形建筑区块，高度 10-60 m。
    """
    rng = np.random.default_rng(seed)
    footprint = np.zeros((height_px, width), dtype=np.float32)
    heights = np.zeros((height_px, width), dtype=np.float32)

    n_buildings = int(rng.integers(15, 40))
    for _ in range(n_buildings):
        bw = int(rng.integers(4, max(width // 4, 5)))
        bh = int(rng.integers(4, max(height_px // 4, 5)))
        r0 = int(rng.integers(0, max(height_px - bh, 1)))
        c0 = int(rng.integers(0, max(width - bw, 1)))
        h_val = float(rng.uniform(10.0, 60.0))
        footprint[r0:r0 + bh, c0:c0 + bw] = 1.0
        heights[r0:r0 + bh, c0:c0 + bw] = h_val

    info = {
        "bbox": bbox,
        "width": width,
        "height": height_px,
        "n_buildings": n_buildings,
        "footprint_fraction": float(np.mean(footprint)),
        "mean_building_height": float(np.mean(heights[footprint > 0])) if np.any(footprint > 0) else 0.0,
    }
    return footprint, heights, info


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
            band = cube[b].astype("float32")
            band = np.where(np.isfinite(band), band, nodata)
            dst.write(band, b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """Read multi-band GeoTIFF → (cube (nb, H, W) float32, bbox [W, S, E, N]).

    NoData values (from raster profile) are converted to NaN so the caller
    can mask them out via ``np.isfinite``.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        nodata = src.nodata
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    if nodata is not None:
        nd = float(nodata)
        cube = np.where(cube == nd, np.nan, cube)
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
            "heights": getattr(args, "heights", None),
            "kernel_size": getattr(args, "kernel_size", 5),
            "floor_height": getattr(args, "floor_height", 3.0),
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
    if args.input and not args.synthetic:
        fp_cube, file_bbox = read_geotiff(args.input)
        footprint = fp_cube[0]
        bbox = bbox if bbox is not None else file_bbox
        if args.heights:
            h_cube, _ = read_geotiff(args.heights)
            heights = h_cube[0]
        else:
            heights = np.full_like(footprint, 12.0)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        footprint, heights, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    # ---- validation (BEFORE os.makedirs to avoid empty output dirs) ----
    if bbox is None:
        raise UsageError("could not determine bbox")
    validate_bbox(bbox, ctx="bbox")
    if args.kernel_size < 1:
        raise ValidationError(f"--kernel-size must be >= 1 (got {args.kernel_size})")
    if not np.isfinite(args.floor_height) or args.floor_height <= 0.0:
        raise ValidationError(
            f"--floor-height must be a positive finite number (got {args.floor_height})"
        )
    if footprint.size == 0:
        raise ValidationError("input raster is empty")
    if args.input and not args.synthetic:
        # Heights may be a separate raster, but footprint NoData suffices for
        # the "all-NoData" check.
        valid_count = int(np.sum(np.isfinite(footprint)))
        if valid_count == 0:
            raise ValidationError(
                f"input raster has no valid (non-NoData) pixels: {args.input}"
            )
        fp_valid = footprint[np.isfinite(footprint)]
        if fp_valid.size and (float(fp_valid.min()) < 0.0 or float(fp_valid.max()) > 1.0):
            raise ValidationError(
                "building footprint must be a binary mask with values in [0, 1]; "
                f"got min={float(fp_valid.min())} max={float(fp_valid.max())}"
            )
        if args.heights:
            if heights.shape != footprint.shape:
                raise ValidationError(
                    f"--heights shape {heights.shape} does not match footprint "
                    f"shape {footprint.shape}"
                )
            if not bool(np.isfinite(heights).any()):
                raise ValidationError(
                    f"--heights raster has no valid (non-NoData) pixels: {args.heights}"
                )
    os.makedirs(output_dir, exist_ok=True)

    # 2) 计算密度和 FAR
    density = compute_density(footprint, kernel_size=args.kernel_size)
    far = compute_far(density, heights, floor_height=args.floor_height)

    # 3) 写出产物（双波段：band1=density, band2=FAR）
    out_tif = os.path.join(output_dir, "building_density.tif")
    stack = np.stack([density, far], axis=0)
    write_geotiff(out_tif, stack, bbox)

    stats_path = os.path.join(output_dir, "density_stats.json")
    stats = {
        "mean_density": float(np.nanmean(density)),
        "max_density": float(np.nanmax(density)),
        "mean_far": float(np.nanmean(far)),
        "max_far": float(np.nanmax(far)),
        "floor_height_m": args.floor_height,
        "n_valid_pixels": int(np.sum(np.isfinite(density))),
        "n_total_pixels": int(density.size),
    }
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "mean_density": stats["mean_density"],
        "max_density": stats["max_density"],
        "mean_far": stats["mean_far"],
        "max_far": stats["max_far"],
        "n_valid_pixels": stats["n_valid_pixels"],
        "n_total_pixels": stats["n_total_pixels"],
    }
    if args.input and not args.synthetic:
        qa["input_nodata"] = -9999.0
    if synth_info is not None:
        qa["synthetic_footprint_fraction"] = synth_info["footprint_fraction"]
        qa["synthetic_mean_height"] = synth_info["mean_building_height"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 2},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] shape: {footprint.shape}")
        print(f"[{SKILL_NAME}] mean density: {stats['mean_density']:.4f}")
        print(f"[{SKILL_NAME}] mean FAR: {stats['mean_far']:.3f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Building density and FAR mapping from building footprints.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input building footprint GeoTIFF (binary 0/1)")
    p.add_argument("--heights", help="building height GeoTIFF (meters)")
    p.add_argument("--kernel-size", type=int, default=5,
                   help="density kernel size in pixels (default: 5)")
    p.add_argument("--floor-height", type=float, default=3.0,
                   help="standard floor height in meters (default: 3.0)")
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
