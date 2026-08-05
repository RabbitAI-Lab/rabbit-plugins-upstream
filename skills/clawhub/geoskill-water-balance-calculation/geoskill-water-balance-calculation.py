#!/usr/bin/env python3
"""water-balance-calculation — 水量平衡计算

逐像元水量平衡计算，核心方程：

    P = ET + Q + ΔS

即 降水 = 蒸散发 + 径流 + 蓄水变化。对每个像元独立计算各分量，并求闭合差
（closure residual）：

    residual = P − ET − Q − ΔS

理想情况下闭合差为 0；实际数据因观测误差存在残差，可用相对闭合误差
（mean|residual| / mean P）评估数据一致性。

数据源：本地降水 GeoTIFF（EPSG:4326，作为 P 分量，其余分量按经验比例合成
用于演示），或 ``--synthetic`` 生成物理闭合（含小扰动）的 P/ET/Q/ΔS 完整
数据集用于离线测试。输出各分量栅格、闭合差栅格与报告 JSON。

隐私声明 / Privacy：
- 默认完全离线运行，不发起任何网络请求。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python water-balance-calculation.py --input precip.tif
    python water-balance-calculation.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "water-balance-calculation"

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


def validate_bbox(bbox):
    """Validate WGS-84 bbox. Returns (W, S, E, N) as floats.

    Rules:
      - 4 numeric values
      - -180 <= W, E <= 180; -90 <= S, N <= 90
      - W < E (no antimeridian crossing; split into two bboxes if needed)
      - S < N
      - width / height strictly positive
    Raises ValidationError (exit 6) on any failure.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(f"bbox must be 4 floats [W S E N], got: {bbox}")
    w, s, e, n = (float(v) for v in bbox)
    for label, val, lo, hi in (("W", w, -180.0, 180.0), ("E", e, -180.0, 180.0),
                               ("S", s, -90.0, 90.0), ("N", n, -90.0, 90.0)):
        if val < lo or val > hi:
            raise ValidationError(
                f"bbox {label}={val} out of range [{lo}, {hi}]; got bbox={bbox}"
            )
    if w >= e:
        raise ValidationError(
            f"bbox W={w} must be < E={e} (no antimeridian crossing; "
            f"if needed, split into two bboxes)"
        )
    if s >= n:
        raise ValidationError(
            f"bbox S={s} must be < N={n}"
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero or negative area: width={e - w:.3e}, height={n - s:.3e}"
        )
    return w, s, e, n


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def closure_residual(
    P: np.ndarray, ET: np.ndarray, Q: np.ndarray, dS: np.ndarray
) -> np.ndarray:
    """水量平衡闭合差：residual = P − ET − Q − ΔS。

    所有输入同形状（标量或数组），单位一致（如 mm/yr）。NoData 像素会得到 NaN
    残差。
    """
    P = np.asarray(P, dtype=np.float64)
    ET = np.asarray(ET, dtype=np.float64)
    Q = np.asarray(Q, dtype=np.float64)
    dS = np.asarray(dS, dtype=np.float64)
    return (P - ET - Q - dS).astype(np.float32)


def water_balance_stats(
    P: np.ndarray, ET: np.ndarray, Q: np.ndarray, dS: np.ndarray,
    residual: np.ndarray, pixel_area: float = 1.0,
) -> Dict[str, Any]:
    """汇总水量平衡统计：各分量均值、闭合差、相对闭合误差、体积量。

    NaN/NoData 像素被 nanmean 跳过统计；要求至少 1 个有限 P 像素。
    """
    P = np.asarray(P, dtype=np.float64)
    valid = np.isfinite(P)
    n_valid = int(valid.sum())
    if n_valid == 0:
        raise ValidationError(
            "no valid (finite) P pixels; cannot compute water balance"
        )
    mean_p = float(np.nanmean(P))
    # residual 中 NaN 像素对应 P 中 NaN 像素
    res_valid = residual[np.isfinite(residual)]
    if res_valid.size == 0:
        abs_res_mean = 0.0
        rel_closure = 0.0
        residual_mean = 0.0
        residual_std = 0.0
    else:
        abs_res_mean = float(np.mean(np.abs(res_valid)))
        rel_closure = abs_res_mean / mean_p if mean_p > 0 else 0.0
        residual_mean = float(np.mean(res_valid))
        residual_std = float(np.std(res_valid))
    return {
        "n_valid_pixels": n_valid,
        "mean_P_mm": mean_p,
        "mean_ET_mm": float(np.nanmean(ET)) if np.any(np.isfinite(ET)) else 0.0,
        "mean_Q_mm": float(np.nanmean(Q)) if np.any(np.isfinite(Q)) else 0.0,
        "mean_dS_mm": float(np.nanmean(dS)) if np.any(np.isfinite(dS)) else 0.0,
        "residual_mean_mm": residual_mean,
        "residual_std_mm": residual_std,
        "abs_residual_mean_mm": abs_res_mean,
        "relative_closure_error": float(rel_closure),
        "pixel_area_m2": float(pixel_area),
        "total_P_volume_m3": float(np.nansum(P) * pixel_area / 1000.0),
    }


