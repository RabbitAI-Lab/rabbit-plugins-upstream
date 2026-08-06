#!/usr/bin/env python3
"""irrigation-scheduling — 灌溉制度优化

基于 FAO-56 Penman-Monteith 参考作物蒸散（ET₀）、作物系数 Kc 得到作物需水
ETc，驱动逐日根区土壤水分平衡，当消耗超过管理允许消耗（MAD）时触发灌溉，
生成灌溉日历与季节性总灌溉需水量空间分布。

核心算法
--------
- **FAO-56 Penman-Monteith ET₀**（Allen et al. 1998）：
  ET₀ = [0.408·Δ·(Rn−G) + γ·(900/(T+273))·u₂·(es−ea)] / [Δ + γ·(1+0.34·u₂)]
- **作物蒸散**：ETc = Kc · ET₀。
- **土壤水分平衡**：D_t = D_{t−1} + ETc_t − P_eff_t − Irr_t；
  当 D_t > MAD·TAW 时灌溉回补至田间持水量（D=0）。
- **季节性需水**：逐像元按土壤参数运行平衡，累加灌溉量。

数据源：本地土壤参数栅格或 ``--synthetic`` 离线模拟 + 内置代表性气象序列。

隐私声明 / Privacy：默认离线，``--synthetic`` 完全无网络，本地处理不上传。

Usage:
    python irrigation-scheduling.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "irrigation-scheduling"

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, DependencyError, to_exit_code,
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

    class DependencyError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=3, kind="EDepend", **k)

    class ProcessError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=7, kind="EProcess", **k)

    def to_exit_code(exc):
        return getattr(exc, "code", 7)

    OutputManifest = None
    OutputFile = None


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 参数校验（前置）
# ---------------------------------------------------------------------------
def validate_bbox(bbox):
    """W/E 经度 ∈ [-180, 180]，S/N 纬度 ∈ [-90, 90]，W<E，S<N。

    跨 180° 经线不支持（按既定约定给拆分提示，不做环绕）。
    """
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise UsageError(f"bbox must be [W, S, E, N], got {bbox!r}")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range: W={w}, E={e}; must be in [-180, 180]")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range: S={s}, N={n}; must be in [-90, 90]")
    if w >= e:
        if w > e and abs(w - e) < 1.0 and w > 170.0:
            raise ValidationError(
                f"bbox crosses the antimeridian (W={w} > E={e}); "
                f"split into two sub-bboxes instead")
        raise ValidationError(
            f"bbox W must be < E; got W={w}, E={e}")
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N; got S={s}, N={n}")
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero area: W={w}, E={e}, S={s}, N={n}")
    return [w, s, e, n]


def validate_params(args):
    """参数域校验：--mad ∈ (0, 1]。"""
    if not (0.0 < args.mad <= 1.0):
        raise ValidationError(
            f"--mad must be in (0, 1]; got {args.mad}")


# ---------------------------------------------------------------------------
# 核心算法：FAO-56 Penman-Monteith
# ---------------------------------------------------------------------------
def saturation_vapor_pressure(t_celsius: float) -> float:
    """饱和水汽压 es (kPa)，Tetens 公式。"""
    t = float(t_celsius)
    return 0.6108 * np.exp(17.27 * t / (t + 237.3))


def slope_vapor_curve(t_celsius: float) -> float:
    """饱和水汽压曲线斜率 Δ (kPa/°C)。"""
    t = float(t_celsius)
    es = saturation_vapor_pressure(t)
    return 4098.0 * es / (t + 237.3) ** 2


def psychrometric_constant(elevation_m: float = 0.0) -> float:
    """湿度计常数 γ (kPa/°C)，随气压（海拔）变化。"""
    p = 101.3 * ((293.0 - 0.0065 * elevation_m) / 293.0) ** 5.26
    return 0.000665 * p


def net_radiation(rs: float, tmean: float, rh: float, lat_deg: float) -> float:
    """净辐射 Rn (MJ/m²/day)，简化 FAO 长短波平衡。"""
    albedo = 0.23
    rns = (1.0 - albedo) * max(rs, 0.0)
    # 长波出射：Stefan-Boltzmann，含湿度与云量（用 Rs/Rso 近似）修正
    sigma = 4.903e-9
    tk = tmean + 273.16
    ea = saturation_vapor_pressure(tmean) * np.clip(rh, 0.0, 100.0) / 100.0
    # 晴空太阳辐射 Rso 近似（Angstrom，取典型晴天比例）
    rso = max(0.2 * 5.0, 0.75 * (0.25 + 0.5) * 5.0)  # 粗略锚定
    cloud = np.clip(0.9 * (max(rs, 0.0) / max(rso, 1e-3)) + 0.1, 0.05, 1.0)
    emissivity = 0.34 - 0.14 * np.sqrt(max(ea, 0.0))
    rnl = sigma * tk ** 4 * emissivity * cloud
    return float(rns - rnl)


def penman_monteith_et0(tmean: float, wind2: float, rh: float, rs: float,
                        lat_deg: float, doy: int, elevation: float = 0.0) -> float:
    """FAO-56 Penman-Monteith 参考蒸散 ET₀ (mm/day)。"""
    delta = slope_vapor_curve(tmean)
    gamma = psychrometric_constant(elevation)
    es = saturation_vapor_pressure(tmean)
    ea = es * np.clip(rh, 0.0, 100.0) / 100.0
    rn = net_radiation(rs, tmean, rh, lat_deg)
    g = 0.0  # 日尺度土壤热通量近似为 0
    u2 = max(wind2, 0.1)
    t_k = tmean + 273.0
    numerator = 0.408 * delta * (rn - g) + gamma * (900.0 / t_k) * u2 * (es - ea)
    denominator = delta + gamma * (1.0 + 0.34 * u2)
    et0 = numerator / denominator
    return float(max(et0, 0.0))


def crop_et(et0: float, kc: float) -> float:
    """作物蒸散 ETc = Kc · ET₀。"""
    return float(max(et0, 0.0) * max(kc, 0.0))


# ---------------------------------------------------------------------------
# 核心算法：土壤水分平衡与灌溉日历
# ---------------------------------------------------------------------------
def total_available_water(theta_fc: float, theta_wp: float, root_depth_mm: float) -> float:
    """根区总有效水 TAW (mm) = (θ_fc − θ_wp) · 根区深度。"""
    if theta_fc <= theta_wp:
        raise ValidationError("theta_fc must exceed theta_wp",
                              theta_fc=theta_fc, theta_wp=theta_wp)
    return float((theta_fc - theta_wp) * root_depth_mm)


def soil_water_balance(et0_series: np.ndarray, precip_series: np.ndarray,
                       kc_series: np.ndarray, theta_fc: float, theta_wp: float,
                       root_depth_mm: float, mad: float = 0.5,
                       eff_precip_frac: float = 0.8,
                       start_date: str = "2026-04-01") -> Dict[str, Any]:
    """逐日根区水分平衡，MAD 触发灌溉回补至田间持水量。

    返回 depletion 序列、灌溉事件列表、季节性总灌溉量 (mm)。
    """
    et0 = np.asarray(et0_series, dtype=np.float32)
    precip = np.asarray(precip_series, dtype=np.float32)
    kc = np.asarray(kc_series, dtype=np.float32)
    n = et0.shape[0]
    if precip.shape[0] != n or kc.shape[0] != n:
        raise ValidationError("et0/precip/kc series must share length")
    if not (0.0 < mad <= 1.0):
        raise ValidationError("mad must be in (0, 1]", mad=mad)

    taw = total_available_water(theta_fc, theta_wp, root_depth_mm)
    threshold = mad * taw

    depletion = np.zeros(n, dtype=np.float32)
    d = 0.0
    events: List[Dict[str, Any]] = []
    total_irr = 0.0
    base = _dt.date.fromisoformat(start_date)
    for i in range(n):
        etc = crop_et(float(et0[i]), float(kc[i]))
        peff = eff_precip_frac * max(float(precip[i]), 0.0)
        d = d + etc - peff
        irr = 0.0
        if d > threshold:
            irr = d  # 回补至田间持水量 (D=0)
            events.append({
                "day_index": int(i),
                "date": (base + _dt.timedelta(days=int(i))).isoformat(),
                "amount_mm": float(irr),
                "et0_mm": float(et0[i]),
            })
            total_irr += irr
            d = 0.0
        d = max(d, 0.0)
        depletion[i] = d

    return {
        "depletion": depletion,
        "events": events,
        "total_irrigation_mm": float(total_irr),
        "n_events": int(len(events)),
        "taw_mm": float(taw),
        "threshold_mm": float(threshold),
    }


def seasonal_requirement_grid(soil_cube: np.ndarray, et0_series: np.ndarray,
                              precip_series: np.ndarray, kc_series: np.ndarray,
                              mad: float = 0.5) -> np.ndarray:
    """逐像元运行水分平衡，返回季节性总灌溉需水量 (mm) 栅格。

    soil_cube 波段顺序 [theta_fc, theta_wp, root_depth_mm]。
    """
    soil_cube = np.asarray(soil_cube, dtype=np.float32)
    if soil_cube.ndim != 3 or soil_cube.shape[0] < 3:
        raise ValidationError("soil input needs 3 bands [theta_fc, theta_wp, root_depth_mm]")
    fc, wp, rd = soil_cube[0], soil_cube[1], soil_cube[2]
    out = np.zeros(fc.shape, dtype=np.float32)
    it = np.nditer([fc, wp, rd], flags=["multi_index"])
    for fcv, wpv, rdv in it:
        fcvf, wpvf, rdvf = float(fcv), float(wpv), float(rdv)
        if fcvf <= wpvf or rdvf <= 0:
            out[it.multi_index] = 0.0
            continue
        res = soil_water_balance(et0_series, precip_series, kc_series,
                                 fcvf, wpvf, rdvf, mad=mad)
        out[it.multi_index] = res["total_irrigation_mm"]
    return out


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_season_weather(n_days: int = 120, lat_deg: float = 39.0, seed: int = 42):
    """生成代表性生长季日气象序列（温度、辐射、降水、Kc）。"""
    rng = np.random.default_rng(seed)
    doy = np.arange(91, 91 + n_days)  # 从 4 月初开始
    # 温度：季节正弦 + 噪声
    tmean = 18.0 + 8.0 * np.sin(np.linspace(0, np.pi, n_days)) + rng.normal(0, 1.5, n_days)
    rs = np.clip(18.0 + 6.0 * np.sin(np.linspace(0, np.pi, n_days)) + rng.normal(0, 2, n_days), 5, 35)
    wind = np.clip(rng.normal(2.0, 0.6, n_days), 0.3, 8)
    rh = np.clip(rng.normal(55, 10, n_days), 20, 95)
    # 降水：偶发
    precip = rng.gamma(1.5, 4.0, n_days) * (rng.random(n_days) < 0.3)
    # Kc 曲线：初期低、中期高、末期降
    kc = np.clip(0.4 + 0.8 * np.sin(np.linspace(0, np.pi, n_days)), 0.3, 1.2)
    et0 = np.array([penman_monteith_et0(float(tmean[i]), float(wind[i]), float(rh[i]),
                                        float(rs[i]), lat_deg, int(doy[i]))
                    for i in range(n_days)], dtype=np.float32)
    return {
        "tmean": tmean.astype(np.float32), "rs": rs.astype(np.float32),
        "wind": wind.astype(np.float32), "rh": rh.astype(np.float32),
        "precip": precip.astype(np.float32), "kc": kc.astype(np.float32),
        "et0": et0, "doy": doy,
    }


def generate_synthetic(bbox: List[float], width: int = 32, height: int = 32, seed: int = 42):
    """波段 [theta_fc, theta_wp, root_depth_mm]；左湿（高持水）右干（砂质）。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1)
    theta_fc = np.clip(0.42 - 0.12 * xx + rng.normal(0, 0.01, (height, width)), 0.15, 0.5)
    theta_wp = np.clip(theta_fc - (0.18 - 0.05 * xx), 0.05, 0.4)
    root_depth = np.full((height, width), 600.0, dtype=np.float32)  # mm
    soil = np.stack([theta_fc, theta_wp, root_depth], axis=0).astype(np.float32)
    weather = generate_season_weather(n_days=120, lat_deg=(bbox[1] + bbox[3]) / 2, seed=seed)
    info = {"bbox": bbox, "width": width, "height": height,
            "band_order": ["theta_fc", "theta_wp", "root_depth_mm"],
            "season_days": 120, "mean_et0": float(weather["et0"].mean())}
    return soil, {"info": info, "weather": weather}


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


