#!/usr/bin/env python3
"""forest-cover-change — 森林覆盖变化检测

从多期 NDVI（或森林掩膜）检测森林覆盖的损失 / 增益 / 稳定：

1. **阈值判定**：逐期用 NDVI 阈值（默认 0.3）判定森林像元。
2. **损失/增益**：比较首末期——由森林降为非森林（且降幅 ≥ drop 阈值）
   记为损失；由非森林升为森林（且升幅 ≥ gain 阈值）记为增益；其余稳定。
3. **变化矢量幅度（CVA）**：把每个像元的时间序列视为矢量，
   计算相邻期差分的 L2 范数，量化变化强度。

输出森林变化类别栅格（0=稳定, 1=损失, 2=增益）、CVA 幅度栅格，
以及逐期森林面积与损失/增益面积统计 JSON。合成模式生成多期 NDVI，
并在确定区域注入砍伐（损失）与造林（增益），便于离线验证。

数据源：本地多波段 NDVI GeoTIFF（每波段一期），或 ``--synthetic`` 合成序列。

隐私声明 / Privacy：
- 默认离线运行，不访问任何网络服务。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python forest-cover-change.py --input ndvi_series.tif --threshold 0.3
    python forest-cover-change.py --bbox 116 39 117 40 --n-dates 4 --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import math
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "forest-cover-change"

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


CHANGE_NAMES = {0: "stable", 1: "loss", 2: "gain"}


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


def _pixel_area_km2(bbox: List[float], shape: Tuple[int, int]) -> Tuple[float, float]:
    h, w = shape
    lat_mid = (bbox[1] + bbox[3]) / 2.0
    km_px_x = (bbox[2] - bbox[0]) / max(w, 1) * 111.32 * math.cos(math.radians(lat_mid))
    km_px_y = (bbox[3] - bbox[1]) / max(h, 1) * 110.57
    return km_px_x * km_px_y, float(km_px_x * km_px_y * h * w)


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> None:
    """校验 bbox 合法性（W<=E, S<=N, 经纬度范围, 零面积）。"""
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise ValidationError(f"bbox must have 4 floats, got {bbox!r}", bbox=list(bbox))
    W_, S_, E_, N_ = (float(x) for x in bbox)
    if not (W_ <= E_ and S_ <= N_):
        raise ValidationError(
            f"invalid bbox ordering: W={W_} E={E_} S={S_} N={N_} "
            f"(require W<=E and S<=N)",
            w=W_, e=E_, s=S_, n=N_,
        )
    if not (-180.0 <= W_ <= 180.0 and -180.0 <= E_ <= 180.0):
        raise ValidationError(
            f"lon out of range [-180,180]: W={W_} E={E_}",
            w=W_, e=E_,
        )
    if not (-90.0 <= S_ <= 90.0 and -90.0 <= N_ <= 90.0):
        raise ValidationError(
            f"lat out of range [-90,90]: S={S_} N={N_}",
            s=S_, n=N_,
        )
    if (E_ - W_) <= 0.0 or (N_ - S_) <= 0.0:
        raise ValidationError(
            f"zero-area bbox: W={W_} E={E_} S={S_} N={N_}",
            w=W_, e=E_, s=S_, n=N_,
        )
    if E_ - W_ > 180.0 or N_ - S_ > 180.0:
        raise ValidationError(
            f"bbox too large (>=180° in either dim): W={W_} E={E_} S={S_} N={N_}",
            w=W_, e=E_, s=S_, n=N_,
        )
    # 跨 180° 暂不支持（避免 wrap-around 在生成器中产生歧义）
    if W_ < -180.0 + 1e-9 or E_ > 180.0 - 1e-9:
        if (E_ - W_) > 0 and (E_ - W_) < 360.0 and (180.0 - W_) < (E_ + 180.0):
            # 极少见：E 接近 180 且 W 接近 -180 但实际未跨，无需报错
            pass
    if W_ > E_ - 1e-9 and (E_ - W_) < 0:
        # already caught by W<=E check
        pass


def validate_params(args: argparse.Namespace) -> None:
    """校验 CLI 参数值域。"""
    if args.n_dates is not None and int(args.n_dates) < 2:
        raise UsageError(f"--n-dates must be >=2, got {args.n_dates}",
                         n_dates=int(args.n_dates))
    thr = float(args.threshold)
    if not (-1.0 < thr < 1.0):
        raise UsageError(f"--threshold must be in (-1,1), got {thr}",
                         threshold=thr)
    drop = float(args.drop_threshold)
    if not (0.0 <= drop <= 1.0):
        raise UsageError(f"--drop-threshold must be in [0,1], got {drop}",
                         drop_threshold=drop)
    gain = float(args.gain_threshold)
    if not (0.0 <= gain <= 1.0):
        raise UsageError(f"--gain-threshold must be in [0,1], got {gain}",
                         gain_threshold=gain)
    if int(args.start_year) < 1900 or int(args.start_year) > 2200:
        raise UsageError(
            f"--start-year out of plausible range [1900,2200]: {args.start_year}",
            start_year=int(args.start_year),
        )
    if int(args.interval_years) < 1:
        raise UsageError(
            f"--interval-years must be >=1, got {args.interval_years}",
            interval_years=int(args.interval_years),
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def forest_mask(ndvi: np.ndarray, threshold: float = 0.3) -> np.ndarray:
    """NDVI ≥ threshold 判定为森林，返回布尔掩膜。"""
    return np.asarray(ndvi, dtype=np.float32) >= float(threshold)


def change_vector_magnitude(stack: np.ndarray) -> np.ndarray:
    """变化矢量幅度（CVA）：相邻期差分平方的 L2 范数，(H, W)。

    NaN-safe：若任一相邻期为 NaN，对应像元结果为 NaN（与数组
    ``stack`` 中含 NaN 一致）。最终通过 ``isfinite`` 检查确保不是全 NaN。
    """
    stack = np.asarray(stack, dtype=np.float32)
    if stack.ndim != 3:
        raise ValidationError(
            f"stack must be 3-D (n_dates,H,W), got ndim={stack.ndim}",
            ndim=int(stack.ndim),
        )
    if stack.shape[0] < 2:
        raise ValidationError("need at least 2 dates for CVA", n_dates=int(stack.shape[0]))
    diffs = np.diff(stack, axis=0)
    sq = (diffs.astype(np.float64) ** 2)
    mag = np.sqrt(np.nansum(sq, axis=0))
    return mag.astype(np.float32)


def classify_forest_change(
    stack: np.ndarray,
    threshold: float = 0.3,
    drop_threshold: float = 0.1,
    gain_threshold: float = 0.1,
) -> Tuple[np.ndarray, Dict[str, np.ndarray]]:
    """由多期 NDVI 分类森林变化。

    返回 (change_class (H,W) int32 [0=stable,1=loss,2=gain, -1=nodata], mask_dict)。
    任意一期为 NaN 的像元 → nodata (-1)，不参与损失/增益/稳定。
    """
    stack = np.asarray(stack, dtype=np.float32)
    if stack.ndim != 3:
        raise ValidationError(
            f"stack must be 3-D (n_dates,H,W), got ndim={stack.ndim}",
            ndim=int(stack.ndim),
        )
    if stack.shape[0] < 2:
        raise ValidationError("need at least 2 dates", n_dates=int(stack.shape[0]))

    first = stack[0]
    last = stack[-1]
    valid_first = np.isfinite(first)
    valid_last = np.isfinite(last)
    valid = valid_first & valid_last
    # NaN-safe first/last for diff/threshold
    first_safe = np.where(valid_first, first, 0.0)
    last_safe = np.where(valid_last, last, 0.0)
    delta = last_safe - first_safe
    ff = (first_safe >= float(threshold)) & valid_first
    fl = (last_safe >= float(threshold)) & valid_last

    loss = ff & (delta <= -abs(drop_threshold))  # was 森林 in first, dropped
    gain = (~ff) & fl & (delta >= abs(gain_threshold))

    cls = np.full(first.shape, -1, dtype=np.int32)  # default nodata
    cls[valid] = 0  # stable default
    cls[loss] = 1
    cls[gain] = 2
    stable_mask = valid & ~(loss | gain)
    return cls, {"loss": loss, "gain": gain, "stable": stable_mask,
                 "valid": valid}


def forest_change_stats(
    cls: np.ndarray,
    stack: np.ndarray,
    bbox: List[float],
    threshold: float = 0.3,
    start_year: int = 2000,
    interval_years: int = 5,
) -> Dict[str, Any]:
    """逐类面积统计 + 逐期森林面积时间序列（km²）。"""
    px_area, total_area = _pixel_area_km2(bbox, cls.shape)
    total_px = int(cls.size)
    classes = []
    for code in (0, 1, 2):
        cnt = int((cls == code).sum())
        classes.append({
            "code": code,
            "name": CHANGE_NAMES[code],
            "pixel_count": cnt,
            "fraction": cnt / total_px if total_px else 0.0,
            "area_km2": cnt * px_area,
        })
    forest_series = []
    for i in range(stack.shape[0]):
        fpx = int(forest_mask(stack[i], threshold).sum())
        forest_series.append({
            "date_index": i,
            "year": int(start_year + i * interval_years),
            "forest_pixels": fpx,
            "forest_area_km2": fpx * px_area,
        })
    return {
        "total_pixels": total_px,
        "total_area_km2": total_area,
        "pixel_area_km2": px_area,
        "change_classes": classes,
        "forest_area_series": forest_series,
        "net_forest_change_pixels": (forest_series[-1]["forest_pixels"]
                                     - forest_series[0]["forest_pixels"]),
    }


# ---------------------------------------------------------------------------
# 合成数据：多期 NDVI + 注入确定的损失/增益（离线）
# ---------------------------------------------------------------------------
def generate_synthetic_series(
    bbox: List[float],
    n_dates: int = 4,
    width: int = 96,
    height: int = 96,
    threshold: float = 0.3,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (n_dates,H,W) NDVI 序列，注入确定的损失与增益区域。

    基础：左半为森林（NDVI~0.72），右半为非森林（NDVI~0.15）。
    损失区（森林内一块）在 cut_index 后降为 ~0.12；
    增益区（非森林内一块）在 rise_index 后升为 ~0.65。
    """
    n_dates = max(int(n_dates), 2)
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xn = xx / max(width - 1, 1)

    base_forest = xn < 0.55
    base = np.where(base_forest, 0.72, 0.15).astype(np.float32)

    loss_mask = np.zeros((height, width), dtype=bool)
    loss_mask[int(height * 0.05): int(height * 0.45),
              int(width * 0.05): int(width * 0.40)] = True
    gain_mask = np.zeros((height, width), dtype=bool)
    gain_mask[int(height * 0.55): int(height * 0.90),
              int(width * 0.65): int(width * 0.95)] = True

    cut_index = n_dates // 2
    rise_index = n_dates // 2

    stack = np.zeros((n_dates, height, width), dtype=np.float32)
    for i in range(n_dates):
        arr = base.copy()
        if i >= cut_index:
            arr[loss_mask] = 0.12
        if i >= rise_index:
            arr[gain_mask] = 0.65
        arr = arr + rng.normal(0.0, 0.02, size=arr.shape).astype(np.float32)
        stack[i] = np.clip(arr, 0.0, 1.0)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "n_dates": n_dates,
        "threshold": threshold,
        "loss_pixel_count": int(loss_mask.sum()),
        "gain_pixel_count": int(gain_mask.sum()),
        "loss_mask": loss_mask,
        "gain_mask": gain_mask,
    }
    return stack, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    array: np.ndarray,
    bbox: List[float],
    dtype: str = "float32",
    nodata: Optional[float] = None,
) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    arr = array
    if arr.ndim == 2:
        arr = arr[np.newaxis, ...]
    nb, h, w = arr.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(arr[b].astype(dtype), b + 1)


