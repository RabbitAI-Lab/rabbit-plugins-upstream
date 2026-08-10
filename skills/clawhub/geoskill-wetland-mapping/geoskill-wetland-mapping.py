#!/usr/bin/env python3
"""wetland-mapping — 湿地制图

多源融合的湿地类型制图。把四个物理量组合成逐像元特征：

- **NDWI / MNDWI**：水体指数，开放水域高、陆地低；
- **NDVI**：植被指数，沼泽植被高、开阔水与滩涂低；
- **DEM（归一化低洼度）**：地形，湿地多处于低洼处；
- **SAR 后向散射 σ⁰**：水面镜面反射、后向散射低。

按规则/阈值决策树分类为：开放水域（water）、沼泽（swamp）、
滩涂（mudflat）与非湿地（non_wetland），优先级 water > swamp > mudflat。
输出湿地类型栅格与逐类面积统计 JSON。合成模式生成含四类湿地的
多源数据（NDWI/NDVI/DEM/SAR），分类结果与注入真值高度一致。

真实输入约定：``--input`` 为 4 波段 GeoTIFF，波段顺序
[NDWI, NDVI, DEM, SAR(dB)]；DEM 会被自动归一化到 [0,1]。

隐私声明 / Privacy：
- 默认离线运行，不访问任何网络服务。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python wetland-mapping.py --input fused_4band.tif --output-dir ./out
    python wetland-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "wetland-mapping"

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


# 波段索引与类别编码
BAND_NDWI, BAND_NDVI, BAND_DEM, BAND_SAR = 0, 1, 2, 3
CLASS_NAMES = {0: "non_wetland", 1: "water", 2: "swamp", 3: "mudflat"}

DEFAULT_THRESHOLDS: Dict[str, float] = {
    "ndwi_water": 0.40,   # 开放水域 NDWI 下限
    "sar_water": -16.0,   # 开放水域 SAR σ⁰ 上限 (dB)
    "ndvi_veg": 0.30,     # 沼泽植被 NDVI 下限
    "elev_wet": 0.40,     # 低洼湿地 DEM(归一化) 上限
    "ndwi_moist": 0.00,   # 沼泽湿润 NDWI 下限
    "sar_wet": -10.0,     # 湿润湿地 SAR σ⁰ 上限 (dB)
    "ndwi_damp": -0.05,   # 滩涂潮湿 NDWI 下限
}


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


def _pixel_area_km2(bbox: List[float], shape: Tuple[int, int]) -> Tuple[float, float]:
    h, w = shape
    lat_mid = (bbox[1] + bbox[3]) / 2.0
    km_px_x = (bbox[2] - bbox[0]) / max(w, 1) * 111.32 * math.cos(math.radians(lat_mid))
    km_px_y = (bbox[3] - bbox[1]) / max(h, 1) * 110.57
    return km_px_x * km_px_y, float(km_px_x * km_px_y * h * w)


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def normalize_dem(dem: np.ndarray) -> np.ndarray:
    """把 DEM 线性归一化到 [0, 1]（0=最低洼，1=最高）。常数返回全 0。"""
    d = np.asarray(dem, dtype=np.float64)
    lo = float(np.nanmin(d)) if d.size else 0.0
    hi = float(np.nanmax(d)) if d.size else 0.0
    if hi - lo < 1e-12:
        return np.zeros(d.shape, dtype=np.float32)
    return ((d - lo) / (hi - lo)).astype(np.float32)


def classify_wetland(
    cube: np.ndarray,
    thresholds: Optional[Dict[str, float]] = None,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """多源融合规则分类湿地类型。

    参数 cube: (4, H, W)，波段顺序 [NDWI, NDVI, DEM(归一化), SAR(dB)]。
    返回 (class_map (H,W) int32, info)。
    编码：0=non_wetland, 1=water, 2=swamp, 3=mudflat。
    """
    cube = np.asarray(cube, dtype=np.float32)
    if cube.ndim != 3:
        raise ValidationError(
            f"cube must be 3-D (4,H,W), got ndim={cube.ndim}", ndim=int(cube.ndim))
    if cube.shape[0] < 4:
        raise ValidationError(
            f"need 4 bands [NDWI,NDVI,DEM,SAR], got {cube.shape[0]}",
            bands=int(cube.shape[0]),
        )
    th = dict(DEFAULT_THRESHOLDS)
    if thresholds:
        th.update(thresholds)

    ndwi = cube[BAND_NDWI]
    ndvi = cube[BAND_NDVI]
    elev = cube[BAND_DEM]
    sar = cube[BAND_SAR]

    water = (ndwi >= th["ndwi_water"]) & (sar <= th["sar_water"])
    wet_low = elev <= th["elev_wet"]
    veg = ndvi >= th["ndvi_veg"]
    moist = ndwi >= th["ndwi_moist"]
    wet_sar = sar <= th["sar_wet"]
    damp = ndwi >= th["ndwi_damp"]

    swamp = (~water) & veg & (wet_low | moist) & wet_sar
    mudflat = (~water) & (~swamp) & (~veg) & wet_low & damp & wet_sar

    cls = np.zeros(cube.shape[1:], dtype=np.int32)
    cls[mudflat] = 3
    cls[swamp] = 2
    cls[water] = 1

    info = {
        "thresholds": th,
        "masks": {
            "water": water, "swamp": swamp,
            "mudflat": mudflat, "non_wetland": ~(water | swamp | mudflat),
        },
    }
    return cls, info


def wetland_area_stats(cls: np.ndarray, bbox: List[float],
                        valid_mask: Optional[np.ndarray] = None) -> Dict[str, Any]:
    """逐类像元数、占比与面积（km²），以及湿地总面积占比。

    若给定 valid_mask，则只统计 valid 像元（其它 NoData 不计入任何类）。
    像元面积仍用 cls.shape 的 (H, W) 计算（bbox 决定）。
    """
    px_area, total_area = _pixel_area_km2(bbox, cls.shape)
    if valid_mask is not None:
        cls_for_stats = cls[valid_mask]
    else:
        cls_for_stats = cls
    total_px = int(cls_for_stats.size)
    classes = []
    for code in (0, 1, 2, 3):
        cnt = int((cls_for_stats == code).sum())
        classes.append({
            "code": code,
            "name": CLASS_NAMES[code],
            "pixel_count": cnt,
            "fraction": cnt / total_px if total_px else 0.0,
            "area_km2": cnt * px_area,
        })
    wet_px = int((cls_for_stats > 0).sum())
    return {
        "total_pixels": total_px,
        "total_area_km2": total_area,
        "pixel_area_km2": px_area,
        "classes": classes,
        "wetland_pixels": wet_px,
        "wetland_fraction": wet_px / total_px if total_px else 0.0,
        "wetland_area_km2": wet_px * px_area,
    }


def classification_accuracy(pred: np.ndarray, truth: np.ndarray) -> Dict[str, Any]:
    """总体精度与逐类召回（供合成模式 QA 使用）。"""
    pred = np.asarray(pred).ravel()
    truth = np.asarray(truth).ravel()
    total = pred.size
    correct = int((pred == truth).sum())
    per_class = {}
    for code in (0, 1, 2, 3):
        gt = truth == code
        if gt.any():
            per_class[CLASS_NAMES[code]] = float((pred[gt] == code).mean())
        else:
            per_class[CLASS_NAMES[code]] = None
    return {
        "overall_accuracy": correct / total if total else 0.0,
        "per_class_recall": per_class,
        "total_pixels": int(total),
    }


# ---------------------------------------------------------------------------
# 合成数据：含四类湿地的多源场景（离线）
# ---------------------------------------------------------------------------
# 各波段在四类地物上的典型取值 [NDWI, NDVI, DEM_norm, SAR_dB]
_SYNTH_SIGNATURES: Dict[str, List[float]] = {
    "water":       [0.60, 0.05, 0.10, -20.0],
    "swamp":       [0.15, 0.55, 0.25, -12.0],
    "mudflat":     [0.05, 0.10, 0.20, -15.0],
    "non_wetland": [-0.20, 0.35, 0.80, -6.0],
}
_SYNTH_CODE = {"non_wetland": 0, "water": 1, "swamp": 2, "mudflat": 3}
# 各波段噪声标准差
_SYNTH_NOISE = [0.02, 0.02, 0.02, 0.5]


def generate_synthetic(
    bbox: List[float],
    width: int = 96,
    height: int = 96,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 (4,H,W) 多源立方体 + (H,W) 真值类别。

    空间布局：中央开放水域，环绕沼泽，外侧滩涂带，其余为非湿地高地。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    cx, cy = width * 0.5, height * 0.5
    r = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    rmax = 0.5 * min(width, height)

    truth = np.zeros((height, width), dtype=np.int32)  # 默认非湿地
    mudflat_zone = r <= 0.80 * rmax
    swamp_zone = r <= 0.55 * rmax
    water_zone = r <= 0.28 * rmax
    truth[mudflat_zone] = _SYNTH_CODE["mudflat"]
    truth[swamp_zone] = _SYNTH_CODE["swamp"]
    truth[water_zone] = _SYNTH_CODE["water"]

    inv_code = {v: k for k, v in _SYNTH_CODE.items()}
    cube = np.zeros((4, height, width), dtype=np.float32)
    for code in range(4):
        mask = truth == code
        sig = _SYNTH_SIGNATURES[inv_code[code]]
        for b in range(4):
            vals = sig[b] + rng.normal(0.0, _SYNTH_NOISE[b],
                                       size=(height, width)).astype(np.float32)
            cube[b][mask] = vals[mask]

    # 物理合理范围裁剪
    cube[BAND_NDWI] = np.clip(cube[BAND_NDWI], -1.0, 1.0)
    cube[BAND_NDVI] = np.clip(cube[BAND_NDVI], -1.0, 1.0)
    cube[BAND_DEM] = np.clip(cube[BAND_DEM], 0.0, 1.0)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "band_order": ["NDWI", "NDVI", "DEM_normalized", "SAR_dB"],
        "truth_pixel_counts": {
            inv_code[c]: int((truth == c).sum()) for c in range(4)
        },
    }
    return cube, truth, info


# ---------------------------------------------------------------------------
# 参数校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Optional[List[float]]) -> List[float]:
    """校验 [W, S, E, N]：W<E、S<N、范围合法；跨 180°给拆分提示。"""
    if bbox is None or len(bbox) != 4:
        raise UsageError(
            "bbox must be 4 floats [W S E N], got: " + repr(bbox),
            bbox=bbox,
        )
    w, s, e, n = bbox
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError(
            f"bbox must contain finite floats, got {bbox}", bbox=bbox)
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of [-180, 180]: W={w} E={e}", bbox=bbox)
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of [-90, 90]: S={s} N={n}", bbox=bbox)
    if s >= n:
        raise ValidationError(
            f"bbox South >= North: S={s} N={n}", bbox=bbox)
    if w > e:
        raise ValidationError(
            f"bbox crosses the 180° meridian (W={w} > E={e}); "
            f"please split the extent or wrap longitudes manually",
            bbox=bbox)
    if abs(e - w) < 1e-9 or abs(n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero area: W={w} E={e} S={s} N={n}", bbox=bbox)
    return [float(w), float(s), float(e), float(n)]


def read_cube_with_nodata(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """读多波段 GeoTIFF 并把 nodata 标记的像元替换为 NaN；同时返回原 nodata。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    return cube, bbox, nodata


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


