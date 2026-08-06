#!/usr/bin/env python3
"""
Building Footprint Height - Extract building heights from DSM/DTM/point cloud.

Estimates building height, floor count proxy, and volume from building
footprints combined with elevation data (DSM, DTM, or LiDAR point cloud).

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
    from _geoskill_data_fetcher import (DataFetcher,
        DataSource,
        DateRange,
        add_bbox_date_args,
        parse_bbox_arg,
        parse_date_range_arg,)
    _SHARED_FETCHER_AVAILABLE = True
except ImportError:
    import sys as _sys
    from pathlib import Path as _Path
    _skill_dir = _Path(__file__).resolve().parent
    _repo_root = _skill_dir.parent.parent
    _local_fetcher = _repo_root / "_geoskill_data_fetcher"
    if _local_fetcher.exists():
        _sys.path.insert(0, str(_repo_root))
    from _geoskill_data_fetcher import (DataFetcher,
        DataSource,
        DateRange,
        add_bbox_date_args,
        parse_bbox_arg,
        parse_date_range_arg,)
    _SHARED_FETCHER_AVAILABLE = True
except Exception:  # pragma: no cover - missing dep is non-fatal
    _SHARED_FETCHER_AVAILABLE = False

try:
    import rasterio
    from rasterio.errors import RasterioIOError
    _RASTERIO_AVAILABLE = True
except ImportError:
    rasterio = None
    RasterioIOError = Exception
    _RASTERIO_AVAILABLE = False

# Suppress NumPy 2.5 "Setting the shape" deprecation warning emitted by
# rasterio<=1.4.3 internals; see comments in blue-carbon-assessment.
import warnings as _warnings_mod
_warnings_mod.filterwarnings(
    "ignore",
    message=r"^Setting the shape on a NumPy array has been deprecated.*",
    category=DeprecationWarning,
)
del _warnings_mod

EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# ============================================================
# Argument Validation
# ============================================================

# File-arg flags that must point to existing paths (None = skip check)
FILE_ARGS = {
    "dsm": "args.dsm",
    "footprints": "args.footprints",
    "dtm": "args.dtm",
    "point-cloud": "args.point_cloud",
    "standard-config": "args.standard_config",
}

# Numeric flags with (min, max) bounds; None = unbounded on that side
NUMERIC_RANGES = {
    "floor-height": (0.5, 100.0),  # sensible building floor height range in meters
}


def validate_args(args) -> int:
    """Validate file existence and numeric ranges.
    Returns exit code (0 = ok, 2 = arg error)."""
    # File existence
    for flag, accessor in FILE_ARGS.items():
        path = eval(accessor)  # safe: only string concat
        if path is None or path == "":
            continue
        if not Path(str(path)).exists():
            print(f"ERROR: --{flag} not found: {path}", file=sys.stderr)
            return 2
    # Numeric ranges
    for flag, (lo, hi) in NUMERIC_RANGES.items():
        val = getattr(args, flag, None)
        if val is None:
            continue
        if not isinstance(val, (int, float)):
            continue
        if lo is not None and val < lo:
            print(f"ERROR: --{flag}={val} below minimum {lo}", file=sys.stderr)
            return 2
        if hi is not None and val > hi:
            print(f"ERROR: --{flag}={val} above maximum {hi}", file=sys.stderr)
            return 2
    return 0


# ============================================================
# Logging
# ============================================================

def setup_logging(output_dir: Path) -> logging.Logger:
    """Setup logging to file and console."""
    logger = logging.getLogger("bfh")
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
    """Close all handlers on the bfh logger."""
    logger = logging.getLogger("bfh")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)


# ============================================================
# Standards
# ============================================================

def load_height_standards(standards_path: Optional[str] = None) -> Dict:
    """Load building height standards from JSON file."""
    if standards_path is None:
        script_dir = Path(__file__).parent
        standards_path = script_dir.parent / "references" / "building_height_standards.json"

    with open(standards_path, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# Geometry Helpers
# ============================================================

def create_polygon(x: float, y: float, w: float, h: float) -> List[List[float]]:
    """
    Create a polygon from origin (x,y) with width w and height h.
    Returns list of [x, y] ring coordinates (closed ring).
    """
    return [
        [x, y],
        [x + w, y],
        [x + w, y + h],
        [x, y + h],
        [x, y],
    ]


def polygon_area(poly: List[List[float]]) -> float:
    """Compute area of a simple polygon using shoelace formula."""
    n = len(poly)
    if n < 4:
        return 0.0
    area = 0.0
    for i in range(n - 1):
        area += poly[i][0] * poly[i + 1][1]
        area -= poly[i + 1][0] * poly[i][1]
    return abs(area) / 2.0


def polygon_bounds(poly: List[List[float]]) -> Tuple[float, float, float, float]:
    """Get (xmin, ymin, xmax, ymax) from polygon."""
    xs = [p[0] for p in poly[:-1]]
    ys = [p[1] for p in poly[:-1]]
    return (min(xs), min(ys), max(xs), max(ys))


def buffer_polygon_inward(poly: List[List[float]], buffer_m: float) -> List[List[float]]:
    """
    Simple inward buffer for axis-aligned rectangles.
    Returns a new polygon shrunk by buffer_m on each side.
    """
    xmin, ymin, xmax, ymax = polygon_bounds(poly)
    new_xmin = xmin + buffer_m
    new_ymin = ymin + buffer_m
    new_xmax = xmax - buffer_m
    new_ymax = ymax - buffer_m

    if new_xmax <= new_xmin or new_ymax <= new_ymin:
        return poly  # Too small to buffer

    return create_polygon(new_xmin, new_ymin,
                         new_xmax - new_xmin, new_ymax - new_ymin)


# ============================================================
# Raster Sampling
# ============================================================

def sample_raster_at_footprint(
    raster: np.ndarray,
    poly: List[List[float]],
    transform: Tuple[float, float, float, float, float, float],
    nodata_value: float = -9999.0,
    edge_buffer: float = 0.0,
) -> Optional[np.ndarray]:
    """
    Sample raster values within a polygon footprint.

    Args:
        raster: 2D numpy array (rows, cols)
        poly: Polygon as list of [x, y] coords in CRS units
        transform: (x_origin, x_pixel_width, y_origin, y_pixel_height, x_skew, y_skew)
                   or simplified (xmin, x_res, ymin, y_res) — see note below
        nodata_value: Nodata value in raster
        edge_buffer: Inward buffer to exclude mixed-edge pixels

    Returns:
        1D array of valid raster values, or None if no valid data

    Note on transform:
        We use a simplified geo-transform: (xmin, x_res, ymin, y_res)
        where x_res > 0 and y_res < 0 (standard north-up raster).
    """
    if raster.ndim != 2:
        return None

    xmin_r, x_res, ymax_r, y_res = transform
    nrows, ncols = raster.shape

    # Apply edge buffer
    if edge_buffer > 0:
        work_poly = buffer_polygon_inward(poly, edge_buffer)
    else:
        work_poly = poly

    pxmin, pymin, pxmax, pymax = polygon_bounds(work_poly)

    # Convert geo coords to pixel indices
    # col = (x - xmin_r) / x_res
    # row = (y - ymax_r) / y_res  (y_res is negative)
    col_start = int(np.floor((pxmin - xmin_r) / x_res))
    col_end = int(np.ceil((pxmax - xmin_r) / x_res))
    row_start = int(np.floor((pymax - ymax_r) / y_res))
    row_end = int(np.ceil((pymin - ymax_r) / y_res))

    # Clip to raster bounds
    col_start = max(0, col_start)
    col_end = min(ncols, col_end)
    row_start = max(0, row_start)
    row_end = min(nrows, row_end)

    if col_end <= col_start or row_end <= row_start:
        return None

    # Collect valid values
    values = []
    for r in range(row_start, row_end):
        for c in range(col_start, col_end):
            # Pixel center in geo coords
            px = xmin_r + (c + 0.5) * x_res
            py = ymax_r + (r + 0.5) * y_res
            if point_in_rect(px, py, pxmin, pymin, pxmax, pymax):
                val = raster[r, c]
                if val != nodata_value and not np.isnan(val) and not np.isinf(val):
                    values.append(val)

    if not values:
        return None

    return np.array(values, dtype=np.float64)

    if not values:
        return None

    return np.array(values, dtype=np.float64)


def point_in_rect(px: float, py: float,
                  xmin: float, ymin: float, xmax: float, ymax: float) -> bool:
    """Check if point (px, py) is inside axis-aligned rectangle."""
    return xmin <= px <= xmax and ymin <= py <= ymax


# ============================================================
# Height Estimation Methods
# ============================================================

def estimate_height_dsm_dtm(
    dsm_values: np.ndarray,
    dtm_values: np.ndarray,
    quantile: float = 0.95,
    min_diff: float = 1.0,
) -> Tuple[Optional[float], Optional[float]]:
    """
    Estimate building height from DSM and DTM value arrays.

    Args:
        dsm_values: Array of DSM elevations within footprint
        dtm_values: Array of DTM elevations within footprint
        quantile: Quantile of DSM to use (robust to outliers)
        min_diff: Minimum height difference to count as building

    Returns:
        (height_m, base_elevation) or (None, None) if invalid
    """
    if dsm_values is None or dtm_values is None:
        return None, None
    if len(dsm_values) == 0 or len(dtm_values) == 0:
        return None, None

    # Base elevation: median of DTM (ground)
    base_elev = float(np.median(dtm_values))

    # Roof elevation: robust quantile of DSM
    roof_elev = float(np.quantile(dsm_values, quantile))

    height = roof_elev - base_elev

    if height < min_diff:
        return None, None

    return height, base_elev


def estimate_height_point_cloud(
    point_z_values: np.ndarray,
    ground_z: Optional[float] = None,
    quantile: float = 0.95,
    min_points: int = 10,
) -> Tuple[Optional[float], Optional[float]]:
    """
    Estimate height from LiDAR point cloud Z values.

    Args:
        point_z_values: Array of point cloud Z elevations
        ground_z: Ground reference (if None, use 5th percentile)
        quantile: Quantile for roof height
        min_points: Minimum points per building

    Returns:
        (height_m, base_elevation) or (None, None) if invalid
    """
    if point_z_values is None or len(point_z_values) < min_points:
        return None, None

    valid_z = point_z_values[~np.isnan(point_z_values) & ~np.isinf(point_z_values)]
    if len(valid_z) < min_points:
        return None, None

    if ground_z is None:
        ground_z = float(np.quantile(valid_z, 0.05))

    roof_z = float(np.quantile(valid_z, quantile))
    height = roof_z - ground_z

    if height < 1.0:
        return None, None

    return height, ground_z


def estimate_height_from_shadow(
    shadow_length_m: float,
    solar_elevation_deg: float,
) -> Optional[float]:
    """
    Estimate height from shadow length and solar elevation angle.

    height = shadow_length * tan(solar_elevation)

    Args:
        shadow_length_m: Length of building shadow on ground
        solar_elevation_deg: Solar elevation angle in degrees

    Returns:
        Height in meters, or None if invalid
    """
    if shadow_length_m <= 0:
        return None
    if solar_elevation_deg <= 0 or solar_elevation_deg >= 90:
        return None

    elevation_rad = np.radians(solar_elevation_deg)
    height = shadow_length_m * np.tan(elevation_rad)

    if height < 1.0 or height > 828.0:
        return None

    return float(height)


# ============================================================
# Floor Count Proxy
# ============================================================

def compute_floor_count(height_m: Optional[float], floor_height_m: float = 3.0,
                        uncertainty_m: float = 0.5) -> Dict[str, Any]:
    """
    Compute floor count proxy from height.

    Args:
        height_m: Building height in meters (None if unknown)
        floor_height_m: Assumed floor height
        uncertainty_m: Uncertainty in floor height assumption

    Returns:
        Dict with floors, min_floors, max_floors, and uncertainty
    """
    if height_m is None or floor_height_m <= 0:
        if floor_height_m <= 0:
            floor_height_m = 3.0
        return {
            "floors_proxy": 0,
            "floors_min": 0,
            "floors_max": 0,
            "floor_height_assumed_m": floor_height_m,
            "uncertainty_m": uncertainty_m,
        }

    floors = height_m / floor_height_m
    floors_int = max(1, int(np.round(floors)))

    # Uncertainty range
    floors_min = max(1, int(np.floor((height_m - uncertainty_m) / floor_height_m)))
    floors_max = max(1, int(np.ceil((height_m + uncertainty_m) / floor_height_m)))

    return {
        "floors_proxy": floors_int,
        "floors_min": floors_min,
        "floors_max": floors_max,
        "floor_height_assumed_m": floor_height_m,
        "uncertainty_m": uncertainty_m,
    }


# ============================================================
# Volume Estimation
# ============================================================

def estimate_volume(footprint_area_m2: float, height_m: float,
                    roof_type: str = "flat") -> float:
    """
    Estimate building volume from footprint area and height.

    For flat roofs: V = area * height
    For pitched roofs: V = area * height * 0.85 (approximate)
    For complex roofs: V = area * height * 0.9

    Args:
        footprint_area_m2: Building footprint area
        height_m: Building height
        roof_type: 'flat', 'pitched', or 'complex'

    Returns:
        Volume in cubic meters
    """
    if footprint_area_m2 <= 0 or height_m <= 0:
        return 0.0

    factors = {
        "flat": 1.0,
        "pitched": 0.85,
        "complex": 0.9,
    }
    factor = factors.get(roof_type, 1.0)

    return footprint_area_m2 * height_m * factor


# ============================================================
# Area Computation (handles projected vs geographic CRS)
# ============================================================

def compute_footprint_area(poly: List[List[float]],
                           is_projected: bool = True,
                           lat_center: float = 0.0) -> float:
    """
    Compute footprint area in square meters.

    For projected CRS: area from shoelace directly.
    For geographic CRS (EPSG:4326): approximate using cos(lat) correction.

    Args:
        poly: Polygon in CRS coordinates
        is_projected: Whether CRS is projected (metric)
        lat_center: Latitude center for geographic CRS correction

    Returns:
        Area in square meters
    """
    raw_area = polygon_area(poly)

    if is_projected:
        return raw_area

    # Geographic CRS: convert degree^2 to m^2
    # 1 degree latitude ≈ 111320 m
    # 1 degree longitude ≈ 111320 * cos(lat) m
    lat_correction = np.cos(np.radians(lat_center))
    meters_per_deg = 111320.0 * lat_correction
    return raw_area * meters_per_deg * 111320.0


# ============================================================
# Quality Assessment
# ============================================================

def assess_quality(
    height_m: Optional[float],
    n_valid_pixels: int,
    n_total_pixels: int,
    height_std: float,
    height_method: str,
    standards: Dict,
) -> Dict[str, Any]:
    """
    Assess quality of height estimation.

    Returns:
        Dict with quality_code, quality_label, coverage_ratio, issues
    """
    issues = []
    qa_std = standards["qa_thresholds"]

    # Check coverage
    coverage = n_valid_pixels / n_total_pixels if n_total_pixels > 0 else 0.0

    # Check height bounds
    if height_m is not None:
        if height_m < qa_std["min_height_m"]:
            issues.append(f"Height {height_m:.1f}m below minimum {qa_std['min_height_m']}m")
        if height_m > qa_std["max_height_m"]:
            issues.append(f"Height {height_m:.1f}m exceeds maximum {qa_std['max_height_m']}m")

    # Check height standard deviation (high std = mixed pixels / trees)
    if height_std > qa_std["max_height_stdev_m"]:
        issues.append(f"Height stdev {height_std:.1f}m exceeds {qa_std['max_height_stdev_m']}m (possible tree mixing)")

    # Check coverage
    if coverage < qa_std["min_coverage_ratio"]:
        issues.append(f"Coverage {coverage:.1%} below minimum {qa_std['min_coverage_ratio']:.1%}")

    # Determine quality code
    codes = standards["quality_codes"]
    if height_m is None:
        quality_code = 5
    elif coverage < 0.5:
        quality_code = 4
    elif height_method == "dsm_minus_dtm" and coverage >= 0.8:
        quality_code = 1
    elif height_method == "point_cloud_quantile":
        quality_code = 2
    else:
        quality_code = 3

    quality_label = codes.get(str(quality_code), "未知")

    return {
        "quality_code": quality_code,
        "quality_label": quality_label,
        "coverage_ratio": round(coverage, 4),
        "height_stdev": round(height_std, 3) if height_std is not None else None,
        "n_valid_pixels": n_valid_pixels,
        "n_total_pixels": n_total_pixels,
        "issues": issues,
    }


# ============================================================
# Building Analysis Pipeline
# ============================================================

def analyze_single_building(
    building_id: int,
    poly: List[List[float]],
    dsm: np.ndarray,
    dtm: np.ndarray,
    transform: Tuple[float, float, float, float],
    standards: Dict,
    dsm_nodata: float = -9999.0,
    dtm_nodata: float = -9999.0,
    point_cloud_z: Optional[np.ndarray] = None,
    height_method: str = "dsm_minus_dtm",
    floor_height_m: float = 3.0,
    is_projected: bool = True,
    lat_center: float = 0.0,
) -> Dict[str, Any]:
    """
    Analyze a single building footprint.

    Args:
        building_id: Unique identifier
        poly: Building footprint polygon
        dsm: DSM raster (2D numpy array)
        dtm: DTM raster (2D numpy array)
        transform: Geo-transform tuple
        standards: Height standards dict
        dsm_nodata: Nodata value for DSM
        dtm_nodata: Nodata value for DTM
        point_cloud_z: Optional point cloud Z values
        height_method: Method for height estimation
        floor_height_m: Assumed floor height
        is_projected: Whether CRS is projected
        lat_center: Latitude for area correction

    Returns:
        Building analysis result dict
    """
    qa_std = standards["qa_thresholds"]

    # Footprint area
    footprint_area = compute_footprint_area(poly, is_projected, lat_center)

    # Sample DSM and DTM with edge buffer
    edge_buffer = qa_std["edge_buffer_m"]
    dsm_vals = sample_raster_at_footprint(dsm, poly, transform, dsm_nodata, edge_buffer)
    dtm_vals = sample_raster_at_footprint(dtm, poly, transform, dtm_nodata, edge_buffer)

    # Count total pixels in footprint (without buffer) for coverage
    dsm_all = sample_raster_at_footprint(dsm, poly, transform, dsm_nodata, 0.0)
    n_total = len(dsm_all) if dsm_all is not None else 0

    # Height estimation
    height_m = None
    base_elev = None
    actual_method = height_method
    height_std = 0.0

    if height_method == "dsm_minus_dtm" and dsm_vals is not None and dtm_vals is not None:
        height_m, base_elev = estimate_height_dsm_dtm(dsm_vals, dtm_vals)
        if dsm_vals is not None:
            height_std = float(np.std(dsm_vals))
        n_valid = min(len(dsm_vals), len(dtm_vals))
    elif height_method == "point_cloud_quantile" and point_cloud_z is not None:
        height_m, base_elev = estimate_height_point_cloud(point_cloud_z)
        n_valid = len(point_cloud_z)
    elif height_method == "shadow_based":
        # Shadow method needs external input — fallback
        actual_method = "shadow_based_unavailable"
        n_valid = 0
    else:
        # Try fallback: DSM only
        if dsm_vals is not None:
            height_m = float(np.quantile(dsm_vals, 0.95))
            base_elev = None
            actual_method = "dsm_only_fallback"
            height_std = float(np.std(dsm_vals))
            n_valid = len(dsm_vals)
        else:
            n_valid = 0

    # Floor count
    floor_info = compute_floor_count(height_m, floor_height_m) if height_m else {
        "floors_proxy": 0,
        "floors_min": 0,
        "floors_max": 0,
        "floor_height_assumed_m": floor_height_m,
        "uncertainty_m": standards["floor_height"]["uncertainty_m"],
    }

    # Volume
    volume = estimate_volume(footprint_area, height_m) if height_m else 0.0

    # Quality
    quality = assess_quality(height_m, n_valid, n_total if n_total > 0 else 1,
                             height_std, actual_method, standards)

    # Roof type classification based on height std
    if height_std > 5.0:
        roof_type = "complex"
    elif height_std > 2.0:
        roof_type = "pitched"
    else:
        roof_type = "flat"

    # Minimum area check
    if footprint_area < qa_std["min_area_m2"]:
        quality["issues"].append(
            f"Area {footprint_area:.1f}m² below minimum {qa_std['min_area_m2']}m²"
        )

    # Volume bound check
    if volume > qa_std["max_volume_m3"]:
        quality["issues"].append(
            f"Volume {volume:.0f}m³ exceeds maximum {qa_std['max_volume_m3']}m³"
        )

    return {
        "building_id": building_id,
        "height_m": round(height_m, 2) if height_m else None,
        "base_elevation_m": round(base_elev, 2) if base_elev else None,
        "floors_proxy": floor_info["floors_proxy"],
        "floors_min": floor_info["floors_min"],
        "floors_max": floor_info["floors_max"],
        "floor_height_assumed_m": floor_info["floor_height_assumed_m"],
        "footprint_area_m2": round(footprint_area, 2),
        "volume_m3": round(volume, 1),
        "roof_type": roof_type,
        "height_method": actual_method,
        "quality_code": quality["quality_code"],
        "quality_label": quality["quality_label"],
        "coverage_ratio": quality["coverage_ratio"],
        "height_stdev": quality["height_stdev"],
        "n_valid_pixels": quality["n_valid_pixels"],
        "n_total_pixels": quality["n_total_pixels"],
        "quality_issues": quality["issues"],
        "geometry": poly,
    }


def analyze_all_buildings(
    footprints: List[Tuple[int, List[List[float]]]],
    dsm: np.ndarray,
    dtm: np.ndarray,
    transform: Tuple[float, float, float, float],
    standards: Dict,
    **kwargs,
) -> List[Dict[str, Any]]:
    """Analyze all building footprints."""
    results = []
    for bldg_id, poly in footprints:
        result = analyze_single_building(
            bldg_id, poly, dsm, dtm, transform, standards, **kwargs
        )
        results.append(result)
    return results


# ============================================================
# Statistics
# ============================================================

def compute_building_stats(buildings: List[Dict]) -> Dict[str, Any]:
    """Compute summary statistics for all buildings."""
    heights = [b["height_m"] for b in buildings if b["height_m"] is not None]
    areas = [b["footprint_area_m2"] for b in buildings]
    volumes = [b["volume_m3"] for b in buildings]
    floors = [b["floors_proxy"] for b in buildings if b["floors_proxy"] > 0]
    qualities = [b["quality_code"] for b in buildings]

    n_total = len(buildings)
    n_with_height = len(heights)
    coverage_pct = n_with_height / n_total * 100 if n_total > 0 else 0.0

    stats = {
        "n_total": n_total,
        "n_with_height": n_with_height,
        "n_missing_height": n_total - n_with_height,
        "height_coverage_pct": round(coverage_pct, 1),
        "total_footprint_area_m2": round(sum(areas), 2),
        "total_volume_m3": round(sum(volumes), 1),
    }

    if heights:
        h_arr = np.array(heights)
        stats.update({
            "height_mean_m": round(float(np.mean(h_arr)), 2),
            "height_median_m": round(float(np.median(h_arr)), 2),
            "height_std_m": round(float(np.std(h_arr)), 2),
            "height_min_m": round(float(np.min(h_arr)), 2),
            "height_max_m": round(float(np.max(h_arr)), 2),
        })

    if floors:
        f_arr = np.array(floors)
        stats.update({
            "floors_mean": round(float(np.mean(f_arr)), 1),
            "floors_max": int(np.max(f_arr)),
            "total_floors_proxy": int(np.sum(f_arr)),
        })

    if areas:
        stats["area_mean_m2"] = round(float(np.mean(areas)), 2)
        stats["area_median_m2"] = round(float(np.median(areas)), 2)

    # Quality code distribution
    quality_dist = {}
    for q in qualities:
        quality_dist[str(q)] = quality_dist.get(str(q), 0) + 1
    stats["quality_code_distribution"] = quality_dist

    return stats


# ============================================================
# Output Writers
# ============================================================

def write_buildings_geojson(buildings: List[Dict], output_dir: Path,
                             filename: str = "buildings_3d.geojson") -> Path:
    """Write buildings as GeoJSON FeatureCollection."""
    path = output_dir / filename
    features = []
    for b in buildings:
        # Remove geometry from properties, use it as GeoJSON geometry
        geom = b.get("geometry")
        props = {k: v for k, v in b.items() if k != "geometry"}

        # Convert numpy types for JSON serialization
        props = json.loads(json.dumps(props, default=str))

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [geom],
            },
            "properties": props,
        }
        features.append(feature)

    geojson = {"type": "FeatureCollection", "features": features}
    path.write_text(
        json.dumps(geojson, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    return path


def write_height_raster(buildings: List[Dict], dsm_shape: Tuple[int, int],
                        transform: Tuple[float, float, float, float],
                        output_dir: Path,
                        nodata: float = -9999.0) -> Path:
    """Write building height as a raster (same grid as DSM)."""
    path = output_dir / "height.tif"
    nrows, ncols = dsm_shape
    height_raster = np.full((nrows, ncols), nodata, dtype=np.float32)

    xmin_r, x_res, ymax_r, y_res = transform

    for b in buildings:
        if b["height_m"] is None:
            continue
        poly = b.get("geometry")
        if poly is None:
            continue
        pxmin, pymin, pxmax, pymax = polygon_bounds(poly)

        col_start = max(0, int(np.floor((pxmin - xmin_r) / x_res)))
        col_end = min(ncols, int(np.ceil((pxmax - xmin_r) / x_res)))
        row_start = max(0, int(np.floor((pymax - ymax_r) / y_res)))
        row_end = min(nrows, int(np.ceil((pymin - ymax_r) / y_res)))

        for r in range(row_start, row_end):
            for c in range(col_start, col_end):
                height_raster[r, c] = b["height_m"]

    # Save as raw numpy binary (simplified; in production use rasterio)
    raw_path = output_dir / "height.npy"
    np.save(str(raw_path), height_raster)

    # Also save metadata
    meta = {
        "shape": list(dsm_shape),
        "transform": list(transform),
        "nodata": nodata,
        "description": "Building height raster (numpy array saved as .npy)",
    }
    meta_path = output_dir / "height_meta.json"
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")

    return raw_path


def write_building_stats_csv(buildings: List[Dict], output_dir: Path) -> Path:
    """Write building statistics to CSV."""
    path = output_dir / "building_stats.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "building_id", "height_m", "floors_proxy", "floors_min",
            "floors_max", "footprint_area_m2", "volume_m3", "roof_type",
            "height_method", "quality_code", "quality_label",
            "coverage_ratio", "height_stdev",
        ])
        for b in buildings:
            writer.writerow([
                b["building_id"],
                b.get("height_m", ""),
                b.get("floors_proxy", ""),
                b.get("floors_min", ""),
                b.get("floors_max", ""),
                b.get("footprint_area_m2", ""),
                b.get("volume_m3", ""),
                b.get("roof_type", ""),
                b.get("height_method", ""),
                b.get("quality_code", ""),
                b.get("quality_label", ""),
                b.get("coverage_ratio", ""),
                b.get("height_stdev", ""),
            ])
    return path


def write_quality_flags_geojson(buildings: List[Dict], output_dir: Path) -> Path:
    """Write quality flags as GeoJSON."""
    path = output_dir / "quality_flags.geojson"
    features = []
    for b in buildings:
        if b.get("quality_issues") or b.get("quality_code", 5) >= 4:
            geom = b.get("geometry")
            if geom is None:
                continue
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [geom],
                },
                "properties": {
                    "building_id": b["building_id"],
                    "quality_code": b["quality_code"],
                    "quality_label": b["quality_label"],
                    "issues": "; ".join(b.get("quality_issues", [])),
                    "height_m": b.get("height_m"),
                },
            })

    geojson = {"type": "FeatureCollection", "features": features}
    path.write_text(
        json.dumps(geojson, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    return path


# ============================================================
# Synthetic Data Generation
# ============================================================

def generate_synthetic_footprints(n_buildings: int = 10,
                                   area: float = 200.0,
                                   seed: int = 42) -> List[Tuple[int, List[List[float]]]]:
    """
    Generate synthetic building footprints for testing.

    Returns:
        List of (building_id, polygon) tuples
    """
    rng = np.random.RandomState(seed)
    footprints = []

    # Grid layout with some jitter
    grid_size = int(np.ceil(np.sqrt(n_buildings)))
    cell_size = area / grid_size

    idx = 0
    for row in range(grid_size):
        for col in range(grid_size):
            if idx >= n_buildings:
                break
            base_x = col * cell_size + rng.uniform(2, cell_size * 0.3)
            base_y = row * cell_size + rng.uniform(2, cell_size * 0.3)
            w = rng.uniform(8, cell_size * 0.5)
            h = rng.uniform(8, cell_size * 0.5)
            poly = create_polygon(float(base_x), float(base_y), float(w), float(h))
            footprints.append((idx + 1, poly))
            idx += 1

    return footprints[:n_buildings]


def generate_synthetic_dtm_dsm(n_rows: int = 100, n_cols: int = 100,
                               area: float = 200.0,
                               building_heights: Optional[List[float]] = None,
                               ground_elev: float = 50.0,
                               seed: int = 42) -> Tuple[np.ndarray, np.ndarray, List[Tuple[int, List[List[float]]]]]:
    """
    Generate synthetic DSM and DTM with known building heights.

    Args:
        n_rows, n_cols: Raster dimensions
        area: Spatial extent in meters (square)
        building_heights: List of known heights for buildings
        ground_elev: Base ground elevation
        seed: Random seed

    Returns:
        (dsm, dtm, footprints) tuple
    """
    rng = np.random.RandomState(seed)
    x_res = area / n_cols
    y_res = area / n_rows

    # DTM: smooth ground surface with slight slope and noise
    dtm = np.zeros((n_rows, n_cols), dtype=np.float32)
    for r in range(n_rows):
        for c in range(n_cols):
            # Gentle slope + small noise
            dtm[r, c] = ground_elev + (r / n_rows) * 2.0 + rng.normal(0, 0.1)

    # DSM starts as DTM
    dsm = dtm.copy()

    # Generate footprints
    if building_heights is None:
        n_buildings = 5
        building_heights = [rng.uniform(6, 30) for _ in range(n_buildings)]
    else:
        n_buildings = len(building_heights)

    footprints = generate_synthetic_footprints(n_buildings, area, seed)

    # Add buildings to DSM
    # Transform: (xmin, x_res, ymax, y_res) — standard north-up raster
    transform = (0.0, x_res, area, -y_res)  # ymax = area, y_res negative
    ymax_r = area  # top of raster

    for i, (bldg_id, poly) in enumerate(footprints):
        height = building_heights[i]
        pxmin, pymin, pxmax, pymax = polygon_bounds(poly)

        col_start = max(0, int(np.floor((pxmin - 0.0) / x_res)))
        col_end = min(n_cols, int(np.ceil((pxmax - 0.0) / x_res)))
        row_start = max(0, int(np.floor((pymax - ymax_r) / (-y_res))))
        row_end = min(n_rows, int(np.ceil((pymin - ymax_r) / (-y_res))))

        for r in range(row_start, row_end):
            for c in range(col_start, col_end):
                dsm[r, c] += height

    return dsm, dtm, footprints


def generate_synthetic_point_cloud(
    footprints: List[Tuple[int, List[List[float]]]],
    heights: List[float],
    area: float = 200.0,
    points_per_building: int = 100,
    seed: int = 42,
) -> Dict[int, np.ndarray]:
    """Generate synthetic point cloud Z values for buildings."""
    rng = np.random.RandomState(seed)
    point_clouds = {}

    for i, (bldg_id, poly) in enumerate(footprints):
        pxmin, pymin, pxmax, pymax = polygon_bounds(poly)
        height = heights[i]
        ground_z = 50.0

        # Generate points: 70% ground + 30% roof
        n_roof = int(points_per_building * 0.3)
        n_ground = points_per_building - n_roof

        ground_points = ground_z + rng.normal(0, 0.3, n_ground)
        roof_points = ground_z + height + rng.normal(0, 0.5, n_roof)

        all_points = np.concatenate([ground_points, roof_points])
        point_clouds[bldg_id] = all_points

    return point_clouds


# ============================================================
# File-based Data Loading
# ============================================================

def load_dsm(path: str) -> Tuple[np.ndarray, Tuple[float, float, float, float]]:
    """Load a single-band DSM GeoTIFF. Returns (raster, transform_tuple)
    where transform_tuple is (xmin, x_res, ymax, y_res) compatible with the
    synthetic branch's transform format.
    """
    if not _RASTERIO_AVAILABLE:
        raise RuntimeError(
            "rasterio is required for file-based mode but is not installed. "
            "Install via: pip install rasterio"
        )
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"DSM not found: {path}")
    with rasterio.open(path) as ds:
        h, w = ds.height, ds.width
        # Read in the raster's native dtype when possible
        src_dtype = ds.dtypes[0]
        np_dtype = np.dtype(src_dtype) if src_dtype in (
            "uint8", "uint16", "int16", "int32", "float32", "float64",
        ) else np.float32
        if np_dtype.kind == "f":
            data = np.empty((h, w), dtype=np.float32)
        else:
            data = np.empty((h, w), dtype=np_dtype)
        ds.read(1, out=data)
        # rasterio Affine.transform: (c, a, b, f, d, e) where a=x_res, e=y_res(neg)
        t = ds.transform
        transform_tuple = (float(t.c), float(t.a), float(t.f), float(t.e))
    return data.astype(np.float32), transform_tuple


def load_footprints_geojson(path: str) -> List[Tuple[int, List[List[float]]]]:
    """Load building footprints from a GeoJSON/Shapefile. Returns list of
    (id, polygon_ring) tuples where polygon_ring is a list of [x, y] pairs.

    Supports:
      * GeoJSON (.geojson / .json) — read with json + shapely
      * Shapefile (.shp) — read with fiona
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Footprints file not found: {path}")
    suffix = p.suffix.lower()

    if suffix in (".geojson", ".json"):
        try:
            import json as _json
            from shapely.geometry import shape as _shape
        except ImportError as e:
            raise RuntimeError(
                "GeoJSON footprints require shapely. Install via: pip install shapely"
            ) from e
        data = _json.loads(p.read_text(encoding="utf-8"))
        features = data.get("features") if isinstance(data, dict) else data
        if not features:
            raise ValueError(f"No features found in GeoJSON: {path}")
        out = []
        for idx, feat in enumerate(features, start=1):
            geom = feat.get("geometry") if isinstance(feat, dict) else None
            if not geom:
                continue
            poly = _shape(geom)
            # Use exterior ring coordinates; skip non-polygons
            if poly.geom_type == "Polygon":
                ring = [[float(x), float(y)] for x, y in poly.exterior.coords]
                out.append((idx, ring))
        if not out:
            raise ValueError(f"No polygon features in GeoJSON: {path}")
        return out

    if suffix == ".shp":
        try:
            import fiona
            from shapely.geometry import shape as _shape
        except ImportError as e:
            raise RuntimeError(
                "Shapefile footprints require fiona + shapely. "
                "Install via: pip install fiona shapely"
            ) from e
        out = []
        with fiona.open(path) as src:
            for idx, feat in enumerate(src, start=1):
                geom = feat.get("geometry")
                if not geom:
                    continue
                poly = _shape(geom)
                if poly.geom_type == "Polygon":
                    ring = [[float(x), float(y)] for x, y in poly.exterior.coords]
                    out.append((idx, ring))
        if not out:
            raise ValueError(f"No polygon features in Shapefile: {path}")
        return out

    raise ValueError(f"Unsupported footprints format: {suffix} (expected .geojson/.json/.shp)")


