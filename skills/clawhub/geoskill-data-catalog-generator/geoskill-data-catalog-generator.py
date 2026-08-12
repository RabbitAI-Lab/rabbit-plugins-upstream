#!/usr/bin/env python3
"""data-catalog-generator — 数据目录生成器

扫描目录中的地理数据文件（栅格 + 矢量），提取元数据并分类，生成可浏览的
数据目录（HTML + CSV + JSON）：

- **扫描**：递归/非递归遍历目录，按扩展名识别栅格与矢量文件。
- **元数据提取**：栅格读尺寸/波段/CRS/范围/分辨率（rasterio）；矢量读要素
  数/几何类型/CRS/范围/字段（geopandas）。无法解析的文件记为 error 而不中断。
- **分类**：按数据类型细分（单波段/多光谱/高光谱；点/线/面/混合）与 CRS
  家族（WGS84 / Web Mercator / 投影 / 未知）。
- **目录输出**：catalog.csv（每文件一行）、catalog.html（带汇总的表格）、
  catalog.json（机读）。

数据源：本地目录或文件（``--input``），或 ``--synthetic`` 模式生成 tif /
geojson / shp / gpkg 混合源集（离线）。

隐私声明 / Privacy：
- 默认完全离线运行，``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python data-catalog-generator.py --input ./data --recursive
    python data-catalog-generator.py --bbox 116 39 117 40 --synthetic --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import html
import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "data-catalog-generator"

RASTER_EXTS = {".tif", ".tiff"}
VECTOR_EXTS = {".geojson", ".json", ".shp", ".gpkg"}
# shapefile 辅助文件不作为独立条目
SHP_AUX_EXTS = {".shx", ".dbf", ".prj", ".cpg"}

# ---- 共享核心库（本地 vendored，随脚本目录一起分发）----
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


def validate_bbox(bbox: List[float]) -> List[float]:
    """Validate WGS-84 bbox; raise ValidationError (rc=6) on bad input.

    Rules:
      - W < E, S < N
      - abs values <= 360/180
      - bbox area >= 1e-8 deg^2
    Cross-180° antimeridian is rejected with a hint to split into two extents.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats: W S E N")
    w, s, e, n = [float(x) for x in bbox]
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError("bbox values must be finite")
    if w >= e:
        raise ValidationError(
            f"bbox W ({w}) must be < E ({e}); cross-180° antimeridian is not supported — split into two extents"
        )
    if s >= n:
        raise ValidationError(f"bbox S ({s}) must be < N ({n})")
    if not (-360.0 <= w <= 360.0 and -360.0 <= e <= 360.0):
        raise ValidationError("bbox W/E out of range [-360, 360]")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError("bbox S/N out of range [-90, 90]")
    if (e - w) * (n - s) < 1e-8:
        raise ValidationError("bbox area is effectively zero; widen W/E or S/N")
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# 核心：扫描 / 元数据提取 / 分类
# ---------------------------------------------------------------------------
def is_geodata(path: str) -> bool:
    ext = os.path.splitext(path)[1].lower()
    return ext in RASTER_EXTS or ext in VECTOR_EXTS


def scan_directory(path: str, recursive: bool = True) -> List[str]:
    """列出目录下的地理数据文件（跳过 shapefile 辅助文件）。"""
    if os.path.isfile(path):
        return [path] if is_geodata(path) else []
    if not os.path.isdir(path):
        raise UsageError(f"input directory not found: {path}", path=path)
    found: List[str] = []
    if recursive:
        for root, _dirs, names in os.walk(path):
            for name in sorted(names):
                p = os.path.join(root, name)
                if is_geodata(p):
                    found.append(p)
    else:
        for name in sorted(os.listdir(path)):
            p = os.path.join(path, name)
            if os.path.isfile(p) and is_geodata(p):
                found.append(p)
    return found


