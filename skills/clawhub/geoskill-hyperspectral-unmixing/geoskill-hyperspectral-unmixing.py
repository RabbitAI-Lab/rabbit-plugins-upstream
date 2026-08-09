#!/usr/bin/env python3
"""hyperspectral-unmixing — 高光谱端元提取与光谱解混

对高光谱立方体 (bands, H, W) 执行端元提取 + 全约束线性光谱解混（FCLSU）：

- **端元提取**：VCA（顶点成分分析，Nascimento & Dias 2005，迭代投影找
  数据单纯形顶点）或简化 N-FINDR（Winter 1999，贪心搜索使单纯形体积
  最大的像元集合）。
- **线性解混**：对每个像元用 scipy.optimize.nnls 求非负最小二乘丰度
  （ANC），再归一化满足和为 1 约束（ASC）。输出逐端元丰度图与残差图。

数据源：本地高光谱 GeoTIFF，或 ``--synthetic`` 用 Dirichlet 随机丰度
线性混合若干端元光谱生成模拟立方体（离线）。

隐私声明 / Privacy：
- 完全离线运行，不访问任何网络服务。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python hyperspectral-unmixing.py --input hyper.tif --n-endmembers 3 --method vca
    python hyperspectral-unmixing.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "hyperspectral-unmixing"

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
# 核心算法：端元提取
# ---------------------------------------------------------------------------
def vca(data: np.ndarray, p: int, seed: int = 42) -> Tuple[np.ndarray, List[int]]:
    """顶点成分分析（VCA）。data: (L, N)，p: 端元数。

    先 PCA 投影到 p 维并加一行齐次坐标 1，然后迭代：取一个与已选端元
    子空间正交的随机方向，把所有像元投影上去，极值像元即新端元。
    返回 (endmembers (L, p), pixel_indices)。
    """
    L, N = data.shape
    if p < 1 or p > min(L, N):
        raise UsageError(f"invalid endmember count p={p} for data shape {data.shape}", p=int(p))
    rng = np.random.default_rng(seed)
    # Drop NaN pixels for endmember extraction
    finite_cols = np.all(np.isfinite(data), axis=0)
    data_clean = data[:, finite_cols]
    if data_clean.shape[1] < p:
        raise ValidationError(
            f"too few finite pixels for VCA: {int(data_clean.shape[1])} vs p={p}"
        )
    mean = data_clean.mean(axis=1, keepdims=True)
    Xc = data_clean - mean
    U, _s, _Vt = np.linalg.svd(Xc, full_matrices=False)
    Up = U[:, :p]                       # (L, p) 主成分子空间
    Y = Up.T @ Xc                       # (p, N) 得分
    Yp = np.vstack([Y, np.ones((1, data_clean.shape[1]))])  # (p+1, N)

    A = np.zeros((p + 1, p))
    end_idx: List[int] = []
    for i in range(p):
        w = rng.standard_normal(p + 1)
        if i > 0:
            Q = A[:, :i]
            coef, *_ = np.linalg.lstsq(Q, w, rcond=None)
            w = w - Q @ coef            # 正交化：去掉已选端元方向分量
        w = w / (np.linalg.norm(w) + 1e-12)
        proj = w @ Yp
        idx = int(np.argmax(np.abs(proj)))
        end_idx.append(idx)
        A[:, i] = Yp[:, idx]
    endmembers = data_clean[:, end_idx]
    return endmembers, end_idx


def _simplex_volume(scores: np.ndarray, idx: List[int]) -> float:
    """齐次坐标单纯形体积：scores (p-1, N)，idx 为 p 个像元下标。"""
    pts = scores[:, idx]                    # (p-1, p)
    M = np.vstack([np.ones((1, len(idx))), pts])
    return float(abs(np.linalg.det(M)))


def nfindr(data: np.ndarray, p: int, iters: int = 25, candidates: int = 60,
           seed: int = 42) -> Tuple[np.ndarray, List[int]]:
    """简化 N-FINDR：PCA 降维后贪心迭代替换端元使单纯形体积最大。

    返回 (endmembers (L, p), pixel_indices)。
    """
    L, N = data.shape
    if p < 1 or p > min(L, N):
        raise UsageError(f"invalid endmember count p={p} for data shape {data.shape}", p=int(p))
    # Drop NaN pixels
    finite_cols = np.all(np.isfinite(data), axis=0)
    data_clean = data[:, finite_cols]
    if data_clean.shape[1] < p:
        raise ValidationError(
            f"too few finite pixels for N-FINDR: {int(data_clean.shape[1])} vs p={p}"
        )
    if p == 1:
        j = int(np.argmax(np.linalg.norm(data_clean, axis=0)))
        return data_clean[:, [j]], [j]
    rng = np.random.default_rng(seed)
    mean = data_clean.mean(axis=1, keepdims=True)
    Xc = data_clean - mean
    U, _s, _Vt = np.linalg.svd(Xc, full_matrices=False)
    scores = U[:, : p - 1].T @ Xc           # (p-1, N)

    idx = rng.choice(data_clean.shape[1], size=p, replace=False).tolist()
    best = _simplex_volume(scores, idx)
    for _ in range(iters):
        improved = False
        for slot in range(p):
            cands = rng.choice(data_clean.shape[1], size=min(candidates, data_clean.shape[1]), replace=False)
            for c in cands:
                trial = idx.copy()
                trial[slot] = int(c)
                v = _simplex_volume(scores, trial)
                if v > best:
                    best, idx = v, trial
                    improved = True
        if not improved:
            break
    return data_clean[:, idx], idx


def extract_endmembers(data: np.ndarray, p: int, method: str = "vca",
                       seed: int = 42) -> Tuple[np.ndarray, List[int]]:
    """端元提取分派。data (L, N)，返回 (endmembers (L, p), indices)。"""
    if method == "vca":
        return vca(data, p, seed=seed)
    if method == "nfindr":
        return nfindr(data, p, seed=seed)
    raise UsageError(f"unknown method '{method}'. Choose from: vca, nfindr", method=method)


# ---------------------------------------------------------------------------
# 核心算法：全约束线性解混（FCLSU）
# ---------------------------------------------------------------------------
def fclsu_unmix(data: np.ndarray, endmembers: np.ndarray
                ) -> Tuple[np.ndarray, np.ndarray]:
    """逐像元非负最小二乘解混 + 和归一化。

    data (L, N)，endmembers (L, p)。返回 (abundances (p, N), rmse (N,))。

    NaN 像元 (光谱含 NaN) 丰度为 0、rmse 为 NaN，由调用方决定如何处理。
    """
    from scipy.optimize import nnls
    L, N = data.shape
    p = endmembers.shape[1]
    ab = np.zeros((p, N), dtype=np.float64)
    rmse = np.full(N, np.nan, dtype=np.float64)
    for i in range(N):
        col = data[:, i]
        if not np.all(np.isfinite(col)):
            continue
        a, _ = nnls(endmembers, col)
        s = a.sum()
        if s > 1e-12:
            a = a / s                   # 和为 1 约束（ASC）
        ab[:, i] = a
        recon = endmembers @ a
        rmse[i] = float(np.sqrt(np.mean((col - recon) ** 2)))
    return ab, rmse


def match_abundances(ab_est: np.ndarray, ab_true: np.ndarray
                     ) -> Tuple[List[int], float]:
    """用匈牙利算法把估计端元与真值端元配对，返回 (perm, mean_mae)。

    ab_est / ab_true: (p, ...)。perm[i] 为估计端元 i 对应的真值端元下标。
    """
    from scipy.optimize import linear_sum_assignment
    p = ab_est.shape[0]
    flat_est = ab_est.reshape(p, -1)
    flat_true = ab_true.reshape(ab_true.shape[0], -1)
    cost = np.zeros((p, flat_true.shape[0]))
    for i in range(p):
        for j in range(flat_true.shape[0]):
            cost[i, j] = np.mean(np.abs(flat_est[i] - flat_true[j]))
    row, col = linear_sum_assignment(cost)
    perm = [int(col[i]) for i in range(p)]
    return perm, float(cost[row, col].mean())


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def endmember_spectra(n: int, n_bands: int, seed: int = 1) -> np.ndarray:
    """生成 n 条峰值位置互异、线性无关的端元光谱 (n, n_bands)。"""
    if n < 1:
        raise UsageError("n_endmembers must be >= 1", n=n)
    if n_bands < 2:
        raise UsageError("n_bands must be >= 2", n_bands=n_bands)
    rng = np.random.default_rng(seed)
    x = np.linspace(0.0, 1.0, n_bands)
    E = np.zeros((n, n_bands), dtype=np.float64)
    for i in range(n):
        peak = (i + 0.5) / n
        E[i] = 0.10 + 0.80 * np.exp(-((x - peak) ** 2) / (2.0 * 0.08 ** 2))
        E[i] += 0.02 * rng.standard_normal(n_bands)
    return np.clip(E, 0.01, 1.0)


def generate_synthetic(bbox: List[float], n_endmembers: int = 3, n_bands: int = 20,
                       width: int = 64, height: int = 64, seed: int = 42,
                       noise: float = 0.005
                       ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """Dirichlet 随机丰度线性混合端元光谱，生成 (bands, H, W) 立方体。

    返回 (cube, truth_abundances (p, H, W), endmembers (p, bands), info)。
    """
    rng = np.random.default_rng(seed)
    E = endmember_spectra(n_endmembers, n_bands, seed=seed + 1)  # (p, L)
    N = width * height
    A = rng.dirichlet(np.ones(n_endmembers) * 0.8, size=N).T     # (p, N)
    data = E.T @ A                                               # (L, N)
    data = data + rng.normal(0.0, noise, data.shape)
    data = np.clip(data, 0.0, 1.0)
    cube = data.reshape(n_bands, height, width).astype(np.float32)
    truth_ab = A.reshape(n_endmembers, height, width)
    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "n_bands": n_bands,
        "n_endmembers": n_endmembers,
        "noise": noise,
    }
    return cube, truth_ab, E, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
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
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_with_nodata(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """Read multi-band cube and replace NoData pixels with NaN.

    A pixel is NoData if ANY band equals the nodata sentinel. Returns
    (cube (bands, H, W), bbox, nodata_value_or_None).
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
        bad_mask = np.any(cube == nodata, axis=0)
        cube[:, bad_mask] = np.nan
    return cube, bbox, nodata


