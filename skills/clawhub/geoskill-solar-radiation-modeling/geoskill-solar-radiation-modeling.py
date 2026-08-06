#!/usr/bin/env python3
"""solar-radiation-modeling — 太阳辐射建模

基于 DEM 地形与天文几何，模拟地表接收的太阳辐射量。流程：
1. 计算太阳位置（赤纬 / 时角 / 高度角 / 方位角）
2. 计算天文辐射（大气顶辐照度）
3. 地形坡向坡度 → 地表入射角 → 地形遮蔽
4. 简化晴空大气透过率模型
5. 逐时刻积分得到时段总辐射量（MJ/m²）

数据源：本地 DEM GeoTIFF，或 --synthetic 生成模拟地形。

隐私声明 / Privacy：
- 默认离线运行，不发起任何网络请求。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python solar-radiation-modeling.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "solar-radiation-modeling"

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


def validate_bbox(bbox: List[float]) -> None:
    """校验 bbox：W<E、S<N、经纬度在合法范围、非零面积；跨 180° 明确提示。"""
    if bbox is None:
        raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
    if len(bbox) != 4:
        raise ValidationError(f"bbox must have exactly 4 numbers, got {len(bbox)}")
    w, s, e, n = [float(x) for x in bbox]
    if w > e:
        raise ValidationError(
            f"bbox minLon ({w}) > maxLon ({e}): crossing the 180° antimeridian is not "
            "supported, please split the region into two bboxes")
    if s > n:
        raise ValidationError(f"bbox minLat ({s}) > maxLat ({n}): S must be <= N")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"bbox longitudes out of range [-180, 180]: {w}, {e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"bbox latitudes out of range [-90, 90]: {s}, {n}")
    if w == e or s == n:
        raise ValidationError("bbox has zero area")


def validate_params(day_of_year: int, time_step: float, turbidity: float, grid_size: int) -> None:
    if day_of_year < 1 or day_of_year > 366:
        raise ValidationError(f"--day-of-year must be in [1, 366], got {day_of_year}")
    if time_step <= 0 or time_step > 24:
        raise ValidationError(f"--time-step must be in (0, 24] hours, got {time_step}")
    if turbidity <= 0:
        raise ValidationError(f"--turbidity must be > 0, got {turbidity}")
    if grid_size < 3:
        raise ValidationError(f"--grid-size must be >= 3, got {grid_size}")


SOLAR_CONSTANT = 1367.0  # W/m²


# ---------------------------------------------------------------------------
# 核心算法：太阳几何
# ---------------------------------------------------------------------------
def solar_declination(day_of_year: int) -> float:
    """太阳赤纬（弧度），Cooper 公式。"""
    return np.deg2rad(23.45 * np.sin(np.deg2rad(360.0 * (284 + day_of_year) / 365.0)))


def hour_angle(solar_hour: float) -> float:
    """时角（弧度），太阳时 12:00 为 0，每小时 15°。"""
    return np.deg2rad(15.0 * (solar_hour - 12.0))


def solar_elevation(lat_rad: float, decl: float, ha: float) -> float:
    """太阳高度角（弧度）。sin(h) = sinφ sinδ + cosφ cosδ cosω。"""
    sin_h = (np.sin(lat_rad) * np.sin(decl)
             + np.cos(lat_rad) * np.cos(decl) * np.cos(ha))
    return float(np.arcsin(np.clip(sin_h, -1.0, 1.0)))


def solar_azimuth(lat_rad: float, decl: float, ha: float, elev: float) -> float:
    """太阳方位角（弧度，正北为 0，顺时针）。"""
    cos_elev = np.cos(elev)
    if cos_elev < 1e-9:
        return 0.0
    cos_az = (np.sin(decl) - np.sin(lat_rad) * np.sin(elev)) / (np.cos(lat_rad) * cos_elev)
    az = np.arccos(np.clip(cos_az, -1.0, 1.0))
    if ha > 0:  # 下午，方位角 > 180°
        az = 2 * np.pi - az
    return float(az)


def extraterrestrial_radiation(day_of_year: int, elev: float) -> float:
    """大气顶垂直于光束的辐照度（W/m²），含日地距离修正。"""
    if elev <= 0:
        return 0.0
    E0 = 1.0 + 0.033 * np.cos(np.deg2rad(360.0 * day_of_year / 365.0))
    return SOLAR_CONSTANT * E0


def slope_aspect(dem: np.ndarray, cell_size: float) -> Tuple[np.ndarray, np.ndarray]:
    """从 DEM 计算坡度（弧度）和坡向（弧度，正北顺时针）。用 Horn 法。"""
    from scipy.ndimage import convolve
    z = dem.astype(np.float64)
    kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float64) / (8.0 * cell_size)
    ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype=np.float64) / (8.0 * cell_size)
    dzdx = convolve(z, kx, mode="nearest")
    dzdy = convolve(z, ky, mode="nearest")
    slope = np.arctan(np.sqrt(dzdx ** 2 + dzdy ** 2))
    aspect = np.arctan2(-dzdy, dzdx)
    # 转为正北顺时针：aspect_from_north
    asp = (np.pi / 2.0 - aspect)
    asp = np.where(asp < 0, asp + 2 * np.pi, asp)
    return slope.astype(np.float32), asp.astype(np.float32)


def incidence_angle_cos(slope: np.ndarray, aspect: np.ndarray,
                        elev: float, azim: float) -> np.ndarray:
    """地表入射角余弦 cos(θ)。

    cosθ = sin(h)cos(s) + cos(h)sin(s)cos(A - a)
    h=太阳高度角, s=坡度, A=太阳方位角, a=坡向。
    """
    cos_theta = (np.sin(elev) * np.cos(slope)
                 + np.cos(elev) * np.sin(slope) * np.cos(azim - aspect))
    return np.clip(cos_theta, 0.0, 1.0)


def atmospheric_transmittance(elev: float, turbidity: float = 3.0) -> float:
    """简化晴空大气透过率（随太阳高度角变化）。

    tau = exp(-turbidity * airmass)，airmass ≈ 1/sin(h)。
    """
    if elev <= 0:
        return 0.0
    sin_h = max(np.sin(elev), 0.05)
    airmass = 1.0 / sin_h
    return float(np.exp(-0.09 * turbidity * airmass / 10.0))


def model_daily_radiation(
    dem: np.ndarray, lat_deg: float, day_of_year: int, cell_size_m: float,
    time_step_h: float = 0.5, turbidity: float = 3.0,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """模拟单日总辐射量（MJ/m²）。

    Returns (radiation_grid, info)。
    """
    slope, aspect = slope_aspect(dem, cell_size_m)
    lat_rad = np.deg2rad(lat_deg)
    decl = solar_declination(day_of_year)
    hours = np.arange(0.0, 24.0, time_step_h)
    accum = np.zeros(dem.shape, dtype=np.float64)
    sun_up_steps = 0
    for hr in hours:
        ha = hour_angle(hr)
        elev = solar_elevation(lat_rad, decl, ha)
        if elev <= 0:
            continue
        sun_up_steps += 1
        azim = solar_azimuth(lat_rad, decl, ha, elev)
        I0 = extraterrestrial_radiation(day_of_year, elev)
        tau = atmospheric_transmittance(elev, turbidity)
        cos_theta = incidence_angle_cos(slope, aspect, elev, azim)
        # 瞬时地表辐照度 W/m²
        flux = I0 * tau * cos_theta
        accum += flux * (time_step_h * 3600.0)  # J/m²
    radiation_mj = accum / 1e6  # → MJ/m²
    info = {
        "day_of_year": int(day_of_year),
        "latitude": float(lat_deg),
        "sun_up_steps": int(sun_up_steps),
        "mean_radiation_mj": float(radiation_mj.mean()),
        "max_radiation_mj": float(radiation_mj.max()),
    }
    return radiation_mj.astype(np.float32), info


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], grid_size: int = 48, seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成合成 DEM：南向坡 + 北向坡对比。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:grid_size, 0:grid_size]
    # 一半南向坡（北高南低），一半北向坡
    yyf = yy / grid_size
    base = 500.0 - 300.0 * yyf  # 总体北高南低（南坡）
    bump = 150.0 * np.exp(-((xx / grid_size - 0.5) ** 2 + (yyf - 0.3) ** 2) / 0.03)
    dem = (base + bump + rng.normal(0, 3, (grid_size, grid_size))).astype(np.float32)
    info = {"grid_size": grid_size, "elev_range": [float(dem.min()), float(dem.max())]}
    return dem, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if array.ndim == 2:
        array = array[np.newaxis, ...]
    if array.ndim != 3:
        raise ValidationError("write_geotiff expects a 2D or 3D array")
    nb, hh, ww = array.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], ww, hh)
    profile = {
        "driver": "GTiff", "height": hh, "width": ww, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(array[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        data = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None:
        data = np.where(data == nodata, np.nan, data)
    data = np.where(np.isfinite(data), data, np.nan)
    return data, bbox


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
        inputs={"input": getattr(args, "input", None), "synthetic": bool(getattr(args, "synthetic", False))},
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

    validate_params(args.day_of_year, args.time_step, args.turbidity, args.grid_size)

    bbox = list(args.bbox) if args.bbox else None
    input_nodata = None

    if args.input and not args.synthetic:
        data, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        dem = data[0] if data.ndim == 3 else data
        valid = np.isfinite(dem)
        n_valid = int(valid.sum())
        input_nodata = True
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        dem, _ = generate_synthetic(bbox, grid_size=args.grid_size)
        valid = np.ones(dem.shape, dtype=bool)
        n_valid = int(dem.size)
        source_note = "synthetic"

    validate_bbox(bbox)
    if n_valid == 0:
        raise ValidationError(
            f"input DEM contains no valid (non-NoData) pixels: all {dem.size} pixels are NoData")

    if dem.size < 9:
        raise ValidationError("DEM too small")
    gs = args.grid_size
    if dem.shape[0] != gs or dem.shape[1] != gs:
        from scipy.ndimage import zoom
        dem = zoom(dem, (gs / dem.shape[0], gs / dem.shape[1]), order=1).astype(np.float32)
        valid = zoom(valid.astype(np.float32), (gs / valid.shape[0], gs / valid.shape[1]),
                     order=0).astype(bool)
        n_valid = int(valid.sum())

    h, w = dem.shape
    dem_f = np.where(valid, dem, 0.0).astype(np.float32)
    lat0 = (bbox[1] + bbox[3]) / 2.0
    dx_m = (bbox[2] - bbox[0]) * 111320.0 * np.cos(np.deg2rad(lat0)) / w
    dy_m = (bbox[3] - bbox[1]) * 110540.0 / h
    cell_size_m = float(np.sqrt(dx_m * dy_m))

    rad, info = model_daily_radiation(
        dem_f, lat0, args.day_of_year, cell_size_m,
        time_step_h=args.time_step, turbidity=args.turbidity,
    )

    rad_masked = np.where(valid, rad, np.nan)
    info["mean_radiation_mj"] = float(np.nanmean(rad_masked))
    info["max_radiation_mj"] = float(np.nanmax(rad_masked))
    info["min_radiation_mj"] = float(np.nanmin(rad_masked))

    os.makedirs(output_dir, exist_ok=True)
    out_tif = os.path.join(output_dir, "solar_radiation.tif")
    rad_out = np.where(valid, rad, -9999.0).astype(np.float32)
    write_geotiff(out_tif, rad_out, bbox)
    stats_path = os.path.join(output_dir, "radiation_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "day_of_year": args.day_of_year,
          "latitude": float(lat0), "n_valid_pixels": n_valid, "n_total_pixels": int(dem.size),
          "input_nodata": input_nodata, **info}
    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  doy: {args.day_of_year}")
        print(f"[{SKILL_NAME}] mean radiation: {info['mean_radiation_mj']:.2f} MJ/m²")
        print(f"[{SKILL_NAME}] max radiation:  {info['max_radiation_mj']:.2f} MJ/m²")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Solar radiation modeling from DEM: astronomy + terrain shading + atmospheric transmittance.",
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input DEM GeoTIFF")
    p.add_argument("--grid-size", type=int, default=48, help="working grid size (default: 48)")
    p.add_argument("--day-of-year", type=int, default=172, help="day of year (default: 172 ~ Jun 21)")
    p.add_argument("--time-step", type=float, default=0.5, help="time step in hours (default: 0.5)")
    p.add_argument("--turbidity", type=float, default=3.0, help="Linke turbidity (default: 3)")
    p.add_argument("--synthetic", action="store_true", help="use synthetic data")
    p.add_argument("--output-dir", default="./output", help="output directory")
    p.add_argument("--quiet", action="store_true", help="suppress output")
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