def read_cube(path: str) -> Tuple[np.ndarray, List[float]]:
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

    bbox_in = list(args.bbox) if args.bbox else None

    # 1) 获取多源数据立方体
    #    通用契约：给了 --input 就读真实栅格；否则（含 --synthetic）走合成。
    synth_info: Optional[Dict[str, Any]] = None
    truth: Optional[np.ndarray] = None
    if args.input and not args.synthetic:
        cube, file_bbox, _nd = read_cube_with_nodata(args.input)
        if cube.shape[0] < 4:
            raise ValidationError(
                f"input needs 4 bands [NDWI, NDVI, DEM, SAR], got {cube.shape[0]}",
                bands=int(cube.shape[0]))
        bbox = validate_bbox(bbox_in) if bbox_in is not None else validate_bbox(file_bbox)
        cube[BAND_DEM] = normalize_dem(cube[BAND_DEM])
        source_note = args.input
    else:
        bbox = validate_bbox(bbox_in)
        cube, truth, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    # QA 计数：有效像元（4 波段都 finite）
    n_valid_4band = int(np.isfinite(cube).all(axis=0).sum())
    n_total = int(cube.shape[1] * cube.shape[2])
    if n_valid_4band == 0:
        raise ValidationError(
            f"input raster has no valid pixels across all 4 bands (n_total={n_total})",
            n_total=n_total)

    # 校验通过后再创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 2) 融合分类
    cls, cinfo = classify_wetland(cube)

    # NaN/部分 NoData 像元 → 输出 nodata=-1（不再计入任何类别）
    valid_mask = np.isfinite(cube).all(axis=0)
    cls_out = cls.copy()
    cls_out[~valid_mask] = -1

    # 面积统计：仅基于有效像元；用完整 cls.shape 算像元面积
    stats = wetland_area_stats(cls, bbox, valid_mask=valid_mask)
    stats["n_valid_pixels"] = int(valid_mask.sum())
    stats["n_total_pixels"] = n_total
    stats["nodata_pixels"] = int((~valid_mask).sum())

    # 3) 写出产物
    cls_tif = os.path.join(output_dir, "wetland_class.tif")
    write_geotiff(cls_tif, cls_out, bbox, dtype="int32", nodata=-1)

    stats_path = os.path.join(output_dir, "area_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "wetland_fraction": stats["wetland_fraction"],
        "wetland_area_km2": stats["wetland_area_km2"],
        "class_fractions": {c["name"]: c["fraction"] for c in stats["classes"]},
        "n_total_pixels": n_total,
        "n_valid_pixels": int(valid_mask.sum()),
    }
    if truth is not None:
        qa["synthetic_accuracy"] = classification_accuracy(cls, truth)
        qa["synthetic_truth_counts"] = synth_info["truth_pixel_counts"]

    outputs = [
        {"path": cls_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "nodata": -1},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] wetland fraction: {stats['wetland_fraction']*100:.2f}%")
        for c in stats["classes"]:
            print(f"[{SKILL_NAME}]   {c['name']:12s} {c['fraction']*100:6.2f}%  "
                  f"{c['area_km2']:.4f} km²")
        if "synthetic_accuracy" in qa:
            print(f"[{SKILL_NAME}] synthetic OA: "
                  f"{qa['synthetic_accuracy']['overall_accuracy']:.4f}")
        print(f"[{SKILL_NAME}] class map: {cls_tif}")
        print(f"[{SKILL_NAME}] stats: {stats_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Multi-source wetland type mapping (NDWI + NDVI + DEM + SAR).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input",
                   help="4-band GeoTIFF [NDWI, NDVI, DEM, SAR(dB)]")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic multi-source scene (offline)")
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
