#!/usr/bin/env python3
"""monsoon-analysis — 季风分析

对风场与降水时序做季风诊断，输出三类指标：

- **风场季节反转**：冬/夏季风风向相反。用纬向风 u 的季节差定义季风指数
  MI = mean(u, 夏半年) − mean(u, 冬半年)（Webster-Yang 型剪切指数），
  并计算冬/夏平均风向夹角（接近 180° 表示强反转）。
- **降水集中度**：季风期降水占全年比例（Concentration），及归一化季节性指数。
- **季风进退日期**：在逐日降水/风场序列上检测突变点 ——  onset（进入）为
  累计降水或纬向风由负转正/越过阈值的日期，retreat（撤退）为峰值后的回落点。

数据源：本地风场/降水 GeoTIFF（多波段时序），或 ``--synthetic`` 生成季节反转
风场 + 季风期集中降水（离线）。支持 ``--region east_asia|south_asia``。

隐私声明 / Privacy：默认离线，``--synthetic`` 完全无网络，所有处理本地完成。

Usage:
    python monsoon-analysis.py --bbox 110 20 122 40 --region east_asia --output-dir ./out
    python monsoon-analysis.py --bbox 70 8 90 30 --region south_asia --synthetic --output-dir ./out

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
SKILL_NAME = "monsoon-analysis"

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


# 区域配置：季风期月份（闭区间）、夏季风主导纬向风符号（东亚夏季偏南→u 略正/南分量，
# 这里以 u 的半年差刻画反转强度；南亚夏季西南风 u 为负但反转更强）
REGIONS: Dict[str, Dict[str, Any]] = {
    "east_asia": {
        "monsoon_months": [5, 6, 7, 8, 9],
        "winter_months": [11, 12, 1, 2],
        "summer_u_sign": 1.0,
        "peak_month": 7,
    },
    "south_asia": {
        "monsoon_months": [6, 7, 8, 9],
        "winter_months": [12, 1, 2],
        "summer_u_sign": -1.0,
        "peak_month": 7,
    },
}


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def wind_direction_deg(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """气象风向（来向，deg，北=0 东=90）。"""
    direc = np.rad2deg(np.arctan2(-u, -v))
    return np.mod(direc, 360.0)


def direction_reversal(u_winter: np.ndarray, v_winter: np.ndarray,
                       u_summer: np.ndarray, v_summer: np.ndarray) -> float:
    """冬/夏平均风向的最小夹角（0-180°）。接近 180° 表示完全反转。"""
    dw = float(np.nanmean(wind_direction_deg(u_winter, v_winter)))
    ds = float(np.nanmean(wind_direction_deg(u_summer, v_summer)))
    diff = abs(dw - ds) % 360.0
    return float(min(diff, 360.0 - diff))


def monsoon_index(u: np.ndarray, summer_idx: List[int],
                  winter_idx: List[int]) -> np.ndarray:
    """季风指数（Webster-Yang 型纬向风剪切）：夏半年均 u − 冬半年均 u。

    返回 (H, W) 数组。
    """
    u_summer = np.mean(u[summer_idx], axis=0)
    u_winter = np.mean(u[winter_idx], axis=0)
    return u_summer - u_winter


def precipitation_concentration(precip: np.ndarray,
                                monsoon_idx: List[int]) -> Dict[str, float]:
    """季风期降水集中度。precip 为 (n,) 序列（可含空间均值后的 1D）。

    返回 concentration（季风期占全年比）与 seasonality（相对均匀分布的偏离）。
    """
    precip = np.asarray(precip, dtype=np.float64)
    total = float(np.sum(precip))
    if total <= 0:
        return {"concentration": 0.0, "seasonality": 0.0,
                "monsoon_total": 0.0, "annual_total": 0.0}
    monsoon_total = float(np.sum(precip[monsoon_idx]))
    concentration = monsoon_total / total
    # 归一化季节性：相对均匀分布（每步 total/n）的 L1 偏离，归一到 [0,1]
    n = precip.size
    uniform = total / n
    seasonality = float(0.5 * np.sum(np.abs(precip - uniform)) / total)
    return {"concentration": concentration, "seasonality": seasonality,
            "monsoon_total": monsoon_total, "annual_total": total}


def detect_onset_retreat(precip_daily: np.ndarray, smooth: int = 5) -> Dict[str, Any]:
    """检测季风进退日期索引。

    - onset：平滑累计降水标准化序列首次越过 0.2 的步。
    - peak：累计降水斜率最大处（即降水速率峰值）。
    - retreat：峰值后标准化累计序列越过 0.8 的步。
    """
    p = np.asarray(precip_daily, dtype=np.float64)
    n = p.size
    if n == 0:
        raise ValidationError("empty precipitation series")
    total = p.sum()
    if total <= 0:
        return {"onset_index": 0, "peak_index": n // 2, "retreat_index": n - 1}

    # 平滑
    if smooth > 1 and n >= smooth:
        kernel = np.ones(smooth) / smooth
        ps = np.convolve(p, kernel, mode="same")
    else:
        ps = p.copy()
    cum = np.cumsum(ps)
    norm = cum / max(cum[-1], 1e-9)

    onset = int(np.argmax(norm >= 0.2))
    retreat = int(np.argmax(norm >= 0.8))
    if retreat <= onset:
        retreat = n - 1
    # peak：降水速率（平滑序列）最大处
    peak = int(np.argmax(ps))
    return {"onset_index": onset, "peak_index": peak, "retreat_index": retreat}


def analyze_monsoon(
    u: np.ndarray,
    v: np.ndarray,
    precip_monthly: np.ndarray,
    precip_daily: np.ndarray,
    months: np.ndarray,
    region: str,
) -> Dict[str, Any]:
    """综合季风诊断。u/v/precip_monthly 为 (n,H,W)，precip_daily 为 (m,) 或 (m,H,W)。"""
    if region not in REGIONS:
        raise UsageError(f"unknown region '{region}'. Choose from: {sorted(REGIONS)}",
                         region=region)
    cfg = REGIONS[region]
    months = np.asarray(months)
    summer_idx = [i for i, m in enumerate(months) if int(m) in cfg["monsoon_months"]]
    winter_idx = [i for i, m in enumerate(months) if int(m) in cfg["winter_months"]]
    if not summer_idx or not winter_idx:
        raise ValidationError(
            f"time series must cover both monsoon {cfg['monsoon_months']} "
            f"and winter {cfg['winter_months']} months for region '{region}'")

    u_summer = np.mean(u[summer_idx], axis=0)
    u_winter = np.mean(u[winter_idx], axis=0)
    v_summer = np.mean(v[summer_idx], axis=0)
    v_winter = np.mean(v[winter_idx], axis=0)

    reversal = direction_reversal(u_winter, v_winter, u_summer, v_summer)
    mi = monsoon_index(u, summer_idx, winter_idx)

    # 降水集中度用域均月降水序列
    if precip_monthly.ndim == 3:
        precip_series = np.array([float(np.mean(precip_monthly[t]))
                                  for t in range(precip_monthly.shape[0])])
    else:
        precip_series = precip_monthly.astype(np.float64)
    conc = precipitation_concentration(precip_series, summer_idx)

    # 进退日期用逐日序列（若多维则取域均）
    if precip_daily.ndim == 3:
        pd_series = np.array([float(np.mean(precip_daily[t]))
                              for t in range(precip_daily.shape[0])])
    else:
        pd_series = precip_daily.astype(np.float64)
    onset_retreat = detect_onset_retreat(pd_series)

    return {
        "region": region,
        "reversal_angle_deg": reversal,
        "monsoon_index_mean": float(np.mean(mi)),
        "monsoon_index_field": mi,
        "u_summer_mean": float(np.mean(u_summer)),
        "u_winter_mean": float(np.mean(u_winter)),
        "summer_idx": summer_idx,
        "winter_idx": winter_idx,
        "concentration": conc["concentration"],
        "seasonality": conc["seasonality"],
        "monsoon_total": conc["monsoon_total"],
        "annual_total": conc["annual_total"],
        "onset_index": onset_retreat["onset_index"],
        "peak_index": onset_retreat["peak_index"],
        "retreat_index": onset_retreat["retreat_index"],
    }


# ---------------------------------------------------------------------------
# 合成数据：季节反转风场 + 季风期集中降水（离线）
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], region: str = "east_asia",
                       n_dates: int = 24, width: int = 64, height: int = 64,
                       seed: int = 42) -> Dict[str, Any]:
    """生成 n_dates 个月（1 月起）的风场 u/v 与月降水，另生成逐日降水用于进退检测。"""
    if region not in REGIONS:
        raise UsageError(f"unknown region '{region}'. Choose from: {sorted(REGIONS)}",
                         region=region)
    cfg = REGIONS[region]
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy = yy / max(height - 1, 1)
    xx = xx / max(width - 1, 1)

    months = np.array([((i % 12) + 1) for i in range(n_dates)], dtype=np.int32)
    # 季节相位：1 月隆冬为 -1，7 月盛夏为 +1
    phase = -np.cos(2 * np.pi * (months - 1) / 12.0)
    sign = cfg["summer_u_sign"]

    u = np.zeros((n_dates, height, width), dtype=np.float32)
    v = np.zeros((n_dates, height, width), dtype=np.float32)
    precip_monthly = np.zeros((n_dates, height, width), dtype=np.float32)

    for t in range(n_dates):
        amp = 6.0 * (0.6 + 0.4 * xx)
        u[t] = sign * amp * phase[t] + rng.normal(0, 0.5, (height, width))
        v[t] = amp * 0.8 * phase[t] + rng.normal(0, 0.5, (height, width))
        month = int(months[t])
        if month in cfg["monsoon_months"]:
            base = 180.0 if month == cfg["peak_month"] else 120.0
            precip_monthly[t] = base + 30.0 * yy + rng.normal(0, 8.0, (height, width))
        else:
            precip_monthly[t] = 25.0 + 10.0 * yy + rng.normal(0, 4.0, (height, width))
        precip_monthly[t] = np.clip(precip_monthly[t], 0.0, None)

    # 逐日降水（覆盖全年 365 天），季风期集中
    daily = np.zeros(365, dtype=np.float32)
    doy_by_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    for m in range(1, 13):
        nd = (doy_by_month[m - 1 + 1] - doy_by_month[m - 1]) if m < 12 else (365 - doy_by_month[11])
        start = doy_by_month[m - 1]
        if m in cfg["monsoon_months"]:
            rate = 9.0 if m == cfg["peak_month"] else 6.0
        else:
            rate = 1.2
        daily[start:start + nd] = rng.gamma(shape=2.0, scale=rate / 2.0, size=nd)

    info = {
        "bbox": bbox, "region": region, "width": width, "height": height,
        "n_dates": n_dates, "months": months.tolist(), "seed": seed,
        "monsoon_months": cfg["monsoon_months"],
        "winter_months": cfg["winter_months"],
    }
    return {"u": u, "v": v, "precip_monthly": precip_monthly,
            "precip_daily": daily, "months": months, "info": info}


# ---------------------------------------------------------------------------
# GeoTIFF I/O
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


def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "region": getattr(args, "region", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
            "n_dates": getattr(args, "n_dates", None),
        },
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
def _months_from_input(n: int) -> np.ndarray:
    return np.array([((i % 12) + 1) for i in range(n)], dtype=np.int32)


# ---------------------------------------------------------------------------
# 输入校验（前置；统一 exit code = 6 ValidationError）
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Any) -> List[float]:
    """W<E、S<N、坐标超范围、零面积、跨 180° 经线 → ValidationError。

    返回标准化的 [W, S, E, N] 列表（4 floats）。
    """
    if not bbox or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats [W S E N]", bbox=bbox)
    W, S, E, N = [float(x) for x in bbox]
    if not (all(np.isfinite([W, S, E, N]))):
        raise ValidationError("bbox must be finite", bbox=[W, S, E, N])
    if not (-180.0 <= W <= 180.0 and -180.0 <= E <= 180.0):
        raise ValidationError("longitude out of [-180, 180]",
                              W=W, E=E)
    if not (-90.0 <= S <= 90.0 and -90.0 <= N <= 90.0):
        raise ValidationError("latitude out of [-90, 90]", S=S, N=N)
    if W >= E:
        raise ValidationError(
            f"bbox W must be < E (W={W}, E={E}); got W>=E", W=W, E=E)
    if S >= N:
        raise ValidationError(
            f"bbox S must be < N (S={S}, N={N}); got S>=N", S=S, N=N)
    if (E - W) * (N - S) <= 0.0:
        raise ValidationError("bbox area is zero or negative", area=(E - W) * (N - S))
    return [W, S, E, N]


def validate_n_dates(n_dates: int) -> int:
    """synthetic 月份数至少 1（实践上 >= 12 才能覆盖冬夏两季）。"""
    if not isinstance(n_dates, int):
        raise ValidationError("n_dates must be an integer", n_dates=n_dates)
    if n_dates < 12:
        raise ValidationError(
            f"n_dates must be >= 12 to cover both summer and winter months "
            f"(got {n_dates})", n_dates=n_dates)
    return n_dates


def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir
    bbox = list(args.bbox) if args.bbox else None

    # 校验前置（synthetic 模式与 input 模式分别按需走）
    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input raster not found: {args.input}", path=args.input)
        if bbox is not None:
            bbox = validate_bbox(bbox)
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        n_dates = validate_n_dates(args.n_dates)

    os.makedirs(output_dir, exist_ok=True)

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if cube.shape[0] < 2:
            raise ValidationError(
                f"input raster must have >=2 bands (u, v); got {cube.shape[0]}",
                bands=int(cube.shape[0]))
        # 解释为交替 u/v 月序列；若无降水则用常数
        n = cube.shape[0] // 2
        u = cube[0:2 * n:2]
        v = cube[1:2 * n:2]
        months = _months_from_input(n)
        precip_monthly = np.full((n, cube.shape[1], cube.shape[2]), 50.0, dtype=np.float32)
        precip_daily = np.ones(365, dtype=np.float32)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        met = generate_synthetic(bbox, region=args.region, n_dates=n_dates)
        u, v = met["u"], met["v"]
        precip_monthly = met["precip_monthly"]
        precip_daily = met["precip_daily"]
        months = met["months"]
        synth_info = met["info"]
        source_note = "synthetic"

    if u.size == 0:
        raise ValidationError("wind field is empty")

    res = analyze_monsoon(u, v, precip_monthly, precip_daily, months, args.region)

    # 输出：季风指数栅格 + 夏/冬 u 风 + 诊断 JSON
    mi_field = res["monsoon_index_field"].astype(np.float32)
    mi_path = os.path.join(output_dir, "monsoon_index.tif")
    write_geotiff(mi_path, mi_field, bbox)

    summer_idx = res["summer_idx"]; winter_idx = res["winter_idx"]
    u_season = np.stack([np.mean(u[summer_idx], axis=0),
                         np.mean(u[winter_idx], axis=0)], axis=0).astype(np.float32)
    u_season_path = os.path.join(output_dir, "u_wind_seasonal.tif")
    write_geotiff(u_season_path, u_season, bbox)

    diag = {
        "region": res["region"],
        "reversal_angle_deg": res["reversal_angle_deg"],
        "monsoon_index_mean": res["monsoon_index_mean"],
        "u_summer_mean": res["u_summer_mean"],
        "u_winter_mean": res["u_winter_mean"],
        "precipitation_concentration": res["concentration"],
        "precipitation_seasonality": res["seasonality"],
        "monsoon_precip_total": res["monsoon_total"],
        "annual_precip_total": res["annual_total"],
        "onset_index": res["onset_index"],
        "peak_index": res["peak_index"],
        "retreat_index": res["retreat_index"],
    }
    diag_path = os.path.join(output_dir, "monsoon_diagnosis.json")
    with open(diag_path, "w", encoding="utf-8") as f:
        json.dump(diag, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "region": args.region,
        "reversal_angle_deg": res["reversal_angle_deg"],
        "precipitation_concentration": res["concentration"],
        "monsoon_index_mean": res["monsoon_index_mean"],
    }
    if synth_info is not None:
        qa["n_dates"] = synth_info["n_dates"]

    outputs = [
        {"path": mi_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": u_season_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 2},
        {"path": diag_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  region: {args.region}")
        print(f"[{SKILL_NAME}] wind reversal: {res['reversal_angle_deg']:.1f} deg")
        print(f"[{SKILL_NAME}] precip concentration: {res['concentration']:.3f}")
        print(f"[{SKILL_NAME}] monsoon index mean: {res['monsoon_index_mean']:.3f}")
        print(f"[{SKILL_NAME}] onset/peak/retreat idx: "
              f"{res['onset_index']}/{res['peak_index']}/{res['retreat_index']}")
        print(f"[{SKILL_NAME}] output: {mi_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Monsoon analysis: wind reversal, monsoon index, precipitation concentration, onset/retreat.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF with alternating u/v bands (monthly)")
    p.add_argument("--region", default="east_asia", choices=sorted(REGIONS.keys()),
                   help="monsoon region (default: east_asia)")
    p.add_argument("--n-dates", type=int, default=24,
                   help="number of synthetic monthly steps (default: 24)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic monsoon series (offline)")
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
