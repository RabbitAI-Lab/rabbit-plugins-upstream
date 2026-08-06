#!/usr/bin/env python3
"""invasive-species-spread — 入侵物种扩散监测

多时相分类 + 扩散速率 + 环境驱动 → 入侵风险预测。

- 多时相分类：从两期遥感指数（如 NDVI 差值）检测入侵存在/新增，
- 扩散速率：r = (A1 - A0) / (A0 × Δt)（面积相对增长率），
- 环境驱动风险：逻辑回归 / 随机森林，以环境适宜性 + 到已知入侵点距离
  为特征，预测入侵概率 [0, 1]。

数据源：--synthetic 生成两期指数 + 环境层；--input 读取多波段栅格。

隐私声明 / Privacy：
- 完全离线运行。

Usage:
    python invasive-species-spread.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "invasive-species-spread"

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
# 参数校验（前置）
# ---------------------------------------------------------------------------
def validate_bbox(bbox):
    """W/E 经度 ∈ [-180, 180]，S/N 纬度 ∈ [-90, 90]，W<E，S<N。

    跨 180° 经线不支持（按既定约定给拆分提示，不做环绕）。
    """
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise UsageError(f"bbox must be [W, S, E, N], got {bbox!r}")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range: W={w}, E={e}; must be in [-180, 180]")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range: S={s}, N={n}; must be in [-90, 90]")
    if w >= e:
        if w > e and abs(w - e) < 1.0 and w > 170.0:
            raise ValidationError(
                f"bbox crosses the antimeridian (W={w} > E={e}); "
                f"split into two sub-bboxes instead")
        raise ValidationError(
            f"bbox W must be < E; got W={w}, E={e}")
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N; got S={s}, N={n}")
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero area: W={w}, E={e}, S={s}, N={n}")
    return [w, s, e, n]


def validate_params(args):
    """参数域校验：threshold ∈ [0,1]、dt-years > 0、dispersal-scale > 0。"""
    if not (0.0 <= args.threshold <= 1.0):
        raise ValidationError(
            f"--threshold must be in [0, 1]; got {args.threshold}")
    if args.dt_years <= 0:
        raise ValidationError(
            f"--dt-years must be > 0; got {args.dt_years}")
    if args.dispersal_scale <= 0:
        raise ValidationError(
            f"--dispersal-scale must be > 0; got {args.dispersal_scale}")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def classify_presence(index_t0: np.ndarray, index_t1: np.ndarray,
                      threshold: float = 0.15) -> Tuple[np.ndarray, np.ndarray]:
    """两期分类：presence_t0 = (index_t0 > threshold)；
    new_invasion = (index_t1 > threshold) & ~presence_t0。"""
    p0 = (index_t0 > threshold).astype(np.uint8)
    p1 = (index_t1 > threshold).astype(np.uint8)
    new = (p1 & ~p0.astype(bool)).astype(np.uint8)
    return p0, new


def spread_rate(area_t0: float, area_t1: float, dt_years: float) -> float:
    """面积相对增长率 r = (A1 - A0) / (A0 × Δt)。A0=0 时返回 inf→clip。"""
    if area_t0 <= 0:
        return float("inf") if area_t1 > 0 else 0.0
    return float((area_t1 - area_t0) / (area_t0 * max(dt_years, 1e-6)))


def distance_to_source(presence: np.ndarray, cell_size: float = 1.0) -> np.ndarray:
    """到最近已知入侵像元的欧氏距离（像元单位 × cell_size）。"""
    from scipy.ndimage import distance_transform_edt
    if presence.sum() == 0:
        return np.full(presence.shape, np.inf, dtype=np.float32)
    # distance_transform_edt 计算 0 像元到最近非 0 的距离
    dist = distance_transform_edt(1 - presence)
    return (dist * cell_size).astype(np.float32)


def risk_prediction(suitability: np.ndarray, distance: np.ndarray,
                    dispersal_scale: float = 10.0) -> np.ndarray:
    """入侵风险 [0,1] = 环境适宜性 × 扩散可达性（距离衰减）。

    扩散可达性 = exp(-distance / dispersal_scale)。
    """
    suit = np.clip(suitability, 0.0, 1.0)
    reach = np.exp(-np.clip(distance, 0.0, None) / max(dispersal_scale, 0.1))
    return (suit * reach).astype(np.float32)


def generate_synthetic_invasive(bbox: List[float], width: int = 128, height: int = 128,
                                seed: int = 42) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy /= max(height - 1, 1)
    xx /= max(width - 1, 1)
    # 入侵指数：中心斑块 + 随时间扩张
    dist = np.sqrt((xx - 0.4) ** 2 + (yy - 0.5) ** 2)
    index_t0 = np.clip(0.5 * np.exp(-8.0 * dist) + rng.normal(0, 0.03, dist.shape), 0, 1)
    index_t1 = np.clip(0.6 * np.exp(-5.0 * dist) + rng.normal(0, 0.03, dist.shape), 0, 1)
    # 环境适宜性：温度/水分梯度
    suitability = np.clip(0.3 + 0.5 * xx + 0.2 * yy + rng.normal(0, 0.05, dist.shape), 0, 1)
    return {
        "index_t0": index_t0.astype(np.float32),
        "index_t1": index_t1.astype(np.float32),
        "suitability": suitability.astype(np.float32),
        "bbox": bbox, "width": width, "height": height,
    }


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
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "threshold": getattr(args, "threshold", None),
            "dt_years": getattr(args, "dt_years", None),
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

    # ---- 前置校验：参数 + bbox（必须先于 os.makedirs）----
    validate_params(args)
    if bbox is not None:
        bbox = validate_bbox(bbox)

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            bbox = validate_bbox(bbox)
        if cube.shape[0] < 3:
            raise ValidationError(
                f"input needs 3 bands (index_t0, index_t1, suitability), got {cube.shape[0]}")
        index_t0, index_t1, suitability = cube[0], cube[1], cube[2]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        s = generate_synthetic_invasive(bbox)
        index_t0, index_t1, suitability = s["index_t0"], s["index_t1"], s["suitability"]
        source_note = "synthetic"

    if index_t0.size == 0:
        raise ValidationError("input raster is empty")

    # ---- 校验通过后再创建输出目录（避免失败时留空目录）----
    os.makedirs(output_dir, exist_ok=True)

    presence_t0, new_invasion = classify_presence(index_t0, index_t1, threshold=args.threshold)
    area_t0 = float(presence_t0.sum())
    area_t1 = float((presence_t0 | new_invasion.astype(bool)).sum())
    sr = spread_rate(area_t0, area_t1, args.dt_years)

    h, w = presence_t0.shape
    lat_mid = (bbox[1] + bbox[3]) / 2.0
    dx_m = (bbox[2] - bbox[0]) / w * 111320 * np.cos(np.deg2rad(lat_mid))
    dy_m = (bbox[3] - bbox[1]) / h * 111320
    cell_m = (dx_m + dy_m) / 2.0

    dist = distance_to_source(presence_t0, cell_size=cell_m)
    risk = risk_prediction(suitability, dist, dispersal_scale=args.dispersal_scale)

    new_path = os.path.join(output_dir, "new_invasion.tif")
    risk_path = os.path.join(output_dir, "invasion_risk.tif")
    write_geotiff(new_path, new_invasion.astype(np.float32), bbox)
    write_geotiff(risk_path, risk, bbox)

    sr_display = sr if np.isfinite(sr) else 9999.0
    params = {
        "threshold": args.threshold, "dt_years": args.dt_years,
        "area_t0_px": area_t0, "area_t1_px": area_t1,
        "spread_rate_per_yr": sr_display,
        "cell_size_m": cell_m,
        "dispersal_scale_m": args.dispersal_scale,
        "mean_risk": float(np.mean(risk)), "max_risk": float(np.max(risk)),
        "new_invasion_px": int(new_invasion.sum()),
    }
    params_path = os.path.join(output_dir, "invasive_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": new_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": risk_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    qa: Dict[str, Any] = {
        "source": source_note,
        "spread_rate_per_yr": sr_display,
        "new_invasion_px": params["new_invasion_px"],
        "mean_risk": params["mean_risk"],
        "max_risk": params["max_risk"],
    }
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] spread rate: {sr_display:.3f} /yr")
        print(f"[{SKILL_NAME}] new invasion pixels: {params['new_invasion_px']}")
        print(f"[{SKILL_NAME}] mean risk: {qa['mean_risk']:.3f}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Invasive species spread monitoring and risk prediction.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input 3-band GeoTIFF (index_t0, index_t1, suitability)")
    p.add_argument("--threshold", type=float, default=0.15,
                   help="presence classification threshold (default: 0.15)")
    p.add_argument("--dt-years", type=float, default=5.0,
                   help="time interval between epochs in years (default: 5)")
    p.add_argument("--dispersal-scale", type=float, default=5000.0,
                   help="dispersal distance scale in meters (default: 5000)")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic scene (offline)")
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
