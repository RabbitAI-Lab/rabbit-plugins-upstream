#!/usr/bin/env python3
"""
Mine Reclamation Monitor - Assess vegetation recovery at mining sites.

Compares pre-mining and post-reclamation vegetation indices to evaluate
recovery progress and generate reclamation reports.
"""

import argparse
import json
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

EXIT_OK = 0
EXIT_ARG = 2
EXIT_PROCESSING = 7


def compute_reclamation(pre_mining_path: Path, post_reclamation_path: Path,
                         reference_path: Path = None) -> Dict[str, Any]:
    """Compute reclamation progress from NDVI rasters."""
    try:
        import numpy as np
        import rasterio
    except ImportError:
        return {"error": "rasterio/numpy not available"}

    with rasterio.open(pre_mining_path) as ds:
        pre_mining = ds.read(1).astype(np.float64)
        transform = ds.transform
        crs = ds.crs
        nodata = ds.nodata
    with rasterio.open(post_reclamation_path) as ds:
        post_reclamation = ds.read(1).astype(np.float64)

    if nodata is not None:
        valid = (pre_mining != nodata) & (post_reclamation != nodata)
    else:
        valid = np.ones_like(pre_mining, dtype=bool)

    # Recovery ratio: post / pre (how much vegetation recovered)
    with np.errstate(divide='ignore', invalid='ignore'):
        recovery_ratio = np.where((pre_mining > 0.1) & valid,
                                   post_reclamation / pre_mining, np.nan)

    # If reference provided, compute recovery vs natural vegetation
    ref_mean = None
    if reference_path and Path(reference_path).exists():
        with rasterio.open(reference_path) as ds:
            ref_data = ds.read(1).astype(np.float64)
        ref_mean = float(np.nanmean(ref_data[ref_data != nodata]))

    pre_mean = float(np.nanmean(pre_mining[valid]))
    post_mean = float(np.nanmean(post_reclamation[valid]))
    recovery_mean = float(np.nanmean(recovery_ratio[~np.isnan(recovery_ratio)]))

    # Area calculation
    if crs and crs.is_projected:
        pixel_area = abs(transform.a * transform.e)
    else:
        pixel_area = (abs(transform.a) * 111320) * (abs(transform.e) * 111320)

    total_pixels = int(np.sum(valid))
    # Recovery classes
    full_recovery = int(np.sum((recovery_ratio >= 0.8) & valid))
    partial_recovery = int(np.sum((recovery_ratio >= 0.5) & (recovery_ratio < 0.8) & valid))
    poor_recovery = int(np.sum((recovery_ratio < 0.5) & valid))

    return {
        "pre_mining_ndvi_mean": round(pre_mean, 4),
        "post_reclamation_ndvi_mean": round(post_mean, 4),
        "recovery_ratio": round(recovery_mean, 4),
        "reference_ndvi_mean": ref_mean,
        "total_pixels": total_pixels,
        "total_area_ha": round(total_pixels * pixel_area / 10000, 2),
        "full_recovery_pixels": full_recovery,
        "partial_recovery_pixels": partial_recovery,
        "poor_recovery_pixels": poor_recovery,
        "full_recovery_pct": round(full_recovery / max(total_pixels, 1) * 100, 1),
    }


def generate_report(result: Dict, output_dir: Path) -> None:
    now = datetime.now(timezone.utc).isoformat()
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><title>Mine Reclamation Report</title>
<style>
body{{font-family:sans-serif;max-width:900px;margin:20px auto;padding:0 20px}}
h1{{color:#1a237e}}.summary{{background:#fff3e0;padding:15px;border-radius:8px}}
table{{border-collapse:collapse;width:100%}}
th,td{{border:1px solid #ffe0b2;padding:8px;text-align:left}}
th{{background:#ffe0b2}}
</style></head>
<body>
<h1>Mine Reclamation Monitor Report</h1>
<p>Generated: {now}</p>
<div class="summary">
<table>
<tr><td>Recovery ratio</td><td><strong>{result.get('recovery_ratio', 0):.2%}</strong></td></tr>
<tr><td>Pre-mining NDVI</td><td><strong>{result.get('pre_mining_ndvi_mean', 0):.3f}</strong></td></tr>
<tr><td>Post-reclamation NDVI</td><td><strong>{result.get('post_reclamation_ndvi_mean', 0):.3f}</strong></td></tr>
<tr><td>Full recovery</td><td><strong>{result.get('full_recovery_pct', 0)}%</strong></td></tr>
</table>
</div>
</body></html>"""
    (output_dir / "report.html").write_text(html, encoding="utf-8")
    (output_dir / "reclamation-report.json").write_text(
        json.dumps({"timestamp": now, "results": result}, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def run_reclamation(args: argparse.Namespace) -> int:
    for p, name in [(Path(args.pre_mining), "Pre-mining"), (Path(args.post_reclamation), "Post-reclamation")]:
        if not p.exists():
            print(f"ERROR: {name} raster not found: {p}", file=sys.stderr)
            return EXIT_ARG

    output_dir = Path(args.output_dir) if args.output_dir else Path("reclamation-output")
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Computing reclamation progress...")
    result = compute_reclamation(Path(args.pre_mining), Path(args.post_reclamation),
                                  args.reference)
    print(f"  Recovery ratio: {result.get('recovery_ratio', 0):.2%}")

    generate_report(result, output_dir)
    manifest = {"timestamp": datetime.now(timezone.utc).isoformat(), "results": result}
    (output_dir / "output-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Output: {output_dir}")
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Mine Reclamation Monitor")
    parser.add_argument("--pre-mining", required=True, help="Pre-mining NDVI raster")
    parser.add_argument("--post-reclamation", required=True, help="Post-reclamation NDVI raster")
    parser.add_argument("--reference", help="Reference (natural) NDVI raster")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")
    args = parser.parse_args()
    try:
        sys.exit(run_reclamation(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
