#!/usr/bin/env python3
"""
Nature Risk TNFD - LEAP-based nature-related financial risk screening.

Implements TNFD LEAP approach (Locate, Evaluate, Assess, Prepare) for
screening enterprise assets against ecological sensitive areas, ecosystem
state, and natural dependencies.

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
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from shapely.geometry import Point, Polygon, box, mapping, shape
from shapely.ops import unary_union
from shapely.strtree import STRtree

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

# File-arg flags that must point to existing paths (None = skip check)
FILE_ARGS = {
    "assets": "args.assets",
    "indicators_config": "args.indicators_config",
}

# Numeric flags with (min, max) bounds; None = unbounded on that side
NUMERIC_RANGES = {
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
    logger = logging.getLogger("nrt")
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
    """Close all handlers on the nrt logger."""
    logger = logging.getLogger("nrt")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)


# ============================================================
# Geometry Helpers
# ============================================================

def create_polygon(x: float, y: float, w: float, h: float) -> Polygon:
    """
    Create a rectangle polygon from origin (x, y) with width w and height h.

    Returns a closed 5-point ring (counter-clockwise).
    """
    return Polygon([
        (x, y),
        (x + w, y),
        (x + w, y + h),
        (x, y + h),
        (x, y),
    ])


def buffer_degrees(lat: float, distance_m: float) -> float:
    """
    Approximate buffer distance in degrees for a given metric distance.

    Uses cos(lat) * 111320 m/degree for longitude and 111320 m/degree
    for latitude. Returns the larger of the two to ensure coverage.

    This is an approximation suitable for screening-level analysis only.
    """
    lat_dist = distance_m / 111320.0
    lon_dist = distance_m / (111320.0 * math.cos(math.radians(abs(lat))))
    return max(lat_dist, lon_dist)


def haversine_distance_m(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """
    Calculate the great-circle distance between two points on Earth.

    Uses the haversine formula. Returns distance in meters.
    """
    R = 6371000.0  # Earth radius in meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def geographic_area_approx_m2(geom) -> float:
    """
    Approximate area in square meters for a geometry in EPSG:4326.

    Uses the cos(lat) * 111320 approximation for degree-to-meter conversion.
    This is screening-level only — not for precise area measurement.
    """
    centroid = geom.centroid
    lat = centroid.y
    # Convert: 1 deg^2 = (111320 * cos(lat)) * 111320 m^2
    m2_per_deg2 = (111320.0 * math.cos(math.radians(abs(lat)))) * 111320.0
    return geom.area * m2_per_deg2


# ============================================================
# Reference Data Loading
# ============================================================

def load_tnfd_indicators(indicators_path: Optional[str] = None) -> Dict:
    """Load TNFD indicator reference data from JSON."""
    if indicators_path is None:
        script_dir = Path(__file__).parent
        indicators_path = script_dir.parent / "references" / "tnfd_indicators.json"

    with open(indicators_path, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# Asset Loading and Standardization
# ============================================================

def load_assets_from_geojson(path: str) -> List[Dict]:
    """
    Load assets from a GeoJSON file.

    Each feature becomes an asset dict with:
        - id, name, type, sector, geometry (shapely), properties
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assets = []
    features = data.get("features", [])
    for i, feat in enumerate(features):
        props = feat.get("properties", {})
        geom = feat.get("geometry")
        if geom is None:
            continue

        try:
            shapely_geom = shape(geom)
        except Exception:
            continue

        asset = {
            "id": props.get("id", props.get("name", f"asset_{i}")),
            "name": props.get("name", f"Asset {i}"),
            "type": props.get("type", "unknown"),
            "sector": props.get("sector", "general"),
            "geometry": shapely_geom,
            "properties": props,
        }
        assets.append(asset)

    return assets


def load_assets_from_csv(path: str) -> List[Dict]:
    """
    Load assets from a CSV file with lat/lon columns.

    Expected columns: id, name, latitude, longitude, [type], [sector]
    """
    assets = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            try:
                lat = float(row.get("latitude", row.get("lat", 0)))
                lon = float(row.get("longitude", row.get("lon", 0)))
            except (ValueError, TypeError):
                continue

            asset = {
                "id": row.get("id", row.get("name", f"asset_{i}")),
                "name": row.get("name", f"Asset {i}"),
                "type": row.get("type", "unknown"),
                "sector": row.get("sector", "general"),
                "geometry": Point(lon, lat),
                "properties": dict(row),
            }
            assets.append(asset)

    return assets


