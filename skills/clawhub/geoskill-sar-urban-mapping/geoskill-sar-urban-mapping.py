#!/usr/bin/env python3
"""sar-urban-mapping — SAR 城市制图

从单时相 SAR 后向散射（σ⁰，线性功率）中提取城市 / 建成区。物理依据：

- **高后向散射**：城市建筑形成大量二面角 / 三面角反射器（double/triple
  bounce），在 C/X 波段上 σ⁰ 显著高于农田与水体。
- **高纹理**：建筑布局造成强空间异质性，GLCM 对比度（contrast）高；
  农田与水面纹理均匀、对比度低。

方法流程：

1. **阈值分割**：``--threshold auto`` 时用 Otsu 最大类间方差法自动确定 σ⁰
   门限；也可传入固定线性 σ⁰ 门限。
2. **纹理辅助**（可选）：计算 GLCM 对比度，叠加纹理门限（Otsu）抑制
   高 σ⁰ 但纹理均匀的裸土 / 平静水面误检。
3. **形态学闭运算**：填充建筑街区内部空洞，连通城市斑块。

输出城市范围二值 GeoTIFF + 面积统计 JSON。

数据源：本地 SAR σ⁰ GeoTIFF（线性功率），或 ``--synthetic`` 生成物理一致的
模拟场景（低值农田 / 水体背景 + 高值高纹理城市斑块），用于离线验证。

隐私声明 / Privacy：
- 默认完全离线，``--synthetic`` 无任何网络。
- 所有处理本地完成，不上传用户数据。

Usage:
    python sar-urban-mapping.py --input sigma0.tif --output-dir ./out
    python sar-urban-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "sar-urban-mapping"

# ---- 复用共享核心库（本地 vendored，随脚本目录一起分发）----
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


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def otsu_threshold(values: np.ndarray, n_bins: int = 256) -> float:
    """Otsu 最大类间方差阈值。

    在一维样本上寻找使类间方差最大的灰度门限，将样本分成两类。
    对双峰直方图（低 σ⁰ 背景 vs 高 σ⁰ 城市）效果良好。
    """
    v = values[np.isfinite(values)]
    if v.size == 0:
        return 0.0
    vmin, vmax = float(v.min()), float(v.max())
    if vmax <= vmin:
        return float(vmin)
    hist, edges = np.histogram(v, bins=n_bins, range=(vmin, vmax))
    centers = 0.5 * (edges[:-1] + edges[1:])
    total = hist.sum()
    if total == 0:
        return float(vmin)
    hist = hist.astype(np.float64)
    weight_bg = np.cumsum(hist)
    weight_fg = total - weight_bg
    mean_cum = np.cumsum(hist * centers)
    mean_total = mean_cum[-1]
    with np.errstate(divide="ignore", invalid="ignore"):
        mean_bg = mean_cum / weight_bg
        mean_fg = (mean_total - mean_cum) / weight_fg
    between = weight_bg * weight_fg * (mean_bg - mean_fg) ** 2
    between = np.nan_to_num(between, nan=0.0, posinf=0.0, neginf=0.0)
    # 取最大类间方差平台的中点，使双峰门限落在两峰之间（而非贴住第一个峰）
    maxval = between.max()
    idxs = np.flatnonzero(between == maxval)
    idx = int(idxs[len(idxs) // 2]) if idxs.size else int(np.argmax(between))
    return float(centers[idx])


def glcm_contrast(gray: np.ndarray, levels: int = 32, window: int = 7) -> np.ndarray:
    """GLCM 对比度纹理（水平 + 垂直邻接，滑窗均值）。

    灰度共生矩阵（GLCM）对比度定义为 ``Σ (i-j)² P(i,j)``。对单位位移
    (dx=1,dy=0) 与 (dx=0,dy=1)，它等于相邻像元灰度差平方的期望，因此可以
    先量化灰度、计算相邻差平方，再用 ``window`` 大小的滑窗取均值来高效
    近似整幅图像的局部 GLCM 对比度。
    """
    g = np.asarray(gray, dtype=np.float32)
    g = np.nan_to_num(g, nan=0.0)
    gmin, gmax = float(g.min()), float(g.max())
    if gmax <= gmin:
        return np.zeros_like(g, dtype=np.float32)
    levels = max(int(levels), 2)
    q = ((g - gmin) / (gmax - gmin) * (levels - 1)).round().astype(np.float32)
    # 相邻像元灰度差平方（水平、垂直）
    dx2 = (q[:, 1:] - q[:, :-1]) ** 2
    dy2 = (q[1:, :] - q[:-1, :]) ** 2
    dx2 = np.pad(dx2, ((0, 0), (0, 1)), mode="edge")
    dy2 = np.pad(dy2, ((0, 1), (0, 0)), mode="edge")
    diff_sq = 0.5 * (dx2 + dy2)
    from scipy.ndimage import uniform_filter
    win = max(int(window), 1)
    contrast = uniform_filter(diff_sq, size=win, mode="reflect")
    return contrast.astype(np.float32)


def morphology_close(mask: np.ndarray, size: int = 5) -> np.ndarray:
    """二值形态学闭运算：先膨胀后腐蚀，填充街区空洞、连通斑块。"""
    from scipy.ndimage import binary_closing, binary_opening
    struct = np.ones((max(int(size), 1),) * 2, dtype=bool)
    closed = binary_closing(mask.astype(bool), structure=struct)
    # 轻微开运算去除孤立噪点
    cleaned = binary_opening(closed, structure=np.ones((3, 3), dtype=bool))
    return cleaned.astype(np.uint8)


def extract_urban(
    sigma0: np.ndarray,
    threshold: Any = "auto",
    use_texture: bool = True,
    tex_levels: int = 32,
    tex_window: int = 7,
    close_size: int = 5,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """从线性 σ⁰ 栅格提取城市建成区二值掩膜。

    返回 ``(mask_uint8, params)``。``threshold`` 为 ``"auto"`` 时用 Otsu，
    否则按给定的线性 σ⁰ 门限。``use_texture`` 为 True 时叠加 GLCM 对比度
    门限（同样用 Otsu）。
    """
    s = np.asarray(sigma0, dtype=np.float32)
    s = np.nan_to_num(s, nan=0.0)
    s = np.clip(s, 0.0, None)

    if isinstance(threshold, str) and threshold.strip().lower() == "auto":
        thr = otsu_threshold(s)
        thr_mode = "otsu"
    else:
        try:
            thr = float(threshold)
        except (TypeError, ValueError):
            raise UsageError(
                f"--threshold must be 'auto' or a float, got {threshold!r}",
                threshold=str(threshold),
            )
        thr_mode = "fixed"
    if thr <= 0:
        raise ValidationError(
            "derived backscatter threshold is non-positive; check input σ⁰",
            threshold=float(thr),
        )

    bright = s > thr
    tex_thr = None
    if use_texture:
        tex = glcm_contrast(s, levels=tex_levels, window=tex_window)
        tex_thr = otsu_threshold(tex)
        mask_raw = bright & (tex > tex_thr)
    else:
        tex = None
        mask_raw = bright

    mask = morphology_close(mask_raw, size=close_size)

    thr_db = float(10.0 * np.log10(thr)) if thr > 0 else None
    params = {
        "threshold_linear": float(thr),
        "threshold_db": thr_db,
        "threshold_mode": thr_mode,
        "texture_used": bool(use_texture),
        "texture_threshold": None if tex_thr is None else float(tex_thr),
        "close_size": int(close_size),
    }
    return mask, params


def pixel_area_km2(bbox: List[float], height: int, width: int) -> float:
    """估算单个像元的地表面积（km²），等经纬度栅格的平面近似。"""
    lat_mid = 0.5 * (bbox[1] + bbox[3])
    km_per_deg_lat = 111.0
    km_per_deg_lon = 111.0 * float(np.cos(np.deg2rad(lat_mid)))
    px_w = (bbox[2] - bbox[0]) / max(width, 1) * km_per_deg_lon
    px_h = (bbox[3] - bbox[1]) / max(height, 1) * km_per_deg_lat
    return float(abs(px_w * px_h))


def urban_statistics(
    mask: np.ndarray, bbox: List[float], params: Dict[str, Any]
) -> Dict[str, Any]:
    """由城市掩膜计算面积统计。"""
    h, w = mask.shape
    px = pixel_area_km2(bbox, h, w)
    n_urban = int(mask.sum())
    n_total = int(mask.size)
    stats = {
        "urban_pixels": n_urban,
        "total_pixels": n_total,
        "urban_fraction": float(mask.mean()),
        "urban_area_km2": n_urban * px,
        "total_area_km2": n_total * px,
        "pixel_area_km2": px,
    }
    stats.update(params)
    return stats


# ---------------------------------------------------------------------------
# 合成数据：物理一致的 SAR 场景（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成线性 σ⁰ 场景：低值农田 / 水体背景 + 高值高纹理城市斑块。

    返回 ``(sigma0, truth_mask, info)``。真值掩膜标记注入的城市像元，
    供测试校验检测面积。σ⁰ 采用乘性斑点噪声（对数正态）模拟 SAR 散斑。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yy_n = yy.astype(np.float32) / max(height - 1, 1)
    xx_n = xx.astype(np.float32) / max(width - 1, 1)

    # 背景：农田 σ⁰ ≈ 0.02 (-17 dB)
    sigma0 = np.full((height, width), 0.02, dtype=np.float32)
    # 水体：左下三角，σ⁰ ≈ 0.002 (-27 dB，镜面反射极低)
    water = (xx_n + yy_n) < 0.55
    sigma0[water] = 0.002

    # 乘性斑点噪声（SAR 典型，对数正态）
    speckle = np.exp(rng.normal(0.0, 0.15, size=(height, width))).astype(np.float32)
    sigma0 = sigma0 * speckle

    # 城市斑块：高 σ⁰ + 高纹理（建筑角反射器 + 棋盘格结构）
    truth = np.zeros((height, width), dtype=np.uint8)
    blocks = [
        (8, 8, 24, 24),
        (34, 6, 50, 20),
        (20, 38, 40, 54),
    ]
    for (r0, c0, r1, c1) in blocks:
        r1 = min(r1, height)
        c1 = min(c1, width)
        rr = r1 - r0
        cc = c1 - c0
        if rr <= 0 or cc <= 0:
            continue
        # 二面角反射造成的高后向散射基底 (-8 dB)
        base = 0.16
        # 棋盘格 + 随机：模拟建筑布局的高纹理
        checker = ((np.arange(rr)[:, None] + np.arange(cc)[None, :]) % 2).astype(np.float32)
        texture = 0.10 * checker + rng.uniform(0.0, 0.12, size=(rr, cc)).astype(np.float32)
        sigma0[r0:r1, c0:c1] = base + texture
        truth[r0:r1, c0:c1] = 1

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "seed": seed,
        "truth_urban_fraction": float(truth.mean()),
        "truth_urban_pixels": int(truth.sum()),
        "mean_sigma0": float(np.mean(sigma0)),
    }
    return sigma0, truth, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    cube: np.ndarray,
    bbox: List[float],
    nodata: float = -9999.0,
    dtype: str = "float32",
) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype(dtype), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_full(path: str) -> Tuple[np.ndarray, List[float], float]:
    """Read multi-band GeoTIFF, replace nodata with NaN, validate n_valid_pixels.

    Returns (cube_with_nan, bbox, nodata). Raises ValidationError if all pixels
    are NoData across all bands. nodata may be None if file has no nodata tag.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None and np.isfinite(nodata):
        cube = np.where(cube == nodata, np.nan, cube)
    n_valid = int(np.sum(np.isfinite(cube)))
    if n_valid == 0:
        raise ValidationError(
            f"input raster has no valid pixels (all {cube.size} are NoData={nodata})"
        )
    return cube, bbox, nodata


