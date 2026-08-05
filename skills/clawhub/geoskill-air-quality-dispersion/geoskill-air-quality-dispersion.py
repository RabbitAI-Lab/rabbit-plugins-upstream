#!/usr/bin/env python3
"""air-quality-dispersion — 空气质量扩散模拟

基于高斯烟羽模型（Gaussian Plume）模拟点源大气污染物浓度场。

标准高斯烟羽公式（含地面反射项）：
  C(x,y,z) = Q/(2π·u·σy·σz) · exp(-y²/(2σy²)) · [exp(-(z-H)²/(2σz²)) + exp(-(z+H)²/(2σz²))]

σy, σz 由 Pasquill-Gifford 稳定度参数化（A-F 六类，Briggs 公式）。
地形修正：地形高于源时，有效源高相对降低，地面浓度增大（乘性因子）。

数据源：--synthetic 生成平坦地形；--input 读取 DEM 做地形修正。

隐私声明 / Privacy：
- 完全离线运行，不访问网络。
- 所有处理在本地完成。

Usage:
    python air-quality-dispersion.py --bbox 116 39 117 40 --synthetic --output-dir ./out
    python air-quality-dispersion.py --bbox 116 39 117 40 --input dem.tif --output-dir ./out

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
SKILL_NAME = "air-quality-dispersion"

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
# bbox / parameter validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox, *, allow_antimeridian: bool = False) -> List[float]:
    """校验 bbox: [W, S, E, N]。

    - 必须为 4 个 float
    - 经度 ∈ [-180, 180]、纬度 ∈ [-90, 90]
    - 必须 W < E 且 S < N（跨 180 经线按设计不支持）
    """
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise UsageError("bbox must be 4 floats [W S E N]", bbox=list(bbox) if bbox else None)
    try:
        w, s, e, n = (float(v) for v in bbox)
    except (TypeError, ValueError) as exc:
        raise UsageError("bbox entries must be numeric", bbox=list(bbox)) from exc
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError("bbox longitude out of range [-180, 180]",
                              w=w, e=e)
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError("bbox latitude out of range [-90, 90]", s=s, n=n)
    if not (w < e):
        if allow_antimeridian and w > 0 and e < 0:
            # 显式支持时跨越 180° 经线；本 skill 默认不开启
            pass
        else:
            raise ValidationError(
                "bbox requires W < E (got W={:.6f} E={:.6f}); "
                "antimeridian crossing is not supported".format(w, e),
                w=w, e=e)
    if not (s < n):
        raise ValidationError(
            "bbox requires S < N (got S={:.6f} N={:.6f})".format(s, n),
            s=s, n=n)
    return [w, s, e, n]


def validate_phys_params(source_strength: float, wind_speed: float,
                         effective_height: float) -> None:
    """校验高斯烟羽物理参数（防止除零 / 数值爆炸）。"""
    if wind_speed is None or float(wind_speed) <= 0.0:
        raise ValidationError(
            "wind-speed must be > 0 (got {:.6f})".format(float(wind_speed or 0.0)),
            wind_speed=float(wind_speed or 0.0))
    if source_strength is None or float(source_strength) <= 0.0:
        raise ValidationError(
            "source-strength must be > 0 (got {:.6f})".format(float(source_strength or 0.0)),
            source_strength=float(source_strength or 0.0))
    if effective_height is None or float(effective_height) < 0.0:
        raise ValidationError(
            "effective-height must be >= 0 (got {:.6f})".format(float(effective_height or 0.0)),
            effective_height=float(effective_height or 0.0))


# ---------------------------------------------------------------------------
# Pasquill-Gifford σy/σz 参数（Briggs 公式）
# σy = ay·x^by / (1+cy·x)^dy  [km→m]
# σz = az·x^bz / (1+cz·x)^dz  [km→m]
# ---------------------------------------------------------------------------
PG_PARAMS: Dict[str, Tuple[float, ...]] = {
    "A": (0.22, 0.911, 0.0001, 0.5, 0.20, 0.911, 0.0001, 0.5),
    "B": (0.16, 0.911, 0.0001, 0.5, 0.12, 0.911, 0.0001, 0.5),
    "C": (0.11, 0.911, 0.0001, 0.5, 0.08, 0.811, 0.0002, 0.5),
    "D": (0.08, 0.911, 0.0001, 0.5, 0.06, 0.711, 0.0015, 0.5),
    "E": (0.06, 0.911, 0.0001, 0.5, 0.03, 0.611, 0.0003, 0.5),
    "F": (0.04, 0.911, 0.0001, 0.5, 0.016, 0.511, 0.0003, 0.5),
}
STABILITY_CLASSES = sorted(PG_PARAMS.keys())


def dispersion_params(x_km: np.ndarray, stability: str) -> Tuple[np.ndarray, np.ndarray]:
    """下风向距离 x(km) 处的 σy, σz (m)。"""
    if stability not in PG_PARAMS:
        raise UsageError(f"unknown stability class '{stability}'. Choose from {STABILITY_CLASSES}")
    ay, by, cy, dy, az, bz, cz, dz = PG_PARAMS[stability]
    x_safe = np.maximum(x_km, 0.01)
    sy = ay * x_safe ** by / (1.0 + cy * x_safe) ** dy * 1000.0
    sz = az * x_safe ** bz / (1.0 + cz * x_safe) ** dz * 1000.0
    return sy.astype(np.float32), sz.astype(np.float32)


def gaussian_plume(
    Q: float, u: float,
    x: np.ndarray, y: np.ndarray,
    H: float, sy: np.ndarray, sz: np.ndarray,
    z: float = 0.0,
) -> np.ndarray:
    """高斯烟羽地面浓度（μg/m³），含地面反射项。Q: g/s, u: m/s, 距离: m。"""
    sy_safe = np.maximum(sy, 0.1)
    sz_safe = np.maximum(sz, 0.1)
    coeff = Q * 1e6 / (2.0 * np.pi * u * sy_safe * sz_safe)
    lat_term = np.exp(-y ** 2 / (2.0 * sy_safe ** 2))
    vert_term = (
        np.exp(-(z - H) ** 2 / (2.0 * sz_safe ** 2))
        + np.exp(-(z + H) ** 2 / (2.0 * sz_safe ** 2))
    )
    conc = coeff * lat_term * vert_term
    conc[x < 1.0] = 0.0
    return conc.astype(np.float32)


def terrain_correction(dem: np.ndarray, source_elev: float, base_H: float) -> np.ndarray:
    """地形修正因子：高于源 → 有效源高相对降低 → 浓度增大。clip [0.5, 3.0]。"""
    dz = np.clip(dem - source_elev, -200.0, 200.0)
    factor = 1.0 + dz / (base_H + 100.0)
    return np.clip(factor, 0.5, 3.0).astype(np.float32)


def generate_synthetic_aq(bbox: List[float], width: int = 128, height: int = 128,
                          seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    dem = (100.0 + rng.normal(0, 2.0, (height, width))).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height}
    return dem, info


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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], np.ndarray]:
    """读取 GeoTIFF 并返回 (cube, bbox, valid_mask)。

    valid_mask 为 (H, W) 布尔数组，像元为有效值（不在 nodata 范围内）时为 True。
    全 NoData 时抛 ValidationError（exit 6）。
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nd = src.nodata
    # 构造 valid_mask（仅对第一波段做诊断）
    band0 = cube[0]
    if nd is None:
        valid = np.isfinite(band0)
    else:
        valid = np.isfinite(band0) & (band0 != float(nd))
    if not bool(valid.any()):
        raise ValidationError(
            f"input raster has no valid (non-NoData) pixels: {path}",
            path=path, nodata=nd)
    return cube, bbox, valid


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
            "stability": getattr(args, "stability", None),
            "source_strength": getattr(args, "source_strength", None),
            "wind_speed": getattr(args, "wind_speed", None),
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

    # 1) bbox 校验（先于任何 IO）
    bbox = list(args.bbox) if args.bbox else None
    if bbox is not None:
        bbox = validate_bbox(bbox)

    # 2) 物理参数校验（防止除零 / 物理上无意义）
    validate_phys_params(args.source_strength, args.wind_speed, args.effective_height)

    os.makedirs(output_dir, exist_ok=True)

    valid_mask: Optional[np.ndarray] = None
    if args.input and not args.synthetic:
        cube, file_bbox, valid_mask = read_geotiff(args.input)
        bbox = bbox if bbox is not None else validate_bbox(file_bbox)
        dem = cube[0]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        dem, _ = generate_synthetic_aq(bbox)
        source_note = "synthetic"

    if dem.size == 0:
        raise ValidationError("input raster is empty")

    # NoData 像元处理：无效像元置 0
    if valid_mask is not None:
        dem = np.where(valid_mask, dem, 0.0).astype(np.float32)

    h, w = dem.shape
    lat_mid = (bbox[1] + bbox[3]) / 2.0
    dx_m = (bbox[2] - bbox[0]) / w * 111320 * np.cos(np.deg2rad(lat_mid))
    dy_m = (bbox[3] - bbox[1]) / h * 111320

    cx, cy = w // 2, h // 2
    source_elev = float(dem[cy, cx])

    XX, YY = np.meshgrid(np.arange(w), np.arange(h))
    x_m = (XX - cx).astype(np.float32) * dx_m
    y_m = (YY - cy).astype(np.float32) * dy_m
    x_km = np.maximum(x_m / 1000.0, 0.0)

    sy, sz = dispersion_params(x_km, args.stability)
    conc = gaussian_plume(args.source_strength, args.wind_speed, x_m, y_m,
                          args.effective_height, sy, sz, z=0.0)
    tcf = terrain_correction(dem, source_elev, args.effective_height)
    conc_corrected = conc * tcf

    # NoData 区域浓度置 0
    if valid_mask is not None:
        conc_corrected = np.where(valid_mask, conc_corrected, 0.0).astype(np.float32)

    out_path = os.path.join(output_dir, "concentration.tif")
    write_geotiff(out_path, conc_corrected, bbox)

    valid_count = int(valid_mask.sum()) if valid_mask is not None else int(dem.size)
    params = {
        "stability": args.stability,
        "source_strength_g_s": args.source_strength,
        "wind_speed_m_s": args.wind_speed,
        "effective_height_m": args.effective_height,
        "source_col": cx, "source_row": cy,
        "valid_pixel_count": valid_count,
        "max_concentration_ug_m3": float(np.max(conc_corrected)),
        "mean_concentration_ug_m3": float(np.mean(conc_corrected)),
    }
    params_path = os.path.join(output_dir, "dispersion_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": out_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    qa: Dict[str, Any] = {
        "source": source_note, "stability": args.stability,
        "valid_pixel_count": valid_count,
        "max_conc_ug_m3": params["max_concentration_ug_m3"],
        "mean_conc_ug_m3": params["mean_concentration_ug_m3"],
    }
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] valid pixels: {valid_count}")
        print(f"[{SKILL_NAME}] max C: {qa['max_conc_ug_m3']:.2f} μg/m³")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Air quality dispersion via Gaussian plume model.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input DEM GeoTIFF for terrain correction")
    p.add_argument("--stability", default="D", choices=STABILITY_CLASSES,
                   help="Pasquill-Gifford stability class (default: D)")
    p.add_argument("--source-strength", type=float, default=100.0, help="emission rate Q (g/s)")
    p.add_argument("--wind-speed", type=float, default=3.0, help="wind speed u (m/s)")
    p.add_argument("--effective-height", type=float, default=50.0, help="stack height H (m)")
    p.add_argument("--synthetic", action="store_true", help="generate flat terrain (offline)")
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
