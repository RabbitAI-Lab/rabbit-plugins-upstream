#!/usr/bin/env python3
"""
LiDAR Point Cloud Analysis - Statistics, classification check, DEM/DSM/CHM, profiles and QA.

Reads LAS/LAZ or synthetic point clouds, computes DEM/DSM/CHM rasters,
cross-sections, density maps, and quality reports.

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
    from _geoskill_data_fetcher import (add_bbox_date_args,)
    _FETCHER_AVAILABLE = True
except ImportError:
    import sys as _sys
    from pathlib import Path as _Path
    _skill_dir = _Path(__file__).resolve().parent
    _repo_root = _skill_dir.parent.parent
    _local_fetcher = _repo_root / "_geoskill_data_fetcher"
    if _local_fetcher.exists():
        _sys.path.insert(0, str(_repo_root))
    from _geoskill_data_fetcher import (add_bbox_date_args,)
    _FETCHER_AVAILABLE = True
except ImportError:  # pragma: no cover - graceful when running standalone
    _FETCHER_AVAILABLE = False

EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# ASPRS LAS classification codes
LAS_CLASSIFICATION = {
    0: "Created, Never Classified",
    1: "Unassigned",
    2: "Ground",
    3: "Low Vegetation",
    4: "Medium Vegetation",
    5: "High Vegetation",
    6: "Building",
    7: "Low Point (Noise)",
    8: "Model Key-point (Mass Point)",
    9: "Water",
    10: "Rail",
    11: "Road Surface",
    12: "Overlap/Reserved",
    13: "Wire - Guard",
    14: "Wire - Conductor",
    15: "Transmission Tower",
    16: "Wire-structure Connector",
    17: "Bridge Deck",
    18: "High Noise",
}

# Short labels for classification
CLASS_SHORT_NAMES = {
    0: "NeverClassified",
    1: "Unassigned",
    2: "Ground",
    3: "LowVeg",
    4: "MedVeg",
    5: "HighVeg",
    6: "Building",
    7: "Noise",
    8: "ModelKey",
    9: "Water",
    10: "Rail",
    11: "Road",
    12: "Overlap",
    13: "WireGuard",
    14: "WireCond",
    15: "Tower",
    16: "WireConn",
    17: "Bridge",
    18: "HighNoise",
}

# Default parameters
DEFAULT_RESOLUTION = 1.0  # meter
DEFAULT_GROUND_METHOD = "grid_min"  # grid_min, pmf (simplified)
DEFAULT_TILE_SIZE = 100.0  # meter
DEFAULT_PRODUCTS = "dem,dsm,chm,density,qa"
DEFAULT_PMF_CELL_SIZE = 5.0
DEFAULT_PMF_WINDOW = 3
DEFAULT_PMF_THRESHOLD = 0.5


# ============================================================
# Logging
# ============================================================

def setup_logging(output_dir: Path) -> logging.Logger:
    """Setup logging to file and console."""
    logger = logging.getLogger("lpca")
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
    """Close all handlers on the lpca logger."""
    logger = logging.getLogger("lpca")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)


# ============================================================
# Point Cloud Data Structure
# ============================================================

class PointCloud:
    """Simple point cloud container using numpy arrays."""

    def __init__(self, x: np.ndarray, y: np.ndarray, z: np.ndarray,
                 classification: Optional[np.ndarray] = None,
                 intensity: Optional[np.ndarray] = None,
                 crs: Optional[str] = None):
        self.x = np.asarray(x, dtype=np.float64)
        self.y = np.asarray(y, dtype=np.float64)
        self.z = np.asarray(z, dtype=np.float64)
        n = len(self.x)
        self.classification = np.asarray(classification, dtype=np.uint8) if classification is not None else np.ones(n, dtype=np.uint8)
        self.intensity = np.asarray(intensity, dtype=np.float32) if intensity is not None else np.zeros(n, dtype=np.float32)
        self.crs = crs

    @property
    def n_points(self) -> int:
        return len(self.x)

    @property
    def bounds(self) -> Tuple[float, float, float, float]:
        """Returns (xmin, ymin, xmax, ymax)."""
        return (float(np.min(self.x)), float(np.min(self.y)),
                float(np.max(self.x)), float(np.max(self.y)))

    @property
    def z_range(self) -> Tuple[float, float]:
        return (float(np.min(self.z)), float(np.max(self.z)))

    def filter_by_class(self, classes: List[int]) -> 'PointCloud':
        """Filter points by classification codes."""
        mask = np.isin(self.classification, classes)
        return PointCloud(
            self.x[mask], self.y[mask], self.z[mask],
            self.classification[mask], self.intensity[mask], self.crs
        )

    def filter_by_bounds(self, xmin: float, ymin: float, xmax: float, ymax: float) -> 'PointCloud':
        """Filter points by bounding box."""
        mask = (self.x >= xmin) & (self.x <= xmax) & (self.y >= ymin) & (self.y <= ymax)
        return PointCloud(
            self.x[mask], self.y[mask], self.z[mask],
            self.classification[mask], self.intensity[mask], self.crs
        )

    def copy(self) -> 'PointCloud':
        return PointCloud(
            self.x.copy(), self.y.copy(), self.z.copy(),
            self.classification.copy(), self.intensity.copy(), self.crs
        )


# ============================================================
# Synthetic Point Cloud Generation
# ============================================================

def generate_synthetic_pointcloud(
    n_points: int = 10000,
    bounds: Tuple[float, float, float, float] = (0, 0, 100, 100),
    ground_slope: float = 0.05,
    vegetation_fraction: float = 0.3,
    building_fraction: float = 0.05,
    noise_fraction: float = 0.01,
    seed: int = 42
) -> PointCloud:
    """
    Generate a synthetic point cloud with ground, vegetation, buildings, and noise.

    Args:
        n_points: Total number of points
        bounds: (xmin, ymin, xmax, ymax)
        ground_slope: Slope factor for ground surface
        vegetation_fraction: Fraction of vegetation points
        building_fraction: Fraction of building points
        noise_fraction: Fraction of noise points
        seed: Random seed

    Returns:
        PointCloud with realistic classification
    """
    rng = np.random.RandomState(seed)
    xmin, ymin, xmax, ymax = bounds
    width = xmax - xmin
    height = ymax - ymin

    # Generate random x, y positions
    x = rng.uniform(xmin, xmax, n_points)
    y = rng.uniform(ymin, ymax, n_points)

    # Ground surface: base height + slope
    z_ground = 10.0 + ground_slope * (x - xmin) + 0.02 * rng.randn(n_points)

    # Assign classifications
    classifications = np.ones(n_points, dtype=np.uint8)  # Default: unassigned

    n_remaining = n_points
    indices = np.arange(n_points)
    rng.shuffle(indices)

    # Ground points (class 2)
    n_ground = int(n_points * (1 - vegetation_fraction - building_fraction - noise_fraction))
    ground_idx = indices[:n_ground]
    classifications[ground_idx] = 2

    # Vegetation points (classes 3, 4, 5)
    n_veg = int(n_points * vegetation_fraction)
    veg_idx = indices[n_ground:n_ground + n_veg]
    veg_class_choice = rng.choice([3, 4, 5], size=len(veg_idx))
    classifications[veg_idx] = veg_class_choice
    # Vegetation height above ground
    veg_height = rng.uniform(2.0, 15.0, len(veg_idx))

    # Building points (class 6)
    n_building = int(n_points * building_fraction)
    building_idx = indices[n_ground + n_veg:n_ground + n_veg + n_building]
    classifications[building_idx] = 6
    building_height = rng.uniform(3.0, 20.0, len(building_idx))

    # Noise points (class 7)
    n_noise = int(n_points * noise_fraction)
    noise_idx = indices[n_ground + n_veg + n_building:n_ground + n_veg + n_building + n_noise]
    classifications[noise_idx] = 7

    # Compute z values
    z = z_ground.copy()
    z[veg_idx] = z_ground[veg_idx] + veg_height
    z[building_idx] = z_ground[building_idx] + building_height
    z[noise_idx] = z_ground[noise_idx] + rng.uniform(-5.0, 30.0, len(noise_idx))

    # Intensity
    intensity = 100.0 + 50.0 * rng.randn(n_points)
    intensity = np.clip(intensity, 0, 255).astype(np.float32)

    return PointCloud(x, y, z, classifications, intensity, crs="EPSG:32650")


# ============================================================
# Point Cloud Statistics
# ============================================================

def compute_pointcloud_stats(pc: PointCloud) -> Dict[str, Any]:
    """Compute comprehensive point cloud statistics."""
    bounds = pc.bounds
    z_min, z_max = pc.z_range
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    area = width * height

    # Classification histogram
    class_hist = {}
    unique_classes = np.unique(pc.classification)
    for cls in unique_classes:
        count = int(np.sum(pc.classification == cls))
        class_name = CLASS_SHORT_NAMES.get(int(cls), f"Class_{cls}")
        class_hist[int(cls)] = {
            "name": class_name,
            "description": LAS_CLASSIFICATION.get(int(cls), "Unknown"),
            "count": count,
            "percentage": round(count / pc.n_points * 100, 2)
        }

    # Density
    density = pc.n_points / area if area > 0 else 0.0

    # Intensity stats
    intensity_mean = float(np.mean(pc.intensity))
    intensity_std = float(np.std(pc.intensity))

    stats = {
        "n_points": pc.n_points,
        "bounds": {
            "xmin": round(bounds[0], 4),
            "ymin": round(bounds[1], 4),
            "xmax": round(bounds[2], 4),
            "ymax": round(bounds[3], 4),
        },
        "width_m": round(width, 4),
        "height_m": round(height, 4),
        "area_m2": round(area, 4),
        "z_range": {"min": round(z_min, 4), "max": round(z_max, 4)},
        "density_pts_per_m2": round(density, 4),
        "classification_histogram": class_hist,
        "intensity": {
            "mean": round(intensity_mean, 2),
            "std": round(intensity_std, 2),
            "min": round(float(np.min(pc.intensity)), 2),
            "max": round(float(np.max(pc.intensity)), 2),
        },
        "crs": pc.crs,
    }
    return stats


# ============================================================
# Point Cloud QA
# ============================================================

def run_pointcloud_qa(pc: PointCloud) -> Dict[str, Any]:
    """
    Run quality assurance checks on point cloud.

    Returns dict with QA results, warnings, and problem points.
    """
    warnings = []
    checks = {}

    # Check 1: Has points
    checks["has_points"] = pc.n_points > 0
    if not checks["has_points"]:
        warnings.append("Point cloud is empty")

    # Check 2: Reasonable bounds
    bounds = pc.bounds
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    checks["reasonable_bounds"] = width > 0 and height > 0
    if not checks["reasonable_bounds"]:
        warnings.append("Degenerate bounding box (zero area)")

    # Check 3: Has classification data
    unique_classes = np.unique(pc.classification)
    checks["has_classification"] = len(unique_classes) > 1 or 2 in unique_classes
    if not checks["has_classification"]:
        warnings.append("No ground classification (class 2) found")

    # Check 4: Ground point coverage
    ground_mask = pc.classification == 2
    ground_count = int(np.sum(ground_mask))
    ground_fraction = ground_count / pc.n_points if pc.n_points > 0 else 0
    checks["ground_coverage_ok"] = ground_fraction > 0.1
    if not checks["ground_coverage_ok"]:
        warnings.append(f"Ground coverage low: {ground_fraction:.1%}")

    # Check 5: No extreme Z outliers
    z_min, z_max = pc.z_range
    z_range = z_max - z_min
    checks["z_range_reasonable"] = z_range < 500  # Less than 500m range
    if not checks["z_range_reasonable"]:
        warnings.append(f"Extreme Z range: {z_range:.1f}m")

    # Check 6: Density
    area = width * height
    density = pc.n_points / area if area > 0 else 0
    checks["density_ok"] = density > 0.01
    if not checks["density_ok"]:
        warnings.append(f"Very low density: {density:.4f} pts/m2")

    # Check 7: Noise fraction
    noise_mask = pc.classification == 7
    noise_count = int(np.sum(noise_mask))
    noise_fraction = noise_count / pc.n_points if pc.n_points > 0 else 0
    checks["noise_acceptable"] = noise_fraction < 0.1
    if not checks["noise_acceptable"]:
        warnings.append(f"High noise fraction: {noise_fraction:.1%}")

    # Identify problem points (noise, high Z)
    problem_mask = noise_mask
    problem_indices = np.where(problem_mask)[0]
    problem_points = []
    for idx in problem_indices[:100]:  # Limit to first 100
        problem_points.append({
            "index": int(idx),
            "x": round(float(pc.x[idx]), 3),
            "y": round(float(pc.y[idx]), 3),
            "z": round(float(pc.z[idx]), 3),
            "classification": int(pc.classification[idx]),
        })

    # Tile-based QA (check density variation)
    tile_size = 10.0  # 10m tiles
    n_tiles_x = max(1, int(width / tile_size))
    n_tiles_y = max(1, int(height / tile_size))
    tile_densities = []
    low_density_tiles = []

    for ti in range(n_tiles_x):
        for tj in range(n_tiles_y):
            tx_min = bounds[0] + ti * tile_size
            tx_max = tx_min + tile_size
            ty_min = bounds[1] + tj * tile_size
            ty_max = ty_min + tile_size

            tile_mask = ((pc.x >= tx_min) & (pc.x < tx_max) &
                         (pc.y >= ty_min) & (pc.y < ty_max))
            tile_count = int(np.sum(tile_mask))
            tile_area = tile_size * tile_size
            tile_density = tile_count / tile_area
            tile_densities.append(tile_density)

            if tile_density < 1.0:  # Less than 1 pt/m2
                low_density_tiles.append({
                    "tile_x": ti,
                    "tile_y": tj,
                    "xmin": round(tx_min, 2),
                    "ymin": round(ty_min, 2),
                    "density": round(tile_density, 3),
                })

    density_variation = float(np.std(tile_densities)) if tile_densities else 0.0
    checks["density_uniform"] = density_variation < np.mean(tile_densities) * 0.5 if tile_densities and np.mean(tile_densities) > 0 else False
    if not checks["density_uniform"]:
        warnings.append(f"Non-uniform density (CV={density_variation:.3f})")

    qa = {
        "status": "pass" if all(checks.values()) else "warning",
        "checks": checks,
        "warnings": warnings,
        "n_warnings": len(warnings),
        "problem_points": {
            "count": int(np.sum(problem_mask)),
            "samples": problem_points,
        },
        "tile_qa": {
            "tile_size_m": tile_size,
            "n_tiles": n_tiles_x * n_tiles_y,
            "density_mean": round(float(np.mean(tile_densities)), 4) if tile_densities else 0,
            "density_std": round(density_variation, 4),
            "low_density_tiles": low_density_tiles[:20],  # Limit output
        },
    }

    return qa


# ============================================================
# Ground Classification
# ============================================================

def classify_ground_gridmin(pc: PointCloud, resolution: float = 1.0,
                             window: int = 3) -> np.ndarray:
    """
    Simple grid-based ground classification.

    For each grid cell, the lowest point is considered ground.
    Then expand to nearby low points within a threshold.

    Args:
        pc: Input point cloud
        resolution: Grid cell size in meters
        window: Morphological window size for dilation

    Returns:
        Boolean mask of ground points
    """
    bounds = pc.bounds
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]

    n_cols = max(1, int(np.ceil(width / resolution)))
    n_rows = max(1, int(np.ceil(height / resolution)))

    # Build grid of minimum Z values
    grid_min_z = np.full((n_rows, n_cols), np.inf)
    grid_min_idx = np.full((n_rows, n_cols), -1, dtype=np.int64)

    col_indices = np.clip(((pc.x - bounds[0]) / resolution).astype(int), 0, n_cols - 1)
    row_indices = np.clip(((pc.y - bounds[1]) / resolution).astype(int), 0, n_rows - 1)

    for i in range(pc.n_points):
        r, c = row_indices[i], col_indices[i]
        if pc.z[i] < grid_min_z[r, c]:
            grid_min_z[r, c] = pc.z[i]
            grid_min_idx[r, c] = i

    # Dilate the minimum surface (simple morphological opening)
    from scipy.ndimage import minimum_filter, generic_filter
    # Apply minimum filter to fill gaps and create smooth surface
    dilated_min = minimum_filter(grid_min_z, size=window, mode='constant', cval=np.inf)

    # Points close to the dilated minimum surface are ground
    ground_threshold = 0.5  # meters above local minimum
    ground_mask = np.zeros(pc.n_points, dtype=bool)

    for i in range(pc.n_points):
        r, c = row_indices[i], col_indices[i]
        if r < n_rows and c < n_cols:
            local_ground_z = dilated_min[r, c]
            if local_ground_z < np.inf and pc.z[i] <= local_ground_z + ground_threshold:
                ground_mask[i] = True

    return ground_mask


def classify_ground_simple(pc: PointCloud, resolution: float = 1.0,
                           slope_threshold: float = 0.3) -> np.ndarray:
    """
    Simple ground classification without scipy dependency.

    Uses grid-based lowest point selection with height threshold.

    Args:
        pc: Input point cloud
        resolution: Grid cell size
        slope_threshold: Max height above local minimum for ground

    Returns:
        Boolean mask of ground points
    """
    bounds = pc.bounds
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]

    n_cols = max(1, int(np.ceil(width / resolution)))
    n_rows = max(1, int(np.ceil(height / resolution)))

    # Build grid of minimum Z values
    grid_min_z = np.full((n_rows, n_cols), np.inf)

    col_indices = np.clip(((pc.x - bounds[0]) / resolution).astype(int), 0, n_cols - 1)
    row_indices = np.clip(((pc.y - bounds[1]) / resolution).astype(int), 0, n_rows - 1)

    for i in range(pc.n_points):
        r, c = row_indices[i], col_indices[i]
        if pc.z[i] < grid_min_z[r, c]:
            grid_min_z[r, c] = pc.z[i]

    # Simple gap filling: replace inf with neighbor average
    for _ in range(3):
        mask_inf = np.isinf(grid_min_z)
        if not np.any(mask_inf):
            break
        # Pad and take neighbor mean
        padded = np.pad(grid_min_z, 1, mode='constant', constant_values=np.inf)
        neighbor_sum = np.zeros_like(grid_min_z)
        neighbor_count = np.zeros_like(grid_min_z)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                shifted = padded[1 + dr:1 + dr + n_rows, 1 + dc:1 + dc + n_cols]
                valid = ~np.isinf(shifted)
                neighbor_sum[valid] += shifted[valid]
                neighbor_count[valid] += 1

        fill_mask = mask_inf & (neighbor_count > 0)
        grid_min_z[fill_mask] = neighbor_sum[fill_mask] / neighbor_count[fill_mask]

    # Remaining inf -> global min
    global_min = np.min(grid_min_z[~np.isinf(grid_min_z)]) if np.any(~np.isinf(grid_min_z)) else 0
    grid_min_z[np.isinf(grid_min_z)] = global_min

    # Classify: points close to grid minimum are ground
    ground_threshold = slope_threshold
    ground_z_values = grid_min_z[row_indices, col_indices]
    ground_mask = pc.z <= ground_z_values + ground_threshold

    return ground_mask


# ============================================================
# Rasterization
# ============================================================

def rasterize_dem(pc: PointCloud, resolution: float = 1.0,
                  ground_mask: Optional[np.ndarray] = None) -> Tuple[np.ndarray, dict]:
    """
    Create DEM (Digital Elevation Model) raster from ground points.

    Args:
        pc: Point cloud
        resolution: Grid resolution in meters
        ground_mask: Boolean mask for ground points

    Returns:
        Tuple of (dem_array, raster_info)
    """
    bounds = pc.bounds
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]

    n_cols = max(1, int(np.ceil(width / resolution)))
    n_rows = max(1, int(np.ceil(height / resolution)))

    if ground_mask is not None:
        x = pc.x[ground_mask]
        y = pc.y[ground_mask]
        z = pc.z[ground_mask]
    else:
        x, y, z = pc.x, pc.y, pc.z

    if len(x) == 0:
        dem = np.full((n_rows, n_cols), np.nan)
        transform = {"xmin": bounds[0], "ymin": bounds[1], "resolution": resolution}
        return dem, transform

    dem = np.full((n_rows, n_cols), np.nan, dtype=np.float64)

    col_indices = np.clip(((x - bounds[0]) / resolution).astype(int), 0, n_cols - 1)
    row_indices = np.clip((n_rows - 1 - ((y - bounds[1]) / resolution)).astype(int), 0, n_rows - 1)

    # Minimum Z per cell (DEM = ground surface)
    for i in range(len(x)):
        r, c = row_indices[i], col_indices[i]
        if np.isnan(dem[r, c]) or z[i] < dem[r, c]:
            dem[r, c] = z[i]

    # Fill small gaps using neighbor interpolation
    dem = fill_nan_neighbors(dem)

    transform = {
        "xmin": bounds[0],
        "ymin": bounds[1],
        "xmax": bounds[0] + n_cols * resolution,
        "ymax": bounds[1] + n_rows * resolution,
        "resolution": resolution,
        "n_rows": n_rows,
        "n_cols": n_cols,
    }

    return dem, transform


def rasterize_dsm(pc: PointCloud, resolution: float = 1.0) -> Tuple[np.ndarray, dict]:
    """
    Create DSM (Digital Surface Model) raster from all points.

    Args:
        pc: Point cloud
        resolution: Grid resolution

    Returns:
        Tuple of (dsm_array, raster_info)
    """
    bounds = pc.bounds
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]

    n_cols = max(1, int(np.ceil(width / resolution)))
    n_rows = max(1, int(np.ceil(height / resolution)))

    dsm = np.full((n_rows, n_cols), np.nan, dtype=np.float64)

    col_indices = np.clip(((pc.x - bounds[0]) / resolution).astype(int), 0, n_cols - 1)
    row_indices = np.clip((n_rows - 1 - ((pc.y - bounds[1]) / resolution)).astype(int), 0, n_rows - 1)

    # Maximum Z per cell (DSM = surface including objects)
    for i in range(pc.n_points):
        r, c = row_indices[i], col_indices[i]
        if np.isnan(dsm[r, c]) or pc.z[i] > dsm[r, c]:
            dsm[r, c] = pc.z[i]

    dsm = fill_nan_neighbors(dsm)

    transform = {
        "xmin": bounds[0],
        "ymin": bounds[1],
        "xmax": bounds[0] + n_cols * resolution,
        "ymax": bounds[1] + n_rows * resolution,
        "resolution": resolution,
        "n_rows": n_rows,
        "n_cols": n_cols,
    }

    return dsm, transform


def rasterize_density(pc: PointCloud, resolution: float = 1.0) -> Tuple[np.ndarray, dict]:
    """
    Create point density raster (points per square meter).

    Args:
        pc: Point cloud
        resolution: Grid resolution

    Returns:
        Tuple of (density_array, raster_info)
    """
    bounds = pc.bounds
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]

    n_cols = max(1, int(np.ceil(width / resolution)))
    n_rows = max(1, int(np.ceil(height / resolution)))

    density_grid = np.zeros((n_rows, n_cols), dtype=np.int32)

    col_indices = np.clip(((pc.x - bounds[0]) / resolution).astype(int), 0, n_cols - 1)
    row_indices = np.clip((n_rows - 1 - ((pc.y - bounds[1]) / resolution)).astype(int), 0, n_rows - 1)

    for i in range(pc.n_points):
        r, c = row_indices[i], col_indices[i]
        density_grid[r, c] += 1

    # Convert to points per m²
    cell_area = resolution * resolution
    density = density_grid.astype(np.float64) / cell_area

    transform = {
        "xmin": bounds[0],
        "ymin": bounds[1],
        "xmax": bounds[0] + n_cols * resolution,
        "ymax": bounds[1] + n_rows * resolution,
        "resolution": resolution,
        "n_rows": n_rows,
        "n_cols": n_cols,
    }

    return density, transform


def compute_chm(dem: np.ndarray, dsm: np.ndarray) -> np.ndarray:
    """
    Compute Canopy Height Model (CHM) = DSM - DEM.

    Args:
        dem: DEM raster
        dsm: DSM raster

    Returns:
        CHM raster
    """
    chm = dsm - dem
    # Negative values (noise) set to 0
    chm = np.where(chm < 0, 0.0, chm)
    # Where either is NaN, result is NaN
    chm = np.where(np.isnan(dem) | np.isnan(dsm), np.nan, chm)
    return chm


def fill_nan_neighbors(arr: np.ndarray, max_iterations: int = 5) -> np.ndarray:
    """Fill NaN values using neighbor mean interpolation."""
    filled = arr.copy()
    for _ in range(max_iterations):
        nan_mask = np.isnan(filled)
        if not np.any(nan_mask):
            break
        # Pad with NaN
        padded = np.pad(filled, 1, mode='constant', constant_values=np.nan)
        # Compute neighbor mean
        neighbor_sum = np.zeros_like(filled)
        neighbor_count = np.zeros_like(filled)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                shifted = padded[1 + dr:1 + dr + filled.shape[0],
                                  1 + dc:1 + dc + filled.shape[1]]
                valid = ~np.isnan(shifted)
                neighbor_sum[valid] += shifted[valid]
                neighbor_count[valid] += 1

        fillable = nan_mask & (neighbor_count > 0)
        filled[fillable] = neighbor_sum[fillable] / neighbor_count[fillable]

    return filled


# ============================================================
# Cross-section / Profile
# ============================================================

def extract_cross_section(pc: PointCloud, x1: float, y1: float,
                          x2: float, y2: float, width: float = 1.0,
                          resolution: float = 0.5) -> Dict[str, Any]:
    """
    Extract a cross-section profile along a line.

    Args:
        pc: Point cloud
        x1, y1: Start point
        x2, y2: End point
        width: Swath width (perpendicular to line)
        resolution: Along-profile resolution

    Returns:
        Dict with profile data
    """
    # Line vector
    dx = x2 - x1
    dy = y2 - y1
    line_length = math.sqrt(dx * dx + dy * dy)
    if line_length == 0:
        return {"error": "Zero-length line"}

    # Unit perpendicular vector
    perp_x = -dy / line_length
    perp_y = dx / line_length

    # Project points onto line
    # Distance along line (t) and perpendicular distance (d)
    t = ((pc.x - x1) * dx + (pc.y - y1) * dy) / (line_length * line_length)
    d = ((pc.x - x1) * perp_x + (pc.y - y1) * perp_y)

    # Filter points within swath
    in_swath = (t >= 0) & (t <= 1) & (np.abs(d) <= width / 2)

    if not np.any(in_swath):
        return {
            "line": {"x1": x1, "y1": y1, "x2": x2, "y2": y2},
            "length_m": round(line_length, 3),
            "n_points": 0,
            "profile": [],
        }

    # Bin along profile
    t_swath = t[in_swath]
    z_swath = pc.z[in_swath]
    class_swath = pc.classification[in_swath]

    n_bins = max(1, int(line_length / resolution))
    bin_edges = np.linspace(0, 1, n_bins + 1)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    profile = []
    for i in range(n_bins):
        in_bin = (t_swath >= bin_edges[i]) & (t_swath < bin_edges[i + 1])
        if np.any(in_bin):
            bin_z = z_swath[in_bin]
            bin_class = class_swath[in_bin]
            profile.append({
                "distance_m": round(float(bin_centers[i] * line_length), 3),
                "z_min": round(float(np.min(bin_z)), 3),
                "z_max": round(float(np.max(bin_z)), 3),
                "z_mean": round(float(np.mean(bin_z)), 3),
                "n_points": int(np.sum(in_bin)),
                "dominant_class": int(np.bincount(bin_class).argmax()) if len(bin_class) > 0 else 0,
            })
        else:
            profile.append({
                "distance_m": round(float(bin_centers[i] * line_length), 3),
                "z_min": None,
                "z_max": None,
                "z_mean": None,
                "n_points": 0,
                "dominant_class": None,
            })

    return {
        "line": {"x1": x1, "y1": y1, "x2": x2, "y2": y2},
        "length_m": round(line_length, 3),
        "width_m": width,
        "n_points": int(np.sum(in_swath)),
        "profile": profile,
    }


# ============================================================
# Multi-temporal DEM Difference
# ============================================================

def compute_dem_difference(dem1: np.ndarray, dem2: np.ndarray,
                           transform1: dict, transform2: dict,
                           stable_mask: Optional[np.ndarray] = None) -> Tuple[np.ndarray, Dict]:
    """
    Compute DEM difference (dem2 - dem1) for change detection.

    Args:
        dem1: Earlier DEM
        dem2: Later DEM
        transform1: Transform info for dem1
        transform2: Transform info for dem2
        stable_mask: Boolean mask of stable areas for bias correction

    Returns:
        Tuple of (difference_raster, stats)
    """
    # Ensure same shape
    if dem1.shape != dem2.shape:
        # Resample to common grid (simple nearest neighbor)
        min_rows = min(dem1.shape[0], dem2.shape[0])
        min_cols = min(dem1.shape[1], dem2.shape[1])
        dem1 = dem1[:min_rows, :min_cols]
        dem2 = dem2[:min_rows, :min_cols]

    diff = dem2 - dem1

    # Bias correction using stable areas
    if stable_mask is not None and stable_mask.shape == diff.shape:
        stable_diff = diff[stable_mask & ~np.isnan(diff)]
        if len(stable_diff) > 0:
            bias = float(np.mean(stable_diff))
            diff = diff - bias
        else:
            bias = 0.0
    else:
        # Use overall mean as bias estimate
        valid = diff[~np.isnan(diff)]
        bias = float(np.mean(valid)) if len(valid) > 0 else 0.0

    # Statistics
    valid_diff = diff[~np.isnan(diff)]
    stats = {
        "mean_diff": round(float(np.mean(valid_diff)), 4) if len(valid_diff) > 0 else None,
        "std_diff": round(float(np.std(valid_diff)), 4) if len(valid_diff) > 0 else None,
        "min_diff": round(float(np.min(valid_diff)), 4) if len(valid_diff) > 0 else None,
        "max_diff": round(float(np.max(valid_diff)), 4) if len(valid_diff) > 0 else None,
        "rmse": round(float(np.sqrt(np.mean(valid_diff ** 2))), 4) if len(valid_diff) > 0 else None,
        "n_valid_pixels": int(len(valid_diff)),
        "bias_correction": round(bias, 4),
    }

    return diff, stats


# ============================================================
# Height Statistics
# ============================================================

def compute_height_statistics(pc: PointCloud, dem: Optional[np.ndarray] = None,
                              transform: Optional[dict] = None) -> Dict[str, Any]:
    """
    Compute above-ground height statistics.

    If DEM is provided, heights are relative to ground.
    Otherwise, uses raw Z values.

    Args:
        pc: Point cloud
        dem: DEM raster (optional)
        transform: Raster transform info

    Returns:
        Dict with height statistics
    """
    if dem is not None and transform is not None:
        # Compute normalized heights
        bounds = pc.bounds
        resolution = transform["resolution"]
        n_rows = dem.shape[0]
        n_cols = dem.shape[1]

        col_indices = np.clip(((pc.x - bounds[0]) / resolution).astype(int), 0, n_cols - 1)
        row_indices = np.clip((n_rows - 1 - ((pc.y - bounds[1]) / resolution)).astype(int), 0, n_rows - 1)

        ground_z = dem[row_indices, col_indices]
        valid = ~np.isnan(ground_z)
        heights = pc.z[valid] - ground_z[valid]
        heights = heights[heights > 0]  # Only above-ground
    else:
        heights = pc.z - float(np.min(pc.z))

    if len(heights) == 0:
        return {
            "n_points_above_ground": 0,
            "height_mean": None,
            "height_median": None,
            "height_max": None,
            "height_percentiles": {},
        }

    percentiles = [10, 25, 50, 75, 90, 95, 99]
    pcts = {}
    for p in percentiles:
        pcts[f"p{p}"] = round(float(np.percentile(heights, p)), 3)

    stats = {
        "n_points_above_ground": int(len(heights)),
        "height_mean": round(float(np.mean(heights)), 3),
        "height_median": round(float(np.median(heights)), 3),
        "height_std": round(float(np.std(heights)), 3),
        "height_min": round(float(np.min(heights)), 3),
        "height_max": round(float(np.max(heights)), 3),
        "height_percentiles": pcts,
    }

    return stats


# ============================================================
# Raster Output Writers
# ============================================================

def write_raster_geotiff(path: Path, data: np.ndarray, transform: dict,
                         crs: str = "EPSG:32650", nodata: float = -9999) -> Path:
    """Write a raster to GeoTIFF."""
    try:
        import rasterio
        from rasterio.transform import from_bounds
    except ImportError:
        # Fallback: write as numpy
        np_path = path.with_suffix(".npy")
        np.save(str(np_path), data)
        return np_path

    rows, cols = data.shape
    xmin = transform["xmin"]
    ymin = transform["ymin"]
    res = transform["resolution"]
    xmax = xmin + cols * res
    ymax = ymin + rows * res

    affine = from_bounds(xmin, ymin, xmax, ymax, cols, rows)

    # Replace NaN with nodata
    out_data = data.copy()
    out_data[np.isnan(out_data)] = nodata

    with rasterio.open(
        str(path), "w", driver="GTiff",
        height=rows, width=cols,
        count=1, dtype=out_data.dtype,
        crs=crs, transform=affine,
        nodata=nodata,
    ) as dst:
        dst.write(out_data, 1)

    return path


def write_profile_geojson(path: Path, profile: Dict) -> Path:
    """Write cross-section profile as GeoJSON."""
    features = []

    # Line geometry
    line = profile.get("line", {})
    line_feature = {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [line.get("x1", 0), line.get("y1", 0)],
                [line.get("x2", 0), line.get("y2", 0)],
            ],
        },
        "properties": {
            "name": "cross_section_line",
            "length_m": profile.get("length_m", 0),
        },
    }
    features.append(line_feature)

    # Profile points
    for pt in profile.get("profile", []):
        if pt.get("z_mean") is not None:
            # Interpolate position along line
            frac = pt["distance_m"] / profile["length_m"] if profile.get("length_m", 0) > 0 else 0
            px = line.get("x1", 0) + frac * (line.get("x2", 0) - line.get("x1", 0))
            py = line.get("y1", 0) + frac * (line.get("y2", 0) - line.get("y1", 0))

            pt_feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [round(px, 3), round(py, 3)],
                },
                "properties": {
                    "distance_m": pt["distance_m"],
                    "z_min": pt.get("z_min"),
                    "z_max": pt.get("z_max"),
                    "z_mean": pt.get("z_mean"),
                    "n_points": pt.get("n_points", 0),
                    "dominant_class": pt.get("dominant_class"),
                },
            }
            features.append(pt_feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features,
    }

    path.write_text(json.dumps(geojson, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


# ============================================================
# Main Analysis Pipeline
# ============================================================

def run_analysis(args: argparse.Namespace) -> int:
    """Main analysis workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("lpca-output")
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logging(output_dir)
    logger.info("LiDAR Point Cloud Analysis - Starting")

    # Parse parameters
    resolution = args.resolution if hasattr(args, 'resolution') and args.resolution else DEFAULT_RESOLUTION
    ground_method = args.ground_method if hasattr(args, 'ground_method') and args.ground_method else DEFAULT_GROUND_METHOD
    products = args.products if hasattr(args, 'products') and args.products else DEFAULT_PRODUCTS
    tile_size = args.tile_size if hasattr(args, 'tile_size') and args.tile_size else DEFAULT_TILE_SIZE
    product_list = [p.strip() for p in products.split(",")]

    # --- Load or generate point cloud ---
    input_path = args.input if hasattr(args, 'input') and args.input else None

    if input_path and Path(input_path).exists():
        # Try to read LAS/LAZ
        try:
            pc = read_las_file(input_path)
            logger.info(f"Loaded point cloud from {input_path}: {pc.n_points} points")
        except Exception as e:
            logger.error(f"Failed to read input file: {e}")
            print(f"ERROR: Failed to read input file: {e}", file=sys.stderr)
            return EXIT_VALIDATION
    else:
        # Generate synthetic data
        logger.info("Generating synthetic point cloud data")
        bounds = (0, 0, 200, 200)
        # New shared --bbox (string "W,S,E,N") takes priority; fall back to --bbox-bounds (4 floats).
        bbox_str = getattr(args, "bbox", None)
        if bbox_str:
            try:
                from _geoskill_data_fetcher import BBox as _BBox
                bb = _BBox.from_string(bbox_str)
                bounds = (bb.lon_min, bb.lat_min, bb.lon_max, bb.lat_max)
            except Exception:
                pass
        elif getattr(args, "bbox_bounds", None):
            bounds = tuple(args.bbox_bounds)
        pc = generate_synthetic_pointcloud(
            n_points=50000, bounds=bounds,
            ground_slope=0.03,
            vegetation_fraction=0.35,
            building_fraction=0.08,
            noise_fraction=0.01,
            seed=42
        )
        logger.info(f"Generated synthetic point cloud: {pc.n_points} points")

    # --- Point Cloud Statistics ---
    stats = compute_pointcloud_stats(pc)
    logger.info(f"Point cloud: {stats['n_points']} points, "
                f"bounds=({stats['bounds']['xmin']:.1f}, {stats['bounds']['ymin']:.1f}, "
                f"{stats['bounds']['xmax']:.1f}, {stats['bounds']['ymax']:.1f}), "
                f"density={stats['density_pts_per_m2']:.2f} pts/m2")

    # --- QA ---
    qa_results = run_pointcloud_qa(pc)
    logger.info(f"QA: {qa_results['status']}, {qa_results['n_warnings']} warnings")

    # --- Ground Classification ---
    if 2 not in pc.classification or np.sum(pc.classification == 2) < pc.n_points * 0.05:
        logger.info(f"Running ground classification (method={ground_method})")
        if ground_method == "grid_min":
            ground_mask = classify_ground_simple(pc, resolution=resolution)
        else:
            # Try scipy-based method
            try:
                ground_mask = classify_ground_gridmin(pc, resolution=resolution)
            except Exception:
                ground_mask = classify_ground_simple(pc, resolution=resolution)

        # Update classification
        pc.classification[ground_mask] = 2
        logger.info(f"Ground classification: {int(np.sum(ground_mask))} ground points")
    else:
        ground_mask = pc.classification == 2
        logger.info(f"Using existing ground classification: {int(np.sum(ground_mask))} points")

    # --- Raster Products ---
    output_files = {}
    dem = None
    dem_transform = None
    dsm = None
    dsm_transform = None

    if "dem" in product_list:
        dem, dem_transform = rasterize_dem(pc, resolution=resolution, ground_mask=ground_mask)
        dem_path = output_dir / "dem.tif"
        write_raster_geotiff(dem_path, dem, dem_transform, crs=pc.crs or "EPSG:32650")
        output_files["dem.tif"] = str(dem_path)
        logger.info(f"DEM: shape={dem.shape}, range=[{np.nanmin(dem):.2f}, {np.nanmax(dem):.2f}]")

    if "dsm" in product_list:
        dsm, dsm_transform = rasterize_dsm(pc, resolution=resolution)
        dsm_path = output_dir / "dsm.tif"
        write_raster_geotiff(dsm_path, dsm, dsm_transform, crs=pc.crs or "EPSG:32650")
        output_files["dsm.tif"] = str(dsm_path)
        logger.info(f"DSM: shape={dsm.shape}, range=[{np.nanmin(dsm):.2f}, {np.nanmax(dsm):.2f}]")

    if "chm" in product_list:
        if dem is None:
            dem, dem_transform = rasterize_dem(pc, resolution=resolution, ground_mask=ground_mask)
        if dsm is None:
            dsm, dsm_transform = rasterize_dsm(pc, resolution=resolution)
        chm = compute_chm(dem, dsm)
        chm_path = output_dir / "chm.tif"
        write_raster_geotiff(chm_path, chm, dem_transform, crs=pc.crs or "EPSG:32650")
        output_files["chm.tif"] = str(chm_path)
        logger.info(f"CHM: shape={chm.shape}, range=[{np.nanmin(chm):.2f}, {np.nanmax(chm):.2f}]")

    if "density" in product_list:
        density, density_transform = rasterize_density(pc, resolution=resolution)
        density_path = output_dir / "density.tif"
        write_raster_geotiff(density_path, density, density_transform, crs=pc.crs or "EPSG:32650")
        output_files["density.tif"] = str(density_path)
        logger.info(f"Density: shape={density.shape}, range=[{np.nanmin(density):.2f}, {np.nanmax(density):.2f}]")

    # --- Cross-section ---
    bounds = pc.bounds
    center_x = (bounds[0] + bounds[2]) / 2
    center_y = (bounds[1] + bounds[3]) / 2
    half_width = (bounds[2] - bounds[0]) / 4

    profile = extract_cross_section(
        pc,
        center_x - half_width, center_y,
        center_x + half_width, center_y,
        width=2.0, resolution=resolution
    )
    profile_path = output_dir / "profiles.geojson"
    write_profile_geojson(profile_path, profile)
    output_files["profiles.geojson"] = str(profile_path)
    logger.info(f"Cross-section: {profile.get('n_points', 0)} points, "
                f"length={profile.get('length_m', 0):.1f}m")

    # --- Height Statistics ---
    height_stats = compute_height_statistics(pc, dem, dem_transform)
    logger.info(f"Height stats: mean={height_stats.get('height_mean')}, "
                f"max={height_stats.get('height_max')}")

    # --- Write Standard Outputs ---

    # pointcloud_qa.json
    pointcloud_qa = {
        "pointcloud_stats": stats,
        "qa_results": qa_results,
        "height_statistics": height_stats,
        "ground_classification": {
            "method": ground_method,
            "n_ground_points": int(np.sum(pc.classification == 2)),
            "ground_fraction": round(float(np.sum(pc.classification == 2) / pc.n_points), 4),
        },
    }
    qa_path = output_dir / "pointcloud_qa.json"
    qa_path.write_text(
        json.dumps(pointcloud_qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    output_files["pointcloud_qa.json"] = str(qa_path)

    # request.json
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "input": input_path or "synthetic",
        "resolution": resolution,
        "ground_method": ground_method,
        "products": product_list,
        "tile_size": tile_size,
        "crs": pc.crs,
        "bounds": stats["bounds"],
        "n_points": stats["n_points"],
        "output_dir": str(output_dir),
    }
    request_path = output_dir / "request.json"
    request_path.write_text(
        json.dumps(request_info, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    output_files["request.json"] = str(request_path)

    # dataset-manifest.json
    dataset_manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "input_source": input_path or "synthetic",
        "n_points": pc.n_points,
        "bounds": stats["bounds"],
        "crs": pc.crs,
        "classification_histogram": stats["classification_histogram"],
        "density_pts_per_m2": stats["density_pts_per_m2"],
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    output_files["dataset-manifest.json"] = str(dataset_path)

    # output-manifest.json
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "analysis_parameters": request_info,
        "output_files": output_files,
        "raster_info": {
            "dem": {
                "shape": list(dem.shape) if dem is not None else None,
                "range": [round(float(np.nanmin(dem)), 3), round(float(np.nanmax(dem)), 3)] if dem is not None else None,
            },
            "dsm": {
                "shape": list(dsm.shape) if dsm is not None else None,
                "range": [round(float(np.nanmin(dsm)), 3), round(float(np.nanmax(dsm)), 3)] if dsm is not None else None,
            },
        },
        "height_summary": height_stats,
        "parameters": vars(args),  # T9: raw CLI args
        "summary": {
            "mode": "file" if input_path else "synthetic",
            "n_outputs": len(output_files),
            "n_points": pc.n_points if pc else 0,
        },
    }
    manifest_path = output_dir / "output-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    output_files["output-manifest.json"] = str(manifest_path)

    # qa.json
    qa = {
        "status": qa_results["status"],
        "checks": qa_results["checks"],
        "warnings": qa_results["warnings"],
        "n_warnings": qa_results["n_warnings"],
        "all_outputs_written": all(Path(p).exists() for p in output_files.values()),
        "n_output_files": len(output_files),
    }
    qa_out_path = output_dir / "qa.json"
    qa_out_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    output_files["qa.json"] = str(qa_out_path)

    logger.info("Analysis complete")
    cleanup_logging()
    return EXIT_OK


# ============================================================
# LAS File Reader (optional, requires laspy)
# ============================================================

def read_las_file(path: str) -> PointCloud:
    """Read a LAS/LAZ file using laspy if available."""
    try:
        import laspy
    except ImportError:
        raise ImportError("laspy required for LAS/LAZ reading. Install with: pip install laspy")

    las = laspy.read(path)
    x = np.array(las.x)
    y = np.array(las.y)
    z = np.array(las.z)
    classification = np.array(las.classification, dtype=np.uint8)
    intensity = np.array(las.intensity, dtype=np.float32)

    crs = None
    try:
        from laspy.vlrs import VLR
        # Try to extract CRS from VLRs
        for vlr in las.vlrs:
            if hasattr(vlr, 'string') and 'CRS' in str(vlr.string):
                crs = str(vlr.string)
                break
    except Exception:
        pass

    return PointCloud(x, y, z, classification, intensity, crs=crs)


# ============================================================
# CLI Entry Point
# ============================================================

# File-arg flags that must point to existing paths (None = skip check)
FILE_ARGS = {
    "input": "args.input",
}

# Numeric flags with (min, max) bounds; None = unbounded on that side
NUMERIC_RANGES = {
    # resolution must be > 0
    "resolution": (0.001, None),
    "tile_size": (0.001, None),
}


def validate_args(args) -> int:
    """Validate file existence and numeric ranges.
    Returns exit code (0 = ok, 2 = arg error)."""
    # File existence
    for flag, accessor in FILE_ARGS.items():
        path = eval(accessor)  # safe: only string concat
        if path is not None and not Path(path).exists():
            print(f"ERROR: --{flag} not found: {path}", file=sys.stderr)
            return 2
    # Numeric ranges
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
    parser = argparse.ArgumentParser(description="LiDAR Point Cloud Analysis")
    parser.add_argument("--input", "-i", default=None,
                        help="Input LAS/LAZ file path")
    parser.add_argument("--output-dir", "-o", default="lpca-output",
                        help="Output directory (default: lpca-output)")
    parser.add_argument("--resolution", type=float, default=DEFAULT_RESOLUTION,
                        help=f"Raster resolution in meters (default: {DEFAULT_RESOLUTION})")
    parser.add_argument("--ground-method", default=DEFAULT_GROUND_METHOD,
                        choices=["grid_min", "pmf"],
                        help=f"Ground classification method (default: {DEFAULT_GROUND_METHOD})")
    parser.add_argument("--products", default=DEFAULT_PRODUCTS,
                        help=f"Comma-separated products to generate (default: {DEFAULT_PRODUCTS})")
    parser.add_argument("--tile-size", type=float, default=DEFAULT_TILE_SIZE,
                        help=f"Tile size in meters (default: {DEFAULT_TILE_SIZE})")
    parser.add_argument("--bbox-bounds", nargs=4, type=float, default=None,
                        metavar=("XMIN", "YMIN", "XMAX", "YMAX"),
                        help="(legacy) Bounding box for synthetic data generation as 4 floats")
    add_bbox_date_args(parser)
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    args = parser.parse_args()

    rc = validate_args(args)
    if rc != 0:
        sys.exit(rc)

    try:
        sys.exit(run_analysis(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
