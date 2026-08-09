#!/usr/bin/env python3
"""least-cost-path — 最小成本路径

基于成本栅格，用 Dijkstra 算法计算从源点到全图的最小累积成本距离（cost
distance）及回溯链接（backlink），再从目标点回溯提取最小成本路径。
支持 8 邻域（对角线距离按 √2 加权）。输出成本距离栅格与路径 GeoJSON。

数据源：本地成本 GeoTIFF，或 --synthetic 生成模拟成本面。

隐私声明 / Privacy：
- 默认离线运行，不发起任何网络请求。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python least-cost-path.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "least-cost-path"

# ---------------------------------------------------------------------------
# Input validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate geographic bbox: W<E, S<N, lat in [-90,90], lon in [-180,180]."""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be [W, S, E, N] with 4 floats")
    w, s, e, n = [float(x) for x in bbox]
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError("bbox contains non-finite values")
    if w < -180.0 or e > 180.0 or s < -90.0 or n > 90.0:
        raise ValidationError(
            f"bbox out of range: lon=[{w},{e}] must be in [-180,180], lat=[{s},{n}] in [-90,90]")
    if w >= e:
        raise ValidationError(
            f"bbox W must be < E; got W={w}, E={e} (likely reversed; this skill does not support wrapping around 180°)")
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N; got S={s}, N={n} (likely reversed)")
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(f"bbox has zero area: W={w}, E={e}, S={s}, N={n}")


def validate_grid_params(args) -> None:
    """Validate --grid-size / --source-*/--dest-* against each other."""
    if args.grid_size is not None and args.grid_size < 2:
        raise ValidationError(f"--grid-size must be >= 2, got {args.grid_size}")
    for nm in ("source_row", "source_col", "dest_row", "dest_col"):
        v = getattr(args, nm)
        if v is not None and v < 0:
            raise ValidationError(f"--{nm} must be >= 0, got {v}")


def read_geotiff_with_nodata(path: str):
    """Read cost GeoTIFF, replacing NoData with NaN; return (data, bbox)."""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        data = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nd = src.nodata
    if nd is not None and np.isfinite(float(nd)):
        data = np.where(data == float(nd), np.nan, data).astype(np.float32)
    return data, bbox

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


# 8 邻域偏移与距离权重
_NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
_SQRT2 = np.sqrt(2.0)


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def dijkstra_cost_distance(
    cost: np.ndarray, source: Tuple[int, int],
) -> Tuple[np.ndarray, np.ndarray]:
    """Dijkstra 计算最小累积成本距离与回溯链接。

    邻接成本 = 0.5 * (cost_i + cost_j) * 邻域距离权重。

    Parameters
    ----------
    cost : (H, W) 单位成本（>0）
    source : (row, col)

    Returns
    -------
    dist : (H, W) float64 累积成本距离
    back : (H, W) int32 回溯邻居索引（0..7），源点为 -1
    """
    if not (0 <= source[0] < cost.shape[0] and 0 <= source[1] < cost.shape[1]):
        raise ValidationError(f"source {source} out of bounds")
    if np.any(cost < 0):
        raise ValidationError("cost surface has negative values")

    h, w = cost.shape
    INF = np.inf
    dist = np.full((h, w), INF, dtype=np.float64)
    back = np.full((h, w), -2, dtype=np.int32)
    dist[source] = 0.0
    back[source] = -1

    heap = [(0.0, source[0], source[1])]
    visited = np.zeros((h, w), dtype=bool)

    while heap:
        d, r, c = heapq.heappop(heap)
        if visited[r, c]:
            continue
        visited[r, c] = True
        c_from = cost[r, c]
        for k, (dr, dc) in enumerate(_NEIGHBORS):
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                continue
            if visited[nr, nc]:
                continue
            step_dist = _SQRT2 if (dr != 0 and dc != 0) else 1.0
            edge_cost = 0.5 * (c_from + cost[nr, nc]) * step_dist
            nd = d + edge_cost
            if nd < dist[nr, nc]:
                dist[nr, nc] = nd
                back[nr, nc] = k  # 记录从邻居回溯到 (r,c) 的方向
                heapq.heappush(heap, (nd, nr, nc))
    return dist, back


def extract_path(back: np.ndarray, dest: Tuple[int, int],
                 source: Tuple[int, int]) -> List[Tuple[int, int]]:
    """从目标点沿 backlink 回溯到源点，返回像元路径 (row, col) 列表（源→目标）。"""
    if not (0 <= dest[0] < back.shape[0] and 0 <= dest[1] < back.shape[1]):
        raise ValidationError(f"dest {dest} out of bounds")
    if back[dest] == -2:
        raise ValidationError("destination unreachable from source")
    path = []
    cur = dest
    guard = 0
    max_iter = back.size + 5
    while True:
        path.append(cur)
        if cur == source:
            break
        k = back[cur]
        if k < 0:
            break
        dr, dc = _NEIGHBORS[k]
        # back 存的是“从哪个邻居来的”，cur 的前驱是 cur - (dr,dc)
        cur = (cur[0] - dr, cur[1] - dc)
        guard += 1
        if guard > max_iter:
            raise ProcessError("backtracking did not converge")
    path.reverse()
    if path[0] != source:
        raise ProcessError("backtracked path does not start at source")
    return path


