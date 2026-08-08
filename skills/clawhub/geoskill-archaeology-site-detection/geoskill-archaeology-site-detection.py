#!/usr/bin/env python3
"""archaeology-site-detection — 考古遗址遥感探测

融合 LiDAR 微地形、多光谱植被异常与 SAR 后向散射异常，自动筛查疑似考古遗址并
给出异常等级。方法论：

- **微地形异常**：对 DEM 做大窗口背景去趋势（local relief），突出人为土丘
  (mound) / 凹陷 (depression) 等微地貌。
- **多光谱异常**：计算 NDVI 并对其去趋势，识别"作物标志"(crop mark) —— 地下
  遗存导致的植被长势差异。
- **SAR 异常**：后向散射全局 z-score，识别湿度/结构异常（壕沟、墙基）。
- **融合与分级**：各异常层归一化后加权/取最大融合，阈值分级（无/低/高），
  局部峰值定位疑似遗址点。

数据源：本地多波段 GeoTIFF（DEM/Red/NIR/SAR），或 ``--synthetic`` 生成含注入
遗迹的模拟场景用于离线测试。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络；本地处理，不上传数据。

Usage:
    python archaeology-site-detection.py --input scene.tif --output-dir ./out
    python archaeology-site-detection.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "archaeology-site-detection"

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


BAND_ROLES = ["dem", "red", "nir", "sar"]
N_REQUIRED_BANDS = len(BAND_ROLES)


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
def ndvi(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
    nir = np.asarray(nir, dtype=np.float32)
    red = np.asarray(red, dtype=np.float32)
    denom = nir + red
    out = np.where(np.abs(denom) > 1e-9, (nir - red) / denom, 0.0)
    return np.clip(out, -1.0, 1.0).astype(np.float32)


def normalize01(arr: np.ndarray) -> np.ndarray:
    """Min-max 归一化到 [0,1]；常数数组返回全 0。"""
    a = np.asarray(arr, dtype=np.float32)
    valid = a[np.isfinite(a)]
    if valid.size == 0:
        return np.zeros_like(a)
    mn, mx = float(valid.min()), float(valid.max())
    if mx - mn < 1e-9:
        return np.zeros_like(a)
    return np.clip((a - mn) / (mx - mn), 0.0, 1.0).astype(np.float32)


def detrend_relief(dem: np.ndarray, size: int = 15) -> np.ndarray:
    """微地形局部起伏：DEM − 大窗口背景（均值滤波去趋势）。"""
    from scipy.ndimage import uniform_filter
    dem = np.asarray(dem, dtype=np.float32)
    bg = uniform_filter(dem, size=max(int(size), 3), mode="nearest")
    return (dem - bg).astype(np.float32)


def vegetation_anomaly(red: np.ndarray, nir: np.ndarray, size: int = 15) -> np.ndarray:
    """作物标志异常：NDVI 对局部背景的正偏差。"""
    from scipy.ndimage import uniform_filter
    nd = ndvi(nir, red)
    bg = uniform_filter(nd, size=max(int(size), 3), mode="nearest")
    return (nd - bg).astype(np.float32)


def sar_anomaly(sar: np.ndarray) -> np.ndarray:
    """SAR 后向散射全局 z-score。"""
    sar = np.asarray(sar, dtype=np.float32)
    valid = sar[np.isfinite(sar)]
    if valid.size == 0:
        return np.zeros_like(sar)
    mu, sd = float(valid.mean()), float(valid.std())
    if sd < 1e-9:
        return np.zeros_like(sar)
    return ((sar - mu) / sd).astype(np.float32)


def fuse_anomalies(
    layers: List[np.ndarray],
    weights: Optional[List[float]] = None,
    method: str = "weighted",
) -> np.ndarray:
    """融合多异常层（先各自归一化到 [0,1]）。

    - weighted：加权求和后裁剪到 [0,1]；
    - max：逐像元取最大。
    """
    if not layers:
        raise ValidationError("no anomaly layers to fuse")
    normed = [normalize01(l) for l in layers]
    if weights is None:
        weights = [1.0 / len(normed)] * len(normed)
    w = np.asarray(weights, dtype=np.float32)
    w = w / max(float(w.sum()), 1e-9)
    stack = np.stack(normed, axis=0)
    if method == "max":
        fused = np.max(stack, axis=0)
    else:  # weighted
        fused = np.tensordot(w, stack, axes=(0, 0))
    return np.clip(fused, 0.0, 1.0).astype(np.float32)


def classify_level(score: np.ndarray, low: float = 0.5, high: float = 0.75) -> np.ndarray:
    """异常分级：0=无，1=低，2=高。"""
    score = np.asarray(score, dtype=np.float32)
    lvl = np.zeros(score.shape, dtype=np.int16)
    lvl = np.where(score >= low, 1, lvl)
    lvl = np.where(score >= high, 2, lvl)
    return lvl.astype(np.int16)


def detect_sites(
    score: np.ndarray,
    threshold: float = 0.6,
    footprint: int = 7,
) -> List[Dict[str, Any]]:
    """局部峰值定位疑似遗址点，返回 [{x, y, score, level}]（score 降序）。"""
    from scipy.ndimage import maximum_filter
    s = np.where(np.isfinite(score), score, 0.0).astype(np.float32)
    lm = maximum_filter(s, size=max(int(footprint), 3), mode="constant")
    peaks = (s == lm) & (s >= float(threshold)) & (s > 0)
    ys, xs = np.where(peaks)
    level = classify_level(s)
    sites = []
    for y, x in zip(ys.tolist(), xs.tolist()):
        sites.append({
            "x": int(x), "y": int(y),
            "score": float(s[y, x]), "level": int(level[y, x]),
        })
    sites.sort(key=lambda d: d["score"], reverse=True)
    return sites


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (4,H,W)：DEM/Red/NIR/SAR，并注入若干已知遗迹（土丘 + 作物标志）。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    ny = yy / max(height - 1, 1)
    nx = xx / max(width - 1, 1)
    dem = 200.0 + 10.0 * nx + 6.0 * ny + rng.normal(0, 0.2, (height, width)).astype(np.float32)

    sites = [
        {"x": int(0.30 * (width - 1)), "y": int(0.35 * (height - 1)), "r": 6, "h": 3.5},
        {"x": int(0.68 * (width - 1)), "y": int(0.62 * (height - 1)), "r": 5, "h": 2.8},
    ]
    cropmark = np.zeros((height, width), dtype=np.float32)
    for st in sites:
        d2 = (xx - st["x"]) ** 2 + (yy - st["y"]) ** 2
        bump = st["h"] * np.exp(-d2 / (2.0 * (st["r"] * 0.6) ** 2))
        dem += bump.astype(np.float32)
        cropmark += np.exp(-d2 / (2.0 * (st["r"] * 0.9) ** 2)).astype(np.float32)

    # 植被：作物标志处 NIR 更高、Red 更低
    red = (0.16 - 0.05 * cropmark + rng.normal(0, 0.004, (height, width))).astype(np.float32)
    nir = (0.22 + 0.18 * cropmark + rng.normal(0, 0.006, (height, width))).astype(np.float32)
    red = np.clip(red, 0.02, 1.0)
    nir = np.clip(nir, 0.02, 1.0)
    # SAR：遗迹处后向散射略高
    sar = (-15.0 + 3.0 * cropmark + rng.normal(0, 0.3, (height, width))).astype(np.float32)

    cube = np.stack([dem, red, nir, sar], axis=0).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "band_roles": BAND_ROLES, "injected_sites": sites}
    return cube, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path, cube, bbox, nodata=-9999.0, dtype="float32"):
    import rasterio
    from rasterio.transform import from_bounds
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {"driver": "GTiff", "height": h, "width": w, "count": nb,
               "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
               "nodata": nodata, "compress": "deflate"}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype(dtype), b + 1)


def read_geotiff(path):
    """Read multi-band GeoTIFF → (cube (nb, H, W) float32, bbox [W, S, E, N]).

    NoData values (from raster profile) are converted to NaN so the caller
    can mask them out via ``np.isfinite`` (e.g. in ``sar_anomaly``).
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
        if np.isfinite(nd):
            cube = np.where(cube == nd, np.nan, cube)
        else:
            cube = np.where(cube == nd, np.nan, cube)
    return cube, bbox


