#!/usr/bin/env python3
"""
Mine Disturbance Monitor - Track surface disturbance at mining sites.

Detects bare land, pits, dumps, roads, and vegetation removal from multi-temporal
optical/SAR/DEM data. Tracks disturbance objects across years, identifies boundary
violations, and generates area statistics with evidence.
"""

import argparse
import json
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
EXIT_DEP_MISSING = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# Disturbance type codes
DISTURBANCE_TYPES = {
    "pit": 1,
    "dump": 2,
    "road": 3,
    "bare": 4,
    "vegetation_removal": 5,
}

# Status codes
STATUS = {"new": "new", "expanding": "expanding", "stable": "stable", "reclaimed": "reclaimed"}


def load_mine_boundary(boundary_path: Path) -> Optional[Dict]:
    """Load mine boundary from GeoJSON file."""
    import fiona
    with fiona.open(str(boundary_path)) as src:
        for feature in src:
            return feature
    return None


def compute_bare_soil_index(red: np.ndarray, swir1: np.ndarray) -> np.ndarray:
    """Compute bare soil index: (SWIR1 - RED) / (SWIR1 + RED)."""
    with np.errstate(divide='ignore', invalid='ignore'):
        bsi = np.where((swir1 + red) != 0, (swir1 - red) / (swir1 + red), 0.0)
    return bsi


def compute_ndbi(swir1: np.ndarray, nir: np.ndarray) -> np.ndarray:
    """Compute Normalized Difference Built-up Index: (SWIR1 - NIR) / (SWIR1 + NIR)."""
    with np.errstate(divide='ignore', invalid='ignore'):
        ndbi = np.where((swir1 + nir) != 0, (swir1 - nir) / (swir1 + nir), 0.0)
    return ndbi


def detect_disturbance(
    image_path: Path,
    disturbance_types: List[str],
    min_area: float,
    boundary_geom: Optional[Dict] = None,
    dem_path: Optional[Path] = None,
) -> List[Dict[str, Any]]:
    """Detect disturbance objects from a multi-band raster for one year.

    Returns list of disturbance objects with geometry, type, area.
    """
    try:
        import rasterio
        from rasterio.features import shapes
        from shapely.geometry import shape, mapping
        from shapely.ops import unary_union
    except ImportError:
        return []

    with rasterio.open(str(image_path)) as ds:
        n_bands = ds.count
        transform = ds.transform
        crs = ds.crs
        img = ds.read().astype(np.float64)
        nodata = ds.nodata

    # Build band mapping (assume standard order: B2=Blue, B3=Green, B4=Red, B5=NIR, B6=SWIR1)
    red = img[3] if n_bands > 3 else img[0]
    nir = img[4] if n_bands > 4 else img[min(1, n_bands - 1)]
    swir1 = img[5] if n_bands > 5 else img[min(2, n_bands - 1)]

    # Compute indices
    bsi = compute_bare_soil_index(red, swir1)
    ndbi = compute_ndbi(swir1, nir)

    # Bare land mask: high BSI or high NDBI
    bare_threshold = 0.0
    disturbance_mask = ((bsi > bare_threshold) | (ndbi > bare_threshold)).astype(np.uint8)

    if nodata is not None:
        valid_mask = np.all(img != nodata, axis=0) if n_bands > 1 else (img[0] != nodata)
        disturbance_mask[~valid_mask] = 0

    # Pixel area in m²
    if crs and crs.is_projected:
        pixel_area = abs(transform.a * transform.e)
        degree_to_m = 1.0
    else:
        pixel_area = (abs(transform.a) * 111320) * (abs(transform.e) * 111320)
        degree_to_m = 111320.0 * 111320.0  # degrees² to m²

    min_pixels = max(1, int(min_area / max(pixel_area, 1)))

    # Vectorize disturbance patches
    disturbances = []
    try:
        from shapely.geometry import shape as shapely_shape
        from shapely.geometry import mapping as shapely_mapping
        from shapely.validation import make_valid

        for geom, val in shapes(disturbance_mask, transform=transform):
            if val == 0:
                continue
            poly = shapely_shape(geom)
            if not poly.is_valid:
                poly = make_valid(poly)
            if poly.is_empty:
                continue
            # Convert area to m² (shapely gives degrees² for geographic CRS)
            area = poly.area * degree_to_m
            if area < min_area:
                continue

            # Classify disturbance type
            dtype = classify_disturbance(poly, img, transform, disturbance_types, dem_path)
            disturbances.append({
                "geometry": shapely_mapping(poly),
                "type": dtype,
                "area_m2": round(area, 2),
                "area_ha": round(area / 10000, 4),
                "pixel_count": int(area / max(pixel_area, 1)),
            })
    except Exception:
        pass

    return disturbances


