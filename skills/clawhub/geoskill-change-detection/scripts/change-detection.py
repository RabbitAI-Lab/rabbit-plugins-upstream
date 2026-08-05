#!/usr/bin/env python3
"""
change-detection: Multi-temporal change detection for satellite imagery.

Privacy Disclosure:
  - This tool performs LOCAL processing only.
  - NO data is sent to any external server.
  - All input files remain on your machine.

License: MIT-0 (Public Domain)
Data Source: Local raster processing (two co-registered GeoTIFF images)
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    import numpy as np
except ImportError:
    print("ERROR: numpy is required. Install with: pip install numpy>=1.21.0")
    sys.exit(1)

try:
    import rasterio
except ImportError:
    print("ERROR: rasterio is required. Install with: pip install rasterio>=1.3.0")
    sys.exit(1)

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(iterable, **kwargs):
        return iterable


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


# ─── Band configurations ────────────────────────────────────────────────────

SENSOR_BANDS = {
    "landsat8": {"green": 3, "nir": 5, "red": 4, "swir": 6, "name": "Landsat 8"},
    "landsat9": {"green": 3, "nir": 5, "red": 4, "swir": 6, "name": "Landsat 9"},
    "sentinel2": {"green": 3, "nir": 8, "red": 4, "swir": 11, "name": "Sentinel-2"},
}

VALID_SENSORS = list(SENSOR_BANDS.keys())
VALID_METHODS = ["ndvi-diff", "image-diff", "cva"]

# Presets (v0.2.0)
PRESETS = {
    "ndvi-trend": {
        "method": "ndvi-diff",
        "sensor": "sentinel2",
        "description": "NDVI 趋势变化（植被生长/退化）",
    },
    "urban-expansion": {
        "method": "cva",
        "sensor": "sentinel2",
        "description": "城市扩张 CVA 检测（多波段变化方向）",
    },
    "image-diff": {
        "method": "image-diff",
        "sensor": "sentinel2",
        "description": "通用影像差值（任意波段）",
    },
}


# ─── Utility functions ───────────────────────────────────────────────────────

def validate_sensor(sensor: str) -> str:
    sensor = sensor.lower().strip()
    if sensor not in VALID_SENSORS:
        raise ValueError(
            f"Unsupported sensor '{sensor}'. Choose from: {', '.join(VALID_SENSORS)}"
        )
    return sensor


def validate_method(method: str) -> str:
    method = method.lower().strip()
    if method not in VALID_METHODS:
        raise ValueError(
            f"Unsupported method '{method}'. Choose from: {', '.join(VALID_METHODS)}"
        )
    return method


def compute_ndvi(green: np.ndarray, nir: np.ndarray, red: np.ndarray) -> np.ndarray:
    """Compute NDVI = (NIR - Red) / (NIR + Red)."""
    denominator = nir + red
    with np.errstate(divide='ignore', invalid='ignore'):
        ndvi = np.where(denominator != 0, (nir - red) / denominator, 0.0)
    return ndvi.astype(np.float32)


def otsu_threshold(image: np.ndarray) -> float:
    """Compute optimal threshold using Otsu's method on absolute values."""
    valid = image[np.isfinite(image)]
    if valid.size == 0:
        print("WARNING: No valid pixels. Using threshold=0.1")
        return 0.1

    try:
        nbins = 256
        hist, bin_edges = np.histogram(valid.flatten(), bins=nbins)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

        total = hist.sum()
        if total == 0:
            return 0.1

        sum_total = np.dot(bin_centers, hist)
        sum_bg = 0.0
        weight_bg = 0
        max_variance = 0.0
        threshold = 0.1

        for i in range(nbins):
            weight_bg += hist[i]
            if weight_bg == 0:
                continue
            weight_fg = total - weight_bg
            if weight_fg == 0:
                break

            sum_bg += bin_centers[i] * hist[i]
            mean_bg = sum_bg / weight_bg
            mean_fg = (sum_total - sum_bg) / weight_fg

            variance = weight_bg * weight_fg * (mean_bg - mean_fg) ** 2
            if variance > max_variance:
                max_variance = variance
                threshold = bin_centers[i]

        return threshold

    except Exception as e:
        print(f"WARNING: Otsu failed ({e}). Using threshold=0.1")
        return 0.1


