#!/usr/bin/env python3
"""
Watershed Delineation - Automated watershed analysis from DEM.

Computes flow direction (D8), flow accumulation, delineates watersheds
from outlet points, extracts stream networks, and generates statistics.

Exit codes:
    0 = success
    2 = argument error
    3 = dependency missing
    7 = processing failure
"""

import argparse
import json
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Shared data-download library (Microsoft Planetary Computer, NASA POWER, OSM)
# Try pip-installed package first; fall back to local copy in repo root.
try:
    import _geoskill_data_fetcher  # noqa: F401
    from _geoskill_data_fetcher import (  # noqa: E402
        BBox, DataFetcher, DataSource, DateRange,
        add_bbox_date_args, parse_bbox_arg, parse_date_range_arg,
    )
    _HAS_FETCHER = True
except Exception:  # pragma: no cover - fallback when shared lib unavailable
    _HAS_FETCHER = False
    DataFetcher = None  # type: ignore
    DataSource = None  # type: ignore
    BBox = None  # type: ignore
    DateRange = None  # type: ignore
    add_bbox_date_args = None  # type: ignore
    parse_bbox_arg = None  # type: ignore
    parse_date_range_arg = None  # type: ignore

def _try_auto_download(args, output_dir: Path) -> Dict[str, Any]:
    """Auto-download DEM (cop-dem-glo-30) from Microsoft Planetary Computer."""
    if not _HAS_FETCHER:
        return {}
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        return {}

    needs_dem = not getattr(args, "dem", None) or not Path(args.dem).exists()
    if not needs_dem:
        return {}

    metadata: Dict[str, Any] = {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "bbox": bbox.to_list(),
    }
    down_dir = output_dir / "downloaded"
    down_dir.mkdir(parents=True, exist_ok=True)

    try:
        fetcher = DataFetcher(source=DataSource.PLANETARY_COMPUTER)
        items = fetcher.search_stac(
            collection="cop-dem-glo-30",
            bbox=bbox,
            date_range=DateRange("2020-01-01", "2021-12-31"),
            limit=1,
        )
        if not items:
            print(f"WARNING: cop-dem-glo-30 search returned 0 items in {bbox.to_string()}", file=sys.stderr)
            return metadata
        paths = fetcher.download_assets(
            items=items, out_dir=down_dir, max_items=1, max_total_mb=300.0,
        )
        if paths:
            args.dem = str(paths[0])
            metadata["collection"] = "cop-dem-glo-30"
            metadata["dem_path"] = str(paths[0])
            print(f"  Auto-downloaded DEM: {paths[0]}")
    except Exception as exc:
        print(f"WARNING: DEM download failed: {exc}", file=sys.stderr)

    return metadata



EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_PROCESSING = 7

# D8 direction encoding: E, SE, S, SW, W, NW, N, NE
# Values 1, 2, 4, 8, 16, 32, 64, 128
# (dr, dc) = (row_delta, col_delta)
D8_DIRECTIONS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
D8_VALUES = [1, 2, 4, 8, 16, 32, 64, 128]


def fill_sinks_dem(dem: "numpy.ndarray") -> "numpy.ndarray":
    """Simple sink filling using iterative raising of pits."""
    import numpy as np
    filled = dem.copy()
    nodata = -9999

    # Find pits (cells lower than all neighbors)
    max_iterations = 100
    for iteration in range(max_iterations):
        pits_found = False
        for r in range(1, filled.shape[0] - 1):
            for c in range(1, filled.shape[1] - 1):
                if filled[r, c] == nodata:
                    continue
                neighbors = []
                for dr, dc in D8_DIRECTIONS:
                    val = filled[r + dr, c + dc]
                    if val != nodata:
                        neighbors.append(val)
                if neighbors and filled[r, c] < min(neighbors):
                    filled[r, c] = min(neighbors) + 0.001  # slight raise
                    pits_found = True
        if not pits_found:
            break

    return filled


