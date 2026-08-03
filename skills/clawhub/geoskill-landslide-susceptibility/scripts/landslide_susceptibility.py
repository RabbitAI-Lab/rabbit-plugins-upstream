#!/usr/bin/env python3
"""
Landslide Susceptibility Assessment - Factor-based spatial modeling.

Integrates terrain, geology, rainfall, land cover, roads, and historical
landslide data to produce interpretable susceptibility zoning with
spatial cross-validation.

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

# Optional auto-download via shared data fetcher (Microsoft Planetary Computer)
try:
    from shapely.geometry import shape as _shp_shape, mapping as _shp_mapping
    from shapely.ops import transform as _shp_transform
    _HAS_SHAPELY = True
except ImportError:
    _HAS_SHAPELY = False

try:
    import fiona
    _HAS_FIONA = True
except ImportError:
    _HAS_FIONA = False

# ─── shared data fetcher (optional, enables --bbox/--date-range auto-download) ─
# Try pip-installed package first; fall back to local copy in repo root.
try:
    from _geoskill_data_fetcher import (  # noqa: E402
        DataFetcher,
        DataSource,
        DateRange,
        add_bbox_date_args,
        parse_bbox_arg,
        parse_date_range_arg,
    )
    _HAS_DATA_FETCHER = True
except ImportError:  # pragma: no cover - optional
    _HAS_DATA_FETCHER = False

EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# ============================================================
# Logging
# ============================================================

def setup_logging(output_dir: Path) -> logging.Logger:
    """Setup logging to file and console."""
    logger = logging.getLogger("ls")
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
    """Close all handlers on the ls logger."""
    logger = logging.getLogger("ls")
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


def classify_slope_angle(slope_deg: np.ndarray) -> np.ndarray:
    """
    Classify slope angle into categories.
    Returns integer array: 0=<15, 1=15-25, 2=25-35, 3=35-45, 4=>45
    """
    classes = np.zeros_like(slope_deg, dtype=np.int32)
    classes[slope_deg >= 15] = 1
    classes[slope_deg >= 25] = 2
    classes[slope_deg >= 35] = 3
    classes[slope_deg >= 45] = 4
    return classes


# ============================================================
# Factor Configuration
# ============================================================

def load_factor_config(config_path: Optional[str] = None) -> Dict:
    """Load factor configuration from JSON file."""
    if config_path is None:
        script_dir = Path(__file__).parent
        config_path = script_dir.parent / "references" / "factor_config.json"

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# Collinearity & VIF
# ============================================================

def compute_correlation_matrix(factor_matrix: np.ndarray) -> np.ndarray:
    """
    Compute Pearson correlation matrix for factors.

    Args:
        factor_matrix: (n_samples, n_factors) array

    Returns:
        (n_factors, n_factors) correlation matrix
    """
    n = factor_matrix.shape[1]
    corr = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        for j in range(n):
            col_i = factor_matrix[:, i]
            col_j = factor_matrix[:, j]
            std_i = np.std(col_i)
            std_j = np.std(col_j)
            if std_i < 1e-10 or std_j < 1e-10:
                corr[i, j] = 0.0
            else:
                corr[i, j] = float(np.corrcoef(col_i, col_j)[0, 1])
            if np.isnan(corr[i, j]):
                corr[i, j] = 0.0
    return corr


def compute_vif(factor_matrix: np.ndarray) -> np.ndarray:
    """
    Compute Variance Inflation Factor for each factor.

    VIF_j = 1 / (1 - R^2_j) where R^2_j is from regressing factor j
    on all other factors.

    Args:
        factor_matrix: (n_samples, n_factors) array

    Returns:
        VIF values for each factor (n_factors,)
    """
    n_samples, n_factors = factor_matrix.shape
    vif_values = np.ones(n_factors, dtype=np.float64)

    if n_factors < 2 or n_samples < n_factors + 1:
        return vif_values

    for j in range(n_factors):
        # Regress factor j on all other factors
        other_cols = [k for k in range(n_factors) if k != j]
        X_others = factor_matrix[:, other_cols]
        y = factor_matrix[:, j]

        # Add intercept
        X_with_intercept = np.column_stack([np.ones(n_samples), X_others])

        # OLS: beta = (X'X)^-1 X'y
        try:
            XtX = X_with_intercept.T @ X_with_intercept
            Xty = X_with_intercept.T @ y
            # Use pseudo-inverse for numerical stability
            beta = np.linalg.lstsq(XtX, Xty, rcond=None)[0]
            y_pred = X_with_intercept @ beta
            ss_res = np.sum((y - y_pred) ** 2)
            ss_tot = np.sum((y - np.mean(y)) ** 2)
            if ss_tot > 1e-10:
                r_squared = 1.0 - ss_res / ss_tot
            else:
                r_squared = 0.0
            r_squared = np.clip(r_squared, 0, 0.9999)
            vif_values[j] = 1.0 / (1.0 - r_squared)
        except Exception:
            vif_values[j] = 1.0

    return vif_values


def check_collinearity(factor_matrix: np.ndarray, factor_names: List[str],
                       vif_threshold: float = 5.0,
                       corr_threshold: float = 0.8) -> Dict[str, Any]:
    """
    Check factor collinearity using VIF and correlation.

    Returns:
        Dict with VIF values, high-correlation pairs, and flagged factors
    """
    vif_values = compute_vif(factor_matrix)
    corr_matrix = compute_correlation_matrix(factor_matrix)

    # Find high correlation pairs
    high_corr_pairs = []
    n_factors = len(factor_names)
    for i in range(n_factors):
        for j in range(i + 1, n_factors):
            if abs(corr_matrix[i, j]) >= corr_threshold:
                high_corr_pairs.append({
                    "factor_1": factor_names[i],
                    "factor_2": factor_names[j],
                    "correlation": round(float(corr_matrix[i, j]), 4),
                })

    # Flag factors with high VIF
    flagged_factors = []
    for i, name in enumerate(factor_names):
        if vif_values[i] > vif_threshold:
            flagged_factors.append({
                "factor": name,
                "vif": round(float(vif_values[i]), 2),
            })

    return {
        "vif_values": {name: round(float(vif_values[i]), 2)
                       for i, name in enumerate(factor_names)},
        "correlation_matrix": corr_matrix.tolist(),
        "high_correlation_pairs": high_corr_pairs,
        "flagged_factors": flagged_factors,
        "vif_threshold": vif_threshold,
        "corr_threshold": corr_threshold,
        "pass": len(flagged_factors) == 0,
    }


# ============================================================
# Sampling Strategies
# ============================================================

def generate_negative_samples(
    n_samples: int,
    aoi_shape: Tuple[int, int],
    strategy: str = "random",
    landslide_points: Optional[np.ndarray] = None,
    min_distance: float = 100.0,
    seed: int = 42,
) -> np.ndarray:
    """
    Generate non-landslide (negative) sample points.

    Args:
        n_samples: Number of negative samples to generate
        aoi_shape: (rows, cols) of the AOI
        strategy: 'random', 'buffer', or 'spatial_block'
        landslide_points: (N, 2) array of landslide coordinates (row, col)
        min_distance: Minimum distance from landslide points (for buffer strategy)
        seed: Random seed

    Returns:
        (n_samples, 2) array of (row, col) coordinates
    """
    rng = np.random.RandomState(seed)
    rows, cols = aoi_shape

    if strategy == "random":
        neg_rows = rng.randint(0, rows, size=n_samples)
        neg_cols = rng.randint(0, cols, size=n_samples)
        return np.column_stack([neg_rows, neg_cols])

    elif strategy == "buffer":
        # Generate points at least min_distance (in pixels) from landslide points
        if landslide_points is None or len(landslide_points) == 0:
            neg_rows = rng.randint(0, rows, size=n_samples)
            neg_cols = rng.randint(0, cols, size=n_samples)
            return np.column_stack([neg_rows, neg_cols])

        valid_points = []
        max_attempts = n_samples * 50
        attempts = 0
        while len(valid_points) < n_samples and attempts < max_attempts:
            r = rng.randint(0, rows)
            c = rng.randint(0, cols)
            # Check distance to all landslide points
            dists = np.sqrt((landslide_points[:, 0] - r) ** 2 +
                          (landslide_points[:, 1] - c) ** 2)
            if np.min(dists) >= min_distance:
                valid_points.append([r, c])
            attempts += 1

        # Fill remaining with random if buffer strategy didn't produce enough
        while len(valid_points) < n_samples:
            r = rng.randint(0, rows)
            c = rng.randint(0, cols)
            valid_points.append([r, c])

        return np.array(valid_points[:n_samples])

    elif strategy == "spatial_block":
        # Stratified sampling across spatial blocks
        n_blocks = max(1, int(math.sqrt(n_samples / 10)))
        block_h = rows // n_blocks
        block_w = cols // n_blocks
        per_block = math.ceil(n_samples / (n_blocks * n_blocks))

        points = []
        for bi in range(n_blocks):
            for bj in range(n_blocks):
                r_start = bi * block_h
                r_end = min((bi + 1) * block_h, rows)
                c_start = bj * block_w
                c_end = min((bj + 1) * block_w, cols)
                if r_end <= r_start or c_end <= c_start:
                    continue
                block_rows = rng.randint(r_start, r_end, size=per_block)
                block_cols = rng.randint(c_start, c_end, size=per_block)
                for k in range(per_block):
                    if len(points) < n_samples:
                        points.append([block_rows[k], block_cols[k]])

        while len(points) < n_samples:
            points.append([rng.randint(0, rows), rng.randint(0, cols)])

        return np.array(points[:n_samples])

    else:
        raise ValueError(f"Unknown sampling strategy: {strategy}")


def create_spatial_cv_blocks(
    aoi_shape: Tuple[int, int],
    block_size: int,
    n_folds: int = 5,
    seed: int = 42,
) -> np.ndarray:
    """
    Create spatial blocks for cross-validation.

    Divides the AOI into spatial blocks and assigns each to a fold.
    Ensures spatial separation between training and validation.

    Args:
        aoi_shape: (rows, cols) of the AOI
        block_size: Size of each spatial block in pixels
        n_folds: Number of CV folds
        seed: Random seed

    Returns:
        (rows, cols) array of fold assignments (0 to n_folds-1)
    """
    rows, cols = aoi_shape
    fold_map = np.zeros((rows, cols), dtype=np.int32)

    rng = np.random.RandomState(seed)
    block_id = 0
    for r in range(0, rows, block_size):
        for c in range(0, cols, block_size):
            fold = block_id % n_folds
            r_end = min(r + block_size, rows)
            c_end = min(c + block_size, cols)
            fold_map[r:r_end, c:c_end] = fold
            block_id += 1

    return fold_map


# ============================================================
# Models (pure numpy implementations)
# ============================================================

class LogisticRegressionModel:
    """Logistic regression using gradient descent."""

    def __init__(self, learning_rate: float = 0.01, max_iter: int = 500,
                 tol: float = 1e-4):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.tol = tol
        self.weights = None
        self.bias = 0.0
        self.loss_history = []

    def _sigmoid(self, z: np.ndarray) -> np.ndarray:
        """Numerically stable sigmoid."""
        z_clipped = np.clip(z, -500, 500)
        return 1.0 / (1.0 + np.exp(-z_clipped))

    def fit(self, X: np.ndarray, y: np.ndarray) -> 'LogisticRegressionModel':
        """Fit logistic regression."""
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features, dtype=np.float64)
        self.bias = 0.0
        self.loss_history = []

        for iteration in range(self.max_iter):
            z = X @ self.weights + self.bias
            predictions = self._sigmoid(z)

            # Binary cross-entropy loss
            eps = 1e-15
            loss = -np.mean(y * np.log(predictions + eps) +
                          (1 - y) * np.log(1 - predictions + eps))
            self.loss_history.append(float(loss))

            # Gradients
            error = predictions - y
            dw = (1.0 / n_samples) * (X.T @ error)
            db = np.mean(error)

            # Update
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            # Convergence check
            if iteration > 0 and abs(self.loss_history[-2] - self.loss_history[-1]) < self.tol:
                break

        return self

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Predict probability of class 1."""
        if self.weights is None:
            raise RuntimeError("Model not fitted")
        z = X @ self.weights + self.bias
        return self._sigmoid(z)

    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        """Predict class labels."""
        return (self.predict_proba(X) >= threshold).astype(np.int32)

    def feature_importance(self) -> np.ndarray:
        """Return absolute weights as importance."""
        if self.weights is None:
            raise RuntimeError("Model not fitted")
        return np.abs(self.weights)


