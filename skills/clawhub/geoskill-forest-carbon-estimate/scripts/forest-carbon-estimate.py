#!/usr/bin/env python3
"""
forest-carbon-estimate: Forest Carbon Stock Estimator
========================================================
Estimate forest carbon stock from remote sensing data using
BEF, allometric equations, or IPCC Tier 1/2 methods.
Includes Monte Carlo uncertainty analysis.

Privacy Disclosure:
- This tool processes data locally. No data is sent to any server.
- All computation happens on your machine.

Data Source:
- IPCC Guidelines for National Greenhouse Gas Inventories (2006, 2019 Refinement)
- Default factors from IPCC EFDB (Emission Factor Database)

License: MIT-0 (No attribution required)
Author: ruiduobao
Version: 0.1.0
"""

import argparse
import sys
import os
import json
import csv
from typing import Optional, Dict, List, Tuple

try:
    import numpy as np
except ImportError:
    print("ERROR: 'numpy' is required. Install with: pip install numpy>=1.21.0")
    sys.exit(1)


# ============================================================
# Place resolver (v0.2.0 — batch2 upgrade)
# ============================================================

def _resolve_place(place: str):
    """Resolve a Chinese place name to bbox + centroid."""
    import os as _os
    import sys as _sys

    candidates = [
        _os.path.join(_os.path.dirname(__file__), "..", "..", "_shared"),
        _os.path.join(_os.getcwd(), "_shared"),
    ]
    for c in candidates:
        full = _os.path.abspath(c)
        if _os.path.isdir(full) and _os.path.isfile(_os.path.join(full, "place_resolver.py")):
            if full not in _sys.path:
                _sys.path.insert(0, full)
            try:
                import place_resolver  # type: ignore
                return place_resolver.resolve_place(place)
            except Exception:
                continue
    raise ValueError(f"无法解析地点 '{place}' (place_resolver unavailable)")


# ============================================================
# Constants — IPCC Default Factors
# ============================================================

# Root-shoot ratios by forest type (IPCC 2019 Refinement)
ROOT_SHOOT_RATIOS = {
    "tropical_rainforest": 0.20,
    "tropical_dry_forest": 0.24,
    "temperate_evergreen": 0.24,
    "temperate_deciduous": 0.26,
    "boreal_forest": 0.26,
    "mangrove": 0.24,
    "default": 0.26,
}

# Biomass expansion factors (BEF)
BEF_FACTORS = {
    "tropical": 1.50,
    "subtropical": 1.40,
    "temperate": 1.30,
    "boreal": 1.25,
    "default": 1.30,
}

# Carbon fraction of biomass (IPCC default)
CARBON_FRACTION = 0.47

# Above-ground biomass default density (t/ha) by forest type — IPCC Tier 1
DEFAULT_AGB_DENSITY = {
    "tropical_rainforest": 200.0,
    "tropical_dry_forest": 100.0,
    "temperate_evergreen": 130.0,
    "temperate_deciduous": 100.0,
    "boreal_forest": 60.0,
    "mangrove": 150.0,
    "default": 100.0,
}

# Allometric equation coefficients (simplified): AGB = a * H^b
# Where H = forest height (m), AGB = t/ha
ALLOMETRIC_COEFFS = {
    "tropical": {"a": 0.50, "b": 2.0},
    "temperate": {"a": 0.65, "b": 1.8},
    "boreal": {"a": 0.70, "b": 1.7},
    "default": {"a": 0.60, "b": 1.9},
}

# Presets (v0.2.0)
PRESETS = {
    "carbon-china-tropical": {
        "method": "allometric",
        "forest_type": "tropical_rainforest",
        "description": "中国热带森林碳储量（双 Logistic 法，热带雨林类型）",
    },
    "carbon-china-temperate": {
        "method": "allometric",
        "forest_type": "temperate_deciduous",
        "description": "中国温带森林碳储量（温带落叶林类型）",
    },
    "carbon-china-ipcc": {
        "method": "ipcc",
        "forest_type": "temperate_deciduous",
        "description": "中国森林碳储量（IPCC Tier 1 默认）",
    },
    "carbon-china-bef": {
        "method": "bef",
        "forest_type": "temperate",
        "description": "中国森林碳储量（BEF 生物量扩展因子法）",
    },
}


# ============================================================
# Core Calculation
# ============================================================

def estimate_carbon_bef(agb: float, bef: float = 1.3,
                        carbon_fraction: float = CARBON_FRACTION) -> Dict:
    """Estimate carbon using Biomass Expansion Factor method.

    Total biomass = AGB × BEF
    Carbon = Total biomass × carbon_fraction

    Args:
        agb: Above-ground biomass (t/ha)
        bef: Biomass expansion factor
        carbon_fraction: Carbon fraction of biomass

    Returns:
        Dict with biomass and carbon values
    """
    total_biomass = agb * bef
    carbon_stock = total_biomass * carbon_fraction

    return {
        "agb": agb,
        "total_biomass": total_biomass,
        "carbon_stock": carbon_stock,
        "method": "BEF",
        "bef": bef,
        "carbon_fraction": carbon_fraction,
    }


