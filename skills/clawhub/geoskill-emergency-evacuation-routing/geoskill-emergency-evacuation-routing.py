#!/usr/bin/env python3
"""emergency-evacuation-routing — 应急疏散路径规划

在栅格成本面上用 Dijkstra 最短路径算法规划疏散路线：

- **最短路径**：8 邻域 Dijkstra，对角移动代价 √2，按像元通行成本加权
- **灾害阻断**：危险像元设为不可通行，路径自动绕行（绝不穿过阻断区）
- **多起点 + 容量约束**：多个疏散起点按“就近优先”分配到避难所，避难所容量满后
  后续起点不再分配（或转向其他避难所）

输出疏散路线（GeoJSON LineString）、距离场（GeoTIFF）与统计（JSON）。

数据源：本地多波段 GeoTIFF（band1=通行成本、band2=危险强度→阻断），
或 ``--synthetic`` 生成含障碍物的场景。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python emergency-evacuation-routing.py --input cost.tif --threshold 1.0
    python emergency-evacuation-routing.py --bbox 116 39 117 40 --synthetic --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import heapq
import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "emergency-evacuation-routing"

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
def validate_bbox(bbox) -> None:
    """Validate geographic bbox. raise ValidationError on any structural issue."""
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            "bbox must be 4 floats [W, S, E, N]", bbox=str(bbox))
    w, s, e, n = [float(v) for v in bbox]
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError("bbox has non-finite values", bbox=bbox)
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0
            and -90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            "bbox out of WGS84 range (lon∈[-180,180], lat∈[-90,90])",
            bbox=bbox)
    if w >= e:
        raise ValidationError(
            f"bbox west ({w}) must be < east ({e}); "
            "this skill does not support anti-meridian crossing — split into two calls",
            bbox=bbox)
    if s >= n:
        raise ValidationError(
            f"bbox south ({s}) must be < north ({n})", bbox=bbox)
    span_lon = e - w
    span_lat = n - s
    if span_lon < 1e-5 or span_lat < 1e-5:
        raise ValidationError(
            f"bbox too small (lon span={span_lon:.7f}, lat span={span_lat:.7f}); "
            "both dimensions must be > 1e-5°", bbox=bbox)


def validate_cli_params(threshold: float, capacity: int) -> None:
    """CLI 参数前置校验（错误→rc=2）。"""
    if not (float(threshold) >= 0):
        raise UsageError(
            f"--threshold must be >= 0; got {threshold}", threshold=threshold)
    if int(capacity) <= 0:
        raise UsageError(
            f"--capacity must be > 0 (people per shelter); got {capacity}",
            capacity=capacity)


_NEIGH = [(-1, -1, np.sqrt(2.0)), (-1, 0, 1.0), (-1, 1, np.sqrt(2.0)),
          (0, -1, 1.0), (0, 1, 1.0),
          (1, -1, np.sqrt(2.0)), (1, 0, 1.0), (1, 1, np.sqrt(2.0))]


# ---------------------------------------------------------------------------
# 核心算法：Dijkstra 最短路径
# ---------------------------------------------------------------------------
def dijkstra(cost_grid: np.ndarray, start: Tuple[int, int],
             blocked: Optional[np.ndarray] = None) -> Tuple[np.ndarray, np.ndarray]:
    """8 邻域 Dijkstra。返回 (距离场 dist, 前驱数组 prev[H,W,2])。

    进入像元 (nr,nc) 的代价 = cost_grid[nr,nc]·步长（对角 √2）。阻断像元代价 ∞（不可达）。
    """
    H, W = cost_grid.shape
    cost = np.asarray(cost_grid, dtype=np.float64).copy()
    cost = np.where(np.isfinite(cost) & (cost > 0), cost, 1.0)  # 非法成本兜底为 1
    if blocked is not None:
        cost[np.asarray(blocked, dtype=bool)] = np.inf
    sr, sc = int(start[0]), int(start[1])
    dist = np.full((H, W), np.inf)
    prev = -np.ones((H, W, 2), dtype=np.int32)
    if not (0 <= sr < H and 0 <= sc < W):
        raise ValidationError(f"start {start} out of bounds")
    if not np.isfinite(cost[sr, sc]):
        return dist, prev  # 起点被阻断 → 全部不可达
    dist[sr, sc] = 0.0
    heap = [(0.0, sr, sc)]
    while heap:
        d, r, c = heapq.heappop(heap)
        if d > dist[r, c]:
            continue
        for dr, dc, step in _NEIGH:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < H and 0 <= nc < W):
                continue
            nd = d + cost[nr, nc] * step
            if nd < dist[nr, nc]:
                dist[nr, nc] = nd
                prev[nr, nc] = (r, c)
                heapq.heappush(heap, (nd, nr, nc))
    return dist, prev


def reconstruct_path(prev: np.ndarray, start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """由前驱数组重建 start→end 路径（像元列表）；不可达返回 None。"""
    start = (int(start[0]), int(start[1]))
    end = (int(end[0]), int(end[1]))
    if end == start:
        return [start]
    if prev[end[0], end[1], 0] < 0:
        return None
    path = [end]
    cur = end
    guard = prev.shape[0] * prev.shape[1] + 1
    while cur != start:
        p = (int(prev[cur[0], cur[1], 0]), int(prev[cur[0], cur[1], 1]))
        if p[0] < 0:
            return None
        cur = p
        path.append(cur)
        guard -= 1
        if guard <= 0:
            return None
    return path[::-1]


def shortest_path(cost_grid: np.ndarray, start: Tuple[int, int], end: Tuple[int, int],
                  blocked: Optional[np.ndarray] = None) -> Tuple[Optional[List[Tuple[int, int]]], float]:
    """最短路径 + 代价。不可达 → (None, inf)。"""
    dist, prev = dijkstra(cost_grid, start, blocked)
    path = reconstruct_path(prev, start, end)
    if path is None:
        return None, float("inf")
    return path, float(dist[end[0], end[1]])


def assign_evacuation(cost_grid: np.ndarray, origins: List[Tuple[int, int]],
                      shelters: List[Tuple[int, int]], blocked: Optional[np.ndarray] = None,
                      capacities: Optional[List[int]] = None) -> Dict[int, Dict[str, Any]]:
    """多起点就近优先疏散分配（带避难所容量约束）。

    返回 {origin_idx: {shelter, path, cost}}，未成功分配的起点不在结果中。
    """
    if not shelters:
        raise ValidationError("no shelters provided")
    if capacities is None:
        capacities = [len(origins)] * len(shelters)
    if len(capacities) != len(shelters):
        raise ValidationError("capacities length != shelters length")
    # 从每个避难所跑一次 Dijkstra（无向图，距离对称）
    shelter_dist = []
    shelter_prev = []
    for s in shelters:
        d, p = dijkstra(cost_grid, s, blocked)
        shelter_dist.append(d)
        shelter_prev.append(p)
    cands = []
    for oi, o in enumerate(origins):
        for si, s in enumerate(shelters):
            d = shelter_dist[si][o[0], o[1]]
            if np.isfinite(d):
                cands.append((float(d), oi, si))
    cands.sort(key=lambda x: x[0])
    remaining = list(capacities)
    assigned_origin = set()
    results: Dict[int, Dict[str, Any]] = {}
    for d, oi, si in cands:
        if oi in assigned_origin or remaining[si] <= 0:
            continue
        path_s2o = reconstruct_path(shelter_prev[si], shelters[si], origins[oi])
        if path_s2o is None:
            continue
        path = path_s2o[::-1]  # origin → shelter
        results[oi] = {"shelter": int(si), "path": path, "cost": float(d)}
        assigned_origin.add(oi)
        remaining[si] -= 1
    return results


# ---------------------------------------------------------------------------
# 合成数据：成本面 + 灾害阻断带 + 起点 + 避难所
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 48, height: int = 48,
                       seed: int = 42) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float64) / max(width - 1, 1)
    cost = 1.0 + 2.0 * np.abs(np.sin(2 * np.pi * xn)) + rng.uniform(0, 0.3, (height, width))
    # 一道近乎纵向的危险阻断带（中部留缺口以便通行）
    hazard = np.zeros((height, width), dtype=np.float32)
    wall_col = int(width * 0.5)
    hazard[:, wall_col - 1:wall_col + 1] = 2.0
    gap = height // 2
    hazard[gap - 2:gap + 2, wall_col - 1:wall_col + 1] = 0.0  # 缺口
    # 起点（西侧多点），避难所（东侧）
    origins = [(height // 4, width // 6), (height // 2, width // 6), (3 * height // 4, width // 6)]
    shelters = [(height // 2, 5 * width // 6)]
    layers = {"cost": cost.astype(np.float32), "hazard": hazard,
              "origins": origins, "shelters": shelters}
    info = {"bbox": bbox, "width": width, "height": height,
            "n_origins": len(origins), "n_shelters": len(shelters)}
    return layers, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0, dtype: str = "float32") -> None:
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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """Read GeoTIFF → (cube, bbox). NoData == profile.nodata 保留原值。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_with_nodata(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """Read GeoTIFF → (cube, bbox, nodata_or_None)。NoData → NaN。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=False).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None and np.isfinite(nodata):
        cube = np.where(cube == float(nodata), np.nan, cube)
    return cube, bbox, nodata


def _px_to_lonlat(rc: Tuple[int, int], bbox: List[float], H: int, W: int) -> List[float]:
    r, c = rc
    lon = bbox[0] + (c + 0.5) / W * (bbox[2] - bbox[0])
    lat = bbox[3] - (r + 0.5) / H * (bbox[3] - bbox[1])
    return [round(lon, 6), round(lat, 6)]


def write_routes_geojson(path: str, results: Dict[int, Dict[str, Any]], origins, shelters,
                         bbox: List[float], H: int, W: int) -> int:
    feats = []
    for oi, res in results.items():
        coords = [_px_to_lonlat(rc, bbox, H, W) for rc in res["path"]]
        feats.append({"type": "Feature",
                      "properties": {"origin_id": int(oi), "shelter_id": int(res["shelter"]),
                                     "cost": round(float(res["cost"]), 4),
                                     "origin": list(origins[oi]), "shelter": list(shelters[res["shelter"]])},
                      "geometry": {"type": "LineString", "coordinates": coords}})
    fc = {"type": "FeatureCollection", "features": feats}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(fc, f, ensure_ascii=False, indent=2)
    return len(feats)


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir: str, inputs: Dict[str, Any], outputs: List[Dict[str, Any]],
                   qa: Dict[str, Any], started_at: str, exit_code: int) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs=inputs, outputs=[OutputFile(**o) for o in outputs], qa=qa,
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

    # ---- 0) CLI 参数前置校验（错误→rc=2）----
    validate_cli_params(threshold=args.threshold, capacity=args.capacity)

    bbox = list(args.bbox) if args.bbox else None
    if bbox is not None:
        validate_bbox(bbox)

    src_nodata = None
    if args.input and not args.synthetic:
        cube, file_bbox, src_nodata = read_geotiff_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        validate_bbox(bbox)
        cost = cube[0]
        hazard = cube[1] if cube.shape[0] > 1 else np.zeros_like(cost)
        H, W = cost.shape
        origins = [(H // 4, W // 6), (H // 2, W // 6), (3 * H // 4, W // 6)]
        shelters = [(H // 2, 5 * W // 6)]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        layers, _info = generate_synthetic(bbox)
        cost, hazard = layers["cost"], layers["hazard"]
        origins, shelters = layers["origins"], layers["shelters"]
        source_note = "synthetic"

    H, W = cost.shape
    # NoData mask：把 NaN 的 cost 视为不可通行；把 NaN 的 hazard 视为 0（无阻断）
    cost_mask = np.isfinite(cost)
    n_valid_cost = int(cost_mask.sum())
    if n_valid_cost == 0:
        raise ValidationError(
            "input has no finite (non-NoData) pixels in cost band after NoData masking; "
            "refusing to compute paths over an empty graph",
            n_total_pixels=int(cost.size), input_nodata=src_nodata)
    safe_cost = np.where(cost_mask, cost, np.nan)
    # hazard 的 NoData 视作无阻断（保守）
    safe_hazard = np.where(np.isfinite(hazard), hazard, 0.0)

    blocked = np.asarray(safe_hazard) > args.threshold
    # 确保起点/避难所不在阻断区
    for (r, c) in origins + shelters:
        blocked[r, c] = False
    # 把 NoData 像元也当作不可通行（避免穿过 NoData 区）
    blocked = blocked | (~cost_mask)

    # 通过校验后再创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    capacities = [args.capacity] * len(shelters)
    # dijkstra 内层 `np.where(isfinite & >0, cost, 1.0)` 会把 NaN → 1.0，所以这里
    # 在外层提前把 cost 中的 NaN 置 1.0 即可（同时 blocked 矩阵已屏蔽这些像元，路径
    # 不会真的走进去）。
    safe_cost = np.nan_to_num(safe_cost, nan=1.0)
    results = assign_evacuation(safe_cost, origins, shelters, blocked=blocked, capacities=capacities)

    # 距离场（到最近避难所）
    min_dist = np.full((H, W), np.inf)
    for s in shelters:
        d, _ = dijkstra(safe_cost, s, blocked)
        min_dist = np.minimum(min_dist, d)
    min_dist[~np.isfinite(min_dist)] = -1.0
    dist_tif = os.path.join(output_dir, "distance_to_shelter.tif")
    write_geotiff(dist_tif, min_dist.astype("float32"), bbox, nodata=-1.0)

    routes_geojson = os.path.join(output_dir, "evacuation_routes.geojson")
    n_routes = write_routes_geojson(routes_geojson, results, origins, shelters, bbox, H, W)

    # 路径有效性与是否避开阻断区校验
    all_avoid = True
    for res in results.values():
        for (r, c) in res["path"]:
            if blocked[r, c]:
                all_avoid = False

    stats = {
        "source": source_note,
        "threshold": args.threshold,
        "capacity_per_shelter": args.capacity,
        "n_origins": len(origins),
        "n_shelters": len(shelters),
        "n_routes_assigned": len(results),
        "routes_avoid_hazard": bool(all_avoid),
        "route_costs": {str(k): round(float(v["cost"]), 4) for k, v in results.items()},
    }
    stats_path = os.path.join(output_dir, "routing_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_routes_assigned": len(results),
        "routes_avoid_hazard": bool(all_avoid),
        "mean_route_cost": float(np.mean([v["cost"] for v in results.values()])) if results else 0.0,
        "n_valid_cost_pixels": n_valid_cost,
        "n_total_pixels": int(cost.size),
        "valid_cost_ratio": float(n_valid_cost / cost.size) if cost.size else 0.0,
        "input_nodata": src_nodata,
    }
    outputs = [
        {"path": dist_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1, "nodata": -1.0},
        {"path": routes_geojson, "kind": "vector", "crs_epsg": 4326, "feature_count": n_routes},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, {"input": args.input, "bbox": bbox, "threshold": args.threshold,
                              "synthetic": bool(args.synthetic)}, outputs, qa, started_at, 0)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] origins: {len(origins)}  shelters: {len(shelters)}  routes: {len(results)}")
        print(f"[{SKILL_NAME}] valid cost pixels: {n_valid_cost}/{int(cost.size)} "
              f"({qa['valid_cost_ratio']:.2%})")
        print(f"[{SKILL_NAME}] routes avoid hazard: {all_avoid}")
        print(f"[{SKILL_NAME}] outputs: {output_dir}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Emergency evacuation routing (Dijkstra + hazard blockage + capacity).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoTIFF (band1=travel cost, band2=hazard intensity)")
    p.add_argument("--threshold", type=float, default=1.0, help="hazard blockage threshold (default: 1.0)")
    p.add_argument("--capacity", type=int, default=1000, help="capacity per shelter (default: 1000)")
    p.add_argument("--synthetic", action="store_true")
    p.add_argument("--output-dir", default="./output")
    p.add_argument("--quiet", action="store_true")
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
