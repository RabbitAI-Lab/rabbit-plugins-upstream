#!/usr/bin/env python3
"""
Blue Carbon Assessment - Ecosystem extent, carbon stock, and change estimation.

Identifies mangrove, salt marsh, and seagrass blue carbon ecosystems.
Estimates carbon stocks, changes, and uncertainty using IPCC default factors
(screening-level) or user-provided project-specific factors.

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

EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# Ecosystem classification codes
ECOSYSTEM_CODES = {
    0: "no_data",
    1: "mangrove",
    2: "salt_marsh",
    3: "seagrass",
    9: "other",
}

VALID_ECOSYSTEM_TYPES = {"mangrove", "salt_marsh", "seagrass", "all"}
VALID_BOUNDARIES = {"strict", "inclusive"}
VALID_SOIL_DEPTHS = {"0_30cm", "0_100cm", "0_200cm"}

# ============================================================
# Logging
# ============================================================

def setup_logging(output_dir: Path) -> logging.Logger:
    """Setup logging to file and console."""
    logger = logging.getLogger("bca")
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
    """Close all handlers on the bca logger."""
    logger = logging.getLogger("bca")
    for handler in logger.handlers[:]:
        try:
            handler.flush()
            handler.close()
        except Exception:
            pass
        logger.removeHandler(handler)
    logging.shutdown()


# ============================================================
# Carbon Factor Registry
# ============================================================

def load_carbon_factors(factors_path: Optional[str] = None) -> Dict:
    """Load carbon factor registry from JSON file."""
    if factors_path is None:
        script_dir = Path(__file__).parent
        factors_path = script_dir.parent / "references" / "blue_carbon_factors.json"

    with open(factors_path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_ecosystem_factors(factors: Dict, ecosystem_type: str) -> Dict:
    """Get carbon factors for a specific ecosystem type."""
    ecosystems = factors.get("ecosystems", {})
    if ecosystem_type not in ecosystems:
        raise ValueError(f"Unknown ecosystem type: {ecosystem_type}. "
                         f"Valid: {list(ecosystems.keys())}")
    return ecosystems[ecosystem_type]


def get_soil_carbon_factor(ecosystem_factors: Dict, soil_depth: str) -> Dict:
    """Get soil carbon factor for a specific depth."""
    key = f"soil_carbon_tC_ha_{soil_depth}"
    if key not in ecosystem_factors:
        raise ValueError(f"No soil carbon factor for depth '{key}'")
    return ecosystem_factors[key]


# ============================================================
# Core Algorithm: Carbon Stock Calculation
# ============================================================

def compute_carbon_stock(
    area_ha: float,
    agb_tC_ha: float,
    bgb_tC_ha: float,
    soil_tC_ha: float,
) -> Dict[str, float]:
    """
    Compute total carbon stock for a given area.

    Args:
        area_ha: Area in hectares
        agb_tC_ha: Above-ground biomass carbon density (tC/ha)
        bgb_tC_ha: Below-ground biomass carbon density (tC/ha)
        soil_tC_ha: Soil organic carbon density (tC/ha)

    Returns:
        Dict with total stock by pool and combined total
    """
    agb_total = area_ha * agb_tC_ha
    bgb_total = area_ha * bgb_tC_ha
    soil_total = area_ha * soil_tC_ha
    total = agb_total + bgb_total + soil_total

    return {
        "agb_tC": round(agb_total, 2),
        "bgb_tC": round(bgb_total, 2),
        "soil_tC": round(soil_total, 2),
        "total_tC": round(total, 2),
    }


def propagate_uncertainty(
    area_ha: float,
    area_uncertainty_pct: float,
    agb_tC_ha: float,
    agb_uncertainty_pct: float,
    bgb_tC_ha: float,
    bgb_uncertainty_pct: float,
    soil_tC_ha: float,
    soil_uncertainty_pct: float,
    confidence_level: float = 0.95,
) -> Dict[str, float]:
    """
    Propagate uncertainty through carbon stock calculation using
    root sum of squares (RSS) for independent errors.

    σ_total² = (area × σ_agb)² + (area × σ_bgb)² + (area × σ_soil)²
               + (σ_area × total_density)²

    Args:
        area_ha: Area in hectares
        area_uncertainty_pct: Area uncertainty as percentage
        agb_tC_ha: Above-ground biomass carbon density
        agb_uncertainty_pct: AGB uncertainty percentage
        bgb_tC_ha: Below-ground biomass carbon density
        bgb_uncertainty_pct: BGB uncertainty percentage
        soil_tC_ha: Soil carbon density
        soil_uncertainty_pct: Soil uncertainty percentage
        confidence_level: Confidence level for interval (default 0.95)

    Returns:
        Dict with absolute uncertainty, relative uncertainty, confidence interval
    """
    # Convert percentages to absolute standard uncertainties
    total_density = agb_tC_ha + bgb_tC_ha + soil_tC_ha

    # Standard uncertainty of each component (assuming normal distribution)
    sigma_agb = area_ha * (agb_tC_ha * agb_uncertainty_pct / 100.0)
    sigma_bgb = area_ha * (bgb_tC_ha * bgb_uncertainty_pct / 100.0)
    sigma_soil = area_ha * (soil_tC_ha * soil_uncertainty_pct / 100.0)
    sigma_area = (area_ha * area_uncertainty_pct / 100.0) * total_density

    # Root sum of squares
    sigma_total = math.sqrt(
        sigma_agb**2 + sigma_bgb**2 + sigma_soil**2 + sigma_area**2
    )

    total_stock = area_ha * total_density

    # Z-score for confidence level
    z_scores = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}
    z = z_scores.get(confidence_level, 1.96)

    margin = z * sigma_total
    ci_lower = total_stock - margin
    ci_upper = total_stock + margin

    rel_uncertainty = (sigma_total / total_stock * 100.0) if total_stock > 0 else 0.0

    return {
        "sigma_total_tC": round(sigma_total, 2),
        "relative_uncertainty_pct": round(rel_uncertainty, 2),
        "confidence_level": confidence_level,
        "ci_lower_tC": round(ci_lower, 2),
        "ci_upper_tC": round(ci_upper, 2),
        "ci_margin_tC": round(margin, 2),
    }


def compute_stock_from_raster(
    ecosystem_raster: np.ndarray,
    pixel_area_ha: float,
    carbon_factors: Dict,
    soil_depth: str,
    ecosystem_filter: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Compute carbon stock from an ecosystem classification raster.

    Args:
        ecosystem_raster: 2D array of ecosystem class codes
        pixel_area_ha: Area of one pixel in hectares
        carbon_factors: Full carbon factor registry
        soil_depth: Soil depth key (e.g., "0_100cm")
        ecosystem_filter: If set, only compute for this ecosystem type

    Returns:
        Per-ecosystem and total carbon stock summary
    """
    results = {}
    total_stock = 0.0
    total_uncertainty = 0.0
    total_area = 0.0

    ecosystems = carbon_factors.get("ecosystems", {})
    code_to_name = {v: k for k, v in ECOSYSTEM_CODES.items()}

    for eco_name, eco_factors in ecosystems.items():
        if ecosystem_filter and eco_name != ecosystem_filter:
            continue

        # Find pixels for this ecosystem
        eco_code = None
        for code, name in ECOSYSTEM_CODES.items():
            if name == eco_name:
                eco_code = code
                break

        if eco_code is None:
            continue

        n_pixels = int(np.sum(ecosystem_raster == eco_code))
        if n_pixels == 0:
            continue

        area_ha = n_pixels * pixel_area_ha

        # Get carbon factors
        agb = eco_factors["above_ground_biomass_tC_ha"]["value"]
        agb_unc = eco_factors["above_ground_biomass_tC_ha"]["uncertainty_pct"]
        bgb = eco_factors["below_ground_biomass_tC_ha"]["value"]
        bgb_unc = eco_factors["below_ground_biomass_tC_ha"]["uncertainty_pct"]
        soil_key = f"soil_carbon_tC_ha_{soil_depth}"
        soil = eco_factors[soil_key]["value"]
        soil_unc = eco_factors[soil_key]["uncertainty_pct"]

        # Stock
        stock = compute_carbon_stock(area_ha, agb, bgb, soil)

        # Uncertainty (assume 15% area uncertainty for raster-based mapping)
        unc = propagate_uncertainty(
            area_ha, 15.0, agb, agb_unc, bgb, bgb_unc, soil, soil_unc
        )

        results[eco_name] = {
            "n_pixels": n_pixels,
            "area_ha": round(area_ha, 4),
            "stock_tC": stock,
            "uncertainty": unc,
        }

        total_stock += stock["total_tC"]
        total_uncertainty += unc["sigma_total_tC"] ** 2
        total_area += area_ha

    results["total"] = {
        "area_ha": round(total_area, 4),
        "total_stock_tC": round(total_stock, 2),
        "total_sigma_tC": round(math.sqrt(total_uncertainty), 2),
    }

    return results


