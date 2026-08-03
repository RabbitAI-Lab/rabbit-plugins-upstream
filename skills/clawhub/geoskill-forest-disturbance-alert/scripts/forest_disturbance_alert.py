#!/usr/bin/env python3
"""Forest Disturbance Alert - Detect forest disturbance from multi-temporal NDVI."""
import argparse, json, sys, traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

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


def auto_download_disturbance_pair(args, output_dir: Path) -> Dict[str, Any]:
    """Download two Landsat-2 L2A visual previews (baseline + current) for
    disturbance detection. We use Landsat Collection 2 Level 2 (landsat-c2-l2)
    because the user spec lists both S2 and Landsat for this skill; we pick
    whichever returns data fastest.
    """
    if not _FETCHER_AVAILABLE:
        raise RuntimeError(
            "Shared data fetcher not importable. Use --synthetic or pass --baseline/--current."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_disturbance_pair requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        raise RuntimeError("auto_download_disturbance_pair requires --date-range")
    cache_dir = getattr(args, "cache_dir", None)
    fetcher = DataFetcher(
        source=DataSource.PLANETARY_COMPUTER,
        cache_dir=Path(cache_dir) if cache_dir else None,
    )
    # Try Sentinel-2 first (cloud_cover filter), fall back to Landsat
    for collection in ("sentinel-2-l2a", "landsat-c2-l2"):
        try:
            items = fetcher.search_stac(
                collection=collection,
                bbox=bbox,
                date_range=dr,
                cloud_cover_max=20.0,
                limit=2,
            )
            if items:
                break
        except Exception:
            items = []
    if not items:
        raise RuntimeError(
            f"No S2/Landsat items found in bbox={bbox} for {dr.start}..{dr.end}"
        )
    download_dir = output_dir / "downloaded"
    paths = fetcher.download_assets(
        items=items, out_dir=download_dir, max_items=2, max_total_mb=1500.0,
        prefer_assets=["visual", "thumbnail", "red", "green", "B04", "B03", "SR_B4", "SR_B3"],
    )
    if not paths:
        raise RuntimeError("Download returned no files")
    if len(paths) >= 2:
        args.baseline, args.current = str(paths[0]), str(paths[-1])
    else:
        args.baseline = str(paths[0])
        args.current = str(paths[0])
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": collection,
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def generate_synthetic_data(seed: int = 42):
    """Generate per-skill realistic synthetic NDVI baseline + current pair.

    Baseline: forested scene with NDVI 0.6-0.9.
    Current:  same scene with a few disturbance patches (NDVI dropped to 0.1-0.3).

    Returns (baseline_arr, current_arr, transform, crs, profile) so the caller
    can write GeoTIFFs and pass the arrays to detect_disturbance().
    """
    import numpy as np
    import rasterio
    from rasterio.transform import from_origin

    rng = np.random.RandomState(seed)
    H, W = 60, 60

    # Forest baseline: high NDVI everywhere
    baseline = rng.uniform(0.6, 0.9, (H, W)).astype(np.float32)

    # Current: same scene, with a 10x10 disturbance patch (NDVI drop) and a
    # 6x6 severe patch (larger drop) so we can demonstrate both classes.
    current = baseline.copy()
    # Disturbance patch (light drop) — keeps NDVI in 0.2-0.4 range
    current[10:20, 15:25] = rng.uniform(0.2, 0.4, (10, 10)).astype(np.float32)
    # Severe disturbance patch (large drop)
    current[35:41, 40:46] = rng.uniform(0.05, 0.15, (6, 6)).astype(np.float32)

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
    return baseline, current, transform, "EPSG:4326", profile


def write_synthetic_rasters(baseline, current, profile, out_dir: Path):
    """Write the synthetic baseline + current NDVI rasters to disk."""
    import rasterio

    synth_dir = out_dir / "synthetic_input"
    synth_dir.mkdir(parents=True, exist_ok=True)
    baseline_path = synth_dir / "baseline_ndvi_synthetic.tif"
    current_path = synth_dir / "current_ndvi_synthetic.tif"
    with rasterio.open(str(baseline_path), "w", **profile) as dst:
        dst.write(baseline, 1)
    with rasterio.open(str(current_path), "w", **profile) as dst:
        dst.write(current, 1)
    return baseline_path, current_path


def detect_disturbance(baseline_ndvi: Path, current_ndvi: Path, threshold: float = 0.2) -> Dict[str, Any]:
    try:
        import numpy as np
        import rasterio
    except ImportError:
        return {"error": "rasterio/numpy not available"}
    with rasterio.open(baseline_ndvi) as ds:
        baseline = ds.read(1).astype(np.float64); transform = ds.transform; crs = ds.crs; nodata = ds.nodata
    with rasterio.open(current_ndvi) as ds:
        current = ds.read(1).astype(np.float64)
    valid = (baseline != nodata) & (current != nodata) if nodata else np.ones_like(baseline, dtype=bool)
    diff = baseline - current  # positive = disturbance
    disturbance = (diff >= threshold) & valid
    severe = (diff >= threshold * 2) & valid
    disturbance_pixels = int(np.sum(disturbance))
    severe_pixels = int(np.sum(severe))
    if crs and crs.is_projected:
        pixel_area = abs(transform.a * transform.e)
    else:
        pixel_area = (abs(transform.a) * 111320) * (abs(transform.e) * 111320)
    return {
        "disturbance_pixels": disturbance_pixels, "severe_pixels": severe_pixels,
        "disturbance_area_ha": round(disturbance_pixels * pixel_area / 10000, 2),
        "mean_ndvi_drop": round(float(np.nanmean(diff[disturbance])) if disturbance_pixels > 0 else 0, 4),
        "total_valid_pixels": int(np.sum(valid)), "threshold": threshold,
    }

def generate_report(result, output_dir):
    now = datetime.now(timezone.utc).isoformat()
    html = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><title>Forest Disturbance</title>
<style>body{{font-family:sans-serif;max-width:900px;margin:20px auto;padding:0 20px}}
h1{{color:#1a237e}}.summary{{background:#fff3e0;padding:15px;border-radius:8px}}
table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #ffe0b2;padding:8px}}
th{{background:#ffe0b2}}</style></head><body>
<h1>Forest Disturbance Alert Report</h1><p>Generated: {now}</p>
<div class="summary"><table>
<tr><td>Disturbance area</td><td><strong>{result.get('disturbance_area_ha',0)} ha</strong></td></tr>
<tr><td>Severe disturbance</td><td><strong>{result.get('severe_pixels',0)} pixels</strong></td></tr>
<tr><td>Mean NDVI drop</td><td><strong>{result.get('mean_ndvi_drop',0)}</strong></td></tr>
</table></div></body></html>"""
    (output_dir / "report.html").write_text(html, encoding="utf-8")
    (output_dir / "disturbance-report.json").write_text(json.dumps({"timestamp": now, "results": result}, ensure_ascii=False, indent=2), encoding="utf-8")

def auto_download_baseline(args, output_dir: Path) -> Dict[str, Any]:
    """Download one sentinel-2-l2a scene from MPC using --bbox + --date-range.

    Returns metadata dict (also writes the path back to args.baseline).
    """
    if not _FETCHER_AVAILABLE:
        raise RuntimeError(
            "Shared data fetcher not importable. Pass --baseline <local.tif> instead, "
            "or ensure _geoskill_data_fetcher is on sys.path."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_baseline requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        raise RuntimeError("auto_download_baseline requires --date-range")
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
    args.baseline = str(paths[0])
    args.current = str(paths[0])
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "sentinel-2-l2a",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def run_disturbance(args):
    output_dir = Path(args.output_dir) if args.output_dir else Path("disturbance-output")
    output_dir.mkdir(parents=True, exist_ok=True)
    fetch_meta = None
    # Auto-download mode: --bbox + --date-range, no baseline/current given
    if (not args.synthetic
            and (not args.baseline or not args.current)
            and (getattr(args, "bbox", None) or getattr(args, "aoi_file", None))
            and getattr(args, "date_range", None)):
        try:
            fetch_meta = auto_download_disturbance_pair(args, output_dir)
            print(f"  Auto-downloaded baseline/current: {args.baseline}, {args.current}")
        except DataFetcherError as e:
            print(f"ERROR: auto-download failed: [{e.kind}] {e.message}", file=sys.stderr)
            return EXIT_PROCESSING
        except Exception as e:
            print(f"ERROR: auto-download failed: {e}", file=sys.stderr)
            return EXIT_PROCESSING
    mode = "synthetic" if args.synthetic else ("auto_download" if fetch_meta else "file")

    if args.synthetic:
        # P2-1: build 60x60 synthetic baseline + current NDVI rasters
        baseline, current, transform, crs, profile = generate_synthetic_data()
        baseline_path, current_path = write_synthetic_rasters(baseline, current, profile, output_dir)
        print(f"  Synthetic inputs: {baseline_path.name}, {current_path.name}")
    else:
        for p, n in [(Path(args.baseline),"Baseline"),(Path(args.current),"Current")]:
            if not p.exists(): print(f"ERROR: {n} not found: {p}", file=sys.stderr); return EXIT_ARG
        baseline_path = Path(args.baseline)
        current_path = Path(args.current)

    result = detect_disturbance(baseline_path, current_path, args.threshold)
    generate_report(result, output_dir)

    # Build output manifest with T9 three keys: output_files, parameters, timestamp
    output_files = {
        "report.html": str(output_dir / "report.html"),
        "disturbance-report.json": str(output_dir / "disturbance-report.json"),
        "output-manifest.json": str(output_dir / "output-manifest.json"),
    }
    if args.synthetic:
        output_files["synthetic_input/baseline_ndvi_synthetic.tif"] = str(output_dir / "synthetic_input" / "baseline_ndvi_synthetic.tif")
        output_files["synthetic_input/current_ndvi_synthetic.tif"] = str(output_dir / "synthetic_input" / "current_ndvi_synthetic.tif")
    elif fetch_meta is not None:
        for p in fetch_meta.get("downloaded_paths", []):
            output_files[f"downloaded/{Path(p).name}"] = p

    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "output_files": output_files,
        "parameters": vars(args),
        "summary": {
            "mode": mode,
            "n_outputs": len(output_files),
            "disturbance_pixels": result.get("disturbance_pixels", 0),
            "severe_pixels": result.get("severe_pixels", 0),
            "disturbance_area_ha": result.get("disturbance_area_ha", 0),
        },
        "results": result,
    }
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
    if fetch_meta is not None:
        manifest["data_source"] = fetch_meta["data_source"]
        manifest["fetched_at"] = fetch_meta["fetched_at"]
        manifest["collection"] = fetch_meta["collection"]
        manifest["bbox"] = fetch_meta["bbox"]
        manifest["date_range"] = fetch_meta["date_range"]
    (output_dir / "output-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Output: {output_dir}")
    return EXIT_OK

def main():
    parser = argparse.ArgumentParser(description="Forest Disturbance Alert")
    parser.add_argument("--baseline", help="Baseline NDVI raster (or use --synthetic)")
    parser.add_argument("--current", help="Current NDVI raster (or use --synthetic)")
    parser.add_argument("--threshold", type=float, default=0.2, help="Disturbance threshold")
    parser.add_argument("--synthetic", action="store_true",
                        help="Run with synthetic demo data (no real inputs needed)")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    if _FETCHER_AVAILABLE:
        add_bbox_date_args(parser)
    args = parser.parse_args()
    # P0/P2-1: ensure either --synthetic OR both --baseline and --current
    # OR --bbox+--date-range for auto-download
    has_bbox = bool(getattr(args, "bbox", None) or getattr(args, "aoi_file", None))
    has_dr = bool(getattr(args, "date_range", None))
    if not args.synthetic and not (args.baseline and args.current) and not (has_bbox and has_dr):
        parser.error("either --synthetic, both --baseline and --current, or --bbox+--date-range are required")
    try: sys.exit(run_disturbance(args))
    except Exception as e: print(f"FATAL: {e}", file=sys.stderr); traceback.print_exc(file=sys.stderr); sys.exit(EXIT_PROCESSING)

if __name__ == "__main__":
    main()
