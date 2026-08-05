#!/usr/bin/env python3
"""urban-ventilation-corridor — 城市通风廊道分析

从建筑形态推导空气动力学粗糙度与通风潜力，并提取最小阻力通风廊道。
核心算法：

- **空气动力学粗糙度**：Macdonald 经验式
  z0 ≈ Cd/2 × λf × h × (1 − λp)，简化为 z0 = 0.1 × 建筑高度 × 平面面积密度。
  建筑越高、越密 → 粗糙度越大 → 通风越差。
- **通风潜力**：VP = exp(−k × z0)，值域 [0, 1]，随粗糙度单调递减。
- **通风廊道**：在阻力栅格（cost = 1 − VP + ε）上，用 8 邻域 Dijkstra
  求从上风缘（左缘中心）到下风缘（右缘中心）的最小阻力路径，即通风廊道。

数据源：本地建筑高度 + 足迹 GeoTIFF，或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络。

Usage:
    python urban-ventilation-corridor.py --input height.tif --footprints fp.tif
    python urban-ventilation-corridor.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "urban-ventilation-corridor"

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
def validate_bbox(bbox: Optional[List[float]]) -> List[float]:
    """Validate a [W, S, E, N] bbox in EPSG:4326.

    Rules:
      - W < E, S < N (non-degenerate)
      - lon ∈ [-180, 180], lat ∈ [-90, 90]
      - bbox area (in degree^2) must be > 0
      - cannot cross the 180° meridian (split into two if needed)
    """
    if bbox is None:
        raise ValidationError("bbox is required (provide --bbox or --input)")
    if len(bbox) != 4:
        raise ValidationError(f"bbox must have 4 floats, got {len(bbox)}")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox lon out of range [-180, 180]: W={w} E={e}",
            bbox=bbox,
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox lat out of range [-90, 90]: S={s} N={n}",
            bbox=bbox,
        )
    if w >= e:
        raise ValidationError(
            f"bbox W must be < E (got W={w} E={e}); cross-180° not supported, "
            f"split into two bboxes and merge results manually",
            bbox=bbox,
        )
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N (got S={s} N={n})",
            bbox=bbox,
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox area too small: dlon={e - w}, dlat={n - s}",
            bbox=bbox,
        )
    return [w, s, e, n]


def validate_params(args: argparse.Namespace) -> None:
    """Validate numeric parameters (roughness model + decay)."""
    if float(args.roughness_coeff) < 0:
        raise ValidationError(
            f"--roughness-coeff must be >= 0 (Macdonald coeff, got {args.roughness_coeff})",
            roughness_coeff=args.roughness_coeff,
        )
    if float(args.decay_k) < 0:
        raise ValidationError(
            f"--decay-k must be >= 0 (ventilation decay constant, got {args.decay_k})",
            decay_k=args.decay_k,
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------

def aerodynamic_roughness(
    mean_height: np.ndarray,
    plan_area_fraction: np.ndarray,
    coeff: float = 0.1,
) -> np.ndarray:
    """空气动力学粗糙度长度 z0（m）。

    Macdonald 经验式简化：z0 = coeff × h × λp，裁剪 ≥ 0。
    """
    h = np.clip(np.asarray(mean_height, dtype=np.float32), 0.0, None)
    l = np.clip(np.asarray(plan_area_fraction, dtype=np.float32), 0.0, 1.0)
    z0 = coeff * h * l
    return z0.astype(np.float32)


def ventilation_potential(roughness: np.ndarray, k: float = 0.5) -> np.ndarray:
    """通风潜力 VP = exp(−k × z0)，值域 (0, 1]，随粗糙度单调递减。"""
    z0 = np.clip(np.asarray(roughness, dtype=np.float32), 0.0, None)
    vp = np.exp(-k * z0)
    return vp.astype(np.float32)


def least_cost_path(
    cost: np.ndarray,
    start: Tuple[int, int],
    end: Tuple[int, int],
) -> Tuple[List[Tuple[int, int]], float]:
    """8 邻域 Dijkstra 最小阻力路径。

    对角线步长 √2，正交步长 1；节点代价取进入该节点的 cost。
    返回 (path, total_cost)。path 为 (row, col) 列表，含首尾。
    """
    cost = np.asarray(cost, dtype=np.float64)
    h, w = cost.shape
    sr, sc = start
    er, ec = end
    INF = float("inf")
    dist = np.full((h, w), INF, dtype=np.float64)
    prev: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {}
    dist[sr, sc] = cost[sr, sc]
    pq = [(dist[sr, sc], sr, sc)]
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
                 (1, -1), (1, 0), (1, 1)]

    while pq:
        d, r, c = heapq.heappop(pq)
        if (r, c) == (er, ec):
            break
        if d > dist[r, c]:
            continue
        for dr, dc in neighbors:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w:
                step = 1.4142135623730951 if (dr != 0 and dc != 0) else 1.0
                nd = d + step * float(cost[nr, nc])
                if nd < dist[nr, nc]:
                    dist[nr, nc] = nd
                    prev[(nr, nc)] = (r, c)
                    heapq.heappush(pq, (nd, nr, nc))

    # 回溯路径
    path: List[Tuple[int, int]] = []
    cur: Optional[Tuple[int, int]] = (er, ec)
    if not np.isfinite(dist[er, ec]):
        return path, INF
    while cur is not None:
        path.append(cur)
        cur = prev.get(cur)
    path.reverse()
    return path, float(dist[er, ec])


def path_to_geojson(path: List[Tuple[int, int]], bbox: List[float],
                    height_px: int, width: int) -> Dict[str, Any]:
    """把像元路径转为 GeoJSON LineString（WGS84 经纬度）。

    用 shapely 构建线几何并序列化（mapping），保证矢量产物符合 GeoJSON 规范。
    """
    from shapely.geometry import LineString, mapping
    if not path:
        return {"type": "FeatureCollection", "features": []}
    w_lon = (bbox[2] - bbox[0]) / max(width, 1)
    h_lat = (bbox[3] - bbox[1]) / max(height_px, 1)
    coords = []
    for r, c in path:
        lon = bbox[0] + (c + 0.5) * w_lon
        lat = bbox[3] - (r + 0.5) * h_lat
        coords.append((round(lon, 6), round(lat, 6)))
    line = LineString(coords)
    feature = {
        "type": "Feature",
        "properties": {"n_vertices": len(coords), "length_deg": float(line.length)},
        "geometry": mapping(line),
    }
    return {"type": "FeatureCollection", "features": [feature]}


# ---------------------------------------------------------------------------
# 合成数据：建筑高度 + 足迹，中间留一条低矮通风廊道
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height_px: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成建筑高度 + 足迹。

    城区建筑高 20-40 m、密度 0.5，但中部横贯一条宽 12 像元的低矮绿带
    （高 2 m、密度 0.1），构成天然通风廊道。
    """
    rng = np.random.default_rng(seed)
    height = np.zeros((height_px, width), dtype=np.float32)
    density = np.zeros((height_px, width), dtype=np.float32)

    corridor_half = 6
    mid = height_px // 2
    for r in range(height_px):
        for c in range(width):
            if abs(r - mid) <= corridor_half:
                # 通风廊道：低矮稀疏
                height[r, c] = 2.0
                density[r, c] = 0.1
            else:
                height[r, c] = float(rng.uniform(20.0, 40.0))
                density[r, c] = float(rng.uniform(0.4, 0.6))

    info = {
        "bbox": bbox, "width": width, "height": height_px,
        "corridor_row": mid,
    }
    return height, density, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    cube: np.ndarray,
    bbox: List[float],
    nodata: float = -9999.0,
) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


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
    bbox: List[float],
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
            "footprints": getattr(args, "footprints", None),
            "roughness_coeff": getattr(args, "roughness_coeff", 0.1),
            "synthetic": bool(getattr(args, "synthetic", False)),
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

    # 1) 参数校验（前置：避免无效输入污染 output_dir）
    validate_params(args)

    bbox = list(args.bbox) if args.bbox else None

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        bbox = validate_bbox(bbox)
        height = cube[0]
        if args.footprints:
            fp_cube, _ = read_geotiff(args.footprints)
            density = np.clip(fp_cube[0], 0.0, 1.0)
        else:
            density = (height > 2.0).astype(np.float32) * 0.5
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        height, density, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    if height.size == 0:
        raise ValidationError("input raster is empty")

    # 校验通过后再创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    h_px, w_px = height.shape

    # 2) 粗糙度 → 通风潜力 → 阻力
    z0 = aerodynamic_roughness(height, density, coeff=args.roughness_coeff)
    vp = ventilation_potential(z0, k=args.decay_k)
    cost = (1.0 - vp + 0.01).astype(np.float64)  # 阻力，加 ε 保证正值

    # 3) 最小阻力廊道（左缘中心 → 右缘中心）
    start = (h_px // 2, 0)
    end = (h_px // 2, w_px - 1)
    path, total_cost = least_cost_path(cost, start, end)

    # 4) 写出栅格（band1=z0, band2=VP）
    out_tif = os.path.join(output_dir, "ventilation.tif")
    stack = np.stack([z0, vp], axis=0)
    write_geotiff(out_tif, stack, bbox)

    # 5) 写出廊道 GeoJSON
    geojson = path_to_geojson(path, bbox, h_px, w_px)
    corridor_path = os.path.join(output_dir, "corridor.geojson")
    with open(corridor_path, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False)

    stats = {
        "mean_roughness_m": float(np.mean(z0)),
        "mean_ventilation_potential": float(np.mean(vp)),
        "corridor_cost": total_cost,
        "corridor_vertices": len(path),
    }
    stats_path = os.path.join(output_dir, "ventilation_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {"source": source_note}
    qa.update(stats)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 2},
        {"path": corridor_path, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": len(geojson["features"])},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean roughness z0: {stats['mean_roughness_m']:.3f} m")
        print(f"[{SKILL_NAME}] mean ventilation potential: {stats['mean_ventilation_potential']:.3f}")
        print(f"[{SKILL_NAME}] corridor cost: {stats['corridor_cost']:.3f}, vertices: {stats['corridor_vertices']}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Urban ventilation corridor from roughness and least-cost path.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input building height GeoTIFF")
    p.add_argument("--footprints", help="plan area fraction / footprint GeoTIFF")
    p.add_argument("--roughness-coeff", type=float, default=0.1,
                   help="Macdonald roughness coefficient (default: 0.1)")
    p.add_argument("--decay-k", type=float, default=0.5,
                   help="ventilation potential decay constant (default: 0.5)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic scene (offline)")
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
