#!/usr/bin/env python3
"""insar-deformation-monitoring — InSAR形变监测

简化差分干涉雷达（D-InSAR）形变监测流程。SAR 单视复影像（SLC）是复数
``A·exp(iφ)``；对同一区域两次成像的 master / slave SLC 做共轭相乘得到
干涉图：

- **干涉相位**：``ifg = angle(master · conj(slave))``，包含地形、形变与
  噪声相位。
- **相干性**：``coh = |Σ m·conj(s)| / sqrt(Σ|m|² · Σ|s|²)``（滑窗估计），
  取值 [0, 1]，衡量干涉质量（失相干来源：时间去相干、体积散射、噪声）。
- **形变量**：相位-形变关系 ``d = ifg · λ / (4π)``（视线向，λ 为雷达波长，
  C 波段 ~0.0555 m）。相位每 2π 周期对应 λ/2 的形变（约 2.8 cm）。

数据源：本地复数 SLC（4 波段 GeoTIFF：``[master_re, master_im, slave_re,
slave_im]``，2 波段时按实数对处理），或用 ``--synthetic`` 生成一对 SLC——
master 为随机相位，slave 在 master 上叠加一个平滑形变相位（线性斜坡 +
沉降漏斗）并加入失相干噪声，真值形变可用于验证。

隐私声明 / Privacy：
- 默认完全离线运行，不发起任何网络请求。
- ``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python insar-deformation-monitoring.py --input slc_pair.tif --wavelength 0.0555
    python insar-deformation-monitoring.py --bbox 116 39 117 40 --synthetic

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
SKILL_NAME = "insar-deformation-monitoring"

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
# Input validation (P0/P1)
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """Validate a [W, S, E, N] bbox. Raises ValidationError on bad order, range,
    zero-area, or crossing the 180° meridian.
    """
    try:
        w, s, e, n = [float(v) for v in bbox]
    except Exception:
        raise ValidationError(f"bbox must be 4 floats, got {bbox!r}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"longitude out of range [-180, 180]: W={w}, E={e}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"latitude out of range [-90, 90]: S={s}, N={n}")
    if w >= e:
        raise ValidationError(
            f"bbox requires W < E (got W={w}, E={e}); check --bbox order")
    if s >= n:
        raise ValidationError(
            f"bbox requires S < N (got S={s}, N={n}); check --bbox order")
    if e - w > 360.0 or n - s > 180.0:
        raise ValidationError(
            f"bbox span too large (dx={e - w}, dy={n - s})")
    if w > 180.0 or e > 180.0 or w < -180.0 or e < -180.0:
        raise ValidationError(
            f"bbox crosses 180° meridian; please split into two sub-bboxes")


def validate_insar_params(wavelength: float, window: int, noise_level: float) -> None:
    """Validate CLI parameter ranges. Raises ValidationError on bad input."""
    if not (float(wavelength) > 0.0):
        raise ValidationError(
            f"--wavelength must be > 0 (got {wavelength})")
    if int(window) < 1:
        raise ValidationError(
            f"--window must be >= 1, got {window}")
    if not (float(noise_level) >= 0.0):
        raise ValidationError(
            f"--noise-level must be >= 0, got {noise_level}")


def read_geotiff_with_nodata(path: str):
    """Read a multiband raster and return (data, bbox, nodata).

    Values equal to the source nodata (if any) are replaced with NaN.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [float(b.left), float(b.bottom), float(b.right), float(b.top)]
        nd = src.nodata
    if nd is not None:
        cube = np.where(cube == nd, np.nan, cube)
    return cube, bbox, nd


def count_valid_pixels(cube: np.ndarray) -> int:
    """Number of locations where ALL bands are finite (not NaN / inf)."""
    if cube.ndim == 3:
        valid_loc = np.all(np.isfinite(cube), axis=0)
    else:
        valid_loc = np.isfinite(cube)
    return int(valid_loc.sum())


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def interferogram(master: np.ndarray, slave: np.ndarray) -> np.ndarray:
    """干涉相位 ``angle(master · conj(slave))``，返回 (-π, π] 弧度。"""
    master = np.asarray(master, dtype=np.complex64)
    slave = np.asarray(slave, dtype=np.complex64)
    if master.shape != slave.shape:
        raise ValidationError(
            f"SLC shape mismatch: {master.shape} vs {slave.shape}",
            master_shape=list(master.shape), slave_shape=list(slave.shape),
        )
    ifg = master * np.conj(slave)
    return np.angle(ifg).astype(np.float32)


