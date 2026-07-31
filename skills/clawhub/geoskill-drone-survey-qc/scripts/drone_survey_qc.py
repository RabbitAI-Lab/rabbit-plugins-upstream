#!/usr/bin/env python3
"""
Drone Survey QC - Automated quality inspection for UAV survey deliverables.

Checks drone aerial images, orthomosaics, DSM/DEM, control points, and
aerial triangulation reports. Generates coverage, clarity, seam, and
accuracy QA.

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



try:
    import rasterio
    _HAS_RASTERIO = True
except ImportError:
    _HAS_RASTERIO = False

EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# File-arg flags that must point to existing paths (None = skip check)
FILE_ARGS = {
    "project_dir": "args.project_dir",
    "orthomosaic": "args.orthomosaic",
    "dsm": "args.dsm",
    "camera_positions": "args.camera_positions",
    "control_points": "args.control_points",
    "standard_config": "args.standard_config",
}

# Numeric flags with (min, max) bounds; None = unbounded on that side
NUMERIC_RANGES = {
    # "camera_positions": (0, None),  # camera_positions is a path in this skill
}


def validate_args(args) -> int:
    """Validate file existence and numeric ranges.
    Returns exit code (0 = ok, 2 = arg error)."""
    for flag, accessor in FILE_ARGS.items():
        path = eval(accessor)  # safe: only string concat
        if path is not None and not Path(str(path)).exists():
            print(f"ERROR: --{flag.replace('_', '-')} not found: {path}", file=sys.stderr)
            return 2
    for flag, (lo, hi) in NUMERIC_RANGES.items():
        val = getattr(args, flag, None)
        if val is None:
            continue
        if not isinstance(val, (int, float)):
            continue
        if lo is not None and val < lo:
            print(f"ERROR: --{flag.replace('_', '-')}={val} below minimum {lo}", file=sys.stderr)
            return 2
        if hi is not None and val > hi:
            print(f"ERROR: --{flag.replace('_', '-')}={val} above maximum {hi}", file=sys.stderr)
            return 2
    return 0

# ============================================================
# Logging
# ============================================================

def setup_logging(output_dir: Path) -> logging.Logger:
    """Setup logging to file and console."""
    logger = logging.getLogger("dsq")
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
    """Close all handlers on the dsq logger."""
    logger = logging.getLogger("dsq")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)


# ============================================================
# QC Standards
# ============================================================

def load_qc_standards(standards_path: Optional[str] = None) -> Dict:
    """Load QC standards from JSON file, merging with defaults for missing keys."""
    # Load defaults first
    script_dir = Path(__file__).parent
    defaults_path = script_dir.parent / "references" / "qc_standards.json"
    with open(defaults_path, "r", encoding="utf-8") as f:
        defaults = json.load(f)

    if standards_path is None:
        return defaults

    # Load custom and merge (custom overrides defaults)
    with open(standards_path, "r", encoding="utf-8") as f:
        custom = json.load(f)

    # Deep merge: custom values override defaults
    merged = defaults.copy()
    for key, value in custom.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key].update(value)
        else:
            merged[key] = value
    return merged


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


def compute_footprint_bounds(
    x: float, y: float, altitude: float,
    sensor_width_mm: float, sensor_height_mm: float,
    focal_length_mm: float, gsd_cm: float
) -> Tuple[float, float, float, float]:
    """
    Compute ground footprint bounds from camera position and parameters.

    Returns:
        (xmin, ymin, xmax, ymax) in ground units
    """
    # Ground coverage width/height in meters
    ground_w = (sensor_width_mm / focal_length_mm) * altitude
    ground_h = (sensor_height_mm / focal_length_mm) * altitude

    xmin = x - ground_w / 2.0
    xmax = x + ground_w / 2.0
    ymin = y - ground_h / 2.0
    ymax = y + ground_h / 2.0

    return (xmin, ymin, xmax, ymax)


def compute_gsd_cm(altitude_m: float, focal_length_mm: float,
                   sensor_width_mm: float, image_width_px: int) -> float:
    """
    Compute GSD (cm/pixel) from flight parameters.

    GSD = (altitude * sensor_width) / (focal_length * image_width) * 100
    """
    gsd_m = (altitude_m * sensor_width_mm) / (focal_length_mm * image_width_px)
    return gsd_m * 100.0  # convert to cm


def compute_overlap(poly_a: List[List[float]], poly_b: List[List[float]]) -> float:
    """
    Compute overlap ratio between two axis-aligned polygons.
    Returns intersection_area / min(area_a, area_b).
    """
    axmin = min(p[0] for p in poly_a[:-1])
    axmax = max(p[0] for p in poly_a[:-1])
    aymin = min(p[1] for p in poly_a[:-1])
    aymax = max(p[1] for p in poly_a[:-1])

    bxmin = min(p[0] for p in poly_b[:-1])
    bxmax = max(p[0] for p in poly_b[:-1])
    bymin = min(p[1] for p in poly_b[:-1])
    bymax = max(p[1] for p in poly_b[:-1])

    # Intersection
    ixmin = max(axmin, bxmin)
    ixmax = min(axmax, bxmax)
    iymin = max(aymin, bymin)
    iymax = min(aymax, bymax)

    if ixmax <= ixmin or iymax <= iymin:
        return 0.0

    inter_area = (ixmax - ixmin) * (iymax - iymin)
    area_a = (axmax - axmin) * (aymax - aymin)
    area_b = (bxmax - bxmin) * (bymax - bymin)

    if area_a <= 0 or area_b <= 0:
        return 0.0

    return inter_area / min(area_a, area_b)


# ============================================================
# Image Quality Analysis
# ============================================================

def detect_blur_laplacian(image: np.ndarray) -> float:
    """
    Detect blur using Laplacian variance.
    Lower values = blurrier image.

    Args:
        image: 2D grayscale array (uint8)

    Returns:
        Variance of Laplacian (higher = sharper)
    """
    # Laplacian kernel
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float64)
    h, w = image.shape

    if h < 3 or w < 3:
        return 0.0

    # Manual convolution (no scipy dependency)
    laplacian = np.zeros((h - 2, w - 2), dtype=np.float64)
    for di in range(3):
        for dj in range(3):
            laplacian += kernel[di, dj] * image[di:h-2+di, dj:w-2+dj].astype(np.float64)

    return float(np.var(laplacian))


def analyze_exposure(image: np.ndarray) -> Dict[str, Any]:
    """
    Analyze exposure statistics.

    Args:
        image: 2D grayscale array (uint8)

    Returns:
        Dict with overexposed/underexposed fractions and mean
    """
    total_pixels = image.size
    if total_pixels == 0:
        return {
            "mean": 0.0,
            "overexposed_fraction": 0.0,
            "underexposed_fraction": 0.0,
        }

    overexposed = int(np.sum(image >= 250))
    underexposed = int(np.sum(image <= 10))

    return {
        "mean": float(np.mean(image)),
        "overexposed_fraction": overexposed / total_pixels,
        "underexposed_fraction": underexposed / total_pixels,
    }


def compute_image_quality(image: np.ndarray) -> Dict[str, Any]:
    """
    Compute comprehensive image quality metrics.

    Args:
        image: 2D grayscale or 3D (H,W,C) array

    Returns:
        Dict with blur, exposure, and contrast metrics
    """
    if image.ndim == 3:
        # Convert to grayscale: weighted average
        if image.shape[2] >= 3:
            gray = (0.299 * image[:, :, 0] +
                    0.587 * image[:, :, 1] +
                    0.114 * image[:, :, 2]).astype(np.uint8)
        else:
            gray = image[:, :, 0].astype(np.uint8)
    else:
        gray = image.astype(np.uint8) if image.dtype != np.uint8 else image

    blur_var = detect_blur_laplacian(gray)
    exposure = analyze_exposure(gray)

    return {
        "blur_variance": round(blur_var, 2),
        "mean_brightness": round(exposure["mean"], 2),
        "overexposed_fraction": round(exposure["overexposed_fraction"], 4),
        "underexposed_fraction": round(exposure["underexposed_fraction"], 4),
        "std_brightness": round(float(np.std(gray.astype(np.float64))), 2),
    }


# ============================================================
# Overlap Analysis
# ============================================================

def analyze_overlap(camera_positions: List[Dict], standards: Dict) -> Dict[str, Any]:
    """
    Analyze forward and side overlap from camera positions.

    Args:
        camera_positions: List of dicts with keys: x, y, altitude,
                         sensor_width_mm, sensor_height_mm, focal_length_mm,
                         image_width_px, image_height_px
        standards: QC standards dict

    Returns:
        Overlap analysis results
    """
    if len(camera_positions) < 2:
        return {
            "n_images": len(camera_positions),
            "forward_overlap_mean": 0.0,
            "side_overlap_mean": 0.0,
            "issues": ["Insufficient images for overlap analysis"],
        }

    # Compute footprints
    footprints = []
    for cam in camera_positions:
        bounds = compute_footprint_bounds(
            cam["x"], cam["y"], cam["altitude"],
            cam.get("sensor_width_mm", 13.2),
            cam.get("sensor_height_mm", 8.8),
            cam.get("focal_length_mm", 8.8),
            cam.get("gsd_cm", 2.0)
        )
        poly = create_polygon(bounds[0], bounds[1],
                             bounds[2] - bounds[0], bounds[3] - bounds[1])
        footprints.append(poly)

    # Compute pairwise overlaps
    # Strategy: cluster cameras into strips by their cross-strip coordinate,
    # then compute forward (same-strip) and side (cross-strip) overlaps.
    forward_overlaps = []
    side_overlaps = []

    if len(camera_positions) >= 2:
        # Determine flight axis from first two images
        dx = camera_positions[1]["x"] - camera_positions[0]["x"]
        dy = camera_positions[1]["y"] - camera_positions[0]["y"]
        flight_axis = "x" if abs(dx) >= abs(dy) else "y"

        # Cross-strip coordinate for each camera
        cross_coords = []
        for cam in camera_positions:
            if flight_axis == "x":
                cross_coords.append(cam["y"])
            else:
                cross_coords.append(cam["x"])

        # Cluster into strips: group cameras with similar cross-strip coordinate
        cross_arr = np.array(cross_coords)
        sorted_cross = np.sort(cross_arr)
        # Find large gaps between consecutive cross-coords (strip boundaries)
        if len(sorted_cross) > 1:
            diffs = np.diff(sorted_cross)
            median_diff = np.median(diffs[diffs > 0.1]) if np.any(diffs > 0.1) else 1.0
            # Strip boundary: gap > 3x median adjacent diff
            boundary_threshold = max(median_diff * 3.0, 10.0)
            strip_id = np.zeros(len(camera_positions), dtype=int)
            for i in range(1, len(camera_positions)):
                if abs(cross_coords[i] - cross_coords[i - 1]) > boundary_threshold:
                    strip_id[i] = strip_id[i - 1] + 1
                else:
                    strip_id[i] = strip_id[i - 1]
        else:
            strip_id = np.zeros(len(camera_positions), dtype=int)

        # Forward overlap: consecutive cameras in same strip
        for i in range(len(footprints) - 1):
            if strip_id[i] == strip_id[i + 1]:
                overlap = compute_overlap(footprints[i], footprints[i + 1])
                forward_overlaps.append(overlap)

        # Side overlap: for each camera, find nearest camera in adjacent strip
        along_coords = []
        for cam in camera_positions:
            along_coords.append(cam["x"] if flight_axis == "x" else cam["y"])

        unique_strips = np.unique(strip_id)
        for s in range(len(unique_strips) - 1):
            curr_strip = np.where(strip_id == unique_strips[s])[0]
            next_strip = np.where(strip_id == unique_strips[s + 1])[0]
            for i in curr_strip:
                # Find nearest camera in adjacent strip by along-strip position
                dists = [abs(along_coords[i] - along_coords[j]) for j in next_strip]
                nearest_j = next_strip[np.argmin(dists)]
                overlap = compute_overlap(footprints[i], footprints[nearest_j])
                side_overlaps.append(overlap)

    # Fallback: if no side overlaps found, use every-other comparison
    if not side_overlaps and len(footprints) >= 3:
        for i in range(len(footprints) - 2):
            overlap = compute_overlap(footprints[i], footprints[i + 2])
            side_overlaps.append(overlap)

    fwd_mean = float(np.mean(forward_overlaps)) if forward_overlaps else 0.0
    side_mean = float(np.mean(side_overlaps)) if side_overlaps else 0.0

    # Check against standards
    issues = []
    overlap_std = standards.get("overlap", {})
    fwd_min = overlap_std.get("forward_min", 0.70)
    side_min = overlap_std.get("side_min", 0.60)

    if fwd_mean < fwd_min:
        issues.append(
            f"Forward overlap {fwd_mean:.1%} below minimum {fwd_min:.1%}"
        )
    if side_mean < side_min:
        issues.append(
            f"Side overlap {side_mean:.1%} below minimum {side_min:.1%}"
        )

    return {
        "n_images": len(camera_positions),
        "forward_overlap_mean": round(fwd_mean, 4),
        "forward_overlap_min": round(float(min(forward_overlaps)) if forward_overlaps else 0.0, 4),
        "side_overlap_mean": round(side_mean, 4),
        "side_overlap_min": round(float(min(side_overlaps)) if side_overlaps else 0.0, 4),
        "issues": issues,
        "pass": len(issues) == 0,
    }


# ============================================================
# GSD Analysis
# ============================================================

def analyze_gsd(camera_positions: List[Dict], standards: Dict) -> Dict[str, Any]:
    """
    Analyze GSD from camera parameters.

    Args:
        camera_positions: List of camera position dicts
        standards: QC standards dict

    Returns:
        GSD analysis results
    """
    if not camera_positions:
        return {"n_images": 0, "gsd_mean_cm": 0.0, "issues": ["No camera data"]}

    gsd_values = []
    for cam in camera_positions:
        gsd = compute_gsd_cm(
            cam["altitude"],
            cam.get("focal_length_mm", 8.8),
            cam.get("sensor_width_mm", 13.2),
            cam.get("image_width_px", 4000)
        )
        gsd_values.append(gsd)

    gsd_arr = np.array(gsd_values)
    gsd_mean = float(np.mean(gsd_arr))
    gsd_max = float(np.max(gsd_arr))

    issues = []
    max_allowed = standards["gsd"]["max_cm"]
    warn_allowed = standards["gsd"]["warning_cm"]

    if gsd_max > max_allowed:
        issues.append(f"Max GSD {gsd_max:.2f} cm exceeds limit {max_allowed:.2f} cm")
    elif gsd_mean > warn_allowed:
        issues.append(f"Mean GSD {gsd_mean:.2f} cm exceeds warning {warn_allowed:.2f} cm")

    return {
        "n_images": len(camera_positions),
        "gsd_mean_cm": round(gsd_mean, 3),
        "gsd_max_cm": round(gsd_max, 3),
        "gsd_min_cm": round(float(np.min(gsd_arr)), 3),
        "issues": issues,
        "pass": len(issues) == 0,
    }


# ============================================================
# Orthomosaic / DSM QA
# ============================================================

def analyze_orthomosaic(raster: np.ndarray, nodata_value: float = 0.0,
                        has_rgb: bool = True) -> Dict[str, Any]:
    """
    Analyze orthomosaic quality: nodata holes, texture, band stats.

    Args:
        raster: 2D or 3D numpy array (H, W) or (H, W, C)
        nodata_value: Value representing nodata
        has_rgb: Whether to check for RGB bands

    Returns:
        Quality metrics dict
    """
    if raster.ndim == 3:
        h, w, c = raster.shape
        # Check each band for nodata
        total_pixels = h * w
        nodata_count = 0
        for band_idx in range(c):
            band = raster[:, :, band_idx]
            nodata_count = max(nodata_count, int(np.sum(band == nodata_value)))
        nodata_fraction = nodata_count / total_pixels if total_pixels > 0 else 0.0

        # Texture: use first band
        gray = raster[:, :, 0].astype(np.float64)
    else:
        h, w = raster.shape
        total_pixels = h * w
        nodata_count = int(np.sum(raster == nodata_value))
        nodata_fraction = nodata_count / total_pixels if total_pixels > 0 else 0.0
        gray = raster.astype(np.float64)

    # Texture statistics
    texture_std = float(np.std(gray))
    texture_mean = float(np.mean(gray))

    # Edge detection (simple gradient magnitude)
    if gray.shape[0] > 2 and gray.shape[1] > 2:
        dx = np.abs(gray[1:, :] - gray[:-1, :])
        dy = np.abs(gray[:, 1:] - gray[:, :-1])
        edge_density = float(np.mean(np.concatenate([dx.flatten(), dy.flatten()])))
    else:
        edge_density = 0.0

    return {
        "shape": list(raster.shape),
        "nodata_fraction": round(nodata_fraction, 6),
        "nodata_count": nodata_count,
        "texture_mean": round(texture_mean, 2),
        "texture_std": round(texture_std, 2),
        "edge_density": round(edge_density, 4),
        "n_bands": raster.shape[2] if raster.ndim == 3 else 1,
    }


def analyze_dsm_quality(raster: np.ndarray, nodata_value: float = -9999.0) -> Dict[str, Any]:
    """
    Analyze DSM/DEM quality.

    Args:
        raster: 2D numpy array of elevation values
        nodata_value: Nodata value

    Returns:
        Quality metrics dict
    """
    if raster.ndim != 2:
        return {"error": "DSM must be 2D raster"}

    total_pixels = raster.size
    nodata_mask = (raster == nodata_value) | np.isnan(raster) | np.isinf(raster)
    nodata_count = int(np.sum(nodata_mask))
    nodata_fraction = nodata_count / total_pixels if total_pixels > 0 else 0.0

    valid_data = raster[~nodata_mask]

    if valid_data.size == 0:
        return {
            "shape": list(raster.shape),
            "nodata_fraction": 1.0,
            "nodata_count": nodata_count,
            "z_min": None,
            "z_max": None,
            "z_mean": None,
            "z_std": None,
        }

    return {
        "shape": list(raster.shape),
        "nodata_fraction": round(nodata_fraction, 6),
        "nodata_count": nodata_count,
        "z_min": round(float(np.min(valid_data)), 3),
        "z_max": round(float(np.max(valid_data)), 3),
        "z_mean": round(float(np.mean(valid_data)), 3),
        "z_std": round(float(np.std(valid_data)), 3),
    }


# ============================================================
# Control Point Analysis
# ============================================================

def analyze_control_points(
    points: List[Dict],
    standards: Dict,
    point_type: str = "gcp"
) -> Dict[str, Any]:
    """
    Analyze control point residuals.

    Args:
        points: List of dicts with keys: id, x, y, z (measured),
                x_ref, y_ref, z_ref (reference/expected)
        standards: QC standards dict
        point_type: 'gcp' (control point) or 'check' (check point)

    Returns:
        Residual analysis results
    """
    if not points:
        return {
            "point_type": point_type,
            "n_points": 0,
            "rmse_xy": 0.0,
            "rmse_z": 0.0,
            "max_residual": 0.0,
            "issues": [f"No {point_type} points provided"],
        }

    residuals_xy = []
    residuals_z = []
    residuals_3d = []
    point_results = []

    for pt in points:
        dx = pt["x"] - pt["x_ref"]
        dy = pt["y"] - pt["y_ref"]
        dz = pt.get("z", 0.0) - pt.get("z_ref", 0.0)

        res_xy = np.sqrt(dx**2 + dy**2)
        res_3d = np.sqrt(dx**2 + dy**2 + dz**2)

        residuals_xy.append(res_xy)
        residuals_z.append(abs(dz))
        residuals_3d.append(res_3d)

        point_results.append({
            "id": pt.get("id", ""),
            "residual_xy": round(res_xy, 4),
            "residual_z": round(abs(dz), 4),
            "residual_3d": round(res_3d, 4),
            "dx": round(dx, 4),
            "dy": round(dy, 4),
            "dz": round(dz, 4),
        })

    rmse_xy = float(np.sqrt(np.mean(np.array(residuals_xy)**2)))
    rmse_z = float(np.sqrt(np.mean(np.array(residuals_z)**2)))
    max_res = float(np.max(residuals_3d))
    mean_res = float(np.mean(residuals_3d))

    # Outlier detection using Median Absolute Deviation (MAD)
    # MAD is robust against outliers inflating the std deviation
    std_res = float(np.std(residuals_3d))
    threshold = standards["control_points"]["outlier_threshold_sigma"]
    outliers = []
    if len(residuals_3d) >= 7:
        median_res = float(np.median(residuals_3d))
        mad = float(np.median(np.abs(np.array(residuals_3d) - median_res)))
        # Scale MAD to approximate σ (for normal distribution: σ ≈ 1.4826 * MAD)
        scaled_mad = 1.4826 * mad if mad > 0 else std_res
        if scaled_mad > 0:
            for i, pr in enumerate(point_results):
                if abs(residuals_3d[i] - median_res) > threshold * scaled_mad:
                    outliers.append(pr["id"])

    # Check against standards
    issues = []
    cp_std = standards["control_points"]

    if point_type == "gcp":
        if rmse_xy > cp_std["rmse_max_m"]:
            issues.append(f"GCP RMSE_XY {rmse_xy:.3f}m exceeds limit {cp_std['rmse_max_m']}m")
        if max_res > cp_std["max_residual_m"]:
            issues.append(f"GCP max residual {max_res:.3f}m exceeds limit {cp_std['max_residual_m']}m")
    else:  # check points
        if rmse_xy > cp_std["rmse_max_m"]:
            issues.append(f"Check point RMSE_XY {rmse_xy:.3f}m exceeds limit {cp_std['rmse_max_m']}m")
        if max_res > cp_std["max_residual_m"]:
            issues.append(f"Check point max residual {max_res:.3f}m exceeds limit {cp_std['max_residual_m']}m")

    if outliers:
        issues.append(f"Outliers detected (>{threshold}σ): {outliers}")

    return {
        "point_type": point_type,
        "n_points": len(points),
        "rmse_xy": round(rmse_xy, 4),
        "rmse_z": round(rmse_z, 4),
        "max_residual": round(max_res, 4),
        "mean_residual": round(mean_res, 4),
        "std_residual": round(std_res, 4),
        "outliers": outliers,
        "point_results": point_results,
        "issues": issues,
        "pass": len(issues) == 0,
    }


# ============================================================
# Rule Engine
# ============================================================

def evaluate_qc_rules(
    image_quality: Optional[Dict],
    overlap: Optional[Dict],
    gsd: Optional[Dict],
    ortho_qa: Optional[Dict],
    dsm_qa: Optional[Dict],
    gcp_results: Optional[Dict],
    check_results: Optional[Dict],
    standards: Dict,
) -> Dict[str, Any]:
    """
    Evaluate all QC rules and produce summary.

    Returns:
        Dict with overall pass/fail, issues list, and per-check results
    """
    checks = {}
    all_issues = []

    # Image quality checks
    if image_quality:
        img_issues = []
        blur_var = image_quality.get("blur_variance", 0)
        if blur_var < standards["blur"]["laplacian_variance_min"]:
            img_issues.append(f"Blur variance {blur_var:.1f} below {standards['blur']['laplacian_variance_min']}")

        overex = image_quality.get("overexposed_fraction", 0)
        if overex > standards["exposure"]["overexposed_fraction_max"]:
            img_issues.append(f"Overexposed fraction {overex:.2%} exceeds limit")

        underex = image_quality.get("underexposed_fraction", 0)
        if underex > standards["exposure"]["underexposed_fraction_max"]:
            img_issues.append(f"Underexposed fraction {underex:.2%} exceeds limit")

        checks["image_quality"] = {
            "pass": len(img_issues) == 0,
            "issues": img_issues,
        }
        all_issues.extend(img_issues)

    # Overlap checks
    if overlap:
        checks["overlap"] = {
            "pass": overlap.get("pass", False),
            "issues": overlap.get("issues", []),
        }
        all_issues.extend(overlap.get("issues", []))

    # GSD checks
    if gsd:
        checks["gsd"] = {
            "pass": gsd.get("pass", False),
            "issues": gsd.get("issues", []),
        }
        all_issues.extend(gsd.get("issues", []))

    # Orthomosaic checks
    if ortho_qa:
        ortho_issues = []
        nd_frac = ortho_qa.get("nodata_fraction", 0)
        if nd_frac > standards["orthomosaic"]["nodata_fraction_max"]:
            ortho_issues.append(f"Nodata fraction {nd_frac:.2%} exceeds {standards['orthomosaic']['nodata_fraction_max']:.2%}")
        checks["orthomosaic"] = {
            "pass": len(ortho_issues) == 0,
            "issues": ortho_issues,
        }
        all_issues.extend(ortho_issues)

    # DSM checks
    if dsm_qa:
        dsm_issues = []
        nd_frac = dsm_qa.get("nodata_fraction", 0)
        if nd_frac > standards["dsm"]["nodata_fraction_max"]:
            dsm_issues.append(f"DSM nodata fraction {nd_frac:.2%} exceeds {standards['dsm']['nodata_fraction_max']:.2%}")
        checks["dsm"] = {
            "pass": len(dsm_issues) == 0,
            "issues": dsm_issues,
        }
        all_issues.extend(dsm_issues)

    # GCP checks
    if gcp_results:
        checks["gcp"] = {
            "pass": gcp_results.get("pass", False),
            "issues": gcp_results.get("issues", []),
        }
        all_issues.extend(gcp_results.get("issues", []))

    # Check point checks
    if check_results:
        checks["check_points"] = {
            "pass": check_results.get("pass", False),
            "issues": check_results.get("issues", []),
        }
        all_issues.extend(check_results.get("issues", []))

    overall_pass = all(c.get("pass", True) for c in checks.values())

    return {
        "overall_pass": overall_pass,
        "n_issues": len(all_issues),
        "checks": checks,
        "all_issues": all_issues,
    }


# ============================================================
# Issue GeoJSON Generation
# ============================================================

def generate_issues_geojson(
    overlap: Optional[Dict] = None,
    gcp_results: Optional[Dict] = None,
    check_results: Optional[Dict] = None,
    camera_positions: Optional[List[Dict]] = None,
) -> Dict:
    """
    Generate GeoJSON FeatureCollection of QC issues.

    Returns:
        GeoJSON dict
    """
    features = []

    # Camera position issues (low overlap)
    if camera_positions and overlap and not overlap.get("pass", True):
        for i, cam in enumerate(camera_positions):
            if i < len(camera_positions) - 1:
                next_cam = camera_positions[i + 1]
                # Check if this pair has low overlap
                fp1 = compute_footprint_bounds(
                    cam["x"], cam["y"], cam["altitude"],
                    cam.get("sensor_width_mm", 13.2),
                    cam.get("sensor_height_mm", 8.8),
                    cam.get("focal_length_mm", 8.8),
                    cam.get("gsd_cm", 2.0)
                )
                fp2 = compute_footprint_bounds(
                    next_cam["x"], next_cam["y"], next_cam["altitude"],
                    next_cam.get("sensor_width_mm", 13.2),
                    next_cam.get("sensor_height_mm", 8.8),
                    next_cam.get("focal_length_mm", 8.8),
                    next_cam.get("gsd_cm", 2.0)
                )
                poly1 = create_polygon(fp1[0], fp1[1], fp1[2]-fp1[0], fp1[3]-fp1[1])
                poly2 = create_polygon(fp2[0], fp2[1], fp2[2]-fp2[0], fp2[3]-fp2[1])
                ov = compute_overlap(poly1, poly2)

                if ov < 0.70:
                    features.append({
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [cam["x"], cam["y"]],
                        },
                        "properties": {
                            "issue_type": "low_overlap",
                            "overlap_ratio": round(ov, 4),
                            "image_index": i,
                            "description": f"Low forward overlap: {ov:.1%}",
                        },
                    })

    # GCP outlier points
    if gcp_results and gcp_results.get("outliers"):
        for pr in gcp_results.get("point_results", []):
            if pr["id"] in gcp_results["outliers"]:
                features.append({
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [0.0, 0.0],  # Would need actual coords
                    },
                    "properties": {
                        "issue_type": "gcp_outlier",
                        "point_id": pr["id"],
                        "residual_3d": pr["residual_3d"],
                        "description": f"GCP outlier: {pr['id']} (residual={pr['residual_3d']}m)",
                    },
                })

    # Check point outliers
    if check_results and check_results.get("outliers"):
        for pr in check_results.get("point_results", []):
            if pr["id"] in check_results["outliers"]:
                features.append({
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [0.0, 0.0],
                    },
                    "properties": {
                        "issue_type": "check_point_outlier",
                        "point_id": pr["id"],
                        "residual_3d": pr["residual_3d"],
                        "description": f"Check point outlier: {pr['id']} (residual={pr['residual_3d']}m)",
                    },
                })

    return {
        "type": "FeatureCollection",
        "features": features,
    }


# ============================================================
# Report Generation
# ============================================================

def generate_qc_report_html(results: Dict, output_dir: Path) -> Path:
    """
    Generate HTML QC report.

    Args:
        results: Full QC results dict
        output_dir: Output directory

    Returns:
        Path to generated HTML file
    """
    path = output_dir / "qc_report.html"

    # Extract values safely for template formatting
    overall_pass = results.get("overall_pass", False)
    n_issues = results.get("n_issues", 0)

    overlap = results.get("overlap", {})
    fwd_overlap = overlap.get("forward_overlap_mean", "N/A")
    side_overlap = overlap.get("side_overlap_mean", "N/A")
    n_images = overlap.get("n_images", "N/A")

    gsd_info = results.get("gsd", {})
    gsd_mean = gsd_info.get("gsd_mean_cm", "N/A")

    ortho = results.get("orthomosaic", {})
    nd_frac = ortho.get("nodata_fraction", "N/A")
    if isinstance(nd_frac, (int, float)):
        nd_frac_str = f"{nd_frac:.2%}"
    else:
        nd_frac_str = str(nd_frac)

    dsm = results.get("dsm", {})
    dsm_nd = dsm.get("nodata_fraction", "N/A")
    if isinstance(dsm_nd, (int, float)):
        dsm_nd_str = f"{dsm_nd:.2%}"
    else:
        dsm_nd_str = str(dsm_nd)

    gcp = results.get("gcp", {})
    gcp_rmse = gcp.get("rmse_xy", "N/A")
    gcp_n = gcp.get("n_points", "N/A")

    check = results.get("check_points", {})
    check_rmse = check.get("rmse_xy", "N/A")
    check_n = check.get("n_points", "N/A")

    status_text = "PASS" if overall_pass else "FAIL"
    status_color = "#28a745" if overall_pass else "#dc3545"

    # Format overlap values
    if isinstance(fwd_overlap, (int, float)):
        fwd_str = f"{fwd_overlap:.1%}"
    else:
        fwd_str = str(fwd_overlap)
    if isinstance(side_overlap, (int, float)):
        side_str = f"{side_overlap:.1%}"
    else:
        side_str = str(side_overlap)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>无人机航测质量检查报告</title>
<style>
body {{ font-family: 'Microsoft YaHei', Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
.container {{ max-width: 900px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
h1 {{ color: #333; border-bottom: 3px solid #007bff; padding-bottom: 10px; }}
h2 {{ color: #555; margin-top: 30px; }}
.status {{ font-size: 24px; font-weight: bold; color: {status_color}; padding: 10px 20px; display: inline-block; border-radius: 4px; background: {"#d4edda" if overall_pass else "#f8d7da"}; }}
table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
th, td {{ padding: 10px 15px; text-align: left; border-bottom: 1px solid #ddd; }}
th {{ background: #f8f9fa; font-weight: 600; }}
.pass {{ color: #28a745; }}
.fail {{ color: #dc3545; }}
.metric {{ font-weight: bold; }}
</style>
</head>
<body>
<div class="container">
<h1>无人机航测质量检查报告</h1>
<p>生成时间: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}</p>
<div class="status">{status_text} — {n_issues} 个问题</div>

<h2>1. 影像覆盖</h2>
<table>
<tr><th>指标</th><th>值</th><th>状态</th></tr>
<tr><td class="metric">影像数量</td><td>{n_images}</td><td>-</td></tr>
<tr><td class="metric">航向重叠 (均值)</td><td>{fwd_str}</td><td class="{'pass' if isinstance(fwd_overlap, (int, float)) and fwd_overlap >= 0.7 else 'fail'}">{'✓' if isinstance(fwd_overlap, (int, float)) and fwd_overlap >= 0.7 else '✗'}</td></tr>
<tr><td class="metric">旁向重叠 (均值)</td><td>{side_str}</td><td class="{'pass' if isinstance(side_overlap, (int, float)) and side_overlap >= 0.6 else 'fail'}">{'✓' if isinstance(side_overlap, (int, float)) and side_overlap >= 0.6 else '✗'}</td></tr>
</table>

<h2>2. GSD</h2>
<table>
<tr><th>指标</th><th>值</th><th>状态</th></tr>
<tr><td class="metric">GSD 均值</td><td>{gsd_mean} cm/px</td><td class="{'pass' if isinstance(gsd_mean, (int, float)) and gsd_mean <= 5.0 else 'fail'}">{'✓' if isinstance(gsd_mean, (int, float)) and gsd_mean <= 5.0 else '✗'}</td></tr>
</table>

<h2>3. 正射影像</h2>
<table>
<tr><th>指标</th><th>值</th></tr>
<tr><td class="metric">空洞比例</td><td>{nd_frac_str}</td></tr>
<tr><td class="metric">纹理均值</td><td>{ortho.get('texture_mean', 'N/A')}</td></tr>
<tr><td class="metric">边缘密度</td><td>{ortho.get('edge_density', 'N/A')}</td></tr>
</table>

<h2>4. DSM</h2>
<table>
<tr><th>指标</th><th>值</th></tr>
<tr><td class="metric">空洞比例</td><td>{dsm_nd_str}</td></tr>
<tr><td class="metric">高程范围</td><td>{dsm.get('z_min', 'N/A')} ~ {dsm.get('z_max', 'N/A')} m</td></tr>
</table>

<h2>5. 控制点</h2>
<table>
<tr><th>指标</th><th>值</th></tr>
<tr><td class="metric">GCP 数量</td><td>{gcp_n}</td></tr>
<tr><td class="metric">GCP RMSE_XY</td><td>{gcp_rmse} m</td></tr>
<tr><td class="metric">检查点数量</td><td>{check_n}</td></tr>
<tr><td class="metric">检查点 RMSE_XY</td><td>{check_rmse} m</td></tr>
</table>

<h2>6. 问题清单</h2>
<table>
<tr><th>#</th><th>问题描述</th></tr>
"""

    for i, issue in enumerate(results.get("all_issues", []), 1):
        html += f"<tr><td>{i}</td><td>{issue}</td></tr>\n"

    if not results.get("all_issues"):
        html += "<tr><td colspan='2'>无问题</td></tr>\n"

    html += """
</table>
</div>
</body>
</html>
"""

    path.write_text(html, encoding="utf-8")
    return path