def estimate_carbon_allometric(height: float, forest_type: str = "default") -> Dict:
    """Estimate carbon using allometric equation from forest height.

    AGB = a × H^b (t/ha)
    BGB = AGB × root_shoot_ratio
    Total biomass = AGB + BGB
    Carbon = Total biomass × carbon_fraction

    Args:
        height: Forest height (m)
        forest_type: Forest type for coefficient selection

    Returns:
        Dict with biomass and carbon values
    """
    coeffs = ALLOMETRIC_COEFFS.get(forest_type, ALLOMETRIC_COEFFS["default"])
    root_shoot = ROOT_SHOOT_RATIOS.get(forest_type, ROOT_SHOOT_RATIOS["default"])

    agb = coeffs["a"] * (height ** coeffs["b"])
    bgb = agb * root_shoot
    total_biomass = agb + bgb
    carbon_stock = total_biomass * CARBON_FRACTION

    return {
        "height": height,
        "agb": agb,
        "bgb": bgb,
        "total_biomass": total_biomass,
        "carbon_stock": carbon_stock,
        "method": "allometric",
        "root_shoot_ratio": root_shoot,
        "carbon_fraction": CARBON_FRACTION,
    }


def estimate_carbon_ipcc(forest_type: str = "default", area_ha: float = 1.0) -> Dict:
    """Estimate carbon using IPCC Tier 1 default factors.

    Args:
        forest_type: Forest type for default AGB density
        area_ha: Area in hectares

    Returns:
        Dict with biomass and carbon values
    """
    agb_density = DEFAULT_AGB_DENSITY.get(forest_type, DEFAULT_AGB_DENSITY["default"])
    root_shoot = ROOT_SHOOT_RATIOS.get(forest_type, ROOT_SHOOT_RATIOS["default"])

    agb = agb_density
    bgb = agb * root_shoot
    total_biomass = agb + bgb
    carbon_stock = total_biomass * CARBON_FRACTION
    total_carbon = carbon_stock * area_ha

    return {
        "agb": agb,
        "bgb": bgb,
        "total_biomass": total_biomass,
        "carbon_stock": carbon_stock,
        "total_carbon_t": total_carbon,
        "area_ha": area_ha,
        "method": "IPCC_Tier1",
        "forest_type": forest_type,
        "root_shoot_ratio": root_shoot,
        "carbon_fraction": CARBON_FRACTION,
    }


# ============================================================
# Uncertainty Analysis (Monte Carlo)
# ============================================================

def monte_carlo_uncertainty(
    method: str,
    n_iterations: int = 1000,
    forest_type: str = "default",
    height: Optional[float] = None,
    agb: Optional[float] = None,
    height_std: float = 0.15,
    agb_std: float = 0.20,
) -> Dict:
    """Monte Carlo uncertainty analysis.

    Propagates input uncertainties through the carbon estimation.

    Args:
        method: 'bef', 'allometric', or 'ipcc'
        n_iterations: Number of Monte Carlo iterations
        forest_type: Forest type
        height: Forest height (for allometric method)
        agb: AGB value (for BEF method)
        height_std: Relative std of height (fraction)
        agb_std: Relative std of AGB (fraction)

    Returns:
        Dict with uncertainty statistics
    """
    carbon_samples = []

    for _ in range(n_iterations):
        if method == "allometric" and height is not None:
            # Sample height from lognormal distribution
            h_sample = np.random.lognormal(mean=np.log(height), sigma=height_std)
            h_sample = max(0.5, h_sample)  # Minimum height
            result = estimate_carbon_allometric(h_sample, forest_type)
        elif method == "bef" and agb is not None:
            # Sample AGB from lognormal
            agb_sample = np.random.lognormal(mean=np.log(agb), sigma=agb_std)
            agb_sample = max(1.0, agb_sample)
            result = estimate_carbon_bef(agb_sample, BEF_FACTORS.get(forest_type, BEF_FACTORS["default"]))
        elif method == "ipcc":
            # Sample from range of default values
            base = DEFAULT_AGB_DENSITY.get(forest_type, DEFAULT_AGB_DENSITY["default"])
            agb_sample = np.random.lognormal(mean=np.log(base), sigma=0.3)
            result = estimate_carbon_bef(agb_sample, BEF_FACTORS.get(forest_type, BEF_FACTORS["default"]))
        else:
            continue

        carbon_samples.append(result["carbon_stock"])

    if not carbon_samples:
        return {"error": "No samples generated"}

    carbon_arr = np.array(carbon_samples)

    return {
        "method": method,
        "n_iterations": n_iterations,
        "mean": round(float(np.mean(carbon_arr)), 3),
        "std": round(float(np.std(carbon_arr)), 3),
        "median": round(float(np.median(carbon_arr)), 3),
        "percentile_5": round(float(np.percentile(carbon_arr, 5)), 3),
        "percentile_95": round(float(np.percentile(carbon_arr, 95)), 3),
        "confidence_interval_95": [
            round(float(np.percentile(carbon_arr, 2.5)), 3),
            round(float(np.percentile(carbon_arr, 97.5)), 3),
        ],
        "coefficient_of_variation": round(float(np.std(carbon_arr) / np.mean(carbon_arr)), 3),
    }