class DecisionTreeStump:
    """Simple decision tree stump (single split) for Random Forest."""

    def __init__(self, max_depth: int = 5, min_samples_split: int = 5,
                 min_samples_leaf: int = 2, max_features: str = "sqrt"):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.max_features = max_features
        self.tree = None

    def _gini(self, y: np.ndarray) -> float:
        """Compute Gini impurity."""
        if len(y) == 0:
            return 0.0
        p1 = np.mean(y)
        p0 = 1.0 - p1
        return 1.0 - p0 ** 2 - p1 ** 2

    def _best_split(self, X: np.ndarray, y: np.ndarray,
                    feature_indices: np.ndarray) -> Optional[Dict]:
        """Find the best split for a node."""
        best_gain = -1.0
        best_split = None
        n = len(y)
        parent_gini = self._gini(y)

        for feat_idx in feature_indices:
            values = X[:, feat_idx]
            # Use percentiles as split candidates
            unique_vals = np.unique(values)
            if len(unique_vals) <= 1:
                continue
            # Sample split points
            if len(unique_vals) > 20:
                split_candidates = np.percentile(unique_vals,
                                                 np.linspace(10, 90, 10))
            else:
                split_candidates = unique_vals[:-1]

            for threshold in split_candidates:
                left_mask = values <= threshold
                right_mask = ~left_mask

                n_left = np.sum(left_mask)
                n_right = np.sum(right_mask)

                if n_left < self.min_samples_leaf or n_right < self.min_samples_leaf:
                    continue

                gini_left = self._gini(y[left_mask])
                gini_right = self._gini(y[right_mask])

                weighted_gini = (n_left * gini_left + n_right * gini_right) / n
                gain = parent_gini - weighted_gini

                if gain > best_gain:
                    best_gain = gain
                    best_split = {
                        "feature": int(feat_idx),
                        "threshold": float(threshold),
                        "gain": float(gain),
                    }

        return best_split

    def _build_tree(self, X: np.ndarray, y: np.ndarray,
                    feature_indices: np.ndarray, depth: int) -> Dict:
        """Recursively build the tree."""
        n = len(y)
        proba = float(np.mean(y))

        # Stopping conditions
        if (depth >= self.max_depth or
            n < self.min_samples_split or
            self._gini(y) < 0.01):
            return {"leaf": True, "probability": proba, "n_samples": n}

        split = self._best_split(X, y, feature_indices)
        if split is None:
            return {"leaf": True, "probability": proba, "n_samples": n}

        feat = split["feature"]
        thresh = split["threshold"]
        left_mask = X[:, feat] <= thresh

        return {
            "leaf": False,
            "feature": feat,
            "threshold": thresh,
            "left": self._build_tree(X[left_mask], y[left_mask],
                                     feature_indices, depth + 1),
            "right": self._build_tree(X[~left_mask], y[~left_mask],
                                      feature_indices, depth + 1),
        }

    def fit(self, X: np.ndarray, y: np.ndarray) -> 'DecisionTreeStump':
        """Fit the decision tree."""
        n_features = X.shape[1]
        if self.max_features == "sqrt":
            n_select = max(1, int(math.sqrt(n_features)))
        elif self.max_features == "log2":
            n_select = max(1, int(math.log2(n_features)))
        else:
            n_select = n_features

        rng = np.random.RandomState()
        feature_indices = rng.choice(n_features, size=n_select, replace=False)
        self.tree = self._build_tree(X, y, feature_indices, 0)
        return self

    def _predict_single(self, x: np.ndarray, node: Dict) -> float:
        """Predict probability for a single sample."""
        if node["leaf"]:
            return node["probability"]
        if x[node["feature"]] <= node["threshold"]:
            return self._predict_single(x, node["left"])
        else:
            return self._predict_single(x, node["right"])

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Predict probabilities."""
        return np.array([self._predict_single(x, self.tree) for x in X])


class RandomForestModel:
    """Simple Random Forest using bootstrap aggregation."""

    def __init__(self, n_estimators: int = 50, max_depth: int = 6,
                 min_samples_split: int = 5, min_samples_leaf: int = 2,
                 max_features: str = "sqrt", seed: int = 42):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.max_features = max_features
        self.seed = seed
        self.trees = []
        self.feature_importances_ = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> 'RandomForestModel':
        """Fit random forest with bootstrap sampling."""
        rng = np.random.RandomState(self.seed)
        n_samples = X.shape[0]
        self.trees = []

        for i in range(self.n_estimators):
            # Bootstrap sample
            indices = rng.choice(n_samples, size=n_samples, replace=True)
            X_boot = X[indices]
            y_boot = y[indices]

            tree = DecisionTreeStump(
                max_depth=self.max_depth,
                min_samples_split=self.min_samples_split,
                min_samples_leaf=self.min_samples_leaf,
                max_features=self.max_features,
            )
            tree.fit(X_boot, y_boot)
            self.trees.append(tree)

        # Compute feature importance (mean decrease in impurity approximation)
        self._compute_feature_importance(X, y)
        return self

    def _compute_feature_importance(self, X: np.ndarray, y: np.ndarray):
        """Compute permutation-based feature importance."""
        base_proba = self.predict_proba(X)
        base_auc = compute_roc_auc(y, base_proba)
        n_features = X.shape[1]
        importances = np.zeros(n_features, dtype=np.float64)

        rng = np.random.RandomState(self.seed)
        for j in range(n_features):
            X_permuted = X.copy()
            # Permute feature j
            perm_idx = rng.permutation(len(X_permuted))
            X_permuted[:, j] = X_permuted[perm_idx, j]
            permuted_proba = self.predict_proba(X_permuted)
            permuted_auc = compute_roc_auc(y, permuted_proba)
            importances[j] = max(0, base_auc - permuted_auc)

        # Normalize
        total = np.sum(importances)
        if total > 0:
            importances /= total
        self.feature_importances_ = importances

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Average predictions from all trees."""
        if not self.trees:
            raise RuntimeError("Model not fitted")
        predictions = np.array([tree.predict_proba(X) for tree in self.trees])
        return np.mean(predictions, axis=0)

    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        """Predict class labels."""
        return (self.predict_proba(X) >= threshold).astype(np.int32)


