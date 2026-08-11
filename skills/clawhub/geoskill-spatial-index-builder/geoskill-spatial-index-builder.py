#!/usr/bin/env python3
"""spatial-index-builder — 空间索引构建

构建三种空间索引并统计查询性能，结果与暴力搜索严格对齐：

- **R-tree**：基于 shapely ``STRtree``，用 ``predicate="intersects"`` 做精确
  相交查询。
- **Quadtree**：自实现四叉树，按外包矩形递归四分，查询时只遍历与窗口相交
  的节点。
- **GeoHash**：自实现 GeoHash 编解码，按质心 cell 建倒排表，查询时枚举覆盖
  窗口的所有 cell 再精确过滤。

每种索引对一批查询窗口计时，并与暴力扫描比较结果一致性与加速比。

数据源：``--input`` 矢量文件，或 ``--synthetic`` 模式生成随机点集（离线）。

隐私声明 / Privacy：
- 默认完全离线运行，``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python spatial-index-builder.py --input pois.shp --queries 20
    python spatial-index-builder.py --bbox 116 39 117 40 --synthetic --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import math
import os
import sys
import time
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "spatial-index-builder"

# GeoHash base32 字符表
_GEOHASH_BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"

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
# 校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> None:
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


def validate_params(features: int, queries: int, precision: int) -> None:
    if features < 1:
        raise ValidationError(f"--features must be >= 1, got {features}")
    if queries < 1:
        raise ValidationError(f"--queries must be >= 1, got {queries}")
    if not (1 <= precision <= 12):
        raise ValidationError(f"--precision must be in [1, 12], got {precision}")


# ---------------------------------------------------------------------------
# 通用：暴力查询与精确过滤
# ---------------------------------------------------------------------------
def query_brute(geoms: Sequence[Any], bbox: Sequence[float]) -> List[int]:
    """暴力扫描：返回几何与 bbox 相交的要素索引。"""
    from shapely.geometry import box
    win = box(*bbox)
    return [i for i, g in enumerate(geoms)
            if g is not None and not g.is_empty and g.intersects(win)]


def refine(geoms: Sequence[Any], candidates: Sequence[int],
           bbox: Sequence[float]) -> List[int]:
    """把候选索引精确过滤为几何真正与 bbox 相交者（去重 + 排序）。"""
    from shapely.geometry import box
    win = box(*bbox)
    return sorted({i for i in candidates
                   if geoms[i] is not None and geoms[i].intersects(win)})


def _envelope(g: Any) -> Optional[Tuple[float, float, float, float]]:
    if g is None or g.is_empty:
        return None
    return g.bounds


# ---------------------------------------------------------------------------
# R-tree（shapely STRtree）
# ---------------------------------------------------------------------------
def build_rtree(geoms: Sequence[Any]) -> Any:
    from shapely import STRtree
    # STRtree 需要非 None 几何；用空几何占位以保持索引对齐
    from shapely.geometry import Point
    safe = [g if (g is not None) else Point() for g in geoms]
    return STRtree(safe)


def query_rtree(tree: Any, geoms: Sequence[Any], bbox: Sequence[float]) -> List[int]:
    from shapely.geometry import box
    idx = tree.query(box(*bbox), predicate="intersects")
    # 排除占位空几何
    return sorted(int(i) for i in idx
                  if geoms[i] is not None and not geoms[i].is_empty
                  and geoms[i].intersects(box(*bbox)))


# ---------------------------------------------------------------------------
# Quadtree（自实现）
# ---------------------------------------------------------------------------
class QuadTree:
    """按外包矩形存储要素索引的四叉树。"""

    def __init__(self, bounds: Tuple[float, float, float, float],
                 capacity: int = 8, max_depth: int = 12, depth: int = 0):
        self.bounds = bounds  # (minx, miny, maxx, maxy)
        self.capacity = capacity
        self.max_depth = max_depth
        self.depth = depth
        self.items: List[Tuple[int, Tuple[float, float, float, float]]] = []
        self.children: Optional[List["QuadTree"]] = None

    def _contains(self, env: Tuple[float, float, float, float]) -> bool:
        b = self.bounds
        return env[0] >= b[0] and env[2] <= b[2] and env[1] >= b[1] and env[3] <= b[3]

    def _intersects(self, env: Tuple[float, float, float, float]) -> bool:
        b = self.bounds
        return not (env[2] < b[0] or env[0] > b[2] or env[3] < b[1] or env[1] > b[3])

    def _subdivide(self) -> None:
        minx, miny, maxx, maxy = self.bounds
        mx, my = (minx + maxx) / 2, (miny + maxy) / 2
        d = self.depth + 1
        self.children = [
            QuadTree((minx, miny, mx, my), self.capacity, self.max_depth, d),
            QuadTree((mx, miny, maxx, my), self.capacity, self.max_depth, d),
            QuadTree((minx, my, mx, maxy), self.capacity, self.max_depth, d),
            QuadTree((mx, my, maxx, maxy), self.capacity, self.max_depth, d),
        ]

    def insert(self, index: int, env: Tuple[float, float, float, float]) -> None:
        if not self._intersects(env):
            return
        if self.children is None:
            if len(self.items) < self.capacity or self.depth >= self.max_depth:
                self.items.append((index, env))
                return
            self._subdivide()
            # 把已存要素重新下放
            old = self.items
            self.items = []
            for idx, e in old:
                self._place(idx, e)
        self._place(index, env)

    def _place(self, index: int, env: Tuple[float, float, float, float]) -> None:
        # 若有子节点且 env 能完整落入某个子节点，则下放；否则留在本节点
        if self.children is not None:
            for c in self.children:
                if c._contains(env):
                    c.insert(index, env)
                    return
        self.items.append((index, env))

    def query(self, bbox: Tuple[float, float, float, float]) -> List[int]:
        result: List[int] = []
        self._query(bbox, result)
        return result

    def _query(self, bbox: Tuple[float, float, float, float], out: List[int]) -> None:
        if not self._intersects(bbox):
            return
        for idx, env in self.items:
            if not (env[2] < bbox[0] or env[0] > bbox[2]
                    or env[3] < bbox[1] or env[1] > bbox[3]):
                out.append(idx)
        if self.children is not None:
            for c in self.children:
                c._query(bbox, out)


def build_quadtree(geoms: Sequence[Any],
                   bounds: Optional[Tuple[float, float, float, float]] = None) -> QuadTree:
    envs = [_envelope(g) for g in geoms]
    valid = [e for e in envs if e is not None]
    if bounds is None:
        if not valid:
            bounds = (0.0, 0.0, 1.0, 1.0)
        else:
            bounds = (min(e[0] for e in valid), min(e[1] for e in valid),
                      max(e[2] for e in valid), max(e[3] for e in valid))
    tree = QuadTree(bounds)
    for i, e in enumerate(envs):
        if e is not None:
            tree.insert(i, e)
    return tree


# ---------------------------------------------------------------------------
# GeoHash（自实现）
# ---------------------------------------------------------------------------
def geohash_encode(lon: float, lat: float, precision: int = 6) -> str:
    lat_range = [-90.0, 90.0]
    lon_range = [-180.0, 180.0]
    bits = 0
    bit_count = 0
    even = True  # 先经度
    out = []
    while len(out) < precision:
        if even:
            mid = (lon_range[0] + lon_range[1]) / 2
            if lon >= mid:
                bits = bits * 2 + 1
                lon_range[0] = mid
            else:
                bits = bits * 2
                lon_range[1] = mid
        else:
            mid = (lat_range[0] + lat_range[1]) / 2
            if lat >= mid:
                bits = bits * 2 + 1
                lat_range[0] = mid
            else:
                bits = bits * 2
                lat_range[1] = mid
        even = not even
        bit_count += 1
        if bit_count == 5:
            out.append(_GEOHASH_BASE32[bits])
            bits = 0
            bit_count = 0
    return "".join(out)


def geohash_cell_size(precision: int) -> Tuple[float, float]:
    """返回指定精度下单个 cell 的 (lon_width, lat_height)（度）。"""
    total_bits = 5 * precision
    lon_bits = (total_bits + 1) // 2  # 经度先分，多一位
    lat_bits = total_bits // 2
    return 360.0 / (2 ** lon_bits), 180.0 / (2 ** lat_bits)


def build_geohash(geoms: Sequence[Any], precision: int = 6,
                  max_cells_per_geom: int = 20000) -> Dict[str, List[int]]:
    """按几何外包矩形覆盖的所有 geohash cell 建倒排表。

    用外包矩形而非仅质心，保证“几何与窗口相交 ⇒ 至少一个索引 cell 落在
    窗口内”，避免多边形质心在窗口外造成的漏检。
    """
    index: Dict[str, List[int]] = {}
    for i, g in enumerate(geoms):
        if g is None or g.is_empty:
            continue
        minx, miny, maxx, maxy = g.bounds
        cells = geohash_cells_in_bbox([minx, miny, maxx, maxy], precision,
                                      max_cells=max_cells_per_geom)
        if not cells:  # 超大几何兜底：退回代表点
            c = g.representative_point()
            cells = [geohash_encode(c.x, c.y, precision)]
        for gh in cells:
            index.setdefault(gh, []).append(i)
    return index


def geohash_cells_in_bbox(bbox: Sequence[float], precision: int,
                          max_cells: int = 100000) -> List[str]:
    """枚举与 bbox 相交的所有 geohash cell（网格对齐，精确）。

    geohash cell 网格以 (-180, -90) 为原点，宽 lon_w、高 lat_h。
    """
    w, s, e, n = bbox
    lon_w, lat_h = geohash_cell_size(precision)
    i_min = int(math.floor((w + 180.0) / lon_w))
    i_max = int(math.floor((e + 180.0) / lon_w))
    j_min = int(math.floor((s + 90.0) / lat_h))
    j_max = int(math.floor((n + 90.0) / lat_h))
    if (i_max - i_min + 1) * (j_max - j_min + 1) > max_cells:
        return []
    cells = set()
    for i in range(i_min, i_max + 1):
        lon = -180.0 + (i + 0.5) * lon_w
        lon = min(max(lon, -179.999999), 179.999999)
        for j in range(j_min, j_max + 1):
            lat = -90.0 + (j + 0.5) * lat_h
            lat = min(max(lat, -89.999999), 89.999999)
            cells.add(geohash_encode(lon, lat, precision))
    return sorted(cells)


def query_geohash(index: Dict[str, List[int]], geoms: Sequence[Any],
                  bbox: Sequence[float], precision: int) -> List[int]:
    cells = geohash_cells_in_bbox(bbox, precision)
    candidates: List[int] = []
    for c in cells:
        candidates.extend(index.get(c, []))
    return refine(geoms, candidates, bbox)


# ---------------------------------------------------------------------------
# 基准测试
# ---------------------------------------------------------------------------
def benchmark(geoms: Sequence[Any], windows: Sequence[Sequence[float]],
              precision: int = 6) -> Dict[str, Any]:
    """对三种索引 + 暴力扫描跑全部窗口，统计一致性与性能。"""
    rtree = build_rtree(geoms)
    qtree = build_quadtree(geoms)
    gh = build_geohash(geoms, precision)

    # 预热 / 计时
    t0 = time.perf_counter()
    brute_results = [query_brute(geoms, w) for w in windows]
    brute_ms = (time.perf_counter() - t0) * 1000

    t0 = time.perf_counter()
    rt_results = [query_rtree(rtree, geoms, w) for w in windows]
    rt_ms = (time.perf_counter() - t0) * 1000

    t0 = time.perf_counter()
    qt_results = [refine(geoms, qtree.query(tuple(w)), w) for w in windows]
    qt_ms = (time.perf_counter() - t0) * 1000

    t0 = time.perf_counter()
    gh_results = [query_geohash(gh, geoms, w, precision) for w in windows]
    gh_ms = (time.perf_counter() - t0) * 1000

    n = len(windows)
    rt_ok = all(rt_results[i] == brute_results[i] for i in range(n))
    qt_ok = all(qt_results[i] == brute_results[i] for i in range(n))
    gh_ok = all(gh_results[i] == brute_results[i] for i in range(n))

    def stats(ms, ok, results, name):
        avg_hits = float(np.mean([len(r) for r in results])) if results else 0.0
        return {
            "index": name,
            "total_ms": round(float(ms), 3),
            "avg_ms": round(float(ms) / n, 4) if n else 0.0,
            "speedup_vs_brute": round(float(brute_ms) / ms, 2) if ms > 0 else None,
            "avg_hits": round(avg_hits, 2),
            "consistent_with_brute": bool(ok),
        }

    return {
        "n_features": len(geoms),
        "n_queries": n,
        "indexes": [
            stats(rt_ms, rt_ok, rt_results, "rtree"),
            stats(qt_ms, qt_ok, qt_results, "quadtree"),
            stats(gh_ms, gh_ok, gh_results, "geohash"),
            stats(brute_ms, True, brute_results, "brute_force"),
        ],
        "all_consistent": bool(rt_ok and qt_ok and gh_ok),
    }


# ---------------------------------------------------------------------------
# 合成数据 / I/O
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], n: int = 300, seed: int = 42) -> Any:
    import geopandas as gpd
    from shapely.geometry import Point
    from pyproj import CRS
    rng = np.random.default_rng(seed)
    w, s, e, n_ = bbox
    xs = rng.uniform(w, e, n)
    ys = rng.uniform(s, n_, n)
    return gpd.GeoDataFrame(
        {"id": np.arange(1, n + 1)},
        geometry=[Point(x, y) for x, y in zip(xs, ys)],
        crs=CRS.from_epsg(4326))


def random_windows(bbox: List[float], k: int = 15, seed: int = 7) -> List[List[float]]:
    rng = np.random.default_rng(seed)
    w, s, e, n_ = bbox
    wins = []
    for _ in range(k):
        x0 = rng.uniform(w, e)
        y0 = rng.uniform(s, n_)
        dx = rng.uniform(0.05, 0.3) * (e - w + 1e-9)
        dy = rng.uniform(0.05, 0.3) * (n_ - s + 1e-9)
        wins.append([x0, y0, min(x0 + dx, e), min(y0 + dy, n_)])
    return wins


def read_vector(path: str) -> Any:
    import geopandas as gpd
    if not os.path.exists(path):
        raise UsageError(f"input vector not found: {path}", path=path)
    try:
        return gpd.read_file(path)
    except Exception as exc:  # noqa: BLE001
        raise ValidationError(f"failed to read '{path}': {exc}") from exc


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
            "queries": getattr(args, "queries", None),
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
    validate_params(args.features, args.queries, args.precision)
    validate_bbox(bbox)

    if args.input and not args.synthetic:
        gdf = read_vector(args.input)
        if gdf.crs is None:
            raise ValidationError(
                f"input '{args.input}' has no coordinate reference system (CRS) defined")
        if gdf.crs.is_geographic and gdf.crs.to_epsg() != 4326:
            gdf = gdf.to_crs(epsg=4326)
        elif not gdf.crs.is_geographic:
            gdf = gdf.to_crs(epsg=4326)
        if bbox is None:
            b = gdf.total_bounds
            bbox = [float(b[0]), float(b[1]), float(b[2]), float(b[3])]
            validate_bbox(bbox)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <vector>")
        gdf = generate_synthetic(bbox, n=args.features)
        source_note = "synthetic"

    if len(gdf) == 0:
        raise ValidationError("input vector has no features")

    geoms = list(gdf.geometry)
    windows = random_windows(bbox, k=args.queries)
    result = benchmark(geoms, windows, precision=args.precision)
    result["source"] = source_note

    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "spatial_index_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2, default=str)

    qa = {
        "source": source_note,
        "n_features": result["n_features"],
        "n_queries": result["n_queries"],
        "all_consistent": result["all_consistent"],
        "indexes": {i["index"]: i["avg_ms"] for i in result["indexes"]},
    }
    outputs = [{"path": report_path, "kind": "json"}]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] features: {result['n_features']}  queries: {result['n_queries']}")
        for ix in result["indexes"]:
            print(f"[{SKILL_NAME}]   {ix['index']:<12} avg {ix['avg_ms']:.4f} ms  "
                  f"hits {ix['avg_hits']:.1f}  consistent={ix['consistent_with_brute']}")
        print(f"[{SKILL_NAME}] all consistent: {result['all_consistent']}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Build R-tree/Quadtree/GeoHash spatial indexes and benchmark queries.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input vector file")
    p.add_argument("--features", type=int, default=300,
                   help="number of synthetic points (default: 300)")
    p.add_argument("--queries", type=int, default=15,
                   help="number of benchmark query windows (default: 15)")
    p.add_argument("--precision", type=int, default=6,
                   help="geohash precision (default: 6)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate synthetic points (offline)")
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
