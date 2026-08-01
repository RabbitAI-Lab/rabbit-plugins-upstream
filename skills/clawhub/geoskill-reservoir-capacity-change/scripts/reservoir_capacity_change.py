#!/usr/bin/env python3
"""
Reservoir Capacity Change - Multi-temporal reservoir storage analysis.

Combines multi-period water surface, DEM, and water level data to establish
level-area-storage relationships, monitoring capacity change and sedimentation.

Exit codes:
    0 = success
    2 = argument error
    3 = dependency missing
    6 = data validation failure
    7 = processing failure
"""

import argparse
import csv
import json
import logging
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

# Default parameters
DEFAULT_CURVE_METHOD = "trapezoidal"
DEFAULT_CONFIDENCE_LEVEL = 0.95
DEFAULT_DEM_ERROR_M = 5.0  # DEM vertical error (meters)
DEFAULT_WATER_LEVEL_ERROR_M = 0.3  # Water level error (meters)
DEFAULT_WATER_BODY_ERROR_PX = 1.0  # Water boundary error (pixels)

# ============================================================
# Logging
# ============================================================

def setup_logging(output_dir: Path) -> logging.Logger:
    """Setup logging to file and console."""
    logger = logging.getLogger("rcc")
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
    """Close all handlers on the rcc logger."""
    logger = logging.getLogger("rcc")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)


# ============================================================
# Geometry Helpers
# ============================================================

def create_polygon(x: float, y: float, w: float, h: float) -> Dict:
    """Create a simple polygon geometry dict (x, y, width, height)."""
    return {
        "type": "Polygon",
        "coordinates": [[
            [x, y],
            [x + w, y],
            [x + w, y + h],
            [x, y + h],
            [x, y],
        ]],
    }


# ============================================================
# Pixel Area Computation
# ============================================================

def compute_pixel_area_m2(transform=None, crs=None, bbox=None, n_rows=None, n_cols=None) -> float:
    """
    Compute pixel area in square meters.

    Handles projected and geographic CRS.
    """
    if transform is not None and crs is not None:
        try:
            if hasattr(crs, 'is_projected') and crs.is_projected:
                return abs(float(transform.a) * float(transform.e))
        except Exception:
            pass

    # Geographic CRS or fallback
    if bbox is not None and n_rows is not None and n_cols is not None:
        xmin, ymin, xmax, ymax = bbox
        center_lat = (ymin + ymax) / 2.0
        lat_rad = np.radians(min(abs(center_lat), 85.0))
        width_m = (xmax - xmin) * 111320.0 * np.cos(lat_rad)
        height_m = (ymax - ymin) * 111320.0
        return (width_m / n_cols) * (height_m / n_rows)

    if transform is not None:
        try:
            pixel_width_deg = abs(float(transform.a))
            pixel_height_deg = abs(float(transform.e))
            center_lat = abs(float(transform.f) + float(transform.e) * 100)
            lat_rad = np.radians(min(center_lat, 85.0))
            return (pixel_height_deg * 111320.0) * (pixel_width_deg * 111320.0 * np.cos(lat_rad))
        except Exception:
            pass

    # Fallback: assume 30m pixels
    return 900.0  # 30m x 30m


# ============================================================
# Core Algorithms: Area and Storage Curves
# ============================================================

def compute_area_at_level(dem: np.ndarray, level: float, pixel_area_m2: float,
                          nodata: float = -9999.0) -> float:
    """
    Compute water surface area at a given elevation level.

    Pixels with elevation <= level are considered inundated.

    Args:
        dem: 2D elevation array
        level: Water surface elevation (m)
        pixel_area_m2: Area per pixel in m²
        nodata: Nodata value in DEM

    Returns:
        Water surface area in m²
    """
    valid = dem != nodata
    inundated = valid & (dem <= level)
    return float(np.sum(inundated)) * pixel_area_m2


def compute_storage_at_level(dem: np.ndarray, level: float, pixel_area_m2: float,
                             nodata: float = -9999.0) -> float:
    """
    Compute water storage volume at a given elevation level.

    Uses prism method: for each inundated pixel, volume = (level - elevation) * pixel_area.

    Args:
        dem: 2D elevation array
        level: Water surface elevation (m)
        pixel_area_m2: Area per pixel in m²
        nodata: Nodata value in DEM

    Returns:
        Storage volume in m³
    """
    valid = dem != nodata
    inundated = valid & (dem <= level)
    if not np.any(inundated):
        return 0.0
    depths = level - dem[inundated]
    depths = np.maximum(depths, 0.0)  # Safety clamp
    return float(np.sum(depths)) * pixel_area_m2


