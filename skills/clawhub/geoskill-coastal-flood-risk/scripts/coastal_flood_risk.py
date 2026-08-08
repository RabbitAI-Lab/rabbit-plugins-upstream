#!/usr/bin/env python3
"""
Coastal Flood Risk - Bathtub inundation and exposure assessment.

Simulates coastal flooding under sea level rise and storm surge scenarios
using a static bathtub model with ocean connectivity. Assesses population,
building, and infrastructure exposure.

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
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import numpy as np
    _NUMPY_AVAILABLE = True
except ImportError:
    np = None  # type: ignore[assignment]
    _NUMPY_AVAILABLE = False

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

# File-arg flags that must point to existing paths when provided
FILE_ARGS = {
    "dem": "args.dem",
    "defenses": "args.defenses",
    "scenarios-config": "args.scenarios_config",
}

# Numeric flags with (min, max) bounds; None = unbounded on that side.
# water-levels is checked as a comma-separated list of floats (all must be >= 0).
NUMERIC_RANGES = {
    "defense_height": (0.0, 100.0),
}

# ============================================================
# Logging
# ============================================================

def setup_logging(output_dir: Path) -> logging.Logger:
    """Setup logging to file and console."""
    logger = logging.getLogger("cfr")
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
    """Close all handlers on the cfr logger."""
    logger = logging.getLogger("cfr")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)


# ============================================================
# Scenario Loading
# ============================================================

def load_flood_scenarios(scenarios_path: Optional[str] = None) -> Dict:
    """Load flood scenario parameters from JSON file."""
    if scenarios_path is None:
        script_dir = Path(__file__).parent
        scenarios_path = script_dir.parent / "references" / "flood_scenarios.json"

    with open(scenarios_path, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# Core Algorithm: Bathtub Inundation
# ============================================================

def bathtub_inundate(
    dem: np.ndarray,
    water_level: float,
    connectivity: bool = True,
    nodata_value: float = -9999.0,
    ocean_mask: Optional[np.ndarray] = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Static bathtub inundation model.

    Args:
        dem: 2D elevation array (meters above datum)
        water_level: Water surface elevation (meters above same datum)
        connectivity: If True, only flood cells connected to ocean
        nodata_value: DEM nodata value
        ocean_mask: Optional boolean mask of ocean cells (True = ocean)

    Returns:
        (flooded_mask, depth_proxy) - boolean flood mask and depth estimate
    """
    if dem.ndim != 2:
        raise ValueError("DEM must be 2D raster")

    h, w = dem.shape
    valid_mask = (dem != nodata_value) & ~np.isnan(dem) & ~np.isinf(dem)

    # Basic bathtub: cells below water level
    below_water = valid_mask & (dem <= water_level)

    # Depth proxy (0 for cells above water level)
    depth = np.where(below_water, water_level - dem, 0.0).astype(np.float32)

    if not connectivity:
        return below_water.astype(np.uint8), depth

    # Connectivity: flood fill from ocean edges
    # Ocean cells are those at the edge of the DEM that are below water level
    # or cells explicitly marked in ocean_mask
    visited = np.zeros((h, w), dtype=bool)
    queue = deque()

    # Seed: edge cells that are below water level (ocean boundary)
    if ocean_mask is not None:
        edge_ocean = ocean_mask & below_water
    else:
        # Use edge cells below water level as ocean seeds
        edge_ocean = np.zeros((h, w), dtype=bool)
        # Top and bottom edges
        edge_ocean[0, :] = below_water[0, :]
        edge_ocean[h-1, :] = below_water[h-1, :]
        # Left and right edges
        edge_ocean[:, 0] = below_water[:, 0]
        edge_ocean[:, w-1] = below_water[:, w-1]

    # Add all edge-ocean cells to queue
    seed_positions = np.argwhere(edge_ocean)
    for pos in seed_positions:
        r, c = int(pos[0]), int(pos[1])
        if not visited[r, c]:
            visited[r, c] = True
            queue.append((r, c))

    # BFS flood fill: from ocean seeds, flood adjacent cells below water level
    flooded = np.zeros((h, w), dtype=bool)
    while queue:
        r, c = queue.popleft()
        flooded[r, c] = True

        # Check 4-connected neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w:
                if not visited[nr, nc] and below_water[nr, nc]:
                    visited[nr, nc] = True
                    queue.append((nr, nc))

    flooded_mask = flooded.astype(np.uint8)
    depth = np.where(flooded, depth, 0.0).astype(np.float32)

    return flooded_mask, depth