def coherence(master: np.ndarray, slave: np.ndarray, window: int = 5) -> np.ndarray:
    """滑窗相干性 ``|Σ m·conj(s)| / sqrt(Σ|m|² · Σ|s|²)``，取值 [0, 1]。"""
    from scipy.ndimage import uniform_filter

    master = np.asarray(master, dtype=np.complex64)
    slave = np.asarray(slave, dtype=np.complex64)
    if master.shape != slave.shape:
        raise ValidationError(
            f"SLC shape mismatch: {master.shape} vs {slave.shape}",
            master_shape=list(master.shape), slave_shape=list(slave.shape),
        )
    if window < 1:
        raise UsageError(f"--window must be >= 1, got {window}", window=int(window))
    if window > 1 and window % 2 == 0:
        window += 1
    eps = 1e-12

    cross = master * np.conj(slave)
    # 复数窗口求和：实部/虚部分别滤波
    num_re = uniform_filter(cross.real.astype(np.float64), size=window, mode="reflect")
    num_im = uniform_filter(cross.imag.astype(np.float64), size=window, mode="reflect")
    num = np.sqrt(num_re ** 2 + num_im ** 2)

    den_m = uniform_filter(np.abs(master).astype(np.float64) ** 2, size=window, mode="reflect")
    den_s = uniform_filter(np.abs(slave).astype(np.float64) ** 2, size=window, mode="reflect")
    den = np.sqrt(np.maximum(den_m * den_s, 0.0))

    coh = num / np.maximum(den, eps)
    return np.clip(coh, 0.0, 1.0).astype(np.float32)


def phase_to_deformation(ifg_phase: np.ndarray, wavelength: float) -> np.ndarray:
    """干涉相位 → 视线向形变：``d = φ · λ / (4π)``（米）。"""
    if wavelength <= 0:
        raise UsageError(
            f"--wavelength must be > 0, got {wavelength}", wavelength=float(wavelength),
        )
    return (np.asarray(ifg_phase, dtype=np.float32) * wavelength / (4.0 * np.pi))


def insar_process(
    master: np.ndarray,
    slave: np.ndarray,
    wavelength: float,
    window: int = 5,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """完整 D-InSAR 链：干涉相位 → 形变 + 相干性。返回 (deformation, coherence, params)。"""
    ifg = interferogram(master, slave)
    coh = coherence(master, slave, window=window)
    deform = phase_to_deformation(ifg, wavelength)
    params = {
        "wavelength_m": float(wavelength),
        "coherence_window": int(window),
        "shape": list(ifg.shape),
        "fringe_spacing_m": float(wavelength / 2.0),
        "mean_coherence": float(np.mean(coh)),
        "deformation_mean_m": float(np.mean(deform)),
        "deformation_min_m": float(np.min(deform)),
        "deformation_max_m": float(np.max(deform)),
        "phase_wrapped": bool(np.any(np.abs(ifg) > np.pi - 1e-3)),
    }
    return deform, coh, params


# ---------------------------------------------------------------------------
# 合成数据：master 随机相位 + slave 叠加平滑形变相位 + 失相干噪声
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 64,
    height: int = 64,
    wavelength: float = 0.0555,
    noise_level: float = 0.25,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成一对合成 SLC（master, slave）及真值形变场。

    master = amp·exp(iφ_rand)；slave = master·exp(iφ_def) + 热噪声，其中
    φ_def = 4π·d_true/λ，d_true 为线性斜坡 + 高斯沉降漏斗（最大形变量控制在
    λ/8 内以避免相位缠绕）。返回 (master, slave, info)。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yn = yy / max(height - 1, 1)
    xn = xx / max(width - 1, 1)

    # 幅度：平滑场（>0）
    amp = (0.8 + 0.2 * np.exp(-(((xn - 0.5) ** 2 + (yn - 0.5) ** 2) / 0.08))).astype(np.float32)

    # 随机散射相位
    phi_master = rng.uniform(-np.pi, np.pi, size=(height, width)).astype(np.float32)
    master = amp * np.exp(1j * phi_master)

    # 真值形变（米）：斜坡 + 沉降漏斗，幅值 < λ/8 以免缠绕
    ramp = 0.006 * xn                      # 东向倾斜
    bowl = -0.008 * np.exp(-(((xn - 0.6) ** 2 + (yn - 0.4) ** 2) / 0.02))  # 沉降
    d_true = (ramp + bowl).astype(np.float32)

    phi_def = 4.0 * np.pi * d_true / wavelength
    slave = master * np.exp(1j * phi_def)

    # 失相干噪声：向 slave 加入与 master 不相关的复噪声（相干性 < 1）
    noise = noise_level * amp.mean() * (
        rng.normal(size=(height, width)) + 1j * rng.normal(size=(height, width))
    )
    slave = slave + noise.astype(np.complex64)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "wavelength_m": float(wavelength),
        "noise_level": float(noise_level),
        "deformation_truth": d_true,
        "deformation_truth_min_m": float(d_true.min()),
        "deformation_truth_max_m": float(d_true.max()),
    }
    return master.astype(np.complex64), slave.astype(np.complex64), info


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


