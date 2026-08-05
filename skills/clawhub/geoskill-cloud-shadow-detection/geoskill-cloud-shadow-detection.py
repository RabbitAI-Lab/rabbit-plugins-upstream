#!/usr/bin/env python3
"""cloud-shadow-detection — 云与云影检测

基于光谱阈值与太阳几何投影，从多光谱反射率影像中检测云和云影，
输出离散云掩膜（0=晴 / 1=云 / 2=云影）与覆盖率统计：

- **云**：高反射率（可见光波段亮度高于 ``--cloud-threshold``）且蓝光波段
  同样高亮的像元，区别于裸土/建筑等中等亮度地物。
- **云影**：低反射率暗像元（亮度低于 ``--shadow-threshold``），并且落在
  由云掩膜沿太阳方位反方向投影（偏移 ``--shadow-shift`` 个像元）得到的
  预测阴影区域内，从而排除水体等固有暗目标。

数据源：本地多波段 GeoTIFF（地表/TOA 反射率）；或 ``--synthetic`` / 仅给
``--bbox`` 时离线生成含云（亮）与云影（暗）的模拟影像。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python cloud-shadow-detection.py --bbox 116 39 117 40 --cloud-threshold 0.3
    python cloud-shadow-detection.py --bbox 116 39 117 40 --synthetic --output-dir ./out
    python cloud-shadow-detection.py --input scene.tif --solar-azimuth 160

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
SKILL_NAME = "cloud-shadow-detection"

# ---- 复用共享核心库（本地 vendored）----
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


# 掩膜类别值
CLEAR = 0
CLOUD = 1
SHADOW = 2


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def brightness(cube: np.ndarray) -> np.ndarray:
    """逐像元全波段均值亮度 (H, W)。cube 形如 (bands, H, W)。"""
    if cube.ndim == 2:
        return cube.astype(np.float32)
    return np.nanmean(cube, axis=0).astype(np.float32)


def blue_band(cube: np.ndarray) -> np.ndarray:
    """取蓝光波段（默认第 0 波段）。"""
    if cube.ndim == 2:
        return cube.astype(np.float32)
    return cube[0].astype(np.float32)


def detect_cloud(cube: np.ndarray, cloud_threshold: float,
                 blue_floor: float = 0.2) -> np.ndarray:
    """检测云：全波段亮度 > cloud_threshold 且蓝光波段 > blue_floor。

    返回 bool 掩膜 (H, W)。
    """
    bright = brightness(cube)
    blue = blue_band(cube)
    return (bright > cloud_threshold) & (blue > blue_floor)


def shadow_offset(solar_azimuth_deg: float, shift_pixels: float) -> Tuple[int, int]:
    """由太阳方位（compass bearing，光照来向）计算阴影投影的像元偏移 (dy, dx)。

    阴影落在太阳的反方向（bearing + 180°）。方位角以正北为 0、顺时针增大。
    图像坐标：行向下为正（北→南），列向右为正（西→东）。
    """
    bearing = np.deg2rad(solar_azimuth_deg + 180.0)  # 阴影方向
    dx = float(np.sin(bearing)) * shift_pixels   # 东向分量 → 列
    dy = float(-np.cos(bearing)) * shift_pixels  # 北向分量取反 → 行
    return int(round(dy)), int(round(dx))


def project_cloud(cloud_mask: np.ndarray, dy: int, dx: int) -> np.ndarray:
    """把云掩膜沿 (dy, dx) 平移，得到预测阴影位置（整数像元最近邻）。"""
    return np.roll(np.roll(cloud_mask, shift=dy, axis=0), shift=dx, axis=1)


def detect_shadow(cube: np.ndarray, cloud_mask: np.ndarray,
                  solar_azimuth_deg: float, shift_pixels: float,
                  shadow_threshold: float) -> np.ndarray:
    """检测云影：暗像元（亮度 < shadow_threshold）∩ 投影云区。

    返回 bool 掩膜 (H, W)。
    """
    bright = brightness(cube)
    dark = bright < shadow_threshold
    dy, dx = shadow_offset(solar_azimuth_deg, shift_pixels)
    predicted = project_cloud(cloud_mask, dy, dx)
    return dark & predicted


def detect_cloud_shadow(
    cube: np.ndarray,
    cloud_threshold: float = 0.3,
    shadow_threshold: float = 0.1,
    solar_azimuth_deg: float = 160.0,
    shift_pixels: float = 10.0,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """联合检测云与云影。

    返回 (mask uint8 (H,W) with values 0/1/2, stats_dict)。
    重叠像元优先标记为云（CLOUD）。
    """
    if cube.size == 0:
        raise ValidationError("input cube is empty")
    cloud = detect_cloud(cube, cloud_threshold)
    shadow = detect_shadow(cube, cloud, solar_azimuth_deg, shift_pixels,
                           shadow_threshold)
    # 云优先于影
    shadow = shadow & (~cloud)

    h, w = cloud.shape
    mask = np.full((h, w), CLEAR, dtype=np.uint8)
    mask[shadow] = SHADOW
    mask[cloud] = CLOUD

    npx = h * w
    n_cloud = int(np.count_nonzero(cloud))
    n_shadow = int(np.count_nonzero(shadow))
    stats = {
        "cloud_pixels": n_cloud,
        "shadow_pixels": n_shadow,
        "clear_pixels": int(npx - n_cloud - n_shadow),
        "total_pixels": int(npx),
        "cloud_fraction": round(n_cloud / npx, 6),
        "shadow_fraction": round(n_shadow / npx, 6),
        "cloud_shadow_fraction": round((n_cloud + n_shadow) / npx, 6),
        "cloud_threshold": cloud_threshold,
        "shadow_threshold": shadow_threshold,
        "solar_azimuth_deg": solar_azimuth_deg,
        "shadow_shift_pixels": shift_pixels,
    }
    return mask, stats


# ---------------------------------------------------------------------------
# 合成数据：含云（亮）与云影（暗）的模拟影像
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    cloud_threshold: float = 0.3,
    shadow_threshold: float = 0.1,
    solar_azimuth_deg: float = 160.0,
    shift_pixels: float = 10.0,
    bands: int = 4,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (bands, H, W) 反射率影像，含一块亮云与按太阳方位投影的暗云影。

    地物背景为中等反射率（~0.2），云方块 ~0.85，云影方块 ~0.03，
    云影位置由 ``shadow_offset`` 精确放置，保证检测可复现。
    """
    rng = np.random.default_rng(seed)
    base = np.full((height, width), 0.20, dtype=np.float32)
    base = base + rng.normal(0, 0.02, size=base.shape).astype(np.float32)
    base = np.clip(base, 0.12, 0.28)

    # 云方块（居中偏上）
    cy0, cx0 = height // 4, width // 3
    ch, cw = height // 6, width // 6
    cloud_mask = np.zeros((height, width), dtype=bool)
    cloud_mask[cy0:cy0 + ch, cx0:cx0 + cw] = True

    # 云影方块：按太阳方位从云平移
    dy, dx = shadow_offset(solar_azimuth_deg, shift_pixels)
    shadow_mask = np.roll(np.roll(cloud_mask, shift=dy, axis=0), shift=dx, axis=1)

    # 先涂影、后涂云，保证重叠像元以云为准（与 truth 的标记顺序一致）
    scene = base.copy()
    scene[shadow_mask] = 0.03
    scene[cloud_mask] = 0.85

    cube = np.zeros((bands, height, width), dtype=np.float32)
    for b in range(bands):
        layer = scene + rng.normal(0, 0.005, size=scene.shape).astype(np.float32)
        cube[b] = np.clip(layer, 0.0, 1.0)

    truth = np.full((height, width), CLEAR, dtype=np.uint8)
    truth[shadow_mask] = SHADOW
    truth[cloud_mask] = CLOUD

    info = {
        "bbox": bbox, "width": width, "height": height, "bands": bands,
        "solar_azimuth_deg": solar_azimuth_deg,
        "shadow_shift_pixels": shift_pixels,
        "truth_cloud_fraction": round(float(np.count_nonzero(cloud_mask)) / (height * width), 6),
        "truth_shadow_fraction": round(float(np.count_nonzero(shadow_mask)) / (height * width), 6),
    }
    return cube, info, truth


