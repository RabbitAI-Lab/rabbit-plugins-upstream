#!/usr/bin/env python3
"""smart-city-digital-twin — 城市信息模型/数字孪生

把多源地理空间数据（地形 DEM、地表 DSM、建筑高度/足迹）融合为城市数字孪生的
3D 场景配置与 API 接口描述，供前端三维引擎（Cesium / three.js / Unreal 等）消费：

- **3D 建筑体块**：由 DSM−DEM 得建筑高度，结合足迹挤出长方体体块
  (minx,miny,maxx,maxy,base_z,height)，LOD1 级别。
- **场景配置**：统一坐标系、场景 bbox、瓦片方案、LOD 距离阈值、图层清单。
- **API 接口描述**：OpenAPI 风格的 REST 端点清单（瓦片 / 建筑 / 场景元数据）。
- **融合完整性**：校验各图层覆盖率与高度一致性。

数据源：本地多波段 GeoTIFF（DEM/DSM）+ 建筑足迹，或 ``--synthetic`` 生成含
规则建筑街区的模拟城市场景用于离线测试。

隐私声明 / Privacy：默认离线运行，``--synthetic`` 完全无网络；本地处理，不上传数据。

Usage:
    python smart-city-digital-twin.py --input terrain.tif --output-dir ./out
    python smart-city-digital-twin.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "smart-city-digital-twin"

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


BAND_ROLES = ["dem", "dsm"]
N_REQUIRED_BANDS = len(BAND_ROLES)
FORMATS = ["scene", "api", "both"]
DEFAULT_CRS = "EPSG:4326"


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


def validate_bbox(bbox) -> None:
    """Validate bbox: W<E, S<N, lon in [-180,180], lat in [-90,90]."""
    if bbox is None or len(bbox) != 4:
        raise UsageError("bbox must be 4 floats: W S E N")
    w, s, e, n = [float(x) for x in bbox]
    if w >= e:
        raise ValidationError(
            f"invalid bbox: W >= E ({w} >= {e}); cross-180° bboxes not supported, "
            f"split the request into two halves")
    if s >= n:
        raise ValidationError(f"invalid bbox: S >= N ({s} >= {n})")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"invalid bbox: longitude out of [-180,180]: [{w}, {e}]")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"invalid bbox: latitude out of [-90,90]: [{s}, {n}]")
    # Zero-area check
    if abs(e - w) < 1e-9 or abs(n - s) < 1e-9:
        raise ValidationError(f"invalid bbox: zero-area ({w},{s},{e},{n})")


def validate_max_distance(value: float) -> None:
    """Validate --max-distance > 0."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        raise ValidationError(f"max-distance must be a number, got {value!r}")
    if v <= 0:
        raise ValidationError(f"max_distance_km must be > 0, got {v}")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def building_height(dsm: np.ndarray, dem: np.ndarray) -> np.ndarray:
    """建筑/地物高度 = DSM − DEM，负值裁剪为 0。"""
    dsm = np.asarray(dsm, dtype=np.float32)
    dem = np.asarray(dem, dtype=np.float32)
    h = dsm - dem
    h = np.where(np.isfinite(h), h, 0.0)
    return np.clip(h, 0.0, None).astype(np.float32)


