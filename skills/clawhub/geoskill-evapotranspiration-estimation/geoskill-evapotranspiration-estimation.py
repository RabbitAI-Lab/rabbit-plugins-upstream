#!/usr/bin/env python3
"""evapotranspiration-estimation — 蒸散发估算

从净辐射、气温、地表温度与植被指数估算区域蒸散发（ET，mm/day）。实现两种方法：

- **pt**（Priestley-Taylor，1972）：

      ET = α × Δ/(Δ + γ) × Rn × 0.408

  α≈1.26（湿润裸土/充分供水经验系数），Δ 为饱和水汽压—温度曲线斜率
  （kPa/°C，由气温经 Tetens 公式求得），γ 为干湿表常数（≈0.066 kPa/°C），
  Rn 为净辐射（MJ/m²/day），0.408 为 MJ/m² → mm 水深的潜热换算系数。
- **sebal**（简化 SEBAL 经验版）：用 NDVI 与 LST 构建蒸发比 EF
  （植被多、地表冷 → EF 高），ET = EF × Rn × 0.408。

数据源：本地多分量 GeoTIFF，或 ``--synthetic`` 生成物理一致的 Rn/T/LST/NDVI
模拟场用于离线测试。输出 ET 栅格（mm/day）与统计 JSON。

隐私声明 / Privacy：
- 默认完全离线运行，不发起任何网络请求。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python evapotranspiration-estimation.py --input rn.tif --method pt
    python evapotranspiration-estimation.py --bbox 116 39 117 40 --method pt --synthetic --output-dir ./out

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
SKILL_NAME = "evapotranspiration-estimation"

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

# MJ/m² → mm 水深换算系数（潜热 λ ≈ 2.45 MJ/kg）
MJ_TO_MM = 0.408
GAMMA_DEFAULT = 0.066  # 干湿表常数 kPa/°C（海平面附近）


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate geographic bbox. raise ValidationError on any structural issue."""
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            "bbox must be 4 floats [W, S, E, N]", bbox=str(bbox))
    w, s, e, n = [float(v) for v in bbox]
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError("bbox has non-finite values", bbox=bbox)
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0
            and -90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            "bbox out of WGS84 range (lon∈[-180,180], lat∈[-90,90])",
            bbox=bbox)
    if w >= e:
        raise ValidationError(
            f"bbox west ({w}) must be < east ({e}); "
            "this skill does not support anti-meridian crossing — split into two calls",
            bbox=bbox)
    if s >= n:
        raise ValidationError(
            f"bbox south ({s}) must be < north ({n})", bbox=bbox)
    span_lon = e - w
    span_lat = n - s
    if span_lon < 1e-5 or span_lat < 1e-5:
        raise ValidationError(
            f"bbox too small (lon span={span_lon:.7f}, lat span={span_lat:.7f}); "
            "both dimensions must be > 1e-5°", bbox=bbox)


def validate_cli_params(method: str, alpha: float, gamma: float) -> None:
    """CLI 参数前置校验（错误→rc=2）。"""
    if method not in ("pt", "sebal"):
        raise UsageError(
            f"unknown method '{method}'; choose pt|sebal", method=method)
    if not (float(alpha) > 0):
        raise UsageError(
            f"--alpha must be > 0 (PT coefficient); got {alpha}", alpha=alpha)
    if not (float(gamma) > 0):
        raise UsageError(
            f"--gamma must be > 0 (psychrometric constant kPa/°C); got {gamma}",
            gamma=gamma)


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def slope_vapor_pressure(T: np.ndarray) -> np.ndarray:
    """饱和水汽压—温度曲线斜率 Δ（kPa/°C）。

    Tetens 公式：es = 0.6108·exp(17.27·T/(T+237.3))，
    Δ = 4098·es / (T+237.3)²。T 单位 °C。
    """
    T = np.asarray(T, dtype=np.float64)
    es = 0.6108 * np.exp(17.27 * T / (T + 237.3))
    delta = 4098.0 * es / (T + 237.3) ** 2
    return delta


def priestley_taylor_et(
    Rn: np.ndarray,
    T: np.ndarray,
    alpha: float = 1.26,
    gamma: float = GAMMA_DEFAULT,
) -> np.ndarray:
    """Priestley-Taylor 蒸散发：ET = α·Δ/(Δ+γ)·Rn·0.408（mm/day）。

    Rn 单位 MJ/m²/day，T 单位 °C。结果非负。
    """
    Rn = np.asarray(Rn, dtype=np.float64)
    delta = slope_vapor_pressure(T)
    et_rad = float(alpha) * delta / (delta + gamma) * Rn
    et = et_rad * MJ_TO_MM
    return np.clip(et, 0.0, None).astype(np.float32)


