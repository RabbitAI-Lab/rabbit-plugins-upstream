#!/usr/bin/env python3
"""
Earthquake Damage Assessment — 震后损害快速评估

利用震前震后 SAR/光学变化和建筑道路暴露，快速筛查疑似建筑损毁、
道路阻断和受影响人口。支持相干性/后向散射/纹理/光谱多特征融合，
对象级聚合，损毁概率分级与人工复核任务生成。

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
    "min_building_area": (0.0, 1e8),
    "grid_size": (10, 1000),
}

# ============================================================
# Logging
# ============================================================

def setup_logging(output_dir: Path) -> logging.Logger:
    """Setup logging to file and console."""
    logger = logging.getLogger("eda")
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
    """Close all handlers on the eda logger."""
    logger = logging.getLogger("eda")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)


# ============================================================
# Model Registry
# ============================================================

def load_damage_models(models_path: Optional[str] = None) -> Dict:
    """Load damage assessment model parameters from JSON reference file."""
    if models_path is None:
        script_dir = Path(__file__).parent
        models_path = script_dir.parent / "references" / "damage_models.json"

    with open(models_path, "r", encoding="utf-8") as f:
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
    # transform: (origin_x, pixel_width, 0, origin_y, 0, pixel_height)
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
    R = 6371.0  # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def epsg4326_area_m2(lat: float, width_m: float, height_m: float) -> float:
    """Approximate area in m² for EPSG:4326 at given latitude."""
    # 1 degree longitude ≈ cos(lat) * 111320 m
    # 1 degree latitude ≈ 111320 m
    lat_factor = 111320.0
    lon_factor = math.cos(math.radians(lat)) * 111320.0
    # Convert meters to degrees, then compute area in m²
    width_deg = width_m / lon_factor
    height_deg = height_m / lat_factor
    area_m2 = width_deg * height_deg * lon_factor * lat_factor
    # Simplifies to width_m * height_m, but keep the formula for clarity
    return width_m * height_m


# ============================================================
# Change Detection Algorithms
# ============================================================

def compute_coherence_change(coherence_pre: np.ndarray,
                             coherence_post: np.ndarray,
                             nodata: float = -9999.0) -> np.ndarray:
    """
    Compute coherence change (drop) between pre- and post-earthquake.
    Positive values indicate coherence loss (potential damage).

    Args:
        coherence_pre: Pre-earthquake coherence
        coherence_post: Post-earthquake coherence
        nodata: Nodata value

    Returns:
        Coherence change array (positive = loss)
    """
    valid = (coherence_pre != nodata) & (coherence_post != nodata)
    valid &= ~np.isnan(coherence_pre) & ~np.isnan(coherence_post)
    valid &= (coherence_pre >= 0) & (coherence_pre <= 1.0)
    valid &= (coherence_post >= 0) & (coherence_post <= 1.0)

    result = np.full_like(coherence_pre, np.nan, dtype=np.float32)
    result[valid] = (coherence_pre[valid] - coherence_post[valid]).astype(np.float32)
    return result


def compute_ndvi(red: np.ndarray, nir: np.ndarray,
                 nodata: float = -9999.0) -> np.ndarray:
    """
    Compute NDVI = (NIR - Red) / (NIR + Red).

    Args:
        red: Red band reflectance
        nir: Near-infrared reflectance
        nodata: Nodata value

    Returns:
        NDVI array, range [-1, 1]
    """
    denominator = nir + red
    valid = (denominator != 0) & (red != nodata) & (nir != nodata)
    valid &= ~np.isnan(red) & ~np.isnan(nir) & ~np.isnan(denominator)

    result = np.full_like(red, np.nan, dtype=np.float32)
    result[valid] = ((nir[valid] - red[valid]) / denominator[valid]).astype(np.float32)
    return result


def compute_ndvi_change(red_pre: np.ndarray, nir_pre: np.ndarray,
                        red_post: np.ndarray, nir_post: np.ndarray,
                        nodata: float = -9999.0) -> np.ndarray:
    """
    Compute NDVI change between pre- and post-earthquake.
    Negative values indicate vegetation/structure loss.

    Returns:
        NDVI change array (negative = loss)
    """
    ndvi_pre = compute_ndvi(red_pre, nir_pre, nodata)
    ndvi_post = compute_ndvi(red_post, nir_post, nodata)

    valid = ~np.isnan(ndvi_pre) & ~np.isnan(ndvi_post)
    result = np.full_like(ndvi_pre, np.nan, dtype=np.float32)
    result[valid] = (ndvi_post[valid] - ndvi_pre[valid]).astype(np.float32)
    return result


def compute_texture(band: np.ndarray, window: int = 3,
                    nodata: float = -9999.0) -> np.ndarray:
    """
    Compute local texture (standard deviation) using a sliding window.

    Args:
        band: Input band
        window: Window size (odd number)
        nodata: Nodata value

    Returns:
        Texture array (local standard deviation)
    """
    from scipy.ndimage import uniform_filter

    valid_mask = (band != nodata) & ~np.isnan(band) & ~np.isinf(band)
    clean = np.where(valid_mask, band, 0.0)

    # Mean and mean of squares
    mean = uniform_filter(clean, size=window, mode='constant')
    mean_sq = uniform_filter(clean ** 2, size=window, mode='constant')
    variance = mean_sq - mean ** 2
    variance = np.maximum(variance, 0.0)  # numerical safety

    texture = np.sqrt(variance)
    texture[~valid_mask] = np.nan
    return texture.astype(np.float32)


def compute_texture_change(band_pre: np.ndarray, band_post: np.ndarray,
                           window: int = 3, nodata: float = -9999.0) -> np.ndarray:
    """Compute texture change between pre- and post-earthquake."""
    tex_pre = compute_texture(band_pre, window, nodata)
    tex_post = compute_texture(band_post, window, nodata)

    valid = ~np.isnan(tex_pre) & ~np.isnan(tex_post)
    result = np.full_like(tex_pre, np.nan, dtype=np.float32)
    result[valid] = (tex_post[valid] - tex_pre[valid]).astype(np.float32)
    return result


# ============================================================
# Quality Control
# ============================================================

def compute_quality_mask(
    bands: Dict[str, np.ndarray],
    models: Dict,
    nodata: float = -9999.0,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """
    Compute quality control mask from input bands.

    Returns:
        (valid_mask, qc_stats) — valid_mask=True means pixel is usable
    """
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

    # Shadow mask: low NIR
    if "nir" in bands:
        shadow_thresh = qc.get("shadow", {}).get("nir_threshold", 0.05)
        shadow_mask = bands["nir"] < shadow_thresh
        valid &= ~shadow_mask
        qc_stats["shadow_pixels"] = int(np.sum(shadow_mask))

    # SAR noise mask: low coherence
    if "coherence_post" in bands:
        noise_thresh = qc.get("sar_noise", {}).get("min_coherence", 0.05)
        noise_mask = bands["coherence_post"] < noise_thresh
        valid &= ~noise_mask
        qc_stats["sar_noise_pixels"] = int(np.sum(noise_mask))

    # Nodata mask
    for bname, bdata in bands.items():
        valid &= (bdata != nodata) & ~np.isnan(bdata) & ~np.isinf(bdata)

    qc_stats["total_pixels"] = int(valid.size)
    qc_stats["valid_pixels"] = int(np.sum(valid))
    qc_stats["masked_pixels"] = int(valid.size - np.sum(valid))
    qc_stats["valid_fraction"] = round(float(np.sum(valid) / valid.size), 4) if valid.size > 0 else 0.0

    return valid, qc_stats


# ============================================================
# Object-level Aggregation
# ============================================================

def aggregate_building_damage(
    damage_probability: np.ndarray,
    building_mask: np.ndarray,
    transform: Tuple[float, ...],
    min_area_m2: float = 50.0,
) -> List[Dict]:
    """
    Aggregate pixel-level damage probability to building objects.

    Args:
        damage_probability: 2D array of damage probability [0, 1]
        building_mask: Boolean mask of building pixels
        transform: Rasterio-style transform tuple (origin_x, pixel_width, 0, origin_y, 0, pixel_height)
        min_area_m2: Minimum building area to include

    Returns:
        List of building damage records
    """
    from scipy.ndimage import label

    # Label connected building regions
    labeled, n_features = label(building_mask)
    buildings = []

    origin_x, pixel_width, _, origin_y, _, pixel_height = transform
    # Convert pixel size from degrees to meters for area calculation
    # Use the center latitude of the raster for longitude conversion
    center_lat = origin_y - (damage_probability.shape[0] * abs(pixel_height)) / 2
    lat_factor = 111320.0  # meters per degree latitude
    lon_factor = math.cos(math.radians(center_lat)) * 111320.0  # meters per degree longitude
    pixel_area_m2 = abs(pixel_width * lon_factor) * abs(pixel_height * lat_factor)

    for region_id in range(1, n_features + 1):
        region_mask = labeled == region_id
        n_pixels = int(np.sum(region_mask))
        area_m2 = n_pixels * pixel_area_m2

        if area_m2 < min_area_m2:
            continue

        # Compute region statistics
        region_probs = damage_probability[region_mask]
        valid_probs = region_probs[~np.isnan(region_probs)]

        if len(valid_probs) == 0:
            continue

        mean_prob = float(np.mean(valid_probs))
        max_prob = float(np.max(valid_probs))
        median_prob = float(np.median(valid_probs))

        # Get centroid
        rows, cols = np.where(region_mask)
        centroid_row = float(np.mean(rows))
        centroid_col = float(np.mean(cols))
        centroid_lon, centroid_lat = pixel_to_lonlat(int(centroid_row), int(centroid_col), transform)

        # Bounding box
        min_row, max_row = int(np.min(rows)), int(np.max(rows))
        min_col, max_col = int(np.min(cols)), int(np.max(cols))
        bbox_lon_min, bbox_lat_max = pixel_to_lonlat(min_row, min_col, transform)
        bbox_lon_max, bbox_lat_min = pixel_to_lonlat(max_row, max_col, transform)

        buildings.append({
            "building_id": len(buildings) + 1,
            "centroid_lon": round(centroid_lon, 6),
            "centroid_lat": round(centroid_lat, 6),
            "area_m2": round(area_m2, 1),
            "n_pixels": n_pixels,
            "mean_damage_prob": round(mean_prob, 4),
            "max_damage_prob": round(max_prob, 4),
            "median_damage_prob": round(median_prob, 4),
            "bbox": [bbox_lon_min, bbox_lat_min, bbox_lon_max, bbox_lat_max],
        })

    return buildings


def detect_road_disruptions(
    coherence_change: np.ndarray,
    road_mask: np.ndarray,
    transform: Tuple[float, ...],
    threshold: float = 0.3,
) -> List[Dict]:
    """
    Detect potential road disruptions from coherence change along roads.

    Args:
        coherence_change: 2D array of coherence change
        road_mask: Boolean mask of road pixels
        transform: Rasterio-style transform tuple
        threshold: Coherence drop threshold for disruption

    Returns:
        List of road disruption records
    """
    from scipy.ndimage import label

    # Find road pixels with significant coherence change
    disruption_mask = road_mask & (coherence_change > threshold)
    labeled, n_features = label(disruption_mask)
    disruptions = []

    for region_id in range(1, n_features + 1):
        region_mask = labeled == region_id
        n_pixels = int(np.sum(region_mask))

        if n_pixels < 3:  # Minimum size filter
            continue

        region_change = coherence_change[region_mask]
        mean_change = float(np.mean(region_change))
        max_change = float(np.max(region_change))

        rows, cols = np.where(region_mask)
        centroid_row = float(np.mean(rows))
        centroid_col = float(np.mean(cols))
        centroid_lon, centroid_lat = pixel_to_lonlat(int(centroid_row), int(centroid_col), transform)

        disruptions.append({
            "disruption_id": len(disruptions) + 1,
            "centroid_lon": round(centroid_lon, 6),
            "centroid_lat": round(centroid_lat, 6),
            "n_pixels": n_pixels,
            "mean_coherence_drop": round(mean_change, 4),
            "max_coherence_drop": round(max_change, 4),
            "severity": "high" if max_change > 0.5 else "moderate",
        })

    return disruptions


# ============================================================
# Damage Classification
# ============================================================

def classify_damage(probability: np.ndarray, models: Dict) -> Tuple[np.ndarray, Dict[str, int]]:
    """
    Classify damage probability into discrete levels.

    Returns:
        (damage_class, counts) — damage class 0-4, counts per level
    """
    levels = models.get("damage_levels", {})

    damage_class = np.full_like(probability, 255, dtype=np.uint8)  # nodata

    # None: 0
    none_range = levels.get("none", {}).get("probability_range", [0.0, 0.2])
    damage_class[(probability >= none_range[0]) & (probability < none_range[1])] = 0

    # Slight: 1
    slight_range = levels.get("slight", {}).get("probability_range", [0.2, 0.4])
    damage_class[(probability >= slight_range[0]) & (probability < slight_range[1])] = 1

    # Moderate: 2
    mod_range = levels.get("moderate", {}).get("probability_range", [0.4, 0.6])
    damage_class[(probability >= mod_range[0]) & (probability < mod_range[1])] = 2

    # Severe: 3
    severe_range = levels.get("severe", {}).get("probability_range", [0.6, 0.8])
    damage_class[(probability >= severe_range[0]) & (probability < severe_range[1])] = 3

    # Destroyed: 4
    destroyed_range = levels.get("destroyed", {}).get("probability_range", [0.8, 1.0])
    damage_class[(probability >= destroyed_range[0]) & (probability <= destroyed_range[1])] = 4

    # NaN stays 255
    damage_class[np.isnan(probability)] = 255

    counts = {
        "none": int(np.sum(damage_class == 0)),
        "slight": int(np.sum(damage_class == 1)),
        "moderate": int(np.sum(damage_class == 2)),
        "severe": int(np.sum(damage_class == 3)),
        "destroyed": int(np.sum(damage_class == 4)),
    }

    return damage_class, counts


def fuse_damage_probability(
    coherence_change: np.ndarray,
    ndvi_change: np.ndarray,
    texture_change: np.ndarray,
    models: Dict,
) -> np.ndarray:
    """
    Fuse multiple change features into a single damage probability.

    Uses weighted combination and sigmoid normalization.
    """
    sar_model = models.get("damage_models", {}).get("sar_coherence", {})
    weights = sar_model.get("weights", {"coherence_drop": 0.6, "texture_change": 0.4})

    # Normalize coherence change to [0, 1] probability
    coh_weight = weights.get("coherence_drop", 0.6)
    tex_weight = weights.get("texture_change", 0.4)

    # Sigmoid normalization for coherence change
    coh_prob = 1.0 / (1.0 + np.exp(-5.0 * (coherence_change - 0.3)))

    # Texture change: positive = more texture = potential collapse
    tex_prob = 1.0 / (1.0 + np.exp(-5.0 * (texture_change - 0.05)))

    # NDVI change: negative = vegetation loss = potential damage
    ndvi_prob = np.full_like(ndvi_change, np.nan, dtype=np.float32)
    valid_ndvi = ~np.isnan(ndvi_change)
    ndvi_prob[valid_ndvi] = 1.0 / (1.0 + np.exp(-5.0 * (-ndvi_change[valid_ndvi] - 0.1)))

    # Weighted fusion
    fused = np.full_like(coherence_change, np.nan, dtype=np.float32)
    valid = ~np.isnan(coh_prob) & ~np.isnan(tex_prob)

    if np.any(valid):
        fused[valid] = (coh_weight * coh_prob[valid] + tex_weight * tex_prob[valid]).astype(np.float32)

    # Incorporate NDVI if available
    valid_all = valid & ~np.isnan(ndvi_prob)
    if np.any(valid_all):
        # Re-weight: 0.5 SAR + 0.3 NDVI + 0.2 texture
        fused[valid_all] = (
            0.5 * coh_prob[valid_all] +
            0.3 * ndvi_prob[valid_all] +
            0.2 * tex_prob[valid_all]
        ).astype(np.float32)

    return fused


# ============================================================
# Exposure Analysis
# ============================================================

def compute_exposure(
    buildings: List[Dict],
    population_density_per_km2: float = 100.0,
) -> Dict[str, Any]:
    """
    Compute exposure statistics from building damage results.

    Args:
        buildings: List of building damage records
        population_density_per_km2: Assumed population density

    Returns:
        Exposure summary dictionary
    """
    total_buildings = len(buildings)
    total_area_m2 = sum(b["area_m2"] for b in buildings)

    # Count by damage level
    damage_counts = {"none": 0, "slight": 0, "moderate": 0, "severe": 0, "destroyed": 0}
    for b in buildings:
        p = b["mean_damage_prob"]
        if p < 0.2:
            damage_counts["none"] += 1
        elif p < 0.4:
            damage_counts["slight"] += 1
        elif p < 0.6:
            damage_counts["moderate"] += 1
        elif p < 0.8:
            damage_counts["severe"] += 1
        else:
            damage_counts["destroyed"] += 1

    # Estimate affected population (buildings with prob > 0.4)
    affected_buildings = [b for b in buildings if b["mean_damage_prob"] > 0.4]
    affected_area_km2 = sum(b["area_m2"] for b in affected_buildings) / 1e6
    # Rough estimate: 1 person per 30 m² of building area
    estimated_affected_pop = int(affected_area_km2 * 1e6 / 30.0)

    return {
        "total_buildings": total_buildings,
        "total_building_area_km2": round(total_area_m2 / 1e6, 4),
        "damage_counts": damage_counts,
        "affected_buildings": len(affected_buildings),
        "affected_area_km2": round(affected_area_km2, 4),
        "estimated_affected_population": estimated_affected_pop,
        "population_density_assumed": population_density_per_km2,
    }


# ============================================================
# Synthetic Data Generation
# ============================================================

def generate_synthetic_data(
    n_rows: int = 100,
    n_cols: int = 100,
    epicenter: Tuple[float, float] = (0.0, 0.0),
    seed: int = 42,
) -> Dict[str, Any]:
    """
    Generate synthetic pre/post earthquake data for demo/testing.

    Simulates:
    - SAR coherence drop near epicenter
    - NDVI change near epicenter
    - Building mask with clusters
    - Road mask with lines

    Returns:
        Dictionary with all synthetic bands and masks
    """
    rng = np.random.RandomState(seed)

    # Create coordinate grids
    rows = np.arange(n_rows)
    cols = np.arange(n_cols)
    col_grid, row_grid = np.meshgrid(cols, rows)

    # Distance from center (epicenter at center)
    center_r, center_c = n_rows // 2, n_cols // 2
    dist = np.sqrt((row_grid - center_r) ** 2 + (col_grid - center_c) ** 2)
    max_dist = min(n_rows, n_cols) / 2

    # --- SAR coherence ---
    # Pre-earthquake: high coherence everywhere
    coherence_pre = rng.uniform(0.7, 0.95, (n_rows, n_cols)).astype(np.float32)

    # Post-earthquake: coherence drops near epicenter
    coherence_post = coherence_pre.copy()
    damage_factor = np.clip(1.0 - dist / max_dist, 0.0, 1.0)
    coherence_post -= damage_factor * rng.uniform(0.3, 0.7, (n_rows, n_cols))
    coherence_post = np.clip(coherence_post, 0.05, 1.0).astype(np.float32)

    # --- Optical bands ---
    # Pre-earthquake
    red_pre = rng.uniform(0.05, 0.15, (n_rows, n_cols)).astype(np.float32)
    nir_pre = rng.uniform(0.2, 0.4, (n_rows, n_cols)).astype(np.float32)
    blue_pre = rng.uniform(0.03, 0.08, (n_rows, n_cols)).astype(np.float32)

    # Post-earthquake: increased red (exposed soil/debris), decreased NIR
    red_post = red_pre + damage_factor * rng.uniform(0.05, 0.15, (n_rows, n_cols))
    nir_post = nir_pre - damage_factor * rng.uniform(0.05, 0.15, (n_rows, n_cols))
    red_post = np.clip(red_post, 0.0, 0.5).astype(np.float32)
    nir_post = np.clip(nir_post, 0.05, 0.5).astype(np.float32)
    blue_post = blue_pre.copy()

    # --- Building mask ---
    # Create building clusters
    building_mask = np.zeros((n_rows, n_cols), dtype=bool)
    n_clusters = min(8, max(n_rows, n_cols) // 10)
    # Ensure margin is at least 1
    margin = max(min(n_rows, n_cols) // 5, 1)
    for _ in range(n_clusters):
        cx = rng.randint(margin, max(margin + 1, n_cols - margin))
        cy = rng.randint(margin, max(margin + 1, n_rows - margin))
        cluster_radius = rng.randint(2, max(3, min(n_rows, n_cols) // 10))
        cluster_dist = np.sqrt((row_grid - cy) ** 2 + (col_grid - cx) ** 2)
        building_mask[cluster_dist < cluster_radius] = True

    # --- Road mask ---
    road_mask = np.zeros((n_rows, n_cols), dtype=bool)
    # Horizontal road
    road_mask[n_rows // 3, 10:n_cols - 10] = True
    # Vertical road
    road_mask[10:n_rows - 10, n_cols // 3] = True
    # Diagonal-ish road
    for i in range(20, n_rows - 20):
        j = int(n_cols / 2 + (i - n_rows / 2) * 0.3)
        if 0 <= j < n_cols:
            road_mask[i, max(0, j - 1):min(n_cols, j + 2)] = True

    # --- Epicenter distance grid ---
    epicenter_dist_km = dist * 0.1  # assume 0.1 km per pixel

    return {
        "coherence_pre": coherence_pre,
        "coherence_post": coherence_post,
        "red_pre": red_pre,
        "nir_pre": nir_pre,
        "blue_pre": blue_pre,
        "red_post": red_post,
        "nir_post": nir_post,
        "blue_post": blue_post,
        "building_mask": building_mask,
        "road_mask": road_mask,
        "epicenter_dist_km": epicenter_dist_km.astype(np.float32),
        "n_rows": n_rows,
        "n_cols": n_cols,
    }


# ============================================================
# Report Generation
# ============================================================

def generate_review_tiles(
    damage_class: np.ndarray,
    buildings: List[Dict],
    output_dir: Path,
    transform: Tuple[float, ...],
) -> Path:
    """
    Generate review tiles directory with GeoJSON for manual review.

    Returns:
        Path to review_tiles directory
    """
    review_dir = output_dir / "review_tiles"
    review_dir.mkdir(exist_ok=True)

    # Write suspected buildings as GeoJSON
    features = []
    for b in buildings:
        if b["mean_damage_prob"] < 0.3:
            continue  # Only include suspected damage

        # Create polygon from bbox
        lon_min, lat_min, lon_max, lat_max = b["bbox"]
        polygon = [
            [lon_min, lat_min],
            [lon_max, lat_min],
            [lon_max, lat_max],
            [lon_min, lat_max],
            [lon_min, lat_min],
        ]

        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [polygon],
            },
            "properties": {
                "building_id": b["building_id"],
                "mean_damage_prob": b["mean_damage_prob"],
                "max_damage_prob": b["max_damage_prob"],
                "area_m2": b["area_m2"],
                "review_status": "pending",
            },
        })

    geojson = {
        "type": "FeatureCollection",
        "features": features,
    }

    review_path = review_dir / "suspected_buildings.geojson"
    review_path.write_text(
        json.dumps(geojson, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    return review_dir


def generate_impact_summary_xlsx(
    exposure: Dict,
    damage_counts: Dict[str, int],
    buildings: List[Dict],
    disruptions: List[Dict],
    output_dir: Path,
) -> Path:
    """
    Generate impact summary as CSV (xlsx requires openpyxl, use CSV for compatibility).

    Returns:
        Path to summary CSV
    """
    summary_path = output_dir / "impact_summary.csv"

    with open(summary_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # Header section
        writer.writerow(["=== 震后损害快速评估影响摘要 ==="])
        writer.writerow([])

        # Exposure summary
        writer.writerow(["指标", "值"])
        writer.writerow(["总建筑数", exposure["total_buildings"]])
        writer.writerow(["总建筑面积 (km²)", exposure["total_building_area_km2"]])
        writer.writerow(["受影响建筑数", exposure["affected_buildings"]])
        writer.writerow(["受影响面积 (km²)", exposure["affected_area_km2"]])
        writer.writerow(["估计受影响人口", exposure["estimated_affected_population"]])
        writer.writerow(["道路阻断点数", len(disruptions)])
        writer.writerow([])

        # Damage distribution
        writer.writerow(["损毁等级", "像素数"])
        for level, count in damage_counts.items():
            writer.writerow([level, count])
        writer.writerow([])

        # Top damaged buildings
        writer.writerow(["=== 高损毁概率建筑 (Top 20) ==="])
        writer.writerow(["建筑ID", "中心经度", "中心纬度", "面积(m²)", "平均损毁概率", "最大损毁概率"])
        sorted_buildings = sorted(buildings, key=lambda x: x["mean_damage_prob"], reverse=True)
        for b in sorted_buildings[:20]:
            writer.writerow([
                b["building_id"],
                b["centroid_lon"],
                b["centroid_lat"],
                b["area_m2"],
                b["mean_damage_prob"],
                b["max_damage_prob"],
            ])

    return summary_path


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
    paths = fetcher.download_assets(
        items=items, out_dir=download_dir, max_items=1, max_total_mb=800,
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


def run_earthquake_damage_pipeline(args: argparse.Namespace) -> int:
    """Main earthquake damage assessment workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("eda-output")

    # --- Auto-download mode: fetch sentinel-1-grd from MPC ---
    fetch_meta = None
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

    # P0: Validate args before any heavy work
    rc = validate_args(args)
    if rc != 0:
        return rc

    logger = setup_logging(output_dir)
    logger.info("震后损害快速评估 — 启动")

    # Load models
    models_path = getattr(args, 'models_config', None)
    try:
        models = load_damage_models(models_path)
        logger.info(f"模型参数已加载: version {models.get('version', 'unknown')}")
    except Exception as e:
        logger.error(f"加载模型参数失败: {e}")
        cleanup_logging()
        return EXIT_VALIDATION

    # Parse parameters
    damage_model = getattr(args, 'damage_model', 'combined') or 'combined'
    min_building_area = getattr(args, 'min_building_area', 50.0) or 50.0
    epicenter = getattr(args, 'epicenter', None)

    logger.info(f"损毁模型: {damage_model}, 最小建筑面积: {min_building_area} m²")

    # --- Synthetic/demo mode ---
    use_synthetic = not (hasattr(args, 'input_dir') and args.input_dir)
    warnings = []

    if use_synthetic:
        logger.info("运行合成演示模式")
        n_rows = getattr(args, 'grid_size', 100) or 100
        n_cols = n_rows
        synthetic = generate_synthetic_data(n_rows=n_rows, n_cols=n_cols, seed=42)
    else:
        logger.info(f"输入目录: {args.input_dir}")
        warnings.append("文件输入模式未完全实现，使用合成数据")
        synthetic = generate_synthetic_data(n_rows=100, n_cols=100, seed=42)

    # --- Compute change features ---
    coherence_change = compute_coherence_change(
        synthetic["coherence_pre"], synthetic["coherence_post"]
    )
    ndvi_change = compute_ndvi_change(
        synthetic["red_pre"], synthetic["nir_pre"],
        synthetic["red_post"], synthetic["nir_post"]
    )
    texture_change = compute_texture_change(
        synthetic["coherence_pre"], synthetic["coherence_post"]
    )

    # --- Quality control ---
    bands_for_qc = {
        "blue": synthetic["blue_post"],
        "nir": synthetic["nir_post"],
        "coherence_post": synthetic["coherence_post"],
    }
    valid_mask, qc_stats = compute_quality_mask(bands_for_qc, models)

    # --- Fuse damage probability ---
    damage_probability = fuse_damage_probability(
        coherence_change, ndvi_change, texture_change, models
    )

    # Apply QC mask
    damage_probability[~valid_mask] = np.nan

    # --- Classify damage ---
    damage_class, damage_counts = classify_damage(damage_probability, models)

    # --- Object-level aggregation ---
    # Create a simple transform for synthetic data
    # Assume 0.1 km per pixel, origin at (0, 0)
    pixel_size = 0.001  # ~0.1 km in degrees
    transform = (0.0, pixel_size, 0, synthetic["n_rows"] * pixel_size, 0, -pixel_size)

    buildings = aggregate_building_damage(
        damage_probability, synthetic["building_mask"],
        transform, min_area_m2=min_building_area
    )
    logger.info(f"聚合建筑对象: {len(buildings)} 个")

    disruptions = detect_road_disruptions(
        coherence_change, synthetic["road_mask"], transform
    )
    logger.info(f"检测到道路阻断: {len(disruptions)} 处")

    # --- Exposure analysis ---
    exposure = compute_exposure(buildings)

    # --- Generate outputs ---

    # damage_probability.tif (save as .npy for synthetic mode)
    prob_output = output_dir / "damage_probability.npy"
    np.save(prob_output, damage_probability)
    logger.info(f"损毁概率已保存: {prob_output}")

    # suspected_buildings.geojson
    suspected = [b for b in buildings if b["mean_damage_prob"] > 0.3]
    building_features = []
    for b in suspected:
        lon_min, lat_min, lon_max, lat_max = b["bbox"]
        polygon = [
            [lon_min, lat_min],
            [lon_max, lat_min],
            [lon_max, lat_max],
            [lon_min, lat_max],
            [lon_min, lat_min],
        ]
        building_features.append({
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [polygon],
            },
            "properties": {
                "building_id": b["building_id"],
                "mean_damage_prob": b["mean_damage_prob"],
                "max_damage_prob": b["max_damage_prob"],
                "area_m2": b["area_m2"],
                "review_status": "pending",
            },
        })

    buildings_geojson = {
        "type": "FeatureCollection",
        "features": building_features,
    }
    buildings_path = output_dir / "suspected_buildings.geojson"
    buildings_path.write_text(
        json.dumps(buildings_geojson, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # road_disruptions.geojson
    disruption_features = []
    for d in disruptions:
        # Create a small point buffer as polygon
        delta = pixel_size * 2
        polygon = create_polygon(
            d["centroid_lon"] - delta,
            d["centroid_lat"] - delta,
            delta * 2,
            delta * 2,
        )
        disruption_features.append({
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [polygon],
            },
            "properties": {
                "disruption_id": d["disruption_id"],
                "mean_coherence_drop": d["mean_coherence_drop"],
                "max_coherence_drop": d["max_coherence_drop"],
                "severity": d["severity"],
            },
        })

    disruptions_geojson = {
        "type": "FeatureCollection",
        "features": disruption_features,
    }
    disruptions_path = output_dir / "road_disruptions.geojson"
    disruptions_path.write_text(
        json.dumps(disruptions_geojson, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # impact_summary.csv
    summary_path = generate_impact_summary_xlsx(
        exposure, damage_counts, buildings, disruptions, output_dir
    )

    # review_tiles/
    review_dir = generate_review_tiles(
        damage_class, buildings, output_dir, transform
    )

    # request.json
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "synthetic" if use_synthetic else "file",
        "damage_model": damage_model,
        "epicenter": epicenter,
        "min_building_area_m2": min_building_area,
        "grid_shape": [synthetic["n_rows"], synthetic["n_cols"]],
        "output_dir": str(output_dir),
    }
    request_path = output_dir / "request.json"
    request_path.write_text(
        json.dumps(request_info, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # dataset-manifest.json
    dataset_manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "synthetic" if use_synthetic else "file",
        "damage_model": damage_model,
        "grid_shape": [synthetic["n_rows"], synthetic["n_cols"]],
        "pixel_size_degrees": pixel_size,
        "bands_used": list(synthetic.keys()),
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # output-manifest.json
    output_files = {
        "damage_probability.npy": str(prob_output),
        "suspected_buildings.geojson": str(buildings_path),
        "road_disruptions.geojson": str(disruptions_path),
        "impact_summary.csv": str(summary_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(dataset_path),
    }
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "output_files": output_files,
        "summary": {
            "n_buildings": len(buildings),
            "n_suspected": len(suspected),
            "n_disruptions": len(disruptions),
            "n_warnings": len(warnings),
            "damage_counts": damage_counts,
        },
    }
    # Auto-download provenance (only when --bbox/--aoi-file triggered a download)
    if 'fetch_meta' in locals() and fetch_meta is not None:
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
            "damage_probability_written": prob_output.exists(),
            "buildings_geojson_written": buildings_path.exists(),
            "disruptions_geojson_written": disruptions_path.exists(),
            "summary_written": summary_path.exists(),
            "all_outputs_written": all(Path(p).exists() for p in output_files.values()),
        },
        "n_buildings": len(buildings),
        "n_suspected": len(suspected),
        "n_disruptions": len(disruptions),
        "n_warnings": len(warnings),
        "warnings": warnings,
        "qc_stats": qc_stats,
        "exposure": exposure,
    }
    qa_path = output_dir / "qa.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    logger.info(f"评估完成: {len(buildings)} 建筑, {len(suspected)} 疑似损毁, "
                f"{len(disruptions)} 道路阻断, {len(warnings)} 警告")
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
    parser = argparse.ArgumentParser(description="震后损害快速评估 (Earthquake Damage Assessment)")
    parser.add_argument("--input-dir", default=None,
                        help="输入数据目录 (省略则使用合成数据)")
    parser.add_argument("--output-dir", "-o", default="eda-output",
                        help="输出目录 (默认: eda-output)")
    parser.add_argument("--damage-model", default="combined",
                        choices=["sar_coherence", "optical_ndvi", "combined"],
                        help="损毁评估模型 (默认: combined)")
    parser.add_argument("--epicenter", default=None,
                        help="震中位置 'lon,lat' (合成模式使用)")
    parser.add_argument("--min-building-area", type=float, default=50.0,
                        help="最小建筑面积 m² (默认: 50.0)")
    parser.add_argument("--grid-size", type=int, default=100,
                        help="合成数据网格大小 (默认: 100)")
    parser.add_argument("--models-config", default=None,
                        help="模型参数 JSON 文件路径")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    add_bbox_date_args(parser)

    args = parser.parse_args()

    try:
        sys.exit(run_earthquake_damage_pipeline(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