def compute_flow_direction(dem: "numpy.ndarray") -> "numpy.ndarray":
    """Compute D8 flow direction raster."""
    import numpy as np
    rows, cols = dem.shape
    flow_dir = np.zeros((rows, cols), dtype=np.int32)
    nodata = -9999

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if dem[r, c] == nodata:
                continue
            max_drop = 0
            best_dir = 0
            for i, (dr, dc) in enumerate(D8_DIRECTIONS):
                nr, nc = r + dr, c + dc
                if dem[nr, nc] == nodata:
                    continue
                # Diagonal distance is sqrt(2), cardinal is 1
                dist = 1.414 if abs(dr) + abs(dc) == 2 else 1.0
                drop = (dem[r, c] - dem[nr, nc]) / dist
                if drop > max_drop:
                    max_drop = drop
                    best_dir = D8_VALUES[i]
            flow_dir[r, c] = best_dir

    return flow_dir


def compute_flow_accumulation(flow_dir: "numpy.ndarray") -> "numpy.ndarray":
    """Compute flow accumulation from D8 flow direction."""
    import numpy as np
    rows, cols = flow_dir.shape
    accumulation = np.ones((rows, cols), dtype=np.int32)

    # Build reverse mapping: for each cell, which cells flow into it
    inflow_cells = {}
    for r in range(rows):
        for c in range(cols):
            if flow_dir[r, c] == 0:
                continue
            # Find where this cell flows to
            for i, val in enumerate(D8_VALUES):
                if flow_dir[r, c] == val:
                    dr, dc = D8_DIRECTIONS[i]
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        inflow_cells.setdefault((nr, nc), []).append((r, c))
                    break

    # Topological sort and accumulate
    visited = set()
    stack = []

    def dfs(cell):
        if cell in visited:
            return
        visited.add(cell)
        r, c = cell
        if (r, c) in inflow_cells:
            for upstream in inflow_cells[(r, c)]:
                dfs(upstream)
                accumulation[r, c] += accumulation[upstream[0], upstream[1]]
        stack.append(cell)

    for r in range(rows):
        for c in range(cols):
            dfs((r, c))

    return accumulation


def delineate_watershed(flow_dir: "numpy.ndarray", outlet_row: int, outlet_col: int) -> "numpy.ndarray":
    """Delineate watershed upstream of an outlet point."""
    import numpy as np
    rows, cols = flow_dir.shape
    watershed = np.zeros((rows, cols), dtype=np.int32)

    # Reverse D8: which direction flows INTO a cell
    reverse_d8 = {}
    for i, (dr, dc) in enumerate(D8_DIRECTIONS):
        reverse_d8[(-dr, -dc)] = D8_VALUES[i]

    # BFS/DFS from outlet, going upstream
    stack = [(outlet_row, outlet_col)]
    visited = set()

    while stack:
        r, c = stack.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        watershed[r, c] = 1

        # Check all neighbors to see if they flow into this cell
        for dr, dc in D8_DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                # Does neighbor flow into this cell?
                neighbor_dir = flow_dir[nr, nc]
                if neighbor_dir == 0:
                    continue
                for i, val in enumerate(D8_VALUES):
                    if neighbor_dir == val:
                        ndr, ndc = D8_DIRECTIONS[i]
                        if ndr == -dr and ndc == -dc:
                            stack.append((nr, nc))
                        break

    return watershed


def extract_streams(flow_accumulation: "numpy.ndarray", threshold: int) -> "numpy.ndarray":
    """Extract stream network from flow accumulation using threshold."""
    import numpy as np
    streams = (flow_accumulation >= threshold).astype(np.int32)
    return streams


def compute_watershed_stats(watershed: "numpy.ndarray", dem: "numpy.ndarray",
                            flow_accumulation: "numpy.ndarray") -> Dict[str, Any]:
    """Compute watershed statistics."""
    import numpy as np
    mask = watershed == 1
    pixel_count = int(np.sum(mask))

    if pixel_count == 0:
        return {"pixel_count": 0, "area_ha": 0}

    elevations = dem[mask]
    valid_elev = elevations[elevations != -9999]

    # Approximate area (assuming 30m pixels)
    pixel_area_m2 = 30 * 30  # SRTM resolution
    area_ha = pixel_count * pixel_area_m2 / 10000

    return {
        "pixel_count": pixel_count,
        "area_ha": round(area_ha, 2),
        "area_km2": round(area_ha / 100, 4),
        "elevation_min": float(np.min(valid_elev)) if len(valid_elev) > 0 else None,
        "elevation_max": float(np.max(valid_elev)) if len(valid_elev) > 0 else None,
        "elevation_mean": float(np.mean(valid_elev)) if len(valid_elev) > 0 else None,
        "max_flow_accumulation": int(np.max(flow_accumulation[mask])) if pixel_count > 0 else 0,
    }