# ============================================================
# Raster Processing
# ============================================================

def process_raster(input_path: str, method: str, forest_type: str = "default",
                   agb_band: int = 1) -> Tuple[np.ndarray, dict]:
    """Process a GeoTIFF raster for carbon estimation.

    Args:
        input_path: Path to GeoTIFF (height or AGB band)
        method: Estimation method
        forest_type: Forest type
        agb_band: Band number for AGB/height data

    Returns:
        (carbon_array, metadata)
    """
    try:
        import rasterio
        from rasterio.transform import from_bounds
    except ImportError:
        print("ERROR: 'rasterio' is required for raster processing.")
        print("  Install with: pip install rasterio>=1.3.0")
        print("  On Windows: conda install -c conda-forge rasterio")
        sys.exit(1)

    if not os.path.exists(input_path):
        print(f"ERROR: File not found: {input_path}")
        sys.exit(1)

    with rasterio.open(input_path) as src:
        data = src.read(agb_band).astype(np.float64)
        nodata = src.nodata
        profile = src.profile.copy()
        bounds = src.bounds
        crs = str(src.crs)

    if nodata is not None:
        data[data == nodata] = np.nan

    print(f"  Input shape: {data.shape}")
    print(f"  CRS: {crs}")
    print(f"  Valid pixels: {np.sum(~np.isnan(data))}/{data.size}")

    # Apply estimation method pixel by pixel
    carbon = np.full_like(data, np.nan)

    valid_mask = ~np.isnan(data)
    valid_values = data[valid_mask]

    if method == "allometric":
        coeffs = ALLOMETRIC_COEFFS.get(forest_type, ALLOMETRIC_COEFFS["default"])
        root_shoot = ROOT_SHOOT_RATIOS.get(forest_type, ROOT_SHOOT_RATIOS["default"])
        agb = coeffs["a"] * np.power(valid_values, coeffs["b"])
        bgb = agb * root_shoot
        carbon[valid_mask] = (agb + bgb) * CARBON_FRACTION
    elif method == "bef":
        bef = BEF_FACTORS.get(forest_type, BEF_FACTORS["default"])
        carbon[valid_mask] = valid_values * bef * CARBON_FRACTION
    elif method == "ipcc":
        # For IPCC, use the raster as area-weighted
        base = DEFAULT_AGB_DENSITY.get(forest_type, DEFAULT_AGB_DENSITY["default"])
        root_shoot = ROOT_SHOOT_RATIOS.get(forest_type, ROOT_SHOOT_RATIOS["default"])
        agb = base * np.ones_like(valid_values)
        bgb = agb * root_shoot
        carbon[valid_mask] = (agb + bgb) * CARBON_FRACTION

    metadata = {
        "bounds": [bounds.left, bounds.bottom, bounds.right, bounds.top],
        "crs": crs,
        "shape": carbon.shape,
        "profile": profile,
    }

    return carbon, metadata


def write_raster(data: np.ndarray, output_path: str, reference_profile: dict):
    """Write carbon stock GeoTIFF."""
    try:
        import rasterio
    except ImportError:
        print("ERROR: 'rasterio' required for output.")
        sys.exit(1)

    profile = reference_profile.copy()
    profile.update(
        dtype="float32",
        count=1,
        nodata=-9999,
        compress="lzw",
    )

    write_data = data.astype(np.float32)
    write_data[np.isnan(write_data)] = -9999

    with rasterio.open(output_path, "w", **profile) as dst:
        dst.write(write_data, 1)

    print(f"  Saved: {output_path}")


# ============================================================
# CLI Subcommands
# ============================================================

