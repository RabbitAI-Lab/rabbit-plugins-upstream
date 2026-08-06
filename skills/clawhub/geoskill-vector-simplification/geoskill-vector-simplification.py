#!/usr/bin/env python3
"""vector-simplification — 矢量简化

用两种经典线简化算法减少矢量几何的顶点数：

- **Douglas-Peucker**（DP）：递归地把点到弦的距离与容差 epsilon 比较，
  删除落在容差带内的点；保形性好，是最常用的线/面简化算法。
- **Visvalingam-Whyatt**：迭代删除“有效面积”（相邻三点构成的三角形面积）
  最小的点，可按目标顶点数或面积阈值停止；对锯齿状线更平滑。

对多边形/线串逐几何简化，统计顶点减少比例与面积保持率。

数据源：本地矢量文件（``--input``），或 ``--synthetic`` 模式生成含高密度
顶点（圆/锯齿线）的测试要素（离线）。

隐私声明 / Privacy：
- 默认完全离线运行，``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python vector-simplification.py --input roads.shp --method douglas-peucker --tolerance 0.001
    python vector-simplification.py --bbox 116 39 117 40 --synthetic --method visvalingam --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "vector-simplification"

METHODS = {"douglas-peucker", "visvalingam"}


def _ensure_geoskill_imports():
    """Late-bind _geoskill_core helpers (avoid global-time re-bind for unit tests)."""
    pass


def validate_bbox(bbox):
    """Validate WGS-84 bbox. Returns (W, S, E, N) as floats.

    Rules:
      - 4 numeric values (already type-coerced by caller)
      - -180 <= W, E <= 180; -90 <= S, N <= 90
      - W < E (no crossing of antimeridian; for that, split into two bboxes)
      - S < N
      - width / height strictly positive (no zero-area)
    Raises ValidationError (exit 6) on any failure.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(f"bbox must be 4 floats [W S E N], got: {bbox}")
    w, s, e, n = (float(v) for v in bbox)
    for label, val, lo, hi in (("W", w, -180.0, 180.0), ("E", e, -180.0, 180.0),
                               ("S", s, -90.0, 90.0), ("N", n, -90.0, 90.0)):
        if val < lo or val > hi:
            raise ValidationError(
                f"bbox {label}={val} out of range [{lo}, {hi}]; got bbox={bbox}"
            )
    if w >= e:
        raise ValidationError(
            f"bbox W={w} must be < E={e} (no antimeridian crossing; "
            f"if needed, split into two bboxes)"
        )
    if s >= n:
        raise ValidationError(
            f"bbox S={s} must be < N={n}"
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero or negative area: width={e - w:.3e}, height={n - s:.3e}"
        )
    return w, s, e, n


def validate_tolerance(tol):
    """Tolerance must be a finite non-negative float."""
    try:
        f = float(tol)
    except (TypeError, ValueError):
        raise ValidationError(f"tolerance must be numeric, got: {tol!r}")
    if f != f or f in (float("inf"), float("-inf")):
        raise ValidationError(f"tolerance must be finite, got: {f}")
    if f < 0:
        raise ValidationError(f"tolerance must be >= 0, got: {f}")
    return f

# ---- 共享核心库（本地 vendored，随脚本目录一起分发）----
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


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def _perp_distance(p, a, b) -> float:
    """点 p 到线段 ab 所在直线的垂直距离。"""
    ax, ay = a
    bx, by = b
    px, py = p
    dx, dy = bx - ax, by - ay
    seg_len2 = dx * dx + dy * dy
    if seg_len2 == 0.0:
        return float(np.hypot(px - ax, py - ay))
    num = abs(dy * px - dx * py + bx * ay - by * ax)
    return num / float(np.sqrt(seg_len2))


def douglas_peucker(coords: Sequence[Tuple[float, float]],
                    epsilon: float) -> List[Tuple[float, float]]:
    """Douglas-Peucker 线简化（迭代实现）。保留首尾点。"""
    pts = [tuple(c) for c in coords]
    n = len(pts)
    if n < 3 or epsilon < 0:
        return pts
    keep = [False] * n
    keep[0] = keep[-1] = True
    stack = [(0, n - 1)]
    while stack:
        i, j = stack.pop()
        if j <= i + 1:
            continue
        dmax = -1.0
        idx = -1
        for k in range(i + 1, j):
            d = _perp_distance(pts[k], pts[i], pts[j])
            if d > dmax:
                dmax = d
                idx = k
        if dmax > epsilon and idx != -1:
            keep[idx] = True
            stack.append((i, idx))
            stack.append((idx, j))
    return [pts[k] for k in range(n) if keep[k]]


def triangle_area(a, b, c) -> float:
    return abs((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])) / 2.0


