#!/usr/bin/env python3
"""education-resource-allocation — 教育资源空间配置

面向教育设施布局优化的空间分析工具：

- **需求估计**：由人口栅格聚合得到每个居住区的学生需求。
- **可达性 + 容量约束分配**：按"最近且有空位"把学生分配到现有学校（容量
  约束），统计覆盖率与超载情况。
- **公平性评价**：用基尼系数 / 变异系数度量各区可达性公平性，∈[0,1]。
- **选址优化**：贪心 p-median，从候选点中选 k 个新建校址，最小化人口加权
  总可达距离。

数据源：本地 GeoTIFF（人口栅格）+ 学校/候选点，或 ``--synthetic`` 生成含人口
分布的模拟场景用于离线测试。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络；本地处理，不上传数据。

Usage:
    python education-resource-allocation.py --input population.tif --output-dir ./out
    python education-resource-allocation.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "education-resource-allocation"

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


BAND_ROLES = ["population"]
N_REQUIRED_BANDS = len(BAND_ROLES)
METHODS = ["allocate", "site-select", "both"]


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


def validate_cli_params(method: str, capacity: float, k_new: int,
                        equity_metric: str) -> None:
    """CLI 参数前置校验（错误→rc=2）。"""
    if method not in METHODS:
        raise UsageError(f"unknown method '{method}'; choose from {METHODS}",
                         method=method)
    if equity_metric not in ("gini", "cv"):
        raise UsageError(
            f"unknown --equity-metric '{equity_metric}'; choose gini|cv",
            equity_metric=equity_metric)
    if not (float(capacity) > 0):
        raise UsageError(
            f"--capacity must be > 0 (students per school); got {capacity}",
            capacity=capacity)
    if int(k_new) < 0:
        raise UsageError(
            f"--k-new must be >= 0; got {k_new}", k_new=k_new)


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def euclid_distance_matrix(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """a (m,2) 与 b (n,2) 的欧氏距离矩阵 (m,n)。"""
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    diff = a[:, None, :] - b[None, :, :]
    return np.sqrt(np.sum(diff * diff, axis=2))


def assign_students(
    demand: np.ndarray,
    zone_coords: np.ndarray,
    school_coords: np.ndarray,
    capacity: np.ndarray,
) -> Dict[str, Any]:
    """容量约束下把各区学生就近分配到学校（贪心：按需求降序、就近有空位）。

    返回 assignment（区->学校或 -1）、served、unserved、每校 load。
    """
    demand = np.asarray(demand, dtype=np.float64)
    capacity = np.asarray(capacity, dtype=np.float64)
    n_zones = len(demand)
    n_schools = len(school_coords)
    dist = euclid_distance_matrix(zone_coords, school_coords)  # (zones, schools)

    load = np.zeros(n_schools, dtype=np.float64)
    assignment = np.full(n_zones, -1, dtype=int)
    served = 0.0
    # 需求大的区优先选择（更易缺位）
    order = np.argsort(-demand)
    for z in order:
        dz = demand[z]
        if dz <= 0:
            continue
        # 按距离排序的学校
        cand = np.argsort(dist[z])
        remaining = dz
        chosen = -1
        for s in cand:
            room = capacity[s] - load[s]
            if room <= 1e-9:
                continue
            take = min(room, remaining)
            load[s] += take
            remaining -= take
            if chosen < 0:
                chosen = int(s)
            if remaining <= 1e-9:
                break
        if chosen >= 0:
            assignment[z] = chosen
        served += (dz - max(remaining, 0.0))
    unserved = float(demand.sum() - served)
    return {"assignment": assignment.tolist(), "load": load.tolist(),
            "served": float(served), "unserved": float(unserved),
            "n_schools": int(n_schools), "capacity": capacity.tolist()}


def coverage_fraction(demand: np.ndarray, assignment: np.ndarray) -> float:
    """被成功分配（assignment != -1）的需求占比。"""
    demand = np.asarray(demand, dtype=np.float64)
    total = demand.sum()
    if total <= 0:
        return 1.0
    assignment = np.asarray(assignment)
    served = demand[assignment >= 0].sum()
    return float(np.clip(served / total, 0.0, 1.0))


def gini(values: np.ndarray) -> float:
    """基尼系数 ∈[0,1]，度量不均等程度（0=完全公平）。"""
    v = np.asarray(values, dtype=np.float64).ravel()
    v = v[np.isfinite(v)]
    if v.size == 0:
        return 0.0
    v = np.sort(v)
    n = v.size
    if n == 1 or v.sum() == 0:
        return 0.0
    cum = np.cumsum(v)
    return float((n + 1 - 2 * cum.sum() / cum[-1]) / n)


def equity_index(access: np.ndarray, metric: str = "gini") -> float:
    """可达性公平性指数 ∈[0,1]，越大越公平。

    - gini：1 − 基尼系数（对可达距离）；
    - cv：1 / (1 + 变异系数)。
    """
    a = np.asarray(access, dtype=np.float64).ravel()
    a = a[np.isfinite(a)]
    if a.size == 0:
        return 1.0
    if metric == "cv":
        mu = a.mean()
        if mu <= 1e-12:
            return 1.0
        cv = a.std() / mu
        return float(1.0 / (1.0 + cv))
    return float(1.0 - gini(a))


def weighted_access(
    zone_coords: np.ndarray,
    school_coords: np.ndarray,
) -> np.ndarray:
    """每个区到最近学校的距离。"""
    if len(school_coords) == 0:
        return np.full(len(zone_coords), np.inf, dtype=np.float64)
    d = euclid_distance_matrix(zone_coords, school_coords)
    return d.min(axis=1)


def select_new_sites(
    candidates: np.ndarray,
    zone_coords: np.ndarray,
    demand: np.ndarray,
    k: int,
    existing: Optional[np.ndarray] = None,
) -> Tuple[List[int], float]:
    """贪心 p-median：从候选点依次选出使加权总距离下降最大的 k 个校址。

    返回 (选中的候选索引列表, 选址后加权总距离)。
    """
    candidates = np.asarray(candidates, dtype=np.float64)
    zone_coords = np.asarray(zone_coords, dtype=np.float64)
    demand = np.asarray(demand, dtype=np.float64)
    if len(candidates) == 0 or k <= 0:
        base = weighted_access(zone_coords, existing if existing is not None else np.zeros((0, 2)))
        return [], float((demand * base).sum())

    # 现状最近距离（含已有学校）
    if existing is not None and len(existing) > 0:
        cur_min = weighted_access(zone_coords, existing)
    else:
        cur_min = np.full(len(zone_coords), np.inf, dtype=np.float64)

    cand_dist = euclid_distance_matrix(zone_coords, candidates)  # (zones, cands)
    selected: List[int] = []
    for _ in range(min(k, len(candidates))):
        best_idx = -1
        best_cost = math.inf
        for c in range(len(candidates)):
            if c in selected:
                continue
            new_min = np.minimum(cur_min, cand_dist[:, c])
            cost = float((demand * new_min).sum())
            if cost < best_cost:
                best_cost = cost
                best_idx = c
        if best_idx < 0:
            break
        selected.append(best_idx)
        cur_min = np.minimum(cur_min, cand_dist[:, best_idx])
    final = float((demand * cur_min).sum())
    return selected, final


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic_scene(
    bbox: List[float], width: int = 128, height: int = 128, seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成人口栅格 + 居住区/学校/候选点。返回 (cube[1,H,W], info)。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    # 两个居住中心
    pop = (200.0 * np.exp(-((((yy / height) - 0.3) ** 2 + ((xx / width) - 0.3) ** 2)) / (2 * 0.1 ** 2))
           + 300.0 * np.exp(-((((yy / height) - 0.7) ** 2 + ((xx / width) - 0.7) ** 2)) / (2 * 0.12 ** 2))
           + rng.normal(0, 5, (height, width))).astype(np.float32)
    pop = np.clip(pop, 0, None)

    # 居住区（粗网格聚合中心）
    gh, gw = 8, 8
    zones = []
    for gi in range(gh):
        for gj in range(gw):
            zones.append([gi + 0.5, gj + 0.5])
    zones = np.array(zones, dtype=np.float64)

    schools = np.array([[2.0, 2.0], [6.0, 6.0]], dtype=np.float64)
    candidates = np.array([[1.0, 5.0], [5.0, 1.0], [3.5, 3.5], [7.0, 2.0]], dtype=np.float64)

    cube = pop[np.newaxis, ...].astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "band_roles": BAND_ROLES, "zones_rc": zones.tolist(),
            "schools_rc": schools.tolist(), "candidates_rc": candidates.tolist(),
            "grid": [gh, gw]}
    return cube, info


def aggregate_zone_demand(population: np.ndarray, gh: int, gw: int) -> np.ndarray:
    """把人口栅格按 gh×gw 网格聚合为每区需求（按学生比例折算）。"""
    h, w = population.shape
    bh, bw = h // gh, w // gw
    demand = np.zeros(gh * gw, dtype=np.float64)
    student_ratio = 0.12
    for gi in range(gh):
        for gj in range(gw):
            r0, r1 = gi * bh, min((gi + 1) * bh, h)
            c0, c1 = gj * bw, min((gj + 1) * bw, w)
            demand[gi * gw + gj] = float(population[r0:r1, c0:c1].sum()) * student_ratio
    return demand


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path, cube, bbox, nodata=-9999.0, dtype="float32"):
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


def read_geotiff(path):
    """Read GeoTIFF → (cube, bbox). NoData == profile.nodata 保留原值。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_with_nodata(path):
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