def extract_raster_metadata(path: str) -> Dict[str, Any]:
    import rasterio
    with rasterio.open(path) as ds:
        b = ds.bounds
        res_x = abs(ds.transform.a) if ds.transform else None
        crs_epsg = None
        if ds.crs is not None:
            try:
                crs_epsg = ds.crs.to_epsg()
            except Exception:  # noqa: BLE001
                crs_epsg = None
        return {
            "kind": "raster",
            "format": "GeoTIFF",
            "width": int(ds.width),
            "height": int(ds.height),
            "band_count": int(ds.count),
            "dtype": str(ds.dtypes[0]) if ds.dtypes else None,
            "crs_epsg": crs_epsg,
            "bbox_wgs84": None if ds.crs is None else _reproject_bbox(ds, b),
            "resolution": [float(res_x)] if res_x is not None else None,
            "nodata": ds.nodata,
        }


def _reproject_bbox(ds: Any, b: Any) -> List[float]:
    """把栅格 bounds 转为 WGS84 bbox；若已是 4326 直接返回。"""
    try:
        if ds.crs is not None and ds.crs.to_epsg() == 4326:
            return [float(b.left), float(b.bottom), float(b.right), float(b.top)]
        from pyproj import Transformer
        tr = Transformer.from_crs(ds.crs, "EPSG:4326", always_xy=True)
        xs = [b.left, b.right, b.left, b.right]
        ys = [b.bottom, b.bottom, b.top, b.top]
        lons, lats = tr.transform(xs, ys)
        return [float(min(lons)), float(min(lats)), float(max(lons)), float(max(lats))]
    except Exception:  # noqa: BLE001
        return [float(b.left), float(b.bottom), float(b.right), float(b.top)]


def extract_vector_metadata(path: str) -> Dict[str, Any]:
    import geopandas as gpd
    gdf = gpd.read_file(path)
    geom_types = sorted({g.geom_type for g in gdf.geometry
                         if g is not None and not g.is_empty})
    crs_epsg = None
    if gdf.crs is not None:
        try:
            crs_epsg = gdf.crs.to_epsg()
        except Exception:  # noqa: BLE001
            crs_epsg = None
    try:
        b = gdf.total_bounds
        raw_bbox = [float(b[0]), float(b[1]), float(b[2]), float(b[3])]
    except Exception:  # noqa: BLE001
        raw_bbox = None
    bbox_wgs84 = _reproject_bbox_vector(gdf, raw_bbox, crs_epsg)
    fields = [c for c in gdf.columns if c != "geometry"]
    return {
        "kind": "vector",
        "format": _vector_format(path),
        "feature_count": int(len(gdf)),
        "geometry_types": geom_types,
        "fields": fields,
        "crs_epsg": crs_epsg,
        "bbox_wgs84": bbox_wgs84,
    }


def _reproject_bbox_vector(gdf: Any, raw_bbox: Optional[List[float]],
                            crs_epsg: Optional[int]) -> Optional[List[float]]:
    """Project vector bounds to WGS84 if not already 4326; return None if missing.

    If the gdf has no CRS or CRS is 4326, return raw_bbox as-is.
    If CRS is something else (e.g. UTM), reproject the 4 corners to 4326.
    If reprojection fails, return raw_bbox (preserved for diagnostic).
    """
    if raw_bbox is None:
        return None
    if crs_epsg is None or crs_epsg == 4326:
        return raw_bbox
    try:
        from pyproj import Transformer
        tr = Transformer.from_crs(f"EPSG:{crs_epsg}", "EPSG:4326", always_xy=True)
        xs = [raw_bbox[0], raw_bbox[2], raw_bbox[0], raw_bbox[2]]
        ys = [raw_bbox[1], raw_bbox[1], raw_bbox[3], raw_bbox[3]]
        lons, lats = tr.transform(xs, ys)
        return [float(min(lons)), float(min(lats)),
                float(max(lons)), float(max(lats))]
    except Exception:  # noqa: BLE001
        return raw_bbox


