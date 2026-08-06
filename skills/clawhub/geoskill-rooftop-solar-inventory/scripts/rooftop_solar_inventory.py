#!/usr/bin/env python3
"""
Rooftop Solar Inventory - Building-level rooftop solar potential assessment.

Extracts roof planes, computes slope/aspect, shading, usable area,
and estimates installed capacity, energy yield, and economic viability.

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
    """Auto-download building footprints (ms-buildings) and NASA POWER GHI."""
    if not _HAS_FETCHER:
        return {}
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        return {}

    needs_buildings = not getattr(args, "buildings", None) or not Path(args.buildings).exists()
    if not needs_buildings:
        return {}

    metadata: Dict[str, Any] = {
        "data_source": "MPC+NASA_POWER",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "bbox": bbox.to_list(),
    }
    down_dir = output_dir / "downloaded"
    down_dir.mkdir(parents=True, exist_ok=True)

    # 1) MS Buildings (Microsoft Planetary Computer)
    try:
        mpc_fetcher = DataFetcher(source=DataSource.PLANETARY_COMPUTER)
        items = mpc_fetcher.search_stac(
            collection="ms-buildings",
            bbox=bbox,
            date_range=DateRange("2020-01-01", "2024-12-31"),
            limit=3,
        )
        if items:
            paths = mpc_fetcher.download_assets(
                items=items, out_dir=down_dir, max_items=1, max_total_mb=200.0,
            )
            if paths:
                args.buildings = str(paths[0])
                metadata["buildings_source"] = "MPC"
                metadata["buildings_collection"] = "ms-buildings"
                metadata["buildings_path"] = str(paths[0])
                metadata["buildings_item_count"] = len(items)
                print(f"  Auto-downloaded MS Buildings: {paths[0]}")
        else:
            print(f"WARNING: ms-buildings search returned 0 items in {bbox.to_string()}", file=sys.stderr)
    except Exception as exc:
        print(f"WARNING: MS Buildings download failed: {exc}", file=sys.stderr)

    # 2) NASA POWER GHI (ALLSKY_SFC_SW_DWN) — daily mean for the bbox centroid
    try:
        dr = parse_date_range_arg(getattr(args, "date_range", None)) or DateRange(
            "2023-01-01", "2023-12-31"
        )
        power_fetcher = DataFetcher(source=DataSource.NASA_POWER)
        df = power_fetcher.fetch_power(
            parameters=["ALLSKY_SFC_SW_DWN", "T2M"],
            bbox=bbox,
            date_range=dr,
            resolution="daily",
        )
        power_path = output_dir / "nasa_power_ghi.csv"
        df.to_csv(power_path)
        # Update the default annual_ghi with the computed mean if user didn't override
        if not getattr(args, "annual_ghi", None) and len(df) > 0 and "ALLSKY_SFC_SW_DWN" in df.columns:
            mean_ghi = float(df["ALLSKY_SFC_SW_DWN"].mean())
            # Annual GHI in kWh/m2 = daily mean (kWh/m2/day) * 365
            args.annual_ghi = round(mean_ghi * 365.0, 1)
        metadata["nasa_power_source"] = "NASA POWER"
        metadata["nasa_power_path"] = str(power_path)
        metadata["nasa_power_parameter"] = "ALLSKY_SFC_SW_DWN"
        print(f"  Auto-downloaded NASA POWER GHI → {power_path}")
    except Exception as exc:
        print(f"WARNING: NASA POWER download failed: {exc}", file=sys.stderr)

    return metadata



EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# Quality codes
QUALITY_HIGH = 1
QUALITY_MEDIUM = 2
QUALITY_LOW = 3
QUALITY_INVALID = 4

# Roof type codes
ROOF_FLAT = 0
ROOF_SINGLE_SLOPE = 1
ROOF_GABLE = 2
ROOF_COMPLEX = 3

# Default parameters
DEFAULT_SETBACK_M = 1.0
DEFAULT_MIN_CONTIGUOUS_AREA_M2 = 10.0
DEFAULT_MIN_ROOF_AREA_M2 = 20.0
DEFAULT_MAX_SLOPE_DEG = 45.0
DEFAULT_PANEL_TYPE = "mono_perc_540w"
DEFAULT_PERFORMANCE_RATIO = 0.82
DEFAULT_SYSTEM_LIFETIME = 25
DEFAULT_ELECTRICITY_PRICE = 0.55
DEFAULT_DISCOUNT_RATE = 0.06
DEFAULT_ANNUAL_GHI = 1400.0
DEFAULT_PEAK_SUN_HOURS = 4.0

# ============================================================
# Geometry Helpers
# ============================================================

def create_polygon(x, y, w, h):
    """Create a shapely polygon (box)."""
    from shapely.geometry import box
    return box(x, y, x + w, y + h)


def _geom_area(geom: Dict) -> float:
    """Compute area from a GeoJSON-like geometry dict."""
    from shapely.geometry import shape
    try:
        return shape(geom).area
    except Exception:
        return 0.0


def _extract_points(geom) -> List:
    """Extract points from a shapely geometry."""
    from shapely.geometry import Point, MultiPoint, LineString, MultiLineString

    if geom.is_empty:
        return []

    if geom.geom_type == "Point":
        return [geom]
    elif geom.geom_type == "MultiPoint":
        return list(geom.geoms)
    elif geom.geom_type == "LineString":
        return [geom.interpolate(0, normalized=True)]
    elif geom.geom_type == "MultiLineString":
        return [g.interpolate(0, normalized=True) for g in geom.geoms]
    elif geom.geom_type == "GeometryCollection":
        points = []
        for g in geom.geoms:
            points.extend(_extract_points(g))
        return points
    else:
        return []


# ============================================================
# Roof Plane Extraction
# ============================================================

def extract_roof_planes(building_geom, dsm: Optional[np.ndarray] = None,
                        transform=None, pixel_size: float = 1.0) -> List[Dict]:
    """
    Extract roof planes from building geometry and optional DSM.

    Without DSM: assumes flat roof (single plane = building footprint).
    With DSM: segments roof into planes based on slope/aspect clustering.

    Args:
        building_geom: Shapely Polygon or dict geometry
        dsm: Digital Surface Model array (optional)
        transform: Affine transform
        pixel_size: Pixel size in map units

    Returns:
        List of roof plane features with geometry and properties
    """
    from shapely.geometry import shape, mapping, Polygon

    if isinstance(building_geom, dict):
        building = shape(building_geom)
    else:
        building = building_geom

    if building.is_empty or building.area == 0:
        return []

    if dsm is None:
        # No DSM: assume flat roof
        return [{
            "geometry": mapping(building),
            "properties": {
                "area_m2": building.area,
                "slope_deg": 0.0,
                "aspect_deg": 0.0,
                "roof_type": ROOF_FLAT,
                "quality": QUALITY_LOW,
                "note": "no_dsm_assumed_flat",
            },
        }]

    # With DSM: segment roof into planes
    return _segment_roof_planes_dsm(building, dsm, transform, pixel_size)


def _segment_roof_planes_dsm(building, dsm: np.ndarray, transform,
                             pixel_size: float) -> List[Dict]:
    """Segment roof planes from DSM using slope/aspect clustering."""
    from shapely.geometry import mapping
    from rasterio.transform import from_bounds
    from rasterio.features import shapes as rasterio_shapes

    if transform is None:
        rows, cols = dsm.shape
        transform = from_bounds(0, 0, cols * pixel_size, rows * pixel_size, cols, rows)

    # Compute slope and aspect from DSM
    slope, aspect = compute_slope_aspect(dsm, pixel_size)

    # Mask to building footprint
    # Simplified: use bounding box of building
    minx, miny, maxx, maxy = building.bounds

    # Convert bounds to pixel coordinates
    inv_transform = ~transform
    col_min, row_max = inv_transform * (minx, miny)
    col_max, row_min = inv_transform * (maxx, maxy)
    col_min, col_max = int(max(0, col_min)), int(min(dsm.shape[1], col_max))
    row_min, row_max = int(max(0, row_min)), int(min(dsm.shape[0], row_max))

    if col_max <= col_min or row_max <= row_min:
        return [{
            "geometry": mapping(building),
            "properties": {
                "area_m2": building.area,
                "slope_deg": 0.0,
                "aspect_deg": 0.0,
                "roof_type": ROOF_FLAT,
                "quality": QUALITY_LOW,
                "note": "dsm_outside_bounds",
            },
        }]

    # Extract building region
    building_slope = slope[row_min:row_max, col_min:col_max]
    building_aspect = aspect[row_min:row_max, col_min:col_max]

    # Cluster by slope and aspect into planes
    # Simple approach: group by slope ranges
    planes = _cluster_planes_by_slope(building, building_slope, building_aspect,
                                       row_min, col_min, transform, pixel_size)

    if not planes:
        return [{
            "geometry": mapping(building),
            "properties": {
                "area_m2": building.area,
                "slope_deg": float(np.mean(building_slope)),
                "aspect_deg": 0.0,
                "roof_type": ROOF_FLAT,
                "quality": QUALITY_MEDIUM,
                "note": "clustering_failed_assumed_flat",
            },
        }]

    return planes


def _cluster_planes_by_slope(building, slope_region, aspect_region,
                              row_offset, col_offset, transform,
                              pixel_size: float) -> List[Dict]:
    """Cluster roof region into planes based on slope similarity."""
    from shapely.geometry import mapping, box, shape
    from shapely.ops import unary_union

    rows, cols = slope_region.shape
    if rows < 2 or cols < 2:
        return []

    # Classify pixels: flat (<5°), moderate (5-30°), steep (>30°)
    flat_mask = slope_region < 5.0
    moderate_mask = (slope_region >= 5.0) & (slope_region < 30.0)
    steep_mask = slope_region >= 30.0

    planes = []
    plane_id = 0

    for mask, roof_type, type_name in [
        (flat_mask, ROOF_FLAT, "flat"),
        (moderate_mask, ROOF_SINGLE_SLOPE, "single_slope"),
        (steep_mask, ROOF_COMPLEX, "steep"),
    ]:
        if not np.any(mask):
            continue

        # Find connected components
        labeled, n_components = _label_connected_components(mask.astype(np.uint8))

        for comp_id in range(1, n_components + 1):
            comp_mask = labeled == comp_id
            area_pixels = np.sum(comp_mask)
            area_m2 = area_pixels * pixel_size * pixel_size

            if area_m2 < DEFAULT_MIN_CONTIGUOUS_AREA_M2:
                continue

            # Get bounding box of component
            comp_rows, comp_cols = np.where(comp_mask)
            min_r, max_r = comp_rows.min(), comp_rows.max()
            min_c, max_c = comp_cols.min(), comp_cols.max()

            # Convert to map coordinates
            abs_r_min = row_offset + min_r
            abs_r_max = row_offset + max_r + 1
            abs_c_min = col_offset + min_c
            abs_c_max = col_offset + max_c + 1

            x1, y1 = transform * (abs_c_min, abs_r_max)
            x2, y2 = transform * (abs_c_max, abs_r_min)

            plane_poly = box(x1, y1, x2, y2)

            # Intersect with building
            try:
                plane_poly = plane_poly.intersection(building)
            except Exception:
                pass

            if plane_poly.is_empty or plane_poly.area < DEFAULT_MIN_CONTIGUOUS_AREA_M2:
                continue

            avg_slope = float(np.mean(slope_region[comp_mask]))
            avg_aspect = float(np.mean(aspect_region[comp_mask]))

            planes.append({
                "geometry": mapping(plane_poly),
                "properties": {
                    "area_m2": round(plane_poly.area, 2),
                    "slope_deg": round(avg_slope, 2),
                    "aspect_deg": round(avg_aspect, 2),
                    "roof_type": roof_type,
                    "quality": QUALITY_HIGH,
                    "note": f"dsm_segmented_{type_name}",
                },
            })
            plane_id += 1

    return planes


def _label_connected_components(mask: np.ndarray) -> Tuple[np.ndarray, int]:
    """Label connected components in a binary mask."""
    from scipy import ndimage
    labeled, n_components = ndimage.label(mask)
    return labeled, n_components


# ============================================================
# Slope and Aspect Computation
# ============================================================

def compute_slope_aspect(dsm: np.ndarray, pixel_size: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute slope and aspect from DSM using gradient method.

    Args:
        dsm: Digital Surface Model (2D array)
        pixel_size: Pixel size in map units

    Tuple of (slope, aspect) in degrees.
    """
    # Compute gradients
    gy, gx = np.gradient(dsm, pixel_size)

    # Slope in degrees
    slope = np.degrees(np.arctan(np.sqrt(gx**2 + gy**2)))

    # Aspect in degrees (0=North, 90=East, 180=South, 270=West)
    aspect = np.degrees(np.arctan2(-gx, gy))
    aspect = np.where(aspect < 0, aspect + 360, aspect)

    return slope, aspect