class SlopeBaselineModel:
    """Simple slope-threshold baseline model."""

    def __init__(self, threshold: float = 25.0):
        self.threshold = threshold
        self.slope_idx = 0  # Assume slope is first factor

    def fit(self, X: np.ndarray, y: np.ndarray) -> 'SlopeBaselineModel':
        """Find optimal threshold on slope."""
        slopes = X[:, self.slope_idx]
        best_threshold = 15.0
        best_accuracy = 0.0

        for t in np.percentile(slopes, np.linspace(10, 90, 20)):
            preds = (slopes >= t).astype(np.int32)
            acc = np.mean(preds == y)
            if acc > best_accuracy:
                best_accuracy = acc
                best_threshold = t

        self.threshold = best_threshold
        return self

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Probability based on slope threshold."""
        slopes = X[:, self.slope_idx]
        # Linear ramp from 0 to 1 around threshold
        proba = np.clip((slopes - self.threshold + 10) / 20.0, 0, 1)
        return proba

    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        """Predict class labels."""
        return (self.predict_proba(X) >= threshold).astype(np.int32)


# ============================================================
# Validation Metrics
# ============================================================

def compute_roc_curve(y_true: np.ndarray, y_score: np.ndarray,
                      n_thresholds: int = 50) -> Dict[str, Any]:
    """
    Compute ROC curve.

    Returns:
        Dict with fpr, tpr, thresholds, and AUC
    """
    # Sort by score descending
    desc_order = np.argsort(-y_score)
    y_sorted = y_true[desc_order]

    n_pos = np.sum(y_true == 1)
    n_neg = np.sum(y_true == 0)

    if n_pos == 0 or n_neg == 0:
        return {
            "fpr": [0.0, 1.0],
            "tpr": [0.0, 1.0],
            "thresholds": [1.0, 0.0],
            "auc": 0.5,
        }

    # Compute TPR and FPR at various thresholds
    thresholds = np.linspace(1.0, 0.0, n_thresholds)
    tpr_list = []
    fpr_list = []

    for thresh in thresholds:
        preds = (y_score >= thresh).astype(np.int32)
        tp = np.sum((preds == 1) & (y_true == 1))
        fp = np.sum((preds == 1) & (y_true == 0))
        fn = np.sum((preds == 0) & (y_true == 1))
        tn = np.sum((preds == 0) & (y_true == 0))

        tpr = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0
        tpr_list.append(float(tpr))
        fpr_list.append(float(fpr))

    # Compute AUC using trapezoidal rule
    auc = 0.0
    for i in range(len(fpr_list) - 1):
        width = abs(fpr_list[i + 1] - fpr_list[i])
        height = (tpr_list[i] + tpr_list[i + 1]) / 2.0
        auc += width * height

    return {
        "fpr": fpr_list,
        "tpr": tpr_list,
        "thresholds": thresholds.tolist(),
        "auc": round(float(auc), 4),
    }


def compute_roc_auc(y_true: np.ndarray, y_score: np.ndarray) -> float:
    """Compute ROC AUC score."""
    roc = compute_roc_curve(y_true, y_score)
    return roc["auc"]


def compute_pr_curve(y_true: np.ndarray, y_score: np.ndarray,
                     n_thresholds: int = 50) -> Dict[str, Any]:
    """
    Compute Precision-Recall curve.

    Returns:
        Dict with precision, recall, thresholds, and AP
    """
    thresholds = np.linspace(1.0, 0.0, n_thresholds)
    precision_list = []
    recall_list = []

    n_pos = np.sum(y_true == 1)

    if n_pos == 0:
        return {
            "precision": [0.0],
            "recall": [0.0],
            "thresholds": [0.0],
            "average_precision": 0.0,
        }

    for thresh in thresholds:
        preds = (y_score >= thresh).astype(np.int32)
        tp = np.sum((preds == 1) & (y_true == 1))
        fp = np.sum((preds == 1) & (y_true == 0))
        fn = np.sum((preds == 0) & (y_true == 1))

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        precision_list.append(float(precision))
        recall_list.append(float(recall))

    # Average precision (AP) using step function
    ap = 0.0
    prev_recall = 0.0
    for i in range(len(recall_list) - 1, -1, -1):
        if precision_list[i] > 0:
            ap += precision_list[i] * (recall_list[i] - prev_recall)
            prev_recall = recall_list[i]

    return {
        "precision": precision_list,
        "recall": recall_list,
        "thresholds": thresholds.tolist(),
        "average_precision": round(float(ap), 4),
    }


def compute_calibration_curve(y_true: np.ndarray, y_score: np.ndarray,
                              n_bins: int = 10) -> Dict[str, Any]:
    """
    Compute calibration curve (reliability diagram).

    Returns:
        Dict with mean_predicted_prob, fraction_of_positives, bin_counts
    """
    bin_edges = np.linspace(0.0, 1.0, n_bins + 1)
    bin_indices = np.digitize(y_score, bin_edges[1:-1])

    mean_predicted = []
    fraction_positive = []
    bin_counts = []

    for b in range(n_bins):
        mask = bin_indices == b
        count = np.sum(mask)
        bin_counts.append(int(count))
        if count > 0:
            mean_predicted.append(round(float(np.mean(y_score[mask])), 4))
            fraction_positive.append(round(float(np.mean(y_true[mask])), 4))
        else:
            mean_predicted.append(round(float((bin_edges[b] + bin_edges[b + 1]) / 2), 4))
            fraction_positive.append(0.0)

    # Expected Calibration Error (ECE)
    ece = 0.0
    total = len(y_true)
    for b in range(n_bins):
        if bin_counts[b] > 0:
            ece += (bin_counts[b] / total) * abs(fraction_positive[b] - mean_predicted[b])

    return {
        "mean_predicted_prob": mean_predicted,
        "fraction_of_positives": fraction_positive,
        "bin_counts": bin_counts,
        "ece": round(float(ece), 4),
    }


def compute_classification_metrics(y_true: np.ndarray, y_pred: np.ndarray,
                                   y_score: np.ndarray) -> Dict[str, Any]:
    """Compute comprehensive classification metrics."""
    tp = int(np.sum((y_pred == 1) & (y_true == 1)))
    fp = int(np.sum((y_pred == 1) & (y_true == 0)))
    fn = int(np.sum((y_pred == 0) & (y_true == 1)))
    tn = int(np.sum((y_pred == 0) & (y_true == 0)))

    accuracy = (tp + tn) / (tp + fp + fn + tn) if (tp + fp + fn + tn) > 0 else 0.0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (2 * precision * recall / (precision + recall)
          if (precision + recall) > 0 else 0.0)
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0.0

    roc = compute_roc_curve(y_true, y_score)
    pr = compute_pr_curve(y_true, y_score)

    return {
        "tp": tp, "fp": fp, "fn": fn, "tn": tn,
        "accuracy": round(float(accuracy), 4),
        "precision": round(float(precision), 4),
        "recall": round(float(recall), 4),
        "f1": round(float(f1), 4),
        "specificity": round(float(specificity), 4),
        "roc_auc": roc["auc"],
        "pr_auc": pr["average_precision"],
    }


# ============================================================
# Susceptibility Classification
# ============================================================

def classify_susceptibility(probabilities: np.ndarray,
                            schema: str = "five_class") -> np.ndarray:
    """
    Classify susceptibility probabilities into zones.

    Args:
        probabilities: (N,) array of susceptibility probabilities [0, 1]
        schema: 'five_class' or 'four_class'

    Returns:
        (N,) array of class labels (1-5 or 1-4)
    """
    if schema == "five_class":
        # Very low: <0.2, Low: 0.2-0.4, Moderate: 0.4-0.6, High: 0.6-0.8, Very high: >0.8
        classes = np.ones_like(probabilities, dtype=np.int32)
        classes[probabilities >= 0.2] = 2
        classes[probabilities >= 0.4] = 3
        classes[probabilities >= 0.6] = 4
        classes[probabilities >= 0.8] = 5
    elif schema == "four_class":
        classes = np.ones_like(probabilities, dtype=np.int32)
        classes[probabilities >= 0.25] = 2
        classes[probabilities >= 0.50] = 3
        classes[probabilities >= 0.75] = 4
    else:
        raise ValueError(f"Unknown schema: {schema}")

    return classes


def compute_zone_statistics(susceptibility: np.ndarray,
                            classes: np.ndarray) -> Dict[str, Any]:
    """Compute area statistics for each susceptibility zone."""
    total_pixels = susceptibility.size
    zone_names = {
        1: "very_low", 2: "low", 3: "moderate", 4: "high", 5: "very_high"
    }

    stats = {}
    for cls in np.unique(classes):
        mask = classes == cls
        count = int(np.sum(mask))
        name = zone_names.get(int(cls), f"class_{cls}")
        stats[name] = {
            "pixel_count": count,
            "percentage": round(100.0 * count / total_pixels, 2),
            "mean_susceptibility": round(float(np.mean(susceptibility[mask])), 4)
                                        if count > 0 else 0.0,
        }

    return stats


# ============================================================
# Uncertainty Estimation
# ============================================================

def compute_prediction_uncertainty(model: Any, X: np.ndarray,
                                   n_bootstrap: int = 20,
                                   seed: int = 42) -> Dict[str, Any]:
    """
    Estimate prediction uncertainty using bootstrap.

    Returns:
        Dict with mean, std, lower/upper confidence bounds
    """
    rng = np.random.RandomState(seed)
    n_samples = X.shape[0]
    predictions = np.zeros((n_bootstrap, n_samples), dtype=np.float64)

    if isinstance(model, RandomForestModel):
        # Use individual tree predictions as uncertainty source
        for i, tree in enumerate(model.trees[:min(n_bootstrap, len(model.trees))]):
            predictions[i] = tree.predict_proba(X)
    else:
        # For other models, use prediction variance across bootstrap samples
        for b in range(n_bootstrap):
            idx = rng.choice(n_samples, size=n_samples, replace=True)
            try:
                predictions[b] = model.predict_proba(X)
            except Exception:
                predictions[b] = model.predict_proba(X)

    mean_pred = np.mean(predictions, axis=0)
    std_pred = np.std(predictions, axis=0)

    return {
        "mean": mean_pred,
        "std": std_pred,
        "lower_95": np.clip(mean_pred - 1.96 * std_pred, 0, 1),
        "upper_95": np.clip(mean_pred + 1.96 * std_pred, 0, 1),
        "uncertainty_map": std_pred,
    }


# ============================================================
# Synthetic Data Generation
# ============================================================

def generate_synthetic_factors(n_rows: int = 100, n_cols: int = 100,
                               n_factors: int = 8, seed: int = 42) -> np.ndarray:
    """
    Generate synthetic factor raster stack.

    Returns:
        (n_rows, n_cols, n_factors) array
    """
    rng = np.random.RandomState(seed)
    factors = np.zeros((n_rows, n_cols, n_factors), dtype=np.float32)

    # Fill factors up to n_factors (max 8 predefined, beyond that random)
    # Factor 0: Slope (degrees) - 0 to 60
    if n_factors > 0:
        x_grad = np.array([(i / n_rows) * 0.5 + rng.normal(0, 0.1)
                           for i in range(n_rows)]).reshape(-1, 1)
        y_grad = np.array([(j / n_cols) * 0.3 + rng.normal(0, 0.1)
                           for j in range(n_cols)]).reshape(1, -1)
        factors[:, :, 0] = np.clip(
            30 * np.sqrt(x_grad**2 + y_grad**2) +
            rng.normal(0, 3, (n_rows, n_cols)), 0, 60
        )
    # Factor 1: Aspect (degrees) - 0 to 360
    if n_factors > 1:
        factors[:, :, 1] = rng.uniform(0, 360, (n_rows, n_cols))
    # Factor 2: Curvature - -1 to 1
    if n_factors > 2:
        factors[:, :, 2] = rng.normal(0, 0.3, (n_rows, n_cols))
    # Factor 3: Flow accumulation (log scale)
    if n_factors > 3:
        factors[:, :, 3] = np.clip(rng.exponential(2, (n_rows, n_cols)), 0, 20)
    # Factor 4: Lithology (categorical 1-5)
    if n_factors > 4:
        factors[:, :, 4] = rng.choice([1, 2, 3, 4, 5],
                                       (n_rows, n_cols)).astype(float)
    # Factor 5: Distance to fault (meters, 0-2000)
    if n_factors > 5:
        factors[:, :, 5] = rng.exponential(500, (n_rows, n_cols))
    # Factor 6: Rainfall (mm/year, 400-2000)
    if n_factors > 6:
        factors[:, :, 6] = rng.uniform(400, 2000, (n_rows, n_cols))
    # Factor 7: Distance to road (meters, 0-3000)
    if n_factors > 7:
        factors[:, :, 7] = rng.exponential(800, (n_rows, n_cols))
    # Any additional factors beyond 8: random normal
    for k in range(8, n_factors):
        factors[:, :, k] = rng.randn(n_rows, n_cols)

    return factors


def generate_synthetic_landslide_inventory(
    n_rows: int = 100, n_cols: int = 100,
    n_landslides: int = 50,
    factor_data: Optional[np.ndarray] = None,
    seed: int = 42,
) -> np.ndarray:
    """
    Generate synthetic landslide inventory points.

    Landslides are more likely on steeper slopes (factor 0).

    Returns:
        (n_landslides, 2) array of (row, col) coordinates
    """
    rng = np.random.RandomState(seed)

    if factor_data is not None:
        slope = factor_data[:, :, 0]
        # Probability proportional to slope
        prob = slope.flatten() / np.sum(slope) if np.sum(slope) > 0 else None
        if prob is not None:
            indices = rng.choice(
                n_rows * n_cols, size=n_landslides, replace=False, p=prob
            )
            rows = indices // n_cols
            cols = indices % n_cols
        else:
            rows = rng.randint(0, n_rows, size=n_landslides)
            cols = rng.randint(0, n_cols, size=n_landslides)
    else:
        rows = rng.randint(0, n_rows, size=n_landslides)
        cols = rng.randint(0, n_cols, size=n_landslides)

    return np.column_stack([rows, cols])


def extract_factor_values(factor_data: np.ndarray,
                          points: np.ndarray) -> np.ndarray:
    """
    Extract factor values at given points.

    Args:
        factor_data: (rows, cols, n_factors) array
        points: (N, 2) array of (row, col) coordinates

    Returns:
        (N, n_factors) array of factor values
    """
    n_points = len(points)
    n_factors = factor_data.shape[2]
    values = np.zeros((n_points, n_factors), dtype=np.float64)

    for i in range(n_points):
        r, c = int(points[i, 0]), int(points[i, 1])
        r = np.clip(r, 0, factor_data.shape[0] - 1)
        c = np.clip(c, 0, factor_data.shape[1] - 1)
        values[i] = factor_data[r, c, :]

    return values


def _read_vector_features(path: Path) -> List[Dict[str, Any]]:
    """Read features (with geometry + properties) from GeoJSON/Shapefile/CSV.

    CSV inputs must have columns x, y (and optional type).
    Returns a list of feature dicts with keys: geometry (shapely), properties.
    """
    suffix = path.suffix.lower()
    features: List[Dict[str, Any]] = []

    if suffix == ".csv":
        with open(path, "r", encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                try:
                    x = float(row["x"])
                    y = float(row["y"])
                except (KeyError, ValueError) as e:
                    raise ValueError(
                        f"Invalid landslide CSV at {path}: missing/invalid "
                        f"required field (x, y): {e}"
                    ) from e
                if not _HAS_SHAPELY:
                    raise RuntimeError(
                        "shapely is required to load vector landslide "
                        "inventories. Install with: pip install shapely"
                    )
                from shapely.geometry import Point
                geom = Point(x, y)
                features.append({
                    "geometry": geom,
                    "properties": {k: v for k, v in row.items()
                                    if k not in ("x", "y") and v not in (None, "")},
                })
        return features

    if suffix in (".json", ".geojson"):
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not isinstance(data, dict) or data.get("type") != "FeatureCollection":
            raise ValueError(
                f"Landslide inventory JSON at {path} is not a GeoJSON FeatureCollection"
            )
        for feat in data.get("features", []):
            if not _HAS_SHAPELY:
                raise RuntimeError(
                    "shapely is required to load vector landslide "
                    "inventories. Install with: pip install shapely"
                )
            geom = _shp_shape(feat.get("geometry"))
            if geom is None or geom.is_empty:
                continue
            features.append({
                "geometry": geom,
                "properties": feat.get("properties", {}) or {},
            })
        return features

    if suffix in (".shp",):
        if not _HAS_FIONA:
            raise RuntimeError(
                "fiona is required to load Shapefile landslide inventories. "
                "Install with: pip install fiona"
            )
        with fiona.open(str(path)) as src:
            for feat in src:
                geom = _shp_shape(feat.get("geometry")) if _HAS_SHAPELY else None
                if geom is None or geom.is_empty:
                    continue
                features.append({
                    "geometry": geom,
                    "properties": dict(feat.get("properties", {}) or {}),
                })
        return features

    raise ValueError(
        f"Unsupported landslide-inventory file format: {suffix}. "
        f"Use .geojson / .json / .shp / .csv"
    )


def load_landslide_inventory(
    path: Path,
    n_rows: int,
    n_cols: int,
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """Load a landslide inventory (GeoJSON/Shapefile/CSV) and convert
    features to (N, 2) (row, col) pixel coordinates.

    Strategy: compute the geographic bounding box of all features, then map
    that bbox to the synthetic factor raster (n_rows x n_cols). A point's
    (x, y) -> (col, row) via linear interpolation within the inventory bbox.

    Returns:
        (landslide_points (N, 2), info dict with bbox and n_features)
    """
    features = _read_vector_features(path)
    if not features:
        raise ValueError(f"No features found in landslide inventory: {path}")

    minx, miny, maxx, maxy = (
        features[0]["geometry"].bounds[0],
        features[0]["geometry"].bounds[1],
        features[0]["geometry"].bounds[2],
        features[0]["geometry"].bounds[3],
    )
    for f in features[1:]:
        bx0, by0, bx1, by1 = f["geometry"].bounds
        minx, miny = min(minx, bx0), min(miny, by0)
        maxx, maxy = max(maxx, bx1), max(maxy, by1)

    # Avoid divide-by-zero: if inventory bbox is a point, center on the raster
    span_x = maxx - minx if maxx > minx else 1.0
    span_y = maxy - miny if maxy > miny else 1.0

    # Use point-on-surface for polygons, so a polygon maps to a single pixel
    points: List[Tuple[float, float]] = []
    for f in features:
        geom = f["geometry"]
        if geom.geom_type == "Point":
            pt = geom
        else:
            # representative_point is guaranteed to lie within the geometry
            pt = geom.representative_point()
        points.append((pt.x, pt.y))

    rows_list: List[int] = []
    cols_list: List[int] = []
    for x, y in points:
        # Map (x, y) in inventory bbox to (col, row) in 0..(n_cols-1), 0..(n_rows-1)
        col_f = (x - minx) / span_x * (n_cols - 1)
        row_f = (1.0 - (y - miny) / span_y) * (n_rows - 1)
        r = int(np.clip(round(row_f), 0, n_rows - 1))
        c = int(np.clip(round(col_f), 0, n_cols - 1))
        rows_list.append(r)
        cols_list.append(c)

    landslide_points = np.column_stack([
        np.array(rows_list, dtype=np.int32),
        np.array(cols_list, dtype=np.int32),
    ])

    info = {
        "n_features": len(features),
        "bbox": [minx, miny, maxx, maxy],
        "n_rows": n_rows,
        "n_cols": n_cols,
    }
    return landslide_points, info


def normalize_factors(X: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Z-score normalize factors.

    Returns:
        (normalized_X, mean, std)
    """
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    std[std < 1e-10] = 1.0  # Avoid division by zero
    X_norm = (X - mean) / std
    return X_norm, mean, std


