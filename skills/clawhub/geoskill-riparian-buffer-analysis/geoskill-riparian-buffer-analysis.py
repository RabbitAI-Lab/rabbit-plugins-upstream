#!/usr/bin/env python3
"""riparian-buffer-analysis — 河岸缓冲带分析

由 DEM 提取河网（D8 汇流累积阈值法），生成多级河岸缓冲带（默认 30/50/100/200 m），
统计各缓冲带内的土地利用 / 覆盖（LULC）构成，并据此评估缓冲带完整性：

- **河网提取**：D8 汇流累积 ≥ 阈值的像元连成河道。
- **多级缓冲带**：在度量坐标系（自动 UTM）下按米缓冲，保证宽度准确。
- **LULC 统计**：植被 / 农田 / 建设用地 / 裸地 / 水体在各缓冲带内的比例。
- **完整性评估**：植被比例越高、建设用地越少，缓冲带完整性越高。

数据源：本地 DEM + LULC 栅格，或 ``--synthetic`` 生成含河道 + 植被—农田—建设
梯度的模拟场景用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python riparian-buffer-analysis.py --input dem.tif --output-dir ./out
    python riparian-buffer-analysis.py --bbox 116 39 117 40 --buffer-distances 30,50,100 --synthetic --output-dir ./out

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
SKILL_NAME = "riparian-buffer-analysis"

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


# LULC 类别定义：code -> (名称, 完整性权重)
LULC_CLASSES: Dict[int, Dict[str, Any]] = {
    1: {"name": "water", "integrity_weight": 0.0},
    2: {"name": "vegetation", "integrity_weight": 1.0},
    3: {"name": "cropland", "integrity_weight": 0.3},
    4: {"name": "built_up", "integrity_weight": -0.8},
    5: {"name": "bare", "integrity_weight": -0.2},
}


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


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
# 核心算法
# ---------------------------------------------------------------------------
def d8_flow_accumulation(dem: np.ndarray, cellsize: float = 1.0) -> np.ndarray:
    """D8 汇流累积（仅返回 acc）。"""
    dem = np.asarray(dem, dtype=np.float64)
    h, w = dem.shape
    n = h * w
    padded = np.full((h + 2, w + 2), np.nan, dtype=np.float64)
    padded[1:-1, 1:-1] = dem
    center = padded[1:-1, 1:-1]
    offsets = [
        (-1, -1, 1.4142135623730951), (-1, 0, 1.0), (-1, 1, 1.4142135623730951),
        (0, -1, 1.0), (0, 1, 1.0),
        (1, -1, 1.4142135623730951), (1, 0, 1.0), (1, 1, 1.4142135623730951),
    ]
    cs = float(cellsize) if cellsize and cellsize > 0 else 1.0
    best_drop = np.full((h, w), -np.inf, dtype=np.float64)
    best_dr = np.zeros((h, w), dtype=np.int64)
    best_dc = np.zeros((h, w), dtype=np.int64)
    best_dir = np.full((h, w), -1, dtype=np.int64)
    for idx, (dr, dc, dist) in enumerate(offsets):
        nb = padded[1 + dr:h + 1 + dr, 1 + dc:w + 1 + dc]
        drop = (center - nb) / (dist * cs)
        valid = np.isfinite(nb) & (drop > best_drop)
        best_drop = np.where(valid, drop, best_drop)
        best_dr = np.where(valid, dr, best_dr)
        best_dc = np.where(valid, dc, best_dc)
        best_dir = np.where(valid, idx, best_dir)
    no_flow = best_drop <= 0.0
    best_dir[no_flow] = -1
    rows, cols = np.indices((h, w))
    nr = np.clip(rows + best_dr, 0, h - 1)
    nc = np.clip(cols + best_dc, 0, w - 1)
    valid_flow = best_dir >= 0
    down = np.where(valid_flow, nr * w + nc, -1).astype(np.int64).ravel()
    indeg = np.zeros(n, dtype=np.int64)
    valid_idx = down[down >= 0]
    if valid_idx.size:
        indeg += np.bincount(valid_idx, minlength=n)
    acc = np.ones(n, dtype=np.float64)
    from collections import deque
    q = deque(int(i) for i in np.where(indeg == 0)[0])
    while q:
        c = q.popleft()
        d = int(down[c])
        if d >= 0:
            acc[d] += acc[c]
            indeg[d] -= 1
            if indeg[d] == 0:
                q.append(d)
    return acc.reshape(h, w)


def extract_river_mask(acc: np.ndarray, threshold: float) -> np.ndarray:
    """汇流累积 ≥ 阈值的像元为河道，返回 bool 掩膜。"""
    acc = np.asarray(acc, dtype=np.float64)
    if threshold <= 1:
        raise UsageError("river threshold must be > 1 (number of contributing cells)")
    return acc >= threshold


def river_geometry(river_mask: np.ndarray, bbox: List[float]):
    """把河道掩膜矢量化为 (合并后的) shapely 几何（EPSG:4326）。"""
    from rasterio.features import shapes
    from rasterio.transform import from_bounds
    from shapely.geometry import shape
    from shapely.ops import unary_union

    h, w = river_mask.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    mask_u8 = river_mask.astype(np.uint8)
    polys = []
    for geom, val in shapes(mask_u8, mask=mask_u8.astype(bool), transform=transform):
        polys.append(shape(geom))
    if not polys:
        return None
    return unary_union(polys)


def utm_epsg_for_bbox(bbox: List[float]) -> int:
    """由 bbox 中心估算 UTM EPSG 码（北半球 326xx / 南半球 327xx）。"""
    lon = 0.5 * (bbox[0] + bbox[2])
    lat = 0.5 * (bbox[1] + bbox[3])
    zone = int((lon + 180.0) / 6.0) + 1
    zone = max(1, min(60, zone))
    return (32600 + zone) if lat >= 0 else (32700 + zone)


def make_buffers(river_geom, distances_m: List[float], bbox: List[float]):
    """在 UTM 下对河道几何做多级缓冲，返回 {dist: gdf_4326} 与 {dist: area_m2}。"""
    import geopandas as gpd

    epsg = utm_epsg_for_bbox(bbox)
    gdf = gpd.GeoDataFrame(geometry=[river_geom], crs="EPSG:4326").to_crs(epsg=epsg)
    buffers_4326: Dict[float, Any] = {}
    areas_m2: Dict[float, float] = {}
    for d in distances_m:
        buf_metric = gdf.geometry.buffer(float(d))
        area = float(buf_metric.area.sum())
        gdf_metric = gpd.GeoDataFrame(geometry=buf_metric.values, crs=f"EPSG:{epsg}")
        buffers_4326[float(d)] = gdf_metric.to_crs(epsg=4326)
        areas_m2[float(d)] = area
    return buffers_4326, areas_m2, epsg


def rasterize_mask(buffer_gdf, shape: Tuple[int, int], transform) -> np.ndarray:
    """把缓冲带多边形栅格化到 LULC 网格，返回 0/1 掩膜。"""
    from rasterio.features import rasterize

    geoms = [(g, 1) for g in buffer_gdf.geometry.values if g is not None and not g.is_empty]
    if not geoms:
        return np.zeros(shape, dtype=np.uint8)
    out = rasterize(geoms, out_shape=shape, transform=transform, fill=0, dtype="uint8")
    return out


def lulc_stats_in_buffer(
    lulc: np.ndarray, buffer_gdf, bbox: List[float]
) -> Dict[str, Any]:
    """统计缓冲带内各 LULC 类别的像元数与比例。"""
    from rasterio.transform import from_bounds

    lulc = np.asarray(lulc)
    h, w = lulc.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    mask = rasterize_mask(buffer_gdf, (h, w), transform).astype(bool)
    inside = lulc[mask]
    total = int(inside.size)
    counts: Dict[str, int] = {}
    fracs: Dict[str, float] = {}
    for code, meta in LULC_CLASSES.items():
        c = int(np.sum(inside == code))
        counts[meta["name"]] = c
        fracs[meta["name"]] = round(c / total, 4) if total else 0.0
    # 未定义类别归入 other
    known = set(LULC_CLASSES.keys())
    other = int(np.sum(~np.isin(inside, list(known)))) if total else 0
    counts["other"] = other
    fracs["other"] = round(other / total, 4) if total else 0.0
    return {"cell_count": total, "counts": counts, "fractions": fracs}


def integrity_score(fracs: Dict[str, float]) -> Tuple[float, str]:
    """由 LULC 比例计算缓冲带完整性评分（0-1）与等级。

    评分 = Σ(weight_i · frac_i)，排除水体后裁剪到 [0,1]。
    等级：high ≥0.6，medium ≥0.3，否则 low。
    """
    water = fracs.get("water", 0.0)
    land = 1.0 - water
    score = 0.0
    if land > 1e-6:
        for code, meta in LULC_CLASSES.items():
            if meta["name"] == "water":
                continue
            f = fracs.get(meta["name"], 0.0) / land
            score += meta["integrity_weight"] * f
    score = float(np.clip(score, 0.0, 1.0))
    if score >= 0.6:
        level = "high"
    elif score >= 0.3:
        level = "medium"
    else:
        level = "low"
    return round(score, 4), level


def analyze_buffers(
    lulc: np.ndarray, buffers_4326: Dict[float, Any], areas_m2: Dict[float, float],
    bbox: List[float],
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """对每个缓冲带做 LULC 统计 + 完整性评估，返回 (stats_list, geojson_features)。"""
    stats_list: List[Dict[str, Any]] = []
    feats: List[Dict[str, Any]] = []
    for d in sorted(buffers_4326.keys()):
        gdf = buffers_4326[d]
        stats = lulc_stats_in_buffer(lulc, gdf, bbox)
        score, level = integrity_score(stats["fractions"])
        entry = {
            "buffer_distance_m": float(d),
            "area_m2": round(areas_m2[d], 1),
            "cell_count": stats["cell_count"],
            "fractions": stats["fractions"],
            "counts": stats["counts"],
            "integrity_score": score,
            "integrity_level": level,
        }
        stats_list.append(entry)
        # 每个缓冲带一个 feature
        for geom in gdf.geometry.values:
            if geom is None or geom.is_empty:
                continue
            from shapely.geometry import mapping
            feats.append({
                "type": "Feature",
                "geometry": mapping(geom),
                "properties": {
                    "buffer_distance_m": float(d),
                    "area_m2": round(areas_m2[d], 1),
                    "integrity_score": score,
                    "integrity_level": level,
                    "vegetation_fraction": stats["fractions"].get("vegetation", 0.0),
                },
            })
    return stats_list, feats


# ---------------------------------------------------------------------------
# 合成数据：含河道 + LULC 梯度的模拟场景（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float], width: int = 96, height: int = 96, seed: int = 42,
) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    """生成含中部河道 + 沿岸植被—农田—建设梯度的合成流域。

    layers: dem / lulc。LULC 编码见 LULC_CLASSES。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yn = yy.astype(np.float64) / max(height - 1, 1)
    xn = xx.astype(np.float64) / max(width - 1, 1)

    # DEM：南北向出口坡 + 强东西向 V 形谷，使全流域汇流到中部单一主干河道
    base = (1.0 - yn) * 25.0                 # 向南出口
    valley = 150.0 * np.abs(xn - 0.5)        # 两侧高、中部低，汇流到中轴
    dem = (200.0 + base + valley + rng.normal(0, 0.05, (height, width))).astype(np.float32)

    # LULC：河道（水）→ 沿岸植被 → 农田 → 外围建设
    dist = np.abs(xn - 0.5)
    lulc = np.full((height, width), 3, dtype=np.int32)  # 默认农田
    lulc[dist < 0.04] = 1      # 河道水体
    lulc[(dist >= 0.04) & (dist < 0.16)] = 2  # 沿岸植被
    lulc[(dist >= 0.16) & (dist < 0.34)] = 3  # 农田
    lulc[dist >= 0.34] = 4     # 外围建设用地
    # 少量裸地噪声
    bare = rng.random((height, width)) < 0.02
    lulc[bare & (dist >= 0.16)] = 5

    lat0 = 0.5 * (bbox[1] + bbox[3])
    dx = (bbox[2] - bbox[0]) * 111320.0 * np.cos(np.deg2rad(lat0)) / width
    dy = (bbox[3] - bbox[1]) * 110540.0 / height
    cellsize_m = float(0.5 * (dx + dy))

    layers = {"dem": dem, "lulc": lulc}
    info = {"bbox": bbox, "width": width, "height": height, "cellsize_m": cellsize_m}
    return layers, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0
) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if array.ndim == 2:
        array = array[np.newaxis, ...]
    nb, h, w = array.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(array[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], float]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        h, w = cube.shape[-2], cube.shape[-1]
        lat0 = 0.5 * (b.bottom + b.top)
        dx = (b.right - b.left) * 111320.0 * np.cos(np.deg2rad(lat0)) / w
        dy = (b.top - b.bottom) * 110540.0 / h
        cellsize_m = float(0.5 * (dx + dy))
    return cube, bbox, cellsize_m