def validate_bbox(bbox: Optional[List[float]], allow_none: bool = False) -> List[float]:
    """Validate a W,S,E,N bbox. Cross-180 / out-of-range / W>=E / S>=N -> ValidationError."""
    if bbox is None:
        if allow_none:
            return None  # type: ignore[return-value]
        raise ValidationError("bbox is required")
    if len(bbox) != 4:
        raise ValidationError(f"bbox must have 4 floats, got {len(bbox)}")
    w, s, e, n = bbox
    for v, name in zip([w, s, e, n], ["W", "S", "E", "N"]):
        if not isinstance(v, (int, float)) or not (-1e9 < v < 1e9):
            raise ValidationError(f"bbox {name}={v!r} not a finite number")
    if w == e or s == n:
        raise ValidationError(f"bbox has zero area: W={w} E={e} S={s} N={n}")
    if not (-180.0 <= w <= 180.0) or not (-180.0 <= e <= 180.0):
        raise ValidationError(f"bbox lon out of [-180,180]: W={w} E={e}")
    if not (-90.0 <= s <= 90.0) or not (-90.0 <= n <= 90.0):
        raise ValidationError(f"bbox lat out of [-90,90]: S={s} N={n}")
    if w > e:
        if not (w > 170.0 and e < -170.0):
            raise ValidationError(
                f"bbox has W>E (minLon > maxLon): W={w} E={e} — "
                f"if crossing the dateline, split into two bboxes (e.g. "
                f"[{w}, {s}, 180, {n}] and [-180, {s}, {e}, {n}])"
            )
        raise ValidationError(
            f"bbox crosses the 180° dateline (W={w} E={e}); "
            f"split into two non-wrapping bboxes ([{w}, {s}, 180, {n}] and "
            f"[-180, {s}, {e}, {n}]) and run separately"
        )
    if s > n:
        raise ValidationError(f"bbox has S>N (minLat > maxLat): S={s} N={n}")
    return [float(w), float(s), float(e), float(n)]