def compute_area_storage_curve(dem: np.ndarray, levels: np.ndarray,
                               pixel_area_m2: float,
                               nodata: float = -9999.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute elevation-area-storage curve.

    Args:
        dem: 2D elevation array
        levels: 1D array of elevation levels (sorted ascending)
        pixel_area_m2: Area per pixel in m²
        nodata: Nodata value in DEM

    Returns:
        Tuple of (areas, storages) arrays in m² and m³
    """
    n = len(levels)
    areas = np.zeros(n, dtype=np.float64)
    storages = np.zeros(n, dtype=np.float64)

    for i, level in enumerate(levels):
        areas[i] = compute_area_at_level(dem, level, pixel_area_m2, nodata)
        storages[i] = compute_storage_at_level(dem, level, pixel_area_m2, nodata)

    # Enforce monotonicity (non-decreasing)
    for i in range(1, n):
        if areas[i] < areas[i - 1]:
            areas[i] = areas[i - 1]
        if storages[i] < storages[i - 1]:
            storages[i] = storages[i - 1]

    return areas, storages


def compute_curve_trapezoidal(dem: np.ndarray, levels: np.ndarray,
                              pixel_area_m2: float,
                              nodata: float = -9999.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute area-storage curve using trapezoidal integration.

    Area at each level is computed directly from pixel counting.
    Storage is integrated from area curve using trapezoidal rule.

    Args:
        dem: 2D elevation array
        levels: 1D array of elevation levels (sorted ascending)
        pixel_area_m2: Area per pixel in m²
        nodata: Nodata value in DEM

    Returns:
        Tuple of (areas, storages) arrays
    """
    n = len(levels)
    areas = np.zeros(n, dtype=np.float64)
    storages = np.zeros(n, dtype=np.float64)

    for i, level in enumerate(levels):
        areas[i] = compute_area_at_level(dem, level, pixel_area_m2, nodata)

    # Trapezoidal integration: V(h) = integral of A(h) dh
    for i in range(1, n):
        dh = levels[i] - levels[i - 1]
        avg_area = (areas[i] + areas[i - 1]) / 2.0
        storages[i] = storages[i - 1] + avg_area * dh

    return areas, storages


# ============================================================
# Water Extent Analysis
# ============================================================

def compute_water_extent_timeseries(water_masks: List[np.ndarray],
                                    dates: List[str],
                                    pixel_area_m2: float,
                                    nodata: int = 0) -> List[Dict[str, Any]]:
    """
    Compute water extent time series from binary water masks.

    Args:
        water_masks: List of 2D binary arrays (1=water, 0=non-water)
        dates: List of date strings corresponding to each mask
        pixel_area_m2: Area per pixel in m²
        nodata: Nodata value

    Returns:
        List of dicts with date, pixel_count, area_m2, area_km2
    """
    timeseries = []
    for mask, date in zip(water_masks, dates):
        if nodata != 0:
            valid = mask != nodata
        else:
            valid = np.ones_like(mask, dtype=bool)
        water_pixels = int(np.sum((mask == 1) & valid))
        area_m2 = water_pixels * pixel_area_m2
        timeseries.append({
            "date": date,
            "water_pixels": water_pixels,
            "area_m2": round(area_m2, 2),
            "area_km2": round(area_m2 / 1e6, 6),
        })
    return timeseries


# ============================================================
# Change Detection
# ============================================================

def compute_relative_storage_change(curve1_areas: np.ndarray,
                                    curve1_storages: np.ndarray,
                                    curve2_areas: np.ndarray,
                                    curve2_storages: np.ndarray,
                                    levels: np.ndarray) -> Dict[str, Any]:
    """
    Compute relative storage change between two curves at same levels.

    Args:
        curve1_areas: Area array for period 1
        curve1_storages: Storage array for period 1
        curve2_areas: Area array for period 2
        curve2_storages: Storage array for period 2
        levels: Elevation levels

    Returns:
        Dict with relative change analysis
    """
    assert len(curve1_areas) == len(levels)
    assert len(curve2_areas) == len(levels)

    area_diff = curve2_areas - curve1_areas
    storage_diff = curve2_storages - curve1_storages

    # Relative change (%)
    with np.errstate(divide='ignore', invalid='ignore'):
        area_rel_change = np.where(curve1_areas > 0,
                                   (area_diff / curve1_areas) * 100.0, 0.0)
        storage_rel_change = np.where(curve1_storages > 0,
                                      (storage_diff / curve1_storages) * 100.0, 0.0)

    # Max storage for normalization
    max_storage = max(float(np.max(curve1_storages)), float(np.max(curve2_storages)))
    max_area = max(float(np.max(curve1_areas)), float(np.max(curve2_areas)))

    return {
        "levels": levels.tolist(),
        "area_diff_m2": [round(float(x), 2) for x in area_diff],
        "storage_diff_m3": [round(float(x), 2) for x in storage_diff],
        "area_rel_change_pct": [round(float(x), 4) for x in area_rel_change],
        "storage_rel_change_pct": [round(float(x), 4) for x in storage_rel_change],
        "max_storage_m3": round(float(max_storage), 2),
        "max_area_m2": round(float(max_area), 2),
        "total_storage_loss_m3": round(float(-np.sum(storage_diff[storage_diff < 0])), 2),
        "total_storage_gain_m3": round(float(np.sum(storage_diff[storage_diff > 0])), 2),
        "net_storage_change_m3": round(float(np.sum(storage_diff)), 2),
    }


def compute_same_level_area_difference(areas1: np.ndarray, areas2: np.ndarray,
                                       levels: np.ndarray) -> Dict[str, Any]:
    """
    Compute area difference at same water levels (sedimentation proxy).

    Positive difference means period 2 has more area (erosion),
    negative means period 2 has less area (sedimentation).
    """
    diff = areas2 - areas1
    return {
        "levels": [round(float(l), 2) for l in levels],
        "area_diff_m2": [round(float(x), 2) for x in diff],
        "mean_diff_m2": round(float(np.mean(diff)), 2),
        "max_loss_m2": round(float(np.min(diff)), 2),
        "max_gain_m2": round(float(np.max(diff)), 2),
    }


# ============================================================
# Uncertainty Analysis
# ============================================================

def compute_uncertainty(dem: np.ndarray, levels: np.ndarray,
                        pixel_area_m2: float,
                        dem_error_m: float = DEFAULT_DEM_ERROR_M,
                        water_level_error_m: float = DEFAULT_WATER_LEVEL_ERROR_M,
                        water_body_error_px: float = DEFAULT_WATER_BODY_ERROR_PX,
                        n_monte_carlo: int = 500,
                        seed: int = 42,
                        confidence: float = DEFAULT_CONFIDENCE_LEVEL,
                        nodata: float = -9999.0) -> Dict[str, Any]:
    """
    Compute uncertainty for area and storage curves.

    Propagates DEM vertical error, water level error, and water boundary
    delineation error through Monte Carlo simulation.

    Args:
        dem: 2D elevation array
        levels: Elevation levels
        pixel_area_m2: Area per pixel in m²
        dem_error_m: DEM vertical RMSE (m)
        water_level_error_m: Water level measurement error (m)
        water_body_error_px: Water boundary delineation error (pixels)
        n_monte_carlo: Number of MC iterations
        seed: Random seed
        confidence: Confidence level
        nodata: DEM nodata value

    Returns:
        Dict with uncertainty results
    """
    rng = np.random.RandomState(seed)
    n_levels = len(levels)

    # Storage for MC results
    mc_areas = np.zeros((n_monte_carlo, n_levels))
    mc_storages = np.zeros((n_monte_carlo, n_levels))

    valid_mask = dem != nodata
    n_valid = int(np.sum(valid_mask))

    for it in range(n_monte_carlo):
        # Perturb DEM with vertical error
        dem_perturbed = dem.copy().astype(np.float64)
        noise = rng.normal(0, dem_error_m, size=dem.shape)
        dem_perturbed[valid_mask] += noise[valid_mask]
        dem_perturbed[~valid_mask] = nodata

        # Perturb water levels
        level_noise = rng.normal(0, water_level_error_m, size=n_levels)
        levels_perturbed = levels + level_noise

        # Sort perturbed levels to maintain monotonicity
        levels_perturbed = np.sort(levels_perturbed)

        # Compute curve with perturbed data
        areas, storages = compute_area_storage_curve(
            dem_perturbed, levels_perturbed, pixel_area_m2, nodata
        )

        # Add boundary error: scale area by pixel uncertainty
        boundary_factor = 1.0 + rng.normal(0, water_body_error_px * np.sqrt(pixel_area_m2) / (np.sqrt(n_valid) * np.sqrt(pixel_area_m2)) if n_valid > 0 and pixel_area_m2 > 0 else 0)
        boundary_factor = max(boundary_factor, 0.5)  # Clamp
        areas = areas * boundary_factor

        mc_areas[it] = areas
        mc_storages[it] = storages

    # Compute statistics
    alpha = 1.0 - confidence
    lower_pct = alpha / 2.0 * 100
    upper_pct = (1.0 - alpha / 2.0) * 100

    area_mean = np.mean(mc_areas, axis=0)
    area_std = np.std(mc_areas, axis=0)
    area_p5 = np.percentile(mc_areas, lower_pct, axis=0)
    area_p95 = np.percentile(mc_areas, upper_pct, axis=0)

    storage_mean = np.mean(mc_storages, axis=0)
    storage_std = np.std(mc_storages, axis=0)
    storage_p5 = np.percentile(mc_storages, lower_pct, axis=0)
    storage_p95 = np.percentile(mc_storages, upper_pct, axis=0)

    return {
        "n_iterations": n_monte_carlo,
        "seed": seed,
        "confidence_level": confidence,
        "dem_error_m": dem_error_m,
        "water_level_error_m": water_level_error_m,
        "water_body_error_px": water_body_error_px,
        "levels": [round(float(l), 2) for l in levels],
        "area": {
            "mean_m2": [round(float(x), 2) for x in area_mean],
            "std_m2": [round(float(x), 2) for x in area_std],
            "p5_m2": [round(float(x), 2) for x in area_p5],
            "p95_m2": [round(float(x), 2) for x in area_p95],
        },
        "storage": {
            "mean_m3": [round(float(x), 2) for x in storage_mean],
            "std_m3": [round(float(x), 2) for x in storage_std],
            "p5_m3": [round(float(x), 2) for x in storage_p5],
            "p95_m3": [round(float(x), 2) for x in storage_p95],
        },
    }


# ============================================================
# Vertical Datum Validation
# ============================================================

def validate_vertical_datum(dem_datum: Optional[str], water_level_datum: Optional[str],
                            logger: logging.Logger) -> Tuple[bool, List[str]]:
    """
    Validate that DEM and water level data use the same vertical datum.

    Returns:
        Tuple of (is_valid, warnings)
    """
    warnings = []

    if dem_datum is None and water_level_datum is None:
        warnings.append(
            "Both DEM and water level datums are unknown. "
            "Absolute storage values are unreliable."
        )
        return False, warnings

    if dem_datum is None:
        warnings.append(
            f"DEM datum unknown, water level datum is '{water_level_datum}'. "
            "Cannot verify datum consistency."
        )
        return False, warnings

    if water_level_datum is None:
        warnings.append(
            f"Water level datum unknown, DEM datum is '{dem_datum}'. "
            "Cannot verify datum consistency."
        )
        return False, warnings

    if dem_datum.lower() != water_level_datum.lower():
        warnings.append(
            f"Datum mismatch: DEM='{dem_datum}', WaterLevel='{water_level_datum}'. "
            "Absolute storage values are unreliable."
        )
        return False, warnings

    return True, warnings


# ============================================================
# Synthetic Data Generation
# ============================================================

def generate_cone_dem(n_rows: int, n_cols: int, center_elev: float,
                      max_depth: float, nodata: float = -9999.0) -> np.ndarray:
    """
    Generate a cone-shaped reservoir DEM.

    The cone has maximum depth at center, elevation increases radially.

    Args:
        n_rows: Number of rows
        n_cols: Number of columns
        center_elev: Elevation at the rim (highest)
        max_depth: Maximum water depth at center
        nodata: Nodata value

    Returns:
        2D elevation array
    """
    dem = np.full((n_rows, n_cols), nodata, dtype=np.float64)
    cy, cx = n_rows / 2.0, n_cols / 2.0
    max_radius = min(cy, cx)

    for i in range(n_rows):
        for j in range(n_cols):
            r = np.sqrt((i - cy) ** 2 + (j - cx) ** 2)
            if r < max_radius:
                # Linear decrease from rim to center
                dem[i, j] = center_elev - max_depth * (1.0 - r / max_radius)

    return dem


def generate_step_dem(n_rows: int, n_cols: int, base_elev: float,
                      step_height: float, n_steps: int = 3,
                      nodata: float = -9999.0) -> np.ndarray:
    """
    Generate a stepped (terraced) reservoir DEM.

    Creates concentric terraces at different elevations.

    Args:
        n_rows: Number of rows
        n_cols: Number of columns
        base_elev: Lowest elevation (bottom)
        step_height: Height of each step
        n_steps: Number of steps
        nodata: Nodata value

    Returns:
        2D elevation array
    """
    dem = np.full((n_rows, n_cols), nodata, dtype=np.float64)
    cy, cx = n_rows / 2.0, n_cols / 2.0
    max_radius = min(cy, cx)

    for i in range(n_rows):
        for j in range(n_cols):
            r = np.sqrt((i - cy) ** 2 + (j - cx) ** 2)
            if r < max_radius:
                # Determine which step this pixel belongs to
                step = int(r / max_radius * n_steps)
                step = min(step, n_steps - 1)
                dem[i, j] = base_elev + step * step_height

    return dem


def generate_synthetic_water_mask(dem: np.ndarray, water_level: float,
                                  nodata: float = -9999.0) -> np.ndarray:
    """
    Generate binary water mask from DEM and water level.

    Returns:
        Binary array: 1=water, 0=land, 0=nodata
    """
    mask = np.zeros_like(dem, dtype=np.uint8)
    valid = dem != nodata
    mask[valid & (dem <= water_level)] = 1
    return mask


# ============================================================
# Output Writers
# ============================================================

def write_area_level_curve(output_dir: Path, levels: np.ndarray,
                           areas: np.ndarray) -> Path:
    """Write area-level curve to CSV."""
    path = output_dir / "area_level_curve.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["elevation_m", "area_m2", "area_km2"])
        for i in range(len(levels)):
            writer.writerow([
                round(float(levels[i]), 2),
                round(float(areas[i]), 2),
                round(float(areas[i]) / 1e6, 6),
            ])
    return path


def write_storage_curve(output_dir: Path, levels: np.ndarray,
                        areas: np.ndarray, storages: np.ndarray) -> Path:
    """Write storage curve to CSV."""
    path = output_dir / "storage_curve.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["elevation_m", "area_m2", "area_km2",
                         "storage_m3", "storage_mcm", "storage_km3"])
        for i in range(len(levels)):
            writer.writerow([
                round(float(levels[i]), 2),
                round(float(areas[i]), 2),
                round(float(areas[i]) / 1e6, 6),
                round(float(storages[i]), 2),
                round(float(storages[i]) / 1e6, 4),
                round(float(storages[i]) / 1e9, 8),
            ])
    return path


