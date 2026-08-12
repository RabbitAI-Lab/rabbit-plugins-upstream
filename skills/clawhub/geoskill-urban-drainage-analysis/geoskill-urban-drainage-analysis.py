#!/usr/bin/env python3
"""urban-drainage-analysis — 城市排水分析

基于 DEM 的 D8 流向 / 汇流累积，结合地形湿度指数（TWI）、不透水面（ISA）
径流系数与设计降雨量，评估城市内涝风险：

- **D8 流向 + 汇流累积**：识别径流汇聚通道。
- **地形湿度指数 TWI = ln(a / tanβ)**：刻画地形汇水倾向，低洼 + 高汇流处 TWI 高。
- **不透水面径流系数**：ISA 越高，产流越多（C = 0.15 + 0.75·ISA）。
- **设计降雨**：降雨量 × 径流系数 × 汇流贡献 → 积水深度估计。

综合风险：对 TWI、汇流累积、ISA 归一化加权，低洼高汇流高不透水面区为高风险。
径流路径由汇流通道追踪矢量化为 LineString。

数据源：本地城市 DEM，或 ``--synthetic`` 生成含低洼盆地 + 不透水面分区的模拟
城区用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python urban-drainage-analysis.py --input dem.tif --rainfall 50 --output-dir ./out
    python urban-drainage-analysis.py --bbox 116 39 117 40 --rainfall 50 --synthetic --output-dir ./out

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
SKILL_NAME = "urban-drainage-analysis"

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


DEFAULT_WEIGHTS = {"twi": 0.45, "flow_acc": 0.25, "isa": 0.30}


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox, *, allow_antimeridian_cross: bool = False) -> None:
    """校验 bbox=[W,S,E,N]（EPSG:4326 度）。"""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must have 4 floats [W S E N]")
    w, s, e, n = [float(v) for v in bbox]
    if not (all(np.isfinite([w, s, e, n]))):
        raise ValidationError("bbox contains non-finite values")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError("bbox lon out of [-180, 180]")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError("bbox lat out of [-90, 90]")
    if w >= e:
        if not allow_antimeridian_cross:
            raise ValidationError(
                f"bbox W>=E ({w} >= {e}); cross-180° not supported"
            )
        raise ValidationError(f"bbox W>=E ({w} >= {e})")
    if s >= n:
        raise ValidationError(f"bbox S>=N ({s} >= {n})")
    if (e - w) < 1e-4 or (n - s) < 1e-4:
        raise ValidationError(
            f"bbox too small (dx={e - w}, dy={n - s}); need >= 1e-4 degrees"
        )


def validate_params(args: argparse.Namespace) -> None:
    """校验 CLI 参数物理合理性 → ValidationError 触发 rc=6。

    注意：--rainfall < 0 由原代码以 UsageError(rc=2) 抛出（tests/test_cli.py 锁定），
    本函数不重复校验。
    """
    if args.width < 4 or args.height < 4:
        raise ValidationError(
            f"--width/--height must be >= 4 (got {args.width} x {args.height})"
        )
    if args.width > 4096 or args.height > 4096:
        raise ValidationError(
            f"--width/--height {args.width} x {args.height} too large (> 4096)"
        )
    if args.n_paths < 1:
        raise ValidationError(
            f"--n-paths must be >= 1 (got {args.n_paths})"
        )
    if args.n_paths > 100:
        raise ValidationError(
            f"--n-paths {args.n_paths} is unrealistically large (> 100)"
        )
    if not (np.isfinite(args.rainfall)):
        raise ValidationError(
            f"--rainfall must be finite (got {args.rainfall})"
        )
    if args.rainfall > 2000.0:
        raise ValidationError(
            f"--rainfall {args.rainfall} mm is unrealistically large "
            f"(extreme rainfall records < 1500 mm/day)"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def compute_slope_rad(dem: np.ndarray, cellsize: float = 1.0) -> np.ndarray:
    dem = np.asarray(dem, dtype=np.float64)
    cs = float(cellsize) if cellsize and cellsize > 0 else 1.0
    gy, gx = np.gradient(dem, cs, cs, edge_order=2 if min(dem.shape) >= 3 else 1)
    return np.arctan(np.sqrt(gx ** 2 + gy ** 2))


def d8_flow_accumulation(
    dem: np.ndarray, cellsize: float = 1.0
) -> Tuple[np.ndarray, np.ndarray]:
    """D8 汇流累积，返回 (acc, down_flat)。见 sediment-transport-modeling 同名函数。"""
    dem = np.asarray(dem, dtype=np.float64)
    h, w = dem.shape
    n = h * w
    padded = np.full((h + 2, w + 2), np.nan, dtype=np.float64)
    padded[1:-1, 1:-1] = dem
    center = padded[1:-1, 1:-1]
    offsets = [
        (-1, -1, 1.4142135623730951), (-1, 0, 1.0), (-1, 1, 1.4142135623730951),
        (0, -1, 1.0), (0, 1, 1.0),
        (1, -1, 1.4142135623730951), (1, 0, 1.0), (1, 1, 1.4142135623730951),
    ]
    cs = float(cellsize) if cellsize and cellsize > 0 else 1.0
    best_drop = np.full((h, w), -np.inf, dtype=np.float64)
    best_dr = np.zeros((h, w), dtype=np.int64)
    best_dc = np.zeros((h, w), dtype=np.int64)
    best_dir = np.full((h, w), -1, dtype=np.int64)
    for idx, (dr, dc, dist) in enumerate(offsets):
        nb = padded[1 + dr:h + 1 + dr, 1 + dc:w + 1 + dc]
        drop = (center - nb) / (dist * cs)
        valid = np.isfinite(nb) & (drop > best_drop)
        best_drop = np.where(valid, drop, best_drop)
        best_dr = np.where(valid, dr, best_dr)
        best_dc = np.where(valid, dc, best_dc)
        best_dir = np.where(valid, idx, best_dir)
    no_flow = best_drop <= 0.0
    best_dir[no_flow] = -1
    rows, cols = np.indices((h, w))
    nr = np.clip(rows + best_dr, 0, h - 1)
    nc = np.clip(cols + best_dc, 0, w - 1)
    valid_flow = best_dir >= 0
    down = np.where(valid_flow, nr * w + nc, -1).astype(np.int64).ravel()
    indeg = np.zeros(n, dtype=np.int64)
    valid_idx = down[down >= 0]
    if valid_idx.size:
        indeg += np.bincount(valid_idx, minlength=n)
    acc = np.ones(n, dtype=np.float64)
    from collections import deque
    q = deque(int(i) for i in np.where(indeg == 0)[0])
    while q:
        c = q.popleft()
        d = int(down[c])
        if d >= 0:
            acc[d] += acc[c]
            indeg[d] -= 1
            if indeg[d] == 0:
                q.append(d)
    return acc.reshape(h, w), down.reshape(h, w)


def topographic_wetness_index(
    acc: np.ndarray, slope_rad: np.ndarray, cellsize: float = 1.0
) -> np.ndarray:
    """TWI = ln(a / tanβ)，a 为单位等高线汇流面积（acc·cellsize）。"""
    acc = np.asarray(acc, dtype=np.float64)
    slope_rad = np.asarray(slope_rad, dtype=np.float64)
    tan_b = np.clip(np.tan(slope_rad), 1e-3, None)
    a = np.clip(acc, 1.0, None) * float(cellsize)
    twi = np.log(a / tan_b)
    return twi


def runoff_coefficient(isa: np.ndarray) -> np.ndarray:
    """不透水面 → 径流系数：C = 0.15 + 0.75·ISA（ISA∈[0,1]）。"""
    isa = np.clip(np.asarray(isa, dtype=np.float64), 0.0, 1.0)
    return 0.15 + 0.75 * isa


def normalize_minmax(arr: np.ndarray) -> np.ndarray:
    arr = np.asarray(arr, dtype=np.float64)
    lo, hi = np.nanmin(arr), np.nanmax(arr)
    if not np.isfinite(lo) or not np.isfinite(hi) or hi - lo < 1e-12:
        return np.zeros_like(arr, dtype=np.float64)
    out = (arr - lo) / (hi - lo)
    return np.nan_to_num(out, nan=0.0, posinf=1.0, neginf=0.0)


def waterlogging_risk(
    twi: np.ndarray, acc: np.ndarray, isa: np.ndarray,
    weights: Optional[Dict[str, float]] = None,
) -> np.ndarray:
    """综合内涝风险（0-1）：TWI、汇流累积、不透水面归一化加权。"""
    w = dict(DEFAULT_WEIGHTS)
    if weights:
        w.update(weights)
    total = sum(w.values())
    if total <= 0:
        raise UsageError("weights must sum to a positive value")
    risk = (
        w["twi"] * normalize_minmax(twi)
        + w["flow_acc"] * normalize_minmax(np.log1p(np.asarray(acc, dtype=np.float64)))
        + w["isa"] * normalize_minmax(isa)
    ) / total
    return np.clip(risk, 0.0, 1.0)


def classify_risk(risk: np.ndarray, low: float = 0.40, high: float = 0.70) -> np.ndarray:
    risk = np.asarray(risk, dtype=np.float64)
    cls = np.zeros(risk.shape, dtype=np.int32)
    cls[risk >= low] = 1
    cls[risk >= high] = 2
    return cls


def waterlogging_depth_mm(
    rainfall_mm: float, C: np.ndarray, acc: np.ndarray
) -> np.ndarray:
    """积水深度估计（mm）：rainfall·C·汇流贡献因子（ln(1+acc) 归一化）。

    深洼 + 高汇流处深度趋近 rainfall·C，上限即产流量。
    """
    C = np.asarray(C, dtype=np.float64)
    acc = np.asarray(acc, dtype=np.float64)
    f = np.log1p(acc)
    fmax = np.nanmax(f)
    f_norm = f / fmax if fmax > 1e-9 else np.zeros_like(f)
    depth = float(rainfall_mm) * C * f_norm
    return np.clip(depth, 0.0, float(rainfall_mm))


def trace_flow_paths(
    down: np.ndarray, acc: np.ndarray, bbox: List[float],
    n_paths: int = 5, acc_percentile: float = 90.0,
) -> List[Dict[str, Any]]:
    """从高汇流像元沿下游追踪径流路径，输出 LineString GeoJSON feature。"""
    acc = np.asarray(acc, dtype=np.float64)
    h, w = acc.shape
    down_flat = down.ravel()
    flat_acc = acc.ravel()
    thr = np.percentile(flat_acc, acc_percentile)
    candidates = np.where(flat_acc >= thr)[0]
    if candidates.size == 0:
        candidates = np.array([int(np.argmax(flat_acc))])
    # 按汇流累积降序选起点
    candidates = candidates[np.argsort(flat_acc[candidates])[::-1]]

    w_deg = (bbox[2] - bbox[0]) / w
    h_deg = (bbox[3] - bbox[1]) / h

    def coord(flat_idx: int) -> List[float]:
        r, c = int(flat_idx // w), int(flat_idx % w)
        return [round(bbox[0] + (c + 0.5) * w_deg, 6),
                round(bbox[3] - (r + 0.5) * h_deg, 6)]

    feats: List[Dict[str, Any]] = []
    covered: set = set()
    for start in candidates:
        if len(feats) >= n_paths:
            break
        if int(start) in covered:
            continue
        path_idx: List[int] = []
        local_accs: List[float] = []
        cur = int(start)
        guard = 0
        max_steps = h * w
        while cur >= 0 and guard < max_steps:
            path_idx.append(cur)
            local_accs.append(float(flat_acc[cur]))
            nxt = int(down_flat[cur])
            if nxt == cur:
                break
            cur = nxt
            guard += 1
        if len(path_idx) < 2:
            continue
        covered.update(path_idx)
        coords = [coord(ci) for ci in path_idx]
        feats.append({
            "type": "Feature",
            "geometry": {"type": "LineString", "coordinates": coords},
            "properties": {
                "n_vertices": len(path_idx),
                "max_acc": round(max(local_accs), 1),
                "mean_acc": round(float(np.mean(local_accs)), 1),
            },
        })
    return feats


# ---------------------------------------------------------------------------
# 合成数据：含低洼盆地 + 不透水面分区的模拟城区（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 96,
    height: int = 96,
    seed: int = 42,
    inject_depression: bool = True,
) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    """生成城市排水合成场景。

    layers: dem / isa。注入一个位于城区中心的低洼盆地（高 ISA），真值记在 info。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yn = yy.astype(np.float64) / max(height - 1, 1)
    xn = xx.astype(np.float64) / max(width - 1, 1)

    # 基础地形：向东南缓倾
    base = (1.0 - yn) * 30.0 + (1.0 - xn) * 20.0
    noise = rng.normal(0, 0.3, (height, width))
    dem = (50.0 + base + noise).astype(np.float64)

    # ISA：中心建成区高，边缘绿地低
    dist_center = np.hypot(xn - 0.5, yn - 0.5)
    isa = np.clip(0.85 - 1.2 * dist_center + rng.normal(0, 0.03, (height, width)), 0.05, 0.95)

    truth = None
    if inject_depression:
        cx, cy, r = 0.5, 0.5, 0.12
        bowl = ((xn - cx) ** 2 + (yn - cy) ** 2)
        mask = bowl < r ** 2
        # 盆地：中心下切 8 m
        dem[mask] -= 8.0 * (1.0 - np.sqrt(bowl[mask]) / r)
        isa[mask] = np.clip(isa[mask] + 0.1, 0, 0.98)  # 盆地内为硬化地面
        truth = {"cx": cx, "cy": cy, "r": r,
                 "lon": bbox[0] + cx * (bbox[2] - bbox[0]),
                 "lat": bbox[3] - cy * (bbox[3] - bbox[1])}

    lat0 = 0.5 * (bbox[1] + bbox[3])
    m_per_deg_lon = 111320.0 * np.cos(np.deg2rad(lat0))
    m_per_deg_lat = 110540.0
    dx = (bbox[2] - bbox[0]) * m_per_deg_lon / width
    dy = (bbox[3] - bbox[1]) * m_per_deg_lat / height
    cellsize_m = float(0.5 * (dx + dy))

    layers = {"dem": dem.astype(np.float32), "isa": isa.astype(np.float32)}
    info = {"bbox": bbox, "width": width, "height": height,
            "cellsize_m": cellsize_m, "truth": truth}
    return layers, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0
) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if array.ndim == 2:
        array = array[np.newaxis, ...]
    nb, h, w = array.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(array[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], float]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        nd = src.nodata
        if nd is not None and np.isfinite(nd):
            cube = np.where(cube == nd, np.nan, cube).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        h, w = cube.shape[-2], cube.shape[-1]
        lat0 = 0.5 * (b.bottom + b.top)
        dx = (b.right - b.left) * 111320.0 * np.cos(np.deg2rad(lat0)) / w
        dy = (b.top - b.bottom) * 110540.0 / h
        cellsize_m = float(0.5 * (dx + dy))
    return cube, bbox, cellsize_m


