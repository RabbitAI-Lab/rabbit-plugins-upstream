#!/usr/bin/env python3
"""map-symbology-optimizer — 地图符号优化

基于色彩理论与视觉感知优化地图符号配色：

- **WCAG 对比度**：计算相对亮度与对比度比（黑-白 = 21:1），为每类挑选
  可读性最佳的黑/白标注文字；
- **色觉无障碍**：用二型色视（deuteranopia）近似矩阵模拟色觉缺陷者的
  感知，要求类别色在模拟后仍保持足够可区分距离；
- **视觉层次**：用类间平均色彩距离度量符号可分辨性，分类用
  Okabe-Ito / Tol 无障碍调色板，输出完整符号方案 JSON + 配色图。

数据源：本地 GeoTIFF，或 ``--synthetic`` 生成连续表面用于离线测试。

隐私声明 / Privacy：完全离线；所有处理本地完成，不上传用户数据。

Usage:
    python map-symbology-optimizer.py --input landcover.tif --classes 5 --palette okabe-ito
    python map-symbology-optimizer.py --bbox 116 39 117 40 --synthetic --method quantile

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import io
import json
import os
import sys
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "map-symbology-optimizer"

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


# Okabe-Ito 无障碍类别调色板（RGB 0-255）
PALETTES: Dict[str, List[Tuple[int, int, int]]] = {
    "okabe-ito": [(230, 159, 0), (86, 180, 233), (0, 158, 115), (240, 228, 66),
                  (0, 114, 178), (213, 94, 0), (204, 121, 167), (0, 0, 0)],
    "tol-muted": [(204, 102, 119), (51, 34, 136), (221, 204, 119), (17, 119, 51),
                  (136, 204, 238), (136, 34, 85), (68, 170, 153), (153, 153, 51)],
    "tol-bright": [(68, 170, 153), (238, 102, 119), (17, 119, 51), (153, 153, 51),
                   (238, 51, 119), (136, 204, 238), (170, 68, 153), (51, 34, 136)],
}
# 二型色视（deuteranopia）近似变换矩阵
DEUTAN_MATRIX = np.array([[0.625, 0.375, 0.0],
                          [0.700, 0.300, 0.0],
                          [0.000, 0.300, 0.700]])
CVD_SAFE_THRESHOLD = 30.0


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法：WCAG 亮度与对比度
# ---------------------------------------------------------------------------
def relative_luminance(rgb: Sequence[float]) -> float:
    """WCAG 2.x 相对亮度：线性化 sRGB 后按 0.2126/0.7152/0.0722 加权。"""
    c = np.asarray(rgb[:3], dtype=np.float64) / 255.0
    lin = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return float(0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2])


def contrast_ratio(rgb1: Sequence[float], rgb2: Sequence[float]) -> float:
    """WCAG 对比度比 (L1+0.05)/(L2+0.05)，范围 [1, 21]。"""
    l1 = relative_luminance(rgb1)
    l2 = relative_luminance(rgb2)
    hi, lo = max(l1, l2), min(l1, l2)
    return float((hi + 0.05) / (lo + 0.05))


def best_text_color(bg_rgb: Sequence[float]) -> Tuple[int, int, int]:
    """为背景色选择对比度更高的黑/白文字颜色。"""
    white = (255, 255, 255)
    black = (0, 0, 0)
    return white if contrast_ratio(bg_rgb, white) >= contrast_ratio(bg_rgb, black) else black


# ---------------------------------------------------------------------------
# 核心算法：色觉无障碍
# ---------------------------------------------------------------------------
def simulate_deuteranopia(rgb: Sequence[float]) -> np.ndarray:
    """二型色视近似模拟（线性矩阵变换）。灰度输入保持灰度不变。"""
    v = np.asarray(rgb[:3], dtype=np.float64)
    return DEUTAN_MATRIX.dot(v)


def min_pairwise_separation(colors: List[Tuple[int, int, int]],
                            simulated: bool = True) -> float:
    """类别色之间的最小成对欧氏距离（可选在色觉模拟空间中计算）。"""
    if len(colors) < 2:
        return float("inf")
    pts = [simulate_deuteranopia(c) if simulated else np.asarray(c, dtype=float)
           for c in colors]
    dmin = float("inf")
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            d = float(np.linalg.norm(pts[i] - pts[j]))
            dmin = min(dmin, d)
    return dmin


def is_colorblind_safe(colors: List[Tuple[int, int, int]],
                       threshold: float = CVD_SAFE_THRESHOLD) -> bool:
    """色觉安全判定：模拟后最小成对距离 >= threshold。"""
    return min_pairwise_separation(colors, simulated=True) >= threshold


def rgb_to_hex(rgb: Sequence[int]) -> str:
    r, g, b = (int(round(max(0, min(255, x)))) for x in rgb[:3])
    return f"#{r:02x}{g:02x}{b:02x}"


# ---------------------------------------------------------------------------
# 核心算法：分类与符号方案优化
# ---------------------------------------------------------------------------
def classify_breaks(values: np.ndarray, method: str, n_classes: int) -> List[float]:
    """返回 n_classes+1 个断点（含 min/max）。"""
    if n_classes < 2:
        raise UsageError("n_classes must be >= 2", n_classes=n_classes)
    v = np.asarray(values, dtype=float)
    v = v[np.isfinite(v)]
    if v.size == 0:
        raise ValidationError("no finite values to classify")
    if method == "equal_interval":
        edges = np.linspace(v.min(), v.max(), n_classes + 1)
    elif method == "quantile":
        edges = np.percentile(v, np.linspace(0, 100, n_classes + 1))
    else:
        raise UsageError(f"unknown method '{method}'", method=method)
    edges = np.sort(edges)
    edges[0] = v.min(); edges[-1] = v.max()
    return [float(x) for x in edges]


def pick_colors(palette_name: str, n: int) -> List[Tuple[int, int, int]]:
    """从无障碍调色板取 n 个颜色（超出时循环）。"""
    if palette_name not in PALETTES:
        raise UsageError(f"unknown palette '{palette_name}'. Choose: {sorted(PALETTES)}",
                         palette=palette_name)
    pal = PALETTES[palette_name]
    return [pal[i % len(pal)] for i in range(n)]


def optimize_symbology(values: np.ndarray, n_classes: int = 5,
                       method: str = "quantile", palette: str = "okabe-ito"
                       ) -> Dict[str, Any]:
    """完整符号优化：分类断点 + 无障碍配色 + 逐类文字色与对比度 + QA。"""
    edges = classify_breaks(values, method, n_classes)
    colors = pick_colors(palette, n_classes)
    classes = []
    for k in range(n_classes):
        bg = colors[k]
        txt = best_text_color(bg)
        classes.append({
            "class": k,
            "range": [edges[k], edges[k + 1]],
            "fill_hex": rgb_to_hex(bg),
            "text_hex": rgb_to_hex(txt),
            "text_contrast": contrast_ratio(bg, txt),
        })
    qa = {
        "palette": palette,
        "method": method,
        "n_classes": n_classes,
        "cvd_safe": is_colorblind_safe(colors),
        "min_separation_simulated": min_pairwise_separation(colors, True),
        "min_text_contrast": min(c["text_contrast"] for c in classes),
        "mean_text_contrast": float(np.mean([c["text_contrast"] for c in classes])),
    }
    return {"breaks": edges, "classes": classes, "qa": qa}


def render_symbology_png(values: np.ndarray, plan: Dict[str, Any]) -> bytes:
    """按符号方案渲染分类图 + 图例，返回 PNG 字节流。"""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap, BoundaryNorm
    edges = plan["breaks"]
    colors = [c["fill_hex"] for c in plan["classes"]]
    v = np.asarray(values, dtype=float)
    # NaN-safe: NaN pixels are masked out so matplotlib doesn't divide by zero
    v = np.ma.masked_invalid(v)
    cmap = ListedColormap(colors)
    norm = BoundaryNorm(edges, ncolors=len(colors), clip=True)
    fig, ax = plt.subplots(figsize=(7.5, 6), dpi=110)
    im = ax.imshow(v, cmap=cmap, norm=norm)
    cbar = fig.colorbar(im, ax=ax, ticks=edges, fraction=0.035, pad=0.02)
    cbar.set_label("class")
    ax.set_title("Optimized symbology")
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=110)
    plt.close(fig)
    return buf.getvalue()


# ---------------------------------------------------------------------------
# 合成数据：多峰连续表面（便于分类出多个可区分区间）
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64,
                       seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1); yy /= max(height - 1, 1)
    bumps = (30.0 * np.exp(-(((xx - 0.25) ** 2 + (yy - 0.3) ** 2) / 0.02))
             + 60.0 * np.exp(-(((xx - 0.7) ** 2 + (yy - 0.6) ** 2) / 0.03))
             + 45.0 * np.exp(-(((xx - 0.5) ** 2 + (yy - 0.85) ** 2) / 0.025)))
    base = 10.0 + 15.0 * xx + 10.0 * yy
    noise = rng.normal(0, 2.0, size=(height, width)).astype(np.float32)
    raster = (base + bumps + noise).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "kind": "synthetic-surface",
            "min": float(raster.min()), "max": float(raster.max())}
    return raster, info


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
    # NoData → NaN
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    return cube, bbox


def validate_bbox(bbox) -> None:
    """Validate bbox as (W, S, E, N); raise ValidationError on bad input.

    Rules (WGS-84):
        * 4 floats
        * W < E, S < N (zero-area or reversed bbox rejected)
        * -180 <= W, E <= 180; -90 <= S, N <= 90
        * bbox spans <1e-4 deg on either axis rejected (effectively zero area)
    Cross-180° is reported as a hint to split, but rejected for clarity.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats (W, S, E, N)", bbox=bbox)
    W, S, E, N = [float(x) for x in bbox]
    if not (-180.0 <= W <= 180.0 and -180.0 <= E <= 180.0):
        raise ValidationError(
            f"longitude out of range: W={W}, E={E} must be in [-180, 180]",
            bbox=bbox,
        )
    if not (-90.0 <= S <= 90.0 and -90.0 <= N <= 90.0):
        raise ValidationError(
            f"latitude out of range: S={S}, N={N} must be in [-90, 90]",
            bbox=bbox,
        )
    if W >= E:
        raise ValidationError(
            f"bbox has W >= E (W={W}, E={E}); please use W < E. "
            f"For cross-180° regions, split into two bboxes.",
            bbox=bbox,
        )
    if S >= N:
        raise ValidationError(
            f"bbox has S >= N (S={S}, N={N}); please use S < N.",
            bbox=bbox,
        )
    if (E - W) < 1e-4 or (N - S) < 1e-4:
        raise ValidationError(
            f"bbox span too small: width={E - W}, height={N - S}; must be >= 1e-4 deg",
            bbox=bbox,
        )


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
                "palette": getattr(args, "palette", None),
                "classes": getattr(args, "classes", None),
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

    synth_info: Optional[Dict[str, Any]] = None
    n_valid_pixels = 0
    input_nodata = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is None:
            raise ValidationError("could not determine bbox from input")
        validate_bbox(bbox)
        band = cube[0]
        valid_mask = np.isfinite(band)
        n_valid_pixels = int(valid_mask.sum())
        input_nodata = "NaN-replaced (src.nodata in cube)"
        if n_valid_pixels == 0:
            raise ValidationError(
                "input raster is entirely NoData (no valid pixels); nothing to render",
                path=args.input, n_total_pixels=int(band.size),
            )
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        band, synth_info = generate_synthetic(bbox)
        n_valid_pixels = int(band.size)  # synthetic has no NoData
        source_note = "synthetic"

    if band.size == 0:
        raise ValidationError("input raster is empty")
    if bbox is None:
        raise UsageError("could not determine bbox")

    # Now that inputs are valid, ensure output dir
    os.makedirs(output_dir, exist_ok=True)

    if args.classes < 2:
        raise ValidationError("classes must be >= 2", n_classes=args.classes)

    plan = optimize_symbology(band, n_classes=args.classes,
                              method=args.method, palette=args.palette)

    png_bytes = render_symbology_png(band, plan)
    png_path = os.path.join(output_dir, "symbology.png")
    with open(png_path, "wb") as f:
        f.write(png_bytes)

    # 可验证产物：类别索引 GeoTIFF + 符号方案 JSON
    edges = np.asarray(plan["breaks"], dtype=float)
    finite_band = np.where(np.isfinite(band), band, edges[0])
    class_idx = np.clip(np.searchsorted(edges, finite_band, side="right") - 1,
                        0, args.classes - 1).astype(np.float32)
    # NoData pixels get a -1 sentinel in the class index raster
    class_idx = np.where(np.isfinite(band), class_idx, -1.0).astype(np.float32)
    tif_path = os.path.join(output_dir, "classes.tif")
    write_geotiff(tif_path, class_idx, bbox, nodata=-1.0)

    plan_json = {"source": source_note, "bbox": bbox, "plan": plan,
                 "generated_at": _utc_now()}
    if synth_info is not None:
        plan_json["synthetic"] = synth_info
    json_path = os.path.join(output_dir, "symbology.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(plan_json, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "palette": args.palette, "method": args.method,
          "n_classes": args.classes,
          "cvd_safe": plan["qa"]["cvd_safe"],
          "min_text_contrast": plan["qa"]["min_text_contrast"],
          "bbox": bbox,
          "n_valid_pixels": n_valid_pixels,
          "n_total_pixels": int(band.size),
          "input_nodata_handling": input_nodata}
    outputs = [
        {"path": png_path, "kind": "text"},
        {"path": tif_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": json_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  classes: {args.classes}  palette: {args.palette}")
        print(f"[{SKILL_NAME}] CVD safe: {plan['qa']['cvd_safe']}  "
              f"min sep: {plan['qa']['min_separation_simulated']:.1f}")
        print(f"[{SKILL_NAME}] text contrast: min={plan['qa']['min_text_contrast']:.2f} "
              f"mean={plan['qa']['mean_text_contrast']:.2f}")
        print(f"[{SKILL_NAME}] png: {png_path}  json: {json_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Optimize map symbology: WCAG contrast, colorblind safety, visual hierarchy.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoTIFF raster")
    p.add_argument("--classes", type=int, default=5, help="number of classes (default: 5)")
    p.add_argument("--method", default="quantile", choices=["quantile", "equal_interval"])
    p.add_argument("--palette", default="okabe-ito", choices=sorted(PALETTES.keys()))
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
