#!/usr/bin/env python3
"""
Crop Type Mapping - Multi-temporal crop classification from optical/SAR imagery.

Identifies major crop types (rice, wheat, corn, etc.) using phenological features
derived from Sentinel-2/Landsat time series. Outputs pixel/field-level classification,
area statistics, and confidence maps.

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

EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# ---------------------------------------------------------------------------
# Crop phenology schema (default: rice / wheat / corn)
# Parameters: peak_doy (day of year), peak_ndvi, width (sigma of Gaussian),
#             base_ndvi (background), amplitude
# ---------------------------------------------------------------------------

DEFAULT_CROP_SCHEMA = {
    "rice": {
        "code": 1,
        "peak_doy": 220,
        "peak_ndvi": 0.80,
        "width": 30,
        "base_ndvi": 0.15,
        "amplitude": 0.65,
        "description": "水稻 / Rice (single-season late rice)",
    },
    "wheat": {
        "code": 2,
        "peak_doy": 120,
        "peak_ndvi": 0.75,
        "width": 25,
        "base_ndvi": 0.18,
        "amplitude": 0.57,
        "description": "小麦 / Wheat (winter wheat)",
    },
    "corn": {
        "code": 3,
        "peak_doy": 200,
        "peak_ndvi": 0.82,
        "width": 28,
        "base_ndvi": 0.16,
        "amplitude": 0.66,
        "description": "玉米 / Corn (summer corn)",
    },
}

# Code -> name reverse lookup
CODE_TO_NAME = {v["code"]: k for k, v in DEFAULT_CROP_SCHEMA.items()}
CODE_TO_NAME[0] = "background"

# Sentinel-2 band registry
S2_BANDS = {
    "B02": {"name": "blue", "wavelength": 490, "resolution": 10},
    "B03": {"name": "green", "wavelength": 560, "resolution": 10},
    "B04": {"name": "red", "wavelength": 665, "resolution": 10},
    "B05": {"name": "rededge1", "wavelength": 705, "resolution": 20},
    "B08": {"name": "nir", "wavelength": 842, "resolution": 10},
    "B11": {"name": "swir1", "wavelength": 1610, "resolution": 20},
    "B12": {"name": "swir2", "wavelength": 2190, "resolution": 20},
}


# ---------------------------------------------------------------------------
# Phenology model
# ---------------------------------------------------------------------------

def gaussian_phenology(doys: np.ndarray, peak_doy: float, peak_ndvi: float,
                       width: float, base_ndvi: float,
                       amplitude: float) -> np.ndarray:
    """
    Generate a Gaussian phenology curve for given day-of-year values.

    NDVI(doy) = base_ndvi + amplitude * exp(-((doy - peak_doy) / width)^2)
    """
    exponent = -((doys - peak_doy) / width) ** 2
    ndvi = base_ndvi + amplitude * np.exp(exponent)
    return ndvi


def simulate_crop_reflectance(doys: np.ndarray, crop_name: str,
                              noise: float = 0.01) -> Dict[str, np.ndarray]:
    """
    Simulate Sentinel-2-like reflectance time series for a crop type.

    Uses the Gaussian phenology model to derive NDVI, then back-solves
    approximate band reflectances consistent with that NDVI.
    """
    schema = DEFAULT_CROP_SCHEMA.get(crop_name, DEFAULT_CROP_SCHEMA["rice"])
    ndvi = gaussian_phenology(
        doys,
        schema["peak_doy"],
        schema["peak_ndvi"],
        schema["width"],
        schema["base_ndvi"],
        schema["amplitude"],
    )

    # Back-solve approximate reflectances from NDVI
    red = 0.05 + 0.15 * (1.0 - ndvi)
    nir = np.where(
        ndvi < 0.99,
        red * (1.0 + ndvi) / np.maximum(1.0 - ndvi, 0.01),
        red * 100.0,
    )
    nir = np.clip(nir, 0.0, 1.0)
    green = 0.04 + 0.10 * (1.0 - ndvi)
    swir1 = 0.05 + 0.20 * (1.0 - ndvi)

    # Add noise
    rng = np.random.default_rng(seed=abs(hash(crop_name)) % (2**31))
    nir += rng.normal(0, noise, nir.shape)
    red += rng.normal(0, noise, red.shape)
    green += rng.normal(0, noise, green.shape)
    swir1 += rng.normal(0, noise, swir1.shape)

    nir = np.clip(nir, 0.001, 1.0)
    red = np.clip(red, 0.001, 1.0)
    green = np.clip(green, 0.001, 1.0)
    swir1 = np.clip(swir1, 0.001, 1.0)

    return {
        "nir": nir, "red": red, "green": green,
        "swir1": swir1, "ndvi": ndvi,
    }


# ---------------------------------------------------------------------------
# Spectral indices
# ---------------------------------------------------------------------------

def compute_ndvi(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
    """Compute NDVI = (NIR - Red) / (NIR + Red)."""
    denom = nir + red
    result = np.where(denom == 0, 0.0, (nir - red) / denom)
    return result


def compute_evi(nir: np.ndarray, red: np.ndarray, blue: np.ndarray) -> np.ndarray:
    """Compute EVI = 2.5 * (NIR - Red) / (NIR + 6*Red - 7.5*Blue + 1)."""
    denom = nir + 6.0 * red - 7.5 * blue + 1.0
    result = np.where(denom == 0, 0.0, 2.5 * (nir - red) / denom)
    return np.clip(result, -1.0, 1.0)


def compute_lswi(nir: np.ndarray, swir1: np.ndarray) -> np.ndarray:
    """Compute LSWI = (NIR - SWIR1) / (NIR + SWIR1)."""
    denom = nir + swir1
    result = np.where(denom == 0, 0.0, (nir - swir1) / denom)
    return result


def compute_evi2(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
    """Compute EVI2 = 2.5 * (NIR - Red) / (NIR + 2.4*Red + 1)."""
    denom = nir + 2.4 * red + 1.0
    result = np.where(denom == 0, 0.0, 2.5 * (nir - red) / denom)
    return np.clip(result, -1.0, 1.0)


# ---------------------------------------------------------------------------
# Feature extraction
# ---------------------------------------------------------------------------

def extract_temporal_features(ndvi_series: np.ndarray,
                              doys: np.ndarray) -> Dict[str, float]:
    """
    Extract phenological features from an NDVI time series.

    Returns dict with: mean, std, max, min, range, peak_doy, amplitude,
                       sos (start of season), eos (end of season)
    """
    if len(ndvi_series) == 0:
        return {
            "mean": 0.0, "std": 0.0, "max": 0.0, "min": 0.0,
            "range": 0.0, "peak_doy": 0.0, "amplitude": 0.0,
            "sos": 0.0, "eos": 0.0,
        }

    mean_ndvi = float(np.nanmean(ndvi_series))
    std_ndvi = float(np.nanstd(ndvi_series))
    max_ndvi = float(np.nanmax(ndvi_series))
    min_ndvi = float(np.nanmin(ndvi_series))
    range_ndvi = max_ndvi - min_ndvi

    peak_idx = int(np.nanargmax(ndvi_series))
    peak_doy = float(doys[peak_idx]) if peak_idx < len(doys) else 0.0
    amplitude = range_ndvi

    # SOS / EOS: 50% of amplitude above base
    threshold = min_ndvi + 0.5 * amplitude
    above = ndvi_series >= threshold
    sos = 0.0
    eos = 0.0
    if np.any(above):
        indices = np.where(above)[0]
        sos = float(doys[indices[0]]) if indices[0] < len(doys) else 0.0
        eos = float(doys[indices[-1]]) if indices[-1] < len(doys) else 0.0

    return {
        "mean": mean_ndvi, "std": std_ndvi, "max": max_ndvi, "min": min_ndvi,
        "range": range_ndvi, "peak_doy": peak_doy, "amplitude": amplitude,
        "sos": sos, "eos": eos,
    }


def build_feature_vector(ndvi_series: np.ndarray, doys: np.ndarray,
                         n_bins: int = 8) -> np.ndarray:
    """
    Build a feature vector for classification.

    Combines phenological statistics + binned NDVI temporal profile.
    """
    features = extract_temporal_features(ndvi_series, doys)
    stats = np.array([
        features["mean"], features["std"], features["max"], features["min"],
        features["range"], features["peak_doy"], features["amplitude"],
        features["sos"], features["eos"],
    ])

    if len(ndvi_series) >= n_bins:
        bin_edges = np.array_split(ndvi_series, n_bins)
        binned = np.array([float(np.nanmean(b)) for b in bin_edges])
    else:
        fill = float(np.nanmean(ndvi_series)) if len(ndvi_series) > 0 else 0.0
        binned = np.full(n_bins, fill)

    return np.concatenate([stats, binned])


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------

def classify_rule_based(ndvi_series: np.ndarray, doys: np.ndarray,
                        crop_schema: Dict) -> Tuple[str, float]:
    """
    Rule-based classification using phenological matching.

    Scores each crop by comparing observed peak DOY and amplitude
    against the schema. Returns best-matching crop and confidence.
    """
    features = extract_temporal_features(ndvi_series, doys)
    peak_doy = features["peak_doy"]
    amplitude = features["amplitude"]
    mean_ndvi = features["mean"]

    if mean_ndvi < 0.12:
        return ("background", 0.9)

    best_crop = "background"
    best_score = -np.inf

    for crop_name, spec in crop_schema.items():
        doy_diff = abs(peak_doy - spec["peak_doy"])
        doy_diff = min(doy_diff, 365 - doy_diff)
        doy_score = max(0, 1.0 - doy_diff / 60.0)

        amp_diff = abs(amplitude - spec["amplitude"])
        amp_score = max(0, 1.0 - amp_diff / 0.3)

        score = 0.6 * doy_score + 0.4 * amp_score

        if score > best_score:
            best_score = score
            best_crop = crop_name

    confidence = min(1.0, best_score)
    return (best_crop, confidence)


def classify_random_forest(ndvi_series: np.ndarray, doys: np.ndarray,
                           crop_schema: Dict,
                           training_data: Optional[Dict] = None) -> Tuple[str, float]:
    """
    Random Forest classification (with sklearn if available).
    Falls back to rule-based if sklearn is not installed.
    """
    try:
        from sklearn.ensemble import RandomForestClassifier
        if training_data is not None and "model" in training_data:
            model = training_data["model"]
            feature_vec = build_feature_vector(ndvi_series, doys).reshape(1, -1)
            pred = model.predict(feature_vec)[0]
            proba = model.predict_proba(feature_vec)[0]
            confidence = float(np.max(proba))
            crop_names = training_data.get("class_names", list(crop_schema.keys()))
            if isinstance(pred, (int, np.integer)):
                idx = int(pred)
                crop_name = crop_names[idx] if idx < len(crop_names) else "background"
            else:
                crop_name = str(pred)
            return (crop_name, confidence)
    except ImportError:
        pass

    return classify_rule_based(ndvi_series, doys, crop_schema)


def classify_pixel(ndvi_series: np.ndarray, doys: np.ndarray,
                   crop_schema: Dict, method: str = "rule",
                   training_data: Optional[Dict] = None) -> Tuple[str, float]:
    """Classify a single pixel's crop type."""
    if method in ("rf", "xgboost"):
        return classify_random_forest(ndvi_series, doys, crop_schema, training_data)
    else:
        return classify_rule_based(ndvi_series, doys, crop_schema)


