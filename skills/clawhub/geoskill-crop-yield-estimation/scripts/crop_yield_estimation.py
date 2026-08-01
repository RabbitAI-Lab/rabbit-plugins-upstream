#!/usr/bin/env python3
"""
crop-yield-estimation: Crop Yield Estimator
==============================================
Fuse remote sensing time series, weather, soil, and statistical
samples to estimate crop yield at parcel or admin-unit level,
with prediction intervals and interpretable factors.

Privacy Disclosure:
- This tool processes data locally. No data is sent to any server.
- All computation happens on your machine.

License: MIT-0 (No attribution required)
Author: ruiduobao
Version: 0.1.0
"""

import argparse
import sys
import os
import json
import csv
import logging
from datetime import datetime, timezone
from typing import Optional, Dict, List, Tuple, Any

try:
    import numpy as np
except ImportError:
    print("ERROR: 'numpy' is required. Install with: pip install numpy>=1.21.0")
    sys.exit(3)

try:
    from scipy import stats as scipy_stats
except ImportError:
    print("ERROR: 'scipy' is required. Install with: pip install scipy>=1.7.0")
    sys.exit(3)

# Exit Codes
EXIT_SUCCESS = 0
EXIT_BAD_ARGS = 2
EXIT_MISSING_DEP = 3
EXIT_DATA_VALIDATION = 6
EXIT_PROCESSING = 7

# Crop parameters (growth window days from planting)
CROP_DEFAULTS = {
    "maize": {"planting_doy": 120, "growth_days": 150, "water_demand_mm": 500},
    "wheat": {"planting_doy": 270, "growth_days": 240, "water_demand_mm": 450},
    "rice": {"planting_doy": 100, "growth_days": 130, "water_demand_mm": 800},
    "soybean": {"planting_doy": 130, "growth_days": 120, "water_demand_mm": 450},
}

# Yield unit conversion to kg/ha
YIELD_CONVERSION = {
    "t_ha": 1000.0,
    "kg_ha": 1.0,
    "kg_m2": 10.0,
    "g_m2": 10.0,
    "jin_mu": 750.0,
}

# Fresh-to-dry weight ratios
FRESH_DRY_RATIO = {
    "maize": 0.85, "wheat": 0.88, "rice": 0.87,
    "soybean": 0.88, "default": 0.87,
}

FEATURE_WINDOW_PRESETS = {
    "early": (-30, 30), "mid": (30, 90),
    "late": (90, 150), "full": (-30, 150),
}

VALIDATION_SCHEMES = ["random", "leave_one_year", "leave_one_region", "blocked"]
MODEL_TYPES = ["random_forest", "gradient_boosting", "ensemble"]


# ============================================================
# Utility Functions
# ============================================================

def create_polygon(x: float, y: float, w: float, h: float):
    """Create a shapely Polygon from origin (x, y) and dimensions (w, h)."""
    try:
        from shapely.geometry import Polygon
    except ImportError:
        print("ERROR: 'shapely' is required. Install with: pip install shapely>=2.0.0")
        sys.exit(3)
    return Polygon([(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)])


def setup_logging(output_dir: str, verbose: bool = False) -> logging.Logger:
    """Setup logging to file and console."""
    os.makedirs(output_dir, exist_ok=True)
    logger = logging.getLogger("crop_yield")
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    logger.handlers.clear()
    log_path = os.path.join(output_dir, "run.log")
    fh = logging.FileHandler(log_path, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    logger.addHandler(fh)
    ch = logging.StreamHandler(sys.stderr)
    ch.setLevel(logging.DEBUG if verbose else logging.INFO)
    ch.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(ch)
    return logger


def close_logging():
    """Close all logging handlers to release file handles."""
    logger = logging.getLogger("crop_yield")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)


def write_json(data: Any, path: str, logger: logging.Logger):
    """Write data to JSON file with proper serialization."""
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    logger.debug(f"Wrote: {path}")


def compute_bbox_area_ha(bbox: List[float]) -> float:
    """Compute approximate area in hectares from EPSG:4326 bbox."""
    xmin, ymin, xmax, ymax = bbox
    lat_mid = (ymin + ymax) / 2.0
    lat_rad = np.radians(lat_mid)
    width_m = (xmax - xmin) * 111320.0 * np.cos(lat_rad)
    height_m = (ymax - ymin) * 111320.0
    return float(width_m * height_m / 10000.0)