# ---------------------------------------------------------------------------
# 主管线
# ---------------------------------------------------------------------------
def run_model(
    dem: np.ndarray, isa: np.ndarray, cellsize_m: float, bbox: List[float],
    rainfall_mm: float = 50.0, weights: Optional[Dict[str, float]] = None,
    n_paths: int = 5,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, List[Dict[str, Any]], Dict[str, Any]]:
    """执行城市排水分析，返回 (risk, cls, depth_mm, flow_paths, summary)。"""
    slope = compute_slope_rad(dem, cellsize_m)
    acc, down = d8_flow_accumulation(dem, cellsize_m)
    twi = topographic_wetness_index(acc, slope, cellsize_m)
    C = runoff_coefficient(isa)
    risk = waterlogging_risk(twi, acc, isa, weights)
    cls = classify_risk(risk)
    depth = waterlogging_depth_mm(rainfall_mm, C, acc)
    paths = trace_flow_paths(down, acc, bbox, n_paths=n_paths)

    high_mask = cls == 2
    summary = {
        "cellsize_m": cellsize_m,
        "rainfall_mm": float(rainfall_mm),
        "twi_mean": round(float(np.mean(twi)), 3),
        "twi_max": round(float(np.max(twi)), 3),
        "runoff_coeff_mean": round(float(np.mean(C)), 3),
        "risk_mean": round(float(np.mean(risk)), 4),
        "risk_max": round(float(np.max(risk)), 4),
        "level_counts": {
            "low": int(np.sum(cls == 0)),
            "medium": int(np.sum(cls == 1)),
            "high": int(np.sum(cls == 2)),
        },
        "high_risk_fraction": round(float(np.mean(high_mask)), 4),
        "depth_max_mm": round(float(np.max(depth)), 2),
        "depth_mean_high_risk_mm": round(float(np.mean(depth[high_mask])), 2) if high_mask.any() else 0.0,
        "n_flow_paths": len(paths),
        "weights": weights or dict(DEFAULT_WEIGHTS),
    }
    return risk.astype(np.float32), cls, depth.astype(np.float32), paths, summary


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
        inputs={
            "input": getattr(args, "input", None),
            "bbox": bbox,
            "synthetic": bool(getattr(args, "synthetic", False)),
            "rainfall_mm": getattr(args, "rainfall", None),
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

    # 1) 参数与 bbox 校验（先做，不创建任何目录）
    validate_params(args)
    # --rainfall < 0 保持 UsageError rc=2（tests/test_cli.py 锁定）
    if args.rainfall < 0:
        raise UsageError("--rainfall must be non-negative")

    bbox = list(args.bbox) if args.bbox else None

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox, cellsize_m = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        dem = cube[0] if cube.ndim == 3 else cube
        h, w = dem.shape
        layers, synth_info = generate_synthetic(bbox, width=w, height=h, inject_depression=False)
        layers["dem"] = dem.astype(np.float32)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        layers, synth_info = generate_synthetic(
            bbox, width=args.width, height=args.height,
            inject_depression=not args.no_depression,
        )
        cellsize_m = synth_info["cellsize_m"]
        source_note = "synthetic"

    # input 模式也要校验 bbox
    if bbox is not None:
        validate_bbox(bbox)

    if layers["dem"].size == 0:
        raise ValidationError("input raster is empty")

    # 全 NaN 检查
    n_total = int(layers["dem"].size)
    n_valid = int(np.sum(np.isfinite(layers["dem"])))
    if n_valid == 0:
        raise ValidationError(
            f"input raster has no valid pixels (n_valid=0, n_total={n_total})"
        )

    # 所有校验通过 → 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    try:
        risk, cls, depth, paths, summary = run_model(
            layers["dem"], layers["isa"], cellsize_m, bbox,
            rainfall_mm=args.rainfall, n_paths=args.n_paths,
        )
    except Exception as exc:  # noqa: BLE001
        raise ProcessError(f"urban drainage analysis failed: {exc}") from exc

    risk_tif = os.path.join(output_dir, "waterlogging_risk.tif")
    write_geotiff(risk_tif, risk, bbox)
    depth_tif = os.path.join(output_dir, "waterlogging_depth_mm.tif")
    write_geotiff(depth_tif, depth, bbox)

    paths_geojson = os.path.join(output_dir, "runoff_paths.geojson")
    with open(paths_geojson, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": paths},
                  f, ensure_ascii=False, indent=2)

    summary_path = os.path.join(output_dir, "drainage_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "rainfall_mm": summary["rainfall_mm"],
        "risk_mean": summary["risk_mean"],
        "risk_max": summary["risk_max"],
        "high_risk_fraction": summary["high_risk_fraction"],
        "depth_max_mm": summary["depth_max_mm"],
        "n_flow_paths": summary["n_flow_paths"],
        "n_total_pixels": n_total,
        "n_valid_pixels": n_valid,
        "input_nodata_handling": "NoData->NaN",
    }

    outputs = [
        {"path": risk_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": depth_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": paths_geojson, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": len(paths)},
        {"path": summary_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] rainfall: {qa['rainfall_mm']} mm  cellsize: {summary['cellsize_m']:.1f} m")
        print(f"[{SKILL_NAME}] risk mean={qa['risk_mean']:.3f}  max={qa['risk_max']:.3f}")
        print(f"[{SKILL_NAME}] high-risk fraction: {qa['high_risk_fraction']:.3%}")
        print(f"[{SKILL_NAME}] max waterlogging depth: {qa['depth_max_mm']:.1f} mm")
        print(f"[{SKILL_NAME}] flow paths: {qa['n_flow_paths']}")
        print(f"[{SKILL_NAME}] output: {risk_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Urban waterlogging risk from D8 flow accumulation, TWI, impervious surface and design rainfall.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input urban DEM GeoTIFF (band 1 as elevation)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic urban scene with a depression (offline)")
    p.add_argument("--width", type=int, default=96, help="synthetic raster width (default 96)")
    p.add_argument("--height", type=int, default=96, help="synthetic raster height (default 96)")
    p.add_argument("--rainfall", type=float, default=50.0,
                   help="design rainfall depth in mm (default 50)")
    p.add_argument("--n-paths", type=int, default=5,
                   help="number of runoff flow paths to trace (default 5)")
    p.add_argument("--no-depression", action="store_true",
                   help="synthetic mode: do not inject a depression (baseline)")
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
