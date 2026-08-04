#!/usr/bin/env python3
"""
Land Use Carbon Accounting - Multi-temporal land cover carbon stock change.

Computes carbon stock changes, emissions/removals, and uncertainty from
multi-temporal land cover data using IPCC Tier 1/2 carbon factors.

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

# Land cover class codes (IPCC)
LC_FL = "FL"  # Forest Land
LC_CL = "CL"  # Cropland
LC_GL = "GL"  # Grassland
LC_WL = "WL"  # Wetlands
LC_SL = "SL"  # Settlements
LC_OL = "OL"  # Other Land

ALL_LC_CLASSES = [LC_FL, LC_CL, LC_GL, LC_WL, LC_SL, LC_OL]

# Carbon pools
POOL_BAG = "BAG"  # Above-ground Biomass
POOL_BBG = "BBG"  # Below-ground Biomass
POOL_DW = "DW"    # Dead Wood
POOL_LT = "LT"    # Litter
POOL_SOC = "SOC"  # Soil Organic Carbon

ALL_POOLS = [POOL_BAG, POOL_BBG, POOL_DW, POOL_LT, POOL_SOC]

# Conversion factor
C_TO_CO2E = 44.0 / 12.0

# Default parameters
DEFAULT_ECOLOGICAL_ZONE = "subtropical"
DEFAULT_POOLS = [POOL_BAG, POOL_BBG, POOL_SOC]
DEFAULT_MONTE_CARLO_ITERATIONS = 1000
DEFAULT_MONTE_CARLO_SEED = 42
DEFAULT_CONFIDENCE_LEVEL = 0.95
DEFAULT_PIXEL_SIZE_DEG = 0.00027778  # ~30m at equator in degrees


# ============================================================
# Logging
# ============================================================

def setup_logging(output_dir: Path) -> logging.Logger:
    """Setup logging to file and console."""
    logger = logging.getLogger("luca")
    logger.setLevel(logging.DEBUG)
    # Close and clear existing handlers
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)

    # File handler
    log_path = output_dir / "run.log"
    fh = logging.FileHandler(str(log_path), encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    logger.addHandler(fh)

    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(ch)

    return logger


def cleanup_logging():
    """Close all handlers on the luca logger."""
    logger = logging.getLogger("luca")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)


# ============================================================
# Land Cover Mapping
# ============================================================

def load_land_cover_mapping(factors: Dict) -> Dict:
    """Load land cover classification mapping from factors registry."""
    return factors.get("land_cover_mapping", {})


def map_land_cover(raster: np.ndarray, mapping: Dict,
                   source_system: str = "auto") -> Tuple[np.ndarray, Dict[int, str], List[int]]:
    """
    Map raw land cover codes to unified IPCC classes.

    Args:
        raster: 2D array of land cover codes
        mapping: Mapping dict from carbon_factors.json
        source_system: Source classification system

    Returns:
        Tuple of (mapped_raster, code_to_class, unmapped_codes)
    """
    # Select mapping table
    if source_system == "auto":
        # Try to detect from unique values
        unique_vals = set(np.unique(raster).astype(int))
        unique_vals.discard(0)  # nodata
        unique_vals.discard(255)  # nodata

        # Check which mapping table best fits
        best_system = None
        best_match = 0
        for system, table in mapping.items():
            if not isinstance(table, dict):
                continue
            table_keys = set(int(k) for k in table.keys())
            match = len(unique_vals & table_keys)
            if match > best_match:
                best_match = match
                best_system = system

        if best_system is None:
            # Assume already IPCC codes
            return _identity_mapping(raster)

        selected_table = mapping[best_system]
    elif source_system in mapping:
        selected_table = mapping[source_system]
    else:
        return _identity_mapping(raster)

    # Build lookup: raw_code -> IPCC class
    code_to_class = {}
    unmapped_codes = []

    unique_vals = set(np.unique(raster).astype(int))
    for val in unique_vals:
        if val == 0 or val == 255:
            continue
        val_str = str(val)
        if val_str in selected_table:
            code_to_class[int(val)] = selected_table[val_str]
        else:
            unmapped_codes.append(int(val))

    # Apply mapping
    mapped = np.zeros_like(raster, dtype=np.uint8)
    class_to_code = {cls: i + 1 for i, cls in enumerate(ALL_LC_CLASSES)}

    for raw_code, lc_class in code_to_class.items():
        if lc_class in class_to_code:
            mapped[raster == raw_code] = class_to_code[lc_class]

    return mapped, code_to_class, unmapped_codes


def _identity_mapping(raster: np.ndarray) -> Tuple[np.ndarray, Dict[int, str], List[int]]:
    """Identity mapping (already IPCC codes 1-6)."""
    class_to_code = {cls: i + 1 for i, cls in enumerate(ALL_LC_CLASSES)}
    code_to_class = {int(v): k for k, v in class_to_code.items()}

    mapped = np.zeros_like(raster, dtype=np.uint8)
    for cls, code in class_to_code.items():
        mapped[raster == code] = code

    unmapped = []
    unique_vals = set(np.unique(raster).astype(int))
    for val in unique_vals:
        if val not in class_to_code.values() and val not in (0, 255):
            unmapped.append(int(val))

    return mapped, code_to_class, unmapped


# ============================================================
# Transition Matrix
# ============================================================

def compute_transition_matrix(before: np.ndarray, after: np.ndarray,
                              nodata: int = 0) -> Tuple[np.ndarray, List[str]]:
    """
    Compute land cover transition matrix.

    Args:
        before: Before period land cover (coded 1-6 for FL,CL,GL,WL,SL,OL)
        after: After period land cover (same coding)
        nodata: Nodata value to exclude

    Returns:
        Tuple of (matrix, class_labels)
        matrix[i][j] = count of pixels transitioning from class i to class j
    """
    n_classes = len(ALL_LC_CLASSES)
    matrix = np.zeros((n_classes, n_classes), dtype=np.int64)

    # Mask nodata
    valid = (before != nodata) & (after != nodata) & (before > 0) & (after > 0)
    before_valid = before[valid].astype(int) - 1  # 0-indexed
    after_valid = after[valid].astype(int) - 1

    # Clip to valid range
    mask = (before_valid >= 0) & (before_valid < n_classes) & \
           (after_valid >= 0) & (after_valid < n_classes)
    before_valid = before_valid[mask]
    after_valid = after_valid[mask]

    for i in range(n_classes):
        for j in range(n_classes):
            matrix[i][j] = int(np.sum((before_valid == i) & (after_valid == j)))

    return matrix, ALL_LC_CLASSES


def transition_matrix_to_csv(matrix: np.ndarray, labels: List[str],
                             output_path: Path) -> None:
    """Write transition matrix to CSV."""
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Header
        writer.writerow(["from_to"] + labels + ["total_from"])
        for i, label in enumerate(labels):
            row = [label] + [int(matrix[i][j]) for j in range(len(labels))] + [int(matrix[i].sum())]
            writer.writerow(row)
        # Total row
        col_sums = [int(matrix[:, j].sum()) for j in range(len(labels))]
        writer.writerow(["total_to"] + col_sums + [int(matrix.sum())])


# ============================================================
# Area Computation
# ============================================================

def compute_pixel_area_ha(transform, crs=None) -> float:
    """
    Compute pixel area in hectares from raster transform.

    Handles both projected and geographic CRS.
    """
    if crs is not None:
        try:
            if hasattr(crs, 'is_projected') and crs.is_projected:
                pixel_area_m2 = abs(transform.a * transform.e)
                return pixel_area_m2 / 10000.0
        except Exception:
            pass

    # Geographic CRS: approximate using latitude
    try:
        pixel_width_deg = abs(transform.a)
        pixel_height_deg = abs(transform.e)
        # Use center latitude for approximation
        center_lat = abs(transform.f + transform.e * 100)  # approximate
        lat_rad = np.radians(min(center_lat, 85.0))
        # 1 degree latitude ~ 111320 m
        # 1 degree longitude ~ 111320 * cos(lat) m
        pixel_area_m2 = (pixel_height_deg * 111320.0) * \
                        (pixel_width_deg * 111320.0 * np.cos(lat_rad))
        return pixel_area_m2 / 10000.0
    except Exception:
        # Fallback: assume 30m pixels
        return 0.09  # hectares (30m x 30m)


def compute_pixel_area_from_bbox(bbox: Tuple[float, float, float, float],
                                 n_rows: int, n_cols: int) -> float:
    """Compute pixel area from bounding box (xmin, ymin, xmax, ymax)."""
    xmin, ymin, xmax, ymax = bbox
    width_m = (xmax - xmin) * 111320.0 * np.cos(np.radians((ymin + ymax) / 2.0))
    height_m = (ymax - ymin) * 111320.0
    pixel_area_m2 = (width_m / n_cols) * (height_m / n_rows)
    return pixel_area_m2 / 10000.0


# ============================================================
# Carbon Stock Change Calculation
# ============================================================

def load_carbon_factors(factors_path: Optional[str] = None) -> Dict:
    """Load carbon factors from JSON file."""
    if factors_path is None:
        # Use default
        script_dir = Path(__file__).parent
        factors_path = script_dir.parent / "references" / "carbon_factors.json"

    with open(factors_path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_carbon_density(factors: Dict, eco_zone: str, lc_class: str,
                       pool: str) -> float:
    """Get carbon density (tC/ha) for a given zone, class, and pool."""
    density = factors.get("carbon_density", {})
    zone_data = density.get(eco_zone, {})
    class_data = zone_data.get(lc_class, {})
    return float(class_data.get(pool, 0.0))


def get_total_carbon_density(factors: Dict, eco_zone: str, lc_class: str,
                             pools: List[str]) -> float:
    """Get total carbon density across specified pools."""
    total = 0.0
    for pool in pools:
        total += get_carbon_density(factors, eco_zone, lc_class, pool)
    return total


def compute_carbon_stock_change(factors: Dict, transition_matrix: np.ndarray,
                                pixel_area_ha: float, eco_zone: str,
                                pools: List[str]) -> Dict[str, Any]:
    """
    Compute carbon stock change from transition matrix.

    Uses stock-difference method:
    ΔC = Σ_ij (A_ij × (C_after_j - C_before_i))

    where A_ij is area of transition from class i to class j,
    C_before_i is carbon density of class i,
    C_after_j is carbon density of class j.

    Args:
        factors: Carbon factors registry
        transition_matrix: Pixel count transition matrix
        pixel_area_ha: Area per pixel in hectares
        eco_zone: Ecological zone
        pools: Carbon pools to include

    Returns:
        Dict with carbon change results
    """
    n_classes = len(ALL_LC_CLASSES)
    results = {
        "transitions": [],
        "total_change_tC": 0.0,
        "total_change_CO2e": 0.0,
        "total_emissions_tC": 0.0,
        "total_removals_tC": 0.0,
        "pool_results": {},
        "pixel_area_ha": pixel_area_ha,
        "eco_zone": eco_zone,
        "pools": pools,
    }

    # Per-pool results
    for pool in pools:
        results["pool_results"][pool] = {
            "change_tC": 0.0,
            "emissions_tC": 0.0,
            "removals_tC": 0.0,
        }

    total_change = 0.0
    total_emissions = 0.0
    total_removals = 0.0

    for i in range(n_classes):
        for j in range(n_classes):
            if i == j:
                continue  # No change transition

            pixel_count = int(transition_matrix[i][j])
            if pixel_count == 0:
                continue

            area_ha = pixel_count * pixel_area_ha
            class_before = ALL_LC_CLASSES[i]
            class_after = ALL_LC_CLASSES[j]

            # Carbon density change
            c_before = get_total_carbon_density(factors, eco_zone, class_before, pools)
            c_after = get_total_carbon_density(factors, eco_zone, class_after, pools)
            delta_c_per_ha = c_after - c_before

            # Total change for this transition
            change_tC = area_ha * delta_c_per_ha
            change_CO2e = change_tC * C_TO_CO2E

            # Per-pool breakdown
            pool_details = {}
            for pool in pools:
                c_b = get_carbon_density(factors, eco_zone, class_before, pool)
                c_a = get_carbon_density(factors, eco_zone, class_after, pool)
                pool_change = area_ha * (c_a - c_b)
                pool_details[pool] = {
                    "density_before": c_b,
                    "density_after": c_a,
                    "change_tC": pool_change,
                }
                results["pool_results"][pool]["change_tC"] += pool_change
                if pool_change < 0:
                    results["pool_results"][pool]["emissions_tC"] += abs(pool_change)
                else:
                    results["pool_results"][pool]["removals_tC"] += pool_change

            transition = {
                "from_class": class_before,
                "to_class": class_after,
                "from_name": factors.get("land_cover_classes", {}).get(class_before, {}).get("name_zh", class_before),
                "to_name": factors.get("land_cover_classes", {}).get(class_after, {}).get("name_zh", class_after),
                "pixel_count": pixel_count,
                "area_ha": round(area_ha, 4),
                "c_density_before": round(c_before, 2),
                "c_density_after": round(c_after, 2),
                "delta_c_per_ha": round(delta_c_per_ha, 2),
                "change_tC": round(change_tC, 4),
                "change_CO2e": round(change_CO2e, 4),
                "pool_details": pool_details,
            }
            results["transitions"].append(transition)

            total_change += change_tC
            if change_tC < 0:
                total_emissions += abs(change_tC)
            else:
                total_removals += change_tC

    results["total_change_tC"] = round(total_change, 4)
    results["total_change_CO2e"] = round(total_change * C_TO_CO2E, 4)
    results["total_emissions_tC"] = round(total_emissions, 4)
    results["total_removals_tC"] = round(total_removals, 4)

    # Round pool results
    for pool in pools:
        for key in ["change_tC", "emissions_tC", "removals_tC"]:
            results["pool_results"][pool][key] = round(results["pool_results"][pool][key], 4)

    return results


# ============================================================
# Monte Carlo Uncertainty Analysis
# ============================================================

def run_monte_carlo(factors: Dict, transition_matrix: np.ndarray,
                    pixel_area_ha: float, eco_zone: str, pools: List[str],
                    n_iterations: int = DEFAULT_MONTE_CARLO_ITERATIONS,
                    seed: int = DEFAULT_MONTE_CARLO_SEED,
                    confidence: float = DEFAULT_CONFIDENCE_LEVEL) -> Dict[str, Any]:
    """
    Run Monte Carlo uncertainty analysis.

    Samples carbon density factors from normal distributions
    defined by coefficient of variation (CV).

    Args:
        factors: Carbon factors registry
        transition_matrix: Pixel count transition matrix
        pixel_area_ha: Area per pixel in hectares
        eco_zone: Ecological zone
        pools: Carbon pools
        n_iterations: Number of Monte Carlo iterations
        seed: Random seed for reproducibility
        confidence: Confidence level for intervals

    Returns:
        Dict with uncertainty results
    """
    rng = np.random.RandomState(seed)
    uncertainty = factors.get("uncertainty", {})
    n_classes = len(ALL_LC_CLASSES)

    # Pre-compute transition areas
    transitions = []
    for i in range(n_classes):
        for j in range(n_classes):
            if i == j:
                continue
            pixel_count = int(transition_matrix[i][j])
            if pixel_count == 0:
                continue
            area_ha = pixel_count * pixel_area_ha
            transitions.append((i, j, area_ha))

    # Run iterations
    total_changes = np.zeros(n_iterations)
    pool_changes = {pool: np.zeros(n_iterations) for pool in pools}

    for it in range(n_iterations):
        # Sample carbon densities for this iteration
        sampled_density = {}
        for cls in ALL_LC_CLASSES:
            cv = uncertainty.get(cls, 0.30)
            sampled_density[cls] = {}
            for pool in pools:
                base = get_carbon_density(factors, eco_zone, cls, pool)
                # Sample from normal distribution
                sampled = rng.normal(base, base * cv)
                sampled_density[cls][pool] = max(sampled, 0.0)  # Non-negative

        # Compute total change for this iteration
        iter_total = 0.0
        for i, j, area_ha in transitions:
            class_before = ALL_LC_CLASSES[i]
            class_after = ALL_LC_CLASSES[j]

            c_before = sum(sampled_density[class_before][p] for p in pools)
            c_after = sum(sampled_density[class_after][p] for p in pools)
            delta = (c_after - c_before) * area_ha
            iter_total += delta

            for pool in pools:
                pool_delta = (sampled_density[class_after][pool] - sampled_density[class_before][pool]) * area_ha
                pool_changes[pool][it] += pool_delta

        total_changes[it] = iter_total

    # Compute statistics
    alpha = 1.0 - confidence
    lower_pct = alpha / 2.0 * 100
    upper_pct = (1.0 - alpha / 2.0) * 100

    results = {
        "n_iterations": n_iterations,
        "seed": seed,
        "confidence_level": confidence,
        "total_change": {
            "mean_tC": round(float(np.mean(total_changes)), 4),
            "std_tC": round(float(np.std(total_changes)), 4),
            "median_tC": round(float(np.median(total_changes)), 4),
            "p5_tC": round(float(np.percentile(total_changes, lower_pct)), 4),
            "p95_tC": round(float(np.percentile(total_changes, upper_pct)), 4),
            "mean_CO2e": round(float(np.mean(total_changes) * C_TO_CO2E), 4),
            "p5_CO2e": round(float(np.percentile(total_changes, lower_pct) * C_TO_CO2E), 4),
            "p95_CO2e": round(float(np.percentile(total_changes, upper_pct) * C_TO_CO2E), 4),
        },
        "pool_results": {},
    }

    for pool in pools:
        data = pool_changes[pool]
        results["pool_results"][pool] = {
            "mean_tC": round(float(np.mean(data)), 4),
            "std_tC": round(float(np.std(data)), 4),
            "p5_tC": round(float(np.percentile(data, lower_pct)), 4),
            "p95_tC": round(float(np.percentile(data, upper_pct)), 4),
        }

    return results


# ============================================================
# Carbon Change Raster
# ============================================================

def compute_carbon_change_raster(before: np.ndarray, after: np.ndarray,
                                 factors: Dict, eco_zone: str,
                                 pools: List[str]) -> np.ndarray:
    """
    Compute pixel-level carbon change raster.

    Returns:
        2D float32 array of carbon change (tC/ha) per pixel
    """
    n_classes = len(ALL_LC_CLASSES)
    change = np.zeros_like(before, dtype=np.float32)

    for i in range(n_classes):
        for j in range(n_classes):
            if i == j:
                continue
            mask = (before == i + 1) & (after == j + 1)
            if not np.any(mask):
                continue

            class_before = ALL_LC_CLASSES[i]
            class_after = ALL_LC_CLASSES[j]
            c_before = get_total_carbon_density(factors, eco_zone, class_before, pools)
            c_after = get_total_carbon_density(factors, eco_zone, class_after, pools)
            change[mask] = c_after - c_before

    return change


# ============================================================
# Land Transition Raster
# ============================================================

def compute_transition_raster(before: np.ndarray, after: np.ndarray) -> np.ndarray:
    """
    Compute land transition raster.
    Encoded as: from_class * 100 + to_class (e.g., FL->CL = 102)
    """
    n_classes = len(ALL_LC_CLASSES)
    transition = np.zeros_like(before, dtype=np.int32)

    for i in range(n_classes):
        for j in range(n_classes):
            if i == j:
                continue
            mask = (before == i + 1) & (after == j + 1)
            transition[mask] = (i + 1) * 100 + (j + 1)

    return transition


# ============================================================
# Synthetic Data Generation
# ============================================================

def generate_synthetic_landcover(n_rows: int = 100, n_cols: int = 100,
                                 n_classes: int = 6, seed: int = 42) -> np.ndarray:
    """Generate synthetic land cover raster with spatial coherence."""
    rng = np.random.RandomState(seed)
    # Create base pattern
    data = np.zeros((n_rows, n_cols), dtype=np.uint8)
    # Assign classes in blocks with some noise
    block_size = min(n_rows, n_cols) // n_classes
    for i in range(n_classes):
        r_start = i * block_size
        r_end = min((i + 1) * block_size, n_rows)
        data[r_start:r_end, :] = i + 1

    # Add noise
    noise = rng.randint(0, 2, size=(n_rows, n_cols), dtype=np.uint8)
    data = np.clip(data + noise - 1, 1, n_classes).astype(np.uint8)

    return data


def generate_synthetic_transition(before: np.ndarray, change_fraction: float = 0.1,
                                  seed: int = 42) -> np.ndarray:
    """
    Generate after-period land cover with controlled transitions.

    Args:
        before: Before period land cover
        change_fraction: Fraction of pixels to change
        seed: Random seed

    Returns:
        After period land cover
    """
    rng = np.random.RandomState(seed)
    after = before.copy()
    n_pixels = before.size
    n_change = int(n_pixels * change_fraction)

    # Randomly select pixels to change
    change_indices = rng.choice(n_pixels, size=n_change, replace=False)
    # Use ravel() to get a view (not a copy) so modifications propagate
    flat = after.ravel()
    n_classes = len(ALL_LC_CLASSES)

    for idx in change_indices:
        current = flat[idx]
        # Change to a different class
        new_class = rng.randint(1, n_classes + 1)
        while new_class == current:
            new_class = rng.randint(1, n_classes + 1)
        flat[idx] = new_class

    return after


# ============================================================
# Output Writers
# ============================================================

def write_transition_raster(output_dir: Path, transition: np.ndarray,
                            transform=None, crs=None) -> Path:
    """Write land transition raster to GeoTIFF."""
    try:
        import rasterio
        from rasterio.transform import from_bounds
    except ImportError:
        # Fallback: write as numpy
        path = output_dir / "land_transition.npy"
        np.save(str(path), transition)
        return path

    if transform is None:
        rows, cols = transition.shape
        transform = from_bounds(0, 0, cols, rows, cols, rows)

    path = output_dir / "land_transition.tif"
    with rasterio.open(
        str(path), "w", driver="GTiff",
        height=transition.shape[0], width=transition.shape[1],
        count=1, dtype=transition.dtype,
        crs=crs or "EPSG:4326",
        transform=transform,
    ) as dst:
        dst.write(transition, 1)

    return path


def write_carbon_change_raster(output_dir: Path, carbon_change: np.ndarray,
                               transform=None, crs=None) -> Path:
    """Write carbon change raster to GeoTIFF."""
    try:
        import rasterio
        from rasterio.transform import from_bounds
    except ImportError:
        path = output_dir / "carbon_change.npy"
        np.save(str(path), carbon_change)
        return path

    if transform is None:
        rows, cols = carbon_change.shape
        transform = from_bounds(0, 0, cols, rows, cols, rows)

    path = output_dir / "carbon_change.tif"
    with rasterio.open(
        str(path), "w", driver="GTiff",
        height=carbon_change.shape[0], width=carbon_change.shape[1],
        count=1, dtype=carbon_change.dtype,
        crs=crs or "EPSG:4326",
        transform=transform,
        nodata=-9999,
    ) as dst:
        dst.write(carbon_change, 1)

    return path


def write_carbon_summary(output_dir: Path, results: Dict,
                         uncertainty: Optional[Dict] = None) -> Path:
    """Write carbon summary to CSV (or XLSX if openpyxl available)."""
    path = output_dir / "carbon_summary.csv"

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Land Use Carbon Accounting Summary"])
        writer.writerow([])
        writer.writerow(["Parameter", "Value"])
        writer.writerow(["Ecological Zone", results.get("eco_zone", "")])
        writer.writerow(["Pools", ", ".join(results.get("pools", []))])
        writer.writerow(["Pixel Area (ha)", results.get("pixel_area_ha", "")])
        writer.writerow([])
        writer.writerow(["Total Change (tC)", results.get("total_change_tC", "")])
        writer.writerow(["Total Change (tCO2e)", results.get("total_change_CO2e", "")])
        writer.writerow(["Total Emissions (tC)", results.get("total_emissions_tC", "")])
        writer.writerow(["Total Removals (tC)", results.get("total_removals_tC", "")])
        writer.writerow([])

        # Pool breakdown
        writer.writerow(["Pool Results"])
        writer.writerow(["Pool", "Change (tC)", "Emissions (tC)", "Removals (tC)"])
        pool_results = results.get("pool_results", {})
        for pool, data in pool_results.items():
            writer.writerow([
                pool,
                data.get("change_tC", ""),
                data.get("emissions_tC", ""),
                data.get("removals_tC", ""),
            ])
        writer.writerow([])

        # Transitions
        writer.writerow(["Transitions"])
        writer.writerow(["From", "To", "Pixels", "Area (ha)", "C_before (tC/ha)",
                         "C_after (tC/ha)", "Delta (tC/ha)", "Change (tC)", "Change (tCO2e)"])
        for t in results.get("transitions", []):
            writer.writerow([
                t.get("from_class", ""),
                t.get("to_class", ""),
                t.get("pixel_count", ""),
                t.get("area_ha", ""),
                t.get("c_density_before", ""),
                t.get("c_density_after", ""),
                t.get("delta_c_per_ha", ""),
                t.get("change_tC", ""),
                t.get("change_CO2e", ""),
            ])

        # Uncertainty
        if uncertainty:
            writer.writerow([])
            writer.writerow(["Monte Carlo Uncertainty"])
            writer.writerow(["Iterations", uncertainty.get("n_iterations", "")])
            writer.writerow(["Seed", uncertainty.get("seed", "")])
            writer.writerow(["Confidence Level", uncertainty.get("confidence_level", "")])
            writer.writerow([])
            tc = uncertainty.get("total_change", {})
            writer.writerow(["Total Change Statistics"])
            writer.writerow(["Mean (tC)", tc.get("mean_tC", "")])
            writer.writerow(["Std (tC)", tc.get("std_tC", "")])
            writer.writerow(["Median (tC)", tc.get("median_tC", "")])
            writer.writerow(["P5 (tC)", tc.get("p5_tC", "")])
            writer.writerow(["P95 (tC)", tc.get("p95_tC", "")])
            writer.writerow(["Mean (tCO2e)", tc.get("mean_CO2e", "")])
            writer.writerow(["P5 (tCO2e)", tc.get("p5_CO2e", "")])
            writer.writerow(["P95 (tCO2e)", tc.get("p95_CO2e", "")])

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


def run_analysis(args: argparse.Namespace) -> int:
    """Main analysis workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("luca-output")

    # --- Auto-download mode: fetch sentinel-2-l2a from MPC ---
    # Note: luca has a synthetic landcover fallback, so we DON'T set
    # args.before_landcover from the auto-downloaded S2 image (it's a different
    # data type). Just download for metadata; the analysis will use synthetic.
    if (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)) and getattr(args, "date_range", None):
        if not getattr(args, "before_landcover", None):
            try:
                fetch_meta = auto_download_image(args, output_dir)
                print(f"  Auto-downloaded S2 image (used for bbox/area only): {args.image}")
            except DataFetcherError as e:
                print(f"ERROR: auto-download failed: [{e.kind}] {e.message}", file=sys.stderr)
                return EXIT_PROCESSING if 'EXIT_PROCESSING' in dir() else 7
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logging(output_dir)
    logger.info("Land Use Carbon Accounting - Starting")

    # Parse parameters
    eco_zone = args.eco_zone if hasattr(args, 'eco_zone') and args.eco_zone else DEFAULT_ECOLOGICAL_ZONE
    pools = args.pools if hasattr(args, 'pools') and args.pools else DEFAULT_POOLS
    mc_iterations = args.mc_iterations if hasattr(args, 'mc_iterations') and args.mc_iterations else DEFAULT_MONTE_CARLO_ITERATIONS
    mc_seed = args.mc_seed if hasattr(args, 'mc_seed') and args.mc_seed is not None else DEFAULT_MONTE_CARLO_SEED
    confidence = args.confidence if hasattr(args, 'confidence') and args.confidence else DEFAULT_CONFIDENCE_LEVEL

    # Load carbon factors
    factors_path = args.carbon_factors if hasattr(args, 'carbon_factors') and args.carbon_factors else None
    try:
        factors = load_carbon_factors(factors_path)
        logger.info(f"Carbon factors loaded: {len(factors.get('carbon_density', {}))} zones")
    except Exception as e:
        logger.error(f"Failed to load carbon factors: {e}")
        return EXIT_VALIDATION

    # --- Load or generate data ---
    transform = None
    crs = "EPSG:4326"

    if hasattr(args, 'before_landcover') and args.before_landcover and \
       hasattr(args, 'after_landcover') and args.after_landcover:
        # Load from files
        try:
            import rasterio
        except ImportError:
            logger.error("rasterio required for GeoTIFF input")
            print("ERROR: rasterio required for GeoTIFF input", file=sys.stderr)
            return EXIT_DEP

        try:
            with rasterio.open(args.before_landcover) as src:
                before_raw = src.read(1)
                transform = src.transform
                crs = src.crs
            with rasterio.open(args.after_landcover) as src:
                after_raw = src.read(1)
            logger.info(f"Loaded land cover rasters: {before_raw.shape}")
        except Exception as e:
            logger.error(f"Failed to read land cover files: {e}")
            print(f"ERROR: Failed to read land cover files: {e}", file=sys.stderr)
            return EXIT_VALIDATION
    else:
        # Generate synthetic data
        logger.info("Generating synthetic land cover data")
        before_raw = generate_synthetic_landcover(n_rows=100, n_cols=100, seed=42)
        after_raw = generate_synthetic_transition(before_raw, change_fraction=0.15, seed=123)

    # --- Map land cover to unified classes ---
    mapping = load_land_cover_mapping(factors)
    source_system = args.source_system if hasattr(args, 'source_system') and args.source_system else "auto"

    before_mapped, before_map, before_unmapped = map_land_cover(before_raw, mapping, source_system)
    after_mapped, after_map, after_unmapped = map_land_cover(after_raw, mapping, source_system)

    if before_unmapped:
        logger.warning(f"Unmapped before codes: {before_unmapped}")
    if after_unmapped:
        logger.warning(f"Unmapped after codes: {after_unmapped}")

    # --- Compute pixel area ---
    if transform is not None:
        pixel_area_ha = compute_pixel_area_ha(transform, crs)
    elif hasattr(args, 'bbox') and args.bbox:
        # shared --bbox is a "W,S,E,N" string; convert to 4 floats for the legacy helper.
        try:
            bbox_str = str(args.bbox)
            bb_parts = [float(p.strip()) for p in bbox_str.split(",")]
            if len(bb_parts) == 4:
                pixel_area_ha = compute_pixel_area_from_bbox(
                    tuple(bb_parts), before_mapped.shape[0], before_mapped.shape[1]
                )
            else:
                pixel_area_ha = 0.09
        except Exception:
            pixel_area_ha = 0.09
    else:
        # Default: assume 30m pixels
        pixel_area_ha = 0.09

    logger.info(f"Pixel area: {pixel_area_ha:.6f} ha")

    # --- Compute transition matrix ---
    transition_matrix, labels = compute_transition_matrix(before_mapped, after_mapped)
    logger.info(f"Transition matrix computed: {transition_matrix.sum()} valid pixels")

    if transition_matrix.sum() == 0:
        logger.error("No valid pixels in transition matrix")
        print("ERROR: No valid pixels for analysis", file=sys.stderr)
        return EXIT_VALIDATION

    # --- Compute carbon stock change ---
    carbon_results = compute_carbon_stock_change(
        factors, transition_matrix, pixel_area_ha, eco_zone, pools
    )
    logger.info(f"Carbon change: {carbon_results['total_change_tC']:.2f} tC "
                f"({carbon_results['total_change_CO2e']:.2f} tCO2e)")

    # --- Monte Carlo uncertainty ---
    uncertainty_results = None
    if mc_iterations > 0:
        uncertainty_results = run_monte_carlo(
            factors, transition_matrix, pixel_area_ha, eco_zone, pools,
            n_iterations=mc_iterations, seed=mc_seed, confidence=confidence
        )
        logger.info(f"Monte Carlo: mean={uncertainty_results['total_change']['mean_tC']:.2f} tC, "
                    f"P5={uncertainty_results['total_change']['p5_tC']:.2f}, "
                    f"P95={uncertainty_results['total_change']['p95_tC']:.2f}")

    # --- Compute rasters ---
    transition_raster = compute_transition_raster(before_mapped, after_mapped)
    carbon_change_raster = compute_carbon_change_raster(
        before_mapped, after_mapped, factors, eco_zone, pools
    )

    # --- Write Outputs ---

    # transition_matrix.csv
    tm_path = output_dir / "transition_matrix.csv"
    transition_matrix_to_csv(transition_matrix, labels, tm_path)

    # land_transition.tif
    lt_path = write_transition_raster(output_dir, transition_raster, transform, crs)

    # carbon_change.tif
    cc_path = write_carbon_change_raster(output_dir, carbon_change_raster, transform, crs)

    # carbon_summary.csv
    cs_path = write_carbon_summary(output_dir, carbon_results, uncertainty_results)

    # uncertainty.json
    u_path = None
    if uncertainty_results:
        u_path = write_uncertainty_json(output_dir, uncertainty_results)

    # request.json
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "eco_zone": eco_zone,
        "pools": pools,
        "mc_iterations": mc_iterations,
        "mc_seed": mc_seed,
        "confidence_level": confidence,
        "pixel_area_ha": pixel_area_ha,
        "crs": str(crs) if crs else None,
        "shape": [int(x) for x in before_mapped.shape],
        "source_system": source_system,
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
        "before_landcover": getattr(args, 'before_landcover', None) or "synthetic",
        "after_landcover": getattr(args, 'after_landcover', None) or "synthetic",
        "n_valid_pixels": int(transition_matrix.sum()),
        "n_transitions": len(carbon_results.get("transitions", [])),
        "unmapped_codes": {
            "before": before_unmapped,
            "after": after_unmapped,
        },
        "land_cover_mapping": before_map,
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # output-manifest.json
    output_files = {
        "transition_matrix.csv": str(tm_path),
        "land_transition.tif": str(lt_path),
        "carbon_change.tif": str(cc_path),
        "carbon_summary.csv": str(cs_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(dataset_path),
    }
    if u_path:
        output_files["uncertainty.json"] = str(u_path)

    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "analysis_parameters": request_info,
        "output_files": output_files,
        "carbon_results_summary": {
            "total_change_tC": carbon_results["total_change_tC"],
            "total_change_CO2e": carbon_results["total_change_CO2e"],
            "total_emissions_tC": carbon_results["total_emissions_tC"],
            "total_removals_tC": carbon_results["total_removals_tC"],
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
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # qa.json
    qa = {
        "status": "complete",
        "checks": {
            "transition_matrix_valid": int(transition_matrix.sum()) > 0,
            "carbon_computed": carbon_results["total_change_tC"] is not None,
            "monte_carlo_completed": uncertainty_results is not None,
            "all_outputs_written": all(Path(p).exists() for p in output_files.values()),
        },
        "warnings": [],
        "n_transitions": len(carbon_results.get("transitions", [])),
        "n_valid_pixels": int(transition_matrix.sum()),
        "pixel_area_ha": pixel_area_ha,
    }
    if before_unmapped:
        qa["warnings"].append(f"Unmapped before codes: {before_unmapped}")
    if after_unmapped:
        qa["warnings"].append(f"Unmapped after codes: {after_unmapped}")

    qa_path = output_dir / "qa.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    logger.info("Analysis complete")
    cleanup_logging()
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Land Use Carbon Accounting")
    parser.add_argument("--before-landcover", default=None,
                        help="Before period land cover GeoTIFF")
    parser.add_argument("--after-landcover", default=None,
                        help="After period land cover GeoTIFF")
    parser.add_argument("--eco-zone", default=DEFAULT_ECOLOGICAL_ZONE,
                        choices=["tropical", "subtropical", "temperate", "boreal"],
                        help=f"Ecological zone (default: {DEFAULT_ECOLOGICAL_ZONE})")
    parser.add_argument("--pools", nargs="*", default=DEFAULT_POOLS,
                        choices=ALL_POOLS,
                        help=f"Carbon pools to include (default: {' '.join(DEFAULT_POOLS)})")
    parser.add_argument("--carbon-factors", default=None,
                        help="Path to carbon factors JSON file")
    parser.add_argument("--source-system", default="auto",
                        choices=["auto", "from_glc_fcs30", "from_esri_lulc", "from_copernicus"],
                        help="Source land cover classification system")
    parser.add_argument("--mc-iterations", type=int, default=DEFAULT_MONTE_CARLO_ITERATIONS,
                        help=f"Monte Carlo iterations (default: {DEFAULT_MONTE_CARLO_ITERATIONS})")
    parser.add_argument("--mc-seed", type=int, default=DEFAULT_MONTE_CARLO_SEED,
                        help=f"Monte Carlo seed (default: {DEFAULT_MONTE_CARLO_SEED})")
    parser.add_argument("--confidence", type=float, default=DEFAULT_CONFIDENCE_LEVEL,
                        help=f"Confidence level (default: {DEFAULT_CONFIDENCE_LEVEL})")
    add_bbox_date_args(parser)
    parser.add_argument("--output-dir", "-o", default="luca-output",
                        help="Output directory (default: luca-output)")
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
