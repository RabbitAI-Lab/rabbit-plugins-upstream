#!/usr/bin/env python3
"""spatial-storytelling — 空间叙事 / 故事地图

把多幅地图、文字解说与统计图表编织成一个**滚动叙事（scrollytelling）** HTML：
每个章节（section）包含一幅内嵌地图图像、一段叙述文字与一张 SVG 图表，
页面随滚动逐章节呈现，适合数据新闻、科普推文与成果展示。

数据源：多波段 GeoTIFF（每波段视为一章的地图底图），或 ``--synthetic``
生成模拟时序用于离线测试。

隐私声明 / Privacy：完全离线；所有处理本地完成，不上传用户数据。

Usage:
    python spatial-storytelling.py --input series.tif --title "城市扩张三十年"
    python spatial-storytelling.py --bbox 116 39 117 40 --synthetic --chapters 3

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
SKILL_NAME = "spatial-storytelling"

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


CMAPS = ["viridis", "YlGn", "plasma", "magma", "turbo", "gray", "terrain", "RdYlGn"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法：章节与图表
# ---------------------------------------------------------------------------
def build_section(index: int, title: str, text: str, image_b64: str,
                  chart_svg: str, stats: Dict[str, float]) -> Dict[str, Any]:
    """组装并校验一个叙事章节。title/text 不能为空。"""
    if not title or not str(title).strip():
        raise ValidationError("section title must be non-empty")
    if not text or not str(text).strip():
        raise ValidationError("section text must be non-empty")
    return {"index": int(index), "title": str(title), "text": str(text),
            "image_b64": image_b64, "chart_svg": chart_svg, "stats": dict(stats)}


def line_chart_svg(xs: List[float], ys: List[float], title: str = "",
                   width: int = 420, height: int = 200, color: str = "#3a7bd5") -> str:
    """生成章节内嵌折线图 SVG。"""
    if len(xs) != len(ys) or len(xs) == 0:
        raise ValidationError("xs/ys must be non-empty and same length")
    pad_l, pad_b, pad_t, pad_r = 44, 26, 22, 12
    plot_w = width - pad_l - pad_r
    plot_h = height - pad_b - pad_t
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    if xmax <= xmin: xmax = xmin + 1.0
    if ymax <= ymin: ymax = ymin + 1.0
    def sx(x): return pad_l + (x - xmin) / (xmax - xmin) * plot_w
    def sy(y): return pad_t + plot_h - (y - ymin) / (ymax - ymin) * plot_h
    pts = " ".join(f"{sx(x):.1f},{sy(y):.1f}" for x, y in zip(xs, ys))
    title_el = f'<text x="{width / 2}" y="14" font-size="12" text-anchor="middle">{title}</text>' if title else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" font-family="sans-serif">{title_el}'
            f'<line x1="{pad_l}" y1="{pad_t}" x2="{pad_l}" y2="{pad_t + plot_h}" stroke="#ccc"/>'
            f'<line x1="{pad_l}" y1="{pad_t + plot_h}" x2="{pad_l + plot_w}" y2="{pad_t + plot_h}" stroke="#ccc"/>'
            f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2.5"/>'
            f'<text x="{pad_l}" y="{height - 6}" font-size="10">{xmin:.1f}</text>'
            f'<text x="{pad_l + plot_w}" y="{height - 6}" font-size="10" text-anchor="end">{xmax:.1f}</text>'
            f'<text x="4" y="{pad_t + 8}" font-size="10">{ymax:.1f}</text>'
            f'<text x="4" y="{pad_t + plot_h}" font-size="10">{ymin:.1f}</text></svg>')


def render_band_png_b64(band: np.ndarray, cmap_name: str) -> str:
    """单波段 → 0..1 归一化 → colormap → PNG → base64。"""
    import matplotlib
    from PIL import Image
    if cmap_name not in CMAPS:
        raise UsageError(f"unknown cmap '{cmap_name}'. Choose: {CMAPS}", cmap=cmap_name)
    v = band.astype(np.float64)
    valid = v[np.isfinite(v)]
    if valid.size == 0:
        raise ValidationError("band has no finite values")
    vmin, vmax = float(valid.min()), float(valid.max())
    if vmax <= vmin: vmax = vmin + 1e-9
    norm = np.clip((v - vmin) / (vmax - vmin), 0.0, 1.0)
    norm = np.nan_to_num(norm, nan=0.0)
    rgb = matplotlib.colormaps[cmap_name](norm)[..., :3]
    buf = io.BytesIO()
    Image.fromarray((rgb * 255).round().astype(np.uint8), "RGB").save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("ascii")


# ---------------------------------------------------------------------------
# 核心算法：滚动叙事 HTML
# ---------------------------------------------------------------------------
def build_story_html(title: str, subtitle: str, sections: List[Dict[str, Any]]) -> str:
    """生成 scrollytelling HTML：粘性地图 + 逐章节文本卡片。"""
    nav_items = "".join(
        f'<a href="#sec-{s["index"]}">{s["index"] + 1}. {s["title"]}</a>'
        for s in sections)
    cards = []
    for s in sections:
        stats_html = "".join(
            f'<div class="stat"><div class="v">{v:.4g}</div><div class="k">{k}</div></div>'
            for k, v in s["stats"].items())
        cards.append(f"""