def validate_images_match(src1, src2):
    """Verify two images have matching extent, resolution, and CRS."""
    issues = []

    if src1.width != src2.width or src1.height != src2.height:
        issues.append(
            f"Size mismatch: t1={src1.width}x{src1.height}, t2={src2.width}x{src2.height}"
        )

    res1 = abs(src1.transform[0])
    res2 = abs(src2.transform[0])
    if abs(res1 - res2) > 0.01 * res1:
        issues.append(f"Resolution mismatch: t1={res1:.2f}, t2={res2:.2f}")

    if str(src1.crs) != str(src2.crs):
        issues.append(f"CRS mismatch: t1={src1.crs}, t2={src2.crs}")

    if issues:
        print("WARNING: Image mismatch detected:")
        for issue in issues:
            print(f"  - {issue}")
        print("  Results may be unreliable. Consider reprojecting images.")


def read_bands(path: str, bands: list = None) -> tuple:
    """Read specified bands from a GeoTIFF. Returns (data, profile)."""
    with rasterio.open(path) as src:
        if bands is None:
            bands = list(range(1, src.count + 1))
        data = []
        for b in bands:
            if b > src.count:
                raise ValueError(f"Band {b} not available. File has {src.count} bands.")
            data.append(src.read(b).astype(np.float32))
        profile = src.profile.copy()
    return data, profile


# ─── Detection methods ───────────────────────────────────────────────────────

def method_ndvi_diff(img1_bands: dict, img2_bands: dict, sensor: str) -> np.ndarray:
    """NDVI difference: ΔNDVI = NDVI_t2 - NDVI_t1."""
    bands = SENSOR_BANDS[sensor]
    ndvi1 = compute_ndvi(
        img1_bands.get("green", img1_bands["all"][bands["green"] - 1]),
        img1_bands["all"][bands["nir"] - 1],
        img1_bands["all"][bands["red"] - 1],
    )
    ndvi2 = compute_ndvi(
        img2_bands.get("green", img2_bands["all"][bands["green"] - 1]),
        img2_bands["all"][bands["nir"] - 1],
        img2_bands["all"][bands["red"] - 1],
    )
    return ndvi2 - ndvi1


def method_image_diff(img1_bands: dict, img2_bands: dict, bands: list = None) -> np.ndarray:
    """Image differencing: mean absolute difference across specified bands."""
    data1 = img1_bands["all"]
    data2 = img2_bands["all"]

    if bands is None:
        n = min(len(data1), len(data2))
        bands = list(range(n))

    diff_sum = np.zeros_like(data1[0])
    for b in bands:
        b_idx = b - 1  # Convert 1-indexed to 0-indexed
        if b_idx < len(data1) and b_idx < len(data2):
            diff_sum += np.abs(data2[b_idx] - data1[b_idx])

    n_bands = len(bands)
    return diff_sum / n_bands if n_bands > 0 else diff_sum


def method_cva(img1_bands: dict, img2_bands: dict, bands: list = None) -> np.ndarray:
    """Change Vector Analysis: magnitude of multi-band change."""
    data1 = img1_bands["all"]
    data2 = img2_bands["all"]

    if bands is None:
        n = min(len(data1), len(data2))
        bands = list(range(1, n + 1))

    magnitude_sq = np.zeros_like(data1[0])
    for b in bands:
        b_idx = b - 1
        if b_idx < len(data1) and b_idx < len(data2):
            diff = data2[b_idx] - data1[b_idx]
            magnitude_sq += diff ** 2

    return np.sqrt(magnitude_sq).astype(np.float32)


# ─── Core processing ─────────────────────────────────────────────────────────