def _vector_format(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    return {".geojson": "GeoJSON", ".json": "GeoJSON",
            ".shp": "Shapefile", ".gpkg": "GeoPackage"}.get(ext, "Vector")


def extract_metadata(path: str) -> Dict[str, Any]:
    """提取单个文件元数据；解析失败时 status=error 但不抛异常。"""
    entry: Dict[str, Any] = {
        "path": path,
        "name": os.path.basename(path),
        "size_bytes": os.path.getsize(path) if os.path.exists(path) else 0,
        "status": "ok",
        "error": None,
    }
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext in RASTER_EXTS:
            entry.update(extract_raster_metadata(path))
        elif ext in VECTOR_EXTS:
            entry.update(extract_vector_metadata(path))
        else:
            entry["status"] = "error"
            entry["error"] = "unsupported extension"
            entry["kind"] = "unknown"
    except Exception as exc:  # noqa: BLE001
        entry["status"] = "error"
        entry["error"] = str(exc)
        entry["kind"] = "unknown"
    return entry


def classify(entry: Dict[str, Any]) -> str:
    """按数据类型细分。"""
    if entry.get("status") != "ok":
        return "Unreadable"
    kind = entry.get("kind")
    if kind == "raster":
        nb = entry.get("band_count", 0) or 0
        if nb <= 1:
            return "Single-band raster"
        if nb <= 4:
            return "Multispectral raster"
        return "Hyperspectral raster"
    if kind == "vector":
        gts = set(entry.get("geometry_types", []))
        if not gts:
            return "Empty vector"
        point_like = {"Point", "MultiPoint"}
        line_like = {"LineString", "MultiLineString"}
        poly_like = {"Polygon", "MultiPolygon"}
        if gts <= point_like:
            return "Point vector"
        if gts <= line_like:
            return "Line vector"
        if gts <= poly_like:
            return "Polygon vector"
        return "Mixed vector"
    return "Unknown"


def crs_family(epsg: Optional[int]) -> str:
    if epsg is None:
        return "Unknown CRS"
    if epsg == 4326:
        return "Geographic (WGS 84)"
    if epsg == 3857:
        return "Web Mercator"
    if 32601 <= epsg <= 32760:
        return "Projected (UTM)"
    return f"Projected (EPSG:{epsg})"


def build_catalog(entries: List[Dict[str, Any]]) -> Dict[str, Any]:
    """汇总目录统计。"""
    n_ok = sum(1 for e in entries if e["status"] == "ok")
    n_err = len(entries) - n_ok
    categories: Dict[str, int] = {}
    formats: Dict[str, int] = {}
    total_features = 0
    for e in entries:
        cat = classify(e)
        categories[cat] = categories.get(cat, 0) + 1
        fmt = e.get("format")
        if e["status"] == "ok" and fmt:
            formats[fmt] = formats.get(fmt, 0) + 1
        if e.get("kind") == "vector" and e["status"] == "ok":
            total_features += e.get("feature_count", 0)
    return {
        "n_files": len(entries),
        "n_readable": n_ok,
        "n_errors": n_err,
        "total_size_bytes": int(sum(e.get("size_bytes", 0) for e in entries)),
        "total_vector_features": int(total_features),
        "categories": categories,
        "formats": formats,
    }


# ---------------------------------------------------------------------------
# 目录输出：CSV / HTML / JSON
# ---------------------------------------------------------------------------
CSV_COLUMNS = ["name", "kind", "format", "category", "crs_family",
               "features_or_bands", "geometry_types", "bbox_wgs84",
               "size_bytes", "status"]


def _row_for_csv(e: Dict[str, Any]) -> List[str]:
    if e.get("kind") == "raster":
        fob = str(e.get("band_count", ""))
        gts = ""
    else:
        fob = str(e.get("feature_count", ""))
        gts = "/".join(e.get("geometry_types", []))
    bbox = e.get("bbox_wgs84")
    bbox_s = ";".join(f"{v:.6f}" for v in bbox) if bbox else ""
    return [
        e.get("name", ""),
        e.get("kind", ""),
        e.get("format", "") or "",
        classify(e),
        crs_family(e.get("crs_epsg")),
        fob,
        gts,
        bbox_s,
        str(e.get("size_bytes", 0)),
        e.get("status", ""),
    ]


def write_catalog_csv(entries: List[Dict[str, Any]], path: str) -> None:
    import csv
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(CSV_COLUMNS)
        for e in entries:
            w.writerow(_row_for_csv(e))


def write_catalog_html(entries: List[Dict[str, Any]], summary: Dict[str, Any],
                       path: str) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    esc = html.escape
    rows = []
    for e in entries:
        cells = [esc(str(x)) for x in _row_for_csv(e)]
        rows.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
    cat_rows = "".join(
        f"<li>{esc(k)}: {v}</li>" for k, v in sorted(summary["categories"].items()))
    fmt_rows = "".join(
        f"<li>{esc(k)}: {v}</li>" for k, v in sorted(summary["formats"].items()))
    doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>{SKILL_NAME} — Data Catalog</title>
<style>
 body {{ font-family: "Segoe UI", Arial, sans-serif; margin: 2rem; color: #222; }}
 h1 {{ font-size: 1.4rem; }}
 .stats {{ background: #f4f7fa; border-radius: 8px; padding: 1rem; margin-bottom: 1rem; }}
 .stats ul {{ margin: 0.3rem 0; }}
 table {{ border-collapse: collapse; width: 100%; font-size: 0.85rem; }}
 th, td {{ border: 1px solid #d0d7de; padding: 4px 8px; text-align: left; }}
 th {{ background: #eef2f6; }}
 tr:nth-child(even) {{ background: #fafbfc; }}
</style>
</head>
<body>
<h1>数据目录 / Data Catalog</h1>
<div class="stats">
  <p>文件总数: <b>{summary['n_files']}</b>（可读 {summary['n_readable']}，错误 {summary['n_errors']}）
     &nbsp;|&nbsp; 总大小: {summary['total_size_bytes']} bytes
     &nbsp;|&nbsp; 矢量要素总数: {summary['total_vector_features']}</p>
  <p>分类: <ul>{cat_rows}</ul></p>
  <p>格式: <ul>{fmt_rows}</ul></p>
</div>
<table>
<thead><tr>{''.join(f'<th>{esc(c)}</th>' for c in CSV_COLUMNS)}</tr></thead>
<tbody>
{''.join(rows)}
</tbody>
</table>
<p style="color:#888;font-size:0.75rem">Generated by {SKILL_NAME} v{VERSION} at {_utc_now()}</p>
</body>
</html>
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)


# ---------------------------------------------------------------------------
# 合成数据：混合源集
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], source_dir: str,
                       size: int = 16) -> List[str]:
    import geopandas as gpd
    from shapely.geometry import Point, LineString, Polygon
    from pyproj import CRS
    os.makedirs(source_dir, exist_ok=True)
    w, s, e, n_ = bbox
    paths = []

    # 单波段栅格
    band = np.random.default_rng(1).uniform(0, 100, (size, size)).astype(np.float32)
    tif1 = os.path.join(source_dir, "dem.tif")
    _write_geotiff(tif1, band[np.newaxis, ...], bbox)
    paths.append(tif1)

    # 三波段多光谱栅格
    cube = np.random.default_rng(2).uniform(0, 1, (3, size, size)).astype(np.float32)
    tif2 = os.path.join(source_dir, "rgb.tif")
    _write_geotiff(tif2, cube, bbox)
    paths.append(tif2)

    rng = np.random.default_rng(3)
    crs = CRS.from_epsg(4326)
    # 点 GeoJSON
    pts = gpd.GeoDataFrame(
        {"id": np.arange(1, 9)},
        geometry=[Point(rng.uniform(w, e), rng.uniform(s, n_)) for _ in range(8)],
        crs=crs)
    gj = os.path.join(source_dir, "pois.geojson")
    pts.to_file(gj, driver="GeoJSON")
    paths.append(gj)

    # 面 Shapefile
    polys = gpd.GeoDataFrame(
        {"id": [1]},
        geometry=[Polygon([(w, s), (w + (e - w) / 2, s), (w + (e - w) / 2, s + (n_ - s) / 2),
                           (w, s + (n_ - s) / 2), (w, s)])],
        crs=crs)
    shp = os.path.join(source_dir, "zones.shp")
    polys.to_file(shp, driver="ESRI Shapefile")
    paths.append(shp)

    # 线 GeoPackage
    lines = gpd.GeoDataFrame(
        {"id": [1, 2]},
        geometry=[LineString([(w, s), (e, n_)]), LineString([(e, s), (w, n_)])],
        crs=crs)
    gpkg = os.path.join(source_dir, "roads.gpkg")
    lines.to_file(gpkg, layer="roads", driver="GPKG")
    paths.append(gpkg)
    return paths


def _write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                   nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {"driver": "GTiff", "height": h, "width": w, "count": nb,
               "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
               "nodata": nodata, "compress": "deflate"}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype("float32"), b + 1)


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
    bbox: Optional[List[float]],
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
            "recursive": bool(getattr(args, "recursive", False)),
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
def validate_params(args: argparse.Namespace) -> None:
    """Validate CLI parameter values; raise ValidationError (rc=6) on bad choices."""
    if int(args.size) < 2:
        raise ValidationError(
            f"--size must be >= 2; got {args.size}"
        )


def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()

    # Phase 1: CLI value validation (BEFORE makedirs)
    validate_params(args)

    bbox = list(args.bbox) if args.bbox else None
    if bbox is not None:
        bbox = validate_bbox(bbox)

    if args.input and not args.synthetic:
        if not os.path.exists(args.input):
            raise UsageError(f"input not found: {args.input}", path=args.input)
        input_path = args.input
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <path>")
        # All input/bbox validation passed -> safe to create output dir
        output_dir = args.output_dir
        os.makedirs(output_dir, exist_ok=True)
        source_dir = os.path.join(output_dir, "source")
        generate_synthetic(bbox, source_dir, size=args.size)
        input_path = source_dir
        source_note = "synthetic"

    # Phase 2: real-input mode makedirs (after input exists check)
    if args.input and not args.synthetic:
        output_dir = args.output_dir
        os.makedirs(output_dir, exist_ok=True)

    files = scan_directory(input_path, recursive=args.recursive)
    entries = [extract_metadata(f) for f in files]
    summary = build_catalog(entries)
    summary["source"] = source_note

    csv_path = os.path.join(output_dir, "catalog.csv")
    html_path = os.path.join(output_dir, "catalog.html")
    json_path = os.path.join(output_dir, "catalog.json")
    write_catalog_csv(entries, csv_path)
    write_catalog_html(entries, summary, html_path)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "entries": entries}, f,
                  ensure_ascii=False, indent=2, default=str)

    qa = {
        "source": source_note,
        "n_files": summary["n_files"],
        "n_readable": summary["n_readable"],
        "total_vector_features": summary["total_vector_features"],
        "categories": summary["categories"],
    }
    outputs = [
        {"path": csv_path, "kind": "table", "row_count": len(entries)},
        {"path": html_path, "kind": "text"},
        {"path": json_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] files: {summary['n_files']}  readable: "
              f"{summary['n_readable']}  errors: {summary['n_errors']}")
        for cat, cnt in sorted(summary["categories"].items()):
            print(f"[{SKILL_NAME}]   {cat}: {cnt}")
        print(f"[{SKILL_NAME}] catalog: {html_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Scan geodata files, extract metadata, and generate an HTML/CSV catalog.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input file or directory to catalog")
    p.add_argument("--recursive", action="store_true",
                   help="recurse into subdirectories (default: top level only)")
    p.add_argument("--size", type=int, default=16,
                   help="synthetic raster size (default: 16)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate synthetic mixed source files (offline)")
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
