#!/usr/bin/env python3
"""
Tailings Dam Risk - Remote sensing change and risk screening for tailings dams.

Screens tailings dam bodies, reservoir areas, catchments, and downstream exposure.
Produces patrol priorities based on hazard, exposure, and evidence.

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

# Shared data-download library (Microsoft Planetary Computer, NASA POWER, OSM)
# Try pip-installed package first; fall back to local copy in repo root.
try:
    import _geoskill_data_fetcher  # noqa: F401
    from _geoskill_data_fetcher import (  # noqa: E402
        BBox, DataFetcher, DataSource, DateRange,
        add_bbox_date_args, parse_bbox_arg, parse_date_range_arg,
    )
    _HAS_FETCHER = True
except Exception:  # pragma: no cover - fallback when shared lib unavailable
    _HAS_FETCHER = False
    DataFetcher = None  # type: ignore
    DataSource = None  # type: ignore
    BBox = None  # type: ignore
    DateRange = None  # type: ignore
    add_bbox_date_args = None  # type: ignore
    parse_bbox_arg = None  # type: ignore
    parse_date_range_arg = None  # type: ignore

def _try_auto_download(args, output_dir: Path) -> Dict[str, Any]:
    """Auto-download DEM (cop-dem-glo-30) and Sentinel-2 water-mask snapshots."""
    if not _HAS_FETCHER:
        return {}
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        return {}

    needs_dem = not getattr(args, "dem_file", None) or not Path(args.dem_file).exists()
    needs_water = not getattr(args, "water_masks", None)
    if not needs_dem and not needs_water:
        return {}

    metadata: Dict[str, Any] = {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "bbox": bbox.to_list(),
    }
    down_dir = output_dir / "downloaded"
    down_dir.mkdir(parents=True, exist_ok=True)

    dr = parse_date_range_arg(getattr(args, "date_range", None)) or DateRange(
        "2023-06-01", "2023-09-30"
    )

    # 1) DEM (cop-dem-glo-30) — single static tile
    if needs_dem:
        try:
            mpc_fetcher = DataFetcher(source=DataSource.PLANETARY_COMPUTER)
            items = mpc_fetcher.search_stac(
                collection="cop-dem-glo-30",
                bbox=bbox,
                date_range=DateRange("2020-01-01", "2020-12-31"),
                limit=1,
            )
            if items:
                paths = mpc_fetcher.download_assets(
                    items=items, out_dir=down_dir, max_items=1, max_total_mb=300.0,
                )
                if paths:
                    args.dem_file = str(paths[0])
                    metadata["dem_source"] = "MPC"
                    metadata["dem_collection"] = "cop-dem-glo-30"
                    metadata["dem_path"] = str(paths[0])
                    print(f"  Auto-downloaded DEM: {paths[0]}")
        except Exception as exc:
            print(f"WARNING: DEM download failed: {exc}", file=sys.stderr)

    # 2) Sentinel-2 L2A — derive 2 water-mask snapshots (early + late in date range)
    if needs_water:
        try:
            mpc_fetcher = DataFetcher(source=DataSource.PLANETARY_COMPUTER)
            items = mpc_fetcher.search_stac(
                collection="sentinel-2-l2a",
                bbox=bbox,
                date_range=dr,
                cloud_cover_max=20.0,
                limit=2,
            )
            if items:
                paths = mpc_fetcher.download_assets(
                    items=items, out_dir=down_dir, max_items=2, max_total_mb=300.0,
                    prefer_assets=["B04", "B08", "B03", "B02"],
                )
                if paths:
                    # Wrap into the multi-arg list form expected by the script
                    args.water_masks = [str(p) for p in paths]
                    metadata["sentinel2_source"] = "MPC"
                    metadata["sentinel2_collection"] = "sentinel-2-l2a"
                    metadata["sentinel2_paths"] = [str(p) for p in paths]
                    print(f"  Auto-downloaded Sentinel-2: {len(paths)} scenes")
        except Exception as exc:
            print(f"WARNING: Sentinel-2 download failed: {exc}", file=sys.stderr)

    return metadata



EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# Risk level codes
RISK_HIGH = 3
RISK_MEDIUM = 2
RISK_LOW = 1
RISK_UNKNOWN = 0

# Quality codes
QUALITY_HIGH = 1
QUALITY_MEDIUM = 2
QUALITY_LOW = 3
QUALITY_INVALID = 4

# Default parameters
DEFAULT_RAINFALL_SCENARIO = "100yr"
DEFAULT_RUNOUT_METHOD = "simplified"
DEFAULT_DEFORMATION_THRESHOLD = 10.0  # mm/yr
DEFAULT_CATCHMENT_THRESHOLD = 1000  # pixels
DEFAULT_EXPOSURE_RADIUS = 5000.0  # meters

# ============================================================
# Geometry Helpers
# ============================================================

def create_polygon(x, y, w, h):
    """Create a shapely polygon (box)."""
    from shapely.geometry import box
    return box(x, y, x + w, y + h)


def safe_json_dumps(obj, **kwargs):
    """JSON dumps with shapely geometry support."""
    def _default(o):
        if hasattr(o, '__geo_interface__'):
            return o.__geo_interface__
        return str(o)
    return json.dumps(obj, default=_default, **kwargs)


def compute_geographic_area(geom, crs=None):
    """
    Compute area handling geographic coordinates.
    EPSG:4326 cannot use transform.a * transform.e / 1e6 directly.
    """
    from shapely.geometry import mapping
    try:
        if crs and hasattr(crs, 'is_projected') and crs.is_projected:
            return geom.area
        # For geographic coordinates, approximate using cos(lat) * 111320
        centroid = geom.centroid
        lat = centroid.y
        lat_factor = np.cos(np.radians(lat))
        # Approximate area: multiply by (111320 * lat_factor * 111320)
        return geom.area * (111320.0 * lat_factor * 111320.0)
    except Exception:
        return geom.area


# ============================================================
# Facility Management
# ============================================================

class TailingsFacility:
    """Represents a tailings dam facility with its properties."""

    def __init__(self, fid: str, name: str, geometry: Dict,
                 dam_height: float = None, capacity: float = None,
                 status: str = "unknown", elevation: float = None):
        self.fid = fid
        self.name = name
        self.geometry = geometry
        self.dam_height = dam_height  # meters
        self.capacity = capacity  # cubic meters
        self.status = status  # active, inactive, closed, unknown
        self.elevation = elevation  # meters
        self.properties = {}

    def to_feature(self) -> Dict:
        """Convert to GeoJSON feature."""
        props = {
            "fid": self.fid,
            "name": self.name,
            "dam_height": self.dam_height,
            "capacity": self.capacity,
            "status": self.status,
            "elevation": self.elevation,
        }
        props.update(self.properties)
        return {
            "type": "Feature",
            "geometry": self.geometry,
            "properties": props,
        }

    def has_critical_data(self) -> bool:
        """Check if critical data (dam height, capacity) is available."""
        return self.dam_height is not None and self.capacity is not None

    def data_completeness(self) -> float:
        """Return data completeness score 0-1."""
        fields = [self.dam_height, self.capacity, self.elevation]
        filled = sum(1 for f in fields if f is not None)
        return filled / len(fields)


def parse_facilities_input(facilities_data: List[Dict]) -> List[TailingsFacility]:
    """Parse facility data from input."""
    facilities = []
    for i, f in enumerate(facilities_data):
        fid = f.get("fid", f.get("id", f"facility_{i}"))
        name = f.get("name", fid)
        geometry = f.get("geometry", f.get("geom"))
        if geometry is None:
            continue
        facility = TailingsFacility(
            fid=fid,
            name=name,
            geometry=geometry,
            dam_height=f.get("dam_height"),
            capacity=f.get("capacity"),
            status=f.get("status", "unknown"),
            elevation=f.get("elevation"),
        )
        facilities.append(facility)
    return facilities


def generate_synthetic_facility(cx: float = 0.0, cy: float = 0.0,
                               size: float = 100.0) -> Dict:
    """Generate a synthetic facility geometry for testing."""
    half = size / 2.0
    return {
        "type": "Polygon",
        "coordinates": [[
            [cx - half, cy - half],
            [cx + half, cy - half],
            [cx + half, cy + half],
            [cx - half, cy + half],
            [cx - half, cy - half],
        ]],
    }


# ============================================================
# Water Surface Change Detection
# ============================================================

def detect_water_surface_change(mask_t1: np.ndarray, mask_t2: np.ndarray,
                                transform=None) -> Dict:
    """
    Detect water surface change between two time periods.

    Args:
        mask_t1: Binary water mask at time 1
        mask_t2: Binary water mask at time 2
        transform: Affine transform

    Returns:
        Dict with change statistics and geometry
    """
    if mask_t1.shape != mask_t2.shape:
        raise ValueError("Mask shapes must match")

    # Compute difference
    diff = mask_t2.astype(np.int16) - mask_t1.astype(np.int16)

    # Expansion: water appeared (0 -> 1)
    expansion = (diff == 1).astype(np.uint8)
    # Contraction: water disappeared (1 -> 0)
    contraction = (diff == -1).astype(np.uint8)

    n_expansion = int(np.sum(expansion))
    n_contraction = int(np.sum(contraction))
    n_water_t1 = int(np.sum(mask_t1))
    n_water_t2 = int(np.sum(mask_t2))

    # Compute change percentage
    if n_water_t1 > 0:
        change_pct = ((n_water_t2 - n_water_t1) / n_water_t1) * 100.0
    else:
        change_pct = 0.0 if n_water_t2 == 0 else 100.0

    # Extract change polygons
    expansion_polygons = _extract_change_polygons(expansion, transform)
    contraction_polygons = _extract_change_polygons(contraction, transform)

    return {
        "n_expansion_pixels": n_expansion,
        "n_contraction_pixels": n_contraction,
        "n_water_t1": n_water_t1,
        "n_water_t2": n_water_t2,
        "change_pct": round(change_pct, 2),
        "expansion_polygons": expansion_polygons,
        "contraction_polygons": contraction_polygons,
        "net_change_pixels": n_expansion - n_contraction,
    }


def _extract_change_polygons(change_mask: np.ndarray, transform=None) -> List[Dict]:
    """Extract polygons from change mask."""
    try:
        from rasterio.features import shapes
        from rasterio.transform import from_bounds
    except ImportError:
        return _extract_polygons_fallback(change_mask, transform)

    if transform is None:
        rows, cols = change_mask.shape
        transform = from_bounds(0, 0, cols, rows, cols, rows)

    results = []
    try:
        for geom, val in shapes(change_mask.astype(np.int32), transform=transform):
            if val == 1 and geom is not None:
                if isinstance(geom, dict) and geom.get("type") is not None:
                    results.append({
                        "geometry": geom,
                        "properties": {"area": _geom_area(geom)},
                    })
    except Exception:
        return _extract_polygons_fallback(change_mask, transform)

    return results


def _extract_polygons_fallback(mask: np.ndarray, transform=None) -> List[Dict]:
    """Fallback polygon extraction without rasterio.features."""
    from shapely.geometry import box

    rows, cols = mask.shape
    if transform is None:
        xmin, ymin, xmax, ymax = 0, 0, cols, rows
    else:
        xmin = transform.c
        ymax = transform.f
        xmax = transform.a * cols + transform.c
        ymin = transform.e * rows + transform.f

    results = []
    visited = np.zeros_like(mask, dtype=bool)
    for r in range(rows):
        for c in range(cols):
            if mask[r, c] == 1 and not visited[r, c]:
                component = _flood_fill(mask, r, c, visited)
                if len(component) >= 2:
                    comp_arr = np.array(component)
                    min_r, min_c = comp_arr.min(axis=0)
                    max_r, max_c = comp_arr.max(axis=0)
                    x1 = xmin + (min_c / cols) * (xmax - xmin)
                    x2 = xmin + ((max_c + 1) / cols) * (xmax - xmin)
                    y2 = ymax - (min_r / rows) * (ymax - ymin)
                    y1 = ymax - ((max_r + 1) / rows) * (ymax - ymin)
                    poly = box(x1, y1, x2, y2)
                    results.append({
                        "geometry": poly.__geo_interface__,
                        "properties": {"area": poly.area},
                    })
    return results


def _flood_fill(mask: np.ndarray, start_r: int, start_c: int,
                visited: np.ndarray) -> List[Tuple[int, int]]:
    """BFS flood fill to find connected component."""
    rows, cols = mask.shape
    component = []
    queue = [(start_r, start_c)]
    visited[start_r, start_c] = True

    while queue:
        r, c = queue.pop(0)
        component.append((r, c))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if mask[nr, nc] == 1 and not visited[nr, nc]:
                    visited[nr, nc] = True
                    queue.append((nr, nc))

    return component


def _geom_area(geom: Dict) -> float:
    """Compute area from a GeoJSON-like geometry dict."""
    from shapely.geometry import shape
    try:
        return shape(geom).area
    except Exception:
        return 0.0


# ============================================================
# Catchment Analysis (Watershed)
# ============================================================

def compute_catchment(dem: np.ndarray, dam_location: Tuple[int, int],
                      transform=None, threshold: int = DEFAULT_CATCHMENT_THRESHOLD) -> Dict:
    """
    Compute upstream catchment area from DEM using flow accumulation.

    Simplified D8-like approach for screening purposes.

    Args:
        dem: Digital Elevation Model (2D array)
        dam_location: (row, col) of dam location
        transform: Affine transform
        threshold: Minimum accumulation for stream definition

    Returns:
        Dict with catchment statistics
    """
    rows, cols = dem.shape

    # Compute flow direction (D8)
    flow_dir = _compute_flow_direction(dem)

    # Compute flow accumulation
    accumulation = _compute_flow_accumulation(flow_dir, rows, cols)

    # Delineate watershed from dam location (upstream area that drains TO dam)
    # For tailings dam risk, we want the upstream catchment that would
    # contribute water to the dam
    catchment_mask = _delineate_watershed(flow_dir, dam_location, rows, cols)

    n_catchment_pixels = int(np.sum(catchment_mask))
    catchment_area_km2 = _pixels_to_area(n_catchment_pixels, transform)

    # Compute statistics
    if n_catchment_pixels > 0:
        catchment_elevations = dem[catchment_mask > 0]
        mean_elevation = float(np.mean(catchment_elevations))
        max_elevation = float(np.max(catchment_elevations))
        min_elevation = float(np.min(catchment_elevations))
        elevation_range = max_elevation - min_elevation
    else:
        mean_elevation = 0.0
        max_elevation = 0.0
        min_elevation = 0.0
        elevation_range = 0.0

    # Extract catchment polygon
    catchment_polygons = _extract_change_polygons(catchment_mask, transform)

    return {
        "n_catchment_pixels": n_catchment_pixels,
        "catchment_area_km2": round(catchment_area_km2, 4),
        "mean_elevation": round(mean_elevation, 2),
        "max_elevation": round(max_elevation, 2),
        "min_elevation": round(min_elevation, 2),
        "elevation_range": round(elevation_range, 2),
        "max_accumulation": int(np.max(accumulation)),
        "catchment_polygons": catchment_polygons,
    }


def _compute_flow_direction(dem: np.ndarray) -> np.ndarray:
    """
    Compute D8 flow direction.
    Returns array of direction codes (0-7) or -1 for flats/peaks.
    Directions: 0=E, 1=SE, 2=S, 3=SW, 4=W, 5=NW, 6=N, 7=NE
    """
    rows, cols = dem.shape
    flow_dir = np.full((rows, cols), -1, dtype=np.int8)

    # Direction offsets: E, SE, S, SW, W, NW, N, NE
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]
    # Distance weights (diagonal = sqrt(2))
    dist = [1.0, 1.414, 1.0, 1.414, 1.0, 1.414, 1.0, 1.414]

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            max_slope = 0.0
            best_dir = -1
            for d in range(8):
                nr, nc = r + dr[d], c + dc[d]
                slope = (dem[r, c] - dem[nr, nc]) / dist[d]
                if slope > max_slope:
                    max_slope = slope
                    best_dir = d
            flow_dir[r, c] = best_dir

    return flow_dir


def _compute_flow_accumulation(flow_dir: np.ndarray, rows: int, cols: int) -> np.ndarray:
    """Compute flow accumulation from flow direction.

    Uses iterative approach with overflow protection for screening purposes.
    """
    accumulation = np.ones((rows, cols), dtype=np.float64)  # float64 avoids int overflow

    # Direction offsets
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    # Simple iterative accumulation with overflow protection
    max_val = float(rows * cols)  # Upper bound for accumulation
    for _ in range(min(rows, cols)):
        changed = False
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                d = flow_dir[r, c]
                if d >= 0:
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < rows and 0 <= nc < cols:
                        new_val = accumulation[r, c] + accumulation[nr, nc]
                        # Cap at max_val to prevent overflow
                        if new_val > max_val:
                            new_val = max_val
                        if new_val > accumulation[nr, nc]:
                            accumulation[nr, nc] = new_val
                            changed = True
        if not changed:
            break

    return accumulation


def _delineate_watershed(flow_dir: np.ndarray, outlet: Tuple[int, int],
                         rows: int, cols: int) -> np.ndarray:
    """
    Delineate watershed upstream of outlet.
    Traces upstream from outlet following reverse flow directions.
    """
    watershed = np.zeros((rows, cols), dtype=np.uint8)

    # Direction offsets
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]
    # Reverse direction
    reverse_dir = {0: 4, 1: 5, 2: 6, 3: 7, 4: 0, 5: 1, 6: 2, 7: 3}

    # BFS from outlet going upstream
    queue = [outlet]
    watershed[outlet[0], outlet[1]] = 1

    while queue:
        r, c = queue.pop(0)
        # Check all neighbors that flow into this cell
        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < rows and 0 <= nc < cols:
                if watershed[nr, nc] == 0:
                    # Check if neighbor flows toward current cell
                    nd = flow_dir[nr, nc]
                    if nd >= 0:
                        nnr, nnc = nr + dr[nd], nc + dc[nd]
                        if nnr == r and nnc == c:
                            watershed[nr, nc] = 1
                            queue.append((nr, nc))

    return watershed


def _pixels_to_area(n_pixels: int, transform=None) -> float:
    """Convert pixel count to area in km²."""
    if transform is None:
        # Assume 30m pixels (Landsat-like)
        pixel_area_m2 = 30.0 * 30.0
    else:
        pixel_area_m2 = abs(transform.a * transform.e)
    return (n_pixels * pixel_area_m2) / 1e6


# ============================================================
# Runout / Impact Zone
# ============================================================

def compute_runout_zone(dem: np.ndarray, dam_location: Tuple[int, int],
                        dam_height: float = None, transform=None,
                        method: str = "simplified") -> Dict:
    """
    Compute simplified runout/impact zone for tailings dam failure.

    This is a SCREENING-ONLY simplified model, not an engineering analysis.

    Args:
        dem: Digital Elevation Model
        dam_location: (row, col) of dam
        dam_height: Dam height in meters (None for unknown)
        transform: Affine transform
        method: "simplified" (screening) or "energy_line" (basic)

    Returns:
        Dict with runout zone statistics
    """
    rows, cols = dem.shape

    if method == "simplified":
        return _compute_runout_simplified(dem, dam_location, dam_height, transform)
    elif method == "energy_line":
        return _compute_runout_energy_line(dem, dam_location, dam_height, transform)
    else:
        raise ValueError(f"Unknown runout method: {method}")


def _compute_runout_simplified(dem: np.ndarray, dam_location: Tuple[int, int],
                               dam_height: float = None, transform=None) -> Dict:
    """
    Simplified runout using elevation drop and reach angle.

    Uses the concept of reach angle (angle of repose for debris flow).
    Typical reach angle: 0.1-0.3 (tan(alpha)) for tailings flows.
    """
    rows, cols = dem.shape
    dam_r, dam_c = dam_location
    dam_elev = dem[dam_r, dam_c]

    # Reach angle (tan alpha) - typical 0.15 for tailings flows
    reach_angle = 0.15

    # If dam height is known, use it to estimate flow energy
    if dam_height is not None and dam_height > 0:
        # Extended reach for higher dams
        effective_height = dam_height
    else:
        # Use elevation difference within local window
        window = 10
        r_min = max(0, dam_r - window)
        r_max = min(rows, dam_r + window)
        c_min = max(0, dam_c - window)
        c_max = min(cols, dam_c + window)
        local_max = np.max(dem[r_min:r_max, c_min:c_max])
        effective_height = max(local_max - dam_elev, 10.0)

    # Compute runout distance based on reach angle
    # Distance = height / tan(alpha)
    runout_distance = effective_height / reach_angle

    # Create runout zone by flooding downstream
    runout_mask = np.zeros((rows, cols), dtype=np.uint8)

    # Trace downstream from dam
    flow_dir = _compute_flow_direction(dem)
    queue = [dam_location]
    runout_mask[dam_r, dam_c] = 1

    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    max_distance_pixels = runout_distance / 30.0  # assume 30m pixels
    if transform is not None:
        pixel_size = abs(transform.a)
        max_distance_pixels = runout_distance / pixel_size

    visited = set()
    while queue:
        r, c = queue.pop(0)
        if (r, c) in visited:
            continue
        visited.add((r, c))

        # Check if still within runout distance
        dist_from_dam = np.sqrt((r - dam_r)**2 + (c - dam_c)**2)
        if dist_from_dam > max_distance_pixels:
            continue

        # Check elevation - stop if uphill from dam
        if dem[r, c] > dam_elev + effective_height:
            continue

        runout_mask[r, c] = 1

        # Follow flow direction
        d = flow_dir[r, c]
        if d >= 0:
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited:
                    queue.append((nr, nc))

    n_runout_pixels = int(np.sum(runout_mask))
    runout_area_km2 = _pixels_to_area(n_runout_pixels, transform)

    # Extract runout polygon
    runout_polygons = _extract_change_polygons(runout_mask, transform)

    return {
        "method": "simplified",
        "reach_angle": reach_angle,
        "effective_height": round(effective_height, 2),
        "runout_distance_m": round(runout_distance, 2),
        "n_runout_pixels": n_runout_pixels,
        "runout_area_km2": round(runout_area_km2, 4),
        "runout_polygons": runout_polygons,
        "is_screening_only": True,
    }


def _compute_runout_energy_line(dem: np.ndarray, dam_location: Tuple[int, int],
                                dam_height: float = None, transform=None) -> Dict:
    """
    Energy line method for runout estimation.

    Uses the concept that flow stops when the terrain rises above
    the energy line (H/L ratio).
    """
    rows, cols = dem.shape
    dam_r, dam_c = dam_location
    dam_elev = dem[dam_r, dam_c]

    # H/L ratio (typical 0.1-0.3 for tailings flows)
    hl_ratio = 0.2

    # Estimate runout
    if dam_height is not None and dam_height > 0:
        H = dam_height
    else:
        window = 10
        r_min = max(0, dam_r - window)
        r_max = min(rows, dam_r + window)
        c_min = max(0, dam_c - window)
        c_max = min(cols, dam_c + window)
        local_max = np.max(dem[r_min:r_max, c_min:c_max])
        H = max(local_max - dam_elev, 10.0)

    runout_distance = H / hl_ratio

    # Create runout zone
    runout_mask = np.zeros((rows, cols), dtype=np.uint8)
    energy_line_elev = dam_elev + H

    # Flood downstream until energy line
    flow_dir = _compute_flow_direction(dem)
    queue = [dam_location]
    runout_mask[dam_r, dam_c] = 1

    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    visited = set()
    while queue:
        r, c = queue.pop(0)
        if (r, c) in visited:
            continue
        visited.add((r, c))

        # Stop if above energy line
        if dem[r, c] > energy_line_elev:
            continue

        runout_mask[r, c] = 1

        d = flow_dir[r, c]
        if d >= 0:
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited:
                    queue.append((nr, nc))

    n_runout_pixels = int(np.sum(runout_mask))
    runout_area_km2 = _pixels_to_area(n_runout_pixels, transform)
    runout_polygons = _extract_change_polygons(runout_mask, transform)

    return {
        "method": "energy_line",
        "hl_ratio": hl_ratio,
        "effective_height": round(H, 2),
        "runout_distance_m": round(runout_distance, 2),
        "n_runout_pixels": n_runout_pixels,
        "runout_area_km2": round(runout_area_km2, 4),
        "runout_polygons": runout_polygons,
        "is_screening_only": True,
    }


# ============================================================
# Downstream Exposure Analysis
# ============================================================

def compute_downstream_exposure(dem: np.ndarray, dam_location: Tuple[int, int],
                                exposure_objects: List[Dict] = None,
                                transform=None,
                                radius: float = DEFAULT_EXPOSURE_RADIUS) -> Dict:
    """
    Compute downstream exposure statistics.

    Analyzes objects (buildings, roads, population) within the
    potential impact zone.

    Args:
        dem: Digital Elevation Model
        dam_location: (row, col) of dam
        exposure_objects: List of exposure objects with geometry
        transform: Affine transform
        radius: Search radius in meters

    Returns:
        Dict with exposure statistics
    """
    rows, cols = dem.shape

    # Compute runout zone first
    runout = compute_runout_zone(dem, dam_location, transform=transform)
    runout_mask = np.zeros((rows, cols), dtype=np.uint8)

    # Reconstruct runout mask from polygons (simplified)
    # For screening, use a buffer around dam location
    if transform is not None:
        pixel_size = abs(transform.a)
    else:
        pixel_size = 30.0

    radius_pixels = int(radius / pixel_size)
    dam_r, dam_c = dam_location

    # Create circular buffer as simplified exposure zone
    for r in range(max(0, dam_r - radius_pixels), min(rows, dam_r + radius_pixels)):
        for c in range(max(0, dam_c - radius_pixels), min(cols, dam_c + radius_pixels)):
            dist = np.sqrt((r - dam_r)**2 + (c - dam_c)**2)
            if dist <= radius_pixels:
                runout_mask[r, c] = 1

    n_exposure_pixels = int(np.sum(runout_mask))
    exposure_area_km2 = _pixels_to_area(n_exposure_pixels, transform)

    # Count exposure objects within zone
    n_objects = 0
    object_types = {}
    if exposure_objects:
        for obj in exposure_objects:
            geom = obj.get("geometry", obj)
            obj_type = obj.get("type", obj.get("properties", {}).get("type", "unknown"))
            # Simplified: check if object centroid is within radius
            if _is_object_in_zone(geom, dam_location, radius_pixels, transform):
                n_objects += 1
                object_types[obj_type] = object_types.get(obj_type, 0) + 1

    # Compute downstream elevation profile
    downstream_profile = _compute_downstream_profile(dem, dam_location, transform)

    return {
        "exposure_radius_m": radius,
        "n_exposure_pixels": n_exposure_pixels,
        "exposure_area_km2": round(exposure_area_km2, 4),
        "n_objects_in_zone": n_objects,
        "object_types": object_types,
        "downstream_profile": downstream_profile,
    }


def _is_object_in_zone(geom, dam_location: Tuple[int, int],
                       radius_pixels: int, transform=None) -> bool:
    """Check if an object is within the exposure zone."""
    from shapely.geometry import shape, Point

    try:
        if isinstance(geom, dict):
            if "geometry" in geom:
                geom = geom["geometry"]
            shapely_geom = shape(geom)
        else:
            shapely_geom = geom

        centroid = shapely_geom.centroid
        dam_r, dam_c = dam_location

        if transform is not None:
            # Convert pixel to coordinates
            dam_x = transform.c + dam_c * transform.a
            dam_y = transform.f + dam_r * transform.e
            dist = np.sqrt((centroid.x - dam_x)**2 + (centroid.y - dam_y)**2)
            return dist <= (radius_pixels * abs(transform.a))
        else:
            # Pixel space
            obj_r = int((centroid.y - transform.f) / transform.e) if transform else 0
            obj_c = int((centroid.x - transform.c) / transform.a) if transform else 0
            dist = np.sqrt((obj_r - dam_r)**2 + (obj_c - dam_c)**2)
            return dist <= radius_pixels
    except Exception:
        return False


def _compute_downstream_profile(dem: np.ndarray, dam_location: Tuple[int, int],
                                transform=None) -> List[Dict]:
    """Compute elevation profile downstream of dam."""
    rows, cols = dem.shape
    dam_r, dam_c = dam_location

    # Trace downstream
    flow_dir = _compute_flow_direction(dem)
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    profile = []
    r, c = dam_r, dam_c
    for step in range(100):  # Max 100 steps
        if r < 0 or r >= rows or c < 0 or c >= cols:
            break
        profile.append({
            "step": step,
            "row": r,
            "col": c,
            "elevation": float(dem[r, c]),
        })
        d = flow_dir[r, c]
        if d < 0:
            break
        r, c = r + dr[d], c + dc[d]

    return profile


# ============================================================
# Risk Scoring
# ============================================================

def compute_risk_score(facility: TailingsFacility,
                       water_change: Dict,
                       catchment: Dict,
                       runout: Dict,
                       exposure: Dict,
                       rules: Dict = None) -> Dict:
    """
    Compute overall risk score based on hazard, exposure, and evidence.

    Risk = f(Hazard, Exposure, Evidence)

    Args:
        facility: Tailings facility object
        water_change: Water surface change results
        catchment: Catchment analysis results
        runout: Runout zone results
        exposure: Downstream exposure results
        rules: Risk scoring rules

    Returns:
        Dict with risk scores and level
    """
    if rules is None:
        rules = _default_risk_rules()

    # Hazard score (0-100)
    hazard_score = _compute_hazard_score(facility, water_change, catchment, runout, rules)

    # Exposure score (0-100)
    exposure_score = _compute_exposure_score(exposure, rules)

    # Evidence score (0-100)
    evidence_score = _compute_evidence_score(water_change, catchment, rules)

    # Combined risk (weighted)
    weights = rules.get("weights", {"hazard": 0.4, "exposure": 0.35, "evidence": 0.25})
    combined = (hazard_score * weights["hazard"] +
                exposure_score * weights["exposure"] +
                evidence_score * weights["evidence"])

    # Determine risk level
    if combined >= rules.get("high_threshold", 70):
        risk_level = RISK_HIGH
    elif combined >= rules.get("medium_threshold", 40):
        risk_level = RISK_MEDIUM
    elif combined >= rules.get("low_threshold", 20):
        risk_level = RISK_LOW
    else:
        risk_level = RISK_UNKNOWN

    # Data completeness penalty
    completeness = facility.data_completeness()
    if completeness < 0.5:
        # Reduce confidence for incomplete data
        confidence = "low"
    elif completeness < 0.8:
        confidence = "medium"
    else:
        confidence = "high"

    return {
        "hazard_score": round(hazard_score, 2),
        "exposure_score": round(exposure_score, 2),
        "evidence_score": round(evidence_score, 2),
        "combined_score": round(combined, 2),
        "risk_level": risk_level,
        "confidence": confidence,
        "data_completeness": round(completeness, 2),
        "is_screening_only": True,
    }


def _compute_hazard_score(facility: TailingsFacility, water_change: Dict,
                          catchment: Dict, runout: Dict, rules: Dict) -> float:
    """Compute hazard score (0-100)."""
    score = 0.0

    # Dam height factor (higher = more hazardous)
    if facility.dam_height is not None:
        dh = facility.dam_height
        if dh > 50:
            score += 30
        elif dh > 30:
            score += 20
        elif dh > 15:
            score += 10
        else:
            score += 5
    else:
        score += 15  # Unknown = moderate hazard

    # Capacity factor
    if facility.capacity is not None:
        cap = facility.capacity
        if cap > 10_000_000:  # > 10 M m³
            score += 20
        elif cap > 1_000_000:
            score += 15
        elif cap > 100_000:
            score += 10
        else:
            score += 5
    else:
        score += 10

    # Water surface change factor
    change_pct = abs(water_change.get("change_pct", 0))
    if change_pct > 50:
        score += 20
    elif change_pct > 20:
        score += 15
    elif change_pct > 10:
        score += 10
    elif change_pct > 5:
        score += 5

    # Catchment size factor
    catchment_area = catchment.get("catchment_area_km2", 0)
    if catchment_area > 10:
        score += 15
    elif catchment_area > 5:
        score += 10
    elif catchment_area > 1:
        score += 5

    # Runout potential
    runout_dist = runout.get("runout_distance_m", 0)
    if runout_dist > 5000:
        score += 15
    elif runout_dist > 2000:
        score += 10
    elif runout_dist > 1000:
        score += 5

    return min(score, 100.0)


def _compute_exposure_score(exposure: Dict, rules: Dict) -> float:
    """Compute exposure score (0-100)."""
    score = 0.0

    n_objects = exposure.get("n_objects_in_zone", 0)
    if n_objects > 100:
        score += 60
    elif n_objects > 50:
        score += 40
    elif n_objects > 20:
        score += 30
    elif n_objects > 5:
        score += 20
    elif n_objects > 0:
        score += 10

    # Exposure area
    area = exposure.get("exposure_area_km2", 0)
    if area > 10:
        score += 40
    elif area > 5:
        score += 30
    elif area > 1:
        score += 20
    elif area > 0.1:
        score += 10

    return min(score, 100.0)


def _compute_evidence_score(water_change: Dict, catchment: Dict, rules: Dict) -> float:
    """Compute evidence score (0-100) based on observed changes."""
    score = 0.0

    # Water surface change evidence
    change_pct = abs(water_change.get("change_pct", 0))
    if change_pct > 30:
        score += 40
    elif change_pct > 15:
        score += 30
    elif change_pct > 5:
        score += 20
    elif change_pct > 1:
        score += 10

    # Net change magnitude
    net_change = abs(water_change.get("net_change_pixels", 0))
    if net_change > 1000:
        score += 30
    elif net_change > 500:
        score += 20
    elif net_change > 100:
        score += 10

    # Catchment evidence (large catchment = more evidence of water contribution)
    catchment_area = catchment.get("catchment_area_km2", 0)
    if catchment_area > 5:
        score += 30
    elif catchment_area > 2:
        score += 20
    elif catchment_area > 0.5:
        score += 10

    return min(score, 100.0)


def _default_risk_rules() -> Dict:
    """Default risk scoring rules."""
    return {
        "weights": {"hazard": 0.4, "exposure": 0.35, "evidence": 0.25},
        "high_threshold": 70,
        "medium_threshold": 40,
        "low_threshold": 20,
    }


# ============================================================
# Deformation Analysis
# ============================================================

def analyze_deformation(deformation_data: np.ndarray,
                        threshold: float = DEFAULT_DEFORMATION_THRESHOLD) -> Dict:
    """
    Analyze deformation data (e.g., from InSAR).

    Args:
        deformation_data: 2D array of deformation rates (mm/yr)
        threshold: Threshold for significant deformation

    Returns:
        Dict with deformation statistics
    """
    if deformation_data is None:
        return {
            "has_data": False,
            "n_significant_pixels": 0,
            "max_deformation": 0.0,
            "mean_deformation": 0.0,
        }

    # Identify significant deformation
    significant = np.abs(deformation_data) > threshold
    n_significant = int(np.sum(significant))

    # Statistics
    valid_data = deformation_data[~np.isnan(deformation_data)]
    if len(valid_data) > 0:
        max_def = float(np.max(np.abs(valid_data)))
        mean_def = float(np.mean(valid_data))
        std_def = float(np.std(valid_data))
    else:
        max_def = 0.0
        mean_def = 0.0
        std_def = 0.0

    return {
        "has_data": True,
        "n_significant_pixels": n_significant,
        "max_deformation": round(max_def, 2),
        "mean_deformation": round(mean_def, 2),
        "std_deformation": round(std_def, 2),
        "threshold": threshold,
    }


# ============================================================
# Rainfall Scenario
# ============================================================

def compute_rainfall_scenario(catchment: Dict,
                              scenario: str = DEFAULT_RAINFALL_SCENARIO) -> Dict:
    """
    Compute rainfall scenario for the catchment.

    Args:
        catchment: Catchment analysis results
        scenario: Rainfall scenario (e.g., "100yr", "500yr")

    Returns:
        Dict with rainfall scenario results
    """
    # Simplified rainfall intensity estimation
    # In practice, would use IDF curves or regional precipitation data
    scenario_multipliers = {
        "100yr": 1.0,
        "500yr": 1.3,
        "1000yr": 1.5,
    }

    multiplier = scenario_multipliers.get(scenario, 1.0)
    catchment_area = catchment.get("catchment_area_km2", 0)

    # Simplified peak flow estimation (rational method)
    # Q = C * i * A
    # Assume C = 0.5 (runoff coefficient), i = rainfall intensity
    # Base intensity: 100 mm/hr for 100yr event
    base_intensity = 100.0  # mm/hr
    intensity = base_intensity * multiplier

    # Peak flow (m³/s)
    runoff_coefficient = 0.5
    area_m2 = catchment_area * 1e6
    peak_flow = runoff_coefficient * (intensity / 1000 / 3600) * area_m2

    return {
        "scenario": scenario,
        "multiplier": multiplier,
        "rainfall_intensity_mm_hr": round(intensity, 2),
        "catchment_area_km2": round(catchment_area, 4),
        "peak_flow_m3s": round(peak_flow, 2),
        "runoff_coefficient": runoff_coefficient,
    }


# ============================================================
# Report Generation
# ============================================================

def generate_risk_report(facilities: List[TailingsFacility],
                         results: List[Dict],
                         output_dir: Path) -> Path:
    """
    Generate risk report in HTML format.

    Args:
        facilities: List of facilities
        results: List of analysis results
        output_dir: Output directory

    Returns:
        Path to generated report
    """
    report_path = output_dir / "risk_report.html"

    html = _build_report_html(facilities, results)
    report_path.write_text(html, encoding="utf-8")

    return report_path


def _build_report_html(facilities: List[TailingsFacility],
                       results: List[Dict]) -> str:
    """Build HTML report content."""
    # Use string formatting carefully to avoid f-string issues with dict values
    parts = []
    parts.append("<!DOCTYPE html>")
    parts.append("<html><head><meta charset='utf-8'>")
    parts.append("<title>Tailings Dam Risk Screening Report</title>")
    parts.append("<style>")
    parts.append("body { font-family: Arial, sans-serif; margin: 40px; }")
    parts.append("h1 { color: #333; }")
    parts.append("table { border-collapse: collapse; width: 100%; margin: 20px 0; }")
    parts.append("th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }")
    parts.append("th { background-color: #4CAF50; color: white; }")
    parts.append(".risk-high { color: red; font-weight: bold; }")
    parts.append(".risk-medium { color: orange; }")
    parts.append(".risk-low { color: green; }")
    parts.append(".warning { background-color: #fff3cd; padding: 10px; border-left: 4px solid #ffc107; }")
    parts.append("</style></head><body>")

    parts.append("<h1>Tailings Dam Risk Screening Report</h1>")
    parts.append(f"<p>Generated: {datetime.now(timezone.utc).isoformat()}</p>")

    # Warning
    parts.append("<div class='warning'>")
    parts.append("<strong>⚠️ SCREENING ONLY:</strong> This report is for screening ")
    parts.append("purposes only and does NOT replace engineering safety assessment. ")
    parts.append("All results must be reviewed by qualified engineers.")
    parts.append("</div>")

    # Summary table
    parts.append("<h2>Facility Risk Summary</h2>")
    parts.append("<table>")
    parts.append("<tr><th>Facility</th><th>Risk Level</th><th>Hazard</th>")
    parts.append("<th>Exposure</th><th>Evidence</th><th>Confidence</th></tr>")

    for result in results:
        risk_level = result.get("risk_level", RISK_UNKNOWN)
        risk_class = ""
        risk_name = ""
        if risk_level == RISK_HIGH:
            risk_class = "risk-high"
            risk_name = "HIGH"
        elif risk_level == RISK_MEDIUM:
            risk_class = "risk-medium"
            risk_name = "MEDIUM"
        elif risk_level == RISK_LOW:
            risk_class = "risk-low"
            risk_name = "LOW"
        else:
            risk_name = "UNKNOWN"

        facility_name = result.get("facility_name", "Unknown")
        hazard = result.get("hazard_score", "N/A")
        exposure = result.get("exposure_score", "N/A")
        evidence = result.get("evidence_score", "N/A")
        confidence = result.get("confidence", "N/A")

        parts.append(f"<tr><td>{facility_name}</td>")
        parts.append(f"<td class='{risk_class}'>{risk_name}</td>")
        parts.append(f"<td>{hazard}</td>")
        parts.append(f"<td>{exposure}</td>")
        parts.append(f"<td>{evidence}</td>")
        parts.append(f"<td>{confidence}</td></tr>")

    parts.append("</table>")

    # Detailed results
    parts.append("<h2>Detailed Results</h2>")
    for result in results:
        facility_name = result.get("facility_name", "Unknown")
        parts.append(f"<h3>{facility_name}</h3>")
        parts.append("<ul>")
        parts.append(f"<li>Combined Score: {result.get('combined_score', 'N/A')}</li>")
        parts.append(f"<li>Data Completeness: {result.get('data_completeness', 'N/A')}</li>")
        parts.append(f"<li>Water Change: {result.get('water_change_pct', 'N/A')}%</li>")
        parts.append(f"<li>Catchment Area: {result.get('catchment_area_km2', 'N/A')} km²</li>")
        parts.append(f"<li>Runout Distance: {result.get('runout_distance_m', 'N/A')} m</li>")
        parts.append(f"<li>Objects in Zone: {result.get('n_objects_in_zone', 'N/A')}</li>")
        parts.append("</ul>")

    parts.append("</body></html>")

    return "\n".join(parts)


# ============================================================
# Synthetic Data Generation
# ============================================================

def generate_synthetic_dem(rows: int = 200, cols: int = 200,
                           dam_row: int = 100, dam_col: int = 100,
                           max_elevation: float = 500.0) -> np.ndarray:
    """
    Generate a synthetic DEM with a valley and dam location.

    Creates a DEM where elevation decreases from top to bottom (north to south),
    with a valley in the middle.
    """
    dem = np.zeros((rows, cols), dtype=np.float64)

    # Base elevation gradient (higher at top, lower at bottom)
    for r in range(rows):
        dem[r, :] = max_elevation * (1.0 - r / rows)

    # Add valley (lower elevation in middle columns)
    valley_center = cols // 2
    valley_width = cols // 4
    for c in range(cols):
        dist_from_center = abs(c - valley_center)
        if dist_from_center < valley_width:
            valley_depth = 50.0 * (1.0 - dist_from_center / valley_width)
            dem[:, c] -= valley_depth

    # Add some noise
    np.random.seed(42)
    dem += np.random.normal(0, 2, dem.shape)

    # Ensure dam location is at a reasonable elevation
    dem[dam_row, dam_col] = max_elevation * 0.5

    return dem


def generate_synthetic_water_mask(rows: int = 200, cols: int = 200,
                                 water_center: Tuple[int, int] = (100, 100),
                                 water_radius: int = 20) -> np.ndarray:
    """Generate a synthetic water mask (circular water body)."""
    mask = np.zeros((rows, cols), dtype=np.uint8)
    cr, cc = water_center

    for r in range(rows):
        for c in range(cols):
            dist = np.sqrt((r - cr)**2 + (c - cc)**2)
            if dist <= water_radius:
                mask[r, c] = 1

    return mask


def generate_synthetic_deformation(rows: int = 200, cols: int = 200,
                                   deformation_center: Tuple[int, int] = (100, 100),
                                   max_rate: float = 25.0) -> np.ndarray:
    """Generate synthetic deformation data (mm/yr)."""
    deformation = np.zeros((rows, cols), dtype=np.float64)
    cr, cc = deformation_center

    for r in range(rows):
        for c in range(cols):
            dist = np.sqrt((r - cr)**2 + (c - cc)**2)
            if dist < 30:
                deformation[r, c] = -max_rate * (1.0 - dist / 30)

    return deformation


# ============================================================
# Main Analysis Pipeline
# ============================================================

def auto_download_dem(args, output_dir: Path) -> Dict[str, Any]:
    """Download DEM (cop-dem-glo-30) + Sentinel-2 (sentinel-2-l2a) water-mask snapshots.

    Returns metadata dict (also writes the paths back to args.dem_file and args.water_masks).
    """
    if not _HAS_FETCHER:
        raise RuntimeError(
            "Shared data fetcher not importable. Pass --dem-file/--water-masks instead, "
            "or ensure _geoskill_data_fetcher is on sys.path."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_dem requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        dr = DateRange("2023-06-01", "2023-09-30")
    cache_dir = getattr(args, "cache_dir", None)
    metadata: Dict[str, Any] = {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
    }

    needs_dem = not getattr(args, "dem_file", None) or not Path(args.dem_file).exists()
    needs_water = not getattr(args, "water_masks", None)
    download_dir = output_dir / "downloaded"

    fetcher = DataFetcher(
        source=DataSource.PLANETARY_COMPUTER,
        cache_dir=Path(cache_dir) if cache_dir else None,
    )

    # 1) DEM (cop-dem-glo-30) — single static tile
    if needs_dem:
        try:
            items = fetcher.search_stac(
                collection="cop-dem-glo-30",
                bbox=bbox,
                date_range=DateRange("2020-01-01", "2021-12-31"),
                limit=1,
            )
            if items:
                paths = fetcher.download_assets(
                    items=items, out_dir=download_dir, max_items=1, max_total_mb=500.0,
                )
                if paths:
                    args.dem_file = str(paths[0])
                    metadata["dem_collection"] = "cop-dem-glo-30"
                    metadata["dem_path"] = str(paths[0])
                    print(f"  Auto-downloaded DEM: {paths[0]}")
        except Exception as exc:
            print(f"WARNING: DEM download failed: {exc}", file=sys.stderr)

    # 2) Sentinel-2 L2A — derive 1 water-mask snapshot (faster download)
    if needs_water:
        try:
            items = fetcher.search_stac(
                collection="sentinel-2-l2a",
                bbox=bbox,
                date_range=dr,
                cloud_cover_max=20.0,
                limit=1,
            )
            if items:
                paths = fetcher.download_assets(
                    items=items, out_dir=download_dir, max_items=1, max_total_mb=300.0,
                    prefer_assets=["B04", "B08", "B03", "B02"],
                )
                if paths:
                    args.water_masks = [str(p) for p in paths]
                    metadata["sentinel2_collection"] = "sentinel-2-l2a"
                    metadata["sentinel2_paths"] = [str(p) for p in paths]
                    print(f"  Auto-downloaded Sentinel-2: {len(paths)} scenes")
        except Exception as exc:
            print(f"WARNING: Sentinel-2 download failed: {exc}", file=sys.stderr)

    metadata["collection"] = metadata.get("dem_collection") or metadata.get("sentinel2_collection", "cop-dem-glo-30")
    return metadata


def run_analysis(args: argparse.Namespace) -> int:
    """Main analysis workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("tdr-output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # --- Auto-download mode: fetch DEM + Sentinel-2 from MPC ---
    fetch_meta: Dict[str, Any] = {}
    if (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)):
        needs_dem = not getattr(args, "dem_file", None) or not Path(args.dem_file).exists()
        needs_water = not getattr(args, "water_masks", None)
        if needs_dem or needs_water:
            try:
                fetch_meta = auto_download_dem(args, output_dir)
                print(f"  Auto-download complete")
            except Exception as e:
                print(f"ERROR: auto-download failed: {e}", file=sys.stderr)
                return EXIT_PROCESSING

    # Setup logging
    log_path = output_dir / "run.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(sys.stderr),
        ],
    )
    logger = logging.getLogger(__name__)

    logger.info("Starting Tailings Dam Risk Screening")
    logger.info(f"Output directory: {output_dir}")

    # Parse parameters
    rainfall_scenario = getattr(args, 'rainfall_scenario', None) or DEFAULT_RAINFALL_SCENARIO
    runout_method = getattr(args, 'runout_method', None) or DEFAULT_RUNOUT_METHOD
    deformation_threshold = getattr(args, 'deformation_threshold', None) or DEFAULT_DEFORMATION_THRESHOLD
    exposure_radius = getattr(args, 'exposure_radius', None) or DEFAULT_EXPOSURE_RADIUS

    # Load or generate facilities
    facilities = []
    if hasattr(args, 'facilities') and args.facilities:
        try:
            facilities_data = json.loads(Path(args.facilities).read_text(encoding="utf-8"))
            facilities = parse_facilities_input(facilities_data)
        except Exception as e:
            logger.error(f"Failed to load facilities: {e}")
            return EXIT_VALIDATION
    else:
        # Generate synthetic facility for demonstration
        facilities = [TailingsFacility(
            fid="demo_001",
            name="Demo Tailings Facility",
            geometry=generate_synthetic_facility(0, 0, 100),
            dam_height=35.0,
            capacity=5_000_000,
            status="active",
            elevation=250.0,
        )]

    if not facilities:
        logger.error("No facilities to analyze")
        return EXIT_VALIDATION

    # Load or generate DEM
    dem = None
    if hasattr(args, 'dem_file') and args.dem_file:
        try:
            import rasterio
            with rasterio.open(args.dem_file) as src:
                dem = src.read(1).astype(np.float64)
                dem_transform = src.transform
                dem_crs = src.crs
        except ImportError:
            logger.error("rasterio required for GeoTIFF input")
            return EXIT_DEP
        except Exception as e:
            logger.error(f"Failed to read DEM: {e}")
            return EXIT_VALIDATION
    else:
        dem = generate_synthetic_dem()
        dem_transform = None
        dem_crs = "EPSG:4326"

    # Load or generate water masks
    water_masks = []
    if hasattr(args, 'water_masks') and args.water_masks:
        try:
            import rasterio
            for mask_path in args.water_masks:
                with rasterio.open(mask_path) as src:
                    water_masks.append(src.read(1).astype(np.uint8))
        except ImportError:
            logger.error("rasterio required for GeoTIFF input")
            return EXIT_DEP
        except Exception as e:
            logger.error(f"Failed to read water mask: {e}")
            return EXIT_VALIDATION
    else:
        # Generate synthetic water masks (3 periods with expansion)
        mask1 = generate_synthetic_water_mask(200, 200, (100, 100), 15)
        mask2 = generate_synthetic_water_mask(200, 200, (100, 100), 20)
        mask3 = generate_synthetic_water_mask(200, 200, (100, 100), 25)
        water_masks = [mask1, mask2, mask3]

    # Load deformation data if available
    deformation = None
    if hasattr(args, 'deformation_data') and args.deformation_data:
        try:
            import rasterio
            with rasterio.open(args.deformation_data) as src:
                deformation = src.read(1).astype(np.float64)
        except Exception as e:
            logger.warning(f"Failed to read deformation data: {e}")

    # Load exposure objects if available
    exposure_objects = []
    if hasattr(args, 'exposure_objects') and args.exposure_objects:
        try:
            exposure_objects = json.loads(
                Path(args.exposure_objects).read_text(encoding="utf-8")
            )
        except Exception as e:
            logger.warning(f"Failed to read exposure objects: {e}")

    # Load risk rules if available
    risk_rules = None
    if hasattr(args, 'risk_rules') and args.risk_rules:
        try:
            risk_rules = json.loads(
                Path(args.risk_rules).read_text(encoding="utf-8")
            )
        except Exception as e:
            logger.warning(f"Failed to read risk rules: {e}")

    # --- Core Analysis ---
    all_results = []
    facility_changes_features = []
    catchments_features = []
    screening_zones_features = []

    for facility in facilities:
        logger.info(f"Analyzing facility: {facility.name}")

        # Determine dam location in pixel space
        # For synthetic data, use center of DEM
        dam_row, dam_col = 100, 100
        if dem is not None:
            dam_row = dem.shape[0] // 2
            dam_col = dem.shape[1] // 2

        # Water surface change detection
        water_change = {}
        if len(water_masks) >= 2:
            water_change = detect_water_surface_change(
                water_masks[0], water_masks[-1], dem_transform
            )
            logger.info(f"Water change: {water_change['change_pct']}%")

            # Add change polygons to facility_changes
            for poly in water_change.get("expansion_polygons", []):
                props = dict(poly.get("properties", {}))
                props["facility_id"] = facility.fid
                props["change_type"] = "expansion"
                facility_changes_features.append({
                    "geometry": poly["geometry"],
                    "properties": props,
                })
            for poly in water_change.get("contraction_polygons", []):
                props = dict(poly.get("properties", {}))
                props["facility_id"] = facility.fid
                props["change_type"] = "contraction"
                facility_changes_features.append({
                    "geometry": poly["geometry"],
                    "properties": props,
                })

        # Catchment analysis
        catchment = {}
        if dem is not None:
            catchment = compute_catchment(dem, (dam_row, dam_col), dem_transform)
            logger.info(f"Catchment area: {catchment['catchment_area_km2']} km²")

            # Add catchment polygons
            for poly in catchment.get("catchment_polygons", []):
                props = dict(poly.get("properties", {}))
                props["facility_id"] = facility.fid
                catchments_features.append({
                    "geometry": poly["geometry"],
                    "properties": props,
                })

        # Runout analysis
        runout = {}
        if dem is not None:
            runout = compute_runout_zone(
                dem, (dam_row, dam_col),
                dam_height=facility.dam_height,
                transform=dem_transform,
                method=runout_method,
            )
            logger.info(f"Runout distance: {runout['runout_distance_m']} m")

            # Add runout polygons to screening zones
            for poly in runout.get("runout_polygons", []):
                props = dict(poly.get("properties", {}))
                props["facility_id"] = facility.fid
                props["zone_type"] = "runout"
                screening_zones_features.append({
                    "geometry": poly["geometry"],
                    "properties": props,
                })

        # Downstream exposure
        exposure = {}
        if dem is not None:
            exposure = compute_downstream_exposure(
                dem, (dam_row, dam_col),
                exposure_objects=exposure_objects,
                transform=dem_transform,
                radius=exposure_radius,
            )
            logger.info(f"Objects in zone: {exposure['n_objects_in_zone']}")

        # Deformation analysis
        def_analysis = {}
        if deformation is not None:
            def_analysis = analyze_deformation(deformation, deformation_threshold)
            logger.info(f"Max deformation: {def_analysis['max_deformation']} mm/yr")

        # Rainfall scenario
        rainfall = {}
        if catchment:
            rainfall = compute_rainfall_scenario(catchment, rainfall_scenario)
            logger.info(f"Peak flow: {rainfall['peak_flow_m3s']} m³/s")

        # Risk scoring
        risk = compute_risk_score(
            facility, water_change, catchment, runout, exposure, risk_rules
        )
        logger.info(f"Risk level: {risk['risk_level']}, Score: {risk['combined_score']}")

        # Compile result
        result = {
            "facility_id": facility.fid,
            "facility_name": facility.name,
            **risk,
            "water_change_pct": water_change.get("change_pct", 0),
            "catchment_area_km2": catchment.get("catchment_area_km2", 0),
            "runout_distance_m": runout.get("runout_distance_m", 0),
            "n_objects_in_zone": exposure.get("n_objects_in_zone", 0),
        }
        all_results.append(result)

    # --- Write Outputs ---

    # facility_changes.geojson
    facility_changes_geojson = {
        "type": "FeatureCollection",
        "features": facility_changes_features,
    }
    facility_changes_path = output_dir / "facility_changes.geojson"
    facility_changes_path.write_text(
        safe_json_dumps(facility_changes_geojson, ensure_ascii=False),
        encoding="utf-8",
    )

    # catchments.geojson
    catchments_geojson = {
        "type": "FeatureCollection",
        "features": catchments_features,
    }
    catchments_path = output_dir / "catchments.geojson"
    catchments_path.write_text(
        safe_json_dumps(catchments_geojson, ensure_ascii=False),
        encoding="utf-8",
    )

    # screening_zones.geojson
    screening_zones_geojson = {
        "type": "FeatureCollection",
        "features": screening_zones_features,
    }
    screening_zones_path = output_dir / "screening_zones.geojson"
    screening_zones_path.write_text(
        safe_json_dumps(screening_zones_geojson, ensure_ascii=False),
        encoding="utf-8",
    )

    # downstream_exposure.xlsx (CSV fallback)
    exposure_path = output_dir / "downstream_exposure.csv"
    with open(exposure_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "facility_id", "facility_name", "exposure_radius_m",
            "exposure_area_km2", "n_objects_in_zone", "object_types",
        ])
        writer.writeheader()
        for result in all_results:
            writer.writerow({
                "facility_id": result.get("facility_id", ""),
                "facility_name": result.get("facility_name", ""),
                "exposure_radius_m": exposure_radius,
                "exposure_area_km2": result.get("exposure_area_km2", ""),
                "n_objects_in_zone": result.get("n_objects_in_zone", ""),
                "object_types": json.dumps(result.get("object_types", {})),
            })

    # risk_report.html
    report_path = generate_risk_report(facilities, all_results, output_dir)

    # request.json
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "rainfall_scenario": rainfall_scenario,
        "runout_method": runout_method,
        "deformation_threshold": deformation_threshold,
        "exposure_radius": exposure_radius,
        "n_facilities": len(facilities),
        "n_water_periods": len(water_masks),
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
        "dem_source": getattr(args, 'dem_file', 'synthetic'),
        "water_masks_source": getattr(args, 'water_masks', 'synthetic'),
        "deformation_source": getattr(args, 'deformation_data', 'none'),
        "n_facilities": len(facilities),
        "n_water_periods": len(water_masks),
        "facilities": [
            {
                "fid": f.fid,
                "name": f.name,
                "has_critical_data": f.has_critical_data(),
                "data_completeness": f.data_completeness(),
            }
            for f in facilities
        ],
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # output-manifest.json
    output_files = {
        "facility_changes.geojson": str(facility_changes_path),
        "catchments.geojson": str(catchments_path),
        "screening_zones.geojson": str(screening_zones_path),
        "downstream_exposure.csv": str(exposure_path),
        "risk_report.html": str(report_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(dataset_path),
    }
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "analysis_parameters": request_info,
        "output_files": output_files,
        "results": all_results,
    }
    if fetch_meta:
        manifest["data_source"] = fetch_meta.get("data_source")
        manifest["fetched_at"] = fetch_meta.get("fetched_at")
        if fetch_meta.get("collection"):
            manifest["collection"] = fetch_meta["collection"]
        if fetch_meta.get("dem_path"):
            manifest["dem_downloaded"] = fetch_meta["dem_path"]
        if fetch_meta.get("sentinel2_paths"):
            manifest["sentinel2_downloaded"] = fetch_meta["sentinel2_paths"]
    manifest_path = output_dir / "output-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # qa.json
    qa = {
        "status": "complete",
        "checks": {
            "facilities_loaded": len(facilities) > 0,
            "dem_loaded": dem is not None,
            "water_masks_loaded": len(water_masks) >= 2,
            "catchment_computed": len(catchment) > 0,
            "runout_computed": len(runout) > 0,
            "risk_scored": len(all_results) > 0,
        },
        "warnings": [],
        "n_facilities": len(facilities),
        "n_results": len(all_results),
    }

    # Add warnings for missing data
    for facility in facilities:
        if not facility.has_critical_data():
            qa["warnings"].append(
                f"Facility {facility.fid}: missing dam_height or capacity"
            )

    qa_path = output_dir / "qa.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    logger.info("Analysis complete")
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Tailings Dam Risk Screening")
    parser.add_argument("--facilities", default=None,
                        help="Path to facilities JSON file")
    parser.add_argument("--dem-file", default=None,
                        help="Path to DEM GeoTIFF file")
    parser.add_argument("--water-masks", nargs="*", default=None,
                        help="Input water mask GeoTIFF files (ordered by time)")
    parser.add_argument("--deformation-data", default=None,
                        help="Path to deformation data GeoTIFF")
    parser.add_argument("--exposure-objects", default=None,
                        help="Path to exposure objects JSON file")
    parser.add_argument("--rainfall-scenario", default=DEFAULT_RAINFALL_SCENARIO,
                        choices=["100yr", "500yr", "1000yr"],
                        help="Rainfall scenario (default: 100yr)")
    parser.add_argument("--runout-method", default=DEFAULT_RUNOUT_METHOD,
                        choices=["simplified", "energy_line"],
                        help="Runout computation method (default: simplified)")
    parser.add_argument("--deformation-threshold", type=float,
                        default=DEFAULT_DEFORMATION_THRESHOLD,
                        help=f"Deformation threshold in mm/yr (default: {DEFAULT_DEFORMATION_THRESHOLD})")
    parser.add_argument("--exposure-radius", type=float,
                        default=DEFAULT_EXPOSURE_RADIUS,
                        help=f"Exposure radius in meters (default: {DEFAULT_EXPOSURE_RADIUS})")
    parser.add_argument("--risk-rules", default=None,
                        help="Path to risk scoring rules JSON file")
    parser.add_argument("--output-dir", "-o", default="tdr-output",
                        help="Output directory (default: tdr-output)")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    if add_bbox_date_args is not None:
        add_bbox_date_args(parser)

    args = parser.parse_args()

    try:
        sys.exit(run_analysis(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
