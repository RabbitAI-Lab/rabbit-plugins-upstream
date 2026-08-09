#!/usr/bin/env python3
"""sar-flood-mapping — SAR洪水制图

利用静水在 SAR 影像上的镜面散射（极低后向散射）特性提取洪水范围：

1. **Otsu 阈值分割**：对 σ⁰ 直方图做双峰分类，最大化类间方差求最优阈值，
   把低于阈值的像元判为候选水体（手写直方图法，不依赖 scikit-image）。
2. **形态学开运算**：``binary_opening``（3×3 结构元）去除孤立噪声像元，
   保持水体连通性。
3. **坡度排除**（可选）：若提供 ``--dem``，计算地表坡度，剔除坡度大于
   ``--max-slope`` 的像元（陡坡上的低 σ⁰ 多为阴影/叠掩，而非静水）。
4. **矢量化**：用 ``rasterio.features.shapes`` 把二值掩膜转为多边形，
   导出 GeoJSON。

数据源：本地 SAR 强度/后向散射 GeoTIFF（线性 σ⁰），或使用 ``--synthetic``
生成含蜿蜒河道与洪泛块的低值水体场景（真值掩膜可用于精度验证）。

隐私声明 / Privacy：
- 默认完全离线运行，不发起任何网络请求。
- ``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python sar-flood-mapping.py --input sar.tif --threshold auto --output-dir ./out
    python sar-flood-mapping.py --bbox 116 39 117 40 --synthetic

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
SKILL_NAME = "sar-flood-mapping"

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


def parse_threshold(spec: str) -> Optional[float]:
    """解析 --threshold：'auto' → None（走 Otsu），否则浮点数。"""
    s = str(spec).strip().lower()
    if s == "auto":
        return None
    try:
        return float(s)
    except ValueError:
        raise UsageError(
            f"--threshold must be 'auto' or a number, got '{spec}'", threshold=spec,
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def otsu_threshold(values: np.ndarray, nbins: int = 128) -> float:
    """Otsu 类间方差最大化阈值（手写直方图法）。

    输入任意形状数组，忽略非有限值，返回最优分割阈值。
    """
    vals = np.asarray(values, dtype=np.float64).ravel()
    vals = vals[np.isfinite(vals)]
    if vals.size == 0:
        raise ValidationError("no finite values for Otsu thresholding")
    vmin, vmax = float(vals.min()), float(vals.max())
    if vmax <= vmin:
        return float(vmin)
    hist, edges = np.histogram(vals, bins=nbins, range=(vmin, vmax))
    centers = 0.5 * (edges[:-1] + edges[1:])
    hist = hist.astype(np.float64)
    total = hist.sum()
    if total == 0:
        return float(centers[0])

    csum = np.cumsum(hist)
    msum = np.cumsum(hist * centers)
    mean_total = msum[-1]

    w0 = csum
    w1 = total - csum
    with np.errstate(divide="ignore", invalid="ignore"):
        mu0 = msum / np.where(w0 > 0, w0, 1.0)
        mu1 = (mean_total - msum) / np.where(w1 > 0, w1, 1.0)
    between = np.where((w0 > 0) & (w1 > 0), w0 * w1 * (mu0 - mu1) ** 2, 0.0)
    idx = int(np.argmax(between))
    return float(centers[idx])


def slope_from_dem(dem: np.ndarray, res_x: float, res_y: float) -> np.ndarray:
    """由 DEM 计算坡度（度）。res_x/res_y 为像元尺寸（同 DEM 单位）。"""
    dem = np.asarray(dem, dtype=np.float32)
    if dem.ndim != 2:
        raise ValidationError(f"DEM must be 2-D, got shape {dem.shape}", shape=list(dem.shape))
    gy, gx = np.gradient(dem, float(res_y), float(res_x), edge_order=1)
    slope_rad = np.arctan(np.sqrt(gx * gx + gy * gy))
    return np.rad2deg(slope_rad).astype(np.float32)


def extract_water(
    sigma: np.ndarray,
    threshold: Optional[float] = None,
    dem: Optional[np.ndarray] = None,
    res_x: float = 1.0,
    res_y: float = 1.0,
    max_slope_deg: float = 15.0,
    opening: bool = True,
) -> Tuple[np.ndarray, float]:
    """从 σ⁰ 场提取水体掩膜。

    返回 (mask uint8 0/1, threshold_used)。``threshold=None`` 时用 Otsu。
    """
    from scipy.ndimage import binary_opening

    sigma = np.asarray(sigma, dtype=np.float32)
    if sigma.ndim != 2:
        raise ValidationError(f"sigma must be 2-D, got shape {sigma.shape}", shape=list(sigma.shape))

    thr = otsu_threshold(sigma) if threshold is None else float(threshold)
    mask = (sigma < thr)
    mask &= np.isfinite(sigma)

    if dem is not None:
        slope = slope_from_dem(dem, res_x, res_y)
        mask &= slope <= max_slope_deg

    if opening:
        struct = np.ones((3, 3), dtype=bool)
        mask = binary_opening(mask, structure=struct)

    return mask.astype(np.uint8), thr


def flood_area_stats(
    mask: np.ndarray,
    bbox: List[float],
) -> Dict[str, Any]:
    """面积统计：像元数、占比、近似面积（km²）。

    用 bbox 中点纬度把度换算为米（1° lat ≈ 110540 m，1° lon ≈ 111320·cos(lat) m）。
    """
    h, w = mask.shape
    water_px = int(mask.sum())
    total_px = int(mask.size)
    lat_mid = 0.5 * (bbox[1] + bbox[3])
    px_w_m = (bbox[2] - bbox[0]) / max(w, 1) * 111320.0 * np.cos(np.deg2rad(lat_mid))
    px_h_m = (bbox[3] - bbox[1]) / max(h, 1) * 110540.0
    area_km2 = water_px * (px_w_m * px_h_m) / 1e6
    return {
        "water_pixels": water_px,
        "total_pixels": total_px,
        "water_fraction": float(water_px / total_px) if total_px else 0.0,
        "area_km2": float(area_km2),
        "pixel_area_m2": float(px_w_m * px_h_m),
    }


def vectorize_mask(mask: np.ndarray, transform) -> Dict[str, Any]:
    """把二值掩膜矢量化为 GeoJSON FeatureCollection（EPSG:4326）。"""
    from rasterio.features import shapes

    feats = []
    gen = shapes(mask.astype("uint8"), mask=mask.astype(bool), transform=transform)
    for geom, value in gen:
        if int(value) == 1:
            feats.append({
                "type": "Feature",
                "properties": {"class": "flood_water", "value": 1},
                "geometry": geom,
            })
    return {
        "type": "FeatureCollection",
        "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
        "features": feats,
    }


def write_geojson(path: str, fc: Dict[str, Any]) -> None:
    """用 geopandas 写 GeoJSON（保证 CRS/编码一致）。"""
    import geopandas as gpd

    if fc["features"]:
        gdf = gpd.GeoDataFrame.from_features(fc["features"], crs="EPSG:4326")
    else:
        gdf = gpd.GeoDataFrame({"class": [], "geometry": []}, crs="EPSG:4326")
        gdf = gdf.set_geometry("geometry")
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    gdf.to_file(path, driver="GeoJSON")


# ---------------------------------------------------------------------------
# 合成数据：σ⁰ 场 + 低值水体（蜿蜒河道 + 洪泛块）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (1, H, W) 含水体场景的 σ⁰ 立方体（线性强度）+ 真值掩膜。

    背景为平滑 σ⁰ 场（~0.05）叠加乘性斑斑噪声；水体为蜿蜒河道 + 一个
    洪泛矩形块，σ⁰ 极低（~0.003）。返回 (cube, info)。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yn = yy / max(height - 1, 1)
    xn = xx / max(width - 1, 1)

    # 背景 σ⁰ 场
    background = 0.05 + 0.01 * np.sin(2.0 * np.pi * xn) + 0.01 * np.cos(2.0 * np.pi * yn)

    # 水体真值掩膜：蜿蜒河道 + 洪泛块
    river_center = 0.55 + 0.18 * np.sin(2.5 * np.pi * xn)
    river = np.abs(yn - river_center) < 0.05
    flood_block = (xn > 0.60) & (xn < 0.85) & (yn > 0.08) & (yn < 0.30)
    water_truth = (river | flood_block).astype(np.uint8)

    sigma = np.where(water_truth > 0, 0.003, background).astype(np.float32)
    # 乘性斑斑噪声（保持水/陆双峰）
    sigma = sigma * np.exp(rng.normal(0.0, 0.18, size=sigma.shape)).astype(np.float32)
    sigma = np.clip(sigma, 1e-5, None).astype(np.float32)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "water_truth": water_truth,
        "truth_water_fraction": float(water_truth.mean()),
    }
    return sigma[np.newaxis, ...], info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    cube: np.ndarray,
    bbox: List[float],
    nodata: float = -9999.0,
) -> None:
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
    """校验地理 bbox 合法性，失败抛 ValidationError（exit 6）。"""
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
            "threshold": getattr(args, "threshold", None),
            "dem": getattr(args, "dem", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
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
    bbox = list(args.bbox) if args.bbox else None
    thr_spec = parse_threshold(args.threshold)

    # 校验 CLI 参数（前置）
    if not (0.0 <= args.max_slope <= 90.0):
        raise ValidationError(
            f"--max-slope must be in [0, 90] degrees (got {args.max_slope})"
        )
    if thr_spec is not None and thr_spec < 0:
        raise ValidationError(
            f"--threshold must be >= 0 (linear sigma0; got {thr_spec})"
        )

    # 1) 获取 σ⁰
    synth_info: Optional[Dict[str, Any]] = None
    input_nodata: Optional[float] = None
    n_valid_pixels: Optional[int] = None
    if args.input and not args.synthetic:
        cube, file_bbox, src_nodata = read_geotiff_full(args.input)
        input_nodata = src_nodata
        if bbox is not None:
            bbox = validate_bbox(bbox)
        else:
            bbox = validate_bbox(file_bbox)
        if cube.shape[0] < 1:
            raise ValidationError(
                f"input raster must have >= 1 band, got {cube.shape[0]}"
            )
        # NoData 处理
        if src_nodata is not None:
            n_total = int(cube[0].size)
            n_nd = int(np.count_nonzero(cube[0] == src_nodata))
            n_valid_pixels = n_total - n_nd
            if n_valid_pixels == 0:
                raise ValidationError(
                    f"input raster has no valid pixels "
                    f"(all {n_nd}/{n_total} are NoData={src_nodata})",
                    path=args.input, nodata=src_nodata,
                )
            cube = np.where(cube == src_nodata, np.nan, cube).astype(np.float32)
        else:
            n_valid_pixels = int(cube[0].size)
        sigma = cube[0]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        cube, synth_info = generate_synthetic(bbox)
        sigma = cube[0]
        n_valid_pixels = int(sigma.size)
        source_note = "synthetic"

    if sigma.size == 0:
        raise ValidationError("input raster is empty")

    # 校验通过后再建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 2) 可选 DEM 坡度排除
    dem = None
    if args.dem:
        dem_cube, _ = read_geotiff(args.dem)
        dem = dem_cube[0]
        if dem.shape != sigma.shape:
            raise ValidationError(
                f"DEM shape {dem.shape} != SAR shape {sigma.shape}",
                dem_shape=list(dem.shape), sar_shape=list(sigma.shape),
            )

    h, w = sigma.shape
    res_x = (bbox[2] - bbox[0]) / max(w, 1)
    res_y = (bbox[3] - bbox[1]) / max(h, 1)

    mask, thr_used = extract_water(
        sigma, threshold=thr_spec, dem=dem,
        res_x=res_x, res_y=res_y, max_slope_deg=args.max_slope,
    )

    stats = flood_area_stats(mask, bbox)
    stats["threshold_used"] = float(thr_used)
    stats["threshold_mode"] = "auto_otsu" if thr_spec is None else "manual"
    stats["slope_exclusion"] = dem is not None

    # 3) 写出产物
    out_tif = os.path.join(output_dir, "flood_extent.tif")
    write_geotiff(out_tif, mask.astype(np.float32), bbox, nodata=-1.0)

    stats_path = os.path.join(output_dir, "flood_area_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    from rasterio.transform import from_bounds
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    fc = vectorize_mask(mask, transform)
    geojson_path = os.path.join(output_dir, "flood_extent.geojson")
    write_geojson(geojson_path, fc)

    qa: Dict[str, Any] = {
        "source": source_note,
        "threshold_used": float(thr_used),
        "water_fraction": stats["water_fraction"],
        "area_km2": stats["area_km2"],
        "n_polygons": len(fc["features"]),
        "n_valid_pixels": int(n_valid_pixels) if n_valid_pixels is not None else None,
        "input_nodata": input_nodata,
    }
    if synth_info is not None:
        truth = synth_info["water_truth"]
        # 与真值的一致性（IoU）
        inter = float(np.logical_and(mask > 0, truth > 0).sum())
        union = float(np.logical_or(mask > 0, truth > 0).sum())
        qa["synthetic_iou"] = inter / union if union > 0 else 0.0
        qa["synthetic_truth_water_fraction"] = synth_info["truth_water_fraction"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": geojson_path, "kind": "vector", "crs_epsg": 4326},
        {"path": stats_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox,
                              input_nodata=input_nodata)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] threshold: {thr_used:.6f} ({stats['threshold_mode']})")
        print(f"[{SKILL_NAME}] water fraction: {stats['water_fraction']:.4f}  "
              f"area: {stats['area_km2']:.4f} km2")
        print(f"[{SKILL_NAME}] polygons: {len(fc['features'])}")
        print(f"[{SKILL_NAME}] raster: {out_tif}")
        print(f"[{SKILL_NAME}] vector: {geojson_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="SAR flood extent mapping via Otsu thresholding of low backscatter.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input SAR intensity/backscatter GeoTIFF (linear sigma0)")
    p.add_argument("--threshold", default="auto",
                   help="'auto' (Otsu) or a numeric sigma0 threshold (default: auto)")
    p.add_argument("--dem", default=None, help="optional DEM GeoTIFF for slope exclusion")
    p.add_argument("--max-slope", type=float, default=15.0,
                   help="max slope (deg) to keep as water when --dem given (default: 15)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic scene (offline)")
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
