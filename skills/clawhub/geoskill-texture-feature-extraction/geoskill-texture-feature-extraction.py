#!/usr/bin/env python3
"""texture-feature-extraction — 纹理特征提取

基于灰度共生矩阵（GLCM, Gray-Level Co-occurrence Matrix）提取影像纹理
特征，用于辅助地物分类、建筑/植被区分、SAR 纹理与地质构造解译。

算法：
- 把单波段影像量化为有限灰度级；
- 在滑动窗口内用 ``skimage.feature.graycomatrix`` 计算 GLCM
  （4 个方向：0°/45°/90°/135°，对称 + 归一化）；
- 用 ``skimage.feature.graycoprops`` 提取
  contrast / dissimilarity / homogeneity / energy / correlation / ASM；
- 多方向取平均，得到逐像元纹理值。

输出：多波段纹理 GeoTIFF（每特征一波段）+ 纹理统计 JSON。

数据源：本地 GeoTIFF（默认用第 1 波段），或使用 ``--synthetic`` 生成
含平滑区与粗糙区的模拟影像用于离线验证（粗糙区 contrast 应更高）。

隐私声明 / Privacy：
- 默认离线运行，仅在显式 ``--place`` 解析地名时才会访问 Nominatim/Open-Meteo。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python texture-feature-extraction.py --input scene.tif --window 7 --features contrast,energy
    python texture-feature-extraction.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "texture-feature-extraction"

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


# skimage graycoprops 支持的特征名
SUPPORTED_FEATURES = [
    "contrast", "dissimilarity", "homogeneity", "energy", "correlation", "ASM",
]
# GLCM 方向：0°, 45°, 90°, 135°
ANGLES = [0.0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# bbox validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox, *, kind: str = "bbox"):
    """校验 W<S<E<N、lat∈[-90,90]、lon∈[-180,180]、跨 180° 单独报错。

    返回 [W, S, E, N]。失败抛 ValidationError (rc=6)。
    """
    if bbox is None:
        raise ValidationError(f"{kind} is required")
    if len(bbox) != 4:
        raise ValidationError(f"{kind} must have 4 floats [W S E N], got {len(bbox)}",
                              bbox=list(bbox))
    w, s, e, n = (float(x) for x in bbox)
    if not all(np.isfinite(v) for v in (w, s, e, n)):
        raise ValidationError(f"{kind} contains non-finite values", bbox=[w, s, e, n])
    if w == e or s == n:
        raise ValidationError(f"{kind} has zero area: W==E or S==N", bbox=[w, s, e, n])
    if w > e:
        raise ValidationError(
            f"{kind} crosses the 180° meridian (W={w} > E={e}); "
            "please split into two sub-bboxes or shift longitudes",
            bbox=[w, s, e, n],
        )
    if s > n:
        raise ValidationError(f"{kind} has S > N (S={s} > N={n})", bbox=[w, s, e, n])
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"{kind} latitude out of range [-90, 90]: S={s}, N={n}",
            bbox=[w, s, e, n],
        )
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"{kind} longitude out of range [-180, 180]: W={w}, E={e}",
            bbox=[w, s, e, n],
        )
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def quantize_band(band: np.ndarray, levels: int = 32) -> np.ndarray:
    """把浮点波段线性量化到 [0, levels-1] 的 uint8（NaN 像素被填 0）。"""
    valid = band[np.isfinite(band)]
    if valid.size == 0:
        return np.zeros(band.shape, dtype=np.uint8)
    bmin, bmax = float(valid.min()), float(valid.max())
    if bmax - bmin < 1e-12:
        return np.zeros(band.shape, dtype=np.uint8)
    q = (band - bmin) / (bmax - bmin) * (levels - 1)
    q = np.nan_to_num(q, nan=0.0)
    return np.clip(q, 0, levels - 1).astype(np.uint8)


def compute_texture(
    band: np.ndarray,
    window: int = 5,
    features: Optional[List[str]] = None,
    levels: int = 32,
) -> Dict[str, np.ndarray]:
    """对单波段影像逐像元滑窗计算 GLCM 纹理特征（多方向平均）。

    返回 {feature_name: (H, W) float32 array}。若 band 中含 NaN 像素，含 NaN 的
    窗口中心像元被标记为 NaN 输出（NaN-safe 滑窗）。
    """
    from skimage.feature import graycomatrix, graycoprops

    if features is None:
        features = ["contrast", "homogeneity", "energy"]
    bad = [f for f in features if f not in SUPPORTED_FEATURES]
    if bad:
        raise UsageError(
            f"unsupported feature(s) {bad}. Choose from: {SUPPORTED_FEATURES}",
            features=bad,
        )
    if window < 3 or window % 2 == 0:
        raise UsageError(f"--window must be an odd integer >= 3, got {window}",
                         window=window)

    h, w = band.shape
    q = quantize_band(band, levels)
    # 单独算 NaN mask（quantize_band 内部 nan->0）；含 NaN 的窗口中心输出 NaN
    has_nan = bool(np.any(~np.isfinite(band)))
    r = window // 2
    qp = np.pad(q, r, mode="reflect")
    nan_mask = (~np.isfinite(band)).astype(np.uint8)
    nan_pad = np.pad(nan_mask, r, mode="reflect")

    out = {f: np.full((h, w), np.nan, dtype=np.float32) for f in features}

    for i in range(h):
        for j in range(w):
            if has_nan and nan_pad[i:i + window, j:j + window].any():
                continue
            patch = qp[i:i + window, j:j + window]
            glcm = graycomatrix(
                patch, distances=[1], angles=ANGLES,
                levels=levels, symmetric=True, normed=True,
            )
            for f in features:
                props = graycoprops(glcm, f)  # shape (1, 4)
                out[f][i, j] = float(np.mean(props))
    return out


def feature_stats(arr: np.ndarray) -> Dict[str, Any]:
    valid = arr[np.isfinite(arr)]
    if valid.size == 0:
        return {"min": 0.0, "max": 0.0, "mean": 0.0, "std": 0.0}
    return {
        "min": float(np.min(valid)),
        "max": float(np.max(valid)),
        "mean": float(np.mean(valid)),
        "std": float(np.std(valid)),
    }


# ---------------------------------------------------------------------------
# 合成数据：平滑区 vs 粗糙区（离线验证）
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float],
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (1, H, W) 影像：左半平滑（低频渐变），右半粗糙（高频噪声）。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xx = xx.astype(np.float32) / max(width - 1, 1)
    yy = yy.astype(np.float32) / max(height - 1, 1)

    smooth = 0.5 + 0.3 * xx + 0.1 * yy  # 平滑渐变
    rough = rng.uniform(0.0, 1.0, (height, width)).astype(np.float32)  # 高频噪声

    half = width // 2
    band = np.empty((height, width), dtype=np.float32)
    band[:, :half] = smooth[:, :half]
    band[:, half:] = rough[:, half:]

    cube = band[np.newaxis, ...]
    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "smooth_region": [0, half],
        "rough_region": [half, width],
    }
    return cube, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    cube: np.ndarray,
    bbox: List[float],
    nodata: float = -9999.0,
) -> None:
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
    """读 GeoTIFF；NoData 像素替换为 NaN 后返回 (cube, bbox)。

    元数据通过模块级 _LAST_READ_META 暴露：nodata / n_valid_pixels / n_total_pixels。
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [float(b.left), float(b.bottom), float(b.right), float(b.top)]
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    n_valid = int(np.count_nonzero(np.isfinite(cube)))
    n_total = int(cube.size)
    globals()["_LAST_READ_META"] = {
        "nodata": nodata, "n_valid_pixels": n_valid, "n_total_pixels": n_total,
    }
    return cube, bbox


