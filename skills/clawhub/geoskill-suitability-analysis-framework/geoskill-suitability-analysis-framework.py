#!/usr/bin/env python3
"""suitability-analysis-framework — 适宜性分析框架

多准则适宜性分析的完整流水线：
1. 因子标准化（min-max 正向/负向，模糊隶属度）
2. 权重确定：AHP（判断矩阵特征向量法 + 一致性检验 CR）或熵权法（客观赋权）
3. 加权叠加（Weighted Linear Combination）
4. 适宜性分级（等间距 / 分位数）

数据源：本地多波段 GeoTIFF 因子栅格，或 --synthetic 生成模拟因子。

隐私声明 / Privacy：
- 默认离线运行，不发起任何网络请求。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python suitability-analysis-framework.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "suitability-analysis-framework"

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


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# Saaty 随机一致性指标 RI（n=1..10）
_SAATY_RI = {1: 0.0, 2: 0.0, 3: 0.58, 4: 0.90, 5: 1.12,
             6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}


# ---------------------------------------------------------------------------
# 核心算法 1：因子标准化
# ---------------------------------------------------------------------------
def normalize_minmax(raster: np.ndarray, positive: bool = True) -> np.ndarray:
    """min-max 标准化到 [0,1]。positive=True 值越大越适宜；False 反向。"""
    r = np.asarray(raster, dtype=np.float64)
    rmin, rmax = float(np.nanmin(r)), float(np.nanmax(r))
    if rmax - rmin < 1e-12:
        return np.full(r.shape, 0.5)
    norm = (r - rmin) / (rmax - rmin)
    return norm if positive else 1.0 - norm


def fuzzy_membership(raster: np.ndarray, lo: float, hi: float,
                     increasing: bool = True) -> np.ndarray:
    """线性模糊隶属度：[lo, hi] 线性过渡到 [0,1]，两侧截断。"""
    r = np.asarray(raster, dtype=np.float64)
    if hi <= lo:
        raise ValidationError("fuzzy hi must be > lo")
    mu = (r - lo) / (hi - lo)
    mu = np.clip(mu, 0.0, 1.0)
    return mu if increasing else 1.0 - mu


# ---------------------------------------------------------------------------
# 核心算法 2：权重
# ---------------------------------------------------------------------------
def ahp_weights(matrix: np.ndarray) -> Dict[str, Any]:
    """AHP 特征向量法求权重 + 一致性检验。

    Parameters
    ----------
    matrix : (n, n) 正互反判断矩阵

    Returns dict: weights, lambda_max, CI, CR, consistent。
    """
    A = np.asarray(matrix, dtype=np.float64)
    n = A.shape[0]
    if A.shape != (n, n):
        raise ValidationError("AHP matrix must be square")
    if np.any(A <= 0):
        raise ValidationError("AHP matrix must be positive")
    if not np.allclose(A, 1.0 / A.T, rtol=1e-6):
        raise ValidationError("AHP matrix must be reciprocal (a_ij = 1/a_ji)")

    # 特征向量法：取最大特征值对应特征向量
    eigvals, eigvecs = np.linalg.eig(A)
    idx = int(np.argmax(eigvals.real))
    lambda_max = float(eigvals[idx].real)
    w = eigvecs[:, idx].real
    w = np.abs(w)
    weights = w / w.sum()

    CI = (lambda_max - n) / (n - 1) if n > 1 else 0.0
    RI = _SAATY_RI.get(n, 1.49)
    CR = CI / RI if RI > 0 else 0.0
    return {"weights": weights, "lambda_max": lambda_max, "CI": CI, "CR": CR,
            "consistent": bool(CR < 0.1)}


def entropy_weights(factors_norm: np.ndarray) -> Dict[str, Any]:
    """熵权法客观赋权。

    Parameters
    ----------
    factors_norm : (n_factors, H, W) 已标准化到 (0,1] 的因子

    Returns dict: weights, entropy, divergence。
    """
    X = np.asarray(factors_norm, dtype=np.float64)
    if X.ndim != 3:
        raise ValidationError("entropy_weights expects (n_factors, H, W)")
    m = X.shape[0]
    # 平移避免 log(0)
    Xp = np.clip(X, 1e-9, None)
    flat = Xp.reshape(m, -1)
    col_sum = flat.sum(axis=1, keepdims=True)
    col_sum = np.where(col_sum < 1e-12, 1e-12, col_sum)
    P = flat / col_sum  # 比重
    k = 1.0 / np.log(flat.shape[1]) if flat.shape[1] > 1 else 1.0
    with np.errstate(divide="ignore", invalid="ignore"):
        lnP = np.where(P > 0, np.log(P), 0.0)
    entropy = -k * (P * lnP).sum(axis=1)  # (m,)
    divergence = 1.0 - entropy
    total = divergence.sum()
    if total < 1e-12:
        weights = np.full(m, 1.0 / m)
    else:
        weights = divergence / total
    return {"weights": weights, "entropy": entropy, "divergence": divergence}


# ---------------------------------------------------------------------------
# 核心算法 3：加权叠加 + 分级
# ---------------------------------------------------------------------------
def weighted_overlay(factors_norm: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """加权线性叠加。weights 自动归一化。"""
    X = np.asarray(factors_norm, dtype=np.float64)
    w = np.asarray(weights, dtype=np.float64)
    if X.shape[0] != w.shape[0]:
        raise ValidationError("factor count != weight count")
    if np.any(w < 0):
        raise ValidationError("weights must be non-negative")
    wsum = w.sum()
    if wsum <= 0:
        raise ValidationError("weights sum to zero")
    w = w / wsum
    return np.tensordot(w, X, axes=(0, 0))


def classify_suitability(score: np.ndarray, n_classes: int = 5,
                         method: str = "equal_interval") -> Tuple[np.ndarray, List[float]]:
    """适宜性分级。返回 (类别栅格 1..n_classes, 断点列表)。"""
    if n_classes < 2:
        raise ValidationError("n_classes must be >= 2")
    s = np.asarray(score, dtype=np.float64)
    if method == "equal_interval":
        edges = np.linspace(s.min(), s.max(), n_classes + 1)
    elif method == "quantile":
        qs = np.linspace(0, 100, n_classes + 1)
        edges = np.percentile(s, qs)
        edges = np.unique(edges)
        if len(edges) < 2:
            edges = np.array([s.min(), s.max()])
    else:
        raise ValidationError(f"unknown method '{method}'")
    classes = np.digitize(s, edges[1:-1], right=False) + 1
    classes = np.clip(classes, 1, len(edges) - 1)
    return classes.astype(np.int32), edges.tolist()


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], grid_size: int = 48, n_factors: int = 4,
                       seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (n_factors, H, W) 模拟因子栅格：坡度/距道路/距水源/土地利用。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:grid_size, 0:grid_size]
    yyf = yy / grid_size
    xxf = xx / grid_size
    factors = []
    # 坡度（负向因子）
    factors.append(5.0 + 25.0 * np.exp(-((xxf - 0.5) ** 2 + (yyf - 0.5) ** 2) / 0.08)
                   + rng.normal(0, 1, (grid_size, grid_size)))
    # 距道路距离（负向）
    factors.append(np.abs(xxf - 0.5) * 100 + rng.normal(0, 2, (grid_size, grid_size)))
    # 距水源距离（负向）
    factors.append(np.sqrt((xxf - 0.2) ** 2 + (yyf - 0.8) ** 2) * 100
                   + rng.normal(0, 2, (grid_size, grid_size)))
    # 土壤质量（正向）
    factors.append(50.0 + 30.0 * np.sin(xxf * 4) * np.cos(yyf * 3)
                   + rng.normal(0, 2, (grid_size, grid_size)))
    factors = factors[:n_factors]
    cube = np.stack(factors, axis=0).astype(np.float32)
    info = {"n_factors": n_factors, "grid_size": grid_size}
    return cube, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O / Manifest
# ---------------------------------------------------------------------------
def write_geotiff(path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if array.ndim == 2:
        array = array[np.newaxis, ...]
    if array.ndim != 3:
        raise ValidationError("write_geotiff expects a 2D or 3D array")
    nb, hh, ww = array.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], ww, hh)
    profile = {
        "driver": "GTiff", "height": hh, "width": ww, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(array[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        data = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return data, bbox


def read_geotiff_full(path: str) -> Tuple[np.ndarray, List[float], int, Optional[float]]:
    """Read GeoTIFF + replace NoData sentinel with NaN; return (cube, bbox, n_valid, input_nodata).

    If *all* pixels are NoData in every band, raises ``ValidationError`` (rc=6).
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=False).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        input_nodata = src.nodata
    if input_nodata is not None:
        cube = np.where(cube == float(input_nodata), np.nan, cube).astype(np.float32)
    valid_mask = np.isfinite(cube)
    n_valid = int(valid_mask.sum())
    if n_valid == 0:
        nodata_str = f"={input_nodata}" if input_nodata is not None else "(none)"
        raise ValidationError(
            f"input raster has no valid pixels (all are NoData{nodata_str})",
            path=path, input_nodata=input_nodata,
        )
    return cube, bbox, n_valid, input_nodata


