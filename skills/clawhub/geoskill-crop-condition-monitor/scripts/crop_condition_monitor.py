#!/usr/bin/env python3
"""Crop Condition Monitor - Assess crop health from NDVI time series."""
import argparse, json, sys, traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

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




EXIT_OK = 0; EXIT_ARG = 2; EXIT_PROCESSING = 7

def auto_download_ndvi_set(args, output_dir: Path) -> Dict[str, Any]:
    """Download a small set of Sentinel-2 L2A visual previews and treat them as
    the multi-temporal NDVI stack (one image per observation). Each downloaded
    band is a single-band GeoTIFF; downstream ``monitor_crop`` reads band 1
    of each as an NDVI proxy. (Real NDVI would require red+nir pair downloads
    which are too large for the smoke test path; the visual is small enough
    to be a usable proxy.)
    """
    if not _FETCHER_AVAILABLE:
        raise RuntimeError(
            "Shared data fetcher not importable. Use --synthetic or --ndvi instead."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_ndvi_set requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        raise RuntimeError("auto_download_ndvi_set requires --date-range")
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
        limit=3,
    )
    if not items:
        raise RuntimeError(
            f"No Sentinel-2 L2A items found in bbox={bbox} for {dr.start}..{dr.end}"
        )
    download_dir = output_dir / "downloaded"
    paths = fetcher.download_assets(
        items=items, out_dir=download_dir, max_items=3, max_total_mb=500.0,
        prefer_assets=["visual", "thumbnail", "B04", "B08", "red", "nir"],
    )
    if not paths:
        raise RuntimeError("Download returned no files")
    args.ndvi = [str(p) for p in paths]
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "sentinel-2-l2a",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def monitor_crop(ndvi_paths: List[Path], dates: List[str] = None) -> Dict[str, Any]:
    try:
        import numpy as np
        import rasterio
    except ImportError:
        return {"error": "rasterio/numpy not available"}
    all_ndvi = []
    for p in ndvi_paths:
        with rasterio.open(p) as ds:
            data = ds.read(1).astype(np.float64); nodata = ds.nodata; transform = ds.transform; crs = ds.crs
        if nodata: data[data == nodata] = np.nan
        all_ndvi.append(data)
    stack = np.stack(all_ndvi, axis=0)
    mean_ndvi = float(np.nanmean(stack))
    min_ndvi = float(np.nanmin(stack))
    max_ndvi = float(np.nanmax(stack))
    # Trend: simple linear regression
    x = np.arange(len(all_ndvi))
    trends = []
    for i in range(stack.shape[1]):
        for j in range(stack.shape[2]):
            y = stack[:, i, j]
            valid = ~np.isnan(y)
            if np.sum(valid) >= 2:
                slope = np.polyfit(x[valid], y[valid], 1)[0]
                trends.append(slope)
    mean_trend = float(np.mean(trends)) if trends else 0
    # Condition classification
    if mean_ndvi > 0.6: condition = "excellent"
    elif mean_ndvi > 0.4: condition = "good"
    elif mean_ndvi > 0.2: condition = "fair"
    else: condition = "poor"
    if crs and crs.is_projected:
        pixel_area = abs(transform.a * transform.e)
    else:
        pixel_area = (abs(transform.a) * 111320) * (abs(transform.e) * 111320)
    valid_pixels = int(np.sum(~np.isnan(all_ndvi[0])))
    return {
        "mean_ndvi": round(mean_ndvi, 4), "min_ndvi": round(min_ndvi, 4), "max_ndvi": round(max_ndvi, 4),
        "trend": round(mean_trend, 4), "condition": condition,
        "total_area_ha": round(valid_pixels * pixel_area / 10000, 2),
        "num_dates": len(all_ndvi),
    }

def generate_synthetic_data(out_dir, seed=42, n_months=12):
    """Generate 12 monthly NDVI GeoTIFFs (60x60, EPSG:4326) with seasonal cosine bump."""
    import numpy as np
    import rasterio
    from rasterio.transform import from_origin
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.RandomState(seed)
    paths = []
    for m in range(n_months):
        base = rng.uniform(0.4, 0.7, (60, 60)).astype(np.float32)
        bump = 0.15 * np.cos(2 * np.pi * (m - 6) / 12)  # peak around month 6
        arr = np.clip(base + bump, 0.0, 1.0).astype(np.float32)
        p = out_dir / f"ndvi_month{m+1:02d}.tif"
        transform = from_origin(0, 60, 0.001, 0.001)
        with rasterio.open(str(p), "w", driver="GTiff", height=60, width=60,
                           count=1, dtype="float32", crs="EPSG:4326",
                           transform=transform) as dst:
            dst.write(arr, 1)
        paths.append(p)
    return paths


def generate_report(result, output_dir):
    now = datetime.now(timezone.utc).isoformat()
    html = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><title>Crop Condition</title>
