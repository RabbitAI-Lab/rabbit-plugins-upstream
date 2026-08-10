#!/usr/bin/env python3
"""urban-canyon-analysis — 城市峡谷分析

从数字表面模型（DSM）推导城市街道峡谷的形态参数。核心算法：

- **建筑高度**：height = DSM - DTM（数字地形模型）。若无 DTM，用形态学
  开运算估计地面，或直接以 DSM 最小值为基准。
- **街道宽度**：对非建筑区做欧氏距离变换，街道中心线宽度 ≈ 2 × 到最近
  建筑的距离。
- **H/W 比**：高宽比 = 建筑高度 / 街道宽度，是城市气候学的核心峡谷参数。
- **天空可视因子 SVF**：二维无限长峡谷的几何解析解
  SVF = 1 / sqrt(1 + (H/W)²)，值域 [0, 1]。
  H/W=0（开阔地）→ SVF=1；H/W→∞（深峡谷）→ SVF→0。

数据源：本地 DSM GeoTIFF（+ 可选 DTM），或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络。

Usage:
    python urban-canyon-analysis.py --input dsm.tif --dtm dtm.tif
    python urban-canyon-analysis.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "urban-canyon-analysis"

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
def validate_bbox(bbox, *, allow_antimeridian_cross: bool = False) -> None:
    """校验 bbox=[W,S,E,N]（EPSG:4326 度）。"""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must have 4 floats [W S E N]")
    w, s, e, n = [float(v) for v in bbox]
    if not (all(np.isfinite([w, s, e, n]))):
        raise ValidationError("bbox contains non-finite values")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError("bbox lon out of [-180, 180]")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError("bbox lat out of [-90, 90]")
    if w >= e:
        if not allow_antimeridian_cross:
            raise ValidationError(
                f"bbox W>=E ({w} >= {e}); cross-180° not supported"
            )
        raise ValidationError(f"bbox W>=E ({w} >= {e})")
    if s >= n:
        raise ValidationError(f"bbox S>=N ({s} >= {n})")
    if (e - w) < 1e-4 or (n - s) < 1e-4:
        raise ValidationError(
            f"bbox too small (dx={e - w}, dy={n - s}); need >= 1e-4 degrees"
        )


def validate_params(args: argparse.Namespace) -> None:
    """校验 CLI 参数物理合理性 → ValidationError 触发 rc=6。"""
    if not (args.threshold > 0 and np.isfinite(args.threshold)):
        raise ValidationError(
            f"--threshold must be > 0 and finite (got {args.threshold})"
        )
    if args.threshold > 1000.0:
        raise ValidationError(
            f"--threshold {args.threshold} m is unrealistically large "
            f"(typical building detection threshold 1-10 m)"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------

def building_height(dsm: np.ndarray, dtm: np.ndarray) -> np.ndarray:
    """建筑高度 = DSM - DTM，裁剪到 ≥ 0。"""
    dsm = np.asarray(dsm, dtype=np.float32)
    dtm = np.asarray(dtm, dtype=np.float32)
    h = dsm - dtm
    return np.clip(h, 0.0, None).astype(np.float32)


def estimate_ground(dsm: np.ndarray, size: int = 15) -> np.ndarray:
    """形态学开运算估计地面（DTM 代理）。

    用灰度腐蚀后再膨胀（开运算）去除高于结构元素尺度的建筑，
    保留近似地面高程。
    """
    from scipy.ndimage import grey_erosion, grey_dilation
    dsm = np.asarray(dsm, dtype=np.float32)
    foot = size
    eroded = grey_erosion(dsm, size=foot, mode="nearest")
    ground = grey_dilation(eroded, size=foot, mode="nearest")
    return ground.astype(np.float32)


def estimate_street_width(building_mask: np.ndarray, pixel_size: float = 1.0) -> np.ndarray:
    """街道宽度 ≈ 2 × 非建筑像元到最近建筑的距离。

    在街道中心线处，到两侧建筑的距离各为 W/2，故 2×distance = W。
    建筑像元处宽度为 0。
    """
    from scipy.ndimage import distance_transform_edt
    mask = np.asarray(building_mask, dtype=bool)
    # 非建筑区到最近建筑的距离（单位：像元）
    dist = distance_transform_edt(~mask)
    width = 2.0 * dist * float(pixel_size)
    width[mask] = 0.0
    return width.astype(np.float32)


def height_width_ratio(height: np.ndarray, street_width: np.ndarray) -> np.ndarray:
    """H/W 比。街道宽度为 0 处（建筑内部）返回 0。"""
    h = np.asarray(height, dtype=np.float32)
    w = np.asarray(street_width, dtype=np.float32)
    hw = np.zeros_like(h)
    valid = w > 1e-6
    hw[valid] = h[valid] / w[valid]
    return hw.astype(np.float32)


def sky_view_factor(hw_ratio: np.ndarray) -> np.ndarray:
    """二维峡谷天空可视因子：SVF = 1 / sqrt(1 + (H/W)²)。

    值域 [0, 1]。H/W=0 → 1（开阔地）；H/W→∞ → 0（深峡谷）。
    """
    hw = np.asarray(hw_ratio, dtype=np.float32)
    hw = np.clip(hw, 0.0, None)
    svf = 1.0 / np.sqrt(1.0 + hw * hw)
    return svf.astype(np.float32)


# ---------------------------------------------------------------------------
# 合成数据：规则街区网格（建筑块 + 直街道）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height_px: int = 128,
    building_h: float = 20.0,
    block: int = 24,
    street: int = 12,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 DSM + DTM。

    地面高程 50 m，规则建筑块（高 building_h）+ 直街道（宽 street 像元）。
    """
    rng = np.random.default_rng(seed)
    ground = np.full((height_px, width), 50.0, dtype=np.float32)
    mask = np.zeros((height_px, width), dtype=bool)

    period = block + street
    for r0 in range(0, height_px, period):
        for c0 in range(0, width, period):
            r1 = min(r0 + block, height_px)
            c1 = min(c0 + block, width)
            mask[r0:r1, c0:c1] = True

    dsm = ground.copy()
    dsm[mask] = ground[mask] + building_h
    # 微小高程噪声
    dsm += rng.normal(0, 0.1, dsm.shape).astype(np.float32)
    dsm = np.clip(dsm, ground - 1.0, None)

    info = {
        "bbox": bbox, "width": width, "height": height_px,
        "building_height_m": building_h,
        "street_width_px": street,
        "expected_hw": building_h / max(street, 1),
    }
    return dsm, ground, info


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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], float]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        nd = src.nodata
        if nd is not None and np.isfinite(nd):
            cube = np.where(cube == nd, np.nan, cube).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        res = float(src.res[0]) if src.res else 1.0
    return cube, bbox, res


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
            "dtm": getattr(args, "dtm", None),
            "threshold": getattr(args, "threshold", 2.0),
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

    # 1) 参数与 bbox 校验（先做，不创建任何目录）
    validate_params(args)

    bbox = list(args.bbox) if args.bbox else None

    synth_info: Optional[Dict[str, Any]] = None
    pixel_size = 1.0
    if args.input and not args.synthetic:
        dsm_cube, file_bbox, res = read_geotiff(args.input)
        dsm = dsm_cube[0]
        bbox = bbox if bbox is not None else file_bbox
        pixel_size = res if res > 0 else 1.0
        if args.dtm:
            dtm_cube, _, _ = read_geotiff(args.dtm)
            dtm = dtm_cube[0]
        else:
            dtm = estimate_ground(dsm)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        dsm, dtm, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    # input 模式也要校验 bbox
    if bbox is not None:
        validate_bbox(bbox)

    if dsm.size == 0:
        raise ValidationError("input raster is empty")

    # 全 NaN 检查
    n_total = int(dsm.size)
    n_valid = int(np.sum(np.isfinite(dsm)))
    if n_valid == 0:
        raise ValidationError(
            f"input raster has no valid pixels (n_valid=0, n_total={n_total})"
        )

    # 所有校验通过 → 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 2) 建筑高度 → 足迹 → 街道宽度 → H/W → SVF
    height = building_height(dsm, dtm)
    # NaN-safe building_mask: NaN -> 0 → not > threshold
    if not np.all(np.isfinite(height)):
        height = np.where(np.isfinite(height), height, 0.0).astype(np.float32)
    building_mask = height > args.threshold
    street_width = estimate_street_width(building_mask, pixel_size=pixel_size)
    hw = height_width_ratio(height, street_width)
    svf = sky_view_factor(hw)

    # 3) 写出（band1=height, band2=H/W, band3=SVF）
    out_tif = os.path.join(output_dir, "urban_canyon.tif")
    stack = np.stack([height, hw, svf], axis=0)
    write_geotiff(out_tif, stack, bbox)

    # 街道像元（有宽度处）的统计
    street_pixels = street_width > 1e-6
    stats = {
        "mean_building_height_m": float(np.mean(height[building_mask])) if building_mask.any() else 0.0,
        "mean_street_width_m": float(np.mean(street_width[street_pixels])) if street_pixels.any() else 0.0,
        "mean_hw_ratio_street": float(np.mean(hw[street_pixels])) if street_pixels.any() else 0.0,
        "mean_svf_street": float(np.mean(svf[street_pixels])) if street_pixels.any() else 0.0,
        "min_svf": float(np.min(svf)),
        "max_svf": float(np.max(svf)),
    }
    stats_path = os.path.join(output_dir, "canyon_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_total_pixels": n_total,
        "n_valid_pixels": n_valid,
        "input_nodata_handling": "NoData->NaN",
        "n_building_pixels": int(building_mask.sum()),
        "n_street_pixels": int(street_pixels.sum()),
    }
    qa.update(stats)
    if synth_info is not None:
        qa["synthetic_expected_hw"] = synth_info["expected_hw"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 3},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean H/W (street): {stats['mean_hw_ratio_street']:.3f}")
        print(f"[{SKILL_NAME}] mean SVF (street): {stats['mean_svf_street']:.3f}")
        print(f"[{SKILL_NAME}] SVF range: [{stats['min_svf']:.3f}, {stats['max_svf']:.3f}]")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Urban canyon H/W ratio and sky view factor from DSM.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input DSM GeoTIFF")
    p.add_argument("--dtm", help="optional DTM GeoTIFF (else morphological ground)")
    p.add_argument("--threshold", type=float, default=2.0,
                   help="building height threshold in meters (default: 2.0)")
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