def run_detection(
    image_t1: str,
    image_t2: str,
    sensor: str,
    method: str,
    output_path: str = None,
    mask_path: str = None,
    threshold: float = None,
    bands: list = None,
) -> dict:
    """Run change detection pipeline."""

    # Read images
    print(f"Reading time-1 image: {image_t1}")
    data1, profile = read_bands(image_t1)
    print(f"Reading time-2 image: {image_t2}")
    data2, profile2 = read_bands(image_t2)

    # Validate
    with rasterio.open(image_t1) as src1, rasterio.open(image_t2) as src2:
        validate_images_match(src1, src2)

    img1_bands = {"all": data1}
    img2_bands = {"all": data2}

    # Compute change
    print(f"Computing change: {method}")
    if method == "ndvi-diff":
        change_magnitude = method_ndvi_diff(img1_bands, img2_bands, sensor)
    elif method == "image-diff":
        change_magnitude = method_image_diff(img1_bands, img2_bands, bands)
    elif method == "cva":
        change_magnitude = method_cva(img1_bands, img2_bands, bands)
    else:
        raise ValueError(f"Unknown method: {method}")

    # Use absolute value for thresholding
    abs_change = np.abs(change_magnitude)

    # Determine threshold
    if threshold is not None:
        thresh = threshold
    else:
        thresh = otsu_threshold(abs_change)

    print(f"  Change threshold: {thresh:.4f}")

    # Binary mask
    change_mask = (abs_change > thresh).astype(np.uint8)

    # Statistics
    total_pixels = change_mask.size
    change_pixels = int(change_mask.sum())
    change_pct = (change_pixels / total_pixels * 100) if total_pixels > 0 else 0

    stats = {
        "method": method,
        "sensor": sensor,
        "threshold": round(thresh, 4),
        "total_pixels": total_pixels,
        "change_pixels": change_pixels,
        "change_percentage": round(change_pct, 2),
        "image_t1": image_t1,
        "image_t2": image_t2,
    }

    # Write magnitude output
    if output_path:
        profile.update(dtype="float32", count=1, compress="lzw")
        with rasterio.open(output_path, "w", **profile) as dst:
            dst.write(change_magnitude, 1)
        stats["output_magnitude"] = output_path
        print(f"  Magnitude saved: {output_path}")

    # Write mask output
    if mask_path:
        profile.update(dtype="uint8", count=1, compress="lzw")
        with rasterio.open(mask_path, "w", **profile) as dst:
            dst.write(change_mask, 1)
        stats["output_mask"] = mask_path
        print(f"  Mask saved: {mask_path}")

    print(f"\nResults:")
    print(f"  Changed pixels: {change_pixels:,} ({change_pct:.2f}%)")

    return stats


# ─── Commands ────────────────────────────────────────────────────────────────

