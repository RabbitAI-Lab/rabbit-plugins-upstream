#!/usr/bin/env python3
"""network-routing — 网络路径规划

在网络图上做路径规划，支持 Dijkstra 与 A*（启发式）两种算法，以及按距离或
时间加权的多约束路径。支持多起终点批量规划，输出每条路径的 GeoJSON 与汇总统计。

数据源：本地网络 GeoJSON，或 --synthetic 生成模拟格网路网。

隐私声明 / Privacy：
- 默认离线运行，不发起任何网络请求。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python network-routing.py --bbox 116 39 117 40 --synthetic --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import heapq
import json
import math
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "network-routing"

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
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float], source: str = "bbox") -> None:
    """校验 EPSG:4326 经纬度 bbox：W<=E、S<=N、超经纬度→ValidationError(6)。
    跨 180° 经线（|E-W| > 360）→ValidationError 并附"拆分为两侧"提示。
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(
            f"{source} must be [W, S, E, N] with 4 floats, got {bbox!r}",
            bbox=bbox,
        )
    w, s, e, n = bbox
    if not all(isinstance(v, (int, float)) and np.isfinite(v) for v in (w, s, e, n)):
        raise ValidationError(
            f"{source} contains non-finite values: {bbox!r}", bbox=bbox,
        )
    # 超经纬度
    if w < -180.0 or e > 180.0 or s < -90.0 or n > 90.0:
        raise ValidationError(
            f"{source} out of WGS-84 range (lon∈[-180,180], lat∈[-90,90]): {bbox!r}",
            bbox=bbox,
        )
    # W>E（包含跨180°与同经度颠倒）
    if w > e:
        gap = e - w  # 负数
        if abs(gap) > 360.0:
            raise ValidationError(
                f"{source} span exceeds 360°: {bbox!r}", bbox=bbox,
            )
        raise ValidationError(
            f"{source} has W>E ({w} > {e}); cross-dateline not supported. "
            f"Split into two bboxes (e.g. [{w}, {s}, 180, {n}] and [-180, {s}, {e}, {n}]) "
            f"and run separately.",
            bbox=bbox,
        )
    if s > n:
        raise ValidationError(
            f"{source} has S>N ({s} > {n}); latitude must increase northward", bbox=bbox,
        )
    # 经纬度宽度过小
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"{source} too small (Δlon={e - w}, Δlat={n - s}); must be > 1e-9 degrees",
            bbox=bbox,
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def build_graph(coords: np.ndarray, edges: List[Tuple[int, int, float, float]]):
    """构建邻接表。edges: (u, v, distance, time)。

    Returns (adj_dist, adj_time)。
    """
    n = coords.shape[0]
    adj_dist: List[List[Tuple[int, float]]] = [[] for _ in range(n)]
    adj_time: List[List[Tuple[int, float]]] = [[] for _ in range(n)]
    for u, v, dist, time in edges:
        if u < 0 or u >= n or v < 0 or v >= n:
            raise ValidationError(f"edge ({u},{v}) references invalid node (n={n})")
        if dist < 0 or time < 0:
            raise ValidationError(f"edge ({u},{v}) has negative weight")
        adj_dist[u].append((v, dist))
        adj_dist[v].append((u, dist))
        adj_time[u].append((v, time))
        adj_time[v].append((u, time))
    return adj_dist, adj_time


def dijkstra_path(adj: List[List[Tuple[int, float]]], source: int,
                  target: int) -> Tuple[List[int], float]:
    """Dijkstra 最短路径。返回 (node_path, cost)。不可达返回 ([], inf)。"""
    n = len(adj)
    if not (0 <= source < n and 0 <= target < n):
        raise ValidationError("source/target out of range")
    dist = np.full(n, np.inf)
    prev = np.full(n, -1, dtype=np.int64)
    dist[source] = 0.0
    heap = [(0.0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        if u == target:
            break
        for v, wgt in adj[u]:
            nd = d + wgt
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))
    if not np.isfinite(dist[target]):
        return [], float("inf")
    return _reconstruct(prev, source, target), float(dist[target])


