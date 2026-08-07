#!/usr/bin/env python3
"""volcanic-hazard-assessment — 火山灾害评估

融合多源观测评估火山活动等级：

- **热红外异常**：亮温相对基线的正异常（岩浆/热液活动）
- **InSAR 形变**：地表隆起/沉降速率（岩浆补给）
- **SO₂ 柱浓度**：脱气强度（喷发前兆）
- **历史喷发新近度**：距上次喷发越近，背景活动性越高

综合为 [0,1] 活动度评分（加权求和），再切成 0–4 级（正常/关注/警示/警告/极端）。

数据源：本地多波段 GeoTIFF（band1=亮温K、band2=形变速率mm/yr、band3=SO₂柱浓度DU），
或 ``--synthetic`` 生成火山场景。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python volcanic-hazard-assessment.py --input volcano.tif --years-since 12
    python volcanic-hazard-assessment.py --bbox 120 30 121 31 --synthetic --output-dir ./out

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
SKILL_NAME = "volcanic-hazard-assessment"

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


ACTIVITY_LABELS = ["normal", "advisory", "watch", "warning", "extreme"]


def validate_bbox(bbox):
    """Validate WGS-84 bbox. Returns (W, S, E, N) as floats.

    Rules:
      - 4 numeric values
      - -180 <= W, E <= 180; -90 <= S, N <= 90
      - W < E (no antimeridian crossing; split into two bboxes if needed)
      - S < N
      - width / height strictly positive
    Raises ValidationError (exit 6) on any failure.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError(f"bbox must be 4 floats [W S E N], got: {bbox}")
    w, s, e, n = (float(v) for v in bbox)
    for label, val, lo, hi in (("W", w, -180.0, 180.0), ("E", e, -180.0, 180.0),
                               ("S", s, -90.0, 90.0), ("N", n, -90.0, 90.0)):
        if val < lo or val > hi:
            raise ValidationError(
                f"bbox {label}={val} out of range [{lo}, {hi}]; got bbox={bbox}"
            )
    if w >= e:
        raise ValidationError(
            f"bbox W={w} must be < E={e} (no antimeridian crossing; "
            f"if needed, split into two bboxes)"
        )
    if s >= n:
        raise ValidationError(
            f"bbox S={s} must be < N={n}"
        )
    if (e - w) < 1e-9 or (n - s) < 1e-9:
        raise ValidationError(
            f"bbox has zero or negative area: width={e - w:.3e}, height={n - s:.3e}"
        )
    return w, s, e, n


def validate_years_since(y):
    """years-since must be a finite non-negative number."""
    try:
        v = float(y)
    except (TypeError, ValueError):
        raise ValidationError(f"years-since must be numeric, got: {y!r}")
    if v != v or v in (float("inf"), float("-inf")):
        raise ValidationError(f"years-since must be finite, got: {v}")
    if v < 0:
        raise ValidationError(f"years-since must be >= 0, got: {v}")
    return v


def validate_recency_tau(tau):
    """recency-tau must be a finite positive number (avoid div-by-zero)."""
    try:
        v = float(tau)
    except (TypeError, ValueError):
        raise ValidationError(f"recency-tau must be numeric, got: {tau!r}")
    if v != v or v in (float("inf"), float("-inf")):
        raise ValidationError(f"recency-tau must be finite, got: {v}")
    if v <= 0:
        raise ValidationError(
            f"recency-tau must be > 0 (avoid div-by-zero), got: {v}"
        )
    return v


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def normalize01(arr: np.ndarray) -> np.ndarray:
    a = np.asarray(arr, dtype=np.float64)
    finite = a[np.isfinite(a)]
    if finite.size == 0:
        return np.zeros_like(a, dtype=np.float32)
    lo, hi = float(finite.min()), float(finite.max())
    if hi - lo <= 1e-12:
        return np.zeros_like(a, dtype=np.float32)
    out = np.where(np.isfinite(a), (a - lo) / (hi - lo), 0.0)
    return out.astype(np.float32)


def thermal_anomaly_index(brightness_temp: np.ndarray, baseline: float) -> np.ndarray:
    """热红外异常指数：亮温相对基线的正异常，归一化到 [0,1]。

    只保留正异常（升温），负异常视为无热活动。
    """
    anom = np.clip(np.asarray(brightness_temp, dtype=np.float64) - float(baseline), 0.0, None)
    return normalize01(anom)