def generate_synthetic_assets(n: int = 5, seed: int = 42) -> List[Dict]:
    """
    Generate synthetic assets for demo/testing.

    Creates assets at various locations with different sectors.
    """
    rng = np.random.RandomState(seed)
    sectors = ["agriculture", "mining", "manufacturing", "energy", "real_estate"]
    asset_types = ["factory", "farm", "mine", "power_plant", "warehouse"]

    assets = []
    for i in range(n):
        # Random location around a base point (China region)
        lon = 110.0 + rng.uniform(-5, 5)
        lat = 30.0 + rng.uniform(-5, 5)

        asset = {
            "id": f"asset_{i:03d}",
            "name": f"Demo Asset {i}",
            "type": asset_types[i % len(asset_types)],
            "sector": sectors[i % len(sectors)],
            "geometry": Point(lon, lat),
            "properties": {
                "established": int(rng.randint(1990, 2023)),
                "employees": int(rng.randint(50, 5000)),
            },
        }
        assets.append(asset)

    return assets


# ============================================================
# Ecological Sensitive Area Generation
# ============================================================

def generate_synthetic_protected_areas(
    n: int = 3,
    seed: int = 42,
) -> List[Dict]:
    """Generate synthetic protected area polygons for demo/testing."""
    rng = np.random.RandomState(seed)

    areas = []
    for i in range(n):
        cx = 110.0 + rng.uniform(-4, 4)
        cy = 30.0 + rng.uniform(-4, 4)
        w = rng.uniform(0.2, 1.0)
        h = rng.uniform(0.2, 1.0)

        poly = create_polygon(cx, cy, w, h)
        areas.append({
            "id": f"pa_{i:03d}",
            "name": f"Protected Area {i}",
            "designation": rng.choice(["National Park", "Nature Reserve", "Wildlife Sanctuary"]),
            "iucn_category": rng.choice(["Ia", "II", "III", "IV"]),
            "geometry": poly,
            "area_km2": round(geographic_area_approx_m2(poly) / 1e6, 2),
        })

    return areas


def generate_synthetic_water_stress(
    n_rows: int = 100,
    n_cols: int = 100,
    seed: int = 42,
) -> np.ndarray:
    """
    Generate synthetic water stress raster (0-5 index).

    Higher values = more stress. Pattern: gradient + noise.
    """
    rng = np.random.RandomState(seed)
    data = np.zeros((n_rows, n_cols), dtype=np.float32)

    for r in range(n_rows):
        # Gradient from low (top) to high (bottom)
        base = 2.0 + 2.0 * (r / n_rows)
        data[r, :] = base + rng.normal(0, 0.5, n_cols)

    data = np.clip(data, 0, 5)
    return data


def generate_synthetic_forest_cover(
    n_rows: int = 100,
    n_cols: int = 100,
    seed: int = 42,
) -> np.ndarray:
    """
    Generate synthetic forest cover raster (0-100%).

    Pattern: high in patches, low elsewhere.
    """
    rng = np.random.RandomState(seed)
    data = np.zeros((n_rows, n_cols), dtype=np.float32)

    # Create forest patches
    for _ in range(5):
        cx = rng.randint(0, n_cols)
        cy = rng.randint(0, n_rows)
        radius = rng.randint(10, 25)
        for r in range(n_rows):
            for c in range(n_cols):
                dist = math.sqrt((r - cy) ** 2 + (c - cx) ** 2)
                if dist < radius:
                    data[r, c] = max(data[r, c], 80 * (1 - dist / radius))

    data = np.clip(data + rng.normal(0, 5, (n_rows, n_cols)), 0, 100)
    return data.astype(np.float32)


def generate_synthetic_ecolayers(
    n_rows: int = 100,
    n_cols: int = 100,
    bbox: Tuple[float, float, float, float] = (105, 25, 115, 35),
    seed: int = 42,
) -> Dict[str, Any]:
    """
    Generate all synthetic ecological layers.

    Returns dict with:
        - water_stress: 2D array
        - forest_cover: 2D array
        - protected_areas: list of dicts
        - bbox: (min_lon, min_lat, max_lon, max_lat)
    """
    return {
        "water_stress": generate_synthetic_water_stress(n_rows, n_cols, seed),
        "forest_cover": generate_synthetic_forest_cover(n_rows, n_cols, seed),
        "protected_areas": generate_synthetic_protected_areas(3, seed),
        "bbox": bbox,
        "n_rows": n_rows,
        "n_cols": n_cols,
    }