# ============================================================
# CSV Writers
# ============================================================

def write_image_quality_csv(image_qualities: List[Dict], output_dir: Path) -> Path:
    """Write per-image quality metrics to CSV."""
    path = output_dir / "image_quality.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "image_index", "blur_variance", "mean_brightness",
            "overexposed_fraction", "underexposed_fraction", "std_brightness"
        ])
        for i, q in enumerate(image_qualities):
            writer.writerow([
                i,
                q.get("blur_variance", ""),
                q.get("mean_brightness", ""),
                q.get("overexposed_fraction", ""),
                q.get("underexposed_fraction", ""),
                q.get("std_brightness", ""),
            ])
    return path


def write_control_point_residuals(gcp_results: Optional[Dict],
                                  check_results: Optional[Dict],
                                  output_dir: Path) -> Path:
    """Write control point residuals to CSV."""
    path = output_dir / "control_point_residuals.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "point_type", "point_id", "residual_xy", "residual_z",
            "residual_3d", "dx", "dy", "dz"
        ])
        for point_type, results in [("gcp", gcp_results), ("check", check_results)]:
            if results and "point_results" in results:
                for pr in results["point_results"]:
                    writer.writerow([
                        point_type,
                        pr.get("id", ""),
                        pr.get("residual_xy", ""),
                        pr.get("residual_z", ""),
                        pr.get("residual_3d", ""),
                        pr.get("dx", ""),
                        pr.get("dy", ""),
                        pr.get("dz", ""),
                    ])
    return path