def deformation_index(rate_mm_yr: np.ndarray) -> np.ndarray:
    """形变指数：地表隆起/沉降速率绝对幅度的归一化（[0,1]）。"""
    return normalize01(np.abs(np.asarray(rate_mm_yr, dtype=np.float64)))


def so2_index(column_du: np.ndarray) -> np.ndarray:
    """SO₂ 柱浓度指数：归一化到 [0,1]（越高脱气越强）。"""
    return normalize01(np.clip(np.asarray(column_du, dtype=np.float64), 0.0, None))


def eruption_recency(years_since: float, tau: float = 50.0) -> float:
    """历史喷发新近度：exp(-years/tau) ∈ (0,1]，越近越高。"""
    if years_since < 0:
        raise ValidationError("years_since must be >= 0")
    return float(np.exp(-float(years_since) / float(tau)))


def activity_score(thermal: np.ndarray, deformation: np.ndarray, so2: np.ndarray,
                   recency: float,
                   weights: Tuple[float, float, float, float] = (0.35, 0.25, 0.25, 0.15)) -> np.ndarray:
    """火山活动度评分（[0,1]）：四个 [0,1] 分量的加权和（权重归一）。

    对每个分量单调不减；全部为零时评分 = 0。
    """
    w = np.asarray(weights, dtype=np.float64)
    if np.any(w < 0):
        raise ValidationError("weights must be non-negative")
    wsum = float(w.sum())
    if wsum <= 1e-12:
        raise ValidationError("sum of weights must be positive")
    th = np.asarray(thermal, dtype=np.float64)
    df = np.asarray(deformation, dtype=np.float64)
    so = np.asarray(so2, dtype=np.float64)
    if not (th.shape == df.shape == so.shape):
        raise ValidationError("thermal/deformation/so2 shape mismatch")
    rec = float(np.clip(recency, 0.0, 1.0))
    score = (w[0] * th + w[1] * df + w[2] * so + w[3] * rec) / wsum
    return np.clip(score, 0.0, 1.0).astype(np.float32)


def classify_activity(score: np.ndarray, breaks: Tuple[float, ...] = (0.2, 0.4, 0.6, 0.8)) -> np.ndarray:
    """活动度分级：0=normal … 4=extreme。"""
    return np.digitize(np.asarray(score, dtype=np.float64), list(breaks)).astype(np.int16)