def generate_synthetic_data(seed: int = 42):
    """Generate 60x60 DEM with realistic terrain (range 100-500m).

    Adds a smooth east-to-west elevation gradient plus noise so flow direction
    and accumulation are non-trivial.
    """
    import numpy as np
    from rasterio.transform import from_origin

    rng = np.random.RandomState(seed)
    H, W = 60, 60

    # Base elevation: gradient from 500m (west) to 100m (east)
    grad = np.linspace(500.0, 100.0, W).astype(np.float32)
    base = np.tile(grad, (H, 1))
    # Add a small hill in the NW and a valley down the middle for realism
    rr, cc = np.meshgrid(np.arange(H), np.arange(W), indexing="ij")
    hill = 80.0 * np.exp(-((rr - 10) ** 2 + (cc - 5) ** 2) / 50.0)
    valley = -40.0 * np.exp(-((cc - W / 2) ** 2) / 30.0)
    noise = rng.normal(0, 3.0, (H, W)).astype(np.float32)
    dem = (base + hill + valley + noise).astype(np.float32)

    transform = from_origin(0.0, float(H), 0.001, 0.001)
    profile = {
        "driver": "GTiff",
        "height": H,
        "width": W,
        "count": 1,
        "dtype": "float32",
        "crs": "EPSG:4326",
        "transform": transform,
        "nodata": None,
    }
    return dem, transform, "EPSG:4326", profile


def write_synthetic_raster(dem, profile, out_dir: Path):
    """Write the synthetic DEM under out_dir/synthetic_input/."""
    import rasterio

    synth_dir = out_dir / "synthetic_input"
    synth_dir.mkdir(parents=True, exist_ok=True)
    dem_path = synth_dir / "dem_synthetic.tif"
    with rasterio.open(str(dem_path), "w", **profile) as dst:
        dst.write(dem, 1)
    return dem_path


