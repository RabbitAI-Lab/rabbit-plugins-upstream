#!/usr/bin/env python3
"""
Agricultural Disaster Assessment - Crop damage estimation.

Fuses crop distribution, hazard intensity, and vegetation anomaly
to estimate agricultural disaster impact and damage severity.

Exit codes:
    0 = success
    2 = argument error
    3 = dependency missing
    6 = data validation failure
    7 = processing failure
"""

import argparse
import json
import os
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

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


def read_raster(path: Path) -> Dict[str, Any]:
    """Read raster data and metadata."""
    try:
        import rasterio
    except ImportError:
        print("ERROR: rasterio required", file=sys.stderr)
        sys.exit(EXIT_DEP)

    with rasterio.open(path) as ds:
        data = ds.read(1)
        return {
            "data": data,
            "crs": str(ds.crs) if ds.crs else None,
            "transform": ds.transform,
            "nodata": ds.nodata,
            "shape": data.shape,
            "bounds": list(ds.bounds),
        }


def compute_ndvi_anomaly(baseline_ndvi: np.ndarray, post_ndvi: np.ndarray,
                          nodata: float = None) -> np.ndarray:
    """
    Compute NDVI anomaly as relative change.

    anomaly = (post - baseline) / (|baseline| + epsilon)
    """
    eps = 1e-6
    mask = np.ones_like(baseline_ndvi, dtype=bool)

    if nodata is not None:
        mask &= (baseline_ndvi != nodata) & (post_ndvi != nodata)

    # Also mask invalid values
    mask &= np.isfinite(baseline_ndvi) & np.isfinite(post_ndvi)
    mask &= (np.abs(baseline_ndvi) > eps)

    anomaly = np.full_like(baseline_ndvi, np.nan)
    anomaly[mask] = (post_ndvi[mask] - baseline_ndvi[mask]) / (np.abs(baseline_ndvi[mask]) + eps)

    return anomaly


def classify_damage(hazard_intensity: np.ndarray, ndvi_anomaly: np.ndarray,
                    crop_mask: np.ndarray, hazard_threshold: float = 0.3,
                    anomaly_threshold: float = -0.3) -> np.ndarray:
    """
    Classify damage severity based on hazard and NDVI anomaly.

    Damage levels:
        0 = no crop (not in crop mask)
        1 = no damage (hazard below threshold or anomaly above threshold)
        2 = mild damage (hazard above threshold, anomaly slightly below)
        3 = moderate damage
        4 = severe damage (hazard high, anomaly very low)
    """
    damage = np.zeros_like(hazard_intensity, dtype=np.uint8)

    # Only assess crop pixels
    crop_pixels = crop_mask > 0
    damage[~crop_pixels] = 0

    # Normalize hazard to [0, 1] range
    h_max = np.nanmax(hazard_intensity)
    h_min = np.nanmin(hazard_intensity)
    h_range = h_max - h_min if h_max > h_min else 1
    hazard_norm = (hazard_intensity - h_min) / h_range

    # Classify
    for i in range(damage.shape[0]):
        for j in range(damage.shape[1]):
            if not crop_pixels[i, j]:
                continue

            h = hazard_norm[i, j]
            a = ndvi_anomaly[i, j]

            if h < hazard_threshold or np.isnan(a):
                damage[i, j] = 1  # no damage
            elif a < anomaly_threshold * 1.5:
                damage[i, j] = 4  # severe
            elif a < anomaly_threshold:
                damage[i, j] = 3  # moderate
            else:
                damage[i, j] = 2  # mild

    return damage


