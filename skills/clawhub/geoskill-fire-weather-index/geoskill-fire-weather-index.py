#!/usr/bin/env python3
"""fire-weather-index — 火险天气指数（加拿大 FWI 系统）

实现加拿大林火天气指数系统（Canadian Forest Fire Weather Index System，
Van Wagner 1987）。以每日正午气象观测（气温 ℃、相对湿度 %、风速 km/h、
24h 降水 mm）为输入，逐日递推六个分量：

- **FFMC**（Fine Fuel Moisture Code，细可燃物湿度码）
- **DMC**（Duff Moisture Code，腐殖质湿度码）
- **DC**（Drought Code，干旱码）
- **ISI**（Initial Spread Index，初始蔓延指数）
- **BUI**（Buildup Index，累积指数）
- **FWI**（Fire Weather Index，火险天气指数）

递推公式与 cffdrs（加拿大林火行为预测开源库）保持一致。FFMC 受降水
快速回落影响；DMC/DC 为累积型干旱指标；ISI/BUI/FWI 为综合指数。

数据源：本地多波段气象 GeoTIFF（4 波段 = 温度/湿度/风速/降水，单日），
或 ``--synthetic`` 生成一段含"干热大风→强降水"事件的气象时序（离线）。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python fire-weather-index.py --bbox 116 39 117 40 --n-dates 30 --output-dir ./out
    python fire-weather-index.py --bbox 116 39 117 40 --synthetic --output-dir ./out
    python fire-weather-index.py --input meteo_day.tif --output-dir ./out

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
SKILL_NAME = "fire-weather-index"

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


# 标准起始码值（Van Wagner 1987，春季典型初值）
FFMC0 = 85.0
DMC0 = 6.0
DC0 = 15.0

# 日长因子（day length factor），北半球约 46°N 的月度值
DLF = np.array([6.5, 7.5, 9.0, 12.8, 13.9, 13.9, 12.4, 10.9, 9.4, 8.0, 7.0, 6.0])

# FWI 火险等级阈值（加拿大常用分级）
FWI_CLASS_BREAKS = [5.0, 10.0, 20.0, 50.0]
FWI_CLASS_NAMES = ["Low", "Moderate", "High", "Very High", "Extreme"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# Input validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate a [W, S, E, N] geographic bbox.

    Raises ValidationError (exit 6) on:
      - non-finite values
      - longitude/latitude out of range
      - W >= E (no antimeridian wrap-around)
      - S >= N
      - zero-area bbox
    """
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


def read_geotiff_with_nodata(path: str):
    """Read a multi-band GeoTIFF, replacing NoData with NaN.

    Returns (cube_float32, bbox_WSEN, n_valid_pixel_steps).
    """
    cube, bbox = read_geotiff(path)
    import rasterio
    with rasterio.open(path) as src:
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == nodata, np.nan, cube).astype(np.float32)
    n_valid = int(np.sum(np.isfinite(cube)))
    return cube, bbox, n_valid


