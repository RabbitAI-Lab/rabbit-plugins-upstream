#!/usr/bin/env python3
"""precision-forestry-monitoring — 精准林业遥感监测

融合多源遥感数据实现林分尺度的精准林业监测，覆盖"单木—林分—健康—生物量"
四个层次：

- **树高 / 单木**：CHM = DSM − DTM，局部峰值检测（non-maximum suppression）
  提取单木位置与树高。
- **冠幅 / 胸径 / 蓄积量**：由冠幅反演胸径（DBH = k·CW），再用异速生长方程
  V = a·DBH^b·H^c 估单木蓄积量，累加得林分蓄积量。
- **郁闭度**：CHM 高于阈值的冠层像元占比，∈[0,1]。
- **健康分级**：NDVI = (NIR−Red)/(NIR+Red)、NDRE = (NIR−RedEdge)/(NIR+RedEdge)
  组合分级（健康 / 中等 / 胁迫）。
- **SAR 生物量**：后向散射 σ⁰(dB)→线性→生物量经验关系（单调递增）。

数据源：本地多波段 GeoTIFF（波段顺序 DSM/DTM/Red/NIR/RedEdge/SAR），或
``--synthetic`` 生成物理一致的模拟林分用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python precision-forestry-monitoring.py --input forest.tif --output-dir ./out
    python precision-forestry-monitoring.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "precision-forestry-monitoring"

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


# 输入波段角色（顺序固定）
BAND_ROLES = ["dsm", "dtm", "red", "nir", "rededge", "sar"]
N_REQUIRED_BANDS = len(BAND_ROLES)

# 默认异速生长参数（DBH 单位 cm，H 单位 m，V 单位 m^3）
DEFAULT_ALLOMETRY = {"a": 6.0e-5, "b": 1.9, "c": 0.9}
# 冠幅(CW, m) -> 胸径(DBH, cm) 的经验斜率
DEFAULT_CROWN_DBH_K = 3.0


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def compute_chm(dsm: np.ndarray, dtm: np.ndarray) -> np.ndarray:
    """冠层高度模型 CHM = DSM − DTM，负值裁剪为 0。"""
    dsm = np.asarray(dsm, dtype=np.float32)
    dtm = np.asarray(dtm, dtype=np.float32)
    chm = dsm - dtm
    chm = np.where(np.isfinite(chm), chm, 0.0)
    return np.clip(chm, 0.0, None).astype(np.float32)


def detect_trees(
    chm: np.ndarray,
    min_height: float = 2.0,
    footprint: int = 5,
) -> List[Dict[str, Any]]:
    """局部峰值检测单木（non-maximum suppression）。

    返回 [{x, y, height}]，按树高降序。x/y 为像元列/行坐标。
    """
    from scipy.ndimage import maximum_filter

    h = np.where(np.isfinite(chm), chm, 0.0).astype(np.float32)
    if h.size == 0:
        return []
    footprint = max(int(footprint), 3)
    local_max = maximum_filter(h, size=footprint, mode="constant")
    # 严格局部极大 + 高于最小树高阈值
    peaks = (h == local_max) & (h >= float(min_height)) & (h > 0)
    ys, xs = np.where(peaks)
    trees: List[Dict[str, Any]] = []
    for y, x in zip(ys.tolist(), xs.tolist()):
        trees.append({"x": int(x), "y": int(y), "height": float(h[y, x])})
    trees.sort(key=lambda t: t["height"], reverse=True)
    return trees


def crown_width_from_chm(
    chm: np.ndarray,
    y: int,
    x: int,
    pixel_size: float,
    frac: float = 0.5,
) -> float:
    """从 CHM 估计单木冠幅（半高全宽，单位 m）。

    以峰值为中心向外扫描，取四个方向上 CHM 降到 peak*frac 的最远平均半径，
    冠幅 = 2 * 半径。保底为一个像元宽度。
    """
    h, w = chm.shape
    peak = float(chm[y, x])
    if peak <= 0:
        return float(pixel_size)
    threshold = peak * float(frac)
    radii: List[float] = []
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        r = 0
        cy, cx = y, x
        while True:
            ny, nx = cy + dy, cx + dx
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                break
            if chm[ny, nx] < threshold:
                break
            r += 1
            cy, cx = ny, nx
        radii.append(float(r))
    mean_radius = float(np.mean(radii)) if radii else 0.0
    crown_width = 2.0 * mean_radius * pixel_size
    return max(crown_width, float(pixel_size))


def crown_to_dbh(crown_width_m: float, k: float = DEFAULT_CROWN_DBH_K) -> float:
    """冠幅(m) -> 胸径 DBH(cm)：DBH = k · CW。"""
    return float(k) * float(crown_width_m)


def allometric_volume(
    dbh_cm: float,
    height_m: float,
    a: float,
    b: float,
    c: float,
) -> float:
    """异速生长方程单木蓄积量 V = a·DBH^b·H^c（m^3）。解析式，无近似。"""
    dbh = max(float(dbh_cm), 0.0)
    height = max(float(height_m), 0.0)
    if dbh <= 0.0 or height <= 0.0:
        return 0.0
    return float(a) * (dbh ** float(b)) * (height ** float(c))


def canopy_closure(chm: np.ndarray, threshold: float = 2.0) -> float:
    """郁闭度：CHM > threshold 的像元占比，∈[0,1]。"""
    valid = chm[np.isfinite(chm)]
    if valid.size == 0:
        return 0.0
    closed = float(np.count_nonzero(valid > float(threshold)))
    return float(np.clip(closed / valid.size, 0.0, 1.0))


def ndvi(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
    """NDVI = (NIR−Red)/(NIR+Red)，∈[-1,1]。"""
    nir = np.asarray(nir, dtype=np.float32)
    red = np.asarray(red, dtype=np.float32)
    denom = nir + red
    out = np.where(np.abs(denom) > 1e-9, (nir - red) / denom, 0.0)
    return np.clip(out, -1.0, 1.0).astype(np.float32)


def ndre(nir: np.ndarray, rededge: np.ndarray) -> np.ndarray:
    """NDRE = (NIR−RedEdge)/(NIR+RedEdge)，∈[-1,1]。"""
    nir = np.asarray(nir, dtype=np.float32)
    re = np.asarray(rededge, dtype=np.float32)
    denom = nir + re
    out = np.where(np.abs(denom) > 1e-9, (nir - re) / denom, 0.0)
    return np.clip(out, -1.0, 1.0).astype(np.float32)


def health_grade(
    ndvi_arr: np.ndarray,
    ndre_arr: np.ndarray,
    method: str = "combined",
) -> np.ndarray:
    """植被健康分级：3=健康，2=中等，1=胁迫，0=无植被/裸地。

    - combined：NDVI 与 NDRE 同时达标才算健康；
    - ndvi / ndre：仅用单指数阈值。
    """
    ndvi_arr = np.asarray(ndvi_arr, dtype=np.float32)
    ndre_arr = np.asarray(ndre_arr, dtype=np.float32)
    grade = np.zeros(ndvi_arr.shape, dtype=np.int16)

    if method == "ndvi":
        healthy = ndvi_arr >= 0.6
        moderate = (ndvi_arr >= 0.3) & (ndvi_arr < 0.6)
    elif method == "ndre":
        healthy = ndre_arr >= 0.3
        moderate = (ndre_arr >= 0.1) & (ndre_arr < 0.3)
    else:  # combined
        healthy = (ndvi_arr >= 0.6) & (ndre_arr >= 0.3)
        moderate = (ndvi_arr >= 0.3) & (ndre_arr >= 0.1) & (~healthy)

    veg = ndvi_arr > 0.1  # 有植被信号
    grade = np.where(healthy, 3, grade)
    grade = np.where(moderate & (~healthy), 2, grade)
    grade = np.where(veg & (~healthy) & (~moderate), 1, grade)
    return grade.astype(np.int16)


def sar_biomass_t_ha(
    sigma0_db: np.ndarray,
    a: float = 220.0,
    b: float = 0.45,
) -> np.ndarray:
    """SAR 后向散射 -> 地上生物量 (t/ha)。

    先把 σ⁰(dB) 转线性功率，再用幂函数经验关系 AGB = a·(σ⁰_lin)^b，
    单调递增，裁剪到 [0, 600] t/ha。
    """
    db = np.asarray(sigma0_db, dtype=np.float32)
    lin = np.power(10.0, db / 10.0)
    agb = float(a) * np.power(np.clip(lin, 1e-9, None), float(b))
    return np.clip(agb, 0.0, 600.0).astype(np.float32)


def estimate_stand(
    chm: np.ndarray,
    pixel_size: float,
    min_height: float = 2.0,
    footprint: int = 5,
    allo: Optional[Dict[str, float]] = None,
    k: float = DEFAULT_CROWN_DBH_K,
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """单木检测 + 异速生长，返回 (trees, summary)。"""
    allo = dict(DEFAULT_ALLOMETRY if allo is None else allo)
    trees = detect_trees(chm, min_height=min_height, footprint=footprint)
    total_volume = 0.0
    heights: List[float] = []
    for t in trees:
        cw = crown_width_from_chm(chm, t["y"], t["x"], pixel_size)
        dbh = crown_to_dbh(cw, k)
        vol = allometric_volume(dbh, t["height"], allo["a"], allo["b"], allo["c"])
        t["crown_width_m"] = float(cw)
        t["dbh_cm"] = float(dbh)
        t["volume_m3"] = float(vol)
        total_volume += vol
        heights.append(t["height"])

    summary = {
        "tree_count": len(trees),
        "total_volume_m3": float(total_volume),
        "mean_height_m": float(np.mean(heights)) if heights else 0.0,
        "max_height_m": float(np.max(heights)) if heights else 0.0,
        "allometry": allo,
        "crown_dbh_k": k,
    }
    return trees, summary


# ---------------------------------------------------------------------------
# 合成数据：物理一致的模拟林分（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (6, H, W) 林分立方体，波段顺序 = BAND_ROLES。

    在规则网格上注入若干已知高度的树（高斯冠层），DSM = DTM + CHM，
    多光谱反射率与 SAR 后向散射随生物量变化，便于测试恢复注入真值。
    """
    rng = np.random.default_rng(seed)

    # 地形：缓坡 + 低频起伏
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    ny = yy / max(height - 1, 1)
    nx = xx / max(width - 1, 1)
    dtm = 120.0 + 15.0 * nx + 8.0 * np.sin(2.0 * np.pi * ny)
    dtm = dtm.astype(np.float32)

    # 注入树：4x4 网格，固定高度（中心最高），高斯冠层
    chm = np.zeros((height, width), dtype=np.float32)
    injected: List[Dict[str, Any]] = []
    cols = np.linspace(0.15, 0.85, 4)
    rows = np.linspace(0.15, 0.85, 4)
    peak_height = 24.0
    sigma_px = 3.0
    for fy in rows:
        for fx in cols:
            cy = int(round(fy * (height - 1)))
            cx = int(round(fx * (width - 1)))
            th = peak_height * (0.6 + 0.4 * (1.0 - abs(fy - 0.5) - abs(fx - 0.5)))
            th = float(np.clip(th, 8.0, peak_height))
            g = th * np.exp(-(((yy - cy) ** 2 + (xx - cx) ** 2)) / (2.0 * sigma_px ** 2))
            chm += g.astype(np.float32)
            injected.append({"x": cx, "y": cy, "height": th})
    chm = chm + rng.normal(0, 0.15, size=chm.shape).astype(np.float32)
    chm = np.clip(chm, 0.0, None).astype(np.float32)

    dsm = (dtm + chm).astype(np.float32)

    # 多光谱：冠层低红高 NIR；裸地相反
    canopy_frac = np.clip(chm / 12.0, 0.0, 1.0)
    red = (0.18 - 0.14 * canopy_frac + rng.normal(0, 0.005, size=chm.shape)).astype(np.float32)
    nir = (0.15 + 0.33 * canopy_frac + rng.normal(0, 0.008, size=chm.shape)).astype(np.float32)
    rededge = (0.10 + 0.22 * canopy_frac + rng.normal(0, 0.006, size=chm.shape)).astype(np.float32)
    red = np.clip(red, 0.01, 1.0)
    nir = np.clip(nir, 0.01, 1.0)
    rededge = np.clip(rededge, 0.01, 1.0)

    # SAR：生物量越大后向散射越强（dB 越高），范围约 [-18, -6]
    sar = (-18.0 + 12.0 * canopy_frac + rng.normal(0, 0.4, size=chm.shape)).astype(np.float32)

    cube = np.stack([dsm, dtm, red, nir, rededge, sar], axis=0).astype(np.float32)
    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "band_roles": BAND_ROLES,
        "injected_trees": injected,
        "peak_height": peak_height,
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
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_full(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """扩展版 read：同时返回 nodata 值（若无则为 None）。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
        if nodata is not None:
            nodata = float(nodata)
    return cube, bbox, nodata


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Optional[List[float]]) -> List[float]:
    """校验地理 bbox 合法性，失败抛 ValidationError（exit 6）。

    检查：4 元长度、经纬度数值范围、S<N、跨 180°（W≥E）、最小跨度。
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats [W S E N]")
    try:
        w, s, e, n = [float(x) for x in bbox]
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox entries must be numeric: {exc}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"latitude out of [-90,90]: S={s}, N={n}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"longitude out of [-180,180]: W={w}, E={e}")
    if s >= n:
        raise ValidationError(
            f"S >= N (S={s}, N={n}); bbox inverted (S must be < N)"
        )
    if w >= e:
        raise ValidationError(
            f"W >= E (W={w}, E={e}); cross-180° bbox not supported. "
            f"Split into two non-antipodal bboxes."
        )
    if (e - w) < 0.001 or (n - s) < 0.001:
        raise ValidationError(
            f"bbox too small ({(e-w):.6f}°×{(n-s):.6f}°); min span is 0.001°"
        )
    return [w, s, e, n]


def pixel_size_m(bbox: List[float], width: int) -> float:
    """由 bbox(度) 与宽度估计像元地面尺寸(m)，取纬度中线。"""
    lat_mid = 0.5 * (bbox[1] + bbox[3])
    span_m = (bbox[2] - bbox[0]) * 111320.0 * np.cos(np.deg2rad(lat_mid))
    return float(abs(span_m) / max(int(width), 1))


# ---------------------------------------------------------------------------
# 矢量输出（GeoJSON，手写 dict，离线无依赖）
# ---------------------------------------------------------------------------
def trees_to_geojson(
    trees: List[Dict[str, Any]],
    bbox: List[float],
    width: int,
    height: int,
) -> Dict[str, Any]:
    """把像元坐标的单木转成 WGS84 点 GeoJSON。"""
    w, s, e, n = bbox
    dx = (e - w) / max(int(width), 1)
    dy = (n - s) / max(int(height), 1)
    feats = []
    for i, t in enumerate(trees):
        lon = w + (t["x"] + 0.5) * dx
        lat = n - (t["y"] + 0.5) * dy  # 行向下 -> 纬度递减
        feats.append({
            "type": "Feature",
            "id": i,
            "geometry": {"type": "Point", "coordinates": [round(lon, 6), round(lat, 6)]},
            "properties": {
                "tree_id": i,
                "height_m": round(t["height"], 2),
                "crown_width_m": round(t.get("crown_width_m", 0.0), 2),
                "dbh_cm": round(t.get("dbh_cm", 0.0), 2),
                "volume_m3": round(t.get("volume_m3", 0.0), 4),
            },
        })
    return {"type": "FeatureCollection", "features": feats}


# ---------------------------------------------------------------------------
# 经营建议
# ---------------------------------------------------------------------------
def management_advice(summary: Dict[str, Any], closure: float,
                      health_frac: Dict[str, float]) -> Dict[str, Any]:
    """根据郁闭度、蓄积量、健康占比生成经营建议。"""
    recs: List[str] = []
    if closure > 0.8:
        recs.append("郁闭度偏高(>0.8)，建议适度间伐以改善林内光照与林木生长。")
    elif closure < 0.3:
        recs.append("郁闭度偏低(<0.3)，林地利用不足，建议补植或封育促进郁闭。")
    else:
        recs.append("郁闭度适中(0.3-0.8)，维持现有经营措施。")

    stressed = health_frac.get("stressed", 0.0)
    if stressed > 0.25:
        recs.append("胁迫像元占比>25%，建议结合地面调查排查病虫害/干旱并优先处置。")
    if summary.get("mean_height_m", 0.0) > 18.0 and summary.get("tree_count", 0) > 0:
        recs.append("平均树高较高且蓄积量可观，可作为主伐/择伐候选林分。")
    if not recs:
        recs.append("林分状态良好，按常规周期监测即可。")
    return {"recommendations": recs, "closure": closure, "health_fraction": health_frac}


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
    input_nodata: Optional[float] = None,
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
            "health_method": getattr(args, "health_method", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
            "bbox": bbox,
            "input_nodata": input_nodata,
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

    # 校验 CLI 参数（前置）
    if args.min_height <= 0:
        raise ValidationError(
            f"--min-height must be > 0 (got {args.min_height})"
        )
    if args.footprint < 3 or args.footprint % 2 == 0:
        raise ValidationError(
            f"--footprint must be odd integer >= 3 (got {args.footprint})"
        )
    if args.closure_threshold < 0:
        raise ValidationError(
            f"--closure-threshold must be >= 0 (got {args.closure_threshold})"
        )

    bbox = list(args.bbox) if args.bbox else None
    n_valid_pixels: Optional[int] = None
    input_nodata: Optional[float] = None

    # 1) 获取数据立方体（通用契约）
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox, src_nodata = read_geotiff_full(args.input)
        input_nodata = src_nodata
        # 若 CLI 同时给 --bbox，先校验之；否则用文件 bbox
        if bbox is not None:
            bbox = validate_bbox(bbox)
        else:
            bbox = validate_bbox(file_bbox)
        # NoData 处理：先把 NoData 替换为 NaN（NaN 在下游算子里安全传播为 0/bare-ground）
        if src_nodata is not None:
            n_total = int(cube.size)
            n_nd = int(np.count_nonzero(cube == src_nodata))
            n_valid_pixels = n_total - n_nd
            if n_valid_pixels == 0:
                raise ValidationError(
                    f"input raster has no valid pixels (all {n_nd}/{n_total} are NoData={src_nodata})",
                    path=args.input, nodata=src_nodata,
                )
            cube = np.where(cube == src_nodata, np.nan, cube).astype(np.float32)
        else:
            n_valid_pixels = int(cube.size)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        cube, synth_info = generate_synthetic_cube(bbox)
        n_valid_pixels = int(cube[0].size)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.ndim != 3 or cube.shape[0] < N_REQUIRED_BANDS:
        raise ValidationError(
            f"input must have >= {N_REQUIRED_BANDS} bands "
            f"({BAND_ROLES}); got shape {cube.shape}",
            bands=int(cube.shape[0] if cube.ndim == 3 else 0),
        )

    # 校验通过后再建输出目录
    os.makedirs(output_dir, exist_ok=True)

    dsm, dtm = cube[0], cube[1]
    red, nir, rededge, sar = cube[2], cube[3], cube[4], cube[5]
    _, h, w = cube.shape

    # 2) CHM + 单木 + 蓄积量
    chm = compute_chm(dsm, dtm)
    px = pixel_size_m(bbox, w)
    trees, summary = estimate_stand(
        chm, pixel_size=px,
        min_height=args.min_height, footprint=args.footprint,
    )

    # 3) 郁闭度
    closure = canopy_closure(chm, threshold=args.closure_threshold)

    # 4) 健康分级
    ndvi_arr = ndvi(nir, red)
    ndre_arr = ndre(nir, rededge)
    grade = health_grade(ndvi_arr, ndre_arr, method=args.health_method)
    g3 = int(np.count_nonzero(grade == 3))
    g2 = int(np.count_nonzero(grade == 2))
    g1 = int(np.count_nonzero(grade == 1))
    veg_total = max(g3 + g2 + g1, 1)
    health_frac = {
        "healthy": g3 / veg_total,
        "moderate": g2 / veg_total,
        "stressed": g1 / veg_total,
    }

    # 5) SAR 生物量
    biomass = sar_biomass_t_ha(sar)

    # 6) 写出产物
    out_chm = os.path.join(output_dir, "chm.tif")
    write_geotiff(out_chm, chm, bbox)
    out_health = os.path.join(output_dir, "health_grade.tif")
    write_geotiff(out_health, grade.astype(np.float32), bbox, nodata=-1.0)
    out_biomass = os.path.join(output_dir, "biomass_t_ha.tif")
    write_geotiff(out_biomass, biomass, bbox)

    closure_arr = (chm > args.closure_threshold).astype(np.float32)
    out_closure = os.path.join(output_dir, "canopy_mask.tif")
    write_geotiff(out_closure, closure_arr, bbox, nodata=-1.0)

    trees_gj = trees_to_geojson(trees, bbox, w, h)
    trees_path = os.path.join(output_dir, "trees.geojson")
    with open(trees_path, "w", encoding="utf-8") as f:
        json.dump(trees_gj, f, ensure_ascii=False)

    advice = management_advice(summary, closure, health_frac)
    report = {
        "source": source_note,
        "pixel_size_m": px,
        "stand": summary,
        "canopy_closure": closure,
        "health_fraction": health_frac,
        "mean_ndvi": float(np.mean(ndvi_arr)),
        "mean_ndre": float(np.mean(ndre_arr)),
        "mean_biomass_t_ha": float(np.mean(biomass)),
        "management": advice,
    }
    report_path = os.path.join(output_dir, "forestry_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_valid_pixels": int(n_valid_pixels) if n_valid_pixels is not None else None,
        "input_nodata": input_nodata,
        "tree_count": summary["tree_count"],
        "total_volume_m3": summary["total_volume_m3"],
        "mean_height_m": summary["mean_height_m"],
        "canopy_closure": closure,
        "mean_biomass_t_ha": float(np.mean(biomass)),
        "health_fraction": health_frac,
    }
    if synth_info is not None:
        qa["synthetic_injected_trees"] = len(synth_info["injected_trees"])

    outputs = [
        {"path": out_chm, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_health, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_biomass, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_closure, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": trees_path, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": len(trees)},
        {"path": report_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox, input_nodata)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] trees: {summary['tree_count']}  "
              f"volume: {summary['total_volume_m3']:.2f} m3  "
              f"mean H: {summary['mean_height_m']:.2f} m")
        print(f"[{SKILL_NAME}] canopy closure: {closure:.3f}")
        print(f"[{SKILL_NAME}] mean biomass: {np.mean(biomass):.2f} t/ha")
        print(f"[{SKILL_NAME}] report: {report_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Precision forestry monitoring: CHM tree height, allometric volume, "
                    "canopy closure, NDVI/NDRE health and SAR biomass fusion.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multi-band GeoTIFF (DSM/DTM/Red/NIR/RedEdge/SAR)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic forest (offline)")
    p.add_argument("--health-method", default="combined",
                   choices=["combined", "ndvi", "ndre"],
                   help="vegetation health grading method (default: combined)")
    p.add_argument("--min-height", type=float, default=2.0,
                   help="minimum tree height for detection, m (default: 2)")
    p.add_argument("--footprint", type=int, default=5,
                   help="local-maximum footprint size in pixels (default: 5)")
    p.add_argument("--closure-threshold", type=float, default=2.0,
                   help="CHM threshold for canopy closure, m (default: 2)")
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
