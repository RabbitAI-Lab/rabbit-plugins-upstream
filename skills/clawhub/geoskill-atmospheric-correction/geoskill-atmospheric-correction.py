#!/usr/bin/env python3
"""atmospheric-correction — 大气校正

对多光谱影像执行大气校正，将 DN / TOA 反射率转换为地表反射率（surface
reflectance）。实现了两种方法：

- **DOS**（Dark Object Subtraction，暗目标扣除，Chavez 1988 简化版）：
  逐波段估计大气路径辐射（用低分位数 DN 作为暗目标），从 TOA 反射率中扣除。
- **6s-simplified**（简化 6S 辐射传输）：在 DOS 基础上叠加一个随波长变化的
  瑞利散射光学厚度改正（蓝光强、红光弱），近似 6S 的大气程辐射行为。

数据源：本地多光谱 GeoTIFF（Landsat C2 L1 / Sentinel-2 L1C / 通用 DN 栅格），
或使用 ``--synthetic`` 生成物理一致的模拟影像用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，仅在显式 ``--place`` 解析地名时才会访问 Nominatim/Open-Meteo。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python atmospheric-correction.py --input scene.tif --sensor landsat8 --method dos
    python atmospheric-correction.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "atmospheric-correction"

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
# 传感器元数据：波段中心波长 (µm) 与太阳大气外辐照度 ESUN (W/m²/µm)
# 数值取自 Chander et al. 2009 (Landsat) / ESA S2 文档，公开领域。
# ---------------------------------------------------------------------------
SENSORS: Dict[str, Dict[str, Any]] = {
    "landsat8": {
        "bands": ["blue", "green", "red", "nir", "swir1", "swir2"],
        "wavelength_um": [0.48, 0.56, 0.65, 0.86, 1.61, 2.20],
        "esun": [1970.0, 1842.0, 1547.0, 951.0, 245.0, 79.0],
        "gain": [0.012],   # 简化：所有波段共用一个 DN->radiance 增益
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


def validate_bbox(bbox, ctx: str = "bbox") -> None:
    """Validate a (W, S, E, N) bbox: 4 floats, lon/lat ranges, W<E, S<N.

    Antimeridian crossing (W > E) is NOT supported; raises ValidationError
    suggesting the user split the bbox.
    """
    if bbox is None or len(bbox) != 4:
        raise UsageError(f"{ctx}: expected 4 floats (W S E N); got {bbox!r}")
    try:
        w, s, e, n = [float(v) for v in bbox]
    except (TypeError, ValueError):
        raise UsageError(f"{ctx}: bbox values must be numeric; got {bbox!r}")
    if not (all(np.isfinite([w, s, e, n]))):
        raise ValidationError(f"{ctx}: bbox values must be finite; got {bbox!r}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"{ctx}: longitude out of range (got W={w} E={e}); expected -180..180"
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"{ctx}: latitude out of range (got S={s} N={n}); expected -90..90"
        )
    if w >= e:
        raise ValidationError(
            f"{ctx}: requires W < E (got W={w} E={e}); "
            f"antimeridian crossing is not supported — split the bbox into two."
        )
    if s >= n:
        raise ValidationError(f"{ctx}: requires S < N (got S={s} N={n})")
    if (e - w) < 1e-6 or (n - s) < 1e-6:
        raise ValidationError(
            f"{ctx}: bbox extent too small ({(e - w):.2e} x {(n - s):.2e} deg); "
            f"need at least ~1e-6 deg in each direction"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def dark_object_reflectance(
    band_toa: np.ndarray,
    esun: float,
    solar_zenith_deg: float,
    gain: float,
    bias: float,
    percentile: float = 1.0,
) -> Tuple[float, float]:
    """估计单个波段的暗目标 TOA 反射率。

    返回 (rho_dark, dn_dark)。使用有效像元的低分位数 DN 作为暗目标，
    再经辐射传输公式转为 TOA 反射率。
    """
    valid = band_toa[np.isfinite(band_toa)]
    if valid.size == 0:
        return 0.0, 0.0
    dn_dark = float(np.percentile(valid, percentile))
    radiance = max(gain * dn_dark + bias, 1e-6)
    cos_theta = np.cos(np.deg2rad(solar_zenith_deg))
    # rho = pi * L / (ESUN * cos(theta))，日地距离 d 取 1.0（简化）
    rho_dark = (np.pi * radiance) / (esun * cos_theta)
    return float(rho_dark), dn_dark


def rayleigh_optical_depth(wavelength_um: float) -> float:
    """简化瑞利光学厚度：tau_R ~ 0.008569 * lambda^-4 * (1 + 0.0113*lambda^-2 + 0.00013*lambda^-4)。

    这是 Hansen & Travis 1974 的经验式，蓝光 (~0.48µm) 约 0.10，红光 (~0.66µm) 约 0.02。
    """
    lam = float(wavelength_um)
    inv2 = lam ** -2
    inv4 = lam ** -4
    return 0.008569 * inv4 * (1.0 + 0.0113 * inv2 + 0.00013 * inv4)


def dos_correct(
    cube: np.ndarray,
    sensor: str,
    solar_zenith_deg: float = 30.0,
    percentile: float = 1.0,
    method: str = "dos",
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """对 (bands, H, W) 的 DN 立方体执行大气校正。

    返回 (surface_reflectance_cube, params_dict)。
    输出反射率裁剪到 [0, 1]。
    """
    if sensor not in SENSORS:
        raise UsageError(
            f"unknown sensor '{sensor}'. Choose from: {sorted(SENSORS)}",
            sensor=sensor,
        )
    meta = SENSORS[sensor]
    esuns = meta["esun"]
    wls = meta["wavelength_um"]
    gain = meta["gain"][0]
    bias = meta["bias"][0]
    nb = cube.shape[0]
    if nb > len(esuns):
        raise ValidationError(
            f"input has {nb} bands but sensor '{sensor}' defines {len(esuns)}",
            bands=int(nb), sensor=sensor,
        )

    cos_theta = np.cos(np.deg2rad(solar_zenith_deg))
    out = np.zeros_like(cube, dtype=np.float32)
    band_params: List[Dict[str, Any]] = []

    for b in range(nb):
        band_dn = cube[b].astype(np.float32)
        # DN -> radiance -> TOA reflectance
        radiance = np.clip(gain * band_dn + bias, 1e-6, None)
        rho_toa = (np.pi * radiance) / (esuns[b] * cos_theta)

        rho_dark, dn_dark = dark_object_reflectance(
            band_dn, esuns[b], solar_zenith_deg, gain, bias, percentile
        )

        rho_surf = rho_toa - rho_dark

        if method == "6s-simplified":
            # 追加瑞利散射程辐射改正（随波长变化）
            tau_r = rayleigh_optical_depth(wls[b])
            # 瑞利路径反射率近似：rho_R ~ tau_R / (4 * cos_theta)
            rho_rayleigh = tau_r / (4.0 * cos_theta)
            rho_surf = rho_surf - rho_rayleigh
            extra = {"tau_rayleigh": float(tau_r), "rho_rayleigh": float(rho_rayleigh)}
        else:
            extra = {}

        rho_surf = np.clip(rho_surf, 0.0, 1.0).astype(np.float32)
        out[b] = rho_surf

        bp = {
            "band_index": b,
            "band_name": meta["bands"][b] if b < len(meta["bands"]) else f"band_{b}",
            "wavelength_um": wls[b],
            "esun": esuns[b],
            "dn_dark": dn_dark,
            "rho_dark": rho_dark,
        }
        bp.update(extra)
        band_params.append(bp)

    params = {
        "method": method,
        "sensor": sensor,
        "solar_zenith_deg": solar_zenith_deg,
        "dark_object_percentile": percentile,
        "bands": band_params,
    }
    return out, params


# ---------------------------------------------------------------------------
# 合成数据：物理一致的模拟影像（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float],
    sensor: str,
    width: int = 128,
    height: int = 128,
    solar_zenith_deg: float = 30.0,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成一个 (bands, H, W) 的 DN 立方体，内含三类地物 + 波长相关霾。

    地物真值反射率：植被（高 NIR）、土壤（平坦）、水体（低且随波长递减）。
    再叠加一个蓝光强、红光弱的大气路径辐射，模拟真实大气效应，
    使 DOS/6s 校正能产生可见且合理的改善。
    """
    rng = np.random.default_rng(seed)
    meta = SENSORS.get(sensor, SENSORS["generic"])
    esuns = meta["esun"]
    wls = meta["wavelength_um"]
    gain = meta["gain"][0]
    bias = meta["bias"][0]
    nb = len(esuns)
    cos_theta = np.cos(np.deg2rad(solar_zenith_deg))

    yy, xx = np.mgrid[0:height, 0:width]
    yy = yy.astype(np.float32) / max(height - 1, 1)
    xx = xx.astype(np.float32) / max(width - 1, 1)

    # 地物分区掩膜：左下=水体，右上=植被，其余=土壤（用平滑边界）
    veg_mask = ((xx + yy) > 1.1).astype(np.float32)
    water_mask = ((xx + yy) < 0.5).astype(np.float32)
    soil_mask = 1.0 - veg_mask - water_mask
    soil_mask = np.clip(soil_mask, 0.0, 1.0)

    # 各地物在每个波段的真实地表反射率（典型值）
    # 顺序：蓝 绿 红 红边/近红外 近红外/短波 短波
    veg_rho = [0.03, 0.08, 0.04, 0.15, 0.45, 0.20]
    soil_rho = [0.10, 0.14, 0.18, 0.22, 0.28, 0.30]
    water_rho = [0.06, 0.05, 0.03, 0.01, 0.005, 0.001]

    cube_dn = np.zeros((nb, height, width), dtype=np.float32)
    truth = np.zeros((nb, height, width), dtype=np.float32)

    for b in range(nb):
        vi = min(b, len(veg_rho) - 1)
        rho_surf = (
            veg_mask * veg_rho[vi]
            + soil_mask * soil_rho[vi]
            + water_mask * water_rho[vi]
        )
        # 加一点空间纹理噪声
        rho_surf = rho_surf + rng.normal(0, 0.005, size=rho_surf.shape).astype(np.float32)
        rho_surf = np.clip(rho_surf, 0.0, 1.0)
        truth[b] = rho_surf

        # 大气路径反射率：瑞利型，蓝光强
        tau_r = rayleigh_optical_depth(wls[b])
        rho_path = tau_r / (4.0 * cos_theta) + 0.01  # +气溶胶底噪
        rho_toa = rho_surf + rho_path

        # TOA 反射率 -> radiance -> DN
        radiance = rho_toa * esuns[b] * cos_theta / np.pi
        dn = (radiance - bias) / gain
        cube_dn[b] = dn.astype(np.float32)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "sensor": sensor,
        "solar_zenith_deg": solar_zenith_deg,
        "surface_truth_stats": {
            f"band_{b}": float(np.mean(truth[b])) for b in range(nb)
        },
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
    """Read multi-band GeoTIFF → (cube (nb, H, W) float32, bbox [W, S, E, N]).

    NoData values (from raster profile) are converted to NaN so the caller
    can mask them out via ``np.isfinite``.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        nodata = src.nodata
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    if nodata is not None:
        nd = float(nodata)
        if np.isfinite(nd):
            cube = np.where(cube == nd, np.nan, cube)
        else:
            cube = np.where(cube == nd, np.nan, cube)
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
            "method": getattr(args, "method", None),
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

    # 1) 获取数据立方体
    #    通用契约：给了 --input 就读真实栅格；否则（含显式 --synthetic）走合成模式。
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, synth_info = generate_synthetic_cube(
            bbox, args.sensor, solar_zenith_deg=args.solar_zenith,
        )
        source_note = "synthetic"

    # ---- validation (BEFORE os.makedirs to avoid empty output dirs) ----
    if bbox is None:
        raise UsageError("could not determine bbox")
    validate_bbox(bbox, ctx="bbox")
    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if args.input and not args.synthetic:
        valid_count = int(np.sum(np.isfinite(cube)))
        if valid_count == 0:
            raise ValidationError(
                f"input raster has no valid (non-NoData) pixels: {args.input}"
            )
    os.makedirs(output_dir, exist_ok=True)

    # 2) 大气校正
    surf, params = dos_correct(
        cube, sensor=args.sensor,
        solar_zenith_deg=args.solar_zenith,
        percentile=args.dark_percentile,
        method=args.method,
    )

    # 3) 写出产物
    out_tif = os.path.join(output_dir, "surface_reflectance.tif")
    write_geotiff(out_tif, surf, bbox)

    params_path = os.path.join(output_dir, "correction_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    # QA：逐波段均值反射率
    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "sensor": args.sensor,
        "n_bands": int(surf.shape[0]),
        "mean_reflectance_per_band": [float(np.mean(surf[b])) for b in range(surf.shape[0])],
        "overall_mean_reflectance": float(np.mean(surf)),
    }
    if synth_info is not None:
        qa["synthetic_truth_mean_per_band"] = synth_info["surface_truth_stats"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(surf.shape[0])},
        {"path": params_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  sensor: {args.sensor}")
        print(f"[{SKILL_NAME}] bands:  {surf.shape[0]}  shape: {surf.shape[1:]}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        print(f"[{SKILL_NAME}] params: {params_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
        print(f"[{SKILL_NAME}] mean surface reflectance: {qa['overall_mean_reflectance']:.4f}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Atmospheric correction (DOS / simplified 6S) for multispectral imagery.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multispectral GeoTIFF (DN / radiance)")
    p.add_argument("--sensor", default="generic", choices=sorted(SENSORS.keys()),
                   help="sensor spectral metadata (default: generic)")
    p.add_argument("--method", default="dos", choices=["dos", "6s-simplified"],
                   help="correction method (default: dos)")
    p.add_argument("--solar-zenith", type=float, default=30.0,
                   help="solar zenith angle in degrees (default: 30)")
    p.add_argument("--dark-percentile", type=float, default=1.0,
                   help="percentile for dark-object DN selection (default: 1.0)")
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
