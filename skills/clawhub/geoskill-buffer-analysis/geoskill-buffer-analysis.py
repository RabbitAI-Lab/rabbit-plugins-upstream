#!/usr/bin/env python3
"""buffer-analysis — 缓冲区分析

对矢量要素生成缓冲区，支持多距离缓冲、缓冲融合（dissolve）、与目标层的叠加
分析，以及缓冲面积统计。地理坐标下用等距投影近似保证面积量算精度。

数据源：本地 GeoJSON，或 --synthetic 生成模拟点/线要素。

隐私声明 / Privacy：
- 默认离线运行，不发起任何网络请求。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python buffer-analysis.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "buffer-analysis"

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, DependencyError,
        to_exit_code,
    )
    from _geoskill_core.manifest import OutputManifest, OutputFile
except ImportError:  # pragma: no cover
    class GeoSkillError(Exception):
        def __init__(self, message: str, code: int = 7, kind: str = "EGeo", **kw):
            super().__init__(message)
            self.message, self.code, self.kind = message, code, kind

    class UsageError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=2, kind="EUsage", **k)

    class DependencyError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=3, kind="EDep", **k)

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
# 核心算法
# ---------------------------------------------------------------------------
def make_buffers(geoms, distance_m: float, quad_segs: int = 32):
    """平面缓冲：对每个几何生成 distance_m 宽（单位为几何坐标单位）的缓冲。

    调用方责任：地理坐标（度）几何必须先投影到局部等距平面（米）再调用本函数，
    见 _build_aeqd_transformers()；禁止在度坐标下直接按固定系数换算缓冲。
    返回 shapely 缓冲几何列表。
    """
    if distance_m <= 0:
        raise ValidationError("buffer distance must be positive")
    buffers = []
    for g in geoms:
        if g.is_empty:
            buffers.append(g)
            continue
        buffers.append(g.buffer(distance_m, quad_segs=quad_segs))
    return buffers


def dissolve_buffers(buffers) -> Any:
    """融合所有缓冲区为一个（可能 MultiPolygon）几何。"""
    from shapely.ops import unary_union
    valid = [b for b in buffers if not b.is_empty]
    if not valid:
        raise ValidationError("no non-empty buffers to dissolve")
    return unary_union(valid)


def overlay_count(buffer_geom, target_geoms) -> Tuple[int, List[int]]:
    """统计与融合缓冲区相交的目标要素数量与索引。"""
    hits = []
    for i, tg in enumerate(target_geoms):
        if tg.is_empty:
            continue
        if buffer_geom.intersects(tg):
            hits.append(i)
    return len(hits), hits


def planar_area_km2(geom, lon0: float, lat0: float) -> float:
    """把地理坐标几何投影到以 (lon0,lat0) 为中心的局部等距平面，返回面积 km²。

    使用等距圆柱近似：x = R*cos(lat0)*lon, y = R*lat（弧度）。
    """
    from shapely.ops import transform
    R = 6371000.0
    lat0r = np.deg2rad(lat0)
    coslat = np.cos(lat0r)

    def proj(lon, lat, z=None):
        x = R * coslat * np.deg2rad(np.asarray(lon))
        y = R * np.deg2rad(np.asarray(lat))
        return (x, y) if z is None else (x, y, z)

    projected = transform(proj, geom)
    return float(projected.area) / 1e6


def validate_bbox(bbox: List[float]) -> List[float]:
    """校验 bbox [W, S, E, N] 合法性；不合法抛 ValidationError（exit 6）。"""
    try:
        w, s, e, n = (float(v) for v in bbox)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox values must be numeric: {bbox}") from exc
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"bbox longitude out of range [-180, 180]: W={w}, E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"bbox latitude out of range [-90, 90]: S={s}, N={n}")
    if w > e:
        raise ValidationError(
            f"bbox W ({w}) > E ({e}); antimeridian-crossing bbox is not supported — "
            "split the request into two bboxes on either side of +/-180")
    if s > n:
        raise ValidationError(f"bbox S ({s}) > N ({n})")
    return [w, s, e, n]


def build_aeqd_transformers(lon0: float, lat0: float):
    """构建以 (lon0, lat0) 为中心的局部方位等距投影 (AEQD) 正/逆变换器。

    方位等距投影保中心点出发的距离，是米制缓冲/量算的推荐局部投影
    （Snyder 1987, USGS PP 1395；Esri Buffer 工具文档同样建议用等距类投影
    做平面缓冲）。缺 pyproj 时抛 DependencyError（exit 3）。
    """
    try:
        from pyproj import CRS, Transformer
    except ImportError as exc:
        raise DependencyError(
            "pyproj is required for metric buffering (pip install pyproj)") from exc
    wgs84 = CRS.from_epsg(4326)
    aeqd = CRS.from_proj4(
        f"+proj=aeqd +lat_0={lat0:.10f} +lon_0={lon0:.10f} +x_0=0 +y_0=0 "
        "+datum=WGS84 +units=m +no_defs")
    fwd = Transformer.from_crs(wgs84, aeqd, always_xy=True)
    inv = Transformer.from_crs(aeqd, wgs84, always_xy=True)
    return fwd, inv


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], n_sources: int = 12, n_targets: int = 60,
                       seed: int = 42) -> Tuple[Any, Any, Dict[str, Any]]:
    """生成源要素（缓冲对象）与目标点层（叠加统计）。返回 (sources_gdf, targets_gdf, info)。"""
    import geopandas as gpd
    from shapely.geometry import Point

    rng = np.random.default_rng(seed)
    w, s, e, n = bbox
    src_pts = [Point(float(rng.uniform(w, e)), float(rng.uniform(s, n))) for _ in range(n_sources)]
    sources = gpd.GeoDataFrame({"src_id": range(n_sources)}, geometry=src_pts, crs="EPSG:4326")
    tgt_pts = [Point(float(rng.uniform(w, e)), float(rng.uniform(s, n))) for _ in range(n_targets)]
    targets = gpd.GeoDataFrame({"tgt_id": range(n_targets)}, geometry=tgt_pts, crs="EPSG:4326")
    info = {"n_sources": n_sources, "n_targets": n_targets}
    return sources, targets, info


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
        inputs={"input": getattr(args, "input", None), "synthetic": bool(getattr(args, "synthetic", False))},
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
    import geopandas as gpd

    started_at = _utc_now()
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    bbox = list(args.bbox) if args.bbox else None

    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input not found: {args.input}", path=args.input)
        try:
            sources = gpd.read_file(args.input)
        except Exception as exc:
            raise ValidationError(f"cannot read input layer: {exc}", path=args.input)
        if sources.empty:
            raise ValidationError("input has no features")
        if sources.crs is None:
            raise ValidationError(
                "input has no coordinate reference system (CRS) defined; "
                "provide data with a CRS (e.g. GeoJSON is always EPSG:4326)")
        if bbox is None:
            b = sources.total_bounds
            bbox = [float(b[0]), float(b[1]), float(b[2]), float(b[3])]
        bbox = validate_bbox(bbox)
        if not sources.crs.is_geographic:
            sources = sources.to_crs(epsg=4326)
        _, targets, _ = generate_synthetic(bbox, n_sources=0, n_targets=args.n_targets)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <geojson>")
        bbox = validate_bbox(bbox)
        sources, targets, _ = generate_synthetic(bbox, n_sources=args.n_sources,
                                                  n_targets=args.n_targets)
        source_note = "synthetic"

    if sources.empty:
        raise ValidationError("empty source layer")

    # --- 米制缓冲：投影到以 bbox 中心为原点的局部等距方位投影 (AEQD)，
    # --- 在平面上以米为单位缓冲，再投回 EPSG:4326 输出。
    # --- （替代旧版 distance/110540 的度近似：该近似不做 cos(lat) 校正，
    # ---  东西向缓冲半径在中高纬系统性偏小，北京纬度约 -22%。）
    from shapely.ops import transform as _shp_transform
    lon0 = (bbox[0] + bbox[2]) / 2.0
    lat0 = (bbox[1] + bbox[3]) / 2.0
    fwd, inv = build_aeqd_transformers(lon0, lat0)
    src_proj = [_shp_transform(fwd.transform, g) for g in sources.geometry]
    buffers_proj = make_buffers(src_proj, args.distance, quad_segs=args.quad_segs)
    dissolved_proj = dissolve_buffers(buffers_proj)
    buffer_area_km2 = float(dissolved_proj.area) / 1e6  # AEQD 平面面积（米制，局部无偏）
    buffers = [_shp_transform(inv.transform, b) for b in buffers_proj]
    dissolved = _shp_transform(inv.transform, dissolved_proj)

    n_hit, hit_idx = overlay_count(dissolved, list(targets.geometry))

    out_buf = os.path.join(output_dir, "buffers.geojson")
    buf_gdf = gpd.GeoDataFrame(
        {"buffer_id": list(range(len(buffers)))},
        geometry=buffers, crs="EPSG:4326")
    buf_gdf.to_file(out_buf, driver="GeoJSON")
    out_dis = os.path.join(output_dir, "dissolved_buffer.geojson")
    gpd.GeoDataFrame({"dissolved": [1]}, geometry=[dissolved], crs="EPSG:4326").to_file(
        out_dis, driver="GeoJSON")
    stats_path = os.path.join(output_dir, "buffer_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump({"distance_m": args.distance, "n_sources": int(len(sources)),
                   "buffer_area_km2": buffer_area_km2, "n_targets_in_buffer": n_hit,
                   "n_targets_total": int(len(targets))},
                  f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "distance_m": args.distance,
          "n_sources": int(len(sources)), "buffer_area_km2": buffer_area_km2,
          "n_targets_in_buffer": n_hit}
    outputs = [
        {"path": out_buf, "kind": "vector", "crs_epsg": 4326, "bbox_wgs84": bbox},
        {"path": out_dis, "kind": "vector", "crs_epsg": 4326, "bbox_wgs84": bbox},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] buffer distance: {args.distance} m")
        print(f"[{SKILL_NAME}] dissolved buffer area: {buffer_area_km2:.4f} km²")
        print(f"[{SKILL_NAME}] targets in buffer: {n_hit}/{len(targets)}")
        print(f"[{SKILL_NAME}] output: {out_dis}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Buffer analysis: vector buffering, dissolve, overlay, and area statistics.",
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input source GeoJSON")
    p.add_argument("--distance", type=float, default=2000.0, help="buffer distance in meters (default: 2000)")
    p.add_argument("--quad-segs", type=int, default=32, help="buffer curve segments (default: 32)")
    p.add_argument("--n-sources", type=int, default=12, help="synthetic source count (default: 12)")
    p.add_argument("--n-targets", type=int, default=60, help="synthetic target count (default: 60)")
    p.add_argument("--synthetic", action="store_true", help="use synthetic data")
    p.add_argument("--output-dir", default="./output", help="output directory")
    p.add_argument("--quiet", action="store_true", help="suppress output")
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