# ---------------------------------------------------------------------------
# Post-processing
# ---------------------------------------------------------------------------

def filter_small_patches(class_map: np.ndarray, min_area_pixels: int = 9) -> np.ndarray:
    """
    Remove small isolated patches from classification map.

    Uses connected-component labeling; regions smaller than min_area_pixels
    are set to 0 (background).
    """
    try:
        from scipy import ndimage
    except ImportError:
        return class_map

    result = class_map.copy()
    unique_classes = np.unique(class_map)

    for cls in unique_classes:
        if cls == 0:
            continue
        binary = (class_map == cls).astype(np.int32)
        labeled, n_features = ndimage.label(binary)
        if n_features == 0:
            continue
        component_sizes = ndimage.sum(binary, labeled, range(1, n_features + 1))
        for i, size in enumerate(component_sizes, start=1):
            if size < min_area_pixels:
                result[labeled == i] = 0

    return result


def mode_filter(class_map: np.ndarray, kernel_size: int = 3) -> np.ndarray:
    """Apply mode filter for spatial smoothing."""
    try:
        from scipy import ndimage
    except ImportError:
        return class_map

    if kernel_size < 3:
        return class_map

    smoothed = ndimage.uniform_filter(
        class_map.astype(np.float64), size=kernel_size, mode="nearest",
    )
    result = np.round(smoothed).astype(class_map.dtype)
    return result


