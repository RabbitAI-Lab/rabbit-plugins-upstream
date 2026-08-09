#!/usr/bin/env python3
"""ecological-corridor-design — 生态廊道设计

基于栖息地适宜性构建阻力面，用最小成本路径（Dijkstra）识别生态廊道，
并计算景观连通性指数（PC / IIC）。

- 阻力面：resistance = max_suit - suitability（适宜性越低阻力越大），
- 最小成本路径：scipy.sparse.csgraph.dijkstra 在 4-邻域栅格图上求最短路径，
- 连通性指数：PC（Probability of Connectivity）或 IIC（Integral Index of Connectivity）。

数据源：--synthetic 生成适宜性栅格 + 源/汇点；--input 读取适宜性栅格。

隐私声明 / Privacy：
- 完全离线运行。

Usage:
    python ecological-corridor-design.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "ecological-corridor-design"

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
# Input validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> None:
    """Validate a [W, S, E, N] geographic bbox (exit 6 on failure)."""
    w, s, e, n = bbox
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError(
            f"bbox contains non-finite values: W={w} S={s} E={e} N={n}",
            bbox=list(bbox),
        )
    if abs(w) > 180.0 or abs(e) > 180.0:
        raise ValidationError(
            f"bbox longitude out of range: W={w} E={e} (must be in [-180, 180])",
            bbox=list(bbox),
        )
    if abs(s) > 90.0 or abs(n) > 90.0:
        raise ValidationError(
            f"bbox latitude out of range: S={s} N={n} (must be in [-90, 90])",
            bbox=list(bbox),
        )
    if w >= e:
        raise ValidationError(
            f"bbox reversed: W ({w}) must be < E ({e}). "
            f"For antimeridian-crossing bboxes, split into W..180 and -180..E.",
            bbox=list(bbox),
        )
    if s >= n:
        raise ValidationError(
            f"bbox reversed: S ({s}) must be < N ({n})", bbox=list(bbox)
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero area: W={w} S={s} E={e} N={n}", bbox=list(bbox)
        )


def validate_params(buffer_px: int, pc_threshold: float) -> None:
    """Validate corridor & PC parameters."""
    if not isinstance(buffer_px, int) or buffer_px < 0:
        raise ValidationError(
            f"--buffer must be a non-negative integer, got {buffer_px}",
            buffer=buffer_px,
        )
    if not np.isfinite(pc_threshold) or pc_threshold < 0.0 or pc_threshold > 1.0:
        raise ValidationError(
            f"--pc-threshold must be in [0, 1], got {pc_threshold}",
            pc_threshold=pc_threshold,
        )


def read_geotiff_with_nodata(
    path: str,
) -> Tuple[np.ndarray, List[float], int]:
    """Read multi-band GeoTIFF replacing NoData with NaN; report n_valid."""
    cube, bbox = read_geotiff(path)
    import rasterio
    with rasterio.open(path) as src:
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == nodata, np.nan, cube).astype(np.float32)
    n_valid = int(np.sum(np.any(np.isfinite(cube), axis=0)))
    return cube, bbox, n_valid


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def resistance_from_suitability(suitability: np.ndarray, max_resistance: float = 100.0) -> np.ndarray:
    """阻力面 = (1 - suitability) × max_resistance + 1。suitability ∈ [0,1]。"""
    suit = np.clip(suitability, 0.0, 1.0)
    return ((1.0 - suit) * max_resistance + 1.0).astype(np.float32)


def build_graph(resistance: np.ndarray) -> Any:
    """构建 4-邻域栅格图的稀疏邻接矩阵（scipy sparse）。"""
    from scipy.sparse import lil_matrix
    h, w = resistance.shape
    n = h * w
    graph = lil_matrix((n, n), dtype=np.float64)

    for r in range(h):
        for c in range(w):
            idx = r * w + c
            # 右邻
            if c + 1 < w:
                nidx = r * w + (c + 1)
                cost = (resistance[r, c] + resistance[r, c + 1]) / 2.0
                graph[idx, nidx] = cost
                graph[nidx, idx] = cost
            # 下邻
            if r + 1 < h:
                nidx = (r + 1) * w + c
                cost = (resistance[r, c] + resistance[r + 1, c]) / 2.0
                graph[idx, nidx] = cost
                graph[nidx, idx] = cost
    return graph.tocsr()


def least_cost_path(resistance: np.ndarray, src: Tuple[int, int],
                    dst: Tuple[int, int]) -> Tuple[List[Tuple[int, int]], float]:
    """Dijkstra 最小成本路径。返回 (路径像元列表, 总成本)。"""
    from scipy.sparse.csgraph import dijkstra

    h, w = resistance.shape
    graph = build_graph(resistance)
    src_idx = src[0] * w + src[1]
    dst_idx = dst[0] * w + dst[1]

    dist, predecessors = dijkstra(graph, indices=src_idx, return_predecessors=True)
    total_cost = float(dist[dst_idx])

    # 回溯路径
    path = []
    current = dst_idx
    while current != src_idx and current >= 0:
        r, c = current // w, current % w
        path.append((r, c))
        current = predecessors[current]
    if current == src_idx:
        path.append((src[0], src[1]))
    path.reverse()
    return path, total_cost


def corridor_raster(resistance: np.ndarray, path: List[Tuple[int, int]],
                    buffer: int = 1) -> np.ndarray:
    """路径缓冲 → 廊道栅格（1=廊道, 0=非廊道）。"""
    h, w = resistance.shape
    corridor = np.zeros((h, w), dtype=np.uint8)
    for r, c in path:
        r0 = max(0, r - buffer)
        r1 = min(h, r + buffer + 1)
        c0 = max(0, c - buffer)
        c1 = min(w, c + buffer + 1)
        corridor[r0:r1, c0:c1] = 1
    return corridor


def probability_of_connectivity(suitability: np.ndarray, threshold: float = 0.5) -> float:
    """PC 指数：连通斑块面积占比的平方和（简化版）。"""
    from scipy.ndimage import label
    binary = (suitability >= threshold).astype(np.int8)
    labeled, n_features = label(binary)
    if n_features == 0:
        return 0.0
    total_area = suitability.size
    pc = 0.0
    for i in range(1, n_features + 1):
        area = float((labeled == i).sum()) / total_area
        pc += area ** 2
    return float(pc)


def generate_synthetic_corridor(bbox: List[float], width: int = 128, height: int = 128,
                                seed: int = 42) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy /= max(height - 1, 1)
    xx /= max(width - 1, 1)
    # 两个高适宜性斑块 + 中间走廊
    patch1 = np.exp(-(((xx - 0.2) ** 2 + (yy - 0.3) ** 2) / 0.02))
    patch2 = np.exp(-(((xx - 0.8) ** 2 + (yy - 0.7) ** 2) / 0.02))
    corridor_band = np.exp(-(((yy - 0.5) ** 2) / 0.01))
    suitability = np.clip(0.2 + 0.7 * patch1 + 0.7 * patch2 + 0.4 * corridor_band
                          + rng.normal(0, 0.03, (height, width)), 0, 1)
    src = (int(0.3 * height), int(0.2 * width))
    dst = (int(0.7 * height), int(0.8 * width))
    return {
        "suitability": suitability.astype(np.float32),
        "src": src, "dst": dst,
        "bbox": bbox, "width": width, "height": height,
    }


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {"driver": "GTiff", "height": h, "width": w, "count": nb,
               "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
               "nodata": nodata, "compress": "deflate"}
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
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "buffer": getattr(args, "buffer", None),
            "pc_threshold": getattr(args, "pc_threshold", None),
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
    bbox = list(args.bbox) if args.bbox else None
    # validate bbox & engineering params up front (before any disk I/O or makedirs)
    if bbox is not None:
        validate_bbox(bbox)
    validate_params(int(args.buffer), float(args.pc_threshold))

    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input raster not found: {args.input}", path=args.input)
        cube, file_bbox, n_valid = read_geotiff_with_nodata(args.input)
        if bbox is None:
            bbox = file_bbox
            validate_bbox(bbox)
        if cube.shape[0] < 1:
            raise ValidationError("input raster has no bands")
        if n_valid == 0:
            raise ValidationError(
                "input raster has no valid (non-NoData) pixels",
                n_bands=int(cube.shape[0]),
            )
        suitability = cube[0]
        h, w = suitability.shape
        # Source/destination: only use if the corresponding pixel is valid,
        # otherwise fall back to the first/last valid pixel.
        h_src, w_src = h // 4, w // 4
        h_dst, w_dst = 3 * h // 4, 3 * w // 4
        if not np.isfinite(suitability[h_src, w_src]):
            ys, xs = np.where(np.isfinite(suitability))
            if ys.size == 0:
                raise ValidationError("no valid pixels for source/destination selection")
            h_src, w_src = int(ys[0]), int(xs[0])
            h_dst, w_dst = int(ys[-1]), int(xs[-1])
        src = (h_src, w_src)
        dst = (h_dst, w_dst)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        s = generate_synthetic_corridor(bbox)
        suitability, src, dst = s["suitability"], s["src"], s["dst"]
        source_note = "synthetic"
        n_valid = int(np.sum(np.isfinite(suitability)))

    if suitability.size == 0:
        raise ValidationError("input raster is empty")

    # NoData handling: a NoData pixel in suitability is meaningless for both
    # the resistance surface and the PC binary mask. We replace remaining
    # NoData pixels with the mean of the valid pixels so that dijkstra can
    # still traverse them (a real corridor should be cautious about
    # NoData regions, but failing to produce any path here is worse).
    if not np.all(np.isfinite(suitability)):
        valid = suitability[np.isfinite(suitability)]
        if valid.size == 0:
            raise ValidationError("no finite suitability values")
        fill = float(valid.mean())
        suitability = np.where(np.isfinite(suitability), suitability, fill).astype(np.float32)

    resistance = resistance_from_suitability(suitability)
    path, total_cost = least_cost_path(resistance, src, dst)
    corridor = corridor_raster(resistance, path, buffer=args.buffer)
    pc = probability_of_connectivity(suitability, threshold=args.pc_threshold)

    # create output dir only after all validations have passed
    os.makedirs(output_dir, exist_ok=True)

    resistance_path = os.path.join(output_dir, "resistance_surface.tif")
    corridor_path = os.path.join(output_dir, "corridor.tif")
    write_geotiff(resistance_path, resistance, bbox)
    write_geotiff(corridor_path, corridor.astype(np.float32), bbox)

    params = {
        "buffer_px": args.buffer,
        "pc_threshold": args.pc_threshold,
        "src_pixel": list(src), "dst_pixel": list(dst),
        "path_length_px": len(path),
        "total_cost": total_cost,
        "corridor_area_px": int(corridor.sum()),
        "pc_index": pc,
    }
    params_path = os.path.join(output_dir, "corridor_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    n_total = int(suitability.size)
    outputs = [
        {"path": resistance_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": corridor_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    qa: Dict[str, Any] = {
        "source": source_note,
        "path_length_px": params["path_length_px"],
        "total_cost": params["total_cost"],
        "corridor_area_px": params["corridor_area_px"],
        "pc_index": params["pc_index"],
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
    }
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] LCP length: {params['path_length_px']} px, cost: {total_cost:.1f}")
        print(f"[{SKILL_NAME}] corridor area: {params['corridor_area_px']} px")
        print(f"[{SKILL_NAME}] PC index: {pc:.4f}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Ecological corridor design via least-cost path and connectivity indices.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input suitability GeoTIFF (band1)")
    p.add_argument("--buffer", type=int, default=2,
                   help="corridor buffer width in pixels (default: 2)")
    p.add_argument("--pc-threshold", type=float, default=0.5,
                   help="suitability threshold for PC index (default: 0.5)")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic scene (offline)")
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