# ============================================================
# File-based Data Loaders
# ============================================================

def load_camera_positions_csv(path: Path) -> List[Dict[str, Any]]:
    """Load camera positions from a CSV file.

    Required columns: x, y, altitude
    Optional columns: sensor_width_mm, sensor_height_mm, focal_length_mm,
                      image_width_px, image_height_px, gsd_cm
    """
    positions: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            try:
                cam = {
                    "x": float(row["x"]),
                    "y": float(row["y"]),
                    "altitude": float(row["altitude"]),
                }
            except (KeyError, ValueError) as e:
                raise ValueError(
                    f"Invalid camera-positions CSV at {path}: missing/invalid "
                    f"required field (x, y, altitude): {e}"
                ) from e
            for opt in ("sensor_width_mm", "sensor_height_mm", "focal_length_mm",
                        "image_width_px", "image_height_px", "gsd_cm"):
                if opt in row and row[opt] not in (None, ""):
                    try:
                        cam[opt] = float(row[opt])
                    except ValueError:
                        pass
            positions.append(cam)
    return positions


def load_camera_positions_json(path: Path) -> List[Dict[str, Any]]:
    """Load camera positions from a JSON file.

    Expected format: list of objects, or {"positions": [...]}, each item with
    keys x, y, altitude (float) and optional camera/sensor fields.
    """
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if isinstance(data, dict):
        if "positions" in data and isinstance(data["positions"], list):
            positions_raw = data["positions"]
        elif "camera_positions" in data and isinstance(data["camera_positions"], list):
            positions_raw = data["camera_positions"]
        else:
            raise ValueError(
                f"Camera-positions JSON at {path} must be a list or contain "
                f"'positions' / 'camera_positions' key"
            )
    elif isinstance(data, list):
        positions_raw = data
    else:
        raise ValueError(f"Camera-positions JSON at {path} has unexpected type {type(data)}")

    positions: List[Dict[str, Any]] = []
    for i, cam in enumerate(positions_raw):
        if not isinstance(cam, dict):
            raise ValueError(f"Camera-positions JSON item #{i} is not an object")
        try:
            entry = {
                "x": float(cam["x"]),
                "y": float(cam["y"]),
                "altitude": float(cam["altitude"]),
            }
        except (KeyError, ValueError) as e:
            raise ValueError(
                f"Camera-positions JSON item #{i} missing/invalid x/y/altitude: {e}"
            ) from e
        for opt in ("sensor_width_mm", "sensor_height_mm", "focal_length_mm",
                    "image_width_px", "image_height_px", "gsd_cm"):
            if opt in cam and cam[opt] is not None:
                try:
                    entry[opt] = float(cam[opt])
                except (TypeError, ValueError):
                    pass
        positions.append(entry)
    return positions