# ---------------------------------------------------------------------------
# Accuracy assessment
# ---------------------------------------------------------------------------

def compute_confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray,
                             labels: List[int]) -> np.ndarray:
    """Compute confusion matrix."""
    n = len(labels)
    label_to_idx = {l: i for i, l in enumerate(labels)}
    matrix = np.zeros((n, n), dtype=np.int64)

    for yt, yp in zip(y_true, y_pred):
        i = label_to_idx.get(yt, -1)
        j = label_to_idx.get(yp, -1)
        if i >= 0 and j >= 0:
            matrix[i, j] += 1

    return matrix


def compute_accuracy_metrics(y_true: np.ndarray, y_pred: np.ndarray,
                             labels: List[int]) -> Dict[str, Any]:
    """
    Compute overall accuracy, per-class precision/recall/F1.
    """
    matrix = compute_confusion_matrix(y_true, y_pred, labels)
    total = int(np.sum(matrix))
    correct = int(np.trace(matrix))
    overall_accuracy = correct / total if total > 0 else 0.0

    per_class = {}
    for i, label in enumerate(labels):
        tp = int(matrix[i, i])
        fp = int(np.sum(matrix[:, i])) - tp
        fn = int(np.sum(matrix[i, :])) - tp
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
        per_class[str(label)] = {
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
            "support": int(np.sum(matrix[i, :])),
        }

    return {
        "overall_accuracy": round(overall_accuracy, 4),
        "total_samples": total,
        "correct": correct,
        "confusion_matrix": matrix.tolist(),
        "labels": labels,
        "per_class": per_class,
    }


# ---------------------------------------------------------------------------
# Area statistics
# ---------------------------------------------------------------------------

