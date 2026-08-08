#!/usr/bin/env python3
"""biodiversity-mapping — 生物多样性制图

基于「生境异质性假说」（habitat heterogeneity hypothesis）估算物种丰富度的
空间代理。用三类遥感/地形代理量加权融合，再经饱和曲线映射为相对物种丰富度：

- **植被生产力代理**：NDVI（红/近红外）——能量可得性，支持更多营养级。
- **结构异质性代理**：NDVI 局部标准差（纹理）——生境结构多样性。
- **地形异质性代理**：DEM 地表粗糙度（梯度模）——微生境与生态位多样性。

三个代理先各自归一化到 [0, 1]，加权得到「生境质量」q，再经
S = Smax * (1 - exp(-k * q)) 饱和曲线得到相对物种丰富度（避免线性外推）。

数据源：本地多光谱 GeoTIFF（band1=红, band2=近红外[, band3=DEM]），或使用
``--synthetic`` 生成物理一致的模拟影像用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，仅 ``--place`` 解析地名时才访问 Nominatim/Open-Meteo。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python biodiversity-mapping.py --input scene.tif --method heterogeneity
    python biodiversity-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "biodiversity-mapping"

# ---- 复用共享核心库（本地 vendored，随脚本目录一起分发）----
try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, DependencyError, ValidationError, ProcessError,
        to_exit_code,
    )
    from _geoskill_core.manifest import OutputManifest, OutputFile
except ImportError:  # pragma: no cover - fallback minimal definitions
    class GeoSkillError(Exception):
        def __init__(self, message: str, code: int = 7, kind: str = "EGeo", **kw):
            super().__init__(message)
            self.message, self.code, self.kind = message, code, kind

    class UsageError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=2, kind="EUsage", **k)

    class DependencyError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=3, kind="EDependency", **k)

    class ValidationError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=6, kind="EValidate", **k)

    class ProcessError(GeoSkillError):
        def __init__(self, m, **k): super().__init__(m, code=7, kind="EProcess", **k)

    def to_exit_code(exc):
        return getattr(exc, "code", 7)

    OutputManifest = None
    OutputFile = None


# ---------------------------------------------------------------------------
# 方法权重：heterogeneity 强调结构/地形多样性；productivity 强调能量可得性
# ---------------------------------------------------------------------------
METHODS: Dict[str, Dict[str, float]] = {
    "heterogeneity": {"w_veg": 0.35, "w_texture": 0.40, "w_terrain": 0.25},
    "productivity": {"w_veg": 0.60, "w_texture": 0.25, "w_terrain": 0.15},
}


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
def ndvi(red: np.ndarray, nir: np.ndarray) -> np.ndarray:
    """归一化植被指数 NDVI = (NIR - RED) / (NIR + RED)，裁剪到 [-1, 1]。

    输入中的 NaN（NoData 像素）保持 NaN 传播，供上层掩膜。
    """
    r = red.astype(np.float64)
    n = nir.astype(np.float64)
    denom = n + r
    out = np.zeros_like(r, dtype=np.float64)
    mask = np.abs(denom) > 1e-9
    out[mask] = (n[mask] - r[mask]) / denom[mask]
    out[~np.isfinite(denom)] = np.nan
    return np.clip(out, -1.0, 1.0).astype(np.float32)


def local_heterogeneity(arr: np.ndarray, window: int = 5) -> np.ndarray:
    """局部标准差（纹理）：以窗口内方差开方度量结构异质性。恒值表面为 0。

    NaN（NoData）像素以 0 填充参与计算，但输出在 NaN 位置保持 NaN。
    """
    try:
        from scipy.ndimage import uniform_filter
    except ImportError as exc:
        raise DependencyError(
            f"scipy is required for local_heterogeneity: {exc}"
        ) from exc

    a = arr.astype(np.float64)
    nan_mask = ~np.isfinite(a)
    a_fill = np.where(nan_mask, 0.0, a)
    size = max(int(window), 1)
    mean = uniform_filter(a_fill, size=size, mode="reflect")
    sq_mean = uniform_filter(a_fill * a_fill, size=size, mode="reflect")
    var = np.clip(sq_mean - mean * mean, 0.0, None)
    out = np.sqrt(var).astype(np.float32)
    out[nan_mask] = np.nan
    return out


def terrain_roughness(dem: np.ndarray) -> np.ndarray:
    """地表粗糙度：DEM 梯度模（|∇z|），度量地形起伏带来的微生境多样性。

    NaN（NoData）像素以 0 填充参与计算，但输出在 NaN 位置保持 NaN。
    """
    z = dem.astype(np.float64)
    nan_mask = ~np.isfinite(z)
    z_fill = np.where(nan_mask, 0.0, z)
    gy, gx = np.gradient(z_fill)
    out = np.sqrt(gx * gx + gy * gy).astype(np.float32)
    out[nan_mask] = np.nan
    return out


def normalize01(arr: np.ndarray) -> np.ndarray:
    """min-max 归一化到 [0, 1]；恒值返回全 0；NaN 位置保持 NaN。"""
    a = arr.astype(np.float64)
    finite = a[np.isfinite(a)]
    if finite.size == 0:
        return np.full_like(a, np.nan, dtype=np.float32)
    lo, hi = float(np.min(finite)), float(np.max(finite))
    if hi - lo < 1e-9:
        return np.where(np.isfinite(a), 0.0, np.nan).astype(np.float32)
    out = np.where(np.isfinite(a), (a - lo) / (hi - lo), np.nan)
    return np.clip(out, 0.0, 1.0).astype(np.float32)


def species_richness(
    ndvi_arr: np.ndarray,
    texture: np.ndarray,
    roughness: np.ndarray,
    method: str = "heterogeneity",
    s_max: float = 200.0,
    k: float = 3.0,
) -> Tuple[np.ndarray, np.ndarray]:
    """由三个归一化代理加权得生境质量 q，经饱和曲线得相对物种丰富度。

    返回 (richness, habitat_quality)。richness ∈ [0, s_max]。
    """
    if method not in METHODS:
        raise UsageError(
            f"unknown method '{method}'. Choose from: {sorted(METHODS)}",
            method=method,
        )
    if not np.isfinite(s_max) or s_max <= 0.0:
        raise ValidationError(f"s_max must be a positive finite number; got {s_max!r}")
    if not np.isfinite(k) or k <= 0.0:
        raise ValidationError(f"k must be a positive finite number; got {k!r}")
    w = METHODS[method]
    q = (
        w["w_veg"] * normalize01(ndvi_arr)
        + w["w_texture"] * normalize01(texture)
        + w["w_terrain"] * normalize01(roughness)
    ).astype(np.float32)
    richness = (s_max * (1.0 - np.exp(-k * q.astype(np.float64)))).astype(np.float32)
    return richness, q


# ---------------------------------------------------------------------------
# 合成数据：物理一致的模拟影像（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (3, H, W) 立方体：band1=红反射率, band2=近红外反射率, band3=DEM(m)。

    地物：左下=水体（低 NIR / 高 RED），右上=植被（高 NIR / 低 RED），
    其余=裸土。DEM 在植被区叠加起伏，制造地形异质性。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yy /= max(height - 1, 1)
    xx /= max(width - 1, 1)

    veg = ((xx + yy) > 1.1)
    water = ((xx + yy) < 0.5)

    red = np.where(veg, 0.04, np.where(water, 0.11, 0.18)).astype(np.float32)
    nir = np.where(veg, 0.45, np.where(water, 0.02, 0.25)).astype(np.float32)
    red += rng.normal(0, 0.006, red.shape).astype(np.float32)
    nir += rng.normal(0, 0.010, nir.shape).astype(np.float32)
    red = np.clip(red, 0.0, 1.0)
    nir = np.clip(nir, 0.0, 1.0)

    # DEM：整体缓坡 + 植被区额外起伏（山丘）
    base = 200.0 + 300.0 * xx.astype(np.float32)
    hills = np.where(
        veg,
        120.0 * np.sin(6.0 * np.pi * xx) * np.cos(6.0 * np.pi * yy),
        0.0,
    ).astype(np.float32)
    dem = base + hills + rng.normal(0, 3.0, base.shape).astype(np.float32)

    cube = np.stack([red, nir, dem], axis=0).astype(np.float32)
    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "bands": ["red", "nir", "dem"],
        "veg_fraction": float(np.mean(veg)),
        "water_fraction": float(np.mean(water)),
    }
    return cube, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
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
            band = cube[b].astype("float32")
            band = np.where(np.isfinite(band), band, nodata)
            dst.write(band, b + 1)


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
            "method": getattr(args, "method", None),
            "window": getattr(args, "window", None),
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

    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    # ---- validation (BEFORE os.makedirs to avoid empty output dirs) ----
    if bbox is None:
        raise UsageError("could not determine bbox")
    validate_bbox(bbox, ctx="bbox")
    if args.window < 1:
        raise ValidationError(f"--window must be >= 1 (got {args.window})")
    if cube.size == 0:
        raise ValidationError("input raster is empty")
    nb = cube.shape[0]
    if nb < 2:
        raise ValidationError(
            f"input raster must have at least 2 bands (red + nir); got {nb} band(s)"
        )
    if args.input and not args.synthetic:
        valid_count = int(np.sum(np.isfinite(cube)))
        if valid_count == 0:
            raise ValidationError(
                f"input raster has no valid (non-NoData) pixels: {args.input}"
            )
        for b in (0, 1):
            if not bool(np.isfinite(cube[b]).any()):
                raise ValidationError(
                    f"input raster band {b + 1} (red/nir) has no valid pixels"
                )
    os.makedirs(output_dir, exist_ok=True)

    nb = cube.shape[0]
    red = cube[0]
    nir = cube[1] if nb >= 2 else cube[0]
    dem = cube[2] if nb >= 3 else None

    ndvi_arr = ndvi(red, nir)
    texture = local_heterogeneity(ndvi_arr, window=args.window)
    if dem is not None:
        roughness = terrain_roughness(dem)
    else:
        # 无 DEM 时用 NDVI 纹理梯度作为地形异质性代理
        roughness = local_heterogeneity(ndvi_arr, window=max(args.window, 7))

    richness, quality = species_richness(
        ndvi_arr, texture, roughness,
        method=args.method, s_max=args.s_max, k=args.k,
    )

    out_rich = os.path.join(output_dir, "species_richness.tif")
    out_qual = os.path.join(output_dir, "habitat_quality.tif")
    write_geotiff(out_rich, richness, bbox)
    write_geotiff(out_qual, quality, bbox)

    params = {
        "method": args.method,
        "weights": METHODS[args.method],
        "window": args.window,
        "s_max": args.s_max,
        "k": args.k,
        "mean_ndvi": float(np.nanmean(ndvi_arr)),
        "mean_texture": float(np.nanmean(texture)),
        "mean_roughness": float(np.nanmean(roughness)),
    }
    params_path = os.path.join(output_dir, "richness_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    valid = np.isfinite(richness)
    n_valid_pixels = int(np.sum(valid))
    n_total_pixels = int(richness.size)
    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "n_input_bands": int(nb),
        "n_valid_pixels": n_valid_pixels,
        "n_total_pixels": n_total_pixels,
        "mean_ndvi": float(np.nanmean(ndvi_arr)),
        "mean_habitat_quality": float(np.nanmean(quality)),
        "mean_richness": float(np.nanmean(richness)),
        "max_richness": float(np.nanmax(richness)),
    }
    if args.input and not args.synthetic:
        qa["input_nodata"] = -9999.0
    if synth_info is not None:
        qa["synthetic_veg_fraction"] = synth_info["veg_fraction"]

    outputs = [
        {"path": out_rich, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_qual, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}")
        print(f"[{SKILL_NAME}] shape: {richness.shape}")
        print(f"[{SKILL_NAME}] mean richness: {qa['mean_richness']:.2f}  max: {qa['max_richness']:.2f}")
        print(f"[{SKILL_NAME}] output: {out_rich}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Biodiversity mapping via habitat-heterogeneity richness proxies.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF (band1=red, band2=nir[, band3=DEM])")
    p.add_argument("--method", default="heterogeneity", choices=sorted(METHODS.keys()),
                   help="richness model (default: heterogeneity)")
    p.add_argument("--window", type=int, default=5,
                   help="texture window size in pixels (default: 5)")
    p.add_argument("--s-max", type=float, default=200.0,
                   help="asymptotic maximum species richness (default: 200)")
    p.add_argument("--k", type=float, default=3.0,
                   help="saturation curve rate (default: 3)")
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
