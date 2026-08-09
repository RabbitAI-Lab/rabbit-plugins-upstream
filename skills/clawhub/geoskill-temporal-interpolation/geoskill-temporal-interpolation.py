#!/usr/bin/env python3
"""temporal-interpolation — 时序插值与重建

对 NDVI（或同类植被指数）时序做时间平滑/插值，重建无云污染的规则
时间序列，用于物候曲线平滑、月度产品生成与云污染 NDVI 重建。

算法：
- **savgol**：Savitzky-Golay 滤波（``scipy.signal.savgol_filter``），
  在时间维（axis=0）滑动多项式拟合，保形去噪，可整立方体向量化；
- **spline**：平滑样条（``scipy.interpolate.UnivariateSpline``），
  逐像元在时间维拟合三次平滑样条并在原格点求值。

输出：平滑后时序 GeoTIFF（多时相波段，每日期一波段）+ 平滑参数 JSON
（含平滑前后逐日期均值，用于评估重建效果）。

数据源：本地多时相 GeoTIFF（波段=日期），或使用 ``--synthetic`` 生成
含噪声物候曲线（温带单峰 + 云污染负偏差）的模拟时序用于离线验证。

隐私声明 / Privacy：
- 默认离线运行，仅在显式 ``--place`` 解析地名时才会访问 Nominatim/Open-Meteo。
- ``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python temporal-interpolation.py --input ndvi_series.tif --method savgol
    python temporal-interpolation.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "temporal-interpolation"

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
# Input validation
# ---------------------------------------------------------------------------
def validate_bbox(bbox: Any) -> None:
    """Validate a W,S,E,N geographic bbox. Raises ValidationError on bad input."""
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValidationError(
            f"bbox must be [W,S,E,N] (4 floats), got {bbox!r}",
            bbox=list(bbox) if hasattr(bbox, "__iter__") else None,
        )
    W, S, E, N = bbox
    for v, name in [(W, "W"), (S, "S"), (E, "E"), (N, "N")]:
        try:
            fv = float(v)
        except (TypeError, ValueError):
            raise ValidationError(
                f"bbox {name}={v!r} is not a finite number", bbox=list(bbox),
            )
        if not np.isfinite(fv):
            raise ValidationError(
                f"bbox {name}={v!r} is not a finite number", bbox=list(bbox),
            )
    if not (-180.0 <= float(W) <= 180.0 and -180.0 <= float(E) <= 180.0):
        raise ValidationError(
            f"bbox longitude out of range [-180,180]: W={W}, E={E}", bbox=list(bbox),
        )
    if not (-90.0 <= float(S) <= 90.0 and -90.0 <= float(N) <= 90.0):
        raise ValidationError(
            f"bbox latitude out of range [-90,90]: S={S}, N={N}", bbox=list(bbox),
        )
    if float(W) >= float(E) and not (float(W) > 170.0 and float(E) < -170.0):
        raise ValidationError(
            f"bbox has W >= E ({W} >= {E}); crossing the antimeridian "
            f"(W near +180, E near -180) is not supported. "
            f"Pass a bbox with W < E (e.g. split into two bboxes).",
            bbox=list(bbox),
        )
    if float(W) > 170.0 and float(E) < -170.0:
        raise ValidationError(
            f"bbox crosses the antimeridian (W={W}, E={E}); not supported. "
            f"Split into two bboxes: [{W}, {S}, 180.0, {N}] and [-180.0, {S}, {E}, {N}].",
            bbox=list(bbox),
        )
    if float(S) >= float(N):
        raise ValidationError(
            f"bbox has S >= N ({S} >= {N}); south must be strictly less than north.",
            bbox=list(bbox),
        )
    if (float(E) - float(W)) < 1e-4 or (float(N) - float(S)) < 1e-4:
        raise ValidationError(
            f"bbox is too small (extent < 1e-4 degrees): W={W},S={S},E={E},N={N}.",
            bbox=list(bbox),
        )


def validate_params(n_dates: int, window: int, smoothing: Optional[float]) -> None:
    """Cross-check CLI params beyond argparse type coercion."""
    if not isinstance(n_dates, int) or n_dates < 2:
        raise ValidationError(
            f"n-dates must be a positive int (>= 2 for smoothing), got {n_dates!r}",
            n_dates=n_dates,
        )
    if n_dates > 366:
        raise ValidationError(
            f"n-dates {n_dates} implausibly large (max 366 = daily)", n_dates=n_dates,
        )
    if not isinstance(window, int) or window < 3:
        raise ValidationError(
            f"--window must be a positive odd int >= 3, got {window!r}", window=window,
        )
    if window > 365:
        raise ValidationError(
            f"--window {window} implausibly large (max 365 = yearly)", window=window,
        )
    if window % 2 == 0:
        raise ValidationError(
            f"--window must be odd (Savitzky-Golay requirement), got {window}",
            window=window,
        )
    if smoothing is not None:
        if not isinstance(smoothing, (int, float)) or not np.isfinite(smoothing):
            raise ValidationError(
                f"--smoothing must be a finite number, got {smoothing!r}",
                smoothing=smoothing,
            )
        if smoothing < 0:
            raise ValidationError(
                f"--smoothing must be >= 0, got {smoothing}", smoothing=smoothing,
            )


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def phenology_curve(n_dates: int) -> np.ndarray:
    """理想温带单峰物候 NDVI 曲线（冬季低 ~0.2，夏季高 ~0.8）。"""
    t = np.linspace(0.0, 1.0, n_dates)
    seasonal = 0.5 - 0.5 * np.cos(2.0 * np.pi * t)  # t=0.5 处最大
    return (0.2 + 0.6 * seasonal).astype(np.float64)


def _savgol_window(n_dates: int, requested: int) -> Tuple[int, int]:
    """返回合法的 (window_length, polyorder)。window 须为奇数且 <= n。"""
    wl = min(requested, n_dates)
    if wl % 2 == 0:
        wl -= 1
    wl = max(3, wl)
    if wl > n_dates:  # n_dates 很小（<3）时退化
        wl = n_dates if n_dates % 2 == 1 else n_dates - 1
        wl = max(wl, 1)
    polyorder = min(2, wl - 1)
    return int(wl), int(polyorder)


def smooth_timeseries(
    cube: np.ndarray,
    method: str = "savgol",
    window_length: int = 5,
    polyorder: int = 2,
    smoothing: Optional[float] = None,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """对 (n_dates, H, W) 时序立方体沿时间维平滑。

    返回 (smoothed_cube, params)。
    """
    n, h, w = cube.shape
    if n < 2:
        raise ValidationError("need at least 2 dates to smooth a time series",
                              n_dates=int(n))

    if method == "savgol":
        from scipy.signal import savgol_filter
        wl, po = _savgol_window(n, window_length)
        if wl < 3 or wl > n:
            raise ValidationError(
                f"savgol needs >=3 dates, got {n}", n_dates=int(n))
        smoothed = savgol_filter(cube.astype(np.float64), wl, po, axis=0)
        params = {"method": "savgol", "window_length": wl, "polyorder": po}

    elif method == "spline":
        from scipy.interpolate import UnivariateSpline
        x = np.arange(n, dtype=np.float64)
        s = float(smoothing) if smoothing is not None else 0.1 * n
        smoothed = np.empty_like(cube, dtype=np.float64)
        for i in range(h):
            for j in range(w):
                y = cube[:, i, j].astype(np.float64)
                if np.allclose(y, y[0]):  # 常数序列，样条会报错
                    smoothed[:, i, j] = y
                    continue
                spl = UnivariateSpline(x, y, k=3, s=s)
                smoothed[:, i, j] = spl(x)
        params = {"method": "spline", "smoothing_factor": s, "k": 3}

    else:
        raise UsageError(f"unknown method '{method}'. Choose savgol or spline",
                         method=method)

    # NDVI 物理范围裁剪
    smoothed = np.clip(smoothed, -1.0, 1.0).astype(np.float32)
    return smoothed, params


def series_rmse(a: np.ndarray, b: np.ndarray) -> float:
    """两个 (n_dates, H, W) 立方体的整体 RMSE。"""
    return float(np.sqrt(np.mean((a - b) ** 2)))


# ---------------------------------------------------------------------------
# 合成数据：物候曲线 + 云污染噪声（离线验证）
# ---------------------------------------------------------------------------
def generate_synthetic_cube(
    bbox: List[float],
    n_dates: int = 12,
    width: int = 32,
    height: int = 32,
    seed: int = 42,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """生成 (n_dates, H, W) 含噪声 NDVI 时序。

    真值 = 物候曲线 × 空间调制；观测 = 真值 + 高斯噪声 + 云污染负偏差。
    info 中含 clean（无噪声）立方体用于验证平滑效果。
    """
    rng = np.random.default_rng(seed)
    curve = phenology_curve(n_dates)  # (n_dates,)

    yy, xx = np.mgrid[0:height, 0:width]
    xx = xx.astype(np.float64) / max(width - 1, 1)
    yy = yy.astype(np.float64) / max(height - 1, 1)
    # 空间调制：振幅与基线随位置缓变
    amp = 0.9 + 0.2 * xx
    base = 0.05 * yy

    clean = np.zeros((n_dates, height, width), dtype=np.float64)
    for t in range(n_dates):
        clean[t] = np.clip(curve[t] * amp + base, 0.0, 1.0)

    # 高斯噪声
    noise = rng.normal(0, 0.03, clean.shape)
    # 云污染：随机像元-日期出现负偏差（云使 NDVI 偏低）
    cloud = rng.random(clean.shape) < 0.15
    cloud_drop = np.where(cloud, rng.uniform(0.1, 0.35, clean.shape), 0.0)

    noisy = clean + noise - cloud_drop
    noisy = np.clip(noisy, -1.0, 1.0).astype(np.float32)
    clean = np.clip(clean, -1.0, 1.0).astype(np.float32)

    info = {
        "bbox": bbox,
        "width": width,
        "height": height,
        "n_dates": n_dates,
        "clean": clean,
        "phenology_mean": curve.tolist(),
    }
    return noisy, info


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
            "method": getattr(args, "method", None),
            "n_dates": getattr(args, "n_dates", None),
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

    # ---- Validate CLI / params up front (no filesystem side effects yet) ----
    validate_params(args.n_dates, args.window, args.smoothing)
    bbox = list(args.bbox) if args.bbox else None

    # 1) 获取数据立方体（通用契约）
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if args.bbox is not None:
            validate_bbox(bbox)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        validate_bbox(bbox)
        cube, synth_info = generate_synthetic_cube(bbox, n_dates=args.n_dates)
        source_note = "synthetic"

    if cube.size == 0:
        raise ValidationError("input raster is empty")

    # ---- All validation passed — safe to create output directory ----
    os.makedirs(output_dir, exist_ok=True)

    # 2) 时序平滑
    smoothed, params = smooth_timeseries(
        cube, method=args.method,
        window_length=args.window, smoothing=args.smoothing,
    )

    # 3) 写出产物
    out_tif = os.path.join(output_dir, "smoothed_series.tif")
    write_geotiff(out_tif, smoothed, bbox)

    mean_before = [float(np.mean(cube[t])) for t in range(cube.shape[0])]
    mean_after = [float(np.mean(smoothed[t])) for t in range(smoothed.shape[0])]
    params_doc = {
        **params,
        "n_dates": int(cube.shape[0]),
        "mean_ndvi_per_date_before": mean_before,
        "mean_ndvi_per_date_after": mean_after,
    }
    params_path = os.path.join(output_dir, "smoothing_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params_doc, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "method": args.method,
        "n_dates": int(cube.shape[0]),
        "overall_mean_before": float(np.mean(cube)),
        "overall_mean_after": float(np.mean(smoothed)),
    }
    if synth_info is not None:
        clean = synth_info["clean"]
        qa["rmse_noisy_vs_clean"] = series_rmse(cube, clean)
        qa["rmse_smoothed_vs_clean"] = series_rmse(smoothed, clean)

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": int(smoothed.shape[0])},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] method: {args.method}  dates: {cube.shape[0]}")
        print(f"[{SKILL_NAME}] mean NDVI before: {qa['overall_mean_before']:.4f}")
        print(f"[{SKILL_NAME}] mean NDVI after:  {qa['overall_mean_after']:.4f}")
        if "rmse_smoothed_vs_clean" in qa:
            print(f"[{SKILL_NAME}] RMSE noisy->clean:    {qa['rmse_noisy_vs_clean']:.4f}")
            print(f"[{SKILL_NAME}] RMSE smoothed->clean: {qa['rmse_smoothed_vs_clean']:.4f}")
        print(f"[{SKILL_NAME}] output: {out_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Temporal smoothing/interpolation of NDVI time series (Savitzky-Golay / spline).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input multi-temporal GeoTIFF (band = date)")
    p.add_argument("--n-dates", type=int, default=12,
                   help="number of dates for synthetic series (default: 12)")
    p.add_argument("--method", default="savgol", choices=["savgol", "spline"],
                   help="smoothing method (default: savgol)")
    p.add_argument("--window", type=int, default=5,
                   help="Savitzky-Golay window length, odd (default: 5)")
    p.add_argument("--smoothing", type=float, default=None,
                   help="spline smoothing factor s (default: 0.1 * n_dates)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a noisy phenology time series (offline)")
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