def load_camera_positions(path: Path) -> List[Dict[str, Any]]:
    """Load camera positions from CSV or JSON based on file extension."""
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return load_camera_positions_csv(path)
    if suffix in (".json", ".geojson"):
        return load_camera_positions_json(path)
    # Try JSON first, fall back to CSV
    try:
        return load_camera_positions_json(path)
    except (ValueError, json.JSONDecodeError):
        return load_camera_positions_csv(path)


def load_control_points_csv(path: Path) -> List[Dict[str, Any]]:
    """Load control / check points from a CSV file.

    Required columns: x, y, x_ref, y_ref
    Optional columns: id, z, z_ref
    """
    points: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            try:
                pt = {
                    "id": str(row.get("id", row.get("point_id", ""))),
                    "x": float(row["x"]),
                    "y": float(row["y"]),
                    "x_ref": float(row["x_ref"]),
                    "y_ref": float(row["y_ref"]),
                }
            except (KeyError, ValueError) as e:
                raise ValueError(
                    f"Invalid control-points CSV at {path}: missing/invalid "
                    f"required field (x, y, x_ref, y_ref): {e}"
                ) from e
            for opt in ("z", "z_ref"):
                if opt in row and row[opt] not in (None, ""):
                    try:
                        pt[opt] = float(row[opt])
                    except ValueError:
                        pass
            points.append(pt)
    return points