def auto_download_dem(args, output_dir: Path) -> Dict[str, Any]:
    """Download one cop-dem-glo-30 scene from MPC using --bbox + --date-range.

    Returns metadata dict (also writes the path back to args.dem).
    """
    if not _HAS_FETCHER:
        raise RuntimeError(
            "Shared data fetcher not importable. Pass --dem <local.tif> instead, "
            "or ensure _geoskill_data_fetcher is on sys.path."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_dem requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        dr = DateRange("2020-01-01", "2021-12-31")
    cache_dir = getattr(args, "cache_dir", None)
    fetcher = DataFetcher(
        source=DataSource.PLANETARY_COMPUTER,
        cache_dir=Path(cache_dir) if cache_dir else None,
    )
    # cop-dem-glo-30 is a static collection (2020-2021); use a wide search range
    # that covers all available tiles regardless of the user-provided date range.
    items = fetcher.search_stac(
        collection="cop-dem-glo-30",
        bbox=bbox,
        date_range=DateRange("2020-01-01", "2021-12-31"),
        limit=1,
    )
    if not items:
        raise RuntimeError(
            f"No cop-dem-glo-30 items found in bbox={bbox} for {dr.start}..{dr.end}"
        )
    download_dir = output_dir / "downloaded"
    paths = fetcher.download_assets(
        items=items, out_dir=download_dir, max_items=1, max_total_mb=500,
    )
    if not paths:
        raise RuntimeError("Download returned no files")
    args.dem = str(paths[0])
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "cop-dem-glo-30",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def run_watershed(args: argparse.Namespace) -> int:
    """Main watershed delineation workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("watershed-output")
    output_dir.mkdir(parents=True, exist_ok=True)
    mode = "synthetic" if args.synthetic else "file"
    fetch_meta: Dict[str, Any] = {}

    if args.synthetic:
        # P2-1: build 60x60 synthetic DEM
        dem_arr, transform_synth, crs_synth, profile = generate_synthetic_data()
        dem_path = write_synthetic_raster(dem_arr, profile, output_dir)
        print(f"  Synthetic DEM: {dem_path.name}")
    else:
        # --- Auto-download mode: fetch cop-dem-glo-30 from MPC ---
        dem_path = Path(args.dem) if getattr(args, "dem", None) else None
        if (dem_path is None or not dem_path.exists()) and \
                (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)):
            try:
                fetch_meta = auto_download_dem(args, output_dir)
                mode = "auto_download"
                print(f"  Auto-downloaded DEM: {args.dem}")
            except Exception as e:
                print(f"ERROR: auto-download failed: {e}", file=sys.stderr)
                return EXIT_PROCESSING
        dem_path = Path(args.dem)
        if not dem_path.exists():
            print(f"ERROR: DEM not found: {dem_path}", file=sys.stderr)
            return EXIT_ARG

    try:
        import numpy as np
        import rasterio
    except ImportError:
        print("ERROR: rasterio and numpy required", file=sys.stderr)
        return EXIT_DEP

    # Load DEM
    print("Loading DEM...")
    with rasterio.open(dem_path) as ds:
        dem = ds.read(1).astype(np.float64)
        transform = ds.transform
        crs = ds.crs
        nodata_ds = ds.nodata

    if nodata_ds is not None:
        dem[dem == nodata_ds] = -9999

    print(f"  DEM: {dem.shape[1]}x{dem.shape[0]}, CRS={crs}")

    # Fill sinks
    print("Filling sinks...")
    filled = fill_sinks_dem(dem)

    # Flow direction
    print("Computing flow direction...")
    flow_dir = compute_flow_direction(filled)

    # Flow accumulation
    print("Computing flow accumulation...")
    flow_acc = compute_flow_accumulation(flow_dir)

    # Determine outlet
    if args.outlet_row is not None and args.outlet_col is not None:
        outlet_row, outlet_col = args.outlet_row, args.outlet_col
    else:
        # Default: highest accumulation point
        outlet_row, outlet_col = np.unravel_index(np.argmax(flow_acc), flow_acc.shape)

    print(f"  Outlet: ({outlet_row}, {outlet_col})")

    # Delineate watershed
    print("Delineating watershed...")
    watershed = delineate_watershed(flow_dir, outlet_row, outlet_col)

    # Extract streams
    threshold = args.stream_threshold
    print(f"Extracting streams (threshold={threshold})...")
    streams = extract_streams(flow_acc, threshold)

    # Statistics
    stats = compute_watershed_stats(watershed, dem, flow_acc)
    print(f"  Watershed: {stats['pixel_count']} pixels ({stats.get('area_ha', 0)} ha)")

    # Save outputs
    print("Saving outputs...")
    out_profile = {
        "driver": "GTiff",
        "height": dem.shape[0],
        "width": dem.shape[1],
        "count": 1,
        "dtype": "int32",
        "crs": crs,
        "transform": transform,
        "nodata": -9999,
    }

    with rasterio.open(str(output_dir / "flow_direction.tif"), "w", **out_profile) as dst:
        dst.write(flow_dir, 1)
    with rasterio.open(str(output_dir / "flow_accumulation.tif"), "w", **out_profile) as dst:
        dst.write(flow_acc, 1)
    with rasterio.open(str(output_dir / "watershed.tif"), "w", **out_profile) as dst:
        dst.write(watershed, 1)
    with rasterio.open(str(output_dir / "streams.tif"), "w", **out_profile) as dst:
        dst.write(streams, 1)

    # Report
    now = datetime.now(timezone.utc).isoformat()
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><title>Watershed Delineation</title>
<style>
body{{font-family:sans-serif;max-width:900px;margin:20px auto;padding:0 20px}}
h1{{color:#1a237e}}.summary{{background:#e3f2fd;padding:15px;border-radius:8px}}
table{{border-collapse:collapse;width:100%}}
th,td{{border:1px solid #bbdefb;padding:8px;text-align:left}}
th{{background:#bbdefb}}
</style></head>
<body>
<h1>Watershed Delineation Report</h1>
<p>Generated: {now}</p>
<div class="summary">
<h2>Watershed Statistics</h2>
<table>
<tr><td>Area</td><td><strong>{stats.get('area_ha', 0)} ha ({stats.get('area_km2', 0)} km²)</strong></td></tr>
<tr><td>Pixels</td><td><strong>{stats['pixel_count']}</strong></td></tr>
<tr><td>Elevation min</td><td><strong>{stats.get('elevation_min', 'N/A')}</strong></td></tr>
<tr><td>Elevation max</td><td><strong>{stats.get('elevation_max', 'N/A')}</strong></td></tr>
<tr><td>Max accumulation</td><td><strong>{stats.get('max_flow_accumulation', 0)}</strong></td></tr>
</table>
</div>
</body></html>"""
    (output_dir / "report.html").write_text(html, encoding="utf-8")

    # Manifest (T9 compliant: timestamp + output_files + parameters + summary)
    output_files = {
        "flow_direction.tif": str(output_dir / "flow_direction.tif"),
        "flow_accumulation.tif": str(output_dir / "flow_accumulation.tif"),
        "watershed.tif": str(output_dir / "watershed.tif"),
        "streams.tif": str(output_dir / "streams.tif"),
        "report.html": str(output_dir / "report.html"),
        "output-manifest.json": str(output_dir / "output-manifest.json"),
    }
    if args.synthetic:
        output_files["synthetic_input/dem_synthetic.tif"] = str(output_dir / "synthetic_input" / "dem_synthetic.tif")

    manifest = {
        "timestamp": now,
        "mode": mode,
        "output_files": output_files,
        "parameters": vars(args),
        "summary": {
            "mode": mode,
            "n_outputs": len(output_files),
            "outlet": [int(outlet_row), int(outlet_col)],
            "stream_threshold": threshold,
            "area_ha": stats.get("area_ha", 0),
            "pixel_count": stats.get("pixel_count", 0),
        },
        "dem": str(dem_path),
        "outlet": [int(outlet_row), int(outlet_col)],
        "stream_threshold": threshold,
        "statistics": stats,
    }
    if fetch_meta:
        manifest["data_source"] = fetch_meta.get("data_source")
        manifest["fetched_at"] = fetch_meta.get("fetched_at")
        if fetch_meta.get("collection"):
            manifest["collection"] = fetch_meta["collection"]
        if fetch_meta.get("downloaded_paths"):
            manifest["dem_downloaded"] = fetch_meta["downloaded_paths"][0]
    # T9 guard: ensure output_files / parameters-or-summary / timestamp exist
    try:
        if not any(k in manifest for k in ("output_files", "files", "outputs", "artifacts", "products", "result_files")):
            manifest["output_files"] = {}
        if not any(k in manifest for k in ("parameters", "summary", "params", "args", "inputs", "result", "results", "stats", "metrics", "qc_summary", "findings")):
            manifest["parameters"] = {k: v for k, v in vars(args).items() if not k.startswith("_") and not callable(v)}
        if not any(k in manifest for k in ("timestamp", "generated_at", "date", "created_at", "run_time", "datetime", "time", "ts")):
            from datetime import datetime as _dt, timezone as _tz
            manifest["timestamp"] = _dt.now(_tz.utc).isoformat()
    except Exception:
        pass

    (output_dir / "output-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"\nOutput: {output_dir}")
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Watershed Delineation")
    parser.add_argument("--dem", help="Input DEM raster (or use --synthetic)")
    parser.add_argument("--outlet-row", type=int, help="Outlet row (default: max accumulation)")
    parser.add_argument("--outlet-col", type=int, help="Outlet column")
    parser.add_argument("--stream-threshold", type=int, default=100,
                        help="Stream threshold in accumulation pixels")
    parser.add_argument("--synthetic", action="store_true",
                        help="Run with synthetic demo data (no real inputs needed)")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    if add_bbox_date_args is not None:
        add_bbox_date_args(parser)

    args = parser.parse_args()
    # P0/P2-1: ensure either --synthetic OR --dem OR (--bbox/--aoi-file for auto-download)
    if not args.synthetic and not args.dem and not (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)):
        parser.error("either --synthetic, --dem, or --bbox/--aoi-file is required")

    try:
        sys.exit(run_watershed(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