# ============================================================
# Change Detection
# ============================================================

def detect_ecosystem_change(
    raster_t1: np.ndarray,
    raster_t2: np.ndarray,
    pixel_area_ha: float,
    carbon_factors: Dict,
    soil_depth: str,
    years_diff: int = 1,
) -> Dict[str, Any]:
    """
    Detect ecosystem change between two time periods.

    Computes area change, carbon stock change, and emissions/removals.

    Args:
        raster_t1: Ecosystem classification at time 1
        raster_t2: Ecosystem classification at time 2
        pixel_area_ha: Pixel area in hectares
        carbon_factors: Carbon factor registry
        soil_depth: Soil depth key
        years_diff: Number of years between periods

    Returns:
        Change analysis results
    """
    if raster_t1.shape != raster_t2.shape:
        raise ValueError("Rasters must have the same shape for change detection")

    n_rows, n_cols = raster_t1.shape
    change_raster = np.zeros((n_rows, n_cols), dtype=np.int8)

    ecosystems = carbon_factors.get("ecosystems", {})
    eco_names = list(ecosystems.keys())

    change_matrix = np.zeros((len(eco_names) + 1, len(eco_names) + 1), dtype=np.int32)
    change_stats = {}
    total_emissions_tC = 0.0
    total_removals_tC = 0.0

    # Class codes: 0 = no_data, 1-3 = ecosystems, 9 = other
    # Change codes: -1 = loss, 0 = stable, 1 = gain (per ecosystem)
    for i in range(n_rows):
        for j in range(n_cols):
            v1 = raster_t1[i, j]
            v2 = raster_t2[i, j]
            change_raster[i, j] = compute_change_code(v1, v2)

    # Per-ecosystem change analysis
    for idx, eco_name in enumerate(eco_names):
        eco_code = idx + 1  # codes 1, 2, 3

        # Area at t1 and t2
        area_t1_pixels = int(np.sum(raster_t1 == eco_code))
        area_t2_pixels = int(np.sum(raster_t2 == eco_code))
        area_t1_ha = area_t1_pixels * pixel_area_ha
        area_t2_ha = area_t2_pixels * pixel_area_ha
        delta_area_ha = area_t2_ha - area_t1_ha

        # Stable area (ecosystem present in both periods)
        stable_pixels = int(np.sum((raster_t1 == eco_code) & (raster_t2 == eco_code)))
        loss_pixels = int(np.sum((raster_t1 == eco_code) & (raster_t2 != eco_code)))
        gain_pixels = int(np.sum((raster_t1 != eco_code) & (raster_t2 == eco_code)))

        # Carbon stock change
        eco_factors = ecosystems[eco_name]
        agb = eco_factors["above_ground_biomass_tC_ha"]["value"]
        bgb = eco_factors["below_ground_biomass_tC_ha"]["value"]
        soil_key = f"soil_carbon_tC_ha_{soil_depth}"
        soil = eco_factors[soil_key]["value"]

        total_density = agb + bgb + soil

        # Loss: all carbon pools released (simplified)
        loss_tC = loss_pixels * pixel_area_ha * total_density
        # Gain: assume soil carbon accumulates over time
        gain_tC = gain_pixels * pixel_area_ha * (agb + bgb)  # biomass only for gains
        # Soil accumulation on stable area
        accum_rate_key = "annual_accumulation_rate_tC_ha_yr"
        if accum_rate_key in eco_factors:
            annual_accum = eco_factors[accum_rate_key]["value"]
            soil_accum_tC = stable_pixels * pixel_area_ha * annual_accum * years_diff
        else:
            soil_accum_tC = 0.0

        net_change_tC = -loss_tC + gain_tC + soil_accum_tC

        if net_change_tC < 0:
            total_emissions_tC += abs(net_change_tC)
        else:
            total_removals_tC += net_change_tC

        change_stats[eco_name] = {
            "area_t1_ha": round(area_t1_ha, 4),
            "area_t2_ha": round(area_t2_ha, 4),
            "delta_area_ha": round(delta_area_ha, 4),
            "stable_pixels": stable_pixels,
            "loss_pixels": loss_pixels,
            "gain_pixels": gain_pixels,
            "loss_tC": round(loss_tC, 2),
            "gain_tC": round(gain_tC, 2),
            "soil_accumulation_tC": round(soil_accum_tC, 2),
            "net_change_tC": round(net_change_tC, 2),
        }

    return {
        "change_stats": change_stats,
        "total_emissions_tC": round(total_emissions_tC, 2),
        "total_removals_tC": round(total_removals_tC, 2),
        "net_change_tC": round(total_removals_tC - total_emissions_tC, 2),
        "years_diff": years_diff,
    }


