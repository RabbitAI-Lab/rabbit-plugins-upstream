#!/usr/bin/env python3
"""spatial-data-dashboard — 空间数据仪表盘

把空间数据（栅格 + 分区）汇总成一个自包含的 HTML 仪表盘：左侧 Leaflet 地图
（内嵌渲染叠加层），右侧 KPI 指标卡 + 纯 SVG 直方图 / 剖面折线图。所有图表
用内置 SVG 生成器绘制，不依赖外部 JS 图表库。

数据源：本地 GeoTIFF（可选），或 ``--synthetic`` 生成 DEM + 规则分区用于离线测试。

隐私声明 / Privacy：默认离线生成；Leaflet 底图仅在浏览器打开时加载。
``--synthetic`` 完全无网络；所有处理本地完成，不上传用户数据。

Usage:
    python spatial-data-dashboard.py --input dem.tif --bins 24 --title "流域 DEM"
    python spatial-data-dashboard.py --bbox 116 39 117 40 --synthetic

License: MIT
"""
from __future__ import annotations

import argparse
import base64
import datetime as _dt
import io
import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "spatial-data-dashboard"

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


def validate_bbox(bbox: List[float]) -> None:
    """校验 bbox：W<E、S<N、经纬度在合法范围、非零面积；跨 180° 明确提示。"""
    if bbox is None:
        raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
    if len(bbox) != 4:
        raise ValidationError(f"bbox must have exactly 4 numbers, got {len(bbox)}")
    w, s, e, n = [float(x) for x in bbox]
    if w > e:
        raise ValidationError(
            f"bbox minLon ({w}) > maxLon ({e}): crossing the 180° antimeridian is not "
            "supported, please split the region into two bboxes")
    if s > n:
        raise ValidationError(f"bbox minLat ({s}) > maxLat ({n}): S must be <= N")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"bbox longitudes out of range [-180, 180]: {w}, {e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"bbox latitudes out of range [-90, 90]: {s}, {n}")
    if w == e or s == n:
        raise ValidationError("bbox has zero area")


def validate_params(bins: int) -> None:
    if bins < 1:
        raise ValidationError(f"--bins must be >= 1, got {bins}")


# ---------------------------------------------------------------------------
# 核心算法：统计
# ---------------------------------------------------------------------------
def raster_histogram(values: np.ndarray, bins: int = 20) -> Tuple[List[float], List[int]]:
    """有效像元直方图。返回 (edges(len=bins+1), counts(len=bins))。"""
    v = np.asarray(values, dtype=float)
    v = v[np.isfinite(v)]
    if v.size == 0:
        edges = np.linspace(0, 1, bins + 1)
        return [float(x) for x in edges], [0] * bins
    counts, edges = np.histogram(v, bins=bins)
    return [float(x) for x in edges], [int(x) for x in counts]


def descriptive_stats(values: np.ndarray) -> Dict[str, float]:
    """描述性统计：count/mean/std/min/max/p5/p50/p95。"""
    v = np.asarray(values, dtype=float)
    v = v[np.isfinite(v)]
    if v.size == 0:
        return {"count": 0, "mean": 0.0, "std": 0.0, "min": 0.0, "max": 0.0,
                "p5": 0.0, "p50": 0.0, "p95": 0.0}
    return {
        "count": int(v.size),
        "mean": float(np.mean(v)),
        "std": float(np.std(v)),
        "min": float(np.min(v)),
        "max": float(np.max(v)),
        "p5": float(np.percentile(v, 5)),
        "p50": float(np.percentile(v, 50)),
        "p95": float(np.percentile(v, 95)),
    }


def zonal_statistics(values: np.ndarray, labels: np.ndarray) -> Dict[int, Dict[str, Any]]:
    """按整数标签数组做分区统计。返回 {label: {mean,min,max,count}}。

    labels 与 values 同形状；负标签（如 -1 nodata）被忽略。
    """
    if values.shape != labels.shape:
        raise ValidationError("values and labels must have the same shape")
    v = np.asarray(values, dtype=float)
    result: Dict[int, Dict[str, Any]] = {}
    for lab in np.unique(labels):
        lab_i = int(lab)
        if lab_i < 0:
            continue
        sel = v[labels == lab_i]
        sel = sel[np.isfinite(sel)]
        if sel.size == 0:
            continue
        result[lab_i] = {
            "mean": float(np.mean(sel)), "min": float(np.min(sel)),
            "max": float(np.max(sel)), "count": int(sel.size),
        }
    return result