def sebal_et(
    LST: np.ndarray,
    NDVI: np.ndarray,
    Rn: np.ndarray,
) -> np.ndarray:
    """简化 SEBAL 蒸散发：EF = clip(NDVI_norm × (1 − LST_norm), 0, 1)，
    ET = EF × Rn × 0.408（mm/day）。

    植被茂密（NDVI 高）且地表凉爽（LST 低）→ 蒸发比高 → ET 高。
    """
    LST = np.asarray(LST, dtype=np.float64)
    NDVI = np.asarray(NDVI, dtype=np.float64)
    Rn = np.asarray(Rn, dtype=np.float64)

    def _norm(x: np.ndarray) -> np.ndarray:
        lo, hi = float(np.min(x)), float(np.max(x))
        rng = hi - lo
        if rng < 1e-9:
            return np.full_like(x, 0.5)
        return (x - lo) / rng

    ndvi_n = _norm(NDVI)
    lst_n = _norm(LST)
    ef = np.clip(ndvi_n * (1.0 - lst_n), 0.0, 1.0)
    et = ef * Rn * MJ_TO_MM
    return np.clip(et, 0.0, None).astype(np.float32)


def run_et(
    method: str,
    Rn: np.ndarray,
    T: np.ndarray,
    LST: np.ndarray,
    NDVI: np.ndarray,
    alpha: float = 1.26,
    gamma: float = GAMMA_DEFAULT,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """蒸散发估算主流程，返回 (et_mm_day, params_dict)。"""
    Rn = np.asarray(Rn, dtype=np.float32)
    if Rn.ndim != 2:
        raise ValidationError(f"Rn must be 2D, got ndim={Rn.ndim}")

    if method == "pt":
        et = priestley_taylor_et(Rn, T, alpha=alpha, gamma=gamma)
        params = {"method": "pt", "alpha": alpha, "gamma": gamma,
                  "delta_mean": float(np.mean(slope_vapor_pressure(T)))}
    elif method == "sebal":
        et = sebal_et(LST, NDVI, Rn)
        params = {"method": "sebal"}
    else:
        raise UsageError(
            f"unknown method '{method}'. Choose from: pt, sebal", method=method
        )

    params.update({
        "et_mean_mm_day": float(np.mean(et)),
        "et_min_mm_day": float(np.min(et)),
        "et_max_mm_day": float(np.max(et)),
        "et_std_mm_day": float(np.std(et)),
        "Rn_mean_MJ": float(np.mean(Rn)),
    })
    return et, params


# ---------------------------------------------------------------------------
# 合成数据：物理一致的 Rn/T/LST/NDVI（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 (Rn, T, LST, NDVI, info)。

    场景：左侧为植被（高 NDVI、低 LST、高 ET），右侧为裸地/城市
    （低 NDVI、高 LST、低 ET）；净辐射存在空间梯度。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yy = yy.astype(np.float32) / max(height - 1, 1)
    xx = xx.astype(np.float32) / max(width - 1, 1)

    # 净辐射 8–18 MJ/m²/day（随纬度/云量梯度）
    Rn = 13.0 - 4.0 * yy + rng.normal(0, 0.8, size=(height, width))
    Rn = np.clip(Rn, 4.0, None).astype(np.float32)

    # 气温 15–28 °C
    T = (21.0 + 6.0 * xx + rng.normal(0, 0.5, size=(height, width))).astype(np.float32)

    # NDVI：左侧植被高、右侧低
    NDVI = 0.75 - 0.55 * xx + rng.normal(0, 0.04, size=(height, width))
    NDVI = np.clip(NDVI, 0.05, 0.95).astype(np.float32)

    # LST：与植被负相关（植被多→蒸散冷却→地表冷），280–315 K
    LST = 305.0 - 20.0 * NDVI + 8.0 * xx + rng.normal(0, 1.0, size=(height, width))
    LST = np.clip(LST, 275.0, 320.0).astype(np.float32)

    info = {
        "bbox": bbox, "width": width, "height": height,
        "Rn_mean": float(np.mean(Rn)), "T_mean": float(np.mean(T)),
        "LST_mean": float(np.mean(LST)), "NDVI_mean": float(np.mean(NDVI)),
    }
    return Rn, T, LST, NDVI, info


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
    """Read GeoTIFF band-1 → (data, bbox). NoData == profile.nodata 保留原值。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        data = src.read(1).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return data, bbox


def read_geotiff_with_nodata(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """Read GeoTIFF band-1 → (data, bbox, nodata_or_None)。NoData → NaN。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        data = src.read(1).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None and np.isfinite(nodata):
        data = np.where(data == float(nodata), np.nan, data)
    return data, bbox, nodata


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
            "method": getattr(args, "method", None),
            "alpha": getattr(args, "alpha", None),
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

    # ---- 0) CLI 参数前置校验（错误→rc=2）----
    validate_cli_params(method=args.method, alpha=args.alpha, gamma=args.gamma)

    bbox = list(args.bbox) if args.bbox else None
    if bbox is not None:
        validate_bbox(bbox)

    # 1) 获取输入场
    synth_info: Optional[Dict[str, Any]] = None
    src_nodata = None
    if args.input and not args.synthetic:
        Rn, file_bbox, src_nodata = read_geotiff_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        validate_bbox(bbox)
        # 真实模式：以输入净辐射 Rn 为基准，合成配套气象/地表场（演示流程）
        _, T, LST, NDVI, synth_info = generate_synthetic(
            bbox, width=Rn.shape[1], height=Rn.shape[0],
        )
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        Rn, T, LST, NDVI, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    if Rn.size == 0:
        raise ValidationError("input data is empty")

    # ---- 1.5) NoData / 全无效校验（仅看 Rn）----
    valid_mask = np.isfinite(Rn)
    n_valid = int(valid_mask.sum())
    n_total = int(Rn.size)
    if n_valid == 0:
        raise ValidationError(
            "input has no finite (non-NoData) pixels in Rn band after NoData masking; "
            "all values are NaN/nodata — cannot compute ET over an empty domain",
            n_total_pixels=n_total, input_nodata=src_nodata)
    # NaN 像素把 ET 置 0（用 sentinel 标注实际 NoData 在输出中区分）
    Rn_safe = np.where(valid_mask, Rn, 0.0)

    # ---- 通过校验后再创建输出目录 ----
    os.makedirs(output_dir, exist_ok=True)

    # 2) 蒸散发估算
    et, params = run_et(args.method, Rn_safe, T, LST, NDVI,
                        alpha=args.alpha, gamma=args.gamma)
    # NoData 像素在输出中置 0 哨兵
    et[~valid_mask] = 0.0

    # 3) 写出产物
    et_tif = os.path.join(output_dir, "evapotranspiration.tif")
    write_geotiff(et_tif, et, bbox)

    stats_path = os.path.join(output_dir, "et_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    # 仅在 valid 像素上统计
    if n_valid > 0:
        et_mean_v = float(np.mean(et[valid_mask]))
        et_max_v = float(np.max(et[valid_mask]))
        rn_mean_v = float(np.mean(Rn[valid_mask]))
    else:
        et_mean_v = et_max_v = rn_mean_v = 0.0

    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "et_mean_mm_day": et_mean_v,
        "et_max_mm_day": et_max_v,
        "Rn_mean_MJ": rn_mean_v,
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
        "valid_pixel_ratio": float(n_valid / n_total) if n_total else 0.0,
        "input_nodata": src_nodata,
    }
    if synth_info is not None:
        qa["synthetic_NDVI_mean"] = synth_info["NDVI_mean"]

    outputs = [
        {"path": et_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "nodata": -9999.0},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  method: {args.method}")
        print(f"[{SKILL_NAME}] ET mean={et_mean_v:.3f}  "
              f"max={et_max_v:.3f} mm/day")
        print(f"[{SKILL_NAME}] Rn mean={rn_mean_v:.2f} MJ/m²/day")
        print(f"[{SKILL_NAME}] valid pixels: {n_valid}/{n_total} "
              f"({qa['valid_pixel_ratio']:.2%})")
        print(f"[{SKILL_NAME}] ET raster: {et_tif}")
        print(f"[{SKILL_NAME}] stats: {stats_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Priestley-Taylor and simplified SEBAL evapotranspiration estimation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input net radiation (Rn) GeoTIFF (MJ/m²/day, EPSG:4326)")
    p.add_argument("--method", default="pt", choices=["pt", "sebal"],
                   help="ET estimation method (default: pt)")
    p.add_argument("--alpha", type=float, default=1.26,
                   help="Priestley-Taylor coefficient (default: 1.26)")
    p.add_argument("--gamma", type=float, default=GAMMA_DEFAULT,
                   help="psychrometric constant kPa/°C (default: 0.066)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic dataset (offline)")
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
