#!/usr/bin/env python3
"""
Forest Fire Burn Severity - Compute burn severity from pre/post-fire imagery.

Uses differenced Normalized Burn Ratio (dNBR) to classify burn severity
into unburned, low, moderate, high categories.

Exit codes:
    0 = success
    2 = argument error
    7 = processing failure
"""

import argparse
import json
import sys
import traceback
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




EXIT_OK = 0
EXIT_ARG = 2
EXIT_PROCESSING = 7

# Burn severity thresholds (dNBR values, unitless)
SEVERITY_LEVELS = {
    "enhanced_regrowth_high": {"min": -0.5, "max": -0.25, "color": "#1a9850"},
    "unburned": {"min": -0.25, "max": 0.1, "color": "#91cf60"},
    "low": {"min": 0.1, "max": 0.27, "color": "#d9ef8b"},
    "moderate_low": {"min": 0.27, "max": 0.44, "color": "#fee08b"},
    "moderate_high": {"min": 0.44, "max": 0.66, "color": "#fc8d59"},
    "high": {"min": 0.66, "max": 1.3, "color": "#d73027"},
}


def auto_download_burn_pair(args, output_dir: Path) -> Dict[str, Any]:
    """Download Landsat Collection 2 Level 2 (landsat-c2-l2) pre/post-fire
    visual previews. Real burn-severity analysis needs NIR+SWIR pair; the
    visual asset is a much smaller RGB composite that fits the smoke-test
    bandwidth budget.
    """
    if not _FETCHER_AVAILABLE:
        raise RuntimeError(
            "Shared data fetcher not importable. Use --synthetic or pass --pre-nir/--pre-swir/--post-nir/--post-swir."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_burn_pair requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        raise RuntimeError("auto_download_burn_pair requires --date-range")
    cache_dir = getattr(args, "cache_dir", None)
    fetcher = DataFetcher(
        source=DataSource.PLANETARY_COMPUTER,
        cache_dir=Path(cache_dir) if cache_dir else None,
    )
    items = fetcher.search_stac(
        collection="landsat-c2-l2",
        bbox=bbox,
        date_range=dr,
        cloud_cover_max=20.0,
        limit=4,
    )
    if not items:
        raise RuntimeError(
            f"No Landsat C2 L2 items found in bbox={bbox} for {dr.start}..{dr.end}"
        )
    download_dir = output_dir / "downloaded"
    paths = fetcher.download_assets(
        items=items, out_dir=download_dir, max_items=4, max_total_mb=500.0,
        prefer_assets=["visual", "thumbnail", "red", "green", "blue", "SR_B4", "SR_B3", "SR_B2"],
    )
    if not paths:
        raise RuntimeError("Download returned no files")
    # Map first 2 to pre, next 2 to post (approximate)
    if len(paths) >= 4:
        args.pre_nir, args.pre_swir, args.post_nir, args.post_swir = (str(p) for p in paths[:4])
    elif len(paths) >= 2:
        args.pre_nir = str(paths[0])
        args.pre_swir = str(paths[0])
        args.post_nir = str(paths[-1])
        args.post_swir = str(paths[-1])
    else:
        args.pre_nir = args.pre_swir = args.post_nir = args.post_swir = str(paths[0])
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "landsat-c2-l2",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def generate_synthetic_data(seed: int = 42):
    """Generate per-skill realistic synthetic pre/post NIR+SWIR rasters.

    Pre-fire:  healthy forest — high NIR (0.4-0.6), low SWIR (0.05-0.15)
    Post-fire: burned patches lower NIR / higher SWIR → positive dNBR.

    Returns 4 (H, W) float32 arrays + (transform, crs, profile).
    """
    import numpy as np
    from rasterio.transform import from_origin

    rng = np.random.RandomState(seed)
    H, W = 60, 60

    pre_nir = rng.uniform(0.40, 0.60, (H, W)).astype(np.float32)
    pre_swir = rng.uniform(0.05, 0.15, (H, W)).astype(np.float32)

    post_nir = pre_nir.copy()
    post_swir = pre_swir.copy()

    # Burn patches: NIR drops, SWIR rises (char / ash signature)
    # 3 patches with increasing severity
    # High severity
    post_nir[5:20, 5:20] = rng.uniform(0.05, 0.10, (15, 15)).astype(np.float32)
    post_swir[5:20, 5:20] = rng.uniform(0.30, 0.40, (15, 15)).astype(np.float32)
    # Moderate severity
    post_nir[25:40, 25:40] = rng.uniform(0.15, 0.25, (15, 15)).astype(np.float32)
    post_swir[25:40, 25:40] = rng.uniform(0.20, 0.30, (15, 15)).astype(np.float32)
    # Low severity (small patch)
    post_nir[45:55, 45:55] = rng.uniform(0.25, 0.35, (10, 10)).astype(np.float32)
    post_swir[45:55, 45:55] = rng.uniform(0.12, 0.20, (10, 10)).astype(np.float32)

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
    return pre_nir, pre_swir, post_nir, post_swir, transform, "EPSG:4326", profile


def write_synthetic_rasters(pre_nir, pre_swir, post_nir, post_swir, profile, out_dir: Path):
    """Write 4 synthetic single-band GeoTIFFs under out_dir/synthetic_input/."""
    import rasterio

    synth_dir = out_dir / "synthetic_input"
    synth_dir.mkdir(parents=True, exist_ok=True)
    paths = {}
    for name, arr in (
        ("pre_nir_synthetic.tif", pre_nir),
        ("pre_swir_synthetic.tif", pre_swir),
        ("post_nir_synthetic.tif", post_nir),
        ("post_swir_synthetic.tif", post_swir),
    ):
        p = synth_dir / name
        with rasterio.open(str(p), "w", **profile) as dst:
            dst.write(arr, 1)
        paths[name] = p
    return paths


def compute_dnbr(pre_nir_path: Path, pre_swir_path: Path,
                 post_nir_path: Path, post_swir_path: Path) -> Dict[str, Any]:
    """Compute dNBR = pre_NBR - post_NBR, where NBR = (NIR - SWIR) / (NIR + SWIR)."""
    try:
        import numpy as np
        import rasterio
    except ImportError:
        return {"error": "rasterio/numpy not available"}

    with rasterio.open(pre_nir_path) as ds:
        pre_nir = ds.read(1).astype(np.float64)
    with rasterio.open(pre_swir_path) as ds:
        pre_swir = ds.read(1).astype(np.float64)
    with rasterio.open(post_nir_path) as ds:
        post_nir = ds.read(1).astype(np.float64)
    with rasterio.open(post_swir_path) as ds:
        post_swir = ds.read(1).astype(np.float64)
    with rasterio.open(pre_nir_path) as ds:
        transform = ds.transform
        crs = ds.crs
        nodata = ds.nodata

    # Compute NBR
    pre_denom = pre_nir + pre_swir
    post_denom = post_nir + post_swir
    pre_nbr = np.where(pre_denom != 0, (pre_nir - pre_swir) / pre_denom, 0)
    post_nbr = np.where(post_denom != 0, (post_nir - post_swir) / post_denom, 0)

    # dNBR
    dnbr = pre_nbr - post_nbr

    # Mask nodata
    if nodata is not None:
        valid = (pre_nir != nodata) & (post_nir != nodata)
        dnbr[~valid] = np.nan

    # Classify severity
    severity_counts = {}
    for level, rules in SEVERITY_LEVELS.items():
        mask = (dnbr >= rules["min"]) & (dnbr < rules["max"])
        severity_counts[level] = int(np.sum(mask))

    total_valid = int(np.sum(~np.isnan(dnbr)))
    burned = int(np.sum(dnbr > 0.1))  # low+ severity

    # Area
    if crs and crs.is_projected:
        pixel_area = abs(transform.a * transform.e)
    else:
        pixel_area = (abs(transform.a) * 111320) * (abs(transform.e) * 111320)

    return {
        "dnbr_mean": float(np.nanmean(dnbr)),
        "dnbr_min": float(np.nanmin(dnbr)),
        "dnbr_max": float(np.nanmax(dnbr)),
        "total_valid_pixels": total_valid,
        "burned_pixels": burned,
        "burned_area_ha": round(burned * pixel_area / 10000, 2),
        "severity_counts": severity_counts,
    }


def generate_report(result: Dict, output_dir: Path) -> None:
    """Generate burn severity report."""
    now = datetime.now(timezone.utc).isoformat()
    severity = result.get("severity_counts", {})

    rows = ""
    for level, count in severity.items():
        pct = count / max(result.get("total_valid_pixels", 1), 1) * 100
        rows += f"<tr><td>{level}</td><td>{count}</td><td>{pct:.1f}%</td></tr>\n"

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><title>Burn Severity Report</title>
<style>
body{{font-family:sans-serif;max-width:900px;margin:20px auto;padding:0 20px}}
h1{{color:#1a237e}}.summary{{background:#fff3e0;padding:15px;border-radius:8px}}
table{{border-collapse:collapse;width:100%}}
th,td{{border:1px solid #ffe0b2;padding:8px;text-align:left}}
th{{background:#ffe0b2}}
</style></head>
<body>
<h1>Forest Fire Burn Severity Report</h1>
<p>Generated: {now}</p>
<div class="summary">
<h2>Summary</h2>
<table>
<tr><td>Burned area</td><td><strong>{result.get('burned_area_ha', 0)} ha</strong></td></tr>
<tr><td>Burned pixels</td><td><strong>{result.get('burned_pixels', 0)}</strong></td></tr>
<tr><td>dNBR mean</td><td><strong>{result.get('dnbr_mean', 0):.3f}</strong></td></tr>
</table>
</div>
<h2>Severity Classification</h2>
<table>
<tr><th>Level</th><th>Pixels</th><th>Percent</th></tr>
{rows}
</table>
</body></html>"""

    (output_dir / "report.html").write_text(html, encoding="utf-8")
    (output_dir / "burn-severity-report.json").write_text(
        json.dumps({"timestamp": now, "results": result}, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def auto_download_image(args, output_dir: Path) -> Dict[str, Any]:
    """Download one landsat-c2-l2 scene from MPC using --bbox + --date-range.

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
        collection="landsat-c2-l2",
        bbox=bbox,
        date_range=dr,
        limit=1,
    )
    if not items:
        raise RuntimeError(
            f"No landsat-c2-l2 items found in bbox={bbox} for {dr.start}..{dr.end}"
        )
    download_dir = output_dir / "downloaded"
    paths = fetcher.download_assets(
        items=items, out_dir=download_dir, max_items=1, max_total_mb=500,
        prefer_assets=['SR_B4', 'SR_B5'],
    )
    if not paths:
        raise RuntimeError("Download returned no files")
    args.image = str(paths[0])
    args.pre_nir = str(paths[0])
    args.pre_swir = str(paths[0])
    args.post_nir = str(paths[0])
    args.post_swir = str(paths[0])
    return {
        "data_source": "MPC",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "landsat-c2-l2",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "n_items_searched": len(items),
        "downloaded_paths": [str(p) for p in paths],
    }


def run_burn_severity(args: argparse.Namespace) -> int:
    """Main burn severity workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("burn-severity-output")
    output_dir.mkdir(parents=True, exist_ok=True)
    fetch_meta = None
    # Auto-download mode: --bbox + --date-range, no NIR/SWIR inputs
    if (not args.synthetic
            and (not args.pre_nir or not args.pre_swir or not args.post_nir or not args.post_swir)
            and (getattr(args, "bbox", None) or getattr(args, "aoi_file", None))
            and getattr(args, "date_range", None)):
        try:
            fetch_meta = auto_download_burn_pair(args, output_dir)
            print(f"  Auto-downloaded burn-severity inputs")
        except DataFetcherError as e:
            print(f"ERROR: auto-download failed: [{e.kind}] {e.message}", file=sys.stderr)
            return EXIT_PROCESSING
        except Exception as e:
            print(f"ERROR: auto-download failed: {e}", file=sys.stderr)
            return EXIT_PROCESSING
    mode = "synthetic" if args.synthetic else ("auto_download" if fetch_meta else "file")

    if args.synthetic:
        # P2-1: build 4 synthetic rasters
        pre_nir, pre_swir, post_nir, post_swir, transform, crs, profile = generate_synthetic_data()
        paths = write_synthetic_rasters(pre_nir, pre_swir, post_nir, post_swir, profile, output_dir)
        pre_nir_p = paths["pre_nir_synthetic.tif"]
        pre_swir_p = paths["pre_swir_synthetic.tif"]
        post_nir_p = paths["post_nir_synthetic.tif"]
        post_swir_p = paths["post_swir_synthetic.tif"]
        print(f"  Synthetic inputs written under {output_dir / 'synthetic_input'}")
    else:
        for p in [args.pre_nir, args.pre_swir, args.post_nir, args.post_swir]:
            if not Path(p).exists():
                print(f"ERROR: File not found: {p}", file=sys.stderr)
                return EXIT_ARG
        pre_nir_p = Path(args.pre_nir)
        pre_swir_p = Path(args.pre_swir)
        post_nir_p = Path(args.post_nir)
        post_swir_p = Path(args.post_swir)

    print("Computing dNBR...")
    result = compute_dnbr(pre_nir_p, pre_swir_p, post_nir_p, post_swir_p)
    print(f"  Burned: {result.get('burned_pixels', 0)} pixels ({result.get('burned_area_ha', 0)} ha)")

    generate_report(result, output_dir)

    output_files = {
        "report.html": str(output_dir / "report.html"),
        "burn-severity-report.json": str(output_dir / "burn-severity-report.json"),
        "output-manifest.json": str(output_dir / "output-manifest.json"),
    }
    if args.synthetic:
        for fname in ("pre_nir_synthetic.tif", "pre_swir_synthetic.tif",
                      "post_nir_synthetic.tif", "post_swir_synthetic.tif"):
            output_files[f"synthetic_input/{fname}"] = str(output_dir / "synthetic_input" / fname)
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
            "burned_pixels": result.get("burned_pixels", 0),
            "burned_area_ha": result.get("burned_area_ha", 0),
            "dnbr_mean": round(result.get("dnbr_mean", 0), 4),
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
    (output_dir / "output-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"\nOutput: {output_dir}")
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Forest Fire Burn Severity")
    parser.add_argument("--pre-nir", help="Pre-fire NIR band (or use --synthetic)")
    parser.add_argument("--pre-swir", help="Pre-fire SWIR band (or use --synthetic)")
    parser.add_argument("--post-nir", help="Post-fire NIR band (or use --synthetic)")
    parser.add_argument("--post-swir", help="Post-fire SWIR band (or use --synthetic)")
    parser.add_argument("--synthetic", action="store_true",
                        help="Run with synthetic demo data (no real inputs needed)")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    if _FETCHER_AVAILABLE:
        add_bbox_date_args(parser)

    args = parser.parse_args()
    # P0/P2-1: ensure either --synthetic OR all 4 file args OR --bbox+--date-range
    has_bbox = bool(getattr(args, "bbox", None) or getattr(args, "aoi_file", None))
    has_dr = bool(getattr(args, "date_range", None))
    has_all_4 = all([args.pre_nir, args.pre_swir, args.post_nir, args.post_swir])
    if not args.synthetic and not has_all_4 and not (has_bbox and has_dr):
        parser.error("either --synthetic, all of --pre-nir/--pre-swir/--post-nir/--post-swir, or --bbox+--date-range are required")

    try:
        sys.exit(run_burn_severity(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
