#!/usr/bin/env python3
"""pca-dimension-reduction — 主成分分析降维

对多波段影像执行主成分分析（PCA, Principal Component Analysis）变换，
把高度相关的多波段数据压缩到少数几个互不相关的主成分，用于降维、
去噪和特征提取。

算法：
- 把 (bands, H, W) 立方体重排为 (bands, N) 矩阵（N = H×W）；
- 逐波段去均值（中心化），计算 bands×bands 协方差矩阵；
- 用 ``np.linalg.eigh`` 做对称特征分解，按特征值降序排列；
- 投影到前 n 个主成分（载荷矩阵 × 中心化数据）。

输出：PCA GeoTIFF（前 n 个主成分）+ 特征值/方差贡献率 JSON + 载荷矩阵。
可选 ``--inverse`` 用前 n 个主成分重构影像（评估信息损失）。

数据源：本地多光谱 GeoTIFF，或使用 ``--synthetic`` 生成高相关多波段
模拟影像用于离线验证（第一主成分应捕获最大方差）。

隐私声明 / Privacy：
- 默认离线运行，仅在显式 ``--place`` 解析地名时才会访问 Nominatim/Open-Meteo。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python pca-dimension-reduction.py --input scene.tif --n-components 3
    python pca-dimension-reduction.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "pca-dimension-reduction"

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
# Validation helpers
# ---------------------------------------------------------------------------
def validate_bbox(bbox: List[float], source: str = "bbox") -> None:
    """Validate geographic bbox: W<=E, S<=N, lon/lat in range, min area.

    Cross-dateline (W>E) is a ValidationError with a hint to split.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(f"{source}: expected 4 floats [W S E N], got {bbox!r}")
    try:
        w, s, e, n = (float(v) for v in bbox)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"{source}: non-numeric bbox values: {bbox!r}") from exc
    for v, name in ((w, "W"), (s, "S"), (e, "E"), (n, "N")):
        if not (v == v):
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


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def pca_transform(
    cube: np.ndarray,
    n_components: int,
    valid_mask: Optional[np.ndarray] = None,
) -> Dict[str, Any]:
    """对 (bands, H, W) 立方体执行 PCA。

    ``valid_mask`` is an optional (H, W) boolean array; only pixels where the
    mask is True participate in the covariance estimation. This is the right
    way to handle NoData (typically the file's declared nodata sentinel): a
    -9999 pixel used to dominate PC1 because it is 4-5 orders of magnitude
    larger than the scene range.

    返回字典：
      scores:      (n_components, H, W) 主成分影像（NoData 区域=0）
      eigenvalues: (bands,) 降序特征值
      explained_ratio: (bands,) 各主成分方差贡献率
      cumulative:  (bands,) 累计贡献率
      loadings:    (bands, bands) 载荷矩阵（列为主成分）
      mean:        (bands,) 各波段均值（用于逆变换，仅基于 valid 像素）
    """
    nb, h, w = cube.shape
    if n_components < 1 or n_components > nb:
        raise UsageError(
            f"n-components must be in [1, {nb}] but got {n_components}",
            n_components=n_components, bands=int(nb),
        )

    # Build / honor the valid mask: a pixel is valid iff all bands are finite.
    if valid_mask is None:
        valid_mask = np.isfinite(cube).all(axis=0)
    else:
        valid_mask = np.asarray(valid_mask, dtype=bool) & np.isfinite(cube).all(axis=0)
    n_valid = int(valid_mask.sum())
    if n_valid < 2:
        raise ValidationError(
            f"need at least 2 valid (non-NoData) pixels to run PCA; got {n_valid}"
        )

    X = cube.reshape(nb, -1).astype(np.float64)  # (bands, N)
    # Subset to valid pixels only
    Xv = X[:, valid_mask.reshape(-1)]  # (bands, n_valid)
    N = Xv.shape[1]

    mean = Xv.mean(axis=1, keepdims=True)  # (bands, 1) — valid-pixel mean
    Xc = Xv - mean

    # 协方差矩阵 (bands, bands)
    cov = (Xc @ Xc.T) / (N - 1)
    eigvals, eigvecs = np.linalg.eigh(cov)  # 升序

    # 降序排列
    order = np.argsort(eigvals)[::-1]
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]
    eigvals = np.clip(eigvals, 0.0, None)

    total = float(eigvals.sum())
    explained = eigvals / total if total > 0 else np.zeros_like(eigvals)
    cumulative = np.cumsum(explained)

    loadings = eigvecs  # (bands, bands)，列为 PC
    # Project *all* pixels onto the loading vectors so the output raster keeps
    # its H×W shape. For NoData pixels the result is meaningless, so we set
    # their score to 0 (a transparent convention).
    Xc_all = X - mean  # (bands, N) using valid-pixel mean
    scores_all = loadings.T @ Xc_all  # (bands, N)
    # Reshape and zero-out NoData pixels
    scores = scores_all.reshape(nb, h, w).astype(np.float32)
    scores = scores * valid_mask[np.newaxis, :, :].astype(np.float32)
    scores = scores[:n_components]

    return {
        "scores": scores,
        "eigenvalues": eigvals.astype(np.float64),
        "explained_ratio": explained.astype(np.float64),
        "cumulative": cumulative.astype(np.float64),
        "loadings": loadings.astype(np.float64),
        "mean": mean.ravel().astype(np.float64),
        "n_valid_pixels": n_valid,
    }


