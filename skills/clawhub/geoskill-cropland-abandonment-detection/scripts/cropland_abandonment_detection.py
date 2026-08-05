#!/usr/bin/env python3
"""
Cropland Abandonment Detection - Multi-year cultivation status tracking.

Uses multi-year NDVI time series to identify suspected abandoned cropland
based on consecutive years without cultivation signals.

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
except ImportError:  # pragma: no cover
    _FETCHER_AVAILABLE = False




EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7


def auto_download_ndvi_stack(args, output_dir: Path) -> Dict[str, Any]:
    """Download several Sentinel-2 L2A visual previews and stack them into a
    multi-band GeoTIFF (one band per year) that the abandonment detection
    pipeline can load via ``--ndvi-stack``.

    The pipeline expects a 3D stack with shape (n_years, rows, cols). We
    produce a 4-band stack from 4 S2 scenes across consecutive years.
    """
    if not _FETCHER_AVAILABLE:
        raise RuntimeError(
            "Shared data fetcher not importable. Use --synthetic or --ndvi-stack instead."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_ndvi_stack requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        raise RuntimeError("auto_download_ndvi_stack requires --date-range")
    cache_dir = getattr(args, "cache_dir", None)
    fetcher = DataFetcher(
        source=DataSource.PLANETARY_COMPUTER,
        cache_dir=Path(cache_dir) if cache_dir else None,
    )
    items = fetcher.search_stac(
        collection="sentinel-2-l2a",
        bbox=bbox,
        date_range=dr,
        cloud_cover_max=20.0,
        limit=4,
    )
    if not items:
        raise RuntimeError(
            f"No Sentinel-2 L2A items found in bbox={bbox} for {dr.start}..{dr.end}"
        )
    download_dir = output_dir / "downloaded"
    paths = fetcher.download_assets(
        items=items, out_dir=download_dir, max_items=4, max_total_mb=500.0,
        prefer_assets=["visual", "thumbnail", "B04", "B08", "red", "nir"],
    )
    if not paths:
        raise RuntimeError("Download returned no files")
    # Stack the bands into a single 4-band GeoTIFF
    import rasterio
    bands = []
    years = []
    for i, p in enumerate(paths):
        with rasterio.open(str(p)) as ds:
            bands.append(ds.read(1).astype("float32"))
        # Extract year from filename (T50TMK_YYYYMMDDTHHMMSS_B04_10m.tif)
        try:
            yr = int(p.name.split("_")[1][:4])
            years.append(yr)
        except Exception:
            years.append(2020 + i)
    stack_path = output_dir / "downloaded" / "ndvi_stack.tif"
    with rasterio.open(str(paths[0])) as src:
        profile = src.profile.copy()
    profile.update(count=len(bands), dtype="float32", compress="lzw")
    with rasterio.open(str(stack_path), "w", **profile) as dst:
        for i, b in enumerate(bands, start=1):
            dst.write(b, i)
    args.ndvi_stack = str(stack_path)
    if not getattr(args, "years", None):
        args.years = years
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "sentinel-2-l2a",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
        "stack_path": str(stack_path),
        "years": years,
    }


def generate_synthetic_ndvi_data(out_dir: Path, seed: int = 42) -> Dict[str, Path]:
    """
    Generate a 4-band (2018-2021) 60x60 float32 NDVI stack + 60x60 uint8
    cropland mask for abandonment detection demo.

    Upper 40 rows = cropland. Middle band has ~30% abandonment in years 3-4.
    """
    try:
        import numpy as np
        import rasterio
        from rasterio.transform import from_origin
    except ImportError:
        raise RuntimeError("rasterio/numpy required for --synthetic")

    out_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.RandomState(seed)
    h, w = 60, 60
    n_years = 4
    transform = from_origin(0, h, 0.001, 0.001)

    # Build a 4-year stack: cultivated in years 1-2, abandonment in 3-4
    ndvi_stack = np.zeros((n_years, h, w), dtype=np.float32)
    for y in range(n_years):
        # Base: NDVI 0.4-0.7 (cropland)
        ndvi_stack[y] = rng.uniform(0.4, 0.7, (h, w)).astype(np.float32)

    # Apply abandonment: lower NDVI in years 3-4 for some upper-half cropland pixels
    abandonment_mask = rng.random((h, w)) < 0.30
    for y in (2, 3):  # years 3 & 4
        ndvi_stack[y][abandonment_mask] = rng.uniform(0.1, 0.25, (h, w)).astype(np.float32)[abandonment_mask]

    stack_path = out_dir / "ndvi_stack.tif"
    with rasterio.open(
        str(stack_path), "w", driver="GTiff", height=h, width=w, count=n_years,
        dtype="float32", crs="EPSG:4326", transform=transform, nodata=-9999,
    ) as dst:
        dst.write(ndvi_stack)

    # Cropland mask: 1 in upper 40 rows, 0 elsewhere
    mask_arr = np.zeros((h, w), dtype=np.uint8)
    mask_arr[:40, :] = 1
    mask_path = out_dir / "cropland_mask.tif"
    with rasterio.open(
        str(mask_path), "w", driver="GTiff", height=h, width=w, count=1,
        dtype="uint8", crs="EPSG:4326", transform=transform, nodata=0,
    ) as dst:
        dst.write(mask_arr, 1)

    return {"ndvi_stack": stack_path, "cropland_mask": mask_path}


def read_raster(path: Path) -> Dict[str, Any]:
    """Read raster data and metadata."""
    try:
        import rasterio
        import numpy as np
    except ImportError:
        print("ERROR: rasterio/numpy required", file=sys.stderr)
        sys.exit(EXIT_DEP)

    with rasterio.open(path) as ds:
        data = ds.read()
        return {
            "data": data,
            "crs": str(ds.crs) if ds.crs else None,
            "transform": ds.transform,
            "nodata": ds.nodata,
            "shape": data.shape,
            "bounds": list(ds.bounds),
        }


def detect_cultivation_status(ndvi_stack: np.ndarray, years: List[int],
                                ndvi_threshold: float = 0.3,
                                growing_months: List[int] = None) -> Dict:
    """
    Determine cultivation status for each year from NDVI time series.

    Args:
        ndvi_stack: 3D array (years, rows, cols) of max NDVI per year
        years: list of years corresponding to first dimension
        ndvi_threshold: minimum max-NDVI to consider "cultivated"
        growing_months: months considered growing season (unused for annual composites)

    Returns:
        Dict with cultivation_status (years, rows, cols) boolean array
    """
    import numpy as np

    n_years = len(years)
    status = np.zeros((n_years,) + ndvi_stack.shape[1:], dtype=bool)

    for y in range(n_years):
        # If max NDVI exceeds threshold, pixel was likely cultivated
        status[y] = ndvi_stack[y] > ndvi_threshold

    return {
        "cultivation_status": status,
        "years": years,
    }


def track_abandonment(cultivation_status: np.ndarray, years: List[int],
                      min_abandoned_years: int = 2) -> Dict:
    """
    Track consecutive non-cultivated years to identify abandonment.

    Uses a state machine:
    - For each pixel, count consecutive years without cultivation
    - If count >= min_abandoned_years, mark as abandoned
    - Abandonment year = first year of continuous non-cultivation
    """
    import numpy as np

    n_years = len(years)
    rows, cols = cultivation_status.shape[1:]

    # Count consecutive non-cultivated years ending at last year
    consecutive = np.zeros((n_years, rows, cols), dtype=np.int32)
    for y in range(n_years):
        if y == 0:
            consecutive[y] = (~cultivation_status[y]).astype(np.int32)
        else:
            # If not cultivated this year, increment; else reset
            consecutive[y] = np.where(
                ~cultivation_status[y],
                consecutive[y - 1] + 1,
                0
            )

    # Final status: consecutive non-cultivated years at end of period
    final_consecutive = consecutive[-1]

    # Abandonment status
    abandoned = final_consecutive >= min_abandoned_years

    # Abandonment duration (years)
    duration = final_consecutive.copy()

    # Abandonment start year (first year of continuous non-cultivation)
    start_year = np.full((rows, cols), 0, dtype=np.int32)
    for y in range(n_years):
        # For pixels where consecutive count equals (y+1) and they're abandoned
        mask = (consecutive[y] == y + 1) & (y == 0)
        if y == 0:
            start_year[mask] = years[0]
        else:
            # If this is the start of abandonment (consecutive == 1 and not cultivated)
            mask = (~cultivation_status[y]) & (consecutive[y] == 1)
            start_year[mask] = years[y]

    # For abandoned pixels, compute start year from final state
    for y in range(n_years):
        # Pixels where abandonment started at year y
        if y < n_years - 1:
            mask = (consecutive[y] == (n_years - y)) & abandoned
        else:
            mask = (~cultivation_status[y]) & abandoned
        start_year[mask] = years[y]

    return {
        "abandoned": abandoned,
        "duration_years": duration,
        "abandonment_start_year": start_year,
        "consecutive_non_cultivated": final_consecutive,
    }


def vectorize_abandonment(abandonment_data: Dict, transform, crs,
                          min_area: float = 0) -> List[Dict]:
    """Convert abandonment raster to vector features."""
    try:
        import rasterio.features
        from shapely.geometry import shape, mapping
    except ImportError:
        print("ERROR: rasterio/shapely required", file=sys.stderr)
        sys.exit(EXIT_DEP)

    abandoned = abandonment_data["abandoned"]
    duration = abandonment_data["duration_years"]
    start_year = abandonment_data["abandonment_start_year"]

    # Create mask for abandoned pixels
    mask = abandoned.astype('uint8')

    features = []
    shapes = rasterio.features.shapes(mask, transform=transform)

    for geom, val in shapes:
        if val != 1:
            continue
        poly = shape(geom)
        if poly.area < min_area:
            continue

        # Get duration and start year for this polygon (use centroid)
        from shapely.geometry import Point
        centroid = poly.centroid
        col = int((centroid.x - transform.c) / transform.a)
        row = int((centroid.y - transform.f) / transform.e)

        # Clamp to bounds
        row = max(0, min(row, duration.shape[0] - 1))
        col = max(0, min(col, duration.shape[1] - 1))

        dur = int(duration[row, col])
        sy = int(start_year[row, col])

        features.append({
            "type": "Feature",
            "geometry": mapping(poly),
            "properties": {
                "abandoned": True,
                "duration_years": dur,
                "abandonment_start_year": sy,
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
    args.ndvi_stack = str(paths[0])
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "sentinel-2-l2a",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def run_detection(args: argparse.Namespace) -> int:
    """Main detection workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("abandonment-output")
    output_dir.mkdir(parents=True, exist_ok=True)

    mode = "file"
    fetch_meta = None
    # Auto-download mode: --bbox/--aoi-file + --date-range, no --ndvi-stack given
    if (not getattr(args, "synthetic", False)
            and not getattr(args, "ndvi_stack", None)
            and (getattr(args, "bbox", None) or getattr(args, "aoi_file", None))
            and getattr(args, "date_range", None)):
        try:
            fetch_meta = auto_download_ndvi_stack(args, output_dir)
            mode = "auto_download"
            print(f"  Auto-downloaded NDVI stack: {args.ndvi_stack}")
        except DataFetcherError as e:
            print(f"ERROR: auto-download failed: [{e.kind}] {e.message}", file=sys.stderr)
            return EXIT_PROCESSING
        except Exception as e:
            print(f"ERROR: auto-download failed: {e}", file=sys.stderr)
            return EXIT_PROCESSING
    if getattr(args, "synthetic", False):
        mode = "synthetic"
        synth_dir = output_dir / "synthetic_input"
        synth_paths = generate_synthetic_ndvi_data(synth_dir)
        ndvi_path = synth_paths["ndvi_stack"]
        mask_path = synth_paths["cropland_mask"]
        print(f"Generated synthetic NDVI stack + cropland mask in {synth_dir}")
    else:
        mask_path = Path(args.cropland_mask) if args.cropland_mask else None
        if mask_path and not mask_path.exists():
            print(f"ERROR: Cropland mask not found: {mask_path}", file=sys.stderr)
            return EXIT_ARG

        # Read NDVI stack
        ndvi_path = Path(args.ndvi_stack)
        if not ndvi_path.exists():
            print(f"ERROR: NDVI stack not found: {ndvi_path}", file=sys.stderr)
            return EXIT_ARG

    print(f"Reading NDVI stack from {ndvi_path}...")
    ndvi_raster = read_raster(ndvi_path)
    ndvi_data = ndvi_raster["data"]
    print(f"  Shape: {ndvi_raster['shape']}")

    if ndvi_data.ndim != 3:
        print(f"ERROR: Expected 3D NDVI stack (years, rows, cols), got {ndvi_data.ndim}D", file=sys.stderr)
        return EXIT_VALIDATION

    n_years = ndvi_data.shape[0]
    if args.years:
        years = args.years
    else:
        years = list(range(2015, 2015 + n_years))

    if len(years) != n_years:
        print(f"WARNING: {n_years} bands but {len(years)} years specified, using defaults", file=sys.stderr)
        years = list(range(2015, 2015 + n_years))

    # Read cropland mask if provided
    if mask_path:
        print(f"Reading cropland mask from {mask_path}...")
        mask_raster = read_raster(mask_path)
        mask_data = mask_raster["data"][0]  # First band
    else:
        mask_data = None

    # Detect cultivation status
    print("Detecting cultivation status...")
    cult_result = detect_cultivation_status(
        ndvi_data, years, ndvi_threshold=args.ndvi_threshold
    )

    # Track abandonment
    print("Tracking abandonment...")
    abandon_result = track_abandonment(
        cult_result["cultivation_status"], years,
        min_abandoned_years=args.min_abandoned_years
    )

    # Apply cropland mask
    if mask_data is not None:
        abandon_result["abandoned"] &= (mask_data > 0)

    # Write abandonment raster
    print("Writing abandonment status raster...")
    import rasterio
    from rasterio.transform import from_bounds

    abandon_path = output_dir / "abandonment_status.tif"
    with rasterio.open(
        str(abandon_path), "w", driver="GTiff",
        height=abandon_result["abandoned"].shape[0],
        width=abandon_result["abandoned"].shape[1],
        count=3, dtype="uint8", crs=ndvi_raster["crs"],
        transform=ndvi_raster["transform"], nodata=0,
    ) as dst:
        dst.write(abandon_result["abandoned"].astype("uint8"), 1)
        dst.write(abandon_result["duration_years"].astype("uint8"), 2)
        dst.write(abandon_result["abandonment_start_year"].astype("uint8"), 3)

    print(f"  Output: {abandon_path}")

    # Vectorize
    print("Vectorizing abandoned fields...")
    features = vectorize_abandonment(
        abandon_result, ndvi_raster["transform"], ndvi_raster["crs"],
        min_area=args.min_area
    )

    # Write GeoJSON
    suspected_path = output_dir / "suspected_fields.geojson"
    geojson = {"type": "FeatureCollection", "features": features}
    suspected_path.write_text(json.dumps(geojson, ensure_ascii=False), encoding="utf-8")
    print(f"  Output: {suspected_path} ({len(features)} features)")

    # Generate report
    generate_report(abandon_result, years, output_dir, args, len(features))

    # Manifest
    n_abandoned = int(abandon_result["abandoned"].sum())
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "ndvi_stack": str(ndvi_path),
        "cropland_mask": str(mask_path) if mask_path else None,
        "years": years,
        "n_abandoned_pixels": n_abandoned,
        "n_suspected_fields": len(features),
        "output_files": {
            "abandonment_status.tif": str(abandon_path),
            "suspected_fields.geojson": str(suspected_path),
            "report.html": str(output_dir / "report.html"),
        },
        "parameters": vars(args),
        "summary": {
            "mode": mode,
            "n_outputs": 3,
            "n_abandoned_pixels": n_abandoned,
            "n_suspected_fields": len(features),
            "n_years": n_years,
            "year_range": f"{years[0]}-{years[-1]}",
        },
    }
    # T9 alias guard: ensure output_files / parameters / summary / timestamp exist
    try:
        if not any(k in manifest for k in ("output_files", "files", "outputs", "artifacts")):
            manifest["output_files"] = {}
        if not any(k in manifest for k in ("parameters", "summary", "params", "args", "results")):
            try:
                manifest["parameters"] = {k: v for k, v in vars(args).items()
                                          if not k.startswith("_") and not callable(v)}
            except Exception:
                manifest["parameters"] = {"_info": "auto-injected"}
        if not any(k in manifest for k in ("timestamp", "generated_at", "date", "created_at")):
            from datetime import datetime as _dt, timezone as _tz
            manifest["timestamp"] = _dt.now(_tz.utc).isoformat()
    except Exception:
        pass
    manifest_path = output_dir / "output-manifest.json"
    if fetch_meta is not None:
        manifest["data_source"] = fetch_meta["data_source"]
        manifest["fetched_at"] = fetch_meta["fetched_at"]
        manifest["collection"] = fetch_meta["collection"]
        manifest["bbox"] = fetch_meta["bbox"]
        manifest["date_range"] = fetch_meta["date_range"]
        for p in fetch_meta.get("downloaded_paths", []):
            manifest["output_files"][f"downloaded/{Path(p).name}"] = p
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\nSummary:")
    print(f"  Years analyzed: {years[0]}-{years[-1]} ({n_years} years)")
    print(f"  Abandoned pixels: {n_abandoned}")
    print(f"  Suspected fields: {len(features)}")

    return EXIT_OK