# ============================================================
# Shading Computation
# ============================================================

def compute_shading(dsm: np.ndarray, azimuth: float = 180.0,
                    altitude: float = 45.0, pixel_size: float = 1.0) -> np.ndarray:
    """
    Compute shading mask from DSM for given sun position.

    Uses ray-casting approach: for each pixel, check if terrain
    blocks the sun at the given azimuth and altitude.

    Args:
        dsm: Digital Surface Model
        azimuth: Sun azimuth in degrees (0=N, 90=E, 180=S)
        altitude: Sun altitude in degrees (0=horizon, 90=zenith)
        pixel_size: Pixel size in map units

    Returns:
        Binary mask (1=shaded, 0=sunlit)
    """
    rows, cols = dsm.shape
    shaded = np.zeros_like(dsm, dtype=np.uint8)

    if altitude <= 0:
        shaded[:] = 1
        return shaded

    # Convert azimuth to direction vector
    # Azimuth: 0=N, 90=E, 180=S, 270=W
    az_rad = np.radians(azimuth)
    dx = np.sin(az_rad)
    dy = np.cos(az_rad)

    # Step along sun direction and check for occluders
    max_distance = max(rows, cols)
    step_size = pixel_size * 0.5

    for r in range(rows):
        for c in range(cols):
            z0 = dsm[r, c]
            # Cast ray toward sun
            dist = step_size
            while dist < max_distance:
                # Position along ray (toward sun = opposite of shadow direction)
                nr = r + (dy * dist / pixel_size)
                nc = c + (dx * dist / pixel_size)

                nr_int = int(round(nr))
                nc_int = int(round(nc))

                if nr_int < 0 or nr_int >= rows or nc_int < 0 or nc_int >= cols:
                    break

                # Required altitude angle to clear this point
                z_terrain = dsm[nr_int, nc_int]
                required_alt = np.degrees(np.arctan2(z_terrain - z0, dist))

                if required_alt > altitude:
                    shaded[r, c] = 1
                    break

                dist += step_size

    return shaded


