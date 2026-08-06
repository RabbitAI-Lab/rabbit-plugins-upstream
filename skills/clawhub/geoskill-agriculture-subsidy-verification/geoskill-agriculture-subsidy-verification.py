#!/usr/bin/env python3
"""agriculture-subsidy-verification — 农业补贴遥感核查

用高分辨率影像做作物识别（crop/non-crop 分类），将其与申报补贴地块矢量叠加，
逐地块计算"遥感实测作物占比"与"申报作物占比"的差异，标记疑似违规地块。

核心算法
--------
- **作物识别**：对高分辨率 NDVI 栅格阈值分类得到作物掩膜（NDVI ∈ [-1,1]）。
- **地块叠加**：用 rasterio.features.rasterize 把申报地块矢量烧录到栅格网格。
- **差异检测**：逐地块统计实测作物占比（NoData 像元不参与分子/分母），
  与申报占比比较，超容差即标记（area-diff）；或做作物/非作物类别匹配
  （class-match）。无有效像元/零像元的地块记为 no-coverage，不判定违规。

数据源：本地高分辨率 NDVI 栅格 + 申报地块矢量（GeoJSON/GPKG/Shapefile），
或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线，``--synthetic`` 完全无网络，本地处理不上传。

Usage:
    python agriculture-subsidy-verification.py --bbox 116 39 117 40 --synthetic --output-dir ./out
    python agriculture-subsidy-verification.py --input ndvi.tif --parcels parcels.geojson

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import math
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "agriculture-subsidy-verification"

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


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> List[float]:
    """校验 bbox：有限、在值域内、W<=E（不支持跨 180°）、S<=N、非退化。"""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must have 4 values: W S E N")
    try:
        w, s, e, n = (float(v) for v in bbox)
    except (TypeError, ValueError):
        raise ValidationError(f"bbox values must be numeric, got {bbox!r}")
    for v, name in ((w, "W"), (s, "S"), (e, "E"), (n, "N")):
        if not math.isfinite(v):
            raise ValidationError(f"bbox {name} is not finite: {v}")
    if not (-180.0 <= w <= 180.0) or not (-180.0 <= e <= 180.0):
        raise ValidationError(f"longitude out of range [-180, 180]: W={w}, E={e}")
    if not (-90.0 <= s <= 90.0) or not (-90.0 <= n <= 90.0):
        raise ValidationError(f"latitude out of range [-90, 90]: S={s}, N={n}")
    if w > e:
        raise ValidationError(
            f"bbox crosses the antimeridian (W={w} > E={e}); "
            "this skill does not wrap around 180° — split the request into two bboxes")
    if s > n:
        raise ValidationError(f"bbox has S > N (S={s}, N={n})")
    if w == e or s == n:
        raise ValidationError(f"bbox is degenerate (zero width or height): {bbox}")
    return [w, s, e, n]


def validate_params(args: argparse.Namespace) -> None:
    """CLI 参数值域校验（越界 → ValidationError → exit 6）。"""
    if not math.isfinite(args.threshold) or not (-1.0 <= args.threshold <= 1.0):
        raise ValidationError(
            f"--threshold must be within the physical NDVI range [-1, 1], got {args.threshold}")
    if not math.isfinite(args.tolerance) or not (0.0 <= args.tolerance <= 1.0):
        raise ValidationError(f"--tolerance must be in [0, 1], got {args.tolerance}")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def classify_crop(ndvi: np.ndarray, threshold: float = 0.30) -> np.ndarray:
    """高分辨率 NDVI 阈值分类：>=threshold 为作物(1)，否则非作物(0)。"""
    ndvi = np.asarray(ndvi, dtype=np.float32)
    if ndvi.ndim != 2:
        raise ValidationError("ndvi must be 2D (H, W)")
    return (ndvi >= threshold).astype(np.uint8)


def rasterize_parcels(parcels_gdf, transform, out_shape: Tuple[int, int]) -> np.ndarray:
    """把申报地块矢量烧录为 parcel_id 栅格（背景 0，地块从 1 起编号）。"""
    try:
        from rasterio.features import rasterize
    except ImportError as exc:  # pragma: no cover
        raise DependencyError("rasterio is required for parcel rasterization") from exc
    if "parcel_id" not in parcels_gdf.columns:
        raise ValidationError("parcels must have a 'parcel_id' column")
    shapes = [(geom, int(pid)) for geom, pid in
              zip(parcels_gdf.geometry, parcels_gdf["parcel_id"])]
    grid = rasterize(shapes, out_shape=out_shape, transform=transform,
                     fill=0, dtype="int32")
    return grid.astype(np.int32)


def observed_crop_fractions(crop_mask: np.ndarray, parcel_grid: np.ndarray,
                            valid_mask: Optional[np.ndarray] = None) -> Dict[int, float]:
    """逐地块统计实测作物占比 = 地块内作物像元 / 地块内有效像元。

    NoData（valid_mask=False）像元不参与分子与分母。无有效像元的地块
    不写入返回字典（调用方按 no-coverage 处理）。
    """
    crop_mask = np.asarray(crop_mask)
    parcel_grid = np.asarray(parcel_grid)
    if crop_mask.shape != parcel_grid.shape:
        raise ValidationError("crop_mask and parcel_grid shape mismatch")
    if valid_mask is None:
        valid_mask = np.ones(crop_mask.shape, dtype=bool)
    elif valid_mask.shape != crop_mask.shape:
        raise ValidationError("valid_mask shape mismatch")
    result: Dict[int, float] = {}
    for pid in np.unique(parcel_grid):
        if pid == 0:
            continue
        mask = (parcel_grid == pid) & valid_mask
        n_px = int(np.sum(mask))
        if n_px == 0:
            continue
        result[int(pid)] = float(np.sum(crop_mask[mask] > 0) / n_px)
    return result


def verify_subsidy(parcels_gdf, observed_fracs: Dict[int, float],
                   tolerance: float = 0.15, method: str = "area-diff") -> List[Dict[str, Any]]:
    """逐地块比较申报与实测作物占比，超容差标记疑似违规。

    method:
      - "area-diff"：|observed - declared| > tolerance 即标记；
      - "class-match"：以 0.5 为界二值化为 作物/非作物 类别，类别不一致即标记。
    observed_fracs 中缺失的地块（无有效像元/零像元）记为 no-coverage，不标记。
    """
    if "declared_crop_frac" not in parcels_gdf.columns:
        raise ValidationError("parcels must have a 'declared_crop_frac' column")
    records: List[Dict[str, Any]] = []
    for _, row in parcels_gdf.iterrows():
        pid = int(row["parcel_id"])
        declared = float(row["declared_crop_frac"])
        if pid not in observed_fracs:
            records.append({
                "parcel_id": pid,
                "declared_crop_frac": round(declared, 4),
                "observed_crop_frac": None,
                "difference": None,
                "flagged": False,
                "reason": "no-coverage",
            })
            continue
        observed = float(observed_fracs[pid])
        diff = observed - declared
        if method == "class-match":
            mismatch = (declared >= 0.5) != (observed >= 0.5)
            records.append({
                "parcel_id": pid,
                "declared_crop_frac": round(declared, 4),
                "observed_crop_frac": round(observed, 4),
                "difference": round(diff, 4),
                "flagged": bool(mismatch),
                "reason": "class-mismatch" if mismatch else "consistent",
            })
        else:
            flagged = abs(diff) > tolerance
            records.append({
                "parcel_id": pid,
                "declared_crop_frac": round(declared, 4),
                "observed_crop_frac": round(observed, 4),
                "difference": round(diff, 4),
                "flagged": bool(flagged),
                "reason": ("over-declared" if diff < -tolerance else
                           "under-declared" if diff > tolerance else "consistent"),
            })
    return records


def run_verification(ndvi: np.ndarray, parcels_gdf, transform,
                     threshold: float = 0.30, tolerance: float = 0.15,
                     valid_mask: Optional[np.ndarray] = None,
                     method: str = "area-diff") -> Dict[str, Any]:
    """主流程：作物识别 → 地块叠加 → 差异检测。"""
    if valid_mask is None:
        valid_mask = np.ones(ndvi.shape, dtype=bool)
    crop_mask = classify_crop(ndvi, threshold)
    parcel_grid = rasterize_parcels(parcels_gdf, transform, out_shape=ndvi.shape)
    obs_fracs = observed_crop_fractions(crop_mask, parcel_grid, valid_mask)
    records = verify_subsidy(parcels_gdf, obs_fracs, tolerance, method=method)
    n_flag = sum(1 for r in records if r["flagged"])
    n_nocov = sum(1 for r in records if r["reason"] == "no-coverage")
    obs_vals = [r["observed_crop_frac"] for r in records if r["observed_crop_frac"] is not None]
    return {
        "crop_mask": crop_mask,
        "parcel_grid": parcel_grid,
        "records": records,
        "stats": {
            "n_parcels": len(records),
            "n_flagged": n_flag,
            "n_no_coverage": n_nocov,
            "flagged_fraction": float(n_flag / len(records)) if records else 0.0,
            "mean_observed_crop_frac": float(np.mean(obs_vals)) if obs_vals else 0.0,
            "crop_pixel_fraction": float(np.mean(crop_mask[valid_mask] > 0)) if valid_mask.any() else 0.0,
            "valid_pixel_fraction": float(valid_mask.mean()),
        },
    }


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 60, height: int = 60, seed: int = 42):
    """构造 4 个申报地块：2 个一致，1 个虚报（申报高/实测低），1 个少报。"""
    import geopandas as gpd
    from shapely.geometry import box
    from rasterio.transform import from_bounds

    rng = np.random.default_rng(seed)
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], width, height)
    px_w = (bbox[2] - bbox[0]) / width
    px_h = (bbox[3] - bbox[1]) / height
    west, south = bbox[0], bbox[1]

    # 地块布局：2x2，每个占半边
    half_w = width // 2
    half_h = height // 2
    # NDVI 真值：parcel1 作物, parcel2 作物, parcel3 裸地(非作物), parcel4 作物
    ndvi = np.full((height, width), 0.12, dtype=np.float32)  # 裸地基底
    # parcel 区域行列范围 (row:y, col:x)
    regions = {
        1: (0, half_h, 0, half_w),        # 左上
        2: (0, half_h, half_w, width),    # 右上
        3: (half_h, height, 0, half_w),   # 左下
        4: (half_h, height, half_w, width),  # 右下
    }
    true_crop = {1: 0.9, 2: 0.85, 3: 0.1, 4: 0.8}  # 实测作物占比
    declared = {1: 0.9, 2: 0.85, 3: 0.9, 4: 0.5}   # 申报占比（3 虚报, 4 少报）
    for pid, (r0, r1, c0, c1) in regions.items():
        hi = true_crop[pid] > 0.5
        base = 0.55 if hi else 0.15
        ndvi[r0:r1, c0:c1] = base + rng.normal(0, 0.03, (r1 - r0, c1 - c0)).astype(np.float32)
        # 让占比更接近目标：在区内随机置一些非作物像元
        frac = true_crop[pid]
        zone = ndvi[r0:r1, c0:c1]
        noncrop = rng.random(zone.shape) > frac
        zone[noncrop] = 0.12
        ndvi[r0:r1, c0:c1] = zone

    # 构造矢量地块（用经纬度 box）
    polys, pids, decls = [], [], []
    for pid, (r0, r1, c0, c1) in regions.items():
        x0 = west + c0 * px_w
        x1 = west + c1 * px_w
        # 行 r 对应纬度从 north 往下
        y1 = bbox[3] - r0 * px_h
        y0 = bbox[3] - r1 * px_h
        polys.append(box(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))
        pids.append(pid)
        decls.append(declared[pid])
    gdf = gpd.GeoDataFrame({"parcel_id": pids, "declared_crop_frac": decls},
                           geometry=polys, crs="EPSG:4326")
    info = {"bbox": bbox, "width": width, "height": height, "n_parcels": len(pids),
            "true_crop_frac": true_crop, "declared_crop_frac": declared}
    return ndvi.astype(np.float32), {"info": info, "parcels": gdf, "transform": transform}


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
    try:
        import rasterio
    except ImportError as exc:
        raise DependencyError(f"rasterio is required for GeoTIFF I/O: {exc}")
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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], Any]:
    try:
        import rasterio
    except ImportError as exc:
        raise DependencyError(f"rasterio is required for GeoTIFF I/O: {exc}")
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        transform = src.transform
    return cube, bbox, transform


def read_ndvi(path: str) -> Tuple[np.ndarray, List[float], Any, Optional[float], Any]:
    """读取 NDVI 栅格全量元数据：(ndvi2d, bbox, transform, nodata, crs)。"""
    try:
        import rasterio
    except ImportError as exc:
        raise DependencyError(f"rasterio is required for GeoTIFF I/O: {exc}")
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    try:
        with rasterio.open(path) as src:
            cube = src.read().astype(np.float32)
            b = src.bounds
            bbox = [b.left, b.bottom, b.right, b.top]
            transform = src.transform
            nodata = src.nodata
            crs = src.crs
    except Exception as exc:
        raise ValidationError(f"cannot read input raster '{path}': {exc}")
    if cube.ndim == 3:
        cube = cube[0]
    return cube, bbox, transform, nodata, crs


def reproject_ndvi_to_wgs84(ndvi: np.ndarray, nodata: Optional[float],
                            src_transform, src_crs) -> Tuple[np.ndarray, List[float], Any]:
    """把投影坐标系的 NDVI 重投影到 EPSG:4326（双线性），返回 (ndvi, bbox, transform)。"""
    try:
        import rasterio  # noqa: F401
    except ImportError as exc:
        raise DependencyError(f"rasterio is required for reprojection: {exc}")
    from rasterio.warp import calculate_default_transform, reproject, Resampling
    from rasterio.transform import array_bounds
    h, w = ndvi.shape
    left, bottom, right, top = array_bounds(h, w, src_transform)
    dst_transform, dst_w, dst_h = calculate_default_transform(
        src_crs, "EPSG:4326", w, h, left, bottom, right, top)
    dst = np.full((dst_h, dst_w), np.nan, dtype=np.float32)
    src = np.where(np.isnan(ndvi), nodata if nodata is not None else -9999.0, ndvi)
    reproject(
        source=src.astype(np.float32), destination=dst,
        src_transform=src_transform, src_crs=src_crs,
        dst_transform=dst_transform, dst_crs="EPSG:4326",
        src_nodata=nodata if nodata is not None else None,
        dst_nodata=float("nan"),
        resampling=Resampling.bilinear,
    )
    l2, b2, r2, t2 = array_bounds(dst_h, dst_w, dst_transform)
    return dst, [l2, b2, r2, t2], dst_transform


def load_parcels(path: str):
    """读取申报地块矢量并做结构校验，返回 EPSG:4326 的 GeoDataFrame。"""
    try:
        import geopandas as gpd
    except ImportError as exc:
        raise DependencyError(f"geopandas is required to read parcels: {exc}")
    if not os.path.exists(path):
        raise UsageError(f"parcels file not found: {path}", path=path)
    try:
        gdf = gpd.read_file(path)
    except Exception as exc:
        raise ValidationError(f"cannot read parcels file '{path}': {exc}")
    if len(gdf) == 0:
        raise ValidationError(f"parcels file '{path}' contains no features")
    if gdf.crs is None:
        raise ValidationError(
            "parcels file has no coordinate reference system (CRS) defined; "
            "cannot overlay on the NDVI raster")
    if gdf.crs.is_projected:
        gdf = gdf.to_crs("EPSG:4326")
    for col in ("parcel_id", "declared_crop_frac"):
        if col not in gdf.columns:
            raise ValidationError(f"parcels must have a '{col}' column")
    for _, row in gdf.iterrows():
        pid = row["parcel_id"]
        try:
            pid_f = float(pid)
        except (TypeError, ValueError):
            raise ValidationError(f"parcel_id must be numeric, got {pid!r}")
        if not math.isfinite(pid_f) or pid_f != int(pid_f) or int(pid_f) <= 0:
            raise ValidationError(f"parcel_id must be a positive integer, got {pid!r}")
        dec = row["declared_crop_frac"]
        try:
            dec_f = float(dec)
        except (TypeError, ValueError):
            raise ValidationError(f"declared_crop_frac must be numeric, got {dec!r}")
        if not math.isfinite(dec_f) or not (0.0 <= dec_f <= 1.0):
            raise ValidationError(
                f"declared_crop_frac must be within [0, 1] (parcel_id={pid}), got {dec!r}")
    return gdf


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
        inputs={"input": getattr(args, "input", None), "parcels": getattr(args, "parcels", None),
                "method": getattr(args, "method", None), "synthetic": bool(getattr(args, "synthetic", False))},
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

    # 参数值域校验（越界 → exit 6）
    validate_params(args)

    bbox = list(args.bbox) if args.bbox else None
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        ndvi, file_bbox, transform, nodata_in, crs = read_ndvi(args.input)
        if crs is None:
            raise ValidationError(
                "input raster has no coordinate reference system (CRS) defined; "
                "cannot georeference outputs")
        if crs.is_projected:
            ndvi, file_bbox, transform = reproject_ndvi_to_wgs84(ndvi, nodata_in, transform, crs)
        bbox = validate_bbox(bbox if bbox is not None else file_bbox)
        if not args.parcels:
            raise UsageError("--input mode requires --parcels <geojson>")
        parcels_gdf = load_parcels(args.parcels)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        ndvi, packed = generate_synthetic(bbox)
        parcels_gdf = packed["parcels"]
        transform = packed["transform"]
        synth_info = packed["info"]
        nodata_in = None
        source_note = "synthetic"

    if ndvi.size == 0:
        raise ValidationError("input raster is empty")

    # NoData / NaN 掩码：无效像元不参与分类统计
    valid = np.isfinite(ndvi)
    if nodata_in is not None:
        valid &= (ndvi != np.float32(nodata_in))
    if not valid.any():
        raise ValidationError("input NDVI raster is entirely NoData — nothing to verify")
    # NDVI 物理值域检查（按有效像元）
    vmin, vmax = float(ndvi[valid].min()), float(ndvi[valid].max())
    if vmin < -1.0 or vmax > 1.0:
        raise ValidationError(
            f"input does not look like NDVI: values [{vmin:.4g}, {vmax:.4g}] exceed the "
            "physical range [-1, 1] (is it a scaled product or a DEM?)")

    res = run_verification(ndvi, parcels_gdf, transform,
                           threshold=args.threshold, tolerance=args.tolerance,
                           valid_mask=valid, method=args.method)

    # crop_mask 输出：无效像元标记 nodata
    crop_out = res["crop_mask"].astype(np.float32)
    crop_out[~valid] = -9999.0
    crop_tif = os.path.join(output_dir, "crop_mask.tif")
    write_geotiff(crop_tif, crop_out, bbox)
    parcel_tif = os.path.join(output_dir, "parcel_grid.tif")
    write_geotiff(parcel_tif, res["parcel_grid"].astype(np.float32), bbox)

    report_json = os.path.join(output_dir, "verification_report.json")
    with open(report_json, "w", encoding="utf-8") as f:
        json.dump({"stats": res["stats"], "records": res["records"]}, f,
                  ensure_ascii=False, indent=2)

    # 差异地块矢量输出
    flagged_json = os.path.join(output_dir, "flagged_parcels.geojson")
    flagged_ids = {r["parcel_id"] for r in res["records"] if r["flagged"]}
    flagged_gdf = parcels_gdf[parcels_gdf["parcel_id"].isin(flagged_ids)].copy()
    flagged_gdf.to_file(flagged_json, driver="GeoJSON")

    qa = {"source": source_note, "method": args.method, "n_parcels": res["stats"]["n_parcels"],
          "n_flagged": res["stats"]["n_flagged"],
          "n_no_coverage": res["stats"]["n_no_coverage"],
          "flagged_fraction": res["stats"]["flagged_fraction"],
          "crop_pixel_fraction": res["stats"]["crop_pixel_fraction"],
          "valid_pixel_fraction": res["stats"]["valid_pixel_fraction"]}
    if synth_info is not None:
        qa["synthetic"] = {k: v for k, v in synth_info.items() if k != "bbox"}

    outputs = [
        {"path": crop_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": parcel_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": report_json, "kind": "json"},
        {"path": flagged_json, "kind": "vector", "crs_epsg": 4326,
         "feature_count": int(len(flagged_gdf))},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] parcels: {qa['n_parcels']}  flagged: {qa['n_flagged']} "
              f"({qa['flagged_fraction'] * 100:.1f}%)  no-coverage: {qa['n_no_coverage']}")
        for r in res["records"]:
            mark = "  !FLAG" if r["flagged"] else ""
            obs = "n/a" if r["observed_crop_frac"] is None else f"{r['observed_crop_frac']:.2f}"
            print(f"  parcel {r['parcel_id']}: declared={r['declared_crop_frac']:.2f} "
                  f"observed={obs} [{r['reason']}]{mark}")
        print(f"[{SKILL_NAME}] output: {report_json}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Agriculture subsidy verification via crop classification overlaid on declared parcels.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input high-resolution NDVI GeoTIFF (single band)")
    p.add_argument("--parcels", help="declared parcels vector (GeoJSON/GPKG/Shapefile; "
                                      "columns: parcel_id, declared_crop_frac)")
    p.add_argument("--method", default="area-diff", choices=["area-diff", "class-match"],
                   help="verification method (default: area-diff)")
    p.add_argument("--threshold", type=float, default=0.30,
                   help="NDVI crop/non-crop threshold in [-1,1] (default: 0.30)")
    p.add_argument("--tolerance", type=float, default=0.15,
                   help="allowed declared-vs-observed fraction difference in [0,1] (default: 0.15)")
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