def sites_to_geojson(sites, bbox, width, height):
    w, s, e, n = bbox
    dx = (e - w) / max(int(width), 1)
    dy = (n - s) / max(int(height), 1)
    feats = []
    for i, st in enumerate(sites):
        lon = w + (st["x"] + 0.5) * dx
        lat = n - (st["y"] + 0.5) * dy
        feats.append({
            "type": "Feature", "id": i,
            "geometry": {"type": "Point", "coordinates": [round(lon, 6), round(lat, 6)]},
            "properties": {"site_id": i, "score": round(st["score"], 4),
                           "anomaly_level": st["level"]},
        })
    return {"type": "FeatureCollection", "features": feats}


def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None),
                "fusion": getattr(args, "fusion", None),
                "synthetic": bool(getattr(args, "synthetic", False)), "bbox": bbox},
        outputs=[OutputFile(**o) for o in outputs], qa=qa,
        software={"python": sys.version.split()[0], "skill": SKILL_NAME},
    )
    path = os.path.join(output_dir, "output-manifest.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(man.to_dict(), f, ensure_ascii=False, indent=2, default=str)
    return path


def process(args):
    started_at = _utc_now()
    output_dir = args.output_dir
    bbox = list(args.bbox) if args.bbox else None

    synth_info = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, synth_info = generate_synthetic_cube(bbox)
        source_note = "synthetic"

    # ---- validation (BEFORE os.makedirs to avoid empty output dirs) ----
    if bbox is None:
        raise UsageError("could not determine bbox")
    validate_bbox(bbox, ctx="bbox")
    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.ndim != 3 or cube.shape[0] < N_REQUIRED_BANDS:
        raise ValidationError(
            f"input must have >= {N_REQUIRED_BANDS} bands ({BAND_ROLES}); got {cube.shape}")
    # All-NoData check (only for real input — synthetic has no NoData)
    if args.input and not args.synthetic:
        valid_count = int(np.sum(np.isfinite(cube)))
        if valid_count == 0:
            raise ValidationError(
                f"input raster has no valid (non-NoData) pixels: {args.input}"
            )
    os.makedirs(output_dir, exist_ok=True)

    dem, red, nir, sar = cube[0], cube[1], cube[2], cube[3]
    _, h, w = cube.shape

    relief = detrend_relief(dem, size=args.window)
    veg = vegetation_anomaly(red, nir, size=args.window)
    sarz = sar_anomaly(sar)

    weights = [args.w_relief, args.w_spectral, args.w_sar]
    fused = fuse_anomalies([relief, veg, sarz], weights=weights, method=args.fusion)
    level = classify_level(fused, low=args.low_threshold, high=args.high_threshold)
    sites = detect_sites(fused, threshold=args.site_threshold, footprint=args.footprint)

    out_fused = os.path.join(output_dir, "anomaly_score.tif")
    write_geotiff(out_fused, fused, bbox)
    out_level = os.path.join(output_dir, "anomaly_level.tif")
    write_geotiff(out_level, level.astype(np.float32), bbox, nodata=-1.0)

    gj = sites_to_geojson(sites, bbox, w, h)
    sites_path = os.path.join(output_dir, "suspected_sites.geojson")
    with open(sites_path, "w", encoding="utf-8") as f:
        json.dump(gj, f, ensure_ascii=False)

    n_high = int(np.count_nonzero(level == 2))
    n_low = int(np.count_nonzero(level == 1))
    report = {
        "source": source_note, "fusion": args.fusion, "weights": weights,
        "n_suspected_sites": len(sites),
        "high_anomaly_px": n_high, "low_anomaly_px": n_low,
        "mean_score": float(np.mean(fused)),
        "sites": sites[:50],
    }
    report_path = os.path.join(output_dir, "detection_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "n_suspected_sites": len(sites),
          "mean_score": float(np.mean(fused)),
          "high_anomaly_px": n_high, "low_anomaly_px": n_low}
    if synth_info is not None:
        qa["synthetic_injected_sites"] = len(synth_info["injected_sites"])

    outputs = [
        {"path": out_fused, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_level, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": sites_path, "kind": "vector", "crs_epsg": 4326, "bbox_wgs84": bbox, "feature_count": len(sites)},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] suspected sites: {len(sites)}  high px: {n_high}")
        print(f"[{SKILL_NAME}] mean anomaly score: {np.mean(fused):.4f}")
        print(f"[{SKILL_NAME}] report: {report_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser():
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Archaeological site detection via LiDAR micro-topography, "
                    "multispectral crop-mark and SAR anomaly fusion.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input multi-band GeoTIFF (DEM/Red/NIR/SAR)")
    p.add_argument("--synthetic", action="store_true")
    p.add_argument("--fusion", default="weighted", choices=["weighted", "max"],
                   help="anomaly fusion method (default: weighted)")
    p.add_argument("--window", type=int, default=15, help="detrend window size (default: 15)")
    p.add_argument("--footprint", type=int, default=7, help="peak footprint (default: 7)")
    p.add_argument("--w-relief", type=float, default=0.4)
    p.add_argument("--w-spectral", type=float, default=0.35)
    p.add_argument("--w-sar", type=float, default=0.25)
    p.add_argument("--low-threshold", type=float, default=0.5)
    p.add_argument("--high-threshold", type=float, default=0.75)
    p.add_argument("--site-threshold", type=float, default=0.6)
    p.add_argument("--output-dir", default="./output")
    p.add_argument("--quiet", action="store_true")
    p.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return p


def main(argv=None):
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