# ---------------------------------------------------------------------------
# 核心算法：FWI 六分量递推（矢量化，空间维度广播）
# ---------------------------------------------------------------------------
def ffmc_step(
    ffmc_prev: np.ndarray,
    temp: np.ndarray,
    rh: np.ndarray,
    ws: np.ndarray,
    precip: np.ndarray,
) -> np.ndarray:
    """FFMC 单日更新。输入/输出均为 2D 数组（H, W）。

    先做降水湿润，再按平衡含水率做干/湿弛豫。
    """
    mo = 147.2 * (101.0 - ffmc_prev) / (59.5 + ffmc_prev)

    rain_mask = precip > 0.5
    rf = np.where(rain_mask, precip - 0.5, 0.0)
    term = 42.5 * rf * np.exp(-100.0 / (251.0 - mo)) * (
        1.0 - np.exp(-6.93 / np.maximum(rf, 1e-6))
    )
    extra = np.where(
        mo > 150.0,
        0.0015 * np.power(np.maximum(mo - 150.0, 0.0), 2) * np.sqrt(np.maximum(rf, 0.0)),
        0.0,
    )
    mr = np.minimum(mo + term + extra, 250.0)
    mo_wet = np.where(rain_mask, mr, mo)

    rh_c = np.clip(rh, 1e-3, 100.0)
    Ed = (0.942 * rh_c ** 0.679 + 11.0 * np.exp((rh_c - 100.0) / 10.0)
          + 0.18 * (21.1 - temp) * (1.0 - np.exp(-0.115 * rh_c)))
    Ew = (0.618 * rh_c ** 0.753 + 10.0 * np.exp((rh_c - 100.0) / 10.0)
          + 0.18 * (21.1 - temp) * (1.0 - np.exp(-0.115 * rh_c)))

    ws_c = np.maximum(ws, 0.0)
    ko = 0.424 * (1.0 - (rh_c / 100.0) ** 1.7) + 0.0694 * np.sqrt(ws_c) * (
        1.0 - (rh_c / 100.0) ** 8)
    kd = ko * 0.581 * np.exp(0.0365 * temp)
    m_dry = Ed + (mo_wet - Ed) * np.power(10.0, -kd)

    k1 = 0.424 * (1.0 - ((100.0 - rh_c) / 100.0) ** 1.7) + 0.0694 * np.sqrt(ws_c) * (
        1.0 - ((100.0 - rh_c) / 100.0) ** 8)
    kw = k1 * 0.581 * np.exp(0.0365 * temp)
    m_wet = Ew - (Ew - mo_wet) * np.power(10.0, -kw)

    m = np.where(mo_wet > Ed, m_dry, np.where(mo_wet < Ew, m_wet, mo_wet))
    ffmc = 59.5 * (250.0 - m) / (147.2 + m)
    return np.clip(ffmc, 0.0, 101.0)


def dmc_step(dmc_prev: np.ndarray, temp: np.ndarray, precip: np.ndarray,
             month: int) -> np.ndarray:
    """DMC 单日更新：降水增湿 + 潜在蒸散累积失水。"""
    dlf = float(DLF[month - 1])
    rain_mask = precip > 1.5
    rw = np.where(rain_mask, 0.92 * precip - 1.27, 0.0)
    wmi = 20.0 + np.exp(5.6348 - dmc_prev / 43.43)
    b = np.where(
        dmc_prev <= 33.0,
        100.0 / (0.5 + 0.3 * dmc_prev),
        np.where(
            dmc_prev <= 65.0,
            14.0 - 1.3 * np.log(np.maximum(dmc_prev, 1e-6)),
            6.2 * np.log(np.maximum(dmc_prev, 1e-6)) - 17.2,
        ),
    )
    wmr = wmi + 1000.0 * rw / (48.77 + b * rw)
    dmc_wet = 43.43 * (5.6348 - np.log(np.maximum(wmr - 20.0, 1e-6)))
    dmc1 = np.where(rain_mask, dmc_wet, dmc_prev)
    dmc1 = np.maximum(dmc1, 0.0)
    t = np.maximum(temp, -1.1)
    pe = np.maximum((0.36 * (t + 2.8) + dlf) / 2.0, 0.0)
    return np.maximum(dmc1 + pe, 0.0)


def dc_step(dc_prev: np.ndarray, temp: np.ndarray, precip: np.ndarray,
            month: int) -> np.ndarray:
    """DC 单日更新：深层有机质干旱码。"""
    dlf = float(DLF[month - 1])
    rain_mask = precip > 2.8
    rw = np.where(rain_mask, 0.83 * precip - 1.27, 0.0)
    smi = 800.0 * np.exp(-dc_prev / 400.0)
    dc_wet = dc_prev - 400.0 * np.log(1.0 + 3.937 * rw / np.maximum(smi, 1e-6))
    dc1 = np.where(rain_mask, dc_wet, dc_prev)
    dc1 = np.maximum(dc1, 0.0)
    t = np.maximum(temp, -2.8)
    pe = np.maximum((0.36 * (t + 2.8) + dlf) / 2.0, 0.0)
    return np.maximum(dc1 + pe, 0.0)


def isi_step(ffmc: np.ndarray, ws: np.ndarray) -> np.ndarray:
    """ISI = 初始蔓延指数：由 FFMC 含水率与风速共同决定。"""
    m = 147.2 * (101.0 - ffmc) / (59.5 + ffmc)
    ff = 91.9 * np.exp(-0.1386 * m) * (1.0 + m ** 5.31 / 4.93e7)
    fw = np.exp(0.05039 * np.maximum(ws, 0.0))
    return np.maximum(0.208 * fw * ff, 0.0)


