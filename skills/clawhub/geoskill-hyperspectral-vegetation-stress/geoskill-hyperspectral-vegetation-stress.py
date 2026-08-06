#!/usr/bin/env python3
"""hyperspectral-vegetation-stress — 高光谱植被胁迫检测

利用高光谱立方体（含红边波段）检测植被胁迫，实现两类方法：

- **red_edge**：红边指数组合。
  - NDRE = (NIR − RedEdge) / (NIR + RedEdge)，胁迫时降低。
  - REP（Red Edge Position，红边位置）：红边一阶导数最大处波长，胁迫时蓝移。
  - PRI = (R531 − R570) / (R531 + R570)，光化学反射率指数，辅助参考。
  综合 NDRE 下降与 REP 蓝移得到 [0,1] 胁迫指数并分级。
- **sam**：光谱角制图（Spectral Angle Mapper），计算每个像元光谱与健康参考
  光谱的夹角，夹角越大越偏离健康状态。

数据源：本地高光谱 GeoTIFF（多波段栅格），或使用 ``--synthetic`` 生成含红边
波段的高光谱立方体（健康背景 + 注入胁迫斑块，红边蓝移 + NIR 下降）。

隐私声明 / Privacy：默认完全离线，不发起网络请求，所有处理本地完成。

Usage:
    python hyperspectral-vegetation-stress.py --bbox 116 39 117 40 --method red_edge --output-dir ./out
    python hyperspectral-vegetation-stress.py --input cube.tif --method sam --output-dir ./out

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
SKILL_NAME = "hyperspectral-vegetation-stress"

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


# 默认波长轴（nm）：覆盖 PRI(531/570)、红(670)、红边(680-750)、NIR(840)
WL_MIN, WL_MAX, WL_STEP = 500.0, 850.0, 10.0
HEALTHY_REP = 715.0   # 健康红边位置 (nm)
HEALTHY_NIR = 0.48
HEALTHY_RED = 0.04


def default_wavelengths(n: int) -> np.ndarray:
    return np.linspace(WL_MIN, WL_MAX, n, dtype=float)


def band_index(wavelengths: np.ndarray, target: float) -> int:
    return int(np.argmin(np.abs(np.asarray(wavelengths) - target)))


# ---------------------------------------------------------------------------
# 光谱模型（健康/胁迫植被）
# ---------------------------------------------------------------------------
def veg_reflectance(
    wl: np.ndarray, rep: float = HEALTHY_REP,
    nir: float = HEALTHY_NIR, red: float = HEALTHY_RED,
) -> np.ndarray:
    """参数化植被反射光谱：红边 sigmoid + 绿峰 + 红吸收谷。

    rep 控制红边位置（胁迫蓝移），nir/red 控制近红外平台与红光基底。
    """
    wl = np.asarray(wl, dtype=float)
    edge = 1.0 / (1.0 + np.exp(-(wl - rep) / 10.0))
    r = red + (nir - red) * edge
    r = r + 0.04 * np.exp(-((wl - 550.0) / 25.0) ** 2)   # 绿峰
    r = r - 0.03 * np.exp(-((wl - 670.0) / 20.0) ** 2)   # 红吸收谷
    return np.clip(r, 0.005, 0.9)


# ---------------------------------------------------------------------------
# 指数与胁迫算法
# ---------------------------------------------------------------------------
def ndre(cube: np.ndarray, wavelengths: np.ndarray) -> np.ndarray:
    """NDRE = (NIR − RedEdge)/(NIR + RedEdge)，NIR~840nm，RedEdge~720nm。

    NoData (NaN) 像元输出 NaN。
    """
    i_nir = band_index(wavelengths, 840.0)
    i_re = band_index(wavelengths, 720.0)
    nir = cube[i_nir].astype(float)
    re = cube[i_re].astype(float)
    invalid = ~(np.isfinite(nir) & np.isfinite(re))
    denom = nir + re
    out = np.where(denom > 1e-6, (nir - re) / denom, 0.0)
    out = np.where(invalid, np.nan, out)
    return out


def pri(cube: np.ndarray, wavelengths: np.ndarray) -> np.ndarray:
    """PRI = (R531 − R570)/(R531 + R570)。NoData (NaN) 像元输出 NaN。"""
    i531 = band_index(wavelengths, 531.0)
    i570 = band_index(wavelengths, 570.0)
    a = cube[i531].astype(float)
    b = cube[i570].astype(float)
    invalid = ~(np.isfinite(a) & np.isfinite(b))
    denom = a + b
    out = np.where(denom > 1e-6, (a - b) / denom, 0.0)
    out = np.where(invalid, np.nan, out)
    return out


def rep_map(cube: np.ndarray, wavelengths: np.ndarray) -> np.ndarray:
    """红边位置：红边窗口(680-750nm)一阶导最大处波长。

    NoData (NaN) 像元输出 NaN（np.gradient 在 NaN 处返回 NaN，argmax 跳过）。
    """
    wl = np.asarray(wavelengths, dtype=float)
    m = (wl >= 680.0) & (wl <= 750.0)
    if int(np.sum(m)) < 3:
        raise ValidationError(
            "wavelengths lack a red-edge window (680-750nm) for REP",
            n_bands=int(cube.shape[0]),
        )
    wl_re = wl[m]
    sub = cube[m].astype(float)
    # NaN-aware gradient: np.gradient does not handle NaN; fall back to 0 gradient at NaN
    sub_filled = np.where(np.isfinite(sub), sub, 0.0)
    deriv = np.gradient(sub_filled, wl_re, axis=0)
    invalid_pix = np.any(~np.isfinite(sub), axis=0)
    idx = np.argmax(deriv, axis=0)
    out = wl_re[idx].astype(float)
    out = np.where(invalid_pix, np.nan, out)
    return out


def sam_map(cube: np.ndarray, reference: np.ndarray) -> np.ndarray:
    """光谱角制图：每像元光谱与参考光谱的夹角 (弧度)。

    NoData (NaN) 像元输出 π/2。
    """
    c = cube.astype(float)
    ref = np.asarray(reference, dtype=float)
    invalid_pix = np.any(~np.isfinite(c), axis=0)
    c_safe = np.where(np.isfinite(c), c, 0.0)
    dot = np.tensordot(c_safe, ref, axes=([0], [0]))
    norm_c = np.sqrt(np.sum(c_safe * c_safe, axis=0))
    norm_r = float(np.sqrt(np.sum(ref * ref)))
    denom = norm_c * norm_r
    cosang = np.where(denom > 1e-9, dot / denom, 1.0)
    cosang = np.clip(cosang, -1.0, 1.0)
    out = np.arccos(cosang)
    out = np.where(invalid_pix, np.pi / 2.0, out)
    return out


def stress_red_edge(
    cube: np.ndarray, wavelengths: np.ndarray,
    ndre_ref: float = 0.20, rep_ref: float = HEALTHY_REP,
    rep_scale: float = 20.0,
) -> Tuple[np.ndarray, Dict[str, np.ndarray]]:
    """红边法胁迫指数 [0,1]：NDRE 下降 + REP 蓝移的综合。

    NoData (NaN) 像元 stress=NaN。
    """
    ndre_arr = ndre(cube, wavelengths)
    rep_arr = rep_map(cube, wavelengths)
    pri_arr = pri(cube, wavelengths)
    s_ndre = np.clip((ndre_ref - ndre_arr) / max(ndre_ref, 1e-6), 0.0, 1.0)
    s_rep = np.clip((rep_ref - rep_arr) / rep_scale, 0.0, 1.0)
    stress = 0.5 * s_ndre + 0.5 * s_rep
    return stress.astype(np.float32), {
        "ndre": ndre_arr.astype(np.float32),
        "rep": rep_arr.astype(np.float32),
        "pri": pri_arr.astype(np.float32),
    }


def stress_sam(
    cube: np.ndarray, wavelengths: np.ndarray, max_angle: float = 0.30,
) -> Tuple[np.ndarray, Dict[str, np.ndarray]]:
    """SAM 法胁迫指数 [0,1]：光谱角 / max_angle。参考光谱为健康植被。

    NoData (NaN) 像元 stress=NaN（angle 被设 π/2，对应 stress>1 clip 到 1；
    输出阶段再覆盖为 NaN）。
    """
    ref = veg_reflectance(wavelengths, HEALTHY_REP, HEALTHY_NIR, HEALTHY_RED)
    ang = sam_map(cube, ref)
    invalid_pix = np.any(~np.isfinite(cube), axis=0)
    stress = np.clip(ang / max_angle, 0.0, 1.0)
    stress = np.where(invalid_pix, np.nan, stress)
    return stress.astype(np.float32), {"sam_angle": ang.astype(np.float32)}


def classify_stress(stress: np.ndarray) -> np.ndarray:
    """连续胁迫指数 → 等级：0健康 1轻度 2中度 3重度。"""
    cls = np.zeros(stress.shape, dtype=np.uint8)
    cls[stress >= 0.25] = 1
    cls[stress >= 0.50] = 2
    cls[stress >= 0.75] = 3
    return cls


# ---------------------------------------------------------------------------
# 合成数据：健康背景 + 胁迫斑块（红边蓝移 + NIR 下降）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float], width: int = 64, height: int = 64, seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 (bands,H,W) 高光谱立方体 + 波长轴 + 真值信息。"""
    rng = np.random.default_rng(seed)
    wl = default_wavelengths(int((WL_MAX - WL_MIN) / WL_STEP) + 1)

    yy, xx = np.mgrid[0:height, 0:width]
    rep = np.full((height, width), HEALTHY_REP, dtype=float)
    nir = np.full((height, width), HEALTHY_NIR, dtype=float)
    red = np.full((height, width), HEALTHY_RED, dtype=float)

    # 胁迫斑块 1（重度，右上）
    c1 = (int(0.72 * height), int(0.72 * width))
    r1 = int(0.20 * min(height, width))
    m1 = ((yy - c1[0]) ** 2 + (xx - c1[1]) ** 2) <= r1 ** 2
    rep[m1] = 698.0
    nir[m1] = 0.28
    red[m1] = 0.06

    # 胁迫斑块 2（中度，左下）
    c2 = (int(0.28 * height), int(0.28 * width))
    r2 = int(0.13 * min(height, width))
    m2 = ((yy - c2[0]) ** 2 + (xx - c2[1]) ** 2) <= r2 ** 2
    rep[m2] = 706.0
    nir[m2] = 0.38
    red[m2] = 0.05

    # 矢量化构建光谱立方体
    wlc = wl[:, None, None]
    edge = 1.0 / (1.0 + np.exp(-(wlc - rep[None, :, :]) / 10.0))
    cube = red[None] + (nir[None] - red[None]) * edge
    cube = cube + 0.04 * np.exp(-((wlc - 550.0) / 25.0) ** 2)
    cube = cube - 0.03 * np.exp(-((wlc - 670.0) / 20.0) ** 2)
    cube = cube + rng.normal(0, 0.004, size=cube.shape)
    cube = np.clip(cube, 0.005, 0.9).astype(np.float32)

    truth_mask = (m1 | m2)
    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "n_bands": int(wl.size),
        "wavelengths": wl.tolist(),
        "stress_blob_1": {"center_rc": list(c1), "radius_px": int(r1), "level": "severe"},
        "stress_blob_2": {"center_rc": list(c2), "radius_px": int(r2), "level": "moderate"},
        "n_stress_pixels": int(np.sum(truth_mask)),
    }
    return cube, wl, info


