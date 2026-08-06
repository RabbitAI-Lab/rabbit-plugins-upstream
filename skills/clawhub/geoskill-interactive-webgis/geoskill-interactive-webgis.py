#!/usr/bin/env python3
"""interactive-webgis — 交互式WebGIS平台

生成一个自包含的轻量级 WebGIS：Leaflet 地图 + 内嵌 GeoJSON 图层 +
客户端属性查询面板（字段 / 运算符 / 值实时过滤要素）。核心提供一个可单测的
属性查询引擎（gt/lt/ge/le/eq/contains），并把查询结果与图层配置一并落盘。

数据源：本地矢量（GeoJSON/Shapefile），或 ``--synthetic`` 生成带属性的 POI
点要素用于离线测试。

隐私声明 / Privacy：完全离线生成；Leaflet 底图仅在浏览器打开时加载。
``--synthetic`` 完全无网络；所有处理本地完成，不上传用户数据。

Usage:
    python interactive-webgis.py --input poi.geojson --query-field value --query-op gt --query-value 50
    python interactive-webgis.py --bbox 116 39 117 40 --synthetic

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
SKILL_NAME = "interactive-webgis"

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


QUERY_OPS = ["gt", "lt", "ge", "le", "eq", "contains"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 参数校验（前置，避免坏 bbox / 坏参数触发下游 numpy 异常被误判为 rc=2）
# ---------------------------------------------------------------------------
def validate_bbox(bbox):
    """W/E 经度 ∈ [-180, 180]，S/N 纬度 ∈ [-90, 90]，W<E，S<N。

    跨 180° 经线不支持（按既定约定给拆分提示，不做环绕）。
    """
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise UsageError(f"bbox must be [W, S, E, N], got {bbox!r}")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range: W={w}, E={e}; must be in [-180, 180]")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range: S={s}, N={n}; must be in [-90, 90]")
    if w >= e:
        if w > e and abs(w - e) < 1.0 and w > 170.0:
            # 跨 180° 经线: 明确提示，不做环绕
            raise ValidationError(
                f"bbox crosses the antimeridian (W={w} > E={e}); "
                f"split into two sub-bboxes instead")
        raise ValidationError(
            f"bbox W must be < E; got W={w}, E={e}")
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N; got S={s}, N={n}")
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero area: W={w}, E={e}, S={s}, N={n}")
    return [w, s, e, n]


def validate_params(args):
    """参数域校验：--n-points >= 1。"""
    if args.n_points is not None and args.n_points < 1:
        raise ValidationError(
            f"--n-points must be >= 1; got {args.n_points}")
    if args.query_op not in QUERY_OPS:
        raise UsageError(
            f"unknown --query-op '{args.query_op}'; choose from {QUERY_OPS}")


# ---------------------------------------------------------------------------
# 核心算法：属性查询引擎
# ---------------------------------------------------------------------------
def query_features(gdf, field: str, op: str, value: Any):
    """按 field/op/value 过滤要素，返回子集 GeoDataFrame。

    op ∈ {gt, lt, ge, le, eq, contains}。数值运算符会尽量把 value 转 float；
    eq 优先按数值比较，失败则按字符串；contains 做子串匹配。
    """
    if field not in gdf.columns:
        raise UsageError(f"field '{field}' not found", field=field)
    if op not in QUERY_OPS:
        raise UsageError(f"unknown op '{op}'. Choose: {QUERY_OPS}", op=op)
    col = gdf[field]
    if op == "contains":
        mask = col.astype(str).str.contains(str(value), na=False)
    elif op == "eq":
        try:
            mask = col == float(value)
        except (ValueError, TypeError):
            mask = col.astype(str) == str(value)
    else:
        try:
            v = float(value)
        except (ValueError, TypeError):
            raise UsageError(f"op '{op}' requires a numeric value", value=str(value))
        if op == "gt":
            mask = col > v
        elif op == "lt":
            mask = col < v
        elif op == "ge":
            mask = col >= v
        else:  # le
            mask = col <= v
    return gdf[mask]


# ---------------------------------------------------------------------------
# 核心算法：点密度栅格化
# ---------------------------------------------------------------------------
def point_density_raster(points_xy: np.ndarray, bbox: List[float],
                         width: int, height: int) -> np.ndarray:
    """把点要素聚合到 (height, width) 计数栅格。每个点落入一个像元。"""
    pts = np.asarray(points_xy, dtype=float)
    w, s, e, n = bbox
    grid = np.zeros((height, width), dtype=np.float32)
    if pts.size == 0:
        return grid
    col = np.floor((pts[:, 0] - w) / (e - w) * width).astype(int)
    row = np.floor((n - pts[:, 1]) / (n - s) * height).astype(int)
    valid = (col >= 0) & (col < width) & (row >= 0) & (row < height)
    for c, r in zip(col[valid], row[valid]):
        grid[r, c] += 1
    return grid


# ---------------------------------------------------------------------------
# WebGIS 配置与 HTML
# ---------------------------------------------------------------------------
def build_webgis_config(title: str, layers: List[Dict[str, Any]],
                        bbox: List[float]) -> Dict[str, Any]:
    """组装 WebGIS 配置：校验每个图层必含 name/type，生成可序列化 dict。"""
    cleaned = []
    for lyr in layers:
        if "name" not in lyr or "type" not in lyr:
            raise ValidationError("each layer must define 'name' and 'type'")
        cleaned.append({
            "name": lyr["name"], "type": lyr["type"],
            "visible": bool(lyr.get("visible", True)),
            "color": lyr.get("color", "#1f78d1"),
            "opacity": float(lyr.get("opacity", 0.9)),
        })
    return {"title": title, "bbox": list(bbox), "layers": cleaned,
            "generated_at": _utc_now()}


def build_webgis_html(config: Dict[str, Any], features_geojson: Dict[str, Any],
                      fields: List[str]) -> str:
    bbox = config["bbox"]
    w, s, e, n = bbox
    cx, cy = (w + e) / 2.0, (s + n) / 2.0
    color = config["layers"][0]["color"] if config["layers"] else "#1f78d1"
    gj = json.dumps(features_geojson, ensure_ascii=False)
    fields_json = json.dumps(fields, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="zh"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{config['title']}</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
html,body{{height:100%;margin:0}}
#map{{position:absolute;inset:0}}
#panel{{position:absolute;top:10px;right:10px;z-index:1000;background:#fff;
padding:12px 14px;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,.2);width:230px;font:13px sans-serif}}
#panel h3{{margin:0 0 8px;font-size:14px}}
select,input{{width:100%;margin:4px 0;padding:4px;box-sizing:border-box}}
#count{{font-weight:700;color:#1f78d1}}
</style></head>
<body>
<div id="map"></div>
<div id="panel">
  <h3>{config['title']}</h3>
  <label>字段 field</label><select id="field"></select>
  <label>运算 op</label>
  <select id="op">
    <option value="gt">&gt;</option><option value="lt">&lt;</option>
    <option value="ge">&gt;=</option><option value="le">&lt;=</option>
    <option value="eq">=</option><option value="contains">contains</option>
  </select>
  <label>值 value</label><input id="val" value="50"/>
  <button onclick="applyQuery()">查询 Query</button>
  <div>命中 match: <span id="count">0</span></div>
</div>
<script>
var FEATURES = {gj};
var FIELDS = {fields_json};
var map = L.map('map').setView([{cy}, {cx}], 10);
L.tileLayer('https://tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png',
  {{maxZoom: 19, attribution: '&copy; OpenStreetMap'}}).addTo(map);
var layerGroup = L.layerGroup().addTo(map);
var sel = document.getElementById('field');
FIELDS.forEach(function(f){{ var o=document.createElement('option'); o.value=f; o.text=f; sel.add(o); }});
function matches(p, field, op, val){{
  var v = p.properties[field];
  if (op==='contains') return String(v).indexOf(val) >= 0;
  if (op==='eq') return String(v)===val || Number(v)===Number(val);
  var nv = Number(v), tv = Number(val);
  if (op==='gt') return nv>tv; if (op==='lt') return nv<tv;
  if (op==='ge') return nv>=tv; if (op==='le') return nv<=tv;
  return false;
}}
function render(subset){{
  layerGroup.clearLayers();
  subset.forEach(function(f){{
    var c = f.geometry.coordinates;
    L.circleMarker([c[1], c[0]], {{radius:6, color:'{color}', fillOpacity:0.8}})
      .bindPopup(JSON.stringify(f.properties)).addTo(layerGroup);
  }});
  document.getElementById('count').textContent = subset.length;
}}
function applyQuery(){{
  var field = document.getElementById('field').value;
  var op = document.getElementById('op').value;
  var val = document.getElementById('val').value;
  var subset = FEATURES.features.filter(function(f){{ return matches(f, field, op, val); }});
  render(subset);
}}
map.fitBounds([[{s}, {w}], [{n}, {e}]]);
render(FEATURES.features);
</script></body></html>
"""