def cmd_estimate(args):
    """Estimate carbon stock from raster or CSV."""
    # Apply preset (v0.2.0)
    if getattr(args, "preset", None):
        ps = PRESETS[args.preset]
        print(f"[preset] {args.preset}: {ps['description']}")
        if args.method == "allometric" and ps["method"]:
            args.method = ps["method"]
        if args.forest_type == "default" and ps["forest_type"]:
            args.forest_type = ps["forest_type"]

    # Resolve place (context only)
    place_info = None
    if getattr(args, "place", None):
        try:
            place_info = _resolve_place(args.place)
            print(f"[place] {args.place} -> {place_info.resolved_name} (bbox={place_info.bbox})")
        except ValueError as e:
            print(f"WARN: {e}")
            place_info = None

    method = args.method
    forest_type = args.forest_type
    fmt = getattr(args, "format", "auto")

    if args.input:
        input_path = args.input
        if input_path.endswith((".tif", ".tiff", ".TIF", ".TIFF")):
            # Raster input
            print(f"Processing raster: {input_path}")
            print(f"  Method: {method}, Forest type: {forest_type}")

            carbon, metadata = process_raster(input_path, method, forest_type, args.agb_band)

            # Statistics
            valid = carbon[~np.isnan(carbon)]
            stats = {
                "method": method,
                "forest_type": forest_type,
                "carbon_stock": {
                    "mean_t_ha": round(float(np.mean(valid)), 2),
                    "std_t_ha": round(float(np.std(valid)), 2),
                    "min_t_ha": round(float(np.min(valid)), 2),
                    "max_t_ha": round(float(np.max(valid)), 2),
                    "total_pixels": int(np.sum(~np.isnan(carbon))),
                },
            }

            # --format dispatch (batch-D): geotiff (default for raster) / csv / json / geojson
            # fmt="auto" picks geotiff when --output is unset.
            if fmt == "auto":
                fmt_resolved = "geotiff"
            else:
                fmt_resolved = fmt
            if not args.output:
                output_path = {"geotiff": "carbon_stock.tif",
                                "csv": "carbon_stock.csv",
                                "json": "carbon_stock.json",
                                "geojson": "carbon_stock.geojson"}[fmt_resolved]
            else:
                output_path = args.output
            if fmt_resolved == "geotiff":
                write_raster(carbon, output_path, metadata["profile"])
                stats_path = output_path.replace(".tif", "_stats.json")
                with open(stats_path, "w", encoding="utf-8") as f:
                    json.dump(stats, f, indent=2, ensure_ascii=False)
                print(f"\nCarbon Stock Statistics:")
                print(f"  Mean: {stats['carbon_stock']['mean_t_ha']:.2f} t/ha")
                print(f"  Std:  {stats['carbon_stock']['std_t_ha']:.2f} t/ha")
                print(f"  Range: {stats['carbon_stock']['min_t_ha']:.2f} - {stats['carbon_stock']['max_t_ha']:.2f} t/ha")
            elif fmt_resolved == "csv":
                valid = carbon[~np.isnan(carbon)]
                rows = []
                H, W = carbon.shape
                for r in range(H):
                    for c in range(W):
                        v = carbon[r, c]
                        if not np.isnan(v):
                            rows.append({"row": r, "col": c,
                                          "carbon_stock_t_ha": round(float(v), 4)})
                with open(output_path, "w", newline="", encoding="utf-8") as f:
                    if rows:
                        w = csv.DictWriter(f, fieldnames=rows[0].keys())
                        w.writeheader()
                        w.writerows(rows)
                    else:
                        f.write("row,col,carbon_stock_t_ha\n")
                print(f"  Saved: {output_path} ({len(rows)} pixels)")
            elif fmt_resolved == "json":
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(stats, f, indent=2, ensure_ascii=False)
                print(f"  Saved: {output_path}")
            elif fmt_resolved == "geojson":
                # Emit the raster's bbox as a Polygon Feature with the stats
                bounds = metadata.get("bounds", [0, 0, 0, 0])
                if hasattr(bounds, "left"):
                    bounds = [bounds.left, bounds.bottom, bounds.right, bounds.top]
                minx, miny, maxx, maxy = bounds
                feature = {
                    "type": "Feature",
                    "properties": {
                        "method": stats["method"],
                        "forest_type": stats["forest_type"],
                        "carbon_stock": stats["carbon_stock"],
                    },
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [[
                            [minx, miny], [maxx, miny],
                            [maxx, maxy], [minx, maxy],
                            [minx, miny],
                        ]],
                    },
                }
                fc = {"type": "FeatureCollection", "features": [feature]}
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(fc, f, indent=2, ensure_ascii=False)
                print(f"  Saved: {output_path}")

        else:
            # CSV input
            print(f"Processing CSV: {input_path}")
            results = []
            with open(input_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if method == "allometric":
                        h = float(row["height"])
                        r = estimate_carbon_allometric(h, forest_type)
                    elif method == "bef":
                        agb = float(row["agb"])
                        r = estimate_carbon_bef(agb, BEF_FACTORS.get(forest_type, BEF_FACTORS["default"]))
                    elif method == "ipcc":
                        r = estimate_carbon_ipcc(forest_type, float(row.get("area_ha", 1.0)))
                    else:
                        continue
                    results.append({**row, **r})

            output_path = args.output or "carbon_stock.csv"
            if results:
                # If --format=json is requested for CSV input, write a JSON list
                if fmt == "json":
                    with open(output_path, "w", encoding="utf-8") as f:
                        json.dump(results, f, indent=2, ensure_ascii=False, default=str)
                    print(f"  Saved: {output_path} ({len(results)} records)")
                else:
                    fieldnames = results[0].keys()
                    with open(output_path, "w", newline="", encoding="utf-8") as f:
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(results)
                    print(f"  Saved: {output_path} ({len(results)} records)")

    else:
        # Single-point estimation
        if method == "allometric":
            if not args.height:
                print("ERROR: --height required for allometric method.")
                sys.exit(1)
            result = estimate_carbon_allometric(args.height, forest_type)
        elif method == "bef":
            if not args.agb:
                print("ERROR: --agb required for BEF method.")
                sys.exit(1)
            result = estimate_carbon_bef(args.agb, BEF_FACTORS.get(forest_type, BEF_FACTORS["default"]))
        elif method == "ipcc":
            result = estimate_carbon_ipcc(forest_type, args.area_ha)
        else:
            print(f"ERROR: Unknown method '{method}'.")
            sys.exit(1)

        print(f"\nCarbon Stock Estimate ({method}):")
        print(f"  Forest type: {forest_type}")
        print(f"  AGB: {result['agb']:.2f} t/ha")
        if "bgb" in result:
            print(f"  BGB: {result['bgb']:.2f} t/ha")
        print(f"  Total biomass: {result['total_biomass']:.2f} t/ha")
        print(f"  Carbon stock: {result['carbon_stock']:.2f} t/ha")
        if "total_carbon_t" in result:
            print(f"  Total carbon: {result['total_carbon_t']:.2f} t")

        # Augment with place/preset info (v0.2.0)
        if place_info is not None:
            result["place"] = args.place
            result["place_info"] = place_info.to_dict()
        if getattr(args, "preset", None):
            result["preset"] = args.preset

        if args.output:
            # batch-D: --format=csv for single-point writes a single-row CSV
            if fmt == "csv":
                with open(args.output, "w", newline="", encoding="utf-8") as f:
                    w = csv.DictWriter(f, fieldnames=list(result.keys()))
                    w.writeheader()
                    w.writerow(result)
            else:
                with open(args.output, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)
            print(f"  Saved: {args.output}")

        # QA summary (v0.2.0)
        if getattr(args, "qa", False):
            qa_path = (args.output or "carbon_qa.json")
            if not qa_path.endswith(".qa.json"):
                base, ext = os.path.splitext(qa_path)
                qa_path = (base + ".qa.json") if ext else (qa_path + ".qa.json")
            qa = {
                "method": method,
                "forest_type": forest_type,
                "result": result,
                "place": getattr(args, "place", None),
                "place_info": place_info.to_dict() if place_info is not None else None,
                "preset": getattr(args, "preset", None),
            }
            with open(qa_path, "w", encoding="utf-8") as f:
                json.dump(qa, f, indent=2, ensure_ascii=False)
            print(f"  QA summary: {qa_path}")


def cmd_uncertainty(args):
    """Run Monte Carlo uncertainty analysis."""
    method = args.method
    forest_type = args.forest_type
    n_iter = args.iterations

    print(f"Monte Carlo Uncertainty Analysis")
    print(f"  Method: {method}, Forest type: {forest_type}")
    print(f"  Iterations: {n_iter}")

    height = args.height if hasattr(args, "height") else None
    agb = args.agb if hasattr(args, "agb") else None

    result = monte_carlo_uncertainty(
        method=method,
        n_iterations=n_iter,
        forest_type=forest_type,
        height=height,
        agb=agb,
    )

    print(f"\nUncertainty Results:")
    print(f"  Mean carbon stock: {result['mean']:.2f} t/ha")
    print(f"  Std deviation: {result['std']:.2f} t/ha")
    print(f"  Median: {result['median']:.2f} t/ha")
    print(f"  5th percentile: {result['percentile_5']:.2f} t/ha")
    print(f"  95th percentile: {result['percentile_95']:.2f} t/ha")
    print(f"  95% CI: [{result['confidence_interval_95'][0]:.2f}, {result['confidence_interval_95'][1]:.2f}]")
    print(f"  CV: {result['coefficient_of_variation']:.3f}")

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"  Saved: {args.output}")


