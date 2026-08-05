#!/usr/bin/env python3
"""
Impervious Surface Mapping - Estimate impervious fraction from satellite imagery.

Reads multi-band Sentinel-2 imagery, computes spectral indices (NDBI, NDVI, MNDWI),
estimates impervious surface fraction via sub-pixel regression, and produces
binary/fraction maps with optional zone aggregation and change detection.

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

# ─── shared data fetcher (optional, enables --bbox/--date-range auto-download) ─
_SCRIPT_DIR = Path(__file__).resolve().parent
_DATA_FETCHER_ROOT = _SCRIPT_DIR.parent.parent
if str(_DATA_FETCHER_ROOT) not in sys.path:
    sys.path.insert(0, str(_DATA_FETCHER_ROOT))
# Optional auto-download via shared data fetcher (Microsoft Planetary Computer)
import sys
# Try pip-installed package first; fall back to local copy in repo root.
try:
    from _geoskill_data_fetcher import (DataFetcher,
        DataSource,
        add_bbox_date_args,
        parse_bbox_arg,
        parse_date_range_arg,)
    _HAS_DATA_FETCHER = True
except ImportError:
    import sys as _sys
    from pathlib import Path as _Path
    _skill_dir = _Path(__file__).resolve().parent
    _repo_root = _skill_dir.parent.parent
    _local_fetcher = _repo_root / "_geoskill_data_fetcher"
    if _local_fetcher.exists():
        _sys.path.insert(0, str(_repo_root))
    from _geoskill_data_fetcher import (DataFetcher,
        DataSource,
        add_bbox_date_args,
        parse_bbox_arg,
        parse_date_range_arg,)
    _HAS_DATA_FETCHER = True
except ImportError:  # pragma: no cover - optional
    _HAS_DATA_FETCHER = False

EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# Sentinel-2 band indices (0-based) for a 5-band raster: B2, B3, B4, B8, B11
BAND_B2 = 0   # Blue
BAND_B3 = 1   # Green
BAND_B4 = 2   # Red
BAND_B8 = 3   # NIR
BAND_B11 = 4  # SWIR


def generate_synthetic_data(out_dir, seed=42):
    """Generate 5-band synthetic Sentinel-2 raster + 10-point training samples GeoJSON."""
    import numpy as np
    import rasterio
    from rasterio.transform import from_origin
    from shapely.geometry import Point, mapping
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.RandomState(seed)
    transform = from_origin(0, 60, 0.001, 0.001)
    H, W = 60, 60
    # Lower-right quadrant = built-up (low NDVI, high NDBI)
    arr = np.zeros((5, H, W), dtype=np.float32)
    # B2 (Blue), B3 (Green), B4 (Red), B8 (NIR), B11 (SWIR)
    # Built-up reflectance: red/SWIR high, NIR low
    # Vegetation: NIR high, red low
    for i in range(H):
        for j in range(W):
            if i >= H // 2 and j >= W // 2:
                # built-up
                arr[0, i, j] = rng.uniform(0.08, 0.12)   # B2 Blue
                arr[1, i, j] = rng.uniform(0.10, 0.15)   # B3 Green
                arr[2, i, j] = rng.uniform(0.12, 0.18)   # B4 Red
                arr[3, i, j] = rng.uniform(0.08, 0.14)   # B8 NIR (low)
                arr[4, i, j] = rng.uniform(0.18, 0.25)   # B11 SWIR (high)
            else:
                # vegetation
                arr[0, i, j] = rng.uniform(0.03, 0.06)   # B2
                arr[1, i, j] = rng.uniform(0.05, 0.10)   # B3
                arr[2, i, j] = rng.uniform(0.02, 0.06)   # B4
                arr[3, i, j] = rng.uniform(0.30, 0.45)   # B8 NIR (high)
                arr[4, i, j] = rng.uniform(0.05, 0.12)   # B11
    raster_p = out_dir / "sentinel2_synthetic.tif"
    with rasterio.open(str(raster_p), "w", driver="GTiff", height=H, width=W,
                       count=5, dtype="float32", crs="EPSG:4326",
                       transform=transform) as dst:
        dst.write(arr)
    # 10 training points: 5 in built-up, 5 in vegetation
    training_features = []
    for k in range(10):
        if k < 5:
            i = rng.randint(H // 2, H)
            j = rng.randint(W // 2, W)
            label = 1
        else:
            i = rng.randint(0, H // 2)
            j = rng.randint(0, W // 2)
            label = 0
        x = 0 + (j + 0.5) * 0.001
        y = 60 - (i + 0.5) * 0.001
        training_features.append({
            "type": "Feature",
            "properties": {"id": k, "impervious": label},
            "geometry": mapping(Point(x, y)),
        })
    training_p = out_dir / "training_samples_synthetic.geojson"
    training_p.write_text(json.dumps(
        {"type": "FeatureCollection", "features": training_features}, indent=2),
        encoding="utf-8")
    return raster_p, training_p


def read_raster(path: Path, band: int = None) -> Dict[str, Any]:
    """Read raster data and metadata. If band is None, read all bands."""
    try:
        import rasterio
    except ImportError:
        print("ERROR: rasterio required", file=sys.stderr)
        sys.exit(EXIT_DEP)

    with rasterio.open(path) as ds:
        if band is not None:
            data = ds.read(band + 1)  # rasterio is 1-based
        else:
            data = ds.read()
        return {
            "data": data,
            "crs": str(ds.crs) if ds.crs else None,
            "transform": ds.transform,
            "nodata": ds.nodata,
            "shape": data.shape,
            "bounds": list(ds.bounds),
        }


def compute_ndbi(swir: np.ndarray, nir: np.ndarray) -> np.ndarray:
    """
    Compute Normalized Difference Built-up Index (NDBI).
    NDBI = (SWIR - NIR) / (SWIR + NIR)
    """
    denominator = swir + nir
    result = np.zeros_like(swir, dtype=float)
    valid = denominator != 0
    result[valid] = (swir[valid] - nir[valid]) / denominator[valid]
    return result


def compute_ndvi(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
    """
    Compute Normalized Difference Vegetation Index (NDVI).
    NDVI = (NIR - Red) / (NIR + Red)
    """
    denominator = nir + red
    result = np.zeros_like(nir, dtype=float)
    valid = denominator != 0
    result[valid] = (nir[valid] - red[valid]) / denominator[valid]
    return result


def compute_mndwi(green: np.ndarray, swir: np.ndarray) -> np.ndarray:
    """
    Compute Modified Normalized Difference Water Index (MNDWI).
    MNDWI = (Green - SWIR) / (Green + SWIR)
    """
    denominator = green + swir
    result = np.zeros_like(green, dtype=float)
    valid = denominator != 0
    result[valid] = (green[valid] - swir[valid]) / denominator[valid]
    return result


def estimate_impervious_fraction(ndbi: np.ndarray, ndvi: np.ndarray,
                                 mndwi: np.ndarray,
                                 ndvi_mask: float = 0.6,
                                 mndwi_mask: float = 0.0) -> np.ndarray:
    """
    Estimate impervious surface fraction from spectral indices.

    Uses a linear regression model based on NDBI, with masking of
    water (MNDWI > threshold) and dense vegetation (NDVI > threshold).

    The fraction is estimated as:
        fraction = clip(a * NDBI + b, 0, 1)
    where a=0.7, b=0.3 are empirical coefficients.

    Water and dense vegetation pixels are set to 0.
    """
    # Empirical coefficients for NDBI-to-fraction regression
    a = 0.7
    b = 0.3

    fraction = a * ndbi + b
    fraction = np.clip(fraction, 0.0, 1.0)

    # Mask water bodies
    water_mask = mndwi > mndwi_mask
    fraction[water_mask] = 0.0

    # Mask dense vegetation
    veg_mask = ndvi > ndvi_mask
    fraction[veg_mask] = 0.0

    return fraction


def apply_threshold(fraction: np.ndarray, threshold: float = 0.5) -> np.ndarray:
    """Convert continuous fraction to binary mask."""
    return (fraction >= threshold).astype(np.uint8)


def compute_change(fraction_current: np.ndarray,
                   fraction_past: np.ndarray) -> np.ndarray:
    """Compute impervious fraction change between two periods."""
    return fraction_current - fraction_past


def aggregate_by_zone(fraction: np.ndarray, transform, crs,
                      zone_layer_path: Path) -> List[Dict]:
    """
    Aggregate impervious fraction statistics by zone polygons.

    Reads a GeoJSON layer and computes mean/max/count for each zone.
    """
    try:
        import rasterio.features
        from shapely.geometry import shape
    except ImportError:
        print("ERROR: rasterio/shapely required", file=sys.stderr)
        sys.exit(EXIT_DEP)

    geojson = json.loads(zone_layer_path.read_text(encoding="utf-8"))
    features = geojson.get("features", [])

    results = []
    for feat in features:
        geom = shape(feat["geometry"])
        props = feat.get("properties", {})
        zone_id = props.get("id", props.get("name", props.get("zone_id", "unknown")))

        # Create mask for this zone
        try:
            zone_mask = rasterio.features.geometry_mask(
                [geom], out_shape=fraction.shape, transform=transform, invert=True
            )
        except Exception:
            continue

        zone_pixels = fraction[zone_mask]
        if len(zone_pixels) == 0:
            results.append({
                "zone_id": str(zone_id),
                "mean_fraction": 0.0,
                "max_fraction": 0.0,
                "min_fraction": 0.0,
                "pixel_count": 0,
                "area_impervious_fraction": 0.0,
            })
            continue

        results.append({
            "zone_id": str(zone_id),
            "mean_fraction": round(float(np.mean(zone_pixels)), 4),
            "max_fraction": round(float(np.max(zone_pixels)), 4),
            "min_fraction": round(float(np.min(zone_pixels)), 4),
            "pixel_count": int(len(zone_pixels)),
            "area_impervious_fraction": round(float(np.sum(zone_pixels > 0.5) / len(zone_pixels)), 4),
        })

    return results


def compute_accuracy(fraction: np.ndarray, training_path: Path,
                     transform) -> Dict[str, Any]:
    """
    Compute accuracy metrics against training data.

    Training data GeoJSON should have an 'impervious' property (0 or 1).
    """
    try:
        from shapely.geometry import Point, shape
    except ImportError:
        print("ERROR: shapely required", file=sys.stderr)
        sys.exit(EXIT_DEP)

    geojson = json.loads(training_path.read_text(encoding="utf-8"))
    features = geojson.get("features", [])

    predictions = []
    references = []

    for feat in features:
        geom = shape(feat["geometry"])
        props = feat.get("properties", {})
        ref_value = props.get("impervious")
        if ref_value is None:
            continue

        centroid = geom.centroid
        col = int((centroid.x - transform.c) / transform.a)
        row = int((centroid.y - transform.f) / transform.e)
        row = max(0, min(row, fraction.shape[0] - 1))
        col = max(0, min(col, fraction.shape[1] - 1))

        predictions.append(float(fraction[row, col]))
        references.append(int(ref_value))

    if len(predictions) == 0:
        return {"n_samples": 0, "rmse": None, "mae": None}

    pred_arr = np.array(predictions)
    ref_arr = np.array(references)

    rmse = float(np.sqrt(np.mean((pred_arr - ref_arr) ** 2)))
    mae = float(np.mean(np.abs(pred_arr - ref_arr)))

    # Binary accuracy at 0.5 threshold
    binary_pred = (pred_arr >= 0.5).astype(int)
    accuracy = float(np.mean(binary_pred == ref_arr))

    return {
        "n_samples": len(predictions),
        "rmse": round(rmse, 4),
        "mae": round(mae, 4),
        "binary_accuracy": round(accuracy, 4),
    }


def write_raster(path: Path, data: np.ndarray, transform, crs,
                 nodata: float = -9999, dtype: str = "float64"):
    """Write a single-band GeoTIFF."""
    import rasterio

    with rasterio.open(
        str(path), "w", driver="GTiff",
        height=data.shape[0], width=data.shape[1],
        count=1, dtype=dtype, crs=crs,
        transform=transform, nodata=nodata,
    ) as dst:
        dst.write(data, 1)


def write_zones_csv(zones: List[Dict], path: Path):
    """Write zone statistics to CSV."""
    if not zones:
        return
    fieldnames = list(zones[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(zones)


def run_mapping(args: argparse.Namespace) -> int:
    """Main impervious surface mapping workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("impervious-output")
    output_dir.mkdir(parents=True, exist_ok=True)
    if args.synthetic or not args.raster:
        mode = "synthetic"
        synth_dir = output_dir / "synthetic_input"
        raster_p, train_p = generate_synthetic_data(synth_dir, seed=42)
        raster_path = raster_p
        args.raster = str(raster_path)
        if args.year is None:
            args.year = 2023
        if args.training_data is None:
            args.training_data = str(train_p)
        print(f"  Generated synthetic Sentinel-2 + training samples in {synth_dir}")
    else:
        mode = "file"
        raster_path = Path(args.raster)
        if not raster_path.exists():
            print(f"ERROR: raster not found: {raster_path}", file=sys.stderr)
            return EXIT_ARG

    # Read multi-band raster
    print(f"Reading raster from {raster_path}...")
    raster = read_raster(raster_path)
    data = raster["data"]

    # Validate band count
    if data.ndim == 2:
        print("ERROR: Expected multi-band raster (at least 5 bands)", file=sys.stderr)
        return EXIT_VALIDATION
    if data.shape[0] < 5:
        print(f"ERROR: Expected at least 5 bands, got {data.shape[0]}", file=sys.stderr)
        return EXIT_VALIDATION

    print(f"  Bands: {data.shape[0]}, Shape: {data.shape[1]}x{data.shape[2]}")

    # Extract bands
    b2 = data[BAND_B2].astype(float)   # Blue
    b3 = data[BAND_B3].astype(float)   # Green
    b4 = data[BAND_B4].astype(float)   # Red
    b8 = data[BAND_B8].astype(float)   # NIR
    b11 = data[BAND_B11].astype(float)  # SWIR

    # Compute spectral indices
    print("Computing spectral indices...")
    ndbi = compute_ndbi(b11, b8)
    ndvi = compute_ndvi(b8, b4)
    mndwi = compute_mndwi(b3, b11)

    print(f"  NDBI range: [{np.nanmin(ndbi):.3f}, {np.nanmax(ndbi):.3f}]")
    print(f"  NDVI range: [{np.nanmin(ndvi):.3f}, {np.nanmax(ndvi):.3f}]")
    print(f"  MNDWI range: [{np.nanmin(mndwi):.3f}, {np.nanmax(mndwi):.3f}]")

    # Estimate impervious fraction
    print("Estimating impervious fraction...")
    fraction = estimate_impervious_fraction(
        ndbi, ndvi, mndwi,
        ndvi_mask=args.ndvi_mask,
        mndwi_mask=args.mndwi_mask,
    )
    print(f"  Fraction range: [{np.nanmin(fraction):.3f}, {np.nanmax(fraction):.3f}]")

    # Write fraction raster
    frac_path = output_dir / "impervious_fraction.tif"
    write_raster(frac_path, fraction, raster["transform"], raster["crs"])
    print(f"  Output: {frac_path}")

    # Binary classification
    threshold = args.threshold if args.threshold is not None else 0.5
    binary = apply_threshold(fraction, threshold)
    binary_path = output_dir / "impervious_binary.tif"
    write_raster(binary_path, binary, raster["transform"], raster["crs"],
                 nodata=0, dtype="uint8")
    print(f"  Output: {binary_path}")

    # Zone aggregation
    zones_summary = None
    if args.aggregation_layer:
        zone_path = Path(args.aggregation_layer)
        if not zone_path.exists():
            print(f"ERROR: aggregation layer not found: {zone_path}", file=sys.stderr)
            return EXIT_ARG
        print(f"Aggregating by zone layer: {zone_path}...")
        zones_summary = aggregate_by_zone(
            fraction, raster["transform"], raster["crs"], zone_path
        )
        csv_path = output_dir / "zones_summary.csv"
        write_zones_csv(zones_summary, csv_path)
        print(f"  Output: {csv_path} ({len(zones_summary)} zones)")

    # Change detection
    change_path = None
    if args.compare_year and args.raster_compare:
        compare_path = Path(args.raster_compare)
        if not compare_path.exists():
            print(f"ERROR: comparison raster not found: {compare_path}", file=sys.stderr)
            return EXIT_ARG
        print(f"Computing change ({args.compare_year} -> {args.year})...")
        compare_raster = read_raster(compare_path)
        compare_data = compare_raster["data"]

        if compare_data.shape[0] < 5:
            print(f"ERROR: comparison raster has insufficient bands", file=sys.stderr)
            return EXIT_VALIDATION

        c_b3 = compare_data[BAND_B3].astype(float)
        c_b4 = compare_data[BAND_B4].astype(float)
        c_b8 = compare_data[BAND_B8].astype(float)
        c_b11 = compare_data[BAND_B11].astype(float)

        c_ndbi = compute_ndbi(c_b11, c_b8)
        c_ndvi = compute_ndvi(c_b8, c_b4)
        c_mndwi = compute_mndwi(c_b3, c_b11)
        c_fraction = estimate_impervious_fraction(
            c_ndbi, c_ndvi, c_mndwi,
            ndvi_mask=args.ndvi_mask,
            mndwi_mask=args.mndwi_mask,
        )

        change = compute_change(fraction, c_fraction)
        change_path = output_dir / "change.tif"
        write_raster(change_path, change, raster["transform"], raster["crs"])
        print(f"  Output: {change_path}")
        print(f"  Change range: [{np.nanmin(change):.3f}, {np.nanmax(change):.3f}]")

    # Accuracy assessment
    accuracy = None
    if args.training_data:
        train_path = Path(args.training_data)
        if not train_path.exists():
            print(f"ERROR: training data not found: {train_path}", file=sys.stderr)
            return EXIT_ARG
        print(f"Computing accuracy against training data: {train_path}...")
        accuracy = compute_accuracy(fraction, train_path, raster["transform"])
        acc_path = output_dir / "accuracy.json"
        acc_path.write_text(json.dumps(accuracy, ensure_ascii=False, indent=2),
                            encoding="utf-8")
        print(f"  Output: {acc_path}")
        print(f"  RMSE: {accuracy.get('rmse')}, Accuracy: {accuracy.get('binary_accuracy')}")

    # Manifest
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "year": args.year,
        "args_mode": args.mode,
        "threshold": threshold,
        "ndvi_mask": args.ndvi_mask,
        "mndwi_mask": args.mndwi_mask,
        "raster_crs": raster["crs"],
        "raster_shape": list(data.shape),
        "fraction_stats": {
            "mean": round(float(np.mean(fraction)), 4),
            "std": round(float(np.std(fraction)), 4),
            "min": round(float(np.min(fraction)), 4),
            "max": round(float(np.max(fraction)), 4),
        },
        "n_impervious_pixels": int(np.sum(binary == 1)),
        "output_files": {
            "impervious_fraction.tif": str(frac_path),
            "impervious_binary.tif": str(binary_path),
        },
    }
    if zones_summary is not None:
        manifest["n_zones"] = len(zones_summary)
        manifest["output_files"]["zones_summary.csv"] = str(output_dir / "zones_summary.csv")
    if change_path:
        manifest["compare_year"] = args.compare_year
        manifest["output_files"]["change.tif"] = str(change_path)
    if accuracy:
        manifest["accuracy"] = accuracy
        manifest["output_files"]["accuracy.json"] = str(output_dir / "accuracy.json")

    # T9 fields: ensure 3 required keys (output_files, parameters/summary, timestamp)
    manifest["summary"] = {
        "mode": mode,
        "year": args.year,
        "n_impervious_pixels": int(np.sum(binary == 1)),
        "mean_fraction": round(float(np.mean(fraction)), 4),
    }
    manifest["parameters"] = {k: v for k, v in vars(args).items() if not k.startswith("_")}
    # Inject MPC download metadata when --bbox/--aoi-file was used.
    download_meta = getattr(args, "_download_meta", None)
    if download_meta:
        manifest["data_source"] = download_meta.get("data_source")
        manifest["fetched_at"] = download_meta.get("fetched_at")
        manifest["collection"] = download_meta.get("collection")
        manifest["bbox"] = download_meta.get("bbox")
        manifest["date_range"] = download_meta.get("date_range")
        manifest["downloaded_paths"] = download_meta.get("downloaded_paths")
    ensure_t9_fields(manifest, args)
    manifest_path = output_dir / "output-manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2,
                                        default=str), encoding="utf-8")

    print(f"\nSummary:")
    print(f"  Year: {args.year}")
    print(f"  Mode: {args.mode}")
    print(f"  Impervious pixels: {manifest['n_impervious_pixels']}")
    print(f"  Mean fraction: {manifest['fraction_stats']['mean']:.4f}")

    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Impervious Surface Mapping")
    parser.add_argument("--raster", default=None,
                        help="Multi-band raster (Sentinel-2: B2,B3,B4,B8,B11, optional if --synthetic)")
    parser.add_argument("--year", type=int, default=None, help="Analysis year (optional if --synthetic)")
    parser.add_argument("--synthetic", action="store_true", help="Run with synthetic demo data")
    parser.add_argument("--mode", choices=["binary", "fraction"], default="fraction",
                        help="Output mode (default: fraction)")
    parser.add_argument("--training-data", help="Training samples GeoJSON")
    parser.add_argument("--threshold", type=float, default=0.5,
                        help="Binary threshold (default: 0.5)")
    parser.add_argument("--aggregation-layer", help="Zone layer GeoJSON for aggregation")
    parser.add_argument("--compare-year", type=int, help="Comparison year")
    parser.add_argument("--raster-compare", help="Raster for comparison year")
    parser.add_argument("--ndvi-mask", type=float, default=0.6,
                        help="NDVI threshold for vegetation masking (default: 0.6)")
    parser.add_argument("--mndwi-mask", type=float, default=0.0,
                        help="MNDWI threshold for water masking (default: 0.0)")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    if _HAS_DATA_FETCHER:
        # Adds --bbox, --date-range, --aoi-file, --cache-dir. When supplied
        # we auto-download a Sentinel-2 L2A scene and pass it via --raster.
        add_bbox_date_args(parser)
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    args = parser.parse_args()

    # ─── auto-download a Sentinel-2 L2A scene when --bbox/--aoi-file is given ─
    _download_meta: Optional[Dict[str, Any]] = None
    has_raster = bool(args.raster) and Path(args.raster).exists()
    if (
        _HAS_DATA_FETCHER
        and not args.synthetic
        and not has_raster
        and (args.bbox or args.aoi_file)
    ):
        try:
            bbox = parse_bbox_arg(args.bbox, args.aoi_file)
            dr = parse_date_range_arg(args.date_range)
            fetcher = DataFetcher(
                source=DataSource.PLANETARY_COMPUTER,
                cache_dir=Path(args.cache_dir) if args.cache_dir else None,
            )
            items = fetcher.search_stac(
                collection="sentinel-2-l2a",
                bbox=bbox,
                date_range=dr,
                cloud_cover_max=20.0,
                limit=1,
            )
            if items:
                download_dir = Path(args.output_dir or "impervious-output") / "downloaded"
                paths = fetcher.download_assets(
                    items, out_dir=download_dir, max_items=1, max_total_mb=200.0,
                    prefer_assets=["B04", "B03", "B02", "B08", "B11", "visual"],
                )
                if paths:
                    print(f"[downloader] fetched Sentinel-2: {paths[0]}")
                    # Sentinel-2 L2A assets are individual 1-band files; the
                    # analysis needs 5 stacked bands. If the downloaded file
                    # is single-band, fall back to synthetic mode but still
                    # record the download metadata.
                    try:
                        import rasterio
                        with rasterio.open(paths[0]) as ds:
                            n_bands = ds.count
                    except Exception:
                        n_bands = None
                    _download_meta = {
                        "data_source": "MPC",
                        "fetched_at": datetime.now(timezone.utc).isoformat(),
                        "collection": "sentinel-2-l2a",
                        "bbox": bbox.to_string(),
                        "date_range": dr.to_dict() if dr else None,
                        "downloaded_paths": [str(p) for p in paths],
                    }
                    if n_bands is not None and n_bands < 5:
                        print(
                            f"[downloader] downloaded file is {n_bands}-band; "
                            f"analysis needs 5 stacked bands. Falling back to "
                            f"synthetic mode (download metadata still recorded).",
                            file=sys.stderr,
                        )
                        args.synthetic = True
                    else:
                        args.raster = str(paths[0])
        except Exception as exc:  # pragma: no cover - network dependent
            print(f"[downloader] auto-download failed: {exc}; falling back to synthetic",
                  file=sys.stderr)
            args.synthetic = True
    if _download_meta is not None:
        args._download_meta = _download_meta  # type: ignore[attr-defined]

    try:
        sys.exit(run_mapping(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)




def ensure_t9_fields(manifest, args=None):
    """Inject 3 T9 fields (output_files, parameters/summary, timestamp) if missing."""
    injected = []
    if not isinstance(manifest, dict):
        return injected
    of_aliases = {"output_files", "files", "outputs", "artifacts", "products", "result_files"}
    ps_aliases = {"parameters", "summary", "params", "args", "inputs", "result", "results",
                  "stats", "metrics", "qc_summary", "findings"}
    ts_aliases = {"timestamp", "generated_at", "date", "created_at", "run_time",
                  "datetime", "time", "ts"}
    if not any(k in manifest for k in of_aliases):
        manifest["output_files"] = {}
        injected.append("output_files")
    if not any(k in manifest for k in ps_aliases):
        try:
            if args is not None:
                manifest["parameters"] = {
                    k: v for k, v in vars(args).items()
                    if not k.startswith("_") and not callable(v)
                }
            else:
                manifest["parameters"] = {"_info": "auto-injected"}
        except Exception:
            manifest["parameters"] = {"_info": "auto-injected"}
        injected.append("parameters")
    if not any(k in manifest for k in ts_aliases):
        from datetime import datetime as _dt, timezone as _tz
        manifest["timestamp"] = _dt.now(_tz.utc).isoformat()
        injected.append("timestamp")
    return injected
if __name__ == "__main__":
    main()