def load_control_points_json(path: Path) -> List[Dict[str, Any]]:
    """Load control / check points from a JSON file."""
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if isinstance(data, dict):
        if "points" in data and isinstance(data["points"], list):
            raw_points = data["points"]
        elif "control_points" in data and isinstance(data["control_points"], list):
            raw_points = data["control_points"]
        else:
            raise ValueError(
                f"Control-points JSON at {path} must be a list or contain "
                f"'points' / 'control_points' key"
            )
    elif isinstance(data, list):
        raw_points = data
    else:
        raise ValueError(f"Control-points JSON at {path} has unexpected type {type(data)}")

    points: List[Dict[str, Any]] = []
    for i, pt in enumerate(raw_points):
        if not isinstance(pt, dict):
            raise ValueError(f"Control-points JSON item #{i} is not an object")
        try:
            entry = {
                "id": str(pt.get("id", pt.get("point_id", ""))),
                "x": float(pt["x"]),
                "y": float(pt["y"]),
                "x_ref": float(pt["x_ref"]),
                "y_ref": float(pt["y_ref"]),
            }
        except (KeyError, ValueError) as e:
            raise ValueError(
                f"Control-points JSON item #{i} missing/invalid x/y/x_ref/y_ref: {e}"
            ) from e
        for opt in ("z", "z_ref"):
            if opt in pt and pt[opt] is not None:
                try:
                    entry[opt] = float(pt[opt])
                except (TypeError, ValueError):
                    pass
        points.append(entry)
    return points


