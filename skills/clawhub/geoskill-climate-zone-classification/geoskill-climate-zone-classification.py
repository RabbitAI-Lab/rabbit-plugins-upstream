#!/usr/bin/env python3
"""climate-zone-classification — 气候区划

基于月均温与月降水栅格执行气候区划，支持两种方案：

- **Köppen-Geiger（柯本-盖格）**：经典规则树。由最冷/最热月均温、年降水与
  降水季节分配判定 A（热带）/B（干旱）/C（温带）/D（寒带）/E（极地）五大组，
  并细分第二/第三字母（如 Af 热带雨林、BWh 热沙漠、Cfa 湿润亚热带、Dfc 亚寒带、
  ET 苔原）。输出编码为整型类别码。
- **Strahler（斯特拉勒发生分类，简化）**：按气温带（热带/副热带/中纬度/副极地/
  极地）与水分条件（湿润/干旱）归并为 10 个发生气候类。

数据源：本地 24 波段 GeoTIFF（band 1-12 = 1-12 月均温 °C，band 13-24 = 1-12 月
降水 mm），或使用 ``--synthetic`` 生成沿纬度分带的模拟气候场用于离线测试。
可选 ``--input2`` 提供第二期数据做气候区变化检测。

隐私声明 / Privacy：
- 默认完全离线运行，不发起任何网络请求。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python climate-zone-classification.py --input climate.tif --classification koppen
    python climate-zone-classification.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "climate-zone-classification"

# ---- Köppen-Geiger 类别码表（整型编码 + 字母标签）----
KOPPEN_CODES: Dict[int, str] = {
    1: "Af", 2: "Am", 3: "Aw", 4: "As",
    5: "BWh", 6: "BWk", 7: "BSh", 8: "BSk",
    9: "Csa", 10: "Csb", 11: "Csc", 12: "Cwa", 13: "Cwb", 14: "Cwc",
    15: "Cfa", 16: "Cfb", 17: "Cfc",
    18: "Dsa", 19: "Dsb", 20: "Dsc", 21: "Dwa", 22: "Dwb", 23: "Dwc", 24: "Dwd",
    25: "Dfa", 26: "Dfb", 27: "Dfc", 28: "Dfd",
    29: "ET", 30: "EF",
}

# ---- Strahler 简化发生分类码表 ----
STRAHLER_CODES: Dict[int, str] = {
    1: "tropical-wet", 2: "tropical-dry", 3: "subtropical-moist",
    4: "mediterranean", 5: "marine-west-coast", 6: "moist-continental",
    7: "dry-continental", 8: "subarctic", 9: "tundra", 10: "polar-ice",
}

# 月份天数（非闰年），用于 Am 阈值中的最短月降水
_MONTH_DAYS = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], dtype=np.float64)

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
# 核心算法
# ---------------------------------------------------------------------------
def koppen_single(
    tmon: np.ndarray,
    pmon: np.ndarray,
) -> Tuple[int, str]:
    """逐点 Köppen-Geiger 分类（标量版）。返回 (code, label)。

    tmon / pmon 为长度 12 的月均温(°C)与月降水(mm)数组。
    规则依据 Peel et al. 2007 (HESS) 的柯本-盖格分类。
    """
    t = np.asarray(tmon, dtype=np.float64).ravel()
    p = np.asarray(pmon, dtype=np.float64).ravel()
    if t.size != 12 or p.size != 12:
        raise ValidationError("need exactly 12 monthly values", n_temp=int(t.size))
    if np.any(~np.isfinite(t)) or np.any(~np.isfinite(p)):
        return 0, "unclassified"

    map_ = float(np.mean(t))
    tmin = float(np.min(t))
    tmax = float(np.max(t))
    n10 = int(np.sum(t >= 10.0))
    psum = float(np.sum(p))

    # 北半球约定：夏 = 4-9 月 (idx 3..8)，冬 = 10-3 月 (idx 0,1,2,9,10,11)
    psummer = float(np.sum(p[3:9]))
    pwinter = float(np.sum(p[[0, 1, 2, 9, 10, 11]]))

    # 干旱阈值（mm/yr）
    if 0.7 * psummer >= pwinter:  # 降水集中于夏
        pthresh = 20.0 * map_ + 280.0
    elif 0.7 * pwinter >= psummer:  # 降水集中于冬
        pthresh = 20.0 * map_
    else:
        pthresh = 20.0 * map_ + 140.0

    # 组 A：热带
    if tmin >= 18.0:
        pmin = float(np.min(p))
        if pmin >= 60.0:
            return 1, "Af"
        am_thresh = 100.0 - psum / 25.0
        if pmin >= am_thresh:
            return 2, "Am"
        if psummer > 0.7 * psum:
            return 3, "Aw"
        return 4, "As"

    # 组 B：干旱
    if psum < pthresh:
        if map_ >= 18.0:
            return (5, "BWh") if psum < 0.5 * pthresh else (7, "BSh")
        return (6, "BWk") if psum < 0.5 * pthresh else (8, "BSk")

    # 组 C：温带（最冷月 > -3°C，最热月 >= 10°C）
    if tmin > -3.0 and tmin < 18.0 and tmax >= 10.0:
        letter = _season_letter(p)
        return _encode_c_d("C", letter, tmax, n10)

    # 组 D：寒带/大陆性（最冷月 <= -3°C，最热月 >= 10°C）
    if tmin <= -3.0 and tmax >= 10.0:
        letter = _season_letter(p)
        return _encode_c_d("D", letter, tmax, n10)

    # 组 E：极地
    if tmax < 10.0:
        return (29, "ET") if tmax >= 0.0 else (30, "EF")

    return 0, "unclassified"


def _season_letter(p: np.ndarray) -> str:
    """判定 C/D 组的第二字母（s/w/f），采用 Köppen 最干月/最湿月规则。

    s（夏干）：夏半年最干月 < 40 mm 且 < 冬半年最湿月/3。
    w（冬干）：冬半年最干月 < 夏半年最湿月/10。
    f（常湿）：其余。
    """
    p_summer = p[3:9]
    p_winter = p[[0, 1, 2, 9, 10, 11]]
    p_driest_summer = float(np.min(p_summer))
    p_wettest_winter = float(np.max(p_winter))
    p_driest_winter = float(np.min(p_winter))
    p_wettest_summer = float(np.max(p_summer))
    if p_driest_summer < 40.0 and p_driest_summer < p_wettest_winter / 3.0:
        return "s"
    if p_driest_winter < p_wettest_summer / 10.0:
        return "w"
    return "f"


def _encode_c_d(group: str, letter: str, tmax: float, n10: int) -> Tuple[int, str]:
    """由组字母(C/D)、季节字母(s/w/f)、最热月温与暖月数编码出类别码。"""
    if tmax >= 22.0:
        third = "a"
    elif n10 >= 4:
        third = "b"
    else:
        third = "c"
    label = f"{group}{letter}{third}"
    # 反查码表
    for code, lab in KOPPEN_CODES.items():
        if lab == label:
            return code, label
    return 0, "unclassified"


def koppen_classify(temp: np.ndarray, precip: np.ndarray) -> np.ndarray:
    """向量化 Köppen-Geiger 分类。

    temp, precip: (12, H, W) 月均温(°C)与月降水(mm)。返回 (H, W) 整型类别码。
    """
    temp = np.asarray(temp, dtype=np.float64)
    precip = np.asarray(precip, dtype=np.float64)
    if temp.shape[0] != 12 or precip.shape[0] != 12:
        raise ValidationError(
            "need 12 monthly bands for temperature and precipitation",
            t_bands=int(temp.shape[0]), p_bands=int(precip.shape[0]),
        )
    h, w = temp.shape[1], temp.shape[2]
    out = np.zeros((h, w), dtype=np.int32)

    map_ = np.mean(temp, axis=0)
    tmin = np.min(temp, axis=0)
    tmax = np.max(temp, axis=0)
    n10 = np.sum(temp >= 10.0, axis=0)
    psum = np.sum(precip, axis=0)
    psummer = np.sum(precip[3:9], axis=0)
    pwinter = precip[0] + precip[1] + precip[2] + precip[9] + precip[10] + precip[11]
    psummer = precip[3] + precip[4] + precip[5] + precip[6] + precip[7] + precip[8]

    pthresh = np.where(0.7 * psummer >= pwinter, 20.0 * map_ + 280.0,
                       np.where(0.7 * pwinter >= psummer, 20.0 * map_,
                                20.0 * map_ + 140.0))

    pmin = np.min(precip, axis=0)
    am_thresh = 100.0 - psum / 25.0

    # 季节字母（全网格）：Köppen 最干月/最湿月规则
    p_driest_summer = np.min(precip[3:9], axis=0)
    p_wettest_summer = np.max(precip[3:9], axis=0)
    winter_months = np.stack(
        [precip[0], precip[1], precip[2], precip[9], precip[10], precip[11]], axis=0)
    p_driest_winter = np.min(winter_months, axis=0)
    p_wettest_winter = np.max(winter_months, axis=0)
    letter = np.full((h, w), "f", dtype="U1")
    s_mask = (p_driest_summer < 40.0) & (p_driest_summer < p_wettest_winter / 3.0)
    w_mask = (p_driest_winter < p_wettest_summer / 10.0) & ~s_mask
    letter[s_mask] = "s"
    letter[w_mask] = "w"

    # 组 A
    a_mask = tmin >= 18.0
    out[a_mask & (pmin >= 60.0)] = 1                          # Af
    out[a_mask & (pmin < 60.0) & (pmin >= am_thresh)] = 2     # Am
    out[a_mask & (pmin < 60.0) & (pmin < am_thresh) & (psummer > 0.7 * psum)] = 3  # Aw
    out[a_mask & (pmin < 60.0) & (pmin < am_thresh) & (psummer <= 0.7 * psum)] = 4  # As

    # 组 B
    b_mask = (~a_mask) & (psum < pthresh)
    hot = map_ >= 18.0
    out[b_mask & hot & (psum < 0.5 * pthresh)] = 5     # BWh
    out[b_mask & hot & (psum >= 0.5 * pthresh)] = 7    # BSh
    out[b_mask & ~hot & (psum < 0.5 * pthresh)] = 6    # BWk
    out[b_mask & ~hot & (psum >= 0.5 * pthresh)] = 8   # BSk

    # 组 C（温带）：最冷月 > -3°C，最热月 >= 10°C
    c_mask = (~a_mask) & (~b_mask) & (tmin > -3.0) & (tmin < 18.0) & (tmax >= 10.0)
    # 组 D（大陆性/寒带）：最冷月 <= -3°C，最热月 >= 10°C
    d_mask = (~a_mask) & (~b_mask) & (~c_mask) & (tmin <= -3.0) & (tmax >= 10.0)

    for grp, grp_mask in (("C", c_mask), ("D", d_mask)):
        for lt in ("s", "w", "f"):
            for td, code_third in (("a", "a"), ("b", "b"), ("c", "c")):
                if td == "a":
                    tmask = tmax >= 22.0
                elif td == "b":
                    tmask = (tmax < 22.0) & (n10 >= 4)
                else:
                    tmask = ~((tmax >= 22.0) | ((tmax < 22.0) & (n10 >= 4)))
                mask = grp_mask & (letter == lt) & tmask
                label = f"{grp}{lt}{code_third}"
                for code, lab in KOPPEN_CODES.items():
                    if lab == label:
                        out[mask] = code
                        break

    # 组 E
    e_mask = (~a_mask) & (~b_mask) & (~c_mask) & (~d_mask) & (tmax < 10.0)
    out[e_mask & (tmax >= 0.0)] = 29   # ET
    out[e_mask & (tmax < 0.0)] = 30    # EF

    return out


def strahler_classify(temp: np.ndarray, precip: np.ndarray) -> np.ndarray:
    """向量化 Strahler 简化发生气候分类。

    返回 (H, W) 整型类别码，码表见 STRAHLER_CODES。
    """
    temp = np.asarray(temp, dtype=np.float64)
    precip = np.asarray(precip, dtype=np.float64)
    if temp.shape[0] != 12 or precip.shape[0] != 12:
        raise ValidationError(
            "need 12 monthly bands for temperature and precipitation",
            t_bands=int(temp.shape[0]), p_bands=int(precip.shape[0]),
        )
    h, w = temp.shape[1], temp.shape[2]
    out = np.zeros((h, w), dtype=np.int32)

    tmin = np.min(temp, axis=0)
    tmax = np.max(temp, axis=0)
    psum = np.sum(precip, axis=0)
    psummer = precip[3] + precip[4] + precip[5] + precip[6] + precip[7] + precip[8]
    pwinter = precip[0] + precip[1] + precip[2] + precip[9] + precip[10] + precip[11]

    # 10: 极地冰原
    m_ice = tmax < 0.0
    # 9: 苔原
    m_tundra = (~m_ice) & (tmax < 10.0)
    # 8: 副极地（寒带）
    m_subarctic = (~m_ice) & (~m_tundra) & (tmin <= -10.0)
    # 6/7: 中纬度大陆性（湿润/干燥）
    m_midlat = (~m_ice) & (~m_tundra) & (~m_subarctic) & (tmin <= 0.0) & (tmax >= 10.0)
    m_dry_cont = m_midlat & (psum < 500.0)
    m_moist_cont = m_midlat & (psum >= 500.0)
    # 3/4/5: 副热带（湿润/地中海/西岸海洋性）
    m_subtrop = (~m_ice) & (~m_tundra) & (~m_subarctic) & (~m_midlat) & (tmin > 0.0) & (tmin < 18.0)
    m_medit = m_subtrop & (psummer < pwinter)
    m_wet_subtrop = m_subtrop & (~m_medit) & (psum >= 800.0)
    m_marine = m_subtrop & (~m_medit) & (~m_wet_subtrop)
    # 1/2: 热带（湿润/干燥）
    m_trop = (~m_ice) & (~m_tundra) & (~m_subarctic) & (~m_midlat) & (~m_subtrop) & (tmin >= 18.0)
    m_trop_dry = m_trop & (psum < 1000.0)
    m_trop_wet = m_trop & (psum >= 1000.0)

    out[m_trop_wet] = 1
    out[m_trop_dry] = 2
    out[m_wet_subtrop] = 3
    out[m_medit] = 4
    out[m_marine] = 5
    out[m_moist_cont] = 6
    out[m_dry_cont] = 7
    out[m_subarctic] = 8
    out[m_tundra] = 9
    out[m_ice] = 10
    return out


def classify_climate(temp: np.ndarray, precip: np.ndarray, method: str = "koppen") -> np.ndarray:
    """统一入口：method ∈ {koppen, strahler}。"""
    if method == "koppen":
        return koppen_classify(temp, precip)
    if method == "strahler":
        return strahler_classify(temp, precip)
    raise UsageError(f"unknown classification '{method}'", method=method)


def code_table(method: str) -> Dict[int, str]:
    return dict(KOPPEN_CODES) if method == "koppen" else dict(STRAHLER_CODES)


def area_statistics(
    codes: np.ndarray,
    bbox: List[float],
    method: str = "koppen",
) -> Dict[str, Any]:
    """统计每个气候类别的像元数、面积占比与估算面积 (km²)。

    面积用等距圆柱近似：像元纬度跨度 × 111.32 km，经度跨度 × 111.32×cos(lat)。
    """
    table = code_table(method)
    h, w = codes.shape
    total = int(codes.size)
    lat_mid = 0.5 * (bbox[1] + bbox[3])
    lon_span = bbox[2] - bbox[0]
    lat_span = bbox[3] - bbox[1]
    pixel_km2 = (lat_span / max(h, 1) * 111.32) * (lon_span / max(w, 1) * 111.32 * np.cos(np.deg2rad(lat_mid)))

    stats: List[Dict[str, Any]] = []
    for code in sorted(set(int(c) for c in np.unique(codes))):
        count = int(np.sum(codes == code))
        label = table.get(code, f"code_{code}")
        stats.append({
            "code": code,
            "label": label,
            "pixel_count": count,
            "fraction": count / total if total else 0.0,
            "area_km2": count * float(pixel_km2),
        })
    return {
        "method": method,
        "total_pixels": total,
        "pixel_area_km2": float(pixel_km2),
        "classes": stats,
    }


def climate_change(
    codes1: np.ndarray,
    codes2: np.ndarray,
) -> Dict[str, Any]:
    """两期气候区划变化检测。返回变化像元数、比例与主要迁移对。"""
    codes1 = np.asarray(codes1)
    codes2 = np.asarray(codes2)
    if codes1.shape != codes2.shape:
        raise ValidationError("shape mismatch between two climate epochs")
    changed = codes1 != codes2
    n_changed = int(np.sum(changed))
    total = int(codes1.size)
    transitions: Dict[str, int] = {}
    idx = np.argwhere(changed)
    for j, i in idx:
        key = f"{int(codes1[j, i])}->{int(codes2[j, i])}"
        transitions[key] = transitions.get(key, 0) + 1
    ranked = sorted(transitions.items(), key=lambda kv: kv[1], reverse=True)[:10]
    return {
        "changed_pixels": n_changed,
        "total_pixels": total,
        "changed_fraction": n_changed / total if total else 0.0,
        "transitions": [{"from_to": k, "count": v} for k, v in ranked],
    }


# ---------------------------------------------------------------------------
# 合成数据：沿纬度分带的模拟气候场（离线测试）
# ---------------------------------------------------------------------------
def _zone_profiles() -> List[Dict[str, Any]]:
    """返回由南（行 0）到北（行末）的气候带剖面。"""
    return [
        {"name": "Af", "base": 27.0, "amp": 1.0, "ptotal": 2200.0, "pat": "uniform"},
        {"name": "Aw", "base": 27.0, "amp": 2.0, "ptotal": 1400.0, "pat": "summer"},
        {"name": "BWh", "base": 25.0, "amp": 9.0, "ptotal": 120.0, "pat": "uniform"},
        {"name": "Cfa", "base": 17.0, "amp": 9.0, "ptotal": 1100.0, "pat": "uniform"},
        {"name": "Dfb", "base": 6.0, "amp": 14.0, "ptotal": 600.0, "pat": "uniform"},
        {"name": "ET", "base": -2.0, "amp": 4.0, "ptotal": 250.0, "pat": "uniform"},
    ]


def _monthly_precip(ptotal: float, pattern: str) -> np.ndarray:
    if pattern == "summer":
        weights = np.array([0.3, 0.3, 0.5, 1.0, 1.6, 2.2, 2.6, 2.6, 1.8, 0.9, 0.4, 0.3])
    elif pattern == "winter":
        weights = np.array([2.2, 2.0, 1.6, 1.0, 0.5, 0.3, 0.2, 0.3, 0.6, 1.2, 1.8, 2.2])
    else:
        weights = np.ones(12)
    return ptotal * weights / np.sum(weights)


def generate_synthetic_cube(
    bbox: List[float],
    height: int = 64,
    width: int = 64,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (24, H, W) 气候立方体：band 0-11 月均温，band 12-23 月降水。

    按行（纬度）分成 6 个气候带，每带赋以物理一致的温降与降水季节分配，
    使柯本分类能恢复出预期的气候类型（Af/Aw/BWh/Cfa/Dfb/ET）。
    """
    rng = np.random.default_rng(seed)
    profiles = _zone_profiles()
    n_bands = len(profiles)
    rows_per = height // n_bands
    lat = np.linspace(bbox[3], bbox[1], height)  # 行 0=北
    temp = np.zeros((12, height, width), dtype=np.float64)
    precip = np.zeros((12, height, width), dtype=np.float64)

    months = np.arange(12)
    for r in range(height):
        # 行 0 为北（高纬），行末为南（低纬）；把剖面按南→北排列后翻转
        band_idx = min(int((height - 1 - r) / max(rows_per, 1)), n_bands - 1)
        prof = profiles[band_idx]
        seasonal = prof["amp"] * np.cos(2.0 * np.pi * (months - 6.0) / 12.0)
        t_profile = prof["base"] + seasonal  # 北半球：7 月(idx6)最热
        p_profile = _monthly_precip(prof["ptotal"], prof["pat"])
        for m in range(12):
            temp[m, r, :] = t_profile[m] + rng.normal(0, 0.15, size=width)
            precip[m, r, :] = np.clip(p_profile[m] * (1.0 + rng.normal(0, 0.03, size=width)), 0.0, None)

    cube = np.concatenate([temp, precip], axis=0).astype(np.float32)
    # 每带中心行（用于验证）
    band_centers = {}
    for bi, prof in enumerate(profiles):
        r = height - 1 - int((bi + 0.5) * rows_per)
        r = int(np.clip(r, 0, height - 1))
        band_centers[prof["name"]] = {"row": r, "col": width // 2}
    info = {
        "bbox": bbox,
        "width": int(width),
        "height": int(height),
        "n_bands": 24,
        "zones": [p["name"] for p in profiles],
        "band_centers": band_centers,
    }
    return cube, info


# ---------------------------------------------------------------------------
# 输入校验：bbox（共用同 animated-map-series 模板）
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> None:
    """Validate a [W, S, E, N] bbox in WGS-84.

    Raises ValidationError (exit 6) for:
      - wrong length
      - non-finite values
      - longitude out of [-180, 180]
      - latitude  out of [-90, 90]
      - W >= E (would make a non-positive-width raster)
      - S >= N
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(
            f"bbox must have 4 floats [W S E N], got {bbox!r}",
        )
    w, s, e, n = bbox
    vals = [w, s, e, n]
    if not all(np.isfinite(vals)):
        raise ValidationError(f"bbox contains non-finite values: {vals}")
    if not (-180.0 <= w <= 180.0) or not (-180.0 <= e <= 180.0):
        raise ValidationError(
            f"longitude out of [-180, 180]: W={w}, E={e}",
        )
    if not (-90.0 <= s <= 90.0) or not (-90.0 <= n <= 90.0):
        raise ValidationError(
            f"latitude out of [-90, 90]: S={s}, N={n}",
        )
    if w >= e:
        raise ValidationError(
            f"bbox W must be < E (W={w}, E={e}); cross-180 not supported; "
            f"split into two bboxes at the dateline",
        )
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N (S={s}, N={n})",
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox extent too small (W={w}, E={e}, S={s}, N={n})",
        )


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    cube: np.ndarray,
    bbox: List[float],
    nodata: float = -9999.0,
    dtype: str = "float32",
) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype(dtype), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """Read a multi-band GeoTIFF, returning (cube, bbox) with NoData→NaN.

    Pixels whose value equals ``src.nodata`` are converted to NaN so that
    downstream classification (Köppen/Strahler) naturally marks them as
    ``unclassified`` (their `isfinite` test fails).
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nd = src.nodata
        if nd is not None:
            mask = cube == float(nd)
            if np.any(mask):
                cube = cube.copy()
                cube[mask] = np.nan
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
            "input2": getattr(args, "input2", None),
            "classification": getattr(args, "classification", None),
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

    # 1) 获取气候立方体（24 波段：温度 12 + 降水 12）
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, synth_info = generate_synthetic_cube(bbox)
        source_note = "synthetic"

    # 2) 校验（先于 makedirs，避免错误路径产生空目录）
    if cube.size == 0:
        raise ValidationError("input climate cube is empty")
    if cube.ndim != 3 or cube.shape[0] != 24:
        raise ValidationError(
            f"input must have 24 bands (12 temp + 12 precip), got {cube.shape[0] if cube.ndim == 3 else cube.ndim}D/{cube.shape[0] if cube.ndim == 3 else 0} bands",
        )
    if bbox is not None:
        validate_bbox(bbox)

    # 3) NoData / 全 NaN 校验（立方体中所有像元、所有时间步的有效性）
    if not np.any(np.isfinite(cube)):
        raise ValidationError(
            "input climate cube has no valid (finite) pixels across all bands "
            "(all NoData or NaN)",
        )

    # 现在 makedirs（所有校验已通过）
    os.makedirs(output_dir, exist_ok=True)

    temp = cube[0:12]
    precip = cube[12:24]

    # 2) 气候区划
    codes = classify_climate(temp, precip, method=args.classification)

    # 3) 面积统计
    stats = area_statistics(codes, bbox, method=args.classification)

    # 4) 可选：变化检测（第二期）
    change_info: Optional[Dict[str, Any]] = None
    if args.input2 and not args.synthetic:
        cube2, _ = read_geotiff(args.input2)
        if cube2.shape != cube.shape:
            raise ValidationError("input2 must have the same shape as input")
        codes2 = classify_climate(cube2[0:12], cube2[12:24], method=args.classification)
        change_info = climate_change(codes, codes2)

    # 5) 写出产物
    class_path = os.path.join(output_dir, "climate_zones.tif")
    write_geotiff(class_path, codes.astype(np.float32), bbox, nodata=0.0)

    stats_path = os.path.join(output_dir, "area_statistics.json")
    stats_payload = {
        "classification": args.classification,
        "code_table": {str(k): v for k, v in code_table(args.classification).items()},
        **stats,
    }
    if change_info is not None:
        stats_payload["change_detection"] = change_info
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats_payload, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "classification": args.classification,
        "shape": list(codes.shape),
        "n_valid_pixels": int(np.sum(
            np.all(np.isfinite(temp), axis=0) & np.all(np.isfinite(precip), axis=0)
        )),
        "n_classes_present": int(len(stats["classes"])),
        "dominant_class": max(stats["classes"], key=lambda c: c["pixel_count"])["label"]
        if stats["classes"] else None,
    }
    if change_info is not None:
        qa["changed_fraction"] = change_info["changed_fraction"]
    if synth_info is not None:
        qa["synthetic_zones"] = synth_info["zones"]

    outputs = [
        {"path": class_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] classification: {args.classification}")
        print(f"[{SKILL_NAME}] shape: {codes.shape}")
        print(f"[{SKILL_NAME}] classes present: {qa['n_classes_present']}")
        print(f"[{SKILL_NAME}] dominant: {qa['dominant_class']}")
        print(f"[{SKILL_NAME}] output: {class_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Climate zone classification (Köppen-Geiger / Strahler).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input 24-band GeoTIFF (12 temp + 12 precip monthly)")
    p.add_argument("--input2", help="optional second-epoch 24-band GeoTIFF for change detection")
    p.add_argument("--classification", default="koppen", choices=["koppen", "strahler"],
                   help="classification scheme (default: koppen)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic latitudinal climate field (offline)")
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