def astar_path(adj: List[List[Tuple[int, float]]], coords: np.ndarray,
               source: int, target: int,
               heuristic_scale: float = 1.0) -> Tuple[List[int], float]:
    """A* 最短路径，启发式 = 欧氏距离 * heuristic_scale（需可采纳：scale≤边权/距离下界）。

    返回 (node_path, cost)。
    """
    n = len(adj)
    if not (0 <= source < n and 0 <= target < n):
        raise ValidationError("source/target out of range")
    tcoord = coords[target]
    g = np.full(n, np.inf)
    prev = np.full(n, -1, dtype=np.int64)
    g[source] = 0.0
    h0 = heuristic_scale * float(np.linalg.norm(coords[source] - tcoord))
    heap = [(h0, 0.0, source)]
    closed = np.zeros(n, dtype=bool)
    while heap:
        f, gval, u = heapq.heappop(heap)
        if closed[u]:
            continue
        closed[u] = True
        if u == target:
            break
        for v, wgt in adj[u]:
            if closed[v]:
                continue
            ng = gval + wgt
            if ng < g[v]:
                g[v] = ng
                prev[v] = u
                h = heuristic_scale * float(np.linalg.norm(coords[v] - tcoord))
                heapq.heappush(heap, (ng + h, ng, v))
    if not np.isfinite(g[target]):
        return [], float("inf")
    return _reconstruct(prev, source, target), float(g[target])


def _reconstruct(prev: np.ndarray, source: int, target: int) -> List[int]:
    path = [target]
    cur = target
    guard = 0
    while cur != source:
        cur = int(prev[cur])
        if cur < 0:
            return []
        path.append(cur)
        guard += 1
        if guard > prev.size + 5:
            break
    path.reverse()
    return path


def admissible_heuristic_scale(coords: np.ndarray,
                               edges: List[Tuple[int, int, float, float]],
                               weight: str) -> float:
    """计算保证 A* 可采纳的启发式缩放系数。

    h(n) = scale * 欧氏距离(n, target) 必须不高估真实代价。
    真实最小代价下界 = sum(边权) ≥ scale_min * sum(欧氏边长) ≥ scale_min * 直线欧氏距离，
    其中 scale_min = min_edges(边权 / 欧氏边长)。取该下界即可采纳。
    """
    idx = 2 if weight == "distance" else 3
    ratios = []
    for edge in edges:
        u, v = edge[0], edge[1]
        euclid = float(np.linalg.norm(coords[u] - coords[v]))
        wgt = float(edge[idx])
        if euclid > 1e-12:
            ratios.append(wgt / euclid)
    if not ratios:
        return 0.0
    return max(min(ratios), 0.0)


def route_od(coords: np.ndarray, adj_dist, adj_time,
             od_pairs: List[Tuple[int, int]], weight: str = "distance",
             algorithm: str = "dijkstra",
             heuristic_scale: float = 1.0) -> List[Dict[str, Any]]:
    """批量起终点路径规划。"""
    adj = adj_dist if weight == "distance" else adj_time
    results = []
    for source, target in od_pairs:
        if algorithm == "astar":
            path, cost = astar_path(adj, coords, source, target,
                                    heuristic_scale=heuristic_scale)
        else:
            path, cost = dijkstra_path(adj, source, target)
        results.append({"source": int(source), "target": int(target),
                        "cost": cost, "n_nodes": len(path), "path": path,
                        "reachable": len(path) > 0})
    return results