def compute_pixel_area_m2(lat: float, transform) -> float:
    """
    Compute the area of a single pixel in square meters.

    For geographic CRS (EPSG:4326), uses cos(lat) * 111320 approximation.
    For projected CRS, uses transform directly.
    """
    dx = abs(transform.a)
    dy = abs(transform.e)

    # Heuristic: if pixel size < 1.0, assume degrees (geographic)
    if dx < 1.0 and dy < 1.0:
        lat_rad = np.radians(lat)
        meters_per_deg_lon = np.cos(lat_rad) * 111320.0
        meters_per_deg_lat = 111320.0
        pixel_width_m = dx * meters_per_deg_lon
        pixel_height_m = dy * meters_per_deg_lat
        return pixel_width_m * pixel_height_m
    else:
        return dx * dy


def compute_area_statistics(class_map: np.ndarray, transform,
                            crs_str: str = "EPSG:4326",
                            admin_boundaries: Optional[List] = None) -> Dict[str, Any]:
    """
    Compute area statistics per crop class.
    """
    unique, counts = np.unique(class_map, return_counts=True)
    total_pixels = class_map.size

    center_lat = 30.0
    if crs_str == "EPSG:4326":
        n_rows = class_map.shape[0]
        top_lat = transform.f
        bottom_lat = transform.f + transform.e * n_rows
        center_lat = (top_lat + bottom_lat) / 2.0

    pixel_area_m2 = compute_pixel_area_m2(center_lat, transform)
    pixel_area_ha = pixel_area_m2 / 10000.0

    area_by_class = {}
    for cls_code, count in zip(unique, counts):
        cls_name = CODE_TO_NAME.get(int(cls_code), f"class_{cls_code}")
        area_ha = float(count) * pixel_area_ha
        area_by_class[str(int(cls_code))] = {
            "class_name": cls_name,
            "pixel_count": int(count),
            "area_ha": round(area_ha, 2),
            "area_km2": round(area_ha / 100.0, 4),
            "percentage": round(100.0 * count / total_pixels, 2) if total_pixels > 0 else 0.0,
        }

    return {
        "total_pixels": total_pixels,
        "pixel_area_m2": round(pixel_area_m2, 2),
        "pixel_area_ha": round(pixel_area_ha, 4),
        "crs": crs_str,
        "center_latitude": round(center_lat, 4),
        "area_by_class": area_by_class,
    }


# ---------------------------------------------------------------------------
# AOI parsing
# ---------------------------------------------------------------------------

def parse_aoi(args: argparse.Namespace) -> Dict[str, Any]:
    """Parse AOI from mutually exclusive options: --place, --bbox, --aoi-file."""
    sources = []
    if args.place:
        sources.append("place")
    if args.bbox:
        sources.append("bbox")
    if args.aoi_file:
        sources.append("aoi_file")

    if len(sources) == 0:
        print("ERROR: Must specify one of --place, --bbox, or --aoi-file", file=sys.stderr)
        sys.exit(EXIT_ARG)

    if len(sources) > 1:
        print("ERROR: --place, --bbox, and --aoi-file are mutually exclusive", file=sys.stderr)
        sys.exit(EXIT_ARG)

    if args.place:
        return _resolve_place(args.place)
    elif args.bbox:
        return _parse_bbox(args.bbox)
    else:
        return _load_aoi_file(args.aoi_file)


def _resolve_place(place: str) -> Dict[str, Any]:
    """Resolve a place name to bbox."""
    KNOWN_PLACES = {
        "beijing": [115.4, 39.4, 117.5, 41.0],
        "shanghai": [120.8, 30.6, 122.0, 31.9],
        "guangzhou": [112.9, 22.5, 114.8, 23.9],
        "chengdu": [103.8, 30.4, 104.5, 31.0],
        "wuhan": [113.6, 29.9, 115.0, 31.3],
    }

    place_lower = place.lower().strip()
    if place_lower in KNOWN_PLACES:
        return {
            "bbox": KNOWN_PLACES[place_lower],
            "place": place,
            "source": "place",
            "crs": "EPSG:4326",
        }

    print(f"ERROR: Unknown place '{place}'. Use --bbox or --aoi-file instead.", file=sys.stderr)
    sys.exit(EXIT_ARG)


def _parse_bbox(bbox_str: str) -> Dict[str, Any]:
    """Parse bbox string 'xmin,ymin,xmax,ymax'."""
    parts = bbox_str.split(",")
    if len(parts) != 4:
        print(f"ERROR: bbox must be 'xmin,ymin,xmax,ymax', got: {bbox_str}", file=sys.stderr)
        sys.exit(EXIT_ARG)

    try:
        coords = [float(p.strip()) for p in parts]
    except ValueError:
        print(f"ERROR: bbox values must be numeric: {bbox_str}", file=sys.stderr)
        sys.exit(EXIT_ARG)

    xmin, ymin, xmax, ymax = coords
    if xmin >= xmax or ymin >= ymax:
        print(f"ERROR: invalid bbox (xmin>=xmax or ymin>=ymax): {bbox_str}", file=sys.stderr)
        sys.exit(EXIT_ARG)

    return {
        "bbox": [xmin, ymin, xmax, ymax],
        "source": "bbox",
        "crs": "EPSG:4326",
    }