def validate_synthetic_params(n_bands: int, n_endmembers: int) -> Tuple[int, int]:
    """Validate synthetic-cube parameters. Returns (n_bands, n_endmembers)."""
    if n_bands is None or n_bands < 2:
        raise ValidationError(f"--n-bands must be >= 2, got {n_bands}")
    if n_endmembers is None or n_endmembers < 1:
        raise ValidationError(f"--n-endmembers must be >= 1, got {n_endmembers}")
    return int(n_bands), int(n_endmembers)


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
def write_manifest(output_dir: str, args: argparse.Namespace,
                   outputs: List[Dict[str, Any]], qa: Dict[str, Any],
                   started_at: str, exit_code: int, bbox: List[float]) -> Optional[str]:
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
            "n_endmembers": getattr(args, "n_endmembers", None),
            "n_bands": getattr(args, "n_bands", None),
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

    # ---- 1. 参数验证 (前置：失败不创建 output_dir) ----
    bbox = list(args.bbox) if args.bbox else None
    if bbox is not None:
        bbox = validate_bbox(bbox)
    n_bands, n_endmembers = validate_synthetic_params(args.n_bands, args.n_endmembers)

    # ---- 2. 数据获取 ----
    truth_ab: Optional[np.ndarray] = None
    input_nodata: Optional[float] = None
    valid_mask: Optional[np.ndarray] = None
    n_valid_input: int = 0
    n_total_input: int = 0
    if args.input and not args.synthetic:
        cube, file_bbox, input_nodata = read_geotiff_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        bbox = validate_bbox(bbox)
        valid_mask = np.all(np.isfinite(cube), axis=0)
        n_valid_input = int(valid_mask.sum())
        n_total_input = int(cube.shape[1] * cube.shape[2])
        if n_valid_input == 0:
            raise ValidationError(
                f"input cube has no valid (non-NoData) pixels "
                f"(nodata={input_nodata}, total={n_total_input})"
            )
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        cube, truth_ab, _true_E, _info = generate_synthetic(
            bbox, n_endmembers=n_endmembers, n_bands=n_bands,
        )
        source_note = "synthetic"
        n_valid_input = int(cube.size)
        n_total_input = int(cube.shape[1] * cube.shape[2])

    # ---- 3. 校验通过后创建 output_dir ----
    os.makedirs(output_dir, exist_ok=True)

    if cube.size == 0:
        raise ValidationError("input raster is empty")
    if cube.ndim != 3 or cube.shape[0] < 2:
        raise ValidationError("input must be a multi-band cube (bands, H, W)",
                              shape=list(cube.shape))

    nb, h, w = cube.shape
    p = n_endmembers
    if p > nb:
        raise ValidationError(f"n_endmembers ({p}) exceeds band count ({nb})",
                              n_endmembers=int(p), n_bands=int(nb))

    data = cube.reshape(nb, -1).astype(np.float64)

    # 端元提取 + 解混
    endmembers, em_idx = extract_endmembers(data, p, method=args.method)
    abundances, rmse = fclsu_unmix(data, endmembers)

    ab_map = abundances.reshape(p, h, w).astype(np.float32)
    resid_map = rmse.reshape(h, w).astype(np.float32)

    # NoData 区域显式置 NaN（输出 -1 哨兵）
    if valid_mask is not None:
        for k in range(p):
            ab_map[k] = np.where(valid_mask, ab_map[k], np.nan).astype(np.float32)
        resid_map = np.where(valid_mask, resid_map, np.nan).astype(np.float32)

    # 精度（合成模式有真值丰度；仅 valid 像元）
    finite_rmse = rmse[np.isfinite(rmse)]
    mean_rmse_val = float(np.mean(finite_rmse)) if finite_rmse.size else float("nan")
    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "n_endmembers": int(p),
        "n_bands": int(nb),
        "mean_rmse": mean_rmse_val,
        "n_valid_pixels": int(n_valid_input),
        "n_total_pixels": int(n_total_input),
        "input_nodata": input_nodata,
    }
    if truth_ab is not None:
        perm, mean_mae = match_abundances(ab_map, truth_ab)
        qa["endmember_match_permutation"] = perm
        qa["mean_abundance_mae"] = mean_mae

    # 写出产物（abundance 和 residual NoData=-1.0 / NaN -> -9999.0）
    ab_tif = os.path.join(output_dir, "abundances.tif")
    write_geotiff(ab_tif, np.nan_to_num(ab_map, nan=-1.0), bbox, nodata=-1.0)

    resid_tif = os.path.join(output_dir, "residual.tif")
    write_geotiff(resid_tif, np.nan_to_num(resid_map, nan=-9999.0), bbox, nodata=-9999.0)

    em_path = os.path.join(output_dir, "endmembers.json")
    em_doc = {
        "method": args.method,
        "n_endmembers": int(p),
        "n_bands": int(nb),
        "pixel_indices": [int(i) for i in em_idx],
        "spectra": endmembers.tolist(),
    }
    with open(em_path, "w", encoding="utf-8") as f:
        json.dump(em_doc, f, ensure_ascii=False, indent=2)

    outputs = [
        {"path": ab_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(p), "nodata": -1.0},
        {"path": resid_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1, "nodata": -9999.0},
        {"path": em_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  endmembers: {p}  bands: {nb}  shape: {(h, w)}")
        print(f"[{SKILL_NAME}] mean RMSE: {qa['mean_rmse']:.5f}")
        if "mean_abundance_mae" in qa:
            print(f"[{SKILL_NAME}] abundance MAE vs truth: {qa['mean_abundance_mae']:.5f}")
        print(f"[{SKILL_NAME}] output: {ab_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Hyperspectral endmember extraction (VCA / N-FINDR) and FCLSU unmixing.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input hyperspectral GeoTIFF (bands, H, W)")
    p.add_argument("--method", default="vca", choices=["vca", "nfindr"],
                   help="endmember extraction method (default: vca)")
    p.add_argument("--n-endmembers", type=int, default=3,
                   help="number of endmembers (default: 3)")
    p.add_argument("--n-bands", type=int, default=20,
                   help="synthetic cube band count (default: 20)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic mixed scene (offline)")
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