def path_cost(cost: np.ndarray, path: List[Tuple[int, int]]) -> float:
    """沿路径累加邻接成本（与 dijkstra 一致的度量）。"""
    total = 0.0
    for i in range(1, len(path)):
        r0, c0 = path[i - 1]
        r1, c1 = path[i]
        step = _SQRT2 if (r0 != r1 and c0 != c1) else 1.0
        total += 0.5 * (cost[r0, c0] + cost[r1, c1]) * step
    return float(total)


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], grid_size: int = 48, seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成合成成本面：低背景 + 一条高成本障碍带。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:grid_size, 0:grid_size]
    cost = np.ones((grid_size, grid_size), dtype=np.float32)
    # 中部垂直障碍带（留一个缺口）
    mid = grid_size // 2
    cost[:, mid - 1:mid + 2] = 50.0
    gap = grid_size // 4
    cost[gap - 2:gap + 2, mid - 1:mid + 2] = 1.0
    cost += rng.uniform(0, 0.3, (grid_size, grid_size)).astype(np.float32)
    info = {"grid_size": grid_size, "cost_range": [float(cost.min()), float(cost.max())]}
    return cost, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if array.ndim == 2:
        array = array[np.newaxis, ...]
    if array.ndim != 3:
        raise ValidationError("write_geotiff expects a 2D or 3D array")
    nb, hh, ww = array.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], ww, hh)
    profile = {
        "driver": "GTiff", "height": hh, "width": ww, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(array[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        data = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nd = src.nodata
    if nd is not None and np.isfinite(float(nd)):
        data = np.where(data == float(nd), np.nan, data).astype(np.float32)
    return data, bbox


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
    started_at = _utc_now()
    output_dir = args.output_dir

    bbox = list(args.bbox) if args.bbox else None
    validate_grid_params(args)

    if args.input and not args.synthetic:
        data, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        cost = data[0] if data.ndim == 3 else data
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        cost, _ = generate_synthetic(bbox, grid_size=args.grid_size)
        source_note = "synthetic"

    if cost.size == 0:
        raise ValidationError("cost raster is empty")
    # Reject if entire cost raster is NoData
    if not np.any(np.isfinite(cost)):
        raise ValidationError(
            "cost raster has no valid pixels (entirely NoData/NaN)")
    # Replace NaN with a high-cost fallback so dijkstra can route around NoData
    # (NaN-as-barrier is a defensible default; user can pre-clean if needed)
    cost = np.where(np.isfinite(cost), cost, 1e6).astype(np.float32)
    cost = np.clip(cost, 1e-6, None)
    if cost.size < 4:
        raise ValidationError("cost raster too small")
    gs = args.grid_size
    if cost.shape[0] != gs or cost.shape[1] != gs:
        from scipy.ndimage import zoom
        cost = zoom(cost, (gs / cost.shape[0], gs / cost.shape[1]), order=1).astype(np.float32)

    h, w = cost.shape
    src = (args.source_row, args.source_col)
    dst = (args.dest_row, args.dest_col)
    if not (0 <= src[0] < h and 0 <= src[1] < w):
        raise UsageError(f"source {src} out of grid {h}x{w}")
    if not (0 <= dst[0] < h and 0 <= dst[1] < w):
        raise UsageError(f"dest {dst} out of grid {h}x{w}")

    os.makedirs(output_dir, exist_ok=True)

    dist, back = dijkstra_cost_distance(cost, src)
    if not np.isfinite(dist[dst]):
        raise ProcessError("destination unreachable")
    path = extract_path(back, dst, src)
    pcost = path_cost(cost, path)

    # 坐标转换：像元 → 经纬度
    xs = np.linspace(bbox[0], bbox[2], w)
    ys = np.linspace(bbox[3], bbox[1], h)
    coords = [[float(xs[c]), float(ys[r])] for r, c in path]

    out_tif = os.path.join(output_dir, "cost_distance.tif")
    dist_out = np.where(np.isfinite(dist), dist, -9999.0).astype(np.float32)
    write_geotiff(out_tif, dist_out, bbox)

    path_geojson = os.path.join(output_dir, "least_cost_path.geojson")
    feat = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "properties": {"source": list(src), "dest": list(dst),
                           "path_cost": pcost, "n_cells": len(path)},
            "geometry": {"type": "LineString", "coordinates": coords},
        }],
    }
    with open(path_geojson, "w", encoding="utf-8") as f:
        json.dump(feat, f, ensure_ascii=False, indent=2)

    qa = {
        "source": source_note,
        "grid_shape": [int(h), int(w)],
        "src": list(src), "dst": list(dst),
        "path_cost": pcost,
        "path_cells": len(path),
        "max_cost_distance": float(dist[np.isfinite(dist)].max()),
        "n_valid_pixels": int(np.isfinite(dist).sum()),
        "n_total_pixels": int(dist.size),
    }
    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": path_geojson, "kind": "vector", "crs_epsg": 4326},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] path {src} -> {dst}")
        print(f"[{SKILL_NAME}] path cost: {pcost:.3f}  cells: {len(path)}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Least-cost path via Dijkstra cost distance + backlink + path extraction.",
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input cost GeoTIFF")
    p.add_argument("--grid-size", type=int, default=48, help="working grid size (default: 48)")
    p.add_argument("--source-row", type=int, default=24, help="source row (default: 24)")
    p.add_argument("--source-col", type=int, default=4, help="source col (default: 4)")
    p.add_argument("--dest-row", type=int, default=24, help="dest row (default: 24)")
    p.add_argument("--dest-col", type=int, default=44, help="dest col (default: 44)")
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
