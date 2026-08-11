#!/usr/bin/env python3
"""band-ratio-analysis — 波段比值分析

批量计算多光谱影像的光谱指数（波段比值/归一化指数）。内置常用指数：

- **NDVI** = (NIR-Red)/(NIR+Red)          归一化植被指数
- **NDWI** = (Green-NIR)/(Green+NIR)      归一化水体指数 (McFeeters 1996)
- **MNDWI** = (Green-SWIR)/(Green+SWIR)   改进型归一化水体指数 (Xu 2006)
- **NDBI** = (SWIR-NIR)/(SWIR+NIR)        归一化建筑指数 (Zha 2003)
- **EVI** = 2.5*(NIR-Red)/(NIR+6*Red-7.5*Blue+1)  增强型植被指数
- **SAVI** = 1.5*(NIR-Red)/(NIR+Red+0.5)  土壤调节植被指数 (Huete 1988)

每个被选中的指数输出一幅单波段 GeoTIFF，并附值域统计 JSON。

数据源：本地多光谱 GeoTIFF（波段顺序 blue/green/red/nir/swir1/swir2），
或使用 ``--synthetic`` 生成物理一致的模拟影像用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，仅在显式 ``--place`` 解析地名时才会访问 Nominatim/Open-Meteo。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python band-ratio-analysis.py --input scene.tif --indices ndvi,ndwi
    python band-ratio-analysis.py --bbox 116 39 117 40 --synthetic --output-dir ./out

License: MIT
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np

VERSION = "1.0.0"
SKILL_NAME = "band-ratio-analysis"

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


# 波段名 -> 在合成/默认立方体中的索引（Landsat 风格 6 波段）
BAND_INDEX = {
    "blue": 0,
    "green": 1,
    "red": 2,
    "nir": 3,
    "swir1": 4,
    "swir2": 5,
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


def _safe_ratio(num: np.ndarray, den: np.ndarray) -> np.ndarray:
    """逐像元除法，分母为 0（或极小）处返回 0，避免 inf/nan。"""
    out = np.zeros_like(num, dtype=np.float32)
    mask = np.abs(den) > 1e-12
    np.divide(num, den, out=out, where=mask)
    return out


# ---------------------------------------------------------------------------
# 指数公式（输入 bands: {name: 2D array}，返回 2D float32 array）
# ---------------------------------------------------------------------------
def _ndvi(b: Dict[str, np.ndarray]) -> np.ndarray:
    return _safe_ratio(b["nir"] - b["red"], b["nir"] + b["red"])


def _ndwi(b: Dict[str, np.ndarray]) -> np.ndarray:
    return _safe_ratio(b["green"] - b["nir"], b["green"] + b["nir"])


def _mndwi(b: Dict[str, np.ndarray]) -> np.ndarray:
    return _safe_ratio(b["green"] - b["swir1"], b["green"] + b["swir1"])


def _ndbi(b: Dict[str, np.ndarray]) -> np.ndarray:
    return _safe_ratio(b["swir1"] - b["nir"], b["swir1"] + b["nir"])


def _evi(b: Dict[str, np.ndarray]) -> np.ndarray:
    num = 2.5 * (b["nir"] - b["red"])
    den = b["nir"] + 6.0 * b["red"] - 7.5 * b["blue"] + 1.0
    return _safe_ratio(num, den)


def _savi(b: Dict[str, np.ndarray]) -> np.ndarray:
    return _safe_ratio(1.5 * (b["nir"] - b["red"]), b["nir"] + b["red"] + 0.5)


# 指数注册表：name -> (所需波段, 计算函数, 中文名, 理论值域)
INDICES: Dict[str, Dict[str, Any]] = {
    "ndvi":  {"bands": ["nir", "red"],            "fn": _ndvi,
              "desc": "归一化植被指数", "range": [-1.0, 1.0]},
    "ndwi":  {"bands": ["green", "nir"],          "fn": _ndwi,
              "desc": "归一化水体指数", "range": [-1.0, 1.0]},
    "mndwi": {"bands": ["green", "swir1"],        "fn": _mndwi,
              "desc": "改进型归一化水体指数", "range": [-1.0, 1.0]},
    "ndbi":  {"bands": ["swir1", "nir"],          "fn": _ndbi,
              "desc": "归一化建筑指数", "range": [-1.0, 1.0]},
    "evi":   {"bands": ["nir", "red", "blue"],    "fn": _evi,
              "desc": "增强型植被指数", "range": [-1.0, 1.0]},
    "savi":  {"bands": ["nir", "red"],            "fn": _savi,
              "desc": "土壤调节植被指数", "range": [-1.0, 1.0]},
}


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def compute_index(name: str, bands: Dict[str, np.ndarray]) -> np.ndarray:
    """计算单个指数。name 不在注册表 → UsageError；缺波段 → ValidationError。"""
    key = name.lower()
    if key not in INDICES:
        raise UsageError(
            f"unknown index '{name}'. Choose from: {sorted(INDICES)}",
            index=name,
        )
    need = INDICES[key]["bands"]
    missing = [bn for bn in need if bn not in bands]
    if missing:
        raise ValidationError(
            f"index '{key}' requires bands {need} but missing {missing}",
            index=key, missing=missing,
        )
    result = INDICES[key]["fn"](bands)
    return np.nan_to_num(result, nan=0.0, posinf=0.0, neginf=0.0).astype(np.float32)


def index_stats(arr: np.ndarray) -> Dict[str, Any]:
    """值域统计：min/max/mean/std + 分位数。"""
    valid = arr[np.isfinite(arr)]
    if valid.size == 0:
        return {"min": 0.0, "max": 0.0, "mean": 0.0, "std": 0.0,
                "p10": 0.0, "p90": 0.0, "n_valid": 0}
    return {
        "min": float(np.min(valid)),
        "max": float(np.max(valid)),
        "mean": float(np.mean(valid)),
        "std": float(np.std(valid)),
        "p10": float(np.percentile(valid, 10)),
        "p90": float(np.percentile(valid, 90)),
        "n_valid": int(valid.size),
    }


# ---------------------------------------------------------------------------
# 合成数据：物理一致的 6 波段模拟影像（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float],
    width: int = 128,
    height: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (6, H, W) 反射率立方体（蓝绿红NIR SWIR1 SWIR2），含三类地物。

    地物真值反射率（典型值）：植被（高 NIR）、土壤（平坦递增）、水体（低且递减）。
    """
    rng = np.random.default_rng(seed)

    yy, xx = np.mgrid[0:height, 0:width]
    yy = yy.astype(np.float32) / max(height - 1, 1)
    xx = xx.astype(np.float32) / max(width - 1, 1)

    veg_mask = ((xx + yy) > 1.1).astype(np.float32)
    water_mask = ((xx + yy) < 0.5).astype(np.float32)
    soil_mask = np.clip(1.0 - veg_mask - water_mask, 0.0, 1.0)

    # 顺序：蓝 绿 红 NIR SWIR1 SWIR2
    veg_rho = [0.03, 0.08, 0.04, 0.45, 0.20, 0.12]
    soil_rho = [0.10, 0.14, 0.18, 0.28, 0.32, 0.30]
    water_rho = [0.06, 0.05, 0.03, 0.01, 0.005, 0.001]

    cube = np.zeros((6, height, width), dtype=np.float32)
    for b in range(6):
        rho = (
            veg_mask * veg_rho[b]
            + soil_mask * soil_rho[b]
            + water_mask * water_rho[b]
        )
        rho = rho + rng.normal(0, 0.005, size=rho.shape).astype(np.float32)
        cube[b] = np.clip(rho, 0.0, 1.0)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "band_names": list(BAND_INDEX.keys()),
        "mean_per_band": {
            name: float(np.mean(cube[i])) for name, i in BAND_INDEX.items()
        },
    }
    return cube, info


