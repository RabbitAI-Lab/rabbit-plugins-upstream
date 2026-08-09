#!/usr/bin/env python3
"""radiometric-calibration — 辐射定标

将传感器原始 DN（数字量化值）转换为物理量，应用传感器增益/偏移与太阳辐照度
参数。实现了两种定标输出：

- **toa_radiance**（大气顶辐射亮度）：L = gain × DN + bias，单位 W/m²/sr/µm。
- **toa_reflectance**（大气顶反射率）：ρ = π · L · d² / (ESUN · cosθ)，
  其中 d 为日地距离（天文单位，默认 1），θ 为太阳天顶角，ESUN 为大气外太阳辐照度。
  结果裁剪到 [0, 1]。

数据源：本地多光谱 GeoTIFF（DN 栅格，Landsat C2 L1 / Sentinel-2 L1C / 通用），
或使用 ``--synthetic`` 生成物理一致的模拟 DN 影像用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python radiometric-calibration.py --input scene.tif --sensor landsat8 --output-type toa_reflectance
    python radiometric-calibration.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "radiometric-calibration"

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


# ---------------------------------------------------------------------------
# 传感器元数据：波段名、中心波长 (µm)、ESUN (W/m²/µm)、DN->radiance 增益/偏移
# 数值取自 Chander et al. 2009 (Landsat) / ESA S2 文档，公开领域。
# ---------------------------------------------------------------------------
SENSORS: Dict[str, Dict[str, Any]] = {
    "landsat8": {
        "bands": ["blue", "green", "red", "nir", "swir1", "swir2"],
        "wavelength_um": [0.48, 0.56, 0.65, 0.86, 1.61, 2.20],
        "esun": [1970.0, 1842.0, 1547.0, 951.0, 245.0, 79.0],
        "gain": [0.012],
        "bias": [-60.0],
    },
    "sentinel2": {
        "bands": ["blue", "green", "red", "re1", "nir", "swir1"],
        "wavelength_um": [0.49, 0.56, 0.66, 0.70, 0.84, 1.61],
        "esun": [1950.0, 1820.0, 1550.0, 1430.0, 990.0, 245.0],
        "gain": [0.0001],
        "bias": [0.0],
    },
    "generic": {
        "bands": ["blue", "green", "red", "nir"],
        "wavelength_um": [0.48, 0.56, 0.66, 0.86],
        "esun": [1970.0, 1842.0, 1547.0, 951.0],
        "gain": [0.01],
        "bias": [0.0],
    },
}


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> None:
    """Validate geographic bbox [W, S, E, N] for ordering, sign, and 180°/90° limits.

    Raises ValidationError on any violation.
    """
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise ValidationError(
            f"--bbox requires 4 floats [W S E N], got {bbox!r}", bbox=list(bbox),
        )
    w, s, e, n = [float(v) for v in bbox]
    # numeric finiteness
    import math
    for name, v in (("W", w), ("S", s), ("E", e), ("N", n)):
        if not math.isfinite(v):
            raise ValidationError(
                f"--bbox {name}={v} is not finite", bbox=list(bbox),
            )
    # W < E (no antimeridian crossing supported in this skill)
    if w >= e:
        raise ValidationError(
            f"--bbox requires W < E (got W={w}, E={e}); "
            f"antimeridian crossing (W>E) is not supported — split into two bboxes",
            bbox=list(bbox), w=float(w), e=float(e),
        )
    # S < N
    if s >= n:
        raise ValidationError(
            f"--bbox requires S < N (got S={s}, N={n})", bbox=list(bbox),
        )
    # ranges
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"--bbox longitudes out of [-180, 180]: W={w}, E={e}",
            bbox=list(bbox),
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"--bbox latitudes out of [-90, 90]: S={s}, N={n}", bbox=list(bbox),
        )


def validate_calibration_inputs(solar_zenith_deg: float, earth_sun_distance: float) -> None:
    """Validate solar zenith angle and earth-sun distance physically."""
    if not (isinstance(solar_zenith_deg, (int, float)) and np.isfinite(float(solar_zenith_deg))):
        raise ValidationError(
            f"--solar-zenith must be a finite number, got {solar_zenith_deg!r}",
            solar_zenith_deg=solar_zenith_deg,
        )
    if not (0.0 <= float(solar_zenith_deg) < 90.0):
        raise ValidationError(
            f"--solar-zenith must be in [0, 90) degrees (cos(theta) must be > 0); got {solar_zenith_deg}",
            solar_zenith_deg=float(solar_zenith_deg),
        )
    if not (isinstance(earth_sun_distance, (int, float)) and np.isfinite(float(earth_sun_distance))):
        raise ValidationError(
            f"--earth-sun-distance must be a finite number, got {earth_sun_distance!r}",
            earth_sun_distance=earth_sun_distance,
        )
    if float(earth_sun_distance) <= 0.0:
        raise ValidationError(
            f"--earth-sun-distance must be > 0; got {earth_sun_distance}",
            earth_sun_distance=float(earth_sun_distance),
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def dn_to_radiance(band_dn: np.ndarray, gain: float, bias: float) -> np.ndarray:
    """DN → 大气顶辐射亮度：L = gain × DN + bias（裁剪到 ≥0）。"""
    radiance = gain * band_dn.astype(np.float32) + bias
    return np.clip(radiance, 0.0, None).astype(np.float32)


def radiance_to_reflectance(
    radiance: np.ndarray,
    esun: float,
    solar_zenith_deg: float,
    earth_sun_distance: float = 1.0,
) -> np.ndarray:
    """辐射亮度 → TOA 反射率：ρ = π · L · d² / (ESUN · cosθ)，裁剪到 [0,1]。"""
    cos_theta = np.cos(np.deg2rad(solar_zenith_deg))
    if cos_theta <= 0:
        raise ValidationError(
            f"solar zenith {solar_zenith_deg}° gives non-positive cos(theta)",
            solar_zenith_deg=float(solar_zenith_deg),
        )
    rho = (np.pi * radiance * earth_sun_distance ** 2) / (esun * cos_theta)
    return np.clip(rho, 0.0, 1.0).astype(np.float32)


def calibrate(
    cube: np.ndarray,
    sensor: str,
    output_type: str = "toa_reflectance",
    solar_zenith_deg: float = 30.0,
    earth_sun_distance: float = 1.0,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """对 (bands, H, W) 的 DN 立方体执行辐射定标。

    返回 (calibrated_cube, params)。output_type ∈ {toa_radiance, toa_reflectance}。
    """
    if sensor not in SENSORS:
        raise UsageError(
            f"unknown sensor '{sensor}'. Choose from: {sorted(SENSORS)}", sensor=sensor,
        )
    if output_type not in ("toa_radiance", "toa_reflectance"):
        raise UsageError(
            f"unknown output-type '{output_type}'. Choose from: toa_radiance, toa_reflectance",
            output_type=output_type,
        )
    meta = SENSORS[sensor]
    esuns = meta["esun"]
    gain = meta["gain"][0]
    bias = meta["bias"][0]
    nb = cube.shape[0]
    if nb > len(esuns):
        raise ValidationError(
            f"input has {nb} bands but sensor '{sensor}' defines {len(esuns)}",
            bands=int(nb), sensor=sensor,
        )

    out = np.zeros_like(cube, dtype=np.float32)
    band_params: List[Dict[str, Any]] = []
    for b in range(nb):
        radiance = dn_to_radiance(cube[b], gain, bias)
        if output_type == "toa_radiance":
            out[b] = radiance
            value_mean = float(np.mean(radiance))
        else:
            refl = radiance_to_reflectance(
                radiance, esuns[b], solar_zenith_deg, earth_sun_distance
            )
            out[b] = refl
            value_mean = float(np.mean(refl))
        band_params.append({
            "band_index": b,
            "band_name": meta["bands"][b] if b < len(meta["bands"]) else f"band_{b}",
            "esun": esuns[b],
            "mean_value": value_mean,
        })

    params = {
        "sensor": sensor,
        "output_type": output_type,
        "solar_zenith_deg": solar_zenith_deg,
        "earth_sun_distance": earth_sun_distance,
        "gain": gain,
        "bias": bias,
        "bands": band_params,
    }
    return out, params


# ---------------------------------------------------------------------------
# 合成数据：物理一致的模拟 DN 影像（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float],
    sensor: str,
    width: int = 128,
    height: int = 128,
    solar_zenith_deg: float = 30.0,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (bands, H, W) 的 DN 立方体：三类地物真值反射率 → TOA → radiance → DN。"""
    rng = np.random.default_rng(seed)
    meta = SENSORS.get(sensor, SENSORS["generic"])
    esuns = meta["esun"]
    gain = meta["gain"][0]
    bias = meta["bias"][0]
    nb = len(esuns)
    cos_theta = np.cos(np.deg2rad(solar_zenith_deg))

    yy, xx = np.mgrid[0:height, 0:width]
    yn = yy.astype(np.float32) / max(height - 1, 1)
    xn = xx.astype(np.float32) / max(width - 1, 1)

    veg_mask = ((xn + yn) > 1.1).astype(np.float32)
    water_mask = ((xn + yn) < 0.5).astype(np.float32)
    soil_mask = np.clip(1.0 - veg_mask - water_mask, 0.0, 1.0)

    veg_rho = [0.03, 0.08, 0.04, 0.15, 0.45, 0.20]
    soil_rho = [0.10, 0.14, 0.18, 0.22, 0.28, 0.30]
    water_rho = [0.06, 0.05, 0.03, 0.01, 0.005, 0.001]

    cube_dn = np.zeros((nb, height, width), dtype=np.float32)
    truth = np.zeros((nb, height, width), dtype=np.float32)
    for b in range(nb):
        vi = min(b, len(veg_rho) - 1)
        rho_surf = veg_mask * veg_rho[vi] + soil_mask * soil_rho[vi] + water_mask * water_rho[vi]
        rho_surf = np.clip(rho_surf + rng.normal(0, 0.005, size=rho_surf.shape).astype(np.float32), 0.0, 1.0)
        truth[b] = rho_surf
        # 简化：地表反射率近似当 TOA（忽略大气程辐射）→ radiance → DN
        radiance = rho_surf * esuns[b] * cos_theta / np.pi
        cube_dn[b] = ((radiance - bias) / gain).astype(np.float32)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "sensor": sensor,
        "surface_truth_stats": {f"band_{b}": float(np.mean(truth[b])) for b in range(nb)},
    }
    return cube_dn, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    cube: np.ndarray,
    bbox: List[float],
    nodata: float = -9999.0,
    mask: Any = None,
) -> None:
    """Write a (bands, H, W) cube to a GeoTIFF. Optional mask (True=NoData)
    writes nodata values for masked pixels."""
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
            band = cube[b].astype("float32")
            if mask is not None:
                band = np.where(mask[b], nodata, band).astype("float32")
            dst.write(band, b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """Read input GeoTIFF, returning (cube, bbox).

    ``cube`` is a numpy MaskedArray (with the NoData mask) when the source has a
    NoData value set, otherwise a regular ``np.ndarray``. Use ``np.ma.getmaskarray``
    to extract the boolean mask (True = NoData) for the MaskedArray case. Use
    ``np.ma.is_masked(cube)`` to detect it.

    Raises ValidationError if the entire raster is NoData.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
        if nodata is not None:
            arr = src.read(masked=True)  # numpy MaskedArray, mask=True means nodata
            if bool(np.ma.getmaskarray(arr).all()):
                raise ValidationError(
                    "input raster is entirely NoData — no pixels to calibrate",
                    path=path,
                )
            cube = arr.astype(np.float32)  # keep mask
        else:
            cube = src.read().astype(np.float32)
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
            "sensor": getattr(args, "sensor", None),
            "output_type": getattr(args, "output_type", None),
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
    os.makedirs(output_dir, exist_ok=True)

    bbox = list(args.bbox) if args.bbox else None

    # Validate synthetic bbox and physics params up-front (cheap, before any I/O)
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        if bbox is not None:
            validate_bbox(bbox)  # user-supplied bbox takes precedence but must be valid
        else:
            validate_bbox(file_bbox)  # file bbox must be valid
            bbox = file_bbox
        source_note = args.input
        synth_info = None
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        cube, synth_info = generate_synthetic_cube(
            bbox, args.sensor, solar_zenith_deg=args.solar_zenith,
        )
        source_note = "synthetic"

    # Extract mask from cube if it is a MaskedArray (real input with NoData)
    # The math path fills the masked values with 0.0 to avoid np operations
    # raising or returning NaN, and the original mask is reapplied at write time.
    if np.ma.is_masked(cube):
        mask: Any = np.ma.getmaskarray(cube).copy()
        cube = np.ma.filled(cube, fill_value=0.0).astype(np.float32)
    else:
        mask = None
        cube = cube.astype(np.float32)

    # Physics-input validation (only matters for toa_reflectance; cheap to always check)
    validate_calibration_inputs(args.solar_zenith, args.earth_sun_distance)

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    out, params = calibrate(
        cube, sensor=args.sensor, output_type=args.output_type,
        solar_zenith_deg=args.solar_zenith, earth_sun_distance=args.earth_sun_distance,
    )

    suffix = "toa_radiance" if args.output_type == "toa_radiance" else "toa_reflectance"
    out_tif = os.path.join(output_dir, f"{suffix}.tif")
    write_geotiff(out_tif, out, bbox, mask=mask)

    params_path = os.path.join(output_dir, "calibration_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "sensor": args.sensor,
        "output_type": args.output_type,
        "n_bands": int(out.shape[0]),
        "mean_value_per_band": [float(np.mean(out[b])) for b in range(out.shape[0])],
        "overall_mean": float(np.mean(out)),
    }
    if synth_info is not None:
        qa["synthetic_truth_mean_per_band"] = synth_info["surface_truth_stats"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(out.shape[0])},
        {"path": params_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] sensor: {args.sensor}  output: {args.output_type}")
        print(f"[{SKILL_NAME}] bands: {out.shape[0]}  shape: {out.shape[1:]}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        print(f"[{SKILL_NAME}] params: {params_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
        print(f"[{SKILL_NAME}] overall mean: {qa['overall_mean']:.5f}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Radiometric calibration: DN to TOA radiance or TOA reflectance.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multispectral GeoTIFF (DN)")
    p.add_argument("--sensor", default="generic", choices=sorted(SENSORS.keys()),
                   help="sensor calibration metadata (default: generic)")
    p.add_argument("--output-type", default="toa_reflectance",
                   choices=["toa_radiance", "toa_reflectance"],
                   help="calibration output (default: toa_reflectance)")
    p.add_argument("--solar-zenith", type=float, default=30.0,
                   help="solar zenith angle in degrees (default: 30)")
    p.add_argument("--earth-sun-distance", type=float, default=1.0,
                   help="earth-sun distance in AU (default: 1.0)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic scene (offline)")
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