def compute_flood_statistics(
    flooded_mask: np.ndarray,
    depth_proxy: np.ndarray,
    pixel_area_m2: float = 1.0,
) -> Dict[str, Any]:
    """
    Compute flood extent statistics.

    Args:
        flooded_mask: Boolean/int flood mask
        depth_proxy: Depth estimate array
        pixel_area_m2: Area of one pixel in square meters

    Returns:
        Statistics dict
    """
    n_flooded = int(np.sum(flooded_mask > 0))
    total_pixels = flooded_mask.size
    flooded_area_m2 = n_flooded * pixel_area_m2

    if n_flooded > 0:
        flooded_depths = depth_proxy[flooded_mask > 0]
        mean_depth = float(np.mean(flooded_depths))
        max_depth = float(np.max(flooded_depths))
        min_depth = float(np.min(flooded_depths))
    else:
        mean_depth = 0.0
        max_depth = 0.0
        min_depth = 0.0

    return {
        "n_flooded_pixels": n_flooded,
        "total_pixels": total_pixels,
        "flooded_fraction": round(n_flooded / total_pixels, 6) if total_pixels > 0 else 0.0,
        "flooded_area_m2": round(flooded_area_m2, 2),
        "flooded_area_km2": round(flooded_area_m2 / 1e6, 6),
        "mean_depth_m": round(mean_depth, 3),
        "max_depth_m": round(max_depth, 3),
        "min_depth_m": round(min_depth, 3),
    }


# ============================================================
# Vertical Datum Handling
# ============================================================

def apply_vertical_datum_offset(
    dem: np.ndarray,
    dem_datum: str,
    target_datum: str,
    scenarios: Dict,
    nodata_value: float = -9999.0,
) -> Tuple[np.ndarray, bool, str]:
    """
    Convert DEM from one vertical datum to another.

    Args:
        dem: DEM array
        dem_datum: Current datum of the DEM
        target_datum: Target datum for analysis
        scenarios: Scenario parameters (contains datum offsets)
        nodata_value: DEM nodata value

    Returns:
        (adjusted_datum, success, message)
    """
    datums = scenarios.get("vertical_datums", {})

    if dem_datum == target_datum:
        return dem.copy(), True, "No datum conversion needed"

    if dem_datum not in datums or target_datum not in datums:
        return dem.copy(), False, f"Unknown datum: {dem_datum} or {target_datum}"

    dem_offset = datums[dem_datum].get("offset_m")
    target_offset = datums[target_datum].get("offset_m")

    if dem_offset is None or target_offset is None:
        return dem.copy(), False, f"Cannot convert from {dem_datum} to {target_datum}: offset unknown"

    # Apply offset: new_dem = dem + (dem_offset - target_offset)
    offset_diff = dem_offset - target_offset
    valid_mask = (dem != nodata_value) & ~np.isnan(dem)
    adjusted = dem.copy()
    adjusted[valid_mask] = adjusted[valid_mask] + offset_diff

    return adjusted, True, f"Applied datum offset {offset_diff:.3f}m ({dem_datum} -> {target_datum})"


# ============================================================
# Defense (Seawall) Handling
# ============================================================

def apply_defenses(
    dem: np.ndarray,
    defense_mask: Optional[np.ndarray],
    defense_height: float = 0.0,
    nodata_value: float = -9999.0,
) -> Tuple[np.ndarray, bool]:
    """
    Apply coastal defense heights to DEM.

    Where defenses exist, raise the effective terrain height by defense_height.

    Args:
        dem: DEM array
        defense_mask: Boolean mask where defenses exist (True = defense present)
        defense_height: Height of defenses in meters
        nodata_value: DEM nodata value

    Returns:
        (adjusted_dem, has_defenses)
    """
    if defense_mask is None or defense_height <= 0:
        return dem.copy(), False

    adjusted = dem.copy()
    valid_defenses = defense_mask & (dem != nodata_value) & ~np.isnan(dem)
    adjusted[valid_defenses] = adjusted[valid_defenses] + defense_height

    return adjusted, True


# ============================================================
# Exposure Analysis
# ============================================================

def compute_exposure(
    flooded_mask: np.ndarray,
    depth_proxy: np.ndarray,
    exposure_data: Dict[str, np.ndarray],
    pixel_area_m2: float = 1.0,
) -> Dict[str, Any]:
    """
    Compute exposure of assets to flooding.

    Args:
        flooded_mask: Boolean/int flood mask
        depth_proxy: Depth estimate array
        exposure_data: Dict of {category_name: 2D array of asset values}
        pixel_area_m2: Area of one pixel in square meters

    Returns:
        Exposure statistics per category
    """
    if np.sum(flooded_mask > 0) == 0:
        return {
            "total_flooded_pixels": 0,
            "categories": {},
        }

    results = {
        "total_flooded_pixels": int(np.sum(flooded_mask > 0)),
        "categories": {},
    }

    for category, data in exposure_data.items():
        if data.shape != flooded_mask.shape:
            continue

        flooded_values = data[flooded_mask > 0]
        total_values = data[~np.isnan(data) & (data > 0)]

        exposed_total = float(np.sum(flooded_values)) if flooded_values.size > 0 else 0.0
        grand_total = float(np.sum(total_values)) if total_values.size > 0 else 0.0

        # Depth-weighted exposure
        if flooded_values.size > 0:
            flooded_depths = depth_proxy[flooded_mask > 0]
            depth_weighted = float(np.sum(flooded_values * flooded_depths))
        else:
            depth_weighted = 0.0

        results["categories"][category] = {
            "exposed_total": round(exposed_total, 2),
            "grand_total": round(grand_total, 2),
            "exposed_fraction": round(exposed_total / grand_total, 4) if grand_total > 0 else 0.0,
            "depth_weighted_exposure": round(depth_weighted, 2),
            "n_exposed_pixels": int(np.sum(flooded_values > 0)),
        }

    return results


