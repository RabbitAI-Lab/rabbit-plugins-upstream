#!/usr/bin/env python3
"""orchard-tree-counting — 果园树木计数

基于冠层高度模型（CHM）做果树计数与冠幅统计：局部峰值检测定位树顶，模板
匹配评估冠层相似度，半高全宽（FWHM）估计单株冠幅直径。

核心算法
--------
- **CHM 峰值检测**：局部最大值定位树顶中心（min_distance 抑制重复）。
- **模板匹配**：构造高斯冠层模板，与 CHM 做归一化互相关，评估冠层匹配强度。
- **冠幅估计**：以峰值为中心，取径向剖面半高全宽（FWHM）估计冠幅直径。

数据源：本地 CHM 栅格（LiDAR/DSM-DTM）或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：默认离线，``--synthetic`` 完全无网络，本地处理不上传。

Usage:
    python orchard-tree-counting.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "orchard-tree-counting"

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, DependencyError, to_exit_code,
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

    class DependencyError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=3, kind="EDepend", **k)

    class ProcessError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=7, kind="EProcess", **k)

    def to_exit_code(exc):
        return getattr(exc, "code", 7)

    OutputManifest = None
    OutputFile = None


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float], source: str = "bbox") -> None:
    """Validate geographic bbox: W<=E, S<=N, lon/lat in range, min area.

    Cross-dateline (W>E) is a ValidationError with a hint to split. This is
    consistent with CONVENTIONS §1.1 (data error → rc=6) and the rest of the
    batch 1/2 reviewed skills.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(f"{source}: expected 4 floats [W S E N], got {bbox!r}")
    try:
        w, s, e, n = (float(v) for v in bbox)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"{source}: non-numeric bbox values: {bbox!r}") from exc
    for v, name in ((w, "W"), (s, "S"), (e, "E"), (n, "N")):
        if not (v == v):  # NaN check
            raise ValidationError(f"{source}: bbox contains NaN at {name}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"{source}: lon out of [-180,180]: W={w} E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"{source}: lat out of [-90,90]: S={s} N={n}")
    if w > e:
        raise ValidationError(
            f"{source}: W ({w}) > E ({e}); cross-dateline bboxes are not supported. "
            "Split into two bboxes on each side of the 180\u00b0 meridian and run separately."
        )
    if s > n:
        raise ValidationError(f"{source}: S ({s}) > N ({n})")
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"{source}: bbox too small (dlon={e - w}, dlat={n - s}); need > 1e-9 degrees"
        )


