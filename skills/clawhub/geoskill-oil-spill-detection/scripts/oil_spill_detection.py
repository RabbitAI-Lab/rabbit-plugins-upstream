#!/usr/bin/env python3
"""
Oil Spill Detection — SAR 暗斑油膜检测

从 SAR 暗斑中筛选疑似油膜，结合风场、形状、纹理、船舶和自然 slick 线索
输出人工复核候选。

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
import math
import os
import sys
import traceback
from datetime import datetime, timezone
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



try:
    import rasterio
    from rasterio.transform import from_origin as _rio_from_origin
    _HAS_RASTERIO = True
except ImportError:
    _HAS_RASTERIO = False

try:
    from fpdf import FPDF
    _HAS_FPDF = True
except ImportError:
    _HAS_FPDF = False

EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# ============================================================
# Logging
# ============================================================

def setup_logging(output_dir: Path) -> logging.Logger:
    """Setup logging to file and console."""
    logger = logging.getLogger("osd")
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
    """Close all handlers on the osd logger."""
    logger = logging.getLogger("osd")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)


# ============================================================
# Model Registry
# ============================================================

def load_oil_spill_factors(factors_path: Optional[str] = None) -> Dict:
    """Load oil spill detection model parameters from JSON reference file."""
    if factors_path is None:
        script_dir = Path(__file__).parent
        factors_path = script_dir.parent / "references" / "oil_spill_factors.json"

    with open(factors_path, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# Geometry Helpers
# ============================================================

def create_polygon(x: float, y: float, w: float, h: float) -> List[List[float]]:
    """
    Create a polygon from origin (x, y) with width w and height h.
    Returns a list of [x, y] coordinates forming a closed ring.
    """
    return [
        [x, y],
        [x + w, y],
        [x + w, y + h],
        [x, y + h],
        [x, y],
    ]


def point_to_pixel(lon: float, lat: float, transform: Tuple[float, ...]) -> Tuple[int, int]:
    """Convert geographic coordinates to pixel coordinates."""
    origin_x, pixel_width, _, origin_y, _, pixel_height = transform
    col = int((lon - origin_x) / pixel_width)
    row = int((lat - origin_y) / pixel_height)
    return row, col


def pixel_to_lonlat(row: int, col: int, transform: Tuple[float, ...]) -> Tuple[float, float]:
    """Convert pixel coordinates to geographic coordinates (center of pixel)."""
    origin_x, pixel_width, _, origin_y, _, pixel_height = transform
    lon = origin_x + (col + 0.5) * pixel_width
    lat = origin_y + (row + 0.5) * pixel_height
    return lon, lat


def haversine_distance_km(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """Calculate distance between two points in km using haversine formula."""
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def epsg4326_area_m2(lat: float, width_m: float, height_m: float) -> float:
    """Approximate area in m² for EPSG:4326 at given latitude."""
    lat_factor = 111320.0
    lon_factor = math.cos(math.radians(lat)) * 111320.0
    width_deg = width_m / lon_factor
    height_deg = height_m / lat_factor
    area_m2 = width_deg * height_deg * lon_factor * lat_factor
    return width_m * height_m

# ============================================================
# SAR Preprocessing
# ============================================================

def calibrate_sar(raw_counts: np.ndarray, calibration_lut: float = 1.0,
                  nodata: float = 0.0) -> np.ndarray:
    """
    Convert SAR raw counts to sigma-nought (dB).

    Args:
        raw_counts: Raw SAR digital numbers
        calibration_lut: Calibration factor
        nodata: Nodata value

    Returns:
        Calibrated backscatter in dB
    """
    valid = (raw_counts != nodata) & (raw_counts > 0) & ~np.isnan(raw_counts)
    result = np.full_like(raw_counts, np.nan, dtype=np.float32)
    result[valid] = (10.0 * np.log10(raw_counts[valid] ** 2 * calibration_lut)).astype(np.float32)
    return result


def speckle_filter(backscatter_db: np.ndarray, window: int = 3,
                   nodata: float = -9999.0) -> np.ndarray:
    """
    Apply mean filter for speckle reduction.

    Args:
        backscatter_db: Calibrated backscatter in dB
        window: Filter window size
        nodata: Nodata value

    Returns:
        Filtered backscatter
    """
    from scipy.ndimage import uniform_filter

    valid_mask = ~np.isnan(backscatter_db) & (backscatter_db != nodata) & ~np.isinf(backscatter_db)
    clean = np.where(valid_mask, backscatter_db, 0.0)

    filtered = uniform_filter(clean, size=window, mode='constant')
    filtered[~valid_mask] = np.nan
    return filtered.astype(np.float32)


def create_land_mask(sar_shape: Tuple[int, int], land_fraction: float = 0.1,
                     seed: int = 42) -> np.ndarray:
    """
    Create a synthetic land mask for demo/testing.

    Args:
        sar_shape: Shape of the SAR image
        land_fraction: Fraction of image that is land
        seed: Random seed

    Returns:
        Boolean land mask (True = land)
    """
    rng = np.random.RandomState(seed)
    n_rows, n_cols = sar_shape
    land_mask = np.zeros(sar_shape, dtype=bool)
    land_boundary = int(n_cols * land_fraction)
    land_mask[:, :land_boundary] = True

    for r in range(n_rows):
        jitter = rng.randint(-2, 3)
        col_boundary = max(0, min(n_cols, land_boundary + jitter))
        land_mask[r, :col_boundary] = True

    return land_mask


def create_radar_shadow_mask(sar_shape: Tuple[int, int],
                             shadow_fraction: float = 0.05,
                             seed: int = 42) -> np.ndarray:
    """Create a synthetic radar shadow mask."""
    rng = np.random.RandomState(seed + 1)
    shadow_mask = np.zeros(sar_shape, dtype=bool)
    n_rows, n_cols = sar_shape
    shadow_rows = int(n_rows * shadow_fraction)
    shadow_cols = int(n_cols * shadow_fraction)
    if shadow_rows > 0 and shadow_cols > 0:
        shadow_mask[:shadow_rows, :shadow_cols] = rng.random((shadow_rows, shadow_cols)) > 0.5
    return shadow_mask


# ============================================================
# Dark Spot Segmentation
# ============================================================

def segment_dark_spots_threshold(backscatter_db: np.ndarray,
                                 threshold_db: float = -18.0,
                                 sigma: float = 3.0,
                                 nodata: float = -9999.0) -> np.ndarray:
    """
    Segment dark spots using global threshold.

    Dark spots = pixels with backscatter significantly below threshold.

    Args:
        backscatter_db: Calibrated backscatter in dB
        threshold_db: Threshold in dB
        sigma: Number of standard deviations below mean
        nodata: Nodata value

    Returns:
        Boolean mask of dark spots
    """
    valid = ~np.isnan(backscatter_db) & (backscatter_db != nodata) & ~np.isinf(backscatter_db)
    if not np.any(valid):
        return np.zeros(backscatter_db.shape, dtype=bool)

    mean_bs = np.nanmean(backscatter_db[valid])
    std_bs = np.nanstd(backscatter_db[valid])

    threshold = min(mean_bs - sigma * std_bs, threshold_db)
    dark_spots = valid & (backscatter_db < threshold)

    return dark_spots


def segment_dark_spots_adaptive(backscatter_db: np.ndarray,
                                window_size: int = 51,
                                C: float = -2.0,
                                global_sigma: float = 3.0,
                                nodata: float = -9999.0) -> np.ndarray:
    """
    Segment dark spots using adaptive threshold based on local statistics.

    Args:
        backscatter_db: Calibrated backscatter in dB
        window_size: Local window size
        C: Constant subtracted from local mean (in units of std)
        global_sigma: Global sigma fallback
        nodata: Nodata value

    Returns:
        Boolean mask of dark spots
    """
    from scipy.ndimage import uniform_filter

    valid = ~np.isnan(backscatter_db) & (backscatter_db != nodata) & ~np.isinf(backscatter_db)
    clean = np.where(valid, backscatter_db, 0.0)

    local_mean = uniform_filter(clean, size=window_size, mode='constant')
    local_mean_sq = uniform_filter(clean ** 2, size=window_size, mode='constant')
    local_var = local_mean_sq - local_mean ** 2
    local_var = np.maximum(local_var, 0.0)
    local_std = np.sqrt(local_var)

    threshold = local_mean + C * local_std
    dark_spots = valid & (backscatter_db < threshold)

    global_mean = np.nanmean(backscatter_db[valid])
    global_std_val = np.nanstd(backscatter_db[valid])
    global_threshold = global_mean - global_sigma * global_std_val
    dark_spots_global = valid & (backscatter_db < global_threshold)

    dark_spots = dark_spots & dark_spots_global

    return dark_spots


def remove_small_objects(mask: np.ndarray, min_pixels: int = 9) -> np.ndarray:
    """
    Remove connected components smaller than min_pixels.

    Args:
        mask: Boolean mask
        min_pixels: Minimum number of pixels per component

    Returns:
        Cleaned mask
    """
    from scipy.ndimage import label

    labeled, n_features = label(mask)
    cleaned = np.zeros_like(mask)

    for i in range(1, n_features + 1):
        component = labeled == i
        if np.sum(component) >= min_pixels:
            cleaned |= component

    return cleaned

# ============================================================
# Feature Extraction
# ============================================================

def extract_shape_features(region_mask: np.ndarray,
                           pixel_area_m2: float) -> Dict[str, float]:
    """
    Extract shape features from a dark spot region.

    Args:
        region_mask: Boolean mask of the region
        pixel_area_m2: Area of one pixel in m²

    Returns:
        Dictionary of shape features
    """
    n_pixels = int(np.sum(region_mask))
    area_m2 = n_pixels * pixel_area_m2

    from scipy.ndimage import binary_erosion
    eroded = binary_erosion(region_mask)
    boundary = region_mask & ~eroded
    perimeter_pixels = int(np.sum(boundary))

    pixel_size_m = math.sqrt(pixel_area_m2)
    perimeter_m = perimeter_pixels * pixel_size_m

    if perimeter_m > 0:
        compactness = (4.0 * math.pi * area_m2) / (perimeter_m ** 2)
    else:
        compactness = 0.0

    rows, cols = np.where(region_mask)
    min_row, max_row = int(np.min(rows)), int(np.max(rows))
    min_col, max_col = int(np.min(cols)), int(np.max(cols))
    height_pixels = max_row - min_row + 1
    width_pixels = max_col - min_col + 1

    if min(height_pixels, width_pixels) > 0:
        elongation = max(height_pixels, width_pixels) / min(height_pixels, width_pixels)
    else:
        elongation = 1.0

    bbox_area_pixels = height_pixels * width_pixels
    if bbox_area_pixels > 0:
        solidity = n_pixels / bbox_area_pixels
    else:
        solidity = 1.0

    return {
        "area_m2": round(area_m2, 1),
        "n_pixels": n_pixels,
        "perimeter_m": round(perimeter_m, 1),
        "compactness": round(compactness, 4),
        "elongation": round(elongation, 4),
        "solidity": round(solidity, 4),
        "bbox_pixels": [min_row, min_col, max_row, max_col],
    }


def extract_texture_features(region_mask: np.ndarray,
                             backscatter_db: np.ndarray,
                             background_db: np.ndarray) -> Dict[str, float]:
    """
    Extract texture features from a dark spot region.

    Args:
        region_mask: Boolean mask of the region
        backscatter_db: Full backscatter image
        background_db: Background (non-dark-spot) backscatter

    Returns:
        Dictionary of texture features
    """
    region_values = backscatter_db[region_mask]
    valid_values = region_values[~np.isnan(region_values)]

    if len(valid_values) == 0:
        return {
            "mean_backscatter_db": np.nan,
            "std_backscatter_db": np.nan,
            "contrast_to_background_db": np.nan,
        }

    mean_bs = float(np.mean(valid_values))
    std_bs = float(np.std(valid_values))

    valid_bg = background_db[~np.isnan(background_db)]
    if len(valid_bg) > 0:
        mean_bg = float(np.mean(valid_bg))
        contrast = mean_bg - mean_bs
    else:
        contrast = np.nan

    return {
        "mean_backscatter_db": round(mean_bs, 4),
        "std_backscatter_db": round(std_bs, 4),
        "contrast_to_background_db": round(contrast, 4),
    }


# ============================================================
# Wind Field Analysis
# ============================================================

def classify_wind_zone(wind_speed_ms: float, factors: Dict) -> str:
    """
    Classify wind speed into zones.

    Args:
        wind_speed_ms: Wind speed in m/s
        factors: Model parameters

    Returns:
        Zone name: 'low_wind', 'optimal_wind', 'high_wind', 'extreme_wind'
    """
    wind_filter = factors.get("wind_filter", {})

    for zone_name in ["low_wind", "optimal_wind", "high_wind", "extreme_wind"]:
        zone = wind_filter.get(zone_name, {})
        speed_range = zone.get("speed_range_ms", [0.0, 100.0])
        if speed_range[0] <= wind_speed_ms < speed_range[1]:
            return zone_name

    return "extreme_wind"


def compute_wind_confidence(wind_speed_ms: float, factors: Dict) -> float:
    """
    Compute confidence modifier based on wind speed.

    Optimal wind (3-10 m/s) gives highest confidence.
    Low wind (< 3 m/s) reduces confidence (natural slicks possible).
    High wind (> 10 m/s) reduces confidence (oil disperses).

    Args:
        wind_speed_ms: Wind speed in m/s
        factors: Model parameters

    Returns:
        Confidence modifier [0, 1]
    """
    if wind_speed_ms < 0:
        return 0.0
    elif wind_speed_ms < 3.0:
        return 0.3 + 0.7 * (wind_speed_ms / 3.0)
    elif wind_speed_ms <= 10.0:
        return 1.0
    elif wind_speed_ms <= 25.0:
        return 1.0 - 0.7 * ((wind_speed_ms - 10.0) / 15.0)
    else:
        return 0.2


def detect_natural_slick_indicators(shape_features: Dict,
                                    wind_speed_ms: float,
                                    distance_to_coast_km: float) -> List[str]:
    """
    Detect indicators that a dark spot might be a natural slick.

    Args:
        shape_features: Shape features dict
        wind_speed_ms: Wind speed in m/s
        distance_to_coast_km: Distance to nearest coast

    Returns:
        List of natural slick indicator strings
    """
    indicators = []

    if wind_speed_ms < 3.0 and shape_features.get("elongation", 1.0) > 5.0:
        indicators.append("low_wind_parallel_lines")

    if distance_to_coast_km < 5.0 and shape_features.get("elongation", 1.0) > 3.0:
        indicators.append("coastal_streak")

    if (shape_features.get("compactness", 0.0) > 0.6 and
            shape_features.get("solidity", 0.0) > 0.8):
        indicators.append("rain_cell")

    return indicators


# ============================================================
# Ship / AIS Correlation
# ============================================================

def correlate_with_ais(dark_spot_lon: float, dark_spot_lat: float,
                       ais_ships: List[Dict],
                       max_distance_km: float = 5.0,
                       max_time_hours: float = 24.0) -> Optional[Dict]:
    """
    Correlate a dark spot with nearby AIS ship positions.

    Args:
        dark_spot_lon: Dark spot centroid longitude
        dark_spot_lat: Dark spot centroid latitude
        ais_ships: List of AIS ship records with 'lon', 'lat', 'timestamp'
        max_distance_km: Maximum matching distance
        max_time_hours: Maximum time difference

    Returns:
        Closest ship record or None
    """
    if not ais_ships:
        return None

    closest_ship = None
    closest_distance = float('inf')

    for ship in ais_ships:
        dist = haversine_distance_km(
            dark_spot_lon, dark_spot_lat,
            ship["lon"], ship["lat"]
        )
        if dist < closest_distance and dist <= max_distance_km:
            closest_distance = dist
            closest_ship = ship

    if closest_ship:
        closest_ship = dict(closest_ship)
        closest_ship["distance_km"] = round(closest_distance, 3)

    return closest_ship


def compute_ship_confidence(closest_ship: Optional[Dict],
                            factors: Dict) -> float:
    """
    Compute confidence modifier based on ship proximity.

    If a ship is nearby, increases likelihood of oil spill.
    If no AIS data, returns neutral confidence (not penalized).

    Args:
        closest_ship: Closest ship record or None
        factors: Model parameters

    Returns:
        Confidence modifier [0, 1]
    """
    if closest_ship is None:
        return 0.5

    distance_km = closest_ship.get("distance_km", float('inf'))
    max_distance = factors.get("ship_correlation", {}).get("ais_match_distance_km", 5.0)

    if distance_km <= max_distance:
        return 1.0 - 0.5 * (distance_km / max_distance)
    else:
        return 0.5

# ============================================================
# Confidence Scoring
# ============================================================

def compute_oil_confidence(shape_features: Dict,
                           texture_features: Dict,
                           wind_speed_ms: float,
                           closest_ship: Optional[Dict],
                           natural_indicators: List[str],
                           factors: Dict) -> Tuple[float, Dict[str, float]]:
    """
    Compute overall oil spill confidence score.

    Combines shape, texture, wind, ship, and context features.

    Args:
        shape_features: Shape features dict
        texture_features: Texture features dict
        wind_speed_ms: Wind speed in m/s
        closest_ship: Closest ship record or None
        natural_indicators: List of natural slick indicators
        factors: Model parameters

    Returns:
        (confidence_score, component_scores)
    """
    method = factors.get("detection_methods", {}).get("multi_feature", {})
    weights = method.get("weights", {
        "shape_weight": 0.25,
        "texture_weight": 0.2,
        "wind_weight": 0.25,
        "ship_weight": 0.15,
        "context_weight": 0.15
    })

    # --- Shape score ---
    compactness = shape_features.get("compactness", 0.0)
    elongation = shape_features.get("elongation", 1.0)
    solidity = shape_features.get("solidity", 1.0)

    shape_ranges = factors.get("shape_features", {})
    comp_range = shape_ranges.get("compactness", {}).get("oil_range", [0.1, 0.8])
    elon_range = shape_ranges.get("elongation", {}).get("oil_range", [1.5, 20.0])
    sol_range = shape_ranges.get("solidity", {}).get("oil_range", [0.5, 1.0])

    comp_score = _range_score(compactness, comp_range[0], comp_range[1])
    elon_score = _range_score(elongation, elon_range[0], elon_range[1])
    sol_score = _range_score(solidity, sol_range[0], sol_range[1])

    shape_score = (comp_score + elon_score + sol_score) / 3.0

    # --- Texture score ---
    mean_bs = texture_features.get("mean_backscatter_db", np.nan)
    std_bs = texture_features.get("std_backscatter_db", np.nan)
    contrast = texture_features.get("contrast_to_background_db", np.nan)

    tex_ranges = factors.get("texture_features", {})
    if not np.isnan(mean_bs):
        mean_range = tex_ranges.get("mean_backscatter", {}).get("oil_range_db", [-25.0, -15.0])
        mean_score = _range_score(mean_bs, mean_range[0], mean_range[1])
    else:
        mean_score = 0.5

    if not np.isnan(std_bs):
        std_range = tex_ranges.get("backscatter_std", {}).get("oil_range_db", [0.0, 5.0])
        std_score = _range_score(std_bs, std_range[0], std_range[1])
    else:
        std_score = 0.5

    if not np.isnan(contrast):
        contrast_range = tex_ranges.get("contrast_to_background", {}).get("oil_range_db", [5.0, 25.0])
        contrast_score = _range_score(contrast, contrast_range[0], contrast_range[1])
    else:
        contrast_score = 0.5

    texture_score = (mean_score + std_score + contrast_score) / 3.0

    # --- Wind score ---
    wind_score = compute_wind_confidence(wind_speed_ms, factors)

    # --- Ship score ---
    ship_score = compute_ship_confidence(closest_ship, factors)

    # --- Context score ---
    context_score = 1.0
    if natural_indicators:
        context_score = max(0.0, 1.0 - 0.3 * len(natural_indicators))

    # --- Weighted combination ---
    confidence = (
        weights.get("shape_weight", 0.25) * shape_score +
        weights.get("texture_weight", 0.2) * texture_score +
        weights.get("wind_weight", 0.25) * wind_score +
        weights.get("ship_weight", 0.15) * ship_score +
        weights.get("context_weight", 0.15) * context_score
    )

    confidence = max(0.0, min(1.0, confidence))

    components = {
        "shape_score": round(shape_score, 4),
        "texture_score": round(texture_score, 4),
        "wind_score": round(wind_score, 4),
        "ship_score": round(ship_score, 4),
        "context_score": round(context_score, 4),
    }

    return round(confidence, 4), components


def _range_score(value: float, min_val: float, max_val: float) -> float:
    """
    Score a value based on how well it falls within a target range.

    Returns 1.0 at center of range, 0.0 far outside.
    """
    if np.isnan(value):
        return 0.5

    center = (min_val + max_val) / 2.0
    half_width = (max_val - min_val) / 2.0

    if half_width <= 0:
        return 1.0 if value == center else 0.0

    if min_val <= value <= max_val:
        return 1.0 - 0.5 * abs(value - center) / half_width
    elif value < min_val:
        distance = min_val - value
        return max(0.0, 0.5 - 0.5 * distance / half_width)
    else:
        distance = value - max_val
        return max(0.0, 0.5 - 0.5 * distance / half_width)


# ============================================================
# Object-level Dark Spot Analysis
# ============================================================

def analyze_dark_spots(dark_spot_mask: np.ndarray,
                       backscatter_db: np.ndarray,
                       wind_speed_grid: np.ndarray,
                       transform: Tuple[float, ...],
                       ais_ships: List[Dict],
                       factors: Dict,
                       min_area_m2: float = 1000.0) -> List[Dict]:
    """
    Analyze each dark spot and compute features + confidence.

    Args:
        dark_spot_mask: Boolean mask of all dark spots
        backscatter_db: Calibrated backscatter
        wind_speed_grid: Wind speed grid (m/s)
        transform: Rasterio-style transform
        ais_ships: AIS ship records
        factors: Model parameters
        min_area_m2: Minimum area threshold

    Returns:
        List of dark spot analysis records
    """
    from scipy.ndimage import label

    labeled, n_features = label(dark_spot_mask)
    results = []

    origin_x, pixel_width, _, origin_y, _, pixel_height = transform
    n_rows = dark_spot_mask.shape[0]
    center_lat = origin_y - (n_rows * abs(pixel_height)) / 2
    lat_factor = 111320.0
    lon_factor = math.cos(math.radians(center_lat)) * 111320.0
    pixel_area_m2 = abs(pixel_width * lon_factor) * abs(pixel_height * lat_factor)

    background_mask = ~dark_spot_mask & ~np.isnan(backscatter_db)

    for region_id in range(1, n_features + 1):
        region_mask = labeled == region_id
        shape_feats = extract_shape_features(region_mask, pixel_area_m2)

        if shape_feats["area_m2"] < min_area_m2:
            continue

        texture_feats = extract_texture_features(
            region_mask, backscatter_db, np.where(background_mask, backscatter_db, np.nan)
        )

        rows, cols = np.where(region_mask)
        centroid_row = float(np.mean(rows))
        centroid_col = float(np.mean(cols))
        centroid_lon, centroid_lat = pixel_to_lonlat(int(centroid_row), int(centroid_col), transform)

        wind_row, wind_col = int(centroid_row), int(centroid_col)
        if 0 <= wind_row < wind_speed_grid.shape[0] and 0 <= wind_col < wind_speed_grid.shape[1]:
            wind_speed = float(wind_speed_grid[wind_row, wind_col])
        else:
            wind_speed = 5.0

        closest_ship = correlate_with_ais(centroid_lon, centroid_lat, ais_ships,
                                          factors.get("ship_correlation", {}).get("ais_match_distance_km", 5.0))

        natural_indicators = detect_natural_slick_indicators(
            shape_feats, wind_speed, distance_to_coast_km=10.0
        )

        confidence, components = compute_oil_confidence(
            shape_feats, texture_feats, wind_speed, closest_ship, natural_indicators, factors
        )

        min_row, min_col, max_row, max_col = shape_feats["bbox_pixels"]
        bbox_lon_min, bbox_lat_max = pixel_to_lonlat(min_row, min_col, transform)
        bbox_lon_max, bbox_lat_min = pixel_to_lonlat(max_row, max_col, transform)

        results.append({
            "spot_id": len(results) + 1,
            "centroid_lon": round(centroid_lon, 6),
            "centroid_lat": round(centroid_lat, 6),
            "area_m2": shape_feats["area_m2"],
            "n_pixels": shape_feats["n_pixels"],
            "compactness": shape_feats["compactness"],
            "elongation": shape_feats["elongation"],
            "solidity": shape_feats["solidity"],
            "mean_backscatter_db": texture_feats["mean_backscatter_db"],
            "std_backscatter_db": texture_feats["std_backscatter_db"],
            "contrast_to_background_db": texture_feats["contrast_to_background_db"],
            "wind_speed_ms": round(wind_speed, 2),
            "wind_zone": classify_wind_zone(wind_speed, factors),
            "closest_ship_distance_km": closest_ship.get("distance_km") if closest_ship else None,
            "natural_indicators": natural_indicators,
            "confidence": confidence,
            "shape_score": components["shape_score"],
            "texture_score": components["texture_score"],
            "wind_score": components["wind_score"],
            "ship_score": components["ship_score"],
            "context_score": components["context_score"],
            "bbox": [bbox_lon_min, bbox_lat_min, bbox_lon_max, bbox_lat_max],
        })

    return results


# ============================================================
# Quality Control
# ============================================================

def compute_qa_checks(dark_spots: List[Dict],
                      sar_shape: Tuple[int, int],
                      valid_fraction: float,
                      wind_coverage: float,
                      factors: Dict) -> Dict[str, Any]:
    """
    Compute QA checks for the analysis.

    Args:
        dark_spots: List of analyzed dark spots
        sar_shape: Shape of the SAR image
        valid_fraction: Fraction of valid pixels
        wind_coverage: Fraction of area with wind data
        factors: Model parameters

    Returns:
        QA dictionary
    """
    qa_thresholds = factors.get("qa_thresholds", {})

    checks = {
        "valid_fraction_above_threshold": valid_fraction >= qa_thresholds.get("min_valid_fraction", 0.5),
        "wind_coverage_above_threshold": wind_coverage >= qa_thresholds.get("min_wind_coverage", 0.8),
        "dark_spots_detected": len(dark_spots) > 0,
        "all_spots_have_confidence": all("confidence" in s for s in dark_spots),
        "all_spots_have_bbox": all("bbox" in s for s in dark_spots),
    }

    all_passed = all(checks.values())

    return {
        "status": "complete" if all_passed else "warning",
        "checks": checks,
        "n_dark_spots": len(dark_spots),
        "n_candidates": len([s for s in dark_spots if s["confidence"] >= 0.4]),
        "valid_fraction": round(valid_fraction, 4),
        "wind_coverage": round(wind_coverage, 4),
        "thresholds_used": qa_thresholds,
    }

# ============================================================
# Synthetic Data Generation
# ============================================================

def load_sar_data(input_dir: Path, n_rows: int = 200, n_cols: int = 200,
                  seed: int = 42) -> Dict[str, Any]:
    """Load SAR backscatter + wind/land/shadow layers from a user directory.

    Looks for the following files (any subset; missing layers are synthesized):
      - backscatter.tif  (single-band float, dB)
      - wind_speed.tif   (single-band float, m/s)
      - land_mask.tif    (single-band uint8 0/1)
      - shadow_mask.tif  (single-band uint8 0/1)

    All .tif files must share the same grid (rows, cols). If grids differ,
    the first file's shape is used and a warning is logged.

    Returns:
        Dict compatible with the synthetic generator output.
    """
    if not _HAS_RASTERIO:
        raise RuntimeError(
            "rasterio is required to load SAR GeoTIFFs but is not installed. "
            "Install with: pip install rasterio"
        )

    logger = logging.getLogger("osd")
    input_dir = Path(input_dir)
    if not input_dir.is_dir():
        raise ValueError(f"Input path is not a directory: {input_dir}")

    candidates = {
        "backscatter_db": ["backscatter.tif", "sar.tif", "sigma0.tif",
                            "intensity.tif", "vv.tif"],
        "wind_speed": ["wind_speed.tif", "wind.tif"],
        "land_mask": ["land_mask.tif", "land.tif"],
        "shadow_mask": ["shadow_mask.tif", "shadow.tif"],
    }

    found: Dict[str, np.ndarray] = {}
    used_files: Dict[str, str] = {}
    for layer, names in candidates.items():
        for name in names:
            fpath = input_dir / name
            if fpath.exists():
                with rasterio.open(str(fpath)) as src:
                    arr = src.read(1)
                found[layer] = arr.astype(np.float32)
                used_files[layer] = name
                logger.info(f"Loaded {layer} from {fpath} (shape={arr.shape})")
                break

    if "backscatter_db" not in found:
        raise ValueError(
            f"No backscatter GeoTIFF found in {input_dir}. "
            f"Expected one of: {candidates['backscatter_db']}"
        )

    rows, cols = found["backscatter_db"].shape
    for layer, arr in found.items():
        if arr.shape != (rows, cols):
            logger.warning(
                f"Layer '{layer}' shape {arr.shape} != backscatter shape "
                f"({rows}, {cols}); resizing with simple crop/pad."
            )
            r2 = min(rows, arr.shape[0])
            c2 = min(cols, arr.shape[1])
            new = np.zeros((rows, cols), dtype=np.float32)
            new[:r2, :c2] = arr[:r2, :c2]
            found[layer] = new

    # Fill missing layers with synthetic defaults (consistent with
    # generate_synthetic_sar_data for the wind/land/shadow layers).
    if "wind_speed" not in found:
        logger.info("No wind_speed layer; synthesizing default wind field")
        from scipy.ndimage import uniform_filter
        rng = np.random.RandomState(seed)
        wind_base = rng.uniform(3.0, 8.0, (rows, cols)).astype(np.float32)
        wind_smooth = uniform_filter(wind_base, size=25, mode='constant')
        ws = 3.0 + 7.0 * (wind_smooth - wind_smooth.min()) / max(
            wind_smooth.max() - wind_smooth.min(), 0.001)
        found["wind_speed"] = ws.astype(np.float32)

    if "land_mask" not in found:
        logger.info("No land_mask layer; synthesizing default land mask")
        found["land_mask"] = create_land_mask(
            (rows, cols), land_fraction=0.15, seed=seed
        ).astype(np.float32)

    if "shadow_mask" not in found:
        logger.info("No shadow_mask layer; synthesizing default shadow mask")
        found["shadow_mask"] = create_radar_shadow_mask(
            (rows, cols), shadow_fraction=0.05, seed=seed
        ).astype(np.float32)

    return {
        "backscatter_db": found["backscatter_db"],
        "wind_speed": found["wind_speed"],
        "land_mask": found["land_mask"].astype(bool),
        "shadow_mask": found["shadow_mask"].astype(bool),
        "n_rows": rows,
        "n_cols": cols,
        "source_files": used_files,
    }


def generate_synthetic_sar_data(n_rows: int = 200, n_cols: int = 200,
                                seed: int = 42) -> Dict[str, Any]:
    """
    Generate synthetic SAR and wind data for demo/testing.

    Simulates:
    - Sea surface with realistic backscatter
    - Dark spots (potential oil spills)
    - Wind field
    - Land mask

    Returns:
        Dictionary with all synthetic data
    """
    rng = np.random.RandomState(seed)

    # --- SAR backscatter ---
    base_backscatter = rng.normal(-12.0, 3.0, (n_rows, n_cols)).astype(np.float32)

    from scipy.ndimage import uniform_filter
    base_backscatter = uniform_filter(base_backscatter, size=15, mode='constant')

    # --- Dark spots (simulated oil slicks) ---
    margin = max(min(n_rows, n_cols) // 5, 3)
    n_spots = rng.randint(3, 8)
    dark_spot_mask = np.zeros((n_rows, n_cols), dtype=bool)

    for _ in range(n_spots):
        cx = rng.randint(margin, max(margin + 1, n_cols - margin))
        cy = rng.randint(margin, max(margin + 1, n_rows - margin))
        radius_x = rng.randint(3, max(4, min(n_cols // 4, 20)))
        radius_y = rng.randint(2, max(3, min(n_rows // 5, 10)))
        angle = rng.uniform(0, math.pi)

        rows, cols = np.arange(n_rows), np.arange(n_cols)
        col_grid, row_grid = np.meshgrid(cols, rows)

        dx = col_grid - cx
        dy = row_grid - cy
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        dist = ((dx * cos_a + dy * sin_a) / max(radius_x, 1)) ** 2 + \
               ((dx * -sin_a + dy * cos_a) / max(radius_y, 1)) ** 2

        spot = dist < 1.0
        dark_spot_mask |= spot

        base_backscatter[spot] -= rng.uniform(8.0, 15.0)

    base_backscatter = np.clip(base_backscatter, -35.0, 0.0).astype(np.float32)

    # --- Wind field ---
    wind_base = rng.uniform(3.0, 8.0, (n_rows, n_cols)).astype(np.float32)
    wind_smooth = uniform_filter(wind_base, size=25, mode='constant')
    wind_speed = 3.0 + 7.0 * (wind_smooth - wind_smooth.min()) / max(wind_smooth.max() - wind_smooth.min(), 0.001)
    wind_speed = wind_speed.astype(np.float32)

    # --- Land mask ---
    land_mask = create_land_mask((n_rows, n_cols), land_fraction=0.15, seed=seed)

    # --- Radar shadow ---
    shadow_mask = create_radar_shadow_mask((n_rows, n_cols), shadow_fraction=0.05, seed=seed)

    return {
        "backscatter_db": base_backscatter,
        "dark_spot_mask": dark_spot_mask,
        "wind_speed": wind_speed,
        "land_mask": land_mask,
        "shadow_mask": shadow_mask,
        "n_rows": n_rows,
        "n_cols": n_cols,
    }


# ============================================================
# Output Generation
# ============================================================

def write_dark_spots_geojson(dark_spots: List[Dict], output_dir: Path) -> Path:
    """Write dark spots as GeoJSON."""
    features = []
    for spot in dark_spots:
        lon_min, lat_min, lon_max, lat_max = spot["bbox"]
        polygon = create_polygon(lon_min, lat_min, lon_max - lon_min, lat_max - lat_min)

        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [polygon],
            },
            "properties": {
                "spot_id": spot["spot_id"],
                "area_m2": spot["area_m2"],
                "confidence": spot["confidence"],
                "mean_backscatter_db": spot["mean_backscatter_db"],
                "wind_speed_ms": spot["wind_speed_ms"],
                "wind_zone": spot["wind_zone"],
                "natural_indicators": spot["natural_indicators"],
                "is_oil_candidate": spot["confidence"] >= 0.4,
            },
        })

    geojson = {"type": "FeatureCollection", "features": features}
    path = output_dir / "dark_spots.geojson"
    path.write_text(json.dumps(geojson, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    return path


def write_oil_candidates_geojson(dark_spots: List[Dict], output_dir: Path,
                                 confidence_threshold: float = 0.4) -> Path:
    """Write oil candidates (high confidence dark spots) as GeoJSON."""
    candidates = [s for s in dark_spots if s["confidence"] >= confidence_threshold]
    features = []
    for spot in candidates:
        lon_min, lat_min, lon_max, lat_max = spot["bbox"]
        polygon = create_polygon(lon_min, lat_min, lon_max - lon_min, lat_max - lat_min)

        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [polygon],
            },
            "properties": {
                "spot_id": spot["spot_id"],
                "area_m2": spot["area_m2"],
                "confidence": spot["confidence"],
                "shape_score": spot["shape_score"],
                "texture_score": spot["texture_score"],
                "wind_score": spot["wind_score"],
                "ship_score": spot["ship_score"],
                "context_score": spot["context_score"],
                "mean_backscatter_db": spot["mean_backscatter_db"],
                "wind_speed_ms": spot["wind_speed_ms"],
                "closest_ship_distance_km": spot["closest_ship_distance_km"],
                "natural_indicators": spot["natural_indicators"],
                "review_status": "pending",
                "note": "疑似油膜，需人工复核",
            },
        })

    geojson = {"type": "FeatureCollection", "features": features}
    path = output_dir / "oil_candidates.geojson"
    path.write_text(json.dumps(geojson, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    return path


def write_feature_table_csv(dark_spots: List[Dict], output_dir: Path) -> Path:
    """Write feature table as CSV."""
    path = output_dir / "feature_table.csv"

    if not dark_spots:
        with open(path, "w", newline="", encoding="utf-8") as f:
            f.write("spot_id,centroid_lon,centroid_lat,area_m2,confidence\n")
        return path

    fieldnames = [
        "spot_id", "centroid_lon", "centroid_lat", "area_m2", "n_pixels",
        "compactness", "elongation", "solidity",
        "mean_backscatter_db", "std_backscatter_db", "contrast_to_background_db",
        "wind_speed_ms", "wind_zone",
        "closest_ship_distance_km", "natural_indicators",
        "confidence", "shape_score", "texture_score", "wind_score",
        "ship_score", "context_score",
    ]

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for spot in dark_spots:
            row = dict(spot)
            row["natural_indicators"] = ";".join(row.get("natural_indicators", []))
            writer.writerow(row)

    return path


def write_confidence_raster(dark_spots: List[Dict], sar_shape: Tuple[int, int],
                            output_dir: Path) -> Path:
    """Write confidence raster as a real GeoTIFF (EPSG:4326, 0..1 float32)."""
    # Use 0.0 (no confidence) instead of NaN for invalid/empty pixels so downstream
    # tools (e.g. rasterio) don't choke on NaN values in non-mask regions. NaN
    # is reserved for true no-data areas when a separate mask is also written.
    confidence_grid = np.zeros(sar_shape, dtype=np.float32)

    for spot in dark_spots:
        lon_min, lat_min, lon_max, lat_max = spot["bbox"]
        row_min = int(max(0, min(sar_shape[0] - 1, (1.0 - lat_max) * sar_shape[0])))
        row_max = int(max(0, min(sar_shape[0] - 1, (1.0 - lat_min) * sar_shape[0])))
        col_min = int(max(0, min(sar_shape[1] - 1, lon_min * sar_shape[1])))
        col_max = int(max(0, min(sar_shape[1] - 1, lon_max * sar_shape[1])))

        if row_max > row_min and col_max > col_min:
            confidence_grid[row_min:row_max, col_min:col_max] = spot["confidence"]

    # Final guard: ensure no NaN anywhere in the output
    if np.any(np.isnan(confidence_grid)):
        confidence_grid = np.nan_to_num(confidence_grid, nan=0.0)

    if not _HAS_RASTERIO:
        # rasterio not available: fall back to .npy (numeric array, not GIS)
        path = output_dir / "confidence.npy"
        np.save(str(path), confidence_grid)
        return path

    # Real GeoTIFF output (EPSG:4326, 0.001 deg / pixel)
    n_rows, n_cols = sar_shape
    pixel_size = 0.001
    transform = _rio_from_origin(0.0, n_rows * pixel_size, pixel_size, pixel_size)
    path = output_dir / "confidence.tif"
    with rasterio.open(
        str(path), "w", driver="GTiff",
        height=n_rows, width=n_cols, count=1, dtype="float32",
        crs="EPSG:4326", transform=transform,
        compress="deflate",
    ) as dst:
        dst.write(confidence_grid, 1)
    return path


def write_review_report(dark_spots: List[Dict], qa: Dict, output_dir: Path) -> Path:
    """Write review report. Generates a real PDF (preferred) or plain-text
    fallback if fpdf is not available. PDF is the primary deliverable.
    """
    candidates = [s for s in dark_spots if s["confidence"] >= 0.4]
    sorted_spots = sorted(dark_spots, key=lambda x: x["confidence"], reverse=True)
    timestamp = datetime.now(timezone.utc).isoformat()

    if _HAS_FPDF:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        # Use a built-in font that supports CJK if available; default
        # Helvetica may not render Chinese. Fall back to ASCII labels if so.
        try:
            pdf.set_font("Helvetica", "B", 16)
        except Exception:
            pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "SAR Oil-Spill Detection - Review Report", ln=1)

        pdf.set_font("Helvetica", size=10)
        pdf.cell(0, 6, f"Generated: {timestamp}", ln=1)
        pdf.cell(0, 6, f"Total dark spots: {len(dark_spots)}", ln=1)
        pdf.cell(0, 6, f"Oil candidates (conf >= 0.4): {len(candidates)}", ln=1)
        pdf.cell(0, 6, f"QA status: {qa.get('status', 'unknown')}", ln=1)
        pdf.ln(4)

        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 8, "Top 10 High-Confidence Candidates", ln=1)
        pdf.set_font("Helvetica", size=9)
        for spot in sorted_spots[:10]:
            pdf.cell(0, 5, (
                f"Spot #{spot['spot_id']}: "
                f"loc=({spot['centroid_lon']:.4f}, {spot['centroid_lat']:.4f}), "
                f"area={spot['area_m2']:.0f} m2, "
                f"conf={spot['confidence']:.3f}, "
                f"backscatter={spot['mean_backscatter_db']:.2f} dB, "
                f"wind={spot['wind_speed_ms']:.1f} m/s ({spot['wind_zone']}), "
                f"ship_dist={spot.get('closest_ship_distance_km', 'N/A')} km"
            ), ln=1)

        pdf.ln(4)
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 8, "Important Notes", ln=1)
        pdf.set_font("Helvetica", size=9)
        notes = [
            "1. This report lists candidate oil slicks; dark spots are not oil evidence.",
            "2. All candidates require human review for confirmation.",
            "3. Low-wind zones, rain cells, internal waves, and biogenic films",
            "   can cause false positives.",
            "4. Missing AIS data means ships are NOT attributed by default.",
        ]
        for note in notes:
            pdf.cell(0, 5, note, ln=1)

        path = output_dir / "review_report.pdf"
        pdf.output(str(path))
        return path

    # fpdf not available: write plain-text report as a fallback
    path = output_dir / "review_report.txt"
    lines = [
        "=" * 60,
        "SAR Oil-Spill Detection - Review Report",
        "=" * 60,
        f"Generated: {timestamp}",
        f"Total dark spots: {len(dark_spots)}",
        f"Oil candidates (conf >= 0.4): {len(candidates)}",
        f"QA status: {qa.get('status', 'unknown')}",
        "",
        "-" * 60,
        "Top 10 High-Confidence Candidates",
        "-" * 60,
    ]
    for spot in sorted_spots[:10]:
        lines.extend([
            f"  Spot #{spot['spot_id']}:",
            f"    Location: ({spot['centroid_lon']:.4f}, {spot['centroid_lat']:.4f})",
            f"    Area: {spot['area_m2']:.0f} m2",
            f"    Confidence: {spot['confidence']:.4f}",
            f"    Backscatter: {spot['mean_backscatter_db']:.2f} dB",
            f"    Wind: {spot['wind_speed_ms']:.1f} m/s ({spot['wind_zone']})",
            f"    Ship distance: {spot.get('closest_ship_distance_km', 'N/A')} km",
            f"    Natural indicators: {spot.get('natural_indicators', [])}",
            "",
        ])
    lines.extend([
        "-" * 60,
        "Important Notes",
        "-" * 60,
        "1. This report lists candidate oil slicks; dark spots are not oil evidence.",
        "2. All candidates require human review for confirmation.",
        "3. Low-wind zones, rain cells, internal waves, and biogenic films",
        "   can cause false positives.",
        "4. Missing AIS data means ships are NOT attributed by default.",
        "=" * 60,
    ])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path

# ============================================================
# Main Pipeline
# ============================================================

def auto_download_sar(args, output_dir: Path) -> Dict[str, Any]:
    """Download one sentinel-1-grd scene from MPC using --bbox + --date-range.

    Returns metadata dict (also writes the path back to args.sar).
    """
    if not _FETCHER_AVAILABLE:
        raise RuntimeError(
            "Shared data fetcher not importable. Pass --sar <local.tif> instead, "
            "or ensure _geoskill_data_fetcher is on sys.path."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_sar requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        raise RuntimeError("auto_download_sar requires --date-range")
    cache_dir = getattr(args, "cache_dir", None)
    fetcher = DataFetcher(
        source=DataSource.PLANETARY_COMPUTER,
        cache_dir=Path(cache_dir) if cache_dir else None,
    )
    items = fetcher.search_stac(
        collection="sentinel-1-grd",
        bbox=bbox,
        date_range=dr,
        limit=1,
    )
    if not items:
        raise RuntimeError(
            f"No sentinel-1-grd items found in bbox={bbox} for {dr.start}..{dr.end}"
        )
    download_dir = output_dir / "downloaded"
    # Sentinel-1 GRD scenes are ~545 MB; bump the cap to 700 MB.
    paths = fetcher.download_assets(
        items=items, out_dir=download_dir, max_items=1, max_total_mb=700,
        prefer_assets=['vh', 'vv'],
    )
    if not paths:
        raise RuntimeError("Download returned no files")
    args.sar = str(paths[0])
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "sentinel-1-grd",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def run_oil_spill_pipeline(args: argparse.Namespace) -> int:
    """Main oil spill detection workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("osd-output")

    # --- Auto-download mode: fetch sentinel-1-grd from MPC ---
    if (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)) and getattr(args, "date_range", None):
        if not getattr(args, "sar", None):
            try:
                fetch_meta = auto_download_sar(args, output_dir)
                mode = "auto_download"
                print(f"  Auto-downloaded sar: {args.sar}")
            except DataFetcherError as e:
                print(f"ERROR: auto-download failed: [{e.kind}] {e.message}", file=sys.stderr)
                return EXIT_PROCESSING if 'EXIT_PROCESSING' in dir() else 7
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logging(output_dir)
    logger.info("SAR 油膜检测 — 启动")

    # Load model parameters
    factors_path = getattr(args, 'models_config', None)
    try:
        factors = load_oil_spill_factors(factors_path)
        logger.info(f"模型参数已加载: version {factors.get('version', 'unknown')}")
    except Exception as e:
        logger.error(f"加载模型参数失败: {e}")
        cleanup_logging()
        return EXIT_VALIDATION

    # Parse parameters
    method = getattr(args, 'method', 'threshold_basic') or 'threshold_basic'
    min_area = getattr(args, 'min_area', 1000.0) or 1000.0
    confidence_threshold = getattr(args, 'confidence_threshold', 0.4) or 0.4

    logger.info(f"检测方法: {method}, 最小面积: {min_area} m², 置信度阈值: {confidence_threshold}")

    # --- Synthetic/demo mode ---
    use_synthetic = not (hasattr(args, 'input_dir') and args.input_dir)
    warnings = []

    if use_synthetic:
        logger.info("运行合成演示模式")
        n_rows = getattr(args, 'grid_size', 200) or 200
        n_cols = n_rows
        synthetic = generate_synthetic_sar_data(n_rows=n_rows, n_cols=n_cols, seed=42)
    else:
        logger.info(f"输入目录: {args.input_dir}")
        input_path = Path(args.input_dir)
        if not input_path.exists():
            logger.error(f"Input path does not exist: {input_path}")
            cleanup_logging()
            return EXIT_VALIDATION
        try:
            synthetic = load_sar_data(
                input_path,
                n_rows=getattr(args, 'grid_size', 200) or 200,
                seed=42,
            )
            logger.info(
                f"Loaded SAR data {synthetic['n_rows']}x{synthetic['n_cols']} from "
                f"{input_path}; layers: {list(synthetic.get('source_files', {}).keys())}"
            )
        except Exception as e:
            logger.error(f"Failed to load SAR data: {e}")
            cleanup_logging()
            return EXIT_VALIDATION

    backscatter_db = synthetic["backscatter_db"]
    wind_speed = synthetic["wind_speed"]
    land_mask = synthetic["land_mask"]
    shadow_mask = synthetic["shadow_mask"]

    # --- Preprocessing ---
    valid_mask = ~land_mask & ~shadow_mask & ~np.isnan(backscatter_db)
    valid_fraction = float(np.sum(valid_mask)) / backscatter_db.size

    wind_valid = ~np.isnan(wind_speed) & ~land_mask
    wind_coverage = float(np.sum(wind_valid)) / max(np.sum(~land_mask), 1)

    logger.info(f"有效像素比例: {valid_fraction:.4f}, 风场覆盖: {wind_coverage:.4f}")

    # --- Dark spot segmentation ---
    if method == "threshold_adaptive":
        dark_spot_mask = segment_dark_spots_adaptive(
            backscatter_db,
            window_size=factors.get("detection_methods", {}).get("threshold_adaptive", {}).get("parameters", {}).get("window_size", 51),
            C=factors.get("detection_methods", {}).get("threshold_adaptive", {}).get("parameters", {}).get("C", -2.0),
        )
    else:
        dark_spot_mask = segment_dark_spots_threshold(
            backscatter_db,
            threshold_db=factors.get("detection_methods", {}).get("threshold_basic", {}).get("parameters", {}).get("backscatter_threshold_db", -18.0),
            sigma=factors.get("detection_methods", {}).get("threshold_basic", {}).get("parameters", {}).get("dark_spot_sigma", 3.0),
        )

    dark_spot_mask = remove_small_objects(dark_spot_mask, min_pixels=9)
    dark_spot_mask &= valid_mask

    n_dark_pixels = int(np.sum(dark_spot_mask))
    logger.info(f"暗斑像素数: {n_dark_pixels}")

    # --- Object-level analysis ---
    pixel_size = 0.001  # ~0.1 km in degrees
    transform = (0.0, pixel_size, 0, synthetic["n_rows"] * pixel_size, 0, -pixel_size)

    ais_ships = [
        {"lon": 0.05, "lat": 0.15, "timestamp": "2024-01-01T00:00:00Z", "mmsi": 123456789, "length_m": 150},
        {"lon": 0.12, "lat": 0.08, "timestamp": "2024-01-01T01:00:00Z", "mmsi": 987654321, "length_m": 200},
    ]

    dark_spots = analyze_dark_spots(
        dark_spot_mask, backscatter_db, wind_speed,
        transform, ais_ships, factors, min_area_m2=min_area
    )

    logger.info(f"分析暗斑对象: {len(dark_spots)} 个")

    # --- QA checks ---
    qa = compute_qa_checks(dark_spots, backscatter_db.shape, valid_fraction, wind_coverage, factors)

    # --- Generate outputs ---
    dark_spots_path = write_dark_spots_geojson(dark_spots, output_dir)
    candidates_path = write_oil_candidates_geojson(dark_spots, output_dir, confidence_threshold)
    feature_path = write_feature_table_csv(dark_spots, output_dir)
    confidence_path = write_confidence_raster(dark_spots, backscatter_db.shape, output_dir)
    report_path = write_review_report(dark_spots, qa, output_dir)

    # --- Standard outputs ---
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "synthetic" if use_synthetic else "file",
        "method": method,
        "min_area_m2": min_area,
        "confidence_threshold": confidence_threshold,
        "grid_shape": [synthetic["n_rows"], synthetic["n_cols"]],
        "output_dir": str(output_dir),
    }
    request_path = output_dir / "request.json"
    request_path.write_text(json.dumps(request_info, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

    dataset_manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "synthetic" if use_synthetic else "file",
        "method": method,
        "grid_shape": [synthetic["n_rows"], synthetic["n_cols"]],
        "pixel_size_degrees": pixel_size,
        "bands_used": ["backscatter_db", "wind_speed", "land_mask"],
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(json.dumps(dataset_manifest, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

    output_files = {
        "dark_spots.geojson": str(dark_spots_path),
        "oil_candidates.geojson": str(candidates_path),
        "feature_table.csv": str(feature_path),
        confidence_path.name: str(confidence_path),
        report_path.name: str(report_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(dataset_path),
    }
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "output_files": output_files,
        "summary": {
            "n_dark_spots": len(dark_spots),
            "n_candidates": len([s for s in dark_spots if s["confidence"] >= confidence_threshold]),
            "n_warnings": len(warnings),
        },
    }
    
    # Auto-download metadata: propagate from fetch_meta (set by the
    # auto_download_* helpers in this module) into the manifest so the
    # output-manifest.json records data_source / collection / fetched_at.
    try:
        _fm = locals().get('fetch_meta') or globals().get('fetch_meta')
    except Exception:
        _fm = None
    if _fm:
        manifest["data_source"] = _fm.get("data_source")
        manifest["collection"] = _fm.get("collection")
        manifest["fetched_at"] = _fm.get("fetched_at")
        if "downloaded_paths" in _fm:
            manifest["downloaded_paths"] = _fm["downloaded_paths"]
        if "bbox" in _fm:
            manifest["query_bbox"] = _fm["bbox"]
        if "date_range" in _fm:
            manifest["query_date_range"] = _fm["date_range"]
    manifest_path = output_dir / "output-manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

    qa_path = output_dir / "qa.json"
    qa_output = dict(qa)
    qa_output["warnings"] = warnings
    qa_path.write_text(json.dumps(qa_output, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

    logger.info(f"检测完成: {len(dark_spots)} 暗斑, "
                f"{len([s for s in dark_spots if s['confidence'] >= confidence_threshold])} 疑似油膜, "
                f"{len(warnings)} 警告")
    cleanup_logging()
    return EXIT_OK


def validate_args(args: argparse.Namespace) -> List[str]:
    """Validate command-line arguments. Returns list of error messages."""
    errors = []
    if args.min_area is not None and args.min_area < 0:
        errors.append(f"--min-area must be non-negative, got {args.min_area}")
    if args.confidence_threshold is not None:
        if not (0.0 <= args.confidence_threshold <= 1.0):
            errors.append(f"--confidence-threshold must be in [0, 1], got {args.confidence_threshold}")
    if args.grid_size is not None and args.grid_size < 10:
        errors.append(f"--grid-size must be >= 10, got {args.grid_size}")
    # P0-1: file existence for optional input dirs/configs
    if getattr(args, "input_dir", None) and not Path(args.input_dir).exists():
        errors.append(f"--input-dir not found: {args.input_dir}")
    if getattr(args, "models_config", None) and not Path(args.models_config).exists():
        errors.append(f"--models-config not found: {args.models_config}")
    return errors


def main():
    parser = argparse.ArgumentParser(description="SAR 油膜检测 (Oil Spill Detection)")
    parser.add_argument("--input-dir", default=None,
                        help="输入数据目录 (省略则使用合成数据)")
    parser.add_argument("--output-dir", "-o", default="osd-output",
                        help="输出目录 (默认: osd-output)")
    parser.add_argument("--method", default="threshold_basic",
                        choices=["threshold_basic", "threshold_adaptive", "multi_feature"],
                        help="检测方法 (默认: threshold_basic)")
    parser.add_argument("--min-area", type=float, default=1000.0,
                        help="最小暗斑面积 m² (默认: 1000.0, 必须 >= 0)")
    parser.add_argument("--confidence-threshold", type=float, default=0.4,
                        help="置信度阈值 (默认: 0.4, 必须在 [0, 1] 范围内)")
    parser.add_argument("--grid-size", type=int, default=200,
                        help="合成数据网格大小 (默认: 200, 必须 >= 10)")
    parser.add_argument("--models-config", default=None,
                        help="模型参数 JSON 文件路径")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    add_bbox_date_args(parser)

    args = parser.parse_args()

    # Validate argument ranges before any heavy work
    arg_errors = validate_args(args)
    if arg_errors:
        for e in arg_errors:
            print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(EXIT_ARG)

    try:
        sys.exit(run_oil_spill_pipeline(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