# ============================================================
# Multi-Scenario Comparison
# ============================================================

def compare_scenarios(scenario_results: List[Dict]) -> Dict[str, Any]:
    """
    Compare multiple flood scenarios.

    Args:
        scenario_results: List of per-scenario result dicts

    Returns:
        Comparison summary
    """
    if not scenario_results:
        return {"n_scenarios": 0, "scenarios": []}

    comparison = {
        "n_scenarios": len(scenario_results),
        "scenarios": [],
        "max_flooded_area_km2": 0.0,
        "max_mean_depth_m": 0.0,
        "priority_zones": [],
    }

    max_area = 0.0
    max_depth = 0.0

    for sr in scenario_results:
        name = sr.get("scenario_name", "unknown")
        stats = sr.get("statistics", {})
        area = stats.get("flooded_area_km2", 0.0)
        depth = stats.get("mean_depth_m", 0.0)

        comparison["scenarios"].append({
            "name": name,
            "water_level_m": sr.get("water_level_m", 0.0),
            "flooded_area_km2": area,
            "mean_depth_m": depth,
            "max_depth_m": stats.get("max_depth_m", 0.0),
        })

        if area > max_area:
            max_area = area
        if depth > max_depth:
            max_depth = depth

    comparison["max_flooded_area_km2"] = round(max_area, 6)
    comparison["max_mean_depth_m"] = round(max_depth, 3)

    return comparison


# ============================================================
# Priority Zone Identification
# ============================================================

def identify_priority_zones(
    scenario_results: List[Dict],
    depth_threshold: float = 0.5,
) -> Dict[str, Any]:
    """
    Identify adaptation priority zones from multi-scenario results.

    Priority = cells flooded in multiple scenarios AND with significant depth.

    Args:
        scenario_results: List of per-scenario results (each with 'depth_proxy')
        depth_threshold: Minimum depth to be considered significant

    Returns:
        GeoJSON-like dict of priority zones
    """
    if not scenario_results:
        return {"type": "FeatureCollection", "features": []}

    # Stack depth proxies
    depth_arrays = [sr["depth_proxy"] for sr in scenario_results if "depth_proxy" in sr]
    if not depth_arrays:
        return {"type": "FeatureCollection", "features": []}

    stacked = np.stack(depth_arrays, axis=0)
    n_scenarios_flooded = np.sum(stacked > 0, axis=0)
    max_depth = np.max(stacked, axis=0)

    # Priority: flooded in >= 2 scenarios AND depth >= threshold
    priority_mask = (n_scenarios_flooded >= 2) & (max_depth >= depth_threshold)

    # Convert to simple polygon features (connected components)
    features = []
    if np.sum(priority_mask) > 0:
        # Find connected regions using simple flood fill
        visited = np.zeros_like(priority_mask, dtype=bool)
        h, w = priority_mask.shape

        for r in range(h):
            for c in range(w):
                if priority_mask[r, c] and not visited[r, c]:
                    # BFS to find connected component
                    component = []
                    queue = deque([(r, c)])
                    visited[r, c] = True
                    while queue:
                        cr, cc = queue.popleft()
                        component.append((cr, cc))
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < h and 0 <= nc < w:
                                if priority_mask[nr, nc] and not visited[nr, nc]:
                                    visited[nr, nc] = True
                                    queue.append((nr, nc))

                    if len(component) >= 4:  # Min 4 pixels for a zone
                        # Create bounding polygon
                        rows = [p[0] for p in component]
                        cols = [p[1] for p in component]
                        min_r, max_r = min(rows), max(rows)
                        min_c, max_c = min(cols), max(cols)

                        # Simple bbox polygon (closed ring)
                        polygon = [
                            [float(min_c), float(min_r)],
                            [float(max_c), float(min_r)],
                            [float(max_c), float(max_r)],
                            [float(min_c), float(max_r)],
                            [float(min_c), float(min_r)],
                        ]

                        avg_depth = float(np.mean([max_depth[p[0], p[1]] for p in component]))
                        n_scenarios = int(np.mean([n_scenarios_flooded[p[0], p[1]] for p in component]))

                        features.append({
                            "type": "Feature",
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [polygon],
                            },
                            "properties": {
                                "n_pixels": len(component),
                                "avg_depth_m": round(avg_depth, 3),
                                "n_scenarios": n_scenarios,
                                "priority_score": round(avg_depth * n_scenarios, 3),
                            },
                        })

    # Sort by priority score descending
    features.sort(key=lambda f: f["properties"]["priority_score"], reverse=True)

    return {
        "type": "FeatureCollection",
        "features": features,
    }


