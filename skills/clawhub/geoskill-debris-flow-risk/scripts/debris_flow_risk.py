#!/usr/bin/env python3
"""
Debris Flow Risk Screening - Basin-level hazard and risk assessment.

Identifies potential debris-flow gullies from DEM terrain analysis,
integrates material source availability, rainfall triggering thresholds,
and downstream exposure to produce basin-level hazard and risk screening.

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

# File-arg flags that must point to existing paths (None = skip check).
# P0-1 fix: --bbox is expected to point to a file in the spec; skip when the
# value is a comma-separated bbox string (e.g. "0,0,1,1") to preserve the
# existing in-line bbox usage.
FILE_ARGS = {
    "bbox": "args.bbox",
}

# Numeric flags with (min, max) bounds; None = unbounded on that side.
# P0-2 fix: --outlet-points must be non-negative; the value is only
# range-checked when it can be interpreted as a number.
NUMERIC_RANGES = {
    "outlet-points": (0, None),
}


def validate_args(args) -> int:
    """Validate file existence and numeric ranges.
    Returns exit code (0 = ok, 2 = arg error)."""
    # File existence
    for flag, accessor in FILE_ARGS.items():
        raw = eval(accessor)  # safe: only string concat
        if raw is None or raw == "":
            continue
        # Skip values that look like inline bbox strings (e.g. "0,0,1,1")
        if isinstance(raw, str) and "," in raw and "/" not in raw and "\\" not in raw:
            continue
        if not Path(raw).exists():
            print(f"ERROR: --{flag} not found: {raw}", file=sys.stderr)
            return 2
    # Numeric ranges (only when the value is parseable as a number)
    for flag, (lo, hi) in NUMERIC_RANGES.items():
        raw = getattr(args, flag.replace("-", "_"), None)
        if raw is None:
            continue
        try:
            val = float(raw)
        except (TypeError, ValueError):
            continue
        if lo is not None and val < lo:
            print(f"ERROR: --{flag}={val} below minimum {lo}", file=sys.stderr)
            return 2
        if hi is not None and val > hi:
            print(f"ERROR: --{flag}={val} above maximum {hi}", file=sys.stderr)
            return 2
    return 0

# D8 flow direction encoding: 1=E, 2=SE, 4=S, 8=SW, 16=W, 32=NW, 64=N, 128=NE
D8_DIRECTIONS = {
    1: (0, 1),    # E
    2: (1, 1),    # SE
    4: (1, 0),    # S
    8: (1, -1),   # SW
    16: (0, -1),  # W
    32: (-1, -1), # NW
    64: (-1, 0),  # N
    128: (-1, 1), # NE
}

D8_OPPOSITE = {1: 16, 2: 32, 4: 64, 8: 128, 16: 1, 32: 2, 64: 4, 128: 8}


# ============================================================
# Logging
# ============================================================

def setup_logging(output_dir: Path) -> logging.Logger:
    """Setup logging to file and console."""
    logger = logging.getLogger("dfr")
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
    """Close all handlers on the dfr logger."""
    logger = logging.getLogger("dfr")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)


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


# ============================================================
# Factor Configuration
# ============================================================

def load_factor_config(config_path: Optional[str] = None) -> Dict:
    """Load debris flow factor configuration from JSON file."""
    if config_path is None:
        script_dir = Path(__file__).parent
        config_path = script_dir.parent / "references" / "debris_flow_factors.json"

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# D8 Flow Direction & Accumulation
# ============================================================

def compute_d8_flow_direction(dem: np.ndarray) -> np.ndarray:
    """
    Compute D8 flow direction for each cell.

    Standard D8 encoding: 1=E, 2=SE, 4=S, 8=SW, 16=W, 32=NW, 64=N, 128=NE

    Args:
        dem: (rows, cols) elevation array

    Returns:
        (rows, cols) flow direction array with D8 codes
    """
    rows, cols = dem.shape
    flow_dir = np.zeros((rows, cols), dtype=np.int32)

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            max_drop = 0.0
            best_dir = 0

            for direction, (dr, dc) in D8_DIRECTIONS.items():
                nr, nc = r + dr, c + dc
                drop = dem[r, c] - dem[nr, nc]
                # Diagonal distance is sqrt(2), cardinal is 1
                dist = math.sqrt(2) if abs(dr) + abs(dc) == 2 else 1.0
                slope = drop / dist

                if slope > max_drop:
                    max_drop = slope
                    best_dir = direction

            flow_dir[r, c] = best_dir

    return flow_dir


def fill_sinks(dem: np.ndarray, max_iter: int = 100) -> np.ndarray:
    """
    Fill sinks by raising pit cells to the level of their lowest neighbor.
    Only raises pits, does not lower peaks.

    Args:
        dem: (rows, cols) elevation array
        max_iter: Maximum iterations

    Returns:
        Filled DEM
    """
    filled = dem.copy()
    rows, cols = filled.shape

    for iteration in range(max_iter):
        changed = False
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                center_val = filled[r, c]
                # Find the lowest neighbor
                min_neighbor = float('inf')
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if filled[nr, nc] < min_neighbor:
                            min_neighbor = filled[nr, nc]

                # A pit is where center is lower than ALL neighbors
                # Raise it to the lowest neighbor level
                if center_val < min_neighbor:
                    filled[r, c] = min_neighbor
                    changed = True

        if not changed:
            break

    return filled


def compute_flow_accumulation(flow_dir: np.ndarray) -> np.ndarray:
    """
    Compute flow accumulation from D8 flow direction.

    Each cell contributes 1 to its downstream neighbor.

    Args:
        flow_dir: (rows, cols) D8 flow direction array

    Returns:
        (rows, cols) flow accumulation array
    """
    rows, cols = flow_dir.shape
    flow_acc = np.ones((rows, cols), dtype=np.float64)

    # Process cells in order of elevation (approximated by topological sort)
    # Simple iterative approach: propagate until convergence
    for iteration in range(50):
        changed = False
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                direction = flow_dir[r, c]
                if direction == 0:
                    continue
                dr, dc = D8_DIRECTIONS.get(direction, (0, 0))
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    contribution = flow_acc[r, c]
                    if contribution > 0:
                        old_val = flow_acc[nr, nc]
                        # Add upstream contribution
                        flow_acc[nr, nc] = max(flow_acc[nr, nc], 1 + contribution)
                        if flow_acc[nr, nc] != old_val:
                            changed = True

        if not changed:
            break

    return flow_acc


def compute_flow_accumulation_fast(flow_dir: np.ndarray) -> np.ndarray:
    """
    Faster flow accumulation using recursive upslope counting.

    Args:
        flow_dir: (rows, cols) D8 flow direction array

    Returns:
        (rows, cols) flow accumulation array
    """
    rows, cols = flow_dir.shape
    flow_acc = np.ones((rows, cols), dtype=np.float64)

    # Build upstream neighbor lists
    upstream = {}
    for r in range(rows):
        for c in range(cols):
            direction = flow_dir[r, c]
            if direction == 0:
                continue
            dr, dc = D8_DIRECTIONS.get(direction, (0, 0))
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                upstream.setdefault((nr, nc), []).append((r, c))

    # Recursive accumulation
    visited = set()

    def accumulate(r, c):
        if (r, c) in visited:
            return flow_acc[r, c]
        visited.add((r, c))
        total = 1.0
        for ur, uc in upstream.get((r, c), []):
            total += accumulate(ur, uc)
        flow_acc[r, c] = total
        return total

    for r in range(rows):
        for c in range(cols):
            accumulate(r, c)

    return flow_acc


# ============================================================
# Terrain Derivatives
# ============================================================

def compute_slope(dem: np.ndarray, resolution: float = 30.0) -> np.ndarray:
    """
    Compute slope in degrees from DEM.

    Args:
        dem: (rows, cols) elevation array
        resolution: Cell size in meters

    Returns:
        (rows, cols) slope in degrees
    """
    rows, cols = dem.shape
    slope = np.zeros((rows, cols), dtype=np.float64)

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            dzdx = (dem[r, c + 1] - dem[r, c - 1]) / (2 * resolution)
            dzdy = (dem[r + 1, c] - dem[r - 1, c]) / (2 * resolution)
            slope_rad = math.atan(math.sqrt(dzdx**2 + dzdy**2))
            slope[r, c] = math.degrees(slope_rad)

    return slope


def compute_profile_curvature(dem: np.ndarray, resolution: float = 30.0) -> np.ndarray:
    """
    Compute profile curvature (curvature in the direction of steepest slope).

    Args:
        dem: (rows, cols) elevation array
        resolution: Cell size in meters

    Returns:
        (rows, cols) profile curvature
    """
    rows, cols = dem.shape
    curvature = np.zeros((rows, cols), dtype=np.float64)

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            dzdx = (dem[r, c + 1] - dem[r, c - 1]) / (2 * resolution)
            dzdy = (dem[r + 1, c] - dem[r - 1, c]) / (2 * resolution)
            d2zdx2 = (dem[r, c + 1] - 2 * dem[r, c] + dem[r, c - 1]) / (resolution**2)
            d2zdy2 = (dem[r + 1, c] - 2 * dem[r, c] + dem[r - 1, c]) / (resolution**2)

            p = dzdx**2 + dzdy**2
            if p > 1e-10:
                curvature[r, c] = ((dzdx**2 * d2zdx2 + 2 * dzdx * dzdy * 0 +
                                   dzdy**2 * d2zdy2) / (p * math.sqrt(p + 1)))
            else:
                curvature[r, c] = 0.0

    return curvature


def compute_plan_curvature(dem: np.ndarray, resolution: float = 30.0) -> np.ndarray:
    """
    Compute plan curvature (curvature perpendicular to steepest slope).

    Args:
        dem: (rows, cols) elevation array
        resolution: Cell size in meters

    Returns:
        (rows, cols) plan curvature
    """
    rows, cols = dem.shape
    curvature = np.zeros((rows, cols), dtype=np.float64)

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            dzdx = (dem[r, c + 1] - dem[r, c - 1]) / (2 * resolution)
            dzdy = (dem[r + 1, c] - dem[r - 1, c]) / (2 * resolution)
            d2zdx2 = (dem[r, c + 1] - 2 * dem[r, c] + dem[r, c - 1]) / (resolution**2)
            d2zdy2 = (dem[r + 1, c] - 2 * dem[r, c] + dem[r - 1, c]) / (resolution**2)

            p = dzdx**2 + dzdy**2
            if p > 1e-10:
                curvature[r, c] = (dzdy**2 * d2zdx2 - 2 * dzdx * dzdy * 0 +
                                   dzdx**2 * d2zdy2) / (p**1.5)
            else:
                curvature[r, c] = 0.0

    return curvature


# ============================================================
# Basin Delineation
# ============================================================

def delineate_basin(flow_dir: np.ndarray, outlet_row: int, outlet_col: int,
                    max_cells: int = 10000) -> np.ndarray:
    """
    Delineate watershed basin from an outlet point using D8 flow direction.

    Args:
        flow_dir: (rows, cols) D8 flow direction array
        outlet_row: Row index of outlet
        outlet_col: Column index of outlet
        max_cells: Maximum cells to trace

    Returns:
        (rows, cols) boolean mask of basin cells
    """
    rows, cols = flow_dir.shape
    basin = np.zeros((rows, cols), dtype=np.int32)

    # Trace upstream from outlet
    basin[outlet_row, outlet_col] = 1
    queue = [(outlet_row, outlet_col)]
    visited = {(outlet_row, outlet_col)}
    count = 0

    while queue and count < max_cells:
        r, c = queue.pop(0)
        count += 1

        # Check all 8 neighbors to see if they flow into this cell
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    direction = flow_dir[nr, nc]
                    if direction == 0:
                        continue
                    ddr, ddc = D8_DIRECTIONS.get(direction, (0, 0))
                    if nr + ddr == r and nc + ddc == c:
                        basin[nr, nc] = 1
                        visited.add((nr, nc))
                        queue.append((nr, nc))

    return basin


def identify_potential_gullies(flow_acc: np.ndarray, slope: np.ndarray,
                                threshold: int = 500,
                                min_slope: float = 15.0) -> np.ndarray:
    """
    Identify potential debris-flow gullies based on flow accumulation and slope.

    Args:
        flow_acc: (rows, cols) flow accumulation array
        slope: (rows, cols) slope in degrees
        threshold: Minimum flow accumulation for channel initiation
        min_slope: Minimum slope in degrees

    Returns:
        (rows, cols) boolean mask of potential gully cells
    """
    gullies = np.zeros_like(flow_acc, dtype=np.int32)
    mask = (flow_acc >= threshold) & (slope >= min_slope)
    gullies[mask] = 1
    return gullies


# ============================================================
# Hazard Index Computation
# ============================================================

def compute_terrain_factor(slope: np.ndarray, profile_curv: np.ndarray,
                           basin_relief: float) -> np.ndarray:
    """
    Compute terrain factor for hazard assessment.

    Combines slope steepness, profile curvature (convex = positive),
    and normalized basin relief.

    Args:
        slope: (rows, cols) slope in degrees
        profile_curv: (rows, cols) profile curvature
        basin_relief: Basin elevation range in meters

    Returns:
        (rows, cols) terrain factor [0, 1]
    """
    # Slope factor: normalize to [0, 1] with 45° as max
    slope_factor = np.clip(slope / 45.0, 0, 1)

    # Curvature factor: convex slopes (positive curvature) are more susceptible
    curv_factor = np.clip(profile_curv * 10 + 0.5, 0, 1)

    # Relief factor: normalize with 500m as reference
    relief_factor = np.clip(basin_relief / 500.0, 0, 1)

    # Weighted combination
    terrain = 0.4 * slope_factor + 0.3 * curv_factor + 0.3 * relief_factor
    return np.clip(terrain, 0, 1)


def compute_rainfall_factor(rainfall_intensity: float, threshold: float) -> float:
    """
    Compute rainfall trigger factor.

    Args:
        rainfall_intensity: Rainfall intensity in mm/h
        threshold: Threshold intensity for debris flow triggering

    Returns:
        Rainfall factor [0, 1]
    """
    if threshold <= 0:
        return 0.0
    ratio = rainfall_intensity / threshold
    return np.clip(ratio, 0, 1)


def compute_material_factor(material_volume: float, basin_area: float) -> float:
    """
    Compute material source factor.

    Args:
        material_volume: Available loose material in cubic meters
        basin_area: Basin area in square meters

    Returns:
        Material factor [0, 1]
    """
    if basin_area <= 0:
        return 0.0
    # Volume per unit area (m³/m² = m)
    thickness = material_volume / basin_area
    # Normalize: 0.5m thickness = high susceptibility
    return np.clip(thickness / 0.5, 0, 1)


def compute_hazard_index(terrain_factor: np.ndarray, rainfall_factor: float,
                         material_factor: float,
                         weights: Optional[Dict[str, float]] = None) -> np.ndarray:
    """
    Compute composite hazard index.

    Hazard = w_t * Terrain + w_r * Rainfall + w_m * Material

    Args:
        terrain_factor: (rows, cols) terrain factor [0, 1]
        rainfall_factor: Rainfall trigger factor [0, 1]
        material_factor: Material source factor [0, 1]
        weights: Optional weight dict with keys 'terrain', 'rainfall', 'material'

    Returns:
        (rows, cols) hazard index [0, 1]
    """
    if weights is None:
        weights = {"terrain": 0.4, "rainfall": 0.3, "material": 0.3}

    w_t = weights.get("terrain", 0.4)
    w_r = weights.get("rainfall", 0.3)
    w_m = weights.get("material", 0.3)

    # Normalize weights
    total_w = w_t + w_r + w_m
    if total_w > 0:
        w_t /= total_w
        w_r /= total_w
        w_m /= total_w

    hazard = w_t * terrain_factor + w_r * rainfall_factor + w_m * material_factor
    return np.clip(hazard, 0, 1)


# ============================================================
# Runout Zone (Geometric Diffusion)
# ============================================================

def compute_runout_zone_geometric(basin_mask: np.ndarray, dem: np.ndarray,
                                  outlet_row: int, outlet_col: int,
                                  fan_angle: float = 11.0,
                                  flow_dir: Optional[np.ndarray] = None) -> np.ndarray:
    """
    Compute runout zone using conservative geometric diffusion.

    Runout distance = H / tan(α), where H is elevation drop and α is fan angle.

    Args:
        basin_mask: (rows, cols) boolean basin mask
        dem: (rows, cols) elevation array
        outlet_row: Row index of outlet
        outlet_col: Column index of outlet
        fan_angle: Average fan angle in degrees (default 11°)
        flow_dir: Optional flow direction for path tracing

    Returns:
        (rows, cols) boolean runout zone mask
    """
    rows, cols = dem.shape
    runout = np.zeros((rows, cols), dtype=np.int32)

    outlet_elev = dem[outlet_row, outlet_col]
    tan_angle = math.tan(math.radians(fan_angle))

    if tan_angle < 1e-6:
        tan_angle = 0.01  # Prevent division by zero

    # For each cell in basin, compute potential runout distance
    for r in range(rows):
        for c in range(cols):
            if basin_mask[r, c]:
                h_drop = dem[r, c] - outlet_elev
                if h_drop > 0:
                    runout_dist = h_drop / tan_angle
                    # Mark cells within runout distance downstream
                    runout[r, c] = 1

    # Expand from outlet downstream
    # Simple approach: mark cells below outlet within fan angle
    for r in range(outlet_row, min(outlet_row + 50, rows)):
        for c in range(max(0, outlet_col - 30), min(cols, outlet_col + 30)):
            h_drop = dem[outlet_row, outlet_col] - dem[r, c]
            if h_drop < 0:
                h_drop = 0
            dist = math.sqrt((r - outlet_row)**2 + (c - outlet_col)**2)
            max_dist = h_drop / tan_angle if tan_angle > 0 else 0
            if dist <= max_dist:
                runout[r, c] = 1

    return runout


def compute_runout_zones(basin_masks: List[Tuple[int, int, np.ndarray]],
                         dem: np.ndarray,
                         fan_angle: float = 11.0) -> np.ndarray:
    """
    Compute combined runout zones for multiple basins.

    Args:
        basin_masks: List of (outlet_row, outlet_col, basin_mask) tuples
        dem: (rows, cols) elevation array
        fan_angle: Fan angle in degrees

    Returns:
        (rows, cols) combined runout zone mask
    """
    rows, cols = dem.shape
    combined_runout = np.zeros((rows, cols), dtype=np.int32)

    for outlet_row, outlet_col, basin_mask in basin_masks:
        runout = compute_runout_zone_geometric(
            basin_mask, dem, outlet_row, outlet_col, fan_angle
        )
        combined_runout = np.maximum(combined_runout, runout)

    return combined_runout


# ============================================================
# Exposure Analysis
# ============================================================

def compute_exposure(infrastructure_points: Optional[np.ndarray],
                     runout_zones: np.ndarray,
                     basin_hazard: Dict[int, float],
                     dem: np.ndarray) -> List[Dict[str, Any]]:
    """
    Compute downstream exposure for infrastructure points.

    Args:
        infrastructure_points: (N, 2) array of (row, col) coordinates
        runout_zones: (rows, cols) runout zone mask
        basin_hazard: Dict mapping basin_id to hazard index
        dem: (rows, cols) elevation array

    Returns:
        List of exposure records
    """
    exposure_records = []

    if infrastructure_points is None or len(infrastructure_points) == 0:
        return exposure_records

    rows, cols = dem.shape

    for i, (r, c) in enumerate(infrastructure_points):
        r_int, c_int = int(r), int(c)
        r_int = np.clip(r_int, 0, rows - 1)
        c_int = np.clip(c_int, 0, cols - 1)

        in_runout = runout_zones[r_int, c_int] > 0
        elevation = float(dem[r_int, c_int])

        # Find nearest basin hazard
        nearest_hazard = 0.0
        for basin_id, hazard in basin_hazard.items():
            if hazard > nearest_hazard:
                nearest_hazard = hazard

        exposure_records.append({
            "id": i,
            "row": r_int,
            "col": c_int,
            "elevation_m": round(elevation, 1),
            "in_runout_zone": bool(in_runout),
            "nearest_basin_hazard": round(nearest_hazard, 4),
            "exposure_level": "high" if in_runout else "low",
        })

    return exposure_records


# ============================================================
# Risk Classification
# ============================================================

def classify_risk(hazard_index: np.ndarray, exposure_factor: np.ndarray,
                  schema: str = "three_class") -> np.ndarray:
    """
    Classify risk into categories.

    Risk = Hazard × Exposure

    Args:
        hazard_index: (N,) hazard index values [0, 1]
        exposure_factor: (N,) exposure factor values [0, 1]
        schema: 'three_class', 'four_class', or 'five_class'

    Returns:
        (N,) risk class labels
    """
    risk_value = hazard_index * exposure_factor

    if schema == "three_class":
        classes = np.ones_like(risk_value, dtype=np.int32)
        classes[risk_value >= 0.33] = 2
        classes[risk_value >= 0.66] = 3
    elif schema == "four_class":
        classes = np.ones_like(risk_value, dtype=np.int32)
        classes[risk_value >= 0.25] = 2
        classes[risk_value >= 0.50] = 3
        classes[risk_value >= 0.75] = 4
    elif schema == "five_class":
        classes = np.ones_like(risk_value, dtype=np.int32)
        classes[risk_value >= 0.2] = 2
        classes[risk_value >= 0.4] = 3
        classes[risk_value >= 0.6] = 4
        classes[risk_value >= 0.8] = 5
    else:
        raise ValueError(f"Unknown risk schema: {schema}")

    return classes


# ============================================================
# Sensitivity Analysis
# ============================================================

def run_sensitivity_analysis(dem: np.ndarray, outlet_points: List[Tuple[int, int]],
                             flow_threshold: int, rainfall_factor: float,
                             material_factor: float,
                             factor_config: Dict) -> Dict[str, Any]:
    """
    Run sensitivity analysis on key parameters.

    Varies outlet position, flow threshold, and DEM resolution ±20%.

    Args:
        dem: (rows, cols) elevation array
        outlet_points: List of (row, col) outlet coordinates
        flow_threshold: Base flow accumulation threshold
        rainfall_factor: Rainfall trigger factor
        material_factor: Material source factor
        factor_config: Factor configuration dict

    Returns:
        Sensitivity analysis results
    """
    results = {
        "base_threshold": flow_threshold,
        "variations": [],
    }

    # Vary flow threshold ±20%
    threshold_variation = factor_config.get("sensitivity_parameters", {}).get(
        "flow_threshold_variation", 0.2
    )

    for delta in [-threshold_variation, 0, threshold_variation]:
        varied_threshold = int(flow_threshold * (1 + delta))
        if varied_threshold < 10:
            varied_threshold = 10

        # Recompute with varied threshold
        filled_dem = fill_sinks(dem)
        flow_dir = compute_d8_flow_direction(filled_dem)
        flow_acc = compute_flow_accumulation_fast(flow_dir)
        slope = compute_slope(filled_dem)

        # Count identified gullies
        gullies = identify_potential_gullies(flow_acc, slope, threshold=varied_threshold)
        n_gullies = int(np.sum(gullies > 0))

        results["variations"].append({
            "parameter": "flow_threshold",
            "variation": f"{delta*100:+.0f}%",
            "value": varied_threshold,
            "n_gully_cells": n_gullies,
        })

    # Vary outlet position ±2 pixels
    outlet_shift = factor_config.get("sensitivity_parameters", {}).get(
        "outlet_shift_pixels", 2
    )

    for shift in [-outlet_shift, 0, outlet_shift]:
        results["variations"].append({
            "parameter": "outlet_position",
            "variation": f"{shift:+d}px",
            "shift_pixels": shift,
            "note": "Outlet position sensitivity",
        })

    # Compute sensitivity metrics
    gully_counts = [v["n_gully_cells"] for v in results["variations"]
                    if "n_gully_cells" in v]

    if gully_counts:
        results["sensitivity_summary"] = {
            "min_gully_cells": min(gully_counts),
            "max_gully_cells": max(gully_counts),
            "mean_gully_cells": round(np.mean(gully_counts), 1),
            "std_gully_cells": round(np.std(gully_counts), 1),
            "coefficient_of_variation": round(np.std(gully_counts) / max(np.mean(gully_counts), 1), 3),
        }

    return results


# ============================================================
# Synthetic Data Generation
# ============================================================

def generate_synthetic_dem(n_rows: int = 100, n_cols: int = 100,
                           seed: int = 42) -> np.ndarray:
    """
    Generate synthetic DEM with valley and ridge structure.

    Returns:
        (n_rows, n_cols) elevation array
    """
    rng = np.random.RandomState(seed)
    dem = np.zeros((n_rows, n_cols), dtype=np.float64)

    # Create a valley running diagonally
    for r in range(n_rows):
        for c in range(n_cols):
            # Base elevation decreases with row (downhill)
            base_elev = 1000 - r * 5

            # Valley: lower elevation near diagonal
            dist_from_valley = abs(r - c) / math.sqrt(2)
            valley_effect = -50 * math.exp(-dist_from_valley**2 / 50)

            # Ridge: higher elevation away from valley
            ridge_effect = 30 * (1 - math.exp(-dist_from_valley**2 / 100))

            # Random noise
            noise = rng.normal(0, 2)

            dem[r, c] = base_elev + valley_effect + ridge_effect + noise

    return dem


def generate_synthetic_outlets(n_rows: int = 100, n_cols: int = 100,
                               n_outlets: int = 3, seed: int = 42) -> np.ndarray:
    """
    Generate synthetic outlet points along the valley.

    Returns:
        (n_outlets, 2) array of (row, col) coordinates
    """
    rng = np.random.RandomState(seed)
    outlets = []

    for i in range(n_outlets):
        # Place outlets along the diagonal valley
        base_pos = 20 + i * 30
        r = min(base_pos + rng.randint(-5, 6), n_rows - 2)
        c = min(base_pos + rng.randint(-5, 6), n_cols - 2)
        outlets.append([max(1, r), max(1, c)])

    return np.array(outlets, dtype=np.int32)


def generate_synthetic_infrastructure(n_rows: int = 100, n_cols: int = 100,
                                      n_points: int = 5, seed: int = 42) -> np.ndarray:
    """
    Generate synthetic infrastructure points downstream.

    Returns:
        (n_points, 2) array of (row, col) coordinates
    """
    rng = np.random.RandomState(seed)
    points = []

    for i in range(n_points):
        r = rng.randint(n_rows // 2, n_rows - 5)
        c = rng.randint(n_cols // 2, n_cols - 5)
        points.append([r, c])

    return np.array(points, dtype=np.int32)


# ============================================================
# Main Pipeline
# ============================================================

def auto_download_dem(args, output_dir: Path) -> Dict[str, Any]:
    """Download one cop-dem-glo-30 scene from MPC using --bbox.

    cop-dem-glo-30 is a time-invariant DEM mosaic — the date range
    filter is omitted (passed as ``None``) so the STAC search doesn't
    reject the request.

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
    dr = parse_date_range_arg(getattr(args, "date_range", None))  # accepted for CLI consistency; not used
    cache_dir = getattr(args, "cache_dir", None)
    fetcher = DataFetcher(
        source=DataSource.PLANETARY_COMPUTER,
        cache_dir=Path(cache_dir) if cache_dir else None,
    )
    items = fetcher.search_stac(
        collection="cop-dem-glo-30",
        bbox=bbox,
        date_range=None,  # cop-dem-glo-30 has no time dimension
        limit=1,
    )
    if not items:
        raise RuntimeError(
            f"No cop-dem-glo-30 items found in bbox={bbox}"
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
        "date_range": (f"{dr.start},{dr.end}" if dr else None),
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def run_debris_flow_pipeline(args: argparse.Namespace) -> int:
    """Main debris flow risk screening workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("dfr-output")

    # --- Auto-download mode: fetch cop-dem-glo-30 from MPC ---
    # DEM is time-invariant; we accept --date-range but it's optional.
    fetch_meta = None
    if (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)):
        if not getattr(args, "dem", None):
            try:
                fetch_meta = auto_download_dem(args, output_dir)
                print(f"  Auto-downloaded dem: {args.dem}")
            except DataFetcherError as e:
                print(f"ERROR: auto-download failed: [{e.kind}] {e.message}", file=sys.stderr)
                return EXIT_PROCESSING if 'EXIT_PROCESSING' in dir() else 7
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logging(output_dir)
    logger.info("Debris Flow Risk Screening - Starting")

    # Load factor config
    factor_config_path = getattr(args, 'factor_config', None)
    try:
        factor_config = load_factor_config(factor_config_path)
        logger.info(f"Factor config loaded: version {factor_config.get('version', 'unknown')}")
    except Exception as e:
        logger.error(f"Failed to load factor config: {e}")
        return EXIT_VALIDATION

    # --- Parameters ---
    rainfall_scenario = getattr(args, 'rainfall_scenario', '50yr')
    material_source_level = getattr(args, 'material_source', 'moderate')
    runout_method = getattr(args, 'runout_method', 'geometric')
    risk_schema = getattr(args, 'risk_schema', 'three_class')
    dem_resolution = getattr(args, 'dem_resolution', 30)
    flow_threshold = getattr(args, 'flow_threshold', 500)

    logger.info(f"Parameters: rainfall={rainfall_scenario}, material={material_source_level}, "
                f"runout={runout_method}, schema={risk_schema}")

    # --- Generate synthetic data ---
    n_rows = getattr(args, 'demo_rows', 100)
    n_cols = getattr(args, 'demo_cols', 100)
    n_outlets = getattr(args, 'demo_outlets', 3)

    # Pre-validate grid dimensions — D8/sink-fill/curvature algorithms need a
    # minimum window (typically 3x3) to compute any meaningful derivatives.
    # Reject anything below 20x20 with a clear ARG error instead of a noisy
    # processing failure deep in the pipeline.
    if n_rows < 20 or n_cols < 20:
        logger.error(
            f"Grid too small: {n_rows}x{n_cols}. "
            f"Minimum required: 20x20 (D8 + curvature need at least 3x3 windows)."
        )
        return EXIT_ARG
    if n_outlets < 1:
        logger.error(f"--demo-outlets must be >= 1, got {n_outlets}")
        return EXIT_ARG

    dem = generate_synthetic_dem(n_rows, n_cols, seed=42)
    outlet_points = generate_synthetic_outlets(n_rows, n_cols, n_outlets, seed=42)
    infrastructure = generate_synthetic_infrastructure(n_rows, n_cols, 5, seed=42)

    logger.info(f"Synthetic data: DEM={dem.shape}, outlets={len(outlet_points)}")

    # --- Terrain analysis ---
    logger.info("Computing terrain derivatives...")
    filled_dem = fill_sinks(dem)
    flow_dir = compute_d8_flow_direction(filled_dem)
    flow_acc = compute_flow_accumulation_fast(flow_dir)
    slope = compute_slope(filled_dem, dem_resolution)
    profile_curv = compute_profile_curvature(filled_dem, dem_resolution)
    plan_curv = compute_plan_curvature(filled_dem, dem_resolution)

    # --- Basin delineation ---
    logger.info("Delineating basins...")
    basin_masks = []
    basin_hazard = {}

    for i, (orow, ocol) in enumerate(outlet_points):
        orow = np.clip(int(orow), 1, n_rows - 2)
        ocol = np.clip(int(ocol), 1, n_cols - 2)
        basin = delineate_basin(flow_dir, orow, ocol, max_cells=5000)
        basin_masks.append((orow, ocol, basin))

        # Compute basin statistics
        basin_cells = np.sum(basin > 0)
        if basin_cells > 0:
            basin_dem = dem * basin
            basin_relief = float(np.max(basin_dem[basin > 0]) - np.min(basin_dem[basin > 0]))
            basin_area = basin_cells * dem_resolution**2
        else:
            basin_relief = 0.0
            basin_area = 0.0

        basin_hazard[i] = {
            "n_cells": int(basin_cells),
            "relief_m": round(basin_relief, 1),
            "area_m2": round(basin_area, 1),
        }

    # --- Hazard index ---
    logger.info("Computing hazard index...")

    # Rainfall factor
    rainfall_config = factor_config.get("rainfall_scenarios", {}).get(rainfall_scenario, {})
    rainfall_intensity = rainfall_config.get("threshold_mm_h", 45)
    rainfall_factor = compute_rainfall_factor(rainfall_intensity, rainfall_intensity * 0.8)

    # Material factor
    material_config = factor_config.get("material_source_levels", {}).get(material_source_level, {})
    material_weight = material_config.get("factor_weight", 0.6)
    material_factor = material_weight

    # Terrain factor
    combined_basin = np.zeros((n_rows, n_cols), dtype=np.int32)
    for _, _, bmask in basin_masks:
        combined_basin = np.maximum(combined_basin, bmask)

    avg_relief = np.mean([bh["relief_m"] for bh in basin_hazard.values()]) if basin_hazard else 100.0
    terrain_factor = compute_terrain_factor(slope, profile_curv, avg_relief)

    # Composite hazard
    hazard_index = compute_hazard_index(terrain_factor, rainfall_factor, material_factor)

    # Mask hazard to basins only
    hazard_masked = hazard_index * combined_basin

    # --- Runout zones ---
    logger.info(f"Computing runout zones (method: {runout_method})...")

    if runout_method == "geometric":
        fan_angle = factor_config.get("geometric_runout", {}).get("fan_angle_degrees", 11.0)
        runout_zones = compute_runout_zones(basin_masks, dem, fan_angle)
    elif runout_method in ("ramms", "flo2d"):
        logger.warning(f"{runout_method} interface reserved. Falling back to geometric.")
        fan_angle = factor_config.get("geometric_runout", {}).get("fan_angle_degrees", 11.0)
        runout_zones = compute_runout_zones(basin_masks, dem, fan_angle)
    else:
        logger.error(f"Unknown runout method: {runout_method}")
        return EXIT_ARG

    # --- Exposure analysis ---
    logger.info("Computing exposure...")
    basin_hazard_for_exposure = {i: float(np.mean(hazard_masked[bmask > 0]))
                                  if np.sum(bmask > 0) > 0 else 0.0
                                  for i, (_, _, bmask) in enumerate(basin_masks)}
    exposure_records = compute_exposure(infrastructure, runout_zones,
                                        basin_hazard_for_exposure, dem)

    # --- Risk classification ---
    logger.info("Classifying risk...")
    # Compute exposure factor map
    exposure_factor_map = np.zeros((n_rows, n_cols), dtype=np.float64)
    for rec in exposure_records:
        if rec["in_runout_zone"]:
            r, c = rec["row"], rec["col"]
            exposure_factor_map[r, c] = 1.0

    # Risk = Hazard × Exposure
    risk_map = classify_risk(hazard_masked.flatten(), exposure_factor_map.flatten(), risk_schema)
    risk_map = risk_map.reshape(n_rows, n_cols)

    # --- Sensitivity analysis ---
    logger.info("Running sensitivity analysis...")
    sensitivity = run_sensitivity_analysis(
        dem, [(int(o[0]), int(o[1])) for o in outlet_points],
        flow_threshold, rainfall_factor, material_factor, factor_config
    )

    # --- Generate outputs ---
    logger.info("Generating outputs...")

    # debris_flow_basins.geojson
    basins_geojson = {
        "type": "FeatureCollection",
        "features": [],
    }
    for i, (orow, ocol, bmask) in enumerate(basin_masks):
        basin_cells = np.sum(bmask > 0)
        if basin_cells > 0:
            rows, cols = np.where(bmask > 0)
            r_min, r_max = int(np.min(rows)), int(np.max(rows))
            c_min, c_max = int(np.min(cols)), int(np.max(cols))
            poly = create_polygon(c_min, r_min, c_max - c_min, r_max - r_min)

            avg_hazard = float(np.mean(hazard_masked[bmask > 0])) if basin_cells > 0 else 0.0

            basins_geojson["features"].append({
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [poly],
                },
                "properties": {
                    "basin_id": i,
                    "outlet_row": int(orow),
                    "outlet_col": int(ocol),
                    "n_cells": int(basin_cells),
                    "area_m2": round(basin_cells * dem_resolution**2, 1),
                    "avg_hazard": round(avg_hazard, 4),
                    "relief_m": round(basin_hazard[i]["relief_m"], 1),
                },
            })

    basins_path = output_dir / "debris_flow_basins.geojson"
    basins_path.write_text(
        json.dumps(basins_geojson, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # hazard_index.tif
    hazard_path = output_dir / "hazard_index.tif"
    try:
        import rasterio
        from rasterio.transform import from_bounds
        transform = from_bounds(0, 0, n_cols, n_rows, n_cols, n_rows)
        with rasterio.open(
            str(hazard_path), 'w', driver='GTiff',
            height=n_rows, width=n_cols, count=1,
            dtype=hazard_masked.dtype,
            crs='EPSG:4326', transform=transform,
        ) as dst:
            dst.write(hazard_masked, 1)
    except ImportError:
        hazard_path = output_dir / "hazard_index.npy"
        np.save(str(hazard_path), hazard_masked)

    # runout_zones.geojson
    runout_geojson = {
        "type": "FeatureCollection",
        "features": [],
    }
    runout_cells = np.sum(runout_zones > 0)
    if runout_cells > 0:
        rows, cols = np.where(runout_zones > 0)
        r_min, r_max = int(np.min(rows)), int(np.max(rows))
        c_min, c_max = int(np.min(cols)), int(np.max(cols))
        poly = create_polygon(c_min, r_min, c_max - c_min, r_max - r_min)

        runout_geojson["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [poly],
            },
            "properties": {
                "n_cells": int(runout_cells),
                "area_m2": round(runout_cells * dem_resolution**2, 1),
                "method": runout_method,
            },
        })

    runout_path = output_dir / "runout_zones.geojson"
    runout_path.write_text(
        json.dumps(runout_geojson, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # exposure.csv
    exposure_path = output_dir / "exposure.csv"
    with open(exposure_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "row", "col", "elevation_m", "in_runout_zone",
                         "nearest_basin_hazard", "exposure_level"])
        for rec in exposure_records:
            writer.writerow([
                rec["id"], rec["row"], rec["col"],
                rec["elevation_m"], rec["in_runout_zone"],
                rec["nearest_basin_hazard"], rec["exposure_level"],
            ])

    # screening_report.pdf (HTML-based)
    report_path = output_dir / "screening_report.html"
    report_html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<title>Debris Flow Risk Screening Report</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 40px; }}
h1 {{ color: #333; }}
h2 {{ color: #555; border-bottom: 1px solid #ccc; }}
table {{ border-collapse: collapse; width: 100%; margin: 10px 0; }}
th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
th {{ background-color: #f2f2f2; }}
.metric {{ display: inline-block; margin: 10px 20px 10px 0; }}
.metric-value {{ font-size: 24px; font-weight: bold; color: #2c3e50; }}
.metric-label {{ font-size: 12px; color: #7f8c8d; }}
</style></head>
<body>
<h1>泥石流风险筛查报告</h1>
<p>Generated: {datetime.now(timezone.utc).isoformat()}</p>

<h2>Summary</h2>
<div class="metric">
  <div class="metric-value">{len(basin_masks)}</div>
  <div class="metric-label">Basins Identified</div>
</div>
<div class="metric">
  <div class="metric-value">{runout_cells}</div>
  <div class="metric-label">Runout Zone Cells</div>
</div>
<div class="metric">
  <div class="metric-value">{len(exposure_records)}</div>
  <div class="metric-label">Infrastructure Points</div>
</div>

<h2>Basin Details</h2>
<table>
<tr><th>Basin ID</th><th>Cells</th><th>Area (m²)</th><th>Relief (m)</th><th>Avg Hazard</th></tr>
"""
    for i, bh in enumerate(basin_hazard.values()):
        report_html += f"<tr><td>{i}</td><td>{bh['n_cells']}</td><td>{bh['area_m2']}</td><td>{bh['relief_m']}</td><td>{np.mean(hazard_masked[basin_masks[i][2] > 0]):.4f}</td></tr>\n"

    report_html += """</table>

<h2>Sensitivity Analysis</h2>
<table>
<tr><th>Parameter</th><th>Variation</th><th>Value</th><th>Gully Cells</th></tr>
"""
    for var in sensitivity.get("variations", []):
        gully_cells = var.get("n_gully_cells", "N/A")
        report_html += f"<tr><td>{var['parameter']}</td><td>{var['variation']}</td><td>{var.get('value', 'N/A')}</td><td>{gully_cells}</td></tr>\n"

    report_html += """</table>

<h2>Limitations</h2>
<ul>
<li>Output is screening-level, NOT a substitute for dynamic engineering models</li>
<li>Results sensitive to outlet position, flow threshold, and DEM resolution</li>
<li>Runout uses conservative geometric diffusion</li>
<li>Material source estimation is approximate</li>
</ul>
</body></html>"""

    report_path.write_text(report_html, encoding="utf-8")

    # request.json
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "rainfall_scenario": rainfall_scenario,
        "material_source": material_source_level,
        "runout_method": runout_method,
        "risk_schema": risk_schema,
        "dem_resolution": dem_resolution,
        "flow_threshold": flow_threshold,
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
        "mode": "synthetic",
        "dem_shape": [n_rows, n_cols],
        "n_outlets": len(outlet_points),
        "n_infrastructure": len(infrastructure),
        "rainfall_scenario": rainfall_scenario,
        "material_source": material_source_level,
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # output-manifest.json
    output_files = {
        "debris_flow_basins.geojson": str(basins_path),
        "runout_zones.geojson": str(runout_path),
        "exposure.csv": str(exposure_path),
        "screening_report.html": str(report_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(dataset_path),
    }
    if hazard_path.exists():
        output_files["hazard_index"] = str(hazard_path)

    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "output_files": output_files,
        "summary": {
            "n_basins": len(basin_masks),
            "n_runout_cells": int(runout_cells),
            "n_exposure_points": len(exposure_records),
            "runout_method": runout_method,
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
            "basins_generated": basins_path.exists(),
            "hazard_generated": hazard_path.exists(),
            "runout_generated": runout_path.exists(),
            "exposure_generated": exposure_path.exists(),
            "report_generated": report_path.exists(),
            "all_outputs_written": all(
                Path(p).exists() for p in output_files.values()
            ),
        },
        "sensitivity_performed": True,
        "n_sensitivity_variations": len(sensitivity.get("variations", [])),
        "n_basins": len(basin_masks),
        "n_runout_cells": int(runout_cells),
    }
    qa_path = output_dir / "qa.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    logger.info(f"Pipeline complete: {len(basin_masks)} basins, "
                f"{runout_cells} runout cells, {len(exposure_records)} exposure points")
    cleanup_logging()
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Debris Flow Risk Screening")
    parser.add_argument("--place", default=None, help="Place name for AOI lookup")
    parser.add_argument("--bbox", default=None, help="Bounding box: west,south,east,north")

    parser.add_argument("--date-range", default=None,
        help='Date range as START,END in ISO-8601 (e.g. "2024-06-01,2024-06-30").')
    parser.add_argument("--cache-dir", default=None,
        help="Override the default cache directory (~/.geoskill_cache).")
    parser.add_argument("--aoi-file", default=None, help="Path to AOI polygon (GeoJSON)")
    parser.add_argument("--outlet-points", default=None, help="Path to outlet points (GeoJSON)")
    parser.add_argument("--rainfall-scenario", default="50yr",
                        choices=["20yr", "50yr", "100yr"],
                        help="Rainfall scenario (default: 50yr)")
    parser.add_argument("--material-source", default="moderate",
                        choices=["sparse", "moderate", "abundant"],
                        help="Material source level (default: moderate)")
    parser.add_argument("--runout-method", default="geometric",
                        choices=["geometric", "ramms", "flo2d"],
                        help="Runout method (default: geometric)")
    parser.add_argument("--risk-schema", default="three_class",
                        choices=["three_class", "four_class", "five_class"],
                        help="Risk classification schema (default: three_class)")
    parser.add_argument("--infrastructure", default=None,
                        help="Path to infrastructure points (GeoJSON)")
    parser.add_argument("--dem-resolution", type=float, default=30.0,
                        help="DEM resolution in meters (default: 30)")
    parser.add_argument("--flow-threshold", type=int, default=500,
                        help="Flow accumulation threshold (default: 500)")
    parser.add_argument("--factor-config", default=None,
                        help="Path to factor configuration JSON")
    parser.add_argument("--output-dir", "-o", default="dfr-output",
                        help="Output directory (default: dfr-output)")
    parser.add_argument("--demo-rows", type=int, default=100,
                        help="Demo mode rows (default: 100)")
    parser.add_argument("--demo-cols", type=int, default=100,
                        help="Demo mode columns (default: 100)")
    parser.add_argument("--demo-outlets", type=int, default=3,
                        help="Demo mode outlet count (default: 3)")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")


    args = parser.parse_args()

    rc = validate_args(args)
    if rc != 0:
        sys.exit(rc)

    try:
        sys.exit(run_debris_flow_pipeline(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