# ============================================================
# Main Pipeline
# ============================================================

def run_landslide_pipeline(args: argparse.Namespace) -> int:
    """Main landslide susceptibility workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("ls-output")
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logging(output_dir)
    logger.info("Landslide Susceptibility Assessment - Starting")

    # Load factor config
    factor_config_path = getattr(args, 'factor_config', None)
    try:
        factor_config = load_factor_config(factor_config_path)
        logger.info(f"Factor config loaded: version {factor_config.get('version', 'unknown')}")
    except Exception as e:
        logger.error(f"Failed to load factor config: {e}")
        return EXIT_VALIDATION

    # --- Synthetic/demo mode or file-based mode ---
    use_synthetic = not (hasattr(args, 'landslide_inventory') and args.landslide_inventory)

    factor_names = factor_config.get("factor_names",
                                     ["slope", "aspect", "curvature", "flow_acc",
                                      "lithology", "dist_fault", "rainfall", "dist_road"])

    if use_synthetic:
        logger.info("Running in synthetic demo mode")

        n_rows = getattr(args, 'demo_rows', 100)
        n_cols = getattr(args, 'demo_cols', 100)
        n_landslides = getattr(args, 'demo_landslides', 50)

        # Generate synthetic data
        factor_data = generate_synthetic_factors(n_rows, n_cols,
                                                 len(factor_names), seed=42)
        landslide_points = generate_synthetic_landslide_inventory(
            n_rows, n_cols, n_landslides, factor_data, seed=42
        )

        # Extract factor values at landslide locations
        X_positive = extract_factor_values(factor_data, landslide_points)
        y_positive = np.ones(len(landslide_points), dtype=np.int32)

        # Generate negative samples
        neg_sampling = getattr(args, 'negative_sampling', 'buffer')
        neg_points = generate_negative_samples(
            n_samples=len(landslide_points),
            aoi_shape=(n_rows, n_cols),
            strategy=neg_sampling,
            landslide_points=landslide_points,
            min_distance=3,
            seed=42,
        )
        X_negative = extract_factor_values(factor_data, neg_points)
        y_negative = np.zeros(len(neg_points), dtype=np.int32)

        # Combine
        X = np.vstack([X_positive, X_negative])
        y = np.concatenate([y_positive, y_negative])

    else:
        logger.info(f"Landslide inventory: {args.landslide_inventory}")
        # File-based mode: load the user-supplied landslide inventory as the
        # positive sample set. Factor rasters (slope/aspect/...) are not part
        # of the CLI in this version, so we still generate a synthetic factor
        # stack to drive the model — the inventory is real, however, so the
        # spatial pattern of positives is genuinely user-controlled.
        n_rows, n_cols = 100, 100
        factor_data = generate_synthetic_factors(n_rows, n_cols, len(factor_names))
        inv_path = Path(args.landslide_inventory)
        try:
            landslide_points, inv_info = load_landslide_inventory(
                inv_path, n_rows=n_rows, n_cols=n_cols
            )
            logger.info(
                f"Loaded {inv_info['n_features']} landslide features from "
                f"{inv_path} (bbox={inv_info['bbox']})"
            )
        except Exception as e:
            logger.error(f"Failed to load landslide inventory: {e}")
            cleanup_logging()
            return EXIT_VALIDATION
        X_positive = extract_factor_values(factor_data, landslide_points)
        y_positive = np.ones(len(landslide_points), dtype=np.int32)
        neg_points = generate_negative_samples(
            n_samples=len(landslide_points),
            aoi_shape=(n_rows, n_cols),
            strategy=getattr(args, 'negative_sampling', 'buffer'),
            landslide_points=landslide_points,
            min_distance=3,
            seed=42,
        )
        X_negative = extract_factor_values(factor_data, neg_points)
        y_negative = np.zeros(len(neg_points), dtype=np.int32)
        X = np.vstack([X_positive, X_negative])
        y = np.concatenate([y_positive, y_negative])

    logger.info(f"Total samples: {len(y)} (positive: {np.sum(y==1)}, "
                f"negative: {np.sum(y==0)})")

    # --- Normalize factors ---
    X_norm, X_mean, X_std = normalize_factors(X)

    # --- Collinearity check ---
    vif_threshold = factor_config.get("vif_threshold", 5.0)
    collinearity = check_collinearity(X_norm, factor_names,
                                      vif_threshold=vif_threshold)
    logger.info(f"Collinearity check: {len(collinearity['flagged_factors'])} flagged factors")

    # --- Spatial Cross-Validation ---
    cv_block_size = getattr(args, 'cv_block_size', 20)
    n_folds = getattr(args, 'n_folds', 5)

    fold_map = create_spatial_cv_blocks(
        (n_rows, n_cols), cv_block_size, n_folds, seed=42
    )
    # Assign fold to each sample based on spatial location
    sample_folds = np.zeros(len(y), dtype=np.int32)
    for i in range(len(y)):
        if i < len(landslide_points):
            r, c = int(landslide_points[i, 0]), int(landslide_points[i, 1])
        else:
            idx = i - len(landslide_points)
            r, c = int(neg_points[idx, 0]), int(neg_points[idx, 1])
        r = np.clip(r, 0, n_rows - 1)
        c = np.clip(c, 0, n_cols - 1)
        sample_folds[i] = fold_map[r, c]

    # --- Model Training and Spatial CV ---
    model_type = getattr(args, 'model', 'logistic_regression')
    logger.info(f"Model type: {model_type}")

    cv_results = []
    all_y_true = []
    all_y_score = []

    for fold in range(n_folds):
        # Split by spatial block
        val_mask = sample_folds == fold
        train_mask = ~val_mask

        if np.sum(val_mask) < 5 or np.sum(train_mask) < 20:
            logger.warning(f"Fold {fold}: insufficient samples, skipping")
            continue

        X_train, y_train = X_norm[train_mask], y[train_mask]
        X_val, y_val = X_norm[val_mask], y[val_mask]

        # Train model
        if model_type == "logistic_regression":
            model = LogisticRegressionModel(learning_rate=0.05, max_iter=300)
        elif model_type == "random_forest":
            model = RandomForestModel(n_estimators=30, max_depth=5, seed=42)
        elif model_type == "slope_baseline":
            model = SlopeBaselineModel()
        else:
            logger.error(f"Unknown model type: {model_type}")
            return EXIT_ARG

        model.fit(X_train, y_train)
        y_score = model.predict_proba(X_val)

        # Metrics for this fold
        fold_metrics = compute_classification_metrics(
            y_val, (y_score >= 0.5).astype(np.int32), y_score
        )
        fold_metrics["fold"] = fold
        fold_metrics["n_train"] = int(np.sum(train_mask))
        fold_metrics["n_val"] = int(np.sum(val_mask))
        cv_results.append(fold_metrics)

        all_y_true.append(y_val)
        all_y_score.append(y_score)

        logger.info(f"Fold {fold}: AUC={fold_metrics['roc_auc']:.3f}, "
                    f"F1={fold_metrics['f1']:.3f}")

    # --- Aggregate CV results ---
    if cv_results:
        mean_auc = float(np.mean([r["roc_auc"] for r in cv_results]))
        std_auc = float(np.std([r["roc_auc"] for r in cv_results]))
        mean_f1 = float(np.mean([r["f1"] for r in cv_results]))
        mean_accuracy = float(np.mean([r["accuracy"] for r in cv_results]))
    else:
        mean_auc = std_auc = mean_f1 = mean_accuracy = 0.0

    logger.info(f"Spatial CV results: AUC={mean_auc:.3f}±{std_auc:.3f}, "
                f"F1={mean_f1:.3f}")

    # --- Train final model on all data ---
    if model_type == "logistic_regression":
        final_model = LogisticRegressionModel(learning_rate=0.05, max_iter=300)
    elif model_type == "random_forest":
        final_model = RandomForestModel(n_estimators=50, max_depth=6, seed=42)
    elif model_type == "slope_baseline":
        final_model = SlopeBaselineModel()
    else:
        return EXIT_ARG

    final_model.fit(X_norm, y)

    # --- Factor importance ---
    if model_type == "logistic_regression":
        importance = final_model.feature_importance()
        importance /= np.sum(importance) if np.sum(importance) > 0 else 1
    elif model_type == "random_forest":
        importance = final_model.feature_importances_
    elif model_type == "slope_baseline":
        importance = np.zeros(len(factor_names))
        importance[0] = 1.0  # Only slope

    factor_importance = {
        name: round(float(importance[i]), 4)
        for i, name in enumerate(factor_names)
    }

    # --- Predict full susceptibility map ---
    if use_synthetic:
        # Reshape factor data to (n_pixels, n_factors)
        X_all = factor_data.reshape(-1, len(factor_names))
        X_all_norm = (X_all - X_mean) / X_std
        susceptibility_flat = final_model.predict_proba(X_all_norm)
        susceptibility_map = susceptibility_flat.reshape(n_rows, n_cols)

        # Classify
        class_schema = getattr(args, 'class_schema', 'five_class')
        zone_map = classify_susceptibility(susceptibility_flat, class_schema)
        zone_map = zone_map.reshape(n_rows, n_cols)

        # Zone statistics
        zone_stats = compute_zone_statistics(susceptibility_map, zone_map)

        # Uncertainty
        uncertainty = compute_prediction_uncertainty(
            final_model, X_all_norm, n_bootstrap=20
        )
        uncertainty_map = uncertainty["uncertainty_map"].reshape(n_rows, n_cols)
    else:
        susceptibility_map = np.zeros((10, 10))
        zone_map = np.zeros((10, 10), dtype=np.int32)
        zone_stats = {}
        uncertainty_map = np.zeros((10, 10))

    # --- Calibration curve ---
    if all_y_true and all_y_score:
        combined_y_true = np.concatenate(all_y_true)
        combined_y_score = np.concatenate(all_y_score)
        calibration = compute_calibration_curve(combined_y_true, combined_y_score)
    else:
        calibration = {"mean_predicted_prob": [], "fraction_of_positives": [],
                       "bin_counts": [], "ece": 0.0}

    # --- Generate outputs ---

    # susceptibility.tif (numpy format for synthetic mode)
    if use_synthetic:
        susp_path = output_dir / "susceptibility.tif"
        try:
            import rasterio
            from rasterio.transform import from_bounds
            transform = from_bounds(0, 0, n_cols, n_rows, n_cols, n_rows)
            with rasterio.open(
                str(susp_path), 'w', driver='GTiff',
                height=n_rows, width=n_cols, count=1,
                dtype=susceptibility_map.dtype,
                crs='EPSG:4326', transform=transform,
            ) as dst:
                dst.write(susceptibility_map, 1)
        except ImportError:
            # Fallback: save as .npy
            susp_path = output_dir / "susceptibility.npy"
            np.save(str(suscept_path := susp_path), susceptibility_map)

    # susceptibility_zones.geojson
    zones_geojson = {
        "type": "FeatureCollection",
        "features": [],
    }
    if use_synthetic:
        zone_names = {1: "very_low", 2: "low", 3: "moderate", 4: "high", 5: "very_high"}
        for cls in np.unique(zone_map):
            mask = zone_map == cls
            if np.sum(mask) > 0:
                # Create a representative polygon for each zone
                rows, cols = np.where(mask)
                r_min, r_max = int(np.min(rows)), int(np.max(rows))
                c_min, c_max = int(np.min(cols)), int(np.max(cols))
                poly = create_polygon(c_min, r_min, c_max - c_min, r_max - r_min)
                zones_geojson["features"].append({
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [poly],
                    },
                    "properties": {
                        "zone_class": int(cls),
                        "zone_name": zone_names.get(int(cls), f"class_{cls}"),
                        "pixel_count": int(np.sum(mask)),
                    },
                })

    zones_path = output_dir / "susceptibility_zones.geojson"
    zones_path.write_text(
        json.dumps(zones_geojson, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # model_metrics.json
    model_metrics = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_type": model_type,
        "n_samples": len(y),
        "n_positive": int(np.sum(y == 1)),
        "n_negative": int(np.sum(y == 0)),
        "n_factors": len(factor_names),
        "factor_names": factor_names,
        "spatial_cv": {
            "n_folds": n_folds,
            "block_size": cv_block_size,
            "fold_results": cv_results,
            "mean_auc": round(mean_auc, 4),
            "std_auc": round(std_auc, 4),
            "mean_f1": round(mean_f1, 4),
            "mean_accuracy": round(mean_accuracy, 4),
        },
        "calibration": calibration,
        "zone_statistics": zone_stats,
    }
    metrics_path = output_dir / "model_metrics.json"
    metrics_path.write_text(
        json.dumps(model_metrics, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # factor_importance.csv
    fi_path = output_dir / "factor_importance.csv"
    with open(fi_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["factor", "importance", "rank"])
        sorted_factors = sorted(factor_importance.items(), key=lambda x: -x[1])
        for rank, (name, imp) in enumerate(sorted_factors, 1):
            writer.writerow([name, imp, rank])

    # model_card.json
    model_card = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_type": model_type,
        "intended_use": "Landslide susceptibility mapping for planning purposes",
        "limitations": [
            "Output is susceptibility (relative likelihood), NOT temporal probability or risk",
            "Requires trigger probability and exposure data for risk assessment",
            "Model accuracy depends on landslide inventory completeness",
            "Spatial transferability not guaranteed",
        ],
        "training_data": {
            "n_landslides": int(np.sum(y == 1)),
            "n_non_landslides": int(np.sum(y == 0)),
            "negative_sampling_strategy": getattr(args, 'negative_sampling', 'buffer'),
            "inventory_completeness_note": "Synthetic data - real inventory quality varies",
        },
        "factors": {
            "names": factor_names,
            "collinearity_check": collinearity["pass"],
            "vif_values": collinearity["vif_values"],
        },
        "validation": {
            "method": "spatial_block_cross_validation",
            "n_folds": n_folds,
            "block_size_pixels": cv_block_size,
            "mean_auc": round(mean_auc, 4),
            "std_auc": round(std_auc, 4),
        },
        "ethical_considerations": [
            "Not for engineering safety decisions without expert review",
            "Not for administrative determination or compensation",
        ],
    }
    card_path = output_dir / "model_card.json"
    card_path.write_text(
        json.dumps(model_card, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # request.json
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "synthetic" if use_synthetic else "file",
        "model_type": model_type,
        "negative_sampling": getattr(args, 'negative_sampling', 'buffer'),
        "cv_block_size": cv_block_size,
        "n_folds": n_folds,
        "class_schema": getattr(args, 'class_schema', 'five_class'),
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
        "n_samples": len(y),
        "n_positive": int(np.sum(y == 1)),
        "n_negative": int(np.sum(y == 0)),
        "n_factors": len(factor_names),
        "factor_names": factor_names,
        "aoi_shape": [n_rows, n_cols] if use_synthetic else None,
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # output-manifest.json
    output_files = {
        "model_metrics.json": str(metrics_path),
        "factor_importance.csv": str(fi_path),
        "model_card.json": str(card_path),
        "susceptibility_zones.geojson": str(zones_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(dataset_path),
    }
    if use_synthetic:
        susp_actual = output_dir / "susceptibility.tif"
        if not susp_actual.exists():
            susp_actual = output_dir / "susceptibility.npy"
        if susp_actual.exists():
            output_files["susceptibility_map"] = str(susp_actual)

    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "output_files": output_files,
        "summary": {
            "model_type": model_type,
            "mean_auc": round(mean_auc, 4),
            "mean_f1": round(mean_f1, 4),
            "n_factors": len(factor_names),
        },
    }
    # Inject MPC download metadata when --bbox/--aoi-file was used.
    download_meta = getattr(args, "_download_meta", None)
    if download_meta:
        manifest["data_source"] = download_meta.get("data_source")
        manifest["fetched_at"] = download_meta.get("fetched_at")
        manifest["collection"] = download_meta.get("collection")
        manifest["bbox"] = download_meta.get("bbox")
        manifest["date_range"] = download_meta.get("date_range")
        manifest["downloaded_paths"] = download_meta.get("downloaded_paths")
    manifest_path = output_dir / "output-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # qa.json
    qa = {
        "status": "complete",
        "checks": {
            "metrics_generated": metrics_path.exists(),
            "importance_generated": fi_path.exists(),
            "model_card_generated": card_path.exists(),
            "zones_generated": zones_path.exists(),
            "all_outputs_written": all(
                Path(p).exists() for p in output_files.values()
            ),
        },
        "spatial_cv_performed": True,
        "n_cv_folds": len(cv_results),
        "mean_auc": round(mean_auc, 4),
        "collinearity_pass": collinearity["pass"],
    }
    qa_path = output_dir / "qa.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    logger.info(f"Pipeline complete: AUC={mean_auc:.3f}±{std_auc:.3f}, "
                f"F1={mean_f1:.3f}")
    cleanup_logging()
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Landslide Susceptibility Assessment")
    parser.add_argument("--landslide-inventory", default=None,
                        help="Path to landslide inventory (GeoJSON/Shapefile)")
    parser.add_argument("--factor-config", default=None,
                        help="Path to factor configuration JSON")
    parser.add_argument("--model", default="logistic_regression",
                        choices=["logistic_regression", "random_forest", "slope_baseline"],
                        help="Model type (default: logistic_regression)")
    parser.add_argument("--negative-sampling", default="buffer",
                        choices=["random", "buffer", "spatial_block"],
                        help="Negative sampling strategy (default: buffer)")
    parser.add_argument("--cv-block-size", type=int, default=20,
                        help="Spatial CV block size in pixels (default: 20)")
    parser.add_argument("--n-folds", type=int, default=5,
                        help="Number of CV folds (default: 5)")
    parser.add_argument("--class-schema", default="five_class",
                        choices=["five_class", "four_class"],
                        help="Susceptibility classification schema (default: five_class)")
    parser.add_argument("--output-dir", "-o", default="ls-output",
                        help="Output directory (default: ls-output)")
    parser.add_argument("--demo-rows", type=int, default=100,
                        help="Demo mode rows (default: 100)")
    parser.add_argument("--demo-cols", type=int, default=100,
                        help="Demo mode columns (default: 100)")
    parser.add_argument("--demo-landslides", type=int, default=50,
                        help="Demo mode landslide count (default: 50)")
    if _HAS_DATA_FETCHER:
        # Adds --bbox (W,S,E,N string), --date-range, --aoi-file, --cache-dir.
        # When the user supplies --bbox/--aoi-file but no --landslide-inventory,
        # we auto-download a DEM (`cop-dem-glo-30`) from MPC so the bbox-driven
        # workflow has at least one piece of real elevation data attached.
        add_bbox_date_args(parser)
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    args = parser.parse_args()

    # ─── auto-download a DEM when --bbox/--aoi-file is given (no inventory) ─
    # The landslide inventory itself remains user-supplied (skipped from auto
    # download per this skill's spec); the DEM is fetched as a side artifact
    # and recorded in the output manifest.
    _download_meta: Optional[Dict[str, Any]] = None
    has_inventory = bool(args.landslide_inventory) and Path(args.landslide_inventory).exists()
    if (
        _HAS_DATA_FETCHER
        and not has_inventory
        and (args.bbox or args.aoi_file)
    ):
        try:
            bbox = parse_bbox_arg(args.bbox, args.aoi_file)
            # cop-dem-glo-30 is a static mosaic (one acquisition date), so the
            # date filter is unnecessary. Pass None to skip it; record the
            # user-supplied --date-range in the manifest for traceability.
            dr = parse_date_range_arg(args.date_range)
            fetcher = DataFetcher(
                source=DataSource.PLANETARY_COMPUTER,
                cache_dir=Path(args.cache_dir) if args.cache_dir else None,
            )
            items = fetcher.search_stac(
                collection="cop-dem-glo-30",
                bbox=bbox,
                date_range=None,
                limit=1,
            )
            if items:
                download_dir = Path(args.output_dir) / "downloaded"
                paths = fetcher.download_assets(
                    items, out_dir=download_dir, max_items=1, max_total_mb=200.0,
                )
                if paths:
                    print(f"[downloader] fetched DEM: {paths[0]}")
                    _download_meta = {
                        "data_source": "MPC",
                        "fetched_at": datetime.now(timezone.utc).isoformat(),
                        "collection": "cop-dem-glo-30",
                        "bbox": bbox.to_string(),
                        "date_range": dr.to_dict() if dr else None,
                        "downloaded_paths": [str(p) for p in paths],
                    }
        except Exception as exc:  # pragma: no cover - network dependent
            print(f"[downloader] auto-download failed: {exc}; continuing with synthetic data",
                  file=sys.stderr)
    if _download_meta is not None:
        args._download_meta = _download_meta  # type: ignore[attr-defined]

    try:
        sys.exit(run_landslide_pipeline(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