def validate_bbox(bbox):
    """Validate EPSG:4326 bbox: W<E, S<N, lon/lat ranges, no crossing antimeridian,
    span > 1e-4°. Raises ``ValidationError`` (rc=6)."""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be [W, S, E, N] with 4 floats")
    W, S, E, N = [float(v) for v in bbox]
    if W < -180.0 or E > 180.0 or S < -90.0 or N > 90.0:
        raise ValidationError(
            f"bbox out of WGS-84 range: W={W} S={S} E={E} N={N} "
            "(must satisfy -180<=lon<=180, -90<=lat<=90)",
            bbox=bbox,
        )
    if W >= E:
        if W > 0 and E < 0 and (W - E) < 360.0:
            raise ValidationError(
                f"bbox crosses 180° antimeridian (W={W}, E={E}); "
                "split into two non-antipodal sub-bboxes",
                bbox=bbox,
            )
        raise ValidationError(
            f"bbox has W>=E (W={W}, E={E}); expected W<E in WGS-84 order",
            bbox=bbox,
        )
    if S >= N:
        raise ValidationError(
            f"bbox has S>=N (S={S}, N={N}); expected S<N in WGS-84 order",
            bbox=bbox,
        )
    if (E - W) < 1e-4 or (N - S) < 1e-4:
        raise ValidationError(
            f"bbox is too small (lon-span={E - W:.6f}, lat-span={N - S:.6f}); "
            "need at least 1e-4° on each axis",
            bbox=bbox,
        )
    return [W, S, E, N]


