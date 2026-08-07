#!/usr/bin/env python3
"""spectral-unmixing — 光谱解混

对多光谱影像执行线性光谱混合模型（LSMM, Linear Spectral Mixture Model）分解，
估计每个像元内各地物端元（endmember）的面积比例（丰度, abundance）。

算法：
- 像元光谱 = Σ (丰度_i × 端元光谱_i) + 残差
- 用 **非负约束最小二乘**（scipy.optimize.nnls）逐像元求解丰度，
  再归一化使各端元丰度之和为 1（fully constrained）。
- 端元来源：内置典型地物光谱（植被/土壤/水体/不透水面），
  或用 ``--endmembers auto`` 从影像中自动提取纯像元端元（贪心最远点法）。

输出：丰度图 GeoTIFF（每端元一波段）+ 端元光谱 JSON + 残差 RMSE。

数据源：本地多光谱 GeoTIFF（波段顺序 blue/green/red/nir/swir1/swir2），
或使用 ``--synthetic`` 生成已知端元+丰度混合的模拟影像用于离线验证。

隐私声明 / Privacy：
- 默认离线运行，仅在显式 ``--place`` 解析地名时才会访问 Nominatim/Open-Meteo。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python spectral-unmixing.py --input scene.tif --n-endmembers 3
    python spectral-unmixing.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "spectral-unmixing"

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


BAND_NAMES = ["blue", "green", "red", "nir", "swir1", "swir2"]

# 内置典型地物端元光谱（6 波段反射率，公开典型值）
# 每行一个端元：[blue, green, red, nir, swir1, swir2]
BUILTIN_ENDMEMBERS: Dict[str, List[float]] = {
    "vegetation": [0.03, 0.08, 0.04, 0.45, 0.20, 0.12],
    "soil":       [0.10, 0.14, 0.18, 0.28, 0.32, 0.30],
    "water":      [0.06, 0.05, 0.03, 0.01, 0.005, 0.001],
    "impervious": [0.12, 0.13, 0.15, 0.20, 0.24, 0.22],
}
ENDMEMBER_ORDER = ["vegetation", "soil", "water", "impervious"]


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def builtin_endmembers(n_endmembers: int, n_bands: int = 6) -> Tuple[np.ndarray, List[str]]:
    """返回内置端元矩阵 (n_endmembers, n_bands) 与名字列表。

    注：内置端元固定为 6 波段（blue/green/red/nir/swir1/swir2）；
    若 ``n_bands != 6`` 则抛 ValidationError（避免静默截断造成不期望的解混结果）。
    """
    if n_endmembers < 1 or n_endmembers > len(ENDMEMBER_ORDER):
        raise UsageError(
            f"n-endmembers must be in [1, {len(ENDMEMBER_ORDER)}] for builtin set",
            n_endmembers=n_endmembers,
        )
    if n_bands != 6:
        raise ValidationError(
            f"builtin endmembers require exactly 6 bands (blue/green/red/nir/swir1/swir2), "
            f"got n_bands={n_bands}; use --endmembers auto for arbitrary band count",
            n_bands=n_bands,
        )
    names = ENDMEMBER_ORDER[:n_endmembers]
    em = np.array([BUILTIN_ENDMEMBERS[n] for n in names], dtype=np.float32)
    return em, names


def unmix_pixel(spectrum: np.ndarray, endmembers: np.ndarray) -> Tuple[np.ndarray, float]:
    """对单个像元光谱做非负约束最小二乘解混。

    spectrum: (n_bands,)
    endmembers: (n_endmembers, n_bands)
    返回 (abundances (n_endmembers,) 归一化和为1, rmse)。
    """
    from scipy.optimize import nnls

    A = endmembers.T.astype(np.float64)  # (n_bands, n_endmembers)
    b = spectrum.astype(np.float64)
    frac, residual = nnls(A, b)
    s = frac.sum()
    if s > 1e-12:
        frac = frac / s
    else:
        frac = np.full(frac.shape, 1.0 / frac.size)
    fitted = endmembers.T @ frac
    rmse = float(np.sqrt(np.mean((fitted - b) ** 2)))
    return frac.astype(np.float32), rmse


def unmix_cube(
    cube: np.ndarray,
    endmembers: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray]:
    """对整个 (bands, H, W) 立方体解混。

    返回 (abundance_cube (n_em, H, W), rmse_map (H, W))。
    """
    nb, h, w = cube.shape
    n_em = endmembers.shape[0]
    if endmembers.shape[1] != nb:
        raise ValidationError(
            f"endmembers have {endmembers.shape[1]} bands but cube has {nb}",
            em_bands=int(endmembers.shape[1]), cube_bands=int(nb),
        )
    abun = np.zeros((n_em, h, w), dtype=np.float32)
    rmse = np.zeros((h, w), dtype=np.float32)
    flat = cube.reshape(nb, -1).T  # (H*W, bands)
    for p in range(flat.shape[0]):
        f, r = unmix_pixel(flat[p], endmembers)
        abun[:, p // w, p % w] = f
        rmse[p // w, p % w] = r
    return abun, rmse


def extract_endmembers_auto(
    cube: np.ndarray,
    n_endmembers: int,
) -> Tuple[np.ndarray, List[str]]:
    """从影像自动提取端元：贪心最远点法（在光谱空间中选纯像元）。

    1. 选亮度最高的像元作为第一个端元；
    2. 迭代选择与已选端元集合最小距离最大的像元（最大化差异性）。
    返回 (endmembers (n_endmembers, n_bands), names)。
    """
    nb, h, w = cube.shape
    flat = cube.reshape(nb, -1).T.astype(np.float64)  # (N, bands)
    n_pix = flat.shape[0]
    if n_pix == 0:
        raise ValidationError("cannot extract endmembers from empty cube")

    brightness = flat.sum(axis=1)
    first = int(np.argmax(brightness))
    selected = [first]

    # 到已选集合的最小距离（初始化为到第一个端元的距离）
    min_dist = np.linalg.norm(flat - flat[first], axis=1)
    min_dist[first] = -1.0

    while len(selected) < n_endmembers and len(selected) < n_pix:
        nxt = int(np.argmax(min_dist))
        if min_dist[nxt] <= 0:
            break
        selected.append(nxt)
        d = np.linalg.norm(flat - flat[nxt], axis=1)
        min_dist = np.minimum(min_dist, d)
        min_dist[nxt] = -1.0

    em = flat[selected].astype(np.float32)
    names = [f"endmember_{i+1}" for i in range(em.shape[0])]
    return em, names


# ---------------------------------------------------------------------------
# 合成数据：已知端元 + 丰度混合（离线验证）
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float],
    n_endmembers: int = 3,
    width: int = 96,
    height: int = 96,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (6, H, W) 混合影像：内置端元 × 空间变化丰度 + 高斯噪声。

    丰度用 softmax(空间线性场) 生成，保证逐像元和为 1。
    """
    rng = np.random.default_rng(seed)
    n_bands = len(BAND_NAMES)
    em, names = builtin_endmembers(n_endmembers, n_bands)

    yy, xx = np.mgrid[0:height, 0:width]
    xx = xx.astype(np.float64) / max(width - 1, 1)
    yy = yy.astype(np.float64) / max(height - 1, 1)

    # 每个端元一个空间线性评分场（不同方向）
    scores = np.zeros((n_endmembers, height, width), dtype=np.float64)
    for i in range(n_endmembers):
        ang = 2.0 * np.pi * i / n_endmembers
        scores[i] = np.cos(ang) * xx + np.sin(ang) * yy + 0.3 * i

    # softmax → 丰度（和为 1）
    scores = scores - scores.max(axis=0, keepdims=True)
    exp_s = np.exp(scores)
    fracs = exp_s / exp_s.sum(axis=0, keepdims=True)  # (n_em, H, W)

    # 混合：cube[b] = Σ_i frac[i] * em[i, b]
    cube = np.einsum("ihw,ib->bhw", fracs, em.astype(np.float64))
    cube = cube + rng.normal(0, 0.003, size=cube.shape)
    cube = np.clip(cube, 0.0, 1.0).astype(np.float32)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "band_names": BAND_NAMES,
        "endmember_names": names,
        "true_endmembers": em.tolist(),
        "true_mean_abundance": {
            names[i]: float(np.mean(fracs[i])) for i in range(n_endmembers)
        },
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
            "n_endmembers": getattr(args, "n_endmembers", None),
            "endmembers": getattr(args, "endmembers", None),
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
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox, n_valid_pixels, input_nodata = read_geotiff_full(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if bbox is not None:
            bbox = validate_bbox(bbox)
        source_note = args.input
    else:
        cube, synth_info = generate_synthetic_cube(bbox, n_endmembers=args.n_endmembers)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    # 2) 确定端元
    if args.endmembers == "auto":
        em, names = extract_endmembers_auto(cube, args.n_endmembers)
    else:
        em, names = builtin_endmembers(args.n_endmembers, n_bands=cube.shape[0])

    # 3) 解混
    abun, rmse = unmix_cube(cube, em)

    # 4) ALL checks passed → safe to makedirs
    os.makedirs(output_dir, exist_ok=True)

    # 5) 写出产物
    out_tif = os.path.join(output_dir, "abundance.tif")
    write_geotiff(out_tif, abun, bbox)

    em_doc = {
        "method": "LSMM + NNLS (fully constrained)",
        "endmember_source": args.endmembers,
        "n_endmembers": int(em.shape[0]),
        "band_names": BAND_NAMES[:cube.shape[0]],
        "endmember_names": names,
        "endmember_spectra": {names[i]: em[i].tolist() for i in range(em.shape[0])},
        "mean_abundance": {names[i]: float(np.mean(abun[i])) for i in range(em.shape[0])},
        "mean_rmse": float(np.mean(rmse)),
    }
    em_path = os.path.join(output_dir, "endmembers.json")
    with open(em_path, "w", encoding="utf-8") as f:
        json.dump(em_doc, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "n_endmembers": int(em.shape[0]),
        "endmember_source": args.endmembers,
        "mean_abundance": em_doc["mean_abundance"],
        "mean_rmse": em_doc["mean_rmse"],
        "n_valid_pixels": n_valid_pixels,
        "input_nodata": input_nodata,
    }
    if synth_info is not None:
        qa["synthetic_true_mean_abundance"] = synth_info["true_mean_abundance"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(abun.shape[0])},
        {"path": em_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] endmembers ({args.endmembers}): {names}")
        for i, nm in enumerate(names):
            print(f"[{SKILL_NAME}]   {nm:12s} mean_abundance={em_doc['mean_abundance'][nm]:.4f}")
        print(f"[{SKILL_NAME}] mean RMSE: {em_doc['mean_rmse']:.5f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Linear spectral unmixing (LSMM + NNLS) for multispectral imagery.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multispectral GeoTIFF")
    p.add_argument("--n-endmembers", type=int, default=3,
                   help="number of endmembers (default: 3)")
    p.add_argument("--endmembers", default="builtin", choices=["builtin", "auto"],
                   help="endmember source: builtin spectra or auto-extract (default: builtin)")
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