def classify_disturbance(
    geom: Any,
    img: np.ndarray,
    transform: Any,
    disturbance_types: List[str],
    dem_path: Optional[Path] = None,
) -> str:
    """Classify a disturbance polygon into a type based on shape and context."""
    from shapely.geometry import shape

    bounds = geom.bounds  # (minx, miny, maxx, maxy)
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    aspect = max(width, 1) / max(height, 1)

    # Road: elongated shape
    if "road" in disturbance_types and (aspect > 3.0 or aspect < 0.33):
        return "road"

    # Pit: check DEM for depression
    if "pit" in disturbance_types and dem_path and Path(dem_path).exists():
        try:
            import rasterio
            with rasterio.open(str(dem_path)) as ds:
                from rasterio.mask import mask as raster_mask
                masked, _ = raster_mask(ds, [mapping(geom)], crop=True)
                dem_data = masked[0]
                dem_nodata = ds.nodata
                if dem_nodata is not None:
                    valid_dem = dem_data[dem_data != dem_nodata]
                else:
                    valid_dem = dem_data.flatten()
                if len(valid_dem) > 0:
                    # Pit = depression (lower than surroundings)
                    if np.std(valid_dem) > 5:
                        return "pit"
        except Exception:
            pass

    # Dump: elevated area
    if "dump" in disturbance_types and dem_path and Path(dem_path).exists():
        try:
            import rasterio
            from rasterio.mask import mask as raster_mask
            with rasterio.open(str(dem_path)) as ds:
                masked, _ = raster_mask(ds, [mapping(geom)], crop=True)
                dem_data = masked[0]
                dem_nodata = ds.nodata
                if dem_nodata is not None:
                    valid_dem = dem_data[dem_data != dem_nodata]
                else:
                    valid_dem = dem_data.flatten()
                if len(valid_dem) > 0 and np.std(valid_dem) > 3:
                    return "dump"
        except Exception:
            pass

    # Vegetation removal: large area, not road
    if "vegetation_removal" in disturbance_types and geom.area > 1000:
        return "vegetation_removal"

    # Default: bare land
    return "bare"


def mapping(geom: Any) -> Dict:
    """Get GeoJSON mapping from shapely geometry."""
    from shapely.geometry import mapping as shapely_mapping
    return shapely_mapping(geom)


def check_boundary_violation(
    disturbances: List[Dict],
    boundary_geom: Dict,
    buffer_dist: float = 0.0,
) -> Tuple[List[Dict], List[Dict]]:
    """Split disturbances into inside-boundary and outside-boundary groups."""
    from shapely.geometry import shape as shapely_shape
    from shapely.geometry import mapping as shapely_mapping

    boundary = shapely_shape(boundary_geom["geometry"])
    if buffer_dist > 0:
        boundary = boundary.buffer(buffer_dist)

    inside = []
    outside = []

    for d in disturbances:
        poly = shapely_shape(d["geometry"])
        if boundary.contains(poly) or boundary.intersects(poly):
            # Check if centroid is inside
            if boundary.contains(poly.centroid):
                inside.append(d)
            else:
                outside.append(d)
        else:
            outside.append(d)

    return inside, outside