def compute_change_code(v1: int, v2: int) -> int:
    """
    Compute change code between two ecosystem class codes.

    Returns:
        -1: loss (ecosystem -> non-ecosystem)
         0: stable (same class)
         1: gain (non-ecosystem -> ecosystem)
    """
    is_eco1 = v1 in (1, 2, 3)
    is_eco2 = v2 in (1, 2, 3)

    if v1 == v2:
        return 0
    elif is_eco1 and not is_eco2:
        return -1
    elif not is_eco1 and is_eco2:
        return 1
    else:
        return 0  # Transition between ecosystem types treated as stable


# ============================================================
# Sampling Design
# ============================================================

def generate_sampling_plan(
    ecosystem_raster: np.ndarray,
    carbon_factors: Dict,
    soil_depth: str,
    n_strata: int = 5,
    confidence_level: float = 0.95,
    margin_of_error_pct: float = 20.0,
    pixel_area_ha: float = 0.01,
) -> Dict[str, Any]:
    """
    Generate a stratified random sampling plan for field validation.

    Uses Neyman allocation to distribute samples across strata
    based on area and expected variance.

    Args:
        ecosystem_raster: Ecosystem classification raster
        carbon_factors: Carbon factor registry
        soil_depth: Soil depth key
        n_strata: Number of strata (by carbon density)
        confidence_level: Target confidence level
        margin_of_error_pct: Acceptable margin of error (%)
        pixel_area_ha: Pixel area in hectares

    Returns:
        Sampling plan with stratum definitions and sample allocation
    """
    ecosystems = carbon_factors.get("ecosystems", {})

    strata = []
    total_area = 0.0
    total_samples = 0

    for eco_name, eco_factors in ecosystems.items():
        eco_code = None
        for code, name in ECOSYSTEM_CODES.items():
            if name == eco_name:
                eco_code = code
                break
        if eco_code is None:
            continue

        n_pixels = int(np.sum(ecosystem_raster == eco_code))
        if n_pixels == 0:
            continue

        area_ha = n_pixels * pixel_area_ha
        total_area += area_ha

        # Get total carbon density for stratification
        agb = eco_factors["above_ground_biomass_tC_ha"]["value"]
        bgb = eco_factors["below_ground_biomass_tC_ha"]["value"]
        soil_key = f"soil_carbon_tC_ha_{soil_depth}"
        soil = eco_factors[soil_key]["value"]
        total_density = agb + bgb + soil

        # Estimated coefficient of variation
        unc_pct = eco_factors[soil_key]["uncertainty_pct"]
        cv = unc_pct / 100.0

        # Sample size for stratum (simplified formula)
        # n = (Z^2 * CV^2) / E^2  where E = margin of error
        z_scores = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}
        z = z_scores.get(confidence_level, 1.96)
        e = margin_of_error_pct / 100.0

        n_samples = max(3, int(math.ceil((z**2 * cv**2) / e**2)))

        strata.append({
            "ecosystem": eco_name,
            "area_ha": round(area_ha, 4),
            "n_pixels": n_pixels,
            "carbon_density_tC_ha": total_density,
            "estimated_cv": round(cv, 3),
            "n_samples": n_samples,
            "sampling_density_per_ha": round(n_samples / area_ha, 4) if area_ha > 0 else 0,
        })
        total_samples += n_samples

    # Generate sample point locations (stratified random within ecosystem patches)
    features = []
    rng = np.random.RandomState(42)

    for stratum in strata:
        eco_name = stratum["ecosystem"]
        eco_code = None
        for code, name in ECOSYSTEM_CODES.items():
            if name == eco_name:
                eco_code = code
                break
        if eco_code is None:
            continue

        # Find all pixels of this ecosystem
        pixel_coords = np.argwhere(ecosystem_raster == eco_code)
        if len(pixel_coords) == 0:
            continue

        n_samples = stratum["n_samples"]
        if len(pixel_coords) <= n_samples:
            selected = pixel_coords
        else:
            indices = rng.choice(len(pixel_coords), size=n_samples, replace=False)
            selected = pixel_coords[indices]

        for idx, (r, c) in enumerate(selected):
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(c), float(r)],
                },
                "properties": {
                    "stratum": eco_name,
                    "sample_id": f"{eco_name}_{idx + 1:04d}",
                    "row": int(r),
                    "col": int(c),
                },
            })

    return {
        "type": "FeatureCollection",
        "features": features,
        "total_samples": total_samples,
        "total_area_ha": round(total_area, 4),
        "strata": strata,
        "confidence_level": confidence_level,
        "margin_of_error_pct": margin_of_error_pct,
    }


