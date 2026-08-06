#!/usr/bin/env python3
"""sar-backscatter-analysis — SAR后向散射分析

对多时相 SAR 后向散射（σ⁰）时序做逐像元统计刻画，是长时间序列 SAR 应用
（物候监测、变化检测、时序分类）的基础步骤。对每个极化通道沿时间轴计算：

- **mean**：时序均值（平均后向散射水平）
- **std**：时序标准差（时间变异性）
- **amplitude**：振幅 ``max - min``（季节动态幅度）
- **cv**：变异系数 ``std / mean``（相对变异性，量纲无关）

并计算极化比 ``ratio = mean(VV) / mean(VH)``，反映散射机制差异（体散射
/ 双反弹射）。

数据源：本地多时相 σ⁰ GeoTIFF（波段按 ``[pol1_t1..tT, pol2_t1..tT]``
排列），或使用 ``--synthetic`` 生成含植被物候正弦信号（VV/VH 不同相位与
幅度）加噪声的时序立方体。

隐私声明 / Privacy：
- 默认完全离线运行，不发起任何网络请求。
- ``--synthetic`` 模式不读取任何外部数据。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python sar-backscatter-analysis.py --input ts.tif --n-dates 6 --polarization vv,vh
    python sar-backscatter-analysis.py --bbox 116 39 117 40 --synthetic --n-dates 8

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
SKILL_NAME = "sar-backscatter-analysis"

VALID_POLS = ("vv", "vh", "hh", "hv")

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


def parse_polarization(spec: str) -> List[str]:
    """解析 ``--polarization vv,vh`` 字符串为极化列表。"""
    pols = [p.strip().lower() for p in spec.split(",") if p.strip()]
    if not pols:
        raise UsageError("--polarization must list at least one channel", spec=spec)
    bad = [p for p in pols if p not in VALID_POLS]
    if bad:
        raise UsageError(
            f"invalid polarization(s) {bad}. Choose from: {list(VALID_POLS)}",
            spec=spec,
        )
    return pols


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def temporal_stats(cube: np.ndarray) -> Dict[str, np.ndarray]:
    """沿时间轴（axis=0）的逐像元统计。

    输入 (T, H, W)，返回 dict: mean/std/amplitude/cv，各为 (H, W) float32。
    ``cv = std / mean``（mean 接近 0 时置 0，避免除零）。
    """
    cube = np.asarray(cube, dtype=np.float32)
    if cube.ndim != 3:
        raise ValidationError(
            f"time-series cube must be 3-D (T,H,W), got shape {cube.shape}",
            shape=list(cube.shape),
        )
    eps = 1e-9
    mean = cube.mean(axis=0)
    std = cube.std(axis=0)
    amplitude = cube.max(axis=0) - cube.min(axis=0)
    cv = np.where(np.abs(mean) > eps, std / np.where(np.abs(mean) > eps, mean, 1.0), 0.0)
    return {
        "mean": mean.astype(np.float32),
        "std": std.astype(np.float32),
        "amplitude": amplitude.astype(np.float32),
        "cv": cv.astype(np.float32),
    }


def polarization_ratio(vv_mean: np.ndarray, vh_mean: np.ndarray) -> np.ndarray:
    """极化比 ``VV / VH``（均值为负或接近 0 时置 0）。"""
    vv_mean = np.asarray(vv_mean, dtype=np.float32)
    vh_mean = np.asarray(vh_mean, dtype=np.float32)
    eps = 1e-9
    ratio = np.where(vh_mean > eps, vv_mean / np.where(vh_mean > eps, vh_mean, 1.0), 0.0)
    return ratio.astype(np.float32)


def region_mean_timeseries(cube: np.ndarray) -> List[float]:
    """逐时相的区域（空间）均值曲线。输入 (T,H,W)，返回长度 T 的列表。"""
    cube = np.asarray(cube, dtype=np.float32)
    return [float(cube[t].mean()) for t in range(cube.shape[0])]


def build_stats_cube(
    cubes: Dict[str, np.ndarray],
    pols: List[str],
) -> Tuple[np.ndarray, List[str]]:
    """把各极化通道的统计堆叠为多波段输出立方体。

    波段顺序：``[pol_mean, pol_std, pol_amplitude, pol_cv] × n_pols``，
    当同时存在 vv 与 vh 时追加一个 ``vv_vh_ratio`` 波段。
    返回 (cube (B,H,W), band_names)。
    """
    bands: List[np.ndarray] = []
    names: List[str] = []
    for pol in pols:
        st = temporal_stats(cubes[pol])
        for key in ("mean", "std", "amplitude", "cv"):
            bands.append(st[key])
            names.append(f"{pol}_{key}")
    if "vv" in cubes and "vh" in cubes:
        ratio = polarization_ratio(
            temporal_stats(cubes["vv"])["mean"],
            temporal_stats(cubes["vh"])["mean"],
        )
        bands.append(ratio)
        names.append("vv_vh_ratio")
    return np.stack(bands, axis=0), names


# ---------------------------------------------------------------------------
# 合成数据：植被物候正弦信号 + 噪声的多时相 σ⁰ 立方体
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    n_dates: int = 6,
    pols: Optional[List[str]] = None,
    width: int = 64,
    height: int = 64,
    seed: int = 42,
) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    """生成各极化通道的 (T, H, W) σ⁰ 立方体（线性强度）。

    每个通道：空间基底 × (1 + 季节振幅·sin(2π(t/T + 相位))) + 高斯噪声。
    VV 季节动态强（植被物候），VH 较弱且相位滞后。返回 (cubes_dict, info)。
    """
    if pols is None:
        pols = ["vv", "vh"]
    if n_dates < 2:
        raise UsageError(f"--n-dates must be >= 2, got {n_dates}", n_dates=int(n_dates))
    rng = np.random.default_rng(seed)

    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    yn = yy / max(height - 1, 1)
    xn = xx / max(width - 1, 1)
    # 空间纹理（平滑变化的地物基底）
    texture = 0.8 + 0.4 * np.exp(-(((xn - 0.4) ** 2 + (yn - 0.6) ** 2) / 0.05))

    # 各极化的物理参数（线性 σ⁰ 量级 + 季节相对振幅 + 相位）
    pol_params = {
        "vv": {"base": 0.05, "season_frac": 0.6, "phase": 0.0, "noise": 0.004},
        "vh": {"base": 0.012, "season_frac": 0.4, "phase": 0.25, "noise": 0.0015},
        "hh": {"base": 0.04, "season_frac": 0.5, "phase": 0.1, "noise": 0.004},
        "hv": {"base": 0.010, "season_frac": 0.35, "phase": 0.3, "noise": 0.0015},
    }

    t = np.arange(n_dates, dtype=np.float32) / float(n_dates)
    cubes: Dict[str, np.ndarray] = {}
    truth_season: Dict[str, float] = {}
    for pol in pols:
        p = pol_params[pol]
        seasonal = 1.0 + p["season_frac"] * np.sin(2.0 * np.pi * (t + p["phase"]))
        cube = np.empty((n_dates, height, width), dtype=np.float32)
        for i in range(n_dates):
            field = p["base"] * texture * seasonal[i]
            field = field + rng.normal(0.0, p["noise"], size=(height, width)).astype(np.float32)
            cube[i] = np.clip(field, 1e-4, None)
        cubes[pol] = cube
        truth_season[pol] = p["season_frac"]

    dates = [
        (_dt.date(2024, 1, 1) + _dt.timedelta(days=12 * i)).isoformat()
        for i in range(n_dates)
    ]
    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "n_dates": int(n_dates),
        "polarizations": list(pols),
        "dates": dates,
        "truth_season_fraction": truth_season,
    }
    return cubes, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O（直接用 rasterio，保证离线可用）
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str,
    cube: np.ndarray,
    bbox: List[float],
    nodata: float = -9999.0,
    band_names: Optional[List[str]] = None,
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
            if band_names and b < len(band_names):
                dst.set_band_description(b + 1, band_names[b])


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_full(path: str) -> Tuple[np.ndarray, List[float], Optional[float]]:
    """扩展版 read：同时返回 nodata 值（若无则为 None）。"""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
        if nodata is not None:
            nodata = float(nodata)
    return cube, bbox, nodata


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Optional[List[float]]) -> List[float]:
    """校验地理 bbox 合法性，失败抛 ValidationError（exit 6）。"""
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats [W S E N]")
    try:
        w, s, e, n = [float(x) for x in bbox]
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"bbox entries must be numeric: {exc}")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError(f"latitude out of [-90,90]: S={s}, N={n}")
    if not (-180.0 <= w <= 180.0 and -180.0 <= e <= 180.0):
        raise ValidationError(f"longitude out of [-180,180]: W={w}, E={e}")
    if s >= n:
        raise ValidationError(
            f"S >= N (S={s}, N={n}); bbox inverted (S must be < N)"
        )
    if w >= e:
        raise ValidationError(
            f"W >= E (W={w}, E={e}); cross-180° bbox not supported. "
            f"Split into two non-antipodal bboxes."
        )
    if (e - w) < 0.001 or (n - s) < 0.001:
        raise ValidationError(
            f"bbox too small ({(e-w):.6f}°×{(n-s):.6f}°); min span is 0.001°"
        )
    return [w, s, e, n]


def cube_from_input(data: np.ndarray, pols: List[str]) -> Dict[str, np.ndarray]:
    """把输入波段立方体解释为各极化时序。

    若波段数能被极化数整除，按 ``[pol_t1..tT, ...]`` 均分；否则全部波段
    归入第一个极化通道。
    """
    nb = data.shape[0]
    n_pols = len(pols)
    cubes: Dict[str, np.ndarray] = {}
    if nb >= n_pols and nb % n_pols == 0:
        t = nb // n_pols
        for i, pol in enumerate(pols):
            cubes[pol] = data[i * t: (i + 1) * t]
    else:
        cubes[pols[0]] = data
    return cubes


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
    input_nodata: Optional[float] = None,
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
            "n_dates": getattr(args, "n_dates", None),
            "polarization": getattr(args, "polarization", None),
            "synthetic": bool(getattr(args, "synthetic", False)),
            "input_nodata": input_nodata,
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
    pols = parse_polarization(args.polarization)

    # 校验 CLI 参数（前置）
    if args.n_dates < 2:
        raise ValidationError(
            f"--n-dates must be >= 2 (got {args.n_dates})"
        )

    # 1) 获取时序立方体
    synth_info: Optional[Dict[str, Any]] = None
    input_nodata: Optional[float] = None
    n_valid_pixels: Optional[int] = None
    if args.input and not args.synthetic:
        data, file_bbox, src_nodata = read_geotiff_full(args.input)
        input_nodata = src_nodata
        if bbox is not None:
            bbox = validate_bbox(bbox)
        else:
            bbox = validate_bbox(file_bbox)
        # NoData 处理
        if src_nodata is not None:
            n_total = int(data[0].size)
            n_nd = int(np.count_nonzero(data[0] == src_nodata))
            n_valid_pixels = n_total - n_nd
            if n_valid_pixels == 0:
                raise ValidationError(
                    f"input raster has no valid pixels "
                    f"(all {n_nd}/{n_total} are NoData={src_nodata})",
                    path=args.input, nodata=src_nodata,
                )
            data = np.where(data == src_nodata, np.nan, data).astype(np.float32)
        else:
            n_valid_pixels = int(data[0].size)
        cubes = cube_from_input(data, pols)
        dates = [f"date_{i}" for i in range(cubes[pols[0]].shape[0])]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        bbox = validate_bbox(bbox)
        cubes, synth_info = generate_synthetic(bbox, n_dates=args.n_dates, pols=pols)
        dates = synth_info["dates"]
        n_valid_pixels = int(next(iter(cubes.values())).size)
        source_note = "synthetic"

    for pol, c in cubes.items():
        if c.size == 0:
            raise ValidationError(f"polarization '{pol}' cube is empty")
        if c.shape[0] < 2:
            raise ValidationError(
                f"polarization '{pol}' needs >= 2 dates, got {c.shape[0]}",
                dates=int(c.shape[0]),
            )

    # 校验通过后再建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 2) 逐极化统计 + 堆叠
    stats_cube, band_names = build_stats_cube(cubes, pols)

    # 3) 写出产物
    out_tif = os.path.join(output_dir, "backscatter_stats.tif")
    write_geotiff(out_tif, stats_cube, bbox, band_names=band_names)

    timeseries = {pol: region_mean_timeseries(cubes[pol]) for pol in cubes}
    ts_payload = {
        "dates": dates,
        "polarizations": list(cubes.keys()),
        "region_mean_timeseries": timeseries,
        "band_names": band_names,
    }
    ts_path = os.path.join(output_dir, "timeseries.json")
    with open(ts_path, "w", encoding="utf-8") as f:
        json.dump(ts_payload, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "polarizations": list(cubes.keys()),
        "n_dates": int(cubes[pols[0]].shape[0]),
        "n_output_bands": int(stats_cube.shape[0]),
        "band_names": band_names,
        "n_valid_pixels": int(n_valid_pixels) if n_valid_pixels is not None else None,
        "input_nodata": input_nodata,
        "overall_mean_backscatter": float(np.mean([
            np.nanmean(cubes[p]) if np.any(np.isfinite(cubes[p])) else 0.0
            for p in cubes
        ])),
    }
    if synth_info is not None:
        qa["synthetic_truth_season_fraction"] = synth_info["truth_season_fraction"]

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(stats_cube.shape[0])},
        {"path": ts_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox,
                              input_nodata=input_nodata)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] polarizations: {list(cubes.keys())}  n_dates: {cubes[pols[0]].shape[0]}")
        print(f"[{SKILL_NAME}] output bands ({len(band_names)}): {band_names}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        print(f"[{SKILL_NAME}] timeseries: {ts_path}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Multi-temporal SAR backscatter time-series statistics and polarization ratio.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="multi-temporal backscatter GeoTIFF")
    p.add_argument("--n-dates", type=int, default=6,
                   help="number of acquisition dates (synthetic, default: 6)")
    p.add_argument("--polarization", default="vv,vh",
                   help="comma-separated polarizations, e.g. vv,vh (default: vv,vh)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a physics-consistent synthetic time series (offline)")
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