def load_control_points(path: Path) -> List[Dict[str, Any]]:
    """Load control / check points from CSV or JSON based on file extension."""
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return load_control_points_csv(path)
    if suffix in (".json", ".geojson"):
        return load_control_points_json(path)
    try:
        return load_control_points_json(path)
    except (ValueError, json.JSONDecodeError):
        return load_control_points_csv(path)


def load_orthomosaic(path: Path) -> np.ndarray:
    """Load orthomosaic GeoTIFF into a numpy array.

    Returns:
        (H, W) for single-band, or (H, W, C) for multi-band (RGB/RGBA).
    """
    if not _HAS_RASTERIO:
        raise RuntimeError(
            "rasterio is required to load orthomosaic GeoTIFFs but is not "
            "installed. Install with: pip install rasterio"
        )
    with rasterio.open(str(path)) as src:
        arr = src.read()  # (C, H, W)
        if arr.shape[0] >= 3:
            # RGB or RGBA: take first 3 bands, transpose to (H, W, C)
            return np.transpose(arr[:3], (1, 2, 0))
        if arr.shape[0] == 1:
            return arr[0]
        return arr[0]


def load_dsm(path: Path) -> np.ndarray:
    """Load DSM/DEM GeoTIFF into a 2D numpy array (H, W)."""
    if not _HAS_RASTERIO:
        raise RuntimeError(
            "rasterio is required to load DSM/DEM GeoTIFFs but is not "
            "installed. Install with: pip install rasterio"
        )
    with rasterio.open(str(path)) as src:
        return src.read(1)


# ============================================================
# Synthetic Data Generation
# ============================================================

