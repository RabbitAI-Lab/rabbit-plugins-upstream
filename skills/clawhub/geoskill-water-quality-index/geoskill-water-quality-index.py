#!/usr/bin/env python3
"""water-quality-index — 水质遥感指数

基于水色遥感经验模型从多光谱影像反演水体叶绿素 a、悬浮物浓度与透明度，
做水体掩膜（NDWI）与富营养化分级。核心内容：

- **叶绿素 a（OC3）**：NASA OC3 四次多项式，log10(chl) = Σ aᵢ·[log10(blue/green)]ⁱ。
- **悬浮物 TSS**：红波段经验反演，基于水体后向散射—吸收（Gordon）关系的解析逆。
- **透明度 Secchi**：与 chl、TSS 负相关的经验模型。
- **水体掩膜**：NDWI = (green − nir)/(green + nir)，阈值分割水/陆。
- **富营养化分级**：按叶绿素 a 浓度分贫/中/富/超富营养四级。

输入：本地多光谱 GeoTIFF（band1=蓝, band2=绿, band3=红, band4=近红外，反射率），
或 ``--synthetic`` 生成含不同 chl/TSS 的水体影像用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，无网络访问。``--synthetic`` 完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python water-quality-index.py --bbox 116 39 117 40 --synthetic
    python water-quality-index.py --bbox 116 39 117 40 --parameters chl_a,tss --synthetic

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
SKILL_NAME = "water-quality-index"

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
# 光学参数：纯水吸收 aw、纯水后向散射 bbw、叶绿素比吸收 a_ph、沉积物比散射 b_sed
# 波段顺序：蓝(0.49) 绿(0.56) 红(0.66) 近红外(0.86)
# ---------------------------------------------------------------------------
AW = np.array([0.015, 0.060, 0.080, 0.400], dtype=np.float64)
BBW = np.array([0.0022, 0.0020, 0.0018, 0.0016], dtype=np.float64)
A_PH = np.array([0.010, 0.004, 0.000, 0.000], dtype=np.float64)   # 红/近红外不吸收（解耦 TSS）
B_SED = np.array([0.0009, 0.0009, 0.0009, 0.0003], dtype=np.float64)  # 可见光近似平坦

# NASA OC3 系数（MODIS/Aqua，公开领域）
OC3_COEF = np.array([0.2424, -2.7423, 1.8017, 0.0015, -1.2280], dtype=np.float64)


# ---------------------------------------------------------------------------
# 前向水体反射率模型（Gordon 简化）：用于合成影像
# ---------------------------------------------------------------------------
def forward_rrs(chl: np.ndarray, tss: np.ndarray) -> np.ndarray:
    """由 chl(mg/m³)、TSS(g/m³) 生成 4 波段离水反射率 Rrs。

    Rrs(λ) ≈ 0.5 · bb(λ) / (a(λ) + bb(λ))。返回 (4, ...) 与输入同形。
    """
    chl = np.asarray(chl, dtype=np.float64)
    tss = np.asarray(tss, dtype=np.float64)
    shape = (4,) + chl.shape
    a = np.zeros(shape, dtype=np.float64)
    bb = np.zeros(shape, dtype=np.float64)
    for b in range(4):
        a[b] = AW[b] + A_PH[b] * chl
        bb[b] = BBW[b] + B_SED[b] * tss
    rrs = 0.5 * bb / (a + bb)
    return np.clip(rrs, 0.0, None)


# ---------------------------------------------------------------------------
# 核心算法 1：水体掩膜（NDWI）
# ---------------------------------------------------------------------------
def ndwi(green: np.ndarray, nir: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """归一化差异水体指数 NDWI = (green − nir)/(green + nir)。"""
    g = np.asarray(green, dtype=np.float64)
    n = np.asarray(nir, dtype=np.float64)
    return (g - n) / (g + n + eps)


def water_mask(ndwi_arr: np.ndarray, threshold: float = 0.0) -> np.ndarray:
    """NDWI 大于阈值为水体。"""
    return np.asarray(ndwi_arr, dtype=np.float64) > threshold


# ---------------------------------------------------------------------------
# 核心算法 2：叶绿素 a（OC3）
# ---------------------------------------------------------------------------
def chl_a_oc3(blue: np.ndarray, green: np.ndarray) -> np.ndarray:
    """NASA OC3 经验算法反演叶绿素 a 浓度 (mg/m³)。

    log10(chl) = a0 + a1·R + a2·R² + a3·R³ + a4·R⁴，R = log10(blue/green)。
    """
    blue = np.clip(np.asarray(blue, dtype=np.float64), 1e-6, None)
    green = np.clip(np.asarray(green, dtype=np.float64), 1e-6, None)
    R = np.log10(blue / green)
    logchl = (OC3_COEF[0] + OC3_COEF[1] * R + OC3_COEF[2] * R ** 2
              + OC3_COEF[3] * R ** 3 + OC3_COEF[4] * R ** 4)
    logchl = np.clip(logchl, -2.0, 2.0)  # 0.01 ~ 100 mg/m³
    return np.power(10.0, logchl)


# ---------------------------------------------------------------------------
# 核心算法 3：悬浮物 TSS（红波段 Gordon 逆）
# ---------------------------------------------------------------------------
def tss_from_red(red: np.ndarray) -> np.ndarray:
    """由红波段反射率反演 TSS (g/m³)。

    基于红光 Gordon 关系 Rrs = 0.5·bb/(a+bb)，其中红光吸收 a≈aw_red 近似常数、
    bb = bbw_red + b_sed·TSS。解析求逆：bb = 2·Rrs·a/(1−2·Rrs)。
    """
    red = np.clip(np.asarray(red, dtype=np.float64), 1e-6, 0.49)
    a = AW[2]  # 红光纯水吸收（常数）
    bb = 2.0 * red * a / (1.0 - 2.0 * red)
    tss = (bb - BBW[2]) / B_SED[2]
    return np.clip(tss, 0.0, None)


# ---------------------------------------------------------------------------
# 核心算法 4：透明度 Secchi（与 chl、TSS 负相关）
# ---------------------------------------------------------------------------
def secchi_depth(chl: np.ndarray, tss: np.ndarray) -> np.ndarray:
    """Secchi 透明度 (m)：随叶绿素与悬浮物升高而降低的经验模型。"""
    chl = np.clip(np.asarray(chl, dtype=np.float64), 0.0, None)
    tss = np.clip(np.asarray(tss, dtype=np.float64), 0.0, None)
    sd = 8.0 / (0.30 + 0.45 * np.power(chl, 0.6) + 0.06 * tss)
    return sd.astype(np.float64)


# ---------------------------------------------------------------------------
# 核心算法 5：富营养化分级（按叶绿素 a，OECD/常用阈值）
# ---------------------------------------------------------------------------
TROPHIC_NAMES = ["oligotrophic", "mesotrophic", "eutrophic", "hypertrophic"]
TROPHIC_CN = ["贫营养", "中营养", "富营养", "超富营养"]


def trophic_class(chl: np.ndarray) -> np.ndarray:
    """按叶绿素 a 浓度分级：0 贫 / 1 中 / 2 富 / 3 超富营养。

    阈值：<2.6, 2.6–7.4, 7.4–20, >20 (mg/m³)。
    """
    chl = np.asarray(chl, dtype=np.float64)
    cls = np.zeros(chl.shape, dtype=np.int32)
    cls[chl >= 2.6] = 1
    cls[chl >= 7.4] = 2
    cls[chl >= 20.0] = 3
    return cls


# ---------------------------------------------------------------------------
# 合成数据：含不同 chl/TSS 的水体影像 + 陆地块
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float], grid_shape: Tuple[int, int] = (64, 64), seed: int = 42,
) -> Dict[str, Any]:
    """生成 4 波段反射率影像：大部分为水体（chl/TSS 空间渐变），一角为陆地。"""
    rng = np.random.default_rng(seed)
    H, W = int(grid_shape[0]), int(grid_shape[1])
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float64)
    xxn = xx / max(W - 1, 1)
    yyn = yy / max(H - 1, 1)

    # 真值：chl 从西北（低）到东南（高），TSS 另一方向渐变
    chl = 0.5 + 35.0 * xxn * yyn + 3.0 * xxn + rng.normal(0, 0.3, (H, W))
    chl = np.clip(chl, 0.2, None)
    tss = 1.0 + 50.0 * (1.0 - xxn) * yyn + 5.0 * yyn + rng.normal(0, 0.5, (H, W))
    tss = np.clip(tss, 0.5, None)

    rrs = forward_rrs(chl, tss)  # (4, H, W)
    # 加传感器噪声
    rrs = rrs + rng.normal(0, 0.0008, rrs.shape)
    rrs = np.clip(rrs, 1e-5, None)

    # 陆地块（右上角）：植被光谱（高近红外）
    land = (xxn > 0.72) & (yyn > 0.72)
    veg = np.array([0.03, 0.09, 0.05, 0.45], dtype=np.float64)
    for b in range(4):
        rrs[b][land] = veg[b] + rng.normal(0, 0.005, np.count_nonzero(land))

    return {
        "bbox": list(bbox),
        "grid_shape": (H, W),
        "rrs": rrs.astype(np.float32),
        "chl_truth": chl.astype(np.float32),
        "tss_truth": tss.astype(np.float32),
        "land_mask": land,
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
    """Backwards-compat reader used by tests/test_core.py::test_read_missing_raises."""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_with_nodata(path: str) -> Tuple[np.ndarray, List[float], Optional[float], int]:
    """Read a multispectral raster and replace NoData pixels with NaN.

    Returns (cube (4, H, W) float32 with NaN at NoData, bbox [W,S,E,N],
    src_nodata value or None, n_valid_pixels where all bands are finite).
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        src_nodata = src.nodata
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    if src_nodata is not None and np.isfinite(src_nodata):
        cube = np.where(cube == np.float32(src_nodata), np.float32(np.nan), cube)
    # Coerce any other non-finite (e.g. NaN already in file) to NaN for consistency
    cube[~np.isfinite(cube)] = np.nan
    n_valid = int(np.isfinite(cube).all(axis=0).sum()) if cube.size else 0
    return cube, bbox, src_nodata, n_valid


