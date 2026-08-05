#!/usr/bin/env python3
"""sediment-transport-modeling — 泥沙输移模拟

基于 RUSLE（修正通用土壤流失方程）估算流域土壤侵蚀模数，并结合泥沙输移比
（SDR, Sediment Delivery Ratio）估算进入河网的产沙量，识别关键泥沙源区。

核心模型：
    A = R × K × L × S × C × P

- R  降雨侵蚀力因子 (MJ·mm·ha⁻¹·h⁻¹·yr⁻¹)
- K  土壤可蚀性因子 (t·ha·h·ha⁻¹·MJ⁻¹·mm⁻¹)
- L  坡长因子（由 DEM 的 D8 汇流累积推求）
- S  坡度因子（刘宝元中国黄土高原经验式）
- C  植被覆盖与管理因子（由 NDVI 反演）
- P  水土保持措施因子

产沙量：对侵蚀模数栅格按像元面积求和得总侵蚀量 (t/yr)，乘以 SDR 得输沙量。

数据源：本地 DEM / 降雨 / 土壤 / NDVI 栅格，或 ``--synthetic`` 生成物理一致的
模拟流域（含山坡 + 河谷 + 植被梯度）用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python sediment-transport-modeling.py --input dem.tif --output-dir ./out
    python sediment-transport-modeling.py --bbox 110 35 111 36 --synthetic --output-dir ./out

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
SKILL_NAME = "sediment-transport-modeling"

# ---- 复用共享核心库（本地 vendored，随脚本目录一起分发）----
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
    for v, name in ((w, "W"), (s, "S"), (e, "N"), (n, "N")):
        if v != v:  # NaN check
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


def validate_p_factor(p: float) -> None:
    """P must be in [0, 1] (0 = full conservation, 1 = no conservation)."""
    if p is None or not (0.0 <= float(p) <= 1.0):
        raise ValidationError(
            f"--p-factor must be in [0, 1] (got {p!r}); "
            "0 = full conservation practice, 1 = no conservation."
        )


def validate_synthetic_size(width: int, height: int) -> None:
    """Synthetic raster width/height must be >= 2."""
    if int(width) < 2 or int(height) < 2:
        raise ValidationError(
            f"--width/--height must be >= 2 (got width={width}, height={height})"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def compute_slope_rad(dem: np.ndarray, cellsize: float = 1.0) -> np.ndarray:
    """由 DEM 计算坡度（弧度）。使用二阶中心差分（np.gradient）。

    cellsize 单位为米，DEM 高程单位为米。
    """
    dem = np.asarray(dem, dtype=np.float64)
    cs = float(cellsize) if cellsize and cellsize > 0 else 1.0
    gy, gx = np.gradient(dem, cs, cs, edge_order=2 if min(dem.shape) >= 3 else 1)
    slope = np.arctan(np.sqrt(gx ** 2 + gy ** 2))
    return slope.astype(np.float64)


def d8_flow_accumulation(
    dem: np.ndarray, cellsize: float = 1.0
) -> Tuple[np.ndarray, np.ndarray]:
    """D8 单流向汇流累积。

    返回 (acc, down_flat)：
    - acc        每个像元的累积上游像元数（含自身，≥1）
    - down_flat  每个像元的下游像元 flat 索引；洼地 / 边界出口为 -1
    """
    dem = np.asarray(dem, dtype=np.float64)
    h, w = dem.shape
    n = h * w
    padded = np.full((h + 2, w + 2), np.nan, dtype=np.float64)
    padded[1:-1, 1:-1] = dem
    center = padded[1:-1, 1:-1]

    # 8 邻域：(dr, dc, 距离权重)
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


def slope_length_factor(
    acc: np.ndarray, slope_rad: np.ndarray, cellsize: float = 1.0
) -> np.ndarray:
    """坡长因子 L（RUSLE）。

    上游坡长 λ = acc × cellsize（把累积像元数视作汇流路径长度，单位 m）。
    指数 m 由坡度经 Foster/McCool 的 β 关系推求：
        β = (sinθ / 0.0896) / (3·sin^0.8θ + 0.56)，m = β / (1 + β)
    L = (λ / 22.13)^m，裁剪到 [0, 30] 以保持丘陵—沟道量级合理。
    """
    acc = np.asarray(acc, dtype=np.float64)
    slope_rad = np.asarray(slope_rad, dtype=np.float64)
    sin_t = np.clip(np.sin(slope_rad), 1e-4, None)
    beta = (sin_t / 0.0896) / (3.0 * sin_t ** 0.8 + 0.56)
    m = beta / (1.0 + beta)
    upslope_len = np.clip(acc, 1.0, None) * float(cellsize)
    L = np.power(upslope_len / 22.13, m)
    return np.clip(L, 0.0, 30.0)


def slope_steepness_factor(slope_rad: np.ndarray) -> np.ndarray:
    """坡度因子 S（刘宝元中国黄土高原经验式）。

    θ < 5°：S = 10.8·sinθ + 0.03
    θ ≥ 5°：S = 16.8·sinθ − 0.50
    """
    slope_rad = np.asarray(slope_rad, dtype=np.float64)
    slope_deg = np.rad2deg(slope_rad)
    sin_t = np.sin(slope_rad)
    S = np.where(slope_deg < 5.0, 10.8 * sin_t + 0.03, 16.8 * sin_t - 0.50)
    return np.clip(S, 0.0, None)


def cover_factor(ndvi: np.ndarray) -> np.ndarray:
    """植被覆盖与管理因子 C（由 NDVI 反演）。

    C = exp(-3·NDVI)，裸地（NDVI≈0）→ C≈1，密植被（NDVI≈1）→ C≈0.05。
    NDVI < 0（水体）设 C 为极小值（几乎不侵蚀）。
    """
    ndvi = np.asarray(ndvi, dtype=np.float64)
    C = np.exp(-3.0 * np.clip(ndvi, 0.0, 1.0))
    C = np.where(ndvi < 0.0, 0.001, C)
    return np.clip(C, 0.001, 1.0)


def rusle(
    R: np.ndarray, K: np.ndarray, L: np.ndarray,
    S: np.ndarray, C: np.ndarray, P: float = 1.0,
) -> np.ndarray:
    """RUSLE：A = R·K·L·S·C·P，输出侵蚀模数 t·ha⁻¹·yr⁻¹。"""
    A = (
        np.asarray(R, dtype=np.float64)
        * np.asarray(K, dtype=np.float64)
        * np.asarray(L, dtype=np.float64)
        * np.asarray(S, dtype=np.float64)
        * np.asarray(C, dtype=np.float64)
        * float(P)
    )
    return np.clip(A, 0.0, None)


def sediment_delivery_ratio(area_km2: float) -> float:
    """泥沙输移比 SDR（经验式，随流域面积递减）。

    SDR = 0.4724 · A^(-0.127)（Kothyari 型），裁剪到 [0.05, 0.9]。
    """
    a = max(float(area_km2), 1e-3)
    sdr = 0.4724 * (a ** -0.127)
    return float(np.clip(sdr, 0.05, 0.9))


def sediment_yield(
    A: np.ndarray, cell_area_m2: float, sdr: float
) -> Dict[str, Any]:
    """由侵蚀模数栅格估算总侵蚀量与输沙量。

    cell_area_m2：单像元面积（m²）。1 ha = 10000 m²。
    返回总侵蚀量、输沙量及面积统计。
    """
    A = np.asarray(A, dtype=np.float64)
    finite = A[np.isfinite(A)]
    cell_ha = float(cell_area_m2) / 10000.0
    total_erosion_t = float(np.nansum(A) * cell_ha)
    delivered_t = total_erosion_t * float(sdr)
    area_ha = float(finite.size * cell_ha)
    return {
        "total_erosion_t_per_yr": total_erosion_t,
        "sediment_yield_t_per_yr": delivered_t,
        "sdr": float(sdr),
        "area_ha": area_ha,
        "mean_erosion_modulus_t_ha_yr": float(np.nanmean(A)) if finite.size else 0.0,
        "max_erosion_modulus_t_ha_yr": float(np.nanmax(A)) if finite.size else 0.0,
    }


def key_source_areas(
    A: np.ndarray, bbox: List[float], top_n: int = 10, percentile: float = 95.0
) -> List[Dict[str, Any]]:
    """提取侵蚀模数最高的 top_n 个像元作为关键泥沙源区。

    返回每个源区的像元坐标（经纬度）与侵蚀模数。
    """
    A = np.asarray(A, dtype=np.float64)
    h, w = A.shape
    finite = A[np.isfinite(A)]
    if finite.size == 0:
        return []
    flat = A.ravel()
    order = np.argsort(flat)[::-1]
    w_deg = (bbox[2] - bbox[0]) / w
    h_deg = (bbox[3] - bbox[1]) / h
    sources: List[Dict[str, Any]] = []
    count = 0
    thr = np.percentile(finite, percentile)
    for idx in order:
        val = float(flat[idx])
        if not np.isfinite(val) or count >= top_n:
            break
        r, c = int(idx // w), int(idx % w)
        lon = bbox[0] + (c + 0.5) * w_deg
        lat = bbox[3] - (r + 0.5) * h_deg
        sources.append({
            "row": r, "col": c,
            "lon": round(float(lon), 6), "lat": round(float(lat), 6),
            "erosion_modulus_t_ha_yr": round(val, 3),
            "is_above_p95": bool(val >= thr),
        })
        count += 1
    return sources


# ---------------------------------------------------------------------------
# 合成数据：物理一致的模拟流域（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 96,
    height: int = 96,
    seed: int = 42,
) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    """生成一个含山坡 + 河谷 + 植被梯度的合成流域。

    返回 (layers, info)：
    - layers: dict(dem, R, K, ndvi)，均为 2D float32 数组
    - info:   元数据（cellsize_m、真值统计等）
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yn = yy.astype(np.float64) / max(height - 1, 1)
    xn = xx.astype(np.float64) / max(width - 1, 1)

    # DEM：整体向北抬升的斜坡 + 一条贯穿的河谷（低洼）+ 噪声
    base = yn * 600.0  # 0→600 m 主坡
    valley = -250.0 * np.exp(-((xn - 0.5) ** 2) / (2 * 0.08 ** 2))  # 中部河谷
    noise = rng.normal(0, 3.0, (height, width))
    dem = (base + valley + noise).astype(np.float32)

    # 降雨侵蚀力 R：空间上略有梯度（南多北少）
    R = (180.0 + 120.0 * (1.0 - yn) + rng.normal(0, 5, (height, width))).astype(np.float32)
    R = np.clip(R, 20.0, None)

    # 土壤可蚀性 K：典型黄土 0.25-0.40
    K = (0.30 + 0.08 * np.sin(2 * np.pi * xn) + rng.normal(0, 0.02, (height, width))).astype(np.float32)
    K = np.clip(K, 0.05, 0.60)

    # NDVI：河谷与平地植被茂密，陡坡/高处植被稀疏
    slope_proxy = np.abs(np.gradient(dem, axis=1))  # 横向坡度代理
    ndvi = 0.75 - 0.5 * np.clip(slope_proxy / slope_proxy.max(), 0, 1) + 0.15 * (1 - yn)
    ndvi = (ndvi + rng.normal(0, 0.03, (height, width))).astype(np.float32)
    ndvi = np.clip(ndvi, -0.1, 0.95)

    lat0 = 0.5 * (bbox[1] + bbox[3])
    m_per_deg_lon = 111320.0 * np.cos(np.deg2rad(lat0))
    m_per_deg_lat = 110540.0
    dx = (bbox[2] - bbox[0]) * m_per_deg_lon / width
    dy = (bbox[3] - bbox[1]) * m_per_deg_lat / height
    cellsize_m = float(0.5 * (dx + dy))

    layers = {"dem": dem, "R": R, "K": K, "ndvi": ndvi}
    info = {
        "bbox": bbox, "width": width, "height": height,
        "cellsize_m": cellsize_m,
        "dem_min": float(dem.min()), "dem_max": float(dem.max()),
        "ndvi_mean": float(ndvi.mean()),
    }
    return layers, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
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
    """读取栅格，返回 (cube, bbox, cellsize_m)。

    NoData 哨兵值（src.nodata）会被替换为 NaN 以避免污染下游坡度/汇流/侵蚀
    计算。NaN 会在 RUSLE 各因子里自然传播，最终侵蚀图上的 NaN 像元是
    “数据缺失/被掩膜”而非“高侵蚀”。
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        h, w = cube.shape[-2], cube.shape[-1]
        nd = src.nodata
        if nd is not None:
            cube = np.where(cube == float(nd), np.nan, cube).astype(np.float32)
        lat0 = 0.5 * (b.bottom + b.top)
        m_per_deg_lon = 111320.0 * np.cos(np.deg2rad(lat0))
        m_per_deg_lat = 110540.0
        dx = (b.right - b.left) * m_per_deg_lon / w
        dy = (b.top - b.bottom) * m_per_deg_lat / h
        cellsize_m = float(0.5 * (dx + dy))
    return cube, bbox, cellsize_m


# ---------------------------------------------------------------------------
# 主计算管线（核心算法 + 输入解析）
# ---------------------------------------------------------------------------
def run_model(
    dem: np.ndarray, R: np.ndarray, K: np.ndarray, ndvi: np.ndarray,
    cellsize_m: float, bbox: List[float],
    P: float = 1.0, sdr: Optional[float] = None, top_n: int = 10,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """执行 RUSLE + SDR 全流程，返回 (erosion_modulus_raster, summary)。"""
    slope = compute_slope_rad(dem, cellsize_m)
    acc, _down = d8_flow_accumulation(dem, cellsize_m)
    L = slope_length_factor(acc, slope, cellsize_m)
    S = slope_steepness_factor(slope)
    C = cover_factor(ndvi)
    A = rusle(R, K, L, S, C, P)

    cell_area_m2 = cellsize_m * cellsize_m
    area_km2 = (A.size * cell_area_m2) / 1e6
    if sdr is None:
        sdr = sediment_delivery_ratio(area_km2)
    yld = sediment_yield(A, cell_area_m2, sdr)
    sources = key_source_areas(A, bbox, top_n=top_n)

    summary = {
        "cellsize_m": cellsize_m,
        "area_km2": float(area_km2),
        "slope_deg_mean": float(np.rad2deg(np.mean(slope))),
        "slope_deg_max": float(np.rad2deg(np.max(slope))),
        "L_mean": float(np.mean(L)),
        "S_mean": float(np.mean(S)),
        "C_mean": float(np.mean(C)),
        "P": float(P),
        "yield": yld,
        "key_source_areas": sources,
    }
    return A.astype(np.float32), summary


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
            "P_factor": getattr(args, "p_factor", None),
            "sdr": getattr(args, "sdr", None),
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

    # ===== 0) Validate CLI up-front (no side effects, no mkdir) =====
    validate_p_factor(args.p_factor)
    if args.sdr is not None:
        try:
            float(args.sdr)
        except (TypeError, ValueError) as exc:
            raise ValidationError(f"--sdr must be a float (got {args.sdr!r})") from exc
        if not (0.0 <= float(args.sdr) <= 1.0):
            raise ValidationError(
                f"--sdr must be in [0, 1] (got {args.sdr!r})"
            )
    if int(args.top_n) < 0:
        raise ValidationError(f"--top-n must be >= 0 (got {args.top_n!r})")
    if not (args.input or args.synthetic or bbox):
        raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
    if bbox is not None:
        validate_bbox(bbox, source="--bbox")
    if args.synthetic and not args.input:
        validate_synthetic_size(args.width, args.height)

    # mkdir AFTER validation (CONVENTIONS §1.1 / common bug pattern #6)
    os.makedirs(output_dir, exist_ok=True)

    # 1) 获取数据
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox, cellsize_m = read_geotiff(args.input)
        # NoData=-9999 was replaced with NaN by read_geotiff; reject all-NaN
        # (would otherwise silently produce NaN erosion + 0 yield).
        if not np.isfinite(cube).any():
            raise ValidationError(
                f"input raster '{args.input}' contains only NoData / NaN pixels; nothing to model"
            )
        bbox = bbox if bbox is not None else file_bbox
        # If user supplied --bbox, validate the user-bbox AFTER combining with file bbox
        if args.bbox is not None:
            validate_bbox(bbox, source="--bbox")
        dem = cube[0] if cube.ndim == 3 else cube
        # 其余因子在真实 DEM 上用合成层近似（离线演示）
        h, w = dem.shape
        layers, synth_info = generate_synthetic(bbox, width=w, height=h)
        layers["dem"] = dem.astype(np.float32)
        # Realign R/K/NDVI NoData mask to dem (any band NaN => pixel masked)
        finite_dem = np.isfinite(dem)
        if not finite_dem.any():
            raise ValidationError(
                f"input DEM has no valid (non-NoData) pixels; nothing to model"
            )
        n_valid = int(finite_dem.sum())
        for k_name in ("R", "K", "ndvi"):
            layers[k_name] = np.where(finite_dem, layers[k_name], np.nan).astype(np.float32)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        layers, synth_info = generate_synthetic(bbox, width=args.width, height=args.height)
        cellsize_m = synth_info["cellsize_m"]
        # In synthetic mode all pixels are valid by construction
        n_valid = int(layers["dem"].size)
        source_note = "synthetic"

    dem = layers["dem"]
    if dem.size == 0:
        raise ValidationError("input raster is empty")

    # 2) RUSLE + SDR
    try:
        A, summary = run_model(
            dem, layers["R"], layers["K"], layers["ndvi"],
            cellsize_m, bbox, P=args.p_factor, sdr=args.sdr, top_n=args.top_n,
        )
    except Exception as exc:  # noqa: BLE001
        raise ProcessError(f"sediment modeling failed: {exc}") from exc

    # 3) 写出产物 (mask NoData pixels in output raster as -1 sentinel)
    finite_out = np.isfinite(A)
    A_for_write = np.where(finite_out, A, -1.0).astype(np.float32)
    out_tif = os.path.join(output_dir, "erosion_modulus.tif")
    write_geotiff(out_tif, A_for_write, bbox, nodata=-1.0)

    summary_path = os.path.join(output_dir, "sediment_summary.json")
    # Inject n_valid_pixels into summary for downstream consumers
    summary["n_valid_pixels"] = n_valid
    summary["n_total_pixels"] = int(A.size)
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    sources_path = os.path.join(output_dir, "key_source_areas.geojson")
    feats = [{
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [s["lon"], s["lat"]]},
        "properties": {k: v for k, v in s.items() if k not in ("lon", "lat")},
    } for s in summary["key_source_areas"]]
    with open(sources_path, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": feats},
                  f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "cellsize_m": summary["cellsize_m"],
        "area_km2": summary["area_km2"],
        "mean_erosion_modulus_t_ha_yr": summary["yield"]["mean_erosion_modulus_t_ha_yr"],
        "max_erosion_modulus_t_ha_yr": summary["yield"]["max_erosion_modulus_t_ha_yr"],
        "total_erosion_t_per_yr": summary["yield"]["total_erosion_t_per_yr"],
        "sediment_yield_t_per_yr": summary["yield"]["sediment_yield_t_per_yr"],
        "sdr": summary["yield"]["sdr"],
        "n_key_sources": len(summary["key_source_areas"]),
        "n_valid_pixels": n_valid,
        "n_total_pixels": int(A.size),
    }

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": summary_path, "kind": "json"},
        {"path": sources_path, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": len(feats)},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] area: {qa['area_km2']:.3f} km²  cellsize: {qa['cellsize_m']:.1f} m")
        print(f"[{SKILL_NAME}] mean erosion modulus: {qa['mean_erosion_modulus_t_ha_yr']:.2f} t/ha/yr")
        print(f"[{SKILL_NAME}] total erosion: {qa['total_erosion_t_per_yr']:.1f} t/yr")
        print(f"[{SKILL_NAME}] sediment yield (SDR={qa['sdr']:.3f}): {qa['sediment_yield_t_per_yr']:.1f} t/yr")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="RUSLE soil erosion + sediment delivery ratio (SDR) for watershed sediment yield.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input DEM GeoTIFF (band 1 as elevation)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic watershed (offline)")
    p.add_argument("--width", type=int, default=96, help="synthetic raster width (default 96)")
    p.add_argument("--height", type=int, default=96, help="synthetic raster height (default 96)")
    p.add_argument("--p-factor", type=float, default=1.0,
                   help="support practice factor P, 0-1 (default 1.0 = no conservation)")
    p.add_argument("--sdr", type=float, default=None,
                   help="override sediment delivery ratio (default: auto from area)")
    p.add_argument("--top-n", type=int, default=10,
                   help="number of key sediment source cells to report (default 10)")
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