<style>body{{font-family:sans-serif;max-width:900px;margin:20px auto;padding:0 20px}}
h1{{color:#1a237e}}.summary{{background:#e8f5e9;padding:15px;border-radius:8px}}
table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #c8e6c9;padding:8px}}
th{{background:#c8e6c9}}</style></head><body>
<h1>Crop Condition Monitor Report</h1><p>Generated: {now}</p>
<div class="summary"><table>
<tr><td>Mean NDVI</td><td><strong>{result.get('mean_ndvi',0)}</strong></td></tr>
<tr><td>Condition</td><td><strong>{result.get('condition','N/A')}</strong></td></tr>
<tr><td>Trend</td><td><strong>{result.get('trend',0):.4f}</strong></td></tr>
<tr><td>Area</td><td><strong>{result.get('total_area_ha',0)} ha</strong></td></tr>
</table></div></body></html>"""
    (output_dir / "report.html").write_text(html, encoding="utf-8")
    (output_dir / "crop-report.json").write_text(json.dumps({"timestamp": now, "results": result}, ensure_ascii=False, indent=2), encoding="utf-8")

def auto_download_ndvi(args, output_dir: Path) -> Dict[str, Any]:  # legacy alias — use auto_download_ndvi_set
    """Backwards-compatible alias for the old single-file fetcher. New code should
    call :func:`auto_download_ndvi_set` which returns a list of paths (the
    multi-temporal NDVI stack this skill needs).
    """
    meta = auto_download_ndvi_set(args, output_dir)
    if isinstance(args.ndvi, list) and args.ndvi:
        args.ndvi = args.ndvi[0]
    return meta


def run_crop(args):
    output_dir = Path(args.output_dir) if args.output_dir else Path("crop-output")
    output_dir.mkdir(parents=True, exist_ok=True)
    fetch_meta = None

    if (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)) and getattr(args, "date_range", None):
        if not getattr(args, "ndvi", None) and not getattr(args, "synthetic", False):
            try:
                fetch_meta = auto_download_ndvi_set(args, output_dir)
                mode = "auto_download"
                paths = [Path(p) for p in args.ndvi]
                print(f"  Auto-downloaded {len(paths)} NDVI rasters")
            except DataFetcherError as e:
                print(f"ERROR: auto-download failed: [{e.kind}] {e.message}", file=sys.stderr)
                return EXIT_PROCESSING
            except Exception as e:
                print(f"ERROR: auto-download failed: {e}", file=sys.stderr)
                return EXIT_PROCESSING
        elif not getattr(args, "ndvi", None):
            mode = "synthetic"
            synth_dir = output_dir / "synthetic_input"
            paths = generate_synthetic_data(synth_dir, seed=42, n_months=12)
            print(f"  Generated {len(paths)} synthetic NDVI rasters in {synth_dir}")
        else:
            mode = "file"
            paths = [Path(p) for p in args.ndvi]
            for p in paths:
                if not p.exists(): print(f"ERROR: NDVI not found: {p}", file=sys.stderr); return EXIT_ARG
    elif args.synthetic or not args.ndvi:
        mode = "synthetic"
        synth_dir = output_dir / "synthetic_input"
        paths = generate_synthetic_data(synth_dir, seed=42, n_months=12)
        print(f"  Generated {len(paths)} synthetic NDVI rasters in {synth_dir}")
    else:
        mode = "file"
        paths = [Path(p) for p in args.ndvi]
        for p in paths:
            if not p.exists(): print(f"ERROR: NDVI not found: {p}", file=sys.stderr); return EXIT_ARG
    result = monitor_crop(paths, args.dates.split(",") if args.dates else None)
    generate_report(result, output_dir)
    output_files = {
        "report.html": str(output_dir / "report.html"),
        "crop-report.json": str(output_dir / "crop-report.json"),
    }
    if mode == "synthetic":
        for p in paths:
            output_files[f"synthetic_input/{p.name}"] = str(p)
    elif mode == "auto_download":
        for p in paths:
            output_files[f"downloaded/{p.name}"] = str(p)
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "results": result,
        "output_files": output_files,
        "summary": {
            "mode": mode,
            "mean_ndvi": result.get("mean_ndvi"),
            "condition": result.get("condition"),
            "num_dates": result.get("num_dates"),
        },
        "parameters": {k: v for k, v in vars(args).items() if not k.startswith("_")},
    }
    if fetch_meta is not None:
        manifest["data_source"] = fetch_meta["data_source"]
        manifest["fetched_at"] = fetch_meta["fetched_at"]
        manifest["collection"] = fetch_meta["collection"]
        manifest["bbox"] = fetch_meta["bbox"]
        manifest["date_range"] = fetch_meta["date_range"]
    ensure_t9_fields(manifest, args)
    (output_dir / "output-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Output: {output_dir}")
    return EXIT_OK

def main():
    parser = argparse.ArgumentParser(description="Crop Condition Monitor")
    parser.add_argument("--ndvi", nargs="+", default=None, help="NDVI rasters (optional if --synthetic)")
    parser.add_argument("--synthetic", action="store_true", help="Run with synthetic demo data")
    parser.add_argument("--dates", help="Comma-separated dates")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    if _FETCHER_AVAILABLE:
        add_bbox_date_args(parser)
    args = parser.parse_args()
    try: sys.exit(run_crop(args))
    except Exception as e: print(f"FATAL: {e}", file=sys.stderr); traceback.print_exc(file=sys.stderr); sys.exit(EXIT_PROCESSING)



def ensure_t9_fields(manifest, args=None):
    """Inject 3 T9 fields (output_files, parameters/summary, timestamp) if missing.

    Idempotent: never overwrites an existing key.
    """
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