def validate_bbox(bbox: List[float]) -> None:
    """Validate bbox = [W, S, E, N]. Raise ValidationError on W>=E, S>=N, out-of-range,
    or cross-180° antipodal bbox."""
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise ValidationError(f"bbox must be 4 floats [W S E N], got {bbox}")
    w, s, e, n = [float(v) for v in bbox]
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"longitude out of range [-180,180]: W={w}, E={e}"
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"latitude out of range [-90,90]: S={s}, N={n}"
        )
    if w >= e:
        if abs(e - (-180.0)) < 1e-9 and w > 0:
            raise ValidationError(
                f"cross-180° bbox not supported (W={w}, E={e}); "
                f"split into two non-antipodal bboxes"
            )
        raise ValidationError(f"W must be < E, got W={w}, E={e}")
    if s >= n:
        raise ValidationError(f"S must be < N, got S={s}, N={n}")
    if (e - w) < 0.001 or (n - s) < 0.001:
        raise ValidationError(
            f"bbox too small (<0.001°), got W={w},S={s},E={e},N={n}"
        )


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
    bbox: List[float],
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
            "threshold": getattr(args, "threshold", None),
            "texture": getattr(args, "texture", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
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
def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir

    bbox = list(args.bbox) if args.bbox else None
    use_texture = str(args.texture).strip().lower() == "true"

    # 1) 获取 σ⁰ 数据（通用契约）
    synth_truth = None
    synth_info: Optional[Dict[str, Any]] = None
    input_nodata: Optional[float] = None
    n_valid_pixels: Optional[int] = None
    if args.input and not args.synthetic:
        if bbox is not None:
            validate_bbox(bbox)
        cube, file_bbox, input_nodata = read_geotiff_full(args.input)
        bbox = bbox if bbox is not None else file_bbox
        sigma0 = cube[0]
        n_valid_pixels = int(np.sum(np.isfinite(sigma0)))
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        sigma0, synth_truth, synth_info = generate_synthetic(bbox)
        n_valid_pixels = int(sigma0.size)
        source_note = "synthetic"

    if sigma0.size == 0:
        raise ValidationError("input raster is empty")
    if not np.any(np.isfinite(sigma0)):
        raise ValidationError("input raster has no finite values")

    # Now safe to create output dir
    os.makedirs(output_dir, exist_ok=True)

    # 2) 城市提取
    mask, params = extract_urban(
        sigma0, threshold=args.threshold, use_texture=use_texture,
    )

    # 3) 面积统计
    stats = urban_statistics(mask, bbox, params)

    # 4) 写出产物
    out_tif = os.path.join(output_dir, "urban_mask.tif")
    write_geotiff(out_tif, mask.astype("uint8"), bbox, nodata=255, dtype="uint8")

    stats_path = os.path.join(output_dir, "urban_statistics.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "urban_fraction": stats["urban_fraction"],
        "urban_area_km2": stats["urban_area_km2"],
        "threshold_linear": stats["threshold_linear"],
        "threshold_db": stats["threshold_db"],
        "texture_used": stats["texture_used"],
        "n_valid_pixels": n_valid_pixels,
        "input_nodata": input_nodata,
    }
    if synth_info is not None:
        qa["synthetic_truth_urban_fraction"] = synth_info["truth_urban_fraction"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] threshold: {stats['threshold_linear']:.4g} "
              f"({stats['threshold_db']:.2f} dB, {stats['threshold_mode']})")
        print(f"[{SKILL_NAME}] texture: {stats['texture_used']}")
        print(f"[{SKILL_NAME}] urban fraction: {stats['urban_fraction']:.4f}  "
              f"area: {stats['urban_area_km2']:.3f} km²")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="SAR urban / built-up area mapping from backscatter threshold + GLCM texture.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input SAR σ⁰ GeoTIFF (linear power)")
    p.add_argument("--threshold", default="auto",
                   help="backscatter threshold: 'auto' (Otsu) or a linear σ⁰ float (default: auto)")
    p.add_argument("--texture", default="true", choices=["true", "false"],
                   help="use GLCM texture to refine urban mask (default: true)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic SAR scene (offline)")
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
