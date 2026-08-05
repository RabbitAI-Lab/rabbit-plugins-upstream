#!/usr/bin/env python3
"""
Wetland Change Monitor - Track wetland extent, inundation frequency, and transitions.

Reads multi-year water occurrence rasters (JRC-style) or multi-band water masks,
computes inundation frequency, classifies wetland types, identifies change patches
(degradation, recovery, stable), and generates vectorized change outputs.

Exit codes:
    0 = success
    2 = argument error
    3 = dependency missing
    6 = validation error
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
    """Auto-download JRC GSW water-frequency (jrc-gsw) and Sentinel-1 GRD (sentinel-1-grd)."""
    if not _HAS_FETCHER:
        return {}
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        return {}

    needs_freq = not getattr(args, "water_frequency", None) or not Path(args.water_frequency).exists()
    needs_masks = not getattr(args, "water_masks", None) or not Path(args.water_masks).exists()
    if not needs_freq and not needs_masks:
        return {}

    metadata: Dict[str, Any] = {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "bbox": bbox.to_list(),
    }
    down_dir = output_dir / "downloaded"
    down_dir.mkdir(parents=True, exist_ok=True)

    dr = parse_date_range_arg(getattr(args, "date_range", None)) or DateRange(
        "2020-01-01", "2020-12-31"
    )

    fetcher = DataFetcher(source=DataSource.PLANETARY_COMPUTER)

    # 1) JRC Global Surface Water — static, so just any date range works
    if needs_freq:
        try:
            items = fetcher.search_stac(
                collection="jrc-gsw",
                bbox=bbox,
                date_range=DateRange("2020-01-01", "2020-12-31"),
                limit=1,
            )
            if items:
                paths = fetcher.download_assets(
                    items=items, out_dir=down_dir, max_items=1, max_total_mb=300.0,
                )
                if paths:
                    args.water_frequency = str(paths[0])
                    metadata["jrc_path"] = str(paths[0])
                    metadata["jrc_collection"] = "jrc-gsw"
                    print(f"  Auto-downloaded JRC GSW: {paths[0]}")
        except Exception as exc:
            print(f"WARNING: JRC GSW download failed: {exc}", file=sys.stderr)

    # 2) Sentinel-1 GRD — provides SAR water detection (multi-band mask)
    if needs_masks:
        try:
            items = fetcher.search_stac(
                collection="sentinel-1-grd",
                bbox=bbox,
                date_range=dr,
                limit=2,
            )
            if items:
                paths = fetcher.download_assets(
                    items=items, out_dir=down_dir, max_items=2, max_total_mb=300.0,
                    prefer_assets=["vv", "vh"],
                )
                if paths:
                    args.water_masks = str(paths[0])
                    metadata["sentinel1_paths"] = [str(p) for p in paths]
                    metadata["sentinel1_collection"] = "sentinel-1-grd"
                    print(f"  Auto-downloaded Sentinel-1 GRD: {len(paths)} scenes")
        except Exception as exc:
            print(f"WARNING: Sentinel-1 GRD download failed: {exc}", file=sys.stderr)

    metadata["collection"] = metadata.get("jrc_collection") or metadata.get("sentinel1_collection", "jrc-gsw")
    return metadata



EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# Wetland type codes
WETLAND_TYPES = {
    1: "permanent_water",
    2: "seasonal_water",
    3: "mudflat",
    4: "vegetation",
    5: "dry_land",
}

# Change type codes
CHANGE_TYPES = {
    "degradation": {"color": "#d32f2f", "description": "Wetland loss or drying"},
    "recovery": {"color": "#2e7d32", "description": "Wetland gain or rewetting"},
    "stable": {"color": "#1565c0", "description": "No significant change"},
    "human_encroachment": {"color": "#f9a825", "description": "Human conversion"},
}


def _check_deps() -> bool:
    """Check that required dependencies are available."""
    try:
        import rasterio  # noqa: F401
        import shapely  # noqa: F401
        return True
    except ImportError:
        return False


def compute_inundation_frequency(water_data: np.ndarray) -> np.ndarray:
    """Compute inundation frequency from multi-band water masks.

    Args:
        water_data: 3D array (bands, rows, cols) where 1=water, 0=dry

    Returns:
        2D array of inundation frequency (0.0 to 1.0)
    """
    if water_data.ndim == 2:
        # Single band - return as-is
        return water_data.astype(np.float64)

    # Count water occurrences across bands
    water_count = np.sum(water_data > 0, axis=0, dtype=np.float64)
    n_bands = water_data.shape[0]
    frequency = water_count / n_bands if n_bands > 0 else water_count
    return frequency


def classify_wetland_type(frequency: np.ndarray,
                          thresholds: Tuple[float, float] = (0.25, 0.75),
                          vegetation_index: Optional[np.ndarray] = None) -> np.ndarray:
    """Classify wetland types based on inundation frequency.

    Args:
        frequency: 2D array of inundation frequency (0-1)
        thresholds: (seasonal_low, seasonal_high) thresholds
        vegetation_index: Optional NDVI-like array for vegetation detection

    Returns:
        2D array of wetland type codes (1-5)
    """
    low_thresh, high_thresh = thresholds
    classification = np.full(frequency.shape, 5, dtype=np.uint8)  # default: dry_land

    # Permanent water: frequency >= high threshold
    classification[frequency >= high_thresh] = 1

    # Seasonal water: low <= frequency < high
    classification[(frequency >= low_thresh) & (frequency < high_thresh)] = 2

    # Mudflat: very low frequency (occasional inundation)
    classification[(frequency > 0) & (frequency < low_thresh)] = 3

    # Vegetation: frequency == 0 but vegetation index indicates green
    if vegetation_index is not None:
        classification[(frequency == 0) & (vegetation_index > 0.3)] = 4
    else:
        # Without vegetation index, use moderate frequency as proxy
        classification[(frequency == 0)] = 5  # dry land

    return classification


def compute_transition_matrix(classification_early: np.ndarray,
                              classification_late: np.ndarray,
                              n_types: int = 5) -> np.ndarray:
    """Compute transition matrix between two time periods.

    Args:
        classification_early: 2D array of wetland types at time 1
        classification_late: 2D array of wetland types at time 2
        n_types: Number of wetland types

    Returns:
        2D transition matrix (n_types x n_types)
    """
    matrix = np.zeros((n_types, n_types), dtype=np.int64)

    for i in range(n_types):
        for j in range(n_types):
            mask = (classification_early == (i + 1)) & (classification_late == (j + 1))
            matrix[i, j] = int(np.sum(mask))

    return matrix


def identify_change_patches(classification_early: np.ndarray,
                            classification_late: np.ndarray,
                            frequency_early: np.ndarray,
                            frequency_late: np.ndarray,
                            min_area_ha: float = 0.5,
                            pixel_area_ha: float = 0.01) -> List[Dict[str, Any]]:
    """Identify change patches between two classifications.

    Args:
        classification_early: Wetland types at time 1
        classification_late: Wetland types at time 2
        frequency_early: Inundation frequency at time 1
        frequency_late: Inundation frequency at time 2
        min_area_ha: Minimum patch area in hectares
        pixel_area_ha: Area per pixel in hectares

    Returns:
        List of change patch dictionaries
    """
    try:
        from rasterio import features
        from shapely.geometry import shape as shapely_shape
    except ImportError:
        return []

    change_mask = classification_early != classification_late
    if not np.any(change_mask):
        return []

    # Label connected components
    labeled_array, num_features = _label_patches(change_mask)
    patches = []

    for patch_id in range(1, num_features + 1):
        patch_mask = labeled_array == patch_id
        patch_pixels = int(np.sum(patch_mask))
        patch_area = patch_pixels * pixel_area_ha

        if patch_area < min_area_ha:
            continue

        # Determine change type
        early_type_mode = _mode(classification_early[patch_mask])
        late_type_mode = _mode(classification_late[patch_mask])
        freq_change = float(np.mean(frequency_late[patch_mask]) - np.mean(frequency_early[patch_mask]))

        change_type = _classify_change(early_type_mode, late_type_mode, freq_change)
        confidence = _compute_confidence(patch_pixels, freq_change, pixel_area_ha)

        # Get patch geometry
        patch_shapes = list(features.shapes(
            patch_mask.astype(np.uint8),
            mask=patch_mask,
        ))

        if patch_shapes:
            geom_json = []
            for geom, val in patch_shapes:
                if val == 1:
                    shapely_geom = shapely_shape(geom)
                    geom_json.append(shapely_geom)

            if geom_json:
                from shapely.ops import unary_union
                merged_geom = unary_union(geom_json)
                patches.append({
                    "change_type": change_type,
                    "early_type": WETLAND_TYPES.get(int(early_type_mode), "unknown"),
                    "late_type": WETLAND_TYPES.get(int(late_type_mode), "unknown"),
                    "area_ha": round(patch_area, 2),
                    "pixel_count": patch_pixels,
                    "frequency_change": round(freq_change, 4),
                    "confidence": round(confidence, 3),
                    "geometry": merged_geom,
                })

    return patches


def _label_patches(binary_mask: np.ndarray) -> Tuple[np.ndarray, int]:
    """Simple connected component labeling using scipy if available, else basic approach."""
    try:
        from scipy import ndimage
        labeled, num = ndimage.label(binary_mask)
        return labeled, num
    except ImportError:
        # Fallback: treat each contiguous region as a patch using basic flood fill
        labeled = np.zeros_like(binary_mask, dtype=np.int32)
        current_label = 0
        rows, cols = binary_mask.shape

        for r in range(rows):
            for c in range(cols):
                if binary_mask[r, c] and labeled[r, c] == 0:
                    current_label += 1
                    _flood_fill(binary_mask, labeled, r, c, current_label, rows, cols)

        return labeled, current_label


def _flood_fill(binary_mask: np.ndarray, labeled: np.ndarray,
                r: int, c: int, label: int, rows: int, cols: int) -> None:
    """Basic flood fill for connected component labeling."""
    stack = [(r, c)]
    while stack:
        cr, cc = stack.pop()
        if cr < 0 or cr >= rows or cc < 0 or cc >= cols:
            continue
        if not binary_mask[cr, cc] or labeled[cr, cc] != 0:
            continue
        labeled[cr, cc] = label
        stack.append((cr - 1, cc))
        stack.append((cr + 1, cc))
        stack.append((cr, cc - 1))
        stack.append((cr, cc + 1))


def _mode(arr: np.ndarray) -> int:
    """Compute the mode of an array."""
    values, counts = np.unique(arr, return_counts=True)
    return int(values[np.argmax(counts)])


def _classify_change(early_type: int, late_type: int, freq_change: float) -> str:
    """Classify the type of change between two wetland types."""
    # Degradation: water -> less water / dry
    if early_type in (1, 2) and late_type in (3, 4, 5):
        return "degradation"
    # Recovery: dry/mud -> water
    if early_type in (3, 4, 5) and late_type in (1, 2):
        return "recovery"
    # Human encroachment: water/vegetation -> dry land with large freq drop
    if late_type == 5 and freq_change < -0.3:
        return "human_encroachment"
    # Stable if same type
    if early_type == late_type:
        return "stable"
    # Default based on frequency change
    if freq_change < -0.2:
        return "degradation"
    elif freq_change > 0.2:
        return "recovery"
    return "stable"


def _compute_confidence(patch_pixels: int, freq_change: float, pixel_area_ha: float) -> float:
    """Compute confidence score for a change patch."""
    # Larger patches with bigger frequency changes = higher confidence
    size_factor = min(1.0, patch_pixels * pixel_area_ha / 5.0)  # saturates at 5 ha
    change_factor = min(1.0, abs(freq_change) / 0.5)  # saturates at 0.5 change
    confidence = 0.4 * size_factor + 0.6 * change_factor
    return min(1.0, max(0.0, confidence))


def vectorize_changes(patches: List[Dict], crs: str = "EPSG:4326") -> Dict[str, Any]:
    """Convert change patches to GeoJSON FeatureCollection."""
    features = []
    for patch in patches:
        geom = patch.get("geometry")
        if geom is None:
            continue
        features.append({
            "type": "Feature",
            "geometry": geom.__geo_interface__ if hasattr(geom, '__geo_interface__') else str(geom),
            "properties": {
                "change_type": patch["change_type"],
                "early_type": patch["early_type"],
                "late_type": patch["late_type"],
                "area_ha": patch["area_ha"],
                "pixel_count": patch["pixel_count"],
                "frequency_change": patch["frequency_change"],
                "confidence": patch["confidence"],
            },
        })

    return {
        "type": "FeatureCollection",
        "features": features,
        "crs": crs,
    }


def write_transition_matrix_csv(matrix: np.ndarray, years: List[int],
                                 output_path: Path) -> None:
    """Write transition matrix to CSV."""
    type_names = [WETLAND_TYPES.get(i + 1, f"type_{i + 1}") for i in range(matrix.shape[0])]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Header
        writer.writerow([""] + type_names)
        # Rows
        for i, name in enumerate(type_names):
            writer.writerow([name] + [int(matrix[i, j]) for j in range(matrix.shape[1])])


def generate_synthetic_data(output_dir: Path, seed: int = 42, n_periods: int = 2):
    """Generate 2-band water mask raster (60x60) for 2 periods.

    Returns the path to the generated multi-band .tif (band0=period1, band1=period2).
    """
    try:
        import rasterio
        from rasterio.transform import from_origin
    except ImportError:
        print("ERROR: rasterio required for synthetic mode", file=sys.stderr)
        sys.exit(EXIT_PROCESSING)

    synth_dir = output_dir / "synthetic_input"
    synth_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.RandomState(seed)
    transform = from_origin(0, 60, 0.001, 0.001)

    def _period_water(intensity: float = 0.6) -> np.ndarray:
        # Construct a water/land pattern: large connected water body in the middle,
        # land elsewhere. Add per-band noise to simulate temporal change.
        arr = np.zeros((60, 60), dtype=np.uint8)
        yy, xx = np.mgrid[0:60, 0:60]
        # 3 ellipses of water in a wetland-style pattern
        for cx, cy, r in [(20, 20, 12), (40, 35, 10), (30, 45, 8)]:
            mask = (xx - cx) ** 2 / (r ** 2) + (yy - cy) ** 2 / (r ** 2 * 0.6) <= 1
            arr[mask] = 1
        # Random sparse water to fill intensity target
        flat_idx = np.argwhere(arr == 0)
        n_extra = int((intensity - arr.mean()) * arr.size)
        if n_extra > 0 and len(flat_idx) > 0:
            picks = rng.choice(len(flat_idx), size=min(n_extra, len(flat_idx)), replace=False)
            arr[flat_idx[picks, 0], flat_idx[picks, 1]] = 1
        return arr

    p1 = _period_water(intensity=0.65)
    p2 = _period_water(intensity=0.50)  # ~15% reduction (degradation)

    out_path = synth_dir / "water_masks_2periods.tif"
    with rasterio.open(
        str(out_path), "w", driver="GTiff",
        height=60, width=60, count=n_periods,
        dtype="uint8", crs="EPSG:4326", transform=transform,
    ) as dst:
        dst.write(p1, 1)
        dst.write(p2, 2)
    return out_path


def auto_download_image(args, output_dir: Path) -> Dict[str, Any]:
    """Download JRC GSW + Sentinel-1 GRD for wetland change monitoring.

    Returns metadata dict (writes paths back to args.water_frequency / args.water_masks).
    """
    if not _HAS_FETCHER:
        raise RuntimeError(
            "Shared data fetcher not importable. Pass --water-frequency/--water-masks "
            "instead, or ensure _geoskill_data_fetcher is on sys.path."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_image requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        dr = DateRange("2020-01-01", "2020-12-31")
    cache_dir = getattr(args, "cache_dir", None)
    metadata: Dict[str, Any] = {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
    }

    needs_freq = not getattr(args, "water_frequency", None) or not Path(args.water_frequency).exists()
    needs_masks = not getattr(args, "water_masks", None) or not Path(args.water_masks).exists()

    fetcher = DataFetcher(
        source=DataSource.PLANETARY_COMPUTER,
        cache_dir=Path(cache_dir) if cache_dir else None,
    )
    download_dir = output_dir / "downloaded"

    # 1) JRC GSW (static water occurrence, JRC Global Surface Water)
    if needs_freq:
        try:
            items = fetcher.search_stac(
                collection="jrc-gsw",
                bbox=bbox,
                date_range=DateRange("2020-01-01", "2020-12-31"),
                limit=1,
            )
            if items:
                paths = fetcher.download_assets(
                    items=items, out_dir=download_dir, max_items=1, max_total_mb=300.0,
                )
                if paths:
                    args.water_frequency = str(paths[0])
                    metadata["jrc_path"] = str(paths[0])
                    metadata["jrc_collection"] = "jrc-gsw"
                    print(f"  Auto-downloaded JRC GSW: {paths[0]}")
        except Exception as exc:
            print(f"WARNING: JRC GSW download failed: {exc}", file=sys.stderr)

    # 2) Sentinel-1 GRD (SAR water mask)
    if needs_masks:
        try:
            items = fetcher.search_stac(
                collection="sentinel-1-grd",
                bbox=bbox,
                date_range=dr,
                limit=2,
            )
            if items:
                paths = fetcher.download_assets(
                    items=items, out_dir=download_dir, max_items=2, max_total_mb=300.0,
                    prefer_assets=["vh", "vv"],
                )
                if paths:
                    args.water_masks = str(paths[0])
                    metadata["sentinel1_paths"] = [str(p) for p in paths]
                    metadata["sentinel1_collection"] = "sentinel-1-grd"
                    print(f"  Auto-downloaded Sentinel-1 GRD: {len(paths)} scenes")
        except Exception as exc:
            print(f"WARNING: Sentinel-1 GRD download failed: {exc}", file=sys.stderr)

    metadata["collection"] = metadata.get("jrc_collection") or metadata.get("sentinel1_collection", "jrc-gsw")
    return metadata


def run_wetland_monitor(args: argparse.Namespace) -> int:
    """Main wetland monitoring workflow."""
    if not _check_deps():
        print("ERROR: Required dependencies missing (rasterio, shapely)", file=sys.stderr)
        return EXIT_DEP

    import rasterio

    output_dir = Path(args.output_dir) if args.output_dir else Path("wetland-output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # --- Auto-download mode: fetch JRC GSW + Sentinel-1 GRD from MPC ---
    fetch_meta: Dict[str, Any] = {}
    if (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)) and not args.synthetic:
        needs_freq = not getattr(args, "water_frequency", None) or not Path(args.water_frequency).exists()
        needs_masks = not getattr(args, "water_masks", None) or not Path(args.water_masks).exists()
        if needs_freq or needs_masks:
            try:
                fetch_meta = auto_download_image(args, output_dir)
                print(f"  Auto-download complete")
            except Exception as e:
                print(f"ERROR: auto-download failed: {e}", file=sys.stderr)
                return EXIT_PROCESSING

    if args.synthetic:
        # Generate 2-band water mask raster for 2 periods
        print("Running in synthetic mode — generating demo water mask raster...")
        synth_path = generate_synthetic_data(output_dir, seed=42, n_periods=2)
        args.water_masks = str(synth_path)
        if not args.years or len(args.years) < 2:
            args.years = [2015, 2020]
        mode = "synthetic"
    else:
        mode = "auto_download" if fetch_meta else "file"

    # Validate inputs
    water_freq_path = Path(args.water_frequency) if args.water_frequency else None
    water_masks_path = Path(args.water_masks) if args.water_masks else None

    if water_freq_path and not water_freq_path.exists():
        print(f"ERROR: Water frequency raster not found: {water_freq_path}", file=sys.stderr)
        return EXIT_ARG
    if water_masks_path and not water_masks_path.exists():
        print(f"ERROR: Water masks raster not found: {water_masks_path}", file=sys.stderr)
        return EXIT_ARG
    if not water_freq_path and not water_masks_path:
        print("ERROR: Must provide --synthetic, --water-frequency, or --water-masks", file=sys.stderr)
        return EXIT_ARG

    years = args.years
    if not years or len(years) < 1:
        print("ERROR: At least one year required", file=sys.stderr)
        return EXIT_ARG

    freq_thresholds = tuple(args.frequency_thresholds) if args.frequency_thresholds else (0.25, 0.75)
    min_area = args.min_area if args.min_area else 0.5

    try:
        # Read input data
        print("Reading water data...")
        if water_freq_path:
            with rasterio.open(water_freq_path) as ds:
                n_bands = ds.count
                water_data = ds.read().astype(np.float64)
                transform = ds.transform
                crs = str(ds.crs) if ds.crs else "EPSG:4326"
                nodata = ds.nodata
                shape = (ds.height, ds.width)
        else:
            with rasterio.open(water_masks_path) as ds:
                n_bands = ds.count
                water_data = ds.read().astype(np.float64)
                transform = ds.transform
                crs = str(ds.crs) if ds.crs else "EPSG:4326"
                nodata = ds.nodata
                shape = (ds.height, ds.width)

        # Validate band count matches years
        if n_bands != len(years):
            print(f"WARNING: Band count ({n_bands}) != year count ({len(years)}). "
                  f"Using min of both.", file=sys.stderr)
            n_bands = min(n_bands, len(years))
            water_data = water_data[:n_bands]
            years = years[:n_bands]

        # Apply nodata mask
        if nodata is not None:
            water_data[water_data == nodata] = 0

        # Compute inundation frequency
        print("Computing inundation frequency...")
        frequency = compute_inundation_frequency(water_data)

        # Classify wetland types (using full time span)
        print("Classifying wetland types...")
        classification = classify_wetland_type(frequency, freq_thresholds)

        # Compute pixel area
        from rasterio.crs import CRS
        crs_obj = CRS.from_string(crs) if crs else None
        if crs_obj and crs_obj.is_projected:
            pixel_area_ha = abs(transform.a * transform.e) / 10000
        else:
            pixel_area_ha = (abs(transform.a) * 111320) * (abs(transform.e) * 111320) / 10000

        # Compute transition matrix (first vs last year)
        if n_bands >= 2:
            print("Computing transition matrix...")
            early_freq = compute_inundation_frequency(water_data[:1])
            late_freq = compute_inundation_frequency(water_data[-1:])
            early_class = classify_wetland_type(early_freq, freq_thresholds)
            late_class = classify_wetland_type(late_freq, freq_thresholds)
            transition_matrix = compute_transition_matrix(early_class, late_class)
        else:
            transition_matrix = np.zeros((5, 5), dtype=np.int64)

        # Identify change patches
        print("Identifying change patches...")
        if n_bands >= 2:
            patches = identify_change_patches(
                early_class, late_class,
                early_freq, late_freq,
                min_area_ha=min_area,
                pixel_area_ha=pixel_area_ha,
            )
        else:
            patches = []

        print(f"  Found {len(patches)} change patches")

        # Write outputs
        print("Writing outputs...")

        # Inundation frequency raster
        freq_path = output_dir / "inundation_frequency.tif"
        with rasterio.open(
            str(freq_path), "w", driver="GTiff",
            height=shape[0], width=shape[1],
            count=1, dtype="float64", crs=crs,
            transform=transform, nodata=-9999,
        ) as dst:
            out_freq = frequency.copy()
            out_freq[np.isnan(out_freq)] = -9999
            dst.write(out_freq, 1)

        # Wetland type classification raster
        type_path = output_dir / "wetland_type.tif"
        with rasterio.open(
            str(type_path), "w", driver="GTiff",
            height=shape[0], width=shape[1],
            count=1, dtype="uint8", crs=crs,
            transform=transform, nodata=0,
        ) as dst:
            dst.write(classification, 1)

        # Change patches GeoJSON
        geojson = vectorize_changes(patches, crs=crs)
        geojson_path = output_dir / "wetland_change.geojson"
        with open(geojson_path, "w", encoding="utf-8") as f:
            json.dump(geojson, f, ensure_ascii=False, indent=2, default=str)

        # Transition matrix CSV
        matrix_path = output_dir / "transition_matrix.csv"
        write_transition_matrix_csv(transition_matrix, years, matrix_path)

        # Summary report
        type_counts = {}
        for code, name in WETLAND_TYPES.items():
            type_counts[name] = int(np.sum(classification == code))

        change_summary = {}
        for p in patches:
            ct = p["change_type"]
            change_summary[ct] = change_summary.get(ct, 0) + 1

        report = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "years": years,
            "crs": crs,
            "shape": list(shape),
            "pixel_area_ha": round(pixel_area_ha, 6),
            "frequency_thresholds": list(freq_thresholds),
            "type_counts": type_counts,
            "change_summary": change_summary,
            "total_change_patches": len(patches),
            "total_change_area_ha": round(sum(p["area_ha"] for p in patches), 2),
            "inundation_frequency_stats": {
                "mean": round(float(np.mean(frequency)), 4),
                "min": round(float(np.min(frequency)), 4),
                "max": round(float(np.max(frequency)), 4),
            },
        }
        report_path = output_dir / "wetland-report.json"
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)

        # Manifest
        manifest_path = output_dir / "output-manifest.json"
        manifest = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "mode": mode,
            "input": str(water_freq_path or water_masks_path),
            "years": years,
            "output_dir": str(output_dir),
            "output_files": {
                "inundation_frequency.tif": str(freq_path),
                "wetland_type.tif": str(type_path),
                "wetland_change.geojson": str(geojson_path),
                "transition_matrix.csv": str(matrix_path),
                "wetland-report.json": str(report_path),
                "output-manifest.json": str(manifest_path),
            },
            "results": {
                "total_patches": len(patches),
                "type_counts": type_counts,
                "change_summary": change_summary,
            },
            "parameters": {k: v for k, v in vars(args).items() if not k.startswith("_") and not callable(v)},
        }
        if fetch_meta:
            manifest["data_source"] = fetch_meta.get("data_source")
            manifest["fetched_at"] = fetch_meta.get("fetched_at")
            if fetch_meta.get("collection"):
                manifest["collection"] = fetch_meta["collection"]
            if fetch_meta.get("jrc_path"):
                manifest["jrc_downloaded"] = fetch_meta["jrc_path"]
            if fetch_meta.get("sentinel1_paths"):
                manifest["sentinel1_downloaded"] = fetch_meta["sentinel1_paths"]
        # T9 manifest field injection (idempotent, ensures 3 required field groups)
        try:
            if isinstance(manifest, dict):
                of_aliases = {"output_files", "files", "outputs", "artifacts", "products", "result_files"}
                ps_aliases = {"parameters", "summary", "params", "args", "inputs", "result", "results", "stats", "metrics", "qc_summary", "findings"}
                ts_aliases = {"timestamp", "generated_at", "date", "created_at", "run_time", "datetime", "time", "ts"}
                if not any(k in manifest for k in of_aliases):
                    manifest["output_files"] = {}
                if not any(k in manifest for k in ps_aliases):
                    try:
                        manifest["parameters"] = {k: v for k, v in vars(args).items() if not k.startswith("_") and not callable(v)}
                    except Exception:
                        manifest["parameters"] = {"_info": "auto-injected"}
                if not any(k in manifest for k in ts_aliases):
                    manifest["timestamp"] = datetime.now(timezone.utc).isoformat()
        except Exception:
            pass
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)

        print(f"\nOutput: {output_dir}")
        print(f"  Change patches: {len(patches)}")
        print(f"  Total change area: {report['total_change_area_ha']:.2f} ha")
        return EXIT_OK

    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return EXIT_PROCESSING


def main():
    parser = argparse.ArgumentParser(description="Wetland Change Monitor")
    parser.add_argument("--water-frequency", help="Multi-band water frequency raster (JRC-style)")
    parser.add_argument("--water-masks", help="Multi-band binary water masks (1=water, 0=dry)")
    parser.add_argument("--synthetic", action="store_true",
                        help="Run with synthetic demo water mask raster (2 bands for 2 periods)")
    parser.add_argument("--years", nargs="+", type=int, help="Years corresponding to bands")
    parser.add_argument("--frequency-thresholds", nargs=2, type=float,
                        help="Two thresholds: seasonal_low seasonal_high (default: 0.25 0.75)")
    parser.add_argument("--change-schema", nargs="+", default=["degradation", "recovery", "stable"],
                        help="Change types to detect")
    parser.add_argument("--include-sar", action="store_true",
                        help="Include SAR-based water detection")
    parser.add_argument("--min-area", type=float, default=0.5,
                        help="Minimum patch area in hectares (default: 0.5)")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    if add_bbox_date_args is not None:
        add_bbox_date_args(parser)

    args = parser.parse_args()

    # Validate: --synthetic OR --water-frequency OR --water-masks OR --bbox/--aoi-file required
    if not args.synthetic and not args.water_frequency and not args.water_masks \
            and not (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)):
        print("ERROR: --synthetic, --water-frequency, --water-masks, or --bbox/--aoi-file is required",
              file=sys.stderr)
        sys.exit(2)

    try:
        sys.exit(run_wetland_monitor(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