def validate_counting_params(min_distance: int, threshold_abs: float,
                             pixel_size: float) -> None:
    """Validate peak-detection / crown-width knobs.

    - ``min_distance`` must be >= 1 (skimage peak_local_max requires a positive
      integer; <1 silently degrades to "all pixels > threshold", producing a
      huge over-count).
    - ``threshold_abs`` must be a finite number.
    - ``pixel_size`` must be > 0 (crown width in meters = fwhm_px * pixel_size).
    """
    if not isinstance(min_distance, int) or min_distance < 1:
        raise ValidationError(
            f"--min-distance must be a positive integer >= 1 (got {min_distance!r}); "
            "< 1 silently degrades peak detection to 'all pixels above threshold'."
        )
    if not (threshold_abs == threshold_abs):  # NaN
        raise ValidationError(f"--threshold must be a finite number (got NaN)")
    if pixel_size <= 0 or not (pixel_size == pixel_size):
        raise ValidationError(
            f"--pixel-size must be > 0 meters (got {pixel_size!r})"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def detect_tree_peaks(chm: np.ndarray, min_distance: int = 4,
                      threshold_abs: float = 1.0) -> np.ndarray:
    """CHM 局部峰值检测，返回 (N, 2) [row, col] 树顶坐标。"""
    try:
        from skimage.feature import peak_local_max
        chm = np.asarray(chm, dtype=np.float32)
        return peak_local_max(chm, min_distance=min_distance,
                              threshold_abs=threshold_abs, exclude_border=True)
    except ImportError:
        from scipy.ndimage import maximum_filter
        chm = np.asarray(chm, dtype=np.float32)
        local_max = maximum_filter(chm, size=min_distance * 2 + 1)
        mask = (chm == local_max) & (chm > threshold_abs)
        return np.argwhere(mask)


def crown_template(radius_px: float, size: Optional[int] = None) -> np.ndarray:
    """构造归一化高斯冠层模板（峰值 1）。"""
    if radius_px <= 0:
        raise ValidationError("radius_px must be > 0")
    if size is None:
        size = int(np.ceil(radius_px * 4)) | 1  # 奇数
    c = size // 2
    yy, xx = np.mgrid[0:size, 0:size].astype(np.float32)
    sigma = radius_px / 2.0
    tmpl = np.exp(-((yy - c) ** 2 + (xx - c) ** 2) / (2 * sigma ** 2))
    return tmpl.astype(np.float32)


def template_match_score(chm: np.ndarray, template: np.ndarray) -> float:
    """CHM 与冠层模板的归一化互相关峰值（0-1，越高越像规则冠层）。"""
    try:
        from scipy.signal import correlate2d
    except ImportError as exc:  # pragma: no cover
        raise DependencyError("scipy is required for template matching") from exc
    chm = np.asarray(chm, dtype=np.float32)
    template = np.asarray(template, dtype=np.float32)
    # NaN safety: replace NaN with the chm mean so they don't dominate
    # the correlation. If everything is NaN, return 0.
    finite = np.isfinite(chm)
    if not finite.any():
        return 0.0
    if not finite.all():
        chm = np.where(finite, chm, float(chm[finite].mean()))
    c = chm - chm.mean()
    t = template - template.mean()
    denom_c = np.sqrt(np.sum(c ** 2)) + 1e-9
    denom_t = np.sqrt(np.sum(t ** 2)) + 1e-9
    corr = correlate2d(c / denom_c, t / denom_t, mode="valid")
    # 归一到匹配像元数的能量
    score = float(corr.max() / np.sqrt(chm.size))
    return float(np.clip(score, 0.0, 1.0))


def crown_width_fwhm(chm: np.ndarray, peak: Tuple[int, int],
                     pixel_size_m: float = 1.0) -> float:
    """以峰值为中心，沿径向取剖面估计半高全宽（冠幅直径，米）。"""
    chm = np.asarray(chm, dtype=np.float32)
    r, c = int(peak[0]), int(peak[1])
    h, w = chm.shape
    # NaN at the peak → can't measure FWHM
    if not (0 <= r < h and 0 <= c < w):
        return 0.0
    height = chm[r, c]
    if not (height == height) or height <= 0:  # NaN or non-positive
        return 0.0
    half = height / 2.0
    yy, xx = np.mgrid[0:h, 0:w]
    dist = np.sqrt((yy - r) ** 2 + (xx - c) ** 2)
    # 在径向距离上插值找半高交叉点
    max_d = int(min(r, c, h - 1 - r, w - 1 - c, 30))
    radii = []
    for d in np.arange(0, max_d + 1, 0.5):
        ring = (dist >= d - 0.25) & (dist < d + 0.25)
        if np.any(ring):
            ring_vals = chm[ring]
            finite_vals = ring_vals[np.isfinite(ring_vals)]
            if finite_vals.size:
                radii.append((d, float(finite_vals.mean())))
    if len(radii) < 2:
        return 0.0
    # 找从中心向外首次降到 half 以下的距离
    cross_d = float(max_d)
    for i in range(1, len(radii)):
        if radii[i][1] <= half:
            d0, v0 = radii[i - 1]
            d1, v1 = radii[i]
            if v0 != v1:
                frac = (v0 - half) / (v0 - v1)
                cross_d = d0 + frac * (d1 - d0)
            else:
                cross_d = d1
            break
    return float(2.0 * cross_d * pixel_size_m)  # 直径 = 2 × 半宽


def count_and_crowns(chm: np.ndarray, min_distance: int = 4,
                     threshold_abs: float = 1.0, pixel_size_m: float = 1.0) -> Dict[str, Any]:
    """主流程：计数 + 模板匹配 + 冠幅统计。"""
    chm = np.asarray(chm, dtype=np.float32)
    if chm.ndim != 2:
        raise ValidationError("chm must be 2D")
    # If input has NaN (NoData), use only the finite mask for peak detection
    # and template matching. This prevents NoData from being read as a
    # "0 m canopy" false negative (or worse, from polluting the template
    # correlation).
    finite = np.isfinite(chm)
    if not finite.any():
        raise ValidationError("chm has no finite (non-NoData) pixels")
    chm_for_peak = np.where(finite, chm, -np.inf)
    peaks = detect_tree_peaks(chm_for_peak, min_distance=min_distance, threshold_abs=threshold_abs)
    n = int(len(peaks))
    crown_tmpl = crown_template(radius_px=max(min_distance, 2))
    match_score = template_match_score(chm, crown_tmpl)
    widths = [crown_width_fwhm(chm, (p[0], p[1]), pixel_size_m) for p in peaks]
    widths = np.array(widths, dtype=np.float32)
    return {
        "count": n,
        "peaks": peaks,
        "template_score": float(match_score),
        "mean_crown_width_m": float(np.mean(widths)) if widths.size else 0.0,
        "median_crown_width_m": float(np.median(widths)) if widths.size else 0.0,
        "crown_widths_m": widths,
        "density_per_ha": float(n / max((chm.size * pixel_size_m ** 2) / 1e4, 1e-9)),
    }


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64,
                       crown_radius_px: float = 3.0, spacing: int = 12, seed: int = 42):
    """规则株行距果园 CHM：高斯冠层，已知冠幅半径。"""
    rng = np.random.default_rng(seed)
    chm = np.full((height, width), 0.3, dtype=np.float32)  # 地表/灌草基底
    positions = []
    for r in range(spacing, height - spacing // 2, spacing):
        for c in range(spacing, width - spacing // 2, spacing):
            positions.append((r, c))
    yy, xx = np.mgrid[0:height, 0:width]
    for (r, c) in positions:
        amp = rng.uniform(6.0, 9.0)
        chm += amp * np.exp(-((yy - r) ** 2 + (xx - c) ** 2) / (2 * crown_radius_px ** 2))
    chm = chm.astype(np.float32)
    info = {"bbox": bbox, "width": width, "height": height,
            "n_trees_true": len(positions), "crown_radius_px": crown_radius_px,
            "spacing_px": spacing}
    return chm, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
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
        inputs={"input": getattr(args, "input", None), "method": getattr(args, "method", None),
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
    os.makedirs(output_dir, exist_ok=True)
    bbox = list(args.bbox) if args.bbox else None

    # Validate counting params first (CLI-layer errors → rc=6, before any I/O)
    validate_counting_params(args.min_distance, args.threshold, args.pixel_size)

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        chm = cube[0] if cube.ndim == 3 else cube
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        # synthetic mode requires explicit bbox validation
        validate_bbox(bbox, source="--bbox")
        chm, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    if chm.size == 0:
        raise ValidationError("input raster is empty")

    # If --bbox is given with --input, validate the user-supplied bbox too
    if bbox is not None and args.bbox is not None:
        validate_bbox(bbox, source="--bbox")

    # If reading from file, defend against all-NoData inputs (would produce 0
    # trees silently). Map NoData sentinel to NaN, then check finite count.
    if not args.synthetic and args.input:
        # We don't know the nodata sentinel here without re-opening the raster;
        # use the file's declared nodata via a quick re-read.
        import rasterio as _rio
        with _rio.open(args.input) as _src:
            _nd = _src.nodata
        if _nd is not None:
            chm = np.where(chm == _nd, np.nan, chm).astype(np.float32)
        finite = np.isfinite(chm)
        if not finite.any():
            raise ValidationError(
                f"input raster '{args.input}' contains only NoData pixels; nothing to count"
            )

    res = count_and_crowns(chm, min_distance=args.min_distance,
                           threshold_abs=args.threshold, pixel_size_m=args.pixel_size)

    chm_tif = os.path.join(output_dir, "chm.tif")
    write_geotiff(chm_tif, chm, bbox)

    stats_json = os.path.join(output_dir, "tree_stats.json")
    stats_out = {k: (v.tolist() if isinstance(v, np.ndarray) else v)
                 for k, v in res.items() if k != "peaks"}
    stats_out["peak_count"] = int(len(res["peaks"]))
    with open(stats_json, "w", encoding="utf-8") as f:
        json.dump(stats_out, f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "method": args.method, "count": res["count"],
          "mean_crown_width_m": res["mean_crown_width_m"],
          "template_score": res["template_score"], "density_per_ha": res["density_per_ha"]}
    if synth_info is not None:
        qa["synthetic"] = {k: v for k, v in synth_info.items() if k != "bbox"}

    outputs = [
        {"path": chm_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_json, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] trees: {res['count']}  mean crown width: {res['mean_crown_width_m']:.2f} m")
        print(f"[{SKILL_NAME}] template score: {res['template_score']:.4f}  density: {res['density_per_ha']:.1f}/ha")
        print(f"[{SKILL_NAME}] output: {chm_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Orchard tree counting via CHM peak detection, template matching and crown width.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input CHM GeoTIFF (single band, meters)")
    p.add_argument("--method", default="peak-template", choices=["peak-template", "peak-only"],
                   help="counting method (default: peak-template)")
    p.add_argument("--min-distance", dest="min_distance", type=int, default=5,
                   help="minimum distance between tree peaks in pixels (default: 5)")
    p.add_argument("--threshold", type=float, default=1.0,
                   help="minimum CHM height for a tree peak (default: 1.0)")
    p.add_argument("--pixel-size", dest="pixel_size", type=float, default=1.0,
                   help="pixel size in meters (default: 1.0)")
    p.add_argument("--synthetic", action="store_true", help="generate synthetic scene (offline)")
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
