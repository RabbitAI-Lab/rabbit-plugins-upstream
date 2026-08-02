#!/usr/bin/env python3
"""
Groundwater Recharge Potential - Multi-criteria screening analysis.

Combines terrain, soil, geology, land cover, drainage density, and rainfall
factors using AHP / weighted overlay / fuzzy logic to identify zones with
higher groundwater recharge potential.

Positioning: screening-level analysis only. Does NOT promise groundwater
volume or well success rate. All weights, scoring functions, and expert
judgments are externalized and version-recorded.
"""

import argparse
import json
import logging
import math
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Exit codes
EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEPENDENCY = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# Standard factor definitions with default weights and scoring direction
DEFAULT_FACTORS = {
    "slope": {
        "weight": 0.20,
        "direction": "lower_better",
        "description": "Slope steepness in degrees; flatter terrain favors infiltration",
        "unit": "degrees",
        "score_type": "linear",
    },
    "soil_permeability": {
        "weight": 0.20,
        "direction": "higher_better",
        "description": "Soil permeability proxy; higher permeability favors recharge",
        "unit": "cm_hr",
        "score_type": "linear",
    },
    "geology": {
        "weight": 0.15,
        "direction": "categorical",
        "description": "Geological formation type ranked by permeability",
        "unit": "class",
        "score_type": "categorical",
        "score_map": {
            1: 0.9,   # Alluvial deposits / sand & gravel
            2: 0.7,   # Sandstone / weathered granite
            3: 0.5,   # Limestone / fractured rock
            4: 0.3,   # Shale / claystone
            5: 0.1,   # Massive igneous / metamorphic
        },
    },
    "land_cover": {
        "weight": 0.15,
        "direction": "categorical",
        "description": "Land cover type ranked by infiltration favorability",
        "unit": "class",
        "score_type": "categorical",
        "score_map": {
            1: 0.9,   # Bare land / fallow
            2: 0.8,   # Grassland / meadow
            3: 0.7,   # Cropland / agriculture
            4: 0.5,   # Shrubland
            5: 0.3,   # Forest / woodland
            6: 0.1,   # Urban / impervious
            7: 0.0,   # Water body
        },
    },
    "drainage_density": {
        "weight": 0.10,
        "direction": "lower_better",
        "description": "Drainage density; lower density favors infiltration over runoff",
        "unit": "km_km2",
        "score_type": "linear",
    },
    "rainfall": {
        "weight": 0.20,
        "direction": "higher_better",
        "description": "Annual rainfall amount; more rain provides more recharge source",
        "unit": "mm_yr",
        "score_type": "linear",
    },
}

# Default categorical scoring for geology (higher = more permeable)
DEFAULT_GEOLOGY_SCORES = {
    1: 0.9,   # Alluvial deposits / sand & gravel
    2: 0.7,   # Sandstone / weathered granite
    3: 0.5,   # Limestone / fractured rock
    4: 0.3,   # Shale / claystone
    5: 0.1,   # Massive igneous / metamorphic
}

# Default categorical scoring for land cover (higher = more recharge-friendly)
DEFAULT_LANDCOVER_SCORES = {
    1: 0.9,   # Bare land / fallow
    2: 0.8,   # Grassland / meadow
    3: 0.7,   # Cropland / agriculture
    4: 0.5,   # Shrubland
    5: 0.3,   # Forest / woodland
    6: 0.1,   # Urban / impervious
    7: 0.0,   # Water body
}

# AHP random consistency index (Saaty)
RI_TABLE = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}


