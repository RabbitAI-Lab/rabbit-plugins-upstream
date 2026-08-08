#!/usr/bin/env python3
"""cyclone-damage-assessment — 台风/气旋灾害评估

用 Holland 参数化风场重建气旋风速分布，经脆弱性曲线转为损毁率，再叠加降水与
风暴潮贡献，与暴露度（资产/人口价值）相乘得到逐像元损失。

模型：

    V(r) = Vmax · sqrt( x·exp(1-x) ),  x = (Rmax/r)^B      （Holland 梯度风，r=Rmax 处取 Vmax，风眼平静）
    DR(V) = 1 / (1 + exp(-k·(V - V50)))                    （sigmoid 脆弱性曲线，[0,1]，随风速单调增）
    损失   = 综合损毁率(风/雨/潮加权) × 暴露价值

数据源：本地多波段 GeoTIFF（band1=暴露价值、band2=降水量），风场由参数合成；
或 ``--synthetic`` 生成完整场景。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python cyclone-damage-assessment.py --input exposure.tif --vmax 55 --rmax 30000
    python cyclone-damage-assessment.py --bbox 120 25 121 26 --synthetic --output-dir ./out

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
SKILL_NAME = "cyclone-damage-assessment"

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
# 核心算法
# ---------------------------------------------------------------------------
def holland_wind_speed(r: np.ndarray, vmax: float, rmax: float, b: float = 1.5) -> np.ndarray:
    """Holland 参数化梯度风速 V(r)（m/s）。

    r 为到风眼距离（m）。在 r=Rmax 处取 Vmax；风眼内部(r<Rmax)迅速衰减到平静；
    外围随距离衰减。对 Vmax 单调（线性比例）。
    """
    r = np.clip(np.asarray(r, dtype=np.float64), 1.0, None)
    if vmax < 0:
        raise ValidationError("vmax must be >= 0")
    if rmax <= 0 or b <= 0:
        raise ValidationError("rmax and b must be > 0")
    x_log = float(b) * (np.log(float(rmax)) - np.log(r))
    x = np.exp(np.clip(x_log, -60.0, 50.0))  # x = (Rmax/r)^B，限幅防溢出
    term = x * np.exp(1.0 - x)               # 大 x 时 exp(1-x)->0, 乘积->0（无 nan）
    v = float(vmax) * np.sqrt(np.clip(term, 0.0, None))
    return v.astype(np.float32)


def wind_field(shape: Tuple[int, int], center_rc: Tuple[float, float],
               vmax: float, rmax: float, cell: float, b: float = 1.5) -> np.ndarray:
    """生成二维风速场（m/s）。center_rc=(row,col)，cell 为像元尺寸(m)。"""
    H, W = shape
    yy, xx = np.mgrid[0:H, 0:W]
    r = np.hypot((yy - center_rc[0]) * cell, (xx - center_rc[1]) * cell)
    return holland_wind_speed(r, vmax, rmax, b)


def vulnerability_curve(wind: np.ndarray, v50: float = 40.0, k: float = 0.12) -> np.ndarray:
    """损毁率 DR(V) ∈ [0,1]：sigmoid，随风速单调递增，V=V50 时 DR=0.5。"""
    w = np.asarray(wind, dtype=np.float64)
    dr = 1.0 / (1.0 + np.exp(-float(k) * (w - float(v50))))
    return dr.astype(np.float32)


def storm_surge(wind: np.ndarray, coeff: float = 0.004) -> np.ndarray:
    """风暴潮增水（m）：近似与风速平方成正比（单调增）。"""
    w = np.clip(np.asarray(wind, dtype=np.float64), 0.0, None)
    return (float(coeff) * w ** 2).astype(np.float32)


def normalize01(arr: np.ndarray) -> np.ndarray:
    a = np.asarray(arr, dtype=np.float64)
    finite = a[np.isfinite(a)]
    if finite.size == 0:
        return np.zeros_like(a, dtype=np.float32)
    lo, hi = float(finite.min()), float(finite.max())
    if hi - lo <= 1e-12:
        return np.zeros_like(a, dtype=np.float32)
    return (np.where(np.isfinite(a), (a - lo) / (hi - lo), 0.0)).astype(np.float32)


def combined_damage(dr_wind: np.ndarray, precip: np.ndarray, surge: np.ndarray,
                    weights: Tuple[float, float, float] = (0.6, 0.2, 0.2)) -> np.ndarray:
    """综合损毁率：风/雨/潮归一化贡献加权，[0,1]。"""
    w = np.asarray(weights, dtype=np.float64)
    if np.any(w < 0) or w.sum() <= 1e-12:
        raise ValidationError("weights must be non-negative with positive sum")
    dw = np.clip(np.asarray(dr_wind, dtype=np.float64), 0, 1)
    dp = normalize01(precip)
    ds = normalize01(surge)
    comb = (w[0] * dw + w[1] * dp + w[2] * ds) / w.sum()
    return np.clip(comb, 0.0, 1.0).astype(np.float32)


def estimate_loss(damage_ratio: np.ndarray, exposure_value: np.ndarray) -> np.ndarray:
    """逐像元损失 = 损毁率 × 暴露价值（非负）。"""
    dr = np.clip(np.asarray(damage_ratio, dtype=np.float64), 0, 1)
    ex = np.clip(np.asarray(exposure_value, dtype=np.float64), 0, None)
    if dr.shape != ex.shape:
        raise ValidationError("damage_ratio/exposure shape mismatch")
    return (dr * ex).astype(np.float32)


# ---------------------------------------------------------------------------
# 合成数据：暴露价值 + 降水 + 海岸（风暴潮）
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64,
                       seed: int = 42) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float64) / max(width - 1, 1)
    yn = yy.astype(np.float64) / max(height - 1, 1)
    exposure = np.clip(3000.0 * np.exp(-(((xn - 0.5) ** 2 + (yn - 0.5) ** 2)) / (2 * 0.3 ** 2))
                       + rng.normal(0, 50, (height, width)), 0, None).astype(np.float32)
    precip = np.clip(150.0 * np.exp(-(((xn - 0.45) ** 2 + (yn - 0.55) ** 2)) / (2 * 0.25 ** 2))
                     + rng.normal(0, 5, (height, width)), 0, None).astype(np.float32)
    coastal = (xn < 0.35).astype(np.float32)  # 西侧沿海
    layers = {"exposure": exposure, "precip": precip, "coastal": coastal}
    info = {"bbox": bbox, "width": width, "height": height}
    return layers, info


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
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0, dtype: str = "float32") -> None:
    import rasterio
    from rasterio.transform import from_bounds
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {"driver": "GTiff", "height": h, "width": w, "count": nb,
               "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
               "nodata": nodata, "compress": "deflate"}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype(dtype), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """Read a multiband GeoTIFF, returning (cube, bbox) with NoData→NaN."""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=True).astype(np.float32)
        cube = np.ma.filled(cube, np.nan)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir: str, inputs: Dict[str, Any], outputs: List[Dict[str, Any]],
                   qa: Dict[str, Any], started_at: str, exit_code: int) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs=inputs, outputs=[OutputFile(**o) for o in outputs], qa=qa,
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

    # 1) bbox 校验（先于 generate_synthetic 与 cell 计算）
    if bbox is not None:
        validate_bbox(bbox)

    # 2) 加载数据
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        # 重新校验 file_bbox（如 bbox 已显式给则上一步已校验）
        if bbox is not None:
            validate_bbox(bbox)
        exposure = cube[0]
        precip = cube[1] if cube.shape[0] > 1 else np.zeros_like(exposure)
        coastal = cube[2] if cube.shape[0] > 2 else np.ones_like(exposure)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        layers, _info = generate_synthetic(bbox)
        exposure, precip, coastal = layers["exposure"], layers["precip"], layers["coastal"]
        source_note = "synthetic"

    # 3) NoData 校验
    if not np.any(np.isfinite(exposure)):
        raise ValidationError(
            "input raster has no valid (finite) exposure pixels (all NoData or NaN)",
        )

    # 现在 makedirs
    os.makedirs(output_dir, exist_ok=True)

    H, W = exposure.shape
    center = (H / 2.0, W / 2.0)
    lat_m = 111320.0
    lon_m = 111320.0 * np.cos(np.deg2rad(np.mean([bbox[1], bbox[3]]))) if bbox else 111320.0
    cell = max(((bbox[2] - bbox[0]) * lon_m / W) if bbox else 1000.0, 1.0)

    wind = wind_field((H, W), center, args.vmax, args.rmax, cell, args.b)
    dr_wind = vulnerability_curve(wind, v50=args.v50, k=args.vk)
    surge = storm_surge(wind) * coastal
    dr = combined_damage(dr_wind, precip, surge)
    loss = estimate_loss(dr, exposure)

    wind_tif = os.path.join(output_dir, "wind_speed.tif")
    write_geotiff(wind_tif, wind, bbox)
    dr_tif = os.path.join(output_dir, "damage_ratio.tif")
    write_geotiff(dr_tif, dr, bbox)
    loss_tif = os.path.join(output_dir, "loss.tif")
    write_geotiff(loss_tif, loss, bbox)

    params = {"source": source_note, "vmax": args.vmax, "rmax": args.rmax,
              "b": args.b, "v50": args.v50, "cell_m": float(cell),
              "center_rc": list(center)}
    params_path = os.path.join(output_dir, "cyclone_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "max_wind_ms": float(wind.max()),
        "mean_damage_ratio": float(dr.mean()),
        "total_loss": float(loss.sum()),
        "total_exposure": float(exposure.sum()),
        "loss_ratio": float(loss.sum() / max(exposure.sum(), 1e-9)),
    }
    outputs = [
        {"path": wind_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": dr_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": loss_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, {"input": args.input, "bbox": bbox,
                              "vmax": args.vmax, "synthetic": bool(args.synthetic)},
                              outputs, qa, started_at, 0)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] Vmax: {args.vmax} m/s  max wind on grid: {qa['max_wind_ms']:.1f} m/s")
        print(f"[{SKILL_NAME}] total loss: {qa['total_loss']:.1f}  loss ratio: {qa['loss_ratio']:.3f}")
        print(f"[{SKILL_NAME}] outputs: {output_dir}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Cyclone damage assessment (Holland wind field + vulnerability + exposure).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoTIFF (band1=exposure value, band2=precipitation, band3=coastal mask)")
    p.add_argument("--vmax", type=float, default=50.0, help="maximum sustained wind (m/s, default: 50)")
    p.add_argument("--rmax", type=float, default=30000.0, help="radius of max wind (m, default: 30000)")
    p.add_argument("--b", type=float, default=1.5, help="Holland B parameter (default: 1.5)")
    p.add_argument("--v50", type=float, default=40.0, help="wind for 50%% damage (m/s, default: 40)")
    p.add_argument("--vk", type=float, default=0.12, help="vulnerability curve steepness (default: 0.12)")
    p.add_argument("--synthetic", action="store_true")
    p.add_argument("--output-dir", default="./output")
    p.add_argument("--quiet", action="store_true")
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