def read_geotiff_nodata(path: str) -> Optional[float]:
    """从 GeoTIFF 读 nodata 值（独立函数）。"""
    import rasterio
    with rasterio.open(path) as src:
        return src.nodata


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None), "method": getattr(args, "method", None),
                "mad": getattr(args, "mad", None), "synthetic": bool(getattr(args, "synthetic", False))},
        outputs=[OutputFile(**o) for o in outputs], qa=qa,
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

    # ---- 前置校验：参数 + bbox（必须先于 os.makedirs）----
    validate_params(args)
    if bbox is not None:
        bbox = validate_bbox(bbox)

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        soil, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            bbox = validate_bbox(bbox)
        # NoData -> NaN 替换；全 NoData -> rc=6
        src_nodata = read_geotiff_nodata(args.input)
        if src_nodata is not None:
            soil = np.where(soil == src_nodata, np.nan, soil).astype(np.float32)
        valid_mask = np.isfinite(soil).all(axis=0)
        if not valid_mask.any():
            raise ValidationError("all input pixels are NoData")
        weather = generate_season_weather(n_days=120, lat_deg=(bbox[1] + bbox[3]) / 2)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        soil, packed = generate_synthetic(bbox)
        weather = packed["weather"]
        synth_info = packed["info"]
        source_note = "synthetic"

    if soil.size == 0:
        raise ValidationError("input raster is empty")
    if soil.shape[0] < 3:
        raise ValidationError("soil input needs 3 bands [theta_fc, theta_wp, root_depth_mm]")

    # ---- 校验通过后再创建输出目录（避免失败时留空目录）----
    os.makedirs(output_dir, exist_ok=True)

    req = seasonal_requirement_grid(soil, weather["et0"], weather["precip"],
                                    weather["kc"], mad=args.mad)

    # 代表性像元（中心）的灌溉日历
    h, w = req.shape
    cx, cy = w // 2, h // 2
    fc_v, wp_v, rd_v = float(soil[0, cy, cx]), float(soil[1, cy, cx]), float(soil[2, cy, cx])
    cal = soil_water_balance(weather["et0"], weather["precip"], weather["kc"],
                             fc_v, wp_v, rd_v, mad=args.mad)

    req_tif = os.path.join(output_dir, "irrigation_requirement.tif")
    write_geotiff(req_tif, req, bbox)

    cal_json = os.path.join(output_dir, "irrigation_calendar.json")
    with open(cal_json, "w", encoding="utf-8") as f:
        json.dump({"center_pixel": [cx, cy], "theta_fc": fc_v, "theta_wp": wp_v,
                   "root_depth_mm": rd_v, "mad": args.mad,
                   "n_events": cal["n_events"], "total_irrigation_mm": cal["total_irrigation_mm"],
                   "events": cal["events"]}, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "method": args.method, "mad": args.mad,
          "mean_seasonal_req_mm": float(np.nanmean(req)),
          "center_n_events": cal["n_events"], "mean_et0": float(weather["et0"].mean())}
    if synth_info is not None:
        qa["synthetic"] = synth_info

    outputs = [
        {"path": req_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": cal_json, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean seasonal requirement: {qa['mean_seasonal_req_mm']:.1f} mm")
        print(f"[{SKILL_NAME}] center pixel events: {cal['n_events']}  total: {cal['total_irrigation_mm']:.1f} mm")
        print(f"[{SKILL_NAME}] output: {req_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Irrigation scheduling via FAO-56 Penman-Monteith ET0 and a MAD-triggered soil water balance.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input soil GeoTIFF [theta_fc, theta_wp, root_depth_mm]")
    p.add_argument("--method", default="penman-monteith", choices=["penman-monteith", "hargreaves"],
                   help="ET0 method (default: penman-monteith)")
    p.add_argument("--mad", type=float, default=0.5,
                   help="management allowed depletion fraction (default: 0.5)")
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
