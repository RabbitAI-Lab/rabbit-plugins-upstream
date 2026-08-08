#!/usr/bin/env python3
"""map-style-transfer — 地图风格迁移

把源栅格的视觉风格迁移到目标风格，含三种可组合的手段：
- **直方图匹配**：把源影像的累积分布映射到参考影像，使均值/方差/色调对齐；
- **风格模板**：gamma / 对比度 / 色调 / 灰度（vintage / cool / warm / noir）；
- **调色板量化**：把连续色彩压缩到有限色阶，产生海报化效果。

数据源：本地 GeoTIFF（可选 ``--reference`` 参考影像做直方图匹配），或
``--synthetic`` 生成模拟影像用于离线测试。

隐私声明 / Privacy：完全离线；所有处理本地完成，不上传用户数据。

Usage:
    python map-style-transfer.py --input scene.tif --reference ref.tif
    python map-style-transfer.py --bbox 116 39 117 40 --synthetic --style noir --levels 6

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
SKILL_NAME = "map-style-transfer"

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


STYLE_TEMPLATES: Dict[str, Dict[str, Any]] = {
    "none":    {"gamma": 1.0, "contrast": 1.0, "tint": None, "grayscale": False},
    "vintage": {"gamma": 1.10, "contrast": 0.92, "tint": (1.08, 0.98, 0.82), "grayscale": False},
    "cool":    {"gamma": 1.00, "contrast": 1.05, "tint": (0.88, 0.98, 1.12), "grayscale": False},
    "warm":    {"gamma": 0.95, "contrast": 1.06, "tint": (1.12, 1.00, 0.88), "grayscale": False},
    "noir":    {"gamma": 1.00, "contrast": 1.30, "tint": None, "grayscale": True},
}


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法：直方图匹配
# ---------------------------------------------------------------------------
def histogram_match(source: np.ndarray, reference: np.ndarray) -> np.ndarray:
    """把 source 的累积分布匹配到 reference（单波段）。

    通过 np.interp 把 source 各唯一值的 CDF 映射到 reference 的取值，
    使结果的均值/方差/整体分布逼近 reference。
    """
    src = np.asarray(source, dtype=float)
    ref = np.asarray(reference, dtype=float)
    s = src[np.isfinite(src)].ravel()
    r = ref[np.isfinite(ref)].ravel()
    if s.size == 0 or r.size == 0:
        return src.copy()
    s_vals, s_inv, s_counts = np.unique(s, return_inverse=True, return_counts=True)
    r_vals, r_counts = np.unique(r, return_counts=True)
    s_cdf = np.cumsum(s_counts).astype(float) / s_counts.sum()
    r_cdf = np.cumsum(r_counts).astype(float) / r_counts.sum()
    mapped = np.interp(s_cdf, r_cdf, r_vals)
    out_flat = mapped[s_inv]
    out = out_flat.reshape(src.shape)
    out = np.where(np.isfinite(src), out, src)
    return out.astype(np.float32)


# ---------------------------------------------------------------------------
# 核心算法：风格模板
# ---------------------------------------------------------------------------
def apply_style_template(rgb: np.ndarray, name: str) -> np.ndarray:
    """对 [0,1] RGB 应用风格模板（灰度→gamma→对比度→色调）。"""
    if name not in STYLE_TEMPLATES:
        raise UsageError(f"unknown style '{name}'. Choose: {sorted(STYLE_TEMPLATES)}", style=name)
    t = STYLE_TEMPLATES[name]
    out = np.asarray(rgb, dtype=float).copy()
    if t.get("grayscale"):
        g = 0.299 * out[..., 0] + 0.587 * out[..., 1] + 0.114 * out[..., 2]
        out = np.stack([g, g, g], axis=-1)
    gamma = float(t.get("gamma", 1.0))
    if gamma != 1.0:
        out = np.power(np.clip(out, 0.0, 1.0), gamma)
    contrast = float(t.get("contrast", 1.0))
    if contrast != 1.0:
        out = (out - 0.5) * contrast + 0.5
    tint = t.get("tint")
    if tint is not None:
        out = out * np.array(tint, dtype=float)
    return np.clip(out, 0.0, 1.0).astype(np.float32)


# ---------------------------------------------------------------------------
# 核心算法：调色板量化
# ---------------------------------------------------------------------------
def quantize_palette(rgb_u8: np.ndarray, levels: int) -> np.ndarray:
    """把 0..255 RGB 每通道量化为 levels 个色阶（取 bin 中心）。

    结果每通道唯一值数 <= levels，总色数 <= levels^3。
    """
    levels = int(levels)
    if levels < 2:
        raise UsageError("levels must be >= 2", levels=levels)
    arr = np.asarray(rgb_u8, dtype=float)
    step = 256.0 / levels
    out = np.floor(arr / step) * step + step / 2.0
    return np.clip(out, 0, 255).astype(np.uint8)


# ---------------------------------------------------------------------------
# 归一化 / RGB 辅助
# ---------------------------------------------------------------------------
def normalize01(band: np.ndarray, lo_pct: float = 2.0, hi_pct: float = 98.0) -> np.ndarray:
    v = np.asarray(band, dtype=float)
    valid = v[np.isfinite(v)]
    if valid.size == 0:
        return np.zeros_like(v, dtype=np.float32)
    lo = float(np.percentile(valid, lo_pct))
    hi = float(np.percentile(valid, hi_pct))
    if hi <= lo: hi = lo + 1e-9
    out = np.clip((v - lo) / (hi - lo), 0.0, 1.0)
    return np.nan_to_num(out, nan=0.0).astype(np.float32)


def gray_to_rgb(gray01: np.ndarray) -> np.ndarray:
    g = np.clip(gray01, 0.0, 1.0)
    return np.repeat(g[..., np.newaxis], 3, axis=2).astype(np.float32)


def encode_png_bytes(rgb_u8: np.ndarray) -> bytes:
    from PIL import Image
    buf = io.BytesIO()
    Image.fromarray(np.clip(rgb_u8, 0, 255).astype(np.uint8), "RGB").save(buf, format="PNG")
    return buf.getvalue()


# ---------------------------------------------------------------------------
# 合成数据：带空间结构的灰度影像（双峰分布）
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64,
                       seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1); yy /= max(height - 1, 1)
    bright = 200.0 * np.exp(-(((xx - 0.35) ** 2 + (yy - 0.4) ** 2) / 0.03))
    base = 40.0 + 60.0 * xx
    noise = rng.normal(0, 5.0, size=(height, width)).astype(np.float32)
    img = (base + bright + noise).astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "kind": "synthetic-image", "min": float(img.min()), "max": float(img.max())}
    return img, info


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
                "reference": getattr(args, "reference", None),
                "style": getattr(args, "style", None),
                "levels": getattr(args, "levels", None),
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

    # 1) 直方图匹配（可选）
    matched = False
    ref_stats = None
    if args.reference:
        ref_cube, _ = read_geotiff(args.reference)
        ref_band = ref_cube[0]
        band = histogram_match(band, ref_band)
        matched = True
        ref_stats = {"mean": float(np.nanmean(ref_band)), "std": float(np.nanstd(ref_band))}

    # 2) 归一化 → RGB → 风格模板
    gray01 = normalize01(band)
    rgb = gray_to_rgb(gray01)
    rgb = apply_style_template(rgb, args.style)

    # 3) 调色板量化（可选）
    rgb_u8 = (rgb * 255.0).round().astype(np.uint8)
    if args.levels and args.levels >= 2:
        rgb_u8 = quantize_palette(rgb_u8, args.levels)

    png_bytes = encode_png_bytes(rgb_u8)
    png_path = os.path.join(output_dir, "styled.png")
    with open(png_path, "wb") as f:
        f.write(png_bytes)

    # 可验证产物：处理后灰度栅格 + 元数据
    out_tif = os.path.join(output_dir, "styled.tif")
    write_geotiff(out_tif, gray01.astype(np.float32), bbox)

    meta = {"source": source_note, "style": args.style, "matched": matched,
            "reference": args.reference, "levels": args.levels, "bbox": bbox,
            "template": STYLE_TEMPLATES[args.style],
            "result_mean": float(np.mean(gray01)), "result_std": float(np.std(gray01)),
            "png_bytes": len(png_bytes), "generated_at": _utc_now()}
    if ref_stats is not None:
        meta["reference_stats"] = ref_stats
    if synth_info is not None:
        meta["synthetic"] = synth_info
    meta_path = os.path.join(output_dir, "style_meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "style": args.style, "matched": matched,
          "levels": args.levels, "result_mean": meta["result_mean"],
          "png_bytes": len(png_bytes), "bbox": bbox,
          "n_valid_pixels": n_valid_pixels,
          "n_total_pixels": int(band.size),
          "input_nodata_handling": input_nodata}
    outputs = [
        {"path": png_path, "kind": "text"},
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": meta_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  style: {args.style}  matched: {matched}")
        print(f"[{SKILL_NAME}] levels: {args.levels}  result mean: {meta['result_mean']:.3f}")
        print(f"[{SKILL_NAME}] png: {png_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Transfer map style via histogram matching, style templates and palette quantization.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoTIFF raster")
    p.add_argument("--reference", help="reference GeoTIFF for histogram matching")
    p.add_argument("--style", default="vintage", choices=sorted(STYLE_TEMPLATES.keys()),
                   help="style template (default: vintage)")
    p.add_argument("--levels", type=int, default=0,
                   help="palette quantization levels per channel (0 = off)")
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
