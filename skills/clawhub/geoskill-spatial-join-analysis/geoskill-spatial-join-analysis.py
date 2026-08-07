#!/usr/bin/env python3
"""spatial-join-analysis — 空间连接分析

对两层矢量数据执行空间连接：
- 关系判断：intersects / within / contains / nearest
- 属性聚合：按连接结果对目标层属性做 count / sum / mean 聚合

数据源：本地 GeoJSON，或 --synthetic 生成模拟点层与面层。

隐私声明 / Privacy：
- 默认离线运行，不发起任何网络请求。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python spatial-join-analysis.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "spatial-join-analysis"

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
# 校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Optional[List[float]]) -> None:
    """校验地理 bbox 合法性（W>E 视为跨 180° 不支持）。"""
    if bbox is None:
        return
    w, s, e, n = bbox
    if w > e:
        raise ValidationError(
            "invalid bbox: minLon > maxLon; crossing the 180° meridian "
            "is not supported, split the extent and run twice")
    if s > n:
        raise ValidationError("invalid bbox: minLat > maxLat")
    for lon, lat in ((w, s), (e, n)):
        if not (-180.0 <= lon <= 180.0):
            raise ValidationError(f"invalid bbox: longitude {lon} out of range [-180, 180]")
        if not (-90.0 <= lat <= 90.0):
            raise ValidationError(f"invalid bbox: latitude {lat} out of range [-90, 90]")


def validate_params(n_points: int, grid_cells: int) -> None:
    if n_points < 1:
        raise ValidationError(f"--n-points must be >= 1, got {n_points}")
    if grid_cells < 1:
        raise ValidationError(f"--grid-cells must be >= 1, got {grid_cells}")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def spatial_join(left_geoms, right_geoms, predicate: str = "intersects") -> List[Tuple[int, int]]:
    """返回满足空间关系的 (left_idx, right_idx) 配对列表。

    predicate: intersects / within / contains / crosses / touches / overlaps。
    用 shapely 的 STRtree 加速 intersects，其余逐对判断。
    """
    from shapely import STRtree
    valid = {"intersects", "within", "contains", "crosses", "touches", "overlaps"}
    if predicate not in valid:
        raise ValidationError(f"unknown predicate '{predicate}'. Choose: {sorted(valid)}")

    pairs: List[Tuple[int, int]] = []
    if predicate == "intersects":
        tree = STRtree(right_geoms)
        for i, lg in enumerate(left_geoms):
            idxs = tree.query(lg, predicate="intersects")
            for j in idxs:
                pairs.append((i, int(j)))
    else:
        for i, lg in enumerate(left_geoms):
            for j, rg in enumerate(right_geoms):
                ok = getattr(lg, predicate)(rg)
                if ok:
                    pairs.append((i, j))
    return pairs


def nearest_join(left_geoms, right_geoms) -> List[Tuple[int, int]]:
    """每个 left 几何连接到最近的 right 几何。返回 (left_idx, right_idx)。"""
    from shapely import STRtree
    tree = STRtree(right_geoms)
    pairs = []
    for i, lg in enumerate(left_geoms):
        j = tree.nearest(lg)
        pairs.append((i, int(j)))
    return pairs


def aggregate_join(pairs: List[Tuple[int, int]], values: np.ndarray,
                   n_left: int, agg: str = "sum") -> np.ndarray:
    """按 left 索引聚合 right 侧的 values。

    agg: count / sum / mean / max / min。count 统计连接次数（忽略 values）。
    未连接的 left → 0（count）或 NaN（其他）。
    """
    values = np.asarray(values, dtype=np.float64)
    out = np.full(n_left, np.nan, dtype=np.float64)
    if agg == "count":
        out = np.zeros(n_left, dtype=np.float64)
        for i, _ in pairs:
            out[i] += 1
        return out
    acc: Dict[int, List[float]] = {}
    for i, j in pairs:
        acc.setdefault(i, []).append(values[j])
    for i, lst in acc.items():
        a = np.array(lst)
        if agg == "sum":
            out[i] = a.sum()
        elif agg == "mean":
            out[i] = a.mean()
        elif agg == "max":
            out[i] = a.max()
        elif agg == "min":
            out[i] = a.min()
        else:
            raise ValidationError(f"unknown aggregation '{agg}'")
    return out


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], n_points: int = 80, grid_cells: int = 4,
                       seed: int = 42) -> Tuple[Any, Any, Dict[str, Any]]:
    """生成点层（带值）与规则网格面层。返回 (points_gdf, polys_gdf, info)。"""
    import geopandas as gpd
    from shapely.geometry import Point, box

    rng = np.random.default_rng(seed)
    w, s, e, n = bbox
    # 点层：向两个中心聚集
    pts, vals = [], []
    centers = np.array([[w + 0.3 * (e - w), s + 0.7 * (n - s)],
                        [w + 0.7 * (e - w), s + 0.3 * (n - s)]])
    for _ in range(n_points):
        c = centers[rng.integers(0, 2)]
        p = c + rng.normal(0, 0.04 * max(e - w, n - s), 2)
        pts.append(Point(float(p[0]), float(p[1])))
        vals.append(float(rng.uniform(1, 100)))
    points_gdf = gpd.GeoDataFrame({"pid": range(n_points), "value": vals},
                                  geometry=pts, crs="EPSG:4326")
    # 面层：规则网格
    polys, poly_ids = [], []
    dx = (e - w) / grid_cells
    dy = (n - s) / grid_cells
    k = 0
    for r in range(grid_cells):
        for c in range(grid_cells):
            polys.append(box(w + c * dx, s + r * dy, w + (c + 1) * dx, s + (r + 1) * dy))
            poly_ids.append(k)
            k += 1
    polys_gdf = gpd.GeoDataFrame({"zone_id": poly_ids}, geometry=polys, crs="EPSG:4326")
    info = {"n_points": n_points, "n_zones": len(polys)}
    return points_gdf, polys_gdf, info


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
    bbox = list(args.bbox) if args.bbox else None
    validate_params(args.n_points, args.grid_cells)
    validate_bbox(bbox)

    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input not found: {args.input}", path=args.input)
        try:
            points_gdf = gpd.read_file(args.input)
        except Exception as exc:  # noqa: BLE001
            raise ValidationError(
                f"failed to read input '{args.input}' (empty or corrupt?): {exc}") from exc
        if "value" not in points_gdf.columns:
            points_gdf["value"] = 1.0
        if points_gdf.crs is not None and not points_gdf.crs.is_geographic:
            points_gdf = points_gdf.to_crs(epsg=4326)
        if bbox is None:
            if len(points_gdf) == 0:
                raise ValidationError("input layer has no features")
            b = points_gdf.total_bounds
            bbox = [float(b[0]), float(b[1]), float(b[2]), float(b[3])]
            validate_bbox(bbox)
        # 面层：用输入点范围做规则网格
        _, polys_gdf, _ = generate_synthetic(bbox, n_points=0, grid_cells=args.grid_cells)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <geojson>")
        points_gdf, polys_gdf, _ = generate_synthetic(bbox, n_points=args.n_points,
                                                       grid_cells=args.grid_cells)
        source_note = "synthetic"

    if points_gdf.empty or polys_gdf.empty:
        raise ValidationError("empty input layer")

    try:
        values = points_gdf["value"].to_numpy(dtype=np.float64)
    except (ValueError, TypeError) as exc:
        raise ValidationError(
            f"column 'value' must be numeric, got: {exc}") from exc

    left_geoms = list(polys_gdf.geometry)   # 面作为 left（聚合单元）
    right_geoms = list(points_gdf.geometry)  # 点作为 right

    if args.predicate == "nearest":
        # 反向：每个点连到最近面
        pairs_pt = nearest_join(right_geoms, left_geoms)
        pairs = [(j, i) for i, j in pairs_pt]  # 转成 (zone, point)
    else:
        pairs = spatial_join(left_geoms, right_geoms, args.predicate)

    agg_vals = aggregate_join(pairs, values, len(left_geoms), args.agg)
    polys_gdf = polys_gdf.copy()
    polys_gdf["join_count"] = aggregate_join(pairs, values, len(left_geoms), "count")
    polys_gdf[f"join_{args.agg}"] = np.where(np.isnan(agg_vals), 0.0, agg_vals)

    out_epsg = points_gdf.crs.to_epsg() if hasattr(points_gdf, "crs") and points_gdf.crs is not None else 4326
    if polys_gdf.crs is None and out_epsg is not None:
        polys_gdf = polys_gdf.set_crs(epsg=out_epsg, allow_override=True)

    os.makedirs(output_dir, exist_ok=True)
    out_geojson = os.path.join(output_dir, "spatial_join.geojson")
    polys_gdf.to_file(out_geojson, driver="GeoJSON")
    stats_path = os.path.join(output_dir, "join_stats.json")
    n_matched = len({i for i, _ in pairs})
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump({"predicate": args.predicate, "agg": args.agg,
                   "n_pairs": len(pairs), "n_zones_matched": n_matched,
                   "total_value": float(values.sum()),
                   "agg_sum": float(np.nansum(agg_vals))},
                  f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "predicate": args.predicate, "agg": args.agg,
          "n_points": int(len(points_gdf)), "n_zones": int(len(polys_gdf)),
          "n_pairs": len(pairs), "n_zones_matched": n_matched}
    outputs = [
        {"path": out_geojson, "kind": "vector", "crs_epsg": out_epsg, "bbox_wgs84": bbox},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] predicate: {args.predicate}  agg: {args.agg}")
        print(f"[{SKILL_NAME}] pairs: {len(pairs)}  zones matched: {n_matched}/{len(polys_gdf)}")
        print(f"[{SKILL_NAME}] output: {out_geojson}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Spatial join: relationship predicates (intersects/within/nearest) + attribute aggregation.",
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input point GeoJSON")
    p.add_argument("--predicate", default="intersects",
                   choices=["intersects", "within", "contains", "crosses", "touches", "overlaps", "nearest"],
                   help="spatial predicate (default: intersects)")
    p.add_argument("--agg", default="sum", choices=["count", "sum", "mean", "max", "min"],
                   help="aggregation (default: sum)")
    p.add_argument("--n-points", type=int, default=80, help="synthetic point count (default: 80)")
    p.add_argument("--grid-cells", type=int, default=4, help="zone grid cells per side (default: 4)")
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