def get_last_read_meta() -> Dict[str, Any]:
    return globals().get("_LAST_READ_META", {"nodata": None,
                                              "n_valid_pixels": 0,
                                              "n_total_pixels": 0})


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
            "window": getattr(args, "window", None),
            "features": getattr(args, "features", None),
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
def parse_features(arg: Optional[str]) -> List[str]:
    if not arg:
        return ["contrast", "homogeneity", "energy"]
    feats = [s.strip() for s in arg.split(",") if s.strip()]
    # 规范化 ASM 大小写
    norm = []
    for f in feats:
        match = [s for s in SUPPORTED_FEATURES if s.lower() == f.lower()]
        if not match:
            raise UsageError(
                f"unsupported feature '{f}'. Choose from: {SUPPORTED_FEATURES}",
                feature=f,
            )
        norm.append(match[0])
    return norm


def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir
    bbox = list(args.bbox) if args.bbox else None
    features = parse_features(args.features)

    # 1) 获取数据立方体（通用契约）
    synth_info: Optional[Dict[str, Any]] = None
    in_meta: Dict[str, Any] = {"nodata": None, "n_valid_pixels": 0, "n_total_pixels": 0}
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        in_meta = get_last_read_meta()
        if bbox is not None:
            bbox = validate_bbox(bbox, kind="--bbox")
        else:
            bbox = validate_bbox(file_bbox, kind="--input file bbox")
        if in_meta["n_valid_pixels"] == 0:
            raise ValidationError(
                f"input raster has no valid pixels (all NoData={in_meta['nodata']})",
                path=args.input, n_total_pixels=in_meta["n_total_pixels"],
            )
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox, kind="--bbox")
        cube, synth_info = generate_synthetic_cube(bbox)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    # 校验通过后再建目录（失败时不留空目录）
    os.makedirs(output_dir, exist_ok=True)

    # 用第 1 波段做纹理（默认灰度）
    band = cube[0]

    # 2) GLCM 纹理
    tex = compute_texture(band, window=args.window, features=features)

    # 3) 组装多波段纹理栅格 + 写出
    tex_cube = np.stack([tex[f] for f in features], axis=0).astype(np.float32)
    out_tif = os.path.join(output_dir, "texture_features.tif")
    write_geotiff(out_tif, tex_cube, bbox)

    stats_doc = {
        "window": args.window,
        "features": features,
        "angles_deg": [0.0, 45.0, 90.0, 135.0],
        "per_feature": {f: feature_stats(tex[f]) for f in features},
    }
    stats_path = os.path.join(output_dir, "texture_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats_doc, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "window": args.window,
        "features": features,
        "mean_per_feature": {f: stats_doc["per_feature"][f]["mean"] for f in features},
    }
    if synth_info is not None:
        qa["synthetic_regions"] = {
            "smooth": synth_info["smooth_region"],
            "rough": synth_info["rough_region"],
        }
    if args.input and not args.synthetic:
        qa["input_nodata"] = in_meta["nodata"]
        qa["input_n_valid_pixels"] = in_meta["n_valid_pixels"]
        qa["input_n_total_pixels"] = in_meta["n_total_pixels"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(tex_cube.shape[0])},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] window: {args.window}  features: {features}")
        for f in features:
            st = stats_doc["per_feature"][f]
            print(f"[{SKILL_NAME}]   {f:14s} mean={st['mean']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="GLCM texture feature extraction for raster imagery.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF (uses band 1)")
    p.add_argument("--window", type=int, default=5,
                   help="odd sliding-window size for GLCM (default: 5)")
    p.add_argument("--features", default=None,
                   help="comma-separated features (default: contrast,homogeneity,energy). "
                        f"Available: {','.join(SUPPORTED_FEATURES)}")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a smooth-vs-rough synthetic scene (offline)")
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