def write_storage_timeseries(output_dir: Path, dates: List[str],
                             water_levels: List[float],
                             storages: List[float]) -> Path:
    """Write storage time series to CSV."""
    path = output_dir / "storage_timeseries.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "water_level_m", "storage_m3", "storage_mcm"])
        for d, wl, s in zip(dates, water_levels, storages):
            writer.writerow([d, round(float(wl), 2),
                             round(float(s), 2), round(float(s) / 1e6, 4)])
    return path


def write_water_extent_timeseries(output_dir: Path,
                                  timeseries: List[Dict]) -> Path:
    """Write water extent time series to CSV."""
    path = output_dir / "water_extent_timeseries.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "water_pixels", "area_m2", "area_km2"])
        for entry in timeseries:
            writer.writerow([
                entry["date"],
                entry["water_pixels"],
                entry["area_m2"],
                entry["area_km2"],
            ])
    return path


def write_uncertainty_json(output_dir: Path, uncertainty: Dict) -> Path:
    """Write uncertainty results to JSON."""
    path = output_dir / "uncertainty.json"
    path.write_text(
        json.dumps(uncertainty, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path


# ============================================================
# Main Analysis Pipeline
# ============================================================

def run_analysis(args: argparse.Namespace) -> int:
    """Main analysis workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("rcc-output")
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logging(output_dir)
    logger.info("Reservoir Capacity Change - Starting")

    # Pre-flight: if user supplied a DEM path, it must exist on disk.
    # This is a clear argument/IO problem (exit 2), not a data-validation
    # problem (exit 6) — distinguishes "you didn't pass a real file" from
    # "the file you passed is corrupt/empty/wrong-shape".
    if hasattr(args, 'dem') and args.dem:
        dem_path = Path(args.dem)
        if not dem_path.exists():
            logger.error(f"DEM file not found: {args.dem}")
            print(f"ERROR: DEM file not found: {args.dem}", file=sys.stderr)
            return EXIT_ARG

    # Parse parameters
    curve_method = args.curve_method if hasattr(args, 'curve_method') and args.curve_method else DEFAULT_CURVE_METHOD
    dem_error = args.dem_error if hasattr(args, 'dem_error') and args.dem_error is not None else DEFAULT_DEM_ERROR_M
    wl_error = args.water_level_error if hasattr(args, 'water_level_error') and args.water_level_error is not None else DEFAULT_WATER_LEVEL_ERROR_M
    wb_error = args.water_body_error if hasattr(args, 'water_body_error') and args.water_body_error is not None else DEFAULT_WATER_BODY_ERROR_PX
    mc_iterations = args.mc_iterations if hasattr(args, 'mc_iterations') and args.mc_iterations is not None else 500
    mc_seed = args.mc_seed if hasattr(args, 'mc_seed') and args.mc_seed is not None else 42
    confidence = args.confidence if hasattr(args, 'confidence') and args.confidence else DEFAULT_CONFIDENCE_LEVEL
    reference_level = args.reference_level if hasattr(args, 'reference_level') and args.reference_level else None

    # --- Load or generate DEM ---
    dem = None
    transform = None
    crs = "EPSG:4326"
    pixel_area_m2 = 900.0  # default 30m
    dem_datum = None
    water_level_datum = None

    if hasattr(args, 'dem') and args.dem:
        try:
            import rasterio
            from rasterio.transform import from_bounds
        except ImportError:
            logger.error("rasterio required for GeoTIFF input")
            print("ERROR: rasterio required for GeoTIFF input", file=sys.stderr)
            return EXIT_DEP

        try:
            with rasterio.open(args.dem) as src:
                dem = src.read(1).astype(np.float64)
                transform = src.transform
                crs = src.crs
            logger.info(f"Loaded DEM: {dem.shape}, CRS={crs}")
        except FileNotFoundError as e:
            # Race-safe: file disappeared between pre-flight and open()
            logger.error(f"DEM file disappeared: {e}")
            print(f"ERROR: DEM file not found: {args.dem}", file=sys.stderr)
            return EXIT_ARG
        except Exception as e:
            logger.error(f"Failed to read DEM: {e}")
            print(f"ERROR: Failed to read DEM: {e}", file=sys.stderr)
            return EXIT_VALIDATION

        # Compute pixel area
        pixel_area_m2 = compute_pixel_area_m2(transform=transform, crs=crs)
        logger.info(f"Pixel area: {pixel_area_m2:.2f} m²")

        # Check for datum info
        dem_datum = None  # Could be extracted from metadata
    else:
        # Generate synthetic cone DEM for demo
        logger.info("Generating synthetic cone DEM")
        dem = generate_cone_dem(100, 100, center_elev=200.0, max_depth=50.0)
        pixel_area_m2 = 900.0  # 30m x 30m

    # --- Validate vertical datum ---
    if hasattr(args, 'dem_datum') and args.dem_datum:
        dem_datum = args.dem_datum
    if hasattr(args, 'water_level_datum') and args.water_level_datum:
        water_level_datum = args.water_level_datum

    datum_ok, datum_warnings = validate_vertical_datum(dem_datum, water_level_datum, logger)
    for w in datum_warnings:
        logger.warning(w)

    if not datum_ok:
        logger.warning("Datum validation failed - results are RELATIVE only")

    # --- Define elevation levels ---
    nodata_val = -9999.0
    valid_mask = dem != nodata_val
    if not np.any(valid_mask):
        logger.error("DEM has no valid pixels")
        print("ERROR: DEM has no valid pixels", file=sys.stderr)
        return EXIT_VALIDATION

    elev_min = float(np.min(dem[valid_mask]))
    elev_max = float(np.max(dem[valid_mask]))

    if reference_level is not None:
        levels_start = max(elev_min, reference_level)
    else:
        levels_start = elev_min

    # Create levels at 1m intervals
    levels = np.arange(levels_start, elev_max + 1.0, 1.0)
    if len(levels) < 2:
        levels = np.linspace(elev_min, elev_max, 10)

    logger.info(f"Elevation range: {elev_min:.1f} - {elev_max:.1f} m, {len(levels)} levels")

    # --- Compute area-storage curve ---
    if curve_method == "trapezoidal":
        areas, storages = compute_curve_trapezoidal(dem, levels, pixel_area_m2, nodata_val)
    else:
        areas, storages = compute_area_storage_curve(dem, levels, pixel_area_m2, nodata_val)

    logger.info(f"Curve computed: max_area={np.max(areas):.0f} m², max_storage={np.max(storages):.0f} m³")

    # --- Compute water extent time series ---
    water_masks = []
    dates = []
    water_levels_input = []

    if hasattr(args, 'water_levels') and args.water_levels:
        # Load water levels from CSV
        try:
            with open(args.water_levels, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    dates.append(row.get("date", row.get("Date", "")))
                    wl = float(row.get("level", row.get("water_level", row.get("Level", 0))))
                    water_levels_input.append(wl)
                    mask = generate_synthetic_water_mask(dem, wl, nodata_val)
                    water_masks.append(mask)
        except Exception as e:
            logger.error(f"Failed to read water levels: {e}")
            return EXIT_VALIDATION
    else:
        # Generate synthetic time series
        logger.info("Generating synthetic water level time series")
        n_periods = 5
        base_level = elev_min + (elev_max - elev_min) * 0.4
        for i in range(n_periods):
            wl = base_level + i * 5.0 + np.random.normal(0, 1.0)
            wl = np.clip(wl, elev_min, elev_max)
            dates.append(f"2020-0{i + 1}-15")
            water_levels_input.append(float(wl))
            mask = generate_synthetic_water_mask(dem, wl, nodata_val)
            water_masks.append(mask)

    # Compute water extent time series
    water_timeseries = compute_water_extent_timeseries(water_masks, dates, pixel_area_m2)

    # Compute storage for each water level in time series
    storage_ts = []
    for wl in water_levels_input:
        s = compute_storage_at_level(dem, wl, pixel_area_m2, nodata_val)
        storage_ts.append(float(s))

    # --- Compute relative change (if 2+ periods) ---
    change_results = None
    if len(water_levels_input) >= 2:
        # Compare first and last period
        wl1, wl2 = water_levels_input[0], water_levels_input[-1]
        area1 = compute_area_at_level(dem, wl1, pixel_area_m2, nodata_val)
        area2 = compute_area_at_level(dem, wl2, pixel_area_m2, nodata_val)
        storage1 = compute_storage_at_level(dem, wl1, pixel_area_m2, nodata_val)
        storage2 = compute_storage_at_level(dem, wl2, pixel_area_m2, nodata_val)

        change_results = {
            "period_1": {"date": dates[0], "level_m": round(wl1, 2),
                         "area_m2": round(area1, 2), "storage_m3": round(storage1, 2)},
            "period_2": {"date": dates[-1], "level_m": round(wl2, 2),
                         "area_m2": round(area2, 2), "storage_m3": round(storage2, 2)},
            "area_change_m2": round(area2 - area1, 2),
            "storage_change_m3": round(storage2 - storage1, 2),
            "storage_change_pct": round((storage2 - storage1) / max(storage1, 1.0) * 100, 4),
        }

    # --- Uncertainty analysis ---
    uncertainty_results = None
    if mc_iterations > 0:
        logger.info(f"Running Monte Carlo uncertainty ({mc_iterations} iterations)")
        uncertainty_results = compute_uncertainty(
            dem, levels, pixel_area_m2,
            dem_error_m=dem_error,
            water_level_error_m=wl_error,
            water_body_error_px=wb_error,
            n_monte_carlo=mc_iterations,
            seed=mc_seed,
            confidence=confidence,
            nodata=nodata_val,
        )
        logger.info("Uncertainty analysis complete")

    # --- Write Outputs ---

    # area_level_curve.csv
    al_path = write_area_level_curve(output_dir, levels, areas)

    # storage_curve.csv
    sc_path = write_storage_curve(output_dir, levels, areas, storages)

    # storage_timeseries.csv
    st_path = write_storage_timeseries(output_dir, dates, water_levels_input, storage_ts)

    # water_extent_timeseries.csv
    wt_path = write_water_extent_timeseries(output_dir, water_timeseries)

    # uncertainty.json
    u_path = None
    if uncertainty_results:
        u_path = write_uncertainty_json(output_dir, uncertainty_results)

    # request.json
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "curve_method": curve_method,
        "dem_error_m": dem_error,
        "water_level_error_m": wl_error,
        "water_body_error_px": wb_error,
        "mc_iterations": mc_iterations,
        "mc_seed": mc_seed,
        "confidence_level": confidence,
        "reference_level": reference_level,
        "pixel_area_m2": pixel_area_m2,
        "crs": str(crs) if crs else None,
        "shape": [int(x) for x in dem.shape],
        "elev_min": round(elev_min, 2),
        "elev_max": round(elev_max, 2),
        "n_levels": len(levels),
        "n_periods": len(dates),
        "datum_valid": datum_ok,
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
        "dem_source": getattr(args, 'dem', None) or "synthetic_cone",
        "water_levels_source": getattr(args, 'water_levels', None) or "synthetic",
        "dem_datum": dem_datum,
        "water_level_datum": water_level_datum,
        "datum_consistent": datum_ok,
        "n_periods": len(dates),
        "dates": dates,
        "water_levels_m": [round(float(x), 2) for x in water_levels_input],
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # output-manifest.json
    output_files = {
        "area_level_curve.csv": str(al_path),
        "storage_curve.csv": str(sc_path),
        "storage_timeseries.csv": str(st_path),
        "water_extent_timeseries.csv": str(wt_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(dataset_path),
    }
    if u_path:
        output_files["uncertainty.json"] = str(u_path)

    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "analysis_parameters": request_info,
        "output_files": output_files,
        "curve_summary": {
            "max_area_m2": round(float(np.max(areas)), 2),
            "max_storage_m3": round(float(np.max(storages)), 2),
            "max_storage_mcm": round(float(np.max(storages)) / 1e6, 4),
        },
    }
    if change_results:
        manifest["change_summary"] = change_results

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
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # qa.json
    qa = {
        "status": "complete",
        "checks": {
            "dem_loaded": dem is not None,
            "curve_computed": len(areas) > 0 and len(storages) > 0,
            "curve_monotonic": bool(np.all(np.diff(areas) >= -1e-6) and np.all(np.diff(storages) >= -1e-6)),
            "timeseries_computed": len(water_timeseries) > 0,
            "uncertainty_computed": uncertainty_results is not None,
            "all_outputs_written": all(Path(p).exists() for p in output_files.values()),
            "datum_consistent": datum_ok,
        },
        "warnings": datum_warnings,
        "n_levels": len(levels),
        "n_periods": len(dates),
        "pixel_area_m2": pixel_area_m2,
        "elev_range": [round(elev_min, 2), round(elev_max, 2)],
    }

    qa_path = output_dir / "qa.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    logger.info("Analysis complete")
    cleanup_logging()
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Reservoir Capacity Change Analysis")
    parser.add_argument("--dem", default=None,
                        help="Path to DEM GeoTIFF file")
    parser.add_argument("--water-levels", default=None,
                        help="Path to water levels CSV file (date, level columns)")
    parser.add_argument("--reservoir-boundary", default=None,
                        help="Path to reservoir boundary GeoJSON/Shapefile")
    parser.add_argument("--place", default=None,
                        help="Place name for AOI lookup")
    add_bbox_date_args(parser)
    parser.add_argument("--start-date", default=None,
                        help="Start date (ISO 8601)")
    parser.add_argument("--end-date", default=None,
                        help="End date (ISO 8601)")
    parser.add_argument("--dates", nargs="*", default=None,
                        help="List of dates")
    parser.add_argument("--curve-method", default=DEFAULT_CURVE_METHOD,
                        choices=["trapezoidal", "prism"],
                        help=f"Curve computation method (default: {DEFAULT_CURVE_METHOD})")
    parser.add_argument("--reference-level", type=float, default=None,
                        help="Reference elevation level (m)")
    parser.add_argument("--dem-error", type=float, default=None,
                        help=f"DEM vertical error in meters (default: {DEFAULT_DEM_ERROR_M})")
    parser.add_argument("--water-level-error", type=float, default=None,
                        help=f"Water level error in meters (default: {DEFAULT_WATER_LEVEL_ERROR_M})")
    parser.add_argument("--water-body-error", type=float, default=None,
                        help=f"Water body boundary error in pixels (default: {DEFAULT_WATER_BODY_ERROR_PX})")
    parser.add_argument("--mc-iterations", type=int, default=500,
                        help=f"Monte Carlo iterations (default: 500)")
    parser.add_argument("--mc-seed", type=int, default=42,
                        help="Monte Carlo random seed")
    parser.add_argument("--confidence", type=float, default=DEFAULT_CONFIDENCE_LEVEL,
                        help=f"Confidence level (default: {DEFAULT_CONFIDENCE_LEVEL})")
    parser.add_argument("--dem-datum", default=None,
                        help="DEM vertical datum (e.g., WGS84, CGCS2000)")
    parser.add_argument("--water-level-datum", default=None,
                        help="Water level vertical datum")
    parser.add_argument("--output-dir", "-o", default="rcc-output",
                        help="Output directory (default: rcc-output)")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    args = parser.parse_args()

    try:
        sys.exit(run_analysis(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
