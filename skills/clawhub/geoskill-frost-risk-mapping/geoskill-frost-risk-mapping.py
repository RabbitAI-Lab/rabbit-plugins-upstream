#!/usr/bin/env python3
"""frost-risk-mapping — 霜冻风险制图

对日最低温时序栅格执行地形修正与霜冻风险分析。核心流程：

- **地形修正**：把（站点插值或再分析）最低温修正到逐像元实际地形——
  高程递减率（lapse rate，默认 6.5°C/km）、冷空气湖（洼地相对高程负异常
  造成的冷池效应）与坡向辐射差异（南坡暖、北坡冷）。
- **霜冻统计**：逐像元统计霜冻日数与频率（Tmin ≤ threshold）、初霜日、终霜日、
  无霜期（最长连续 Tmin > threshold 的天数）。
- **风险分级**：由霜冻频率分为 0 无 / 1 低 / 2 中 / 3 高 / 4 严重 五级。

数据源：本地日最低温时序 GeoTIFF（多波段=多日）+ DEM，或使用 ``--synthetic``
生成含山脊与洼地的 DEM 及受高程影响的最低温场用于离线测试。

隐私声明 / Privacy：
- 默认完全离线运行，不发起任何网络请求。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python frost-risk-mapping.py --input tmin_ts.tif --dem dem.tif --threshold 0
    python frost-risk-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "frost-risk-mapping"

# 默认气温直减率（°C/m）：约 6.5°C/km
DEFAULT_LAPSE = 0.0065

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
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """校验 bbox 合法性（W<=E, S<=N, 经纬度范围, 零面积）。"""
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise ValidationError(f"bbox must have 4 floats, got {bbox!r}", bbox=list(bbox))
    W_, S_, E_, N_ = (float(x) for x in bbox)
    if not (W_ <= E_ and S_ <= N_):
        raise ValidationError(
            f"invalid bbox ordering: W={W_} E={E_} S={S_} N={N_} "
            f"(require W<=E and S<=N)",
            w=W_, e=E_, s=S_, n=N_,
        )
    if not (-180.0 <= W_ <= 180.0 and -180.0 <= E_ <= 180.0):
        raise ValidationError(
            f"lon out of range [-180,180]: W={W_} E={E_}",
            w=W_, e=E_,
        )
    if not (-90.0 <= S_ <= 90.0 and -90.0 <= N_ <= 90.0):
        raise ValidationError(
            f"lat out of range [-90,90]: S={S_} N={N_}",
            s=S_, n=N_,
        )
    if (E_ - W_) <= 0.0 or (N_ - S_) <= 0.0:
        raise ValidationError(
            f"zero-area bbox: W={W_} E={E_} S={S_} N={N_}",
            w=W_, e=E_, s=S_, n=N_,
        )


def validate_params(args) -> None:
    """校验 CLI 参数值域。"""
    if args.bbox is not None:
        validate_bbox(args.bbox)
    if int(args.n_dates) < 1:
        raise UsageError(f"--n-dates must be >=1, got {args.n_dates}",
                         n_dates=int(args.n_dates))
    # 阈值取典型最低温合理范围（-80 ~ +40 °C）
    if not (-80.0 <= float(args.threshold) <= 40.0):
        raise UsageError(
            f"--threshold out of plausible range [-80,40] °C: {args.threshold}",
            threshold=float(args.threshold),
        )


# ---------------------------------------------------------------------------
# 核心算法：地形属性
# ---------------------------------------------------------------------------
def terrain_attributes(
    dem: np.ndarray,
    res_m: float = 1000.0,
) -> Tuple[np.ndarray, np.ndarray]:
    """由 DEM 计算坡度(°)与坡向(°，顺时针自北：0=北, 90=东, 180=南, 270=西)。

    约定行索引 0 为北。返回 (slope_deg, aspect_deg)。
    """
    dem = np.asarray(dem, dtype=np.float64)
    if dem.ndim != 2:
        raise ValidationError("DEM must be 2-D", ndim=int(dem.ndim))
    res = max(float(res_m), 1e-6)
    # np.gradient: axis0=行(向南递增)，axis1=列(向东递增)
    g_row, g_col = np.gradient(dem, res, res)
    gx = g_col                      # dz/dx（东向）
    gy = -g_row                     # dz/dy（北向，行递增=向南，故取负）
    slope_rad = np.arctan(np.sqrt(gx ** 2 + gy ** 2))
    slope_deg = np.degrees(slope_rad)
    # 下坡方向 d = -gradient；坡向=下坡方向相对北的顺时针角
    aspect_rad = np.arctan2(-gx, -gy)
    aspect_deg = (np.degrees(aspect_rad) + 360.0) % 360.0
    return slope_deg.astype(np.float32), aspect_deg.astype(np.float32)


def aspect_correction(
    aspect_deg: np.ndarray,
    slope_deg: np.ndarray,
    max_effect: float = 0.8,
) -> np.ndarray:
    """坡向辐射修正（°C）：南坡增温、北坡降温，随坡度增大而增强。

    correction = max_effect × cos(aspect - 180°) × sin(slope)。
    """
    aspect = np.deg2rad(np.asarray(aspect_deg, dtype=np.float64))
    slope = np.deg2rad(np.asarray(slope_deg, dtype=np.float64))
    southness = np.cos(aspect - np.pi)  # 南=+1，北=-1
    return (max_effect * southness * np.sin(slope)).astype(np.float32)


def cold_air_pooling(
    dem: np.ndarray,
    radius: int = 5,
    pool_factor: float = 0.08,
    cap: float = -6.0,
) -> np.ndarray:
    """冷空气湖效应（°C，负值为降温）。

    以相对高程（DEM 减去其局部均值）衡量洼地汇流潜力：相对高程为负的洼地
    积聚冷空气而降温，山脊相对高程为正基本不受影响。降温幅度以 ``cap`` 为下限。
    """
    from scipy.ndimage import uniform_filter

    dem = np.asarray(dem, dtype=np.float64)
    size = 2 * int(max(radius, 1)) + 1
    focal_mean = uniform_filter(dem, size=size, mode="nearest")
    rel = dem - focal_mean
    # 仅洼地（rel<0）产生降温，并以 cap 为下限
    anomaly = np.clip(np.minimum(rel, 0.0) * float(pool_factor), float(cap), 0.0)
    return anomaly.astype(np.float32)


def apply_terrain_correction(
    tmin_ts: np.ndarray,
    dem: np.ndarray,
    lapse_rate: float = DEFAULT_LAPSE,
    pool_factor: float = 0.08,
    max_aspect_effect: float = 0.8,
    ref_elev: Optional[float] = None,
    res_m: float = 1000.0,
) -> np.ndarray:
    """对 (n_dates, H, W) 最低温时序施加地形修正，返回修正后时序。

    T_corr = T + [−lapse×(dem − ref_elev)] + cold_air_pooling + aspect_correction。
    高程越高越冷；洼地更冷；南坡略暖、北坡略冷。
    """
    tmin_ts = np.asarray(tmin_ts, dtype=np.float64)
    dem = np.asarray(dem, dtype=np.float64)
    if tmin_ts.ndim != 3:
        raise ValidationError("temperature time series must be (n_dates, H, W)")
    if tmin_ts.shape[1:] != dem.shape:
        raise ValidationError("DEM and temperature grid shapes mismatch")

    if ref_elev is None:
        ref_elev = float(np.mean(dem))

    lapse_term = -float(lapse_rate) * (dem - ref_elev)      # (H,W)
    pool_term = cold_air_pooling(dem, pool_factor=pool_factor)  # (H,W)
    slope, aspect = terrain_attributes(dem, res_m=res_m)
    aspect_term = aspect_correction(aspect, slope, max_effect=max_aspect_effect)

    correction = lapse_term + pool_term + aspect_term  # (H,W)
    return (tmin_ts + correction[None, :, :]).astype(np.float32)


# ---------------------------------------------------------------------------
# 核心算法：霜冻统计
# ---------------------------------------------------------------------------
def frost_frequency(tmin_ts: np.ndarray, threshold: float = 0.0) -> np.ndarray:
    """逐像元霜冻频率：Tmin ≤ threshold 的天数占比 (0-1)。

    NaN-safe：NaN 像元视为无效，频率按有效天数算（保留 NaN 标识）。
    """
    tmin_ts = np.asarray(tmin_ts, dtype=np.float64)
    if tmin_ts.ndim != 3:
        raise ValidationError("temperature time series must be (n_dates, H, W)")
    n = tmin_ts.shape[0]
    valid = np.isfinite(tmin_ts)
    frost = (tmin_ts <= threshold) & valid
    valid_count = valid.sum(axis=0).astype(np.float64)
    with np.errstate(invalid="ignore", divide="ignore"):
        freq = np.where(valid_count > 0, frost.sum(axis=0) / np.maximum(valid_count, 1), np.nan)
    return freq.astype(np.float32)


def _longest_run_above(series: np.ndarray, threshold: float) -> int:
    """一维序列中最长连续 > threshold 的游程长度（无霜期）。"""
    best = cur = 0
    for v in series:
        if v > threshold:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    return int(best)


def frost_season(
    tmin_ts: np.ndarray,
    threshold: float = 0.0,
) -> Dict[str, np.ndarray]:
    """逐像元首霜日、终霜日与无霜期。

    - first_frost: 首个 Tmin ≤ threshold 的日索引（无则 -1）
    - last_frost: 末个 Tmin ≤ threshold 的日索引（无则 -1）
    - frost_free_period: 最长连续 Tmin > threshold 的天数
    - frost_days: 霜冻总天数

    NaN-safe：NaN 像元既不算 frost 也不算 above。
    """
    tmin_ts = np.asarray(tmin_ts, dtype=np.float64)
    n, h, w = tmin_ts.shape
    valid = np.isfinite(tmin_ts)
    frost = (tmin_ts <= threshold) & valid
    above = (tmin_ts > threshold) & valid

    days = np.arange(n)
    any_frost = np.any(frost, axis=0)
    first_idx = np.argmax(frost, axis=0)  # 全 False 时为 0
    first_frost = np.where(any_frost, first_idx, -1).astype(np.int32)
    last_idx = n - 1 - np.argmax(frost[::-1], axis=0)
    last_frost = np.where(any_frost, last_idx, -1).astype(np.int32)

    # NaN-safe longest run above
    frost_free = np.zeros((h, w), dtype=np.int32)
    for j in range(h):
        for i in range(w):
            s = tmin_ts[:, j, i]
            v = above[:, j, i]
            # 仅在 valid 段内的最长连续 above 段
            best = cur = 0
            for k in range(n):
                if v[k]:
                    cur += 1
                    if cur > best:
                        best = cur
                else:
                    cur = 0
            frost_free[j, i] = int(best)

    frost_days = np.sum(frost, axis=0).astype(np.int32)
    return {
        "first_frost": first_frost,
        "last_frost": last_frost,
        "frost_free_period": frost_free,
        "frost_days": frost_days,
    }


def frost_risk_class(frost_freq: np.ndarray) -> np.ndarray:
    """由霜冻频率分级：0 无 / 1 低(≤0.1) / 2 中(≤0.3) / 3 高(≤0.6) / 4 严重(>0.6)。"""
    f = np.asarray(frost_freq, dtype=np.float64)
    out = np.zeros(f.shape, dtype=np.int32)
    out[f > 0.0] = 1
    out[f > 0.1] = 2
    out[f > 0.3] = 3
    out[f > 0.6] = 4
    return out


# ---------------------------------------------------------------------------
# 合成数据：含山脊与洼地的 DEM + 受高程影响的最低温时序
# ---------------------------------------------------------------------------
def generate_synthetic_dem(
    height: int = 64,
    width: int = 64,
    seed: int = 42,
) -> np.ndarray:
    """生成含两座山脊与一个中央洼地的 DEM（米）。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yn = yy.astype(np.float64) / max(height - 1, 1)
    xn = xx.astype(np.float64) / max(width - 1, 1)

    dem = np.full((height, width), 500.0, dtype=np.float64)
    # 两座山脊（高斯隆起）
    dem += 350.0 * np.exp(-(((xn - 0.25) ** 2 + (yn - 0.30) ** 2) / 0.02))
    dem += 300.0 * np.exp(-(((xn - 0.75) ** 2 + (yn - 0.70) ** 2) / 0.03))
    # 中央洼地（霜穴，冷空气湖）
    dem -= 500.0 * np.exp(-(((xn - 0.50) ** 2 + (yn - 0.50) ** 2) / 0.02))
    dem += rng.normal(0, 5.0, (height, width))
    return dem.astype(np.float32)