# ---------------------------------------------------------------------------
# 合成路网
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], grid_n: int = 12, speed: float = 1.0,
                       seed: int = 42) -> Tuple[np.ndarray, List[Tuple[int, int, float, float]], Dict[str, Any]]:
    """生成格网路网。边含 distance（欧氏）与 time（distance/speed，主干更快）。

    Returns (coords, edges[(u,v,dist,time)], info)。
    """
    rng = np.random.default_rng(seed)
    w, s, e, n = bbox
    xs = np.linspace(w, e, grid_n)
    ys = np.linspace(n, s, grid_n)
    gx, gy = np.meshgrid(xs, ys)
    coords = np.column_stack([gx.ravel(), gy.ravel()])
    coords += rng.normal(0, 0.0005, coords.shape)
    N = coords.shape[0]
    edges: List[Tuple[int, int, float, float]] = []
    for r in range(grid_n):
        for c in range(grid_n):
            i = r * grid_n + c
            if c < grid_n - 1:
                j = i + 1
                d = float(np.linalg.norm(coords[i] - coords[j]))
                # 横向主干道更快
                t = d / (speed * 2.0) if r == grid_n // 2 else d / speed
                edges.append((i, j, d, t))
            if r < grid_n - 1:
                j = i + grid_n
                d = float(np.linalg.norm(coords[i] - coords[j]))
                t = d / speed
                edges.append((i, j, d, t))
    info = {"n_nodes": N, "n_edges": len(edges), "grid_n": grid_n}
    return coords, edges, info