def validate_bbox(bbox: Optional[List[float]]) -> List[float]:
    """Validate geographic bbox [W,S,E,N]. Returns bbox on success.

    Rules:
      - all four values present
      - longitudes in [-180, 180]; latitudes in [-90, 90]
      - W < E (no cross-180 support; raises a hint to split)
      - S < N
      - area > 1e-6 deg² (avoid degenerate / zero-area bbox)
    """
    if bbox is None or len(bbox) != 4:
        raise UsageError("--bbox requires 4 floats: W S E N (deg)")
    W, S, E, N = (float(v) for v in bbox)
    if not (-180.0 <= W <= 180.0 and -180.0 <= E <= 180.0):
        raise ValidationError(
            f"longitude out of [-180, 180]: W={W} E={E}",
            west=W, east=E,
        )
    if not (-90.0 <= S <= 90.0 and -90.0 <= N <= 90.0):
        raise ValidationError(
            f"latitude out of [-90, 90]: S={S} N={N}",
            south=S, north=N,
        )
    if W >= E:
        if W > 179.0 and E < -179.0:
            raise ValidationError(
                f"bbox crosses 180° meridian (W={W} > E={E}); "
                "split into two sub-bboxes (e.g. W1=-180/E1=<lng> and W2=<lng>/E2=180)",
                west=W, east=E, crosses_antimeridian=True,
            )
        raise ValidationError(
            f"bbox W ({W}) must be < E ({E}); check argument order: --bbox W S E N",
            west=W, east=E,
        )
    if S >= N:
        raise ValidationError(
            f"bbox S ({S}) must be < N ({N}); check argument order: --bbox W S E N",
            south=S, north=N,
        )
    area_deg2 = (E - W) * (N - S)
    if area_deg2 < 1e-6:
        raise ValidationError(
            f"bbox area too small: {area_deg2:.2e} deg² (must be > 1e-6)",
            area_deg2=area_deg2,
        )
    return [W, S, E, N]


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
            "parameters": getattr(args, "parameters", None),
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
# 参数解析
# ---------------------------------------------------------------------------
VALID_PARAMS = ("chl_a", "tss", "secchi")