<section class="chapter" id="sec-{s['index']}">
  <div class="img"><img src="data:image/png;base64,{s['image_b64']}"/></div>
  <div class="card">
    <h2>{s['index'] + 1}. {s['title']}</h2>
    <p>{s['text']}</p>
    <div class="stats">{stats_html}</div>
    {s['chart_svg']}
  </div>
</section>""")
    cards_html = "\n".join(cards)
    return f"""<!DOCTYPE html>
<html lang="zh"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<style>
html,body{{margin:0;font-family:'Segoe UI',sans-serif;background:#0f141a;color:#e8eef4;scroll-behavior:smooth}}
header{{min-height:60vh;display:flex;flex-direction:column;justify-content:center;align-items:center;
text-align:center;background:linear-gradient(#16202c,#0f141a);padding:40px 20px}}
header h1{{font-size:2.6em;margin:0 0 10px}}
header p{{color:#9db4c8;max-width:640px}}
nav{{position:sticky;top:0;background:rgba(15,20,26,.92);padding:10px 20px;z-index:50;
display:flex;gap:16px;flex-wrap:wrap;border-bottom:1px solid #223}}
nav a{{color:#7fb3ff;text-decoration:none;font-size:13px}}
.chapter{{display:flex;flex-wrap:wrap;gap:24px;align-items:center;
max-width:1000px;margin:60px auto;padding:0 20px}}
.img{{flex:1 1 380px}}
.img img{{width:100%;border-radius:10px;box-shadow:0 10px 30px rgba(0,0,0,.5)}}
.card{{flex:1 1 380px;background:#16202c;border-radius:12px;padding:22px 26px}}
.card h2{{margin-top:0;color:#7fb3ff}}
.stats{{display:flex;gap:10px;flex-wrap:wrap;margin:14px 0}}
.stat{{background:#0f141a;border-radius:8px;padding:8px 14px;text-align:center}}
.stat .v{{font-weight:700;font-size:15px;color:#ffd479}}
.stat .k{{font-size:11px;color:#9db4c8}}
footer{{text-align:center;color:#5d7386;padding:40px}}
</style></head>
<body>
<header><h1>{title}</h1><p>{subtitle}</p></header>
<nav>{nav_items}</nav>
{cards_html}
<footer>由 {SKILL_NAME} 生成 · {_utc_now()}</footer>
</body></html>
"""


# ---------------------------------------------------------------------------
# 合成数据：城市化梯度时序（chapters 期）
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], chapters: int = 3, width: int = 64,
                       height: int = 64, seed: int = 42
                       ) -> Tuple[np.ndarray, Dict[str, Any]]:
    if chapters < 1:
        raise UsageError("chapters must be >= 1", chapters=chapters)
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1); yy /= max(height - 1, 1)
    core = np.exp(-(((xx - 0.5) ** 2 + (yy - 0.5) ** 2) / 0.03))
    stack = np.zeros((chapters, height, width), dtype=np.float32)
    for t in range(chapters):
        spread = 0.02 + 0.012 * t  # 城市逐年向外扩张
        urban = np.exp(-(((xx - 0.5) ** 2 + (yy - 0.5) ** 2) / spread))
        noise = rng.normal(0, 0.015, size=(height, width)).astype(np.float32)
        stack[t] = np.clip(0.15 + 0.7 * urban + noise, 0.0, 1.0)
    info = {"bbox": bbox, "width": width, "height": height,
            "chapters": chapters, "kind": "synthetic-urban-series",
            "mean_per_chapter": [float(np.mean(stack[t])) for t in range(chapters)]}
    return stack, info


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
    return cube, bbox


def read_geotiff_full(path):
    """Read GeoTIFF + replace NoData sentinel with NaN; return (cube, bbox, n_valid, input_nodata).

    The first band of every per-band n_valid count is reported. If *all* pixels are NoData
    in every band, raises ``ValidationError`` (rc=6).
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=False).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        input_nodata = src.nodata
    # Replace NoData sentinel with NaN
    if input_nodata is not None:
        cube = np.where(cube == float(input_nodata), np.nan, cube).astype(np.float32)
    valid_mask = np.isfinite(cube)
    n_valid = int(valid_mask.sum())
    if n_valid == 0:
        nodata_str = f"={input_nodata}" if input_nodata is not None else "(none)"
        raise ValidationError(
            f"input raster has no valid pixels (all are NoData{nodata_str})",
            path=path, input_nodata=input_nodata,
        )
    return cube, bbox, n_valid, input_nodata


def validate_bbox(bbox):
    """Validate EPSG:4326 bbox: W<E, S<N, lon/lat ranges, no crossing antimeridian,
    span > 1e-4°. Raises ``ValidationError`` (rc=6)."""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be [W, S, E, N] with 4 floats")
    W, S, E, N = [float(v) for v in bbox]
    if W < -180.0 or E > 180.0 or S < -90.0 or N > 90.0:
        raise ValidationError(
            f"bbox out of WGS-84 range: W={W} S={S} E={E} N={N} "
            "(must satisfy -180<=lon<=180, -90<=lat<=90)",
            bbox=bbox,
        )
    if W >= E:
        if W == E or (W > 0 and E < 0 and (W - E) >= 360.0 - 1e-6):
            # equal width or wraps fully around globe (>=360) - reject
            raise ValidationError(
                f"bbox has W>=E (W={W}, E={E}); expected W<E in WGS-84 order",
                bbox=bbox,
            )
        # Detect antimeridian-crossing (W > 0 and E < 0, span < 360)
        if W > 0 and E < 0 and (W - E) < 360.0:
            raise ValidationError(
                f"bbox crosses 180° antimeridian (W={W}, E={E}); "
                "split into two non-antipodal sub-bboxes",
                bbox=bbox,
            )
        # Otherwise reversed lon order (W > E in same hemisphere)
        raise ValidationError(
            f"bbox has W>=E (W={W}, E={E}); expected W<E in WGS-84 order",
            bbox=bbox,
        )
    if S >= N:
        raise ValidationError(
            f"bbox has S>=N (S={S}, N={N}); expected S<N in WGS-84 order",
            bbox=bbox,
        )
    if (E - W) < 1e-4 or (N - S) < 1e-4:
        raise ValidationError(
            f"bbox is too small (lon-span={E - W:.6f}, lat-span={N - S:.6f}); "
            "need at least 1e-4° on each axis",
            bbox=bbox,
        )
    return [W, S, E, N]


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
                "chapters": getattr(args, "chapters", None),
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

    # 1) bbox validation FIRST (before makedirs to avoid orphan output dirs)
    if args.input and not args.synthetic:
        # file-based: read later; we still validate any user-supplied bbox
        if bbox is not None:
            bbox = validate_bbox(bbox)
    else:
        # synthetic mode requires a valid bbox
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)

    n_valid_pixels = None
    input_nodata = None
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        stack, file_bbox, n_valid_pixels, input_nodata = read_geotiff_full(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            bbox = validate_bbox(bbox)
        source_note = args.input
    else:
        stack, synth_info = generate_synthetic(bbox, chapters=args.chapters)
        source_note = "synthetic"

    if stack.size == 0:
        raise ValidationError("input raster is empty")
    if bbox is None:
        raise UsageError("could not determine bbox")
    if stack.ndim == 2:
        stack = stack[np.newaxis, ...]

    # 2) ALL checks passed → now safe to makedirs
    os.makedirs(output_dir, exist_ok=True)

    n = stack.shape[0]
    # NaN-safe per-band means; if any band is fully NaN that's a data error
    means = []
    for t in range(n):
        m = float(np.nanmean(stack[t])) if np.any(np.isfinite(stack[t])) else float("nan")
        if not np.isfinite(m):
            raise ValidationError(
                f"band {t} of input raster is all NoData/NaN",
                band=t, input_nodata=input_nodata,
            )
        means.append(m)

    sections: List[Dict[str, Any]] = []
    for t in range(n):
        band = stack[t]
        stats = {"mean": float(np.nanmean(band)), "min": float(np.nanmin(band)),
                 "max": float(np.nanmax(band))}
        image_b64 = render_band_png_b64(band, args.cmap)
        chart = line_chart_svg(list(range(n)), means, title="各期均值 trend")
        title = f"{args.chapter_prefix} {t + 1}"
        text = (f"这一时期的平均强度为 {stats['mean']:.3f}"
                f"（范围 {stats['min']:.3f} – {stats['max']:.3f}）。"
                f"相对第 1 期变化 {((stats['mean'] - means[0]) * 100):+.1f}%。")
        sections.append(build_section(t, title, text, image_b64, chart, stats))

    html = build_story_html(args.title, args.subtitle, sections)
    html_path = os.path.join(output_dir, "story.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    # 可验证产物：结构化 JSON + 多期 GeoTIFF
    story_json = {"title": args.title, "source": source_note, "bbox": bbox,
                  "chapters": n, "means": means, "cmap": args.cmap,
                  "sections": [{"index": s["index"], "title": s["title"],
                                "text": s["text"], "stats": s["stats"]}
                               for s in sections],
                  "generated_at": _utc_now()}
    if synth_info is not None:
        story_json["synthetic"] = synth_info
    json_path = os.path.join(output_dir, "story.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(story_json, f, ensure_ascii=False, indent=2)

    tif_path = os.path.join(output_dir, "story_stack.tif")
    write_geotiff(tif_path, stack, bbox)

    qa = {"source": source_note, "chapters": n, "means": means,
          "cmap": args.cmap, "bbox": bbox,
          "n_valid_pixels": n_valid_pixels,
          "input_nodata": input_nodata}
    outputs = [
        {"path": html_path, "kind": "text"},
        {"path": json_path, "kind": "json"},
        {"path": tif_path, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": n},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  chapters: {n}")
        print(f"[{SKILL_NAME}] means: {[round(m, 3) for m in means]}")
        print(f"[{SKILL_NAME}] story: {html_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Weave maps, text and charts into a scrolling story HTML.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input multi-band GeoTIFF (each band = one chapter)")
    p.add_argument("--chapters", type=int, default=3, help="synthetic chapter count")
    p.add_argument("--chapter-prefix", default="Chapter", help="chapter title prefix")
    p.add_argument("--cmap", default="viridis", choices=CMAPS)
    p.add_argument("--title", default="Spatial Story", help="story title")
    p.add_argument("--subtitle", default="A data-driven spatial narrative.",
                   help="story subtitle")
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