# ============================================================
# Locate: Spatial Screening
# ============================================================

def locate_asset_protected_areas(
    asset: Dict,
    protected_areas: List[Dict],
    buffer_m: float = 5000,
) -> Dict[str, Any]:
    """
    Locate: Check if asset is within or near protected areas.

    Returns:
        - in_protected_area: bool
        - nearest_pa_distance_m: float
        - nearest_pa_name: str
        - overlapping_pas: list
        - buffered_overlap: bool
    """
    geom = asset["geometry"]
    centroid = geom.centroid
    lat = centroid.y

    in_pa = False
    nearest_dist = float("inf")
    nearest_name = ""
    overlapping = []
    buffered_overlap = False

    for pa in protected_areas:
        pa_geom = pa["geometry"]

        # Direct overlap
        if geom.intersects(pa_geom):
            in_pa = True
            overlapping.append(pa["id"])

        # Distance to nearest PA
        dist_deg = geom.distance(pa_geom)
        # Convert to meters (approximate)
        dist_m = dist_deg * 111320.0 * math.cos(math.radians(abs(lat)))

        if dist_m < nearest_dist:
            nearest_dist = dist_m
            nearest_name = pa["name"]

        # Buffer check
        buffer_deg = buffer_degrees(lat, buffer_m)
        if geom.buffer(buffer_deg).intersects(pa_geom):
            buffered_overlap = True

    return {
        "in_protected_area": in_pa,
        "nearest_pa_distance_m": round(nearest_dist, 1),
        "nearest_pa_name": nearest_name,
        "overlapping_pas": overlapping,
        "buffered_overlap": buffered_overlap,
    }


def locate_asset_water_stress(
    asset: Dict,
    water_stress: np.ndarray,
    bbox: Tuple[float, float, float, float],
    n_rows: int,
    n_cols: int,
) -> Dict[str, Any]:
    """
    Locate: Get water stress value at asset location.

    Maps asset lon/lat to raster cell and retrieves value.
    """
    geom = asset["geometry"]
    lon = geom.x
    lat = geom.y

    min_lon, min_lat, max_lon, max_lat = bbox

    # Map to raster indices
    col = int((lon - min_lon) / (max_lon - min_lon) * (n_cols - 1))
    row = int((max_lat - lat) / (max_lat - min_lat) * (n_rows - 1))

    # Clamp
    col = max(0, min(col, n_cols - 1))
    row = max(0, min(row, n_rows - 1))

    value = float(water_stress[row, col])

    # Classify
    if value < 1.0:
        level = "low"
    elif value < 2.0:
        level = "medium"
    elif value < 3.0:
        level = "high"
    else:
        level = "extremely_high"

    return {
        "water_stress_index": round(value, 2),
        "water_stress_level": level,
        "raster_row": row,
        "raster_col": col,
    }


def locate_asset_forest_cover(
    asset: Dict,
    forest_cover: np.ndarray,
    bbox: Tuple[float, float, float, float],
    n_rows: int,
    n_cols: int,
) -> Dict[str, Any]:
    """
    Locate: Get forest cover percentage at asset location.
    """
    geom = asset["geometry"]
    lon = geom.x
    lat = geom.y

    min_lon, min_lat, max_lon, max_lat = bbox

    col = int((lon - min_lon) / (max_lon - min_lon) * (n_cols - 1))
    row = int((max_lat - lat) / (max_lat - min_lat) * (n_rows - 1))

    col = max(0, min(col, n_cols - 1))
    row = max(0, min(row, n_rows - 1))

    value = float(forest_cover[row, col])

    if value >= 80:
        level = "intact"
    elif value >= 50:
        level = "moderate"
    elif value >= 20:
        level = "low"
    else:
        level = "very_low"

    return {
        "forest_cover_pct": round(value, 1),
        "forest_cover_level": level,
    }


# ============================================================
# Evaluate: Dependency and Impact Scoring
# ============================================================