# ============================================================
# Report Generation
# ============================================================

def generate_report_html(buildings: List[Dict], stats: Dict,
                         output_dir: Path) -> Path:
    """Generate HTML report for building height analysis."""
    path = output_dir / "report.html"

    n_total = stats.get("n_total", 0)
    n_with = stats.get("n_with_height", 0)
    coverage = stats.get("height_coverage_pct", 0.0)
    h_mean = stats.get("height_mean_m", "N/A")
    h_median = stats.get("height_median_m", "N/A")
    h_max = stats.get("height_max_m", "N/A")
    vol_total = stats.get("total_volume_m3", 0)
    floors_total = stats.get("total_floors_proxy", "N/A")

    # Format values safely
    if isinstance(h_mean, (int, float)):
        h_mean_str = f"{h_mean:.1f}"
    else:
        h_mean_str = str(h_mean)
    if isinstance(h_median, (int, float)):
        h_median_str = f"{h_median:.1f}"
    else:
        h_median_str = str(h_median)
    if isinstance(h_max, (int, float)):
        h_max_str = f"{h_max:.1f}"
    else:
        h_max_str = str(h_max)
    if isinstance(coverage, (int, float)):
        coverage_str = f"{coverage:.1f}%"
    else:
        coverage_str = str(coverage)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>建筑高度分析报告</title>