# ---------------------------------------------------------------------------
# 核心算法：SVG 图表（无外部依赖）
# ---------------------------------------------------------------------------
def svg_histogram(edges: List[float], counts: List[int],
                  width: int = 340, height: int = 190, color: str = "#4a90d9",
                  title: str = "") -> str:
    """生成直方图 SVG 字符串。柱数 = len(counts)。"""
    pad_l, pad_b, pad_t = 36, 26, 22
    plot_w = width - pad_l - 8
    plot_h = height - pad_b - pad_t
    n = len(counts)
    maxc = max(counts) if counts else 1
    maxc = max(maxc, 1)
    bar_w = plot_w / max(n, 1)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
             f'viewBox="0 0 {width} {height}" font-family="sans-serif">']
    if title:
        parts.append(f'<text x="{width / 2}" y="14" font-size="12" text-anchor="middle">{title}</text>')
    # 轴
    parts.append(f'<line x1="{pad_l}" y1="{pad_t}" x2="{pad_l}" y2="{pad_t + plot_h}" stroke="#999"/>')
    parts.append(f'<line x1="{pad_l}" y1="{pad_t + plot_h}" x2="{pad_l + plot_w}" '
                 f'y2="{pad_t + plot_h}" stroke="#999"/>')
    for i, c in enumerate(counts):
        h = plot_h * (c / maxc)
        x = pad_l + i * bar_w
        y = pad_t + plot_h - h
        parts.append(f'<rect x="{x + 0.5:.1f}" y="{y:.1f}" width="{bar_w - 1:.1f}" '
                     f'height="{h:.1f}" fill="{color}"/>')
    parts.append(f'<text x="{pad_l}" y="{height - 6}" font-size="10">{edges[0]:.1f}</text>')
    parts.append(f'<text x="{pad_l + plot_w}" y="{height - 6}" font-size="10" '
                 f'text-anchor="end">{edges[-1]:.1f}</text>')
    parts.append(f'<text x="4" y="{pad_t + 8}" font-size="10">{maxc}</text>')
    parts.append("</svg>")
    return "".join(parts)


def svg_line(xs: List[float], ys: List[float], width: int = 340, height: int = 190,
             color: str = "#d9534f", title: str = "") -> str:
    """生成折线图 SVG。点数 = len(xs)。"""
    pad_l, pad_b, pad_t = 40, 26, 22
    plot_w = width - pad_l - 8
    plot_h = height - pad_b - pad_t
    xs = [float(x) for x in xs]; ys = [float(y) for y in ys]
    xmin, xmax = (min(xs), max(xs)) if xs else (0, 1)
    ymin, ymax = (min(ys), max(ys)) if ys else (0, 1)
    if xmax <= xmin: xmax = xmin + 1.0
    if ymax <= ymin: ymax = ymin + 1.0
    def sx(x): return pad_l + (x - xmin) / (xmax - xmin) * plot_w
    def sy(y): return pad_t + plot_h - (y - ymin) / (ymax - ymin) * plot_h
    pts = " ".join(f"{sx(x):.1f},{sy(y):.1f}" for x, y in zip(xs, ys))
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
             f'viewBox="0 0 {width} {height}" font-family="sans-serif">']
    if title:
        parts.append(f'<text x="{width / 2}" y="14" font-size="12" text-anchor="middle">{title}</text>')
    parts.append(f'<line x1="{pad_l}" y1="{pad_t}" x2="{pad_l}" y2="{pad_t + plot_h}" stroke="#999"/>')
    parts.append(f'<line x1="{pad_l}" y1="{pad_t + plot_h}" x2="{pad_l + plot_w}" '
                 f'y2="{pad_t + plot_h}" stroke="#999"/>')
    parts.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2"/>')
    parts.append(f'<text x="{pad_l}" y="{height - 6}" font-size="10">{xmin:.1f}</text>')
    parts.append(f'<text x="{pad_l + plot_w}" y="{height - 6}" font-size="10" '
                 f'text-anchor="end">{xmax:.1f}</text>')
    parts.append(f'<text x="4" y="{pad_t + 8}" font-size="10">{ymax:.1f}</text>')
    parts.append(f'<text x="4" y="{pad_t + plot_h}" font-size="10">{ymin:.1f}</text>')
    parts.append("</svg>")
    return "".join(parts)