# ---------------------------------------------------------------------------
# 合成数据：火山场景（热异常中心 + 形变隆起 + SO₂ 烟羽）
# ---------------------------------------------------------------------------
def generate_synthetic(bbox: List[float], width: int = 64, height: int = 64,
                       baseline: float = 290.0, seed: int = 42) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    xn = xx.astype(np.float64) / max(width - 1, 1)
    yn = yy.astype(np.float64) / max(height - 1, 1)
    cx, cy = 0.5, 0.45
    r2 = (xn - cx) ** 2 + (yn - cy) ** 2
    # 亮温：背景 baseline，火山口热异常 +60K
    bt = baseline + 60.0 * np.exp(-r2 / (2 * 0.08 ** 2)) + rng.normal(0, 1.0, (height, width))
    # 形变速率：火山口隆起 +120 mm/yr，向外衰减
    deform = 120.0 * np.exp(-r2 / (2 * 0.12 ** 2)) + rng.normal(0, 2.0, (height, width))
    # SO₂ 烟羽：向下风方向（东）拖尾
    so2 = 800.0 * np.exp(-(((xn - 0.55) ** 2) / (2 * 0.15 ** 2) + (yn - cy) ** 2 / (2 * 0.06 ** 2)))
    so2 = np.clip(so2 + rng.normal(0, 5.0, so2.shape), 0.0, None)
    layers = {"brightness_temp": bt.astype(np.float32),
              "deformation": deform.astype(np.float32),
              "so2": so2.astype(np.float32)}
    info = {"bbox": bbox, "width": width, "height": height, "baseline": baseline,
            "max_bt": float(bt.max())}
    return layers, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(path: str, cube: np.ndarray, bbox: List[float],
                  nodata: float = -9999.0, dtype: str = "float32") -> None:
    import rasterio
    from rasterio.transform import from_bounds
    if cube.ndim == 2:
        cube = cube[np.newaxis, ...]
    nb, h, w = cube.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {"driver": "GTiff", "height": h, "width": w, "count": nb,
               "dtype": dtype, "crs": "EPSG:4326", "transform": transform,
               "nodata": nodata, "compress": "deflate"}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(cube[b].astype(dtype), b + 1)


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
def write_manifest(output_dir: str, inputs: Dict[str, Any], outputs: List[Dict[str, Any]],
                   qa: Dict[str, Any], started_at: str, exit_code: int) -> Optional[str]:
    if OutputManifest is None:
        return None
    cmd = " ".join([SKILL_NAME] + sys.argv[1:])
    man = OutputManifest(
        skill=SKILL_NAME, skill_version=VERSION, command=cmd,
        started_at=started_at, finished_at=_utc_now(), exit_code=exit_code,
        inputs=inputs, outputs=[OutputFile(**o) for o in outputs], qa=qa,
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

    # ---- P0/P1: validate bbox, years_since, recency_tau BEFORE mkdir ----
    if bbox is not None:
        bbox = list(validate_bbox(bbox))
    args.years_since = validate_years_since(args.years_since)
    args.recency_tau = validate_recency_tau(args.recency_tau)

    os.makedirs(output_dir, exist_ok=True)

    if args.input and not args.synthetic:
        cube, file_bbox = read_geotiff(args.input)
        bbox = bbox if bbox is not None else file_bbox
        if cube.shape[0] < 3:
            raise ValidationError("input needs >=3 bands (brightness_temp, deformation, so2)")
        bt, deform, so2 = cube[0], cube[1], cube[2]
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        layers, _info = generate_synthetic(bbox, baseline=args.baseline)
        bt, deform, so2 = layers["brightness_temp"], layers["deformation"], layers["so2"]
        source_note = "synthetic"

    th = thermal_anomaly_index(bt, args.baseline)
    df = deformation_index(deform)
    so = so2_index(so2)
    rec = eruption_recency(args.years_since, tau=args.recency_tau)
    score = activity_score(th, df, so, rec)
    level = classify_activity(score)

    score_tif = os.path.join(output_dir, "activity_score.tif")
    write_geotiff(score_tif, score, bbox)
    level_tif = os.path.join(output_dir, "activity_level.tif")
    write_geotiff(level_tif, level.astype("int16"), bbox, nodata=-1, dtype="int16")

    params = {"source": source_note, "baseline": args.baseline,
              "years_since": args.years_since, "recency": rec,
              "recency_tau": args.recency_tau, "labels": ACTIVITY_LABELS}
    params_path = os.path.join(output_dir, "volcano_params.json")
    with open(params_path, "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    level_frac = {ACTIVITY_LABELS[i]: float(np.mean(level == i)) for i in range(len(ACTIVITY_LABELS))}
    qa: Dict[str, Any] = {
        "source": source_note,
        "mean_score": float(np.mean(score)),
        "max_score": float(np.max(score)),
        "recency": rec,
        "level_fraction": level_frac,
        "alert_fraction": float(np.mean(level >= 3)),
    }
    outputs = [
        {"path": score_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": level_tif, "kind": "raster", "crs_epsg": 4326, "bbox_wgs84": bbox, "band_count": 1},
        {"path": params_path, "kind": "json"},
    ]
    man_path = write_manifest(output_dir, {"input": args.input, "bbox": bbox,
                              "years_since": args.years_since, "synthetic": bool(args.synthetic)},
                              outputs, qa, started_at, 0)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] recency: {rec:.3f}  mean score: {qa['mean_score']:.4f}  max: {qa['max_score']:.4f}")
        print(f"[{SKILL_NAME}] alert fraction (>=warning): {qa['alert_fraction']:.3f}")
        print(f"[{SKILL_NAME}] outputs: {output_dir}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Volcanic hazard assessment (thermal + InSAR + SO2 + eruption recency).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    p.add_argument("--input", help="input GeoTIFF (band1=brightness_temp K, band2=deformation mm/yr, band3=SO2 DU)")
    p.add_argument("--baseline", type=float, default=290.0, help="background brightness temperature (K, default: 290)")
    p.add_argument("--years-since", type=float, default=20.0, help="years since last eruption (default: 20)")
    p.add_argument("--recency-tau", type=float, default=50.0, help="recency decay timescale (yr, default: 50)")
    p.add_argument("--synthetic", action="store_true")
    p.add_argument("--output-dir", default="./output")
    p.add_argument("--quiet", action="store_true")
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