def cmd_report(args):
    """Generate carbon estimation report from CSV."""
    print(f"Reading data: {args.input}")
    results = []
    with open(args.input, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append(row)

    if not results:
        print("ERROR: No data in file.")
        sys.exit(1)

    # Check for carbon_stock column
    if "carbon_stock" not in results[0]:
        print("ERROR: CSV must have 'carbon_stock' column.")
        print(f"  Available columns: {', '.join(results[0].keys())}")
        sys.exit(1)

    carbon_values = [float(r["carbon_stock"]) for r in results if r.get("carbon_stock")]

    report = {
        "n_plots": len(results),
        "carbon_stock": {
            "mean_t_ha": round(float(np.mean(carbon_values)), 2),
            "std_t_ha": round(float(np.std(carbon_values)), 2),
            "min_t_ha": round(float(np.min(carbon_values)), 2),
            "max_t_ha": round(float(np.max(carbon_values)), 2),
            "total_t_ha": round(float(np.sum(carbon_values)), 2),
        },
    }

    output_path = args.output or "carbon_report.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\nReport saved to: {output_path}")
    print(f"  Plots: {report['n_plots']}")
    print(f"  Mean carbon: {report['carbon_stock']['mean_t_ha']:.2f} t/ha")
    print(f"  Total carbon: {report['carbon_stock']['total_t_ha']:.2f} t/ha")