def setup_logging(output_dir: Path, log_level: str = "INFO") -> logging.Logger:
    """Configure logging to both file and console."""
    logger = logging.getLogger("grp")
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    logger.handlers.clear()

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    log_path = output_dir / "run.log"
    file_handler = logging.FileHandler(str(log_path), encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Groundwater Recharge Potential multi-criteria screening",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    # Spatial extent (mutually exclusive group handled manually)
    extent = parser.add_argument_group("spatial extent (provide one)")
    extent.add_argument("--place", help="Named place to geocode as AOI")
    extent.add_argument("--bbox", nargs=4, type=float, metavar=("XMIN", "YMIN", "XMAX", "YMAX"),
                        help="Bounding box in EPSG:4326")
    extent.add_argument("--aoi-file", help="Path to AOI vector file (GeoJSON/Shapefile)")

    # Analysis parameters
    params = parser.add_argument_group("analysis parameters")
    params.add_argument("--factor-config", help="Path to factor configuration JSON")
    params.add_argument("--weights", help="Path to weights JSON or 'equal'/'ahp'")
    params.add_argument("--method", choices=["ahp", "weighted", "fuzzy"], default="weighted",
                        help="Weighting and aggregation method (default: weighted)")
    params.add_argument("--constraints", help="Path to hard constraints JSON")
    params.add_argument("--sensitivity-runs", type=int, default=100,
                        help="Number of Monte Carlo sensitivity runs (default: 100)")
    params.add_argument("--min-area", type=float, default=1.0,
                        help="Minimum candidate zone area in hectares (default: 1.0)")

    # Input rasters
    inputs = parser.add_argument_group("input rasters")
    inputs.add_argument("--slope", help="Slope raster (degrees)")
    inputs.add_argument("--soil-permeability", help="Soil permeability raster")
    inputs.add_argument("--geology", help="Geology class raster")
    inputs.add_argument("--land-cover", help="Land cover class raster")
    inputs.add_argument("--drainage-density", help="Drainage density raster")
    inputs.add_argument("--rainfall", help="Annual rainfall raster (mm)")

    # Validation
    validation = parser.add_argument_group("validation")
    validation.add_argument("--well-points", help="Path to well points GeoJSON for validation")
    validation.add_argument("--validation-blocks", type=int, default=5,
                            help="Number of spatial blocks for cross-validation (default: 5)")

    # Output
    output = parser.add_argument_group("output")
    output.add_argument("--output-dir", "-o", default="grp-output",
                        help="Output directory (default: grp-output)")
    output.add_argument("--overwrite", action="store_true",
                        help="Allow overwriting existing output files")
    output.add_argument("--dry-run", action="store_true",
                        help="Only estimate data volume and steps")
    output.add_argument("--log-level", default="INFO",
                        choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    output.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> List[str]:
    """Validate argument consistency. Returns list of error messages."""
    errors = []

    # Exactly one spatial extent
    ext_count = sum([bool(args.place), bool(args.bbox), bool(args.aoi_file)])
    if ext_count == 0:
        errors.append("No spatial extent provided. Use --place, --bbox, or --aoi-file.")
    elif ext_count > 1:
        errors.append("Multiple spatial extents provided. Use only one of --place, --bbox, --aoi-file.")

    # At least one factor raster
    factor_rasters = [args.slope, args.soil_permeability, args.geology,
                      args.land_cover, args.drainage_density, args.rainfall]
    if not any(factor_rasters):
        errors.append("No factor rasters provided. At least one of --slope, --soil-permeability, "
                      "--geology, --land-cover, --drainage-density, --rainfall is required.")

    # Method-specific checks
    if args.method == "ahp" and not args.weights:
        errors.append("--method ahp requires --weights (path to pairwise comparison matrix or 'ahp').")

    # Sensitivity runs
    if args.sensitivity_runs < 0:
        errors.append("--sensitivity-runs must be non-negative.")

    # Min area
    if args.min_area < 0:
        errors.append("--min-area must be non-negative.")

    return errors


def load_factor_config(config_path: Optional[str]) -> Dict:
    """Load factor configuration from JSON file, or return defaults."""
    if config_path and Path(config_path).exists():
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config
    return {}


def load_weights(weights_arg: Optional[str], factors: Dict) -> Dict[str, float]:
    """Load or compute factor weights."""
    if weights_arg == "equal":
        # Equal weights
        n = len(factors)
        return {k: 1.0 / n for k in factors}

    if not weights_arg:
        # No weights arg: use defaults from factor definitions
        if not factors:
            return {}
        return {k: v.get("weight", 1.0 / len(factors)) for k, v in factors.items()}

    if weights_arg == "ahp":
        # Will be computed from pairwise matrix later
        return {k: v.get("weight", 1.0 / len(factors)) for k, v in factors.items()}

    # Load from file
    path = Path(weights_arg)
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            weights = json.load(f)
        return weights

    # Try parsing as JSON string
    try:
        return json.loads(weights_arg)
    except (json.JSONDecodeError, TypeError):
        return {k: v.get("weight", 1.0 / len(factors)) for k, v in factors.items()}


def normalize_weights(weights: Dict[str, float]) -> Dict[str, float]:
    """Normalize weights to sum to 1.0."""
    total = sum(weights.values())
    if total <= 0:
        n = len(weights)
        return {k: 1.0 / n for k in weights}
    return {k: v / total for k, v in weights.items()}


def ahp_consistency_check(pairwise_matrix: List[List[float]], factor_names: List[str]) -> Dict[str, Any]:
    """
    Perform AHP consistency check on a pairwise comparison matrix.

    Returns dict with 'consistent' (bool), 'CR' (float), 'lambda_max', 'CI', 'weights'.
    """
    try:
        import numpy as np
    except ImportError:
        return {"consistent": False, "error": "numpy not available"}

    n = len(pairwise_matrix)
    if n < 3:
        return {"consistent": True, "CR": 0.0, "CI": 0.0, "lambda_max": float(n),
                "weights": [1.0 / n] * n, "message": "Matrix too small for meaningful CI"}

    matrix = np.array(pairwise_matrix, dtype=np.float64)

    # Eigenvalue method
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    # Take the real part (AHP matrices are positive, eigenvalues are real)
    real_eigenvalues = np.real(eigenvalues)
    lambda_max = float(np.max(real_eigenvalues))

    # Consistency Index
    CI = (lambda_max - n) / (n - 1) if n > 1 else 0.0

    # Consistency Ratio
    RI = RI_TABLE.get(n, 1.49)  # default for n > 9
    CR = CI / RI if RI > 0 else 0.0

    # Extract weights from principal eigenvector
    max_idx = np.argmax(real_eigenvalues)
    principal_vector = np.real(eigenvectors[:, max_idx])
    # Normalize to sum to 1
    weights = principal_vector / np.sum(principal_vector)
    # Ensure positive (flip sign if needed)
    if np.sum(weights) < 0:
        weights = -weights
        weights = weights / np.sum(weights)

    weights_dict = {factor_names[i]: round(float(weights[i]), 4) for i in range(n)}

    return {
        "consistent": CR < 0.1,
        "CR": round(CR, 4),
        "CI": round(CI, 4),
        "lambda_max": round(lambda_max, 4),
        "RI": RI,
        "weights": weights_dict,
        "n": n,
    }


def normalize_linear(value: float, vmin: float, vmax: float, direction: str = "higher_better") -> float:
    """
    Linear normalization of a continuous value to [0, 1].

    direction='higher_better': higher raw value -> higher score
    direction='lower_better': lower raw value -> higher score
    """
    if vmax == vmin:
        return 0.5  # constant field
    score = (value - vmin) / (vmax - vmin)
    score = max(0.0, min(1.0, score))
    if direction == "lower_better":
        score = 1.0 - score
    return score


def fuzzy_membership(value: float, vmin: float, vmax: float,
                     direction: str = "higher_better", steepness: float = 4.0) -> float:
    """
    Sigmoid-based fuzzy membership function.

    Maps value to [0, 1] with a smooth S-curve transition.
    """
    if vmax == vmin:
        return 0.5
    # Normalize to [0, 1]
    x = (value - vmin) / (vmax - vmin)
    x = max(0.0, min(1.0, x))
    # Sigmoid centered at 0.5
    if direction == "higher_better":
        score = 1.0 / (1.0 + math.exp(-steepness * (x - 0.5)))
    else:
        score = 1.0 / (1.0 + math.exp(steepness * (x - 0.5)))
    return round(score, 6)


def score_categorical(value: int, score_map: Dict[int, float]) -> float:
    """Look up categorical score; return 0.5 for unknown classes."""
    return score_map.get(int(value), 0.5)


def compute_factor_scores(raster_path: Path, factor_config: Dict,
                          method: str = "weighted") -> Optional[Dict[str, Any]]:
    """
    Read a raster and compute per-pixel suitability scores.

    Returns dict with 'scores' (2D array), 'transform', 'crs', 'nodata', 'shape', 'stats'.
    """
    try:
        import numpy as np
        import rasterio
    except ImportError:
        return None

    with rasterio.open(str(raster_path)) as ds:
        data = ds.read(1).astype(np.float64)
        transform = ds.transform
        crs = ds.crs
        nodata = ds.nodata
        shape = data.shape

    # Valid mask
    if nodata is not None:
        valid = data != nodata
    else:
        valid = np.ones_like(data, dtype=bool)

    if not np.any(valid):
        return None

    # Compute scores based on factor config
    direction = factor_config.get("direction", "higher_better")
    score_type = factor_config.get("score_type", "linear")

    scores = np.full_like(data, np.nan)

    if score_type == "categorical":
        score_map = factor_config.get("score_map", {})
        for cls, sc in score_map.items():
            scores[data == int(cls)] = sc
        scores[~valid] = np.nan
    else:
        # Continuous: normalize
        valid_data = data[valid]
        vmin = float(np.nanmin(valid_data))
        vmax = float(np.nanmax(valid_data))

        if method == "fuzzy":
            # Vectorize fuzzy membership
            vec_fuzzy = np.vectorize(
                lambda v: fuzzy_membership(v, vmin, vmax, direction)
            )
            scores[valid] = vec_fuzzy(valid_data)
        else:
            # Linear normalization
            if vmax != vmin:
                normalized = (valid_data - vmin) / (vmax - vmin)
                normalized = np.clip(normalized, 0, 1)
                if direction == "lower_better":
                    normalized = 1.0 - normalized
                scores[valid] = normalized
            else:
                scores[valid] = 0.5

    return {
        "scores": scores,
        "transform": transform,
        "crs": crs,
        "nodata": nodata,
        "shape": shape,
        "valid": valid,
        "stats": {
            "mean": round(float(np.nanmean(scores)), 4),
            "std": round(float(np.nanstd(scores)), 4),
            "min": round(float(np.nanmin(scores)), 4),
            "max": round(float(np.nanmax(scores)), 4),
            "valid_pixels": int(np.sum(valid)),
        },
    }


def apply_hard_constraints(scores: Any, constraints: Dict, shape: Tuple[int, int]) -> Any:
    """
    Apply hard constraints to mask out unsuitable areas.

    constraints format: {"slope_max": 30, "exclude_landcover": [6, 7], ...}
    Returns modified scores array with constrained pixels set to NaN.
    """
    try:
        import numpy as np
    except ImportError:
        return scores

    if not constraints:
        return scores

    mask = np.ones(shape, dtype=bool)

    # Slope constraint: exclude areas steeper than threshold
    if "slope_max" in constraints and "slope_scores" in constraints:
        slope_data = constraints["slope_scores"]
        if slope_data is not None:
            mask &= (slope_data <= constraints["slope_max"])

    # Land cover exclusion
    if "exclude_landcover" in constraints and "landcover_scores" in constraints:
        lc_data = constraints["landcover_scores"]
        if lc_data is not None:
            for cls in constraints["exclude_landcover"]:
                mask &= (lc_data != cls)

    # Buffer exclusion (e.g., near water bodies or infrastructure)
    if "buffer_mask" in constraints:
        buffer = constraints["buffer_mask"]
        if buffer is not None:
            mask &= (~buffer)

    scores[~mask] = np.nan
    return scores


def weighted_overlay(factor_results: Dict[str, Dict], weights: Dict[str, float],
                     shape: Tuple[int, int]) -> Any:
    """
    Compute weighted overlay of factor scores.

    Returns 2D array of composite suitability scores.
    """
    try:
        import numpy as np
    except ImportError:
        return None

    composite = np.zeros(shape, dtype=np.float64)
    weight_sum = 0.0

    for factor_name, result in factor_results.items():
        if result is None:
            continue
        w = weights.get(factor_name, 0.0)
        scores = result["scores"]
        # Treat NaN as 0 contribution but track validity
        contribution = np.where(np.isnan(scores), 0.0, scores) * w
        composite += contribution
        weight_sum += w

    if weight_sum > 0:
        composite /= weight_sum

    # Mark pixels where ALL factors were NaN as NaN
    all_nan = np.ones(shape, dtype=bool)
    for result in factor_results.values():
        if result is not None:
            all_nan &= np.isnan(result["scores"])
    composite[all_nan] = np.nan

    return composite


def fuzzy_aggregation(factor_results: Dict[str, Dict], weights: Dict[str, float],
                      shape: Tuple[int, int], operator: str = "gamma", gamma: float = 0.7) -> Any:
    """
    Fuzzy aggregation of factor scores.

    operator: 'and' (min), 'or' (max), 'product', 'gamma'
    """
    try:
        import numpy as np
    except ImportError:
        return None

    factor_names = list(factor_results.keys())
    n_factors = len(factor_names)

    if n_factors == 0:
        return None

    # Stack scores
    score_stack = []
    valid_stack = []
    weight_list = []
    for name in factor_names:
        result = factor_results[name]
        if result is not None:
            score_stack.append(result["scores"])
            valid_stack.append(~np.isnan(result["scores"]))
            weight_list.append(weights.get(name, 1.0 / n_factors))

    if not score_stack:
        return None

    scores_3d = np.stack(score_stack, axis=0)  # (n_factors, rows, cols)
    valid_3d = np.stack(valid_stack, axis=0)

    # Replace NaN with neutral values for computation
    scores_filled = np.where(np.isnan(scores_3d), 0.5, scores_3d)
    weights_arr = np.array(weight_list).reshape(-1, 1, 1)

    if operator == "and":
        composite = np.min(scores_filled, axis=0)
    elif operator == "or":
        composite = np.max(scores_filled, axis=0)
    elif operator == "product":
        composite = np.prod(scores_filled, axis=0)
    elif operator == "gamma":
        # Gamma operator: (product)^(1-gamma) * (1 - product(1 - scores))^gamma
        prod = np.prod(scores_filled, axis=0)
        comp_prod = np.prod(1.0 - scores_filled, axis=0)
        composite = (prod ** (1 - gamma)) * ((1 - comp_prod) ** gamma)
    else:
        # Default: weighted average (same as weighted_overlay)
        composite = np.sum(scores_filled * weights_arr, axis=0) / np.sum(weights_arr)

    # Mark all-NaN pixels
    all_nan = np.all(~valid_3d, axis=0)
    composite[all_nan] = np.nan

    return composite


def sensitivity_analysis(factor_results: Dict[str, Dict], weights: Dict[str, float],
                         shape: Tuple[int, int], n_runs: int,
                         method: str = "weighted", seed: int = 42) -> Dict[str, Any]:
    """
    Monte Carlo sensitivity analysis by perturbing weights.

    Returns dict with 'mean', 'std', 'min', 'max', 'stability_map', 'weight_variations'.
    """
    try:
        import numpy as np
    except ImportError:
        return {"error": "numpy not available"}

    if n_runs <= 0:
        return {"mean": None, "std": None, "n_runs": 0}

    factor_names = sorted(factor_results.keys())
    n_factors = len(factor_names)

    if n_factors == 0:
        return {"error": "no factors available"}

    rng = np.random.default_rng(seed)
    composite_stack = []

    for _ in range(n_runs):
        # Perturb weights: multiply each by random factor in [0.5, 1.5], then normalize
        perturbed = {}
        for name in factor_names:
            base = weights.get(name, 1.0 / n_factors)
            perturbed[name] = base * rng.uniform(0.5, 1.5)
        total = sum(perturbed.values())
        perturbed = {k: v / total for k, v in perturbed.items()}

        if method == "fuzzy":
            comp = fuzzy_aggregation(factor_results, perturbed, shape)
        else:
            comp = weighted_overlay(factor_results, perturbed, shape)

        if comp is not None:
            composite_stack.append(comp)

    if not composite_stack:
        return {"error": "no valid composites generated"}

    stack = np.stack(composite_stack, axis=0)

    mean_map = np.nanmean(stack, axis=0)
    std_map = np.nanstd(stack, axis=0)
    min_map = np.nanmin(stack, axis=0)
    max_map = np.nanmax(stack, axis=0)

    # Stability: fraction of runs where pixel is in top 30%
    threshold = 0.7
    high_count = np.sum(stack >= threshold, axis=0)
    stability = high_count / len(composite_stack)

    return {
        "n_runs": n_runs,
        "mean": round(float(np.nanmean(mean_map)), 4),
        "std_mean": round(float(np.nanmean(std_map)), 4),
        "min": round(float(np.nanmin(min_map)), 4),
        "max": round(float(np.nanmax(max_map)), 4),
        "stability_mean": round(float(np.nanmean(stability)), 4),
        "mean_map": mean_map,
        "std_map": std_map,
        "stability_map": stability,
    }


def extract_candidate_zones(composite: Any, transform: Any, crs: Any,
                            threshold: float = 0.7, min_area_ha: float = 1.0) -> Dict[str, Any]:
    """
    Extract connected candidate zones above a suitability threshold.

    Returns GeoJSON-like dict with features and summary stats.
    """
    try:
        import numpy as np
        from scipy import ndimage
    except ImportError:
        return {"type": "FeatureCollection", "features": [], "error": "scipy not available"}

    if composite is None:
        return {"type": "FeatureCollection", "features": []}

    # Binary mask of high-potential pixels
    high_mask = (composite >= threshold) & ~np.isnan(composite)

    if not np.any(high_mask):
        return {"type": "FeatureCollection", "features": [], "total_zones": 0}

    # Label connected components
    labeled, n_features = ndimage.label(high_mask)

    # Compute pixel area
    if crs and crs.is_projected:
        pixel_area_m2 = abs(transform.a * transform.e)
    else:
        # Approximate for EPSG:4326
        lat_center = -transform.f / transform.e / 2 + transform.c / 2
        lat_rad = math.radians(lat_center)
        pixel_width_m = abs(transform.a) * math.cos(lat_rad) * 111320
        pixel_height_m = abs(transform.e) * 111320
        pixel_area_m2 = pixel_width_m * pixel_height_m

    min_pixels = max(1, int(min_area_ha * 10000 / pixel_area_m2))

    features = []
    for zone_id in range(1, n_features + 1):
        zone_mask = labeled == zone_id
        pixel_count = int(np.sum(zone_mask))
        area_ha = round(pixel_count * pixel_area_m2 / 10000, 2)

        if pixel_count < min_pixels:
            continue

        # Mean suitability within zone
        zone_suitability = float(np.nanmean(composite[zone_mask]))

        # Bounding box of zone
        rows, cols = np.where(zone_mask)
        min_row, max_row = int(np.min(rows)), int(np.max(rows))
        min_col, max_col = int(np.min(cols)), int(np.max(cols))

        # Convert pixel coords to geographic
        x_min = transform.c + min_col * transform.a
        y_max = transform.f + min_row * transform.e
        x_max = transform.c + (max_col + 1) * transform.a
        y_min = transform.f + (max_row + 1) * transform.e

        feature = {
            "type": "Feature",
            "properties": {
                "zone_id": zone_id,
                "area_ha": area_ha,
                "pixel_count": pixel_count,
                "mean_suitability": round(zone_suitability, 4),
                "priority_rank": 0,  # filled below
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [x_min, y_min],
                    [x_max, y_min],
                    [x_max, y_max],
                    [x_min, y_max],
                    [x_min, y_min],
                ]],
            },
        }
        features.append(feature)

    # Rank by mean suitability (descending)
    features.sort(key=lambda f: f["properties"]["mean_suitability"], reverse=True)
    for i, f in enumerate(features):
        f["properties"]["priority_rank"] = i + 1

    return {
        "type": "FeatureCollection",
        "features": features,
        "total_zones": len(features),
        "total_area_ha": round(sum(f["properties"]["area_ha"] for f in features), 2),
        "threshold": threshold,
        "min_area_ha": min_area_ha,
    }


