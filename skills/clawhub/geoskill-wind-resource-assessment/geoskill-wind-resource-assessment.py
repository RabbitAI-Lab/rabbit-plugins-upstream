#!/usr/bin/env python3
"""wind-resource-assessment — 风能资源评估

对风速时序执行 Weibull 分布拟合与风功率密度（WPD）估算，评估区域风能资源。
核心流程：

- **Weibull 拟合**：对逐像元风速时序估计形状参数 k 与尺度参数 c。支持
  矩估计（method of moments）与最大似然（MLE）两种方法。
- **风功率密度**：WPD = 0.5 × ρ × mean(v³)，ρ 为标准空气密度 ≈ 1.225 kg/m³。
- **高度外推**：用幂律风切变（power-law wind shear）将参考高度风速外推
  到目标轮毂高度（如 100 m）。
- **发电量估算**：由 WPD、代表面积与容量系数估算年发电量（MWh/yr）。

数据源：本地风速栅格时序 GeoTIFF（多波段 = 多时相），或使用 ``--synthetic``
生成符合 Weibull 分布的模拟风速场用于离线测试。

隐私声明 / Privacy：
- 默认完全离线运行，不发起任何网络请求。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python wind-resource-assessment.py --input wind_ts.tif --height 100
    python wind-resource-assessment.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "wind-resource-assessment"

# 标准空气密度 (kg/m³)，海平面 15°C
AIR_DENSITY = 1.225

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
def validate_bbox(bbox: Optional[List[float]], source: str = "bbox") -> None:
    """校验 EPSG:4326 经纬度 bbox：W<=E、S<=N、超经纬度→ValidationError(rc=6)。
    跨 180° 经线（|E-W| > 360）→ValidationError 并附"拆分为两侧"提示。
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(
            f"{source} must be [W, S, E, N] with 4 floats, got {bbox!r}",
            bbox=bbox,
        )
    w, s, e, n = bbox
    if not all(isinstance(v, (int, float)) and np.isfinite(v) for v in (w, s, e, n)):
        raise ValidationError(
            f"{source} contains non-finite values: {bbox!r}", bbox=bbox,
        )
    if w < -180.0 or e > 180.0 or s < -90.0 or n > 90.0:
        raise ValidationError(
            f"{source} out of WGS-84 range (lon∈[-180,180], lat∈[-90,90]): {bbox!r}",
            bbox=bbox,
        )
    if w > e:
        gap = e - w  # 负数
        if abs(gap) > 360.0:
            raise ValidationError(
                f"{source} span exceeds 360°: {bbox!r}", bbox=bbox,
            )
        raise ValidationError(
            f"{source} has W>E ({w} > {e}); cross-dateline not supported. "
            f"Split into two bboxes (e.g. [{w}, {s}, 180, {n}] and [-180, {s}, {e}, {n}]) "
            f"and run separately.",
            bbox=bbox,
        )
    if s > n:
        raise ValidationError(
            f"{source} has S>N ({s} > {n}); latitude must increase northward", bbox=bbox,
        )
    if (e - w) <= 0.0 or (n - s) <= 0.0:
        raise ValidationError(
            f"{source} has zero or negative area: {bbox!r}", bbox=bbox,
        )