def compute_shading_multipass(dsm: np.ndarray, sun_positions: List[Tuple[float, float]],
                               pixel_size: float = 1.0) -> np.ndarray:
    """
    Compute annual shading from multiple sun positions.

    Args:
        dsm: Digital Surface Model
        sun_positions: List of (azimuth, altitude) tuples
        pixel_size: Pixel size in map units

    Returns:
        Fraction of time shaded (0-1)
    """
    if not sun_positions:
        return np.zeros_like(dsm, dtype=np.float64)

    shading_sum = np.zeros_like(dsm, dtype=np.float64)
    for azimuth, altitude in sun_positions:
        shading_sum += compute_shading(dsm, azimuth, altitude, pixel_size)

    return shading_sum / len(sun_positions)


# ============================================================
# Usable Area Computation
# ============================================================

def compute_usable_area(roof_plane: Dict, setback_m: float = DEFAULT_SETBACK_M,
                        obstacles: Optional[List[Dict]] = None,
                        min_area: float = DEFAULT_MIN_CONTIGUOUS_AREA_M2) -> Dict:
    """
    Compute usable area for solar installation on a roof plane.

    Subtracts:
    - Edge setback (buffer inward)
    - Obstacles (HVAC, vents, etc.)
    - Minimum contiguous area filter

    Args:
        roof_plane: Roof plane feature dict
        setback_m: Edge setback distance in meters
        obstacles: List of obstacle geometries (optional)
        min_area: Minimum contiguous area in m2

    Returns:
        Dict with usable area info
    """
    from shapely.geometry import shape, mapping
    from shapely.ops import unary_union

    geom = roof_plane["geometry"]
    if isinstance(geom, dict):
        roof = shape(geom)
    else:
        roof = geom

    if roof.is_empty:
        return {
            "usable_area_m2": 0.0,
            "usable_fraction": 0.0,
            "geometry": mapping(roof),
            "note": "empty_roof",
        }

    original_area = roof.area

    # Apply setback (negative buffer)
    try:
        usable = roof.buffer(-setback_m)
    except Exception:
        usable = roof

    if usable.is_empty or usable.area < min_area:
        return {
            "usable_area_m2": 0.0,
            "usable_fraction": 0.0,
            "geometry": mapping(roof),
            "note": "setback_too_large",
        }

    # Subtract obstacles
    if obstacles:
        obstacle_geoms = []
        for obs in obstacles:
            try:
                obs_geom = obs["geometry"] if isinstance(obs["geometry"], dict) else obs["geometry"]
                if isinstance(obs_geom, dict):
                    obstacle_geoms.append(shape(obs_geom))
                else:
                    obstacle_geoms.append(obs_geom)
            except Exception:
                pass

        if obstacle_geoms:
            try:
                obstacle_union = unary_union(obstacle_geoms)
                usable = usable.difference(obstacle_union)
            except Exception:
                pass

    if usable.is_empty:
        return {
            "usable_area_m2": 0.0,
            "usable_fraction": 0.0,
            "geometry": mapping(roof),
            "note": "obstacles_cover_all",
        }

    # Handle MultiPolygon - take largest component
    if usable.geom_type == "MultiPolygon":
        usable = max(usable.geoms, key=lambda p: p.area)

    usable_area = usable.area
    if usable_area < min_area:
        return {
            "usable_area_m2": 0.0,
            "usable_fraction": 0.0,
            "geometry": mapping(roof),
            "note": "below_min_area",
        }

    return {
        "usable_area_m2": round(usable_area, 2),
        "usable_fraction": round(usable_area / original_area, 4) if original_area > 0 else 0.0,
        "geometry": mapping(usable),
        "note": "ok",
    }


# ============================================================
# Solar Potential Computation
# ============================================================