def parse_parameters(spec: str) -> List[str]:
    parts = [p.strip().lower() for p in spec.split(",") if p.strip()]
    bad = [p for p in parts if p not in VALID_PARAMS]
    if bad:
        raise UsageError(
            f"unknown parameter(s) {bad}. Choose from: {list(VALID_PARAMS)}",
            parameters=bad,
        )
    if not parts:
        raise UsageError("--parameters must not be empty")
    # 去重保序
    seen, out = set(), []
    for p in parts:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir

    # ---- (1) 参数校验（任何目录创建之前） ----
    params = parse_parameters(args.parameters)
    if not (-1.0 <= args.ndwi_threshold <= 1.0):
        raise ValidationError(
            f"--ndwi-threshold must be in [-1, 1], got {args.ndwi_threshold}",
            ndwi_threshold=args.ndwi_threshold,
        )
    if args.seed is not None and int(args.seed) < 0:
        raise ValidationError(
            f"--seed must be a non-negative integer, got {args.seed}",
            seed=args.seed,
        )

    bbox = list(args.bbox) if args.bbox else None
    truth = None
    n_valid_pixels = 0
    src_nodata = None
    if args.input and not args.synthetic:
        cube, file_bbox, src_nodata, n_valid_pixels = read_geotiff_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if cube.shape[0] < 4:
            raise ValidationError(
                f"input raster needs >= 4 bands (blue, green, red, nir), got {cube.shape[0]}",
                bands=int(cube.shape[0]),
            )
        if n_valid_pixels == 0:
            raise ValidationError(
                "input raster has 0 valid (non-NoData) pixels across all bands; "
                "cannot retrieve water quality",
                input_nodata=src_nodata,
            )
        blue, green, red, nir = cube[0], cube[1], cube[2], cube[3]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        synth = generate_synthetic(bbox, seed=args.seed)
        rrs = synth["rrs"]
        blue, green, red, nir = rrs[0], rrs[1], rrs[2], rrs[3]
        truth = synth
        source_note = "synthetic"
        n_valid_pixels = int(blue.size)

    if blue.size == 0:
        raise ValidationError("empty input raster")

    # ---- (2) 校验通过后再创建输出目录 ----
    os.makedirs(output_dir, exist_ok=True)

    # ---- (3) 水体掩膜：NDWI > 阈值 且 4 波段都有效 ----
    ndwi_arr = ndwi(green, nir)
    wmask = water_mask(ndwi_arr, threshold=args.ndwi_threshold)
    valid_mask = (
        np.isfinite(blue) & np.isfinite(green) & np.isfinite(red) & np.isfinite(nir)
    )
    wmask = wmask & valid_mask
    n_water = int(np.count_nonzero(wmask))
    if n_water == 0:
        raise ValidationError(
            "no water pixels detected (NDWI mask empty or all pixels NoData)",
            ndwi_threshold=args.ndwi_threshold,
        )

    # ---- (4) 反演 ----
    chl = chl_a_oc3(blue, green).astype(np.float32)
    tss = tss_from_red(red).astype(np.float32)
    sec = secchi_depth(chl, tss).astype(np.float32)
    troph = trophic_class(chl)

    nodata = -9999.0
    chl_out = np.where(wmask, chl, nodata).astype(np.float32)
    tss_out = np.where(wmask, tss, nodata).astype(np.float32)
    sec_out = np.where(wmask, sec, nodata).astype(np.float32)
    troph_out = np.where(wmask, troph, -1).astype(np.float32)

    # ---- (5) 水体像元统计（已保证 wmask 内 4 波段均有效） ----
    wchl = chl[wmask]
    wtss = tss[wmask]
    wsec = sec[wmask]
    wtroph = troph[wmask]

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_valid_pixels": n_valid_pixels,
        "input_nodata": src_nodata,
        "n_water_pixels": n_water,
        "water_fraction": float(np.mean(wmask)),
        "chl_a_mean": float(np.mean(wchl)),
        "chl_a_min": float(np.min(wchl)),
        "chl_a_max": float(np.max(wchl)),
        "tss_mean": float(np.mean(wtss)),
        "secchi_mean": float(np.mean(wsec)),
        "trophic_distribution": {
            TROPHIC_NAMES[i]: int(np.count_nonzero(wtroph == i)) for i in range(4)
        },
    }

    # ---- (6) 与真值相关（合成模式，水体像元）；常量数组 corr 不定义 ----
    if truth is not None:
        ct = truth["chl_truth"][wmask]
        tt = truth["tss_truth"][wmask]
        if wchl.size >= 2 and wchl.std() > 0 and ct.std() > 0:
            qa["chl_a_corr_truth"] = float(np.corrcoef(wchl, ct)[0, 1])
        else:
            qa["chl_a_corr_truth"] = None
        if wtss.size >= 2 and wtss.std() > 0 and tt.std() > 0:
            qa["tss_corr_truth"] = float(np.corrcoef(wtss, tt)[0, 1])
        else:
            qa["tss_corr_truth"] = None

    # 输出栅格
    outputs: List[Dict[str, Any]] = []
    raster_map = {"chl_a": (chl_out, "chl_a.tif"), "tss": (tss_out, "tss.tif"),
                  "secchi": (sec_out, "secchi.tif")}
    for p in params:
        arr, fname = raster_map[p]
        path = os.path.join(output_dir, fname)
        write_geotiff(path, arr, bbox, nodata=nodata)
        outputs.append({"path": path, "kind": "raster", "crs_epsg": 4326,
                        "bbox_wgs84": bbox, "band_count": 1, "nodata": nodata})

    # 富营养化分级栅格（总是输出）
    troph_path = os.path.join(output_dir, "trophic_class.tif")
    write_geotiff(troph_path, troph_out, bbox, nodata=-1)
    outputs.append({"path": troph_path, "kind": "raster", "crs_epsg": 4326,
                    "bbox_wgs84": bbox, "band_count": 1, "nodata": -1})

    # 报告
    report = {
        "source": source_note,
        "parameters": params,
        "ndwi_threshold": args.ndwi_threshold,
        "water_pixels": n_water,
        "chl_a": {"mean": qa["chl_a_mean"], "min": qa["chl_a_min"], "max": qa["chl_a_max"]},
        "tss": {"mean": qa["tss_mean"]},
        "secchi": {"mean": qa["secchi_mean"]},
        "trophic_classes": {TROPHIC_CN[i]: int(np.count_nonzero(wtroph == i)) for i in range(4)},
        "trophic_names": {TROPHIC_NAMES[i]: int(np.count_nonzero(wtroph == i)) for i in range(4)},
    }
    if truth is not None:
        report["validation"] = {
            "chl_a_corr_truth": qa["chl_a_corr_truth"],
            "tss_corr_truth": qa["tss_corr_truth"],
        }
    report_path = os.path.join(output_dir, "water_quality_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    outputs.append({"path": report_path, "kind": "json"})

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  water pixels: {n_water}")
        print(f"[{SKILL_NAME}] chl-a mean: {qa['chl_a_mean']:.2f} mg/m³  "
              f"tss mean: {qa['tss_mean']:.2f} g/m³  secchi mean: {qa['secchi_mean']:.2f} m")
        if "chl_a_corr_truth" in qa:
            chl_corr = qa['chl_a_corr_truth']
            tss_corr = qa['tss_corr_truth']
            chl_s = f"{chl_corr:.3f}" if isinstance(chl_corr, float) else "n/a"
            tss_s = f"{tss_corr:.3f}" if isinstance(tss_corr, float) else "n/a"
            print(f"[{SKILL_NAME}] corr vs truth — chl: {chl_s}  tss: {tss_s}")
        print(f"[{SKILL_NAME}] trophic: {report['trophic_names']}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Water quality retrieval (chl-a / TSS / Secchi) from water-color imagery.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multispectral GeoTIFF (blue, green, red, nir reflectance)")
    p.add_argument("--parameters", default="chl_a,tss,secchi",
                   help="comma-separated outputs: chl_a,tss,secchi (default: all)")
    p.add_argument("--ndwi-threshold", type=float, default=0.0,
                   help="NDWI water/land threshold (default: 0.0)")
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