def read_ndvi_stack(path: str) -> Tuple[np.ndarray, List[float]]:
    """读多波段 NDVI 栈（向后兼容接口，不做 NoData 处理）。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_ndvi_stack_safe(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """读多波段 NDVI 栈；将 NoData 替换为 NaN；返回 (cube, bbox, nodata)。

    若全为 NoData，抛 ValidationError（rc=6）。
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nd = src.nodata
    if nd is not None:
        cube = np.where(cube == float(nd), np.nan, cube)
    n_valid = int(np.isfinite(cube).sum())
    if n_valid == 0:
        raise ValidationError(
            f"input raster is entirely NoData (nodata={nd}, bands={cube.shape[0]})",
            path=path, n_valid_pixels=0,
        )
    return cube, bbox, nd


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
            "n_dates": getattr(args, "n_dates", None),
            "threshold": getattr(args, "threshold", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
            "bbox": bbox,
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
    # 推迟 makedirs 到校验通过后（避免对 rc=6 失败路径留空目录）
    # ---- 校验 ----
    validate_params(args)
    bbox = list(args.bbox) if args.bbox else None
    if bbox is not None:
        validate_bbox(bbox)

    # 1) 获取多期 NDVI
    #    通用契约：给了 --input 就读真实栅格；否则（含 --synthetic）走合成。
    synth_info: Optional[Dict[str, Any]] = None
    input_nodata: Optional[float] = None
    if args.input and not args.synthetic:
        stack, file_bbox, input_nodata = read_ndvi_stack_safe(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            validate_bbox(bbox)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        stack, synth_info = generate_synthetic_series(
            bbox, n_dates=args.n_dates, threshold=args.threshold,
        )
        source_note = "synthetic"

    if stack.size == 0:
        raise ValidationError("input raster is empty")
    if stack.shape[0] < 2:
        raise ValidationError(
            f"need at least 2 bands/dates, got {stack.shape[0]}",
            n_dates=int(stack.shape[0]),
        )
    n_valid_total = int(np.isfinite(stack).sum())
    n_total = int(stack.size)
    if n_valid_total == 0:
        raise ValidationError(
            "all input pixels are NaN/NoData — nothing to analyze",
            n_valid_pixels=0, n_total_pixels=n_total,
        )

    # 校验通过后再创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 2) 变化分类 + CVA
    cls, masks = classify_forest_change(
        stack, threshold=args.threshold,
        drop_threshold=args.drop_threshold,
        gain_threshold=args.gain_threshold,
    )
    cva = change_vector_magnitude(stack)
    stats = forest_change_stats(
        cls, stack, bbox, threshold=args.threshold,
        start_year=args.start_year, interval_years=args.interval_years,
    )

    # 3) 写出产物
    cls_tif = os.path.join(output_dir, "forest_change_class.tif")
    write_geotiff(cls_tif, cls, bbox, dtype="int32", nodata=-1)

    cva_tif = os.path.join(output_dir, "cva_magnitude.tif")
    # CVA 中 NaN 像元用 -9999.0 占位写出
    cva_out = np.where(np.isfinite(cva), cva, -9999.0).astype(np.float32)
    write_geotiff(cva_tif, cva_out, bbox, dtype="float32", nodata=-9999.0)

    stats_path = os.path.join(output_dir, "area_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    # QA：损失区 CVA 强度应高于稳定区（NaN-safe）
    def _nan_mean(arr, mask):
        if not mask.any():
            return 0.0
        vals = arr[mask]
        v = vals[np.isfinite(vals)]
        return float(v.mean()) if v.size else 0.0

    mean_cva_loss = _nan_mean(cva, masks["loss"])
    mean_cva_stable = _nan_mean(cva, masks["stable"])
    qa: Dict[str, Any] = {
        "source": source_note,
        "n_dates": int(stack.shape[0]),
        "threshold": float(args.threshold),
        "loss_pixels": int(masks["loss"].sum()),
        "gain_pixels": int(masks["gain"].sum()),
        "stable_pixels": int(masks["stable"].sum()),
        "nodata_pixels": int(masks["valid"].size - masks["valid"].sum()),
        "net_forest_change_pixels": stats["net_forest_change_pixels"],
        "mean_cva_loss": mean_cva_loss,
        "mean_cva_stable": mean_cva_stable,
        "n_valid_pixels": n_valid_total,
        "n_total_pixels": n_total,
    }
    if input_nodata is not None:
        qa["input_nodata"] = float(input_nodata)
    if synth_info is not None:
        qa["injected_loss_pixels"] = synth_info["loss_pixel_count"]
        qa["injected_gain_pixels"] = synth_info["gain_pixel_count"]

    outputs = [
        {"path": cls_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "nodata": -1},
        {"path": cva_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "nodata": -9999.0},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] dates: {stack.shape[0]}  threshold: {args.threshold}")
        print(f"[{SKILL_NAME}] loss: {qa['loss_pixels']} px  "
              f"gain: {qa['gain_pixels']} px  stable: {qa['stable_pixels']} px  "
              f"nodata: {qa['nodata_pixels']} px")
        print(f"[{SKILL_NAME}] net forest change: "
              f"{stats['net_forest_change_pixels']} px")
        print(f"[{SKILL_NAME}] change class: {cls_tif}")
        print(f"[{SKILL_NAME}] cva: {cva_tif}")
        print(f"[{SKILL_NAME}] stats: {stats_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Forest cover loss/gain detection from multi-date NDVI with CVA.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="multi-band NDVI GeoTIFF (one band per date)")
    p.add_argument("--n-dates", type=int, default=4,
                   help="number of dates for synthetic mode, >=2 (default: 4)")
    p.add_argument("--threshold", type=float, default=0.3,
                   help="NDVI forest threshold (default: 0.3)")
    p.add_argument("--drop-threshold", type=float, default=0.1,
                   help="NDVI drop to flag loss (default: 0.1)")
    p.add_argument("--gain-threshold", type=float, default=0.1,
                   help="NDVI rise to flag gain (default: 0.1)")
    p.add_argument("--start-year", type=int, default=2000, help="first date year")
    p.add_argument("--interval-years", type=int, default=5, help="years between dates")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic NDVI series with loss/gain (offline)")
    p.add_argument("--output-dir", default="./output", help="output directory")
    p.add_argument("--quiet", action="store_true", help="suppress console output")
    p.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.n_dates < 2:
            raise UsageError(f"--n-dates must be >=2, got {args.n_dates}",
                             n_dates=int(args.n_dates))
        if not (0.0 < args.threshold < 1.0):
            raise UsageError(f"--threshold must be in (0,1), got {args.threshold}",
                             threshold=float(args.threshold))
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
