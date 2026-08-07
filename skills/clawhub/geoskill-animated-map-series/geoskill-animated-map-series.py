#!/usr/bin/env python3
"""animated-map-series — 动态地图序列 / 动画

把多期栅格（多波段 GeoTIFF 的每个波段 = 一期，或合成时序）用**统一色标**
渲染成逐帧 PNG，再合成为循环 GIF 动画。统一色标保证各期之间可比较。

数据源：本地多波段 GeoTIFF（每波段一期），或 ``--synthetic`` 生成一段物理
一致的 NDVI 时序（季节性正弦 + 趋势 + 噪声）。

隐私声明 / Privacy：
- 完全离线生成，无网络。所有处理本地完成，不上传用户数据。

Usage:
    python animated-map-series.py --input ndvi_series.tif --cmap viridis
    python animated-map-series.py --bbox 116 39 117 40 --synthetic --periods 8

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import io
import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "animated-map-series"

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


CMAPS = ["viridis", "YlGn", "RdYlGn", "plasma", "magma", "turbo", "gray", "terrain"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


def validate_bbox(bbox, ctx: str = "bbox") -> None:
    """Validate a (W, S, E, N) bbox: 4 floats, lon/lat ranges, W<E, S<N.

    Antimeridian crossing (W > E) is NOT supported; raises ValidationError
    suggesting the user split the bbox.
    """
    if bbox is None or len(bbox) != 4:
        raise UsageError(f"{ctx}: expected 4 floats (W S E N); got {bbox!r}")
    try:
        w, s, e, n = [float(v) for v in bbox]
    except (TypeError, ValueError):
        raise UsageError(f"{ctx}: bbox values must be numeric; got {bbox!r}")
    if not (all(np.isfinite([w, s, e, n]))):
        raise ValidationError(f"{ctx}: bbox values must be finite; got {bbox!r}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"{ctx}: longitude out of range (got W={w} E={e}); expected -180..180"
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"{ctx}: latitude out of range (got S={s} N={n}); expected -90..90"
        )
    if w >= e:
        raise ValidationError(
            f"{ctx}: requires W < E (got W={w} E={e}); "
            f"antimeridian crossing is not supported — split the bbox into two."
        )
    if s >= n:
        raise ValidationError(f"{ctx}: requires S < N (got S={s} N={n})")
    if (e - w) < 1e-6 or (n - s) < 1e-6:
        raise ValidationError(
            f"{ctx}: bbox extent too small ({(e - w):.2e} x {(n - s):.2e} deg); "
            f"need at least ~1e-6 deg in each direction"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def unified_scale(
    stack: np.ndarray, method: str = "minmax", pct: float = 2.0
) -> Tuple[float, float]:
    """为整个时序计算统一色标端点 (vmin, vmax)，保证各期可比较。

    method=minmax 用全局最小/最大；method=percentile 用全局低/高分位数。
    """
    valid = stack[np.isfinite(stack)]
    if valid.size == 0:
        return 0.0, 0.0
    if method == "percentile":
        vmin = float(np.percentile(valid, pct))
        vmax = float(np.percentile(valid, 100.0 - pct))
    else:
        vmin = float(np.min(valid))
        vmax = float(np.max(valid))
    if vmax <= vmin:
        vmax = vmin + 1.0
    return vmin, vmax


def normalize_frame(band: np.ndarray, vmin: float, vmax: float) -> np.ndarray:
    """用统一端点把单期归一化到 [0,1]。"""
    if vmax <= vmin:
        return np.zeros_like(band, dtype=np.float32)
    out = (band.astype(np.float32) - vmin) / (vmax - vmin)
    return np.clip(np.nan_to_num(out, nan=0.0), 0.0, 1.0).astype(np.float32)


def colormap_rgb(gray01: np.ndarray, cmap_name: str) -> np.ndarray:
    """[0,1] → (H,W,3) uint8 RGB。"""
    import matplotlib
    if cmap_name not in CMAPS:
        raise UsageError(f"unknown cmap '{cmap_name}'. Choose from: {CMAPS}", cmap=cmap_name)
    cmap = matplotlib.colormaps[cmap_name]
    rgb = cmap(np.clip(gray01, 0.0, 1.0))[..., :3]
    return (rgb * 255.0).round().astype(np.uint8)


def render_frame_png(
    gray01: np.ndarray, cmap_name: str, label: str,
    vmin: float, vmax: float, cell: int = 4, margin: int = 24,
) -> bytes:
    """渲染单帧：放大栅格 + 顶部时间标签 + 底部色标条。"""
    from PIL import Image, ImageDraw, ImageFont
    rgb = colormap_rgb(gray01, cmap_name)
    h, w = rgb.shape[:2]
    img = Image.fromarray(rgb, "RGB").resize((w * cell, h * cell), Image.NEAREST)
    canvas = Image.new("RGB", (w * cell, h * cell + margin * 2), (255, 255, 255))
    canvas.paste(img, (0, margin))
    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.load_default()
    except Exception:  # pragma: no cover
        font = None
    draw.text((6, 4), label, fill=(0, 0, 0), font=font)
    # 色标条：从 vmin 到 vmax 的渐变
    bar = np.linspace(0.0, 1.0, w * cell).astype(np.float32)
    bar_rgb = colormap_rgb(bar[np.newaxis, :], cmap_name)  # (1, w*cell, 3)
    bar_img = Image.fromarray(bar_rgb, "RGB").resize((w * cell, 10), Image.NEAREST)
    canvas.paste(bar_img, (0, margin + h * cell + 4))
    draw.text((6, margin + h * cell + 14), f"{vmin:.2f}", fill=(0, 0, 0), font=font)
    draw.text((w * cell - 40, margin + h * cell + 14), f"{vmax:.2f}", fill=(0, 0, 0), font=font)
    buf = io.BytesIO()
    canvas.save(buf, format="PNG")
    return buf.getvalue()


def compose_gif(frame_pngs: List[bytes], duration_ms: int = 500) -> bytes:
    """把帧 PNG 列表合成为循环 GIF。"""
    from PIL import Image
    if not frame_pngs:
        raise ValidationError("no frames to compose")
    imgs = []
    for b in frame_pngs:
        im = Image.open(io.BytesIO(b)).convert("RGB")
        imgs.append(im.quantize(colors=256, method=Image.Quantize.MEDIANCUT))
    buf = io.BytesIO()
    imgs[0].save(
        buf, format="GIF", save_all=True, append_images=imgs[1:],
        duration=duration_ms, loop=0, optimize=False,
    )
    return buf.getvalue()


# ---------------------------------------------------------------------------
# 合成数据：NDVI 季节性时序
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float], periods: int = 8, width: int = 64, height: int = 64, seed: int = 42
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (periods, H, W) 的 NDVI 时序：季节正弦 + 线性趋势 + 空间格局 + 噪声。"""
    if periods < 1:
        raise UsageError("periods must be >= 1", periods=periods)
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy /= max(height - 1, 1); xx /= max(width - 1, 1)
    # 空间基线：植被从西南向东北增多
    base = 0.25 + 0.4 * (0.5 * xx + 0.5 * yy)
    t = np.arange(periods, dtype=np.float32)
    phase = 2.0 * np.pi * t / max(periods, 1)
    stack = np.zeros((periods, height, width), dtype=np.float32)
    for k in range(periods):
        seasonal = 0.18 * np.sin(phase[k])
        trend = 0.005 * k
        noise = rng.normal(0, 0.01, size=(height, width)).astype(np.float32)
        ndvi = base + seasonal + trend + noise
        stack[k] = np.clip(ndvi, 0.0, 1.0)
    info = {"bbox": bbox, "width": width, "height": height, "periods": periods,
            "kind": "synthetic-ndvi-series",
            "mean_per_period": [float(np.mean(stack[k])) for k in range(periods)]}
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
    """Read multi-band GeoTIFF → (cube (nb, H, W) float32, bbox [W, S, E, N]).

    NoData values (from raster profile) are converted to NaN so the caller
    can mask them out via ``np.isfinite`` (e.g. in ``unified_scale``).
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        nodata = src.nodata
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    if nodata is not None and np.isfinite(nodata):
        cube = np.where(cube == float(nodata), np.nan, cube)
    elif nodata is not None and (cube == float(nodata)).any():
        # NoData was set to a non-finite sentinel (e.g. nan). Only mask finite
        # candidates — keep the rest as-is.
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
                "cmap": getattr(args, "cmap", None),
                "periods": getattr(args, "periods", None),
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
    if args.input and not args.synthetic:
        stack, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        stack, synth_info = generate_synthetic(bbox, periods=args.periods)
        source_note = "synthetic"

    # ---- validation (BEFORE os.makedirs to avoid leaving empty output dirs) ----
    if bbox is None:
        raise UsageError("could not determine bbox")
    validate_bbox(bbox, ctx="bbox")
    if stack.size == 0:
        raise ValidationError("input raster is empty")
    # All-NoData check: if read_geotiff turned NoData→NaN, an all-NaN cube means
    # the input had no valid pixels at all.
    if args.input and not args.synthetic and stack.ndim >= 2:
        valid_count = int(np.sum(np.isfinite(stack)))
        if valid_count == 0:
            raise ValidationError(
                f"input raster has no valid (non-NoData) pixels: {args.input}"
            )
    os.makedirs(output_dir, exist_ok=True)
    if stack.ndim == 2:
        stack = stack[np.newaxis, ...]

    n_periods = stack.shape[0]
    vmin, vmax = unified_scale(stack, method=args.scale, pct=args.pct)

    frames_dir = os.path.join(output_dir, "frames")
    os.makedirs(frames_dir, exist_ok=True)
    frame_pngs: List[bytes] = []
    frame_stats: List[Dict[str, Any]] = []
    for k in range(n_periods):
        norm = normalize_frame(stack[k], vmin, vmax)
        label = f"t={k + 1}/{n_periods}"
        png = render_frame_png(norm, args.cmap, label, vmin, vmax)
        frame_pngs.append(png)
        with open(os.path.join(frames_dir, f"frame_{k:03d}.png"), "wb") as f:
            f.write(png)
        frame_stats.append({
            "frame": k, "mean": float(np.nanmean(stack[k])),
            "min": float(np.nanmin(stack[k])), "max": float(np.nanmax(stack[k])),
        })

    gif_bytes = compose_gif(frame_pngs, duration_ms=args.duration)
    gif_path = os.path.join(output_dir, "animation.gif")
    with open(gif_path, "wb") as f:
        f.write(gif_bytes)

    # 可验证产物：多期 stack GeoTIFF + frames.json
    out_tif = os.path.join(output_dir, "series_stack.tif")
    write_geotiff(out_tif, stack, bbox)
    frames_json = {
        "n_periods": n_periods, "cmap": args.cmap, "scale": args.scale,
        "vmin": vmin, "vmax": vmax, "duration_ms": args.duration,
        "source": source_note, "bbox": bbox, "frames": frame_stats,
    }
    if synth_info is not None:
        frames_json["synthetic"] = synth_info
    json_path = os.path.join(output_dir, "frames.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(frames_json, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "n_periods": n_periods, "cmap": args.cmap,
          "vmin": vmin, "vmax": vmax, "gif_bytes": len(gif_bytes), "bbox": bbox}
    outputs = [
        {"path": gif_path, "kind": "text"},
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": n_periods},
        {"path": json_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  periods: {n_periods}")
        print(f"[{SKILL_NAME}] scale: [{vmin:.3f}, {vmax:.3f}]  cmap: {args.cmap}")
        print(f"[{SKILL_NAME}] gif:  {gif_path}  ({len(gif_bytes)} bytes)")
        print(f"[{SKILL_NAME}] frames: {frames_dir}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Compose a multi-temporal raster series into a unified-scale GIF animation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input multi-band GeoTIFF (each band = one period)")
    p.add_argument("--cmap", default="YlGn", choices=CMAPS, help="colormap (default: YlGn)")
    p.add_argument("--scale", default="minmax", choices=["minmax", "percentile"],
                   help="unified scale method (default: minmax)")
    p.add_argument("--pct", type=float, default=2.0,
                   help="percentile for scale method (default: 2)")
    p.add_argument("--periods", type=int, default=8,
                   help="number of synthetic periods (default: 8)")
    p.add_argument("--duration", type=int, default=500,
                   help="per-frame duration ms in GIF (default: 500)")
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