# ---------------------------------------------------------------------------
# 渲染叠加层（复用百分位拉伸 + terrain colormap）
# ---------------------------------------------------------------------------
def render_overlay_b64(band: np.ndarray) -> Tuple[str, float, float]:
    import matplotlib
    from PIL import Image
    v = band.astype(np.float32)
    valid = v[np.isfinite(v)]
    lo = float(np.percentile(valid, 2)) if valid.size else 0.0
    hi = float(np.percentile(valid, 98)) if valid.size else 1.0
    if hi <= lo: hi = lo + 1e-9
    norm = np.clip((v - lo) / (hi - lo), 0.0, 1.0)
    rgb = matplotlib.colormaps["terrain"](norm)[..., :3]
    img = Image.fromarray((rgb * 255).round().astype(np.uint8), "RGB")
    buf = io.BytesIO(); img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("ascii"), lo, hi


# ---------------------------------------------------------------------------
# 合成数据：DEM + 规则分区标签
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64,
                       zones_x: int = 4, zones_y: int = 4, seed: int = 42
                       ) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1); yy /= max(height - 1, 1)
    peak = 1400.0 * np.exp(-(((xx - 0.6) ** 2 + (yy - 0.55) ** 2) / 0.02))
    base = 150.0 + 200.0 * xx + 100.0 * yy
    noise = rng.normal(0, 7.0, size=(height, width)).astype(np.float32)
    dem = (base + peak + noise).astype(np.float32)
    # 分区标签（0..zones_x*zones_y-1）
    zx = np.clip((xx * zones_x).astype(int), 0, zones_x - 1)
    zy = np.clip((yy * zones_y).astype(int), 0, zones_y - 1)
    labels = (zy * zones_x + zx).astype(np.int32)
    info = {"bbox": bbox, "width": width, "height": height,
            "zones": int(zones_x * zones_y), "kind": "synthetic-dem-zones"}
    return dem, labels, info


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


def read_geotiff(path):
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == nodata, np.nan, cube)
    cube = np.where(np.isfinite(cube), cube, np.nan)
    return cube, bbox


