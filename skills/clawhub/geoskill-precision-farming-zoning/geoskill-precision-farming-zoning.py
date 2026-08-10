#!/usr/bin/env python3
"""precision-farming-zoning — 精准农业管理分区

对多源农田数据层（植被长势、地形、土壤水分等）做标准化，用 K-means 聚类划分
管理分区，并依据每区特征均值给出差异化管理建议。

核心算法
--------
- **标准化**：逐层 z-score（均值 0、方差 1），消除量纲差异。
- **K-means 空间聚类**：在标准化特征空间聚成 k 个管理区。
- **分区建议**：按每区长势/水分均值生成施肥/灌溉/巡田建议。

数据源：本地多源栅格或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线，``--synthetic`` 完全无网络，本地处理不上传。

Usage:
    python precision-farming-zoning.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "precision-farming-zoning"

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, DependencyError, to_exit_code,
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

    class DependencyError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=3, kind="EDepend", **k)

    class ProcessError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=7, kind="EProcess", **k)

    def to_exit_code(exc):
        return getattr(exc, "code", 7)

    OutputManifest = None
    OutputFile = None

LAYER_NAMES = ["ndvi", "elevation", "soil_moisture"]


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
        if not (v == v):
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


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def standardize_layers(cube: np.ndarray) -> Tuple[np.ndarray, List[Dict[str, float]]]:
    """逐层 z-score 标准化，返回 (标准化 cube, 每层统计)。"""
    cube = np.asarray(cube, dtype=np.float32)
    if cube.ndim != 3:
        raise ValidationError("input cube must be (bands, H, W)")
    out = np.zeros_like(cube, dtype=np.float32)
    stats: List[Dict[str, float]] = []
    for b in range(cube.shape[0]):
        layer = cube[b]
        mu = float(np.nanmean(layer))
        sd = float(np.nanstd(layer))
        if sd < 1e-9:
            sd = 1.0  # 常值层，避免除零
        out[b] = ((layer - mu) / sd).astype(np.float32)
        stats.append({"band": b, "mean": mu, "std": float(np.nanstd(layer))})
    return out, stats


def kmeans_zone(features: np.ndarray, n_zones: int = 3, seed: int = 42) -> np.ndarray:
    """对 (H, W, F) 标准化特征做 K-means，返回 (H, W) 分区标签。"""
    try:
        from sklearn.cluster import KMeans
    except ImportError as exc:  # pragma: no cover
        raise DependencyError("scikit-learn is required for K-means zoning") from exc
    if n_zones < 1:
        raise ValidationError("n_zones must be >= 1", n_zones=int(n_zones))
    h, w = features.shape[:2]
    flat = np.nan_to_num(features.reshape(-1, features.shape[-1]), nan=0.0).astype(np.float32)
    n_unique = int(np.unique(np.round(flat, 4), axis=0).shape[0])
    k = min(n_zones, max(1, n_unique))
    km = KMeans(n_clusters=k, n_init=10, random_state=seed)
    labels = km.fit_predict(flat)
    return labels.reshape(h, w).astype(np.int32)


def zone_summary(cube: np.ndarray, labels: np.ndarray) -> List[Dict[str, Any]]:
    """每区原始特征均值汇总。"""
    cube = np.asarray(cube, dtype=np.float32)
    out: List[Dict[str, Any]] = []
    for z in sorted(np.unique(labels)):
        mask = labels == z
        means = {LAYER_NAMES[b] if b < len(LAYER_NAMES) else f"layer_{b}":
                 float(np.nanmean(cube[b][mask])) for b in range(cube.shape[0])}
        means["zone"] = int(z)
        means["pixel_count"] = int(np.sum(mask))
        out.append(means)
    return out


def zone_recommendation(summary: Dict[str, Any]) -> str:
    """依据区长势/水分均值生成管理建议。"""
    ndvi = summary.get("ndvi", 0.0)
    sm = summary.get("soil_moisture", 0.0)
    notes: List[str] = []
    if ndvi < 0.3:
        notes.append("长势偏低：增施氮肥并核查病虫害")
    elif ndvi < 0.55:
        notes.append("长势中等：维持常规施肥")
    else:
        notes.append("长势良好：可酌情减量施肥")
    if sm < 0.2:
        notes.append("土壤偏干：优先安排灌溉")
    elif sm > 0.4:
        notes.append("土壤偏湿：注意排水防涝")
    else:
        notes.append("墒情适宜：按需灌溉")
    return "；".join(notes)


def zone_management(cube: np.ndarray, n_zones: int = 3, seed: int = 42) -> Dict[str, Any]:
    """主流程：标准化 → K-means → 每区汇总与建议。

    NoData 语义：所有波段同时为有限值的像元参与聚类；任何波段为 NaN
    的像元被标记为 -1（nodata label），不计入任何 zone 的统计。
    """
    cube = np.asarray(cube, dtype=np.float32)
    if cube.ndim != 3 or cube.shape[0] < 1:
        raise ValidationError("input needs >=1 band as (bands, H, W)")
    # Per-pixel valid mask: a pixel is valid iff all bands are finite.
    finite = np.isfinite(cube).all(axis=0)
    n_valid = int(finite.sum())
    if n_valid < 1:
        raise ValidationError(
            f"need at least 1 valid (non-NoData) pixel; got {n_valid}"
        )
    std, stats = standardize_layers(cube)
    features = np.moveaxis(std, 0, -1)  # (H, W, F)
    # KMeans only over valid pixels
    h, w = features.shape[:2]
    flat_full = features.reshape(-1, features.shape[-1]).astype(np.float32)
    flat_valid = flat_full[finite.reshape(-1)]
    km = None
    try:
        from sklearn.cluster import KMeans
    except ImportError as exc:  # pragma: no cover
        raise DependencyError("scikit-learn is required for K-means zoning") from exc
    n_unique = int(np.unique(np.round(flat_valid, 4), axis=0).shape[0])
    k = min(n_zones, max(1, n_unique))
    km = KMeans(n_clusters=k, n_init=10, random_state=seed)
    valid_labels = km.fit_predict(flat_valid)
    labels = np.full(h * w, -1, dtype=np.int32)
    labels[finite.reshape(-1)] = valid_labels
    labels = labels.reshape(h, w)
    summaries = zone_summary(cube, labels)
    for s in summaries:
        s["recommendation"] = zone_recommendation(s)
    return {
        "labels": labels,
        "std_cube": std,
        "layer_stats": stats,
        "zones": summaries,
        "n_zones": int(labels.max() + 1) if labels.size else 0,
        "n_valid_pixels": n_valid,
        "n_total_pixels": int(finite.size),
    }


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 60, height: int = 60, seed: int = 42):
    """构造 3 个空间分区的多源层 [ndvi, elevation, soil_moisture]。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1)
    yy /= max(height - 1, 1)

    # 3 个分区（按 x+y 分段）
    s = xx + yy
    zone_a = (s < 0.8).astype(np.float32)   # 高产低洼湿润
    zone_b = ((s >= 0.8) & (s < 1.3)).astype(np.float32)  # 中等
    zone_c = (s >= 1.3).astype(np.float32)  # 低产高地干燥

    ndvi = zone_a * 0.72 + zone_b * 0.48 + zone_c * 0.25
    elevation = zone_a * 30.0 + zone_b * 60.0 + zone_c * 95.0
    soil_moisture = zone_a * 0.42 + zone_b * 0.28 + zone_c * 0.15

    ndvi += rng.normal(0, 0.02, ndvi.shape).astype(np.float32)
    elevation += rng.normal(0, 1.5, elevation.shape).astype(np.float32)
    soil_moisture += rng.normal(0, 0.01, soil_moisture.shape).astype(np.float32)

    cube = np.stack([np.clip(ndvi, 0, 1), elevation, np.clip(soil_moisture, 0, 1)], 0).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height, "band_order": LAYER_NAMES,
            "true_zones": 3}
    return cube, info


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
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None), "method": getattr(args, "method", None),
                "n_zones": getattr(args, "n_zones", None), "synthetic": bool(getattr(args, "synthetic", False))},
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
    os.makedirs(output_dir, exist_ok=True)
    bbox = list(args.bbox) if args.bbox else None

    # Validate CLI parameters up-front
    if not isinstance(args.n_zones, int) or args.n_zones < 1:
        raise ValidationError(
            f"--n-zones must be a positive integer >= 1 (got {args.n_zones!r}); "
            "< 1 KMeans clusters produce no usable management zones."
        )

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        # Replace NoData sentinel with NaN so z-score standardization and
        # KMeans don't see -9999 as a strong outlier / 自己的 cluster.
        import rasterio as _rio
        with _rio.open(args.input) as _src:
            _nd = _src.nodata
        if _nd is not None:
            cube = np.where(cube == _nd, np.nan, cube).astype(np.float32)
        if not np.isfinite(cube).any():
            raise ValidationError(
                f"input raster '{args.input}' contains only NoData pixels; nothing to zone"
            )
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox, source="--bbox")
        cube, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    # If --bbox is also given with --input, validate the user-supplied bbox
    if bbox is not None and args.bbox is not None:
        validate_bbox(bbox, source="--bbox")

    res = zone_management(cube, n_zones=args.n_zones)

    # Mask NoData pixels in the output raster (write as -1, a sentinel label
    # outside the valid {0, ..., n_zones-1} range).
    labels_for_write = res["labels"].astype(np.float32)
    finite = np.isfinite(cube).all(axis=0)
    labels_for_write = np.where(finite, labels_for_write, -1.0)

    zone_tif = os.path.join(output_dir, "management_zones.tif")
    write_geotiff(zone_tif, labels_for_write, bbox, nodata=-1.0)

    zones_json = os.path.join(output_dir, "zone_recommendations.json")
    with open(zones_json, "w", encoding="utf-8") as f:
        json.dump({"n_zones": res["n_zones"], "zones": res["zones"],
                   "layer_stats": res["layer_stats"]}, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "method": args.method, "n_zones": res["n_zones"],
          "zones": res["zones"],
          "n_valid_pixels": int(res.get("n_valid_pixels", 0)),
          "n_total_pixels": int(res.get("n_total_pixels", 0))}
    if synth_info is not None:
        qa["synthetic"] = synth_info

    outputs = [
        {"path": zone_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": zones_json, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] zones: {res['n_zones']}")
        for z in res["zones"]:
            print(f"  zone {z['zone']}: ndvi={z.get('ndvi', 0):.3f} -> {z['recommendation']}")
        print(f"[{SKILL_NAME}] output: {zone_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Precision farming management zoning via standardized K-means clustering.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multi-layer GeoTIFF [ndvi, elevation, soil_moisture, ...]")
    p.add_argument("--method", default="kmeans", choices=["kmeans", "equal-interval"],
                   help="zoning method (default: kmeans)")
    p.add_argument("--n-zones", dest="n_zones", type=int, default=3,
                   help="number of management zones (default: 3)")
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