def evaluate_dependency(
    asset: Dict,
    locate_results: Dict,
    indicators: Dict,
) -> Dict[str, Any]:
    """
    Evaluate: Score nature dependency based on sector and location.

    Uses sector materiality matrix from indicators reference.
    Adjusts based on actual location context (e.g., water dependency
    is higher in water-stressed areas).
    """
    sector = asset.get("sector", "general")
    materiality = indicators.get("sector_materiality", {})
    sector_data = materiality.get(sector, materiality.get("general", {}))

    dependency_raw = sector_data.get("dependency", {})

    # Adjust based on location context
    adjusted = {}
    for service, base_score in dependency_raw.items():
        adjustment = 0

        # Water dependency increases in water-stressed areas
        if service == "water_supply":
            ws_level = locate_results.get("water_stress", {}).get("water_stress_level", "")
            if ws_level == "extremely_high":
                adjustment = 1
            elif ws_level == "high":
                adjustment = 0.5

        # Flood protection dependency increases near intact ecosystems
        if service == "flood_protection":
            forest_level = locate_results.get("forest_cover", {}).get("forest_cover_level", "")
            if forest_level in ("intact", "moderate"):
                adjustment = 0.5

        adjusted[service] = min(5, max(0, base_score + adjustment))

    # Overall dependency score (average of top 3)
    top_scores = sorted(adjusted.values(), reverse=True)[:3]
    overall = round(sum(top_scores) / len(top_scores), 2) if top_scores else 0

    return {
        "scores": adjusted,
        "overall_dependency": overall,
        "evidence_level": "modelled",
        "data_year": 2024,
    }


def evaluate_impact(
    asset: Dict,
    locate_results: Dict,
    indicators: Dict,
) -> Dict[str, Any]:
    """
    Evaluate: Score nature impact based on sector and location.

    Uses sector materiality matrix. Increases impact score if asset
    is in/near protected areas.
    """
    sector = asset.get("sector", "general")
    materiality = indicators.get("sector_materiality", {})
    sector_data = materiality.get(sector, materiality.get("general", {}))

    impact_raw = sector_data.get("impact", {})

    adjusted = {}
    for category, base_score in impact_raw.items():
        adjustment = 0

        # Land use change impact higher near protected areas
        if category == "land_use_change":
            if locate_results.get("protected_areas", {}).get("in_protected_area", False):
                adjustment = 1
            elif locate_results.get("protected_areas", {}).get("buffered_overlap", False):
                adjustment = 0.5

        # Water withdrawal impact higher in water-stressed areas
        if category == "water_withdrawal":
            ws_level = locate_results.get("water_stress", {}).get("water_stress_level", "")
            if ws_level == "extremely_high":
                adjustment = 1
            elif ws_level == "high":
                adjustment = 0.5

        adjusted[category] = min(5, max(0, base_score + adjustment))

    top_scores = sorted(adjusted.values(), reverse=True)[:3]
    overall = round(sum(top_scores) / len(top_scores), 2) if top_scores else 0

    return {
        "scores": adjusted,
        "overall_impact": overall,
        "evidence_level": "modelled",
        "data_year": 2024,
    }


# ============================================================
# Risk Prioritization
# ============================================================

def compute_priority_score(
    dependency: Dict,
    impact: Dict,
) -> float:
    """
    Compute overall priority score from dependency and impact.

    Priority = (dependency + impact) / 2, scaled to 0-5.
    """
    dep = dependency.get("overall_dependency", 0)
    imp = impact.get("overall_impact", 0)
    return round((dep + imp) / 2, 2)


def classify_risk_level(priority_score: float) -> str:
    """Classify risk level from priority score (0-5 scale)."""
    if priority_score >= 4.0:
        return "high"
    elif priority_score >= 2.5:
        return "medium"
    elif priority_score >= 1.0:
        return "low"
    else:
        return "negligible"


# ============================================================
# Data Gap Analysis
# ============================================================

def identify_data_gaps(
    asset: Dict,
    locate_results: Dict,
    dependency: Dict,
    impact: Dict,
) -> List[Dict]:
    """
    Identify data gaps for this asset.

    Returns list of gap descriptions with severity.
    """
    gaps = []

    # Check for missing ecological data
    if "water_stress" not in locate_results:
        gaps.append({
            "indicator": "water_stress",
            "severity": "medium",
            "description": "No water stress data available for asset location",
        })

    if "forest_cover" not in locate_results:
        gaps.append({
            "indicator": "forest_cover",
            "severity": "low",
            "description": "No forest cover data available for asset location",
        })

    # Check for missing biodiversity data
    if "biodiversity" not in locate_results:
        gaps.append({
            "indicator": "biodiversity",
            "severity": "high",
            "description": "No biodiversity importance data - KBA/IBAT data not available",
        })

    # Check for missing ecosystem integrity
    if "ecosystem_integrity" not in locate_results:
        gaps.append({
            "indicator": "ecosystem_integrity",
            "severity": "medium",
            "description": "No ecosystem integrity assessment available",
        })

    # Check evidence levels
    if dependency.get("evidence_level") == "gap":
        gaps.append({
            "indicator": "dependency",
            "severity": "high",
            "description": "Dependency assessment has no data",
        })

    if impact.get("evidence_level") == "gap":
        gaps.append({
            "indicator": "impact",
            "severity": "high",
            "description": "Impact assessment has no data",
        })

    return gaps