# ---------------------------------------------------------------------------
# 仪表盘 HTML 组装
# ---------------------------------------------------------------------------
def build_dashboard_html(bbox: List[float], overlay_b64: str, title: str,
                         stats: Dict[str, Any], hist_svg: str, line_svg: str,
                         zonal: Dict[int, Dict[str, Any]]) -> str:
    w, s, e, n = bbox
    cx, cy = (w + e) / 2.0, (s + n) / 2.0
    bounds = f"[[{s}, {w}], [{n}, {e}]]"
    kpis = [
        ("像元数", f"{stats.get('count', 0):,}"),
        ("均值", f"{stats.get('mean', 0):.2f}"),
        ("标准差", f"{stats.get('std', 0):.2f}"),
        ("最小 / 最大", f"{stats.get('min', 0):.1f} / {stats.get('max', 0):.1f}"),
    ]
    kpi_html = "".join(
        f'<div class="kpi"><div class="v">{v}</div><div class="k">{k}</div></div>'
        for k, v in kpis)
    zonal_rows = "".join(
        f'<tr><td>{lab}</td><td>{z["mean"]:.2f}</td><td>{z["min"]:.2f}</td>'
        f'<td>{z["max"]:.2f}</td><td>{z["count"]}</td></tr>'
        for lab, z in sorted(zonal.items()))
    return f"""<!DOCTYPE html>
<html lang="zh"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
body{{margin:0;font-family:sans-serif;background:#f4f6f8}}
header{{background:#1f3a5f;color:#fff;padding:12px 18px;font-size:18px}}
.wrap{{display:flex;flex-wrap:wrap;gap:14px;padding:14px}}
#map{{flex:1 1 480px;height:460px;border-radius:8px}}
.panel{{flex:1 1 360px;background:#fff;border-radius:8px;padding:14px;box-shadow:0 1px 4px rgba(0,0,0,.1)}}
.kpis{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:12px}}
.kpi{{flex:1 1 70px;background:#eef3fa;border-radius:6px;padding:8px;text-align:center}}
.kpi .v{{font-size:16px;font-weight:700;color:#1f3a5f}}
.kpi .k{{font-size:11px;color:#667}}
table{{border-collapse:collapse;width:100%;font-size:12px}}
th,td{{border:1px solid #ddd;padding:4px 6px;text-align:right}}
th{{background:#f0f0f0}}
</style></head>
<body>
<header>{title}</header>
<div class="wrap">
  <div id="map"></div>
  <div class="panel">
    <div class="kpis">{kpi_html}</div>
    {hist_svg}
    {line_svg}
    <h4>分区统计 Zonal</h4>
    <table><tr><th>zone</th><th>mean</th><th>min</th><th>max</th><th>count</th></tr>
    {zonal_rows}</table>
  </div>
</div>
<script>
var map = L.map('map').setView([{cy}, {cx}], 10);
L.tileLayer('https://tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png',
  {{maxZoom: 19, attribution: '&copy; OpenStreetMap'}}).addTo(map);
L.imageOverlay('data:image/png;base64,{overlay_b64}', {bounds}, {{opacity: 0.85}}).addTo(map);
map.fitBounds({bounds});
</script>
</body></html>
"""


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
                "bins": getattr(args, "bins", None),
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

    validate_params(args.bins)

    bbox = list(args.bbox) if args.bbox else None

    synth_info: Optional[Dict[str, Any]] = None
    input_nodata = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        band = cube[0]
        input_nodata = True
        # 用分位数把像元分成 16 个区作为“分区”
        valid = np.isfinite(band)
        qs = np.quantile(band[valid], np.linspace(0, 1, 17)[1:-1]) if valid.any() else None
        lab = np.digitize(band, qs) if qs is not None else np.full(band.shape, -1, dtype=np.int32)
        labels = np.where(valid, lab, -1).astype(np.int32)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        band, labels, synth_info = generate_synthetic(bbox)
        valid = np.isfinite(band)
        source_note = "synthetic"

    validate_bbox(bbox)

    n_valid = int(valid.sum())
    n_total = int(band.size)
    if n_valid == 0:
        raise ValidationError(
            f"input raster contains no valid (non-NoData) pixels: all {n_total} pixels are NoData")
    if band.size == 0:
        raise ValidationError("input raster is empty")
    if bbox is None:
        raise UsageError("could not determine bbox")

    stats = descriptive_stats(band)
    edges, counts = raster_histogram(band, bins=args.bins)
    zonal = zonal_statistics(band, labels)
    overlay_b64, lo, hi = render_overlay_b64(band)

    hist_svg = svg_histogram(edges, counts, title="值分布 Histogram", color="#4a90d9")
    # 折线：分区均值随 zone 的变化
    zone_ids = sorted(zonal.keys())
    zone_means = [zonal[z]["mean"] for z in zone_ids]
    line_svg = svg_line([float(z) for z in zone_ids], zone_means,
                        title="分区均值 Zonal mean", color="#d9534f")

    html = build_dashboard_html(bbox, overlay_b64, args.title, stats,
                                hist_svg, line_svg, zonal)
    os.makedirs(output_dir, exist_ok=True)
    html_path = os.path.join(output_dir, "dashboard.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    # 可验证产物：JSON + GeoTIFF
    dash_json = {"title": args.title, "source": source_note, "bbox": bbox,
                 "bins": args.bins, "stats": stats,
                 "histogram": {"edges": edges, "counts": counts},
                 "zonal": {str(k): v for k, v in zonal.items()},
                 "overlay_stretch": [lo, hi], "generated_at": _utc_now()}
    if synth_info is not None:
        dash_json["synthetic"] = synth_info
    json_path = os.path.join(output_dir, "dashboard.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(dash_json, f, ensure_ascii=False, indent=2)

    out_tif = os.path.join(output_dir, "dashboard_data.tif")
    write_geotiff(out_tif, np.where(valid, band, -9999.0).astype(np.float32), bbox)

    qa = {"source": source_note, "bins": args.bins, "mean": stats["mean"],
          "std": stats["std"], "n_zones": len(zonal),
          "n_valid_pixels": n_valid, "n_total_pixels": n_total,
          "input_nodata": input_nodata,
          "hist_count_sum": int(sum(counts)), "bbox": bbox}
    outputs = [
        {"path": html_path, "kind": "text"},
        {"path": json_path, "kind": "json"},
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] stats: mean={stats['mean']:.2f} std={stats['std']:.2f} "
              f"range=[{stats['min']:.1f}, {stats['max']:.1f}]")
        print(f"[{SKILL_NAME}] zones: {len(zonal)}  hist bins: {args.bins}")
        print(f"[{SKILL_NAME}] dashboard: {html_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Build a self-contained spatial data dashboard (map + SVG charts).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoTIFF raster")
    p.add_argument("--bins", type=int, default=20, help="histogram bins (default: 20)")
    p.add_argument("--title", default="Spatial Dashboard")
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
