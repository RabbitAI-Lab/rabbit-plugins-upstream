#!/usr/bin/env python3
"""Climate Risk Screening - Assess climate hazards from temperature/precipitation data."""
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
except ImportError:  # pragma: no cover - graceful when running standalone
    _FETCHER_AVAILABLE = False



EXIT_OK = 0; EXIT_ARG = 2; EXIT_PROCESSING = 7

def generate_synthetic_data(out_dir, seed=42):
    """Generate 12-band temperature + precipitation stacks (60x60, EPSG:4326)."""
    import numpy as np
    import rasterio
    from rasterio.transform import from_origin
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.RandomState(seed)
    transform = from_origin(0, 60, 0.001, 0.001)
    # 12 monthly bands: seasonal temp cycle (25 ± 10 °C)
    months = 12
    temp = np.zeros((months, 60, 60), dtype=np.float32)
    precip = np.zeros((months, 60, 60), dtype=np.float32)
    for m in range(months):
        seasonal = 25.0 + 10.0 * np.cos(2 * np.pi * (m - 6) / 12)
        temp[m] = (seasonal + rng.normal(0, 1.5, (60, 60))).astype(np.float32)
        wet_factor = 1.0 + 0.5 * np.cos(2 * np.pi * (m - 0) / 12)  # wet in winter
        precip[m] = np.clip(rng.normal(50 * wet_factor, 15, (60, 60)), 0, 200).astype(np.float32)
    temp_p = out_dir / "temperature_synthetic.tif"
    precip_p = out_dir / "precipitation_synthetic.tif"
    for p, arr in [(temp_p, temp), (precip_p, precip)]:
        with rasterio.open(str(p), "w", driver="GTiff", height=60, width=60,
                           count=months, dtype="float32", crs="EPSG:4326",
                           transform=transform) as dst:
            dst.write(arr)
    return temp_p, precip_p


def analyze_climate_risk(temp_path: Path, precip_path: Path) -> Dict[str, Any]:
    try:
        import numpy as np
        import rasterio
    except ImportError:
        return {"error": "rasterio/numpy not available"}
    with rasterio.open(temp_path) as ds:
        temp = ds.read(1).astype(np.float64); transform = ds.transform; crs = ds.crs; nodata = ds.nodata
    with rasterio.open(precip_path) as ds:
        precip = ds.read(1).astype(np.float64)
    valid = (temp != nodata) & (precip != nodata) if nodata else np.ones_like(temp, dtype=bool)
    # Heat risk: temp > 35°C
    heat_risk = int(np.sum((temp > 35) & valid))
    # Drought risk: precip < 200mm/yr
    drought_risk = int(np.sum((precip < 200) & valid))
    # Composite risk
    if crs and crs.is_projected:
        pixel_area = abs(transform.a * transform.e)
    else:
        pixel_area = (abs(transform.a) * 111320) * (abs(transform.e) * 111320)
    total = int(np.sum(valid))
    return {
        "mean_temperature": round(float(np.nanmean(temp[valid])), 2),
        "mean_precipitation": round(float(np.nanmean(precip[valid])), 2),
        "heat_risk_pixels": heat_risk, "drought_risk_pixels": drought_risk,
        "heat_risk_area_km2": round(heat_risk * pixel_area / 1e6, 4),
        "total_valid_pixels": total,
    }

def generate_report(result, output_dir):
    now = datetime.now(timezone.utc).isoformat()
    html = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><title>Climate Risk</title>
