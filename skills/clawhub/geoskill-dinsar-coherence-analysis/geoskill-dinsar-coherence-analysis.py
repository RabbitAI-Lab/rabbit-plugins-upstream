#!/usr/bin/env python3
"""dinsar-coherence-analysis — D-InSAR 相干性分析

从配准后的主 / 从复单视复图像（SLC）估计 **复相干系数** 与 **干涉相位**：

- **复相干系数**（complex coherence）

      γ = |Σ (m · conj(s))| / sqrt(Σ|m|² · Σ|s|²)

  在 ``--looks-r`` × ``--looks-a`` 的多视窗口内求和估计。γ∈[0,1]：稳定
  散射体（建筑、裸岩）相干性高；发生变化的区域（新建 / 拆除、滑坡体、
  植被）去相关、相干性低。
- **干涉相位** φ = angle(Σ m · conj(s))，反映视线向形变 / 地形相位。

多视（multi-looking）用窗口均值实现：分子、分母同窗口归一化相互抵消，
等价于对协方差项做 boxcar 估计。

数据源：本地主 / 从复 SLC GeoTIFF（2 波段：实部 + 虚部），或 ``--synthetic``
生成主从复 SLC（稳定区高相关、注入变化斑块去相关）用于离线验证。

隐私声明 / Privacy：
- 默认完全离线，``--synthetic`` 无网络。
- 所有处理本地完成，不上传用户数据。

Usage:
    python dinsar-coherence-analysis.py --input master.tif --slave slave.tif --output-dir ./out
    python dinsar-coherence-analysis.py --bbox 116 39 117 40 --looks-r 5 --looks-a 1 --output-dir ./out

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
SKILL_NAME = "dinsar-coherence-analysis"

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
# 校验：bbox / looks / threshold
# ---------------------------------------------------------------------------
def validate_bbox(bbox) -> None:
    """P0: bbox 合法性前置校验。"""
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            f"bbox must be a 4-element [W S E N]; got {bbox!r}"
        )
    try:
        w, s, e, n = [float(v) for v in bbox]
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox values must be numeric; got {bbox!r}") from exc
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range [-180, 180]: W={w}, E={e}"
        )
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range [-90, 90]: S={s}, N={n}"
        )
    if w >= e:
        if w > 0 and e < 0 and (e - w) > -360:
            raise ValidationError(
                f"bbox W ({w}) >= E ({e}); cross-180° antimeridian is not "
                f"supported — split into two extents"
            )
        raise ValidationError(f"bbox W ({w}) must be < E ({e})")
    if s >= n:
        raise ValidationError(f"bbox S ({s}) must be < N ({n})")
    area = (e - w) * (n - s)
    if area <= 0:
        raise ValidationError(f"bbox area must be > 0; got {area}")


def validate_dinsar_params(looks_r: int, looks_a: int, coh_threshold: float) -> None:
    if not isinstance(looks_r, int) or looks_r < 1:
        raise UsageError(f"--looks-r must be >= 1; got {looks_r}")
    if not isinstance(looks_a, int) or looks_a < 1:
        raise UsageError(f"--looks-a must be >= 1; got {looks_a}")
    if not (0.0 <= coh_threshold <= 1.0):
        raise UsageError(
            f"--coh-threshold must be in [0, 1]; got {coh_threshold}"
        )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def complex_coherence(
    master: np.ndarray,
    slave: np.ndarray,
    looks_r: int = 5,
    looks_a: int = 1,
) -> Tuple[np.ndarray, np.ndarray]:
    """估计复相干系数 γ 与干涉相位 φ。

    参数为复数二维数组（主 / 从 SLC）。在 ``(looks_r, looks_a)`` 窗口内做
    boxcar 多视：对 ``m·conj(s)``、``|m|²``、``|s|²`` 分别滑窗平均，窗口
    归一化在比值中抵消。返回 ``(gamma, phase)``，γ∈[0,1]，φ∈(-π,π]。
    """
    m = np.asarray(master, dtype=np.complex64)
    s = np.asarray(slave, dtype=np.complex64)
    if m.shape != s.shape:
        raise ValidationError(
            f"master/slave shape mismatch: {m.shape} vs {s.shape}",
            master_shape=tuple(m.shape), slave_shape=tuple(s.shape),
        )
    looks_r = max(int(looks_r), 1)
    looks_a = max(int(looks_a), 1)

    from scipy.ndimage import uniform_filter
    size = (looks_r, looks_a)
    prod = m * np.conj(s)
    num_r = uniform_filter(prod.real.astype(np.float64), size=size, mode="reflect")
    num_i = uniform_filter(prod.imag.astype(np.float64), size=size, mode="reflect")
    den_m = uniform_filter((m.real ** 2 + m.imag ** 2).astype(np.float64), size=size, mode="reflect")
    den_s = uniform_filter((s.real ** 2 + s.imag ** 2).astype(np.float64), size=size, mode="reflect")

    denom = np.sqrt(np.clip(den_m, 0.0, None) * np.clip(den_s, 0.0, None))
    with np.errstate(divide="ignore", invalid="ignore"):
        gamma = np.sqrt(num_r ** 2 + num_i ** 2) / denom
    gamma = np.nan_to_num(gamma, nan=0.0, posinf=1.0, neginf=0.0)
    gamma = np.clip(gamma, 0.0, 1.0).astype(np.float32)

    phase = np.arctan2(num_i, num_r).astype(np.float32)
    return gamma, phase


def coherence_statistics(
    gamma: np.ndarray,
    bbox: List[float],
    coh_threshold: float = 0.3,
) -> Dict[str, Any]:
    """相干性统计：均值、分位数、低相干区占比与面积。"""
    g = gamma[np.isfinite(gamma)]
    lat_mid = 0.5 * (bbox[1] + bbox[3])
    km_per_deg_lon = 111.0 * float(np.cos(np.deg2rad(lat_mid)))
    area_km2 = abs((bbox[2] - bbox[0]) * km_per_deg_lon * (bbox[3] - bbox[1]) * 111.0)
    h, w = gamma.shape
    low = (g < coh_threshold)
    stats = {
        "mean_coherence": float(np.mean(g)) if g.size else 0.0,
        "median_coherence": float(np.median(g)) if g.size else 0.0,
        "std_coherence": float(np.std(g)) if g.size else 0.0,
        "min_coherence": float(np.min(g)) if g.size else 0.0,
        "max_coherence": float(np.max(g)) if g.size else 0.0,
        "coherence_threshold": float(coh_threshold),
        "low_coherence_fraction": float(low.mean()) if g.size else 0.0,
        "low_coherence_pixels": int(low.sum()),
        "total_pixels": int(gamma.size),
        "scene_area_km2": float(area_km2),
        "low_coherence_area_km2": float(area_km2 * (low.sum() / gamma.size)) if gamma.size else 0.0,
        "multilook_shape": [int(h), int(w)],
    }
    return stats


# ---------------------------------------------------------------------------
# 合成数据：主从复 SLC（稳定区高相关 + 变化区去相关）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, Any]]:
    """生成主 / 从复 SLC。

    - master：瑞利幅度 + 均匀随机相位（典型完全发育散斑）。
    - slave 稳定区：``master · exp(i·φ_def) + 小热噪声``，保持高相干；
      ``φ_def`` 为沿列缓慢变化的形变相位条纹。
    - slave 变化区：注入若干独立随机 SLC 斑块，完全去相关。

    返回 ``(master, slave, truth_change, info)``。
    """
    rng = np.random.default_rng(seed)
    amp_m = rng.rayleigh(1.0, size=(height, width)).astype(np.float32)
    phase_m = rng.uniform(-np.pi, np.pi, size=(height, width))
    master = (amp_m * np.exp(1j * phase_m)).astype(np.complex64)

    # 稳定区形变相位：沿列的缓变条纹（视线向形变）
    phi_def = np.linspace(0.0, 2.0 * np.pi, width)[None, :].repeat(height, axis=0)
    noise = (rng.normal(0, 0.08, (height, width)) + 1j * rng.normal(0, 0.08, (height, width)))
    slave = master * np.exp(1j * phi_def) + noise * amp_m[:, :]

    truth_change = np.zeros((height, width), dtype=np.uint8)
    patches = [(8, 8, 30, 30), (34, 34, 56, 56)]
    for (r0, c0, r1, c1) in patches:
        r1 = min(r1, height)
        c1 = min(c1, width)
        rr, cc = r1 - r0, c1 - c0
        if rr <= 0 or cc <= 0:
            continue
        amp_s = rng.rayleigh(1.0, (rr, cc))
        ph = rng.uniform(-np.pi, np.pi, (rr, cc))
        slave[r0:r1, c0:c1] = (amp_s * np.exp(1j * ph)).astype(np.complex64)
        truth_change[r0:r1, c0:c1] = 1

    slave = slave.astype(np.complex64)
    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "seed": seed,
        "change_fraction": float(truth_change.mean()),
        "patches": [list(p) for p in patches],
    }
    return master, slave, truth_change, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    cube: np.ndarray,
    bbox: List[float],
    nodata: float = -9999.0,
    dtype: str = "float32",
) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype(dtype), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read(masked=False).astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None:
        cube = np.where(cube == float(nodata), np.nan, cube)
    return cube, bbox


def read_nodata(path: str) -> Optional[float]:
    """从 GeoTIFF 文件读 nodata 值（不读数据）。用于记录到 qa。"""
    import rasterio
    with rasterio.open(path) as src:
        return src.nodata


def read_complex_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """读取复 SLC：2 波段视为 (实部, 虚部)，单波段视为实部（相位 0）。"""
    cube, bbox = read_geotiff(path)
    if cube.shape[0] >= 2:
        c = cube[0] + 1j * cube[1]
    else:
        c = cube[0] + 0j
    return c.astype(np.complex64), bbox


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
            "slave": getattr(args, "slave", None),
            "looks_r": getattr(args, "looks_r", None),
            "looks_a": getattr(args, "looks_a", None),
            "polarization": getattr(args, "polarization", None),
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
    looks_r = int(args.looks_r)
    looks_a = int(args.looks_a)
    coh_threshold = float(args.coh_threshold)

    # 0) 参数前置校验（P0/P1）
    if args.synthetic or not args.input:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <master> --slave <slave>")
        validate_bbox(bbox)
    validate_dinsar_params(looks_r, looks_a, coh_threshold)

    # 1) 获取主从复 SLC（通用契约）
    truth_change = None
    synth_info: Optional[Dict[str, Any]] = None
    input_nodata: Optional[float] = None
    if args.input and not args.synthetic:
        master, file_bbox = read_complex_geotiff(args.input)
        input_nodata = read_nodata(args.input)
        if not args.slave:
            raise UsageError("--slave <raster> is required with --input")
        slave, _ = read_complex_geotiff(args.slave)
        bbox = bbox if bbox is not None else file_bbox
        source_note = args.input
    else:
        master, slave, truth_change, synth_info = generate_synthetic(bbox)
        source_note = "synthetic"

    if master.size == 0:
        raise ValidationError("input raster is empty")

    # 2) bbox + NoData 校验（前置，确保无效输入不创建 output 目录）
    if bbox is not None:
        validate_bbox(bbox)
    n_valid = int(np.count_nonzero(np.isfinite(master)))
    if n_valid == 0:
        raise ValidationError(
            "master SLC has no valid pixels (all NoData/NaN); nothing to analyze"
        )

    # 3) 所有校验通过后才创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 4) 相干性 + 相位
    gamma, phase = complex_coherence(master, slave, looks_r=looks_r, looks_a=looks_a)
    stats = coherence_statistics(gamma, bbox, coh_threshold=coh_threshold)

    # 5) 写出产物
    coh_tif = os.path.join(output_dir, "coherence.tif")
    phase_tif = os.path.join(output_dir, "phase.tif")
    write_geotiff(coh_tif, gamma, bbox, nodata=-9999.0)
    write_geotiff(phase_tif, phase, bbox, nodata=-9999.0)

    stats_path = os.path.join(output_dir, "coherence_statistics.json")
    stats_out = dict(stats)
    stats_out["looks_r"] = looks_r
    stats_out["looks_a"] = looks_a
    stats_out["polarization"] = args.polarization
    stats_out["input_nodata"] = input_nodata
    stats_out["n_valid_pixels"] = n_valid
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats_out, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "mean_coherence": stats["mean_coherence"],
        "low_coherence_fraction": stats["low_coherence_fraction"],
        "looks": [looks_r, looks_a],
        "polarization": args.polarization,
        "n_valid_pixels": n_valid,
        "input_nodata": input_nodata,
    }
    if synth_info is not None:
        qa["synthetic_change_fraction"] = synth_info["change_fraction"]

    outputs = [
        {"path": coh_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": phase_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": stats_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] looks: {looks_r} x {looks_a}  pol: {args.polarization}")
        print(f"[{SKILL_NAME}] mean coherence: {stats['mean_coherence']:.4f}")
        print(f"[{SKILL_NAME}] low-coherence (<{coh_threshold}) fraction: "
              f"{stats['low_coherence_fraction']:.4f}")
        print(f"[{SKILL_NAME}] output: {coh_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="D-InSAR complex coherence and interferometric phase estimation with multi-looking.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="master complex SLC GeoTIFF (2 bands: real, imag)")
    p.add_argument("--slave", help="slave complex SLC GeoTIFF (required with --input)")
    p.add_argument("--looks-r", type=int, default=5,
                   help="number of range looks (window rows, default: 5)")
    p.add_argument("--looks-a", type=int, default=1,
                   help="number of azimuth looks (window cols, default: 1)")
    p.add_argument("--polarization", default="vv", choices=["vv", "vh", "hh", "hv"],
                   help="polarization channel label (default: vv)")
    p.add_argument("--coh-threshold", type=float, default=0.3,
                   help="threshold defining low-coherence area (default: 0.3)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate synthetic master/slave SLCs (offline)")
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