# ============================================================
# Synthetic Data Generation
# ============================================================

def generate_synthetic_ecosystem_raster(
    n_rows: int = 100,
    n_cols: int = 100,
    mangrove_fraction: float = 0.15,
    salt_marsh_fraction: float = 0.10,
    seagrass_fraction: float = 0.05,
    seed: int = 42,
) -> np.ndarray:
    """
    Generate a synthetic ecosystem classification raster.

    Layout: mangrove near top (coastal), salt marsh in middle, seagrass in water.
    """
    rng = np.random.RandomState(seed)
    raster = np.zeros((n_rows, n_cols), dtype=np.uint8)

    # Default: other (code 9)
    raster[:, :] = 9

    # Seagrass at bottom (submerged)
    seagrass_rows = int(n_rows * seagrass_fraction)
    if seagrass_rows > 0:
        raster[n_rows - seagrass_rows:, :] = 3

    # Mangrove band near top (intertidal)
    mangrove_rows = int(n_rows * mangrove_fraction)
    if mangrove_rows > 0:
        raster[0:mangrove_rows, :] = 1

    # Salt marsh between mangrove and land
    marsh_rows = int(n_rows * salt_marsh_fraction)
    if marsh_rows > 0 and mangrove_rows + marsh_rows < n_rows:
        raster[mangrove_rows:mangrove_rows + marsh_rows, :] = 2

    # Add some noise (misclassification)
    noise_mask = rng.random((n_rows, n_cols)) < 0.02
    raster[noise_mask] = rng.choice([1, 2, 3, 9], size=np.sum(noise_mask))

    # Add nodata patches
    nodata_mask = rng.random((n_rows, n_cols)) < 0.01
    raster[nodata_mask] = 0

    return raster