def validate_params(args: argparse.Namespace) -> None:
    """校验 --height / --z-ref / --roughness / --air-density / --capacity-factor / --n-dates → ValidationError(rc=6)。"""
    if float(args.height) <= 0.0:
        raise ValidationError(
            f"--height must be > 0 m, got {args.height}", height=args.height,
        )
    if float(args.z_ref) <= 0.0:
        raise ValidationError(
            f"--z-ref must be > 0 m, got {args.z_ref}", z_ref=args.z_ref,
        )
    if float(args.roughness) <= 0.0:
        raise ValidationError(
            f"--roughness must be > 0 m, got {args.roughness}", roughness=args.roughness,
        )
    if float(args.air_density) <= 0.0:
        raise ValidationError(
            f"--air-density must be > 0 kg/m^3, got {args.air_density}",
            air_density=args.air_density,
        )
    if not (0.0 <= float(args.capacity_factor) <= 1.0):
        raise ValidationError(
            f"--capacity-factor must be in [0, 1], got {args.capacity_factor}",
            capacity_factor=args.capacity_factor,
        )
    if int(args.n_dates) < 2:
        raise ValidationError(
            f"--n-dates must be >= 2 (Weibull needs at least 2 time steps), "
            f"got {args.n_dates}", n_dates=args.n_dates,
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def fit_weibull(v: np.ndarray, method: str = "moment") -> Tuple[float, float]:
    """对风速样本拟合 Weibull 分布，返回 (形状 k, 尺度 c)。

    - ``moment``：矩估计。由均值与方差先估计 k，再由 Gamma 函数反推 c。
      k ≈ (σ/μ)^(-1.086)（Justus & Mikhail 1978 经验式），c = μ/Γ(1+1/k)。
    - ``mle``：最大似然。用 scipy.stats.weibull_min.fit（固定 loc=0）。

    负风速被截断为 0；全零样本返回 (0.0, 0.0)。
    """
    v = np.asarray(v, dtype=np.float64)
    v = v[np.isfinite(v)]
    v = v[v > 0.0]
    if v.size < 2:
        return 0.0, 0.0

    mu = float(np.mean(v))
    sigma = float(np.std(v, ddof=1))
    if mu <= 0.0:
        return 0.0, 0.0

    if method == "mle":
        from scipy.stats import weibull_min
        # floc=0 固定位置参数为 0，得到形状 c_（即 k）与尺度 scale（即 c）
        c_, _, scale = weibull_min.fit(v, floc=0.0)
        return float(c_), float(scale)

    # 矩估计
    if sigma <= 0.0:
        # 无方差：退化为常数风，k 很大，c≈μ
        return 20.0, mu
    k = (sigma / mu) ** -1.086
    k = float(np.clip(k, 0.5, 20.0))
    from scipy.special import gamma as _gamma
    c = mu / float(_gamma(1.0 + 1.0 / k))
    return k, c


def weibull_mean_v3(k: float, c: float) -> float:
    """由 Weibull 参数解析计算 E[v³] = c³·Γ(1 + 3/k)。

    用于无时序样本时的 WPD 闭合估算。k<=0 或 c<=0 时返回 0。
    """
    if k <= 0.0 or c <= 0.0:
        return 0.0
    from scipy.special import gamma as _gamma
    return float(c ** 3 * _gamma(1.0 + 3.0 / k))


def wind_power_density(v: np.ndarray, rho: float = AIR_DENSITY) -> float:
    """平均风功率密度 WPD = 0.5 × ρ × mean(v³)，单位 W/m²。"""
    v = np.asarray(v, dtype=np.float64)
    v = v[np.isfinite(v)]
    v = np.clip(v, 0.0, None)
    if v.size == 0:
        return 0.0
    return float(0.5 * rho * np.mean(v ** 3))


def extrapolate_wind(
    v_ref: np.ndarray,
    z_ref: float,
    z_target: float,
    roughness: float = 0.14,
) -> np.ndarray:
    """幂律风切变外推：v(z) = v_ref × (z/z_ref)^α。

    α 由地表粗糙度长度 z0 近似：α ≈ 1/ln(z_ref/z0)（简化）。roughness 越大
    （城市/森林）切变越强。z_target <= z_ref 时按比例缩小。
    """
    v_ref = np.asarray(v_ref, dtype=np.float64)
    z0 = max(float(roughness), 1e-3)
    z_ref = max(float(z_ref), z0 + 1.0)
    z_target = max(float(z_target), 0.0)
    alpha = 1.0 / np.log(z_ref / z0)
    ratio = (z_target / z_ref) ** alpha if z_ref > 0 else 1.0
    return v_ref * ratio


def annual_energy_mwh(
    wpd: float,
    rotor_area_m2: float = 12566.0,
    capacity_factor: float = 0.35,
    rated_power_kw: float = 2000.0,
) -> float:
    """由 WPD 估算单台机组年发电量（MWh/yr）。

    简化模型：年发电量 = 额定功率 × 容量系数 × 8760 h，再按 WPD 与额定
    WPD（~400 W/m² 对应满发）的比例做线性修正（上限 1.0）。rotor_area
    默认 2MW 机组叶轮面积（直径 ~120m）。
    """
    if wpd <= 0.0:
        return 0.0
    rated_wpd = 400.0
    load_fraction = min(wpd / rated_wpd, 1.0)
    mwh = rated_power_kw * capacity_factor * 8760.0 * load_fraction / 1000.0
    return float(mwh)


def assess_wind_field(
    cube: np.ndarray,
    height: float = 100.0,
    z_ref: float = 10.0,
    roughness: float = 0.14,
    method: str = "moment",
    rho: float = AIR_DENSITY,
) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    """对 (n_dates, H, W) 风速时序立方体逐像元评估风能资源。

    返回 (rasters, params)：
    - rasters["mean_wind"]：时序平均风速（外推到 height）
    - rasters["wpd"]：平均风功率密度 WPD（W/m²，基于 height 高度风速）
    - rasters["weibull_k"]：形状参数
    - rasters["weibull_c"]：尺度参数（m/s）
    """
    if cube.ndim != 3:
        raise ValidationError(
            f"expected a 3-D wind-speed cube (n_dates, H, W), got ndim={cube.ndim}",
            ndim=int(cube.ndim),
        )
    n_dates, h, w = cube.shape
    if n_dates < 2:
        raise ValidationError(
            f"need at least 2 time steps for Weibull fitting, got {n_dates}",
            n_dates=int(n_dates),
        )

    mean_wind = np.zeros((h, w), dtype=np.float32)
    wpd = np.zeros((h, w), dtype=np.float32)
    weibull_k = np.zeros((h, w), dtype=np.float32)
    weibull_c = np.zeros((h, w), dtype=np.float32)

    for j in range(h):
        for i in range(w):
            series = cube[:, j, i]
            # 外推到目标高度
            v_target = extrapolate_wind(series, z_ref, height, roughness)
            k, c = fit_weibull(v_target, method=method)
            mean_wind[j, i] = float(np.mean(np.clip(v_target, 0.0, None)))
            wpd[j, i] = wind_power_density(v_target, rho=rho)
            weibull_k[j, i] = k
            weibull_c[j, i] = c

    rasters = {
        "mean_wind": mean_wind,
        "wpd": wpd,
        "weibull_k": weibull_k,
        "weibull_c": weibull_c,
    }
    params = {
        "height_m": float(height),
        "z_ref_m": float(z_ref),
        "roughness": float(roughness),
        "air_density": float(rho),
        "fit_method": method,
        "n_dates": int(n_dates),
        "mean_wpd": float(np.mean(wpd)),
        "mean_wind_speed": float(np.mean(mean_wind)),
        "mean_weibull_k": float(np.mean(weibull_k[weibull_k > 0])) if np.any(weibull_k > 0) else 0.0,
        "mean_weibull_c": float(np.mean(weibull_c[weibull_c > 0])) if np.any(weibull_c > 0) else 0.0,
    }
    return rasters, params


# ---------------------------------------------------------------------------
# 合成数据：符合 Weibull 分布的模拟风速场（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float],
    n_dates: int = 50,
    height: int = 64,
    width: int = 64,
    true_k: float = 2.0,
    true_c: float = 7.0,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (n_dates, H, W) 的风速时序，逐像元服从 Weibull(k, c)。

    空间上叠加一个由西向东递增的尺度因子（模拟地形/海岸效应），
    使 c 在区域内变化，便于检验 Weibull 参数恢复。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xx_norm = xx.astype(np.float64) / max(width - 1, 1)

    # 尺度参数 c 空间变化：西部偏小，东部偏大（+/- 20%）
    c_field = true_c * (0.85 + 0.30 * xx_norm)  # 范围 ~[0.85c, 1.15c]
    # 形状参数 k 略微空间变化
    k_field = true_k * (1.0 + 0.10 * (xx_norm - 0.5))

    cube = np.zeros((n_dates, height, width), dtype=np.float32)
    for t in range(n_dates):
        from scipy.stats import weibull_min
        samples = weibull_min.rvs(
            k_field, scale=c_field, size=(height, width), random_state=rng
        )
        cube[t] = samples.astype(np.float32)

    info = {
        "bbox": bbox,
        "n_dates": int(n_dates),
        "width": int(width),
        "height": int(height),
        "true_k": float(true_k),
        "true_c": float(true_c),
        "note": "wind speeds at ~10 m reference height",
    }
    return cube, info


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
            "height": getattr(args, "height", None),
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

    # 1) 获取风速时序立方体
    #    通用契约：给了 --input 就读真实栅格；否则（含显式 --synthetic）走合成模式。
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        validate_bbox(bbox, source=f"--input bbox {file_bbox!r}")
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox, source="--bbox")
        cube, synth_info = generate_synthetic_cube(
            bbox, n_dates=args.n_dates,
        )
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input wind-speed cube is empty")
    if cube.ndim == 2:
        raise ValidationError(
            "input must be a multi-band time series (n_dates, H, W); got 2-D",
        )

    # 2) 数值参数校验（输入数据 ok 之后）
    validate_params(args)

    # ---- 校验全部通过后再创建输出目录 ----
    os.makedirs(output_dir, exist_ok=True)

    # 2) 风能资源评估
    rasters, params = assess_wind_field(
        cube, height=args.height, z_ref=args.z_ref,
        roughness=args.roughness, method=args.method, rho=args.air_density,
    )

    # 3) 发电量估算（用区域平均 WPD）
    energy = annual_energy_mwh(
        params["mean_wpd"], capacity_factor=args.capacity_factor,
    )
    params["estimated_annual_energy_mwh"] = energy

    # 4) 写出产物
    mean_wind_path = os.path.join(output_dir, "mean_wind_speed.tif")
    wpd_path = os.path.join(output_dir, "wind_power_density.tif")
    weibull_path = os.path.join(output_dir, "weibull_params.tif")

    write_geotiff(mean_wind_path, rasters["mean_wind"], bbox)
    write_geotiff(wpd_path, rasters["wpd"], bbox)
    weibull_stack = np.stack([rasters["weibull_k"], rasters["weibull_c"]], axis=0)
    write_geotiff(weibull_path, weibull_stack, bbox)

    params_path = os.path.join(output_dir, "weibull_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "height_m": float(args.height),
        "n_dates": int(params["n_dates"]),
        "mean_wind_speed": params["mean_wind_speed"],
        "mean_wpd": params["mean_wpd"],
        "mean_weibull_k": params["mean_weibull_k"],
        "mean_weibull_c": params["mean_weibull_c"],
        "estimated_annual_energy_mwh": energy,
    }
    if synth_info is not None:
        qa["synthetic_true_k"] = synth_info["true_k"]
        qa["synthetic_true_c"] = synth_info["true_c"]

    outputs = [
        {"path": mean_wind_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": wpd_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": weibull_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 2},
        {"path": params_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  height: {args.height} m")
        print(f"[{SKILL_NAME}] shape: {cube.shape}")
        print(f"[{SKILL_NAME}] mean wind speed: {params['mean_wind_speed']:.3f} m/s")
        print(f"[{SKILL_NAME}] mean WPD: {params['mean_wpd']:.2f} W/m2")
        print(f"[{SKILL_NAME}] mean Weibull k={params['mean_weibull_k']:.3f} "
              f"c={params['mean_weibull_c']:.3f} m/s")
        print(f"[{SKILL_NAME}] est. annual energy: {energy:.1f} MWh/yr")
        print(f"[{SKILL_NAME}] output: {wpd_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Wind resource assessment: Weibull fitting + wind power density.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input wind-speed time-series GeoTIFF (bands=dates)")
    p.add_argument("--height", type=float, default=100.0,
                   help="target hub height in metres (default: 100)")
    p.add_argument("--z-ref", type=float, default=10.0,
                   help="reference measurement height in metres (default: 10)")
    p.add_argument("--roughness", type=float, default=0.14,
                   help="surface roughness length z0 in metres (default: 0.14)")
    p.add_argument("--air-density", type=float, default=AIR_DENSITY,
                   help="air density in kg/m3 (default: 1.225)")
    p.add_argument("--capacity-factor", type=float, default=0.35,
                   help="turbine capacity factor for energy estimate (default: 0.35)")
    p.add_argument("--n-dates", type=int, default=50,
                   help="number of synthetic time steps (default: 50)")
    p.add_argument("--method", default="moment", choices=["moment", "mle"],
                   help="Weibull fitting method (default: moment)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a Weibull-distributed synthetic wind field (offline)")
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