# ---------------------------------------------------------------------------
# 输出 / Manifest
# ---------------------------------------------------------------------------
def write_routes_geojson(path: str, coords: np.ndarray, results: List[Dict[str, Any]],
                         weight: str, algorithm: str) -> None:
    feats = []
    for i, res in enumerate(results):
        line = [[float(coords[nid, 0]), float(coords[nid, 1])] for nid in res["path"]]
        geom = {"type": "LineString", "coordinates": line} if len(line) >= 2 else {"type": "Point", "coordinates": line[0] if line else [0, 0]}
        feats.append({
            "type": "Feature",
            "properties": {"route_id": i, "source": res["source"], "target": res["target"],
                           "cost": (None if not math.isfinite(res["cost"]) else res["cost"]),
                           "weight": weight, "algorithm": algorithm,
                           "n_nodes": res["n_nodes"], "reachable": res["reachable"]},
            "geometry": geom,
        })
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": feats}, f, ensure_ascii=False, indent=2)


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
    started_at = _utc_now()
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    bbox = list(args.bbox) if args.bbox else None

    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input not found: {args.input}", path=args.input)
        with open(args.input, encoding="utf-8") as f:
            net = json.load(f)
        coords, edges, n_nodes = _parse_network(net)
        if bbox is None:
            bbox = [float(coords[:, 0].min()), float(coords[:, 1].min()),
                    float(coords[:, 0].max()), float(coords[:, 1].max())]
        # 派生出的 bbox 仍要校验（可能输入数据本身就越界/颠倒）
        validate_bbox(bbox, source="derived bbox from --input")
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <geojson>")
        validate_bbox(bbox, source="--bbox")
        coords, edges, _ = generate_synthetic(bbox, grid_n=args.grid_n, speed=args.speed)
        n_nodes = coords.shape[0]
        source_note = "synthetic"

    if n_nodes < 2:
        raise ValidationError("network too small")

    adj_dist, adj_time = build_graph(coords, edges)
    od_pairs = _parse_od(args.od, n_nodes)
    h_scale = admissible_heuristic_scale(coords, edges, args.weight)
    results = route_od(coords, adj_dist, adj_time, od_pairs,
                       weight=args.weight, algorithm=args.algorithm,
                       heuristic_scale=h_scale)

    n_reach = sum(1 for r in results if r["reachable"])
    out_geojson = os.path.join(output_dir, "routes.geojson")
    write_routes_geojson(out_geojson, coords, results, args.weight, args.algorithm)
    stats_path = os.path.join(output_dir, "routing_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump({"weight": args.weight, "algorithm": args.algorithm,
                   "n_pairs": len(od_pairs), "n_reachable": n_reach,
                   "routes": [{"source": r["source"], "target": r["target"],
                               "cost": (None if not math.isfinite(r["cost"]) else r["cost"]),
                               "n_nodes": r["n_nodes"]} for r in results]},
                  f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "n_nodes": int(n_nodes), "n_edges": len(edges),
          "weight": args.weight, "algorithm": args.algorithm,
          "n_pairs": len(od_pairs), "n_reachable": n_reach}
    outputs = [
        {"path": out_geojson, "kind": "vector", "crs_epsg": 4326},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] network: {n_nodes} nodes, {len(edges)} edges")
        print(f"[{SKILL_NAME}] routing {len(od_pairs)} OD pairs ({args.weight}/{args.algorithm})")
        print(f"[{SKILL_NAME}] reachable: {n_reach}/{len(od_pairs)}")
        print(f"[{SKILL_NAME}] output: {out_geojson}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def _parse_network(net: Dict[str, Any]) -> Tuple[np.ndarray, List[Tuple[int, int, float, float]], int]:
    node_coords: Dict[int, Tuple[float, float]] = {}
    raw_edges: List[Tuple[int, int, float, float]] = []
    for feat in net.get("features", []):
        props = feat.get("properties", {})
        geom = feat.get("geometry", {})
        if geom.get("type") == "Point" and "node" in props:
            c = geom["coordinates"]
            node_coords[int(props["node"])] = (float(c[0]), float(c[1]))
    if not node_coords:
        raise ValidationError("no node features found")
    ids = sorted(node_coords)
    id2idx = {nid: i for i, nid in enumerate(ids)}
    coords = np.array([node_coords[nid] for nid in ids], dtype=np.float64)
    for feat in net.get("features", []):
        props = feat.get("properties", {})
        geom = feat.get("geometry", {})
        if geom.get("type") == "LineString" and "u" in props and "v" in props:
            u, v = int(props["u"]), int(props["v"])
            euclid = float(np.linalg.norm(np.array(node_coords[u]) - np.array(node_coords[v])))
            dist = float(props.get("distance", euclid))
            time = float(props.get("time", euclid))
            raw_edges.append((id2idx[u], id2idx[v], dist, time))
    return coords, raw_edges, len(ids)


def _parse_od(spec: Optional[str], n_nodes: int) -> List[Tuple[int, int]]:
    if not spec:
        # 默认 3 对：跨网格对角与边
        return [(0, n_nodes - 1), (0, n_nodes // 2), (n_nodes // 3, 2 * n_nodes // 3)]
    pairs = []
    for part in spec.split(";"):
        part = part.strip()
        if not part:
            continue
        try:
            a_str, b_str = part.split(",")
            a, b = int(a_str.strip()), int(b_str.strip())
        except (ValueError, AttributeError) as exc:
            raise UsageError(
                f"--od pair '{part}' must be 'u,v' integers (got ValueError: {exc})"
            )
        pairs.append((a, b))
    if not pairs:
        raise UsageError("no valid OD pairs in --od")
    for a, b in pairs:
        if not (0 <= a < n_nodes and 0 <= b < n_nodes):
            raise ValidationError(
                f"OD pair ({a},{b}) out of range (n={n_nodes})",
                pair=[int(a), int(b)], n_nodes=int(n_nodes),
            )
    return pairs


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Network routing: Dijkstra/A* with distance/time constraints and multi-OD pairs.",
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input network GeoJSON")
    p.add_argument("--grid-n", type=int, default=12, help="synthetic grid size (default: 12)")
    p.add_argument("--speed", type=float, default=1.0, help="travel speed (default: 1)")
    p.add_argument("--weight", default="distance", choices=["distance", "time"],
                   help="edge weight (default: distance)")
    p.add_argument("--algorithm", default="dijkstra", choices=["dijkstra", "astar"],
                   help="routing algorithm (default: dijkstra)")
    p.add_argument("--od", default=None, help="OD pairs as 'u,v;u,v' (default: auto)")
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