def compute_installed_capacity(usable_area_m2: float, panel_type: str = DEFAULT_PANEL_TYPE,
                                panel_specs: Optional[Dict] = None) -> Dict:
    """
    Compute installed capacity from usable area and panel specifications.

    Args:
        usable_area_m2: Usable roof area in m2
        panel_type: Panel type key
        panel_specs: Panel specifications dict (optional)

    Returns:
        Dict with capacity info
    """
    if panel_specs is None:
        panel_specs = _get_default_panel_specs(panel_type)

    panel_area = panel_specs.get("area_m2", 2.5)
    peak_power = panel_specs.get("peak_power_wp", 540)
    spacing_ratio = panel_specs.get("spacing_ratio", 0.5)

    # Effective area per panel (including spacing)
    effective_area_per_panel = panel_area * (1 + spacing_ratio)

    # Number of panels
    n_panels = int(usable_area_m2 / effective_area_per_panel)

    # Installed capacity
    capacity_kw = (n_panels * peak_power) / 1000.0

    return {
        "n_panels": n_panels,
        "capacity_kw": round(capacity_kw, 2),
        "panel_type": panel_type,
        "panel_area_m2": panel_area,
        "peak_power_wp": peak_power,
        "usable_area_m2": round(usable_area_m2, 2),
        "coverage_ratio": round(n_panels * panel_area / usable_area_m2, 4) if usable_area_m2 > 0 else 0,
    }


def compute_energy_yield(capacity_kw: float, annual_ghi: float = DEFAULT_ANNUAL_GHI,
                          performance_ratio: float = DEFAULT_PERFORMANCE_RATIO,
                          slope_deg: float = 0.0, aspect_deg: float = 180.0,
                          shading_fraction: float = 0.0) -> Dict:
    """
    Compute annual energy yield.

    Uses simplified PVWatts model:
    E = P * GHI/PR * (1 - shading) * orientation_factor

    Args:
        capacity_kw: Installed capacity in kW
        annual_ghi: Annual Global Horizontal Irradiance in kWh/m2
        performance_ratio: System performance ratio
        slope_deg: Roof slope in degrees
        aspect_deg: Roof aspect in degrees (0=N, 90=E, 180=S)
        shading_fraction: Fraction of time shaded (0-1)

    Returns:
        Dict with energy yield info
    """
    # Orientation factor: optimal is south-facing (180°) at ~30° tilt
    # Simplified model
    orientation_factor = _compute_orientation_factor(slope_deg, aspect_deg)

    # Annual energy yield (kWh)
    annual_kwh = capacity_kw * (annual_ghi / 1.0) * performance_ratio * orientation_factor * (1 - shading_fraction)

    # Specific yield (kW/kWp)
    specific_yield = annual_kwh / capacity_kw if capacity_kw > 0 else 0

    # Capacity factor
    capacity_factor = annual_kwh / (capacity_kw * 8760) if capacity_kw > 0 else 0

    return {
        "annual_kwh": round(annual_kwh, 1),
        "specific_yield_kwh_per_kw": round(specific_yield, 1),
        "capacity_factor": round(capacity_factor, 4),
        "orientation_factor": round(orientation_factor, 4),
        "performance_ratio": performance_ratio,
        "shading_loss_pct": round(shading_fraction * 100, 2),
    }


def _compute_orientation_factor(slope_deg: float, aspect_deg: float) -> float:
    """
    Compute orientation factor relative to optimal (south-facing, 30° tilt).

    For flat roofs (<=5°), assumes tilted mounting at optimal angle.
    For sloped roofs, computes based on actual orientation.
    Simplified model for Northern Hemisphere.
    """
    # Flat roofs: assume tilted mounting at ~30° facing south
    if slope_deg <= 5.0:
        return 0.95  # Near-optimal with tilted mounting

    # Optimal: slope=30°, aspect=180° (south)
    optimal_slope = 30.0
    optimal_aspect = 180.0

    # Slope factor: 1.0 at optimal, decreases for steeper
    slope_diff = abs(slope_deg - optimal_slope)
    slope_factor = max(0.75, 1.0 - slope_diff / 120.0)

    # Aspect factor: 1.0 at south, 0.65 at north
    aspect_diff = abs(aspect_deg - optimal_aspect)
    if aspect_diff > 180:
        aspect_diff = 360 - aspect_diff
    aspect_factor = max(0.65, 1.0 - aspect_diff / 250.0)

    return slope_factor * aspect_factor


# ============================================================
# Economic Analysis
# ============================================================

def compute_economic_analysis(capacity_kw: float, annual_kwh: float,
                               system_config: Optional[Dict] = None) -> Dict:
    """
    Compute economic metrics for solar installation.

    Args:
        capacity_kw: Installed capacity in kW
        annual_kwh: Annual energy yield in kWh
        system_config: Economic parameters (optional)

    Returns:
        Dict with economic metrics
    """
    if system_config is None:
        system_config = {}

    electricity_price = system_config.get("electricity_price_cny_per_kwh", DEFAULT_ELECTRICITY_PRICE)
    feed_in_tariff = system_config.get("feed_in_tariff_cny_per_kwh", 0.42)
    self_consumption_ratio = system_config.get("self_consumption_ratio", 0.7)
    system_lifetime = system_config.get("system_lifetime_years", DEFAULT_SYSTEM_LIFETIME)
    discount_rate = system_config.get("discount_rate", DEFAULT_DISCOUNT_RATE)
    om_cost_pct = system_config.get("om_cost_annual_pct", 0.01)

    # Get panel cost
    panel_type = system_config.get("panel_type", DEFAULT_PANEL_TYPE)
    panel_specs = _get_default_panel_specs(panel_type)
    cost_per_wp = panel_specs.get("cost_per_wp_cny", 0.85)

    # Total system cost (includes BOS, installation, etc.)
    # Total cost = panel cost * 1.5 (BOS factor)
    total_cost_cny = capacity_kw * 1000 * cost_per_wp * 1.5

    # Annual revenue
    self_consumed = annual_kwh * self_consumption_ratio
    exported = annual_kwh * (1 - self_consumption_ratio)
    annual_revenue = self_consumed * electricity_price + exported * feed_in_tariff

    # Annual O&M cost
    annual_om = total_cost_cny * om_cost_pct

    # Net annual benefit
    annual_net = annual_revenue - annual_om

    # Simple payback period
    payback_years = total_cost_cny / annual_net if annual_net > 0 else float('inf')

    # NPV over system lifetime
    npv = -total_cost_cny
    degradation = panel_specs.get("degradation_rate", 0.0055)
    for year in range(1, system_lifetime + 1):
        year_revenue = annual_revenue * (1 - degradation) ** year
        year_net = year_revenue - annual_om
        npv += year_net / (1 + discount_rate) ** year

    # LCOE
    total_generation = sum(
        annual_kwh * (1 - degradation) ** y / (1 + discount_rate) ** y
        for y in range(1, system_lifetime + 1)
    )
    total_costs = total_cost_cny + sum(
        annual_om / (1 + discount_rate) ** y
        for y in range(1, system_lifetime + 1)
    )
    lcoe = total_costs / total_generation if total_generation > 0 else 0

    return {
        "total_investment_cny": round(total_cost_cny, 2),
        "annual_revenue_cny": round(annual_revenue, 2),
        "annual_om_cny": round(annual_om, 2),
        "annual_net_benefit_cny": round(annual_net, 2),
        "payback_years": round(payback_years, 2) if payback_years < 100 else 999,
        "npv_cny": round(npv, 2),
        "lcoe_cny_per_kwh": round(lcoe, 4),
        "system_lifetime_years": system_lifetime,
    }