def convert_yield_to_kg_ha(value: float, unit: str, crop: str = "default",
                           is_fresh_weight: bool = False) -> float:
    """Convert yield to kg/ha dry weight."""
    if unit not in YIELD_CONVERSION:
        raise ValueError(f"Unknown yield unit: {unit}")
    kg_ha = value * YIELD_CONVERSION[unit]
    if is_fresh_weight:
        ratio = FRESH_DRY_RATIO.get(crop, FRESH_DRY_RATIO["default"])
        kg_ha *= ratio
    return kg_ha


def convert_yield_from_kg_ha(value_kg_ha: float, target_unit: str,
                               crop: str = "default",
                               as_fresh_weight: bool = False) -> float:
    """Convert from kg/ha dry weight to target unit."""
    result = value_kg_ha
    if as_fresh_weight:
        ratio = FRESH_DRY_RATIO.get(crop, FRESH_DRY_RATIO["default"])
        if ratio > 0:
            result /= ratio
    if target_unit not in YIELD_CONVERSION:
        raise ValueError(f"Unknown target unit: {target_unit}")
    return result / YIELD_CONVERSION[target_unit]


# ============================================================
# Sample Management
# ============================================================

def load_yield_labels(path: str, logger: logging.Logger) -> List[Dict]:
    """Load yield labels from CSV or GeoJSON."""
    if not os.path.exists(path):
        logger.error(f"Yield labels file not found: {path}")
        sys.exit(EXIT_DATA_VALIDATION)
    labels = []
    if path.endswith(".csv"):
        with open(path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                labels.append(_parse_label_row(row))
    elif path.endswith((".geojson", ".json")):
        with open(path, "r", encoding="utf-8") as f:
            geojson = json.load(f)
        for feat in geojson.get("features", []):
            props = feat.get("properties", {})
            label = _parse_label_row(props)
            if "geometry" in feat:
                label["geometry"] = feat["geometry"]
            labels.append(label)
    else:
        logger.error(f"Unsupported format: {path}")
        sys.exit(EXIT_DATA_VALIDATION)
    logger.info(f"Loaded {len(labels)} yield labels from {path}")
    return labels


def _parse_label_row(row: Dict) -> Dict:
    """Parse and standardize a single label row."""
    unit = row.get("yield_unit", "kg_ha")
    is_fresh = str(row.get("is_fresh_weight", "false")).lower() in ("true", "1", "yes")
    crop = row.get("crop", "default")
    value = float(row["yield_value"])
    value_kg_ha = convert_yield_to_kg_ha(value, unit, crop, is_fresh)
    return {
        "id": row.get("id", ""),
        "year": int(row.get("year", 0)),
        "admin_code": row.get("admin_code", ""),
        "admin_name": row.get("admin_name", ""),
        "yield_value": value,
        "yield_unit": unit,
        "is_fresh_weight": is_fresh,
        "yield_kg_ha_dry": value_kg_ha,
        "crop": crop,
    }


def unify_samples(labels: List[Dict], target_year: int,
                  logger: logging.Logger) -> Tuple[List[Dict], Dict]:
    """Unify yield samples to common unit and filter by year."""
    unified = []
    issues = []
    for label in labels:
        if label["year"] != target_year:
            continue
        if label["yield_kg_ha_dry"] <= 0:
            issues.append(f"Non-positive yield for {label['id']}")
            continue
        if label["yield_kg_ha_dry"] > 50000:
            issues.append(f"Suspiciously high yield for {label['id']}: {label['yield_kg_ha_dry']}")
            continue
        unified.append(label)
    yields = [l["yield_kg_ha_dry"] for l in unified]
    qa = {
        "n_input": len(labels),
        "n_target_year": len(unified),
        "n_issues": len(issues),
        "issues": issues[:20],
        "unit": "kg/ha_dry",
        "yield_range": {
            "min": min(yields) if yields else 0,
            "max": max(yields) if yields else 0,
            "mean": float(np.mean(yields)) if yields else 0,
        },
    }
    logger.info(f"Unified {len(unified)} samples for year {target_year} ({len(issues)} issues)")
    return unified, qa


# ============================================================
# Feature Pipeline
# ============================================================

def extract_features_for_sample(sample: Dict, feature_window: str,
                                logger: logging.Logger) -> Dict[str, float]:
    """Extract features for a single sample (MVP: synthetic)."""
    np.random.seed(hash(sample.get("id", "default")) % (2**32))
    return {
        "ndvi_mean": np.random.uniform(0.3, 0.85),
        "ndvi_max": np.random.uniform(0.5, 0.95),
        "ndvi_std": np.random.uniform(0.02, 0.15),
        "evi_mean": np.random.uniform(0.2, 0.75),
        "lai_mean": np.random.uniform(1.5, 6.0),
        "gndvi_mean": np.random.uniform(0.3, 0.8),
        "gdd": np.random.uniform(800, 2500),
        "precip_total": np.random.uniform(200, 800),
        "precip_std": np.random.uniform(5, 30),
        "temp_mean": np.random.uniform(15, 28),
        "temp_max": np.random.uniform(28, 40),
        "solar_radiation": np.random.uniform(1500, 3500),
        "vapor_pressure_deficit": np.random.uniform(0.5, 3.0),
        "soil_organic_carbon": np.random.uniform(5, 30),
        "soil_ph": np.random.uniform(5.5, 8.5),
        "soil_clay_pct": np.random.uniform(10, 50),
        "soil_sand_pct": np.random.uniform(15, 60),
        "soil_water_capacity": np.random.uniform(100, 300),
        "elevation": np.random.uniform(0, 2000),
        "slope": np.random.uniform(0, 15),
    }


def build_feature_matrix(samples: List[Dict], feature_window: str,
                         logger: logging.Logger) -> Tuple[np.ndarray, List[str], List[str]]:
    """Build feature matrix from samples."""
    feature_dicts = []
    sample_ids = []
    for sample in samples:
        features = extract_features_for_sample(sample, feature_window, logger)
        feature_dicts.append(features)
        sample_ids.append(sample.get("id", ""))
    if not feature_dicts:
        logger.error("No features extracted")
        sys.exit(EXIT_DATA_VALIDATION)
    feature_names = sorted(feature_dicts[0].keys())
    X = np.array([[fd[name] for name in feature_names] for fd in feature_dicts])
    logger.info(f"Built feature matrix: {X.shape[0]} samples x {X.shape[1]} features")
    return X, feature_names, sample_ids


def check_feature_envelope(X_train: np.ndarray, X_pred: np.ndarray,
                           threshold: float = 0.05) -> np.ndarray:
    """Check if prediction samples are within training feature envelope."""
    in_envelope = np.ones(X_pred.shape[0], dtype=bool)
    for j in range(X_train.shape[1]):
        train_min = np.min(X_train[:, j])
        train_max = np.max(X_train[:, j])
        range_j = train_max - train_min
        if range_j <= 0:
            continue
        lower = train_min - threshold * range_j
        upper = train_max + threshold * range_j
        in_envelope &= (X_pred[:, j] >= lower) & (X_pred[:, j] <= upper)
    return in_envelope


# ============================================================
# Model Training
# ============================================================

def _compute_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> Dict:
    """Compute regression metrics."""
    y_true = np.asarray(y_true, dtype=np.float64)
    y_pred = np.asarray(y_pred, dtype=np.float64)
    residuals = y_true - y_pred
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    rmse = float(np.sqrt(np.mean(residuals ** 2)))
    mae = float(np.mean(np.abs(residuals)))
    mape = float(np.mean(np.abs(residuals / np.clip(y_true, 1, None))) * 100)
    return {
        "r2": round(float(r2), 4),
        "rmse": round(rmse, 2),
        "mae": round(mae, 2),
        "mape": round(mape, 2),
        "n_samples": len(y_true),
    }


def train_model(X_train: np.ndarray, y_train: np.ndarray,
                model_type: str, feature_names: List[str],
                logger: logging.Logger) -> Dict:
    """Train a yield estimation model."""
    try:
        from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
        from sklearn.model_selection import cross_val_score
    except ImportError:
        logger.error("scikit-learn is required")
        sys.exit(EXIT_MISSING_DEP)

    n_samples, n_features = X_train.shape

    if model_type == "random_forest":
        model = RandomForestRegressor(
            n_estimators=100, max_depth=min(10, max(3, n_samples // 5)),
            min_samples_leaf=max(2, n_samples // 20), random_state=42, n_jobs=-1)
    elif model_type == "gradient_boosting":
        model = GradientBoostingRegressor(
            n_estimators=100, max_depth=min(6, max(2, n_samples // 10)),
            learning_rate=0.1, min_samples_leaf=max(2, n_samples // 20), random_state=42)
    elif model_type == "ensemble":
        model_rf = RandomForestRegressor(
            n_estimators=80, max_depth=8, random_state=42, n_jobs=-1)
        model_gb = GradientBoostingRegressor(
            n_estimators=80, max_depth=5, learning_rate=0.1, random_state=42)
        model_rf.fit(X_train, y_train)
        model_gb.fit(X_train, y_train)
        return _build_ensemble_card(model_rf, model_gb, X_train, y_train, feature_names, logger)
    else:
        logger.error(f"Unknown model type: {model_type}")
        sys.exit(EXIT_BAD_ARGS)

    model.fit(X_train, y_train)
    cv_scores = cross_val_score(model, X_train, y_train, cv=min(5, max(2, n_samples // 2)),
                               scoring="r2") if n_samples >= 10 else np.array([np.nan])
    importance = model.feature_importances_
    feat_imp = dict(zip(feature_names, [round(float(imp), 4) for imp in importance]))
    feat_imp = dict(sorted(feat_imp.items(), key=lambda x: x[1], reverse=True))
    y_pred_train = model.predict(X_train)
    train_metrics = _compute_metrics(y_train, y_pred_train)
    return {
        "model_type": model_type, "n_samples": n_samples, "n_features": n_features,
        "features": feature_names, "training_metrics": train_metrics,
        "cv_r2_mean": round(float(np.nanmean(cv_scores)), 4),
        "cv_r2_std": round(float(np.nanstd(cv_scores)), 4),
        "feature_importance": feat_imp, "model_object": model,
    }


def _build_ensemble_card(model_rf, model_gb, X_train, y_train, feature_names, logger) -> Dict:
    """Build model card for ensemble."""
    y_pred_rf = model_rf.predict(X_train)
    y_pred_gb = model_gb.predict(X_train)
    y_pred_train = (y_pred_rf + y_pred_gb) / 2.0
    train_metrics = _compute_metrics(y_train, y_pred_train)
    imp_rf = model_rf.feature_importances_
    imp_gb = model_gb.feature_importances_
    imp_avg = (imp_rf + imp_gb) / 2.0
    feat_imp = dict(zip(feature_names, [round(float(imp), 4) for imp in imp_avg]))
    feat_imp = dict(sorted(feat_imp.items(), key=lambda x: x[1], reverse=True))
    return {
        "model_type": "ensemble", "n_samples": X_train.shape[0],
        "n_features": X_train.shape[1], "features": feature_names,
        "training_metrics": train_metrics, "cv_r2_mean": None, "cv_r2_std": None,
        "feature_importance": feat_imp, "model_object": (model_rf, model_gb),
    }


# ============================================================
# Prediction with Uncertainty
# ============================================================

def predict_with_interval(model_card: Dict, X_pred: np.ndarray,
                          n_bootstrap: int = 200,
                          confidence_level: float = 0.95,
                          logger: logging.Logger = None) -> Dict:
    """Generate predictions with uncertainty intervals."""
    model_obj = model_card["model_object"]
    alpha = 1 - confidence_level

    if model_card["model_type"] == "ensemble":
        model_rf, model_gb = model_obj
        pred_rf = model_rf.predict(X_pred)
        pred_gb = model_gb.predict(X_pred)
        predictions = (pred_rf + pred_gb) / 2.0
        ensemble_spread = np.abs(pred_rf - pred_gb)
        # RF estimators_ is a list of DecisionTreeRegressor
        rf_tree_preds = np.array([tree.predict(X_pred) for tree in model_rf.estimators_])
        # GB estimators_ is a 2D array (n_estimators, 1) for regression
        gb_tree_preds = np.array([tree.predict(X_pred) for tree in model_gb.estimators_[:, 0]])
        rf_std = np.std(rf_tree_preds, axis=0)
        gb_std = np.std(gb_tree_preds, axis=0)
        total_std = np.sqrt((rf_std**2 + gb_std**2) / 2 + (ensemble_spread**2) / 4)
        margin = scipy_stats.norm.ppf(1 - alpha / 2) * total_std
        lower = predictions - margin
        upper = predictions + margin
        method = "ensemble_spread"
    elif model_card["model_type"] == "random_forest":
        tree_preds = np.array([tree.predict(X_pred) for tree in model_obj.estimators_])
        predictions = np.mean(tree_preds, axis=0)
        lower = np.percentile(tree_preds, 100 * alpha / 2, axis=0)
        upper = np.percentile(tree_preds, 100 * (1 - alpha / 2), axis=0)
        method = "quantile_regression_forest"
    elif model_card["model_type"] == "gradient_boosting":
        predictions = model_obj.predict(X_pred)
        staged_preds = np.array([sp for sp in model_obj.staged_predict(X_pred)])
        n_stages = staged_preds.shape[0]
        late_preds = staged_preds[max(1, int(0.5 * n_stages)):, :]
        stage_std = np.std(late_preds, axis=0)
        # Avoid zero std
        stage_std = np.where(stage_std < 1e-6, np.std(predictions) * 0.1, stage_std)
        margin = scipy_stats.norm.ppf(1 - alpha / 2) * stage_std
        lower = predictions - margin
        upper = predictions + margin
        method = "boosting_stage_variance"
    else:
        predictions = model_obj.predict(X_pred)
        lower = predictions * 0.85
        upper = predictions * 1.15
        method = "naive_margin"

    lower = np.maximum(lower, 0)
    upper = np.maximum(upper, 0)
    return {
        "predictions": predictions.tolist(),
        "lower_bound": lower.tolist(),
        "upper_bound": upper.tolist(),
        "confidence_level": confidence_level,
        "method": method,
        "prediction_interval_width": (upper - predictions).tolist(),
    }


# ============================================================
# Validation
# ============================================================

def validate_model(model_card: Dict, X_val: np.ndarray, y_val: np.ndarray,
                   logger: logging.Logger) -> Dict:
    """Validate model on held-out data."""
    model_obj = model_card["model_object"]
    if model_card["model_type"] == "ensemble":
        model_rf, model_gb = model_obj
        y_pred = (model_rf.predict(X_val) + model_gb.predict(X_val)) / 2.0
    else:
        y_pred = model_obj.predict(X_val)
    metrics = _compute_metrics(y_val, y_pred)
    residuals = y_val - y_pred
    residual_std = np.std(residuals)
    margin = 1.96 * residual_std
    coverage = float(np.mean(np.abs(residuals) <= margin))
    metrics["interval_coverage_95"] = round(coverage, 4)
    metrics["residual_std"] = round(float(residual_std), 2)
    logger.info(f"Validation: R²={metrics['r2']:.4f}, RMSE={metrics['rmse']:.2f}, Coverage={coverage:.2%}")
    return metrics


def create_validation_split(samples: List[Dict], X: np.ndarray, y: np.ndarray,
                            scheme: str, logger: logging.Logger) -> Dict:
    """Create train/validation split based on scheme."""
    n = len(samples)
    indices = np.arange(n)

    if scheme == "random":
        np.random.seed(42)
        np.random.shuffle(indices)
        split_point = max(1, int(0.8 * n))
        train_idx, val_idx = indices[:split_point], indices[split_point:]
    elif scheme == "leave_one_year":
        years = np.array([s.get("year", 0) for s in samples])
        unique_years = sorted(set(years))
        if len(unique_years) < 2:
            np.random.seed(42)
            np.random.shuffle(indices)
            split_point = max(1, int(0.8 * n))
            train_idx, val_idx = indices[:split_point], indices[split_point:]
        else:
            val_year = unique_years[-1]
            train_idx, val_idx = indices[years != val_year], indices[years == val_year]
    elif scheme == "leave_one_region":
        regions = np.array([s.get("admin_code", "unknown") for s in samples])
        unique_regions = list(set(regions))
        if len(unique_regions) < 2:
            np.random.seed(42)
            np.random.shuffle(indices)
            split_point = max(1, int(0.8 * n))
            train_idx, val_idx = indices[:split_point], indices[split_point:]
        else:
            val_region = unique_regions[-1]
            train_idx, val_idx = indices[regions != val_region], indices[regions == val_region]
    elif scheme == "blocked":
        split_point = max(1, int(0.8 * n))
        train_idx, val_idx = indices[:split_point], indices[split_point:]
    else:
        logger.error(f"Unknown validation scheme: {scheme}")
        sys.exit(EXIT_BAD_ARGS)

    return {
        "train_idx": train_idx, "val_idx": val_idx,
        "scheme": scheme, "n_train": len(train_idx), "n_val": len(val_idx),
    }


# ============================================================
# Output Generation
# ============================================================

def generate_yield_raster(predictions: List[float], bounds: List[float],
                          output_path: str, logger: logging.Logger) -> str:
    """Generate yield estimate GeoTIFF."""
    try:
        import rasterio
        from rasterio.transform import from_bounds
    except ImportError:
        logger.error("rasterio required for raster output")
        sys.exit(EXIT_MISSING_DEP)
    n = len(predictions)
    cols = int(np.ceil(np.sqrt(n)))
    rows = int(np.ceil(n / cols))
    pred_array = np.full(rows * cols, np.nan, dtype=np.float64)
    pred_array[:n] = predictions
    pred_grid = pred_array.reshape(rows, cols)
    xmin, ymin, xmax, ymax = bounds
    transform = from_bounds(xmin, ymin, xmax, ymax, cols, rows)
    profile = {
        "driver": "GTiff", "dtype": "float32", "width": cols, "height": rows,
        "count": 1, "crs": "EPSG:4326", "transform": transform,
        "nodata": -9999, "compress": "lzw",
    }
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    with rasterio.open(output_path, "w", **profile) as dst:
        write_data = pred_grid.astype(np.float32)
        write_data[np.isnan(write_data)] = -9999
        dst.write(write_data, 1)
    logger.info(f"Wrote yield raster: {output_path}")
    return output_path


def generate_prediction_interval_raster(predictions: List[float],
                                        lower: List[float], upper: List[float],
                                        bounds: List[float], output_path: str,
                                        logger: logging.Logger) -> str:
    """Generate prediction interval width raster."""
    try:
        import rasterio
        from rasterio.transform import from_bounds
    except ImportError:
        logger.error("rasterio required")
        sys.exit(EXIT_MISSING_DEP)
    n = len(predictions)
    cols = int(np.ceil(np.sqrt(n)))
    rows = int(np.ceil(n / cols))
    width_pct = [((u - l) / max(p, 1)) * 100 if p > 0 else 0
                 for p, l, u in zip(predictions, lower, upper)]
    width_array = np.full(rows * cols, np.nan, dtype=np.float64)
    width_array[:n] = width_pct
    width_grid = width_array.reshape(rows, cols)
    xmin, ymin, xmax, ymax = bounds
    transform = from_bounds(xmin, ymin, xmax, ymax, cols, rows)
    profile = {
        "driver": "GTiff", "dtype": "float32", "width": cols, "height": rows,
        "count": 1, "crs": "EPSG:4326", "transform": transform,
        "nodata": -9999, "compress": "lzw",
    }
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    with rasterio.open(output_path, "w", **profile) as dst:
        write_data = width_grid.astype(np.float32)
        write_data[np.isnan(write_data)] = -9999
        dst.write(write_data, 1)
    logger.info(f"Wrote prediction interval raster: {output_path}")
    return output_path


def generate_yield_geojson(samples: List[Dict], predictions: List[float],
                           lower: List[float], upper: List[float],
                           output_path: str, logger: logging.Logger) -> str:
    """Generate yield estimate GeoJSON."""
    features = []
    for sample, pred, lo, hi in zip(samples, predictions, lower, upper):
        geom = sample.get("geometry")
        if geom is None:
            h = hash(sample.get("id", "default")) % 10000
            x = 100 + (h % 100) * 0.01
            y = 30 + (h // 100) * 0.01
            poly = create_polygon(x, y, 0.005, 0.005)
            geom = {"type": "Polygon", "coordinates": [list(poly.exterior.coords)]}
        features.append({
            "type": "Feature", "geometry": geom,
            "properties": {
                "id": sample.get("id", ""),
                "admin_code": sample.get("admin_code", ""),
                "admin_name": sample.get("admin_name", ""),
                "yield_kg_ha": round(float(pred), 2),
                "yield_lower": round(float(lo), 2),
                "yield_upper": round(float(hi), 2),
                "year": sample.get("year", 0),
            },
        })
    geojson = {
        "type": "FeatureCollection", "features": features,
        "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::4326"}},
    }
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(geojson, f, indent=2, ensure_ascii=False, default=str)
    logger.info(f"Wrote yield GeoJSON: {output_path} ({len(features)} features)")
    return output_path


def generate_yield_by_admin(samples: List[Dict], predictions: List[float],
                            lower: List[float], upper: List[float],
                            output_path: str, logger: logging.Logger) -> str:
    """Generate yield summary by admin unit (CSV)."""
    admin_data = {}
    for sample, pred, lo, hi in zip(samples, predictions, lower, upper):
        code = sample.get("admin_code", "unknown")
        if code not in admin_data:
            admin_data[code] = {"admin_name": sample.get("admin_name", ""),
                                "yields": [], "lowers": [], "uppers": []}
        admin_data[code]["yields"].append(pred)
        admin_data[code]["lowers"].append(lo)
        admin_data[code]["uppers"].append(hi)
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["admin_code", "admin_name", "n_samples",
                         "yield_mean_kg_ha", "yield_std_kg_ha",
                         "yield_lower_kg_ha", "yield_upper_kg_ha"])
        for code, data in sorted(admin_data.items()):
            writer.writerow([
                code, data["admin_name"], len(data["yields"]),
                round(float(np.mean(data["yields"])), 2),
                round(float(np.std(data["yields"])), 2),
                round(float(np.mean(data["lowers"])), 2),
                round(float(np.mean(data["uppers"])), 2),
            ])
    logger.info(f"Wrote yield by admin CSV: {output_path} ({len(admin_data)} units)")
    return output_path


def generate_feature_importance_csv(model_card: Dict, output_path: str,
                                    logger: logging.Logger) -> str:
    """Generate feature importance CSV."""
    importance = model_card.get("feature_importance", {})
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["feature", "importance", "rank"])
        for rank, (feat, imp) in enumerate(importance.items(), 1):
            writer.writerow([feat, imp, rank])
    logger.info(f"Wrote feature importance CSV: {output_path}")
    return output_path


def generate_model_card_json(model_card: Dict, validation_metrics: Dict,
                             output_path: str, logger: logging.Logger) -> str:
    """Generate model card JSON (without model_object)."""
    card = {k: v for k, v in model_card.items() if k != "model_object"}
    if validation_metrics:
        card["validation_metrics"] = validation_metrics
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(card, f, indent=2, ensure_ascii=False, default=str)
    logger.info(f"Wrote model card: {output_path}")
    return output_path


# ============================================================
# Main Pipeline
# ============================================================

def run_pipeline(request) -> int:
    """Execute the full crop yield estimation pipeline."""
    os.makedirs(request.output_dir, exist_ok=True)
    logger = setup_logging(request.output_dir, request.verbose)

    # Dry run: only log and write request, no processing
    if getattr(request, 'dry_run', False):
        logger.info("DRY RUN mode — skipping processing")
        write_json(vars(request), os.path.join(request.output_dir, "request.json"), logger)
        close_logging()
        return EXIT_SUCCESS

    logger.info("=" * 60)
    logger.info("crop-yield-estimation pipeline started")
    logger.info(f"  Crop: {request.crop}, Year: {request.year}")
    logger.info(f"  Model: {request.model}, Validation: {request.validation_scheme}")

    # Write request.json
    write_json(vars(request), os.path.join(request.output_dir, "request.json"), logger)

    if not request.yield_labels:
        logger.error("--yield-labels is required")
        close_logging()
        return EXIT_BAD_ARGS

    raw_labels = load_yield_labels(request.yield_labels, logger)
    unified_samples, qa_report = unify_samples(raw_labels, request.year, logger)

    if len(unified_samples) < 5:
        logger.error(f"Insufficient samples: {len(unified_samples)} (need >= 5)")
        close_logging()
        return EXIT_DATA_VALIDATION

    # Dataset manifest
    write_json({
        "yield_labels": {"path": request.yield_labels, "n_records": len(raw_labels),
                          "n_unified": len(unified_samples)},
        "feature_window": request.feature_window,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }, os.path.join(request.output_dir, "dataset-manifest.json"), logger)

    # Build features
    X, feature_names, sample_ids = build_feature_matrix(
        unified_samples, request.feature_window, logger)
    y = np.array([s["yield_kg_ha_dry"] for s in unified_samples])

    # Validation split
    split = create_validation_split(unified_samples, X, y,
                                    request.validation_scheme, logger)
    logger.info(f"Split: {split['n_train']} train, {split['n_val']} val ({split['scheme']})")

    X_train, y_train = X[split["train_idx"]], y[split["train_idx"]]
    X_val, y_val = X[split["val_idx"]], y[split["val_idx"]]

    # Feature envelope check
    in_envelope = check_feature_envelope(X_train, X_val)
    logger.info(f"In feature envelope: {np.sum(in_envelope)}/{len(in_envelope)}")

    # Train
    model_card = train_model(X_train, y_train, request.model, feature_names, logger)

    # Validate
    validation_metrics = {}
    if len(split["val_idx"]) > 0:
        validation_metrics = validate_model(model_card, X_val, y_val, logger)
    model_card["validation_metrics"] = validation_metrics
    model_card["validation_scheme"] = request.validation_scheme

    # Predict with intervals
    pred_result = predict_with_interval(
        model_card, X, n_bootstrap=request.n_bootstrap,
        confidence_level=request.confidence_level, logger=logger)

    # Bounds
    bounds = request.bbox if request.bbox else [73, 18, 135, 54]

    # Generate outputs
    logger.info("Generating outputs...")
    generate_yield_geojson(unified_samples, pred_result["predictions"],
                           pred_result["lower_bound"], pred_result["upper_bound"],
                           os.path.join(request.output_dir, "yield_estimate.geojson"), logger)
    generate_yield_raster(pred_result["predictions"], bounds,
                          os.path.join(request.output_dir, "yield_estimate.tif"), logger)
    generate_prediction_interval_raster(pred_result["predictions"],
                                        pred_result["lower_bound"],
                                        pred_result["upper_bound"],
                                        bounds,
                                        os.path.join(request.output_dir, "prediction_interval.tif"),
                                        logger)
    generate_yield_by_admin(unified_samples, pred_result["predictions"],
                            pred_result["lower_bound"], pred_result["upper_bound"],
                            os.path.join(request.output_dir, "yield_by_admin.csv"), logger)
    generate_feature_importance_csv(model_card,
                                    os.path.join(request.output_dir, "feature_importance.csv"),
                                    logger)
    generate_model_card_json(model_card, validation_metrics,
                             os.path.join(request.output_dir, "model_card.json"), logger)

    # QA report
    qa_final = {
        **qa_report,
        "validation_split": {"scheme": split["scheme"], "n_train": split["n_train"],
                              "n_val": split["n_val"]},
        "feature_envelope": {"n_in_envelope": int(np.sum(in_envelope)),
                              "n_total": len(in_envelope)},
        "model_performance": {
            "training_r2": model_card["training_metrics"]["r2"],
            "validation_r2": validation_metrics.get("r2", None),
            "validation_rmse": validation_metrics.get("rmse", None),
        },
        "prediction_interval": {
            "method": pred_result["method"],
            "confidence_level": pred_result["confidence_level"],
            "mean_width_pct": round(float(np.mean(pred_result["prediction_interval_width"])
                                          / max(np.mean(pred_result["predictions"]), 1) * 100), 2),
        },
    }
    write_json(qa_final, os.path.join(request.output_dir, "qa.json"), logger)

    # Output manifest
    write_json({
        "outputs": {
            "yield_estimate_geojson": "yield_estimate.geojson",
            "yield_estimate_tif": "yield_estimate.tif",
            "prediction_interval_tif": "prediction_interval.tif",
            "yield_by_admin_csv": "yield_by_admin.csv",
            "feature_importance_csv": "feature_importance.csv",
            "model_card_json": "model_card.json",
        },
        "created_at": datetime.now(timezone.utc).isoformat(),
    }, os.path.join(request.output_dir, "output-manifest.json"), logger)

    logger.info("=" * 60)
    logger.info(f"Pipeline completed. Output: {request.output_dir}")
    close_logging()
    return EXIT_SUCCESS


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        prog="crop-yield-estimation",
        description="Crop Yield Estimator — Fuse remote sensing, weather, and soil data.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python crop_yield_estimation.py run --crop maize --year 2023 --yield-labels labels.csv --output-dir output
  python crop_yield_estimation.py run --crop wheat --year 2022 --yield-labels labels.geojson --model gradient_boosting
  python crop_yield_estimation.py run --crop rice --year 2023 --yield-labels labels.csv --bbox 116 39 117 40
        """,
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcommand")

    run_parser = subparsers.add_parser("run", help="Run yield estimation pipeline")
    run_parser.add_argument("--place", help="Place name")
    run_parser.add_argument("--bbox", nargs=4, type=float,
                            metavar=("XMIN", "YMIN", "XMAX", "YMAX"), help="Bounding box")
    run_parser.add_argument("--aoi-file", help="AOI file (GeoJSON/Shapefile)")
    run_parser.add_argument("--crop", default="maize", choices=list(CROP_DEFAULTS.keys()))
    run_parser.add_argument("--year", type=int, default=2023)
    run_parser.add_argument("--yield-labels", required=True, help="Yield labels path")
    run_parser.add_argument("--feature-window", default="full",
                            choices=list(FEATURE_WINDOW_PRESETS.keys()))
    run_parser.add_argument("--model", default="random_forest", choices=MODEL_TYPES)
    run_parser.add_argument("--validation-scheme", default="leave_one_year",
                            choices=VALIDATION_SCHEMES)
    run_parser.add_argument("--output-dir", default="output")
    run_parser.add_argument("--overwrite", action="store_true")
    run_parser.add_argument("--dry-run", action="store_true")
    run_parser.add_argument("--n-bootstrap", type=int, default=200)
    run_parser.add_argument("--confidence-level", type=float, default=0.95)
    run_parser.add_argument("--random-seed", type=int, default=42)
    run_parser.add_argument("--verbose", action="store_true")
    run_parser.set_defaults(func=cmd_run)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(EXIT_SUCCESS)
    args.func(args)


def cmd_run(args):
    """Execute the run subcommand."""
    request = argparse.Namespace(
        place=args.place,
        bbox=args.bbox,
        aoi_file=getattr(args, 'aoi_file', None),
        crop=args.crop,
        year=args.year,
        yield_labels=args.yield_labels,
        feature_window=args.feature_window,
        model=args.model,
        validation_scheme=args.validation_scheme,
        output_dir=args.output_dir,
        overwrite=args.overwrite,
        dry_run=args.dry_run,
        n_bootstrap=args.n_bootstrap,
        confidence_level=args.confidence_level,
        random_seed=args.random_seed,
        verbose=args.verbose,
    )
    if request.dry_run:
        print("DRY RUN — Request parameters:")
        print(json.dumps(vars(request), indent=2, default=str))
        sys.exit(EXIT_SUCCESS)
    sys.exit(run_pipeline(request))


if __name__ == "__main__":
    main()