def bui_step(dmc: np.ndarray, dc: np.ndarray) -> np.ndarray:
    """BUI = 累积指数：DMC 与 DC 的非线性组合。"""
    denom = np.maximum(dmc + 0.4 * dc, 1e-6)
    branch1 = 0.8 * dmc * dc / denom
    branch2 = dmc - (1.0 - 0.8 * dc / denom) * (0.92 + (0.0114 * dmc) ** 1.7)
    bui = np.where(dmc <= 0.4 * dc, branch1, branch2)
    return np.maximum(bui, 0.0)


def fwi_step(isi: np.ndarray, bui: np.ndarray) -> np.ndarray:
    """FWI = 火险天气指数：ISI 与 BUI 经函数 fD 组合。"""
    fD = np.where(
        bui <= 80.0,
        0.626 * np.power(np.maximum(bui, 0.0), 0.809) + 2.0,
        1000.0 / (25.0 + 108.64 * np.exp(-0.023 * bui)),
    )
    B = 0.1 * isi * fD
    # 裁剪 log 项 >=0，避免 B<=1 时对负数取小数次幂产生 NaN/告警
    log_term = np.maximum(0.434 * np.log(np.maximum(B, 1e-6)), 0.0)
    fwi = np.where(B <= 1.0, B, np.exp(2.72 * np.power(log_term, 0.647)))
    return np.maximum(fwi, 0.0)


def classify_fwi(fwi: np.ndarray) -> np.ndarray:
    """将 FWI 值映射到火险等级（1=Low … 5=Extreme）。"""
    cls = np.ones(fwi.shape, dtype=np.int32)
    for i, brk in enumerate(FWI_CLASS_BREAKS):
        cls = np.where(fwi >= brk, i + 2, cls)
    return cls


def compute_fwi_series(
    temp: np.ndarray,
    rh: np.ndarray,
    ws: np.ndarray,
    precip: np.ndarray,
    months: np.ndarray,
) -> Dict[str, np.ndarray]:
    """逐日递推 FWI 六分量。

    输入为 (n_dates, H, W) 数组，months 为长度 n_dates 的整型月份（1-12）。
    返回同名键的 (n_dates, H, W) 数组字典。
    """
    temp = np.asarray(temp, dtype=np.float64)
    rh = np.asarray(rh, dtype=np.float64)
    ws = np.asarray(ws, dtype=np.float64)
    precip = np.asarray(precip, dtype=np.float64)
    if not (temp.shape == rh.shape == ws.shape == precip.shape):
        raise ValidationError(
            f"meteo arrays shape mismatch: {temp.shape} {rh.shape} {ws.shape} {precip.shape}")
    if temp.ndim != 3:
        raise ValidationError(f"meteo arrays must be 3D (n,H,W), got ndim={temp.ndim}")
    n = temp.shape[0]
    H, W = temp.shape[1:]
    if len(months) != n:
        raise ValidationError(f"months length {len(months)} != n_dates {n}")

    ffmc_prev = np.full((H, W), FFMC0)
    dmc_prev = np.full((H, W), DMC0)
    dc_prev = np.full((H, W), DC0)

    out = {k: np.zeros((n, H, W), dtype=np.float32)
           for k in ["FFMC", "DMC", "DC", "ISI", "BUI", "FWI"]}

    for t in range(n):
        month = int(months[t])
        if not 1 <= month <= 12:
            raise ValidationError(f"month {month} out of range 1..12 at step {t}")
        ffmc = ffmc_step(ffmc_prev, temp[t], rh[t], ws[t], precip[t])
        dmc = dmc_step(dmc_prev, temp[t], precip[t], month)
        dc = dc_step(dc_prev, temp[t], precip[t], month)
        isi = isi_step(ffmc, ws[t])
        bui = bui_step(dmc, dc)
        fwi = fwi_step(isi, bui)
        out["FFMC"][t] = ffmc.astype(np.float32)
        out["DMC"][t] = dmc.astype(np.float32)
        out["DC"][t] = dc.astype(np.float32)
        out["ISI"][t] = isi.astype(np.float32)
        out["BUI"][t] = bui.astype(np.float32)
        out["FWI"][t] = fwi.astype(np.float32)
        ffmc_prev, dmc_prev, dc_prev = ffmc, dmc, dc
    return out


