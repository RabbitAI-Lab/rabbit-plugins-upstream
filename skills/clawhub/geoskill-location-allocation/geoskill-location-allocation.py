#!/usr/bin/env python3
"""location-allocation — 选址-分配分析

经典设施选址模型的求解：
- **p-median**：最小化需求加权总距离（贪心 + Teitz-Bart 交换改进）
- **p-center**：最小化最大服务距离（最坏情况最优）
- **max-coverage**：在距离阈值内最大化覆盖需求（MCLP 贪心）

数据源：本地 CSV/GeoJSON 需求点，或 --synthetic 生成模拟需求分布。

隐私声明 / Privacy：
- 默认离线运行，不发起任何网络请求。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python location-allocation.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "location-allocation"

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
def distance_matrix(demand_xy: np.ndarray, facility_xy: np.ndarray) -> np.ndarray:
    """需求点 x 候选设施点的欧氏距离矩阵 (n_demand, n_fac)。"""
    dx = demand_xy[:, None, 0] - facility_xy[None, :, 0]
    dy = demand_xy[:, None, 1] - facility_xy[None, :, 1]
    return np.sqrt(dx * dx + dy * dy)


def _assignment_cost(dmat: np.ndarray, weights: np.ndarray,
                     selected: List[int]) -> Tuple[float, np.ndarray]:
    """给定已选设施集合，计算需求加权总成本与每个需求的最近设施。"""
    sub = dmat[:, selected]
    nearest_local = np.argmin(sub, axis=1)
    nearest_dist = sub[np.arange(dmat.shape[0]), nearest_local]
    cost = float((weights * nearest_dist).sum())
    return cost, np.array([selected[i] for i in nearest_local])


def p_median(dmat: np.ndarray, weights: np.ndarray, p: int,
             max_swap_iter: int = 50) -> Dict[str, Any]:
    """p-median：贪心构造 + Teitz-Bart 交换。

    Returns dict: selected, cost, assignment。
    """
    n_fac = dmat.shape[1]
    if p < 1 or p > n_fac:
        raise ValidationError(f"p must be in [1, {n_fac}]")
    weights = np.asarray(weights, dtype=np.float64)
    if weights.shape[0] != dmat.shape[0]:
        raise ValidationError("weights length != demand count")

    # 贪心构造：逐个加入使成本下降最多的设施
    selected: List[int] = []
    remaining = set(range(n_fac))
    for _ in range(p):
        best_j, best_cost = None, np.inf
        for j in remaining:
            trial = selected + [j]
            c, _ = _assignment_cost(dmat, weights, trial)
            if c < best_cost:
                best_cost, best_j = c, j
        selected.append(best_j)
        remaining.remove(best_j)

    # Teitz-Bart 交换改进
    improved = True
    iters = 0
    while improved and iters < max_swap_iter:
        improved = False
        iters += 1
        cur_cost, _ = _assignment_cost(dmat, weights, selected)
        for si in range(len(selected)):
            for j in list(remaining):
                trial = selected.copy()
                trial[si] = j
                c, _ = _assignment_cost(dmat, weights, trial)
                if c < cur_cost - 1e-9:
                    removed = selected[si]
                    selected[si] = j
                    remaining.remove(j)
                    remaining.add(removed)
                    cur_cost = c
                    improved = True
                    break
            if improved:
                break
    cost, assignment = _assignment_cost(dmat, weights, selected)
    return {"selected": sorted(selected), "cost": cost,
            "assignment": assignment.tolist(), "swap_iters": iters}


def p_center(dmat: np.ndarray, p: int, max_swap_iter: int = 50) -> Dict[str, Any]:
    """p-center：最小化最大需求-设施距离。贪心 + 交换。"""
    n_fac = dmat.shape[1]
    if p < 1 or p > n_fac:
        raise ValidationError(f"p must be in [1, {n_fac}]")

    def maxdist(sel):
        return float(dmat[:, sel].min(axis=1).max())

    selected: List[int] = []
    remaining = set(range(n_fac))
    # 贪心：每次加入使当前最大距离下降最多的
    for _ in range(p):
        best_j, best_md = None, np.inf
        for j in remaining:
            md = maxdist(selected + [j])
            if md < best_md:
                best_md, best_j = md, j
        selected.append(best_j)
        remaining.remove(best_j)

    improved = True
    iters = 0
    while improved and iters < max_swap_iter:
        improved = False
        iters += 1
        cur = maxdist(selected)
        for si in range(len(selected)):
            for j in list(remaining):
                trial = selected.copy()
                trial[si] = j
                md = maxdist(trial)
                if md < cur - 1e-9:
                    removed = selected[si]
                    selected[si] = j
                    remaining.remove(j)
                    remaining.add(removed)
                    cur = md
                    improved = True
                    break
            if improved:
                break
    sub = dmat[:, selected]
    nearest_local = np.argmin(sub, axis=1)
    assignment = [selected[i] for i in nearest_local]
    return {"selected": sorted(selected), "max_distance": maxdist(selected),
            "assignment": assignment, "swap_iters": iters}


def max_coverage(dmat: np.ndarray, weights: np.ndarray, p: int,
                 threshold: float) -> Dict[str, Any]:
    """最大覆盖（MCLP 贪心）：阈值内覆盖需求权重最大化。"""
    n_fac = dmat.shape[1]
    if p < 1 or p > n_fac:
        raise ValidationError(f"p must be in [1, {n_fac}]")
    weights = np.asarray(weights, dtype=np.float64)
    covered = dmat <= threshold  # (n_demand, n_fac) bool
    uncovered_weight = weights.copy()
    selected: List[int] = []
    remaining = set(range(n_fac))
    for _ in range(p):
        best_j, best_gain = None, -1.0
        for j in remaining:
            gain = float((uncovered_weight * covered[:, j]).sum())
            if gain > best_gain:
                best_gain, best_j = gain, j
        selected.append(best_j)
        remaining.remove(best_j)
        uncovered_weight = np.where(covered[:, best_j], 0.0, uncovered_weight)
    covered_mask = covered[:, selected].any(axis=1)
    covered_demand = float(weights[covered_mask].sum())
    return {"selected": sorted(selected), "covered_demand": covered_demand,
            "total_demand": float(weights.sum()),
            "coverage_ratio": float(covered_demand / weights.sum()) if weights.sum() > 0 else 0.0,
            "covered_mask": covered_mask.tolist()}


def brute_force_p_median(dmat: np.ndarray, weights: np.ndarray, p: int) -> Tuple[List[int], float]:
    """暴力枚举（仅用于小规模验证）。"""
    from itertools import combinations
    best_sel, best_cost = None, np.inf
    for combo in combinations(range(dmat.shape[1]), p):
        c, _ = _assignment_cost(dmat, weights, list(combo))
        if c < best_cost:
            best_cost, best_sel = c, list(combo)
    return best_sel, best_cost


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], n_demand: int = 60, n_candidates: int = 20,
                       seed: int = 42) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成需求点（含权重）与候选设施点。

    Returns (demand_xy, weights, candidate_xy, info)。
    """
    rng = np.random.default_rng(seed)
    w, s, e, n = bbox
    # 需求点向两个聚集中心集中
    centers = np.array([[w + 0.3 * (e - w), s + 0.3 * (n - s)],
                        [w + 0.7 * (e - w), s + 0.7 * (n - s)]])
    demand = []
    for _ in range(n_demand):
        c = centers[rng.integers(0, 2)]
        demand.append(c + rng.normal(0, 0.05 * max(e - w, n - s), 2))
    demand_xy = np.array(demand)
    weights = rng.uniform(1, 10, n_demand)
    candidate_xy = rng.uniform([w, s], [e, n], (n_candidates, 2))
    info = {"n_demand": n_demand, "n_candidates": n_candidates}
    return demand_xy, weights, candidate_xy, info


