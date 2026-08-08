#!/usr/bin/env python3
"""glacier-retreat-monitoring — 冰川退缩监测

用归一化差分雪指数 NDSI=(Green−SWIR)/(Green+SWIR) 提取多期冰川范围
（NDSI>0.4 为雪/冰），把每期冰川栅格矢量化为边界多边形（shapely + geopandas），
并沿时间序列分析：

- **面积变化曲线**：每期冰川面积（像元计数 × 像元面积）。
- **末端位置变化**：用冰川质心行坐标（像元坐标系，行号随海拔降低而增大）
  代表冰川末端位置；质心行号减小说明冰川向高海拔后退。
- **退缩速率**：相邻两期之间的末端位移（米）/ 时间间隔。

输出：多期冰川边界 GeoJSON 序列、退缩速率/面积 JSON、末期冰川掩膜 GeoTIFF。

数据源：本地多波段多期 GeoTIFF（波段顺序 green/swir，按期循环 + 高程波段），
或 ``--synthetic`` 生成含冰川后退的物理一致山谷场景（离线）。

隐私声明 / Privacy：默认离线，不访问网络，所有处理本地完成。

Usage:
    python glacier-retreat-monitoring.py --input glacier.tif --n-dates 3 --output-dir ./out
    python glacier-retreat-monitoring.py --bbox 86 28 87 29 --synthetic --n-dates 3 --output-dir ./out

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
SKILL_NAME = "glacier-retreat-monitoring"

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


NDSI_THRESHOLD = 0.4         # 雪/冰判识阈值
YEARS_PER_STEP = 1.0         # 相邻期之间的时间间隔（年）


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """校验 bbox 合法性（W<=E, S<=N, 经纬度范围, 零面积）。"""
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise ValidationError(f"bbox must have 4 floats, got {bbox!r}", bbox=list(bbox))
    W_, S_, E_, N_ = (float(x) for x in bbox)
    if not (W_ <= E_ and S_ <= N_):
        raise ValidationError(
            f"invalid bbox ordering: W={W_} E={E_} S={S_} N={N_} "
            f"(require W<=E and S<=N)",
            w=W_, e=E_, s=S_, n=N_,
        )
    if not (-180.0 <= W_ <= 180.0 and -180.0 <= E_ <= 180.0):
        raise ValidationError(
            f"lon out of range [-180,180]: W={W_} E={E_}",
            w=W_, e=E_,
        )
    if not (-90.0 <= S_ <= 90.0 and -90.0 <= N_ <= 90.0):
        raise ValidationError(
            f"lat out of range [-90,90]: S={S_} N={N_}",
            s=S_, n=N_,
        )
    if (E_ - W_) <= 0.0 or (N_ - S_) <= 0.0:
        raise ValidationError(
            f"zero-area bbox: W={W_} E={E_} S={S_} N={N_}",
            w=W_, e=E_, s=S_, n=N_,
        )


def validate_params(args) -> None:
    """校验 CLI 参数值域。"""
    if args.bbox is not None:
        validate_bbox(args.bbox)
    if int(args.n_dates) < 1:
        raise UsageError(f"--n-dates must be >=1, got {args.n_dates}",
                         n_dates=int(args.n_dates))
    thr = float(args.ndsi_threshold)
    if not (-1.0 < thr < 1.0):
        raise UsageError(
            f"--ndsi-threshold must be in (-1, 1), got {thr}",
            ndsi_threshold=thr,
        )
    yrs = float(args.years_per_step)
    if yrs <= 0.0:
        raise UsageError(
            f"--years-per-step must be > 0, got {yrs}",
            years_per_step=yrs,
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def ndsi_index(green: np.ndarray, swir: np.ndarray) -> np.ndarray:
    """归一化差分雪指数 NDSI = (Green − SWIR) / (Green + SWIR)。

    NaN-safe：输入 NaN 像元 → 输出 NaN。
    """
    green = green.astype(np.float32)
    swir = swir.astype(np.float32)
    denom = green + swir
    out = np.zeros_like(denom, dtype=np.float32)
    valid = (denom != 0) & np.isfinite(green) & np.isfinite(swir)
    out[valid] = (green[valid] - swir[valid]) / denom[valid]
    return np.clip(out, -1.0, 1.0)


def glacier_mask(ndsi: np.ndarray, threshold: float = NDSI_THRESHOLD) -> np.ndarray:
    """NDSI 阈值化得到冰川/雪冰掩膜（NaN 不算冰川）。"""
    out = ndsi > threshold
    out = out & np.isfinite(ndsi)
    return out


def glacier_area_m2(mask: np.ndarray, pixel_area_m2: float) -> float:
    return float(mask.sum()) * pixel_area_m2


def terminus_row(mask: np.ndarray) -> float:
    """冰川质心行坐标（像元坐标系）。行号增大 = 向低海拔 = 前进；减小 = 退缩。

    空掩膜返回 nan。
    """
    rows, cols = np.where(mask)
    if rows.size == 0:
        return float("nan")
    return float(rows.mean())


def glacier_polygons(
    mask: np.ndarray,
    bbox: List[float],
    date_index: int,
    pixel_area_m2: float = 1.0,
) -> List[Dict[str, Any]]:
    """把单期冰川掩膜矢量化为多边形 feature 列表。

    用 matplotlib 等高线在 NDSI 二值场上提取 0.5 等值线环，转为 shapely 多边形，
    再投影到地理坐标（EPSG:4326）。返回 feature 字典列表（含 geometry 与 properties）。
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from shapely.geometry import Polygon, MultiPolygon, mapping
    from shapely.validation import make_valid

    h, w = mask.shape
    field = mask.astype(np.float32)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    cs = ax.contour(field, levels=[0.5])
    plt.close(fig)

    feats: List[Dict[str, Any]] = []
    for level in cs.allsegs:
        for seg in level:
            if len(seg) < 4:
                continue
            # 像元坐标 (col, row) -> 地理坐标
            cols = seg[:, 0]
            rows = seg[:, 1]
            lons = bbox[0] + (cols + 0.5) * (bbox[2] - bbox[0]) / w
            lats = bbox[3] - (rows + 0.5) * (bbox[3] - bbox[1]) / h
            ring = np.column_stack([lons, lats])
            poly = Polygon(ring)
            if not poly.is_valid:
                poly = make_valid(poly)
            if poly.is_empty:
                continue
            if isinstance(poly, MultiPolygon):
                geoms = list(poly.geoms)
                poly = max(geoms, key=lambda g: g.area)
            area_deg2 = float(poly.area)
            feats.append({
                "type": "Feature",
                "geometry": mapping(poly),
                "properties": {
                    "date_index": int(date_index),
                    "area_deg2": area_deg2,
                    "area_m2": float(mask.sum()) * pixel_area_m2,
                },
            })
    return feats