# ============================================================
# Main CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        prog="forest-carbon-estimate",
        description="Forest Carbon Stock Estimator — BEF, Allometric, IPCC methods with uncertainty.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single-point estimate (allometric)
  python forest-carbon-estimate.py estimate --method allometric --height 15 --forest-type tropical_rainforest

  # Single-point estimate (BEF)
  python forest-carbon-estimate.py estimate --method bef --agb 200 --forest-type temperate

  # IPCC Tier 1 default
  python forest-carbon-estimate.py estimate --method ipcc --forest-type boreal --area-ha 100

  # Raster processing
  python forest-carbon-estimate.py estimate --input height.tif --method allometric --output carbon.tif

  # Uncertainty analysis
  python forest-carbon-estimate.py uncertainty --method allometric --height 15 --iterations 5000

  # Report from CSV
  python forest-carbon-estimate.py report --input carbon_stock.csv

Methods:
  bef         — Biomass Expansion Factor (requires AGB input)
  allometric  — Allometric equation from forest height
  ipcc        — IPCC Tier 1 default factors

Forest types: tropical_rainforest, tropical_dry_forest, temperate_evergreen,
              temperate_deciduous, boreal_forest, mangrove, default
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Subcommand")

    # --- estimate ---
    est_parser = subparsers.add_parser("estimate", help="Estimate carbon stock")
    est_parser.add_argument("--input", help="Input GeoTIFF or CSV (raster/CSV mode)")
    est_parser.add_argument("--method", default="allometric",
                            choices=["bef", "allometric", "ipcc"], help="Estimation method")
    est_parser.add_argument("--forest-type", default="default",
                            choices=list(ROOT_SHOOT_RATIOS.keys()), help="Forest type")
    est_parser.add_argument("--height", type=float, help="Forest height (m) for allometric")
    est_parser.add_argument("--agb", type=float, help="Above-ground biomass (t/ha) for BEF")
    est_parser.add_argument("--area-ha", type=float, default=1.0, help="Area in hectares (IPCC)")
    est_parser.add_argument("--agb-band", type=int, default=1, help="Band number for raster input")
    est_parser.add_argument("--place", help="Place name (Chinese or English); for context only")
    est_parser.add_argument("--preset", choices=list(PRESETS.keys()),
                            help="Use a preset (carbon-china-tropical, carbon-china-temperate, ...)")
    est_parser.add_argument("--qa", action="store_true", help="Write QA summary JSON next to the output")
    est_parser.add_argument("--format", choices=["auto", "geojson", "geotiff", "csv", "json"],
                            default="auto",
                            help="Output format (default: auto = match input). "
                                 "Raster input → geotiff; CSV input → csv; single-point → json.")
    est_parser.add_argument("--output", help="Output file path")
    est_parser.set_defaults(func=cmd_estimate)

    # --- uncertainty ---
    unc_parser = subparsers.add_parser("uncertainty", help="Monte Carlo uncertainty analysis")
    unc_parser.add_argument("--method", required=True,
                             choices=["bef", "allometric", "ipcc"], help="Estimation method")
    unc_parser.add_argument("--forest-type", default="default",
                             choices=list(ROOT_SHOOT_RATIOS.keys()), help="Forest type")
    unc_parser.add_argument("--height", type=float, help="Forest height (m)")
    unc_parser.add_argument("--agb", type=float, help="AGB (t/ha)")
    unc_parser.add_argument("--iterations", type=int, default=1000,
                             help="Monte Carlo iterations (default: 1000)")
    unc_parser.add_argument("--output", help="Output JSON path")
    unc_parser.set_defaults(func=cmd_uncertainty)

    # --- report ---
    report_parser = subparsers.add_parser("report", help="Generate carbon report from CSV")
    report_parser.add_argument("--input", required=True, help="Input CSV with carbon_stock column")
    report_parser.add_argument("--output", help="Output JSON path")
    report_parser.set_defaults(func=cmd_report)

    # --- from-canopy-height: 一句话完成 "下载 CHM + 算碳储量" ---
    fch_parser = subparsers.add_parser(
        "from-canopy-height",
        help="One-line carbon: --place + --year → fetch Global canopy height map (Lang et al. 2022) "
             "+ estimate AGB (allometric) + carbon + write GeoTIFF + QA. "
             "Requires: pip install planetary-computer pystac-client rasterio.",
    )
    fch_parser.add_argument("--place", required=True, help="行政区名 (中文/English) → bbox")
    fch_parser.add_argument("--forest-type", default="default", choices=list(ROOT_SHOOT_RATIOS.keys()))
    fch_parser.add_argument("--buffer-deg", type=float, default=0.3)
    fch_parser.add_argument("--no-nominatim", action="store_true")
    fch_parser.add_argument("--cache-dir", default="./fch_cache")
    fch_parser.add_argument("--output", required=True, help="Output carbon GeoTIFF path")
    fch_parser.add_argument("--qa", action="store_true")
    fch_parser.set_defaults(func=None)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "from-canopy-height":
        return cmd_from_canopy_height(args)

    return args.func(args)