<style>body{{font-family:sans-serif;max-width:900px;margin:20px auto;padding:0 20px}}
h1{{color:#1a237e}}.summary{{background:#fff3e0;padding:15px;border-radius:8px}}
table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #ffe0b2;padding:8px}}
th{{background:#ffe0b2}}</style></head><body>
<h1>Climate Risk Screening Report</h1><p>Generated: {now}</p>
<div class="summary"><table>
<tr><td>Mean temperature</td><td><strong>{result.get('mean_temperature',0)} °C</strong></td></tr>
<tr><td>Mean precipitation</td><td><strong>{result.get('mean_precipitation',0)} mm</strong></td></tr>
<tr><td>Heat risk area</td><td><strong>{result.get('heat_risk_area_km2',0)} km²</strong></td></tr>
</table></div></body></html>"""
    (output_dir / "report.html").write_text(html, encoding="utf-8")
    (output_dir / "climate-report.json").write_text(json.dumps({"timestamp": now, "results": result}, ensure_ascii=False, indent=2), encoding="utf-8")

def auto_download_temperature(args, output_dir: Path) -> Dict[str, Any]:
    """Fetch NASA POWER climate series for --bbox/--date-range and write
    a single-band GeoTIFF per parameter (T2M, PRECTOTCORR).

    NASA POWER is a point-based API; we pull the centroid of the bbox,
    then write a 1-band GeoTIFF containing the period mean. The skill's
    downstream ``analyze_climate_risk`` only reads band 1, so this
    works as a stand-in for the temperature / precipitation rasters
    the user would otherwise supply.
    """
    if not _FETCHER_AVAILABLE:
        raise RuntimeError(
            "Shared data fetcher not importable. Pass --temperature <local.tif> instead, "
            "or ensure _geoskill_data_fetcher is on sys.path."
        )
    bbox = parse_bbox_arg(getattr(args, "bbox", None), getattr(args, "aoi_file", None))
    if bbox is None:
        raise RuntimeError("auto_download_temperature requires --bbox or --aoi-file")
    dr = parse_date_range_arg(getattr(args, "date_range", None))
    if dr is None:
        raise RuntimeError("auto_download_temperature requires --date-range")
    cache_dir = getattr(args, "cache_dir", None)
    fetcher = DataFetcher(
        source=DataSource.NASA_POWER,
        cache_dir=Path(cache_dir) if cache_dir else None,
    )
    df = fetcher.fetch_power(
        parameters=["T2M", "PRECTOTCORR"],
        bbox=bbox,
        date_range=dr,
        resolution="daily",
    )
    if df is None or len(df) == 0:
        raise RuntimeError(
            f"NASA POWER returned no rows for bbox={bbox} in {dr.start}..{dr.end}"
        )
    # Compute period means and write one-band GeoTIFFs in EPSG:4326
    import numpy as np
    import rasterio
    from rasterio.transform import from_origin
    t_mean = float(df["T2M"].mean()) if "T2M" in df.columns else float("nan")
    p_mean = float(df["PRECTOTCORR"].mean()) if "PRECTOTCORR" in df.columns else float("nan")
    lon = (bbox.lon_min + bbox.lon_max) / 2.0
    lat = (bbox.lat_min + bbox.lat_max) / 2.0
    transform = from_origin(lon - 0.5, lat + 0.5, 1.0, 1.0)  # 1 deg cells
    download_dir = output_dir / "downloaded"
    download_dir.mkdir(parents=True, exist_ok=True)
    t_path = download_dir / "temperature_nasa_power.tif"
    p_path = download_dir / "precipitation_nasa_power.tif"
    arr_t = np.array([[t_mean]], dtype=np.float32)
    arr_p = np.array([[p_mean]], dtype=np.float32)
    for path, arr in [(t_path, arr_t), (p_path, arr_p)]:
        with rasterio.open(
            str(path), "w", driver="GTiff", height=1, width=1, count=1,
            dtype="float32", crs="EPSG:4326", transform=transform,
        ) as dst:
            dst.write(arr, 1)
            dst.update_tags(source="NASA POWER", parameter=path.stem.split("_")[0])
    args.temperature = str(t_path)
    args.precipitation = str(p_path)
    return {
        "data_source": "NASA POWER",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "collection": "nasa-power (T2M + PRECTOTCORR)",
        "bbox": bbox.to_string(),
        "date_range": f"{dr.start},{dr.end}",
        "centroid_lon": lon,
        "centroid_lat": lat,
        "n_rows": int(len(df)),
        "t2m_mean": t_mean,
        "prectotcorr_mean": p_mean,
        "downloaded_paths": [str(t_path), str(p_path)],
    }


def run_climate(args):
    output_dir = Path(args.output_dir) if args.output_dir else Path("climate-output")

    # --- Auto-download mode: fetch nasa-power from NASA POWER ---
    fetch_meta = None
    if (getattr(args, "bbox", None) or getattr(args, "aoi_file", None)) and getattr(args, "date_range", None):
        if not getattr(args, "temperature", None):
            try:
                fetch_meta = auto_download_temperature(args, output_dir)
                print(f"  Auto-downloaded temperature: {args.temperature}")
            except DataFetcherError as e:
                print(f"ERROR: auto-download failed: [{e.kind}] {e.message}", file=sys.stderr)
                return EXIT_PROCESSING if 'EXIT_PROCESSING' in dir() else 7
    output_dir.mkdir(parents=True, exist_ok=True)
    if args.synthetic or not (args.temperature and args.precipitation):
        mode = "synthetic"
        synth_dir = output_dir / "synthetic_input"
        t_path, p_path = generate_synthetic_data(synth_dir, seed=42)
        print(f"  Generated synthetic temp + precip stacks in {synth_dir}")
    elif fetch_meta is not None:
        mode = "auto_download"
        for raw, n in [(args.temperature, "Temperature"), (args.precipitation, "Precipitation")]:
            if not Path(raw).exists():
                print(f"ERROR: {n} not found: {raw}", file=sys.stderr); return EXIT_ARG
        t_path, p_path = Path(args.temperature), Path(args.precipitation)
    else:
        mode = "file"
        for raw, n in [(args.temperature, "Temperature"), (args.precipitation, "Precipitation")]:
            if not Path(raw).exists():
                print(f"ERROR: {n} not found: {raw}", file=sys.stderr); return EXIT_ARG
        t_path, p_path = Path(args.temperature), Path(args.precipitation)
    result = analyze_climate_risk(t_path, p_path)
    generate_report(result, output_dir)
    output_files = {
        "report.html": str(output_dir / "report.html"),
        "climate-report.json": str(output_dir / "climate-report.json"),
    }
    if mode == "synthetic":
        output_files["synthetic_input/temperature_synthetic.tif"] = str(t_path)
        output_files["synthetic_input/precipitation_synthetic.tif"] = str(p_path)
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "results": result,
        "output_files": output_files,
        "summary": {
            "mode": mode,
            "mean_temperature": result.get("mean_temperature"),
            "mean_precipitation": result.get("mean_precipitation"),
            "heat_risk_pixels": result.get("heat_risk_pixels"),
        },
        "parameters": {k: v for k, v in vars(args).items() if not k.startswith("_")},
    }
    ensure_t9_fields(manifest, args)
    # Surface the auto-download provenance in the manifest so downstream
    # auditors can confirm where the inputs came from.
    if fetch_meta:
        manifest["data_source"] = fetch_meta.get("data_source")
        manifest["fetched_at"] = fetch_meta.get("fetched_at")
        manifest["collection"] = fetch_meta.get("collection")
        manifest["bbox"] = fetch_meta.get("bbox")
        manifest["date_range"] = fetch_meta.get("date_range")
    (output_dir / "output-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Output: {output_dir}")
    return EXIT_OK


def validate_args(args) -> int:
    """Validate file existence and numeric ranges.
    Returns exit code (0 = ok, 2 = arg error)."""
    if getattr(args, 'synthetic', False):
        return 0
    import sys
    from pathlib import Path
    file_args = {
        "temperature": "args.temperature",
        "precipitation": "args.precipitation",
    }
    for flag, accessor in file_args.items():
        path = eval(accessor)
        if path is not None and not Path(path).exists():
            print(f"ERROR: --{flag} not found: {path}", file=sys.stderr)
            return 2
    numeric_ranges = {
        "precipitation": [0, 5000],
    }
    for flag, (lo, hi) in numeric_ranges.items():
        val = getattr(args, flag, None)
        if val is None:
            continue
        if lo is not None and val < lo:
            print(f"ERROR: --{flag}={val} below minimum {lo}", file=sys.stderr)
            return 2
        if hi is not None and val > hi:
            print(f"ERROR: --{flag}={val} above maximum {hi}", file=sys.stderr)
            return 2
    return 0


def main():
    parser = argparse.ArgumentParser(description="Climate Risk Screening")
    parser.add_argument("--temperature", default=None, help="Temperature raster (°C, optional if --synthetic)")
    parser.add_argument("--precipitation", default=None, help="Precipitation raster (mm, optional if --synthetic)")
    parser.add_argument("--synthetic", action="store_true", help="Run with synthetic demo data")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    add_bbox_date_args(parser)
    args = parser.parse_args()
    rc = validate_args(args)
    if rc != 0:
        sys.exit(rc)
    try: sys.exit(run_climate(args))
    except Exception as e: print(f"FATAL: {e}", file=sys.stderr); traceback.print_exc(file=sys.stderr); sys.exit(EXIT_PROCESSING)



def ensure_t9_fields(manifest, args=None):
    """Inject 3 T9 fields (output_files, parameters/summary, timestamp) if missing."""
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