def analyze_retreat(
    areas: List[float],
    terminus_rows: List[float],
    pixel_size_m: float,
    years_per_step: float = YEARS_PER_STEP,
) -> Dict[str, Any]:
    """由面积序列与末端行序列计算退缩统计。

    NaN-safe：单期 mask 为空（terminus_row = NaN）的相邻期被跳过；
    total_shift 用首个/末个有效 (finite) 末期行计算。
    """
    n = len(areas)
    rates: List[Dict[str, Any]] = []
    for i in range(1, n):
        d_row = terminus_rows[i] - terminus_rows[i - 1]
        if not (np.isfinite(d_row)):
            # 任一末期行为 NaN（冰川消失/未检出）— 跳过该期
            rates.append({
                "from": i - 1, "to": i,
                "terminus_shift_m": float("nan"),
                "retreat_rate_m_per_yr": float("nan"),
                "area_change_m2": float(areas[i] - areas[i - 1]),
            })
            continue
        disp_m = d_row * pixel_size_m
        rate = disp_m / years_per_step if years_per_step > 0 else 0.0
        rates.append({
            "from": i - 1, "to": i,
            "terminus_shift_m": float(disp_m),
            "retreat_rate_m_per_yr": float(rate),
            "area_change_m2": float(areas[i] - areas[i - 1]),
        })

    # total shift：取首个/末个有限 terminus_row
    valid_rows = [t for t in terminus_rows if np.isfinite(t)]
    if len(valid_rows) >= 2:
        first_valid = next(t for t in terminus_rows if np.isfinite(t))
        last_valid = next(t for t in reversed(terminus_rows) if np.isfinite(t))
        total_shift = (last_valid - first_valid) * pixel_size_m
    elif len(valid_rows) == 1:
        total_shift = 0.0
    else:
        total_shift = float("nan")

    # retreating 判定：面积单调下降 或 末端行后移
    area_declining = areas[-1] < areas[0]
    if np.isfinite(total_shift):
        retreating = bool(total_shift < 0) or bool(area_declining)
    else:
        retreating = bool(area_declining)

    return {
        "areas_m2": [float(a) for a in areas],
        "terminus_rows": [float(t) for t in terminus_rows],
        "n_dates": n,
        "total_area_change_m2": float(areas[-1] - areas[0]),
        "total_terminus_shift_m": float(total_shift) if np.isfinite(total_shift) else 0.0,
        "retreating": bool(retreating),
        "interval_rates": rates,
    }


