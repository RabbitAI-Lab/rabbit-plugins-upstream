#!/usr/bin/env python3
"""service-area-analysis — 服务区分析

基于网络图（节点 + 加权边）计算设施服务区（等时圈）。对每个设施用 Dijkstra
计算网络通行时间，按时间阈值划分服务区，支持多设施叠加与最近设施分配，
统计每个阈值下的覆盖节点数/需求量。

数据源：本地网络 GeoJSON，或 --synthetic 生成模拟格网道路。

隐私声明 / Privacy：
- 默认离线运行，不发起任何网络请求。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python service-area-analysis.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "service-area-analysis"

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
# 校验前置
# ---------------------------------------------------------------------------
def validate_bbox(bbox, source: str = "bbox") -> None:
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
        if v != v:
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


def validate_grid_n(grid_n: int) -> None:
    if int(grid_n) < 2:
        raise ValidationError(
            f"--grid-n must be >= 2 (got {grid_n!r}); "
            "at least 2 nodes (a 1x1 grid = single isolated node) is needed for service area."
        )


def validate_speed(speed: float) -> None:
    try:
        v = float(speed)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"--speed must be a float (got {speed!r})") from exc
    if v <= 0:
        raise ValidationError(f"--speed must be > 0 (got {speed!r})")


def validate_thresholds(thresholds: str) -> List[float]:
    """Parse and validate --thresholds (comma-separated floats, all > 0)."""
    parts = [t.strip() for t in thresholds.split(",") if t.strip()]
    if not parts:
        raise ValidationError("--thresholds must list at least one positive value")
    out = []
    for t in parts:
        try:
            v = float(t)
        except ValueError as exc:
            raise ValidationError(f"--thresholds: non-numeric value {t!r}") from exc
        if v <= 0:
            raise ValidationError(f"--thresholds: value must be > 0 (got {v})")
        out.append(v)
    return out


# ---------------------------------------------------------------------------
# 核心算法：网络图 + Dijkstra
# ---------------------------------------------------------------------------
def build_adjacency(edges: List[Tuple[int, int, float]], n_nodes: int) -> List[List[Tuple[int, float]]]:
    """由边列表 (u, v, weight) 构建无向邻接表。"""
    adj: List[List[Tuple[int, float]]] = [[] for _ in range(n_nodes)]
    for u, v, wgt in edges:
        if u < 0 or u >= n_nodes or v < 0 or v >= n_nodes:
            raise ValidationError(f"edge ({u},{v}) references invalid node (n={n_nodes})")
        if wgt < 0:
            raise ValidationError(f"edge ({u},{v}) has negative weight")
        adj[u].append((v, wgt))
        adj[v].append((u, wgt))
    return adj


def dijkstra(adj: List[List[Tuple[int, float]]], source: int) -> np.ndarray:
    """单源 Dijkstra，返回到所有节点的最短距离。不可达为 inf。"""
    n = len(adj)
    if not (0 <= source < n):
        raise ValidationError(f"source {source} out of range (n={n})")
    dist = np.full(n, np.inf, dtype=np.float64)
    dist[source] = 0.0
    heap = [(0.0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, wgt in adj[u]:
            nd = d + wgt
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist


def service_area(
    adj: List[List[Tuple[int, float]]], facilities: List[int], threshold: float,
) -> Dict[str, Any]:
    """计算多设施服务区。

    Returns
    -------
    dict 含：
      reachable_any : (n,) bool 任一设施在阈值内可达
      nearest_facility : (n,) int 最近设施索引（-1 表示全部超阈值）
      min_time : (n,) float 到最近设施的时间
      covered_count : int 覆盖节点数
    """
    n = len(adj)
    if not facilities:
        raise ValidationError("no facilities provided")
    min_time = np.full(n, np.inf, dtype=np.float64)
    nearest = np.full(n, -1, dtype=np.int32)
    for fi, fac in enumerate(facilities):
        d = dijkstra(adj, fac)
        closer = d < min_time
        min_time[closer] = d[closer]
        nearest[closer] = fi
    reachable_any = min_time <= threshold
    nearest[~reachable_any] = -1
    return {
        "reachable_any": reachable_any,
        "nearest_facility": nearest,
        "min_time": min_time,
        "covered_count": int(reachable_any.sum()),
    }


def coverage_by_threshold(
    adj: List[List[Tuple[int, float]]], facilities: List[int],
    thresholds: List[float], demand: Optional[np.ndarray] = None,
) -> List[Dict[str, Any]]:
    """在多个时间阈值上统计覆盖节点数与覆盖需求量。"""
    if demand is None:
        demand = np.ones(len(adj))
    demand = np.asarray(demand, dtype=np.float64)
    results = []
    # 复用最近设施时间
    n = len(adj)
    min_time = np.full(n, np.inf)
    for fac in facilities:
        d = dijkstra(adj, fac)
        min_time = np.minimum(min_time, d)
    for thr in thresholds:
        mask = min_time <= thr
        results.append({
            "threshold": float(thr),
            "covered_nodes": int(mask.sum()),
            "covered_demand": float(demand[mask].sum()),
            "total_demand": float(demand.sum()),
        })
    return results


# ---------------------------------------------------------------------------
# 合成网络：规则格网道路
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], grid_n: int = 12, speed: float = 1.0,
                       seed: int = 42) -> Tuple[np.ndarray, List[Tuple[int, int, float]], Dict[str, Any]]:
    """生成 grid_n x grid_n 规则格网，边权 = 欧氏距离 / speed（通行时间）。

    Returns (coords (N,2), edges, info)。
    """
    rng = np.random.default_rng(seed)
    w, s, e, n = bbox
    xs = np.linspace(w, e, grid_n)
    ys = np.linspace(n, s, grid_n)
    gx, gy = np.meshgrid(xs, ys)
    coords = np.column_stack([gx.ravel(), gy.ravel()])
    # 加一点坐标扰动模拟真实路网
    coords += rng.normal(0, 0.001, coords.shape)
    N = coords.shape[0]
    edges: List[Tuple[int, int, float]] = []
    for r in range(grid_n):
        for c in range(grid_n):
            i = r * grid_n + c
            if c < grid_n - 1:
                j = r * grid_n + c + 1
                d = float(np.linalg.norm(coords[i] - coords[j])) / speed
                edges.append((i, j, d))
            if r < grid_n - 1:
                j = (r + 1) * grid_n + c
                d = float(np.linalg.norm(coords[i] - coords[j])) / speed
                edges.append((i, j, d))
    info = {"n_nodes": N, "n_edges": len(edges), "grid_n": grid_n}
    return coords, edges, info


# ---------------------------------------------------------------------------
# GeoJSON / I/O
# ---------------------------------------------------------------------------
def write_geojson(path: str, coords: np.ndarray, nearest: np.ndarray,
                  facilities: List[int], min_time: np.ndarray) -> None:
    feats = []
    for fi, fac in enumerate(facilities):
        feats.append({
            "type": "Feature",
            "properties": {"kind": "facility", "facility_index": fi, "node": int(fac)},
            "geometry": {"type": "Point", "coordinates": [float(coords[fac, 0]), float(coords[fac, 1])]},
        })
    for i in range(coords.shape[0]):
        feats.append({
            "type": "Feature",
            "properties": {"kind": "node", "node": int(i),
                           "nearest_facility": int(nearest[i]),
                           "travel_time": (None if not np.isfinite(min_time[i]) else float(min_time[i]))},
            "geometry": {"type": "Point", "coordinates": [float(coords[i, 0]), float(coords[i, 1])]},
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
    bbox = list(args.bbox) if args.bbox else None

    # ===== 0) Validate CLI up-front (no side effects, no mkdir) =====
    if not (args.input or args.synthetic or bbox):
        raise UsageError("provide --bbox (synthetic mode) or --input <geojson>")
    if bbox is not None:
        validate_bbox(bbox, source="--bbox")
    validate_grid_n(args.grid_n)
    validate_speed(args.speed)
    thresholds = validate_thresholds(args.thresholds)

    # mkdir AFTER validation (CONVENTIONS §1.1 / common bug pattern #6)
    os.makedirs(output_dir, exist_ok=True)

    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input not found: {args.input}", path=args.input)
        with open(args.input, encoding="utf-8") as f:
            net = json.load(f)
        coords, edges, n_nodes = _parse_network(net)
        if bbox is None:
            bbox = [float(coords[:, 0].min()), float(coords[:, 1].min()),
                    float(coords[:, 0].max()), float(coords[:, 1].max())]
        if args.bbox is not None:
            validate_bbox(bbox, source="--bbox")
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <geojson>")
        coords, edges, _ = generate_synthetic(bbox, grid_n=args.grid_n, speed=args.speed)
        n_nodes = coords.shape[0]
        source_note = "synthetic"

    if n_nodes < 2:
        raise ValidationError("network too small")

    adj = build_adjacency(edges, n_nodes)
    facilities = _select_facilities(args.facilities, n_nodes)

    sa = service_area(adj, facilities, max(thresholds))
    cov = coverage_by_threshold(adj, facilities, thresholds)

    out_geojson = os.path.join(output_dir, "service_area.geojson")
    write_geojson(out_geojson, coords, sa["nearest_facility"], facilities, sa["min_time"])
    stats_path = os.path.join(output_dir, "service_area_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump({"facilities": facilities, "coverage": cov,
                   "covered_count_at_max": sa["covered_count"]}, f, ensure_ascii=False, indent=2)

    qa = {
        "source": source_note,
        "n_nodes": int(n_nodes),
        "n_edges": len(edges),
        "n_facilities": len(facilities),
        "thresholds": thresholds,
        "coverage": cov,
    }
    outputs = [
        {"path": out_geojson, "kind": "vector", "crs_epsg": 4326},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] network: {n_nodes} nodes, {len(edges)} edges")
        print(f"[{SKILL_NAME}] facilities: {facilities}")
        for c in cov:
            print(f"[{SKILL_NAME}]   t<={c['threshold']:.2f}: {c['covered_nodes']} nodes, demand {c['covered_demand']:.1f}")
        print(f"[{SKILL_NAME}] output: {out_geojson}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def _parse_network(net: Dict[str, Any]) -> Tuple[np.ndarray, List[Tuple[int, int, float]], int]:
    """从 GeoJSON FeatureCollection 解析节点(带 node id)与边(LineString)。"""
    node_coords: Dict[int, Tuple[float, float]] = {}
    edges: List[Tuple[int, int, float]] = []
    for feat in net.get("features", []):
        props = feat.get("properties", {})
        geom = feat.get("geometry", {})
        if geom.get("type") == "Point" and "node" in props:
            c = geom["coordinates"]
            node_coords[int(props["node"])] = (float(c[0]), float(c[1]))
    if not node_coords:
        raise ValidationError("no node features (Point with 'node' property) found")
    ids = sorted(node_coords)
    id2idx = {nid: i for i, nid in enumerate(ids)}
    coords = np.array([node_coords[nid] for nid in ids], dtype=np.float64)
    for feat in net.get("features", []):
        props = feat.get("properties", {})
        geom = feat.get("geometry", {})
        if geom.get("type") == "LineString" and "u" in props and "v" in props:
            u, v = int(props["u"]), int(props["v"])
            wgt = float(props.get("weight", np.linalg.norm(
                np.array(node_coords[u]) - np.array(node_coords[v]))))
            edges.append((id2idx[u], id2idx[v], wgt))
    return coords, edges, len(ids)


def _select_facilities(spec: Optional[str], n_nodes: int) -> List[int]:
    if not spec:
        # 默认四象限各一个
        return sorted({n_nodes // 4, n_nodes // 2, 3 * n_nodes // 4, 0})
    facs = [int(x) for x in spec.split(",") if x.strip()]
    for f in facs:
        if not (0 <= f < n_nodes):
            raise UsageError(f"facility node {f} out of range (n={n_nodes})")
    if not facs:
        raise UsageError("no valid facilities in --facilities")
    return facs


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Service area analysis: network isochrones, multi-facility coverage statistics.",
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input network GeoJSON")
    p.add_argument("--grid-n", type=int, default=12, help="synthetic grid size per side (default: 12)")
    p.add_argument("--speed", type=float, default=1.0, help="travel speed (default: 1)")
    p.add_argument("--facilities", default=None, help="facility node ids as 'id,id,...' (default: auto)")
    p.add_argument("--thresholds", default="0.05,0.1,0.2,0.5",
                   help="comma-separated time thresholds (default: 0.05,0.1,0.2,0.5)")
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