# ---------------------------------------------------------------------------
# 合成数据：带属性的 POI 点
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], n: int = 120, seed: int = 42):
    import geopandas as gpd
    from shapely.geometry import Point
    rng = np.random.default_rng(seed)
    w, s, e, nn = bbox
    categories = ["school", "hospital", "park", "market", "station"]
    xs = rng.uniform(w + 0.02 * (e - w), e - 0.02 * (e - w), n)
    ys = rng.uniform(s + 0.02 * (nn - s), nn - 0.02 * (nn - s), n)
    values = rng.integers(1, 100, n)
    cats = [categories[int(i) % len(categories)] for i in rng.integers(0, len(categories), n)]
    names = [f"POI-{i + 1}" for i in range(n)]
    geom = [Point(x, y) for x, y in zip(xs, ys)]
    gdf = gpd.GeoDataFrame({"name": names, "category": cats, "value": values,
                            "geometry": geom}, crs="EPSG:4326")
    return gdf


def read_vector(path):
    import geopandas as gpd
    if not os.path.exists(path):
        raise UsageError(f"input vector not found: {path}", path=path)
    return gpd.read_file(path)


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path, cube, bbox, nodata=-9999.0):
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
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox):
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None),
                "query_field": getattr(args, "query_field", None),
                "query_op": getattr(args, "query_op", None),
                "synthetic": bool(getattr(args, "synthetic", False))},
        outputs=[OutputFile(**o) for o in outputs], qa=qa,
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

    # ---- 前置校验：参数 + bbox（必须先于 os.makedirs，失败不产空目录）----
    validate_params(args)
    if bbox is not None:
        bbox = validate_bbox(bbox)

    synth = False
    if args.input and not args.synthetic:
        gdf = read_vector(args.input)
        b = gdf.total_bounds
        bbox = bbox if bbox is not None else [float(b[0]), float(b[1]), float(b[2]), float(b[3])]
        if bbox is not None:
            bbox = validate_bbox(bbox)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <vector>")
        gdf = generate_synthetic(bbox, n=args.n_points)
        synth = True
        source_note = "synthetic"

    if len(gdf) == 0:
        raise ValidationError("input has no features")
    if bbox is None:
        raise UsageError("could not determine bbox")

    # ---- 校验通过后再创建输出目录（避免失败时留空目录）----
    os.makedirs(output_dir, exist_ok=True)

    # 选择查询字段：优先数值列（供 gt/lt 等运算），其次第一个非几何列
    non_geom = [c for c in gdf.columns if c != "geometry"]
    numeric_cols = [c for c in non_geom if np.issubdtype(gdf[c].dtype, np.number)]
    field = args.query_field or (numeric_cols[0] if numeric_cols
                                 else (non_geom[0] if non_geom else None))
    if field is not None and field not in gdf.columns:
        raise UsageError(f"query field '{field}' not found", field=field)

    # 执行服务端查询（生成可验证的查询结果）
    if field is not None:
        subset = query_features(gdf, field, args.query_op, args.query_value)
    else:
        subset = gdf.iloc[0:0]

    # 图层配置
    layers = [{"name": "features", "type": "circle", "color": args.color,
               "visible": True, "opacity": 0.9}]
    config = build_webgis_config(args.title, layers, bbox)

    # GeoJSON 导出
    features_geojson = json.loads(gdf.to_json())
    geojson_path = os.path.join(output_dir, "features.geojson")
    with open(geojson_path, "w", encoding="utf-8") as f:
        json.dump(features_geojson, f, ensure_ascii=False)

    # HTML
    html = build_webgis_html(config, features_geojson, non_geom)
    html_path = os.path.join(output_dir, "webgis.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    # 可验证产物：密度栅格 + JSON（含查询结果统计）
    pts = np.array([[g.xy[0][0], g.xy[1][0]] for g in gdf.geometry])
    density = point_density_raster(pts, bbox, 64, 64)
    tif_path = os.path.join(output_dir, "density.tif")
    write_geotiff(tif_path, density, bbox)

    webgis_json = {"config": config, "source": source_note, "bbox": bbox,
                   "n_features": int(len(gdf)),
                   "query": {"field": field, "op": args.query_op,
                             "value": args.query_value,
                             "n_matches": int(len(subset))},
                   "fields": non_geom,
                   "density_total": float(density.sum()),
                   "generated_at": _utc_now()}
    json_path = os.path.join(output_dir, "webgis.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(webgis_json, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "n_features": int(len(gdf)),
          "query_field": field, "query_op": args.query_op,
          "n_matches": int(len(subset)), "density_total": float(density.sum()),
          "bbox": bbox}
    outputs = [
        {"path": html_path, "kind": "text"},
        {"path": geojson_path, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": int(len(gdf))},
        {"path": tif_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": json_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  features: {len(gdf)}")
        print(f"[{SKILL_NAME}] query: {field} {args.query_op} {args.query_value} → {len(subset)} matches")
        print(f"[{SKILL_NAME}] webgis: {html_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Generate a self-contained interactive WebGIS with attribute query.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input vector (GeoJSON/Shapefile)")
    p.add_argument("--query-field", default=None, help="field to query (default: first)")
    p.add_argument("--query-op", default="gt", choices=QUERY_OPS)
    p.add_argument("--query-value", default="50", help="query value (default: 50)")
    p.add_argument("--n-points", type=int, default=120, help="synthetic POI count")
    p.add_argument("--color", default="#1f78d1", help="marker color")
    p.add_argument("--title", default="Interactive WebGIS")
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
