#!/usr/bin/env python3
"""spatial-autocorrelation — 空间自相关分析

计算 Global Moran's I、Local Moran's I (LISA) 与 Getis-Ord Gi*，
并用蒙特卡洛随机置换检验评估显著性。用于识别空间聚集/离散模式。

数据源：本地 GeoTIFF 栅格，或 --synthetic 生成模拟场。

隐私声明 / Privacy：
- 默认离线运行，不发起任何网络请求。
- 所有处理在本地完成，不上传用户数据。

Usage:
    python spatial-autocorrelation.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "spatial-autocorrelation"

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


def validate_bbox(bbox: List[float]) -> None:
    """校验 bbox：W<E、S<N、经纬度在合法范围、非零面积；跨 180° 明确提示。"""
    if bbox is None:
        raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
    if len(bbox) != 4:
        raise ValidationError(f"bbox must have exactly 4 numbers, got {len(bbox)}")
    w, s, e, n = [float(x) for x in bbox]
    if w > e:
        raise ValidationError(
            f"bbox minLon ({w}) > maxLon ({e}): crossing the 180° antimeridian is not "
            "supported, please split the region into two bboxes")
    if s > n:
        raise ValidationError(f"bbox minLat ({s}) > maxLat ({n}): S must be <= N")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"bbox longitudes out of range [-180, 180]: {w}, {e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"bbox latitudes out of range [-90, 90]: {s}, {n}")
    if w == e or s == n:
        raise ValidationError("bbox has zero area")


def validate_params(grid_size: int, permutations: int) -> None:
    if grid_size < 4:
        raise ValidationError(f"--grid-size must be >= 4, got {grid_size}")
    if permutations < 1:
        raise ValidationError(f"--permutations must be >= 1, got {permutations}")


# ---------------------------------------------------------------------------
# 空间权重矩阵
# ---------------------------------------------------------------------------
def rook_weights(shape: Tuple[int, int]) -> np.ndarray:
    """构建栅格的 rook 邻接行标准化权重矩阵 W (n x n)。"""
    h, w = shape
    n = h * w
    W = np.zeros((n, n), dtype=np.float64)
    for r in range(h):
        for c in range(w):
            i = r * w + c
            neigh = []
            if r > 0:
                neigh.append((r - 1) * w + c)
            if r < h - 1:
                neigh.append((r + 1) * w + c)
            if c > 0:
                neigh.append(r * w + c - 1)
            if c < w - 1:
                neigh.append(r * w + c + 1)
            if neigh:
                for j in neigh:
                    W[i, j] = 1.0 / len(neigh)
    return W


def knn_weights(coords: np.ndarray, k: int = 8) -> np.ndarray:
    """基于 k 最近邻的行标准化权重矩阵。"""
    from scipy.spatial import cKDTree
    n = coords.shape[0]
    tree = cKDTree(coords)
    _, idx = tree.query(coords, k=min(k + 1, n))
    W = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        neigh = idx[i][1:]  # 排除自身
        if neigh.size:
            W[i, neigh] = 1.0 / neigh.size
    return W


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def global_morans_i(x: np.ndarray, W: np.ndarray) -> Dict[str, float]:
    """Global Moran's I。

    I = (n / S0) * (sum_i sum_j w_ij (x_i - xbar)(x_j - xbar)) / (sum_i (x_i - xbar)^2)
    返回 I、期望值 E[I]、方差 Var[I]（正态近似）、z 值、p 值。
    """
    x = np.asarray(x, dtype=np.float64).ravel()
    n = x.shape[0]
    if W.shape != (n, n):
        raise ValidationError("W shape mismatch with x length")
    z = x - x.mean()
    S0 = W.sum()
    if S0 == 0:
        raise ValidationError("weight matrix sums to zero")
    num = z @ W @ z
    den = (z ** 2).sum()
    I = (n / S0) * (num / den)
    EI = -1.0 / (n - 1)
    # 方差（随机化假设下的近似）
    S1 = 0.5 * ((W + W.T) ** 2).sum()
    S2 = ((W.sum(1) + W.sum(0)) ** 2).sum()
    b2 = n * (z ** 4).sum() / (den ** 2)  # kurtosis
    var_num = (n * ((n ** 2 - 3 * n + 3) * S1 - n * S2 + 3 * S0 ** 2)
               - b2 * ((n ** 2 - n) * S1 - 2 * n * S2 + 6 * S0 ** 2))
    var_den = (n - 1) * (n - 2) * (n - 3) * S0 ** 2
    VarI = var_num / var_den - EI ** 2
    VarI = max(VarI, 1e-12)
    zscore = (I - EI) / np.sqrt(VarI)
    from scipy.stats import norm
    p = 2.0 * (1.0 - norm.cdf(abs(zscore)))
    return {"I": float(I), "expected": float(EI), "variance": float(VarI),
            "z_score": float(zscore), "p_value": float(p)}


def local_morans_i(x: np.ndarray, W: np.ndarray) -> np.ndarray:
    """Local Moran's I (LISA)。

    I_i = z_i / m2 * sum_j w_ij z_j，其中 m2 = sum z^2 / n。
    返回逐点局部 I 值。
    """
    x = np.asarray(x, dtype=np.float64).ravel()
    n = x.shape[0]
    z = x - x.mean()
    m2 = (z ** 2).sum() / n
    if m2 < 1e-12:
        return np.zeros(n)
    Wz = W @ z
    return (z / m2) * Wz


def getis_ord_gi_star(x: np.ndarray, W: np.ndarray) -> np.ndarray:
    """Getis-Ord Gi*（含自身权重）。

    Gi*_i = (sum_j w_ij x_j - Xbar * sum_j w_ij) /
            {S * [n sum_j w_ij^2 - (sum_j w_ij)^2] / (n-1)}^0.5
    返回逐点 z 得分。
    """
    x = np.asarray(x, dtype=np.float64).ravel()
    n = x.shape[0]
    # 确保含自身（Gi* 需要 w_ii）
    Ws = W.copy()
    np.fill_diagonal(Ws, 1.0)
    xbar = x.mean()
    S = np.sqrt((x ** 2).sum() / n - xbar ** 2)
    S = max(S, 1e-12)
    row_sum = Ws.sum(1)
    row_sq = (Ws ** 2).sum(1)
    num = Ws @ x - xbar * row_sum
    den = S * np.sqrt((n * row_sq - row_sum ** 2) / (n - 1))
    den = np.where(den < 1e-12, 1e-12, den)
    return num / den


def monte_carlo_morans_i(x: np.ndarray, W: np.ndarray, permutations: int = 99,
                         seed: int = 42) -> Dict[str, float]:
    """蒙特卡洛置换检验 Moran's I 的伪 p 值。"""
    rng = np.random.default_rng(seed)
    obs = global_morans_i(x, W)["I"]
    n = x.shape[0]
    count = 0
    for _ in range(permutations):
        xp = rng.permutation(x)
        Ip = global_morans_i(xp, W)["I"]
        if Ip >= obs:
            count += 1
    pseudo_p = (count + 1) / (permutations + 1)
    return {"observed_I": float(obs), "pseudo_p": float(pseudo_p),
            "permutations": int(permutations)}


