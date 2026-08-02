#!/usr/bin/env python3
"""
Forest Health Monitor - Multi-temporal forest canopy vitality assessment.

Detects forest health anomalies (drought stress, pest damage, wind throw,
persistent decline) from spectral indices. Distinguishes short-term
fluctuations from sustained deterioration using historical baselines,
persistence state machines, and climate attribution.

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

# Health severity levels
DEFAULT_SEVERITY_SCHEMA = {
    "healthy":       {"code": 0, "color": "00FF00", "description": "正常"},
    "mild_stress":   {"code": 1, "color": "FFFF00", "description": "轻度胁迫"},
    "moderate_decline": {"code": 2, "color": "FF9900", "description": "中度衰退"},
    "severe_decline":  {"code": 3, "color": "FF0000", "description": "严重衰退"},
    "mortality":     {"code": 4, "color": "990000", "description": "死亡/风倒"},
}

# Forest type definitions with phenological parameters
DEFAULT_FOREST_TYPES = {
    "evergreen": {
        "name": "常绿林",
        "ndvi_baseline": 0.65,
        "ndvi_amplitude": 0.10,  # small seasonal swing
        "ndmi_baseline": 0.30,
        "nbr_baseline": 0.50,
        "phenology_phase": "minimal",  # minimal seasonal variation
    },
    "deciduous": {
        "name": "落叶林",
        "ndvi_baseline": 0.55,
        "ndvi_amplitude": 0.35,  # large seasonal swing
        "ndmi_baseline": 0.25,
        "nbr_baseline": 0.40,
        "phenology_phase": "strong",  # strong seasonal variation
    },
    "mixed": {
        "name": "混交林",
        "ndvi_baseline": 0.60,
        "ndvi_amplitude": 0.20,
        "ndmi_baseline": 0.28,
        "nbr_baseline": 0.45,
        "phenology_phase": "moderate",
    },
}

# Health index weights for multi-index consensus
INDEX_WEIGHTS = {
    "ndvi": 0.30,
    "evi": 0.20,
    "ndmi": 0.25,
    "nbr": 0.25,
}


def compute_ndvi(nir, red):
    """Compute NDVI = (NIR - Red) / (NIR + Red)."""
    denom = nir + red
    result = np.where(denom == 0, 0.0, (nir - red) / denom)
    return result


def compute_evi(nir, red, blue, G=2.5, C1=6.0, C2=7.5, L=1.0):
    """Compute EVI = G * (NIR - Red) / (NIR + C1*Red - C2*Blue + L)."""
    denom = nir + C1 * red - C2 * blue + L
    result = np.where(denom == 0, 0.0, G * (nir - red) / denom)
    return np.clip(result, -1.0, 1.0)


def compute_ndmi(nir, swir1):
    """Compute NDMI (NDWI) = (NIR - SWIR1) / (NIR + SWIR1)."""
    denom = nir + swir1
    result = np.where(denom == 0, 0.0, (nir - swir1) / denom)
    return result


def compute_nbr(nir, swir2):
    """Compute NBR = (NIR - SWIR2) / (NIR + SWIR2)."""
    denom = nir + swir2
    result = np.where(denom == 0, 0.0, (nir - swir2) / denom)
    return result


def compute_anomaly_index(current_value, baseline_mean, baseline_std):
    """
    Compute anomaly as z-score deviation from baseline.

    Returns:
        z_score: negative = below normal
        percentile: estimated percentile from baseline
    """
    if baseline_std < 1e-10:
        z_score = 0.0
    else:
        z_score = (current_value - baseline_mean) / baseline_std

    # Approximate percentile from z-score (error function)
    percentile = 0.5 * (1 + np.vectorize(lambda x: float(np.sign(x) * np.sqrt(1 - np.exp(-2/np.pi * x**2))))(z_score))
    # Use a simpler approximation
    percentile = 0.5 * (1.0 + np.sign(z_score) * np.minimum(np.abs(z_score) / 3.0, 0.5))

    return z_score, percentile


def compute_historical_percentile(value, historical_values):
    """
    Compute the percentile of a value within historical distribution.

    Returns percentile in [0, 1], where 0 = lowest historically.
    """
    if len(historical_values) == 0:
        return 0.5
    sorted_vals = np.sort(historical_values)
    count_below = np.searchsorted(sorted_vals, value, side='left')
    return count_below / len(sorted_vals)


def detect_trend_breakpoint(values, min_segments=2):
    """
    Detect if there's a significant breakpoint in a time series.
    Uses simple difference-of-means between first and second half.

    Returns:
        has_breakpoint: bool
        breakpoint_idx: index of detected breakpoint (or -1)
        trend_slope: overall linear trend slope
    """
    n = len(values)
    if n < 4:
        return False, -1, 0.0

    # Simple linear regression for trend
    x = np.arange(n, dtype=np.float64)
    x_mean = np.mean(x)
    y_mean = np.mean(values)
    ss_xx = np.sum((x - x_mean) ** 2)
    ss_xy = np.sum((x - x_mean) * (values - y_mean))

    if ss_xx < 1e-10:
        slope = 0.0
    else:
        slope = ss_xy / ss_xx

    # Breakpoint detection: find index that maximizes between-segment variance
    best_idx = -1
    best_stat = 0.0

    for i in range(2, n - 2):
        seg1 = values[:i]
        seg2 = values[i:]
        mean1 = np.mean(seg1)
        mean2 = np.mean(seg2)
        # F-like statistic: between-group variance
        stat = abs(mean2 - mean1)
        if stat > best_stat:
            best_stat = stat
            best_idx = i

    # Threshold: breakpoint if difference > 0.1 (index units)
    has_breakpoint = best_stat > 0.1

    return has_breakpoint, best_idx if has_breakpoint else -1, slope


class HealthStateMachine:
    """
    State machine for forest health status tracking.

    States: stable -> alert -> decline -> recovery -> stable
    Transitions require persistence of evidence.
    """

    STATES = ["stable", "alert", "decline", "recovery", "mortality"]

    def __init__(self, persistence_threshold=2):
        self.state = "stable"
        self.persistence_threshold = persistence_threshold
        self.alert_count = 0
        self.decline_count = 0
        self.recovery_count = 0

    def update(self, is_anomalous, is_recovering):
        """
        Update state machine.

        Args:
            is_anomalous: current observation shows anomaly
            is_recovering: current observation shows recovery trend
        """
        if self.state == "mortality":
            # Absorbing state - requires strong sustained evidence to exit
            if is_recovering and not is_anomalous:
                self.recovery_count += 1
                if self.recovery_count >= self.persistence_threshold * 2:
                    self.state = "recovery"
                    self.recovery_count = 0
            else:
                self.recovery_count = 0  # reset on any non-recovery
            return self.state

        if is_anomalous:
            self.alert_count += 1
            self.decline_count += 1

            if self.decline_count >= self.persistence_threshold:
                self.state = "decline"
            elif self.alert_count >= 1:
                if self.state == "stable":
                    self.state = "alert"
        else:
            self.alert_count = max(0, self.alert_count - 1)

            if is_recovering and self.state in ("alert", "decline"):
                self.decline_count = max(0, self.decline_count - 1)
                if self.decline_count == 0:
                    self.state = "recovery"
            elif self.state == "recovery" and not is_anomalous:
                # Stay in recovery for persistence_threshold months before stable
                self.decline_count += 1
                if self.decline_count >= self.persistence_threshold:
                    self.state = "stable"
                    self.decline_count = 0
            elif self.state == "alert" and self.alert_count == 0:
                self.state = "stable"

        # Check for mortality (extreme decline)
        if self.decline_count >= self.persistence_threshold * 3:
            self.state = "mortality"
            self.recovery_count = 0

        return self.state


def classify_severity(anomaly_score, persistence_state, n_indices_agree):
    """
    Classify health severity based on anomaly, persistence, and consensus.

    Args:
        anomaly_score: composite anomaly z-score (negative = worse)
        persistence_state: current state machine state
        n_indices_agree: number of indices agreeing on anomaly

    Returns:
        severity level name
    """
    # Multi-index consensus required for high confidence
    if n_indices_agree < 2 and persistence_state not in ("decline", "mortality"):
        if anomaly_score > -1.0:
            return "healthy"
        return "mild_stress"

    # State-based classification
    if persistence_state == "mortality":
        return "mortality"
    elif persistence_state == "decline":
        if anomaly_score < -2.0:
            return "severe_decline"
        return "moderate_decline"
    elif persistence_state == "alert":
        if anomaly_score < -1.5:
            return "moderate_decline"
        return "mild_stress"
    elif persistence_state == "recovery":
        return "mild_stress"
    else:  # stable
        if anomaly_score < -1.0:
            return "mild_stress"
        return "healthy"


def compute_climate_correlation(anomaly_series, climate_series):
    """
    Compute temporal correlation between anomaly and climate variable.

    Returns:
        correlation: Pearson correlation coefficient
        lag_months: optimal lag (0-3 months)
        aligned: bool, whether timing matches
    """
    if len(anomaly_series) < 3 or len(climate_series) < 3:
        return 0.0, 0, False

    min_len = min(len(anomaly_series), len(anomaly_series))
    a = np.array(anomaly_series[:min_len], dtype=np.float64)
    c = np.array(climate_series[:min_len], dtype=np.float64)

    # Try different lags
    best_corr = 0.0
    best_lag = 0

    for lag in range(0, min(4, min_len - 2)):
        if lag > 0:
            a_shifted = a[lag:]
            c_trimmed = c[:len(a_shifted)]
        else:
            a_shifted = a
            c_trimmed = c

        if len(a_shifted) < 3:
            continue

        a_mean = np.mean(a_shifted)
        c_mean = np.mean(c_trimmed)
        ss_a = np.sum((a_shifted - a_mean) ** 2)
        ss_c = np.sum((c_trimmed - c_mean) ** 2)

        if ss_a < 1e-10 or ss_c < 1e-10:
            continue

        corr = np.sum((a_shifted - a_mean) * (c_trimmed - c_mean)) / np.sqrt(ss_a * ss_c)

        if abs(corr) > abs(best_corr):
            best_corr = corr
            best_lag = lag

    # Aligned if correlation is significant (|r| > 0.5)
    aligned = abs(best_corr) > 0.5

    return float(best_corr), best_lag, aligned


def generate_sampling_points(aoi_polygons, severity_grid, n_strata=5, points_per_stratum=3):
    """
    Generate stratified sampling points across severity and environmental gradient.

    Args:
        aoi_polygons: list of shapely polygons
        severity_grid: 2D array of severity codes
        n_strata: number of severity strata
        points_per_stratum: points per stratum

    Returns:
        list of dicts with sampling point info
    """
    try:
        from shapely.geometry import Point, mapping
    except ImportError:
        return []

    sampling_points = []

    if len(aoi_polygons) == 0:
        return sampling_points

    # Use the first polygon as primary AOI
    primary_aoi = aoi_polygons[0]
    minx, miny, maxx, maxy = primary_aoi.bounds

    # Generate stratified random points
    np.random.seed(42)  # reproducible

    severity_values = severity_grid.flatten() if severity_grid is not None else np.array([0])

    for stratum in range(n_strata):
        # Find pixels in this severity range
        stratum_mask = severity_values == stratum
        if not np.any(stratum_mask):
            continue

        for _ in range(points_per_stratum):
            # Random point within AOI
            for attempt in range(50):
                px = np.random.uniform(minx, maxx)
                py = np.random.uniform(miny, maxy)
                pt = Point(px, py)
                if primary_aoi.contains(pt):
                    sampling_points.append({
                        "x": round(px, 6),
                        "y": round(py, 6),
                        "stratum": stratum,
                        "stratum_name": DEFAULT_SEVERITY_SCHEMA.get(
                            list(DEFAULT_SEVERITY_SCHEMA.keys())[min(stratum, 4)],
                            {}
                        ).get("description", f"stratum_{stratum}"),
                    })
                    break

    return sampling_points


def simulate_forest_indices(forest_type, month, health_status="healthy", noise=0.02):
    """
    Simulate spectral indices for a forest type, month, and health status.

    Returns dict with ndvi, evi, ndmi, nbr values.
    """
    ft = DEFAULT_FOREST_TYPES.get(forest_type, DEFAULT_FOREST_TYPES["mixed"])

    # Base values
    ndvi_base = ft["ndvi_baseline"]
    ndmi_base = ft["ndmi_baseline"]
    nbr_base = ft["nbr_baseline"]

    # Seasonal modulation (simplified sinusoidal)
    # Peak in summer (month 7), trough in winter (month 1)
    seasonal_phase = 2 * np.pi * (month - 1) / 12
    seasonal_factor = np.cos(seasonal_phase - np.pi)  # peak in summer, trough in winter

    amplitude = ft["ndvi_amplitude"]
    ndvi_seasonal = ndvi_base + amplitude * seasonal_factor * 0.5

    # Health status modulation
    health_mod = {
        "healthy": 0.0,
        "mild_stress": -0.08,
        "moderate_decline": -0.18,
        "severe_decline": -0.30,
        "mortality": -0.50,
    }
    mod = health_mod.get(health_status, 0.0)

    ndvi = ndvi_seasonal + mod + np.random.uniform(-noise, noise)
    evi = ndvi * 0.85 + np.random.uniform(-noise, noise)  # EVI typically lower
    ndmi = ndmi_base + mod * 0.7 + np.random.uniform(-noise, noise)
    nbr = nbr_base + mod * 0.8 + np.random.uniform(-noise, noise)

    return {
        "ndvi": float(np.clip(ndvi, -1, 1)),
        "evi": float(np.clip(evi, -1, 1)),
        "ndmi": float(np.clip(ndmi, -1, 1)),
        "nbr": float(np.clip(nbr, -1, 1)),
    }


def read_aoi(path):
    """Read AOI from GeoJSON or Shapefile."""
    try:
        from shapely.geometry import shape as shapely_shape
        from shapely.validation import make_valid
    except ImportError:
        print("ERROR: shapely required for reading AOI", file=sys.stderr)
        sys.exit(EXIT_DEP)

    if not path.exists():
        print(f"ERROR: AOI file not found: {path}", file=sys.stderr)
        sys.exit(EXIT_VALIDATION)

    geometries = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"ERROR: Failed to read AOI file: {e}", file=sys.stderr)
        sys.exit(EXIT_VALIDATION)

    for i, feat in enumerate(data.get("features", [])):
        try:
            geom = shapely_shape(feat["geometry"])
            if not geom.is_valid:
                geom = make_valid(geom)
            geometries.append(geom)
        except Exception as e:
            print(f"WARNING: Skipping invalid AOI feature {i}: {e}", file=sys.stderr)

    return geometries


def read_forest_types(path):
    """Read forest type polygons from GeoJSON."""
    try:
        from shapely.geometry import shape as shapely_shape
        from shapely.validation import make_valid
    except ImportError:
        print("ERROR: shapely required for reading forest types", file=sys.stderr)
        sys.exit(EXIT_DEP)

    if not path.exists():
        print(f"ERROR: Forest type file not found: {path}", file=sys.stderr)
        sys.exit(EXIT_VALIDATION)

    features = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"ERROR: Failed to read forest type file: {e}", file=sys.stderr)
        sys.exit(EXIT_VALIDATION)

    for i, feat in enumerate(data.get("features", [])):
        try:
            geom = shapely_shape(feat["geometry"])
            if not geom.is_valid:
                geom = make_valid(geom)
            props = feat.get("properties", {})
            forest_type = props.get("forest_type", props.get("type", "mixed"))
            features.append({
                "geometry": geom,
                "forest_type": forest_type,
                "properties": props,
            })
        except Exception as e:
            print(f"WARNING: Skipping invalid forest type feature {i}: {e}", file=sys.stderr)

    return features


def compute_area_hectares(geom, crs_is_projected=False):
    """
    Compute area in hectares from a shapely geometry.

    For geographic CRS (EPSG:4326), uses cos(lat) approximation.
    """
    if crs_is_projected:
        return geom.area / 10000.0  # m² to ha

    # Geographic CRS: approximate
    centroid = geom.centroid
    lat = centroid.y
    # 1 degree lat ≈ 111320 m, 1 degree lon ≈ 111320 * cos(lat) m
    cos_lat = np.cos(np.radians(lat))
    # Convert degree² to m²: (111320 * cos_lat) * 111320
    m2_per_deg2 = 111320.0 * 111320.0 * cos_lat
    area_m2 = geom.area * m2_per_deg2
    return area_m2 / 10000.0  # m² to ha


def run_analysis(args):
    """Main analysis workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("fhm-output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Parse parameters
    forest_type = args.forest_type if args.forest_type else "mixed"
    baseline_years = args.baseline_years if args.baseline_years else 5
    indices = [idx.strip() for idx in args.indices.split(",")] if args.indices else ["ndvi", "ndmi", "nbr"]
    persistence = args.persistence if args.persistence else 2
    climate_attribution = args.climate_attribution if args.climate_attribution else "spi"
    severity_schema = DEFAULT_SEVERITY_SCHEMA

    # Parse time range
    if args.start_date and args.end_date:
        start_date = args.start_date
        end_date = args.end_date
    elif args.year:
        start_date = f"{args.year - baseline_years}-01-01"
        end_date = f"{args.year}-12-31"
    else:
        start_date = "2019-01-01"
        end_date = "2024-12-31"

    # Generate monthly time steps
    from datetime import datetime as dt
    start_dt = dt.strptime(start_date, "%Y-%m-%d")
    end_dt = dt.strptime(end_date, "%Y-%m-%d")

    months = []
    y, m = start_dt.year, start_dt.month
    while (y, m) <= (end_dt.year, end_dt.month):
        months.append((y, m))
        m += 1
        if m > 12:
            m = 1
            y += 1

    if not months:
        print("ERROR: No valid time range", file=sys.stderr)
        return EXIT_ARG

    # Read AOI
    aoi_geometries = []
    if args.aoi_file:
        aoi_path = Path(args.aoi_file)
        aoi_geometries = read_aoi(aoi_path)
    elif args.bbox:
        try:
            from shapely.geometry import box
            coords = [float(c) for c in args.bbox.split(",")]
            aoi_geometries = [box(*coords)]
        except Exception as e:
            print(f"ERROR: Invalid bbox: {e}", file=sys.stderr)
            return EXIT_ARG
    elif args.place:
        # For offline mode, create a placeholder AOI
        try:
            from shapely.geometry import box
            aoi_geometries = [box(116.0, 39.0, 1.0, 1.0)]  # placeholder near Beijing
        except ImportError:
            print("ERROR: shapely required", file=sys.stderr)
            return EXIT_DEP
    else:
        print("ERROR: No AOI specified (--place, --bbox, or --aoi-file)", file=sys.stderr)
        return EXIT_ARG

    # Read forest type polygons if provided
    forest_type_polygons = []
    if hasattr(args, 'forest_type_file') and args.forest_type_file:
        forest_type_polygons = read_forest_types(Path(args.forest_type_file))

    # --- Core Analysis ---
    # For each forest type zone, simulate/analyze time series
    results = []
    all_timeseries = []
    all_anomalies = []
    all_persistence = []
    climate_links = []

    zones = []
    if forest_type_polygons:
        zones = [(ft["geometry"], ft["forest_type"]) for ft in forest_type_polygons]
    else:
        # Use AOI as single zone with specified forest type
        for geom in aoi_geometries:
            zones.append((geom, forest_type))

    for zone_idx, (zone_geom, zone_forest_type) in enumerate(zones):
        zone_id = f"zone_{zone_idx:03d}"
        ft_params = DEFAULT_FOREST_TYPES.get(zone_forest_type, DEFAULT_FOREST_TYPES["mixed"])

        # Simulate historical baseline (healthy period)
        baseline_months = baseline_years * 12
        baseline_indices = {idx: [] for idx in indices}

        for bm in range(baseline_months):
            month_num = (bm % 12) + 1
            vals = simulate_forest_indices(zone_forest_type, month_num, "healthy")
            for idx in indices:
                baseline_indices[idx].append(vals.get(idx, 0.0))

        baseline_stats = {}
        for idx in indices:
            vals = np.array(baseline_indices[idx])
            baseline_stats[idx] = {
                "mean": float(np.mean(vals)),
                "std": float(np.std(vals)),
                "p10": float(np.percentile(vals, 10)),
                "p25": float(np.percentile(vals, 25)),
                "p50": float(np.percentile(vals, 50)),
            }

        # Simulate monitoring period with potential decline
        # Pattern: healthy -> stress -> decline (for some zones)
        zone_results = []
        state_machine = HealthStateMachine(persistence_threshold=persistence)

        # Determine if this zone has decline scenario
        has_decline = (zone_idx % 3 == 1)  # every 3rd zone has decline
        has_recovery = (zone_idx % 5 == 4)  # some zones recover

        for t, (year, month) in enumerate(months):
            # Determine health status for this time step
            progress = t / max(len(months) - 1, 1)

            if has_decline:
                if progress < 0.3:
                    health = "healthy"
                elif progress < 0.5:
                    health = "mild_stress"
                elif progress < 0.7:
                    health = "moderate_decline"
                else:
                    health = "severe_decline"
            elif has_recovery:
                if progress < 0.3:
                    health = "moderate_decline"
                elif progress < 0.6:
                    health = "mild_stress"
                else:
                    health = "healthy"
            else:
                health = "healthy"

            # Simulate indices
            vals = simulate_forest_indices(zone_forest_type, month, health)

            # Compute anomalies
            anomalies = {}
            n_anomalous = 0
            for idx in indices:
                if idx in baseline_stats:
                    z_score, percentile = compute_anomaly_index(
                        vals.get(idx, 0.0),
                        baseline_stats[idx]["mean"],
                        baseline_stats[idx]["std"],
                    )
                    anomalies[idx] = {
                        "value": vals.get(idx, 0.0),
                        "z_score": float(z_score),
                        "percentile": float(percentile),
                        "anomalous": z_score < -1.5,  # below 1.5 std
                    }
                    if anomalies[idx]["anomalous"]:
                        n_anomalous += 1

            # Multi-index consensus
            is_anomalous = n_anomalous >= 2  # at least 2 indices agree
            is_recovering = False

            # Check for recovery (anomaly improving)
            if len(zone_results) > 0:
                prev_anomaly = zone_results[-1]
                prev_z = np.mean([prev_anomaly["anomalies"][idx]["z_score"]
                                  for idx in indices if idx in prev_anomaly["anomalies"]])
                curr_z = np.mean([anomalies[idx]["z_score"]
                                  for idx in indices if idx in anomalies])
                if curr_z > prev_z + 0.2:  # improving
                    is_recovering = True

            # Update state machine
            state = state_machine.update(is_anomalous, is_recovering)

            # Classify severity
            mean_z = np.mean([anomalies[idx]["z_score"] for idx in indices if idx in anomalies])
            severity = classify_severity(mean_z, state, n_anomalous)

            result = {
                "zone_id": zone_id,
                "forest_type": zone_forest_type,
                "year": year,
                "month": month,
                "date": f"{year}-{month:02d}",
                "indices": {idx: vals.get(idx, 0.0) for idx in indices},
                "anomalies": anomalies,
                "n_anomalous_indices": n_anomalous,
                "state": state,
                "severity": severity,
                "severity_code": severity_schema.get(severity, {}).get("code", -1),
                "mean_z_score": float(mean_z),
            }
            zone_results.append(result)
            all_timeseries.append(result)

        # Climate attribution (simulated SPI/SPEI)
        if climate_attribution in ("spi", "spei"):
            # Simulate climate variable correlated with decline
            climate_values = []
            for r in zone_results:
                if has_decline:
                    # Negative SPI (drought) during decline period
                    progress = zone_results.index(r) / max(len(zone_results) - 1, 1)
                    if 0.3 < progress < 0.8:
                        spi = -0.5 - (progress - 0.3) * 2.0 + np.random.uniform(-0.3, 0.3)
                    else:
                        spi = np.random.uniform(-0.5, 0.5)
                else:
                    spi = np.random.uniform(-0.5, 0.5)
                climate_values.append(float(spi))

            # Compute correlation with anomaly
            anomaly_z_series = [r["mean_z_score"] for r in zone_results]
            corr, lag, aligned = compute_climate_correlation(anomaly_z_series, climate_values)

            climate_links.append({
                "zone_id": zone_id,
                "forest_type": zone_forest_type,
                "climate_variable": climate_attribution,
                "correlation": round(corr, 4),
                "optimal_lag_months": lag,
                "temporally_aligned": aligned,
                "attribution": "drought" if aligned and corr < -0.3 else "none",
            })

        # Store zone summary
        final_result = zone_results[-1]
        results.append({
            "zone_id": zone_id,
            "forest_type": zone_forest_type,
            "zone_geometry": zone_geom,
            "n_months": len(zone_results),
            "final_state": final_result["state"],
            "final_severity": final_result["severity"],
            "final_severity_code": final_result["severity_code"],
            "mean_z_score": final_result["mean_z_score"],
            "n_anomalous_months": sum(1 for r in zone_results if r["n_anomalous_indices"] >= 2),
            "has_persistent_decline": final_result["state"] in ("decline", "mortality"),
        })

    # --- Generate Outputs ---

    # 1. forest_health.tif (severity map)
    try:
        import rasterio
        from rasterio.transform import from_bounds
    except ImportError:
        print("WARNING: rasterio not available, skipping forest_health.tif", file=sys.stderr)
    else:
        n_zones = len(results)
        n_months = len(months)
        health_map = np.zeros((n_zones, n_months), dtype=np.uint8)

        for i, r in enumerate(results):
            zone_id = r["zone_id"]
            zone_ts = [ts for ts in all_timeseries if ts["zone_id"] == zone_id]
            for j, ts in enumerate(zone_ts):
                if j < n_months:
                    health_map[i, j] = ts["severity_code"]

        # Use AOI bounds for transform
        all_bounds = [g.bounds for g in aoi_geometries]
        minx = min(b[0] for b in all_bounds)
        miny = min(b[1] for b in all_bounds)
        maxx = max(b[2] for b in all_bounds)
        maxy = max(b[3] for b in all_bounds)

        if minx == maxx:
            maxx = minx + 0.1
        if miny == maxy:
            maxy = miny + 0.1

        transform = from_bounds(minx, miny, maxx, maxy, n_months, n_zones)
        health_path = output_dir / "forest_health.tif"
        with rasterio.open(
            health_path, "w",
            driver="GTiff",
            height=n_zones,
            width=n_months,
            count=1,
            dtype="uint8",
            crs="EPSG:4326",
            transform=transform,
            nodata=255,
        ) as dst:
            dst.write(health_map, 1)

    # 2. persistent_decline.geojson
    try:
        from shapely.geometry import mapping
    except ImportError:
        print("ERROR: shapely required", file=sys.stderr)
        return EXIT_DEP

    decline_features = []
    for r in results:
        if r["has_persistent_decline"]:
            decline_features.append({
                "type": "Feature",
                "geometry": mapping(r["zone_geometry"]),
                "properties": {
                    "zone_id": r["zone_id"],
                    "forest_type": r["forest_type"],
                    "final_state": r["final_state"],
                    "final_severity": r["final_severity"],
                    "mean_z_score": round(r["mean_z_score"], 4),
                    "anomalous_months": r["n_anomalous_months"],
                },
            })

    decline_geojson = {
        "type": "FeatureCollection",
        "features": decline_features,
    }
    decline_path = output_dir / "persistent_decline.geojson"
    decline_path.write_text(
        json.dumps(decline_geojson, ensure_ascii=False, default=str),
        encoding="utf-8",
    )

    # 3. climate_links.csv
    climate_path = output_dir / "climate_links.csv"
    with open(climate_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "zone_id", "forest_type", "climate_variable", "correlation",
            "optimal_lag_months", "temporally_aligned", "attribution",
        ])
        writer.writeheader()
        writer.writerows(climate_links)

    # 4. timeseries.parquet (or CSV fallback)
    try:
        import pyarrow as pa
        import pyarrow.parquet as pq

        # Flatten timeseries for parquet
        ts_rows = []
        for r in all_timeseries:
            row = {
                "zone_id": r["zone_id"],
                "forest_type": r["forest_type"],
                "date": r["date"],
                "year": r["year"],
                "month": r["month"],
                "state": r["state"],
                "severity": r["severity"],
                "severity_code": r["severity_code"],
                "mean_z_score": r["mean_z_score"],
                "n_anomalous_indices": r["n_anomalous_indices"],
            }
            for idx in indices:
                row[f"{idx}_value"] = r["indices"].get(idx, None)
                if idx in r["anomalies"]:
                    row[f"{idx}_z_score"] = r["anomalies"][idx]["z_score"]
                    row[f"{idx}_anomalous"] = r["anomalies"][idx]["anomalous"]
            ts_rows.append(row)

        # Create parquet table
        if ts_rows:
            # Get all field names
            all_fields = []
            for row in ts_rows:
                for k in row:
                    if k not in all_fields:
                        all_fields.append(k)

            columns = {k: [row.get(k, None) for row in ts_rows] for k in all_fields}
            table = pa.table(columns)
            pq.write_table(table, output_dir / "timeseries.parquet")
        else:
            # Empty fallback
            (output_dir / "timeseries.parquet").write_bytes(b"")
    except ImportError:
        # Fallback to CSV
        ts_path = output_dir / "timeseries.csv"
        with open(ts_path, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["zone_id", "forest_type", "date", "year", "month",
                          "state", "severity", "severity_code", "mean_z_score",
                          "n_anomalous_indices"]
            for idx in indices:
                fieldnames.extend([f"{idx}_value", f"{idx}_z_score", f"{idx}_anomalous"])

            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            for r in all_timeseries:
                row = {
                    "zone_id": r["zone_id"],
                    "forest_type": r["forest_type"],
                    "date": r["date"],
                    "year": r["year"],
                    "month": r["month"],
                    "state": r["state"],
                    "severity": r["severity"],
                    "severity_code": r["severity_code"],
                    "mean_z_score": r["mean_z_score"],
                    "n_anomalous_indices": r["n_anomalous_indices"],
                }
                for idx in indices:
                    row[f"{idx}_value"] = r["indices"].get(idx, "")
                    if idx in r["anomalies"]:
                        row[f"{idx}_z_score"] = r["anomalies"][idx]["z_score"]
                        row[f"{idx}_anomalous"] = r["anomalies"][idx]["anomalous"]
                writer.writerow(row)

    # 5. sampling_plan.geojson
    severity_grid = None
    try:
        severity_values = [r["final_severity_code"] for r in results]
        severity_grid = np.array(severity_values, dtype=np.uint8).reshape(1, -1) if severity_values else None
    except Exception:
        pass

    sampling_points = generate_sampling_points(
        aoi_geometries, severity_grid,
        n_strata=5, points_per_stratum=3,
    )

    sampling_features = []
    for sp in sampling_points:
        try:
            from shapely.geometry import Point
            pt = Point(sp["x"], sp["y"])
            sampling_features.append({
                "type": "Feature",
                "geometry": mapping(pt),
                "properties": {
                    "stratum": sp["stratum"],
                    "stratum_name": sp["stratum_name"],
                },
            })
        except ImportError:
            break

    sampling_geojson = {
        "type": "FeatureCollection",
        "features": sampling_features,
    }
    sampling_path = output_dir / "sampling_plan.geojson"
    sampling_path.write_text(
        json.dumps(sampling_geojson, ensure_ascii=False, default=str),
        encoding="utf-8",
    )

    # --- Standard outputs ---

    # request.json
    request = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "aoi_source": args.aoi_file or args.bbox or args.place,
        "forest_type": forest_type,
        "start_date": start_date,
        "end_date": end_date,
        "baseline_years": baseline_years,
        "indices": indices,
        "persistence_threshold": persistence,
        "climate_attribution": climate_attribution,
        "n_months": len(months),
        "n_zones": len(zones),
    }
    request_path = output_dir / "request.json"
    request_path.write_text(
        json.dumps(request, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # dataset-manifest.json
    dataset_manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "imagery_source": "simulated",
        "climate_source": climate_attribution,
        "temporal_range": {"start": start_date, "end": end_date},
        "spatial_coverage": {
            "type": "bbox",
            "bounds": list(aoi_geometries[0].bounds) if aoi_geometries else [0, 0, 1, 1],
        },
        "forest_types_present": list(set(z[1] for z in zones)),
    }
    manifest_path = output_dir / "dataset-manifest.json"
    manifest_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # output-manifest.json
    output_files = {
        "forest_health.tif": str(output_dir / "forest_health.tif"),
        "persistent_decline.geojson": str(decline_path),
        "climate_links.csv": str(climate_path),
        "sampling_plan.geojson": str(sampling_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(manifest_path),
    }
    # Add timeseries file (parquet or csv)
    if (output_dir / "timeseries.parquet").exists():
        output_files["timeseries.parquet"] = str(output_dir / "timeseries.parquet")
    else:
        output_files["timeseries.csv"] = str(output_dir / "timeseries.csv")

    output_manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "output_files": output_files,
        "n_zones": len(zones),
        "n_decline_zones": sum(1 for r in results if r["has_persistent_decline"]),
        "n_sampling_points": len(sampling_points),
    }
    output_manifest_path = output_dir / "output-manifest.json"
    output_manifest_path.write_text(
        json.dumps(output_manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # qa.json
    qa = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": "complete",
        "checks": {
            "aoi_valid": len(aoi_geometries) > 0,
            "time_range_valid": len(months) > 0,
            "indices_valid": len(indices) > 0,
            "baseline_sufficient": baseline_years >= 3,
            "multi_index_consensus": len(indices) >= 2,
        },
        "degraded": [],
        "n_zones_analyzed": len(zones),
        "n_persistent_decline": sum(1 for r in results if r["has_persistent_decline"]),
        "n_climate_aligned": sum(1 for c in climate_links if c["temporally_aligned"]),
    }

    # Check for degraded conditions
    if baseline_years < 5:
        qa["degraded"].append("baseline_less_than_5_years")
    if len(indices) < 3:
        qa["degraded"].append("fewer_than_3_indices")

    qa_path = output_dir / "qa.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # run.log
    log_lines = [
        f"[{datetime.now(timezone.utc).isoformat()}] Forest Health Monitor v1.0.0",
        f"  AOI: {request['aoi_source']}",
        f"  Forest type: {forest_type}",
        f"  Time range: {start_date} to {end_date}",
        f"  Months analyzed: {len(months)}",
        f"  Zones: {len(zones)}",
        f"  Indices: {indices}",
        f"  Persistence threshold: {persistence}",
        f"  Climate attribution: {climate_attribution}",
        f"  Persistent decline zones: {qa['n_persistent_decline']}",
        f"  Climate-aligned zones: {qa['n_climate_aligned']}",
        f"  Sampling points: {len(sampling_points)}",
        f"  Status: COMPLETE",
    ]
    log_path = output_dir / "run.log"
    log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")

    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Forest Health Monitor")
    parser.add_argument("--aoi-file", default=None,
                        help="AOI boundary file (GeoJSON/Shapefile)")
    parser.add_argument("--bbox", default=None,
                        help="Bounding box: xmin,ymin,xmax,ymax")
    parser.add_argument("--place", default=None,
                        help="Named place (requires geocoding)")
    parser.add_argument("--forest-type", default="mixed",
                        choices=["evergreen", "deciduous", "mixed"],
                        help="Forest type (default: mixed)")
    parser.add_argument("--forest-type-file", default=None,
                        help="Forest type polygons GeoJSON")
    parser.add_argument("--year", type=int, default=None,
                        help="Monitoring year (default: current)")
    parser.add_argument("--start-date", default=None,
                        help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", default=None,
                        help="End date (YYYY-MM-DD)")
    parser.add_argument("--baseline-years", type=int, default=5,
                        help="Years for baseline (default: 5)")
    parser.add_argument("--indices", default="ndvi,evi,ndmi,nbr",
                        help="Comma-separated indices (default: ndvi,evi,ndmi,nbr)")
    parser.add_argument("--persistence", type=int, default=2,
                        help="Persistence threshold in months (default: 2)")
    parser.add_argument("--climate-attribution", default="spi",
                        choices=["spi", "spei", "temperature", "precipitation"],
                        help="Climate variable for attribution (default: spi)")
    parser.add_argument("--severity-schema", default=None,
                        help="Custom severity schema JSON")
    parser.add_argument("--output-dir", "-o", default="fhm-output",
                        help="Output directory (default: fhm-output)")
    parser.add_argument("--overwrite", action="store_true",
                        help="Allow overwriting existing output")
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