def generate_synthetic_tmin(
    dem: np.ndarray,
    n_dates: int = 30,
    base_temp: float = 4.0,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成（参考高程上的）日最低温时序 (n_dates, H, W)，含季节性降温趋势。

    注意：返回的是"平坦参考面"温度，尚未做地形修正；地形影响由
    apply_terrain_correction 施加，从而保证"温度随高程递减"可被检验。
    """
    rng = np.random.default_rng(seed)
    h, w = dem.shape
    ts = np.zeros((n_dates, h, w), dtype=np.float32)
    # 季节降温趋势：前期偏暖，后期偏冷
    trend = -4.0 * np.arange(n_dates) / max(n_dates - 1, 1)
    for t in range(n_dates):
        ts[t] = base_temp + trend[t] + rng.normal(0, 1.5, (h, w))
    info = {
        "n_dates": int(n_dates),
        "base_temp": float(base_temp),
        "shape": [int(h), int(w)],
    }
    return ts, info


def generate_synthetic(
    bbox: List[float],
    n_dates: int = 30,
    height: int = 64,
    width: int = 64,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """返回 (dem, tmin_ts, info)。tmin_ts 已施加地形修正。"""
    dem = generate_synthetic_dem(height, width, seed=seed)
    tmin_flat, tinfo = generate_synthetic_tmin(dem, n_dates=n_dates, seed=seed)
    tmin_ts = apply_terrain_correction(tmin_flat, dem)
    info = {
        "bbox": bbox,
        "n_dates": int(n_dates),
        "width": int(width),
        "height": int(height),
        "dem_min": float(np.min(dem)),
        "dem_max": float(np.max(dem)),
        **tinfo,
    }
    return dem, tmin_ts, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
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
    """读 GeoTIFF（向后兼容接口）。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_safe(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """读 GeoTIFF；NoData → NaN；全 NoData 抛 ValidationError。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nd = src.nodata
    if nd is not None:
        cube = np.where(cube == float(nd), np.nan, cube)
    n_valid = int(np.isfinite(cube).sum())
    if n_valid == 0:
        raise ValidationError(
            f"input raster is entirely NoData (nodata={nd}, shape={cube.shape})",
            path=path, n_valid_pixels=0,
        )
    return cube, bbox, nd


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
            "dem": getattr(args, "dem", None),
            "threshold": getattr(args, "threshold", None),
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
def _res_from_bbox(bbox: List[float], height: int, width: int) -> float:
    """由 bbox 与栅格尺寸估算像元分辨率（米），用于坡度计算。"""
    lat_mid = 0.5 * (bbox[1] + bbox[3])
    dx = (bbox[2] - bbox[0]) * 111320.0 * np.cos(np.deg2rad(lat_mid)) / max(width, 1)
    dy = (bbox[3] - bbox[1]) * 110540.0 / max(height, 1)
    return float(max(0.5 * (dx + dy), 1.0))


def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir
    bbox = list(args.bbox) if args.bbox else None

    # 1) 校验（在 makedirs 之前）
    validate_params(args)

    # 2) 获取数据
    synth_info: Optional[Dict[str, Any]] = None
    input_nodata: Optional[float] = None
    if args.input and not args.synthetic:
        tmin_ts, file_bbox, input_nodata = read_geotiff_safe(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            validate_bbox(bbox)
        if tmin_ts.ndim != 3:
            raise ValidationError("input must be a time series (n_dates, H, W)")
        if args.dem:
            dem_cube, _, _ = read_geotiff_safe(args.dem)
            dem = dem_cube[0]
        else:
            dem = generate_synthetic_dem(tmin_ts.shape[1], tmin_ts.shape[2])
        if args.correction == "terrain":
            res_m = _res_from_bbox(bbox, tmin_ts.shape[1], tmin_ts.shape[2])
            tmin_ts = apply_terrain_correction(tmin_ts, dem, res_m=res_m)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        dem, tmin_ts, synth_info = generate_synthetic(bbox, n_dates=args.n_dates)
        source_note = "synthetic"

    if tmin_ts.size == 0:
        raise ValidationError("input temperature cube is empty")
    n_valid_total = int(np.isfinite(tmin_ts).sum())
    n_total = int(tmin_ts.size)
    if n_valid_total == 0:
        raise ValidationError(
            "all input temperature pixels are NaN/NoData — nothing to analyze",
            n_valid_pixels=0, n_total_pixels=n_total,
        )

    # 3) 校验通过后再创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 4) 霜冻统计
    freq = frost_frequency(tmin_ts, threshold=args.threshold)
    season = frost_season(tmin_ts, threshold=args.threshold)
    risk = frost_risk_class(np.nan_to_num(freq, nan=0.0))  # NaN 视为 0 风险（nodata 哨兵）

    # 5) 写出产物（NaN 替换为 -9999.0 哨兵）
    risk_path = os.path.join(output_dir, "frost_risk.tif")
    frost_free_path = os.path.join(output_dir, "frost_free_period.tif")
    freq_path = os.path.join(output_dir, "frost_frequency.tif")
    risk_safe = np.where(np.isfinite(risk), risk, -1).astype(np.float32)
    write_geotiff(risk_path, risk_safe, bbox, nodata=-1.0)
    write_geotiff(frost_free_path, season["frost_free_period"].astype(np.float32), bbox,
                  nodata=-1.0)
    freq_safe = np.where(np.isfinite(freq), freq, -9999.0).astype(np.float32)
    write_geotiff(freq_path, freq_safe, bbox, nodata=-9999.0)

    # 6) 统计 JSON（NaN-safe）
    def _nanmean(a):
        v = a[np.isfinite(a)] if a.size else np.array([])
        return float(v.mean()) if v.size else 0.0

    risk_dist = {str(k): int(np.sum((risk == k) & np.isfinite(risk))) for k in range(5)}
    stats = {
        "threshold_c": float(args.threshold),
        "n_dates": int(tmin_ts.shape[0]),
        "shape": [int(tmin_ts.shape[1]), int(tmin_ts.shape[2])],
        "correction": args.correction,
        "dem_min_m": float(np.min(dem)),
        "dem_max_m": float(np.max(dem)),
        "mean_frost_frequency": _nanmean(freq),
        "mean_frost_free_days": float(np.mean(season["frost_free_period"])),
        "mean_frost_days": float(np.mean(season["frost_days"])),
        "risk_distribution": risk_dist,
    }
    stats_path = os.path.join(output_dir, "frost_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "threshold_c": float(args.threshold),
        "correction": args.correction,
        "mean_frost_frequency": stats["mean_frost_frequency"],
        "mean_frost_free_days": stats["mean_frost_free_days"],
        "risk_distribution": risk_dist,
        "n_valid_pixels": n_valid_total,
        "n_total_pixels": n_total,
    }
    if input_nodata is not None:
        qa["input_nodata"] = float(input_nodata)
    if synth_info is not None:
        qa["synthetic_dem_range"] = [synth_info["dem_min"], synth_info["dem_max"]]

    outputs = [
        {"path": risk_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "nodata": -1.0},
        {"path": frost_free_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "nodata": -1.0},
        {"path": freq_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "nodata": -9999.0},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] threshold: {args.threshold} C  n_dates: {tmin_ts.shape[0]}")
        print(f"[{SKILL_NAME}] mean frost frequency: {stats['mean_frost_frequency']:.3f}")
        print(f"[{SKILL_NAME}] mean frost-free days: {stats['mean_frost_free_days']:.1f}")
        print(f"[{SKILL_NAME}] risk distribution: {risk_dist}")
        print(f"[{SKILL_NAME}] output: {risk_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Frost risk mapping with terrain-corrected min-temperature.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input daily-min temperature time-series GeoTIFF (bands=days)")
    p.add_argument("--dem", help="optional DEM GeoTIFF (metres); synthetic if omitted")
    p.add_argument("--threshold", type=float, default=0.0,
                   help="frost temperature threshold in deg C (default: 0)")
    p.add_argument("--correction", default="terrain", choices=["terrain", "none"],
                   help="apply terrain correction (lapse/pooling/aspect) or none (default: terrain)")
    p.add_argument("--n-dates", type=int, default=30,
                   help="number of synthetic daily time steps (default: 30)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic DEM + min-temperature field (offline)")
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