def extrude_buildings(
    height: np.ndarray,
    bbox: List[float],
    threshold: float = 3.0,
    max_features: int = 5000,
) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """把高度栅格中连通的高值区挤出为 LOD1 长方体体块。

    用 4-连通域标记，每个连通体块取其外包矩形 + 平均高度。
    返回 (FeatureCollection, 体块属性列表)。
    """
    from scipy.ndimage import label
    h = np.asarray(height, dtype=np.float32)
    H, W = h.shape
    w, s, e, n = bbox
    dx = (e - w) / max(W, 1)
    dy = (n - s) / max(H, 1)

    mask = h >= float(threshold)
    lab, nfeat = label(mask)
    feats = []
    props = []
    for i in range(1, nfeat + 1):
        ys, xs = np.where(lab == i)
        if ys.size == 0:
            continue
        y0, y1 = int(ys.min()), int(ys.max())
        x0, x1 = int(xs.min()), int(xs.max())
        mean_h = float(h[lab == i].mean())
        max_h = float(h[lab == i].max())
        minx = w + x0 * dx
        maxx = w + (x1 + 1) * dx
        maxy = n - y0 * dy
        miny = n - (y1 + 1) * dy
        base_z = 0.0
        geom = {
            "type": "Polygon",
            "coordinates": [[
                [round(minx, 7), round(miny, 7)],
                [round(maxx, 7), round(miny, 7)],
                [round(maxx, 7), round(maxy, 7)],
                [round(minx, 7), round(maxy, 7)],
                [round(minx, 7), round(miny, 7)],
            ]],
        }
        bid = f"bldg_{i:05d}"
        feats.append({"type": "Feature", "id": bid, "geometry": geom,
                      "properties": {"height_m": round(mean_h, 2),
                                     "max_height_m": round(max_h, 2),
                                     "base_z": base_z, "lod": 1}})
        props.append({"id": bid, "minx": minx, "miny": miny, "maxx": maxx, "maxy": maxy,
                      "base_z": base_z, "height_m": mean_h, "max_height_m": max_h})
        if len(feats) >= max_features:
            break
    return {"type": "FeatureCollection", "features": feats}, props


def compute_lod(max_distance_km: float, n_levels: int = 4) -> List[Dict[str, Any]]:
    """按距离分档的 LOD 阈值（近高精度、远低精度）。

    返回 [{lod, max_distance_km}]，距离阈值随 LOD 升高（细节降低）而递增。
    """
    if max_distance_km <= 0:
        raise ValidationError(f"max_distance_km must be > 0, got {max_distance_km}")
    n = max(int(n_levels), 2)
    levels = []
    for i in range(n):
        frac = (i + 1) / n
        levels.append({"lod": i, "max_distance_km": round(float(max_distance_km) * frac, 4)})
    return levels


def tile_scheme(bbox: List[float], base_zoom: int = 14) -> Dict[str, Any]:
    """简易瓦片方案描述（Web Mercator 风格）。"""
    w, s, e, n = bbox
    return {"type": "xyz", "crs": "EPSG:3857", "base_zoom": int(base_zoom),
            "min_zoom": int(base_zoom) - 2, "max_zoom": int(base_zoom) + 4,
            "extent_wgs84": [w, s, e, n]}


def build_scene_config(
    bbox: List[float],
    layers: List[Dict[str, Any]],
    crs: str = DEFAULT_CRS,
    max_distance_km: float = 5.0,
) -> Dict[str, Any]:
    """组装统一的 3D 场景配置。"""
    if len(bbox) != 4 or bbox[0] >= bbox[2] or bbox[1] >= bbox[3]:
        raise ValidationError(f"invalid bbox: {bbox}")
    return {
        "version": VERSION,
        "crs": crs,
        "bbox_wgs84": [float(x) for x in bbox],
        "center": [0.5 * (bbox[0] + bbox[2]), 0.5 * (bbox[1] + bbox[3])],
        "layers": layers,
        "lod_levels": compute_lod(max_distance_km),
        "tiles": tile_scheme(bbox),
        "units": {"horizontal": "degree", "vertical": "meter"},
    }


def build_api_spec(base_url: str = "https://api.example.org/twin") -> Dict[str, Any]:
    """OpenAPI 风格的接口描述（端点清单）。"""
    paths = {
        "/scene": {"get": {"summary": "获取场景配置", "responses": {"200": "scene config JSON"}}},
        "/tiles/{z}/{x}/{y}.png": {"get": {"summary": "获取瓦片", "responses": {"200": "PNG tile"}}},
        "/buildings": {"get": {"summary": "列出建筑体块", "responses": {"200": "GeoJSON"}}},
        "/buildings/{id}": {"get": {"summary": "获取单个建筑", "responses": {"200": "building JSON"}}},
        "/terrain": {"get": {"summary": "获取地形网格", "responses": {"200": "quantized-mesh"}}},
        "/health": {"get": {"summary": "服务健康检查", "responses": {"200": "ok"}}},
    }
    return {"openapi": "3.0.0", "info": {"title": "Smart City Digital Twin API",
                                         "version": VERSION},
            "servers": [{"url": base_url}], "paths": paths}