# ---------------------------------------------------------------------------
# 合成数据
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], grid_size: int = 32, mode: str = "cluster",
                       seed: int = 42) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成合成栅格场。mode: cluster(聚集) / random(随机) / gradient(梯度)。"""
    rng = np.random.default_rng(seed)
    h = w = grid_size
    if mode == "cluster":
        field = np.zeros((h, w))
        for _ in range(4):
            cy, cx = rng.integers(0, h), rng.integers(0, w)
            yy, xx = np.mgrid[0:h, 0:w]
            field += rng.uniform(1, 5) * np.exp(-((yy - cy) ** 2 + (xx - cx) ** 2) / (2 * 4.0 ** 2))
        field += rng.normal(0, 0.1, (h, w))
    elif mode == "gradient":
        yy, xx = np.mgrid[0:h, 0:w]
        field = (xx / w + yy / h).astype(np.float64) + rng.normal(0, 0.02, (h, w))
    else:  # random
        field = rng.normal(0, 1, (h, w))
    info = {"grid_size": grid_size, "mode": mode,
            "value_range": [float(field.min()), float(field.max())]}
    return field, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if array.ndim == 2:
        array = array[np.newaxis, ...]
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
        nodata = src.nodata
    if nodata is not None:
        data = np.where(data == nodata, np.nan, data)
    data = np.where(np.isfinite(data), data, np.nan)
    return data, bbox


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
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

    validate_params(args.grid_size, args.permutations)

    bbox = list(args.bbox) if args.bbox else None
    input_nodata = None

    if args.input and not args.synthetic:
        data, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        field = data[0] if data.ndim == 3 else data
        input_nodata = True
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        field, _ = generate_synthetic(bbox, grid_size=args.grid_size, mode=args.mode)
        source_note = "synthetic"

    validate_bbox(bbox)

    valid = np.isfinite(field)
    n_valid = int(valid.sum())
    n_total = int(field.size)
    if n_valid == 0:
        raise ValidationError(
            f"input raster contains no valid (non-NoData) pixels: all {n_total} pixels are NoData")
    if field.size < 4:
        raise ValidationError("raster too small for spatial autocorrelation")
    # 限制尺寸以控制 W 矩阵规模
    gs = args.grid_size
    if field.shape[0] > gs or field.shape[1] > gs:
        from scipy.ndimage import zoom
        zy = gs / field.shape[0]
        zx = gs / field.shape[1]
        field = zoom(field, (zy, zx), order=1)
        valid = zoom(valid.astype(np.float64), (zy, zx), order=0).astype(bool)
        n_valid = int(valid.sum())

    fill = float(np.nanmean(np.where(valid, field, np.nan)))
    field = np.where(valid, field, fill).astype(np.float64)
    n_valid_pixels = int(valid.sum())

    W = rook_weights(field.shape)
    x = field.ravel()

    gm = global_morans_i(x, W)
    mc = monte_carlo_morans_i(x, W, permutations=args.permutations)
    lisa = local_morans_i(x, W).reshape(field.shape)
    gi = getis_ord_gi_star(x, W).reshape(field.shape)

    os.makedirs(output_dir, exist_ok=True)
    out_lisa = os.path.join(output_dir, "lisa.tif")
    write_geotiff(out_lisa, np.where(valid, lisa, -9999.0), bbox)
    out_gi = os.path.join(output_dir, "gi_star.tif")
    write_geotiff(out_gi, np.where(valid, gi, -9999.0), bbox)
    stats_path = os.path.join(output_dir, "autocorrelation_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump({"global_morans_i": gm, "monte_carlo": mc}, f, ensure_ascii=False, indent=2)

    qa = {
        "source": source_note,
        "grid_shape": list(field.shape),
        "n_valid_pixels": int(n_valid),
        "n_total_pixels": int(n_total),
        "input_nodata": input_nodata,
        "global_morans_i": gm,
        "monte_carlo": mc,
        "gi_star_mean": float(np.nanmean(np.where(valid, gi, np.nan))),
        "lisa_mean": float(np.nanmean(np.where(valid, lisa, np.nan))),
    }
    outputs = [
        {"path": out_lisa, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": out_gi, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}  mode: {getattr(args, 'mode', 'n/a')}")
        print(f"[{SKILL_NAME}] Moran's I = {gm['I']:.4f}  z = {gm['z_score']:.3f}  p = {gm['p_value']:.4f}")
        print(f"[{SKILL_NAME}] MC pseudo-p = {mc['pseudo_p']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_gi}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Spatial autocorrelation: Global Moran's I, LISA, Getis-Ord Gi* with Monte Carlo test.",
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input GeoTIFF raster")
    p.add_argument("--mode", default="cluster", choices=["cluster", "random", "gradient"],
                   help="synthetic field mode (default: cluster)")
    p.add_argument("--grid-size", type=int, default=24, help="working grid size (default: 24)")
    p.add_argument("--permutations", type=int, default=99, help="MC permutations (default: 99)")
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
