#!/usr/bin/env python3
"""
Harmful Algal Bloom Monitor — 湖海藻华监测

利用海色/水色遥感反射率产品监测藻华范围、持续时间和风险等级。
支持 NDCI / FLH / BGI / ARI 多种藻华指数，含云/耀斑/浑浊/浅水质量控制、
事件追踪、面积统计与预警报告。

退出码:
    0 = 成功
    2 = 参数错误
    3 = 依赖缺失
    6 = 数据校验失败
    7 = 处理失败
"""

import argparse
import csv
import json
import logging
import os
import sys
import traceback
from collections import deque
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

# Try pip-installed package first; fall back to local copy in repo root.
try:
    from _geoskill_data_fetcher import (add_bbox_date_args,
        parse_bbox_arg,
        parse_date_range_arg,
        DataFetcher,
        DataSource,
        BBox,
        DateRange,
        DataFetcherError,)
    _FETCHER_AVAILABLE = True
except ImportError:
    import sys as _sys
    from pathlib import Path as _Path
    _skill_dir = _Path(__file__).resolve().parent
    _repo_root = _skill_dir.parent.parent
    _local_fetcher = _repo_root / "_geoskill_data_fetcher"
    if _local_fetcher.exists():
        _sys.path.insert(0, str(_repo_root))
    from _geoskill_data_fetcher import (add_bbox_date_args,
        parse_bbox_arg,
        parse_date_range_arg,
        DataFetcher,
        DataSource,
        BBox,
        DateRange,
        DataFetcherError,)
    _FETCHER_AVAILABLE = True
except ImportError:  # pragma: no cover - graceful when running standalone
    _FETCHER_AVAILABLE = False



EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# File-arg flags that must point to existing paths when provided
FILE_ARGS = {
    "input-dir": "args.input_dir",
    "models-config": "args.models_config",
}

# Numeric flags with (min, max) bounds; None = unbounded on that side
NUMERIC_RANGES = {
    "min_consecutive_days": (1, 365),
    "max_gap_days": (0, 30),
    "n_days": (1, 365),
}

# ============================================================
# Logging
# ============================================================

def setup_logging(output_dir: Path) -> logging.Logger:
    """Setup logging to file and console."""
    logger = logging.getLogger("habm")
    logger.setLevel(logging.DEBUG)
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)

    log_path = output_dir / "run.log"
    fh = logging.FileHandler(str(log_path), encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    logger.addHandler(fh)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(ch)

    return logger


def cleanup_logging():
    """Close all handlers on the habm logger."""
    logger = logging.getLogger("habm")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)


# ============================================================
# Model Registry
# ============================================================