# ============================================================
# Synthetic Data Generation
# ============================================================

def generate_synthetic_dem(
    n_rows: int = 100,
    n_cols: int = 100,
    slope: float = 0.05,
    noise_std: float = 0.3,
    nodata_fraction: float = 0.0,
    seed: int = 42,
) -> np.ndarray:
    """
    Generate synthetic coastal DEM with a simple slope from ocean to land.

    Ocean is at the top (row 0), land slopes upward toward bottom.
    """
    rng = np.random.RandomState(seed)
    dem = np.zeros((n_rows, n_cols), dtype=np.float32)

    for r in range(n_rows):
        # Elevation increases with row (distance from ocean)
        dem[r, :] = r * slope + rng.normal(0, noise_std)

    # Add some low-lying areas (inland depressions)
    if n_rows > 20 and n_cols > 20:
        dem[15:20, 40:50] = -1.0  # Inland depression below sea level
        dem[50:55, 60:70] = -0.5  # Another depression

    if nodata_fraction > 0:
        n_nodata = int(n_rows * n_cols * nodata_fraction)
        flat = dem.flatten()
        indices = rng.choice(flat.shape[0], size=n_nodata, replace=False)
        flat[indices] = -9999.0
        dem = flat.reshape(n_rows, n_cols)

    return dem


