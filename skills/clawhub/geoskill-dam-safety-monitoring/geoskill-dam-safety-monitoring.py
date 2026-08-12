#!/usr/bin/env python3
"""dam-safety-monitoring — 大坝安全遥感监测

融合多源遥感指标对大坝及其周边进行安全风险评估：

- **InSAR 形变**：坝体沉降 / 位移速率（mm/yr），绝对值越大越危险。
- **NDVI 异常**：渗漏区常出现植被异常（异常繁茂或异常衰退），用与背景的
  偏差绝对值刻画。
- **热红外渗流**：渗流水蒸发导致地表温度异常（通常偏冷），用与背景温度的
  偏差绝对值刻画。
- **水位变化**：库水位快速涨落增加渗透与滑坡风险。

综合风险评分：对各指标归一化到 [0,1] 后加权求和，按阈值分为低 / 中 / 高三级。
高值区经连通域提取并矢量化为异常区域 GeoJSON。

数据源：本地形变栅格，或 ``--synthetic`` 生成含坝体 + 注入沉降/渗流异常区的
模拟场景用于离线测试。

隐私声明 / Privacy：
- 默认离线运行，``--synthetic`` 完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

Usage:
    python dam-safety-monitoring.py --input deformation.tif --output-dir ./out
    python dam-safety-monitoring.py --bbox 116 39 117 40 --synthetic --output-dir ./out

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
SKILL_NAME = "dam-safety-monitoring"

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


# 默认权重（综合风险评分）
DEFAULT_WEIGHTS = {
    "deformation": 0.40,
    "ndvi_anomaly": 0.20,
    "thermal_anomaly": 0.25,
    "water_change": 0.15,
}

# 风险分级阈值
RISK_LEVELS = {"low": 0.33, "high": 0.66}


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")


def validate_bbox(bbox: List[float]) -> List[float]:
    """Validate WGS-84 bbox; raise ValidationError (rc=6) on bad input.

    Rules:
      - W < E, S < N
      - abs values <= 360/180 (allow a small slack for antimeridian wrap)
      - bbox area >= 1e-8 deg^2 (avoid fully zero extent)
    Note: cross-antimeridian (W > 180 or E < -180) is allowed if bbox span is
    explicitly < 360 deg; we still reject *plain* W > E here.
    """
    if bbox is None or len(bbox) != 4:
        raise ValidationError("bbox must be 4 floats: W S E N")
    w, s, e, n = [float(x) for x in bbox]
    if not all(np.isfinite([w, s, e, n])):
        raise ValidationError("bbox values must be finite")
    if w >= e:
        raise ValidationError(
            f"bbox W ({w}) must be < E ({e}); cross-180° antimeridian is not supported — split into two extents"
        )
    if s >= n:
        raise ValidationError(f"bbox S ({s}) must be < N ({n})")
    if not (-360.0 <= w <= 360.0 and -360.0 <= e <= 360.0):
        raise ValidationError("bbox W/E out of range [-360, 360]")
    if not (-90.0 <= s <= 90.0 and -90.0 <= n <= 90.0):
        raise ValidationError("bbox S/N out of range [-90, 90]")
    if (e - w) * (n - s) < 1e-8:
        raise ValidationError("bbox area is effectively zero; widen W/E or S/N")
    return [w, s, e, n]


# ---------------------------------------------------------------------------
# 核心算法
# ---------------------------------------------------------------------------
def normalize_minmax(arr: np.ndarray) -> np.ndarray:
    """把数组线性归一化到 [0,1]。全等值时返回全 0。"""
    arr = np.asarray(arr, dtype=np.float64)
    lo, hi = np.nanmin(arr), np.nanmax(arr)
    if not np.isfinite(lo) or not np.isfinite(hi) or hi - lo < 1e-12:
        return np.zeros_like(arr, dtype=np.float64)
    out = (arr - lo) / (hi - lo)
    return np.nan_to_num(out, nan=0.0, posinf=1.0, neginf=0.0)


def anomaly_magnitude(arr: np.ndarray) -> np.ndarray:
    """异常幅度 = 像元与背景（中值）的偏差绝对值。"""
    arr = np.asarray(arr, dtype=np.float64)
    bg = np.nanmedian(arr)
    return np.abs(arr - bg)


def composite_risk(
    deformation: np.ndarray,
    ndvi: np.ndarray,
    thermal: np.ndarray,
    water_change: np.ndarray,
    weights: Optional[Dict[str, float]] = None,
) -> np.ndarray:
    """综合风险评分（0-1）。

    deformation 用绝对形变速率；ndvi / thermal 用异常幅度；water_change 用
    水位变化幅度。各指标归一化后按权重加权和，再归一化到 [0,1]。
    """
    w = dict(DEFAULT_WEIGHTS)
    if weights:
        w.update(weights)
    total_w = sum(w.values())
    if total_w <= 0:
        raise UsageError("weights must sum to a positive value")

    ind_def = normalize_minmax(np.abs(np.asarray(deformation, dtype=np.float64)))
    ind_ndvi = normalize_minmax(anomaly_magnitude(ndvi))
    ind_therm = normalize_minmax(anomaly_magnitude(thermal))
    ind_water = normalize_minmax(np.abs(np.asarray(water_change, dtype=np.float64)))

    risk = (
        w["deformation"] * ind_def
        + w["ndvi_anomaly"] * ind_ndvi
        + w["thermal_anomaly"] * ind_therm
        + w["water_change"] * ind_water
    ) / total_w
    return np.clip(risk, 0.0, 1.0)


def classify_risk(
    risk: np.ndarray, low: float = RISK_LEVELS["low"], high: float = RISK_LEVELS["high"]
) -> np.ndarray:
    """风险分级：0=低, 1=中, 2=高。"""
    risk = np.asarray(risk, dtype=np.float64)
    cls = np.zeros(risk.shape, dtype=np.int32)
    cls[risk >= low] = 1
    cls[risk >= high] = 2
    return cls


def detect_anomalies(risk: np.ndarray, threshold: float) -> Tuple[np.ndarray, int]:
    """对风险栅格做连通域提取，返回 (labels, n_features)。背景（<threshold）为 0。"""
    from scipy import ndimage

    risk = np.asarray(risk, dtype=np.float64)
    mask = risk >= threshold
    labels, n = ndimage.label(mask, structure=np.ones((3, 3)))
    return labels, int(n)


def polygonize_anomalies(
    risk: np.ndarray, threshold: float, bbox: List[float], min_area_frac: float = 0.0
) -> List[Dict[str, Any]]:
    """把高风险连通域矢量化为 GeoJSON feature 列表。

    每个 feature 带 risk_mean / risk_max / area_deg2 属性。
    min_area_frac：相对整景面积的最小占比，过滤碎斑。
    """
    from rasterio.features import shapes
    from rasterio.transform import from_bounds
    from shapely.geometry import shape

    risk = np.asarray(risk, dtype=np.float64)
    h, w = risk.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    mask = (risk >= threshold).astype(np.uint8)
    total_area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])
    min_area = min_area_frac * total_area

    feats: List[Dict[str, Any]] = []
    from rasterio import features as _rf

    for geom, val in shapes(mask, mask=mask.astype(bool), transform=transform):
        poly = shape(geom)
        area = poly.area
        if area < min_area:
            continue
        # 计算该多边形覆盖像元的风险统计（用栅格化掩膜）
        rast = _rf.rasterize(
            [(geom, 1)], out_shape=(h, w), transform=transform, fill=0, dtype="uint8"
        )
        vals = risk[rast == 1]
        risk_mean = float(np.mean(vals)) if vals.size else float(threshold)
        risk_max = float(np.max(vals)) if vals.size else float(threshold)
        feats.append({
            "type": "Feature",
            "geometry": geom,
            "properties": {
                "risk_mean": round(risk_mean, 4),
                "risk_max": round(risk_max, 4),
                "area_deg2": round(float(area), 8),
            },
        })
    feats.sort(key=lambda f: f["properties"]["risk_max"], reverse=True)
    return feats


def risk_summary(
    risk: np.ndarray, cls: np.ndarray, feats: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """汇总风险统计与等级占比。"""
    risk = np.asarray(risk, dtype=np.float64)
    n = risk.size
    counts = np.bincount(cls.ravel(), minlength=3)
    return {
        "risk_mean": round(float(np.nanmean(risk)), 4),
        "risk_max": round(float(np.nanmax(risk)), 4),
        "level_counts": {
            "low": int(counts[0]), "medium": int(counts[1]), "high": int(counts[2]),
        },
        "level_fraction": {
            "low": round(float(counts[0] / n), 4),
            "medium": round(float(counts[1] / n), 4),
            "high": round(float(counts[2] / n), 4),
        },
        "n_anomaly_polygons": len(feats),
    }


# ---------------------------------------------------------------------------
# 合成数据：含坝体 + 注入沉降 / 渗流异常区（离线测试）
# ---------------------------------------------------------------------------
def generate_synthetic(
    bbox: List[float],
    width: int = 96,
    height: int = 96,
    seed: int = 42,
    inject_anomaly: bool = True,
) -> Tuple[Dict[str, np.ndarray], Dict[str, Any]]:
    """生成大坝安全监测合成场景。

    layers: dem / deformation(mm/yr) / ndvi / thermal(°C) / water_change(m)
    注入一个位于坝体中部偏右的沉降 + 渗流异常区，真值位置记录在 info。
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:height, 0:width]
    yn = yy.astype(np.float64) / max(height - 1, 1)
    xn = xx.astype(np.float64) / max(width - 1, 1)

    # DEM：一条东西向坝体（中部高起的脊），北侧为库区（低）
    dam_ridge = 60.0 * np.exp(-((yn - 0.5) ** 2) / (2 * 0.05 ** 2))
    reservoir = -20.0 * np.clip((0.5 - yn) * 4, 0, 1)  # 北侧库区低洼
    dem = (300.0 + dam_ridge + reservoir + rng.normal(0, 1.0, (height, width))).astype(np.float32)

    # 形变背景：接近 0 的微小形变
    deformation = rng.normal(0, 2.0, (height, width)).astype(np.float64)
    # NDVI 背景：坝体草地 ~0.4
    ndvi = (0.4 + rng.normal(0, 0.03, (height, width)))
    # 热红外背景：~25°C
    thermal = (25.0 + rng.normal(0, 0.3, (height, width)))
    # 水位变化背景：小幅
    water_change = rng.normal(0, 0.2, (height, width))

    truth = None
    if inject_anomaly:
        # 异常区中心（归一化坐标），半径
        cx, cy, r = 0.65, 0.5, 0.10
        blob = ((xn - cx) ** 2 + (yn - cy) ** 2) < r ** 2
        deformation[blob] -= 35.0          # 显著沉降
        ndvi[blob] += 0.35                 # 渗漏导致植被异常繁茂
        thermal[blob] -= 4.0               # 渗流蒸发降温
        water_change[blob] += 1.5          # 局部水位扰动
        truth = {"cx": cx, "cy": cy, "r": r,
                 "lon": bbox[0] + cx * (bbox[2] - bbox[0]),
                 "lat": bbox[3] - cy * (bbox[3] - bbox[1])}

    layers = {
        "dem": dem,
        "deformation": deformation.astype(np.float32),
        "ndvi": np.clip(ndvi, -0.2, 1.0).astype(np.float32),
        "thermal": thermal.astype(np.float32),
        "water_change": water_change.astype(np.float32),
    }
    info = {"bbox": bbox, "width": width, "height": height, "truth": truth}
    return layers, info