<style>
body {{ font-family: 'Microsoft YaHei', Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
.container {{ max-width: 900px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
h1 {{ color: #333; border-bottom: 3px solid #28a745; padding-bottom: 10px; }}
h2 {{ color: #555; margin-top: 30px; }}
table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
th, td {{ padding: 10px 15px; text-align: left; border-bottom: 1px solid #ddd; }}
th {{ background: #f8f9fa; font-weight: 600; }}
.metric {{ font-weight: bold; }}
.ok {{ color: #28a745; }}
.warn {{ color: #ffc107; }}
.fail {{ color: #dc3545; }}
</style>
</head>
<body>
<div class="container">
<h1>建筑高度分析报告</h1>
<p>生成时间: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}</p>

<h2>1. 概览</h2>
<table>
<tr><th>指标</th><th>值</th></tr>
<tr><td class="metric">建筑总数</td><td>{n_total}</td></tr>
<tr><td class="metric">成功估算高度</td><td>{n_with} ({coverage_str})</td></tr>
<tr><td class="metric">总建筑底面积</td><td>{stats.get('total_footprint_area_m2', 'N/A')} m²</td></tr>
<tr><td class="metric">总建筑体量</td><td>{vol_total} m³</td></tr>
<tr><td class="metric">总层数代理</td><td>{floors_total}</td></tr>
</table>

<h2>2. 高度统计</h2>
<table>
<tr><th>指标</th><th>值</th></tr>
<tr><td class="metric">平均高度</td><td>{h_mean_str} m</td></tr>
<tr><td class="metric">中位数高度</td><td>{h_median_str} m</td></tr>
<tr><td class="metric">最大高度</td><td>{h_max_str} m</td></tr>
<tr><td class="metric">最小高度</td><td>{stats.get('height_min_m', 'N/A')} m</td></tr>
<tr><td class="metric">高标准差</td><td>{stats.get('height_std_m', 'N/A')} m</td></tr>
</table>

<h2>3. 质量分布</h2>
<table>
<tr><th>质量码</th><th>说明</th><th>数量</th></tr>
"""

    codes = {
        "1": "高度可靠（DSM-DTM，覆盖度>80%）",
        "2": "高度较可靠（点云分位数）",
        "3": "高度估算（阴影/粗 DEM）",
        "4": "高度可疑（覆盖度不足或异常）",
        "5": "高度缺失",
    }
    dist = stats.get("quality_code_distribution", {})
    for code, label in codes.items():
        count = dist.get(code, 0)
        css_class = "ok" if code in ("1", "2") else ("warn" if code == "3" else "fail")
        html += f'<tr><td class="{css_class}">#{code}</td><td>{label}</td><td>{count}</td></tr>\n'

    html += """
</table>

<h2>4. 建筑明细</h2>
<table>
<tr><th>ID</th><th>高度(m)</th><th>层数</th><th>面积(m²)</th><th>体量(m³)</th><th>质量</th></tr>
"""

    for b in buildings:
        h = b.get("height_m")
        h_str = f"{h:.1f}" if h is not None else "N/A"
        q = b.get("quality_code", 5)
        q_class = "ok" if q <= 2 else ("warn" if q == 3 else "fail")
        html += (f'<tr><td>{b["building_id"]}</td><td>{h_str}</td>'
                 f'<td>{b.get("floors_proxy", "N/A")}</td>'
                 f'<td>{b.get("footprint_area_m2", "N/A")}</td>'
                 f'<td>{b.get("volume_m3", "N/A")}</td>'
                 f'<td class="{q_class}">#{q} {b.get("quality_label", "")}</td></tr>\n')

    html += """
</table>
</div>
</body>
</html>
"""

    path.write_text(html, encoding="utf-8")
    return path


# ============================================================
# Main Pipeline
# ============================================================

def run_pipeline(args: argparse.Namespace) -> int:
    """Main building height estimation workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("bfh-output")
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logging(output_dir)
    logger.info("Building Footprint Height - Starting")

    # Load standards
    standards_path = getattr(args, 'standard_config', None)
    try:
        standards = load_height_standards(standards_path)
        logger.info(f"Standards loaded: version {standards.get('version', 'unknown')}")
    except Exception as e:
        logger.error(f"Failed to load standards: {e}")
        return EXIT_VALIDATION

    # --- Synthetic/demo mode or file-based mode ---
    # --synthetic forces synthetic; otherwise, providing --dsm uses real file input.
    explicit_synthetic = getattr(args, 'synthetic', False)
    has_user_file = bool(getattr(args, 'dsm', None))
    use_synthetic = explicit_synthetic or not has_user_file

    if use_synthetic:
        if explicit_synthetic:
            logger.info("Running in --synthetic demo mode")
        else:
            logger.info("No --dsm provided; using synthetic demo data")

        # Generate synthetic data
        known_heights = [9.0, 15.0, 21.0, 6.0, 30.0]
        dsm, dtm, footprints = generate_synthetic_dtm_dsm(
            n_rows=100, n_cols=100, area=200.0,
            building_heights=known_heights, seed=42
        )
        transform = (0.0, 2.0, 200.0, -2.0)  # (xmin, x_res, ymax, y_res)

        # Generate point clouds for each building
        point_clouds = generate_synthetic_point_cloud(
            footprints, known_heights, 200.0, 100, seed=42
        )

        # Determine method
        height_method = getattr(args, 'height_method', 'dsm_minus_dtm')
        floor_height = getattr(args, 'floor_height', 3.0)

        # Analyze buildings
        buildings = []
        for bldg_id, poly in footprints:
            pc_z = point_clouds.get(bldg_id)
            result = analyze_single_building(
                bldg_id, poly, dsm, dtm, transform, standards,
                point_cloud_z=pc_z,
                height_method=height_method,
                floor_height_m=floor_height,
            )
            buildings.append(result)

    else:
        # File-based mode — actually load the DSM (and optional DTM, footprints, point cloud)
        logger.info(f"File-based mode: loading DSM {args.dsm}")
        try:
            dsm, transform = load_dsm(args.dsm)
        except (FileNotFoundError, RasterioIOError, ValueError, RuntimeError) as e:
            logger.error(f"Failed to load DSM: {e}")
            return EXIT_VALIDATION
        logger.info(f"  Loaded DSM: shape={dsm.shape}, transform={transform}")

        # DTM: required for dsm_minus_dtm method; if user provided one, use it;
        # otherwise fall back to a smoothed DTM (low-percentile of DSM) as a
        # reasonable approximation that keeps the pipeline working.
        dtm_path = getattr(args, 'dtm', None)
        if dtm_path:
            try:
                dtm, _ = load_dsm(dtm_path)
                if dtm.shape != dsm.shape:
                    logger.warning(
                        f"  DSM/DTM shape mismatch: {dsm.shape} vs {dtm.shape}; "
                        f"resampling not implemented, using percentile-DTM on DSM"
                    )
                    dtm = np.percentile(dsm, 5, axis=0).astype(np.float32)
                    dtm = np.broadcast_to(dtm, dsm.shape).copy()
            except (FileNotFoundError, RasterioIOError, ValueError, RuntimeError) as e:
                logger.warning(f"  DTM load failed: {e}; using percentile-DTM on DSM")
                dtm = np.percentile(dsm, 5, axis=0).astype(np.float32)
                dtm = np.broadcast_to(dtm, dsm.shape).copy()
        else:
            # Use 5th-percentile per-column as a coarse DTM approximation
            # (better than a uniform min-filter for varied terrain).
            dtm = np.percentile(dsm, 5, axis=0).astype(np.float32)
            dtm = np.broadcast_to(dtm, dsm.shape).copy()
            logger.info("  No --dtm provided; using percentile-DTM approximation")

        # Footprints: load from file, or skip height estimation and just report raster stats
        fp_path = getattr(args, 'footprints', None)
        if fp_path:
            try:
                footprints = load_footprints_geojson(fp_path)
                logger.info(f"  Loaded {len(footprints)} footprints from {fp_path}")
            except (FileNotFoundError, ValueError, RuntimeError) as e:
                logger.error(f"Failed to load footprints: {e}")
                return EXIT_VALIDATION
        else:
            # Without footprints, we still produce a height raster derived from
            # the DSM. Synthesize a single 'whole-scene' footprint so the rest
            # of the pipeline can run.
            logger.info("  No --footprints provided; treating whole scene as one building")
            xmin, x_res, ymax, y_res = transform
            h, w = dsm.shape
            xmax = xmin + w * x_res
            ymin = ymax + h * y_res
            footprints = [(1, [
                [float(xmin), float(ymax)],
                [float(xmax), float(ymax)],
                [float(xmax), float(ymin)],
                [float(xmin), float(ymin)],
                [float(xmin), float(ymax)],
            ])]

        height_method = getattr(args, 'height_method', 'dsm_minus_dtm')
        floor_height = getattr(args, 'floor_height', 3.0)

        # Optional point cloud (CSV with x,y,z columns) — for the dsm_minus_dtm
        # branch it's a no-op; the analyze function checks presence internally.
        buildings = []
        for bldg_id, poly in footprints:
            result = analyze_single_building(
                bldg_id, poly, dsm, dtm, transform, standards,
                height_method=height_method,
                floor_height_m=floor_height,
            )
            buildings.append(result)

    # --- Compute statistics ---
    stats = compute_building_stats(buildings)
    logger.info(f"Analysis complete: {stats['n_with_height']}/{stats['n_total']} buildings with height")

    # --- Write outputs ---

    # buildings_3d.geojson
    geojson_path = write_buildings_geojson(buildings, output_dir)

    # height.tif (as .npy + meta)
    height_path = write_height_raster(buildings, dsm.shape, transform, output_dir)

    # building_stats.csv
    stats_path = write_building_stats_csv(buildings, output_dir)

    # quality_flags.geojson
    quality_path = write_quality_flags_geojson(buildings, output_dir)

    # report.html
    report_path = generate_report_html(buildings, stats, output_dir)

    # request.json
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "synthetic" if use_synthetic else "file",
        "height_method": getattr(args, 'height_method', 'dsm_minus_dtm'),
        "floor_height_m": getattr(args, 'floor_height', 3.0),
        "n_buildings": len(buildings),
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
        "n_buildings": len(buildings),
        "raster_shape": list(dsm.shape),
        "transform": list(transform),
        "height_method": getattr(args, 'height_method', 'dsm_minus_dtm'),
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # output-manifest.json
    output_files = {
        "buildings_3d.geojson": str(geojson_path),
        "height_raster_meta": str(output_dir / "height_meta.json"),
        "building_stats.csv": str(stats_path),
        "quality_flags.geojson": str(quality_path),
        "report.html": str(report_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(dataset_path),
    }
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "output_files": output_files,
        "parameters": vars(args),
        "summary": {
            "n_buildings": stats["n_total"],
            "n_with_height": stats["n_with_height"],
            "height_coverage_pct": stats["height_coverage_pct"],
        },
    }
    # Auto-download metadata (only present when --bbox/--aoi-file was used)
    if getattr(args, "_data_source", None):
        manifest["data_source"] = args._data_source
        manifest["fetched_at"] = datetime.now(timezone.utc).isoformat()
        manifest["collection"] = getattr(args, "_collection", None)
        manifest["bbox"] = getattr(args, "bbox", None)
        manifest["date_range"] = getattr(args, "date_range", None)
    manifest_path = output_dir / "output-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # qa.json
    qa = {
        "status": "complete",
        "checks": {
            "geojson_generated": geojson_path.exists(),
            "stats_generated": stats_path.exists(),
            "quality_flags_generated": quality_path.exists(),
            "report_generated": report_path.exists(),
            "all_outputs_written": all(Path(p).exists() for p in output_files.values()),
        },
        "statistics": stats,
    }
    qa_path = output_dir / "qa.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    logger.info(f"Complete: {stats['n_with_height']}/{stats['n_total']} buildings, "
                f"coverage={stats['height_coverage_pct']:.1f}%")
    cleanup_logging()
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Building Footprint Height Estimation")
    parser.add_argument("--dsm", default=None, help="Path to DSM GeoTIFF")
    parser.add_argument("--dtm", default=None, help="Path to DTM GeoTIFF")
    parser.add_argument("--footprints", default=None, help="Path to building footprints GeoJSON/Shapefile")
    parser.add_argument("--point-cloud", default=None, help="Path to LiDAR point cloud (LAS/CSV)")
    parser.add_argument("--synthetic", action="store_true",
                        help="Run with synthetic demo data (no real inputs needed)")
    parser.add_argument("--height-method", default="dsm_minus_dtm",
                        choices=["dsm_minus_dtm", "point_cloud_quantile", "shadow_based"],
                        help="Height estimation method (default: dsm_minus_dtm)")
    parser.add_argument("--floor-height", type=float, default=3.0,
                        help="Assumed floor height in meters (default: 3.0)")
    parser.add_argument("--output-dir", "-o", default="bfh-output",
                        help="Output directory (default: bfh-output)")
    parser.add_argument("--standard-config", default=None,
                        help="Path to building height standards JSON")
    add_bbox_date_args(parser)  # --bbox/--date-range/--aoi-file/--cache-dir
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    args = parser.parse_args()

    # If user supplied --bbox/--aoi-file but no --dsm, auto-download a
    # Copernicus GLO-30 DEM from Microsoft Planetary Computer.
    if not getattr(args, "dsm", None) and (
        getattr(args, "bbox", None) or getattr(args, "aoi_file", None)
    ):
        ok = _auto_download_dem(args)
        if not ok:
            print(
                "ERROR: --bbox/--aoi-file given but DEM download failed; "
                "pass --dsm explicitly to use a local file.",
                file=sys.stderr,
            )
            sys.exit(EXIT_VALIDATION)

    rc = validate_args(args)
    if rc != 0:
        sys.exit(rc)

    try:
        sys.exit(run_pipeline(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


def _auto_download_dem(args) -> bool:
    """Download one Copernicus GLO-30 DEM tile covering ``args.bbox``.

    Returns True on success (and mutates ``args.dsm`` to the downloaded
    path), False on any failure.
    """
    if not _SHARED_FETCHER_AVAILABLE:
        return False
    try:
        bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
        if bbox is None:
            return False
        # cop-dem-glo-30 is time-invariant; date_range can be omitted.
        # (MPC's date range is strict; for DEM we ignore the date_range arg)
        fetcher = DataFetcher(source=DataSource.PLANETARY_COMPUTER)
        items = fetcher.search_stac(
            collection="cop-dem-glo-30",
            bbox=bbox,
            date_range=DateRange("2020-01-01", "2021-12-31"),
            limit=1,
        )
        if not items:
            return False
        out_dir = Path(args.output_dir or "bfh-output") / "downloaded"
        paths = fetcher.download_assets(
            items=items, out_dir=out_dir, max_items=1, max_total_mb=200.0,
            prefer_assets=["data"],
        )
        if not paths:
            return False
        args.dsm = str(paths[0])
        args._data_source = "MPC"
        args._collection = "cop-dem-glo-30"
        return True
    except Exception as exc:
        print(f"WARN: auto-download failed: {exc}", file=sys.stderr)
        return False


if __name__ == "__main__":
    main()