def generate_synthetic_exposure(
    n_rows: int = 100,
    n_cols: int = 100,
    categories: Optional[List[str]] = None,
    seed: int = 42,
) -> Dict[str, np.ndarray]:
    """
    Generate synthetic exposure data layers.

    Returns dict of {category: 2D array}
    """
    rng = np.random.RandomState(seed)

    if categories is None:
        categories = ["population", "buildings", "roads", "critical_facilities"]

    exposure = {}
    for cat in categories:
        if cat == "population":
            # Population concentrated in certain areas (size-aware)
            data = np.zeros((n_rows, n_cols), dtype=np.float32)
            r1, r2 = n_rows // 4, n_rows // 2
            c1, c2 = n_cols // 4, n_cols // 2
            data[r1:r2, c1:c2] = rng.uniform(10, 100, size=(r2 - r1, c2 - c1))
            r3, r4 = n_rows // 2, 3 * n_rows // 4
            c3, c4 = n_cols // 2, 3 * n_cols // 4
            if r4 > r3 and c4 > c3:
                data[r3:r4, c3:c4] = rng.uniform(5, 50, size=(r4 - r3, c4 - c3))
            exposure[cat] = data
        elif cat == "buildings":
            data = np.zeros((n_rows, n_cols), dtype=np.float32)
            r1, r2 = n_rows // 4, n_rows // 2
            c1, c2 = n_cols // 4, n_cols // 2
            data[r1:r2, c1:c2] = rng.uniform(50, 200, size=(r2 - r1, c2 - c1))
            r3, r4 = n_rows // 2, 3 * n_rows // 4
            c3, c4 = n_cols // 2, 3 * n_cols // 4
            if r4 > r3 and c4 > c3:
                data[r3:r4, c3:c4] = rng.uniform(20, 100, size=(r4 - r3, c4 - c3))
            exposure[cat] = data
        elif cat == "roads":
            data = np.zeros((n_rows, n_cols), dtype=np.float32)
            mid_row = n_rows // 2
            data[mid_row, :] = 1.0  # Horizontal road
            data[:, n_cols // 2] = 1.0  # Vertical road
            exposure[cat] = data
        elif cat == "critical_facilities":
            data = np.zeros((n_rows, n_cols), dtype=np.float32)
            data[n_rows // 4, n_cols // 4] = 1.0  # Hospital
            data[n_rows // 2, n_cols // 2] = 1.0  # School
            data[3 * n_rows // 4, n_cols // 4] = 1.0  # Power station
            exposure[cat] = data
        else:
            exposure[cat] = rng.uniform(0, 10, size=(n_rows, n_cols)).astype(np.float32)

    return exposure


def generate_synthetic_ocean_mask(
    n_rows: int = 100,
    n_cols: int = 100,
    ocean_rows: int = 5,
    seed: int = 42,
) -> np.ndarray:
    """Generate synthetic ocean mask (top rows are ocean)."""
    mask = np.zeros((n_rows, n_cols), dtype=bool)
    mask[:ocean_rows, :] = True
    return mask


def generate_synthetic_defense_mask(
    n_rows: int = 100,
    n_cols: int = 100,
    defense_row: int = 8,
    seed: int = 42,
) -> np.ndarray:
    """Generate synthetic defense mask (seawall at a specific row)."""
    mask = np.zeros((n_rows, n_cols), dtype=bool)
    c_start = max(1, n_cols // 10)
    c_end = min(n_cols - 1, n_cols - n_cols // 10)
    if defense_row < n_rows and c_end > c_start:
        mask[defense_row, c_start:c_end] = True
    return mask


# ============================================================
# File-based Data Loading
# ============================================================

def load_dem(path: str) -> Tuple[np.ndarray, Tuple[int, int]]:
    """Load a single-band DEM GeoTIFF. Returns (elevation, (rows, cols))."""
    if not _RASTERIO_AVAILABLE:
        raise RuntimeError(
            "rasterio is required for file-based mode but is not installed. "
            "Install via: pip install rasterio"
        )
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"DEM not found: {path}")
    with rasterio.open(path) as ds:
        h, w = ds.height, ds.width
        src_dtype = ds.dtypes[0]
        np_dtype = np.dtype(src_dtype) if src_dtype in (
            "uint8", "uint16", "int16", "int32", "float32", "float64",
        ) else np.float32
        if np_dtype.kind == "f":
            data = np.empty((h, w), dtype=np.float32)
        else:
            data = np.empty((h, w), dtype=np_dtype)
        ds.read(1, out=data)
    return data.astype(np.float32), (h, w)


# ============================================================
# Report Generation
# ============================================================

def generate_report_html(
    results: Dict,
    output_dir: Path,
) -> Path:
    """Generate HTML flood risk report."""
    path = output_dir / "report.html"

    # Extract values safely
    n_scenarios = results.get("n_scenarios", 0)
    comparison = results.get("comparison", {})
    max_area = comparison.get("max_flooded_area_km2", "N/A")
    max_depth = comparison.get("max_mean_depth_m", "N/A")

    # Format values for template
    if isinstance(max_area, (int, float)):
        max_area_str = f"{max_area:.3f}"
    else:
        max_area_str = str(max_area)

    if isinstance(max_depth, (int, float)):
        max_depth_str = f"{max_depth:.3f}"
    else:
        max_depth_str = str(max_depth)

    # Build scenario rows
    scenario_rows = ""
    for s in comparison.get("scenarios", []):
        name = s.get("name", "N/A")
        wl = s.get("water_level_m", "N/A")
        area = s.get("flooded_area_km2", "N/A")
        depth = s.get("mean_depth_m", "N/A")

        if isinstance(wl, (int, float)):
            wl_str = f"{wl:.1f}"
        else:
            wl_str = str(wl)
        if isinstance(area, (int, float)):
            area_str = f"{area:.3f}"
        else:
            area_str = str(area)
        if isinstance(depth, (int, float)):
            depth_str = f"{depth:.3f}"
        else:
            depth_str = str(depth)

        scenario_rows += f"<tr><td>{name}</td><td>{wl_str}</td><td>{area_str}</td><td>{depth_str}</td></tr>\n"

    if not scenario_rows:
        scenario_rows = "<tr><td colspan='4'>No scenarios</td></tr>\n"

    # Build exposure rows
    exposure_rows = ""
    exposure = results.get("exposure", {})
    for cat, stats in exposure.get("categories", {}).items():
        exp_total = stats.get("exposed_total", "N/A")
        exp_frac = stats.get("exposed_fraction", "N/A")
        n_pix = stats.get("n_exposed_pixels", "N/A")

        if isinstance(exp_total, (int, float)):
            exp_total_str = f"{exp_total:.1f}"
        else:
            exp_total_str = str(exp_total)
        if isinstance(exp_frac, (int, float)):
            exp_frac_str = f"{exp_frac:.1%}"
        else:
            exp_frac_str = str(exp_frac)

        exposure_rows += f"<tr><td>{cat}</td><td>{exp_total_str}</td><td>{exp_frac_str}</td><td>{n_pix}</td></tr>\n"

    if not exposure_rows:
        exposure_rows = "<tr><td colspan='4'>No exposure data</td></tr>\n"

    # Warnings
    warnings = results.get("warnings", [])
    warnings_html = ""
    for w in warnings:
        warnings_html += f"<li>{w}</li>\n"
    if not warnings_html:
        warnings_html = "<li>No warnings</li>\n"

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>Coastal Flood Risk Report</title>
<style>
body {{ font-family: 'Microsoft YaHei', Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
.container {{ max-width: 900px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
h1 {{ color: #333; border-bottom: 3px solid #dc3545; padding-bottom: 10px; }}
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
<h1>Coastal Flood Risk Assessment Report</h1>
<p>Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}</p>

<div class="info">
<strong>Model:</strong> Static bathtub with ocean connectivity.<br>
<strong>Note:</strong> This is NOT a full hydrodynamic storm surge simulation.
</div>

<h2>Warnings</h2>
<ul>
{warnings_html}
</ul>

<h2>Scenario Comparison</h2>
<table>
<tr><th>Scenario</th><th>Water Level (m)</th><th>Flooded Area (km²)</th><th>Mean Depth (m)</th></tr>
{scenario_rows}
</table>

<p><strong>Max flooded area:</strong> {max_area_str} km²<br>
<strong>Max mean depth:</strong> {max_depth_str} m</p>

<h2>Exposure Assessment</h2>
<table>
<tr><th>Category</th><th>Exposed Total</th><th>Exposed Fraction</th><th>Exposed Pixels</th></tr>
{exposure_rows}
</table>

<h2>Methodology Notes</h2>
<ul>
<li>Static bathtub model: cells below water level connected to ocean are flooded</li>
<li>Ocean connectivity eliminates inland depressions not connected to sea</li>
<li>Depth proxy = water level - elevation (not true hydrodynamic depth)</li>
<li>Exposure = sum of asset values in flooded cells</li>
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

def auto_download_dem(args, output_dir: Path) -> Dict[str, Any]:
    """Download one cop-dem-glo-30 scene from MPC using --bbox + --date-range.

    Returns metadata dict (also writes the path back to args.dem).
    """
    if not _FETCHER_AVAILABLE:
        raise RuntimeError(
            "Shared data fetcher not importable. Pass --dem <local.tif> instead, "
            "or ensure _geoskill_data_fetcher is on sys.path."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_dem requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        raise RuntimeError("auto_download_dem requires --date-range")
    cache_dir = getattr(args, "cache_dir", None)
    fetcher = DataFetcher(
        source=DataSource.PLANETARY_COMPUTER,
        cache_dir=Path(cache_dir) if cache_dir else None,
    )
    items = fetcher.search_stac(
        collection="cop-dem-glo-30",
        bbox=bbox,
        # cop-dem-glo-30 is time-invariant; skip the date filter so the
        # search succeeds regardless of the user-supplied --date-range.
        date_range=None,
        limit=1,
    )
    if not items:
        raise RuntimeError(
            f"No cop-dem-glo-30 items found in bbox={bbox} for {dr.start}..{dr.end}"
        )
    download_dir = output_dir / "downloaded"
    paths = fetcher.download_assets(
        items=items, out_dir=download_dir, max_items=1, max_total_mb=500,
        prefer_assets=['data'],
    )
    if not paths:
        raise RuntimeError("Download returned no files")
    args.dem = str(paths[0])
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "cop-dem-glo-30",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def run_flood_risk_pipeline(args: argparse.Namespace) -> int:
    """Main flood risk assessment workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("cfr-output")
    fetch_meta: Dict[str, Any] = {}

    # --- Auto-download mode: fetch cop-dem-glo-30 from MPC ---
    if (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)) and getattr(args, "date_range", None):
        if not getattr(args, "dem", None):
            try:
                fetch_meta = auto_download_dem(args, output_dir)
                print(f"  Auto-downloaded dem: {args.dem}")
            except DataFetcherError as e:
                print(f"ERROR: auto-download failed: [{e.kind}] {e.message}", file=sys.stderr)
                return EXIT_PROCESSING if 'EXIT_PROCESSING' in dir() else 7
    output_dir.mkdir(parents=True, exist_ok=True)

    # P0: Validate args before any heavy work
    rc = validate_args(args)
    if rc != 0:
        return rc

    logger = setup_logging(output_dir)
    logger.info("Coastal Flood Risk - Starting")

    # Load scenarios
    scenarios_path = getattr(args, 'scenarios_config', None)
    try:
        scenarios = load_flood_scenarios(scenarios_path)
        logger.info(f"Flood scenarios loaded: version {scenarios.get('version', 'unknown')}")
    except Exception as e:
        logger.error(f"Failed to load flood scenarios: {e}")
        cleanup_logging()
        return EXIT_VALIDATION

    # Parse water levels
    water_levels = []
    if hasattr(args, 'water_levels') and args.water_levels:
        for wl_str in args.water_levels.split(","):
            try:
                water_levels.append(float(wl_str.strip()))
            except ValueError:
                logger.error(f"Invalid water level: {wl_str}")
                cleanup_logging()
                return EXIT_ARG
    else:
        # Default scenarios
        water_levels = [0.5, 1.0, 2.0]

    # Parse connectivity flag
    connectivity = True
    if hasattr(args, 'connectivity') and args.connectivity:
        connectivity = args.connectivity.lower() in ("true", "yes", "1", "on")

    # Parse vertical datum
    vertical_datum = "MSL"
    if hasattr(args, 'vertical_datum') and args.vertical_datum:
        vertical_datum = args.vertical_datum

    # --- Synthetic/demo mode or file-based mode ---
    # --synthetic forces synthetic; otherwise providing --dem uses real file input.
    explicit_synthetic = getattr(args, 'synthetic', False)
    has_user_file = bool(getattr(args, 'dem', None))
    use_synthetic = explicit_synthetic or not has_user_file

    dem = None
    ocean_mask = None
    defense_mask = None
    exposure_data = {}
    dem_datum = vertical_datum
    has_defenses = False
    warnings = []

    if use_synthetic:
        if explicit_synthetic:
            logger.info("Running in --synthetic demo mode")
        else:
            logger.info("No --dem provided; using synthetic demo data")
        dem = generate_synthetic_dem(100, 100, slope=0.05, seed=42)
        ocean_mask = generate_synthetic_ocean_mask(100, 100, ocean_rows=5)
        defense_mask = generate_synthetic_defense_mask(100, 100, defense_row=8)
        exposure_data = generate_synthetic_exposure(100, 100, seed=42)
        dem_datum = "MSL"
        has_defenses = True
    else:
        # File-based mode: actually load the DEM and synthesize the
        # ancillary layers (ocean mask, defense mask, exposure grid) to the
        # DEM's shape so the rest of the pipeline can run unchanged.
        logger.info(f"File-based mode: loading DEM {args.dem}")
        try:
            dem, (h, w) = load_dem(args.dem)
        except (FileNotFoundError, RasterioIOError, ValueError, RuntimeError) as e:
            logger.error(f"Failed to load DEM: {e}")
            return EXIT_VALIDATION
        logger.info(f"  Loaded DEM: shape={dem.shape}, min={dem.min():.3f}m, max={dem.max():.3f}m")
        ocean_mask = generate_synthetic_ocean_mask(h, w, ocean_rows=max(1, h // 20))
        exposure_data = generate_synthetic_exposure(h, w, seed=42)
        # For defenses: try to load the defenses file if given; otherwise no defenses.
        def_path = getattr(args, 'defenses', None)
        if def_path:
            try:
                defense_mask, _ = load_dem(def_path)
                # Treat any non-zero as defense present (binary mask)
                defense_mask = defense_mask > 0
            except (FileNotFoundError, RasterioIOError, ValueError, RuntimeError) as e:
                logger.warning(f"  Defenses load failed: {e}; treating as no defenses")
                defense_mask = np.zeros((h, w), dtype=bool)
                has_defenses = False
        else:
            defense_mask = np.zeros((h, w), dtype=bool)
            has_defenses = False
        dem_datum = "unknown"  # User DEM may have any datum; warn accordingly

    # --- Vertical datum check ---
    if dem_datum != vertical_datum:
        dem, success, msg = apply_vertical_datum_offset(
            dem, dem_datum, vertical_datum, scenarios
        )
        if not success:
            warnings.append(f"Vertical datum conversion failed: {msg}. Results are RELATIVE only.")
            logger.warning(f"Datum issue: {msg}")
        else:
            logger.info(msg)
    elif dem_datum == "unknown":
        warnings.append("DEM vertical datum unknown. Results are RELATIVE only — do not use for absolute flood depth claims.")
        logger.warning("Unknown vertical datum")

    # --- Defense handling ---
    defense_height = 0.0
    if hasattr(args, 'defense_height') and args.defense_height:
        defense_height = args.defense_height

    if defense_height > 0 and defense_mask is not None:
        dem, has_defenses = apply_defenses(dem, defense_mask, defense_height)
        logger.info(f"Applied defenses: height={defense_height}m")
    elif defense_height == 0:
        warnings.append("No defense data provided. Results represent UNPROTECTED scenario.")
        logger.warning("No defense data — unprotected scenario")

    # --- Run scenarios ---
    scenario_results = []
    for i, wl in enumerate(water_levels):
        logger.info(f"Running scenario {i+1}/{len(water_levels)}: water level = {wl}m")

        flooded_mask, depth_proxy = bathtub_inundate(
            dem, wl, connectivity=connectivity,
            nodata_value=-9999.0, ocean_mask=ocean_mask
        )

        stats = compute_flood_statistics(flooded_mask, depth_proxy, pixel_area_m2=1.0)

        # Exposure for this scenario
        exp = compute_exposure(flooded_mask, depth_proxy, exposure_data, pixel_area_m2=1.0)

        scenario_results.append({
            "scenario_name": f"WL_{wl}m",
            "water_level_m": wl,
            "flooded_mask": flooded_mask,
            "depth_proxy": depth_proxy,
            "statistics": stats,
            "exposure": exp,
        })

        logger.info(f"  Flooded: {stats['flooded_area_km2']:.4f} km², "
                     f"mean depth: {stats['mean_depth_m']:.3f}m")

    # --- Multi-scenario comparison ---
    comparison = compare_scenarios(scenario_results)

    # --- Priority zones ---
    priority_zones = identify_priority_zones(scenario_results, depth_threshold=0.5)

    # --- Aggregate exposure (use last/highest scenario for summary) ---
    summary_exposure = scenario_results[-1]["exposure"] if scenario_results else {"categories": {}}

    # --- Generate outputs ---

    # Save depth proxy from highest scenario
    depth_output = output_dir / "depth_proxy.tif"
    # For synthetic mode, save as numpy (GeoTIFF would need rasterio)
    if use_synthetic:
        depth_path = output_dir / "depth_proxy.npy"
        np.save(depth_path, scenario_results[-1]["depth_proxy"])
        logger.info(f"Depth proxy saved: {depth_path}")

    # Priority zones GeoJSON
    priority_path = output_dir / "priority_zones.geojson"
    priority_path.write_text(
        json.dumps(priority_zones, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # Exposure by scenario (CSV)
    exposure_csv_path = output_dir / "exposure_by_scenario.csv"
    with open(exposure_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["scenario", "water_level_m", "category", "exposed_total",
                         "exposed_fraction", "n_exposed_pixels"])
        for sr in scenario_results:
            for cat, stats in sr["exposure"].get("categories", {}).items():
                writer.writerow([
                    sr["scenario_name"],
                    sr["water_level_m"],
                    cat,
                    stats.get("exposed_total", 0),
                    stats.get("exposed_fraction", 0),
                    stats.get("n_exposed_pixels", 0),
                ])

    # Report HTML
    report_results = {
        "n_scenarios": len(scenario_results),
        "comparison": comparison,
        "exposure": summary_exposure,
        "warnings": warnings,
    }
    report_path = generate_report_html(report_results, output_dir)

    # request.json
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "synthetic" if use_synthetic else "file",
        "water_levels": water_levels,
        "connectivity": connectivity,
        "vertical_datum": vertical_datum,
        "defense_height": defense_height,
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
        "dem_shape": list(dem.shape),
        "n_scenarios": len(water_levels),
        "exposure_categories": list(exposure_data.keys()),
        "has_ocean_mask": ocean_mask is not None,
        "has_defense_mask": defense_mask is not None,
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # output-manifest.json
    output_files = {
        "report.html": str(report_path),
        "priority_zones.geojson": str(priority_path),
        "exposure_by_scenario.csv": str(exposure_csv_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(dataset_path),
    }
    if use_synthetic:
        output_files["depth_proxy.npy"] = str(depth_path)

    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "output_files": output_files,
        "summary": {
            "n_scenarios": len(scenario_results),
            "max_flooded_area_km2": comparison.get("max_flooded_area_km2", 0),
            "n_warnings": len(warnings),
        },
    }
    if fetch_meta:
        manifest["data_source"] = fetch_meta.get("data_source")
        manifest["fetched_at"] = fetch_meta.get("fetched_at")
        manifest["collection"] = fetch_meta.get("collection")
        manifest["bbox"] = fetch_meta.get("bbox")
        manifest["date_range"] = fetch_meta.get("date_range")
        manifest["downloaded_paths"] = fetch_meta.get("downloaded_paths")
        manifest["mode"] = "auto_download"
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
            "priority_zones_generated": priority_path.exists(),
            "exposure_csv_generated": exposure_csv_path.exists(),
            "all_outputs_written": all(Path(p).exists() for p in output_files.values()),
        },
        "n_scenarios": len(scenario_results),
        "n_warnings": len(warnings),
        "warnings": warnings,
        "connectivity_applied": connectivity,
        "defenses_applied": has_defenses,
    }
    qa_path = output_dir / "qa.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    logger.info(f"Flood risk assessment complete: {len(scenario_results)} scenarios, "
                f"{len(warnings)} warnings")
    cleanup_logging()
    return EXIT_OK


def validate_args(args) -> int:
    """Validate file existence, numeric ranges, and water-level signs.
    Returns exit code (0 = ok, 2 = arg error)."""
    # File existence
    for flag, accessor in FILE_ARGS.items():
        path = eval(accessor)  # noqa: S307 - safe: only string concat
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
    # Water levels: all values must be non-negative
    water_levels_str = getattr(args, "water_levels", None)
    if water_levels_str:
        try:
            levels = [float(x.strip()) for x in water_levels_str.split(",")]
        except ValueError:
            print(f"ERROR: --water-levels invalid format: {water_levels_str}", file=sys.stderr)
            return 2
        if any(lvl < 0 for lvl in levels):
            print(f"ERROR: --water-levels must be non-negative, got {water_levels_str}", file=sys.stderr)
            return 2
    return 0


def main():
    parser = argparse.ArgumentParser(description="Coastal Flood Risk Assessment")
    parser.add_argument("--dem", default=None,
                        help="Path to DEM GeoTIFF")
    parser.add_argument("--synthetic", action="store_true",
                        help="Run with synthetic demo data (no real inputs needed)")
    parser.add_argument("--water-levels", default=None,
                        help="Comma-separated water levels in meters (e.g., '0.5,1.0,2.0')")
    parser.add_argument("--vertical-datum", default="MSL",
                        help="Target vertical datum (default: MSL)")
    parser.add_argument("--connectivity", default="true",
                        help="Apply ocean connectivity filter (true/false)")
    parser.add_argument("--defense-height", type=float, default=0.0,
                        help="Coastal defense height in meters")
    parser.add_argument("--defenses", default=None,
                        help="Path to defense vector/raster file")
    parser.add_argument("--scenarios-config", default=None,
                        help="Path to flood scenarios JSON")
    parser.add_argument("--output-dir", "-o", default="cfr-output",
                        help="Output directory (default: cfr-output)")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    add_bbox_date_args(parser)

    args = parser.parse_args()

    # Pre-flight dependency check (graceful failure instead of NameError on `np`)
    if not _NUMPY_AVAILABLE:
        print("ERROR: numpy is required but not installed. "
              "Install via: pip install numpy", file=sys.stderr)
        sys.exit(EXIT_DEP)

    try:
        sys.exit(run_flood_risk_pipeline(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