def generate_synthetic_data(seed: int = 42):
    """Generate synthetic agricultural-disaster inputs.

    Returns a dict with raster paths and a label (in-memory). All rasters
    share shape (60, 60), float32 dtype, EPSG:4326, and 0.001-deg transform.
    """
    try:
        import rasterio
        from rasterio.transform import from_origin
    except ImportError:
        print("ERROR: rasterio required", file=sys.stderr)
        sys.exit(EXIT_DEP)

    rng = np.random.RandomState(seed)
    transform = from_origin(0, 60, 0.001, 0.001)  # 60 cells of 0.001 deg
    crs = "EPSG:4326"
    h, w = 60, 60

    # Crop mask: ~60% pixels are crops (binary 0/1)
    crop_mask = (rng.uniform(0, 1, (h, w)) < 0.6).astype(np.float32)
    # Hazard intensity: 0..1, with a cluster of high values in the center
    yy, xx = np.mgrid[0:h, 0:w]
    hazard = np.exp(-((xx - 30) ** 2 + (yy - 30) ** 2) / (2 * 12 ** 2)).astype(np.float32)
    hazard = hazard + rng.normal(0, 0.05, (h, w)).astype(np.float32)
    hazard = np.clip(hazard, 0.0, 1.0)
    # Baseline NDVI: healthy vegetation 0.4-0.8
    baseline = rng.uniform(0.4, 0.8, (h, w)).astype(np.float32)
    # Post NDVI: drop in damaged areas, mild drop elsewhere
    drop = (rng.uniform(0.05, 0.4, (h, w)) * hazard).astype(np.float32)
    post = np.clip(baseline - drop, 0.0, 1.0).astype(np.float32)

    return {
        "transform": transform,
        "crs": crs,
        "shape": (h, w),
        "crop_mask": crop_mask,
        "hazard": hazard,
        "baseline_ndvi": baseline,
        "post_ndvi": post,
    }


def write_synthetic_rasters(synth: Dict, out_dir: Path) -> Dict[str, str]:
    """Write the synthetic dict to GeoTIFF files. Returns path map."""
    try:
        import rasterio
    except ImportError:
        print("ERROR: rasterio required", file=sys.stderr)
        sys.exit(EXIT_DEP)

    out_dir.mkdir(parents=True, exist_ok=True)
    paths = {}
    for key in ("crop_mask", "hazard", "baseline_ndvi", "post_ndvi"):
        arr = synth[key]
        p = out_dir / f"{key}.tif"
        with rasterio.open(
            str(p), "w", driver="GTiff",
            height=arr.shape[0], width=arr.shape[1],
            count=1, dtype="float32", crs=synth["crs"],
            transform=synth["transform"], nodata=None,
        ) as dst:
            dst.write(arr.astype(np.float32), 1)
        paths[key] = str(p)
    return paths


def vectorize_damage(damage: np.ndarray, crop_mask: np.ndarray,
                     transform, crs, min_area: float = 0) -> List[Dict]:
    """Convert damage raster to vector features."""
    try:
        import rasterio.features
        from shapely.geometry import shape, mapping
    except ImportError:
        print("ERROR: rasterio/shapely required", file=sys.stderr)
        sys.exit(EXIT_DEP)

    features = []
    # Only vectorize damaged pixels (damage >= 2)
    damage_mask = (damage >= 2).astype('uint8')

    shapes = rasterio.features.shapes(damage_mask, transform=transform)
    for geom, val in shapes:
        if val != 1:
            continue
        poly = shape(geom)
        if poly.area < min_area:
            continue

        # Get damage level at centroid
        from shapely.geometry import Point
        centroid = poly.centroid
        col = int((centroid.x - transform.c) / transform.a)
        row = int((centroid.y - transform.f) / transform.e)
        row = max(0, min(row, damage.shape[0] - 1))
        col = max(0, min(col, damage.shape[1] - 1))

        dmg_level = int(damage[row, col])

        features.append({
            "type": "Feature",
            "geometry": mapping(poly),
            "properties": {
                "damage_level": dmg_level,
                "damage_label": {2: "mild", 3: "moderate", 4: "severe"}.get(dmg_level, "unknown"),
                "area_m2": round(poly.area, 2),
            },
        })

    return features