def visvalingam_count(coords: Sequence[Tuple[float, float]],
                      target: int) -> List[Tuple[float, float]]:
    """Visvalingam-Whyatt：删除到只剩 target 个顶点（首尾必留）。"""
    pts = [tuple(c) for c in coords]
    target = max(2, int(target))
    while len(pts) > target:
        min_area = float("inf")
        min_idx = -1
        for i in range(1, len(pts) - 1):
            a = triangle_area(pts[i - 1], pts[i], pts[i + 1])
            if a < min_area:
                min_area = a
                min_idx = i
        if min_idx == -1:
            break
        pts.pop(min_idx)
    return pts


def visvalingam_threshold(coords: Sequence[Tuple[float, float]],
                          threshold: float) -> List[Tuple[float, float]]:
    """Visvalingam-Whyatt：删除有效面积 < threshold 的内部点。"""
    pts = [tuple(c) for c in coords]
    changed = True
    while changed and len(pts) > 2:
        changed = False
        min_area = float("inf")
        min_idx = -1
        for i in range(1, len(pts) - 1):
            a = triangle_area(pts[i - 1], pts[i], pts[i + 1])
            if a < min_area:
                min_area = a
                min_idx = i
        if min_idx != -1 and min_area < threshold:
            pts.pop(min_idx)
            changed = True
    return pts


def simplify_coords(coords: Sequence[Tuple[float, float]], method: str,
                    tolerance: float, target: Optional[int] = None
                    ) -> List[Tuple[float, float]]:
    if method == "douglas-peucker":
        return douglas_peucker(coords, tolerance)
    if method == "visvalingam":
        if target:
            return visvalingam_count(coords, target)
        # tolerance 作为面积阈值；面积量级与坐标平方相关
        return visvalingam_threshold(coords, tolerance)
    raise UsageError(f"unknown method '{method}'. Choose from: {sorted(METHODS)}")


def _simplify_ring(coords, method, tolerance, target) -> List[Tuple[float, float]]:
    """简化闭合环：去重尾点 → 简化 → 保证 ≥3 点 → 重新闭合。"""
    pts = [tuple(c) for c in coords]
    closed = len(pts) >= 2 and pts[0] == pts[-1]
    open_pts = pts[:-1] if closed else pts
    simp = simplify_coords(open_pts, method, tolerance, target)
    if len(simp) < 3:
        simp = open_pts[:3] if len(open_pts) >= 3 else list(open_pts)
    return simp + [simp[0]]


def simplify_geometry(geom: Any, method: str, tolerance: float,
                      target: Optional[int] = None) -> Any:
    """对单个 shapely 几何做简化，返回新几何。"""
    from shapely.geometry import (
        LineString, MultiLineString, Polygon, MultiPolygon,
        GeometryCollection, Point,
    )
    if geom is None or geom.is_empty:
        return geom
    gt = geom.geom_type
    if gt == "Point":
        return geom
    if gt == "LineString":
        simp = simplify_coords(list(geom.coords), method, tolerance, target)
        return LineString(simp) if len(simp) >= 2 else geom
    if gt == "MultiLineString":
        return MultiLineString([simplify_geometry(g, method, tolerance, target)
                                for g in geom.geoms])
    if gt == "Polygon":
        ext = _simplify_ring(list(geom.exterior.coords), method, tolerance, target)
        holes = [_simplify_ring(list(r.coords), method, tolerance, target)
                 for r in geom.interiors]
        try:
            return Polygon(ext, holes)
        except Exception:  # noqa: BLE001
            return geom
    if gt == "MultiPolygon":
        return MultiPolygon([simplify_geometry(g, method, tolerance, target)
                             for g in geom.geoms])
    if gt == "GeometryCollection":
        return GeometryCollection([simplify_geometry(g, method, tolerance, target)
                                   for g in geom.geoms])
    return geom


def vertex_count(geom: Any) -> int:
    """统计一个几何的顶点总数。"""
    if geom is None or geom.is_empty:
        return 0
    gt = geom.geom_type
    if gt in ("Point",):
        return 1
    if gt == "LineString":
        return len(geom.coords)
    if gt == "Polygon":
        return len(geom.exterior.coords) + sum(len(r.coords) for r in geom.interiors)
    if gt.startswith("Multi") or gt == "GeometryCollection":
        return sum(vertex_count(g) for g in geom.geoms)
    return 0


def simplify_geodataframe(gdf: Any, method: str, tolerance: float,
                          target: Optional[int] = None) -> Tuple[Any, Dict[str, Any]]:
    """简化整个 GeoDataFrame，返回 (新 gdf, 统计)。"""
    import geopandas as gpd
    new_geoms = []
    in_v = out_v = 0
    area_in = area_out = 0.0
    for geom in gdf.geometry:
        in_v += vertex_count(geom)
        if geom is not None and geom.geom_type in ("Polygon", "MultiPolygon"):
            area_in += geom.area
        simp = simplify_geometry(geom, method, tolerance, target)
        out_v += vertex_count(simp)
        if simp is not None and simp.geom_type in ("Polygon", "MultiPolygon"):
            area_out += simp.area
        new_geoms.append(simp)

    out_gdf = gdf.copy()
    out_gdf["geometry"] = new_geoms
    reduction = (1.0 - out_v / in_v) if in_v else 0.0
    area_retention = (area_out / area_in) if area_in > 0 else 1.0
    stats = {
        "method": method,
        "tolerance": tolerance,
        "target_vertices": target,
        "input_vertices": int(in_v),
        "output_vertices": int(out_v),
        "vertex_reduction": int(in_v - out_v),
        "vertex_reduction_pct": round(float(reduction) * 100.0, 2),
        "area_retention": round(float(area_retention), 6),
    }
    return out_gdf, stats


