#!/usr/bin/env python3
"""bare-soil-mapping — 裸土/裸地制图

融合三个互补特征提取裸土/裸地分布：

- **BSI（裸土指数）**：BSI = ((SWIR+Red) − (NIR+Blue)) / ((SWIR+Red) + (NIR+Blue))。
  裸土在红光与短波红外高反射、近红外相对低，BSI 偏高；植被因 NIR 高而 BSI 为负。
- **亮度（Brightness）**：多波段反射率均值。用于排除暗色水体（亮度极低）。
- **纹理（Texture）**：局部标准差。裸土表面均一、对比度低；城镇建筑异质、纹理高。

把三者转为 [0,1] 隶属度并相乘得到裸土得分，阈值化（``--threshold auto`` 用
Otsu 自动阈值，或显式浮点数）得到裸土掩膜。

数据源：本地多波段 GeoTIFF（波段顺序 blue/green/red/nir/swir），
或 ``--synthetic`` 生成含裸土/植被/城镇/水体的物理一致场景（离线）。

隐私声明 / Privacy：默认离线，不访问网络，所有处理本地完成。

Usage:
    python bare-soil-mapping.py --input scene.tif --threshold auto --output-dir ./out
    python bare-soil-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "bare-soil-mapping"

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


# ---- 隶属度参数 ----
BSI_LO = 0.20
BSI_HI = 0.50
TEX_LO = 0.02
TEX_HI = 0.06
BRIGHT_LO = 0.05
BRIGHT_HI = 0.12
DEFAULT_SCORE_THRESHOLD = 0.40

# 波段顺序
B_BLUE, B_GREEN, B_RED, B_NIR, B_SWIR = 0, 1, 2, 3, 4


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


def _ramp(x: np.ndarray, lo: float, hi: float) -> np.ndarray:
    if hi <= lo:
        return (x > lo).astype(np.float32)
    return np.clip((x - lo) / (hi - lo), 0.0, 1.0).astype(np.float32)


# ---------------------------------------------------------------------------
# 特征
# ---------------------------------------------------------------------------
def bsi_index(blue: np.ndarray, green: np.ndarray, red: np.ndarray,
              nir: np.ndarray, swir: np.ndarray) -> np.ndarray:
    """裸土指数 BSI = ((SWIR+Red) − (NIR+Blue)) / ((SWIR+Red) + (NIR+Blue))。"""
    blue = blue.astype(np.float32); red = red.astype(np.float32)
    nir = nir.astype(np.float32); swir = swir.astype(np.float32)
    a = swir + red
    b = nir + blue
    denom = a + b
    out = np.zeros_like(denom, dtype=np.float32)
    valid = denom != 0
    out[valid] = (a[valid] - b[valid]) / denom[valid]
    return np.clip(out, -1.0, 1.0)


def brightness(cube: np.ndarray) -> np.ndarray:
    """多波段反射率均值（亮度）。"""
    return cube.mean(axis=0).astype(np.float32)


def local_std(img: np.ndarray, size: int = 5) -> np.ndarray:
    """局部标准差（纹理强度），用均值滤波器计算 E[x²]−E[x]²。"""
    from scipy.ndimage import uniform_filter
    img = img.astype(np.float32)
    size = max(int(size), 1)
    m = uniform_filter(img, size=size, mode="reflect")
    m2 = uniform_filter(img * img, size=size, mode="reflect")
    var = np.clip(m2 - m * m, 0.0, None)
    return np.sqrt(var).astype(np.float32)


def otsu_threshold(values: np.ndarray, bins: int = 256) -> float:
    """大津法自动阈值（类间方差最大），输入取值范围 [0,1]。"""
    v = values[np.isfinite(values)]
    if v.size == 0:
        return DEFAULT_SCORE_THRESHOLD
    hist, edges = np.histogram(v, bins=bins, range=(0.0, 1.0))
    centers = (edges[:-1] + edges[1:]) / 2.0
    total = hist.sum()
    if total == 0:
        return DEFAULT_SCORE_THRESHOLD
    w0 = np.cumsum(hist).astype(np.float64)
    w1 = total - w0
    mu0_num = np.cumsum(hist * centers)
    mu_total = mu0_num[-1]
    with np.errstate(divide="ignore", invalid="ignore"):
        mu0 = np.where(w0 > 0, mu0_num / np.where(w0 == 0, 1, w0), 0.0)
        mu1 = np.where(w1 > 0, (mu_total - mu0_num) / np.where(w1 == 0, 1, w1), 0.0)
    between = w0 * w1 * (mu0 - mu1) ** 2
    # 类间方差在双峰间隙内呈平台；取平台中点使阈值落在两簇之间
    peak = between.max()
    peak_idx = np.where(np.isclose(between, peak, rtol=1e-9, atol=1e-12))[0]
    idx = int(peak_idx[len(peak_idx) // 2])
    return float(centers[idx])


def resolve_threshold(arg: str, score: np.ndarray) -> float:
    """解析 --threshold：'auto' 走 Otsu，否则解析为 [0,1] 浮点。"""
    s = str(arg).strip().lower()
    if s == "auto":
        return otsu_threshold(score)
    try:
        t = float(s)
    except ValueError:
        raise UsageError(f"invalid --threshold '{arg}' (use 'auto' or a float in [0,1])",
                         threshold=arg)
    if not (0.0 <= t <= 1.0):
        raise UsageError(f"--threshold must be within [0,1], got {t}", threshold=arg)
    return t


# ---------------------------------------------------------------------------
# 裸土评分与提取
# ---------------------------------------------------------------------------
def bare_soil_score(cube: np.ndarray, texture_size: int = 5
                    ) -> Tuple[np.ndarray, Dict[str, np.ndarray]]:
    """融合 BSI + 亮度 + 纹理，返回 (score, components)。"""
    if cube.ndim != 3 or cube.shape[0] < 5:
        raise ValidationError(
            f"input needs >=5 bands (blue/green/red/nir/swir), got shape {cube.shape}",
            shape=str(cube.shape),
        )
    blue = cube[B_BLUE]; green = cube[B_GREEN]; red = cube[B_RED]
    nir = cube[B_NIR]; swir = cube[B_SWIR]

    bsi = bsi_index(blue, green, red, nir, swir)
    bright = brightness(cube[:5])
    tex = local_std(bright, size=texture_size)

    bsi_m = _ramp(bsi, BSI_LO, BSI_HI)
    tex_m = 1.0 - _ramp(tex, TEX_LO, TEX_HI)
    bright_m = _ramp(bright, BRIGHT_LO, BRIGHT_HI)

    score = (bsi_m * tex_m * bright_m).astype(np.float32)
    components = {"bsi": bsi, "brightness": bright, "texture": tex,
                  "bsi_m": bsi_m, "tex_m": tex_m, "bright_m": bright_m}
    return score, components


def extract_bare_soil(cube: np.ndarray, threshold_arg: str = "auto",
                      texture_size: int = 5
                      ) -> Tuple[np.ndarray, np.ndarray, float, Dict[str, np.ndarray]]:
    """提取裸土。返回 (mask, score, applied_threshold, components)。"""
    score, components = bare_soil_score(cube, texture_size=texture_size)
    thr = resolve_threshold(threshold_arg, score)
    mask = score > thr
    return mask, score, thr, components


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic_scene(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成 (5, H, W) 场景：blue/green/red/nir/swir。

    布局：裸土块（高 BSI、低纹理）、植被（负 BSI）、城镇（亮且高纹理）、水体（暗）。
    返回 (cube, truth_bare_soil_mask, info)。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yyn = yy.astype(np.float32) / max(height - 1, 1)
    xxn = xx.astype(np.float32) / max(width - 1, 1)

    blue = np.zeros((height, width), dtype=np.float32)
    green = np.zeros((height, width), dtype=np.float32)
    red = np.zeros((height, width), dtype=np.float32)
    nir = np.zeros((height, width), dtype=np.float32)
    swir = np.zeros((height, width), dtype=np.float32)

    # 默认植被（上半部）
    veg = yyn < 0.40
    blue[veg] = 0.03; green[veg] = 0.09; red[veg] = 0.04
    nir[veg] = 0.45; swir[veg] = 0.18

    # 城镇（右下角，高纹理）
    urban = (yyn >= 0.40) & (xxn > 0.55)
    blue[urban] = 0.20; green[urban] = 0.22; red[urban] = 0.25
    nir[urban] = 0.28; swir[urban] = 0.25

    # 水体（左下角，暗）
    water = (yyn >= 0.40) & (xxn < 0.20)
    blue[water] = 0.05; green[water] = 0.04; red[water] = 0.03
    nir[water] = 0.02; swir[water] = 0.01

    # 裸土块（中部）
    bare = (yyn >= 0.40) & (xxn >= 0.20) & (xxn <= 0.55)
    blue[bare] = 0.10; green[bare] = 0.14; red[bare] = 0.30
    nir[bare] = 0.18; swir[bare] = 0.40

    # 纹理：城镇强随机、裸土极平滑、植被中等
    urban_tex = rng.uniform(-0.15, 0.15, size=(height, width)).astype(np.float32)
    veg_tex = rng.normal(0, 0.02, size=(height, width)).astype(np.float32)
    bare_tex = rng.normal(0, 0.004, size=(height, width)).astype(np.float32)
    for arr in (blue, green, red, nir, swir):
        arr[urban] += urban_tex[urban]
        arr[veg] += veg_tex[veg]
        arr[bare] += bare_tex[bare]
        np.clip(arr, 0.0, 1.0, out=arr)

    cube = np.stack([blue, green, red, nir, swir], axis=0).astype(np.float32)
    truth = bare.astype(np.uint8)
    info = {
        "bbox": bbox, "width": width, "height": height,
        "truth_bare_soil_px": int(truth.sum()),
    }
    return cube, truth, info


def pixel_area_m2(bbox: List[float], height: int, width: int) -> float:
    lat0 = (bbox[1] + bbox[3]) / 2.0
    x_m = (bbox[2] - bbox[0]) * 111320.0 * np.cos(np.deg2rad(lat0)) / max(width, 1)
    y_m = (bbox[3] - bbox[1]) * 110540.0 / max(height, 1)
    return float(abs(x_m * y_m))


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0) -> None:
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
    """Read multi-band GeoTIFF → (cube (nb, H, W) float32, bbox [W, S, E, N]).

    NoData values (from raster profile) are converted to NaN so the caller
    can mask them out via ``np.isfinite``.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        nodata = src.nodata
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    if nodata is not None:
        nd = float(nodata)
        cube = np.where(cube == nd, np.nan, cube)
    return cube, bbox


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir, args, outputs, qa, started_at, exit_code, bbox) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
            "threshold": getattr(args, "threshold", "auto"),
        },
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
    truth: Optional[np.ndarray] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, truth, synth_info = generate_synthetic_scene(bbox)
        source_note = "synthetic"

    # ---- validation (BEFORE os.makedirs to avoid empty output dirs) ----
    if bbox is None:
        raise UsageError("could not determine bbox")
    validate_bbox(bbox, ctx="bbox")
    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.ndim != 3 or cube.shape[0] < 5:
        raise ValidationError(
            f"input needs >=5 bands (blue/green/red/nir/swir), got shape {cube.shape}")
    if args.input and not args.synthetic:
        valid_count = int(np.sum(np.isfinite(cube)))
        if valid_count == 0:
            raise ValidationError(
                f"input raster has no valid (non-NoData) pixels: {args.input}"
            )
    os.makedirs(output_dir, exist_ok=True)

    h, w = cube.shape[1], cube.shape[2]
    px_area = pixel_area_m2(bbox, h, w)

    mask, score, thr, components = extract_bare_soil(
        cube, threshold_arg=args.threshold, texture_size=args.texture_size)

    # 写出
    mask_tif = os.path.join(output_dir, "bare_soil.tif")
    write_geotiff(mask_tif, mask.astype(np.float32), bbox)

    bsi_tif = os.path.join(output_dir, "bsi.tif")
    write_geotiff(bsi_tif, components["bsi"], bbox)

    px = int(mask.sum())
    area_m2 = px * px_area
    stats = {
        "bare_soil_pixels": px,
        "pixel_area_m2": px_area,
        "bare_soil_area_m2": area_m2,
        "bare_soil_area_ha": area_m2 / 10000.0,
        "bare_soil_area_km2": area_m2 / 1e6,
        "bare_soil_fraction": float(px) / mask.size,
        "applied_threshold": thr,
        "threshold_mode": args.threshold,
        "mean_bsi": float(np.mean(components["bsi"])),
        "texture_size": int(args.texture_size),
    }
    stats_path = os.path.join(output_dir, "bare_soil_area.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "bare_soil_area_ha": stats["bare_soil_area_ha"],
        "applied_threshold": thr,
        "mean_bsi": stats["mean_bsi"],
    }
    if synth_info is not None and truth is not None:
        pred = mask.astype(bool)
        gt = truth.astype(bool)
        inter = float(np.logical_and(pred, gt).sum())
        union = float(np.logical_or(pred, gt).sum())
        qa["synthetic_truth_iou"] = (inter / union) if union > 0 else 0.0

    outputs = [
        {"path": mask_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": bsi_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] threshold: {thr:.4f} (mode={args.threshold})")
        print(f"[{SKILL_NAME}] bare soil: {px} px  {stats['bare_soil_area_ha']:.2f} ha "
              f"({stats['bare_soil_fraction']*100:.1f}%)")
        print(f"[{SKILL_NAME}] output: {mask_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Bare soil mapping by fusing BSI, brightness and local texture.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multi-band GeoTIFF (blue/green/red/nir/swir)")
    p.add_argument("--threshold", default="auto",
                   help="score threshold: 'auto' (Otsu) or a float in [0,1] (default: auto)")
    p.add_argument("--texture-size", type=int, default=5,
                   help="moving-window size for texture (default: 5)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic scene (offline)")
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