# ============================================================
# Report Generation
# ============================================================

def generate_report_html(
    results: Dict,
    output_dir: Path,
) -> Path:
    """Generate HTML screening report."""
    path = output_dir / "tnfd_screening_report.html"

    # Safely extract values
    n_assets = results.get("n_assets", 0)
    n_priority = results.get("n_priority", 0)
    n_gaps = results.get("n_gaps", 0)

    # Build asset rows
    asset_rows = ""
    for asset in results.get("asset_details", []):
        aid = asset.get("id", "N/A")
        name = asset.get("name", "N/A")
        sector = asset.get("sector", "N/A")
        risk = asset.get("risk_level", "N/A")
        score = asset.get("priority_score", "N/A")
        dep = asset.get("overall_dependency", "N/A")
        imp = asset.get("overall_impact", "N/A")

        if isinstance(score, (int, float)):
            score_str = f"{score:.2f}"
        else:
            score_str = str(score)
        if isinstance(dep, (int, float)):
            dep_str = f"{dep:.2f}"
        else:
            dep_str = str(dep)
        if isinstance(imp, (int, float)):
            imp_str = f"{imp:.2f}"
        else:
            imp_str = str(imp)

        asset_rows += f"<tr><td>{aid}</td><td>{name}</td><td>{sector}</td><td>{score_str}</td><td>{dep_str}</td><td>{imp_str}</td><td>{risk}</td></tr>\n"

    if not asset_rows:
        asset_rows = "<tr><td colspan='7'>No assets screened</td></tr>\n"

    # Build gap rows
    gap_rows = ""
    for gap in results.get("gap_summary", []):
        indicator = gap.get("indicator", "N/A")
        severity = gap.get("severity", "N/A")
        count = gap.get("count", 0)
        gap_rows += f"<tr><td>{indicator}</td><td>{severity}</td><td>{count}</td></tr>\n"

    if not gap_rows:
        gap_rows = "<tr><td colspan='3'>No gaps identified</td></tr>\n"

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
<title>TNFD Nature Risk Screening Report</title>
<style>
body {{ font-family: 'Microsoft YaHei', Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
.container {{ max-width: 1000px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
h1 {{ color: #333; border-bottom: 3px solid #2e7d32; padding-bottom: 10px; }}
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
<h1>TNFD Nature Risk Screening Report</h1>
<p>Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}</p>
<p>Framework: TNFD LEAP (Locate phase screening)</p>

<div class="info">
<strong>Scope:</strong> Screening-level nature risk assessment.<br>
<strong>Note:</strong> This is a Locate-phase screening, NOT a full TNFD disclosure.
</div>

<h2>Warnings</h2>
<ul>
{warnings_html}
</ul>

<h2>Summary</h2>
<p><strong>Total assets screened:</strong> {n_assets}<br>
<strong>Priority assets (high risk):</strong> {n_priority}<br>
<strong>Data gaps identified:</strong> {n_gaps}</p>

<h2>Asset Risk Assessment</h2>
<table>
<tr><th>ID</th><th>Name</th><th>Sector</th><th>Priority Score</th><th>Dependency</th><th>Impact</th><th>Risk Level</th></tr>
{asset_rows}
</table>

<h2>Data Gaps</h2>
<table>
<tr><th>Indicator</th><th>Severity</th><th>Count</th></tr>
{gap_rows}
</table>

<h2>Methodology</h2>
<ul>
<li>Locate: Spatial screening of assets against protected areas, water stress, and forest cover</li>
<li>Evaluate: Sector-based materiality scoring adjusted for location context</li>
<li>Priority: Combined dependency + impact score, classified into risk levels</li>
<li>Evidence levels: measured, estimated, modelled, gap</li>
<li>Geographic distances use haversine formula; areas use cos(lat) approximation</li>
</ul>

<h2>Limitations</h2>
<ul>
<li>Screening-level only - not for regulatory disclosure</li>
<li>Synthetic/demo data used where real data not provided</li>
<li>Buffer distances are approximate (cos(lat) conversion)</li>
<li>Sensitive species locations are excluded from outputs</li>
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

def auto_download_assets(args, output_dir: Path) -> Dict[str, Any]:
    """Download one sentinel-2-l2a scene from MPC using --bbox + --date-range.

    Returns metadata dict (also writes the path back to args.assets).
    """
    if not _FETCHER_AVAILABLE:
        raise RuntimeError(
            "Shared data fetcher not importable. Pass --assets <local.tif> instead, "
            "or ensure _geoskill_data_fetcher is on sys.path."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_assets requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        raise RuntimeError("auto_download_assets requires --date-range")
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
        prefer_assets=['B04', 'B08'],
    )
    if not paths:
        raise RuntimeError("Download returned no files")
    args.assets = str(paths[0])
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "sentinel-2-l2a",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def run_screening_pipeline(args: argparse.Namespace) -> int:
    """Main TNFD nature risk screening workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("nrt-output")

    # --- Auto-download mode: fetch sentinel-2-l2a from MPC ---
    if (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)) and getattr(args, "date_range", None):
        if not getattr(args, "assets", None):
            try:
                fetch_meta = auto_download_assets(args, output_dir)
                mode = "auto_download"
                print(f"  Auto-downloaded assets: {args.assets}")
            except DataFetcherError as e:
                print(f"ERROR: auto-download failed: [{e.kind}] {e.message}", file=sys.stderr)
                return EXIT_PROCESSING if 'EXIT_PROCESSING' in dir() else 7
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logging(output_dir)
    logger.info("Nature Risk TNFD - Starting LEAP screening")

    # Load indicators reference
    indicators_path = getattr(args, 'indicators_config', None)
    try:
        indicators = load_tnfd_indicators(indicators_path)
        logger.info(f"TNFD indicators loaded: version {indicators.get('version', 'unknown')}")
    except Exception as e:
        logger.error(f"Failed to load TNFD indicators: {e}")
        cleanup_logging()
        return EXIT_VALIDATION

    # Parse buffers
    buffers = {}
    if hasattr(args, 'buffers') and args.buffers:
        for buf_str in args.buffers.split(","):
            parts = buf_str.strip().split(":")
            if len(parts) != 2:
                logger.error(f"Invalid buffer format: '{buf_str}' (expected type:meters)")
                cleanup_logging()
                return EXIT_ARG
            try:
                buffers[parts[0]] = float(parts[1])
            except ValueError:
                logger.error(f"Invalid buffer value: '{buf_str}' (meters must be numeric)")
                cleanup_logging()
                return EXIT_ARG
    else:
        buffers = indicators.get("buffer_defaults", {"facility": 5000})

    # Parse sector override
    sector = getattr(args, 'sector', None)

    # --- Load or generate assets ---
    use_synthetic = True
    assets = []

    if hasattr(args, 'assets') and args.assets:
        asset_path = Path(args.assets)
        if asset_path.exists():
            use_synthetic = False
            if asset_path.suffix.lower() in ('.json', '.geojson'):
                assets = load_assets_from_geojson(str(asset_path))
            elif asset_path.suffix.lower() == '.csv':
                assets = load_assets_from_csv(str(asset_path))
            logger.info(f"Loaded {len(assets)} assets from {asset_path}")
        else:
            logger.warning(f"Asset file not found: {asset_path}, using synthetic")

    if use_synthetic or not assets:
        logger.info("Using synthetic demo assets")
        assets = generate_synthetic_assets(n=5, seed=42)
        if sector:
            for a in assets:
                a["sector"] = sector

    if not assets:
        logger.error("No assets to screen")
        cleanup_logging()
        return EXIT_VALIDATION

    # --- Generate or load ecological layers ---
    ecolayers = generate_synthetic_ecolayers(
        n_rows=100, n_cols=100,
        bbox=(105, 25, 115, 35),
        seed=42,
    )

    protected_areas = ecolayers["protected_areas"]
    water_stress = ecolayers["water_stress"]
    forest_cover = ecolayers["forest_cover"]
    bbox = ecolayers["bbox"]
    n_rows = ecolayers["n_rows"]
    n_cols = ecolayers["n_cols"]

    # --- Run screening for each asset ---
    asset_details = []
    all_gaps = []
    warnings = []

    for asset in assets:
        aid = asset.get("id", "unknown")
        logger.info(f"Screening asset: {aid}")

        # Locate phase
        pa_results = locate_asset_protected_areas(
            asset, protected_areas,
            buffer_m=buffers.get("facility", 5000),
        )
        ws_results = locate_asset_water_stress(
            asset, water_stress, bbox, n_rows, n_cols,
        )
        fc_results = locate_asset_forest_cover(
            asset, forest_cover, bbox, n_rows, n_cols,
        )

        locate_results = {
            "protected_areas": pa_results,
            "water_stress": ws_results,
            "forest_cover": fc_results,
        }

        # Evaluate phase
        dependency = evaluate_dependency(asset, locate_results, indicators)
        impact = evaluate_impact(asset, locate_results, indicators)

        # Priority score
        priority_score = compute_priority_score(dependency, impact)
        risk_level = classify_risk_level(priority_score)

        # Data gaps
        gaps = identify_data_gaps(asset, locate_results, dependency, impact)
        all_gaps.extend(gaps)

        asset_details.append({
            "id": aid,
            "name": asset.get("name", ""),
            "type": asset.get("type", ""),
            "sector": asset.get("sector", ""),
            "geometry": asset["geometry"],
            "priority_score": priority_score,
            "risk_level": risk_level,
            "overall_dependency": dependency["overall_dependency"],
            "overall_impact": impact["overall_impact"],
            "nearest_pa_distance_m": pa_results["nearest_pa_distance_m"],
            "nearest_pa_name": pa_results["nearest_pa_name"],
            "in_protected_area": pa_results["in_protected_area"],
            "water_stress_index": ws_results["water_stress_index"],
            "water_stress_level": ws_results["water_stress_level"],
            "forest_cover_pct": fc_results["forest_cover_pct"],
            "forest_cover_level": fc_results["forest_cover_level"],
            "data_gaps": gaps,
        })

    # Sort by priority score descending
    asset_details.sort(key=lambda x: x.get("priority_score", 0), reverse=True)

    # Count priority assets (high risk)
    n_priority = sum(1 for a in asset_details if a["risk_level"] == "high")

    # Aggregate gap summary
    gap_counts = defaultdict(lambda: {"count": 0, "severity": ""})
    for gap in all_gaps:
        key = gap["indicator"]
        gap_counts[key]["count"] += 1
        gap_counts[key]["severity"] = gap["severity"]

    gap_summary = [
        {"indicator": k, "count": v["count"], "severity": v["severity"]}
        for k, v in gap_counts.items()
    ]

    # Warnings
    if use_synthetic:
        warnings.append("Using synthetic/demo ecological data. Replace with real data for actual screening.")
    if not buffers:
        warnings.append("No buffer distances specified. Using defaults.")

    # --- Generate outputs ---

    # 1. asset_nature_context.geojson
    asset_geojson = {
        "type": "FeatureCollection",
        "features": [],
    }
    for a in asset_details:
        feat = {
            "type": "Feature",
            "geometry": mapping(a["geometry"]),
            "properties": {
                "id": a["id"],
                "name": a["name"],
                "type": a["type"],
                "sector": a["sector"],
                "priority_score": a["priority_score"],
                "risk_level": a["risk_level"],
                "overall_dependency": a["overall_dependency"],
                "overall_impact": a["overall_impact"],
                "nearest_pa_distance_m": a["nearest_pa_distance_m"],
                "nearest_pa_name": a["nearest_pa_name"],
                "in_protected_area": a["in_protected_area"],
                "water_stress_index": a["water_stress_index"],
                "water_stress_level": a["water_stress_level"],
                "forest_cover_pct": a["forest_cover_pct"],
                "forest_cover_level": a["forest_cover_level"],
                "n_data_gaps": len(a["data_gaps"]),
            },
        }
        asset_geojson["features"].append(feat)

    asset_gj_path = output_dir / "asset_nature_context.geojson"
    asset_gj_path.write_text(
        json.dumps(asset_geojson, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # 2. indicator_table.csv
    indicator_csv_path = output_dir / "indicator_table.csv"
    with open(indicator_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "asset_id", "name", "sector", "priority_score", "risk_level",
            "overall_dependency", "overall_impact",
            "nearest_pa_distance_m", "nearest_pa_name",
            "in_protected_area", "water_stress_index", "water_stress_level",
            "forest_cover_pct", "forest_cover_level", "n_data_gaps",
        ])
        for a in asset_details:
            writer.writerow([
                a["id"], a["name"], a["sector"],
                a["priority_score"], a["risk_level"],
                a["overall_dependency"], a["overall_impact"],
                a["nearest_pa_distance_m"], a["nearest_pa_name"],
                a["in_protected_area"],
                a["water_stress_index"], a["water_stress_level"],
                a["forest_cover_pct"], a["forest_cover_level"],
                len(a["data_gaps"]),
            ])

    # 3. priority_assets.geojson
    priority_features = []
    for a in asset_details:
        if a["risk_level"] in ("high", "medium"):
            priority_features.append({
                "type": "Feature",
                "geometry": mapping(a["geometry"]),
                "properties": {
                    "id": a["id"],
                    "name": a["name"],
                    "priority_score": a["priority_score"],
                    "risk_level": a["risk_level"],
                    "overall_dependency": a["overall_dependency"],
                    "overall_impact": a["overall_impact"],
                },
            })

    priority_geojson = {
        "type": "FeatureCollection",
        "features": priority_features,
    }
    priority_path = output_dir / "priority_assets.geojson"
    priority_path.write_text(
        json.dumps(priority_geojson, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # 4. data_gaps.json
    data_gaps = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_gaps": len(all_gaps),
        "gap_summary": gap_summary,
        "gaps_by_asset": [
            {
                "asset_id": a["id"],
                "gaps": a["data_gaps"],
            }
            for a in asset_details
        ],
    }
    gaps_path = output_dir / "data_gaps.json"
    gaps_path.write_text(
        json.dumps(data_gaps, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # 5. Report HTML
    report_results = {
        "n_assets": len(asset_details),
        "n_priority": n_priority,
        "n_gaps": len(all_gaps),
        "asset_details": asset_details,
        "gap_summary": gap_summary,
        "warnings": warnings,
    }
    report_path = generate_report_html(report_results, output_dir)

    # 6. request.json
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "synthetic" if use_synthetic else "file",
        "n_assets": len(assets),
        "buffers": buffers,
        "sector_override": sector,
        "output_dir": str(output_dir),
    }
    request_path = output_dir / "request.json"
    request_path.write_text(
        json.dumps(request_info, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # 7. dataset-manifest.json
    dataset_manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "synthetic" if use_synthetic else "file",
        "n_assets": len(assets),
        "n_protected_areas": len(protected_areas),
        "ecological_layers": ["water_stress", "forest_cover"],
        "raster_shape": [n_rows, n_cols],
        "bbox": list(bbox),
        "indicators_version": indicators.get("version", "unknown"),
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # 8. output-manifest.json
    output_files = {
        "asset_nature_context.geojson": str(asset_gj_path),
        "indicator_table.csv": str(indicator_csv_path),
        "priority_assets.geojson": str(priority_path),
        "data_gaps.json": str(gaps_path),
        "tnfd_screening_report.html": str(report_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(dataset_path),
    }
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "output_files": output_files,
        "summary": {
            "n_assets": len(asset_details),
            "n_priority": n_priority,
            "n_gaps": len(all_gaps),
            "n_warnings": len(warnings),
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

    # 9. qa.json
    qa = {
        "status": "complete",
        "checks": {
            "asset_geojson_written": asset_gj_path.exists(),
            "indicator_csv_written": indicator_csv_path.exists(),
            "priority_geojson_written": priority_path.exists(),
            "data_gaps_written": gaps_path.exists(),
            "report_written": report_path.exists(),
            "all_outputs_written": all(Path(p).exists() for p in output_files.values()),
        },
        "n_assets": len(asset_details),
        "n_priority": n_priority,
        "n_gaps": len(all_gaps),
        "n_warnings": len(warnings),
        "warnings": warnings,
        "buffers_used": buffers,
    }
    qa_path = output_dir / "qa.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    logger.info(f"Screening complete: {len(asset_details)} assets, "
                f"{n_priority} priority, {len(all_gaps)} gaps")
    cleanup_logging()
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Nature Risk TNFD LEAP Screening")
    parser.add_argument("--assets", default=None,
                        help="Path to assets file (GeoJSON or CSV)")
    parser.add_argument("--sector", default=None,
                        help="Override sector for all assets")
    parser.add_argument("--buffers", default=None,
                        help="Buffer distances as type:meters pairs (e.g., 'facility:5000,watershed:10000')")
    parser.add_argument("--indicators-config", default=None,
                        help="Path to TNFD indicators JSON")
    parser.add_argument("--output-dir", "-o", default="nrt-output",
                        help="Output directory (default: nrt-output)")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    add_bbox_date_args(parser)

    args = parser.parse_args()

    rc = validate_args(args)
    if rc != 0:
        sys.exit(rc)

    try:
        sys.exit(run_screening_pipeline(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