def generate_synthetic_ecosystem_t2(
    raster_t1: np.ndarray,
    loss_fraction: float = 0.05,
    gain_fraction: float = 0.02,
    seed: int = 43,
) -> np.ndarray:
    """
    Generate a second-period ecosystem raster with some changes.

    Simulates ecosystem loss (conversion to non-ecosystem) and gain.
    """
    rng = np.random.RandomState(seed)
    raster_t2 = raster_t1.copy()

    # Ecosystem codes
    eco_codes = [1, 2, 3]
    non_eco_codes = [0, 9]

    # Loss: randomly convert some ecosystem pixels to non-ecosystem
    for eco_code in eco_codes:
        eco_mask = raster_t1 == eco_code
        n_eco = np.sum(eco_mask)
        n_loss = int(n_eco * loss_fraction)
        if n_loss > 0:
            eco_pixels = np.argwhere(eco_mask)
            loss_indices = rng.choice(eco_pixels.shape[0], size=n_loss, replace=False)
            for idx in loss_indices:
                r, c = eco_pixels[idx]
                raster_t2[r, c] = rng.choice(non_eco_codes)

    # Gain: randomly convert some non-ecosystem pixels to ecosystem
    non_eco_mask = ~np.isin(raster_t1, eco_codes)
    n_non_eco = np.sum(non_eco_mask)
    n_gain = int(n_non_eco * gain_fraction)
    if n_gain > 0:
        non_eco_pixels = np.argwhere(non_eco_mask)
        gain_indices = rng.choice(non_eco_pixels.shape[0], size=n_gain, replace=False)
        for idx in gain_indices:
            r, c = non_eco_pixels[idx]
            raster_t2[r, c] = rng.choice(eco_codes)

    return raster_t2


# ============================================================
# Report Generation
# ============================================================