# ---------------------------------------------------------------------------
# GeoTIFF I/O
# ---------------------------------------------------------------------------
def write_geotiff(
    path: str, array: np.ndarray, bbox: List[float], nodata: float = -9999.0
) -> None:
    import rasterio
    from rasterio.transform import from_bounds

    if array.ndim == 2:
        array = array[np.newaxis, ...]
    nb, h, w = array.shape
    transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], w, h)
    profile = {
        "driver": "GTiff", "height": h, "width": w, "count": nb,
        "dtype": "float32", "crs": "EPSG:4326", "transform": transform,
        "nodata": nodata, "compress": "deflate",
    }
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with rasterio.open(path, "w", **profile) as dst:
        for b in range(nb):
            dst.write(array[b].astype("float32"), b + 1)


def read_geotiff(path: str) -> Tuple[np.ndarray, List[float]]:
    """Read first band of a GeoTIFF as float32.

    Returns (cube, bbox). NoData is preserved as-is in the array — callers that
    need to mask NoData should use `read_geotiff_full` (NaN-substituted) or
    call `count_valid()` to validate.
    """
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
    return cube, bbox


def read_geotiff_full(path: str) -> Tuple[np.ndarray, List[float], float]:
    """Read first band with NoData replaced by NaN; returns (cube, bbox, nodata)."""
    import rasterio
    if not os.path.exists(path):
        raise UsageError(f"input raster not found: {path}", path=path)
    with rasterio.open(path) as src:
        cube = src.read().astype(np.float32)
        b = src.bounds
        bbox = [b.left, b.bottom, b.right, b.top]
        nodata = src.nodata
    if nodata is not None and np.isfinite(nodata):
        cube = np.where(cube == nodata, np.nan, cube)
    return cube, bbox, (float(nodata) if nodata is not None else float("nan"))