# ---------------------------------------------------------------------------
# 合成数据：高密度圆与锯齿线
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], n_circles: int = 3,
                       vertices: int = 64, seed: int = 42) -> Any:
    import geopandas as gpd
    from shapely.geometry import Polygon, LineString
    from pyproj import CRS

    rng = np.random.default_rng(seed)
    w, s, e, n_ = bbox
    geoms, attrs = [], {"id": [], "kind": []}
    cx = np.linspace(w + (e - w) * 0.2, e - (e - w) * 0.2, n_circles)
    cy = (s + n_) / 2.0
    r = (e - w) * 0.08
    for i, x in enumerate(cx):
        ang = np.linspace(0, 2 * np.pi, vertices, endpoint=False)
        ring = [(x + r * np.cos(a), cy + r * np.sin(a)) for a in ang]
        ring.append(ring[0])
        geoms.append(Polygon(ring))
        attrs["id"].append(i + 1)
        attrs["kind"].append("circle")
    # 一条锯齿线
    xs = np.linspace(w, e, vertices)
    ys = s + (n_ - s) * 0.2 + rng.normal(0, (n_ - s) * 0.01, vertices)
    geoms.append(LineString(list(zip(xs, ys))))
    attrs["id"].append(n_circles + 1)
    attrs["kind"].append("zigzag")
    return gpd.GeoDataFrame(attrs, geometry=geoms, crs=CRS.from_epsg(4326))


def write_geojson(path: str, gdf: Any) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    if len(gdf) == 0:
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"type": "FeatureCollection", "features": []}, f)
        return
    gdf.to_file(path, driver="GeoJSON")


def read_vector(path: str) -> Any:
    import geopandas as gpd
    if not os.path.exists(path):
        raise UsageError(f"input vector not found: {path}", path=path)
    try:
        return gpd.read_file(path)
    except Exception as exc:  # noqa: BLE001
        raise ValidationError(f"failed to read vector '{path}': {exc}") from exc


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(
    output_dir: str,
    args: argparse.Namespace,
    outputs: List[Dict[str, Any]],
    qa: Dict[str, Any],
    started_at: str,
    exit_code: int,
    bbox: Optional[List[float]],
) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME,
        skill_version=VERSION,
        command=cmd,
        started_at=started_at,
        finished_at=_utc_now(),
        exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "method": getattr(args, "method", None),
            "tolerance": getattr(args, "tolerance", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
            "bbox": bbox,
        },
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

    # ---- P0/P1: validate all inputs BEFORE creating output directory ----
    if bbox is not None:
        bbox = list(validate_bbox(bbox))
    args.tolerance = validate_tolerance(args.tolerance)

    os.makedirs(output_dir, exist_ok=True)

    if args.input and not args.synthetic:
        gdf = read_vector(args.input)
        if bbox is None and gdf.crs is not None:
            b = gdf.total_bounds
            bbox = [float(b[0]), float(b[1]), float(b[2]), float(b[3])]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <vector>")
        gdf = generate_synthetic(bbox)
        source_note = "synthetic"

    if len(gdf) == 0:
        raise ValidationError("input vector has no features")

    out_gdf, stats = simplify_geodataframe(gdf, args.method, args.tolerance)
    stats["source"] = source_note

    out_geojson = os.path.join(output_dir, "simplified.geojson")
    write_geojson(out_geojson, out_gdf)
    stats_path = os.path.join(output_dir, "simplification_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2, default=str)

    qa = {
        "source": source_note,
        "method": args.method,
        "n_features": int(len(out_gdf)),
        "input_vertices": stats["input_vertices"],
        "output_vertices": stats["output_vertices"],
        "vertex_reduction_pct": stats["vertex_reduction_pct"],
        "area_retention": stats["area_retention"],
    }
    outputs = [
        {"path": out_geojson, "kind": "vector", "feature_count": int(len(out_gdf))},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  tolerance: {args.tolerance}")
        print(f"[{SKILL_NAME}] vertices: {stats['input_vertices']} -> {stats['output_vertices']} "
              f"(-{stats['vertex_reduction_pct']}%)")
        print(f"[{SKILL_NAME}] area retention: {stats['area_retention']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_geojson}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Simplify vector geometries with Douglas-Peucker / Visvalingam.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input vector file")
    p.add_argument("--method", default="douglas-peucker", choices=sorted(METHODS),
                   help="simplification method (default: douglas-peucker)")
    p.add_argument("--tolerance", type=float, default=0.001,
                   help="DP distance tolerance / Visvalingam area threshold (default: 0.001)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate synthetic high-vertex features (offline)")
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