def run_water_balance(
    P: np.ndarray, ET: np.ndarray, Q: np.ndarray, dS: np.ndarray,
    bbox: List[float],
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """水量平衡主流程，返回 (residual, report)。"""
    for name, arr in [("P", P), ("ET", ET), ("Q", Q), ("dS", dS)]:
        if np.asarray(arr).ndim != 2:
            raise ValidationError(f"component '{name}' must be 2D")
    shape = np.asarray(P).shape
    for name, arr in [("ET", ET), ("Q", Q), ("dS", dS)]:
        if np.asarray(arr).shape != shape:
            raise ValidationError(
                f"component '{name}' shape {np.asarray(arr).shape} != P shape {shape}"
            )

    residual = closure_residual(P, ET, Q, dS)
    h, w = shape
    pixel_area = pixel_area_m2(bbox, h, w)
    report = water_balance_stats(P, ET, Q, dS, residual, pixel_area)
    return residual, report


def pixel_area_m2(bbox: List[float], height: int, width: int) -> float:
    """估算单个像元的地表面积（平方米）。"""
    w, s, e, n = bbox
    mid_lat = (s + n) / 2.0
    dx_m = (e - w) / max(width, 1) * 111320.0 * np.cos(np.deg2rad(mid_lat))
    dy_m = (n - s) / max(height, 1) * 110540.0
    return float(abs(dx_m * dy_m))


# ---------------------------------------------------------------------------
# 合成数据：物理闭合（含小扰动）的 P/ET/Q/ΔS（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 (P, ET, Q, dS, info)，满足 P = ET + Q + ΔS（含 ~0.4% 小扰动）。

    P 为 400–1200 mm/yr 的空间场；ET ≈ 0.45P，Q ≈ 0.30P，
    ΔS 取闭合残值使方程精确成立，再叠加 std≈3 mm 的观测扰动。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yy = yy.astype(np.float32) / max(height - 1, 1)
    xx = xx.astype(np.float32) / max(width - 1, 1)

    P = 800.0 - 400.0 * xx + 200.0 * yy
    P = P + rng.normal(0, 50, size=P.shape).astype(np.float32)
    P = np.clip(P, 150.0, None).astype(np.float32)

    ET = (0.45 * P + rng.normal(0, 8, size=P.shape)).astype(np.float32)
    Q = (0.30 * P + rng.normal(0, 8, size=P.shape)).astype(np.float32)
    ET = np.clip(ET, 0.0, None).astype(np.float32)
    Q = np.clip(Q, 0.0, None).astype(np.float32)

    # ΔS 先取闭合残值（使方程精确成立），再叠加小扰动
    dS_exact = P - ET - Q
    perturb = rng.normal(0, 3.0, size=P.shape).astype(np.float32)
    dS = (dS_exact + perturb).astype(np.float32)

    info = {
        "bbox": bbox, "width": width, "height": height,
        "P_mean": float(np.mean(P)), "ET_mean": float(np.mean(ET)),
        "Q_mean": float(np.mean(Q)), "dS_mean": float(np.mean(dS)),
        "perturb_std_mm": 3.0,
    }
    return P, ET, Q, dS, info


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


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float], np.ndarray]:
    """Read a single-band raster, replacing NoData with NaN.

    Returns (array_2D, bbox, valid_mask).  All values identified as NoData
    (by the file's nodata metadata or by NaN in the data) become NaN in the
    array and False in the mask.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        if src.count < 1:
            raise ValidationError(f"input raster has 0 bands: {path}")
        data = src.read(1).astype(np.float64)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    valid_mask = np.isfinite(data)
    if nodata is not None:
        try:
            valid_mask &= (data != float(nodata))
        except (TypeError, ValueError):
            pass
    data = np.where(valid_mask, data, np.nan).astype(np.float32)
    return data, bbox, valid_mask


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

    # ---- P0/P1: validate bbox BEFORE mkdir ----
    if bbox is not None:
        bbox = list(validate_bbox(bbox))

    os.makedirs(output_dir, exist_ok=True)

    # 1) 获取四个分量
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        P, file_bbox, valid_mask = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            bbox = list(validate_bbox(bbox))
        # 真实模式：以降水 P 为基准，按经验比例合成其余分量（演示流程，精确闭合）
        ET = (0.45 * P).astype(np.float32)
        Q = (0.30 * P).astype(np.float32)
        dS = (P - ET - Q).astype(np.float32)
        n_valid = int(valid_mask.sum())
        if n_valid < 1:
            raise ValidationError(
                f"input P raster has 0 valid pixels (all NoData); need at least 1"
            )
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        P, ET, Q, dS, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    if P.size == 0:
        raise ValidationError("input data is empty")

    # 2) 水量平衡
    residual, report = run_water_balance(P, ET, Q, dS, bbox)

    # 3) 写出产物
    comp_tif = os.path.join(output_dir, "balance_components.tif")
    write_geotiff(comp_tif, np.stack([P, ET, Q, dS], axis=0), bbox)
    resid_tif = os.path.join(output_dir, "closure_residual.tif")
    write_geotiff(resid_tif, residual, bbox)

    report_path = os.path.join(output_dir, "water_balance_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "mean_P_mm": report["mean_P_mm"],
        "mean_ET_mm": report["mean_ET_mm"],
        "mean_Q_mm": report["mean_Q_mm"],
        "mean_dS_mm": report["mean_dS_mm"],
        "relative_closure_error": report["relative_closure_error"],
        "residual_std_mm": report["residual_std_mm"],
    }

    outputs = [
        {"path": comp_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 4},
        {"path": resid_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": report_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] P={report['mean_P_mm']:.1f}  ET={report['mean_ET_mm']:.1f}  "
              f"Q={report['mean_Q_mm']:.1f}  dS={report['mean_dS_mm']:.1f} (mm)")
        print(f"[{SKILL_NAME}] residual mean={report['residual_mean_mm']:.3f}  "
              f"std={report['residual_std_mm']:.3f} mm")
        print(f"[{SKILL_NAME}] relative closure error: {report['relative_closure_error']*100:.2f}%")
        print(f"[{SKILL_NAME}] components: {comp_tif}")
        print(f"[{SKILL_NAME}] residual:   {resid_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Per-pixel water balance P = ET + Q + dS with closure residual assessment.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input precipitation (P) GeoTIFF (EPSG:4326)")
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