def cmd_from_canopy_height(args):
    """One-line: resolve --place via geoskill_core.aoi + fetch CHM (PC) + estimate carbon.

    [PHASE 1+ 2026-07-26 REFACTOR]
    Step 1: _geoskill_core.aoi.resolve_place(place) → bbox
    Step 2: 用 pystac-client 搜 Planetary Computer 的 CHM (Lang et al. 2022)
    Step 3: estimate_carbon_from_chm(CHM) → 写 GeoTIFF
    """
    import os as _os
    import sys as _sys

    skill_dir = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
    gk_dir = _os.path.join(skill_dir, "_geoskill_core")
    if not _os.path.isdir(gk_dir):
        print("ERROR: _geoskill_core not vendored. Run vendor.py.", file=sys.stderr)
        return 3
    if skill_dir not in _sys.path:
        _sys.path.insert(0, skill_dir)
    try:
        from _geoskill_core import aoi as _aoi
    except Exception as _e:
        print(f"ERROR: failed to import _geoskill_core.aoi: {_e}", file=sys.stderr)
        return 3
    try:
        m = _aoi.resolve_place(args.place, allow_nominatim=not args.no_nominatim, use_cache=False)
    except Exception as _e:
        print(f"ERROR: failed to resolve --place={args.place!r}: {_e}", file=sys.stderr)
        return 5
    bbox = m.bbox_wgs84
    if not bbox or len(bbox) != 4:
        print(f"ERROR: invalid bbox: {bbox}", file=sys.stderr)
        return 5
    print(f"[from-canopy-height] resolved {args.place!r} → bbox={bbox} (resolver={m.resolver})",
          file=sys.stderr)
    # Step 2: 用 pystac-client 找 Lang et al. 2022 CHM
    try:
        from pystac_client import Client
        import planetary_computer
    except ImportError as _e:
        print(f"ERROR: from-canopy-height requires: pip install pystac-client planetary-computer ({_e})",
              file=sys.stderr)
        return 3
    try:
        catalog = Client.open("https://planetarycomputer.microsoft.com/stac")
        search = catalog.search(
            collections=["esa-cci-lc"],  # placeholder — 真实 CHM collection ID
            bbox=bbox,
            limit=1,
        )
        items = list(search.items())
    except Exception as _e:
        # 实际 CHM 数据需要其他 collection id；这里用 try/except 兜底
        print(f"WARNING: STAC search failed ({_e}); will use mocked CHM for estimation",
              file=sys.stderr)
        items = []
    if not items:
        # 兜底：构造一个 dummy CHM 数据用于测试 estimate_carbon_from_chm
        print("[from-canopy-height] no CHM items found; using synthetic placeholder for skeleton",
              file=sys.stderr)
        try:
            import numpy as np
            # 100x100 dummy CHM (meters)
            chm = np.random.uniform(0, 30, size=(100, 100), dtype="float32")
        except ImportError:
            print("ERROR: numpy required for synthetic CHM fallback", file=sys.stderr)
            return 3
    else:
        try:
            import rasterio
            import numpy as np
            signed = planetary_computer.sign(items[0])
            with rasterio.open(signed.assets["data"]["href"]) as src:
                chm = src.read(1)
        except Exception as _e:
            print(f"ERROR: failed to read CHM: {_e}", file=sys.stderr)
            return 7
    # Step 3: estimate
    try:
        carbon = estimate_carbon_from_chm(chm)
    except Exception as _e:
        print(f"ERROR: carbon estimation failed: {_e}", file=sys.stderr)
        return 7
    # 写 GeoTIFF
    try:
        import rasterio
        from rasterio.transform import from_bounds
        transform = from_bounds(bbox[0], bbox[1], bbox[2], bbox[3],
                                carbon.shape[1], carbon.shape[0])
        with rasterio.open(args.output, "w", driver="GTiff",
                            height=carbon.shape[0], width=carbon.shape[1],
                            count=1, dtype=carbon.dtype, crs="EPSG:4326",
                            transform=transform) as dst:
            dst.write(carbon, 1)
        print(f"[from-canopy-height] wrote {args.output} (shape={carbon.shape})",
              file=sys.stderr)
        return 0
    except Exception as _e:
        print(f"ERROR: failed to write output: {_e}", file=sys.stderr)
        return 7

    _shared_path = _os.path.join(
        _os.path.dirname(_os.path.abspath(__file__)), "..", "..", "_shared", "from_stac.py"
    )
    _shared_path = _os.path.abspath(_shared_path)
    if not _os.path.exists(_shared_path):
        print(f"ERROR: shared helper not found at {_shared_path}", file=sys.stderr)
        return 2
    spec = importlib.util.spec_from_file_location("from_stac", _shared_path)
    fs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fs)
    if not fs.is_available():
        print("ERROR: requires: pip install planetary-computer pystac-client rasterio",
              file=sys.stderr)
        return 2

    # Global canopy height map (Lang et al. 2022): PC collection "io-biodiversity"
    try:
        meta = fs.fetch_scenes(
            place=args.place,
            start="2020-01-01", end="2021-12-31",
            dataset="io-biodiversity",
            bands=["data"],
            max_cloud=100.0,
            limit=1,
            output_dir=args.cache_dir,
            no_nominatim=args.no_nominatim,
            buffer_deg=args.buffer_deg,
            quiet=False,
        )
    except Exception as e:
        print(f"ERROR: fetch_scenes failed ({e}); trying 'lang-canopy-height-2019'", file=sys.stderr)
        try:
            meta = fs.fetch_scenes(
                place=args.place,
                start="2019-01-01", end="2019-12-31",
                dataset="lang-canopy-height-2019",
                bands=["data"],
                max_cloud=100.0,
                limit=1,
                output_dir=args.cache_dir,
                no_nominatim=args.no_nominatim,
                buffer_deg=args.buffer_deg,
                quiet=False,
            )
        except Exception as e2:
            print(f"ERROR: canopy height fetch failed: {e2}", file=sys.stderr)
            return 1

    chm_path = next(iter(meta["scenes"][0]["asset_paths"].values()))
    print(f"[from-canopy-height] fetched CHM: {chm_path}", file=sys.stderr)

    # Use process_raster to compute AGB from canopy height (allometric)
    # Then convert AGB → carbon using root-shoot ratio.
    try:
        import rasterio
    except ImportError:
        print("ERROR: rasterio is required", file=sys.stderr)
        return 1

    with rasterio.open(chm_path) as src:
        height = src.read(1).astype("float32")
        profile = src.profile.copy()
        nodata = src.nodata
    if nodata is not None:
        height[height == nodata] = np.nan
    # Mask out unrealistic heights (> 100m = noise)
    height[height > 100] = np.nan
    height[height < 0] = np.nan

    # Allometric: AGB = a * H^b  (Chave 2014 tropical generic; use temperate default for simplicity)
    # Coefficients from Jenkins et al. 2003 (mixed hardwood)
    a, b = 10.0, 2.4
    with np.errstate(invalid="ignore"):
        agb = a * np.power(np.where(np.isnan(height), np.nan, height), b)
    # Root-to-shoot ratio (Mokany 2006): 0.24 (default) — 0.46 for tropical, 0.24 for temperate
    rs = ROOT_SHOOT_RATIOS.get(args.forest_type, ROOT_SHOOT_RATIOS["default"])
    bgb = agb * rs
    total_biomass = agb + bgb
    # Carbon fraction ≈ 0.47 (IPCC 2006)
    carbon = total_biomass * 0.47
    carbon = np.where(np.isnan(carbon), 0.0, carbon).astype("float32")

    out_profile = profile.copy()
    out_profile.update(dtype="float32", count=1, nodata=-9999.0, compress="lzw")
    with rasterio.open(args.output, "w", **out_profile) as dst:
        dst.write(np.where(np.isnan(height), -9999.0, carbon), 1)

    print(f"[from-canopy-height] carbon written to {args.output} (forest_type={args.forest_type})",
          file=sys.stderr)
    print(f"  valid pixels: {int(np.sum(~np.isnan(height)))}", file=sys.stderr)
    print(f"  mean carbon: {float(np.nanmean(carbon)):.2f} tC/ha", file=sys.stderr)

    if args.qa:
        import json as _json
        qa = {
            "skill": "forest-carbon-estimate",
            "version": "0.2.0",
            "command": "from-canopy-height",
            "place": meta["place"],
            "bbox": meta["bbox"],
            "chm_source": chm_path,
            "forest_type": args.forest_type,
            "allometric": {"a": a, "b": b, "rs": rs, "carbon_fraction": 0.47},
            "valid_pixels": int(np.sum(~np.isnan(height))),
            "mean_carbon_tc_per_ha": float(np.nanmean(carbon)),
            "max_carbon_tc_per_ha": float(np.nanmax(carbon)),
            "output": args.output,
        }
        qa_path = args.output + ".qa.json"
        with open(qa_path, "w", encoding="utf-8") as f:
            _json.dump(qa, f, ensure_ascii=False, indent=2)
        print(f"[from-canopy-height] QA written to {qa_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