def slc_from_cube(cube: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """把实数波段立方体解释为一对复数 SLC。

    - ≥4 波段：``[m_re, m_im, s_re, s_im]``
    - 2/3 波段：``[m_re, s_re]``（虚部为 0）
    """
    nb = cube.shape[0]
    if nb >= 4:
        master = cube[0] + 1j * cube[1]
        slave = cube[2] + 1j * cube[3]
    elif nb >= 2:
        master = cube[0] + 1j * np.zeros_like(cube[0])
        slave = cube[1] + 1j * np.zeros_like(cube[1])
    else:
        raise ValidationError(
            "input needs >=2 bands (real pair) or >=4 bands (complex SLC pair)",
            bands=int(nb),
        )
    return master.astype(np.complex64), slave.astype(np.complex64)


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
            "wavelength": getattr(args, "wavelength", None),
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

    # 1) 获取 SLC 对
    synth_info: Optional[Dict[str, Any]] = None
    src_nd = None
    if args.input and not args.synthetic:
        cube, file_bbox, _src_nd = read_geotiff_with_nodata(args.input)
        bbox = bbox if bbox is not None else file_bbox
        master, slave = slc_from_cube(cube)
        source_note = args.input
        src_nd = _src_nd
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        master, slave, synth_info = generate_synthetic(
            bbox, wavelength=args.wavelength, noise_level=args.noise_level,
        )
        source_note = "synthetic"

    # Parameter validation (BEFORE side-effect makedirs).
    if bbox is not None:
        validate_bbox(bbox)
    validate_insar_params(args.wavelength, args.window, args.noise_level)

    if master.size == 0:
        raise ValidationError("input raster is empty")

    # Check NoData propagation — at least one valid pixel must remain in the
    # complex SLC. We count across the real/imaginary cube before conversion.
    if args.input and not args.synthetic:
        # Re-read once to count (the earlier read already converted; we
        # stored `_src_nd` but not the cube). Reading twice is fine for a
        # small SLC pair.
        cube_for_count, _, _ = read_geotiff_with_nodata(args.input)
        n_valid = count_valid_pixels(cube_for_count)
    else:
        # Synthetic mode: all pixels are finite.
        n_valid = int(np.isfinite(master).sum())
    if n_valid == 0:
        raise ValidationError(
            "input SLC has no valid pixels (all NoData / NaN); cannot estimate")

    # 2) D-InSAR 处理
    deform, coh, params = insar_process(
        master, slave, wavelength=args.wavelength, window=args.window,
    )

    # 3) Side effects begin only after all validation passes.
    os.makedirs(output_dir, exist_ok=True)

    deform_tif = os.path.join(output_dir, "deformation.tif")
    coh_tif = os.path.join(output_dir, "coherence.tif")
    write_geotiff(deform_tif, deform, bbox)
    write_geotiff(coh_tif, coh, bbox)

    params_path = os.path.join(output_dir, "insar_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    n_total = int(deform.size)
    qa: Dict[str, Any] = {
        "source": source_note,
        "wavelength_m": float(args.wavelength),
        "n_valid_pixels": n_valid,
        "n_total_pixels": n_total,
        "input_nodata": src_nd,
        "mean_coherence": params["mean_coherence"],
        "deformation_mean_m": params["deformation_mean_m"],
        "deformation_range_m": [params["deformation_min_m"], params["deformation_max_m"]],
    }
    if synth_info is not None:
        d_truth = synth_info["deformation_truth"]
        if np.std(deform) > 0 and np.std(d_truth) > 0:
            corr = float(np.corrcoef(deform.ravel(), d_truth.ravel())[0, 1])
        else:
            corr = 0.0
        qa["synthetic_correlation_with_truth"] = corr
        qa["synthetic_truth_range_m"] = [
            synth_info["deformation_truth_min_m"],
            synth_info["deformation_truth_max_m"],
        ]

    outputs = [
        {"path": deform_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": coh_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] wavelength: {args.wavelength} m  window: {args.window}")
        print(f"[{SKILL_NAME}] shape: {params['shape']}")
        print(f"[{SKILL_NAME}] mean coherence: {params['mean_coherence']:.3f}")
        print(f"[{SKILL_NAME}] deformation range: "
              f"[{params['deformation_min_m'] * 100:.3f}, {params['deformation_max_m'] * 100:.3f}] cm")
        print(f"[{SKILL_NAME}] deformation: {deform_tif}")
        print(f"[{SKILL_NAME}] coherence:  {coh_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Simplified D-InSAR deformation monitoring from master/slave SLCs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="SLC pair GeoTIFF (4 bands: m_re m_im s_re s_im)")
    p.add_argument("--wavelength", type=float, default=0.0555,
                   help="radar wavelength in meters (default: 0.0555, C-band)")
    p.add_argument("--window", type=int, default=5,
                   help="coherence estimation window size (default: 5)")
    p.add_argument("--noise-level", type=float, default=0.25,
                   help="synthetic decorrelation noise level (default: 0.25)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic SLC pair (offline)")
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
