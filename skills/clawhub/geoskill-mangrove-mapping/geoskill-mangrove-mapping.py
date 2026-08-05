#!/usr/bin/env python3
"""mangrove-mapping — 红树林制图

融合多光谱与 SAR 特征提取红树林分布。红树林生长在热带/亚热带海岸潮间带，
具有四个可遥感识别的特征：

- **NDVI 高值**：茂密常绿植被，近红外高反射、红光低反射，NDVI 通常 > 0.5。
- **NDWI 边界**：红树林位于水陆交界，用 McFeeters NDWI=(Green−NIR)/(Green+NIR)
  定位水体，再用距离变换得到每个陆地像元到海岸线的距离。
- **海岸缓冲**：红树林只出现在距海岸线一定缓冲范围内（潮间带）。
- **SAR 潮汐影响**：潮间带淹水使树干产生多次散射，SAR 后向散射偏亮，
  可与开阔水面（暗）和陆域植被区分。

算法把上述特征转成 [0,1] 的隶属度并做规则融合（乘积 + SAR 调制），
阈值化得到红树林掩膜。支持多期输入做红树林变化（增益/损失）检测。

数据源：本地多波段 GeoTIFF（波段顺序 green/red/nir/swir[/sar]），
或 ``--synthetic`` 生成物理一致的海岸带模拟场景（离线）。

隐私声明 / Privacy：
- 默认离线运行，不访问任何网络服务。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python mangrove-mapping.py --input scene.tif --output-dir ./out
    python mangrove-mapping.py --bbox 110 21 111 22 --synthetic --output-dir ./out

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
SKILL_NAME = "mangrove-mapping"

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
# 融合阈值（隶属度函数参数，公开经验值）
# ---------------------------------------------------------------------------
NDVI_VEG_LO = 0.30          # NDVI 植被隶属度下界
NDVI_VEG_HI = 0.50          # NDVI 植被隶属度上界
COAST_INNER_PX = 1.0        # 海岸缓冲内界（像元）
COAST_OUTER_PX = 15.0       # 海岸缓冲外界（像元）
WATER_NDWI_THRESH = 0.0     # NDWI > 此值判为水体
SAR_TARGET = 0.35           # 红树林 SAR 后向散射目标（线性）
SAR_WIDTH = 0.18            # SAR 隶属度高斯宽度
SAR_WEIGHT = 0.40           # SAR 调制权重
SCORE_THRESHOLD = 0.45      # 融合得分阈值

# 输入波段顺序（1-indexed）
BAND_GREEN, BAND_RED, BAND_NIR, BAND_SWIR, BAND_SAR = 0, 1, 2, 3, 4


def validate_bbox(bbox) -> None:
    """校验 bbox 是 W<E、S<N、lon∈[-180,180]、lat∈[-90,90]、非零面积。
    跨 180° 经线必须拆成两个子 bbox。"""
    if bbox is None:
        raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range [-180, 180]: W={w}, E={e}",
            bbox=list(bbox),
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range [-90, 90]: S={s}, N={n}",
            bbox=list(bbox),
        )
    if w >= e:
        if w == e:
            raise ValidationError(
                f"bbox has zero width: W==E=={w} (degenerate AOI)",
                bbox=list(bbox),
            )
        raise ValidationError(
            f"bbox is reversed (W={w} >= E={e}); need W < E. "
            f"For datelines that cross 180° (e.g. 179.5 -> -179.5), "
            f"split into two sub-bboxes and run the skill on each separately.",
            bbox=list(bbox),
        )
    if s >= n:
        raise ValidationError(
            f"bbox is reversed (S={s} >= N={n}); need S < N",
            bbox=list(bbox),
        )


def validate_threshold(value: float, name: str) -> None:
    """校验阈值在 [0, 1] 区间。"""
    if not np.isfinite(value):
        raise ValidationError(f"{name} must be a finite number, got {value!r}",
                              **{name: float(value)})
    if not (0.0 <= value <= 1.0):
        raise ValidationError(
            f"{name} must be in [0, 1], got {value}",
            **{name: float(value)},
        )


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 光谱指数
# ---------------------------------------------------------------------------
def ndvi_index(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
    """归一化植被指数 NDVI = (NIR − Red) / (NIR + Red)，范围 [−1, 1]。"""
    nir = nir.astype(np.float32)
    red = red.astype(np.float32)
    denom = nir + red
    out = np.zeros_like(denom, dtype=np.float32)
    valid = denom != 0
    out[valid] = (nir[valid] - red[valid]) / denom[valid]
    return np.clip(out, -1.0, 1.0)


def ndwi_index(green: np.ndarray, nir: np.ndarray) -> np.ndarray:
    """McFeeters 归一化水体指数 NDWI = (Green − NIR) / (Green + NIR)。"""
    green = green.astype(np.float32)
    nir = nir.astype(np.float32)
    denom = green + nir
    out = np.zeros_like(denom, dtype=np.float32)
    valid = denom != 0
    out[valid] = (green[valid] - nir[valid]) / denom[valid]
    return np.clip(out, -1.0, 1.0)


def derive_water_mask(ndwi: np.ndarray, threshold: float = WATER_NDWI_THRESH) -> np.ndarray:
    """由 NDWI 阈值提取水体掩膜（True = 水）。"""
    return ndwi > threshold


def coast_distance_px(water: np.ndarray) -> np.ndarray:
    """每个陆地像元到最近水体（海岸线）的欧氏距离，单位：像元。

    水体像元距离为 0。用 scipy 距离变换实现。
    """
    from scipy.ndimage import distance_transform_edt
    land = ~water.astype(bool)
    return distance_transform_edt(land).astype(np.float32)


def _ramp(x: np.ndarray, lo: float, hi: float) -> np.ndarray:
    """线性隶属度：< lo → 0，> hi → 1，之间线性。"""
    if hi <= lo:
        return (x > lo).astype(np.float32)
    return np.clip((x - lo) / (hi - lo), 0.0, 1.0).astype(np.float32)


def mangrove_score(
    ndvi: np.ndarray,
    coast_dist: np.ndarray,
    sar: Optional[np.ndarray] = None,
    score_threshold: float = SCORE_THRESHOLD,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """规则融合计算红树林得分。

    score = veg_membership × coast_membership × (1 − w + w × tidal_membership)

    返回 (mask, score, components)。components 含各隶属度均值，便于诊断。
    """
    veg = _ramp(ndvi, NDVI_VEG_LO, NDVI_VEG_HI)
    coast = 1.0 - _ramp(coast_dist, COAST_INNER_PX, COAST_OUTER_PX)

    if sar is not None:
        tidal = np.exp(-((sar.astype(np.float32) - SAR_TARGET) / SAR_WIDTH) ** 2)
        tidal = np.clip(tidal, 0.0, 1.0).astype(np.float32)
        modulator = (1.0 - SAR_WEIGHT) + SAR_WEIGHT * tidal
    else:
        tidal = np.ones_like(veg)
        modulator = np.ones_like(veg)

    score = (veg * coast * modulator).astype(np.float32)
    mask = score > score_threshold
    components = {
        "mean_veg_membership": float(np.mean(veg)),
        "mean_coast_membership": float(np.mean(coast)),
        "mean_tidal_membership": float(np.mean(tidal)),
        "sar_used": sar is not None,
    }
    return mask, score, components


def extract_mangroves(
    cube: np.ndarray,
    score_threshold: float = SCORE_THRESHOLD,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any], Dict[str, Any]]:
    """从多波段立方体提取红树林。

    输入 cube 形状 (bands, H, W)，波段顺序 green/red/nir/swir[/sar]。
    返回 (mask, score, indices_dict, components_dict)。
    """
    if cube.ndim != 3 or cube.shape[0] < 4:
        raise ValidationError(
            f"input needs >=4 bands (green/red/nir/swir), got shape {cube.shape}",
            shape=str(cube.shape),
        )
    green = cube[BAND_GREEN].astype(np.float32)
    red = cube[BAND_RED].astype(np.float32)
    nir = cube[BAND_NIR].astype(np.float32)
    sar = cube[BAND_SAR].astype(np.float32) if cube.shape[0] >= 5 else None

    ndvi = ndvi_index(nir, red)
    ndwi = ndwi_index(green, nir)
    water = derive_water_mask(ndwi)
    coast_dist = coast_distance_px(water)

    mask, score, components = mangrove_score(ndvi, coast_dist, sar, score_threshold)
    indices = {
        "ndvi": ndvi,
        "ndwi": ndwi,
        "water": water.astype(np.float32),
        "coast_distance": coast_dist,
    }
    return mask, score, indices, components


# ---------------------------------------------------------------------------
# 多期变化
# ---------------------------------------------------------------------------
def mangrove_change(
    mask_t0: np.ndarray,
    mask_t1: np.ndarray,
    pixel_area_m2: float = 1.0,
) -> Dict[str, Any]:
    """比较两期红树林掩膜，统计增益/损失/持续面积。"""
    m0 = mask_t0.astype(bool)
    m1 = mask_t1.astype(bool)
    persist = np.logical_and(m0, m1)
    gain = np.logical_and(~m0, m1)
    loss = np.logical_and(m0, ~m1)
    return {
        "area_t0_m2": float(m0.sum()) * pixel_area_m2,
        "area_t1_m2": float(m1.sum()) * pixel_area_m2,
        "persist_m2": float(persist.sum()) * pixel_area_m2,
        "gain_m2": float(gain.sum()) * pixel_area_m2,
        "loss_m2": float(loss.sum()) * pixel_area_m2,
        "net_change_m2": float(m1.sum() - m0.sum()) * pixel_area_m2,
        "persist_px": int(persist.sum()),
        "gain_px": int(gain.sum()),
        "loss_px": int(loss.sum()),
    }


# ---------------------------------------------------------------------------
# 面积换算
# ---------------------------------------------------------------------------
def pixel_area_m2(bbox: List[float], height: int, width: int) -> float:
    """由 bbox（W S E N，经纬度）与栅格尺寸估算单个像元面积（m²）。"""
    lat0 = (bbox[1] + bbox[3]) / 2.0
    x_m = (bbox[2] - bbox[0]) * 111320.0 * np.cos(np.deg2rad(lat0)) / max(width, 1)
    y_m = (bbox[3] - bbox[1]) * 110540.0 / max(height, 1)
    return float(abs(x_m * y_m))


# ---------------------------------------------------------------------------
# 合成数据：物理一致的海岸带场景（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic_scene(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    seed: int = 42,
    epoch: int = 0,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成一个 (5, H, W) 的海岸带场景：green/red/nir/swir/sar。

    场景布局：左侧为海洋，右侧为陆地，波浪状海岸线。陆地上有：
    - 紧邻海岸的红树林带（高 NDVI + 亮 SAR 多次散射）——随 epoch 退缩；
    - 远岸的陆域植被（高 NDVI，远离海岸）；
    - 近岸裸质潮滩（低 NDVI）。
    返回 (cube, truth_mangrove_mask, info)。
    """
    rng = np.random.default_rng(seed + epoch)
    yy, xx = np.mgrid[0:height, 0:width]
    yyn = yy.astype(np.float32) / max(height - 1, 1)
    xxn = xx.astype(np.float32) / max(width - 1, 1)

    # 波浪状海岸线（水体在左侧）
    coast_x = 0.38 + 0.04 * np.sin(2.0 * np.pi * yyn * 2.0)
    water = xxn < coast_x

    # 红树林带宽度随 epoch 退缩（模拟退化/损失）
    mang_width = max(0.02, 0.075 - 0.020 * epoch)
    mang_segment = (yyn > 0.25) & (yyn < 0.75)
    mangrove = (
        (xxn >= coast_x) & (xxn <= coast_x + mang_width) & mang_segment
    )
    upland = (xxn > 0.70)

    green = np.full((height, width), 0.14, dtype=np.float32)
    red = np.full((height, width), 0.18, dtype=np.float32)
    nir = np.full((height, width), 0.20, dtype=np.float32)
    swir = np.full((height, width), 0.25, dtype=np.float32)
    sar = np.full((height, width), 0.10, dtype=np.float32)

    # 水体
    green[water] = 0.06; red[water] = 0.03; nir[water] = 0.015
    swir[water] = 0.005; sar[water] = 0.03
    # 陆域植被
    green[upland] = 0.09; red[upland] = 0.04; nir[upland] = 0.45
    swir[upland] = 0.20; sar[upland] = 0.15
    # 红树林（高 NDVI + 亮 SAR）
    green[mangrove] = 0.10; red[mangrove] = 0.05; nir[mangrove] = 0.40
    swir[mangrove] = 0.18; sar[mangrove] = 0.35

    noise = rng.normal(0, 0.006, size=(height, width)).astype(np.float32)
    green = np.clip(green + noise, 0, 1)
    red = np.clip(red + noise, 0, 1)
    nir = np.clip(nir + noise, 0, 1)
    swir = np.clip(swir + noise, 0, 1)
    sar = np.clip(sar + rng.normal(0, 0.01, size=(height, width)).astype(np.float32), 0, 1)

    cube = np.stack([green, red, nir, swir, sar], axis=0).astype(np.float32)
    truth = mangrove.astype(np.uint8)
    info = {
        "bbox": bbox, "width": width, "height": height, "epoch": epoch,
        "mangrove_width_frac": float(mang_width),
        "truth_mangrove_px": int(truth.sum()),
    }
    return cube, truth, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0) -> None:
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
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox) -> Optional[str]:
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
            "n_dates": int(getattr(args, "n_dates", 1)),
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

    # 1) 参数前置校验
    validate_threshold(args.score_threshold, "--score-threshold")
    if args.n_dates < 1:
        raise ValidationError(
            f"--n-dates must be >= 1, got {args.n_dates}",
            n_dates=int(args.n_dates),
        )

    bbox = list(args.bbox) if args.bbox else None

    # 2) 获取数据 —— 通用契约
    synth_info: Optional[Dict[str, Any]] = None
    scenes: List[np.ndarray] = []
    truths: List[np.ndarray] = []
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        validate_bbox(bbox)
        scenes.append(cube)
        source_note = args.input
    else:
        validate_bbox(bbox)
        for ep in range(args.n_dates):
            cube, truth, info = generate_synthetic_scene(bbox, epoch=ep)
            scenes.append(cube)
            truths.append(truth)
            synth_info = info
        source_note = "synthetic"

    if scenes[0].size == 0:
        raise ValidationError("input raster is empty")
    if scenes[0].ndim != 3 or scenes[0].shape[0] < 4:
        raise ValidationError(
            f"input needs >=4 bands (green/red/nir/swir), got shape {scenes[0].shape}"
        )

    # 校验通过后再建输出目录
    os.makedirs(output_dir, exist_ok=True)

    h, w = scenes[0].shape[1], scenes[0].shape[2]
    px_area = pixel_area_m2(bbox, h, w)

    # 2) 逐期提取红树林
    masks: List[np.ndarray] = []
    scores: List[np.ndarray] = []
    for cube in scenes:
        mask, score, indices, components = extract_mangroves(cube, args.score_threshold)
        masks.append(mask)
        scores.append(score)

    # 3) 写出末期红树林掩膜 + 得分
    out_tif = os.path.join(output_dir, "mangrove.tif")
    last_mask = masks[-1].astype(np.float32)
    write_geotiff(out_tif, last_mask, bbox, nodata=-9999.0)

    score_tif = os.path.join(output_dir, "mangrove_score.tif")
    write_geotiff(score_tif, scores[-1], bbox, nodata=-9999.0)

    # 面积统计
    px_count = int(masks[-1].sum())
    area_m2 = px_count * px_area
    stats = {
        "mangrove_pixels": px_count,
        "pixel_area_m2": px_area,
        "mangrove_area_m2": area_m2,
        "mangrove_area_ha": area_m2 / 10000.0,
        "mangrove_area_km2": area_m2 / 1e6,
        "n_dates": len(scenes),
        "components": components,
    }

    change = None
    if len(masks) >= 2:
        change = mangrove_change(masks[0], masks[-1], px_area)
        stats["change_first_to_last"] = change
        change_tif = os.path.join(output_dir, "mangrove_change.tif")
        # 1=持续, 2=增益, 3=损失
        chg = np.zeros_like(last_mask, dtype=np.float32)
        chg[np.logical_and(masks[0], masks[-1])] = 1
        chg[np.logical_and(~masks[0].astype(bool), masks[-1])] = 2
        chg[np.logical_and(masks[0], ~masks[-1].astype(bool))] = 3
        write_geotiff(change_tif, chg, bbox, nodata=-9999.0)

    stats_path = os.path.join(output_dir, "mangrove_area.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_dates": len(scenes),
        "mangrove_area_ha": stats["mangrove_area_ha"],
        "mean_score": float(np.mean(scores[-1])),
    }
    if change is not None:
        qa["net_change_ha"] = change["net_change_m2"] / 10000.0
    if synth_info is not None and truths:
        # 与真值一致性（IoU）
        pred = masks[-1].astype(bool)
        gt = truths[-1].astype(bool)
        inter = float(np.logical_and(pred, gt).sum())
        union = float(np.logical_or(pred, gt).sum())
        qa["synthetic_truth_iou"] = (inter / union) if union > 0 else 0.0

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": score_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]
    if change is not None:
        outputs.append({"path": os.path.join(output_dir, "mangrove_change.tif"),
                        "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox,
                        "band_count": 1})

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] dates: {len(scenes)}  shape: {scenes[0].shape[1:]}")
        print(f"[{SKILL_NAME}] mangrove: {px_count} px  {stats['mangrove_area_ha']:.2f} ha")
        if change is not None:
            print(f"[{SKILL_NAME}] net change: {change['net_change_m2']/10000.0:.2f} ha "
                  f"(gain {change['gain_m2']/10000.0:.2f} / loss {change['loss_m2']/10000.0:.2f})")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Mangrove mapping by fusing NDVI / NDWI coast buffer / SAR tidal signatures.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multi-band GeoTIFF (green/red/nir/swir[/sar])")
    p.add_argument("--n-dates", type=int, default=1,
                   help="number of synthetic epochs for change detection (default: 1)")
    p.add_argument("--score-threshold", type=float, default=SCORE_THRESHOLD,
                   help=f"fusion score threshold (default: {SCORE_THRESHOLD})")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent coastal scene (offline)")
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