def fusion_completeness(dem: np.ndarray, dsm: np.ndarray, n_buildings: int) -> Dict[str, Any]:
    """融合完整性校验：各图层覆盖率与高度一致性（NaN 安全）。"""
    dem = np.asarray(dem, dtype=np.float32)
    dsm = np.asarray(dsm, dtype=np.float32)
    total = dem.size
    dem_valid = int(np.count_nonzero(np.isfinite(dem)))
    dsm_valid = int(np.count_nonzero(np.isfinite(dsm)))
    dem_cov = float(dem_valid) / max(total, 1)
    dsm_cov = float(dsm_valid) / max(total, 1)
    h = building_height(dsm, dem)
    h_valid_mask = np.isfinite(h)
    h_valid = int(h_valid_mask.sum())
    mean_h = float(np.nanmean(h)) if h_valid > 0 else 0.0
    max_h = float(np.nanmax(h)) if h_valid > 0 else 0.0
    return {
        "dem_coverage": dem_cov, "dsm_coverage": dsm_cov,
        "n_buildings": int(n_buildings),
        "mean_height_m": mean_h, "max_height_m": max_h,
        "n_valid_pixels": h_valid, "n_total_pixels": int(total),
        "consistent": bool(dem_cov > 0.9 and dsm_cov > 0.9),
    }


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic_scene(
    bbox: List[float], width: int = 128, height: int = 128, seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (2,H,W)：DEM/DSM，含规则街区建筑。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    dem = (40.0 + 5.0 * np.sin(np.pi * xx / width) + rng.normal(0, 0.3, (height, width))).astype(np.float32)
    dsm = dem.copy()

    # 规则街区：网格上放置建筑方块（高 9~45m）
    buildings = 0
    for gy in range(1, height - 6, 10):
        for gx in range(1, width - 6, 10):
            if rng.random() < 0.7:
                bh = float(rng.uniform(9, 45))
                bw = int(rng.integers(3, 6))
                dsm[gy:gy + bw, gx:gx + bw] = dem[gy:gy + bw, gx:gx + bw] + bh
                buildings += 1

    cube = np.stack([dem, dsm], axis=0).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "band_roles": BAND_ROLES, "n_buildings_injected": buildings}
    return cube, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path, cube, bbox, nodata=-9999.0, dtype="float32"):
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