# ---------------------------------------------------------------------------
# GeoTIFF / 高光谱 I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, array: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if array.ndim == 2:
        array = array[np.newaxis, ...]
    nb, h, w = array.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(array[b].astype("float32"), b + 1)


def read_cube(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_cube_with_nodata(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """Read multi-band cube and replace NoData pixels with NaN.

    A pixel is NoData if ANY band equals the nodata sentinel. Returns
    (cube (bands, H, W), bbox, nodata_value_or_None).
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None and np.isfinite(nodata):
        bad_mask = np.any(cube == nodata, axis=0)
        cube[:, bad_mask] = np.nan
    return cube, bbox, nodata


def validate_bbox(bbox: Optional[List[float]], allow_none: bool = False) -> List[float]:
    """Validate a W,S,E,N bbox. Cross-180 / out-of-range / W>=E / S>=N -> ValidationError."""
    if bbox is None:
        if allow_none:
            return None  # type: ignore[return-value]
        raise ValidationError("bbox is required")
    if len(bbox) != 4:
        raise ValidationError(f"bbox must have 4 floats, got {len(bbox)}")
    w, s, e, n = bbox
    for v, name in zip([w, s, e, n], ["W", "S", "E", "N"]):
        if not isinstance(v, (int, float)) or not (-1e9 < v < 1e9):
            raise ValidationError(f"bbox {name}={v!r} not a finite number")
    if w == e or s == n:
        raise ValidationError(f"bbox has zero area: W={w} E={e} S={s} N={n}")
    if not (-180.0 <= w <= 180.0) or not (-180.0 <= e <= 180.0):
        raise ValidationError(f"bbox lon out of [-180,180]: W={w} E={e}")
    if not (-90.0 <= s <= 90.0) or not (-90.0 <= n <= 90.0):
        raise ValidationError(f"bbox lat out of [-90,90]: S={s} N={n}")
    if w > e:
        if not (w > 170.0 and e < -170.0):
            raise ValidationError(
                f"bbox has W>E (minLon > maxLon): W={w} E={e} — "
                f"if crossing the dateline, split into two bboxes (e.g. "
                f"[{w}, {s}, 180, {n}] and [-180, {s}, {e}, {n}])"
            )
        raise ValidationError(
            f"bbox crosses the 180° dateline (W={w} E={e}); "
            f"split into two non-wrapping bboxes ([{w}, {s}, 180, {n}] and "
            f"[-180, {s}, {e}, {n}]) and run separately"
        )
    if s > n:
        raise ValidationError(f"bbox has S>N (minLat > maxLat): S={s} N={n}")
    return [float(w), float(s), float(e), float(n)]


def validate_params(max_angle: float, anomaly_thresh: float) -> Tuple[float, float]:
    """Validate CLI thresholds. Returns (max_angle, anomaly_thresh)."""
    if max_angle is None or max_angle <= 0:
        raise ValidationError(f"--max-angle must be > 0, got {max_angle}")
    if not (0.0 <= anomaly_thresh <= 1.0):
        raise ValidationError(f"--anomaly-thresh must be in [0, 1], got {anomaly_thresh}")
    return float(max_angle), float(anomaly_thresh)


# ---------------------------------------------------------------------------
# 异常区域矢量化（连通域 bbox 多边形）
# ---------------------------------------------------------------------------
def pixel_to_geo(col: float, row: float, bbox: List[float], h: int, w: int) -> List[float]:
    W_, S, E, N = bbox
    lon = W_ + (col + 0.5) / w * (E - W_)
    lat = N - (row + 0.5) / h * (N - S)
    return [float(lon), float(lat)]


def extract_anomalies(
    stress: np.ndarray, cls: np.ndarray, bbox: List[float],
    thresh: float = 0.40,
) -> List[Dict[str, Any]]:
    """阈值化 + 连通域，输出每个胁迫斑块的 bbox 多边形要素。"""
    from scipy.ndimage import label

    h, w = stress.shape
    mask = stress >= thresh
    labeled, n = label(mask)
    features: List[Dict[str, Any]] = []
    for lab in range(1, n + 1):
        ys, xs = np.where(labeled == lab)
        r0, r1 = int(ys.min()), int(ys.max())
        c0, c1 = int(xs.min()), int(xs.max())
        sub = stress[labeled == lab]
        cls_sub = cls[labeled == lab]
        p0 = pixel_to_geo(c0, r0, bbox, h, w)
        p1 = pixel_to_geo(c1, r1, bbox, h, w)
        lon0, lat0 = min(p0[0], p1[0]), min(p0[1], p1[1])
        lon1, lat1 = max(p0[0], p1[0]), max(p0[1], p1[1])
        ring = [[lon0, lat0], [lon1, lat0], [lon1, lat1], [lon0, lat1], [lon0, lat0]]
        features.append({
            "type": "Feature",
            "geometry": {"type": "Polygon", "coordinates": [ring]},
            "properties": {
                "n_pixels": int(sub.size),
                "mean_stress": float(np.mean(sub)),
                "max_stress": float(np.max(sub)),
                "max_class": int(np.max(cls_sub)),
            },
        })
    features.sort(key=lambda f: f["properties"]["mean_stress"], reverse=True)
    return features


def write_geojson(path: str, features: List[Dict[str, Any]]) -> None:
    fc = {"type": "FeatureCollection", "features": features}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(fc, f, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "method": getattr(args, "method", None),
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

    # ---- 1. 参数验证 (前置：失败不创建 output_dir) ----
    bbox = list(args.bbox) if args.bbox else None
    if bbox is not None:
        bbox = validate_bbox(bbox)
    max_angle, anomaly_thresh = validate_params(args.max_angle, args.anomaly_thresh)

    # ---- 2. 数据获取 ----
    synth_info: Optional[Dict[str, Any]] = None
    input_nodata: Optional[float] = None
    valid_mask: Optional[np.ndarray] = None
    n_valid_input: int = 0
    n_total_input: int = 0
    if args.input and not args.synthetic:
        cube, file_bbox, input_nodata = read_cube_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        bbox = validate_bbox(bbox)
        valid_mask = np.all(np.isfinite(cube), axis=0)
        n_valid_input = int(valid_mask.sum())
        n_total_input = int(cube.shape[1] * cube.shape[2])
        if n_valid_input == 0:
            raise ValidationError(
                f"input cube has no valid (non-NoData) pixels "
                f"(nodata={input_nodata}, total={n_total_input})"
            )
        wavelengths = default_wavelengths(cube.shape[0])
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, wavelengths, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"
        n_valid_input = int(cube.size)
        n_total_input = int(cube.shape[1] * cube.shape[2])

    # ---- 3. 校验通过后创建 output_dir ----
    os.makedirs(output_dir, exist_ok=True)

    if cube.size == 0 or cube.ndim != 3:
        raise ValidationError("input must be a 3D (bands,H,W) hyperspectral cube")

    # 计算胁迫指数
    if args.method == "sam":
        stress, aux = stress_sam(cube, wavelengths, max_angle=max_angle)
    else:
        stress, aux = stress_red_edge(cube, wavelengths)

    # classify_stress 不能处理 NaN（s>=0.25 比较结果为 False 但 NaN 不计入）
    cls_raw = classify_stress(stress)
    if valid_mask is not None:
        cls = np.where(valid_mask, cls_raw, 255).astype(np.uint8)  # 255 = nodata sentinel
    else:
        cls = cls_raw

    # 输出（NoData 区写 -9999.0 / 255 哨兵）
    level_path = os.path.join(output_dir, "stress_level.tif")
    write_geotiff(level_path, cls.astype(np.float32), bbox, nodata=255.0)

    index_path = os.path.join(output_dir, "stress_index.tif")
    write_geotiff(index_path, np.nan_to_num(stress, nan=-9999.0), bbox, nodata=-9999.0)

    # 异常检测（仅 valid 像元）
    if valid_mask is not None:
        stress_for_anom = np.where(valid_mask, stress, -np.inf)  # 无效像元 stress<0 必不过阈
    else:
        stress_for_anom = stress
    cls_for_anom = np.where(valid_mask, cls_raw, 0).astype(np.uint8) if valid_mask is not None else cls_raw
    anomalies = extract_anomalies(stress_for_anom, cls_for_anom, bbox, thresh=anomaly_thresh)
    anomaly_path = os.path.join(output_dir, "anomaly.geojson")
    write_geojson(anomaly_path, anomalies)

    class_counts = {int(k): int(v) for k, v in
                    zip(*np.unique(cls, return_counts=True))}
    finite_stress = stress[np.isfinite(stress)]
    mean_stress = float(np.mean(finite_stress)) if finite_stress.size else float("nan")
    report = {
        "source": source_note,
        "method": args.method,
        "n_bands": int(cube.shape[0]),
        "shape": [int(cube.shape[1]), int(cube.shape[2])],
        "class_counts": class_counts,
        "mean_stress": mean_stress,
        "n_anomalies": len(anomalies),
        "aux_mean": {k: float(np.mean(v[np.isfinite(v)])) if np.any(np.isfinite(v)) else None
                     for k, v in aux.items()},
    }
    report_path = os.path.join(output_dir, "stress_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "n_bands": int(cube.shape[0]),
        "mean_stress": mean_stress,
        "class_counts": class_counts,
        "n_anomalies": len(anomalies),
        "n_valid_pixels": int(n_valid_input),
        "n_total_pixels": int(n_total_input),
        "input_nodata": input_nodata,
    }
    if synth_info is not None:
        qa["synthetic_n_stress_pixels"] = synth_info["n_stress_pixels"]

    outputs = [
        {"path": level_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "nodata": 255.0},
        {"path": index_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "nodata": -9999.0},
        {"path": anomaly_path, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": len(anomalies)},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  method: {args.method}")
        print(f"[{SKILL_NAME}] bands: {cube.shape[0]}  shape: {cube.shape[1:]}")
        print(f"[{SKILL_NAME}] mean stress: {qa['mean_stress']:.4f}")
        print(f"[{SKILL_NAME}] class counts: {class_counts}")
        print(f"[{SKILL_NAME}] anomalies: {len(anomalies)}")
        print(f"[{SKILL_NAME}] output: {level_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Hyperspectral vegetation stress detection via red-edge indices (NDRE/REP/PRI) and SAM.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input hyperspectral GeoTIFF (bands,H,W)")
    p.add_argument("--method", default="red_edge", choices=["red_edge", "sam"],
                   help="stress detection method (default: red_edge)")
    p.add_argument("--max-angle", type=float, default=0.30,
                   help="SAM angle (rad) mapped to stress=1 (default: 0.30)")
    p.add_argument("--anomaly-thresh", type=float, default=0.40,
                   help="stress index threshold for anomaly polygons (default: 0.40)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic hyperspectral scene (offline)")
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