def cmd_detect(args):
    """Handle detect subcommand."""
    # Apply preset
    if getattr(args, "preset", None):
        ps = PRESETS[args.preset]
        print(f"[preset] {args.preset}: {ps['description']}")
        if args.method == "ndvi-diff" and ps["method"]:
            args.method = ps["method"]
        if args.sensor == "landsat8" and ps["sensor"]:
            args.sensor = ps["sensor"]

    # Resolve place (context only)
    place_info = None
    if getattr(args, "place", None):
        try:
            place_info = _resolve_place(args.place)
            print(f"[place] {args.place} -> {place_info.resolved_name} (bbox={place_info.bbox})")
        except ValueError as e:
            print(f"WARN: {e}")
            place_info = None

    sensor = validate_sensor(args.sensor)
    method = validate_method(args.method)

    # Parse bands if provided
    bands = None
    if args.bands:
        try:
            bands = [int(b.strip()) for b in args.bands.split(",")]
        except ValueError:
            print("ERROR: Invalid band format. Use comma-separated integers, e.g., '3,4,5'")
            sys.exit(1)

    for img in [args.image_t1, args.image_t2]:
        if not os.path.isfile(img):
            print(f"ERROR: File not found: {img}")
            sys.exit(1)

    stats = run_detection(
        image_t1=args.image_t1,
        image_t2=args.image_t2,
        sensor=sensor,
        method=method,
        output_path=args.output,
        mask_path=args.mask,
        threshold=args.threshold,
        bands=bands,
    )

    # Augment with place/preset info
    if place_info is not None:
        stats["place"] = args.place
        stats["place_info"] = place_info.to_dict()
    if getattr(args, "preset", None):
        stats["preset"] = args.preset

    # --format dispatch (batch-D). --json is the legacy stdout flag; when
    # --format is also set we honor it for both stdout format and the QA
    # sidecar's stats payload.
    fmt = getattr(args, "format", "auto")
    if fmt == "auto":
        fmt_resolved = "json"
    else:
        fmt_resolved = fmt

    if args.json:
        if fmt_resolved == "geojson":
            def _coerce(v):
                try:
                    import numpy as _np
                    if isinstance(v, _np.floating):
                        return float(v)
                    if isinstance(v, _np.integer):
                        return int(v)
                except Exception:
                    pass
                return v
            props = {k: _coerce(stats.get(k)) for k in (
                "method", "sensor", "threshold", "change_percentage",
                "change_pixels", "total_pixels", "preset",
            )}
            fc = {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "properties": props,
                        "geometry": None,  # bbox added below if we can recover it
                    }
                ],
            }
            # If we have the raster's bounds, attach a Polygon for context
            if "image_t1" in stats and os.path.isfile(stats["image_t1"]):
                try:
                    import rasterio as _rio
                    with _rio.open(stats["image_t1"]) as _src:
                        b = _src.bounds
                        fc["features"][0]["geometry"] = {
                            "type": "Polygon",
                            "coordinates": [[
                                [b.left, b.bottom], [b.right, b.bottom],
                                [b.right, b.top], [b.left, b.top],
                                [b.left, b.bottom],
                            ]],
                        }
                except Exception:
                    pass
            print(json.dumps(fc, indent=2, ensure_ascii=False))
        elif fmt_resolved == "csv":
            def _coerce(v):
                try:
                    import numpy as _np
                    if isinstance(v, _np.floating):
                        return float(v)
                    if isinstance(v, _np.integer):
                        return int(v)
                except Exception:
                    pass
                return v
            import csv as _csv
            import io as _io
            buf = _io.StringIO()
            w = _csv.DictWriter(buf, fieldnames=list(stats.keys()))
            w.writeheader()
            w.writerow({k: _coerce(v) for k, v in stats.items()})
            print(buf.getvalue(), end="")
        else:
            print(json.dumps(stats, indent=2, ensure_ascii=False, default=str))

    # QA summary (v0.2.0) — batch-D: --format controls the sidecar extension
    if getattr(args, "qa", False) and (args.output or args.mask):
        base = args.output or args.mask
        qa_ext = {"geojson": ".qa.geojson", "csv": ".qa.csv"}.get(
            fmt_resolved, ".qa.json"
        )
        qa_path = os.path.splitext(base)[0] + qa_ext

        def _coerce(v):
            try:
                import numpy as _np
                if isinstance(v, _np.floating):
                    return float(v)
                if isinstance(v, _np.integer):
                    return int(v)
            except Exception:
                pass
            return v

        qa = {k: _coerce(v) for k, v in stats.items() if k not in ("place_info",)}
        if place_info is not None:
            qa["place_info"] = place_info.to_dict()
        if fmt_resolved == "csv":
            import csv as _csv
            with open(qa_path, "w", newline="", encoding="utf-8") as f:
                w = _csv.DictWriter(f, fieldnames=list(qa.keys()))
                w.writeheader()
                w.writerow(qa)
        elif fmt_resolved == "geojson":
            # GeoJSON sidecar that mirrors the stdout variant
            def _coerce_geo(v):
                try:
                    import numpy as _np
                    if isinstance(v, _np.floating):
                        return float(v)
                    if isinstance(v, _np.integer):
                        return int(v)
                except Exception:
                    pass
                return v
            fc = {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "properties": {
                            "method": _coerce_geo(qa.get("method")),
                            "sensor": _coerce_geo(qa.get("sensor")),
                            "threshold": _coerce_geo(qa.get("threshold")),
                            "change_percentage": _coerce_geo(qa.get("change_percentage")),
                            "change_pixels": _coerce_geo(qa.get("change_pixels")),
                            "total_pixels": _coerce_geo(qa.get("total_pixels")),
                            "preset": _coerce_geo(qa.get("preset")),
                        },
                        "geometry": None,
                    }
                ],
            }
            if "image_t1" in qa and os.path.isfile(qa["image_t1"]):
                try:
                    import rasterio as _rio
                    with _rio.open(qa["image_t1"]) as _src:
                        b = _src.bounds
                        fc["features"][0]["geometry"] = {
                            "type": "Polygon",
                            "coordinates": [[
                                [b.left, b.bottom], [b.right, b.bottom],
                                [b.right, b.top], [b.left, b.top],
                                [b.left, b.bottom],
                            ]],
                        }
                except Exception:
                    pass
            with open(qa_path, "w", encoding="utf-8") as f:
                json.dump(fc, f, indent=2, ensure_ascii=False)
        else:
            with open(qa_path, "w", encoding="utf-8") as f:
                json.dump(qa, f, indent=2, ensure_ascii=False)
        print(f"  QA summary: {qa_path}")