def read_geotiff(path):
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None),
                "format": getattr(args, "format", None),
                "synthetic": bool(getattr(args, "synthetic", False)), "bbox": bbox},
        outputs=[OutputFile(**o) for o in outputs], qa=qa,
        software={"python": sys.version.split()[0], "skill": SKILL_NAME},
    )
    path = os.path.join(output_dir, "output-manifest.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(man.to_dict(), f, ensure_ascii=False, indent=2, default=str)
    return path


def process(args):
    started_at = _utc_now()
    output_dir = args.output_dir
    bbox = list(args.bbox) if args.bbox else None

    # --- Upfront validation (BEFORE makedirs; rc=6 for bad data, rc=2 for bad CLI) ---
    if args.bbox is not None:
        validate_bbox(args.bbox)
    validate_max_distance(args.max_distance)

    # --- Mode dispatch ---
    synth_info = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, synth_info = generate_synthetic_scene(bbox)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.ndim != 3 or cube.shape[0] < N_REQUIRED_BANDS:
        raise ValidationError(
            f"input must have >= {N_REQUIRED_BANDS} bands ({BAND_ROLES}); got {cube.shape}")
    if bbox is None:
        raise ValidationError("bbox is required")

    # Re-validate bbox when sourced from --input (clamp to file_bbox if user passed one)
    if args.bbox is None:
        validate_bbox(bbox)

    # --- Output dir (only after all upfront validation passes) ---
    os.makedirs(output_dir, exist_ok=True)

    dem, dsm = cube[0], cube[1]
    height = building_height(dsm, dem)

    out_height = os.path.join(output_dir, "building_height.tif")
    write_geotiff(out_height, height, bbox)

    outputs = [{"path": out_height, "kind": "raster", "crs_epsg": 4326,
                "bbox_wgs84": bbox, "band_count": 1}]
    qa: Dict[str, Any] = {"source": source_note, "format": args.format,
                          "input_nodata": -9999.0}

    gj, props = extrude_buildings(height, bbox, threshold=args.height_threshold)
    n_bldg = len(props)
    qa["n_buildings"] = n_bldg
    completeness = fusion_completeness(dem, dsm, n_bldg)
    qa.update(completeness)

    if args.format in ("scene", "both"):
        buildings_path = os.path.join(output_dir, "buildings_3d.geojson")
        with open(buildings_path, "w", encoding="utf-8") as f:
            json.dump(gj, f, ensure_ascii=False)
        outputs.append({"path": buildings_path, "kind": "vector", "crs_epsg": 4326,
                        "bbox_wgs84": bbox, "feature_count": n_bldg})

        layers = [
            {"id": "terrain", "type": "dem", "source": "dem", "crs": DEFAULT_CRS},
            {"id": "surface", "type": "dsm", "source": "dsm", "crs": DEFAULT_CRS},
            {"id": "buildings", "type": "3d-tiles", "source": "buildings_3d.geojson",
             "lod": 1, "count": n_bldg},
        ]
        scene = build_scene_config(bbox, layers, crs=DEFAULT_CRS, max_distance_km=args.max_distance)
        scene["fusion"] = completeness
        scene_path = os.path.join(output_dir, "scene_config.json")
        with open(scene_path, "w", encoding="utf-8") as f:
            json.dump(scene, f, ensure_ascii=False, indent=2)
        outputs.append({"path": scene_path, "kind": "json"})

    if args.format in ("api", "both"):
        api = build_api_spec(base_url=args.base_url)
        api["stats"] = {"n_buildings": n_bldg, "bbox_wgs84": [float(x) for x in bbox]}
        api_path = os.path.join(output_dir, "api_spec.json")
        with open(api_path, "w", encoding="utf-8") as f:
            json.dump(api, f, ensure_ascii=False, indent=2)
        outputs.append({"path": api_path, "kind": "json"})

    report = {"source": source_note, "format": args.format, "n_buildings": n_bldg,
              "fusion": completeness}
    report_path = os.path.join(output_dir, "twin_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    outputs.append({"path": report_path, "kind": "json"})

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  format: {args.format}")
        print(f"[{SKILL_NAME}] buildings (LOD1): {n_bldg}  mean height: {completeness['mean_height_m']:.2f} m")
        print(f"[{SKILL_NAME}] fusion consistent: {completeness['consistent']}")
        print(f"[{SKILL_NAME}] report: {report_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser():
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Smart city digital twin: multi-source fusion to 3D scene config + API spec.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input multi-band GeoTIFF (DEM/DSM)")
    p.add_argument("--synthetic", action="store_true")
    p.add_argument("--format", default="both", choices=FORMATS,
                   help="output format (default: both)")
    p.add_argument("--height-threshold", type=float, default=3.0,
                   help="min height (m) to be a building (default: 3)")
    p.add_argument("--max-distance", type=float, default=5.0,
                   help="max LOD distance km (default: 5)")
    p.add_argument("--base-url", default="https://api.example.org/twin", help="API base URL")
    p.add_argument("--output-dir", default="./output")
    p.add_argument("--quiet", action="store_true")
    p.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return p


def main(argv=None):
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
