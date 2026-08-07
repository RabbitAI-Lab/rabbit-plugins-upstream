#!/usr/bin/env python3
"""stream-flow-simulation — 径流模拟

基于 SCS-CN 产流法与三角单位线，由土地利用、DEM 与设计降雨模拟流域径流
过程线与洪峰流量。核心内容：

- **SCS-CN 产流**：S = 25400/CN − 254，Ia = 0.2·S，径流深 Q = (P−Ia)² / (P−Ia+S)。
  CN 由土地利用类型查表（USDA-NRCS 标准值）。
- **设计暴雨**：三角形雨型，总雨量 = ``--rainfall``，时长随重现期缩短
  （重现期越大雨峰越集中）。
- **单位线汇流**：Kirpich 公式由 DEM 坡度/流长估算汇流时间，构建三角单位线，
  与净雨过程卷积得径流过程线，保证水量守恒。
- 输出：径流深栅格、径流过程线 JSON、洪峰流量。

数据源：本地土地利用 / DEM GeoTIFF（band1=土地利用码, band2=DEM），或
``--synthetic`` 生成物理一致的 DEM + 下垫面用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，无网络访问。``--synthetic`` 完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python stream-flow-simulation.py --bbox 116 39 117 40 --rainfall 100 --return-period 10
    python stream-flow-simulation.py --bbox 116 39 117 40 --synthetic --rainfall 80

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
SKILL_NAME = "stream-flow-simulation"

# ---- 复用共享核心库（本地 vendored）----
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
# 土地利用 → SCS-CN 查表（USDA-NRCS TR-55，AMC II 中等湿润条件典型值）
# ---------------------------------------------------------------------------
CN_TABLE: Dict[int, Dict[str, Any]] = {
    0: {"name": "water", "cn": 100},
    1: {"name": "urban_high", "cn": 89},
    2: {"name": "urban_low", "cn": 70},
    3: {"name": "cropland", "cn": 75},
    4: {"name": "grassland", "cn": 69},
    5: {"name": "forest", "cn": 55},
    6: {"name": "bare", "cn": 77},
    7: {"name": "wetland", "cn": 78},
}
DEFAULT_CN = 75


def cn_from_landuse(landuse: np.ndarray) -> np.ndarray:
    """把土地利用整型码栅格映射为 CN 栅格。未知码用默认 CN。"""
    lu = np.asarray(landuse)
    cn = np.full(lu.shape, float(DEFAULT_CN), dtype=np.float64)
    for code, meta in CN_TABLE.items():
        cn[lu == code] = float(meta["cn"])
    return cn


# ---------------------------------------------------------------------------
# 核心算法 1：SCS-CN 产流
# ---------------------------------------------------------------------------
def scs_runoff_depth(
    precip_mm: float, cn: np.ndarray, ia_ratio: float = 0.2,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """SCS-CN 产流深。

    S = 25400/CN − 254；Ia = ia_ratio·S；当 P > Ia 时
    Q = (P − Ia)² / (P − Ia + S)，否则 Q = 0。
    返回 (Q, S, Ia)，均为与 cn 同形的数组（precip 为标量时广播）。
    """
    cn = np.asarray(cn, dtype=np.float64)
    cn = np.clip(cn, 1.0, 100.0)
    S = 25400.0 / cn - 254.0
    Ia = ia_ratio * S
    P = float(precip_mm)
    excess = P - Ia
    Q = np.where(excess > 0, excess ** 2 / (excess + S), 0.0)
    # CN=100（水面）时 S→0，直接 Q≈P
    Q = np.where(cn >= 99.999, P, Q)
    return Q.astype(np.float64), S.astype(np.float64), Ia.astype(np.float64)


# ---------------------------------------------------------------------------
# 核心算法 2：设计暴雨雨型与三角单位线
# ---------------------------------------------------------------------------
def triangular_fractions(n_steps: int, peak_index: Optional[int] = None) -> np.ndarray:
    """生成归一化的三角形时间分配（总和为 1）。

    peak_index 默认在 0.4·n 处（雨峰偏前）。
    """
    n = max(2, int(n_steps))
    if peak_index is None:
        peak_index = int(round(0.4 * (n - 1)))
    peak_index = int(np.clip(peak_index, 0, n - 1))
    x = np.arange(n, dtype=np.float64)
    if peak_index == 0:
        rising = np.ones(1)
    else:
        rising = x[:peak_index + 1] / peak_index
    if peak_index == n - 1:
        falling = np.ones(0)
    else:
        falling = (n - 1 - x[peak_index + 1:]) / (n - 1 - peak_index)
    tri = np.concatenate([rising, falling])
    tri = np.clip(tri, 0.0, None)
    s = tri.sum()
    if s <= 0:
        return np.full(n, 1.0 / n)
    return tri / s


def kirpich_tc_hours(length_m: float, slope: float) -> float:
    """Kirpich 汇流时间（小时）。L 单位 m，slope = 高差/流长 (m/m)。"""
    L = max(float(length_m), 10.0)
    S = max(float(slope), 1e-4)
    tc_min = 0.0195 * (L ** 0.77) * (S ** -0.385)
    tc_h = tc_min / 60.0
    return float(np.clip(tc_h, 0.5, 72.0))


def unit_hydrograph_response(
    area_km2: float, tp_h: float, tb_h: float, dt_h: float,
) -> Tuple[np.ndarray, np.ndarray]:
    """三角单位线对 1 mm 净雨的出流响应 (m³/s)。

    三角形：0 → 峰值(tp) → 0(tb)，体积 = 1 mm × area = area×1000 m³。
    返回 (time_hours, response_m3s_per_mm)，满足 Σ response·dt = volume。
    """
    dt_h = max(float(dt_h), 1e-3)
    tp_h = max(float(tp_h), dt_h)
    tb_h = max(float(tb_h), tp_h + dt_h)
    t = np.arange(0.0, tb_h + dt_h * 0.5, dt_h)
    # 三角形状
    shape = np.where(t <= tp_h, t / tp_h, np.maximum(0.0, (tb_h - t) / (tb_h - tp_h)))
    shape = np.clip(shape, 0.0, None)
    dt_s = dt_h * 3600.0
    volume = area_km2 * 1000.0  # 1 mm over basin (m³)
    shape_sum = shape.sum()
    if shape_sum <= 0:
        raise ProcessError("degenerate unit hydrograph shape")
    # response[k]·dt_s 之和 = volume → response = volume/dt_s · shape/Σshape
    response = (volume / dt_s) * (shape / shape_sum)
    return t, response


# ---------------------------------------------------------------------------
# 核心算法 3：净雨—单位线卷积 → 径流过程线
# ---------------------------------------------------------------------------
def convolve_hydrograph(
    q_depth_mm: float,
    area_km2: float,
    storm_frac: np.ndarray,
    uh_time: np.ndarray,
    uh_response: np.ndarray,
    dt_h: float,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, float]]:
    """把净雨过程（按 storm_frac 分配 q_depth_mm）与单位线卷积。

    返回 (time_hours, discharge_m3s, stats)。水量守恒：
    Σ Q·dt = q_depth_mm × area_km2 × 1000。
    """
    storm_frac = np.asarray(storm_frac, dtype=np.float64)
    if storm_frac.size == 0 or abs(storm_frac.sum()) < 1e-12:
        raise ValidationError("invalid storm fractions")
    storm_frac = storm_frac / storm_frac.sum()
    i_eff = float(q_depth_mm) * storm_frac  # mm per storm step

    q = np.convolve(i_eff, uh_response)  # m³/s
    n = q.size
    time = np.arange(n, dtype=np.float64) * dt_h

    dt_s = dt_h * 3600.0
    total_volume = float(q_depth_mm) * area_km2 * 1000.0
    routed_volume = float(np.sum(q) * dt_s)
    peak = float(np.max(q))
    peak_time = float(time[int(np.argmax(q))])
    stats = {
        "peak_discharge_m3s": peak,
        "time_to_peak_h": peak_time,
        "total_runoff_volume_m3": total_volume,
        "routed_volume_m3": routed_volume,
        "volume_balance_ratio": routed_volume / total_volume if total_volume > 0 else 0.0,
    }
    return time, q, stats


# ---------------------------------------------------------------------------
# 合成数据：DEM + 土地利用 + 流域几何
# ---------------------------------------------------------------------------
def bbox_area_km2(bbox: List[float]) -> float:
    w, s, e, n = bbox
    lat0 = 0.5 * (s + n)
    width_km = (e - w) * 111.32 * np.cos(np.deg2rad(lat0))
    height_km = (n - s) * 110.57
    return float(max(width_km * height_km, 1e-6))


def generate_synthetic(
    bbox: List[float], grid_shape: Tuple[int, int] = (64, 64), seed: int = 42,
) -> Dict[str, Any]:
    """生成一个向出口（左下角）倾斜的 DEM 与分块土地利用栅格。"""
    rng = np.random.default_rng(seed)
    H, W = int(grid_shape[0]), int(grid_shape[1])
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float64)
    xxn = xx / max(W - 1, 1)
    yyn = yy / max(H - 1, 1)
    # 地形：从右上（高）向左下（低）倾斜 + 起伏噪声
    relief = 120.0
    dem = relief * (0.6 * xxn + 0.4 * yyn) + rng.normal(0, 3.0, (H, W))
    dem = dem - dem.min() + 50.0  # 基准海拔 50 m 起

    # 土地利用分区：水体（河谷）、城镇、耕地、草地、林地
    landuse = np.full((H, W), 3, dtype=np.int32)  # 默认耕地
    landuse[(xxn + yyn) < 0.35] = 5              # 左上林地
    landuse[(xxn > 0.6) & (yyn > 0.6)] = 1       # 右上城镇
    landuse[(xxn + yyn) > 1.5] = 4               # 右下草地
    landuse[(xxn < 0.2) & (yyn < 0.2)] = 0       # 左下水体/出口
    landuse[(xxn > 0.3) & (xxn < 0.5) & (yyn > 0.3) & (yyn < 0.5)] = 6  # 裸地斑块

    area_km2 = bbox_area_km2(bbox)
    # 流长（对角线，m）与平均坡度
    length_m = np.sqrt(((bbox[2] - bbox[0]) * 111320 * np.cos(np.deg2rad(0.5 * (bbox[1] + bbox[3])))) ** 2
                       + ((bbox[3] - bbox[1]) * 110570) ** 2)
    slope = max(float(dem.max() - dem.min()), 1.0) / max(length_m, 1.0)
    return {
        "bbox": list(bbox),
        "grid_shape": (H, W),
        "dem": dem.astype(np.float32),
        "landuse": landuse,
        "area_km2": area_km2,
        "length_m": float(length_m),
        "slope": float(slope),
    }


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str, cube: np.ndarray, bbox: List[float], nodata: float = -9999.0,
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


def read_geotiff_full(path: str) -> Tuple[np.ndarray, List[float], int, Optional[float]]:
    """Read GeoTIFF + replace NoData sentinel with NaN; return (cube, bbox, n_valid, input_nodata).

    If *all* pixels are NoData in every band, raises ``ValidationError`` (rc=6).
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=False).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        input_nodata = src.nodata
    if input_nodata is not None:
        cube = np.where(cube == float(input_nodata), np.nan, cube).astype(np.float32)
    valid_mask = np.isfinite(cube)
    n_valid = int(valid_mask.sum())
    if n_valid == 0:
        nodata_str = f"={input_nodata}" if input_nodata is not None else "(none)"
        raise ValidationError(
            f"input raster has no valid pixels (all are NoData{nodata_str})",
            path=path, input_nodata=input_nodata,
        )
    return cube, bbox, n_valid, input_nodata