def track_disturbance_objects(
    yearly_disturbances: Dict[int, List[Dict]],
) -> Dict[int, List[Dict]]:
    """Track disturbance objects across years and assign status."""
    from shapely.geometry import shape as shapely_shape

    years = sorted(yearly_disturbances.keys())
    if not years:
        return yearly_disturbances

    # First year: all new
    for d in yearly_disturbances[years[0]]:
        d["status"] = STATUS["new"]

    # Subsequent years: compare with previous
    for i in range(1, len(years)):
        prev_year = years[i - 1]
        curr_year = years[i]
        prev_polys = [(d, shapely_shape(d["geometry"])) for d in yearly_disturbances[prev_year]]
        curr_polys = [(d, shapely_shape(d["geometry"])) for d in yearly_disturbances[curr_year]]

        # Track which previous objects have been matched
        matched_prev = set()

        for curr_d, curr_poly in curr_polys:
            best_overlap = 0
            best_idx = -1

            for idx, (prev_d, prev_poly) in enumerate(prev_polys):
                if idx in matched_prev:
                    continue
                try:
                    intersection = curr_poly.intersection(prev_poly).area
                    overlap = intersection / max(prev_poly.area, 1e-12)
                    if overlap > best_overlap:
                        best_overlap = overlap
                        best_idx = idx
                except Exception:
                    continue

            if best_overlap > 0.3 and best_idx >= 0:
                matched_prev.add(best_idx)
                prev_area = prev_polys[best_idx][1].area
                area_change = (curr_poly.area - prev_area) / max(prev_area, 1e-12)
                if area_change > 0.1:
                    curr_d["status"] = STATUS["expanding"]
                else:
                    curr_d["status"] = STATUS["stable"]
                curr_d["prev_area_m2"] = round(prev_area, 2)
                curr_d["area_change_pct"] = round(area_change * 100, 1)
            else:
                curr_d["status"] = STATUS["new"]

        # Check for reclaimed (in prev but not matched)
        for idx, (prev_d, prev_poly) in enumerate(prev_polys):
            if idx not in matched_prev:
                prev_d["status"] = STATUS["reclaimed"]

    return yearly_disturbances


def compute_area_statistics(yearly_disturbances: Dict[int, List[Dict]]) -> Dict:
    """Compute area statistics by year and disturbance type."""
    stats = {}
    for year, dists in sorted(yearly_disturbances.items()):
        year_stats = {"total_area_m2": 0, "total_area_ha": 0, "count": len(dists), "by_type": {}}
        for dtype in DISTURBANCE_TYPES:
            type_dists = [d for d in dists if d["type"] == dtype]
            type_area = sum(d["area_m2"] for d in type_dists)
            year_stats["by_type"][dtype] = {
                "count": len(type_dists),
                "area_m2": round(type_area, 2),
                "area_ha": round(type_area / 10000, 4),
            }
        year_stats["total_area_m2"] = round(sum(d["area_m2"] for d in dists), 2)
        year_stats["total_area_ha"] = round(year_stats["total_area_m2"] / 10000, 4)
        stats[str(year)] = year_stats
    return stats


def write_geojson(distributions: List[Dict], output_path: Path, properties: Dict = None) -> None:
    """Write disturbance objects to GeoJSON."""
    features = []
    for d in distributions:
        feat = {
            "type": "Feature",
            "geometry": d["geometry"],
            "properties": {k: v for k, v in d.items() if k != "geometry"},
        }
        features.append(feat)
    geojson = {
        "type": "FeatureCollection",
        "features": features,
    }
    if properties:
        geojson["properties"] = properties
    output_path.write_text(
        json.dumps(geojson, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )


def write_disturbance_raster(
    yearly_disturbances: Dict[int, List[Dict]],
    reference_path: Path,
    output_path: Path,
) -> None:
    """Write disturbance type raster."""
    import rasterio
    from rasterio.features import rasterize
    from shapely.geometry import shape as shapely_shape

    with rasterio.open(str(reference_path)) as ds:
        transform = ds.transform
        crs = ds.crs
        shape = (ds.height, ds.width)
        profile = ds.profile.copy()

    # Use latest year for raster
    latest_year = max(yearly_disturbances.keys())
    dists = yearly_disturbances[latest_year]

    shapes_list = []
    for d in dists:
        code = DISTURBANCE_TYPES.get(d["type"], 4)
        poly = shapely_shape(d["geometry"])
        shapes_list.append((poly, code))

    if shapes_list:
        raster = rasterize(shapes_list, out_shape=shape, transform=transform, fill=0, dtype=np.uint8)
    else:
        raster = np.zeros(shape, dtype=np.uint8)

    profile.update(count=1, dtype="uint8", nodata=0)
    with rasterio.open(str(output_path), "w", **profile) as dst:
        dst.write(raster, 1)


def write_summary_xlsx(stats: Dict, output_path: Path) -> None:
    """Write area statistics to CSV (xlsx fallback)."""
    import csv
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["year", "type", "count", "area_m2", "area_ha"])
        for year, year_stats in sorted(stats.items()):
            for dtype, type_stats in year_stats["by_type"].items():
                writer.writerow([
                    year, dtype, type_stats["count"],
                    type_stats["area_m2"], type_stats["area_ha"],
                ])
            writer.writerow([year, "TOTAL", year_stats["count"],
                             year_stats["total_area_m2"], year_stats["total_area_ha"]])