def pixel_size_m(bbox: List[float], height: int, width: int) -> float:
    lat0 = (bbox[1] + bbox[3]) / 2.0
    x_m = (bbox[2] - bbox[0]) * 111320.0 * np.cos(np.deg2rad(lat0)) / max(width, 1)
    y_m = (bbox[3] - bbox[1]) * 110540.0 / max(height, 1)
    return float((abs(x_m) + abs(y_m)) / 2.0)


def pixel_area_m2(bbox: List[float], height: int, width: int) -> float:
    s = pixel_size_m(bbox, height, width)
    return float(s * s)


# ---------------------------------------------------------------------------
# 合成数据：山谷冰川随期后退
# ---------------------------------------------------------------------------
def generate_synthetic_series(
    bbox: List[float],
    n_dates: int = 3,
    width: int = 128,
    height: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 (n_dates, 2, H, W) 立方体（green, swir）与高程栅格。

    地形：海拔随行号减小而升高（顶部为高处）。雪线高程随期上升，
    冰川（雪线以上区域）随之缩小并向高处后退。
    返回 (cube, elevation, info)。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yyn = yy.astype(np.float32) / max(height - 1, 1)

    # 高程：顶部高（row 0 = 3000m），底部低（row H-1 = 1000m）
    elevation = (3000.0 - 2000.0 * yyn).astype(np.float32)

    # 雪线随期上升：2000 -> 2000 + step*(n-1)
    snowlines = [2000.0 + 250.0 * k for k in range(n_dates)]

    cube = np.zeros((n_dates, 2, height, width), dtype=np.float32)
    for k in range(n_dates):
        glacier = elevation > snowlines[k]
        green = np.where(glacier, 0.80, 0.12).astype(np.float32)
        swir = np.where(glacier, 0.10, 0.35).astype(np.float32)
        green = np.clip(green + rng.normal(0, 0.01, size=green.shape).astype(np.float32), 0, 1)
        swir = np.clip(swir + rng.normal(0, 0.01, size=swir.shape).astype(np.float32), 0, 1)
        cube[k, 0] = green
        cube[k, 1] = swir

    info = {
        "bbox": bbox, "width": width, "height": height, "n_dates": n_dates,
        "snowlines": snowlines,
        "injected_snowline_rise_total_m": float(snowlines[-1] - snowlines[0]),
    }
    return cube, elevation, info


def unpack_cube(cube: np.ndarray, n_dates: int) -> Tuple[List[np.ndarray], List[np.ndarray]]:
    """把 (n_dates, 2, H, W) 立方体拆成 green 列表与 swir 列表。"""
    if cube.ndim != 4 or cube.shape[1] < 2:
        raise ValidationError(
            f"expected cube shape (n_dates, 2, H, W) with green/swir, got {cube.shape}",
            shape=str(cube.shape),
        )
    if cube.shape[0] < n_dates:
        raise ValidationError(
            f"cube has {cube.shape[0]} dates, need >= {n_dates}",
            dates=int(cube.shape[0]), n_dates=int(n_dates),
        )
    greens = [cube[k, 0].astype(np.float32) for k in range(n_dates)]
    swirs = [cube[k, 1].astype(np.float32) for k in range(n_dates)]
    return greens, swirs


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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """读 GeoTIFF（向后兼容接口）。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_safe(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """读 GeoTIFF；NoData → NaN；全 NoData 抛 ValidationError。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nd = src.nodata
    if nd is not None:
        cube = np.where(cube == float(nd), np.nan, cube)
    n_valid = int(np.isfinite(cube).sum())
    if n_valid == 0:
        raise ValidationError(
            f"input raster is entirely NoData (nodata={nd}, shape={cube.shape})",
            path=path, n_valid_pixels=0,
        )
    return cube, bbox, nd


def features_to_geodataframe(features: List[Dict[str, Any]]):
    """把 feature 字典列表构建为 geopandas.GeoDataFrame（CRS=EPSG:4326）。"""
    import geopandas as gpd
    from shapely.geometry import shape
    if not features:
        return gpd.GeoDataFrame(
            {"date_index": [], "area_m2": []}, geometry=[], crs="EPSG:4326")
    rows = [f["properties"] for f in features]
    geoms = [shape(f["geometry"]) for f in features]
    return gpd.GeoDataFrame(rows, geometry=geoms, crs="EPSG:4326")


def write_geojson(path: str, features: List[Dict[str, Any]]) -> None:
    fc = {"type": "FeatureCollection", "features": features}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(fc, f, ensure_ascii=False)


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
            "synthetic": bool(getattr(args, "synthetic", False)),
            "n_dates": int(getattr(args, "n_dates", 3)),
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

    # 1) 校验（在 makedirs 之前）
    validate_params(args)

    synth_info: Optional[Dict[str, Any]] = None
    input_nodata: Optional[float] = None
    if args.input and not args.synthetic:
        raw, file_bbox, input_nodata = read_geotiff_safe(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            validate_bbox(bbox)
        # 真实输入：3D = (n_dates*2, H, W) -> reshape to (n_dates, 2, H, W)
        if raw.ndim == 3:
            expected_bands = 2 * int(args.n_dates)
            if raw.shape[0] == expected_bands:
                h_, w_ = raw.shape[1], raw.shape[2]
                raw = raw.reshape(int(args.n_dates), 2, h_, w_)
            elif raw.shape[0] == 2 and int(args.n_dates) == 1:
                raw = raw[np.newaxis, ...]
            else:
                raise ValidationError(
                    f"input raster has {raw.shape[0]} bands, but --n-dates={args.n_dates} "
                    f"requires {expected_bands} bands (n_dates*2 green/swir) or 2 bands (single date)",
                    bands=int(raw.shape[0]), n_dates=int(args.n_dates),
                )
        greens, swirs = unpack_cube(raw, args.n_dates)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, _elev, synth_info = generate_synthetic_series(bbox, n_dates=args.n_dates)
        greens, swirs = unpack_cube(cube, args.n_dates)
        source_note = "synthetic"

    if greens[0].size == 0:
        raise ValidationError("input raster is empty")
    n_valid_total = int(sum(np.isfinite(g).sum() + np.isfinite(s).sum()
                            for g, s in zip(greens, swirs)))
    n_total = int(sum(g.size + s.size for g, s in zip(greens, swirs)))
    if n_valid_total == 0:
        raise ValidationError(
            "all input pixels are NaN/NoData — nothing to analyze",
            n_valid_pixels=0, n_total_pixels=n_total,
        )

    # 2) 校验通过后再创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    h, w = greens[0].shape
    px_area = pixel_area_m2(bbox, h, w)
    px_size = pixel_size_m(bbox, h, w)

    all_features: List[Dict[str, Any]] = []
    areas: List[float] = []
    term_rows: List[float] = []
    masks: List[np.ndarray] = []
    for k in range(len(greens)):
        ndsi = ndsi_index(greens[k], swirs[k])
        mask = glacier_mask(ndsi, args.ndsi_threshold)
        masks.append(mask)
        areas.append(glacier_area_m2(mask, px_area))
        term_rows.append(terminus_row(mask))
        feats = glacier_polygons(mask, bbox, date_index=k, pixel_area_m2=px_area)
        all_features.extend(feats)

    retreat = analyze_retreat(areas, term_rows, px_size, years_per_step=args.years_per_step)

    # 用 geopandas 汇总边界多边形
    gdf = features_to_geodataframe(all_features)
    polygon_summary = {
        "n_polygons": int(len(gdf)),
        "per_date_count": [int((gdf["date_index"] == k).sum()) for k in range(len(greens))]
        if len(gdf) else [],
    }

    # 写出
    boundary_path = os.path.join(output_dir, "glacier_boundaries.geojson")
    write_geojson(boundary_path, all_features)

    mask_tif = os.path.join(output_dir, "glacier_last.tif")
    write_geotiff(mask_tif, masks[-1].astype(np.float32), bbox)

    stats = {
        "n_dates": len(greens),
        "ndsi_threshold": args.ndsi_threshold,
        "pixel_area_m2": px_area,
        "pixel_size_m": px_size,
        "years_per_step": args.years_per_step,
        "area_curve_m2": retreat["areas_m2"],
        "terminus_rows": retreat["terminus_rows"],
        "total_area_change_m2": retreat["total_area_change_m2"],
        "total_terminus_shift_m": retreat["total_terminus_shift_m"],
        "retreating": retreat["retreating"],
        "interval_rates": retreat["interval_rates"],
        "polygon_summary": polygon_summary,
    }
    stats_path = os.path.join(output_dir, "glacier_retreat.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_dates": len(greens),
        "n_polygons": len(all_features),
        "retreating": retreat["retreating"],
        "total_terminus_shift_m": retreat["total_terminus_shift_m"],
        "total_area_change_m2": retreat["total_area_change_m2"],
        "n_valid_pixels": n_valid_total,
        "n_total_pixels": n_total,
    }
    if input_nodata is not None:
        qa["input_nodata"] = float(input_nodata)
    if synth_info is not None:
        qa["synthetic_snowline_rise_m"] = synth_info["injected_snowline_rise_total_m"]

    outputs = [
        {"path": boundary_path, "kind": "vector", "crs_epsg": 4326, "bbox_wgs84": bbox},
        {"path": mask_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] dates: {len(greens)}  polygons: {len(all_features)}")
        print(f"[{SKILL_NAME}] area curve (m2): {[round(a) for a in retreat['areas_m2']]}")
        print(f"[{SKILL_NAME}] total terminus shift: {retreat['total_terminus_shift_m']:.1f} m "
              f"({'retreat' if retreat['retreating'] else 'advance'})")
        print(f"[{SKILL_NAME}] output: {boundary_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Glacier retreat monitoring from multi-temporal NDSI boundaries.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input cube GeoTIFF (n_dates, 2=green/swir, H, W)")
    p.add_argument("--n-dates", type=int, default=3,
                   help="number of epochs (default: 3)")
    p.add_argument("--ndsi-threshold", type=float, default=NDSI_THRESHOLD,
                   help=f"NDSI glacier threshold (default: {NDSI_THRESHOLD})")
    p.add_argument("--years-per-step", type=float, default=YEARS_PER_STEP,
                   help="years between consecutive epochs (default: 1)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent valley glacier scene (offline)")
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