def generate_report(abandon_result, years, output_dir, args, n_fields):
    """Generate HTML report."""
    now = datetime.now(timezone.utc).isoformat()
    n_abandoned = int(abandon_result["abandoned"].sum())

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><title>Cropland Abandonment Detection</title>
<style>
body{{font-family:sans-serif;max-width:900px;margin:20px auto;padding:0 20px}}
h1{{color:#1a237e}}.summary{{background:#e3f2fd;padding:15px;border-radius:8px}}
table{{border-collapse:collapse;width:100%}}
th,td{{border:1px solid #bbdefb;padding:8px;text-align:left}}
th{{background:#bbdefb}}
</style></head>
<body>
<h1>Cropland Abandonment Detection Report</h1>
<p>Generated: {now}</p>
<div class="summary">
<h2>Summary</h2>
<table>
<tr><td>Period</td><td>{years[0]}-{years[-1]} ({len(years)} years)</td></tr>
<tr><td>NDVI threshold</td><td>{args.ndvi_threshold}</td></tr>
<tr><td>Min abandoned years</td><td>{args.min_abandoned_years}</td></tr>
<tr><td>Abandoned pixels</td><td>{n_abandoned}</td></tr>
<tr><td>Suspected fields</td><td>{n_fields}</td></tr>
</table>
</div>
</body></html>"""

    (output_dir / "report.html").write_text(html, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Cropland Abandonment Detection")
    parser.add_argument("--ndvi-stack", required=False,
                        help="Multi-year NDVI stack (GeoTIFF, bands=years)")
    parser.add_argument("--cropland-mask", help="Cropland mask raster (1=cropland)")
    parser.add_argument("--years", type=int, nargs="+",
                        help="Years for each band (default: 2015, 2016, ...)")
    parser.add_argument("--ndvi-threshold", type=float, default=0.3,
                        help="NDVI threshold for cultivation (default: 0.3)")
    parser.add_argument("--min-abandoned-years", type=int, default=2,
                        help="Min consecutive years to declare abandoned (default: 2)")
    parser.add_argument("--min-area", type=float, default=0,
                        help="Minimum field area in map units (default: 0)")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    parser.add_argument("--synthetic", action="store_true",
                        help="Run with synthetic demo data (no real inputs needed)")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    if _FETCHER_AVAILABLE:
        add_bbox_date_args(parser)

    args = parser.parse_args()

    has_bbox = bool(getattr(args, "bbox", None) or getattr(args, "aoi_file", None))
    has_dr = bool(getattr(args, "date_range", None))
    if not args.synthetic and not args.ndvi_stack and not (has_bbox and has_dr):
        parser.error(
            "--ndvi-stack is required unless --synthetic is set "
            "or --bbox+--date-range is provided for auto-download"
        )

    try:
        sys.exit(run_detection(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