# ---------------------------------------------------------------------------
# 合成数据：含"干热大风 → 强降水"事件的气象时序（离线）
# ---------------------------------------------------------------------------
def generate_synthetic_meteo(
    bbox: List[float],
    n_dates: int = 30,
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Dict[str, Any]:
    """生成物理一致的逐日气象场。

    前 60% 为干热大风期（FFMC/FWI 攀升），约 70% 处插入一次强降水事件
    （FFMC 快速回落），随后缓慢恢复。返回数组均为 (n_dates, H, W)。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy = yy / max(height - 1, 1)
    xx = xx / max(width - 1, 1)

    # 空间基础温度梯度：南部（下缘）更暖
    base_temp = 30.0 - 4.0 * yy + 1.5 * np.sin(2.0 * np.pi * xx)

    temp = np.zeros((n_dates, height, width), dtype=np.float32)
    rh = np.zeros((n_dates, height, width), dtype=np.float32)
    ws = np.zeros((n_dates, height, width), dtype=np.float32)
    precip = np.zeros((n_dates, height, width), dtype=np.float32)

    dry_end = int(0.6 * n_dates)
    rain_day = int(0.7 * n_dates)
    # 起始日期：北半球盛夏（7 月）
    start = _dt.datetime(2025, 7, 1)
    dates = [(start + _dt.timedelta(days=int(i))).strftime("%Y-%m-%d") for i in range(n_dates)]
    months = np.array([(start + _dt.timedelta(days=int(i))).month for i in range(n_dates)],
                      dtype=np.int32)

    for t in range(n_dates):
        if t < dry_end:
            # 干热大风期
            temp[t] = base_temp + 2.0 + rng.normal(0, 0.6, (height, width))
            rh[t] = 26.0 + 8.0 * xx + rng.normal(0, 2.0, (height, width))
            ws[t] = 18.0 + 6.0 * yy + rng.normal(0, 1.0, (height, width))
            precip[t] = 0.0
        elif t == rain_day:
            # 强降水事件
            temp[t] = base_temp - 6.0 + rng.normal(0, 0.5, (height, width))
            rh[t] = 90.0 + rng.normal(0, 2.0, (height, width))
            ws[t] = 8.0 + rng.normal(0, 1.0, (height, width))
            precip[t] = 24.0 + rng.normal(0, 2.0, (height, width))
        else:
            # 过渡 / 恢复期
            temp[t] = base_temp - 1.0 + rng.normal(0, 0.6, (height, width))
            rh[t] = 55.0 + 10.0 * xx + rng.normal(0, 2.0, (height, width))
            ws[t] = 12.0 + 3.0 * yy + rng.normal(0, 1.0, (height, width))
            precip[t] = np.where(rng.random((height, width)) < 0.15,
                                 rng.uniform(0.5, 4.0, (height, width)), 0.0)
        rh[t] = np.clip(rh[t], 5.0, 100.0)
        ws[t] = np.clip(ws[t], 0.0, None)
        precip[t] = np.clip(precip[t], 0.0, None)
        temp[t] = np.clip(temp[t], -5.0, 45.0)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "n_dates": n_dates,
        "dates": dates,
        "months": months.tolist(),
        "dry_end_index": dry_end,
        "rain_day_index": rain_day,
        "seed": seed,
    }
    return {
        "temp": temp.astype(np.float32),
        "rh": rh.astype(np.float32),
        "ws": ws.astype(np.float32),
        "precip": precip.astype(np.float32),
        "months": months,
        "info": info,
    }


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0) -> None:
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
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
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
            "synthetic": bool(getattr(args, "synthetic", False)),
            "n_dates": getattr(args, "n_dates", None),
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
    if bbox is not None:
        validate_bbox(bbox)
    if args.n_dates is not None and args.n_dates < 1:
        raise ValidationError(
            f"--n-dates must be >= 1, got {args.n_dates}", n_dates=args.n_dates
        )

    # 1) 获取气象数据
    synth_info: Optional[Dict[str, Any]] = None
    n_valid = 0
    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input raster not found: {args.input}", path=args.input)
        cube, file_bbox, n_valid = read_geotiff_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        validate_bbox(bbox)
        if cube.shape[0] < 4:
            raise ValidationError(
                "input raster must have >=4 bands (temp, rh, ws, precip); "
                f"got {cube.shape[0]}", bands=int(cube.shape[0]))
        # 单日 4 波段 → 单日递推
        temp = cube[0:1].astype(np.float32)
        rh = cube[1:2].astype(np.float32)
        ws = cube[2:3].astype(np.float32)
        precip = cube[3:4].astype(np.float32)
        months = np.array([7], dtype=np.int32)
        dates = ["single-day"]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        met = generate_synthetic_meteo(bbox, n_dates=args.n_dates)
        temp = met["temp"]; rh = met["rh"]; ws = met["ws"]; precip = met["precip"]
        months = met["months"]
        synth_info = met["info"]
        dates = synth_info["dates"]
        source_note = "synthetic"
        n_valid = int(np.sum(np.isfinite(temp)))

    if temp.size == 0:
        raise ValidationError("meteo data is empty")
    if n_valid == 0:
        raise ValidationError(
            "meteo data has no valid (non-NoData) pixel steps",
            shape=list(temp.shape),
        )

    # 2) FWI 递推
    series = compute_fwi_series(temp, rh, ws, precip, months)

    # Only create output dir after all validations have passed
    os.makedirs(output_dir, exist_ok=True)

    # 3) 输出：末日六分量栈 + 火险等级 + 时序 JSON
    final_stack = np.stack([series[k][-1] for k in ["FFMC", "DMC", "DC", "ISI", "BUI", "FWI"]],
                           axis=0).astype(np.float32)
    out_tif = os.path.join(output_dir, "fwi_components.tif")
    write_geotiff(out_tif, final_stack, bbox)

    fwi_final = series["FWI"][-1]
    class_final = classify_fwi(fwi_final).astype(np.float32)
    class_path = os.path.join(output_dir, "fwi_danger_class.tif")
    write_geotiff(class_path, class_final, bbox)

    # 时序：逐日空间均值
    timeseries = {
        "dates": dates,
        "FFMC_mean": [float(np.mean(series["FFMC"][t])) for t in range(len(dates))],
        "DMC_mean": [float(np.mean(series["DMC"][t])) for t in range(len(dates))],
        "DC_mean": [float(np.mean(series["DC"][t])) for t in range(len(dates))],
        "ISI_mean": [float(np.mean(series["ISI"][t])) for t in range(len(dates))],
        "BUI_mean": [float(np.mean(series["BUI"][t])) for t in range(len(dates))],
        "FWI_mean": [float(np.mean(series["FWI"][t])) for t in range(len(dates))],
    }
    ts_path = os.path.join(output_dir, "fwi_timeseries.json")
    with open(ts_path, "w", encoding="utf-8") as f:
        json.dump(timeseries, f, ensure_ascii=False, indent=2)

    # 火险等级面积占比
    total = class_final.size
    class_frac = {name: float(np.sum(class_final == (i + 1)) / total)
                  for i, name in enumerate(FWI_CLASS_NAMES)}

    n_total_pixel_steps = int(temp.shape[0] * temp.shape[1] * temp.shape[2])
    qa: Dict[str, Any] = {
        "source": source_note,
        "n_dates": int(len(dates)),
        "final_mean_components": {k: float(np.mean(series[k][-1]))
                                  for k in ["FFMC", "DMC", "DC", "ISI", "BUI", "FWI"]},
        "max_FWI": float(np.max(series["FWI"][-1])),
        "danger_class_fraction": class_frac,
        "n_valid_pixel_steps": n_valid,
        "n_total_pixel_steps": n_total_pixel_steps,
    }
    if synth_info is not None:
        qa["rain_day_index"] = synth_info["rain_day_index"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 6},
        {"path": class_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": ts_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  n_dates: {len(dates)}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        print(f"[{SKILL_NAME}] danger class: {class_path}")
        print(f"[{SKILL_NAME}] timeseries: {ts_path}")
        print(f"[{SKILL_NAME}] final mean FWI: {qa['final_mean_components']['FWI']:.3f}  "
              f"max FWI: {qa['max_FWI']:.3f}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Canadian FWI System: recursive FFMC/DMC/DC/ISI/BUI/FWI from daily weather.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input meteo GeoTIFF (4 bands: temp, rh, ws, precip)")
    p.add_argument("--n-dates", type=int, default=30,
                   help="number of synthetic daily steps (default: 30)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic weather series (offline)")
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