def write_manifest(
    output_dir: str, args: argparse.Namespace, outputs: List[Dict[str, Any]],
    qa: Dict[str, Any], started_at: str, exit_code: int, bbox: List[float],
) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs={"input": getattr(args, "input", None), "synthetic": bool(getattr(args, "synthetic", False))},
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

    # 1) bbox validation FIRST (before makedirs)
    if args.input and not args.synthetic:
        if bbox is not None:
            bbox = validate_bbox(bbox)
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)

    n_valid_pixels = None
    input_nodata = None
    if args.input and not args.synthetic:
        cube, file_bbox, n_valid_pixels, input_nodata = read_geotiff_full(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            bbox = validate_bbox(bbox)
        source_note = args.input
    else:
        cube, _ = generate_synthetic(bbox, grid_size=args.grid_size, n_factors=args.n_factors)
        source_note = "synthetic"

    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    m = cube.shape[0]
    if m < 2:
        raise ValidationError("need at least 2 factors")

    # 因子方向：前 n_factors-1 个负向（距离/坡度类），最后一个正向
    positives = [False] * (m - 1) + [True]
    normed = np.stack([normalize_minmax(cube[i], positive=positives[i]) for i in range(m)])

    # 权重
    if args.weighting == "ahp":
        A = _build_ahp_matrix(m, args.ahp_dominance)
        res_w = ahp_weights(A)
        weights = res_w["weights"]
        weight_info = {"method": "ahp", "weights": weights.tolist(),
                       "CR": res_w["CR"], "consistent": res_w["consistent"]}
    else:
        res_w = entropy_weights(normed)
        weights = res_w["weights"]
        weight_info = {"method": "entropy", "weights": weights.tolist(),
                       "entropy": res_w["entropy"].tolist()}

    score = weighted_overlay(normed, weights)
    classes, edges = classify_suitability(score, args.n_classes, args.classify_method)

    # 2) ALL checks passed → safe to makedirs
    os.makedirs(output_dir, exist_ok=True)

    out_score = os.path.join(output_dir, "suitability_score.tif")
    write_geotiff(out_score, score.astype(np.float32), bbox)
    out_class = os.path.join(output_dir, "suitability_class.tif")
    write_geotiff(out_class, classes.astype(np.float32), bbox)
    stats_path = os.path.join(output_dir, "suitability_stats.json")
    uniq, counts = np.unique(classes, return_counts=True)
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump({"weighting": weight_info, "class_edges": edges,
                   "class_counts": {int(u): int(c) for u, c in zip(uniq, counts)},
                   "score_min": float(score.min()), "score_max": float(score.max())},
                  f, ensure_ascii=False, indent=2)

    qa = {"source": source_note, "n_factors": int(m),
          "weighting_method": args.weighting,
          "weights": weights.tolist(),
          "score_mean": float(score.mean()),
          "high_suitability_pct": float((classes >= args.n_classes - 1).mean() * 100),
          "n_valid_pixels": n_valid_pixels,
          "input_nodata": input_nodata}
    outputs = [
        {"path": out_score, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_class, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  factors: {m}")
        print(f"[{SKILL_NAME}] weighting: {args.weighting}")
        print(f"[{SKILL_NAME}] weights: {np.round(weights, 3).tolist()}")
        print(f"[{SKILL_NAME}] score range: [{score.min():.3f}, {score.max():.3f}]")
        print(f"[{SKILL_NAME}] high suitability: {qa['high_suitability_pct']:.1f}%")
        print(f"[{SKILL_NAME}] output: {out_score}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def _build_ahp_matrix(n: int, dominance: float) -> np.ndarray:
    """构造一致的 AHP 判断矩阵：因子 i 相对 j 的重要性按线性梯度。"""
    if dominance < 1:
        dominance = 1.0
    base = np.linspace(dominance, 1.0, n)  # 第一个因子最重要
    A = np.outer(base, 1.0 / base)
    return A


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Suitability analysis: factor normalization, AHP/entropy weighting, weighted overlay, classification.",
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multi-band factor GeoTIFF")
    p.add_argument("--grid-size", type=int, default=48, help="synthetic grid size (default: 48)")
    p.add_argument("--n-factors", type=int, default=4, help="synthetic factor count (default: 4)")
    p.add_argument("--weighting", default="ahp", choices=["ahp", "entropy"],
                   help="weighting method (default: ahp)")
    p.add_argument("--ahp-dominance", type=float, default=3.0,
                   help="AHP dominance ratio of most important factor (default: 3)")
    p.add_argument("--n-classes", type=int, default=5, help="suitability classes (default: 5)")
    p.add_argument("--classify-method", default="equal_interval",
                   choices=["equal_interval", "quantile"], help="classification method")
    p.add_argument("--synthetic", action="store_true", help="use synthetic data")
    p.add_argument("--output-dir", default="./output", help="output directory")
    p.add_argument("--quiet", action="store_true", help="suppress output")
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