def count_valid(arr: np.ndarray) -> int:
    """Number of pixels with a finite, non-NaN value."""
    a = np.asarray(arr)
    return int(np.sum(np.isfinite(a)))


# ---------------------------------------------------------------------------
# 主管线
# ---------------------------------------------------------------------------
def run_model(
    deformation: np.ndarray, ndvi: np.ndarray, thermal: np.ndarray,
    water_change: np.ndarray, bbox: List[float],
    weights: Optional[Dict[str, float]] = None,
    threshold: float = 0.5, min_area_frac: float = 0.001,
) -> Tuple[np.ndarray, np.ndarray, List[Dict[str, Any]], Dict[str, Any]]:
    """执行综合风险评估，返回 (risk, cls, feats, summary)。"""
    risk = composite_risk(deformation, ndvi, thermal, water_change, weights)
    cls = classify_risk(risk)
    feats = polygonize_anomalies(risk, threshold, bbox, min_area_frac=min_area_frac)
    summary = risk_summary(risk, cls, feats)
    summary["threshold"] = float(threshold)
    summary["weights"] = weights or dict(DEFAULT_WEIGHTS)
    return risk.astype(np.float32), cls, feats, summary


def validate_params(args: argparse.Namespace) -> None:
    """Validate CLI parameters; raise UsageError (rc=2) on bad CLI input,
    ValidationError (rc=6) on bad value choices."""
    if not (0.0 <= float(args.threshold) <= 1.0):
        raise ValidationError(
            f"--threshold must be in [0, 1]; got {args.threshold}"
        )
    if not (0.0 <= float(args.min_area_frac) <= 1.0):
        raise ValidationError(
            f"--min-area-frac must be in [0, 1]; got {args.min_area_frac}"
        )
    if int(args.width) < 2 or int(args.height) < 2:
        raise UsageError(
            f"--width/--height must be >= 2; got {args.width}x{args.height}"
        )


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
        inputs={
            "input": getattr(args, "input", None),
            "bbox": bbox,
            "synthetic": bool(getattr(args, "synthetic", False)),
            "threshold": getattr(args, "threshold", None),
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

    # ---- Phase 1: CLI value validation (BEFORE makedirs) ----
    validate_params(args)

    bbox = list(args.bbox) if args.bbox else None
    if bbox is not None:
        bbox = validate_bbox(bbox)

    # ---- Phase 2: input source decision ----
    input_nodata: float = float("nan")
    synth_info: Optional[Dict[str, Any]] = None
    if args.input and not args.synthetic:
        cube, file_bbox, input_nodata = read_geotiff_full(args.input)
        bbox = bbox if bbox is not None else file_bbox
        bbox = validate_bbox(bbox)
        deformation = cube[0] if cube.ndim == 3 else cube
        if deformation.size == 0:
            raise ValidationError("input raster is empty")
        n_valid = count_valid(deformation)
        if n_valid == 0:
            raise ValidationError(
                f"input raster has no valid pixels (nodata={input_nodata}); check the source data"
            )
        h, w = deformation.shape
        layers, synth_info = generate_synthetic(bbox, width=w, height=h, inject_anomaly=False)
        layers["deformation"] = deformation.astype(np.float32)
        source_note = args.input
    else:
        if bbox is None:
            raise UsageError("provide --bbox (synthetic mode) or --input <raster>")
        layers, synth_info = generate_synthetic(
            bbox, width=args.width, height=args.height, inject_anomaly=not args.no_anomaly,
        )
        source_note = "synthetic"

    # ---- Phase 3: create output dir (after all validation passes) ----
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    n_valid_def = count_valid(layers["deformation"])

    try:
        risk, cls, feats, summary = run_model(
            layers["deformation"], layers["ndvi"], layers["thermal"],
            layers["water_change"], bbox, threshold=args.threshold,
            min_area_frac=args.min_area_frac,
        )
    except Exception as exc:  # noqa: BLE001
        raise ProcessError(f"dam safety analysis failed: {exc}") from exc

    out_tif = os.path.join(output_dir, "deformation_rate.tif")
    write_geotiff(out_tif, layers["deformation"], bbox)
    risk_tif = os.path.join(output_dir, "composite_risk.tif")
    write_geotiff(risk_tif, risk, bbox)

    anomaly_geojson = os.path.join(output_dir, "anomaly_zones.geojson")
    with open(anomaly_geojson, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": feats},
                  f, ensure_ascii=False, indent=2)

    summary_path = os.path.join(output_dir, "risk_assessment.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    qa: Dict[str, Any] = {
        "source": source_note,
        "input_nodata": input_nodata,
        "n_valid_pixels": int(n_valid_def),
        "risk_mean": summary["risk_mean"],
        "risk_max": summary["risk_max"],
        "level_fraction": summary["level_fraction"],
        "n_anomaly_polygons": summary["n_anomaly_polygons"],
        "threshold": summary["threshold"],
    }

    outputs = [
        {"path": out_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": risk_tif, "kind": "raster", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "band_count": 1},
        {"path": anomaly_geojson, "kind": "vector", "crs_epsg": 4326,
         "bbox_wgs84": bbox, "feature_count": len(feats)},
        {"path": summary_path, "kind": "json"},
    ]

    man_path = write_manifest(output_dir, args, outputs, qa, started_at, 0, bbox)

    if not args.quiet:
        print(f"[{SKILL_NAME}] source: {source_note}")
        print(f"[{SKILL_NAME}] risk mean={qa['risk_mean']:.3f}  max={qa['risk_max']:.3f}")
        print(f"[{SKILL_NAME}] high-risk fraction: {qa['level_fraction']['high']:.3%}")
        print(f"[{SKILL_NAME}] anomaly polygons: {qa['n_anomaly_polygons']}")
        print(f"[{SKILL_NAME}] output: {risk_tif}")
        if man_path:
            print(f"[{SKILL_NAME}] manifest: {man_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog=SKILL_NAME,
        description="Multi-source dam safety risk assessment (InSAR deformation + NDVI + thermal + water level).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                   help="geographic extent [minLon minLat maxLon maxLat]")
    p.add_argument("--input", help="input deformation-rate GeoTIFF (mm/yr, band 1)")
    p.add_argument("--synthetic", action="store_true",
                   help="generate a synthetic dam scene with injected anomalies (offline)")
    p.add_argument("--width", type=int, default=96, help="synthetic raster width (default 96)")
    p.add_argument("--height", type=int, default=96, help="synthetic raster height (default 96)")
    p.add_argument("--threshold", type=float, default=0.5,
                   help="composite risk threshold for anomaly extraction (default 0.5)")
    p.add_argument("--min-area-frac", type=float, default=0.001,
                   help="min anomaly polygon area as fraction of scene (default 0.001)")
    p.add_argument("--no-anomaly", action="store_true",
                   help="synthetic mode: do not inject an anomaly (baseline)")
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