def auto_download_image(args, output_dir: Path) -> Dict[str, Any]:
    """Download one sentinel-2-l2a scene from MPC using --bbox + --date-range.

    Returns metadata dict (also writes the path back to args.image).
    """
    if not _FETCHER_AVAILABLE:
        raise RuntimeError(
            "Shared data fetcher not importable. Pass --image <local.tif> instead, "
            "or ensure _geoskill_data_fetcher is on sys.path."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_image requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        raise RuntimeError("auto_download_image requires --date-range")
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
        prefer_assets=['B04', 'B08', 'B02'],
    )
    if not paths:
        raise RuntimeError("Download returned no files")
    args.image = str(paths[0])
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "sentinel-2-l2a",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def run_assessment(args: argparse.Namespace) -> int:
    """Main assessment workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("disaster-output")

    use_synthetic = bool(getattr(args, "synthetic", False))
    mode = "synthetic" if use_synthetic else "file"

    # --- Auto-download mode: fetch sentinel-2-l2a from MPC ---
    # (Skip when --synthetic is set to allow synthetic demo with bbox+date-range)
    if (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)) and getattr(args, "date_range", None) and not use_synthetic:
        if not getattr(args, "image", None):
            try:
                fetch_meta = auto_download_image(args, output_dir)
                mode = "auto_download"
                print(f"  Auto-downloaded image: {args.image}")
            except DataFetcherError as e:
                print(f"ERROR: auto-download failed: [{e.kind}] {e.message}", file=sys.stderr)
                return EXIT_PROCESSING if 'EXIT_PROCESSING' in dir() else 7
    output_dir.mkdir(parents=True, exist_ok=True)

    if use_synthetic:
        print("Running in synthetic demo mode (seed=42)...")
        synth = generate_synthetic_data(seed=42)
        synth_dir = output_dir / "synthetic_input"
        synth_paths = write_synthetic_rasters(synth, synth_dir)
        crop_path = Path(synth_paths["crop_mask"])
        hazard_path = Path(synth_paths["hazard"])
        baseline_path = Path(synth_paths["baseline_ndvi"])
        post_path = Path(synth_paths["post_ndvi"])
    else:
        crop_path = Path(args.crop_map)
        hazard_path = Path(args.hazard_raster)
        baseline_path = Path(args.baseline_ndvi)
        post_path = Path(args.post_ndvi)
        for p, name in [(crop_path, "crop map"), (hazard_path, "hazard raster"),
                        (baseline_path, "baseline NDVI"), (post_path, "post NDVI")]:
            if not p.exists():
                print(f"ERROR: {name} not found: {p}", file=sys.stderr)
                return EXIT_ARG

    # Read inputs
    print(f"Reading crop map from {crop_path}...")
    crop_raster = read_raster(crop_path)
    crop_data = crop_raster["data"]

    print(f"Reading hazard raster from {hazard_path}...")
    hazard_raster = read_raster(hazard_path)
    hazard_data = hazard_raster["data"]

    print(f"Reading baseline NDVI from {baseline_path}...")
    baseline_raster = read_raster(baseline_path)
    baseline_data = baseline_raster["data"]

    print(f"Reading post-disaster NDVI from {post_path}...")
    post_raster = read_raster(post_path)
    post_data = post_raster["data"]

    # Validate shapes match
    shapes = [crop_data.shape, hazard_data.shape, baseline_data.shape, post_data.shape]
    if len(set(shapes)) > 1:
        print(f"ERROR: Shape mismatch: {shapes}", file=sys.stderr)
        return EXIT_VALIDATION

    # Compute NDVI anomaly
    print("Computing NDVI anomaly...")
    anomaly = compute_ndvi_anomaly(baseline_data, post_data,
                                    nodata=baseline_raster["nodata"])

    # Classify damage
    print("Classifying damage...")
    damage = classify_damage(
        hazard_data, anomaly, crop_data,
        hazard_threshold=args.hazard_threshold,
        anomaly_threshold=args.anomaly_threshold
    )

    # Write damage raster
    print("Writing damage raster...")
    import rasterio
    damage_path = output_dir / "affected_crops.tif"
    with rasterio.open(
        str(damage_path), "w", driver="GTiff",
        height=damage.shape[0], width=damage.shape[1],
        count=1, dtype="uint8", crs=crop_raster["crs"],
        transform=crop_raster["transform"], nodata=0,
    ) as dst:
        dst.write(damage, 1)
    print(f"  Output: {damage_path}")

    # Vectorize
    print("Vectorizing damaged fields...")
    features = vectorize_damage(
        damage, crop_data, crop_raster["transform"], crop_raster["crs"],
        min_area=args.min_area
    )

    damage_path_geojson = output_dir / "field_damage.geojson"
    geojson = {"type": "FeatureCollection", "features": features}
    damage_path_geojson.write_text(json.dumps(geojson, ensure_ascii=False), encoding="utf-8")
    print(f"  Output: {damage_path_geojson} ({len(features)} features)")

    # Statistics
    stats = compute_statistics(damage, crop_data)

    # Generate report
    generate_report(stats, output_dir, args, len(features))

    # Manifest
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "parameters": vars(args),
        "crop_map": str(crop_path),
        "hazard_raster": str(hazard_path),
        "baseline_ndvi": str(baseline_path),
        "post_ndvi": str(post_path),
        "statistics": stats,
        "n_damaged_fields": len(features),
        "summary": {
            "mode": mode,
            "n_outputs": 3,
            "crop_pixels": stats["crop_pixels"],
            "damaged_pixels": stats["damaged_pixels"],
            "n_damaged_fields": len(features),
        },
        "output_files": {
            "affected_crops.tif": str(damage_path),
            "field_damage.geojson": str(damage_path_geojson),
            "report.html": str(output_dir / "report.html"),
        },
    }
    manifest_path = output_dir / "output-manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\nSummary:")
    print(f"  Mode: {mode}")
    print(f"  Crop pixels: {stats['crop_pixels']}")
    print(f"  Damaged pixels: {stats['damaged_pixels']}")
    print(f"  Mild: {stats['mild']}, Moderate: {stats['moderate']}, Severe: {stats['severe']}")
    print(f"  Damaged fields: {len(features)}")

    return EXIT_OK


def compute_statistics(damage: np.ndarray, crop_mask: np.ndarray) -> Dict:
    """Compute damage statistics."""
    crop_pixels = int((crop_mask > 0).sum())
    damaged_pixels = int(((damage >= 2) & (crop_mask > 0)).sum())
    mild = int(((damage == 2) & (crop_mask > 0)).sum())
    moderate = int(((damage == 3) & (crop_mask > 0)).sum())
    severe = int(((damage == 4) & (crop_mask > 0)).sum())

    return {
        "crop_pixels": crop_pixels,
        "damaged_pixels": damaged_pixels,
        "damage_fraction": round(damaged_pixels / crop_pixels, 4) if crop_pixels > 0 else 0,
        "mild": mild,
        "moderate": moderate,
        "severe": severe,
    }


def generate_report(stats: Dict, output_dir: Path, args: argparse.Namespace, n_fields: int):
    """Generate HTML report."""
    now = datetime.now(timezone.utc).isoformat()

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><title>Agricultural Disaster Assessment</title>
<style>
body{{font-family:sans-serif;max-width:900px;margin:20px auto;padding:0 20px}}
h1{{color:#1a237e}}.summary{{background:#e3f2fd;padding:15px;border-radius:8px}}
table{{border-collapse:collapse;width:100%}}
th,td{{border:1px solid #bbdefb;padding:8px;text-align:left}}
th{{background:#bbdefb}}
</style></head>
<body>
<h1>Agricultural Disaster Assessment Report</h1>
<p>Generated: {now}</p>
<div class="summary">
<h2>Summary</h2>
<table>
<tr><td>Crop pixels</td><td>{stats['crop_pixels']}</td></tr>
<tr><td>Damaged pixels</td><td>{stats['damaged_pixels']} ({stats['damage_fraction']*100:.1f}%)</td></tr>
<tr><td>Mild damage</td><td>{stats['mild']}</td></tr>
<tr><td>Moderate damage</td><td>{stats['moderate']}</td></tr>
<tr><td>Severe damage</td><td>{stats['severe']}</td></tr>
<tr><td>Damaged fields</td><td>{n_fields}</td></tr>
</table>
</div>
</body></html>"""

    (output_dir / "report.html").write_text(html, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Agricultural Disaster Assessment")
    parser.add_argument("--crop-map", required=False, default=None,
                        help="Crop distribution raster (not needed with --synthetic)")
    parser.add_argument("--hazard-raster", required=False, default=None,
                        help="Hazard intensity raster (not needed with --synthetic)")
    parser.add_argument("--baseline-ndvi", required=False, default=None,
                        help="Baseline NDVI (normal year; not needed with --synthetic)")
    parser.add_argument("--post-ndvi", required=False, default=None,
                        help="Post-disaster NDVI (not needed with --synthetic)")
    parser.add_argument("--synthetic", action="store_true",
                        help="Run with synthetic demo data (seed=42)")
    parser.add_argument("--hazard-threshold", type=float, default=0.3,
                        help="Hazard intensity threshold (default: 0.3)")
    parser.add_argument("--anomaly-threshold", type=float, default=-0.3,
                        help="NDVI anomaly threshold (default: -0.3)")
    parser.add_argument("--min-area", type=float, default=0,
                        help="Minimum field area filter")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    add_bbox_date_args(parser)

    args = parser.parse_args()

    # If not synthetic, all file args are required
    if not args.synthetic:
        missing = [name for name, val in [
            ("--crop-map", args.crop_map),
            ("--hazard-raster", args.hazard_raster),
            ("--baseline-ndvi", args.baseline_ndvi),
            ("--post-ndvi", args.post_ndvi),
        ] if val is None]
        if missing:
            parser.error(f"the following arguments are required (unless --synthetic): {' '.join(missing)}")

    try:
        sys.exit(run_assessment(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