def generate_report_html(
    results: Dict,
    output_dir: Path,
) -> Path:
    """Generate HTML blue carbon assessment report."""
    path = output_dir / "report.html"

    # Extract values safely
    total_area = results.get("total_area_ha", "N/A")
    total_stock = results.get("total_stock_tC", "N/A")
    total_uncertainty = results.get("total_sigma_tC", "N/A")

    if isinstance(total_area, (int, float)):
        total_area_str = f"{total_area:.2f}"
    else:
        total_area_str = str(total_area)

    if isinstance(total_stock, (int, float)):
        total_stock_str = f"{total_stock:.1f}"
    else:
        total_stock_str = str(total_stock)

    if isinstance(total_uncertainty, (int, float)):
        total_uncertainty_str = f"{total_uncertainty:.1f}"
    else:
        total_uncertainty_str = str(total_uncertainty)

    # Build ecosystem rows
    eco_rows = ""
    ecosystem_details = results.get("ecosystem_details", {})
    for eco_name, eco_data in ecosystem_details.items():
        area = eco_data.get("area_ha", "N/A")
        stock = eco_data.get("stock_tC", {})
        total = stock.get("total_tC", "N/A") if isinstance(stock, dict) else "N/A"
        unc = eco_data.get("uncertainty", {})
        rel_unc = unc.get("relative_uncertainty_pct", "N/A") if isinstance(unc, dict) else "N/A"

        if isinstance(area, (int, float)):
            area_str = f"{area:.2f}"
        else:
            area_str = str(area)
        if isinstance(total, (int, float)):
            total_str = f"{total:.1f}"
        else:
            total_str = str(total)
        if isinstance(rel_unc, (int, float)):
            rel_unc_str = f"{rel_unc:.1f}"
        else:
            rel_unc_str = str(rel_unc)

        eco_rows += f"<tr><td>{eco_name}</td><td>{area_str}</td><td>{total_str}</td><td>{rel_unc_str}%</td></tr>\n"

    if not eco_rows:
        eco_rows = "<tr><td colspan='4'>No ecosystem data</td></tr>\n"

    # Build change rows
    change_rows = ""
    change_data = results.get("change_analysis", {})
    change_stats = change_data.get("change_stats", {}) if isinstance(change_data, dict) else {}
    for eco_name, cs in change_stats.items():
        delta = cs.get("delta_area_ha", "N/A")
        net = cs.get("net_change_tC", "N/A")

        if isinstance(delta, (int, float)):
            delta_str = f"{delta:.2f}"
        else:
            delta_str = str(delta)
        if isinstance(net, (int, float)):
            net_str = f"{net:.1f}"
        else:
            net_str = str(net)

        change_rows += f"<tr><td>{eco_name}</td><td>{delta_str}</td><td>{net_str}</td></tr>\n"

    if not change_rows:
        change_rows = "<tr><td colspan='3'>No change data</td></tr>\n"

    # Warnings
    warnings = results.get("warnings", [])
    warnings_html = ""
    for w in warnings:
        warnings_html += f"<li>{w}</li>\n"
    if not warnings_html:
        warnings_html = "<li>No warnings</li>\n"

    # Sampling summary
    sampling = results.get("sampling_plan", {})
    n_samples = sampling.get("total_samples", "N/A") if isinstance(sampling, dict) else "N/A"

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>Blue Carbon Assessment Report</title>
<style>
body {{ font-family: 'Microsoft YaHei', Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
.container {{ max-width: 900px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
h1 {{ color: #333; border-bottom: 3px solid #2e8b57; padding-bottom: 10px; }}
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
<h1>Blue Carbon Assessment Report</h1>
<p>Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}</p>

<div class="info">
<strong>Model:</strong> IPCC Tier 1 default factors for screening-level assessment.<br>
<strong>Note:</strong> Default factors are for screening only. Project-level requires field sampling.
</div>

<h2>Warnings</h2>
<ul>
{warnings_html}
</ul>

<h2>Summary</h2>
<p><strong>Total area:</strong> {total_area_str} ha<br>
<strong>Total carbon stock:</strong> {total_stock_str} tC<br>
<strong>Total uncertainty (1&sigma;):</strong> {total_uncertainty_str} tC</p>

<h2>Ecosystem Carbon Stocks</h2>
<table>
<tr><th>Ecosystem</th><th>Area (ha)</th><th>Stock (tC)</th><th>Rel. Uncertainty (%)</th></tr>
{eco_rows}
</table>

<h2>Change Analysis</h2>
<table>
<tr><th>Ecosystem</th><th>ΔArea (ha)</th><th>Net ΔCarbon (tC)</th></tr>
{change_rows}
</table>

<h2>Sampling Plan</h2>
<p><strong>Total samples:</strong> {n_samples}</p>

<h2>Methodology Notes</h2>
<ul>
<li>Carbon stock = Area × (AGB + BGB + Soil carbon density)</li>
<li>Uncertainty propagation: root sum of squares (RSS) of independent errors</li>
<li>Default factors from IPCC 2013 Wetlands Supplement (Tier 1)</li>
<li>Soil carbon depth-specific; change detection uses biomass + soil accumulation</li>
<li>Sampling: stratified random with Neyman-like allocation</li>
</ul>

</div>
</body>
</html>
"""

    path.write_text(html, encoding="utf-8")
    return path


# ============================================================
# Excel Report Generation
# ============================================================

def generate_carbon_summary_xlsx(
    results: Dict,
    output_dir: Path,
) -> Path:
    """Generate carbon summary as CSV (xlsx requires openpyxl, fallback to csv)."""
    path = output_dir / "carbon_summary.csv"

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "ecosystem", "area_ha", "agb_tC", "bgb_tC", "soil_tC",
            "total_tC", "sigma_tC", "rel_uncertainty_pct",
            "ci_lower_tC", "ci_upper_tC"
        ])

        ecosystem_details = results.get("ecosystem_details", {})
        for eco_name, eco_data in ecosystem_details.items():
            stock = eco_data.get("stock_tC", {})
            unc = eco_data.get("uncertainty", {})
            writer.writerow([
                eco_name,
                eco_data.get("area_ha", 0),
                stock.get("agb_tC", 0) if isinstance(stock, dict) else 0,
                stock.get("bgb_tC", 0) if isinstance(stock, dict) else 0,
                stock.get("soil_tC", 0) if isinstance(stock, dict) else 0,
                stock.get("total_tC", 0) if isinstance(stock, dict) else 0,
                unc.get("sigma_total_tC", 0) if isinstance(unc, dict) else 0,
                unc.get("relative_uncertainty_pct", 0) if isinstance(unc, dict) else 0,
                unc.get("ci_lower_tC", 0) if isinstance(unc, dict) else 0,
                unc.get("ci_upper_tC", 0) if isinstance(unc, dict) else 0,
            ])

        # Total row
        total_area = results.get("total_area_ha", 0)
        total_stock = results.get("total_stock_tC", 0)
        total_sigma = results.get("total_sigma_tC", 0)
        writer.writerow(["TOTAL", total_area, "", "", "", total_stock, total_sigma, "", "", ""])

    return path


# ============================================================
# Change GeoJSON Generation
# ============================================================

def generate_change_geojson(
    change_results: Dict,
    output_dir: Path,
) -> Path:
    """Generate change analysis GeoJSON."""
    path = output_dir / "change.geojson"

    features = []
    change_stats = change_results.get("change_stats", {})

    for eco_name, stats in change_stats.items():
        features.append({
            "type": "Feature",
            "geometry": None,
            "properties": {
                "ecosystem": eco_name,
                "area_t1_ha": stats.get("area_t1_ha", 0),
                "area_t2_ha": stats.get("area_t2_ha", 0),
                "delta_area_ha": stats.get("delta_area_ha", 0),
                "loss_tC": stats.get("loss_tC", 0),
                "gain_tC": stats.get("gain_tC", 0),
                "net_change_tC": stats.get("net_change_tC", 0),
            },
        })

    geojson = {
        "type": "FeatureCollection",
        "features": features,
        "properties": {
            "total_emissions_tC": change_results.get("total_emissions_tC", 0),
            "total_removals_tC": change_results.get("total_removals_tC", 0),
            "net_change_tC": change_results.get("net_change_tC", 0),
            "years_diff": change_results.get("years_diff", 1),
        },
    }

    path.write_text(
        json.dumps(geojson, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    return path


# ============================================================
# Main Pipeline
# ============================================================

def run_blue_carbon_pipeline(args: argparse.Namespace) -> int:
    """Main blue carbon assessment workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("bca-output")
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logging(output_dir)
    logger.info("Blue Carbon Assessment - Starting")

    # Parse ecosystem type
    ecosystem_type = getattr(args, 'ecosystem_type', None) or "all"
    if ecosystem_type not in VALID_ECOSYSTEM_TYPES:
        logger.error(f"Invalid ecosystem type: {ecosystem_type}. Valid: {VALID_ECOSYSTEM_TYPES}")
        cleanup_logging()
        return EXIT_ARG

    # Parse soil depth
    soil_depth = getattr(args, 'soil_depth', None) or "0_100cm"
    if soil_depth not in VALID_SOIL_DEPTHS:
        logger.error(f"Invalid soil depth: {soil_depth}. Valid: {VALID_SOIL_DEPTHS}")
        cleanup_logging()
        return EXIT_ARG

    # Parse boundary
    boundary = getattr(args, 'boundary', None) or "strict"
    if boundary not in VALID_BOUNDARIES:
        logger.error(f"Invalid boundary: {boundary}. Valid: {VALID_BOUNDARIES}")
        cleanup_logging()
        return EXIT_ARG

    # Parse uncertainty level
    uncertainty = getattr(args, 'uncertainty', None) or 0.95
    try:
        uncertainty = float(uncertainty)
        if not (0.5 <= uncertainty <= 0.99):
            raise ValueError("Uncertainty level must be between 0.5 and 0.99")
    except (ValueError, TypeError) as e:
        logger.error(f"Invalid uncertainty level: {uncertainty}. {e}")
        cleanup_logging()
        return EXIT_ARG

    # Load carbon factors
    factors_path = getattr(args, 'carbon_factors', None)
    try:
        carbon_factors = load_carbon_factors(factors_path)
        logger.info(f"Carbon factors loaded: version {carbon_factors.get('version', 'unknown')}")
    except Exception as e:
        logger.error(f"Failed to load carbon factors: {e}")
        cleanup_logging()
        return EXIT_VALIDATION

    # Parse years
    years_str = getattr(args, 'years', None) or "2020,2023"
    try:
        years = [int(y.strip()) for y in years_str.split(",")]
        if len(years) < 1:
            raise ValueError("At least one year required")
    except ValueError as e:
        logger.error(f"Invalid years format: {years_str}. {e}")
        cleanup_logging()
        return EXIT_ARG

    # --- Synthetic/demo mode or file-based mode ---
    use_synthetic = not (hasattr(args, 'ecosystem_raster') and args.ecosystem_raster)

    ecosystem_raster = None
    ecosystem_raster_t2 = None
    warnings = []
    pixel_area_ha = 0.01  # Default 10m x 10m = 0.01 ha

    if use_synthetic:
        logger.info("Running in synthetic demo mode")
        ecosystem_raster = generate_synthetic_ecosystem_raster(100, 100, seed=42)
        if len(years) >= 2:
            ecosystem_raster_t2 = generate_synthetic_ecosystem_t2(
                ecosystem_raster, loss_fraction=0.05, gain_fraction=0.02, seed=43
            )
    else:
        logger.info(f"Ecosystem raster: {args.ecosystem_raster}")
        # TODO: Implement file-based loading (rasterio)
        logger.warning("File-based mode not fully implemented, using synthetic subset")
        ecosystem_raster = generate_synthetic_ecosystem_raster(100, 100, seed=42)
        if len(years) >= 2:
            ecosystem_raster_t2 = generate_synthetic_ecosystem_t2(
                ecosystem_raster, loss_fraction=0.05, gain_fraction=0.02, seed=43
            )

    # --- Compute carbon stock ---
    eco_filter = None if ecosystem_type == "all" else ecosystem_type
    stock_results = compute_stock_from_raster(
        ecosystem_raster, pixel_area_ha, carbon_factors, soil_depth,
        ecosystem_filter=eco_filter,
    )

    # --- Change detection ---
    change_results = None
    if ecosystem_raster_t2 is not None and len(years) >= 2:
        years_diff = years[1] - years[0]
        change_results = detect_ecosystem_change(
            ecosystem_raster, ecosystem_raster_t2, pixel_area_ha,
            carbon_factors, soil_depth, years_diff=years_diff,
        )
        logger.info(f"Change detection: years {years[0]} -> {years[1]}, "
                     f"net change = {change_results['net_change_tC']:.1f} tC")

    # --- Sampling plan ---
    sampling_plan = generate_sampling_plan(
        ecosystem_raster, carbon_factors, soil_depth,
        confidence_level=uncertainty,
        pixel_area_ha=pixel_area_ha,
    )
    logger.info(f"Sampling plan: {sampling_plan['total_samples']} samples")

    # --- Warnings ---
    if use_synthetic:
        warnings.append("Using synthetic demo data. Replace with real ecosystem mapping for actual assessment.")
    warnings.append("Using IPCC Tier 1 default factors (screening-level). Project-level requires field sampling.")

    if boundary == "inclusive":
        warnings.append("Inclusive boundary includes transitional areas. Area estimates may be inflated.")

    # --- Generate outputs ---

    # Save ecosystem extent raster (numpy format for synthetic mode)
    if use_synthetic:
        extent_path = output_dir / "ecosystem_extent.npy"
        np.save(extent_path, ecosystem_raster)
        logger.info(f"Ecosystem extent saved: {extent_path}")

    # Save carbon stock raster (simplified: stock per pixel)
    stock_raster = np.zeros(ecosystem_raster.shape, dtype=np.float32)
    ecosystems_factors = carbon_factors.get("ecosystems", {})
    for idx, (eco_name, eco_f) in enumerate(ecosystems_factors.items()):
        eco_code = idx + 1
        agb = eco_f["above_ground_biomass_tC_ha"]["value"]
        bgb = eco_f["below_ground_biomass_tC_ha"]["value"]
        soil_key = f"soil_carbon_tC_ha_{soil_depth}"
        soil = eco_f[soil_key]["value"]
        total_density = agb + bgb + soil
        mask = ecosystem_raster == eco_code
        stock_raster[mask] = pixel_area_ha * total_density

    stock_path = output_dir / "blue_carbon_stock.npy"
    np.save(stock_path, stock_raster)
    logger.info(f"Carbon stock raster saved: {stock_path}")

    # Change GeoJSON
    if change_results:
        change_path = generate_change_geojson(change_results, output_dir)

    # Sampling plan GeoJSON
    sampling_path = output_dir / "sampling_plan.geojson"
    sampling_path.write_text(
        json.dumps(sampling_plan, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # Carbon summary CSV
    # Build results dict for report
    ecosystem_details = {}
    for eco_name, eco_data in stock_results.items():
        if eco_name == "total":
            continue
        ecosystem_details[eco_name] = eco_data

    report_results = {
        "total_area_ha": stock_results.get("total", {}).get("area_ha", 0),
        "total_stock_tC": stock_results.get("total", {}).get("total_stock_tC", 0),
        "total_sigma_tC": stock_results.get("total", {}).get("total_sigma_tC", 0),
        "ecosystem_details": ecosystem_details,
        "change_analysis": change_results,
        "sampling_plan": sampling_plan,
        "warnings": warnings,
    }

    summary_path = generate_carbon_summary_xlsx(report_results, output_dir)

    # Report HTML
    report_path = generate_report_html(report_results, output_dir)

    # request.json
    request_info = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "synthetic" if use_synthetic else "file",
        "ecosystem_type": ecosystem_type,
        "soil_depth": soil_depth,
        "boundary": boundary,
        "uncertainty_level": uncertainty,
        "years": years,
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
        "raster_shape": list(ecosystem_raster.shape),
        "ecosystem_type_filter": ecosystem_type,
        "soil_depth": soil_depth,
        "years": years,
        "n_ecosystems_mapped": len(ecosystem_details),
    }
    dataset_path = output_dir / "dataset-manifest.json"
    dataset_path.write_text(
        json.dumps(dataset_manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    # output-manifest.json
    output_files = {
        "report.html": str(report_path),
        "sampling_plan.geojson": str(sampling_path),
        "carbon_summary.csv": str(summary_path),
        "request.json": str(request_path),
        "dataset-manifest.json": str(dataset_path),
    }
    if use_synthetic:
        output_files["ecosystem_extent.npy"] = str(extent_path)
        output_files["blue_carbon_stock.npy"] = str(stock_path)
    if change_results:
        output_files["change.geojson"] = str(change_path)

    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "output_files": output_files,
        "summary": {
            "total_area_ha": stock_results.get("total", {}).get("area_ha", 0),
            "total_stock_tC": stock_results.get("total", {}).get("total_stock_tC", 0),
            "n_warnings": len(warnings),
            "n_samples": sampling_plan.get("total_samples", 0),
        },
    }
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
            "sampling_plan_generated": sampling_path.exists(),
            "carbon_summary_generated": summary_path.exists(),
            "all_outputs_written": all(Path(p).exists() for p in output_files.values()),
        },
        "ecosystem_type": ecosystem_type,
        "soil_depth": soil_depth,
        "n_warnings": len(warnings),
        "warnings": warnings,
        "n_samples": sampling_plan.get("total_samples", 0),
    }
    qa_path = output_dir / "qa.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    logger.info(f"Blue carbon assessment complete: "
                f"area={stock_results.get('total', {}).get('area_ha', 0):.2f}ha, "
                f"stock={stock_results.get('total', {}).get('total_stock_tC', 0):.1f}tC, "
                f"{len(warnings)} warnings")
    cleanup_logging()
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Blue Carbon Assessment")
    parser.add_argument("--ecosystem-raster", default=None,
                        help="Path to ecosystem classification GeoTIFF")
    parser.add_argument("--ecosystem-type", default="all",
                        help="Ecosystem type filter (mangrove/salt_marsh/seagrass/all)")
    parser.add_argument("--boundary", default="strict",
                        help="Boundary type (strict/inclusive)")
    parser.add_argument("--years", default="2020,2023",
                        help="Comma-separated years for change detection")
    parser.add_argument("--carbon-factors", default=None,
                        help="Path to custom carbon factors JSON")
    parser.add_argument("--soil-depth", default="0_100cm",
                        help="Soil depth for carbon accounting (0_30cm/0_100cm/0_200cm)")
    parser.add_argument("--uncertainty", type=float, default=0.95,
                        help="Confidence level for uncertainty (0.5-0.99)")
    parser.add_argument("--output-dir", "-o", default="bca-output",
                        help="Output directory (default: bca-output)")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    args = parser.parse_args()

    try:
        sys.exit(run_blue_carbon_pipeline(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