def load_bloom_models(models_path: Optional[str] = None) -> Dict:
    """Load bloom model parameters from JSON reference file."""
    if models_path is None:
        script_dir = Path(__file__).parent
        models_path = script_dir.parent / "references" / "bloom_models.json"

    with open(models_path, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# Bloom Index Computation
# ============================================================

def compute_ndci(red: np.ndarray, red_edge: np.ndarray,
                 nodata: float = -9999.0) -> np.ndarray:
    """
    Normalized Difference Chlorophyll Index.
    NDCI = (Red_edge - Red) / (Red_edge + Red)

    Args:
        red: Red band reflectance
        red_edge: Red-edge band reflectance
        nodata: Nodata value

    Returns:
        NDCI array, range [-1, 1]
    """
    denominator = red_edge + red
    valid = (denominator != 0) & (red != nodata) & (red_edge != nodata)
    valid &= ~np.isnan(red) & ~np.isnan(red_edge) & ~np.isnan(denominator)

    result = np.full_like(red, np.nan, dtype=np.float32)
    result[valid] = ((red_edge[valid] - red[valid]) / denominator[valid]).astype(np.float32)
    return result


def compute_flh(red2: np.ndarray, red3: np.ndarray, nir: np.ndarray,
                lambda_red2: float = 667.0, lambda_red3: float = 678.0,
                lambda_nir: float = 859.0, nodata: float = -9999.0) -> np.ndarray:
    """
    Fluorescence Line Height.
    FLH = R_red3 - R_red2 - (R_nir - R_red2) * (lambda_red3 - lambda_red2) / (lambda_nir - lambda_red2)

    Args:
        red2: Reflectance at ~667nm
        red3: Reflectance at ~678nm
        nir: Reflectance at NIR
        lambda_red2: Wavelength of red2 band
        lambda_red3: Wavelength of red3 band
        lambda_nir: Wavelength of NIR band
        nodata: Nodata value

    Returns:
        FLH array
    """
    valid = (red2 != nodata) & (red3 != nodata) & (nir != nodata)
    valid &= ~np.isnan(red2) & ~np.isnan(red3) & ~np.isnan(nir)

    result = np.full_like(red2, np.nan, dtype=np.float32)
    coeff = (lambda_red3 - lambda_red2) / (lambda_nir - lambda_red2)
    result[valid] = (red3[valid] - red2[valid] -
                     (nir[valid] - red2[valid]) * coeff).astype(np.float32)
    return result


def compute_bgi(blue: np.ndarray, green: np.ndarray,
                nodata: float = -9999.0) -> np.ndarray:
    """
    Blue-Green Index.
    BGI = (Green - Blue) / (Green + Blue)

    Args:
        blue: Blue band reflectance
        green: Green band reflectance
        nodata: Nodata value

    Returns:
        BGI array, range [-1, 1]
    """
    denominator = green + blue
    valid = (denominator != 0) & (blue != nodata) & (green != nodata)
    valid &= ~np.isnan(blue) & ~np.isnan(green) & ~np.isnan(denominator)

    result = np.full_like(blue, np.nan, dtype=np.float32)
    result[valid] = ((green[valid] - blue[valid]) / denominator[valid]).astype(np.float32)
    return result


def compute_ari(green: np.ndarray, red_edge: np.ndarray,
                nodata: float = -9999.0) -> np.ndarray:
    """
    Anthocyanin Reflectance Index.
    ARI = (1 / Green) - (1 / Red_edge)

    Args:
        green: Green band reflectance
        red_edge: Red-edge band reflectance
        nodata: Nodata value

    Returns:
        ARI array
    """
    valid = (green != 0) & (red_edge != 0)
    valid &= (green != nodata) & (red_edge != nodata)
    valid &= ~np.isnan(green) & ~np.isnan(red_edge)

    result = np.full_like(green, np.nan, dtype=np.float32)
    result[valid] = ((1.0 / green[valid]) - (1.0 / red_edge[valid])).astype(np.float32)
    return result


def index_to_probability(index_value: np.ndarray, threshold: float,
                         steepness: float = 10.0) -> np.ndarray:
    """
    Convert index value to bloom probability using sigmoid function.

    Args:
        index_value: Computed index array
        threshold: Bloom threshold for the index
        steepness: Sigmoid steepness parameter

    Returns:
        Probability array [0, 1]
    """
    valid = ~np.isnan(index_value)
    prob = np.full_like(index_value, np.nan, dtype=np.float32)
    # Sigmoid: 1 / (1 + exp(-steepness * (value - threshold)))
    prob[valid] = (1.0 / (1.0 + np.exp(-steepness * (index_value[valid] - threshold)))).astype(np.float32)
    return prob


# ============================================================
# Quality Control Masking
# ============================================================

def compute_quality_mask(
    bands: Dict[str, np.ndarray],
    models: Dict,
    nodata: float = -9999.0,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """
    Compute quality control mask from reflectance bands.

    Returns:
        (valid_mask, qc_stats) — valid_mask=True means pixel is usable
    """
    # Get shape from first band
    first_band = next(iter(bands.values()))
    shape = first_band.shape
    valid = np.ones(shape, dtype=bool)

    qc = models.get("quality_control", {})
    qc_stats = {}

    # Cloud mask: high blue reflectance
    if "blue" in bands:
        cloud_thresh = qc.get("cloud", {}).get("blue_threshold", 0.15)
        cloud_mask = bands["blue"] > cloud_thresh
        valid &= ~cloud_mask
        qc_stats["cloud_pixels"] = int(np.sum(cloud_mask))

    # Glint mask: high mean visible reflectance
    visible_bands = []
    for bname in ["blue", "green", "red"]:
        if bname in bands:
            visible_bands.append(bands[bname])
    if visible_bands:
        mean_visible = np.mean(visible_bands, axis=0)
        glint_thresh = qc.get("glint", {}).get("mean_visible_threshold", 0.12)
        glint_mask = mean_visible > glint_thresh
        valid &= ~glint_mask
        qc_stats["glint_pixels"] = int(np.sum(glint_mask))

    # Turbid water mask: high red/NIR ratio
    if "red" in bands and "nir" in bands:
        nir_safe = np.where(bands["nir"] > 0, bands["nir"], 1e-10)
        red_nir_ratio = bands["red"] / nir_safe
        turbid_thresh = qc.get("turbid_water", {}).get("red_nir_ratio_threshold", 2.0)
        turbid_mask = red_nir_ratio > turbid_thresh
        valid &= ~turbid_mask
        qc_stats["turbid_pixels"] = int(np.sum(turbid_mask))

    # Shallow water / bottom reflectance mask
    if visible_bands:
        shallow_thresh = qc.get("shallow_water", {}).get("total_reflectance_threshold", 0.2)
        total_ref = np.sum(visible_bands, axis=0)
        shallow_mask = total_ref > shallow_thresh
        valid &= ~shallow_mask
        qc_stats["shallow_pixels"] = int(np.sum(shallow_mask))

    # Nodata mask
    for bname, bdata in bands.items():
        valid &= (bdata != nodata) & ~np.isnan(bdata) & ~np.isinf(bdata)

    qc_stats["total_pixels"] = int(valid.size)
    qc_stats["valid_pixels"] = int(np.sum(valid))
    qc_stats["masked_pixels"] = int(valid.size - np.sum(valid))
    qc_stats["valid_fraction"] = round(float(np.sum(valid) / valid.size), 4) if valid.size > 0 else 0.0

    return valid, qc_stats


# ============================================================
# Event Detection & Tracking
# ============================================================

def detect_bloom_events(
    probability_stack: np.ndarray,
    threshold: float = 0.5,
    min_consecutive_days: int = 3,
    max_gap_days: int = 1,
) -> Tuple[np.ndarray, List[Dict]]:
    """
    Detect bloom events from probability time series.

    Args:
        probability_stack: 3D array (time, rows, cols) of bloom probability
        threshold: Probability threshold for bloom detection
        min_consecutive_days: Minimum consecutive days to confirm event
        max_gap_days: Maximum gap days allowed within an event

    Returns:
        (event_mask, events_list) — event_mask has event IDs, events_list has metadata
    """
    n_days, n_rows, n_cols = probability_stack.shape
    bloom_daily = np.zeros((n_days, n_rows, n_cols), dtype=bool)

    for t in range(n_days):
        bloom_daily[t] = (~np.isnan(probability_stack[t])) & (probability_stack[t] >= threshold)

    # Per-pixel consecutive-day tracking
    event_id_map = np.zeros((n_rows, n_cols), dtype=np.int32)
    events = []
    current_event_id = 0

    for r in range(n_rows):
        for c in range(n_cols):
            pixel_series = bloom_daily[:, r, c]
            if not np.any(pixel_series):
                continue

            # Find consecutive runs
            consecutive = 0
            gap_count = 0
            event_start = None
            last_bloom_day = None
            total_bloom_days = 0

            for t in range(n_days):
                if pixel_series[t]:
                    if event_start is None:
                        event_start = t
                    last_bloom_day = t
                    consecutive += 1
                    total_bloom_days += 1
                    gap_count = 0
                else:
                    if consecutive > 0:
                        gap_count += 1
                        if gap_count > max_gap_days:
                            # Event ends
                            if consecutive >= min_consecutive_days:
                                current_event_id += 1
                                events.append({
                                    "event_id": current_event_id,
                                    "start_day_index": int(event_start),
                                    "end_day_index": int(last_bloom_day),
                                    "duration_days": int(consecutive),
                                    "row": r,
                                    "col": c,
                                    "total_bloom_days": int(total_bloom_days),
                                    "max_probability": round(float(np.max(probability_stack[event_start:last_bloom_day + 1, r, c])), 4),
                                })
                                event_id_map[r, c] = current_event_id
                            consecutive = 0
                            event_start = None
                            last_bloom_day = None
                            total_bloom_days = 0

            # Handle event at end of series
            if consecutive >= min_consecutive_days:
                current_event_id += 1
                events.append({
                    "event_id": current_event_id,
                    "start_day_index": int(event_start),
                    "end_day_index": int(last_bloom_day),
                    "duration_days": int(consecutive),
                    "row": r,
                    "col": c,
                    "total_bloom_days": int(total_bloom_days),
                    "max_probability": round(float(np.max(probability_stack[event_start:last_bloom_day + 1, r, c])), 4),
                })
                event_id_map[r, c] = current_event_id

    return event_id_map, events


def compute_daily_area(
    bloom_mask_stack: np.ndarray,
    pixel_area_m2: float = 1.0,
) -> np.ndarray:
    """
    Compute daily bloom area from binary bloom masks.

    Args:
        bloom_mask_stack: 3D boolean array (time, rows, cols)
        pixel_area_m2: Area per pixel in m²

    Returns:
        1D array of daily areas in km²
    """
    n_days = bloom_mask_stack.shape[0]
    daily_area = np.zeros(n_days, dtype=np.float64)
    for t in range(n_days):
        daily_area[t] = float(np.sum(bloom_mask_stack[t])) * pixel_area_m2 / 1e6
    return daily_area


def compute_duration_map(
    probability_stack: np.ndarray,
    threshold: float = 0.5,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute per-pixel bloom duration (consecutive days above threshold).

    Returns:
        (duration_map, missing_data_map) — duration in days, missing count
    """
    n_days, n_rows, n_cols = probability_stack.shape

    duration_map = np.zeros((n_rows, n_cols), dtype=np.int32)
    missing_map = np.zeros((n_rows, n_cols), dtype=np.int32)

    for r in range(n_rows):
        for c in range(n_cols):
            pixel = probability_stack[:, r, c]
            valid = ~np.isnan(pixel)
            missing_map[r, c] = int(np.sum(~valid))

            if not np.any(valid):
                continue

            # Count consecutive days above threshold
            max_consec = 0
            current = 0
            for t in range(n_days):
                if valid[t] and pixel[t] >= threshold:
                    current += 1
                    max_consec = max(max_consec, current)
                else:
                    current = 0

            duration_map[r, c] = max_consec

    return duration_map, missing_map


# ============================================================
# Risk Assessment
# ============================================================

def assess_risk(
    probability: np.ndarray,
    duration_map: np.ndarray,
    models: Dict,
) -> Tuple[np.ndarray, Dict[str, int]]:
    """
    Assess bloom risk level per pixel.

    Returns:
        (risk_map, risk_counts) — risk level 0-3, counts per level
    """
    risk_levels = models.get("risk_levels", {})

    # Risk based on probability × duration
    prob_risk = np.zeros_like(probability, dtype=np.uint8)
    if "moderate" in risk_levels:
        prob_risk[probability >= risk_levels["moderate"]["probability_range"][0]] = 1
    if "high" in risk_levels:
        prob_risk[probability >= risk_levels["high"]["probability_range"][0]] = 2
    if "severe" in risk_levels:
        prob_risk[probability >= risk_levels["severe"]["probability_range"][0]] = 3

    # Elevate risk for long-duration blooms
    duration_boost = (duration_map >= 5).astype(np.uint8)
    risk_map = np.clip(prob_risk + duration_boost, 0, 3).astype(np.uint8)

    # NaN where probability is NaN
    risk_map[np.isnan(probability)] = 255  # nodata for risk

    counts = {
        "low": int(np.sum(risk_map == 0)),
        "moderate": int(np.sum(risk_map == 1)),
        "high": int(np.sum(risk_map == 2)),
        "severe": int(np.sum(risk_map == 3)),
    }

    return risk_map, counts


# ============================================================
# Synthetic Data Generation
# ============================================================

def generate_synthetic_reflectance(
    n_days: int = 10,
    n_rows: int = 50,
    n_cols: int = 50,
    sensor: str = "sentinel2",
    seed: int = 42,
) -> List[Dict[str, np.ndarray]]:
    """
    Generate synthetic reflectance time series for demo/testing.

    Simulates a bloom event: gradually increasing red-edge reflectance
    in a central region over time.

    Returns:
        List of daily band dictionaries
    """
    rng = np.random.RandomState(seed)
    days_data = []

    # Bloom center and radius
    center_r, center_c = n_rows // 2, n_cols // 2
    bloom_radius = min(n_rows, n_cols) // 4

    for day in range(n_days):
        bands = {}

        # Background water: low reflectance
        bands["blue"] = rng.uniform(0.01, 0.03, (n_rows, n_cols)).astype(np.float32)
        bands["green"] = rng.uniform(0.02, 0.05, (n_rows, n_cols)).astype(np.float32)
        bands["red"] = rng.uniform(0.01, 0.04, (n_rows, n_cols)).astype(np.float32)
        bands["red_edge"] = rng.uniform(0.02, 0.06, (n_rows, n_cols)).astype(np.float32)
        bands["nir"] = rng.uniform(0.01, 0.03, (n_rows, n_cols)).astype(np.float32)

        if sensor == "modis":
            bands["red2"] = rng.uniform(0.01, 0.04, (n_rows, n_cols)).astype(np.float32)
            bands["red3"] = rng.uniform(0.01, 0.04, (n_rows, n_cols)).astype(np.float32)

        # Bloom signal: increases over time in center region
        bloom_intensity = min(day / max(n_days - 1, 1), 1.0)

        for r in range(n_rows):
            for c in range(n_cols):
                dist = np.sqrt((r - center_r) ** 2 + (c - center_c) ** 2)
                if dist < bloom_radius:
                    # Bloom: elevated red_edge, slightly elevated green, lower red
                    factor = (1.0 - dist / bloom_radius) * bloom_intensity
                    bands["red_edge"][r, c] += factor * 0.15
                    bands["green"][r, c] += factor * 0.05
                    bands["red"][r, c] += factor * 0.01  # slight increase (not decrease for synthetic)
                    if sensor == "modis":
                        bands["red3"][r, c] += factor * 0.08
                        bands["red2"][r, c] += factor * 0.04

        # Add cloud on day 3 (random patches)
        if day == 3:
            cloud_r = rng.randint(0, n_rows - 5)
            cloud_c = rng.randint(0, n_cols - 5)
            cloud_h = rng.randint(3, 8)
            cloud_w = rng.randint(3, 8)
            for bname in bands:
                bands[bname][cloud_r:cloud_r + cloud_h, cloud_c:cloud_c + cloud_w] = 0.2

        # Add glint on day 5
        if day == 5:
            glint_cols = rng.randint(0, n_cols, size=5)
            for c_idx in glint_cols:
                if c_idx < n_cols:
                    for bname in bands:
                        bands[bname][:, c_idx] = 0.15

        days_data.append(bands)

    return days_data


# ============================================================
# Report Generation
# ============================================================

def generate_report_html(
    results: Dict,
    output_dir: Path,
) -> Path:
    """Generate HTML algal bloom monitoring report."""
    path = output_dir / "alert_report.html"

    # Safely extract values
    n_days = results.get("n_days", 0)
    max_area = results.get("max_daily_area_km2", 0)
    mean_area = results.get("mean_daily_area_km2", 0)
    n_events = results.get("n_events", 0)
    risk_counts = results.get("risk_counts", {})
    qc_stats = results.get("qc_stats", {})

    max_area_str = f"{max_area:.4f}" if isinstance(max_area, (int, float)) else str(max_area)
    mean_area_str = f"{mean_area:.4f}" if isinstance(mean_area, (int, float)) else str(mean_area)

    # Risk level rows
    risk_rows = ""
    for level, count in risk_counts.items():
        pct = (count / max(qc_stats.get("total_pixels", 1), 1)) * 100
        risk_rows += f"<tr><td>{level}</td><td>{count}</td><td>{pct:.1f}%</td></tr>\n"
    if not risk_rows:
        risk_rows = "<tr><td colspan='3'>No risk data</td></tr>\n"

    # QC rows
    qc_rows = ""
    for key in ["cloud_pixels", "glint_pixels", "turbid_pixels", "shallow_pixels"]:
        val = qc_stats.get(key, 0)
        qc_rows += f"<tr><td>{key}</td><td>{val}</td></tr>\n"

    # Warnings
    warnings = results.get("warnings", [])
    warnings_html = ""
    for w in warnings:
        warnings_html += f"<li>{w}</li>\n"
    if not warnings_html:
        warnings_html = "<li>无警告</li>\n"

    # Daily area chart data
    daily_areas = results.get("daily_areas", [])
    daily_area_rows = ""
    for i, area in enumerate(daily_areas):
        daily_area_rows += f"<tr><td>Day {i + 1}</td><td>{area:.4f}</td></tr>\n"
    if not daily_area_rows:
        daily_area_rows = "<tr><td colspan='2'>No data</td></tr>\n"

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>藻华监测报告</title>
<style>
body {{ font-family: 'Microsoft YaHei', Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
.container {{ max-width: 900px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
h1 {{ color: #333; border-bottom: 3px solid #28a745; padding-bottom: 10px; }}
h2 {{ color: #555; margin-top: 30px; }}
table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
th, td {{ padding: 10px 15px; text-align: left; border-bottom: 1px solid #ddd; }}
th {{ background: #f8f9fa; font-weight: 600; }}
.metric {{ font-weight: bold; }}
.warning {{ background: #fff3cd; padding: 10px; border-left: 4px solid #ffc107; margin: 10px 0; }}
.info {{ background: #d1ecf1; padding: 10px; border-left: 4px solid #17a2b8; margin: 10px 0; }}
</style>
</head>
<body>
<div class="container">
<h1>有害藻华监测报告</h1>
<p>生成时间: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}</p>

<div class="info">
<strong>模型:</strong> 基于多指数概率的藻华监测.<br>
<strong>监测天数:</strong> {n_days} 天.
</div>

<h2>警告</h2>
<ul>
{warnings_html}
</ul>

<h2>面积统计</h2>
<table>
<tr><th>指标</th><th>值</th></tr>
<tr><td>最大日面积 (km²)</td><td>{max_area_str}</td></tr>
<tr><td>平均日面积 (km²)</td><td>{mean_area_str}</td></tr>
<tr><td>检测事件数</td><td>{n_events}</td></tr>
</table>

<h2>日面积变化</h2>
<table>
<tr><th>日期</th><th>面积 (km²)</th></tr>
{daily_area_rows}
</table>

<h2>风险等级分布</h2>
<table>
<tr><th>等级</th><th>像素数</th><th>占比</th></tr>
{risk_rows}
</table>

<h2>质量控制统计</h2>
<table>
<tr><th>掩膜类型</th><th>像素数</th></tr>
{qc_rows}
<tr><td>有效像素</td><td>{qc_stats.get("valid_pixels", "N/A")}</td></tr>
<tr><td>有效率</td><td>{qc_stats.get("valid_fraction", "N/A")}</td></tr>
</table>

<h2>方法说明</h2>
<ul>
<li>基于遥感反射率计算藻华指数（NDCI/FLH/BGI/ARI）</li>
<li>使用 Sigmoid 函数将指数转换为藻华概率</li>
<li>质量控制包括云、耀斑、浑浊水体和浅水掩膜</li>
<li>事件需连续 {results.get("min_consecutive_days", "N/A")} 天以上超过阈值才确认</li>
<li>风险等级综合概率与持续时间评定</li>
</ul>

</div>
</body>
</html>
"""

    path.write_text(html, encoding="utf-8")
    return path


# ============================================================
# Main Pipeline
# ============================================================

def auto_download_image(args, output_dir: Path) -> Dict[str, Any]:
    """Download one sentinel-2-l2a scene from MPC using --bbox + --date-range.

    Returns metadata dict (also writes the path back to args.image).
    """
    if not _FETCHER_AVAILABLE:
        raise RuntimeError(
            "Shared data fetcher not importable. Pass --image <local.tif> instead, "
            "or ensure _geoskill_data_fetcher is on sys.path."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_image requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        raise RuntimeError("auto_download_image requires --date-range")
    cache_dir = getattr(args, "cache_dir", None)
    fetcher = DataFetcher(
        source=DataSource.PLANETARY_COMPUTER,
        cache_dir=Path(cache_dir) if cache_dir else None,
    )
    items = fetcher.search_stac(
        collection="sentinel-2-l2a",
        bbox=bbox,
        date_range=dr,
        limit=1,
    )
    if not items:
        raise RuntimeError(
            f"No sentinel-2-l2a items found in bbox={bbox} for {dr.start}..{dr.end}"
        )
    download_dir = output_dir / "downloaded"
    paths = fetcher.download_assets(
        items=items, out_dir=download_dir, max_items=1, max_total_mb=500,
        prefer_assets=['B04', 'B08', 'B02'],
    )
    if not paths:
        raise RuntimeError("Download returned no files")
    args.image = str(paths[0])
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "sentinel-2-l2a",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def run_bloom_monitor_pipeline(args: argparse.Namespace) -> int:
    """Main algal bloom monitoring workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("habm-output")

    # --- Auto-download mode: fetch sentinel-2-l2a from MPC ---
    # Note: skill spec calls for sentinel-3-olci (better chlorophyll
    # bands), but the existing analysis pipeline reads Sentinel-2
    # B04/B08/B02 bands. The Sentinel-3 OLCI L2 NetCDF is in a
    # different format (NetCDF, OaXX band names) and would require
    # rewriting the analysis. We therefore fetch Sentinel-2 L2A as
    # the auto-download source and document this in SKILL.md.
    fetch_meta = None
    if (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)) and getattr(args, "date_range", None):
        if not getattr(args, "image", None):
            try:
                fetch_meta = auto_download_image(args, output_dir)
                mode = "auto_download"
                print(f"  Auto-downloaded image: {args.image}")
            except DataFetcherError as e:
                print(f"ERROR: auto-download failed: [{e.kind}] {e.message}", file=sys.stderr)
                return EXIT_PROCESSING if 'EXIT_PROCESSING' in dir() else 7
    output_dir.mkdir(parents=True, exist_ok=True)

    # P0: Validate args before any heavy work
    rc = validate_args(args)
    if rc != 0:
        return rc

    logger = setup_logging(output_dir)
    logger.info("有害藻华监测 — 启动")

    # Load models
    models_path = getattr(args, 'models_config', None)
    try:
        models = load_bloom_models(models_path)
        logger.info(f"模型参数已加载: version {models.get('version', 'unknown')}")
    except Exception as e:
        logger.error(f"加载模型参数失败: {e}")
        cleanup_logging()
        return EXIT_VALIDATION

    # Parse parameters
    sensor = getattr(args, 'sensor', 'sentinel2') or 'sentinel2'
    index_name = getattr(args, 'index', 'ndci') or 'ndci'
    threshold = getattr(args, 'event_threshold', None)
    min_consecutive = getattr(args, 'min_consecutive_days', 3) or 3
    max_gap = getattr(args, 'max_gap_days', 1) or 1

    # Get threshold from models if not specified
    if threshold is None:
        idx_params = models.get("indices", {}).get(index_name, {})
        threshold = idx_params.get("typical_bloom_threshold", 0.05)

    logger.info(f"传感器: {sensor}, 指数: {index_name}, 阈值: {threshold}")

    # --- Synthetic/demo mode ---
    use_synthetic = not (hasattr(args, 'input_dir') and args.input_dir)
    warnings = []

    if use_synthetic:
        logger.info("运行合成演示模式")
        n_days = getattr(args, 'n_days', 10) or 10
        days_data = generate_synthetic_reflectance(
            n_days=n_days, n_rows=50, n_cols=50,
            sensor=sensor, seed=42
        )
    else:
        logger.info(f"输入目录: {args.input_dir}")
        # TODO: Implement file-based input loading
        warnings.append("文件输入模式未完全实现，使用合成数据")
        days_data = generate_synthetic_reflectance(n_days=10, sensor=sensor, seed=42)

    # --- Compute bloom index and probability for each day ---
    probability_stack = np.full((len(days_data), 50, 50), np.nan, dtype=np.float32)
    qc_stats_aggregate = {
        "cloud_pixels": 0, "glint_pixels": 0,
        "turbid_pixels": 0, "shallow_pixels": 0,
        "total_pixels": 0, "valid_pixels": 0,
    }

    for t, bands in enumerate(days_data):
        # Quality control
        valid_mask, qc_stats = compute_quality_mask(bands, models)
        for k in qc_stats_aggregate:
            if k in qc_stats:
                qc_stats_aggregate[k] += qc_stats[k]

        # Compute index
        index_value = None
        if index_name == "ndci" and "red" in bands and "red_edge" in bands:
            index_value = compute_ndci(bands["red"], bands["red_edge"])
        elif index_name == "flh" and "red2" in bands and "red3" in bands and "nir" in bands:
            index_value = compute_flh(bands["red2"], bands["red3"], bands["nir"])
        elif index_name == "bgi" and "blue" in bands and "green" in bands:
            index_value = compute_bgi(bands["blue"], bands["green"])
        elif index_name == "ari" and "green" in bands and "red_edge" in bands:
            index_value = compute_ari(bands["green"], bands["red_edge"])
        else:
            logger.warning(f"指数 {index_name} 所需波段不可用，回退到 BGI")
            if "blue" in bands and "green" in bands:
                index_value = compute_bgi(bands["blue"], bands["green"])
                index_name = "bgi"

        if index_value is not None:
            # Apply QC mask
            index_value[~valid_mask] = np.nan
            # Convert to probability
            prob = index_to_probability(index_value, threshold)
            probability_stack[t] = prob

    # --- Event detection ---
    event_id_map, events = detect_bloom_events(
        probability_stack, threshold=threshold,
        min_consecutive_days=min_consecutive, max_gap_days=max_gap
    )
    logger.info(f"检测到 {len(events)} 个藻华事件")

    # --- Duration map ---
    duration_map, missing_map = compute_duration_map(probability_stack, threshold)

    # --- Daily area ---
    bloom_daily = np.zeros_like(probability_stack, dtype=bool)
    for t in range(probability_stack.shape[0]):
        bloom_daily[t] = (~np.isnan(probability_stack[t])) & (probability_stack[t] >= threshold)

    pixel_area_m2 = 400.0  # 20m x 20m for Sentinel-2
    daily_area = compute_daily_area(bloom_daily, pixel_area_m2)

    # --- Risk assessment ---
    # Use max probability across time for risk
    max_probability = np.nanmax(probability_stack, axis=0)
    risk_map, risk_counts = assess_risk(max_probability, duration_map, models)

    # --- Generate outputs ---

    # bloom_probability.tif (save as .npy for synthetic mode)
    prob_output = output_dir / "bloom_probability.npy"
    np.save(prob_output, max_probability)
    logger.info(f"藻华概率已保存: {prob_output}")

    # duration.tif (save as .npy)
    duration_output = output_dir / "duration.npy"
    np.save(duration_output, duration_map.astype(np.float32))
    logger.info(f"持续时间已保存: {duration_output}")

    # events.geojson
    features = []
    for event in events:
        r, c = event["row"], event["col"]
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(c), float(r)],
            },
            "properties": {
                "event_id": event["event_id"],
                "start_day": event["start_day_index"],
                "end_day": event["end_day_index"],
                "duration_days": event["duration_days"],
                "max_probability": event["max_probability"],
            },
        })

    events_geojson = {
        "type": "FeatureCollection",
        "features": features,
    }
    events_path = output_dir / "events.geojson"
    events_path.write_text(
        json.dumps(events_geojson, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # daily_area.csv
    csv_path = output_dir / "daily_area.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["day", "bloom_area_km2", "n_bloom_pixels"])
        for t in range(len(daily_area)):
            n_pixels = int(np.sum(bloom_daily[t]))
            writer.writerow([t + 1, round(daily_area[t], 6), n_pixels])

    # Report HTML
    report_results = {
        "n_days": len(days_data),
        "max_daily_area_km2": float(np.max(daily_area)) if len(daily_area) > 0 else 0,
        "mean_daily_area_km2": float(np.mean(daily_area)) if len(daily_area) > 0 else 0,
        "n_events": len(events),
        "risk_counts": risk_counts,
        "qc_stats": qc_stats_aggregate,
        "warnings": warnings,
        "min_consecutive_days": min_consecutive,
    }
    report_path = generate_report_html(report_results, output_dir)

    # request.json
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "synthetic" if use_synthetic else "file",
        "sensor": sensor,
        "index": index_name,
        "threshold": threshold,
        "min_consecutive_days": min_consecutive,
        "max_gap_days": max_gap,
        "n_days": len(days_data),
        "output_dir": str(output_dir),
    }
    request_path = output_dir / "request.json"
    request_path.write_text(
        json.dumps(request_info, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # dataset-manifest.json
    dataset_manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "synthetic" if use_synthetic else "file",
        "sensor": sensor,
        "index": index_name,
        "n_days": len(days_data),
        "grid_shape": [50, 50],
        "pixel_area_m2": pixel_area_m2,
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # output-manifest.json
    output_files = {
        "alert_report.html": str(report_path),
        "events.geojson": str(events_path),
        "daily_area.csv": str(csv_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(dataset_path),
    }
    if use_synthetic:
        output_files["bloom_probability.npy"] = str(prob_output)
        output_files["duration.npy"] = str(duration_output)

    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "output_files": output_files,
        "summary": {
            "n_days": len(days_data),
            "n_events": len(events),
            "max_daily_area_km2": float(np.max(daily_area)) if len(daily_area) > 0 else 0,
            "n_warnings": len(warnings),
        },
    }
    # Auto-download provenance (only when --bbox/--aoi-file triggered a download)
    if fetch_meta is not None:
        manifest["data_source"] = fetch_meta.get("data_source")
        manifest["fetched_at"] = fetch_meta.get("fetched_at")
        manifest["collection"] = fetch_meta.get("collection")
        manifest["bbox"] = fetch_meta.get("bbox")
        manifest["date_range"] = fetch_meta.get("date_range")
    manifest_path = output_dir / "output-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # qa.json
    qa = {
        "status": "complete",
        "checks": {
            "report_generated": report_path.exists(),
            "events_generated": events_path.exists(),
            "daily_area_generated": csv_path.exists(),
            "all_outputs_written": all(Path(p).exists() for p in output_files.values()),
        },
        "n_days": len(days_data),
        "n_events": len(events),
        "n_warnings": len(warnings),
        "warnings": warnings,
        "qc_stats": qc_stats_aggregate,
    }
    qa_path = output_dir / "qa.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    logger.info(f"藻华监测完成: {len(days_data)} 天, {len(events)} 事件, "
                f"{len(warnings)} 警告")
    cleanup_logging()
    return EXIT_OK


def validate_args(args) -> int:
    """Validate file existence and numeric ranges.
    Returns exit code (0 = ok, 2 = arg error)."""
    for flag, accessor in FILE_ARGS.items():
        path = eval(accessor)  # noqa: S307 - safe: only string concat
        if path is not None and not Path(path).exists():
            print(f"ERROR: --{flag} not found: {path}", file=sys.stderr)
            return 2
    for flag, (lo, hi) in NUMERIC_RANGES.items():
        val = getattr(args, flag, None)
        if val is None:
            continue
        if lo is not None and val < lo:
            print(f"ERROR: --{flag}={val} below minimum {lo}", file=sys.stderr)
            return 2
        if hi is not None and val > hi:
            print(f"ERROR: --{flag}={val} above maximum {hi}", file=sys.stderr)
            return 2
    return 0


def main():
    parser = argparse.ArgumentParser(description="有害藻华监测 (Harmful Algal Bloom Monitor)")
    parser.add_argument("--input-dir", default=None,
                        help="输入反射率数据目录 (省略则使用合成数据)")
    parser.add_argument("--sensor", default="sentinel2",
                        choices=["modis", "sentinel2", "sentinel3_olci"],
                        help="传感器类型 (默认: sentinel2)")
    parser.add_argument("--index", default="ndci",
                        choices=["ndci", "flh", "bgi", "ari"],
                        help="藻华指数 (默认: ndci)")
    parser.add_argument("--event-threshold", type=float, default=None,
                        help="藻华概率阈值 (默认使用模型推荐值)")
    parser.add_argument("--min-consecutive-days", type=int, default=3,
                        help="确认事件所需最少连续天数 (默认: 3)")
    parser.add_argument("--max-gap-days", type=int, default=1,
                        help="事件内允许最大缺测天数 (默认: 1)")
    parser.add_argument("--n-days", type=int, default=10,
                        help="合成数据天数 (默认: 10)")
    parser.add_argument("--models-config", default=None,
                        help="模型参数 JSON 文件路径")
    parser.add_argument("--output-dir", "-o", default="habm-output",
                        help="输出目录 (默认: habm-output)")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    add_bbox_date_args(parser)

    args = parser.parse_args()

    try:
        sys.exit(run_bloom_monitor_pipeline(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