def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None),
                "method": getattr(args, "method", None),
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

    # ---- 0) CLI 参数前置校验（错误→rc=2）----
    validate_cli_params(
        method=args.method, capacity=args.capacity,
        k_new=args.k_new, equity_metric=args.equity_metric,
    )

    bbox = list(args.bbox) if args.bbox else None
    if bbox is not None:
        validate_bbox(bbox)

    synth_info = None
    src_nodata = None
    if args.input and not args.synthetic:
        cube, file_bbox, src_nodata = read_geotiff_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        validate_bbox(bbox)
        source_note = args.input
        gh, gw = 8, 8
        # 真实模式：自动生成演示用学校/候选点
        schools = np.array([[2.0, 2.0], [6.0, 6.0]], dtype=np.float64)
        candidates = np.array([[1.0, 5.0], [5.0, 1.0], [3.5, 3.5]], dtype=np.float64)
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, synth_info = generate_synthetic_scene(bbox)
        gh, gw = synth_info["grid"]
        schools = np.array(synth_info["schools_rc"], dtype=np.float64)
        candidates = np.array(synth_info["candidates_rc"], dtype=np.float64)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.ndim != 3 or cube.shape[0] < N_REQUIRED_BANDS:
        raise ValidationError(
            f"input must have >= {N_REQUIRED_BANDS} band ({BAND_ROLES}); got {cube.shape}")

    population = cube[0]
    n_valid_pixels = int(np.isfinite(population).sum())
    n_total_pixels = int(population.size)
    if n_valid_pixels == 0:
        raise ValidationError(
            "input has no finite (non-NoData) pixels after NoData masking; "
            "all values are NaN/nodata — cannot estimate demand",
            n_total_pixels=n_total_pixels, input_nodata=src_nodata)
    # 用 NaN 安全的聚合：把 NaN 视为 0 需求（不下钻聚合只对 valid 求和）
    pop_for_agg = np.nan_to_num(population, nan=0.0)

    # ---- 通过校验后再创建输出目录 ----
    os.makedirs(output_dir, exist_ok=True)

    zones = np.array([[gi + 0.5, gj + 0.5] for gi in range(gh) for gj in range(gw)], dtype=np.float64)
    demand = aggregate_zone_demand(pop_for_agg, gh, gw)
    capacity = np.full(len(schools), args.capacity, dtype=np.float64)

    outputs = []
    qa: Dict[str, Any] = {
        "source": source_note, "method": args.method,
        "n_zones": int(len(zones)), "total_demand": float(demand.sum()),
        "n_valid_pixels": n_valid_pixels, "n_total_pixels": n_total_pixels,
        "valid_pixel_ratio": float(n_valid_pixels / n_total_pixels) if n_total_pixels else 0.0,
        "input_nodata": src_nodata,
    }

    if args.method in ("allocate", "both"):
        res = assign_students(demand, zones, schools, capacity)
        cov = coverage_fraction(demand, res["assignment"])
        acc = weighted_access(zones, schools)
        equity = equity_index(acc, metric=args.equity_metric)
        qa["coverage"] = cov
        qa["equity_index"] = equity
        qa["unserved"] = res["unserved"]
        alloc = {"assignment": res["assignment"], "load": res["load"],
                 "capacity": res["capacity"], "served": res["served"],
                 "unserved": res["unserved"], "coverage": cov,
                 "equity_index": equity, "equity_metric": args.equity_metric}
        alloc_path = os.path.join(output_dir, "allocation.json")
        with open(alloc_path, "w", encoding="utf-8") as f:
            json.dump(alloc, f, ensure_ascii=False, indent=2, default=float)
        outputs.append({"path": alloc_path, "kind": "json"})

    if args.method in ("site-select", "both"):
        base_cost = float((demand * weighted_access(zones, schools)).sum())
        selected, new_cost = select_new_sites(candidates, zones, demand, args.k_new, schools)
        improvement = (base_cost - new_cost) / base_cost if base_cost > 0 else 0.0
        qa["selected_sites"] = [int(s) for s in selected]
        qa["access_cost_before"] = base_cost
        qa["access_cost_after"] = new_cost
        qa["improvement"] = improvement
        site = {"selected_candidate_indices": [int(s) for s in selected],
                "selected_coords": [candidates[s].tolist() for s in selected],
                "k": args.k_new, "cost_before": base_cost, "cost_after": new_cost,
                "improvement": improvement}
        site_path = os.path.join(output_dir, "site_selection.json")
        with open(site_path, "w", encoding="utf-8") as f:
            json.dump(site, f, ensure_ascii=False, indent=2, default=float)
        outputs.append({"path": site_path, "kind": "json"})

    report = {"source": source_note, "method": args.method, "qa": qa}
    report_path = os.path.join(output_dir, "education_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2, default=float)
    outputs.append({"path": report_path, "kind": "json"})

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  method: {args.method}")
        print(f"[{SKILL_NAME}] valid pixels: {n_valid_pixels}/{n_total_pixels} "
              f"({qa['valid_pixel_ratio']:.2%})")
        if "coverage" in qa:
            print(f"[{SKILL_NAME}] coverage: {qa['coverage']:.3f}  equity: {qa['equity_index']:.3f}")
        if "improvement" in qa:
            print(f"[{SKILL_NAME}] new sites: {qa['selected_sites']}  "
                  f"access cost ↓{qa['improvement']*100:.1f}%")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser():
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Education resource allocation: capacity assignment, equity and p-median site selection.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoTIFF (population)")
    p.add_argument("--synthetic", action="store_true")
    p.add_argument("--method", default="both", choices=METHODS,
                   help="analysis method (default: both)")
    p.add_argument("--capacity", type=float, default=200.0, help="school capacity (default: 200)")
    p.add_argument("--k-new", type=int, default=2, help="number of new sites to select (default: 2)")
    p.add_argument("--equity-metric", default="gini", choices=["gini", "cv"],
                   help="equity metric (default: gini)")
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
