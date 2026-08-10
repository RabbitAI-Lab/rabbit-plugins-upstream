#!/usr/bin/env python3
"""logistics-optimization — 物流路径优化

求解物流配送中的路径优化问题，支持两种模式：

- **TSP**（旅行商问题）：最近邻启发式 + 2-opt 局部搜索，求访问所有节点并
  返回起点的最短回路。
- **VRP**（带容量车辆路径问题）：按"需求降序 + 最近可装车"贪心把客户分配到
  车辆（容量约束），每辆车内部再用 TSP 优化子回路；支持时间窗可行性检查。

距离用 Haversine（经纬度）或欧氏距离；所有坐标本地计算，不上传数据。

数据源：本地 GeoJSON 点要素（第一个点为仓库 depot，其余为客户；可用属性
``demand`` / ``tw_open`` / ``tw_close`` 指定需求与时间窗），或 ``--synthetic``
随机生成节点用于离线测试。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络；本地处理，不上传数据。

Usage:
    python logistics-optimization.py --input nodes.geojson --mode vrp --output-dir ./out
    python logistics-optimization.py --bbox 116 39 117 40 --synthetic --mode tsp --output-dir ./out

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
SKILL_NAME = "logistics-optimization"

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
# Validation helpers
# ---------------------------------------------------------------------------
def validate_bbox(bbox, allow_antimeridian: bool = False):
    """Validate geographic bbox. Returns bbox as list[float] on success.

    Cross-180° (W > E) is rejected with a hint unless ``allow_antimeridian``.
    """
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            f"bbox must be 4 floats [W S E N], got {bbox!r}")
    w, s, e, n = (float(x) for x in bbox)
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0
            and -90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox out of range (-180..180 lon, -90..90 lat): [{w}, {s}, {e}, {n}]")
    if w == e or s == n:
        raise ValidationError(
            f"bbox has zero area: W==E ({w}) or S==N ({s}); "
            f"got [{w}, {s}, {e}, {n}]")
    if s > n:
        raise ValidationError(
            f"bbox S>N (south > north): [{w}, {s}, {e}, {n}]")
    if w > e:
        if not allow_antimeridian:
            raise ValidationError(
                f"bbox crosses antimeridian (W>E: {w}>{e}); "
                f"split into two bboxes and merge results manually")
        return [w, s, e, n]
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def haversine_km(lon1, lat1, lon2, lat2) -> float:
    """两点大圆距离 (km)。"""
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2.0 * r * math.asin(min(1.0, math.sqrt(a)))


def distance_matrix(coords: np.ndarray, metric: str = "haversine") -> np.ndarray:
    """坐标 (n,2)=[lon,lat]（haversine）或 [x,y]（euclidean）的距离矩阵。"""
    coords = np.asarray(coords, dtype=np.float64)
    n = coords.shape[0]
    d = np.zeros((n, n), dtype=np.float64)
    if metric == "euclidean":
        for i in range(n):
            diff = coords - coords[i]
            d[i] = np.sqrt(np.sum(diff * diff, axis=1))
    else:
        for i in range(n):
            for j in range(i + 1, n):
                dij = haversine_km(coords[i, 0], coords[i, 1], coords[j, 0], coords[j, 1])
                d[i, j] = d[j, i] = dij
    return d


def tour_length(tour: List[int], dist: np.ndarray) -> float:
    """闭合回路总长（tour 含或不含末尾起点都支持）。"""
    total = 0.0
    for k in range(len(tour) - 1):
        total += float(dist[tour[k], tour[k + 1]])
    return total


def tsp_nearest_neighbor(dist: np.ndarray, start: int = 0) -> List[int]:
    """最近邻启发式 TSP，返回闭合回路 [start, ..., start]。"""
    n = dist.shape[0]
    if n == 0:
        return []
    if n == 1:
        return [start, start]
    unvisited = set(range(n))
    unvisited.discard(start)
    tour = [start]
    cur = start
    while unvisited:
        nxt = min(unvisited, key=lambda j: dist[cur, j])
        tour.append(nxt)
        unvisited.discard(nxt)
        cur = nxt
    tour.append(start)  # 回到起点
    return tour


def two_opt(tour: List[int], dist: np.ndarray, max_iter: int = 100) -> List[int]:
    """2-opt 局部搜索改进回路。tour 为闭合回路 [start,...,start]。"""
    if len(tour) <= 4:
        return list(tour)
    # 工作序列去掉末尾重复起点
    route = tour[:-1] if tour[0] == tour[-1] else list(tour)
    n = len(route)
    improved = True
    it = 0
    best_len = tour_length(route + [route[0]], dist)
    while improved and it < max_iter:
        improved = False
        it += 1
        for i in range(1, n - 1):
            for k in range(i + 1, n):
                a, b = route[i - 1], route[i]
                c, d = route[k], route[(k + 1) % n]
                delta = (dist[a, c] + dist[b, d]) - (dist[a, b] + dist[c, d])
                if delta < -1e-9:
                    route[i:k + 1] = reversed(route[i:k + 1])
                    improved = True
        new_len = tour_length(route + [route[0]], dist)
        if new_len < best_len - 1e-9:
            best_len = new_len
    return route + [route[0]]


def solve_tsp(dist: np.ndarray, start: int = 0, use_2opt: bool = True) -> Tuple[List[int], float]:
    """TSP：最近邻 (+2-opt)。返回 (tour, length)。"""
    tour = tsp_nearest_neighbor(dist, start)
    if use_2opt:
        tour = two_opt(tour, dist)
    return tour, tour_length(tour, dist)


def _split_vrp_customers(
    demands: np.ndarray,
    capacity: float,
    dist: np.ndarray,
) -> List[List[int]]:
    """把客户(节点1..n)按需求降序、最近可装车贪心分配到车辆。

    节点0为仓库。返回每辆车的客户索引列表（不含仓库）。
    """
    demands = np.asarray(demands, dtype=np.float64)
    n = len(demands)
    if np.any(demands > capacity + 1e-9):
        bad = int(np.argmax(demands))
        raise ValidationError(
            f"customer {bad} demand {demands[bad]} exceeds vehicle capacity {capacity}")
    order = sorted(range(1, n), key=lambda i: demands[i], reverse=True)
    vehicles: List[List[int]] = []
    loads: List[float] = []
    last_node: List[int] = []
    for c in order:
        placed = False
        # 选择可装且离该客户最近的车辆
        best_v = -1
        best_d = math.inf
        for v in range(len(vehicles)):
            if loads[v] + demands[c] <= capacity + 1e-9:
                dd = dist[last_node[v], c]
                if dd < best_d:
                    best_d = dd
                    best_v = v
        if best_v >= 0:
            vehicles[best_v].append(c)
            loads[best_v] += demands[c]
            last_node[best_v] = c
            placed = True
        if not placed:
            vehicles.append([c])
            loads.append(float(demands[c]))
            last_node.append(c)
    return vehicles


def solve_vrp(
    dist: np.ndarray,
    demands: np.ndarray,
    capacity: float,
    use_2opt: bool = True,
) -> Dict[str, Any]:
    """带容量 VRP：贪心分配 + 每车 TSP。节点0为仓库。"""
    demands = np.asarray(demands, dtype=np.float64)
    if dist.shape[0] != len(demands):
        raise ValidationError("distance matrix and demands length mismatch")
    vehicles = _split_vrp_customers(demands, capacity, dist)
    routes = []
    total_cost = 0.0
    total_demand = 0.0
    for cust in vehicles:
        if not cust:
            continue
        sub_nodes = [0] + cust
        sub_idx = {node: k for k, node in enumerate(sub_nodes)}
        sub_dist = dist[np.ix_(sub_nodes, sub_nodes)]
        sub_tour, sub_len = solve_tsp(sub_dist, start=0, use_2opt=use_2opt)
        # 映射回全局节点索引
        global_tour = [sub_nodes[i] for i in sub_tour]
        load = float(sum(demands[c] for c in cust))
        routes.append({"customers": cust, "tour": global_tour,
                       "load": load, "length": float(sub_len)})
        total_cost += sub_len
        total_demand += load
    return {"routes": routes, "n_vehicles": len(routes),
            "total_cost": float(total_cost), "total_demand": float(total_demand),
            "capacity": float(capacity)}


def check_time_windows(
    tour: List[int],
    dist: np.ndarray,
    tw_open: np.ndarray,
    tw_close: np.ndarray,
    speed: float = 40.0,
    service: float = 0.0,
) -> Tuple[bool, List[float]]:
    """沿回路检查时间窗可行性（可等待，不可迟到）。

    speed: km/h；dist 单位 km。返回 (feasible, arrival_times)。
    """
    t = 0.0
    arrivals: List[float] = []
    feasible = True
    for k in range(len(tour) - 1):
        i, j = tour[k], tour[k + 1]
        travel = float(dist[i, j]) / max(float(speed), 1e-6) * 60.0  # min
        t += travel
        open_j = float(tw_open[j])
        close_j = float(tw_close[j])
        if t > close_j + 1e-6:
            feasible = False
        if t < open_j:
            t = open_j  # 等待
        arrivals.append(t)
        t += float(service)
    return feasible, arrivals


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic_nodes(
    bbox: List[float], n_customers: int = 15, seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """随机生成仓库 + 客户节点。返回 (coords[n,2], demands[n], info)。"""
    rng = np.random.default_rng(seed)
    w, s, e, n = bbox
    depot = np.array([[0.5 * (w + e), 0.5 * (s + n)]])
    cust = np.column_stack([
        rng.uniform(w, e, n_customers),
        rng.uniform(s, n, n_customers),
    ])
    coords = np.vstack([depot, cust]).astype(np.float64)
    demands = np.concatenate([[0.0], rng.integers(1, 6, n_customers).astype(np.float64)])
    info = {"bbox": bbox, "n_nodes": int(coords.shape[0]), "n_customers": n_customers}
    return coords, demands, info


def read_nodes_geojson(path: str) -> Tuple[np.ndarray, np.ndarray, List[float]]:
    """读 GeoJSON 点要素 -> (coords, demands, bbox)。"""
    if not os.path.exists(path):
        raise UsageError(f"input geojson not found: {path}", path=path)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    feats = data.get("features", [])
    pts = [ft["geometry"]["coordinates"] for ft in feats
           if ft.get("geometry", {}).get("type") == "Point"]
    if len(pts) < 2:
        raise ValidationError("need at least 2 point features (depot + customers)")
    coords = np.array([[p[0], p[1]] for p in pts], dtype=np.float64)
    demands = []
    for ft in feats:
        if ft.get("geometry", {}).get("type") != "Point":
            continue
        demands.append(float(ft.get("properties", {}).get("demand", 1.0)))
    demands = np.array(demands, dtype=np.float64)
    lons = coords[:, 0]
    lats = coords[:, 1]
    bbox = [float(lons.min()), float(lats.min()), float(lons.max()), float(lats.max())]
    return coords, demands, bbox


def routes_to_geojson(coords: np.ndarray, routes: List[Dict[str, Any]]) -> Dict[str, Any]:
    feats = []
    for v, r in enumerate(routes):
        tour = r["tour"]
        line = [[round(float(coords[i, 0]), 6), round(float(coords[i, 1]), 6)] for i in tour]
        feats.append({"type": "Feature", "id": v,
                      "geometry": {"type": "LineString", "coordinates": line},
                      "properties": {"vehicle": v, "load": round(r["load"], 3),
                                     "length": round(r["length"], 4),
                                     "n_stops": len(r["customers"])}})
    return {"type": "FeatureCollection", "features": feats}


def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None),
                "mode": getattr(args, "mode", None),
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

    # ---- Validate bbox and params early ----
    if bbox is not None:
        bbox = validate_bbox(bbox)
    if args.mode == "vrp" and args.capacity <= 0:
        raise ValidationError(
            f"--capacity must be > 0 in VRP mode (got {args.capacity})")
    if args.n_customers < 1:
        raise ValidationError(
            f"--n-customers must be >= 1 in synthetic mode (got {args.n_customers})")

    synth_info = None
    if args.input and not args.synthetic:
        coords, demands, file_bbox = read_nodes_geojson(args.input)
        if bbox is None:
            bbox = validate_bbox(file_bbox)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <geojson>")
        coords, demands, synth_info = generate_synthetic_nodes(bbox, n_customers=args.n_customers)
        source_note = "synthetic"

    if coords.shape[0] < 2:
        # Don't create output_dir; surface clear error.
        raise ValidationError("need at least 2 nodes (depot + 1 customer)")

    # ---- Now safe to create output directory ----
    os.makedirs(output_dir, exist_ok=True)

    dist = distance_matrix(coords, metric=args.metric)

    if args.mode == "tsp":
        tour, length = solve_tsp(dist, start=0, use_2opt=not args.no_2opt)
        routes = [{"customers": tour[1:-1], "tour": tour,
                   "load": float(sum(demands[i] for i in tour[1:-1])), "length": length}]
        solution = {"mode": "tsp", "tour": tour, "total_cost": length,
                    "n_vehicles": 1, "total_demand": float(demands.sum())}
    else:  # vrp
        sol = solve_vrp(dist, demands, capacity=args.capacity, use_2opt=not args.no_2opt)
        routes = sol["routes"]
        solution = {"mode": "vrp", **sol}

    routes_gj = routes_to_geojson(coords, routes)
    routes_path = os.path.join(output_dir, "routes.geojson")
    with open(routes_path, "w", encoding="utf-8") as f:
        json.dump(routes_gj, f, ensure_ascii=False)

    # 节点
    nodes_feats = [{"type": "Feature", "id": int(i),
                    "geometry": {"type": "Point",
                                 "coordinates": [round(float(coords[i, 0]), 6), round(float(coords[i, 1]), 6)]},
                    "properties": {"node": int(i), "role": "depot" if i == 0 else "customer",
                                   "demand": float(demands[i])}}
                   for i in range(coords.shape[0])]
    nodes_path = os.path.join(output_dir, "nodes.geojson")
    with open(nodes_path, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": nodes_feats}, f, ensure_ascii=False)

    sol_path = os.path.join(output_dir, "solution.json")
    with open(sol_path, "w", encoding="utf-8") as f:
        json.dump(solution, f, ensure_ascii=False, indent=2, default=float)

    qa = {"source": source_note, "mode": args.mode,
          "n_nodes": int(coords.shape[0]),
          "n_vehicles": solution.get("n_vehicles", len(routes)),
          "total_cost": float(solution.get("total_cost", 0.0))}
    outputs = [
        {"path": routes_path, "kind": "vector", "crs_epsg": 4326, "bbox_wgs84": bbox, "feature_count": len(routes)},
        {"path": nodes_path, "kind": "vector", "crs_epsg": 4326, "bbox_wgs84": bbox, "feature_count": int(coords.shape[0])},
        {"path": sol_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mode: {args.mode}  nodes: {coords.shape[0]}  "
              f"vehicles: {solution.get('n_vehicles', 1)}")
        print(f"[{SKILL_NAME}] total cost: {solution.get('total_cost', 0.0):.3f} km")
        print(f"[{SKILL_NAME}] solution: {sol_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser():
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Logistics route optimization: TSP (NN + 2-opt) and capacitated VRP.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoJSON of point nodes (depot first)")
    p.add_argument("--synthetic", action="store_true")
    p.add_argument("--mode", default="tsp", choices=["tsp", "vrp"],
                   help="optimization mode (default: tsp)")
    p.add_argument("--metric", default="haversine", choices=["haversine", "euclidean"],
                   help="distance metric (default: haversine)")
    p.add_argument("--capacity", type=float, default=15.0, help="vehicle capacity for VRP (default: 15)")
    p.add_argument("--n-customers", type=int, default=15, help="synthetic customer count (default: 15)")
    p.add_argument("--no-2opt", action="store_true", help="disable 2-opt improvement")
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