# ---------------------------------------------------------------------------
# 输入校验：bbox（共用同 animated-map-series 模板）
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> None:
    """Validate a [W, S, E, N] bbox in WGS-84.

    Raises ValidationError (exit 6) for:
      - wrong length
      - non-finite values
      - longitude out of [-180, 180]
      - latitude  out of [-90, 90]
      - W >= E (would make a non-positive-width raster)
      - S >= N
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(
            f"bbox must have 4 floats [W S E N], got {bbox!r}",
        )
    w, s, e, n = bbox
    vals = [w, s, e, n]
    if not all(np.isfinite(vals)):
        raise ValidationError(f"bbox contains non-finite values: {vals}")
    if not (-180.0 <= w <= 180.0) or not (-180.0 <= e <= 180.0):
        raise ValidationError(
            f"longitude out of [-180, 180]: W={w}, E={e}",
        )
    if not (-90.0 <= s <= 90.0) or not (-90.0 <= n <= 90.0):
        raise ValidationError(
            f"latitude out of [-90, 90]: S={s}, N={n}",
        )
    if w >= e:
        raise ValidationError(
            f"bbox W must be < E (W={w}, E={e}); cross-180 not supported; "
            f"split into two bboxes at the dateline",
        )
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N (S={s}, N={n})",
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox extent too small (W={w}, E={e}, S={s}, N={n})",
        )


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """Read a multiband GeoTIFF, returning (cube, bbox) with NoData→NaN."""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=True).astype(np.float32)
        cube = np.ma.filled(cube, np.nan)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def write_mask_geotiff(path: str, mask: np.ndarray, bbox: List[float]) -> None:
    import rasterio
    from rasterio.transform import from_bounds
    if mask.ndim == 3:
        mask = mask[0]
    h, w = mask.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": 1,
        "dtype": "uint8", "crs": "EPSG:4326", "transform": transform,
        "nodata": 255, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        dst.write(mask.astype("uint8"), 1)


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
            "cloud_threshold": getattr(args, "cloud_threshold", None),
            "solar_azimuth": getattr(args, "solar_azimuth", None),
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

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, synth_info, _truth = generate_synthetic(
            bbox, cloud_threshold=args.cloud_threshold,
            shadow_threshold=args.shadow_threshold,
            solar_azimuth_deg=args.solar_azimuth,
            shift_pixels=args.shadow_shift,
        )
        source_note = "synthetic"

    # 校验（先于 makedirs）
    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.ndim == 3 and cube.shape[0] < 2:
        raise ValidationError(
            f"input must have at least 2 bands (need a 'blue' band); got {cube.shape[0]} band(s)",
        )
    if bbox is not None:
        validate_bbox(bbox)
    if not np.any(np.isfinite(cube)):
        raise ValidationError(
            "input raster has no valid (finite) pixels across all bands (all NoData or NaN)",
        )

    # 现在 makedirs
    os.makedirs(output_dir, exist_ok=True)

    mask, stats = detect_cloud_shadow(
        cube, cloud_threshold=args.cloud_threshold,
        shadow_threshold=args.shadow_threshold,
        solar_azimuth_deg=args.solar_azimuth,
        shift_pixels=args.shadow_shift,
    )

    out_tif = os.path.join(output_dir, "cloud_shadow_mask.tif")
    write_mask_geotiff(out_tif, mask, bbox)

    stats_path = os.path.join(output_dir, "coverage_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {"source": source_note}
    qa.update(stats)
    if synth_info is not None:
        qa["truth_cloud_fraction"] = synth_info["truth_cloud_fraction"]
        qa["truth_shadow_fraction"] = synth_info["truth_shadow_fraction"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] cloud fraction:    {stats['cloud_fraction']:.4f}")
        print(f"[{SKILL_NAME}] shadow fraction:   {stats['shadow_fraction']:.4f}")
        print(f"[{SKILL_NAME}] mask: {out_tif}")
        print(f"[{SKILL_NAME}] stats: {stats_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Detect clouds and cloud shadows from multispectral reflectance imagery.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multiband GeoTIFF (reflectance)")
    p.add_argument("--cloud-threshold", type=float, default=0.3,
                   help="brightness threshold for cloud (default: 0.3)")
    p.add_argument("--shadow-threshold", type=float, default=0.1,
                   help="brightness threshold for dark shadow candidates (default: 0.1)")
    p.add_argument("--solar-azimuth", type=float, default=160.0,
                   help="solar azimuth in degrees, direction light comes from (default: 160)")
    p.add_argument("--shadow-shift", type=float, default=10.0,
                   help="shadow projection offset in pixels (default: 10)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic scene with cloud and shadow (offline)")
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
