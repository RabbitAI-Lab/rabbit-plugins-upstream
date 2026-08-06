#!/usr/bin/env python3
"""map-layout-automation — 地图排版自动化

把栅格地图自动排版成制图成品：图幅 + 标题 + 图例（colorbar）+ 比例尺 +
指北针。比例尺长度按图幅宽度与参考纬度换算成“整数千米”（1-2-5 序列），
指北针为标准北向箭头。输出高分辨率 PNG 与矢量 PDF。

数据源：本地 GeoTIFF，或 ``--synthetic`` 生成模拟 DEM 用于离线测试。

隐私声明 / Privacy：完全离线；所有处理本地完成，不上传用户数据。

Usage:
    python map-layout-automation.py --input dem.tif --title "研究区地形"
    python map-layout-automation.py --bbox 116 39 117 40 --synthetic --no-north

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
SKILL_NAME = "map-layout-automation"

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


CMAPS = ["terrain", "viridis", "magma", "inferno", "plasma", "gray", "turbo", "YlGn"]
M_PER_DEG_LAT = 111320.0  # 每纬度米数（近似常数）


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法：制图元素几何
# ---------------------------------------------------------------------------
def meters_per_degree_lon(lat_deg: float) -> float:
    """给定纬度处每经度的米数（球面近似）：111320 * cos(lat)。"""
    return M_PER_DEG_LAT * float(np.cos(np.deg2rad(lat_deg)))


def nice_round_km(target_km: float) -> float:
    """把目标长度圆整到 1-2-5 序列中不大于它的最大者（比例尺“整数千米”）。

    序列：0.5, 1, 2, 5, 10, 20, 50, ..., 若目标小于 0.5 返回 0.5。
    """
    if target_km <= 0:
        raise UsageError("target_km must be > 0", target_km=target_km)
    candidates = [0.5]
    base = 1.0
    while base < target_km * 10:
        candidates.extend([base, 2 * base, 5 * base])
        base *= 10
    best = 0.5
    for c in candidates:
        if c <= target_km:
            best = c
    return best


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


def scale_bar_km(bbox: List[float], fraction: float = 0.25) -> Tuple[float, float]:
    """计算比例尺条长度（km）与图幅实际宽度（km）。

    比例尺条目标 = 图幅宽度 × fraction，再圆整到 1-2-5 序列。
    """
    if fraction <= 0 or fraction > 1:
        raise UsageError("fraction must be in (0, 1]", fraction=fraction)
    w_deg = bbox[2] - bbox[0]
    if w_deg <= 0:
        raise UsageError("invalid bbox width", bbox=bbox)
    lat_mid = 0.5 * (bbox[1] + bbox[3])
    width_km = w_deg * meters_per_degree_lon(lat_mid) / 1000.0
    return nice_round_km(width_km * fraction), width_km


def draw_scale_bar(ax, bbox: List[float], bar_km: float) -> None:
    """在图幅左下角画比例尺条（黑白分段）+ 千米标注（数据坐标）。"""
    import matplotlib.patches as mpatches
    w_deg = bbox[2] - bbox[0]
    h_deg = bbox[3] - bbox[1]
    lat_mid = 0.5 * (bbox[1] + bbox[3])
    km_per_deg = meters_per_degree_lon(lat_mid) / 1000.0
    bar_deg = bar_km / km_per_deg
    x0 = bbox[0] + 0.05 * w_deg
    y0 = bbox[1] + 0.06 * h_deg
    half = bar_deg / 2.0
    ax.add_patch(mpatches.Rectangle((x0, y0), half, 0.012 * h_deg,
                                    facecolor="black", edgecolor="black"))
    ax.add_patch(mpatches.Rectangle((x0 + half, y0), half, 0.012 * h_deg,
                                    facecolor="white", edgecolor="black"))
    ax.text(x0, y0 - 0.02 * h_deg, "0", fontsize=8, ha="left")
    ax.text(x0 + half, y0 - 0.02 * h_deg, f"{bar_km / 2:g}", fontsize=8, ha="center")
    ax.text(x0 + bar_deg, y0 - 0.02 * h_deg, f"{bar_km:g} km", fontsize=8, ha="right")


def draw_north_arrow(ax, bbox: List[float]) -> None:
    """在图幅右上角画指北针（北向箭头 + N 标注）。"""
    w_deg = bbox[2] - bbox[0]
    h_deg = bbox[3] - bbox[1]
    x = bbox[2] - 0.08 * w_deg
    y = bbox[1] + 0.12 * h_deg
    ax.annotate("", xy=(x, y + 0.10 * h_deg), xytext=(x, y),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=2.0))
    ax.text(x, y + 0.115 * h_deg, "N", fontsize=11, fontweight="bold",
            ha="center", va="bottom")


def compose_layout(dem: np.ndarray, bbox: List[float], title: str,
                   cmap_name: str, bar_km: float,
                   show_scalebar: bool = True, show_north: bool = True,
                   show_legend: bool = True, dpi: int = 120):
    """把 DEM + 制图元素排版为 figure（调用方保存 PNG/PDF）。"""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    if cmap_name not in CMAPS:
        raise UsageError(f"unknown cmap '{cmap_name}'. Choose: {CMAPS}", cmap=cmap_name)

    fig, ax = plt.subplots(figsize=(8, 6.5), dpi=dpi)
    im = ax.imshow(dem, extent=[bbox[0], bbox[2], bbox[1], bbox[3]],
                   origin="upper", cmap=cmap_name)
    ax.set_xlabel("Longitude (°E)")
    ax.set_ylabel("Latitude (°N)")
    ax.set_title(title, fontsize=14, fontweight="bold", pad=10)
    if show_legend:
        cbar = fig.colorbar(im, ax=ax, fraction=0.035, pad=0.02)
        cbar.set_label("Elevation (m)")
    if show_scalebar:
        draw_scale_bar(ax, bbox, bar_km)
    if show_north:
        draw_north_arrow(ax, bbox)
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 128, height: int = 128,
                       seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1); yy /= max(height - 1, 1)
    peak = 1300.0 * np.exp(-(((xx - 0.6) ** 2 + (yy - 0.5) ** 2) / 0.02))
    basin = -200.0 * np.exp(-(((xx - 0.2) ** 2 + (yy - 0.25) ** 2) / 0.015))
    base = 180.0 + 150.0 * xx + 80.0 * yy
    noise = rng.normal(0, 6.0, size=(height, width)).astype(np.float32)
    dem = (base + peak + basin + noise).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "min_elev": float(dem.min()), "max_elev": float(dem.max()),
            "kind": "synthetic-dem"}
    return dem, info


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
    # Replace NoData sentinel(s) with NaN so downstream ops are NoData-safe
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    return cube, bbox


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
                "title": getattr(args, "title", None),
                "cmap": getattr(args, "cmap", None),
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
        dem = cube[0]
        # NoData handling: NaN-replaced cube; count valid finite pixels
        valid_mask = np.isfinite(dem)
        n_valid_pixels = int(valid_mask.sum())
        input_nodata = "NaN-replaced (src.nodata in cube)"
        if n_valid_pixels == 0:
            raise ValidationError(
                "input raster is entirely NoData (no valid pixels); nothing to render",
                path=args.input, n_total_pixels=int(dem.size),
            )
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        dem, synth_info = generate_synthetic(bbox)
        n_valid_pixels = int(dem.size)  # synthetic has no NoData
        source_note = "synthetic"

    if dem.size == 0:
        raise ValidationError("input raster is empty")
    if bbox is None:
        raise UsageError("could not determine bbox")

    # Now that we know we have something valid, ensure output dir
    os.makedirs(output_dir, exist_ok=True)

    bar_km, width_km = scale_bar_km(bbox, fraction=args.bar_fraction)
    fig = compose_layout(dem, bbox, args.title, args.cmap, bar_km,
                         show_scalebar=not args.no_scalebar,
                         show_north=not args.no_north,
                         show_legend=not args.no_legend, dpi=args.dpi)
    png_path = os.path.join(output_dir, "layout.png")
    pdf_path = os.path.join(output_dir, "layout.pdf")
    fig.savefig(png_path, dpi=args.dpi)
    fig.savefig(pdf_path, format="pdf")
    import matplotlib.pyplot as plt
    plt.close(fig)

    # 可验证产物：DEM 栅格 + 排版元数据
    tif_path = os.path.join(output_dir, "layout_data.tif")
    # Write NaN as -9999 sentinel in the GeoTIFF for downstream tools;
    # keep the in-memory `dem` with NaN for compose_layout masking.
    dem_for_tif = np.where(np.isfinite(dem), dem, -9999.0).astype(np.float32)
    write_geotiff(tif_path, dem_for_tif, bbox, nodata=-9999.0)
    meta = {"source": source_note, "title": args.title, "cmap": args.cmap,
            "scale_bar_km": bar_km, "map_width_km": width_km,
            "bar_fraction": args.bar_fraction,
            "elements": {"scalebar": not args.no_scalebar,
                         "north": not args.no_north,
                         "legend": not args.no_legend},
            "dpi": args.dpi, "bbox": bbox,
            "shape": [int(dem.shape[0]), int(dem.shape[1])],
            "n_valid_pixels": n_valid_pixels,
            "n_total_pixels": int(dem.size),
            "input_nodata_handling": input_nodata,
            "generated_at": _utc_now()}
    if synth_info is not None:
        meta["synthetic"] = synth_info
    meta_path = os.path.join(output_dir, "layout_meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "scale_bar_km": bar_km, "map_width_km": width_km,
          "cmap": args.cmap, "dpi": args.dpi, "bbox": bbox,
          "n_valid_pixels": n_valid_pixels,
          "n_total_pixels": int(dem.size),
          "input_nodata_handling": input_nodata}
    outputs = [
        {"path": png_path, "kind": "text"},
        {"path": pdf_path, "kind": "text"},
        {"path": tif_path, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": meta_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] map width: {width_km:.1f} km  scale bar: {bar_km:g} km")
        print(f"[{SKILL_NAME}] png: {png_path}  pdf: {pdf_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Automate cartographic layout: title, legend, scale bar, north arrow.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoTIFF raster")
    p.add_argument("--title", default="Map Layout", help="map title")
    p.add_argument("--cmap", default="terrain", choices=CMAPS)
    p.add_argument("--bar-fraction", type=float, default=0.25,
                   help="scale bar as fraction of map width (default: 0.25)")
    p.add_argument("--dpi", type=int, default=120, help="output dpi (default: 120)")
    p.add_argument("--no-scalebar", action="store_true", help="omit scale bar")
    p.add_argument("--no-north", action="store_true", help="omit north arrow")
    p.add_argument("--no-legend", action="store_true", help="omit legend/colorbar")
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