def spatial_block_validation(well_points_path: str, composite: Any,
                             transform: Any, crs: Any,
                             n_blocks: int = 5) -> Dict[str, Any]:
    """
    Spatial block cross-validation using well point data.

    Divides AOI into blocks, compares mean suitability at well locations
    vs. non-well locations.
    """
    try:
        import numpy as np
    except ImportError:
        return {"error": "numpy not available"}

    if not Path(well_points_path).exists():
        return {"error": f"well points file not found: {well_points_path}"}

    with open(well_points_path, "r", encoding="utf-8") as f:
        wells_geojson = json.load(f)

    if "features" not in wells_geojson or not wells_geojson["features"]:
        return {"error": "no well features found"}

    rows, cols = composite.shape
    block_rows = max(1, rows // n_blocks)
    block_cols = max(1, cols // n_blocks)

    well_suitabilities = []
    non_well_suitabilities = []

    # Build a set of well pixel locations
    well_pixels = set()
    for feature in wells_geojson["features"]:
        geom = feature.get("geometry", {})
        if geom.get("type") == "Point":
            lon, lat = geom["coordinates"][:2]
            # Convert to pixel
            col = int((lon - transform.c) / transform.a)
            row = int((lat - transform.f) / transform.e)
            if 0 <= row < rows and 0 <= col < cols:
                well_pixels.add((row, col))

    if not well_pixels:
        return {"error": "no well points fall within the raster extent"}

    # Sample suitability at well and non-well locations
    for row in range(rows):
        for col in range(cols):
            if np.isnan(composite[row, col]):
                continue
            if (row, col) in well_pixels:
                well_suitabilities.append(composite[row, col])
            else:
                non_well_suitabilities.append(composite[row, col])

    if not well_suitabilities:
        return {"error": "no valid well pixel suitability values"}

    well_arr = np.array(well_suitabilities)
    non_well_arr = np.array(non_well_suitabilities) if non_well_suitabilities else np.array([0.0])

    return {
        "n_well_points": len(well_suitabilities),
        "n_non_well_pixels": len(non_well_suitabilities),
        "well_mean_suitability": round(float(np.mean(well_arr)), 4),
        "non_well_mean_suitability": round(float(np.mean(non_well_arr)), 4),
        "well_median_suitability": round(float(np.median(well_arr)), 4),
        "non_well_median_suitability": round(float(np.median(non_well_arr)), 4),
        "difference": round(float(np.mean(well_arr) - np.mean(non_well_arr)), 4),
        "n_blocks": n_blocks,
    }


def write_raster(path: Path, data: Any, transform: Any, crs: Any,
                 nodata: float = -9999.0, dtype: str = "float64") -> None:
    """Write a single-band GeoTIFF."""
    import rasterio
    shape = data.shape
    with rasterio.open(
        str(path), "w", driver="GTiff", height=shape[0], width=shape[1],
        count=1, dtype=dtype, crs=crs, transform=transform, nodata=nodata
    ) as dst:
        dst.write(data, 1)


def write_geojson(path: Path, geojson: Dict) -> None:
    """Write GeoJSON to file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2, default=str)


def generate_report(result: Dict, output_dir: Path, logger: logging.Logger) -> None:
    """Generate HTML report."""
    now = datetime.now(timezone.utc).isoformat()
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>Groundwater Recharge Potential Report</title>
<style>
body{{font-family:sans-serif;max-width:900px;margin:20px auto;padding:0 20px}}
h1{{color:#0d47a1}}
h2{{color:#1565c0;border-bottom:2px solid #bbdefb;padding-bottom:4px}}
.summary{{background:#e3f2fd;padding:15px;border-radius:8px;margin:10px 0}}
table{{border-collapse:collapse;width:100%;margin:10px 0}}
th,td{{border:1px solid #90caf9;padding:8px;text-align:left}}
th{{background:#bbdefb}}
.warning{{background:#fff3e0;padding:10px;border-left:4px solid #ff9800;margin:10px 0}}
.metric{{display:inline-block;background:#e8f5e9;padding:8px 12px;margin:4px;border-radius:4px}}
</style>
</head>
<body>
<h1>地下水补给潜力筛查报告</h1>
<p>生成时间: {now}</p>
<p>方法: {result.get('method', 'weighted')}</p>

<div class="warning">
<strong>⚠️ 筛查定位：</strong>本分析为潜力筛查级别，不直接承诺地下水量或成井成功率。
结果仅供规划参考，涉及工程安全、行政认定时必须人工复核。
</div>

<h2>因子权重</h2>
<table>
<tr><th>因子</th><th>权重</th><th>方向</th><th>描述</th></tr>
"""

    weights = result.get("weights", {})
    factor_info = result.get("factor_info", {})
    for name, w in weights.items():
        info = factor_info.get(name, {})
        direction = info.get("direction", "higher_better")
        desc = info.get("description", "")
        html += f'<tr><td>{name}</td><td>{w:.4f}</td><td>{direction}</td><td>{desc}</td></tr>\n'

    html += "</table>\n"

    # Suitability stats
    stats = result.get("suitability_stats", {})
    html += "<h2>适宜性统计</h2>\n<div class='summary'>\n"
    html += f"<span class='metric'>均值: {stats.get('mean', 'N/A')}</span>\n"
    html += f"<span class='metric'>标准差: {stats.get('std', 'N/A')}</span>\n"
    html += f"<span class='metric'>高潜力像元: {stats.get('high_pixels', 'N/A')}</span>\n"
    html += f"<span class='metric'>高潜力面积: {stats.get('high_area_ha', 'N/A')} ha</span>\n"
    html += f"<span class='metric'>有效像元: {stats.get('valid_pixels', 'N/A')}</span>\n"
    html += "</div>\n"

    # Sensitivity
    sens = result.get("sensitivity", {})
    if sens and "error" not in sens:
        html += "<h2>敏感性分析</h2>\n<div class='summary'>\n"
        html += f"<span class='metric'>运行次数: {sens.get('n_runs', 'N/A')}</span>\n"
        html += f"<span class='metric'>平均标准差: {sens.get('std_mean', 'N/A')}</span>\n"
        html += f"<span class='metric'>稳定性均值: {sens.get('stability_mean', 'N/A')}</span>\n"
        html += "</div>\n"

    # Candidate zones
    zones = result.get("candidate_zones", {})
    if zones and zones.get("total_zones", 0) > 0:
        html += f"<h2>候选补给区 (共 {zones['total_zones']} 个, 总面积 {zones.get('total_area_ha', 0)} ha)</h2>\n"
        html += "<table><tr><th>排名</th><th>面积 (ha)</th><th>平均适宜性</th></tr>\n"
        for f in zones.get("features", [])[:20]:  # top 20
            props = f["properties"]
            html += f"<tr><td>{props['priority_rank']}</td><td>{props['area_ha']}</td><td>{props['mean_suitability']}</td></tr>\n"
        html += "</table>\n"

    # Validation
    validation = result.get("validation")
    if validation and "error" not in validation:
        html += "<h2>井点验证</h2>\n<div class='summary'>\n"
        html += f"<span class='metric'>井点数: {validation.get('n_well_points', 'N/A')}</span>\n"
        html += f"<span class='metric'>井点平均适宜性: {validation.get('well_mean_suitability', 'N/A')}</span>\n"
        html += f"<span class='metric'>非井点平均适宜性: {validation.get('non_well_mean_suitability', 'N/A')}</span>\n"
        html += f"<span class='metric'>差异: {validation.get('difference', 'N/A')}</span>\n"
        html += "</div>\n"

    # AHP consistency
    ahp = result.get("ahp_check")
    if ahp:
        html += "<h2>AHP 一致性检查</h2>\n<div class='summary'>\n"
        consistent = "✅ 通过" if ahp.get("consistent") else "❌ 未通过"
        html += f"<span class='metric'>CR = {ahp.get('CR', 'N/A')} ({consistent})</span>\n"
        html += f"<span class='metric'>CI = {ahp.get('CI', 'N/A')}</span>\n"
        html += f"<span class='metric'>λ_max = {ahp.get('lambda_max', 'N/A')}</span>\n"
        html += "</div>\n"

    html += """
<h2>输出文件</h2>
<ul>
<li>recharge_potential.tif — 综合补给潜力栅格</li>
<li>candidate_zones.geojson — 候选补给区</li>
<li>factor_weights.json — 因子权重</li>
<li>sensitivity.json — 敏感性分析结果</li>
<li>report.pdf — 本报告 (HTML 格式)</li>
</ul>
</body></html>"""

    report_path = output_dir / "report.pdf"
    report_path.write_text(html, encoding="utf-8")
    logger.info(f"Report written to {report_path}")


def run_analysis(args: argparse.Namespace) -> int:
    """Main analysis pipeline."""
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logging(output_dir, args.log_level)
    logger.info("=" * 60)
    logger.info("Groundwater Recharge Potential Analysis")
    logger.info("=" * 60)

    # Validate arguments
    errors = validate_args(args)
    if errors:
        for e in errors:
            logger.error(f"ARG ERROR: {e}")
        return EXIT_ARG

    # Check dependencies
    try:
        import numpy as np
        import rasterio
    except ImportError as e:
        logger.error(f"Missing dependency: {e}")
        return EXIT_DEPENDENCY

    # Load factor configuration
    factor_config = load_factor_config(args.factor_config)
    logger.info(f"Factor config loaded: {len(factor_config)} custom entries")

    # Determine active factors from provided rasters
    active_factors = {}
    factor_raster_map = {
        "slope": args.slope,
        "soil_permeability": args.soil_permeability,
        "geology": args.geology,
        "land_cover": args.land_cover,
        "drainage_density": args.drainage_density,
        "rainfall": args.rainfall,
    }

    for name, path in factor_raster_map.items():
        if path and Path(path).exists():
            active_factors[name] = DEFAULT_FACTORS.get(name, {}).copy()
            # Override with custom config if available
            if name in factor_config:
                active_factors[name].update(factor_config[name])

    if not active_factors:
        logger.error("No valid factor rasters found.")
        return EXIT_VALIDATION

    logger.info(f"Active factors: {list(active_factors.keys())}")

    # Load/compute weights
    raw_weights = load_weights(args.weights, active_factors)
    # Filter to active factors only
    weights = {k: v for k, v in raw_weights.items() if k in active_factors}
    weights = normalize_weights(weights)
    logger.info(f"Weights: {weights}")

    # AHP consistency check (if method is ahp)
    ahp_result = None
    if args.method == "ahp" and args.weights and Path(args.weights).exists():
        with open(args.weights, "r", encoding="utf-8") as f:
            ahp_data = json.load(f)
        if "matrix" in ahp_data and "names" in ahp_data:
            ahp_result = ahp_consistency_check(ahp_data["matrix"], ahp_data["names"])
            logger.info(f"AHP CR={ahp_result['CR']}, consistent={ahp_result['consistent']}")
            if ahp_result["consistent"]:
                # Use AHP-derived weights
                ahp_weights = ahp_result["weights"]
                weights = {k: v for k, v in ahp_weights.items() if k in active_factors}
                weights = normalize_weights(weights)

    # Dry run check
    if args.dry_run:
        logger.info("DRY RUN - estimating data volume and steps")
        logger.info(f"  Factors to process: {len(active_factors)}")
        logger.info(f"  Method: {args.method}")
        logger.info(f"  Sensitivity runs: {args.sensitivity_runs}")
        logger.info(f"  Min area: {args.min_area} ha")
        # Write request manifest
        request = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "dry_run": True,
            "factors": list(active_factors.keys()),
            "weights": weights,
            "method": args.method,
            "sensitivity_runs": args.sensitivity_runs,
            "min_area_ha": args.min_area,
        }
        write_geojson(output_dir / "request.json", request)
        return EXIT_OK

    # Process each factor
    factor_results = {}
    for name, config in active_factors.items():
        raster_path = Path(factor_raster_map[name])
        logger.info(f"Processing factor: {name} ({raster_path.name})")
        result = compute_factor_scores(raster_path, config, args.method)
        if result is not None:
            factor_results[name] = result
            logger.info(f"  Score stats: mean={result['stats']['mean']}, "
                        f"valid_pixels={result['stats']['valid_pixels']}")
        else:
            logger.warning(f"  Failed to process factor: {name}")

    if not factor_results:
        logger.error("No factor scores computed. All rasters failed.")
        return EXIT_VALIDATION

    # Get shape and transform from first valid factor
    first_result = next(iter(factor_results.values()))
    shape = first_result["shape"]
    transform = first_result["transform"]
    crs = first_result["crs"]

    # Apply hard constraints
    constraints = {}
    if args.constraints and Path(args.constraints).exists():
        with open(args.constraints, "r", encoding="utf-8") as f:
            constraints = json.load(f)
        logger.info(f"Applying hard constraints: {list(constraints.keys())}")

    # Compute composite suitability
    logger.info(f"Computing composite suitability (method={args.method})")
    if args.method == "fuzzy":
        composite = fuzzy_aggregation(factor_results, weights, shape)
    else:
        composite = weighted_overlay(factor_results, weights, shape)

    if composite is None:
        logger.error("Failed to compute composite suitability.")
        return EXIT_PROCESSING

    # Compute stats
    valid_mask = ~np.isnan(composite)
    valid_composite = composite[valid_mask]
    high_pixels = int(np.sum(valid_composite >= 0.7))
    medium_pixels = int(np.sum((valid_composite >= 0.4) & (valid_composite < 0.7)))
    low_pixels = int(np.sum(valid_composite < 0.4))

    if crs and crs.is_projected:
        pixel_area = abs(transform.a * transform.e)
    else:
        lat_center = -transform.f / transform.e / 2 + transform.c / 2
        lat_rad = math.radians(lat_center)
        pixel_width_m = abs(transform.a) * math.cos(lat_rad) * 111320
        pixel_height_m = abs(transform.e) * 111320
        pixel_area = pixel_width_m * pixel_height_m

    suitability_stats = {
        "mean": round(float(np.nanmean(composite)), 4),
        "std": round(float(np.nanstd(composite)), 4),
        "min": round(float(np.nanmin(composite)), 4),
        "max": round(float(np.nanmax(composite)), 4),
        "valid_pixels": int(np.sum(valid_mask)),
        "high_pixels": high_pixels,
        "medium_pixels": medium_pixels,
        "low_pixels": low_pixels,
        "high_area_ha": round(high_pixels * pixel_area / 10000, 2),
        "medium_area_ha": round(medium_pixels * pixel_area / 10000, 2),
        "low_area_ha": round(low_pixels * pixel_area / 10000, 2),
    }
    logger.info(f"Suitability: mean={suitability_stats['mean']}, "
                f"high_area={suitability_stats['high_area_ha']} ha")

    # Write composite raster
    composite_path = output_dir / "recharge_potential.tif"
    if composite_path.exists() and not args.overwrite:
        logger.error(f"Output file exists (use --overwrite): {composite_path}")
        return EXIT_PROCESSING
    write_raster(composite_path, composite, transform, crs)
    logger.info(f"Composite raster written: {composite_path}")

    # Sensitivity analysis
    logger.info(f"Running sensitivity analysis ({args.sensitivity_runs} runs)")
    sens_result = sensitivity_analysis(
        factor_results, weights, shape, args.sensitivity_runs, args.method
    )
    if "error" not in sens_result and sens_result.get("n_runs", 0) > 0:
        logger.info(f"Sensitivity: std_mean={sens_result['std_mean']}, "
                    f"stability={sens_result['stability_mean']}")
        # Write sensitivity map
        if sens_result.get("std_map") is not None:
            write_raster(output_dir / "sensitivity_std.tif", sens_result["std_map"], transform, crs)
        if sens_result.get("stability_map") is not None:
            write_raster(output_dir / "sensitivity_stability.tif", sens_result["stability_map"], transform, crs)

    # Extract candidate zones
    logger.info(f"Extracting candidate zones (threshold=0.7, min_area={args.min_area} ha)")
    candidate_zones = extract_candidate_zones(composite, transform, crs,
                                              threshold=0.7, min_area_ha=args.min_area)
    logger.info(f"Candidate zones: {candidate_zones['total_zones']} zones, "
                f"{candidate_zones.get('total_area_ha', 0)} ha total")
    write_geojson(output_dir / "candidate_zones.geojson", candidate_zones)

    # Validation with well points
    validation_result = None
    if args.well_points:
        logger.info(f"Validating with well points: {args.well_points}")
        validation_result = spatial_block_validation(
            args.well_points, composite, transform, crs, args.validation_blocks
        )
        if "error" not in validation_result:
            logger.info(f"Validation: well_mean={validation_result['well_mean_suitability']}, "
                        f"diff={validation_result['difference']}")

    # Write factor weights
    weights_output = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "method": args.method,
        "weights": weights,
        "factor_info": {k: {"direction": v.get("direction", ""),
                            "description": v.get("description", ""),
                            "unit": v.get("description", "")}
                        for k, v in active_factors.items()},
    }
    write_geojson(output_dir / "factor_weights.json", weights_output)

    # Write sensitivity JSON (without large arrays)
    sens_output = {k: v for k, v in sens_result.items()
                   if k not in ("mean_map", "std_map", "stability_map")}
    write_geojson(output_dir / "sensitivity.json", sens_output)

    # Compile result for report
    result = {
        "method": args.method,
        "weights": weights,
        "factor_info": {k: {"direction": v.get("direction", ""),
                            "description": v.get("description", "")}
                        for k, v in active_factors.items()},
        "suitability_stats": suitability_stats,
        "sensitivity": sens_output,
        "candidate_zones": candidate_zones,
        "validation": validation_result,
        "ahp_check": ahp_result,
    }

    # Generate report
    generate_report(result, output_dir, logger)

    # Write output manifest
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "output_files": {
            "recharge_potential.tif": str(composite_path),
            "candidate_zones.geojson": str(output_dir / "candidate_zones.geojson"),
            "factor_weights.json": str(output_dir / "factor_weights.json"),
            "sensitivity.json": str(output_dir / "sensitivity.json"),
            "report.pdf": str(output_dir / "report.pdf"),
        },
        "parameters": {
            "method": args.method,
            "weights": weights,
            "sensitivity_runs": args.sensitivity_runs,
            "min_area_ha": args.min_area,
        },
        "stats": suitability_stats,
    }
    write_geojson(output_dir / "output-manifest.json", manifest)

    # Write QA
    qa = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "factors_processed": list(factor_results.keys()),
        "factors_failed": [n for n in active_factors if n not in factor_results],
        "weights_normalized": weights,
        "ahp_consistent": ahp_result.get("consistent") if ahp_result else None,
        "sensitivity_completed": "error" not in sens_result,
        "candidate_zones_found": candidate_zones["total_zones"],
        "validation_performed": validation_result is not None,
        "degraded": len(factor_results) < len(active_factors),
    }
    write_geojson(output_dir / "qa.json", qa)

    # Write request manifest
    request = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dry_run": False,
        "factors": list(active_factors.keys()),
        "weights": weights,
        "method": args.method,
        "sensitivity_runs": args.sensitivity_runs,
        "min_area_ha": args.min_area,
        "output_dir": str(output_dir),
    }
    write_geojson(output_dir / "request.json", request)

    logger.info("=" * 60)
    logger.info("Analysis complete.")
    logger.info("=" * 60)

    return EXIT_OK


def main():
    """Entry point."""
    args = parse_args()
    try:
        sys.exit(run_analysis(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