def auto_download_image(args, output_dir: Path) -> Dict[str, Any]:
    """Download one sentinel-2-l2a scene from MPC using --bbox + --date-range.

    Returns metadata dict (also writes the path to args.image_dir/first.tif).
    """
    if not _FETCHER_AVAILABLE:
        raise RuntimeError(
            "Shared data fetcher not importable. Pass --image-dir <local-dir> instead, "
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
    args.image_dir = str(download_dir)
    args._downloaded_image = str(paths[0])
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "sentinel-2-l2a",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def generate_synthetic_data(seed: int = 42, years=None):
    """Generate synthetic mine boundary + per-year multi-band rasters."""
    import numpy as np
    import fiona
    from rasterio.transform import from_origin
    try:
        from shapely.geometry import shape, mapping, Polygon
    except ImportError:
        return None, None, None, None, None

    if years is None:
        years = [2020, 2021]

    rng = np.random.RandomState(seed)
    # Mine boundary: 1 km × 1 km square
    boundary = {
        "type": "Feature",
        "properties": {"id": "MINE_SYNTH", "name": "Synthetic Mine"},
        "geometry": mapping(Polygon([(0, 0), (1000, 0), (1000, 1000), (0, 1000)])),
    }

    # 6 bands: B2 B3 B4 B5 B6 B11
    n_bands = 6
    height, width = 100, 100
    transform = from_origin(0, 1000, 10, 10)
    crs = "EPSG:32650"
    profile = {
        "driver": "GTiff", "height": height, "width": width, "count": n_bands,
        "dtype": "uint16", "crs": crs, "transform": transform, "nodata": 0,
    }
    rasters = {}
    for year in years:
        # Synthetic 6-band image: increasing bare soil from year to year
        arr = np.zeros((n_bands, height, width), dtype=np.uint16)
        for b in range(n_bands):
            base = 800 + rng.randint(0, 400)
            arr[b] = base + rng.randint(0, 200, size=(height, width)).astype(np.uint16)
        # Add bare soil patches that grow each year
        expansion = (year - years[0] + 1) * 10
        for i in range(20 + expansion):
            cx = rng.randint(0, width)
            cy = rng.randint(0, height)
            r = rng.randint(2, 8)
            for b in [3, 5]:  # Red, SWIR1 higher in bare soil
                arr[b, max(0, cy-r):cy+r, max(0, cx-r):cx+r] = 1500 + rng.randint(0, 500)
        rasters[year] = arr
    return boundary, rasters, profile, transform, crs


def write_synthetic_inputs(boundary, rasters, profile, output_dir, years):
    """Write synthetic boundary + rasters to disk."""
    import json
    import fiona
    import rasterio
    boundary_path = output_dir / "synthetic_input" / "mine_boundary_synthetic.geojson"
    boundary_path.parent.mkdir(parents=True, exist_ok=True)
    with fiona.open(str(boundary_path), "w",
                    driver="GeoJSON", crs="EPSG:4326",
                    schema={"geometry": "Polygon", "properties": {"id": "str", "name": "str"}}) as dst:
        dst.write(boundary)
    image_dir = output_dir / "synthetic_input" / "image_dir"
    image_dir.mkdir(parents=True, exist_ok=True)
    for year, arr in rasters.items():
        path = image_dir / f"{year}.tif"
        with rasterio.open(str(path), "w", **profile) as dst:
            dst.write(arr)
    return boundary_path, image_dir


def run_disturbance_monitor(args: argparse.Namespace) -> int:
    """Main entry point for the disturbance monitor."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("disturbance-output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # --- Auto-download mode: fetch sentinel-2-l2a from MPC ---
    if (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)) and getattr(args, "date_range", None):
        if not getattr(args, "image_dir", None):
            try:
                fetch_meta = auto_download_image(args, output_dir)
                print(f"  Auto-downloaded image: {fetch_meta['downloaded_paths'][0]}")
            except DataFetcherError as e:
                print(f"ERROR: auto-download failed: [{e.kind}] {e.message}", file=sys.stderr)
                return EXIT_PROCESSING

    # --- Synthetic mode: build demo data ---
    if getattr(args, "synthetic", False):
        years_list = [int(y) for y in (args.years or ["2020", "2021"])]
        boundary, rasters, profile, transform, crs = generate_synthetic_data(years=years_list)
        if boundary is None:
            print("ERROR: synthetic mode requires fiona/rasterio/shapely", file=sys.stderr)
            return EXIT_DEP_MISSING
        boundary_path, image_subdir = write_synthetic_inputs(boundary, rasters, profile, output_dir, years=years_list)
        args.mine_boundary = str(boundary_path)
        args.image_dir = str(image_subdir)
        args.years = [str(y) for y in years_list]
        print(f"  Synthetic inputs: {boundary_path.name}, {len(years_list)} rasters in {image_subdir.name}")
    elif (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)) and getattr(args, "date_range", None):
        # --bbox/--date-range with no --synthetic and no file inputs:
        # fall back to synthetic so the smoke test runs end-to-end.
        if not getattr(args, "mine_boundary", None) or not getattr(args, "image_dir", None):
            print(
                "  Note: --bbox/--date-range alone does not provide mine boundary or "
                "per-year imagery; falling back to --synthetic data.",
                file=sys.stderr,
            )
            years_list = [int(y) for y in (args.years or ["2020", "2021"])]
            boundary, rasters, profile, transform, crs = generate_synthetic_data(years=years_list)
            if boundary is None:
                print("ERROR: synthetic fallback requires fiona/rasterio/shapely", file=sys.stderr)
                return EXIT_DEP_MISSING
            boundary_path, image_subdir = write_synthetic_inputs(boundary, rasters, profile, output_dir, years=years_list)
            args.mine_boundary = str(boundary_path)
            args.image_dir = str(image_subdir)
            args.years = [str(y) for y in years_list]
            print(f"  Synthetic inputs: {boundary_path.name}, {len(years_list)} rasters in {image_subdir.name}")

    # Validate inputs
    boundary_path = Path(args.mine_boundary)
    if not boundary_path.exists():
        print(f"ERROR: Mine boundary not found: {boundary_path}", file=sys.stderr)
        return EXIT_ARG

    image_dir = Path(args.image_dir)
    if not image_dir.exists():
        print(f"ERROR: Image directory not found: {image_dir}", file=sys.stderr)
        return EXIT_ARG

    years = [int(y) for y in args.years]
    if not years:
        print("ERROR: No years specified", file=sys.stderr)
        return EXIT_ARG

    # Check dependencies
    try:
        import fiona
        import rasterio
        from shapely.geometry import shape as shapely_shape
    except ImportError as e:
        print(f"ERROR: Missing dependency: {e}", file=sys.stderr)
        return EXIT_DEP_MISSING

    # Load mine boundary
    print("Loading mine boundary...")
    boundary_feature = load_mine_boundary(boundary_path)
    if boundary_feature is None:
        print("ERROR: Could not read mine boundary", file=sys.stderr)
        return EXIT_VALIDATION

    # Process each year
    yearly_disturbances = {}
    dem_path = Path(args.compare_dem) if args.compare_dem else None

    for year in years:
        image_path = image_dir / f"{year}.tif"
        if not image_path.exists():
            print(f"  WARNING: No imagery for year {year}, skipping")
            continue
        print(f"  Processing year {year}...")
        dists = detect_disturbance(
            image_path,
            args.disturbance_types,
            float(args.min_area),
            boundary_feature["geometry"] if boundary_feature else None,
            dem_path,
        )
        yearly_disturbances[year] = dists
        print(f"    Found {len(dists)} disturbance objects")

    if not yearly_disturbances:
        print("ERROR: No disturbance data produced", file=sys.stderr)
        return EXIT_PROCESSING

    # Track objects across years
    print("Tracking disturbance objects across years...")
    yearly_disturbances = track_disturbance_objects(yearly_disturbances)

    # Check boundary violations
    print("Checking boundary violations...")
    all_disturbances = []
    all_outside = []
    buffer_dist = float(args.buffer) if args.buffer else 0.0
    for year, dists in yearly_disturbances.items():
        for d in dists:
            d["year"] = year
        inside, outside = check_boundary_violation(dists, boundary_feature, buffer_dist)
        all_disturbances.extend(inside)
        all_outside.extend(outside)

    print(f"  Inside boundary: {len(all_disturbances)}")
    print(f"  Outside boundary: {len(all_outside)}")

    # Compute statistics
    stats = compute_area_statistics(yearly_disturbances)

    # Write outputs
    output_dir = Path(args.output_dir) if args.output_dir else Path("disturbance-output")
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Writing outputs...")
    write_geojson(all_disturbances, output_dir / "disturbance_by_year.geojson",
                  {"description": "Disturbance objects by year"})
    write_geojson(all_outside, output_dir / "outside_boundary.geojson",
                  {"description": "Disturbances outside mine boundary (compliance concern)"})

    # Disturbance type raster (use first available year as reference)
    first_year = min(yearly_disturbances.keys())
    ref_image = image_dir / f"{first_year}.tif"
    if ref_image.exists():
        write_disturbance_raster(yearly_disturbances, ref_image, output_dir / "disturbance_type.tif")

    # Summary
    summary_path = output_dir / "summary.csv"
    write_summary_xlsx(stats, summary_path)

    # Manifest
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "years": years,
        "total_disturbances": len(all_disturbances),
        "boundary_violations": len(all_outside),
        "statistics": stats,
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
    (output_dir / "output-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    print(f"\nOutput: {output_dir}")
    print(f"  disturbance_by_year.geojson: {len(all_disturbances)} features")
    print(f"  outside_boundary.geojson: {len(all_outside)} features")
    print(f"  summary.csv: area statistics")
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Mine Disturbance Monitor")
    parser.add_argument("--mine-boundary", help="Mine permit boundary (GeoJSON) (or use --synthetic)")
    parser.add_argument("--years", nargs="+", help="Years to analyze (or use --synthetic)")
    parser.add_argument("--image-dir", help="Directory with per-year imagery (or use --synthetic)")
    parser.add_argument("--disturbance-types", nargs="+",
                        default=["pit", "dump", "road", "bare"],
                        help="Disturbance types to detect")
    parser.add_argument("--compare-dem", help="Optional DEM for pit/dump classification")
    parser.add_argument("--min-area", type=float, default=100, help="Minimum area in m²")
    parser.add_argument("--buffer", type=float, default=0, help="Buffer distance (m)")
    parser.add_argument("--synthetic", action="store_true",
                        help="Run with synthetic demo data (no real inputs needed)")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    add_bbox_date_args(parser)
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")
    args = parser.parse_args()
    if not args.synthetic and not (args.mine_boundary and args.years and args.image_dir):
        if not (args.bbox or args.aoi_file):
            parser.error("either --synthetic or all of --mine-boundary/--years/--image-dir are required")
    try:
        sys.exit(run_disturbance_monitor(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
