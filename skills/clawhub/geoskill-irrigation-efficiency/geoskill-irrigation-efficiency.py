#!/usr/bin/env python3
"""irrigation-efficiency — 灌溉效率评估

基于作物蒸散发（ET）与有效降水计算净灌溉需水量，并评估田间灌溉效率的
空间分布。核心内容：

- **作物蒸散发**：ET = PET × Kc，Kc 由作物类型查表（FAO-56 中期作物系数）。
- **有效降水**：把总降雨折算为作物可利用部分，支持 ``fixed``（固定系数）与
  ``usda``（USDA-SCS 经验式，强降雨利用率更低）两种方法。
- **净灌溉需水量**：demand = max(ET − Pe, 0)。
- **灌溉效率**：efficiency = clip(demand / applied, 0, 1)；当实灌量不足时
  另计缺水亏缺量 deficit = max(demand − applied, 0)。

输入：本地 GeoTIFF（band1=作物ET, band2=总降水, band3=实灌量），或
``--synthetic`` 生成物理一致的 ET/降水/作物/灌溉栅格用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，无网络访问。``--synthetic`` 完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python irrigation-efficiency.py --bbox 116 39 117 40 --synthetic
    python irrigation-efficiency.py --bbox 116 39 117 40 --eff-method usda --synthetic

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
SKILL_NAME = "irrigation-efficiency"

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
    """参数域校验：--eff-coeff ∈ (0, 1]。"""
    if args.eff_method not in ("fixed", "usda"):
        raise UsageError(
            f"unknown --eff-method '{args.eff_method}'; choose: fixed, usda")
    if args.eff_method == "fixed" and not (0.0 < args.eff_coeff <= 1.0):
        raise ValidationError(
            f"--eff-coeff must be in (0, 1] when --eff-method=fixed; got {args.eff_coeff}")


# ---------------------------------------------------------------------------
# FAO-56 中期作物系数 Kc（典型值）
# ---------------------------------------------------------------------------
KC_TABLE: Dict[int, Dict[str, Any]] = {
    0: {"name": "fallow", "kc": 0.30},
    1: {"name": "wheat", "kc": 1.15},
    2: {"name": "maize", "kc": 1.20},
    3: {"name": "rice", "kc": 1.20},
    4: {"name": "cotton", "kc": 1.15},
    5: {"name": "soybean", "kc": 1.10},
    6: {"name": "vegetable", "kc": 1.05},
}
DEFAULT_KC = 1.0


def kc_from_crop(crop: np.ndarray) -> np.ndarray:
    """把作物类型整型码栅格映射为 Kc 栅格。"""
    c = np.asarray(crop)
    kc = np.full(c.shape, float(DEFAULT_KC), dtype=np.float64)
    for code, meta in KC_TABLE.items():
        kc[c == code] = float(meta["kc"])
    return kc


# ---------------------------------------------------------------------------
# 核心算法 1：作物蒸散发
# ---------------------------------------------------------------------------
def crop_evapotranspiration(pet: np.ndarray, kc: np.ndarray) -> np.ndarray:
    """作物蒸散发 ET = PET × Kc（FAO-56 单作物系数法）。"""
    pet = np.asarray(pet, dtype=np.float64)
    kc = np.asarray(kc, dtype=np.float64)
    et = pet * kc
    return np.clip(et, 0.0, None)


# ---------------------------------------------------------------------------
# 核心算法 2：有效降水
# ---------------------------------------------------------------------------
def effective_precipitation(
    precip: np.ndarray, method: str = "fixed", coeff: float = 0.75,
) -> np.ndarray:
    """把总降雨折算为作物根区可利用的有效降水 Pe。

    - fixed: Pe = coeff · P（0<coeff≤1）。
    - usda:  USDA-SCS 经验式（月尺度，P 单位 mm）：
             P<250: Pe = P·(125−0.2P)/125；P≥250: Pe = 125+0.1P。
    结果裁剪到 [0, P]。
    """
    P = np.clip(np.asarray(precip, dtype=np.float64), 0.0, None)
    if method == "fixed":
        if not (0.0 < coeff <= 1.0):
            raise UsageError(
                f"coeff must be in (0, 1]; got {coeff}", coeff=coeff)
        pe = coeff * P
    elif method == "usda":
        pe = np.where(P < 250.0, P * (125.0 - 0.2 * P) / 125.0, 125.0 + 0.1 * P)
    else:
        raise UsageError(f"unknown eff-method '{method}'. Choose: fixed, usda", method=method)
    pe = np.clip(pe, 0.0, P)
    return pe.astype(np.float64)


# ---------------------------------------------------------------------------
# 核心算法 3：净灌溉需水量与灌溉效率
# ---------------------------------------------------------------------------
def irrigation_demand(et: np.ndarray, eff_precip: np.ndarray) -> np.ndarray:
    """净灌溉需水量 = max(ET − Pe, 0)。"""
    et = np.asarray(et, dtype=np.float64)
    pe = np.asarray(eff_precip, dtype=np.float64)
    return np.clip(et - pe, 0.0, None)


def irrigation_efficiency(demand: np.ndarray, applied: np.ndarray) -> np.ndarray:
    """灌溉效率 = clip(demand / applied, 0, 1)。

    applied≤0 的像元（无灌溉记录）记为 0。当实灌量 ≥ 需水量时效率 = demand/applied；
    实灌不足时效率取 1（所灌全部被利用），亏缺另行统计。
    """
    demand = np.asarray(demand, dtype=np.float64)
    applied = np.asarray(applied, dtype=np.float64)
    eff = np.zeros_like(demand, dtype=np.float64)
    valid = applied > 1e-9
    eff[valid] = np.clip(demand[valid] / applied[valid], 0.0, 1.0)
    return eff


def water_deficit(demand: np.ndarray, applied: np.ndarray) -> np.ndarray:
    """灌溉亏缺量 = max(demand − applied, 0)（实灌不足的缺口）。"""
    return np.clip(np.asarray(demand, dtype=np.float64) - np.asarray(applied, dtype=np.float64), 0.0, None)


# ---------------------------------------------------------------------------
# 合成数据：ET / 降水 / 作物 / 实灌量
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float], grid_shape: Tuple[int, int] = (64, 64), seed: int = 42,
) -> Dict[str, Any]:
    """生成一个生长季尺度的灌溉场景（单位 mm/season）。"""
    rng = np.random.default_rng(seed)
    H, W = int(grid_shape[0]), int(grid_shape[1])
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float64)
    xxn = xx / max(W - 1, 1)
    yyn = yy / max(H - 1, 1)

    # 参考蒸散发 PET：空间渐变（干旱区更高）
    pet = 520.0 + 160.0 * xxn - 60.0 * yyn + rng.normal(0, 15.0, (H, W))
    pet = np.clip(pet, 200.0, None)

    # 作物类型分区
    crop = np.full((H, W), 1, dtype=np.int32)      # 小麦
    crop[xxn > 0.66] = 2                           # 玉米
    crop[(xxn < 0.33) & (yyn > 0.66)] = 3          # 水稻
    crop[(xxn > 0.33) & (xxn < 0.66) & (yyn < 0.33)] = 4  # 棉花
    crop[(xxn < 0.15) & (yyn < 0.15)] = 0          # 休耕
    kc = kc_from_crop(crop)
    et = crop_evapotranspiration(pet, kc)

    # 降水：东南多、西北少
    precip = 380.0 - 140.0 * xxn + 90.0 * yyn + rng.normal(0, 25.0, (H, W))
    precip = np.clip(precip, 50.0, None)

    # 实灌量：围绕真需水量波动（农户行为差异），部分过灌、部分欠灌
    pe = effective_precipitation(precip, method="fixed", coeff=0.75)
    true_demand = irrigation_demand(et, pe)
    applied = true_demand * rng.uniform(0.7, 1.5, (H, W)) + rng.normal(0, 10.0, (H, W))
    applied = np.clip(applied, 0.0, None)

    return {
        "bbox": list(bbox),
        "grid_shape": (H, W),
        "pet": pet.astype(np.float32),
        "crop": crop,
        "kc": kc.astype(np.float32),
        "et": et.astype(np.float32),
        "precip": precip.astype(np.float32),
        "applied": applied.astype(np.float32),
    }


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
    """从 GeoTIFF 读 nodata 值（独立函数，便于 test_geotiff_roundtrip 兼容 2-tuple 接口）。"""
    import rasterio
    with rasterio.open(path) as src:
        return src.nodata


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
            "eff_method": getattr(args, "eff_method", None),
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

    # ---- 前置校验：参数 + bbox（必须先于 os.makedirs）----
    validate_params(args)
    if bbox is not None:
        bbox = validate_bbox(bbox)

    synth_info = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            bbox = validate_bbox(bbox)
        if cube.shape[0] < 3:
            raise ValidationError(
                "input raster needs >= 3 bands (crop_ET, precip, applied)",
                bands=int(cube.shape[0]),
            )
        # NoData -> NaN 替换；全 NoData -> rc=6
        src_nodata = read_geotiff_nodata(args.input)
        if src_nodata is not None:
            cube = np.where(cube == src_nodata, np.nan, cube).astype(np.float32)
        valid_mask = np.isfinite(cube).all(axis=0)
        if not valid_mask.any():
            raise ValidationError("all input pixels are NoData")
        et = cube[0].astype(np.float64)
        precip = cube[1].astype(np.float64)
        applied = cube[2].astype(np.float64)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        synth_info = generate_synthetic(bbox, seed=args.seed)
        et = synth_info["et"].astype(np.float64)
        precip = synth_info["precip"].astype(np.float64)
        applied = synth_info["applied"].astype(np.float64)
        source_note = "synthetic"

    if et.size == 0:
        raise ValidationError("empty input raster")

    # ---- 校验通过后再创建输出目录（避免失败时留空目录）----
    os.makedirs(output_dir, exist_ok=True)

    # 有效降水 → 需水量 → 效率
    pe = effective_precipitation(precip, method=args.eff_method, coeff=args.eff_coeff)
    demand = irrigation_demand(et, pe)
    eff = irrigation_efficiency(demand, applied)
    deficit = water_deficit(demand, applied)

    # 输出栅格
    out_demand = os.path.join(output_dir, "irrigation_demand.tif")
    write_geotiff(out_demand, demand.astype(np.float32), bbox)
    out_eff = os.path.join(output_dir, "irrigation_efficiency.tif")
    write_geotiff(out_eff, eff.astype(np.float32), bbox)
    out_deficit = os.path.join(output_dir, "water_deficit.tif")
    write_geotiff(out_deficit, deficit.astype(np.float32), bbox)

    # 报告（NaN-safe：partial NoData 时 nanmean 仍返回有效值）
    valid_eff = eff[(applied > 1e-9) & np.isfinite(demand) & np.isfinite(applied)]
    valid_demand = demand[np.isfinite(demand)]
    report = {
        "source": source_note,
        "eff_method": args.eff_method,
        "eff_coeff": args.eff_coeff,
        "mean_crop_et_mm": float(np.nanmean(et)) if np.isfinite(et).any() else 0.0,
        "mean_precip_mm": float(np.nanmean(precip)) if np.isfinite(precip).any() else 0.0,
        "mean_effective_precip_mm": float(np.nanmean(pe)) if np.isfinite(pe).any() else 0.0,
        "mean_demand_mm": float(valid_demand.mean()) if valid_demand.size else 0.0,
        "mean_applied_mm": float(np.nanmean(applied)) if np.isfinite(applied).any() else 0.0,
        "mean_efficiency": float(valid_eff.mean()) if valid_eff.size else 0.0,
        "mean_deficit_mm": float(np.nanmean(deficit)) if np.isfinite(deficit).any() else 0.0,
        "demand_gt_applied_fraction": float(
            np.mean(valid_demand > applied[np.isfinite(applied) & np.isfinite(demand)])
        ) if valid_demand.size else 0.0,
    }
    report_path = os.path.join(output_dir, "irrigation_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    qa = {
        "source": source_note,
        "eff_method": args.eff_method,
        "mean_demand_mm": report["mean_demand_mm"],
        "mean_efficiency": report["mean_efficiency"],
        "mean_deficit_mm": report["mean_deficit_mm"],
        "efficiency_min": float(np.nanmin(eff)) if np.isfinite(eff).any() else 0.0,
        "efficiency_max": float(np.nanmax(eff)) if np.isfinite(eff).any() else 0.0,
    }
    outputs = [
        {"path": out_demand, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_eff, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_deficit, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  eff-method: {args.eff_method}")
        print(f"[{SKILL_NAME}] mean ET: {report['mean_crop_et_mm']:.1f} mm  "
              f"mean demand: {report['mean_demand_mm']:.1f} mm")
        print(f"[{SKILL_NAME}] mean efficiency: {report['mean_efficiency']:.3f}  "
              f"mean deficit: {report['mean_deficit_mm']:.1f} mm")
        print(f"[{SKILL_NAME}] output: {out_demand}  {out_eff}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Irrigation efficiency assessment from crop ET and effective precipitation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF (band1=crop_ET, band2=precip, band3=applied)")
    p.add_argument("--eff-method", default="fixed", choices=["fixed", "usda"],
                   help="effective precipitation method (default: fixed)")
    p.add_argument("--eff-coeff", type=float, default=0.75,
                   help="effective precip coefficient for method=fixed (default: 0.75)")
    p.add_argument("--seed", type=int, default=42, help="random seed (default: 42)")
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
