#!/usr/bin/env python3
"""green-infrastructure-mapping — 绿色基础设施制图

从高分辨率多光谱影像制图绿色基础设施（绿地、树木）。核心算法：

- **NDVI**：(NIR − Red) / (NIR + Red)，值域 [−1, 1]，植被 > 0.3。
- **绿地分类**：NDVI > 阈值 → 绿地像元。
- **树木检测**：对 NDVI 场做局部极大值检测（scipy.ndimage.maximum_filter），
  统计树冠候选数（需高于阈值且与邻域有足够对比）。
- **连通性指数**：最大绿地连通斑块面积 / 总绿地面积 ∈ [0, 1]。
  值越高表示绿地越连通（生态廊道完整性越好）。

数据源：本地多光谱 GeoTIFF（Red, NIR），或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络。

Usage:
    python green-infrastructure-mapping.py --input multispectral.tif
    python green-infrastructure-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "green-infrastructure-mapping"

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
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox):
    """Validate a geographic bbox [W, S, E, N] in EPSG:4326.

    Rules (consistent across the project):
      - W < E (no antimeridian wrap; user must split the request)
      - S < N
      - -180 <= W, E <= 180
      - -90 <= S, N <= 90
      - E - W > 0 (non-zero width)
      - N - S > 0 (non-zero height)
    Returns the bbox on success; raises ValidationError on failure.
    """
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError("bbox must be a sequence of 4 floats [W S E N]")
    w, s, e, n = [float(v) for v in bbox]
    if not (w < e):
        raise ValidationError(
            f"bbox W={w} must be < E={e} (antimeridian wrap not supported; "
            f"split your request into two boxes if needed)")
    if not (s < n):
        raise ValidationError(f"bbox S={s} must be < N={n}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox lon must be in [-180, 180], got W={w}, E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox lat must be in [-90, 90], got S={s}, N={n}")
    return [w, s, e, n]


def validate_ndvi_threshold(thr):
    """NDVI must lie in [-1, 1]."""
    try:
        thr = float(thr)
    except (TypeError, ValueError):
        raise ValidationError(f"--ndvi-threshold must be a number, got {thr!r}")
    if not (-1.0 <= thr <= 1.0):
        raise ValidationError(
            f"--ndvi-threshold must be in [-1, 1], got {thr}")
    return thr


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------

def ndvi(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
    nir = np.asarray(nir, dtype=np.float32)
    red = np.asarray(red, dtype=np.float32)
    denom = nir + red
    out = np.where(denom > 1e-6, (nir - red) / denom, 0.0)
    return np.clip(out, -1.0, 1.0).astype(np.float32)


def classify_green(ndvi_arr: np.ndarray, threshold: float = 0.3) -> np.ndarray:
    """NDVI > threshold → 绿地（uint8 1/0）。"""
    return (np.asarray(ndvi_arr, dtype=np.float32) > threshold).astype(np.uint8)


def tree_count(ndvi_arr: np.ndarray, min_ndvi: float = 0.4,
               neighborhood: int = 5) -> int:
    """树木（树冠）计数：NDVI 局部极大值，且高于 min_ndvi。

    局部极大值：像元值等于邻域（maximum_filter）最大值且 > min_ndvi。
    """
    from scipy.ndimage import maximum_filter
    n = np.asarray(ndvi_arr, dtype=np.float32)
    local_max = maximum_filter(n, size=neighborhood, mode="nearest")
    peaks = (n == local_max) & (n > min_ndvi)
    # 去除平台：用 label 统计连通峰值簇
    from scipy.ndimage import label
    labeled, n_features = label(peaks)
    return int(n_features)


def connectivity_index(green_mask: np.ndarray) -> Tuple[float, int]:
    """连通性指数 = 最大连通斑块面积 / 总绿地面积 ∈ [0, 1]。

    返回 (connectivity, n_patches)。无绿地时返回 (0, 0)。
    """
    from scipy.ndimage import label
    mask = np.asarray(green_mask, dtype=bool)
    total = int(mask.sum())
    if total == 0:
        return 0.0, 0
    labeled, n_patches = label(mask)
    if n_patches == 0:
        return 0.0, 0
    sizes = np.bincount(labeled.ravel())
    sizes[0] = 0  # 背景
    largest = int(sizes.max())
    return float(largest) / float(total), int(n_patches)


# ---------------------------------------------------------------------------
# 合成数据：绿地斑块 + 散布树木 + 非绿地背景
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height_px: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 Red, NIR 影像。

    左半区：大片连通绿地（高 NIR）+ 散布树冠（更高 NIR 的圆形斑块）。
    右半区：不透水面（低 NIR，低 Red 高）+ 少量孤立绿地。
    """
    rng = np.random.default_rng(seed)
    red = np.zeros((height_px, width), dtype=np.float32)
    nir = np.zeros((height_px, width), dtype=np.float32)

    # 背景：不透水面
    red[:, :] = 0.20
    nir[:, :] = 0.22

    # 左半区大绿地
    green_mask = np.zeros((height_px, width), dtype=bool)
    green_mask[:, :width // 2] = True
    red[green_mask] = 0.06
    nir[green_mask] = 0.45

    # 散布树冠（圆形高 NDVI 斑块）
    n_trees = 25
    tree_centers = []
    for _ in range(n_trees):
        r = int(rng.integers(4, height_px - 4))
        c = int(rng.integers(4, width // 2 - 4))
        rr, cc = np.ogrid[-r:height_px - r, -c:width - c]
        circle = (rr * rr + cc * cc) <= 9  # 半径 3
        red[circle] = 0.03
        nir[circle] = 0.65
        tree_centers.append((r, c))

    # 右半区少量孤立绿地
    for _ in range(5):
        r = int(rng.integers(4, height_px - 4))
        c = int(rng.integers(width // 2 + 4, width - 4))
        rr, cc = np.ogrid[-r:height_px - r, -c:width - c]
        circle = (rr * rr + cc * cc) <= 16
        red[circle] = 0.06
        nir[circle] = 0.45

    red += rng.normal(0, 0.005, red.shape).astype(np.float32)
    nir += rng.normal(0, 0.005, nir.shape).astype(np.float32)
    red = np.clip(red, 0.01, 1.0)
    nir = np.clip(nir, 0.01, 1.0)

    info = {
        "bbox": bbox, "width": width, "height": height_px,
        "n_trees_injected": n_trees,
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
    """Read a multispectral GeoTIFF. Returns (cube, bbox).

    NoData values declared in the file's metadata are replaced with NaN
    in the returned cube; downstream code uses NaN-safe operations. The
    public test API is kept 2-tuple for backward compatibility; the
    NoData value is exposed via the ``nodata`` attribute of the returned
    ``cube`` (a numpy array with a ``.nodata`` attr set in this module).
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    # Stash nodata for callers that need it without changing the public
    # return shape. We attach it to a small wrapper class.
    wrapped = _CubeWithNodata(cube, nodata)
    return wrapped, bbox


class _CubeWithNodata(np.ndarray):
    """ndarray subclass that carries an extra ``nodata`` attribute.

    Used only for the public read_geotiff return value; arithmetic and
    array operations behave like a normal ndarray.
    """
    nodata: Optional[float]

    def __new__(cls, input_array, nodata=None):
        obj = np.asarray(input_array).view(cls)
        obj.nodata = nodata
        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.nodata = getattr(obj, "nodata", None)


def _finite_mask(cube: np.ndarray) -> np.ndarray:
    """Per-pixel mask that is True iff every band is finite (not NaN/inf)."""
    return np.isfinite(np.asarray(cube)).all(axis=0)


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
            "ndvi_threshold": getattr(args, "ndvi_threshold", 0.3),
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

    # --- pre-flight validation (BEFORE making output dir) -----------------
    bbox = list(args.bbox) if args.bbox else None
    ndvi_thr = validate_ndvi_threshold(args.ndvi_threshold)

    synth_info: Optional[Dict[str, Any]] = None
    input_nodata: Optional[float] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        input_nodata = getattr(cube, "nodata", None)
        # validate the user-supplied bbox (if any) up-front
        if bbox is not None:
            bbox = validate_bbox(bbox)
        else:
            bbox = validate_bbox(file_bbox)
        if cube.shape[0] < 2:
            raise ValidationError(
                f"input must have at least 2 bands (Red, NIR), got {cube.shape[0]}")
        if cube.size == 0:
            raise ValidationError("input raster is empty")
        red = cube[0]
        nir = cube[1]
        # Detect all-NoData early (no valid pixels after mask)
        valid = _finite_mask(cube[:2])
        n_valid = int(valid.sum())
        if n_valid == 0:
            raise ValidationError(
                f"input raster has no valid pixels "
                f"(all values are nodata={input_nodata})")
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError(
                "provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        red, nir, synth_info = generate_synthetic(bbox)
        # synthetic cube is by construction fully valid
        n_valid = int(red.size)
        source_note = "synthetic"

    # All checks passed → now create the output dir.
    os.makedirs(output_dir, exist_ok=True)

    # 2) NDVI → 绿地分类 → 树木 → 连通性
    ndvi_arr = ndvi(nir, red)
    green = classify_green(ndvi_arr, threshold=ndvi_thr)
    n_trees = tree_count(ndvi_arr, min_ndvi=ndvi_thr + 0.1)
    conn, n_patches = connectivity_index(green)

    # 3) 写出（band1=NDVI, band2=green mask）
    out_tif = os.path.join(output_dir, "green_infrastructure.tif")
    stack = np.stack([ndvi_arr, green.astype(np.float32)], axis=0)
    write_geotiff(out_tif, stack, bbox)

    # NaN-safe summary statistics (in case --input had partial NoData)
    mean_ndvi = float(np.nanmean(ndvi_arr)) if np.isfinite(ndvi_arr).any() else 0.0
    green_frac = float(np.nanmean(green.astype(np.float32))) if green.size else 0.0

    stats = {
        "mean_ndvi": mean_ndvi,
        "green_fraction": green_frac,
        "tree_count": n_trees,
        "connectivity_index": conn,
        "n_patches": n_patches,
    }
    stats_path = os.path.join(output_dir, "green_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {"source": source_note, "n_valid_pixels": n_valid,
                          "input_nodata": input_nodata}
    qa.update(stats)
    if synth_info is not None:
        qa["synthetic_n_trees"] = synth_info["n_trees_injected"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 2},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] green fraction: {stats['green_fraction']:.4f}")
        print(f"[{SKILL_NAME}] tree count: {n_trees}")
        print(f"[{SKILL_NAME}] connectivity: {conn:.3f} ({n_patches} patches)")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Green infrastructure mapping from NDVI, tree detection and connectivity.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multispectral GeoTIFF (Red, NIR)")
    p.add_argument("--ndvi-threshold", type=float, default=0.3,
                   help="green classification NDVI threshold (default: 0.3)")
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
