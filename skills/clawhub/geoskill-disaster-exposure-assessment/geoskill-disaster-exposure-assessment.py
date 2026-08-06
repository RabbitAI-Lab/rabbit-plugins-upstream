#!/usr/bin/env python3
"""disaster-exposure-assessment — 灾害暴露度评估

将灾害危险区与资产/人口做空间叠加，统计暴露量：

- **栅格叠加**：逐像元 暴露量 = 危险区内资产/人口之和（精确）
- **分级统计**：按危险等级分区汇总暴露量
- **矢量叠加**：资产点位与危险区多边形空间连接（geopandas.sjoin），统计落入危险区的点位价值

输出暴露统计 JSON、危险区矢量边界（GeoJSON）与暴露掩膜（GeoTIFF）。

数据源：本地多波段 GeoTIFF（band1=危险强度、band2=资产价值、band3=人口），
或 ``--synthetic`` 生成场景（含资产点位）。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python disaster-exposure-assessment.py --input region.tif --threshold 1.0
    python disaster-exposure-assessment.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "disaster-exposure-assessment"

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
# 校验：bbox / breaks
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """P0: bbox 合法性前置校验。"""
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            f"bbox must be a 4-element [W S E N]; got {bbox!r}"
        )
    try:
        w, s, e, n = [float(v) for v in bbox]
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox values must be numeric; got {bbox!r}") from exc
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range [-180, 180]: W={w}, E={e}"
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range [-90, 90]: S={s}, N={n}"
        )
    if w >= e:
        if w > 0 and e < 0 and (e - w) > -360:
            raise ValidationError(
                f"bbox W ({w}) >= E ({e}); cross-180° antimeridian is not "
                f"supported — split into two extents"
            )
        raise ValidationError(f"bbox W ({w}) must be < E ({e})")
    if s >= n:
        raise ValidationError(f"bbox S ({s}) must be < N ({n})")
    area = (e - w) * (n - s)
    if area <= 0:
        raise ValidationError(f"bbox area must be > 0; got {area}")


def validate_breaks(breaks) -> None:
    """P1: --breaks 必须是非空且严格递增的实数列表。"""
    if not breaks or len(breaks) < 1:
        raise UsageError("--breaks must be a non-empty list of thresholds")
    for b in breaks:
        if not isinstance(b, (int, float)) or float(b) != float(b):  # NaN check
            raise UsageError(f"--breaks values must be finite; got {b!r}")
    breaks_f = [float(b) for b in breaks]
    for i in range(1, len(breaks_f)):
        if breaks_f[i] <= breaks_f[i - 1]:
            raise UsageError(
                f"--breaks must be strictly increasing; got {breaks_f}"
            )


# ---------------------------------------------------------------------------
# 核心算法：栅格叠加
# ---------------------------------------------------------------------------
def exposed_total(hazard_mask: np.ndarray, value: np.ndarray) -> float:
    """危险区内价值总和（精确）：Σ value[mask]。mask 为布尔危险区。"""
    if np.shape(hazard_mask) != np.shape(value):
        raise ValidationError("hazard_mask/value shape mismatch")
    mask = np.asarray(hazard_mask, dtype=bool)
    v = np.asarray(value, dtype=np.float64)
    return float(np.sum(v[mask]))


def exposure_fraction(hazard_mask: np.ndarray, value: np.ndarray) -> float:
    """暴露价值占总价值的比例 [0,1]。"""
    total = float(np.sum(np.asarray(value, dtype=np.float64)))
    if total <= 1e-12:
        return 0.0
    return exposed_total(hazard_mask, value) / total


def exposure_by_zone(zones: np.ndarray, value: np.ndarray) -> Dict[int, float]:
    """按分区（整型栅格）汇总价值：{zone_id: 区内价值总和}。各区之和 = 全区总和。"""
    if np.shape(zones) != np.shape(value):
        raise ValidationError("zones/value shape mismatch")
    z = np.asarray(zones)
    v = np.asarray(value, dtype=np.float64)
    out: Dict[int, float] = {}
    for zi in np.unique(z):
        out[int(zi)] = float(np.sum(v[z == zi]))
    return out


def classify_hazard(intensity: np.ndarray, breaks: Tuple[float, ...] = (0.5, 1.5)) -> np.ndarray:
    """危险强度分级：0=无/低,1=中,2=高。intensity<=0 视为无危险(zone 0)。"""
    a = np.asarray(intensity, dtype=np.float64)
    z = np.digitize(a, list(breaks)).astype(np.int16)
    z[a <= 0] = 0
    return z


# ---------------------------------------------------------------------------
# 核心算法：矢量叠加（geopandas + shapely）
# ---------------------------------------------------------------------------
def point_exposure(points_xy: np.ndarray, values: np.ndarray, polygon) -> Tuple[float, int]:
    """资产点位与危险区多边形的空间连接：返回 (落入区内的价值总和, 点数)。

    使用 geopandas.sjoin(predicate='within') + shapely 几何。
    """
    import geopandas as gpd
    from shapely.geometry import Point
    pts = np.asarray(points_xy, dtype=np.float64)
    vals = np.asarray(values, dtype=np.float64)
    if pts.ndim != 2 or pts.shape[1] != 2:
        raise ValidationError("points_xy must be (N,2)")
    if pts.shape[0] != vals.shape[0]:
        raise ValidationError("points_xy/values length mismatch")
    if pts.shape[0] == 0:
        return 0.0, 0
    gdf_pts = gpd.GeoDataFrame({"value": vals},
                               geometry=[Point(x, y) for x, y in pts], crs="EPSG:4326")
    gdf_zone = gpd.GeoDataFrame(geometry=[polygon], crs="EPSG:4326")
    joined = gpd.sjoin(gdf_pts, gdf_zone, how="inner", predicate="within")
    return float(joined["value"].sum()), int(len(joined))


def vectorize_mask(mask: np.ndarray, transform) -> List[Any]:
    """栅格危险区掩膜 → shapely 多边形列表（rasterio.features + shapely）。"""
    import rasterio.features
    from shapely.geometry import shape
    polys = []
    m = np.asarray(mask, dtype=np.uint8)
    for geom, _val in rasterio.features.shapes(m, mask=m.astype(bool), transform=transform):
        polys.append(shape(geom))
    return polys


def write_zones_geojson(path: str, polygons: List[Any], crs_epsg: int = 4326) -> int:
    """把 shapely 多边形列表写成 GeoJSON FeatureCollection，返回要素数。"""
    from shapely.geometry import mapping
    feats = []
    for i, poly in enumerate(polygons):
        feats.append({"type": "Feature", "properties": {"zone_id": i, "area_deg2": float(poly.area)},
                      "geometry": mapping(poly)})
    fc = {"type": "FeatureCollection", "features": feats}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(fc, f, ensure_ascii=False, indent=2)
    return len(feats)


# ---------------------------------------------------------------------------
# 合成数据：危险强度场 + 资产价值 + 人口 + 资产点位
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64,
                       seed: int = 42) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float64) / max(width - 1, 1)
    yn = yy.astype(np.float64) / max(height - 1, 1)
    hazard = np.clip(2.0 * np.exp(-(((xn - 0.4) ** 2 + (yn - 0.5) ** 2)) / (2 * 0.2 ** 2))
                     + rng.normal(0, 0.05, (height, width)), 0, None)
    asset = np.clip(1000.0 * np.exp(-(((xn - 0.5) ** 2 + (yn - 0.5) ** 2)) / (2 * 0.3 ** 2))
                    + rng.normal(0, 20, (height, width)), 0, None)
    population = np.clip(500.0 * np.exp(-(((xn - 0.5) ** 2 + (yn - 0.45) ** 2)) / (2 * 0.28 ** 2))
                         + rng.normal(0, 10, (height, width)), 0, None)
    # 资产点位（经纬度），部分落在危险区
    n_pts = 50
    px = rng.uniform(bbox[0], bbox[2], n_pts)
    py = rng.uniform(bbox[1], bbox[3], n_pts)
    pvals = rng.uniform(100, 5000, n_pts)
    layers = {"hazard": hazard.astype(np.float32), "asset": asset.astype(np.float32),
              "population": population.astype(np.float32),
              "points_xy": np.column_stack([px, py]), "point_values": pvals}
    info = {"bbox": bbox, "width": width, "height": height, "n_points": n_pts}
    return layers, info


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
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=False).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    return cube, bbox


def read_nodata(path: str) -> Optional[float]:
    """从 GeoTIFF 文件读 nodata 值（不读数据）。用于记录到 qa。"""
    import rasterio
    with rasterio.open(path) as src:
        return src.nodata


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

    # 0) 参数前置校验（P0/P1）
    if args.synthetic or not args.input:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
    validate_breaks(list(args.breaks))

    points_xy = None
    point_values = None
    input_nodata: Optional[float] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        input_nodata = read_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if cube.shape[0] < 3:
            raise ValidationError("input needs >=3 bands (hazard, asset_value, population)")
        hazard, asset, population = cube[0], cube[1], cube[2]
        source_note = args.input
    else:
        layers, _info = generate_synthetic(bbox)
        hazard, asset, population = layers["hazard"], layers["asset"], layers["population"]
        points_xy, point_values = layers["points_xy"], layers["point_values"]
        source_note = "synthetic"

    # 1) bbox + NoData 校验（前置，确保无效输入不创建 output 目录）
    if bbox is not None:
        validate_bbox(bbox)
    n_valid = int(np.count_nonzero(np.isfinite(hazard)))
    if n_valid == 0:
        raise ValidationError(
            "input hazard raster has no valid pixels (all NoData/NaN); nothing to assess"
        )

    # 2) 所有校验通过后才创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    zones = classify_hazard(hazard, breaks=tuple(args.breaks))
    hazard_mask = zones >= 1  # 任一危险等级都算暴露区

    exposed_asset = exposed_total(hazard_mask, asset)
    exposed_pop = exposed_total(hazard_mask, population)
    asset_frac = exposure_fraction(hazard_mask, asset)
    by_zone = exposure_by_zone(zones, asset)

    # 栅格输出
    mask_tif = os.path.join(output_dir, "exposed_mask.tif")
    write_geotiff(mask_tif, hazard_mask.astype("int16"), bbox, nodata=-1, dtype="int16")

    # 矢量化危险区
    from rasterio.transform import from_bounds
    H, W = hazard.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], W, H)
    polys = vectorize_mask(hazard_mask, transform)
    zones_geojson = os.path.join(output_dir, "hazard_zone.geojson")
    n_feat = write_zones_geojson(zones_geojson, polys)

    # 矢量点位暴露（合成/有点位时）
    point_stats = None
    if points_xy is not None and len(polys) > 0:
        from shapely.ops import unary_union
        union_poly = unary_union(polys)
        pv, pn = point_exposure(points_xy, point_values, union_poly)
        point_stats = {"exposed_point_value": pv, "exposed_point_count": pn,
                       "total_points": int(len(point_values))}

    stats = {
        "source": source_note,
        "breaks": list(args.breaks),
        "exposed_asset_value": exposed_asset,
        "exposed_population": exposed_pop,
        "asset_exposure_fraction": asset_frac,
        "exposed_pixel_fraction": float(np.mean(hazard_mask)),
        "exposure_by_zone": {str(k): v for k, v in by_zone.items()},
        "point_exposure": point_stats,
        "input_nodata": input_nodata,
        "n_valid_pixels": n_valid,
    }
    stats_path = os.path.join(output_dir, "exposure_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "exposed_asset_value": exposed_asset,
        "exposed_population": exposed_pop,
        "asset_exposure_fraction": asset_frac,
        "zone_feature_count": n_feat,
        "n_valid_pixels": n_valid,
        "input_nodata": input_nodata,
    }
    outputs = [
        {"path": mask_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": zones_geojson, "kind": "vector", "crs_epsg": 4326, "feature_count": n_feat},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, {"input": args.input, "bbox": bbox, "breaks": args.breaks,
                              "synthetic": bool(args.synthetic)}, outputs, qa, started_at, 0)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] exposed asset: {exposed_asset:.1f}  exposed pop: {exposed_pop:.1f}")
        print(f"[{SKILL_NAME}] asset exposure fraction: {asset_frac:.3f}  zone features: {n_feat}")
        print(f"[{SKILL_NAME}] outputs: {output_dir}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Disaster exposure assessment (hazard x asset/population spatial overlay).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoTIFF (band1=hazard intensity, band2=asset value, band3=population)")
    p.add_argument("--breaks", nargs="+", type=float, default=[0.5, 1.5],
                   help="hazard classification thresholds (default: 0.5 1.5)")
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