def inverse_pca(
    scores: np.ndarray,
    loadings: np.ndarray,
    mean: np.ndarray,
    n_bands: int,
) -> np.ndarray:
    """用前 n 个主成分重构 (bands, H, W) 影像（近似逆变换）。"""
    n_pc, h, w = scores.shape
    flat = scores.reshape(n_pc, -1).astype(np.float64)  # (n_pc, N)
    recon = loadings[:, :n_pc] @ flat  # (bands, N)
    recon = recon + mean.reshape(n_bands, 1)
    return recon.reshape(n_bands, h, w).astype(np.float32)


# ---------------------------------------------------------------------------
# 合成数据：高相关多波段影像（离线验证）
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float],
    n_bands: int = 6,
    width: int = 128,
    height: int = 128,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (n_bands, H, W) 高相关影像：一个主导潜在场 + 各波段线性缩放 + 噪声。

    这样第一主成分会捕获绝大部分方差，便于验证 PCA 正确性。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xx = xx.astype(np.float64) / max(width - 1, 1)
    yy = yy.astype(np.float64) / max(height - 1, 1)

    # 主导潜在场（平滑空间梯度 + 正弦）
    latent = 0.6 * xx + 0.3 * yy + 0.1 * np.sin(4 * np.pi * xx)

    cube = np.zeros((n_bands, height, width), dtype=np.float32)
    weights = np.linspace(0.5, 1.5, n_bands)
    for b in range(n_bands):
        band = weights[b] * latent + 0.2 + rng.normal(0, 0.02, (height, width))
        cube[b] = np.clip(band, 0.0, None).astype(np.float32)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "n_bands": n_bands,
        "mean_per_band": [float(np.mean(cube[b])) for b in range(n_bands)],
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
            "n_components": getattr(args, "n_components", None),
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
    os.makedirs(output_dir, exist_ok=True)

    bbox = list(args.bbox) if args.bbox else None

    # 1) 获取数据立方体（通用契约）
    synth_info: Optional[Dict[str, Any]] = None
    valid_mask: Optional[np.ndarray] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        # Build a per-pixel valid mask from the file's declared NoData sentinel
        # so PCA ignores -9999 instead of letting it dominate PC1.
        import rasterio as _rio
        with _rio.open(args.input) as _src:
            _nd = _src.nodata
        if _nd is not None:
            valid_mask = (cube != _nd).all(axis=0)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox, source="--bbox")
        cube, synth_info = generate_synthetic_cube(bbox)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    # If --bbox is also given with --input, validate the user-supplied bbox
    if bbox is not None and args.bbox is not None:
        validate_bbox(bbox, source="--bbox")

    # 2) PCA
    res = pca_transform(cube, args.n_components, valid_mask=valid_mask)
    scores = res["scores"]

    # 3) 写出主成分 GeoTIFF
    out_tif = os.path.join(output_dir, "pca_components.tif")
    write_geotiff(out_tif, scores, bbox)

    # 可选：逆变换重构
    outputs: List[Dict[str, Any]] = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(scores.shape[0])},
    ]
    recon_rmse: Optional[float] = None
    if args.inverse:
        recon = inverse_pca(scores, res["loadings"], res["mean"], cube.shape[0])
        recon_tif = os.path.join(output_dir, "pca_reconstruction.tif")
        write_geotiff(recon_tif, recon, bbox)
        outputs.append({"path": recon_tif, "kind": "raster", "crs_epsg": 4326,
                        "bbox_wgs84": bbox, "band_count": int(recon.shape[0])})
        recon_rmse = float(np.sqrt(np.mean((recon - cube) ** 2)))

    # 特征值 / 贡献率 / 载荷 JSON
    eigen_doc = {
        "n_bands": int(cube.shape[0]),
        "n_components": int(args.n_components),
        "eigenvalues": res["eigenvalues"].tolist(),
        "explained_variance_ratio": res["explained_ratio"].tolist(),
        "cumulative_ratio": res["cumulative"].tolist(),
        "loadings": res["loadings"].tolist(),
        "band_means": res["mean"].tolist(),
    }
    if recon_rmse is not None:
        eigen_doc["reconstruction_rmse"] = recon_rmse
    eigen_path = os.path.join(output_dir, "pca_statistics.json")
    with open(eigen_path, "w", encoding="utf-8") as f:
        json.dump(eigen_doc, f, ensure_ascii=False, indent=2)
    outputs.append({"path": eigen_path, "kind": "json"})

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_bands": int(cube.shape[0]),
        "n_components": int(args.n_components),
        "pc1_explained_ratio": float(res["explained_ratio"][0]),
        "cumulative_kept": float(res["cumulative"][args.n_components - 1]),
        "n_valid_pixels": int(res.get("n_valid_pixels", cube.shape[1] * cube.shape[2])),
    }
    if recon_rmse is not None:
        qa["reconstruction_rmse"] = recon_rmse
    if synth_info is not None:
        qa["synthetic_mean_per_band"] = synth_info["mean_per_band"]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] bands: {cube.shape[0]}  components kept: {args.n_components}")
        print(f"[{SKILL_NAME}] PC1 explained ratio: {qa['pc1_explained_ratio']:.4f}")
        print(f"[{SKILL_NAME}] cumulative kept:    {qa['cumulative_kept']:.4f}")
        if recon_rmse is not None:
            print(f"[{SKILL_NAME}] reconstruction RMSE: {recon_rmse:.5f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="PCA dimension reduction for multispectral imagery.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multispectral GeoTIFF")
    p.add_argument("--n-components", type=int, default=3,
                   help="number of principal components to keep (default: 3)")
    p.add_argument("--inverse", action="store_true",
                   help="also write a PCA reconstruction from kept components")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a correlated synthetic scene (offline)")
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