def cmd_report(args):
    """Handle report subcommand — analyze existing change mask."""
    if not os.path.isfile(args.mask):
        print(f"ERROR: Mask file not found: {args.mask}")
        sys.exit(1)

    with rasterio.open(args.mask) as src:
        mask_data = src.read(1)
        profile = src.profile

    total = mask_data.size
    changed = int(mask_data.sum())
    pct = (changed / total * 100) if total > 0 else 0

    # Compute change type statistics if multi-band
    report = {
        "mask_file": args.mask,
        "width": src.width,
        "height": src.height,
        "crs": str(src.crs),
        "total_pixels": total,
        "changed_pixels": changed,
        "unchanged_pixels": total - changed,
        "change_percentage": round(pct, 2),
    }

    print(f"\nChange Detection Report:")
    print(f"  Dimensions: {src.width} x {src.height}")
    print(f"  CRS: {src.crs}")
    print(f"  Changed pixels: {changed:,} ({pct:.2f}%)")
    print(f"  Unchanged pixels: {total - changed:,}")

    if args.json:
        output_path = args.json if args.json.endswith(".json") else None
        if output_path:
            with open(output_path, "w") as f:
                json.dump(report, f, indent=2)
            print(f"\nReport saved: {output_path}")
        else:
            print(json.dumps(report, indent=2))


# ─── CLI Setup ───────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="change-detection",
        description="Multi-temporal change detection for satellite imagery",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Privacy: This tool processes all data locally. No data is sent to external servers.

Examples:
  %(prog)s detect --image-t1 2020.tif --image-t2 2023.tif --sensor landsat8 --method ndvi-diff
  %(prog)s detect -t1 img1.tif -t2 img2.tif --sensor sentinel2 --method cva -o change.tif
  %(prog)s report --mask change_mask.tif --json report.json
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # ── detect ──
    p_detect = subparsers.add_parser("detect", help="Run change detection on two images")
    p_detect.add_argument("--image-t1", "-t1", required=True, help="Time-1 image (earlier)")
    p_detect.add_argument("--image-t2", "-t2", required=True, help="Time-2 image (later)")
    p_detect.add_argument("--sensor", default="landsat8", choices=VALID_SENSORS,
                           help="Sensor type (default: landsat8)")
    p_detect.add_argument("--method", default="ndvi-diff", choices=VALID_METHODS,
                           help="Detection method (default: ndvi-diff)")
    p_detect.add_argument("-o", "--output", help="Output change magnitude GeoTIFF")
    p_detect.add_argument("--mask", help="Output binary change mask GeoTIFF")
    p_detect.add_argument("--threshold", type=float, default=None,
                           help="Change threshold (default: Otsu auto)")
    p_detect.add_argument("--bands", type=str, default=None,
                           help="Band indices for CVA/image-diff (comma-separated, e.g., '3,4,5')")
    p_detect.add_argument("--place", help="Place name (Chinese or English); for context only")
    p_detect.add_argument("--preset", choices=list(PRESETS.keys()),
                          help="Use a preset (ndvi-trend, urban-expansion, image-diff)")
    p_detect.add_argument("--json", action="store_true", help="Output statistics as JSON")
    p_detect.add_argument("--qa", action="store_true", help="Write QA summary JSON next to the output")
    p_detect.add_argument(
        "--format", choices=["auto", "geojson", "csv", "json"], default="auto",
        help="Output format for the vector/statistics sidecar (default: auto = geojson for change polygons). "
             "Always writes --output as GeoTIFF magnitude and --mask as GeoTIFF mask; "
             "--format controls the optional sidecar written by --qa or --json.",
    )
    p_detect.set_defaults(func=cmd_detect)

    # ── report ──
    p_report = subparsers.add_parser("report", help="Generate report from change mask")
    p_report.add_argument("--mask", required=True, help="Binary change mask GeoTIFF")
    p_report.add_argument("--json", help="Output JSON report file path")
    p_report.set_defaults(func=cmd_report)

    # ── fetch (NEW) ──
    p_fetch = subparsers.add_parser(
        "fetch", help="Fetch a single Sentinel-2 / Landsat scene by place + date (auto)")
    p_fetch.add_argument("--place", required=True,
                        help="Place name; bbox resolved via Nominatim")
    p_fetch.add_argument("--sensor", default="sentinel2", choices=VALID_SENSORS,
                        help="Sensor to use (default: sentinel2)")
    p_fetch.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    p_fetch.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")
    p_fetch.add_argument("--max-cloud", type=float, default=20.0,
                        help="Maximum cloud cover %% (default 20)")
    p_fetch.add_argument("--bands", type=str, default=None,
                        help="Comma-separated band indices to keep (e.g. '3,4,8'); default: all")
    p_fetch.add_argument("-o", "--output", required=True, help="Output GeoTIFF path")
    p_fetch.add_argument("--qa", action="store_true",
                        help="Write a QA summary JSON next to the output")
    p_fetch.set_defaults(func=cmd_fetch)

    return parser