# ---------------------------------------------------------------------------
# 主管线
# ---------------------------------------------------------------------------
def run_model(
    dem: np.ndarray, lulc: np.ndarray, cellsize_m: float, bbox: List[float],
    river_threshold: float, buffer_distances: List[float],
) -> Dict[str, Any]:
    """提取河网 → 多级缓冲 → LULC 统计 → 完整性评估。"""
    acc = d8_flow_accumulation(dem, cellsize_m)
    river_mask = extract_river_mask(acc, river_threshold)
    n_river_cells = int(np.sum(river_mask))
    if n_river_cells == 0:
        raise ValidationError(
            "no river cells found; lower --river-threshold",
            threshold=float(river_threshold),
        )
    river_geom = river_geometry(river_mask, bbox)
    if river_geom is None:
        raise ProcessError("failed to vectorize river network")

    buffers_4326, areas_m2, epsg = make_buffers(river_geom, buffer_distances, bbox)
    stats_list, feats = analyze_buffers(lulc, buffers_4326, areas_m2, bbox)

    # 面积随距离单调不减
    areas_sorted = [areas_m2[d] for d in sorted(areas_m2.keys())]
    monotonic = all(areas_sorted[i] <= areas_sorted[i + 1] + 1e-6
                    for i in range(len(areas_sorted) - 1))

    return {
        "cellsize_m": cellsize_m,
        "utm_epsg": epsg,
        "n_river_cells": n_river_cells,
        "river_threshold": float(river_threshold),
        "buffer_distances_m": sorted(float(d) for d in buffer_distances),
        "buffers": stats_list,
        "features": feats,
        "river_geom": river_geom,
        "area_monotonic": bool(monotonic),
    }


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(
    output_dir: str, args: argparse.Namespace, outputs: List[Dict[str, Any]],
    qa: Dict[str, Any], started_at: str, exit_code: int, bbox: List[float],
) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "bbox": bbox,
            "synthetic": bool(getattr(args, "synthetic", False)),
            "buffer_distances": getattr(args, "buffer_distances", None),
            "river_threshold": getattr(args, "river_threshold", None),
        },
        outputs=[OutputFile(**o) for o in outputs],
        qa=qa,
        software={"python": sys.version.split()[0], "skill": SKILL_NAME},
    )
    path = os.path.join(output_dir, "output-manifest.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(man.to_dict(), f, ensure_ascii=False, indent=2, default=str)
    return path


def _parse_distances(s: str) -> List[float]:
    try:
        vals = [float(x) for x in str(s).split(",") if x.strip()]
    except ValueError:
        raise UsageError(f"invalid --buffer-distances '{s}', use e.g. 30,50,100")
    if not vals:
        raise UsageError("--buffer-distances must contain at least one value")
    if any(v <= 0 for v in vals):
        raise UsageError("buffer distances must be positive")
    return vals


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    bbox = list(args.bbox) if args.bbox else None
    buffer_distances = _parse_distances(args.buffer_distances)

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox, cellsize_m = read_geotiff(args.input)
        if bbox is not None:
            validate_bbox(bbox)
        else:
            validate_bbox(file_bbox)
            bbox = file_bbox
        dem = cube[0] if cube.ndim == 3 else cube
        h, w = dem.shape
        layers, synth_info = generate_synthetic(bbox, width=w, height=h)
        layers["dem"] = dem.astype(np.float32)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        layers, synth_info = generate_synthetic(bbox, width=args.width, height=args.height)
        cellsize_m = synth_info["cellsize_m"]
        source_note = "synthetic"

    if layers["dem"].size == 0:
        raise ValidationError("input raster is empty")

    try:
        result = run_model(
            layers["dem"], layers["lulc"], cellsize_m, bbox,
            river_threshold=args.river_threshold,
            buffer_distances=buffer_distances,
        )
    except GeoSkillError:
        raise
    except Exception as exc:  # noqa: BLE001
        raise ProcessError(f"riparian buffer analysis failed: {exc}") from exc

    # 写出产物
    from shapely.geometry import mapping

    river_geojson = os.path.join(output_dir, "river_network.geojson")
    with open(river_geojson, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": [{
            "type": "Feature",
            "geometry": mapping(result["river_geom"]),
            "properties": {"n_river_cells": result["n_river_cells"]},
        }]}, f, ensure_ascii=False, indent=2)

    buffers_geojson = os.path.join(output_dir, "buffers.geojson")
    with open(buffers_geojson, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": result["features"]},
                  f, ensure_ascii=False, indent=2)

    lulc_stats_path = os.path.join(output_dir, "lulc_stats.json")
    with open(lulc_stats_path, "w", encoding="utf-8") as f:
        json.dump({"buffers": result["buffers"]}, f, ensure_ascii=False, indent=2)

    integrity_path = os.path.join(output_dir, "integrity_assessment.json")
    integrity_payload = {
        "cellsize_m": result["cellsize_m"],
        "utm_epsg": result["utm_epsg"],
        "river_threshold": result["river_threshold"],
        "n_river_cells": result["n_river_cells"],
        "area_monotonic": result["area_monotonic"],
        "buffers": [{
            "buffer_distance_m": b["buffer_distance_m"],
            "area_m2": b["area_m2"],
            "integrity_score": b["integrity_score"],
            "integrity_level": b["integrity_level"],
            "vegetation_fraction": b["fractions"].get("vegetation", 0.0),
            "built_up_fraction": b["fractions"].get("built_up", 0.0),
        } for b in result["buffers"]],
    }
    with open(integrity_path, "w", encoding="utf-8") as f:
        json.dump(integrity_payload, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_river_cells": result["n_river_cells"],
        "n_buffers": len(result["buffers"]),
        "buffer_distances_m": result["buffer_distances_m"],
        "area_monotonic": result["area_monotonic"],
        "integrity_scores": [b["integrity_score"] for b in result["buffers"]],
        "n_buffer_features": len(result["features"]),
    }

    outputs = [
        {"path": river_geojson, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": 1},
        {"path": buffers_geojson, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": len(result["features"])},
        {"path": lulc_stats_path, "kind": "json"},
        {"path": integrity_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] river cells: {result['n_river_cells']}  UTM EPSG:{result['utm_epsg']}")
        for b in result["buffers"]:
            print(f"[{SKILL_NAME}]   buffer {b['buffer_distance_m']:>6.0f} m: "
                  f"area={b['area_m2']:.0f} m²  veg={b['fractions'].get('vegetation',0):.2f}  "
                  f"integrity={b['integrity_score']:.2f} ({b['integrity_level']})")
        print(f"[{SKILL_NAME}] area monotonic with distance: {result['area_monotonic']}")
        print(f"[{SKILL_NAME}] output: {buffers_geojson}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Riparian buffer delineation from DEM-derived river network with LULC stats and integrity assessment.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input DEM GeoTIFF (band 1 as elevation)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic watershed with river + LULC (offline)")
    p.add_argument("--width", type=int, default=96, help="synthetic raster width (default 96)")
    p.add_argument("--height", type=int, default=96, help="synthetic raster height (default 96)")
    p.add_argument("--buffer-distances", default="30,50,100,200",
                   help="comma-separated buffer distances in meters (default 30,50,100,200)")
    p.add_argument("--river-threshold", type=float, default=50.0,
                   help="flow-accumulation threshold for river extraction (default 50)")
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
