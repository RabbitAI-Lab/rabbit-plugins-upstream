#!/usr/bin/env python3
"""crop-health-diagnosis — 作物健康诊断

融合多光谱指数（NDVI / NDRE）与热红外（LST）构建综合健康评分，结合历史
NDVI 基线做异常（偏差）检测，并用 K-means 空间聚类划分健康等级分区。

核心算法
--------
- **NDVI**  = (NIR - Red) / (NIR + Red)
- **NDRE**  = (NIR - RedEdge) / (NIR + RedEdge)（红边归一化，对叶绿素敏感）
- **健康评分**：对 NDVI/NDRE/LST 归一化后加权合成，0（差）~1（健康）。
  LST 越高通常代表蒸散发受限、胁迫越强，故取 (1 - LST_norm)。
- **历史偏差异常检测**：z = (NDVI_now - hist_mean) / hist_std，
  负 z 表示当前长势低于历史同期（疑似胁迫）。
- **空间聚类**：K-means 对 [NDVI, NDRE, LST] 特征聚类，划分管理分区。

数据源：本地多光谱 + 热红外 GeoTIFF，或 ``--synthetic`` 离线模拟。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python crop-health-diagnosis.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "crop-health-diagnosis"

try:
    from _geoskill_core.errors import (
        GeoSkillError, UsageError, ValidationError, ProcessError, DependencyError, to_exit_code,
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
# 核心算法
# ---------------------------------------------------------------------------
def _safe_ratio(num: np.ndarray, den: np.ndarray) -> np.ndarray:
    """逐像元除法，分母接近 0 时返回 0，避免 inf/nan。"""
    out = np.zeros_like(num, dtype=np.float32)
    mask = np.abs(den) > 1e-9
    np.divide(num, den, out=out, where=mask)
    return out


def compute_ndvi(red: np.ndarray, nir: np.ndarray) -> np.ndarray:
    """归一化植被指数 NDVI = (NIR - Red) / (NIR + Red)，范围 [-1, 1]。"""
    red = np.asarray(red, dtype=np.float32)
    nir = np.asarray(nir, dtype=np.float32)
    return np.clip(_safe_ratio(nir - red, nir + red), -1.0, 1.0).astype(np.float32)


def compute_ndre(rededge: np.ndarray, nir: np.ndarray) -> np.ndarray:
    """红边归一化指数 NDRE = (NIR - RedEdge) / (NIR + RedEdge)，范围 [-1, 1]。"""
    rededge = np.asarray(rededge, dtype=np.float32)
    nir = np.asarray(nir, dtype=np.float32)
    return np.clip(_safe_ratio(nir - rededge, nir + rededge), -1.0, 1.0).astype(np.float32)


def normalize01(arr: np.ndarray, lo: float, hi: float) -> np.ndarray:
    """把 arr 从物理区间 [lo, hi] 线性拉伸到 [0, 1]。"""
    arr = np.asarray(arr, dtype=np.float32)
    if hi <= lo:
        raise ValidationError("normalize01 requires hi > lo", lo=lo, hi=hi)
    return np.clip((arr - lo) / (hi - lo), 0.0, 1.0).astype(np.float32)


def health_score(
    ndvi: np.ndarray,
    ndre: np.ndarray,
    lst: np.ndarray,
    w_ndvi: float = 0.4,
    w_ndre: float = 0.3,
    w_lst: float = 0.3,
    lst_lo: float = 293.0,
    lst_hi: float = 323.0,
) -> np.ndarray:
    """综合健康评分，范围 [0, 1]。

    NDVI/NDRE 已在 [-1,1]，拉伸到 [0,1]；LST（开尔文）越高越胁迫，取反向。
    """
    ndvi_n = normalize01(ndvi, -0.2, 0.9)
    ndre_n = normalize01(ndre, -0.2, 0.6)
    lst_n = normalize01(lst, lst_lo, lst_hi)
    score = w_ndvi * ndvi_n + w_ndre * ndre_n + w_lst * (1.0 - lst_n)
    return np.clip(score, 0.0, 1.0).astype(np.float32)


def anomaly_zscore(current: np.ndarray, hist_mean: np.ndarray, hist_std: np.ndarray) -> np.ndarray:
    """历史偏差 z 分数：(当前 - 历史均值) / 历史标准差。负值=低于历史同期。"""
    current = np.asarray(current, dtype=np.float32)
    hist_mean = np.asarray(hist_mean, dtype=np.float32)
    hist_std = np.asarray(hist_std, dtype=np.float32)
    std = np.maximum(hist_std, 1e-3)
    return ((current - hist_mean) / std).astype(np.float32)


def spatial_cluster(features: np.ndarray, n_clusters: int = 3, seed: int = 42) -> np.ndarray:
    """对 (H, W, F) 特征做 K-means 空间聚类，返回 (H, W) 整型标签。"""
    try:
        from sklearn.cluster import KMeans
    except ImportError as exc:  # pragma: no cover
        raise DependencyError("scikit-learn is required for spatial clustering") from exc
    if n_clusters < 1:
        raise ValidationError("n_clusters must be >= 1", n_clusters=int(n_clusters))
    h, w = features.shape[:2]
    flat = features.reshape(-1, features.shape[-1]).astype(np.float32)
    finite = np.nan_to_num(flat, nan=0.0, posinf=0.0, neginf=0.0)
    k = min(n_clusters, max(1, int(np.unique(np.round(finite, 4), axis=0).shape[0])))
    km = KMeans(n_clusters=k, n_init=10, random_state=seed)
    labels = km.fit_predict(finite)
    return labels.reshape(h, w).astype(np.int32)


def classify_health(score: np.ndarray) -> np.ndarray:
    """把 [0,1] 健康评分分为 4 级：0=差, 1=偏差, 2=中等, 3=健康。"""
    score = np.asarray(score, dtype=np.float32)
    out = np.zeros(score.shape, dtype=np.int32)
    out[score >= 0.4] = 1
    out[score >= 0.6] = 2
    out[score >= 0.75] = 3
    return out


def diagnose(
    cube: np.ndarray,
    hist_mean: Optional[np.ndarray] = None,
    hist_std: Optional[np.ndarray] = None,
    n_clusters: int = 3,
) -> Dict[str, Any]:
    """主流程：cube 波段顺序 [Red, RedEdge, NIR, LST]。

    返回 dict：ndvi/ndre/health/level/cluster/anomaly 等数组与统计。
    """
    cube = np.asarray(cube, dtype=np.float32)
    if cube.ndim != 3 or cube.shape[0] < 4:
        raise ValidationError(
            "input needs >=4 bands ordered [Red, RedEdge, NIR, LST]",
            bands=int(cube.shape[0]) if cube.ndim == 3 else int(cube.ndim),
        )
    red, rededge, nir, lst = cube[0], cube[1], cube[2], cube[3]
    ndvi = compute_ndvi(red, nir)
    ndre = compute_ndre(rededge, nir)
    health = health_score(ndvi, ndre, lst)
    level = classify_health(health)
    features = np.stack([ndvi, ndre, normalize01(lst, 293.0, 323.0)], axis=-1)
    cluster = spatial_cluster(features, n_clusters=n_clusters)

    if hist_mean is not None and hist_std is not None:
        anomaly = anomaly_zscore(ndvi, hist_mean, hist_std)
    else:
        # 无历史基线时用全局均值/标准差作退化基线
        mu = float(np.nanmean(ndvi))
        sd = float(np.nanstd(ndvi)) + 1e-3
        anomaly = anomaly_zscore(ndvi, np.full_like(ndvi, mu), np.full_like(ndvi, sd))

    return {
        "ndvi": ndvi,
        "ndre": ndre,
        "health": health,
        "level": level,
        "cluster": cluster,
        "anomaly": anomaly,
        "stats": {
            "mean_ndvi": float(np.nanmean(ndvi)),
            "mean_ndre": float(np.nanmean(ndre)),
            "mean_lst": float(np.nanmean(lst)),
            "mean_health": float(np.nanmean(health)),
            "mean_anomaly_z": float(np.nanmean(anomaly)),
            "n_clusters": int(cluster.max() + 1) if cluster.size else 0,
            "level_hist": {str(i): int(np.sum(level == i)) for i in range(4)},
        },
    }


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 [Red, RedEdge, NIR, LST] 4 波段立方体 + 历史 NDVI 基线。

    场景：左下健康农田（高 NIR / 低 LST），右上胁迫区（低 NIR / 高 LST）。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    xx /= max(width - 1, 1)
    yy /= max(height - 1, 1)

    healthy = ((xx + yy) < 1.0).astype(np.float32)  # 左下健康
    stressed = ((xx + yy) > 1.2).astype(np.float32)  # 右上胁迫
    mid = np.clip(1.0 - healthy - stressed, 0.0, 1.0)

    # 反射率（地表物理典型值）
    red = healthy * 0.04 + mid * 0.10 + stressed * 0.18
    rededge = healthy * 0.08 + mid * 0.15 + stressed * 0.22
    nir = healthy * 0.48 + mid * 0.32 + stressed * 0.18
    # 地表温度（K）：健康=低（蒸散发强），胁迫=高
    lst = healthy * 298.0 + mid * 308.0 + stressed * 318.0

    for arr in (red, rededge, nir):
        arr += rng.normal(0, 0.004, arr.shape).astype(np.float32)
    lst += rng.normal(0, 0.4, lst.shape).astype(np.float32)

    red = np.clip(red, 0.0, 1.0)
    rededge = np.clip(rededge, 0.0, 1.0)
    nir = np.clip(nir, 0.0, 1.0)

    cube = np.stack([red, rededge, nir, lst], axis=0).astype(np.float32)

    # 历史 NDVI 基线：整体略高于当前，制造部分负异常
    cur_ndvi = compute_ndvi(red, nir)
    hist_mean = np.clip(cur_ndvi + 0.05 + rng.normal(0, 0.02, cur_ndvi.shape), -1, 1)
    hist_std = np.full(cur_ndvi.shape, 0.06, dtype=np.float32)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "band_order": ["Red", "RedEdge", "NIR", "LST"],
        "healthy_fraction": float(healthy.mean()),
        "stressed_fraction": float(stressed.mean()),
    }
    aux = {"hist_mean": hist_mean.astype(np.float32), "hist_std": hist_std}
    return cube, {"info": info, "aux": aux}


# ---------------------------------------------------------------------------
# 输入校验：bbox（共用同 animated-map-series 模板）
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float]) -> None:
    """Validate a [W, S, E, N] bbox in WGS-84.

    Raises ValidationError (exit 6) for:
      - wrong length
      - non-finite values
      - longitude out of [-180, 180]
      - latitude  out of [-90, 90]
      - W >= E (would make a non-positive-width raster)
      - S >= N
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(
            f"bbox must have 4 floats [W S E N], got {bbox!r}",
        )
    w, s, e, n = bbox
    vals = [w, s, e, n]
    if not all(np.isfinite(vals)):
        raise ValidationError(f"bbox contains non-finite values: {vals}")
    if not (-180.0 <= w <= 180.0) or not (-180.0 <= e <= 180.0):
        raise ValidationError(
            f"longitude out of [-180, 180]: W={w}, E={e}",
        )
    if not (-90.0 <= s <= 90.0) or not (-90.0 <= n <= 90.0):
        raise ValidationError(
            f"latitude out of [-90, 90]: S={s}, N={n}",
        )
    if w >= e:
        raise ValidationError(
            f"bbox W must be < E (W={w}, E={e}); cross-180 not supported; "
            f"split into two bboxes at the dateline",
        )
    if s >= n:
        raise ValidationError(
            f"bbox S must be < N (S={s}, N={n})",
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox extent too small (W={w}, E={e}, S={s}, N={n})",
        )


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
    dtype = "int32" if np.issubdtype(cube.dtype, np.integer) else "float32"
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata if dtype == "float32" else None, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b], b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """Read a multiband GeoTIFF, returning (cube, bbox) with NoData→NaN."""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=True).astype(np.float32)
        cube = np.ma.filled(cube, np.nan)
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
        skill=SKILL_NAME,
        skill_version=VERSION,
        command=cmd,
        started_at=started_at,
        finished_at=_utc_now(),
        exit_code=exit_code,
        inputs={
            "input": getattr(args, "input", None),
            "method": getattr(args, "method", None),
            "n_clusters": getattr(args, "n_clusters", None),
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

    aux_arrays: Dict[str, np.ndarray] = {}
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, packed = generate_synthetic(bbox)
        aux_arrays = packed["aux"]
        synth_info = packed["info"]
        source_note = "synthetic"

    # 校验（先于 makedirs）
    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if bbox is not None:
        validate_bbox(bbox)
    if not np.any(np.isfinite(cube)):
        raise ValidationError(
            "input cube has no valid (finite) pixels across all bands (all NoData or NaN)",
        )

    # 现在 makedirs
    os.makedirs(output_dir, exist_ok=True)

    res = diagnose(
        cube,
        hist_mean=aux_arrays.get("hist_mean"),
        hist_std=aux_arrays.get("hist_std"),
        n_clusters=args.n_clusters,
    )

    health_tif = os.path.join(output_dir, "health_score.tif")
    write_geotiff(health_tif, res["health"], bbox)

    multi_tif = os.path.join(output_dir, "diagnosis_layers.tif")
    layers = np.stack([res["ndvi"], res["ndre"], res["anomaly"]], axis=0).astype(np.float32)
    write_geotiff(multi_tif, layers, bbox)

    level_tif = os.path.join(output_dir, "health_level.tif")
    write_geotiff(level_tif, res["level"].astype(np.float32), bbox)

    cluster_tif = os.path.join(output_dir, "health_cluster.tif")
    write_geotiff(cluster_tif, res["cluster"].astype(np.float32), bbox)

    qa = {
        "source": source_note,
        "method": args.method,
        "n_clusters": int(res["stats"]["n_clusters"]),
        "mean_health": res["stats"]["mean_health"],
        "mean_ndvi": res["stats"]["mean_ndvi"],
        "mean_anomaly_z": res["stats"]["mean_anomaly_z"],
        "level_hist": res["stats"]["level_hist"],
    }
    if synth_info is not None:
        qa["synthetic"] = synth_info

    outputs = [
        {"path": health_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": multi_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 3},
        {"path": level_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": cluster_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] mean health: {qa['mean_health']:.4f}  mean NDVI: {qa['mean_ndvi']:.4f}")
        print(f"[{SKILL_NAME}] clusters: {qa['n_clusters']}  levels: {qa['level_hist']}")
        print(f"[{SKILL_NAME}] output: {health_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Crop health diagnosis from NDVI/NDRE/LST with anomaly detection and clustering.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF with bands [Red, RedEdge, NIR, LST]")
    p.add_argument("--method", default="combined", choices=["combined", "ndvi-only", "anomaly"],
                   help="diagnosis emphasis (default: combined)")
    p.add_argument("--n-clusters", dest="n_clusters", type=int, default=3,
                   help="number of K-means management zones (default: 3)")
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