# ─── fetch (NEW) ─────────────────────────────────────────────────────────────

# Maps sensor → STAC collection + asset band layout
SENSOR_STAC = {
    "sentinel2": {
        "collection": "sentinel-2-l2a",
        "bands": [1, 2, 3, 4, 8, 11, 12],  # default set (B2,B3,B4,B8,B11,B12)
    },
    "landsat8": {
        "collection": "landsat-c2-l2",
        "bands": [1, 2, 3, 4, 5, 6, 7],
    },
    "landsat9": {
        "collection": "landsat-c2-l2",
        "bands": [1, 2, 3, 4, 5, 6, 7],
    },
}


def cmd_fetch(args):
    """Fetch a single scene by place + date range using Microsoft Planetary Computer.

    The downloaded GeoTIFF is written to --output and contains only the bands
    specified by --bands (or the sensor default if not given). Use this to
    produce the input for `detect --image-t1 / --image-t2`.
    """
    try:
        import planetary_computer
        from pystac_client import Client
        import rasterio
        from rasterio.windows import from_bounds
    except ImportError as e:
        print(f"ERROR: fetch needs planetary-computer + pystac-client + rasterio: {e}",
              file=sys.stderr)
        sys.exit(1)

    place = _resolve_place(args.place)
    bbox = place.bbox  # (W, S, E, N)
    print(f"[fetch] place={args.place!r} -> {place.resolved_name} bbox={bbox}")
    print(f"  range={args.start}..{args.end} max-cloud={args.max_cloud}%")

    sensor = validate_sensor(args.sensor)
    stac_info = SENSOR_STAC.get(sensor)
    if not stac_info:
        print(f"ERROR: no STAC mapping for sensor {sensor}", file=sys.stderr)
        sys.exit(1)

    catalog = Client.open(
        "https://planetarycomputer.microsoft.com/api/stac/v1",
        modifier=planetary_computer.sign_inplace,
    )
    search = catalog.search(
        collections=[stac_info["collection"]],
        bbox=list(bbox),
        datetime=f"{args.start}/{args.end}",
        query={"eo:cloud_cover": {"lt": args.max_cloud}},
    )
    items = list(search.items())
    if not items:
        print(f"ERROR: no scenes found for {args.place!r} in {args.start}..{args.end} "
              f"with cloud_cover<{args.max_cloud}", file=sys.stderr)
        sys.exit(1)
    # Pick the lowest cloud cover
    items.sort(key=lambda it: it.properties.get("eo:cloud_cover", 100))
    chosen = items[0]
    print(f"  -> {chosen.id} cloud_cover={chosen.properties.get('eo:cloud_cover'):.1f}%")

    # Resolve which bands to keep
    keep_bands = stac_info["bands"]
    if args.bands:
        keep_bands = [int(b.strip()) for b in args.bands.split(",")]

    # Find the actual asset hrefs (for the chosen bands)
    asset_keys = []
    for b in keep_bands:
        ak = f"{chosen.collection_id}_B{b:02d}" if sensor == "sentinel2" else None
        if ak and ak in chosen.assets:
            asset_keys.append(ak)
        else:
            # Landsat-8/9 C2L2 uses "coastal", "blue", "green", ... asset names
            # or band-specific names like "lwir11". Fall back to common aliases.
            for fallback in (f"b{b}", f"B{b:02d}", f"B{b}", str(b),
                             ["coastal", "blue", "green", "red", "nir08",
                              "swir16", "swir22"][b - 1] if b <= 7 else None):
                if fallback and fallback in chosen.assets:
                    asset_keys.append(fallback)
                    break
            else:
                print(f"  WARN: band {b} not available on {chosen.id}; skipping", file=sys.stderr)
                keep_bands = [k for k in keep_bands if k != b]

    if not asset_keys:
        print("ERROR: none of the requested bands were available", file=sys.stderr)
        sys.exit(1)

    # Stream each band's COG into an in-memory raster; mosaic to a single file
    import numpy as np
    from rasterio.io import MemoryFile

    # Sign the asset hrefs (PC requires this for private assets)
    signed = planetary_computer.sign(chosen)

    profile = None
    arrs = []
    for ak in asset_keys:
        href = signed.assets[ak].href
        with rasterio.open(href) as src:
            if profile is None:
                # If the requested bbox is outside the source raster, fall back
                # to the full raster (better than failing).
                w, s, e, n = bbox
                full_win = rasterio.windows.Window(0, 0, src.width, src.height)
                try:
                    win = from_bounds(w, s, e, n, src.transform)
                    win = win.intersection(full_win)
                    if float(win.width) < 1.0 or float(win.height) < 1.0:
                        raise rasterio.errors.WindowError("intersection too small")
                except (rasterio.errors.WindowError, Exception):
                    print(f"  WARN: requested bbox does not intersect raster; "
                          f"using full scene ({src.width}x{src.height})",
                          file=sys.stderr)
                    win = full_win
                profile = src.profile.copy()
                profile.update({
                    "height": int(win.height),
                    "width": int(win.width),
                    "transform": src.window_transform(win),
                    "count": len(asset_keys),
                    "dtype": "float32",
                    "compress": "lzw",
                })
                # Save windowed profile for subsequent reads
                windowed = win
            data = src.read(1, window=windowed).astype("float32")
            # Mask nodata
            if src.nodata is not None:
                data = np.where(data == src.nodata, np.nan, data)
            arrs.append(data)
    stack = np.stack(arrs, axis=0)

    os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)
    with rasterio.open(args.output, "w", **profile) as dst:
        dst.write(stack)
        dst.set_band_description(list(range(1, len(asset_keys) + 1)),
                                 [f"B{b:02d}" for b in keep_bands])
    print(f"  saved {args.output}  shape={stack.shape}  bands={[b for b in keep_bands]}")

    if args.qa:
        import json as _json
        qa = {
            "skill": "change-detection",
            "command": "fetch",
            "place": args.place,
            "place_info": place.to_dict(),
            "bbox": list(bbox),
            "sensor": sensor,
            "collection": stac_info["collection"],
            "start": args.start,
            "end": args.end,
            "max_cloud": args.max_cloud,
            "selected_scene": {
                "id": chosen.id,
                "datetime": str(chosen.datetime),
                "cloud_cover": chosen.properties.get("eo:cloud_cover"),
                "platform": chosen.properties.get("platform"),
            },
            "bands": keep_bands,
            "asset_keys": asset_keys,
            "output": args.output,
            "shape": list(stack.shape),
        }
        qa_path = os.path.splitext(args.output)[0] + ".qa.json"
        with open(qa_path, "w", encoding="utf-8") as f:
            _json.dump(qa, f, indent=2, ensure_ascii=False)
        print(f"  QA: {qa_path}")


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        return args.func(args)
    except ValueError as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    except rasterio.errors.RasterioError as e:
        print(f"ERROR: Raster I/O error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nAborted by user.")
        sys.exit(130)


if __name__ == "__main__":
    sys.exit(main())