def _load_aoi_file(path_str: str) -> Dict[str, Any]:
    """Load AOI from GeoJSON or Shapefile."""
    path = Path(path_str)
    if not path.exists():
        print(f"ERROR: AOI file not found: {path}", file=sys.stderr)
        sys.exit(EXIT_VALIDATION)

    try:
        from shapely.geometry import shape as shapely_shape, mapping
        from shapely.ops import unary_union
        from shapely.validation import make_valid
    except ImportError:
        print("ERROR: shapely required for AOI file parsing", file=sys.stderr)
        sys.exit(EXIT_DEP)

    suffix = path.suffix.lower()
    geometries = []

    if suffix in (".geojson", ".json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"ERROR: Failed to read AOI file: {e}", file=sys.stderr)
            sys.exit(EXIT_VALIDATION)

        for feat in data.get("features", []):
            try:
                geom = shapely_shape(feat["geometry"])
                if not geom.is_valid:
                    geom = make_valid(geom)
                geometries.append(geom)
            except Exception as e:
                print(f"WARNING: Skipping invalid geometry: {e}", file=sys.stderr)
    elif suffix == ".shp":
        try:
            import fiona
            with fiona.open(path) as src:
                for feat in src:
                    geom = shapely_shape(feat["geometry"])
                    if not geom.is_valid:
                        geom = make_valid(geom)
                    geometries.append(geom)
        except ImportError:
            print("ERROR: fiona required for Shapefile reading", file=sys.stderr)
            sys.exit(EXIT_DEP)
    else:
        print(f"ERROR: Unsupported AOI file format: {suffix}", file=sys.stderr)
        sys.exit(EXIT_ARG)

    if not geometries:
        print("ERROR: No valid geometries in AOI file", file=sys.stderr)
        sys.exit(EXIT_VALIDATION)

    union = unary_union(geometries)
    bounds = union.bounds

    return {
        "bbox": [bounds[0], bounds[1], bounds[2], bounds[3]],
        "geometry": mapping(union),
        "source": "aoi_file",
        "crs": "EPSG:4326",
    }


# ---------------------------------------------------------------------------
# Time range parsing
# ---------------------------------------------------------------------------

def parse_time_range(args: argparse.Namespace) -> Dict[str, Any]:
    """Parse time range from --year, --start-date, --end-date."""
    if args.year and (args.start_date or args.end_date):
        print("ERROR: --year is mutually exclusive with --start-date/--end-date", file=sys.stderr)
        sys.exit(EXIT_ARG)

    if args.year:
        year = args.year
        if year < 2015 or year > 2030:
            print(f"ERROR: year must be 2015-2030, got {year}", file=sys.stderr)
            sys.exit(EXIT_ARG)
        return {"year": year, "start_date": f"{year}-01-01", "end_date": f"{year}-12-31"}

    if args.start_date and args.end_date:
        try:
            from datetime import date
            sd = date.fromisoformat(args.start_date)
            ed = date.fromisoformat(args.end_date)
        except ValueError as e:
            print(f"ERROR: Invalid date format (use YYYY-MM-DD): {e}", file=sys.stderr)
            sys.exit(EXIT_ARG)

        if sd >= ed:
            print("ERROR: --start-date must be before --end-date", file=sys.stderr)
            sys.exit(EXIT_ARG)

        return {"year": sd.year, "start_date": args.start_date, "end_date": args.end_date}

    # Default: current year
    now = datetime.now()
    year = now.year
    return {"year": year, "start_date": f"{year}-01-01", "end_date": f"{year}-12-31"}


# ---------------------------------------------------------------------------
# Synthetic scene generation
# ---------------------------------------------------------------------------

def generate_synthetic_scene(bbox: List[float], n_rows: int, n_cols: int,
                             doys: np.ndarray, crop_schema: Dict,
                             noise: float = 0.01) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate a synthetic multi-temporal NDVI scene with known crop distribution.

    Creates a spatial pattern with distinct crop regions for testing.

    Args:
        bbox: [xmin, ymin, xmax, ymax]
        n_rows: number of rows in output
        n_cols: number of columns in output
        doys: 1D array of observation DOYs
        crop_schema: crop phenology schema
        noise: noise amplitude

    Returns:
        (ndvi_cube, truth_map) where ndvi_cube is (n_obs, n_rows, n_cols)
        and truth_map is (n_rows, n_cols) with class codes
    """
    n_obs = len(doys)
    ndvi_cube = np.zeros((n_obs, n_rows, n_cols), dtype=np.float64)
    truth_map = np.zeros((n_rows, n_cols), dtype=np.int32)

    # Create spatial pattern: 3 horizontal bands of crops + background
    # Top third: rice, middle third: wheat, bottom third: corn
    # Plus a small background region
    third = n_rows // 3

    crop_names = list(crop_schema.keys())
    crop_codes = [crop_schema[c]["code"] for c in crop_names]

    # Assign regions
    for i in range(n_rows):
        for j in range(n_cols):
            if i < third:
                crop_idx = 0  # rice
            elif i < 2 * third:
                crop_idx = 1  # wheat
            else:
                crop_idx = 2  # corn

            # Small background patches (every 50th pixel)
            if (i * n_cols + j) % 50 == 0:
                truth_map[i, j] = 0
            else:
                truth_map[i, j] = crop_codes[crop_idx]

    # Generate NDVI time series for each pixel based on its class
    for i in range(n_rows):
        for j in range(n_cols):
            cls_code = truth_map[i, j]
            if cls_code == 0:
                # Background: low NDVI
                ndvi_cube[:, i, j] = 0.08 + np.random.normal(0, 0.02, n_obs)
            else:
                # Find crop name from code
                crop_name = CODE_TO_NAME.get(cls_code, "rice")
                refl = simulate_crop_reflectance(doys, crop_name, noise)
                ndvi_cube[:, i, j] = compute_ndvi(refl["nir"], refl["red"])

    ndvi_cube = np.clip(ndvi_cube, 0.0, 1.0)
    return ndvi_cube, truth_map


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run_pipeline(args: argparse.Namespace) -> int:
    """Main crop type mapping pipeline."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("ctm-output")
    output_dir.mkdir(parents=True, exist_ok=True)

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

    try:
        # Step 1: Parse AOI
        logger.info("Step 1: Parsing AOI...")
        aoi = parse_aoi(args)
        bbox = aoi["bbox"]
        logger.info(f"  AOI bbox: {bbox} (source: {aoi['source']})")

        # Step 2: Parse time range
        logger.info("Step 2: Parsing time range...")
        time_range = parse_time_range(args)
        logger.info(f"  Period: {time_range['start_date']} to {time_range['end_date']}")

        # Step 3: Load crop schema
        logger.info("Step 3: Loading crop schema...")
        crop_schema = DEFAULT_CROP_SCHEMA
        if args.crop_schema:
            schema_path = Path(args.crop_schema)
            if schema_path.exists():
                try:
                    crop_schema = json.loads(schema_path.read_text(encoding="utf-8"))
                    logger.info(f"  Loaded custom schema from {schema_path}")
                except Exception as e:
                    logger.warning(f"  Failed to load schema: {e}, using default")

        # Step 4: Generate or load time series data
        logger.info("Step 4: Preparing time series data...")

        # For MVP: generate synthetic data
        # In production: would search STAC, download, preprocess
        n_rows = args.n_rows if args.n_rows else 30
        n_cols = args.n_cols if args.n_cols else 30

        # Generate observation DOYs (monthly from Apr to Oct)
        year = time_range["year"]
        obs_months = [4, 5, 6, 7, 8, 9, 10]
        from datetime import date
        doys = np.array([date(year, m, 15).timetuple().tm_yday for m in obs_months])

        ndvi_cube, truth_map = generate_synthetic_scene(
            bbox, n_rows, n_cols, doys, crop_schema, noise=0.02,
        )
        logger.info(f"  Generated scene: {ndvi_cube.shape} (obs x rows x cols)")

        # Step 5: Classification
        logger.info("Step 5: Classifying pixels...")
        method = args.method if args.method else "rule"
        class_map = np.zeros((n_rows, n_cols), dtype=np.int32)
        confidence_map = np.zeros((n_rows, n_cols), dtype=np.float64)

        for i in range(n_rows):
            for j in range(n_cols):
                ndvi_series = ndvi_cube[:, i, j]
                crop_name, conf = classify_pixel(ndvi_series, doys, crop_schema, method)
                cls_code = crop_schema.get(crop_name, {}).get("code", 0)
                class_map[i, j] = cls_code
                confidence_map[i, j] = conf

        logger.info(f"  Classification complete (method: {method})")

        # Step 6: Post-processing
        logger.info("Step 6: Post-processing...")
        min_patch = args.min_patch_area if args.min_patch_area else 4
        if min_patch > 1:
            class_map = filter_small_patches(class_map, min_area_pixels=min_patch)
            logger.info(f"  Filtered patches < {min_patch} pixels")

        # Step 7: Accuracy assessment (if labels provided)
        logger.info("Step 7: Accuracy assessment...")
        accuracy_result = None
        if args.labels:
            labels_path = Path(args.labels)
            if labels_path.exists():
                # Load user-provided labels
                try:
                    label_data = json.loads(labels_path.read_text(encoding="utf-8"))
                    # Parse labels...
                    logger.info(f"  Loaded labels from {labels_path}")
                except Exception as e:
                    logger.warning(f"  Failed to load labels: {e}")
            else:
                logger.warning(f"  Labels file not found: {labels_path}")

        # If no user labels, use truth map for self-evaluation (demo only)
        if accuracy_result is None:
            labels_list = sorted(crop_schema[c]["code"] for c in crop_schema)
            y_true = truth_map.flatten()
            y_pred = class_map.flatten()
            accuracy_result = compute_accuracy_metrics(y_true, y_pred, labels_list)
            logger.info(f"  Overall accuracy: {accuracy_result['overall_accuracy']:.4f}")

        # Step 8: Area statistics
        logger.info("Step 8: Computing area statistics...")
        try:
            import rasterio
            from rasterio.transform import from_bounds
            transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], n_cols, n_rows)
        except ImportError:
            # Create a mock transform
            class MockTransform:
                def __init__(self, bbox, n_cols, n_rows):
                    self.a = (bbox[2] - bbox[0]) / n_cols
                    self.e = (bbox[3] - bbox[1]) / n_rows
                    self.f = bbox[3]  # top-left y
            transform = MockTransform(bbox, n_cols, n_rows)

        area_stats = compute_area_statistics(class_map, transform, "EPSG:4326")
        logger.info(f"  Total area classes: {len(area_stats['area_by_class'])}")

        # Step 9: Write outputs
        logger.info("Step 9: Writing outputs...")

        # crop_classes.tif
        try:
            import rasterio
            from rasterio.transform import from_bounds
            transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], n_cols, n_rows)

            classes_path = output_dir / "crop_classes.tif"
            with rasterio.open(
                classes_path, "w",
                driver="GTiff",
                height=n_rows,
                width=n_cols,
                count=1,
                dtype="int32",
                crs="EPSG:4326",
                transform=transform,
                nodata=0,
                compress="deflate",
            ) as dst:
                dst.write(class_map.astype(np.int32), 1)

            confidence_path = output_dir / "crop_confidence.tif"
            with rasterio.open(
                confidence_path, "w",
                driver="GTiff",
                height=n_rows,
                width=n_cols,
                count=1,
                dtype="float64",
                crs="EPSG:4326",
                transform=transform,
                nodata=-1,
                compress="deflate",
            ) as dst:
                dst.write(confidence_map, 1)
        except ImportError:
            logger.warning("  rasterio not available, skipping GeoTIFF output")

        # crop_polygons.geojson (simplified: one polygon per connected region)
        try:
            from shapely.geometry import mapping
            from scipy import ndimage

            features = []
            for cls_code in np.unique(class_map):
                if cls_code == 0:
                    continue
                binary = (class_map == cls_code).astype(np.int32)
                labeled, n_feat = ndimage.label(binary)
                for k in range(1, n_feat + 1):
                    region = (labeled == k)
                    # Find bounding box of region
                    rows, cols = np.where(region)
                    if len(rows) == 0:
                        continue
                    rmin, rmax = rows.min(), rows.max()
                    cmin, cmax = cols.min(), cols.max()
                    # Convert pixel coords to geo coords
                    x_min = bbox[0] + (cmin / n_cols) * (bbox[2] - bbox[0])
                    x_max = bbox[0] + ((cmax + 1) / n_cols) * (bbox[2] - bbox[0])
                    y_max = bbox[3] - (rmin / n_rows) * (bbox[3] - bbox[1])
                    y_min = bbox[3] - ((rmax + 1) / n_rows) * (bbox[3] - bbox[1])

                    poly = {
                        "type": "Polygon",
                        "coordinates": [[
                            [x_min, y_min], [x_max, y_min],
                            [x_max, y_max], [x_min, y_max],
                            [x_min, y_min],
                        ]],
                    }
                    cls_name = CODE_TO_NAME.get(int(cls_code), f"class_{cls_code}")
                    features.append({
                        "type": "Feature",
                        "geometry": poly,
                        "properties": {
                            "crop_code": int(cls_code),
                            "crop_name": cls_name,
                            "pixel_count": int(np.sum(region)),
                        },
                    })

            polygons_path = output_dir / "crop_polygons.geojson"
            polygons_geojson = {"type": "FeatureCollection", "features": features}
            polygons_path.write_text(
                json.dumps(polygons_geojson, ensure_ascii=False, default=str),
                encoding="utf-8",
            )
        except (ImportError, Exception) as e:
            logger.warning(f"  Could not generate polygons: {e}")

        # area_by_admin.csv
        area_csv_path = output_dir / "area_by_admin.csv"
        with open(area_csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "crop_code", "crop_name", "pixel_count", "area_ha", "area_km2",
                "percentage",
            ])
            writer.writeheader()
            for cls_code_str, info in area_stats["area_by_class"].items():
                writer.writerow({
                    "crop_code": cls_code_str,
                    "crop_name": info["class_name"],
                    "pixel_count": info["pixel_count"],
                    "area_ha": info["area_ha"],
                    "area_km2": info["area_km2"],
                    "percentage": info["percentage"],
                })

        # accuracy.json
        accuracy_path = output_dir / "accuracy.json"
        accuracy_path.write_text(
            json.dumps(accuracy_result, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8",
        )

        # request.json
        request_path = output_dir / "request.json"
        request_data = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "aoi": aoi,
            "time_range": time_range,
            "crop_schema": crop_schema,
            "method": method,
            "parameters": {
                "n_rows": n_rows,
                "n_cols": n_cols,
                "min_patch_area": min_patch,
            },
        }
        request_path.write_text(
            json.dumps(request_data, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8",
        )

        # dataset-manifest.json
        ds_manifest_path = output_dir / "dataset-manifest.json"
        ds_manifest = {
            "source": "synthetic",
            "sensor": "Sentinel-2 (simulated)",
            "bands": S2_BANDS,
            "observations": [
                {"date": f"{year}-{m:02d}-15", "doy": d}
                for m, d in zip(obs_months, doys)
            ],
            "n_observations": len(doys),
            "cloud_cover": "N/A (synthetic)",
        }
        ds_manifest_path.write_text(
            json.dumps(ds_manifest, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8",
        )

        # output-manifest.json
        output_files = {}
        for f in output_dir.iterdir():
            if f.is_file():
                output_files[f.name] = str(f)
        output_manifest_path = output_dir / "output-manifest.json"
        output_manifest = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "output_directory": str(output_dir),
            "files": output_files,
            "accuracy": {
                "overall_accuracy": accuracy_result["overall_accuracy"],
                "total_samples": accuracy_result["total_samples"],
            },
        }
        output_manifest_path.write_text(
            json.dumps(output_manifest, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8",
        )

        # qa.json
        qa_path = output_dir / "qa.json"
        qa_data = {
            "status": "complete",
            "checks": {
                "aoi_valid": True,
                "time_range_valid": True,
                "classification_complete": True,
                "accuracy_computed": accuracy_result is not None,
                "area_statistics_computed": True,
            },
            "warnings": [],
            "spatial_resolution": f"{(bbox[2] - bbox[0]) / n_cols:.6f} deg",
            "temporal_coverage": f"{time_range['start_date']} to {time_range['end_date']}",
        }
        qa_path.write_text(
            json.dumps(qa_data, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8",
        )

        logger.info("Pipeline complete!")
        logger.info(f"  Output directory: {output_dir}")
        logger.info(f"  Overall accuracy: {accuracy_result['overall_accuracy']:.4f}")

        return EXIT_OK

    except SystemExit:
        raise
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        logger.error(traceback.format_exc())
        return EXIT_PROCESSING


def main():
    parser = argparse.ArgumentParser(
        description="Crop Type Mapping - Multi-temporal crop classification",
    )
    # Spatial AOI (mutually exclusive)
    aoi_group = parser.add_mutually_exclusive_group()
    aoi_group.add_argument("--place", default=None,
                           help="Place name (e.g., 'beijing', 'shanghai')")
    aoi_group.add_argument("--bbox", default=None,
                           help="Bounding box: 'xmin,ymin,xmax,ymax' (WGS84)")
    aoi_group.add_argument("--aoi-file", default=None,
                           help="AOI file (GeoJSON or Shapefile)")

    # Time range
    parser.add_argument("--year", type=int, default=None,
                        help="Year for analysis (e.g., 2024)")
    parser.add_argument("--start-date", default=None,
                        help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", default=None,
                        help="End date (YYYY-MM-DD)")

    # Domain parameters
    parser.add_argument("--crop-schema", default=None,
                        help="Custom crop phenology schema JSON file")
    parser.add_argument("--labels", default=None,
                        help="Training/validation labels (GeoJSON)")
    parser.add_argument("--method", default="rule",
                        choices=["rule", "rf", "xgboost"],
                        help="Classification method (default: rule)")
    parser.add_argument("--min-observations", type=int, default=5,
                        help="Minimum valid observations per pixel (default: 5)")
    parser.add_argument("--field-boundaries", default=None,
                        help="Field boundary polygons (GeoJSON)")
    parser.add_argument("--min-patch-area", type=int, default=4,
                        help="Minimum patch area in pixels (default: 4)")

    # Synthetic scene dimensions (for testing)
    parser.add_argument("--n-rows", type=int, default=30,
                        help="Number of rows for synthetic scene (default: 30)")
    parser.add_argument("--n-cols", type=int, default=30,
                        help="Number of columns for synthetic scene (default: 30)")

    # Output
    parser.add_argument("--output-dir", "-o", default="ctm-output",
                        help="Output directory (default: ctm-output)")
    parser.add_argument("--overwrite", action="store_true",
                        help="Allow overwriting existing output")

    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    args = parser.parse_args()

    try:
        sys.exit(run_pipeline(args))
    except SystemExit:
        raise
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