def generate_synthetic_camera_positions(n_images: int = 20,
                                        strip_spacing: float = 50.0,
                                        image_spacing: float = 30.0,
                                        altitude: float = 100.0,
                                        seed: int = 42) -> List[Dict]:
    """
    Generate synthetic camera positions for testing.

    Creates a simple strip pattern with configurable overlap.
    """
    rng = np.random.RandomState(seed)
    positions = []

    n_strips = max(1, int(np.sqrt(n_images)))
    n_per_strip = max(1, n_images // n_strips)

    idx = 0
    for strip in range(n_strips):
        for i in range(n_per_strip):
            if idx >= n_images:
                break
            x = i * image_spacing + rng.normal(0, 1.0)
            y = strip * strip_spacing + rng.normal(0, 1.0)
            positions.append({
                "x": float(x),
                "y": float(y),
                "altitude": altitude + float(rng.normal(0, 2.0)),
                "sensor_width_mm": 13.2,
                "sensor_height_mm": 8.8,
                "focal_length_mm": 8.8,
                "image_width_px": 4000,
                "image_height_px": 3000,
                "gsd_cm": 2.0,
            })
            idx += 1

    return positions[:n_images]


def generate_synthetic_control_points(n_gcp: int = 5, n_check: int = 3,
                                      max_error: float = 0.03,
                                      seed: int = 42) -> Tuple[List[Dict], List[Dict]]:
    """
    Generate synthetic control and check points with known residuals.

    Returns:
        (gcp_points, check_points)
    """
    rng = np.random.RandomState(seed)

    gcps = []
    for i in range(n_gcp):
        x_ref = float(rng.uniform(0, 500))
        y_ref = float(rng.uniform(0, 500))
        z_ref = float(rng.uniform(50, 150))
        gcps.append({
            "id": f"GCP{i+1:02d}",
            "x": x_ref + float(rng.normal(0, max_error)),
            "y": y_ref + float(rng.normal(0, max_error)),
            "z": z_ref + float(rng.normal(0, max_error * 1.5)),
            "x_ref": x_ref,
            "y_ref": y_ref,
            "z_ref": z_ref,
        })

    checks = []
    for i in range(n_check):
        x_ref = float(rng.uniform(0, 500))
        y_ref = float(rng.uniform(0, 500))
        z_ref = float(rng.uniform(50, 150))
        checks.append({
            "id": f"CHK{i+1:02d}",
            "x": x_ref + float(rng.normal(0, max_error)),
            "y": y_ref + float(rng.normal(0, max_error)),
            "z": z_ref + float(rng.normal(0, max_error * 1.5)),
            "x_ref": x_ref,
            "y_ref": y_ref,
            "z_ref": z_ref,
        })

    return gcps, checks


def generate_synthetic_orthomosaic(n_rows: int = 100, n_cols: int = 100,
                                   n_bands: int = 3, nodata_fraction: float = 0.0,
                                   seed: int = 42) -> np.ndarray:
    """Generate synthetic orthomosaic raster."""
    rng = np.random.RandomState(seed)
    raster = rng.randint(50, 200, size=(n_rows, n_cols, n_bands), dtype=np.uint8)

    if nodata_fraction > 0:
        n_nodata = int(n_rows * n_cols * nodata_fraction)
        flat = raster.reshape(-1, n_bands)
        indices = rng.choice(flat.shape[0], size=n_nodata, replace=False)
        flat[indices] = 0
        raster = flat.reshape(n_rows, n_cols, n_bands)

    return raster


def generate_synthetic_dsm(n_rows: int = 100, n_cols: int = 100,
                          z_min: float = 50.0, z_max: float = 150.0,
                          nodata_fraction: float = 0.0,
                          seed: int = 42) -> np.ndarray:
    """Generate synthetic DSM raster."""
    rng = np.random.RandomState(seed)
    dsm = rng.uniform(z_min, z_max, size=(n_rows, n_cols)).astype(np.float32)

    if nodata_fraction > 0:
        n_nodata = int(n_rows * n_cols * nodata_fraction)
        flat = dsm.flatten()
        indices = rng.choice(flat.shape[0], size=n_nodata, replace=False)
        flat[indices] = -9999.0
        dsm = flat.reshape(n_rows, n_cols)

    return dsm


def generate_synthetic_image(size: Tuple[int, int] = (100, 100),
                             blur: bool = False,
                             brightness: float = 128.0,
                             seed: int = 42) -> np.ndarray:
    """Generate synthetic grayscale image for quality testing."""
    rng = np.random.RandomState(seed)
    if blur:
        # Smooth image (low variance = blurry)
        base = rng.normal(brightness, 5.0, size=size).astype(np.float64)
        # Simple box blur
        kernel_size = 5
        from numpy.lib.stride_tricks import sliding_window_view
        # Manual averaging
        h, w = size
        blurred = np.zeros_like(base)
        half = kernel_size // 2
        for di in range(-half, half + 1):
            for dj in range(-half, half + 1):
                shifted = np.roll(np.roll(base, di, axis=0), dj, axis=1)
                blurred += shifted
        blurred /= kernel_size ** 2
        return np.clip(blurred, 0, 255).astype(np.uint8)
    else:
        # Sharp image with edges
        img = rng.normal(brightness, 30.0, size=size)
        # Add some sharp features
        img[size[0]//4:3*size[0]//4, size[1]//4:3*size[1]//4] += 50
        return np.clip(img, 0, 255).astype(np.uint8)


# ============================================================
# Main Pipeline
# ============================================================

def auto_download_orthomosaic(args, output_dir: Path) -> Dict[str, Any]:
    """Download one sentinel-2-l2a scene from MPC using --bbox + --date-range.

    Returns metadata dict (also writes the path back to args.orthomosaic).
    """
    if not _FETCHER_AVAILABLE:
        raise RuntimeError(
            "Shared data fetcher not importable. Pass --orthomosaic <local.tif> instead, "
            "or ensure _geoskill_data_fetcher is on sys.path."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_orthomosaic requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        raise RuntimeError("auto_download_orthomosaic requires --date-range")
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
    args.orthomosaic = str(paths[0])
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "sentinel-2-l2a",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def run_qc_pipeline(args: argparse.Namespace) -> int:
    """Main QC workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("dsq-output")

    # --- Auto-download mode: fetch sentinel-2-l2a from MPC ---
    if (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)) and getattr(args, "date_range", None):
        if not getattr(args, "orthomosaic", None):
            try:
                fetch_meta = auto_download_orthomosaic(args, output_dir)
                mode = "auto_download"
                print(f"  Auto-downloaded orthomosaic: {args.orthomosaic}")
            except DataFetcherError as e:
                print(f"ERROR: auto-download failed: [{e.kind}] {e.message}", file=sys.stderr)
                return EXIT_PROCESSING if 'EXIT_PROCESSING' in dir() else 7
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logging(output_dir)
    logger.info("Drone Survey QC - Starting")

    # Load standards
    standards_path = getattr(args, 'standard_config', None)
    try:
        standards = load_qc_standards(standards_path)
        logger.info(f"QC standards loaded: version {standards.get('version', 'unknown')}")
    except Exception as e:
        logger.error(f"Failed to load QC standards: {e}")
        return EXIT_VALIDATION

    # --- Synthetic/demo mode or file-based mode ---
    # File-based mode is triggered when ANY of the file-bearing flags
    # (--project-dir / --orthomosaic / --dsm / --camera-positions / --control-points)
    # is supplied. Otherwise we run in pure synthetic demo mode.
    _file_flags = (
        "project_dir", "orthomosaic", "dsm",
        "camera_positions", "control_points",
    )
    use_synthetic = not any(
        getattr(args, f, None) for f in _file_flags
    )

    image_qualities = []
    camera_positions = None
    overlap_results = None
    gsd_results = None
    ortho_qa = None
    dsm_qa = None
    gcp_results = None
    check_results = None

    if use_synthetic:
        logger.info("Running in synthetic demo mode")

        # Generate synthetic data
        camera_positions = generate_synthetic_camera_positions(n_images=20, seed=42)
        gcps, checks = generate_synthetic_control_points(n_gcp=5, n_check=3, seed=42)
        ortho = generate_synthetic_orthomosaic(100, 100, 3, nodata_fraction=0.01, seed=42)
        dsm = generate_synthetic_dsm(100, 100, nodata_fraction=0.02, seed=42)

        # Analyze
        overlap_results = analyze_overlap(camera_positions, standards)
        gsd_results = analyze_gsd(camera_positions, standards)
        ortho_qa = analyze_orthomosaic(ortho, nodata_value=0, has_rgb=True)
        dsm_qa = analyze_dsm_quality(dsm, nodata_value=-9999.0)
        gcp_results = analyze_control_points(gcps, standards, "gcp")
        check_results = analyze_control_points(checks, standards, "check")

        # Generate synthetic image qualities
        for i in range(5):
            img = generate_synthetic_image(seed=i)
            q = compute_image_quality(img)
            image_qualities.append(q)

    else:
        # File-based mode
        logger.info(f"Project directory: {args.project_dir}")
        # Load user-supplied files. Each flag is optional but at least one
        # file-bearing flag should be present in file mode; if only some are
        # given, fill the rest with small synthetic subsets so the pipeline
        # can still run end-to-end (logged as a warning).

        provided = {
            "orthomosaic": getattr(args, "orthomosaic", None),
            "dsm": getattr(args, "dsm", None),
            "camera_positions": getattr(args, "camera_positions", None),
            "control_points": getattr(args, "control_points", None),
        }
        provided = {k: v for k, v in provided.items() if v}
        if not provided:
            logger.error(
                "File-based mode requires at least one of --orthomosaic / --dsm / "
                "--camera-positions / --control-points"
            )
            cleanup_logging()
            return EXIT_ARG
        logger.info(f"Loading user-supplied files: {sorted(provided.keys())}")

        # Camera positions
        if provided.get("camera_positions"):
            cp_path = Path(args.camera_positions)
            try:
                camera_positions = load_camera_positions(cp_path)
                logger.info(
                    f"Loaded {len(camera_positions)} camera positions from {cp_path}"
                )
            except Exception as e:
                logger.error(f"Failed to load camera positions: {e}")
                cleanup_logging()
                return EXIT_VALIDATION
        else:
            logger.warning("No --camera-positions given; filling with a small synthetic sample for overlap/GSD analysis")
            camera_positions = generate_synthetic_camera_positions(n_images=10, seed=42)

        # Overlap / GSD analyses need camera positions
        overlap_results = analyze_overlap(camera_positions, standards)
        gsd_results = analyze_gsd(camera_positions, standards)

        # Orthomosaic
        if provided.get("orthomosaic"):
            ortho_path = Path(args.orthomosaic)
            try:
                ortho = load_orthomosaic(ortho_path)
                has_rgb = (ortho.ndim == 3 and ortho.shape[2] >= 3)
                ortho_qa = analyze_orthomosaic(ortho, nodata_value=0, has_rgb=has_rgb)
                logger.info(
                    f"Loaded orthomosaic {ortho.shape} from {ortho_path}"
                )
            except Exception as e:
                logger.error(f"Failed to load orthomosaic: {e}")
                cleanup_logging()
                return EXIT_VALIDATION
        else:
            logger.warning("No --orthomosaic given, skipping orthomosaic QA")
            ortho_qa = None

        # DSM
        if provided.get("dsm"):
            dsm_path = Path(args.dsm)
            try:
                dsm = load_dsm(dsm_path)
                dsm_qa = analyze_dsm_quality(dsm, nodata_value=-9999.0)
                logger.info(f"Loaded DSM {dsm.shape} from {dsm_path}")
            except Exception as e:
                logger.error(f"Failed to load DSM: {e}")
                cleanup_logging()
                return EXIT_VALIDATION
        else:
            logger.warning("No --dsm given, skipping DSM QA")
            dsm_qa = None

        # Control points
        if provided.get("control_points"):
            cp_path = Path(args.control_points)
            try:
                all_points = load_control_points(cp_path)
                # Split into GCP and check points by 'type' field if present,
                # else treat all as GCPs.
                gcps = [p for p in all_points if p.get("type", "gcp") != "check"]
                checks = [p for p in all_points if p.get("type") == "check"]
                if not checks and len(gcps) >= 3:
                    # Use last ~30% as check points if not labeled
                    n_check = max(1, len(gcps) // 3)
                    checks = gcps[-n_check:]
                    gcps = gcps[:-n_check]
                gcp_results = analyze_control_points(gcps, standards, "gcp")
                check_results = analyze_control_points(checks, standards, "check")
                logger.info(
                    f"Loaded {len(all_points)} control points "
                    f"({len(gcps)} gcp, {len(checks)} check) from {cp_path}"
                )
            except Exception as e:
                logger.error(f"Failed to load control points: {e}")
                cleanup_logging()
                return EXIT_VALIDATION
        else:
            logger.warning("No --control-points given, skipping GCP QA")
            gcp_results = None
            check_results = None

        # In file mode, no synthetic image qualities by default
        # (user can supply raw images via --project-dir in a future iteration)

    # --- Rule evaluation ---
    rule_results = evaluate_qc_rules(
        image_quality=image_qualities[0] if image_qualities else None,
        overlap=overlap_results,
        gsd=gsd_results,
        ortho_qa=ortho_qa,
        dsm_qa=dsm_qa,
        gcp_results=gcp_results,
        check_results=check_results,
        standards=standards,
    )

    # --- Generate outputs ---

    # qc.json
    qc_data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "standards_version": standards.get("version", "unknown"),
        "overall_pass": rule_results["overall_pass"],
        "n_issues": rule_results["n_issues"],
        "checks": rule_results["checks"],
        "all_issues": rule_results["all_issues"],
        "overlap": overlap_results,
        "gsd": gsd_results,
        "orthomosaic": ortho_qa,
        "dsm": dsm_qa,
        "gcp": gcp_results,
        "check_points": check_results,
    }
    qc_path = output_dir / "qc.json"
    qc_path.write_text(
        json.dumps(qc_data, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # issues.geojson
    issues_geojson = generate_issues_geojson(
        overlap=overlap_results,
        gcp_results=gcp_results,
        check_results=check_results,
        camera_positions=camera_positions,
    )
    issues_path = output_dir / "issues.geojson"
    issues_path.write_text(
        json.dumps(issues_geojson, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # image_quality.csv
    if image_qualities:
        iq_path = write_image_quality_csv(image_qualities, output_dir)
    else:
        iq_path = output_dir / "image_quality.csv"
        iq_path.write_text("image_index,blur_variance,mean_brightness\n", encoding="utf-8")

    # control_point_residuals.csv
    cp_path = write_control_point_residuals(gcp_results, check_results, output_dir)

    # qc_report.html
    report_path = generate_qc_report_html(rule_results, output_dir)

    # request.json
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "synthetic" if use_synthetic else "file",
        "project_dir": getattr(args, 'project_dir', None),
        "standards_version": standards.get("version", "unknown"),
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
        "n_images": len(camera_positions) if camera_positions else 0,
        "n_gcp": gcp_results.get("n_points", 0) if gcp_results else 0,
        "n_check": check_results.get("n_points", 0) if check_results else 0,
        "has_orthomosaic": ortho_qa is not None,
        "has_dsm": dsm_qa is not None,
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # output-manifest.json
    output_files = {
        "qc.json": str(qc_path),
        "issues.geojson": str(issues_path),
        "image_quality.csv": str(iq_path),
        "control_point_residuals.csv": str(cp_path),
        "qc_report.html": str(report_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(dataset_path),
    }
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "output_files": output_files,
        "qc_summary": {
            "overall_pass": rule_results["overall_pass"],
            "n_issues": rule_results["n_issues"],
        },
    }
    manifest_path = output_dir / "output-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # qa.json
    qa = {
        "status": "complete",
        "checks": {
            "qc_generated": qc_path.exists(),
            "issues_generated": issues_path.exists(),
            "report_generated": report_path.exists(),
            "all_outputs_written": all(Path(p).exists() for p in output_files.values()),
        },
        "n_issues": rule_results["n_issues"],
        "overall_pass": rule_results["overall_pass"],
    }
    qa_path = output_dir / "qa.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    logger.info(f"QC complete: {'PASS' if rule_results['overall_pass'] else 'FAIL'}, "
                f"{rule_results['n_issues']} issues")
    cleanup_logging()
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Drone Survey QC")
    parser.add_argument("--project-dir", default=None,
                        help="Project directory to analyze")
    parser.add_argument("--orthomosaic", default=None,
                        help="Path to orthomosaic GeoTIFF")
    parser.add_argument("--dsm", default=None,
                        help="Path to DSM/DEM GeoTIFF")
    parser.add_argument("--camera-positions", default=None,
                        help="Path to camera positions CSV/JSON")
    parser.add_argument("--control-points", default=None,
                        help="Path to control points CSV/JSON")
    parser.add_argument("--standard-config", default=None,
                        help="Path to QC standards JSON")
    parser.add_argument("--output-dir", "-o", default="dsq-output",
                        help="Output directory (default: dsq-output)")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    add_bbox_date_args(parser)

    args = parser.parse_args()

    rc = validate_args(args)
    if rc != 0:
        sys.exit(rc)

    try:
        sys.exit(run_qc_pipeline(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