# ---------------------------------------------------------------------------
# 输出 / Manifest
# ---------------------------------------------------------------------------
def write_geojson(path: str, demand_xy: np.ndarray, weights: np.ndarray,
                  candidate_xy: np.ndarray, selected: List[int],
                  assignment: Optional[List[int]], model: str) -> None:
    feats = []
    for j in selected:
        feats.append({
            "type": "Feature",
            "properties": {"kind": "facility", "node": int(j), "model": model},
            "geometry": {"type": "Point",
                         "coordinates": [float(candidate_xy[j, 0]), float(candidate_xy[j, 1])]},
        })
    for i in range(candidate_xy.shape[0]):
        feats.append({
            "type": "Feature",
            "properties": {"kind": "candidate", "node": int(i), "selected": i in selected},
            "geometry": {"type": "Point",
                         "coordinates": [float(candidate_xy[i, 0]), float(candidate_xy[i, 1])]},
        })
    for i in range(demand_xy.shape[0]):
        props = {"kind": "demand", "node": int(i), "weight": float(weights[i])}
        if assignment is not None:
            props["assigned_to"] = int(assignment[i])
        feats.append({
            "type": "Feature",
            "properties": props,
            "geometry": {"type": "Point",
                         "coordinates": [float(demand_xy[i, 0]), float(demand_xy[i, 1])]},
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

    # ---- Validate bbox and params early ----
    if bbox is not None:
        bbox = validate_bbox(bbox)
    if args.p < 1:
        raise ValidationError(f"--p must be >= 1 (got {args.p})")
    if args.threshold < 0:
        raise ValidationError(
            f"--threshold must be >= 0 for max-coverage (got {args.threshold})")
    if args.n_demand is not None and args.n_demand < 1:
        raise ValidationError(
            f"--n-demand must be >= 1 in synthetic mode (got {args.n_demand})")
    if args.n_candidates is not None and args.n_candidates < 1:
        raise ValidationError(
            f"--n-candidates must be >= 1 in synthetic mode (got {args.n_candidates})")

    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input not found: {args.input}", path=args.input)
        demand_xy, weights, candidate_xy = _load_csv(args.input)
        if bbox is None:
            allxy = np.vstack([demand_xy, candidate_xy])
            bbox = [float(allxy[:, 0].min()), float(allxy[:, 1].min()),
                    float(allxy[:, 0].max()), float(allxy[:, 1].max())]
            bbox = validate_bbox(bbox)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <csv>")
        demand_xy, weights, candidate_xy, _ = generate_synthetic(
            bbox, n_demand=args.n_demand, n_candidates=args.n_candidates)
        source_note = "synthetic"

    if demand_xy.shape[0] == 0 or candidate_xy.shape[0] == 0:
        raise ValidationError("empty demand or candidate set")
    if args.p > candidate_xy.shape[0]:
        raise UsageError(f"p={args.p} exceeds candidate count {candidate_xy.shape[0]}")

    # ---- Now safe to create output directory ----
    os.makedirs(output_dir, exist_ok=True)

    dmat = distance_matrix(demand_xy, candidate_xy)
    assignment = None
    if args.model == "p-median":
        res = p_median(dmat, weights, args.p)
        selected = res["selected"]
        assignment = res["assignment"]
        metric = {"objective_cost": res["cost"]}
    elif args.model == "p-center":
        res = p_center(dmat, args.p)
        selected = res["selected"]
        assignment = res["assignment"]
        metric = {"max_distance": res["max_distance"]}
    else:  # max-coverage
        res = max_coverage(dmat, weights, args.p, args.threshold)
        selected = res["selected"]
        metric = {"covered_demand": res["covered_demand"],
                  "coverage_ratio": res["coverage_ratio"]}

    out_geojson = os.path.join(output_dir, "allocation.geojson")
    write_geojson(out_geojson, demand_xy, weights, candidate_xy, selected, assignment, args.model)
    stats_path = os.path.join(output_dir, "allocation_stats.json")
    serializable = {k: (v.tolist() if isinstance(v, np.ndarray) else v) for k, v in res.items()}
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump({"model": args.model, "p": args.p, "threshold": args.threshold,
                   "selected": selected, **{k: (v if not isinstance(v, list) else v)
                                           for k, v in metric.items()}},
                  f, ensure_ascii=False, indent=2, default=str)

    qa = {"source": source_note, "model": args.model, "p": args.p,
          "n_demand": int(demand_xy.shape[0]), "n_candidates": int(candidate_xy.shape[0]),
          "selected": selected, **metric}
    outputs = [
        {"path": out_geojson, "kind": "vector", "crs_epsg": 4326},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  model: {args.model}  p: {args.p}")
        print(f"[{SKILL_NAME}] selected facilities: {selected}")
        for k, v in metric.items():
            print(f"[{SKILL_NAME}] {k}: {v:.4f}" if isinstance(v, float) else f"[{SKILL_NAME}] {k}: {v}")
        print(f"[{SKILL_NAME}] output: {out_geojson}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def _load_csv(path: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """CSV 列：x,y,weight,kind (kind='demand' or 'candidate')。"""
    import csv
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if len(rows) < 2:
        raise ValidationError("CSV has no data rows")
    header = [h.strip().lower() for h in rows[0]]
    col = {h: i for i, h in enumerate(header)}
    if "x" not in col or "y" not in col or "kind" not in col:
        raise ValidationError("CSV must contain columns: x, y, kind")
    demand, weights, cand = [], [], []
    for r in rows[1:]:
        if not r:
            continue
        x, y = float(r[col["x"]]), float(r[col["y"]])
        kind = r[col["kind"]].strip().lower()
        if kind == "demand":
            demand.append([x, y])
            w = float(r[col["weight"]]) if "weight" in col else 1.0
            weights.append(w)
        elif kind == "candidate":
            cand.append([x, y])
    if not demand or not cand:
        raise ValidationError("need both demand and candidate rows")
    return np.array(demand), np.array(weights), np.array(cand)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Location-allocation: p-median, p-center, and max-coverage models with demand weights.",
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input CSV (x,y,weight,kind)")
    p.add_argument("--model", default="p-median", choices=["p-median", "p-center", "max-coverage"],
                   help="location model (default: p-median)")
    p.add_argument("--p", type=int, default=3, help="number of facilities (default: 3)")
    p.add_argument("--threshold", type=float, default=0.2, help="coverage distance threshold (default: 0.2)")
    p.add_argument("--n-demand", type=int, default=60, help="synthetic demand count (default: 60)")
    p.add_argument("--n-candidates", type=int, default=20, help="synthetic candidate count (default: 20)")
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