# ============================================================
# Building Ranking
# ============================================================

def rank_buildings(building_results: List[Dict],
                   weight_capacity: float = 0.4,
                   weight_economics: float = 0.3,
                   weight_solar: float = 0.3) -> List[Dict]:
    """
    Rank buildings by solar potential.

    Composite score based on:
    - Installed capacity (40%)
    - Economic viability (30%)
    - Solar resource quality (30%)

    Args:
        building_results: List of building analysis results
        weight_capacity: Weight for capacity score
        weight_economics: Weight for economics score
        weight_solar: Weight for solar resource score

    Returns:
        Sorted list with ranking added
    """
    if not building_results:
        return []

    # Extract metrics for normalization
    capacities = [b.get("capacity_kw", 0) for b in building_results]
    npvs = [b.get("npv_cny", 0) for b in building_results]
    specific_yields = [b.get("specific_yield", 0) for b in building_results]

    max_capacity = max(capacities) if capacities else 1
    max_npv = max(npvs) if npvs else 1
    max_sy = max(specific_yields) if specific_yields else 1

    for b in building_results:
        cap_score = b.get("capacity_kw", 0) / max_capacity if max_capacity > 0 else 0
        econ_score = b.get("npv_cny", 0) / max_npv if max_npv > 0 else 0
        solar_score = b.get("specific_yield", 0) / max_sy if max_sy > 0 else 0

        composite = (weight_capacity * cap_score +
                     weight_economics * econ_score +
                     weight_solar * solar_score)

        b["score"] = round(composite, 4)
        b["rank"] = 0  # Will be set after sorting

    # Sort by score descending
    building_results.sort(key=lambda x: x.get("score", 0), reverse=True)

    for i, b in enumerate(building_results):
        b["rank"] = i + 1

    return building_results


# ============================================================
# Synthetic Data Generation
# ============================================================

def generate_synthetic_buildings(n_buildings: int = 5, area_size: float = 200.0,
                                  seed: int = 42) -> List[Dict]:
    """
    Generate synthetic building footprints for testing.

    Args:
        n_buildings: Number of buildings to generate
        area_size: Size of the area (square side length)
        seed: Random seed

    Returns:
        List of building feature dicts
    """
    from shapely.geometry import mapping

    rng = np.random.RandomState(seed)
    buildings = []

    for i in range(n_buildings):
        # Random position
        x = rng.uniform(10, area_size - 30)
        y = rng.uniform(10, area_size - 30)

        # Random size (10-30m)
        w = rng.uniform(10, 30)
        h = rng.uniform(10, 30)

        poly = create_polygon(x, y, w, h)

        buildings.append({
            "geometry": mapping(poly),
            "properties": {
                "building_id": i,
                "building_type": ["residential", "commercial", "industrial"][i % 3],
                "floors": int(rng.randint(1, 10)),
                "footprint_area_m2": round(poly.area, 2),
            },
        })

    return buildings


def generate_synthetic_dsm(buildings: List[Dict], area_size: float = 200.0,
                            pixel_size: float = 1.0, roof_height: float = 10.0,
                            seed: int = 42) -> np.ndarray:
    """
    Generate a synthetic DSM with buildings as raised plateaus.

    Args:
        buildings: List of building features
        area_size: Size of the area
        pixel_size: Pixel size
        roof_height: Height of buildings
        seed: Random seed

    Returns:
        DSM array
    """
    from shapely.geometry import shape

    n_pixels = int(area_size / pixel_size)
    dsm = np.zeros((n_pixels, n_pixels), dtype=np.float64)

    # Add some terrain variation
    rng = np.random.RandomState(seed)
    terrain = rng.uniform(0, 2, (n_pixels, n_pixels))
    # Smooth terrain
    from scipy.ndimage import gaussian_filter
    terrain = gaussian_filter(terrain, sigma=5)
    dsm += terrain

    # Add buildings as raised areas
    for b in buildings:
        geom = b["geometry"]
        if isinstance(geom, dict):
            poly = shape(geom)
        else:
            poly = geom

        minx, miny, maxx, maxy = poly.bounds
        col_min = max(0, int(minx / pixel_size))
        col_max = min(n_pixels, int(np.ceil(maxx / pixel_size)))
        row_min = max(0, int(miny / pixel_size))
        row_max = min(n_pixels, int(np.ceil(maxy / pixel_size)))

        for r in range(row_min, row_max):
            for c in range(col_min, col_max):
                x = c * pixel_size + pixel_size / 2
                y = r * pixel_size + pixel_size / 2
                from shapely.geometry import Point
                if poly.contains(Point(x, y)):
                    dsm[r, c] += roof_height

    return dsm


# ============================================================
# Panel Specs Helper
# ============================================================