def validate_bbox(bbox):
    """Validate EPSG:4326 bbox: W<E, S<N, lon/lat ranges, no crossing antimeridian,
    span > 1e-4°. Raises ``ValidationError`` (rc=6)."""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be [W, S, E, N] with 4 floats")
    W, S, E, N = [float(v) for v in bbox]
    if W < -180.0 or E > 180.0 or S < -90.0 or N > 90.0:
        raise ValidationError(
            f"bbox out of WGS-84 range: W={W} S={S} E={E} N={N} "
            "(must satisfy -180<=lon<=180, -90<=lat<=90)",
            bbox=bbox,
        )
    if W >= E:
        if W > 0 and E < 0 and (W - E) < 360.0:
            raise ValidationError(
                f"bbox crosses 180° antimeridian (W={W}, E={E}); "
                "split into two non-antipodal sub-bboxes",
                bbox=bbox,
            )
        raise ValidationError(
            f"bbox has W>=E (W={W}, E={E}); expected W<E in WGS-84 order",
            bbox=bbox,
        )
    if S >= N:
        raise ValidationError(
            f"bbox has S>=N (S={S}, N={N}); expected S<N in WGS-84 order",
            bbox=bbox,
        )
    if (E - W) < 1e-4 or (N - S) < 1e-4:
        raise ValidationError(
            f"bbox is too small (lon-span={E - W:.6f}, lat-span={N - S:.6f}); "
            "need at least 1e-4° on each axis",
            bbox=bbox,
        )
    return [W, S, E, N]


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(
    output_dir, args, outputs, qa, started_at, exit_code, bbox,
) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "rainfall_mm": getattr(args, "rainfall", None),
            "return_period": getattr(args, "return_period", None),
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
    rainfall = float(args.rainfall)
    if rainfall <= 0:
        raise UsageError("--rainfall must be > 0 mm", rainfall=rainfall)
    rp = float(args.return_period)
    if rp < 1:
        raise UsageError("--return-period must be >= 1 year", return_period=rp)

    # 1) bbox validation FIRST (before makedirs)
    if args.input and not args.synthetic:
        if bbox is not None:
            bbox = validate_bbox(bbox)
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)

    n_valid_pixels = None
    input_nodata = None
    # 2) 下垫面（土地利用 + DEM）
    if args.input and not args.synthetic:
        cube, file_bbox, n_valid_pixels, input_nodata = read_geotiff_full(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            bbox = validate_bbox(bbox)
        landuse = cube[0].astype(np.int32)
        if cube.shape[0] >= 2:
            dem = cube[1]
        else:
            dem = np.zeros_like(cube[0])
        source_note = args.input
    else:
        synth = generate_synthetic(bbox)
        landuse = synth["landuse"]
        dem = synth["dem"]
        source_note = "synthetic"

    if landuse.size == 0:
        raise ValidationError("empty landuse raster")

    H, W = landuse.shape
    area_km2 = bbox_area_km2(bbox)

    # 3) SCS-CN 产流深（空间分布）
    cn = cn_from_landuse(landuse)
    Q_depth, S, Ia = scs_runoff_depth(rainfall, cn)
    q_mean = float(np.mean(Q_depth))

    # 4) 汇流参数：Kirpich 汇流时间 → 三角单位线
    length_m = float(np.sqrt(area_km2) * 1000.0)  # 等效流域长度
    if args.input and not args.synthetic and dem.max() > dem.min():
        slope = float(dem.max() - dem.min()) / max(length_m, 1.0)
    else:
        slope = float(dem.max() - dem.min()) / max(length_m, 1.0) if dem.size else 0.01
    slope = max(slope, 1e-4)
    tc_h = kirpich_tc_hours(length_m, slope)
    tp_h = 0.67 * tc_h
    tb_h = 2.67 * tp_h

    # 重现期越大 → 暴雨历时越短、雨峰越集中
    duration_h = max(1.0, 24.0 / np.sqrt(rp))
    dt_h = max(0.25, min(duration_h, tb_h) / 24.0)
    n_storm = max(2, int(np.ceil(duration_h / dt_h)))

    storm_frac = triangular_fractions(n_storm)
    uh_time, uh_response = unit_hydrograph_response(area_km2, tp_h, tb_h, dt_h)

    # 5) 卷积得径流过程线
    time_h, discharge, stats = convolve_hydrograph(
        q_mean, area_km2, storm_frac, uh_time, uh_response, dt_h,
    )

    # 6) ALL checks passed → safe to makedirs
    os.makedirs(output_dir, exist_ok=True)

    # 7) 输出
    out_tif = os.path.join(output_dir, "runoff_depth.tif")
    write_geotiff(out_tif, Q_depth.astype(np.float32), bbox)

    hydro = {
        "rainfall_mm": rainfall,
        "return_period_yr": rp,
        "area_km2": area_km2,
        "mean_cn": float(np.mean(cn)),
        "mean_runoff_depth_mm": q_mean,
        "runoff_coefficient": q_mean / rainfall if rainfall > 0 else 0.0,
        "tc_hours": tc_h,
        "tp_hours": tp_h,
        "storm_duration_hours": float(duration_h),
        "dt_hours": dt_h,
        "time_hours": [float(x) for x in time_h],
        "discharge_m3s": [float(x) for x in discharge],
        "stats": stats,
    }
    hydro_path = os.path.join(output_dir, "hydrograph.json")
    with open(hydro_path, "w", encoding="utf-8") as f:
        json.dump(hydro, f, ensure_ascii=False, indent=2)

    qa = {
        "source": source_note,
        "area_km2": area_km2,
        "mean_cn": hydro["mean_cn"],
        "mean_runoff_depth_mm": q_mean,
        "runoff_coefficient": hydro["runoff_coefficient"],
        "peak_discharge_m3s": stats["peak_discharge_m3s"],
        "time_to_peak_h": stats["time_to_peak_h"],
        "volume_balance_ratio": stats["volume_balance_ratio"],
        "n_valid_pixels": n_valid_pixels,
        "input_nodata": input_nodata,
    }
    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": hydro_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  rainfall: {rainfall} mm  RP: {rp} yr")
        print(f"[{SKILL_NAME}] area: {area_km2:.2f} km²  mean CN: {hydro['mean_cn']:.1f}")
        print(f"[{SKILL_NAME}] runoff depth: {q_mean:.2f} mm  coeff: {hydro['runoff_coefficient']:.3f}")
        print(f"[{SKILL_NAME}] peak: {stats['peak_discharge_m3s']:.2f} m³/s @ {stats['time_to_peak_h']:.2f} h")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="SCS-CN runoff + triangular unit hydrograph stream-flow simulation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF (band1=landuse code, band2=DEM optional)")
    p.add_argument("--rainfall", type=float, default=100.0,
                   help="design storm total depth in mm (default: 100)")
    p.add_argument("--return-period", type=float, default=10.0,
                   help="storm return period in years (default: 10)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate synthetic DEM + landuse (offline)")
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