def cube_to_bands(cube: np.ndarray, band_names: List[str]) -> Dict[str, np.ndarray]:
    """把 (bands, H, W) 立方体按名字典展开。"""
    return {name: cube[i].astype(np.float32)
            for name, i in BAND_INDEX.items() if i < cube.shape[0]}


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
            "indices": getattr(args, "indices", None),
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
def parse_indices(arg: Optional[str]) -> List[str]:
    """解析 --indices 逗号列表；缺省 = 全部指数。"""
    if not arg:
        return list(INDICES.keys())
    names = [s.strip().lower() for s in arg.split(",") if s.strip()]
    bad = [n for n in names if n not in INDICES]
    if bad:
        raise UsageError(
            f"unknown index(es) {bad}. Choose from: {sorted(INDICES)}",
            indices=bad,
        )
    return names


def process(args: argparse.Namespace) -> int:
    started_at = _utc_now()
    output_dir = args.output_dir

    bbox = list(args.bbox) if args.bbox else None
    indices = parse_indices(args.indices)

    # 1) 获取数据立方体（通用契约）
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, synth_info = generate_synthetic_cube(bbox)
        source_note = "synthetic"

    # ---- validation (BEFORE os.makedirs to avoid empty output dirs) ----
    if bbox is None:
        raise UsageError("could not determine bbox")
    validate_bbox(bbox, ctx="bbox")
    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if args.input and not args.synthetic:
        valid_count = int(np.sum(np.isfinite(cube)))
        if valid_count == 0:
            raise ValidationError(
                f"input raster has no valid (non-NoData) pixels: {args.input}"
            )
    os.makedirs(output_dir, exist_ok=True)

    bands = cube_to_bands(cube, list(BAND_INDEX.keys()))

    # 2) 逐指数计算 + 写出
    outputs: List[Dict[str, Any]] = []
    all_stats: Dict[str, Any] = {}
    for name in indices:
        arr = compute_index(name, bands)
        st = index_stats(arr)
        st["description"] = INDICES[name]["desc"]
        st["theoretical_range"] = INDICES[name]["range"]
        all_stats[name] = st

        out_tif = os.path.join(output_dir, f"{name}.tif")
        write_geotiff(out_tif, arr, bbox)
        outputs.append({
            "path": out_tif, "kind": "raster", "crs_epsg": 4326,
            "bbox_wgs84": bbox, "band_count": 1,
        })

    stats_path = os.path.join(output_dir, "index_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(all_stats, f, ensure_ascii=False, indent=2)
    outputs.append({"path": stats_path, "kind": "json"})

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_indices": len(indices),
        "indices": indices,
        "mean_per_index": {k: v["mean"] for k, v in all_stats.items()},
    }
    if synth_info is not None:
        qa["synthetic_mean_per_band"] = synth_info["mean_per_band"]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] indices: {indices}")
        for name in indices:
            st = all_stats[name]
            print(f"[{SKILL_NAME}]   {name:6s} mean={st['mean']:+.4f} "
                  f"[{st['min']:+.4f}, {st['max']:+.4f}]")
        print(f"[{SKILL_NAME}] stats: {stats_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Batch spectral index (band ratio) computation for multispectral imagery.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multispectral GeoTIFF (bands: blue/green/red/nir/swir1/swir2)")
    p.add_argument("--indices", default=None,
                   help="comma-separated indices (default: all). "
                        f"Available: {','.join(sorted(INDICES))}")
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