def _get_default_panel_specs(panel_type: str) -> Dict:
    """Get default panel specifications."""
    defaults = {
        "mono_perc_540w": {
            "peak_power_wp": 540,
            "area_m2": 2.583,
            "efficiency": 0.209,
            "degradation_rate": 0.0055,
            "cost_per_wp_cny": 0.85,
            "spacing_ratio": 0.5,
        },
        "mono_perc_600w": {
            "peak_power_wp": 600,
            "area_m2": 2.968,
            "efficiency": 0.202,
            "degradation_rate": 0.0055,
            "cost_per_wp_cny": 0.80,
            "spacing_ratio": 0.5,
        },
        "hjt_700w": {
            "peak_power_wp": 700,
            "area_m2": 3.106,
            "efficiency": 0.225,
            "degradation_rate": 0.004,
            "cost_per_wp_cny": 1.10,
            "spacing_ratio": 0.5,
        },
    }
    return defaults.get(panel_type, defaults["mono_perc_540w"])


# ============================================================
# Main Analysis Pipeline
# ============================================================

def auto_download_buildings(args, output_dir: Path) -> Dict[str, Any]:
    """Download ms-buildings + NASA POWER GHI using --bbox + --date-range.

    Returns metadata dict (also writes the path back to args.buildings).
    """
    if not _HAS_FETCHER:
        raise RuntimeError(
            "Shared data fetcher not importable. Pass --buildings <local.geojson> instead, "
            "or ensure _geoskill_data_fetcher is on sys.path."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_buildings requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        dr = DateRange("2020-01-01", "2024-12-31")
    cache_dir = getattr(args, "cache_dir", None)
    metadata: Dict[str, Any] = {
        "data_source": "MPC+NASA_POWER",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
    }

    # 1) MS Buildings (Microsoft Planetary Computer)
    mpc_fetcher = DataFetcher(
        source=DataSource.PLANETARY_COMPUTER,
        cache_dir=Path(cache_dir) if cache_dir else None,
    )
    download_dir = output_dir / "downloaded"
    download_dir.mkdir(parents=True, exist_ok=True)
    # ms-buildings is a static collection (Bing imagery 2014-2021), use wide range
    try:
        items = mpc_fetcher.search_stac(
            collection="ms-buildings",
            bbox=bbox,
            date_range=DateRange("2018-01-01", "2024-12-31"),
            limit=3,
        )
        if items:
            paths = mpc_fetcher.download_assets(
                items=items, out_dir=download_dir, max_items=1, max_total_mb=500,
                prefer_assets=['data'],
            )
            if paths:
                args.buildings = str(paths[0])
                metadata["collection"] = "ms-buildings"
                metadata["n_items_searched"] = len(items)
                metadata["downloaded_paths"] = [str(p) for p in paths]
                print(f"  Auto-downloaded MS Buildings: {paths[0]}")
            else:
                print("WARNING: ms-buildings download returned no files", file=sys.stderr)
        else:
            print(f"WARNING: ms-buildings search returned 0 items in {bbox.to_string()}", file=sys.stderr)
    except Exception as exc:
        # ms-buildings uses Azure blob URLs (abfs://) which the shared fetcher
        # can't download. Record the error and continue so NASA POWER still runs.
        print(f"WARNING: ms-buildings auto-download failed: {exc}", file=sys.stderr)
        metadata["ms_buildings_error"] = str(exc)

    # 2) NASA POWER GHI (ALLSKY_SFC_SW_DWN) — daily mean for bbox centroid
    try:
        power_fetcher = DataFetcher(source=DataSource.NASA_POWER)
        ghi_dr = DateRange("2023-01-01", "2023-12-31")
        df = power_fetcher.fetch_power(
            parameters=["ALLSKY_SFC_SW_DWN", "T2M"],
            bbox=bbox,
            date_range=ghi_dr,
            resolution="daily",
        )
        power_path = output_dir / "nasa_power_ghi.csv"
        df.to_csv(power_path)
        # Update the default annual_ghi with the computed mean if user didn't override
        if not getattr(args, "annual_ghi", None) and len(df) > 0 and "ALLSKY_SFC_SW_DWN" in df.columns:
            mean_ghi = float(df["ALLSKY_SFC_SW_DWN"].mean())
            # Annual GHI in kWh/m2 = daily mean (kWh/m2/day) * 365
            args.annual_ghi = round(mean_ghi * 365.0, 1)
        metadata["nasa_power_path"] = str(power_path)
        metadata["nasa_power_parameter"] = "ALLSKY_SFC_SW_DWN"
        print(f"  Auto-downloaded NASA POWER GHI → {power_path}")
    except Exception as exc:
        print(f"WARNING: NASA POWER download failed: {exc}", file=sys.stderr)
        metadata["nasa_power_error"] = str(exc)

    return metadata


def run_analysis(args: argparse.Namespace) -> int:
    """Main analysis workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("rsi-output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # --- Auto-download mode: fetch ms-buildings + NASA POWER from MPC ---
    fetch_meta: Dict[str, Any] = {}
    if (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)) and not getattr(args, "buildings", None):
        try:
            fetch_meta = auto_download_buildings(args, output_dir)
            print(f"  Auto-download complete (buildings={args.buildings})")
        except Exception as e:
            # ms-buildings uses Azure blob URLs (abfs://) which the shared
            # fetcher can't download. Fall back to synthetic buildings so
            # the user can still run the analysis.
            print(f"WARNING: auto-download failed ({e}); falling back to synthetic buildings",
                  file=sys.stderr)
            fetch_meta = {"data_source": "MPC+NASA_POWER", "fetched_at": datetime.now(timezone.utc).isoformat(),
                          "collection": "ms-buildings", "download_error": str(e)}

    # Setup logging
    log_path = output_dir / "run.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )
    logger = logging.getLogger(__name__)

    logger.info("Rooftop Solar Inventory Analysis Started")

    # Parse parameters
    setback_m = getattr(args, 'setback', None) or DEFAULT_SETBACK_M
    panel_type = getattr(args, 'panel_type', None) or DEFAULT_PANEL_TYPE
    min_contiguous_area = getattr(args, 'min_contiguous_area', None) or DEFAULT_MIN_CONTIGUOUS_AREA_M2
    annual_ghi = getattr(args, 'annual_ghi', None) or DEFAULT_ANNUAL_GHI
    performance_ratio = getattr(args, 'performance_ratio', None) or DEFAULT_PERFORMANCE_RATIO
    electricity_price = getattr(args, 'electricity_price', None) or DEFAULT_ELECTRICITY_PRICE
    discount_rate = getattr(args, 'discount_rate', None) or DEFAULT_DISCOUNT_RATE
    system_lifetime = getattr(args, 'system_lifetime', None) or DEFAULT_SYSTEM_LIFETIME

    # --- Load or generate data ---
    buildings = []
    dsm = None
    transform = None
    pixel_size = 1.0

    if hasattr(args, 'buildings') and args.buildings:
        # Load buildings from file
        try:
            import geopandas as gpd
            gdf = gpd.read_file(args.buildings)
            for idx, row in gdf.iterrows():
                buildings.append({
                    "geometry": row.geometry.__geo_interface__,
                    "properties": {
                        "building_id": idx,
                        "building_type": row.get("building_type", "unknown"),
                        "floors": row.get("floors", 1),
                        "footprint_area_m2": row.geometry.area,
                    },
                })
        except ImportError:
            logger.error("geopandas required for building file input")
            return EXIT_DEP
        except Exception as e:
            logger.error(f"Failed to load buildings: {e}")
            return EXIT_VALIDATION
    else:
        # Generate synthetic buildings
        buildings = generate_synthetic_buildings(n_buildings=5)
        logger.info(f"Generated {len(buildings)} synthetic buildings")

    if hasattr(args, 'dsm') and args.dsm:
        try:
            import rasterio
            with rasterio.open(args.dsm) as src:
                dsm = src.read(1)
                transform = src.transform
                pixel_size = abs(transform.a)
        except ImportError:
            logger.error("rasterio required for DSM input")
            return EXIT_DEP
        except Exception as e:
            logger.error(f"Failed to load DSM: {e}")
            return EXIT_VALIDATION

    if not buildings:
        logger.error("No buildings to analyze")
        return EXIT_VALIDATION

    # --- Analyze each building ---
    building_results = []
    all_roof_planes = []
    all_candidates = []

    for b in buildings:
        b_id = b["properties"].get("building_id", 0)
        logger.info(f"Analyzing building {b_id}")

        # Extract roof planes
        planes = extract_roof_planes(b["geometry"], dsm, transform, pixel_size)

        for plane in planes:
            plane_props = plane["properties"]
            area = plane_props["area_m2"]
            slope = plane_props["slope_deg"]
            aspect = plane_props["aspect_deg"]

            # Skip if slope too steep
            if slope > DEFAULT_MAX_SLOPE_DEG:
                continue

            # Skip if area too small
            if area < DEFAULT_MIN_ROOF_AREA_M2:
                continue

            # Compute usable area
            obstacles = b["properties"].get("obstacles", [])
            usable = compute_usable_area(plane, setback_m, obstacles, min_contiguous_area)

            if usable["usable_area_m2"] <= 0:
                continue

            # Compute installed capacity
            capacity_info = compute_installed_capacity(
                usable["usable_area_m2"], panel_type
            )

            if capacity_info["capacity_kw"] <= 0:
                continue

            # Compute energy yield
            energy_info = compute_energy_yield(
                capacity_info["capacity_kw"],
                annual_ghi,
                performance_ratio,
                slope,
                aspect,
            )

            # Compute economics
            econ_config = {
                "panel_type": panel_type,
                "electricity_price_cny_per_kwh": electricity_price,
                "discount_rate": discount_rate,
                "system_lifetime_years": system_lifetime,
            }
            econ_info = compute_economic_analysis(
                capacity_info["capacity_kw"],
                energy_info["annual_kwh"],
                econ_config,
            )

            result = {
                "building_id": b_id,
                "building_type": b["properties"].get("building_type", "unknown"),
                "capacity_kw": capacity_info["capacity_kw"],
                "n_panels": capacity_info["n_panels"],
                "usable_area_m2": usable["usable_area_m2"],
                "roof_area_m2": area,
                "slope_deg": slope,
                "aspect_deg": aspect,
                "annual_kwh": energy_info["annual_kwh"],
                "specific_yield": energy_info["specific_yield_kwh_per_kw"],
                "capacity_factor": energy_info["capacity_factor"],
                "total_investment_cny": econ_info["total_investment_cny"],
                "annual_revenue_cny": econ_info["annual_revenue_cny"],
                "payback_years": econ_info["payback_years"],
                "npv_cny": econ_info["npv_cny"],
                "lcoe_cny_per_kwh": econ_info["lcoe_cny_per_kwh"],
                "roof_type": plane_props.get("roof_type", ROOF_FLAT),
                "quality": plane_props.get("quality", QUALITY_MEDIUM),
            }
            building_results.append(result)

            # Add to candidates
            all_candidates.append({
                "geometry": usable["geometry"],
                "properties": result,
            })

            # Add to roof planes
            all_roof_planes.append(plane)

    # --- Rank buildings ---
    building_results = rank_buildings(building_results)

    # --- Write Outputs ---

    # roof_planes.geojson
    roof_planes_geojson = {
        "type": "FeatureCollection",
        "features": all_roof_planes,
    }
    roof_planes_path = output_dir / "roof_planes.geojson"
    roof_planes_path.write_text(
        json.dumps(roof_planes_geojson, ensure_ascii=False, default=str),
        encoding="utf-8",
    )

    # solar_candidates.geojson
    candidates_geojson = {
        "type": "FeatureCollection",
        "features": all_candidates,
    }
    candidates_path = output_dir / "solar_candidates.geojson"
    candidates_path.write_text(
        json.dumps(candidates_geojson, ensure_ascii=False, default=str),
        encoding="utf-8",
    )

    # building_potential.csv
    csv_path = output_dir / "building_potential.csv"
    if building_results:
        csv_fields = [
            "rank", "building_id", "building_type", "capacity_kw", "n_panels",
            "usable_area_m2", "roof_area_m2", "slope_deg", "aspect_deg",
            "annual_kwh", "specific_yield", "capacity_factor",
            "total_investment_cny", "annual_revenue_cny", "payback_years",
            "npv_cny", "lcoe_cny_per_kwh", "score", "roof_type", "quality",
        ]
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=csv_fields, extrasaction="ignore")
            writer.writeheader()
            for r in building_results:
                writer.writerow(r)

    # shading.tif (if DSM available)
    if dsm is not None:
        try:
            import rasterio
            from rasterio.transform import from_bounds

            if transform is None:
                transform = from_bounds(0, 0, dsm.shape[1], dsm.shape[0],
                                        dsm.shape[1], dsm.shape[0])

            shading = compute_shading(dsm, azimuth=180.0, altitude=45.0,
                                      pixel_size=pixel_size)

            shading_path = output_dir / "shading.tif"
            with rasterio.open(
                shading_path, "w",
                driver="GTiff",
                height=shading.shape[0],
                width=shading.shape[1],
                count=1,
                dtype=shading.dtype,
                crs="EPSG:32650",
                transform=transform,
            ) as dst:
                dst.write(shading, 1)
        except ImportError:
            logger.warning("rasterio not available, skipping shading.tif output")
        except Exception as e:
            logger.warning(f"Failed to write shading.tif: {e}")

    # request.json
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "setback_m": setback_m,
        "panel_type": panel_type,
        "min_contiguous_area_m2": min_contiguous_area,
        "annual_ghi_kwh_per_m2": annual_ghi,
        "performance_ratio": performance_ratio,
        "electricity_price_cny_per_kwh": electricity_price,
        "discount_rate": discount_rate,
        "system_lifetime_years": system_lifetime,
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
        "n_buildings": len(buildings),
        "dsm_available": dsm is not None,
        "buildings_source": "file" if (hasattr(args, 'buildings') and args.buildings) else "synthetic",
        "buildings": [
            {
                "building_id": b["properties"].get("building_id", i),
                "building_type": b["properties"].get("building_type", "unknown"),
                "footprint_area_m2": b["properties"].get("footprint_area_m2", 0),
            }
            for i, b in enumerate(buildings)
        ],
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # output-manifest.json
    output_files = {
        "roof_planes.geojson": str(roof_planes_path),
        "solar_candidates.geojson": str(candidates_path),
        "building_potential.csv": str(csv_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(dataset_path),
    }
    if dsm is not None and (output_dir / "shading.tif").exists():
        output_files["shading.tif"] = str(output_dir / "shading.tif")

    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "analysis_parameters": request_info,
        "output_files": output_files,
        "n_candidates": len(all_candidates),
        "total_capacity_kw": round(sum(r["capacity_kw"] for r in building_results), 2),
        "total_annual_kwh": round(sum(r["annual_kwh"] for r in building_results), 1),
        "total_investment_cny": round(sum(r["total_investment_cny"] for r in building_results), 2),
        "building_rankings": [
            {"rank": r["rank"], "building_id": r["building_id"], "score": r["score"]}
            for r in building_results
        ],
        "parameters": vars(args),  # T9: raw CLI args
        "summary": {
            "n_outputs": len(output_files),
            "n_candidates": len(all_candidates),
            "n_buildings": len(building_results),
            "total_capacity_kw": round(sum(r["capacity_kw"] for r in building_results), 2),
        },
    }
    if fetch_meta:
        manifest["data_source"] = fetch_meta.get("data_source")
        manifest["fetched_at"] = fetch_meta.get("fetched_at")
        if fetch_meta.get("collection"):
            manifest["collection"] = fetch_meta["collection"]
        if fetch_meta.get("nasa_power_path"):
            output_files["nasa_power_ghi.csv"] = fetch_meta["nasa_power_path"]
        if fetch_meta.get("n_items_searched") is not None:
            manifest["items_searched"] = fetch_meta["n_items_searched"]
    manifest_path = output_dir / "output-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # qa.json
    qa = {
        "status": "complete",
        "checks": {
            "buildings_loaded": len(buildings) > 0,
            "roof_planes_extracted": len(all_roof_planes) > 0,
            "candidates_identified": len(all_candidates) > 0,
            "rankings_computed": len(building_results) > 0,
            "dsm_used": dsm is not None,
        },
        "warnings": [],
        "n_buildings": len(buildings),
        "n_roof_planes": len(all_roof_planes),
        "n_candidates": len(all_candidates),
        "total_capacity_kw": round(sum(r["capacity_kw"] for r in building_results), 2),
    }
    if dsm is None:
        qa["warnings"].append("No DSM available - assuming flat roofs with low confidence")

    qa_path = output_dir / "qa.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    logger.info(f"Analysis complete: {len(all_candidates)} candidates, "
                f"{sum(r['capacity_kw'] for r in building_results):.1f} kW total")

    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Rooftop Solar Inventory Analysis")
    parser.add_argument("--buildings", default=None,
                        help="Building footprints file (GeoJSON/Shapefile)")
    parser.add_argument("--dsm", default=None,
                        help="Digital Surface Model GeoTIFF")
    parser.add_argument("--point-cloud", default=None,
                        help="Point cloud file (LAS/LAZ)")
    parser.add_argument("--setback", type=float, default=DEFAULT_SETBACK_M,
                        help=f"Edge setback in meters (default: {DEFAULT_SETBACK_M})")
    parser.add_argument("--panel-type", default=DEFAULT_PANEL_TYPE,
                        choices=["mono_perc_540w", "mono_perc_600w", "hjt_700w"],
                        help=f"Panel type (default: {DEFAULT_PANEL_TYPE})")
    parser.add_argument("--min-contiguous-area", type=float,
                        default=DEFAULT_MIN_CONTIGUOUS_AREA_M2,
                        help=f"Minimum contiguous area in m2 (default: {DEFAULT_MIN_CONTIGUOUS_AREA_M2})")
    parser.add_argument("--annual-ghi", type=float, default=DEFAULT_ANNUAL_GHI,
                        help=f"Annual GHI in kWh/m2 (default: {DEFAULT_ANNUAL_GHI})")
    parser.add_argument("--performance-ratio", type=float,
                        default=DEFAULT_PERFORMANCE_RATIO,
                        help=f"Performance ratio (default: {DEFAULT_PERFORMANCE_RATIO})")
    parser.add_argument("--electricity-price", type=float,
                        default=DEFAULT_ELECTRICITY_PRICE,
                        help=f"Electricity price CNY/kWh (default: {DEFAULT_ELECTRICITY_PRICE})")
    parser.add_argument("--discount-rate", type=float, default=DEFAULT_DISCOUNT_RATE,
                        help=f"Discount rate (default: {DEFAULT_DISCOUNT_RATE})")
    parser.add_argument("--system-lifetime", type=int, default=DEFAULT_SYSTEM_LIFETIME,
                        help=f"System lifetime in years (default: {DEFAULT_SYSTEM_LIFETIME})")
    parser.add_argument("--output-dir", "-o", default="rsi-output",
                        help="Output directory (default: rsi-output)")
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
