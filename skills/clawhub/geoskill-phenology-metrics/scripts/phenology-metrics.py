#!/usr/bin/env python3
"""
phenology-metrics: Extract phenological metrics from NDVI/EVI time series.

Privacy Disclosure:
  - This tool performs LOCAL processing only.
  - NO data is sent to any external server.
  - All input files remain on your machine.

License: MIT-0 (Public Domain)
Data Source: Local processing of NDVI/EVI time series
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
    import pandas as pd
except ImportError:
    print("ERROR: pandas is required. Install with: pip install pandas>=1.3.0")
    sys.exit(1)

try:
    from scipy.optimize import curve_fit
    from scipy.signal import savgol_filter
except ImportError:
    print("ERROR: scipy is required. Install with: pip install scipy>=1.7.0")
    sys.exit(1)


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


# ─── Constants ───────────────────────────────────────────────────────────────

VALID_METHODS = ["threshold", "derivative", "logistic"]

# Presets (v0.2.0)
PRESETS = {
    "phenology-ndvi": {
        "method": "logistic",
        "value_col": "ndvi",
        "date_col": "date",
        "description": "NDVI 时序物候（双 Logistic 拟合，推荐）",
    },
    "phenology-evi": {
        "method": "logistic",
        "value_col": "evi",
        "date_col": "date",
        "description": "EVI 时序物候（双 Logistic 拟合）",
    },
    "phenology-threshold": {
        "method": "threshold",
        "value_col": "ndvi",
        "date_col": "date",
        "description": "NDVI 阈值法物候（SOS/EOS/LOS）",
    },
    "phenology-fast": {
        "method": "derivative",
        "value_col": "ndvi",
        "date_col": "date",
        "description": "导数法物候（最快但对噪声敏感）",
    },
}


# ─── Double logistic function ────────────────────────────────────────────────

def double_logistic(x, a, b, c, d, e, f):
    """
    Double logistic function for phenology fitting.

    f(x) = a + (b - a) / (1 + exp(-c * (x - d))) + (e - b) / (1 + exp(-f * (x - d)))

    Parameters:
        a: minimum value (baseline)
        b: maximum value (peak)
        c: green-up rate
        d: green-up midpoint (SOS)
        e: end-season value
        f: senescence rate
    """
    return a + (b - a) / (1 + np.exp(-c * (x - d))) - (b - e) / (1 + np.exp(-f * (x - d)))


def double_logistic_simple(x, a, b, c, d, e, f):
    """Simpler double logistic formulation."""
    return a + b / (1 + np.exp(-c * (x - d))) - e / (1 + np.exp(-f * (x - d)))


# ─── Phenology extraction methods ────────────────────────────────────────────

def extract_threshold(dates, values, ratio=0.5):
    """
    Extract phenology using threshold method.

    SOS and EOS are the dates where the curve crosses `ratio` of the amplitude.
    """
    vmin = np.nanmin(values)
    vmax = np.nanmax(values)
    amplitude = vmax - vmin
    threshold_val = vmin + ratio * amplitude

    # Find SOS: first crossing above threshold (ascending)
    sos = None
    for i in range(1, len(values)):
        if values[i - 1] < threshold_val <= values[i]:
            # Linear interpolation
            frac = (threshold_val - values[i - 1]) / (values[i] - values[i - 1])
            sos = dates[i - 1] + frac * (dates[i] - dates[i - 1])
            break

    # Find EOS: last crossing below threshold (descending)
    eos = None
    for i in range(len(values) - 2, -1, -1):
        if values[i] >= threshold_val > values[i + 1]:
            frac = (threshold_val - values[i]) / (values[i + 1] - values[i])
            eos = dates[i] + frac * (dates[i + 1] - dates[i])
            break

    return {
        "sos": float(sos) if sos is not None else None,
        "eos": float(eos) if eos is not None else None,
        "los": float(eos - sos) if (sos is not None and eos is not None) else None,
        "threshold_value": float(threshold_val),
        "threshold_ratio": ratio,
    }


def extract_derivative(dates, values, window=5, polyorder=2):
    """
    Extract phenology using derivative method.

    SOS: maximum of first derivative (steepest green-up)
    EOS: minimum of first derivative (steepest senescence)
    """
    # Smooth the curve
    if len(values) < window:
        window = len(values) if len(values) % 2 == 1 else len(values) - 1
    if window < 3:
        window = 3

    try:
        smoothed = savgol_filter(values, window, polyorder)
    except Exception:
        smoothed = values

    # Compute first derivative
    dx = np.diff(dates)
    dy = np.diff(smoothed)
    deriv = dy / dx

    # SOS: max derivative (steepest ascent)
    sos_idx = np.argmax(deriv)
    sos = dates[sos_idx]

    # EOS: min derivative (steepest descent)
    eos_idx = np.argmin(deriv)
    eos = dates[eos_idx]

    return {
        "sos": float(sos),
        "eos": float(eos),
        "los": float(eos - sos) if eos > sos else None,
        "sos_greenup_rate": float(deriv[sos_idx]),
        "eos_senescence_rate": float(deriv[eos_idx]),
    }


def fit_logistic(dates, values):
    """
    Fit double logistic function and extract phenology metrics.
    """
    # Normalize x to start from 0
    x = np.array(dates, dtype=np.float64)
    x_norm = x - x[0]
    y = np.array(values, dtype=np.float64)

    # Initial parameter guesses
    y_min = np.nanmin(y)
    y_max = np.nanmax(y)
    peak_idx = np.nanargmax(y)

    p0 = [
        y_min,        # a: baseline
        y_max,        # b: peak
        0.1,          # c: green-up rate
        x_norm[peak_idx],  # d: green-up midpoint
        y_min,        # e: end value
        0.1,          # f: senescence rate
    ]

    bounds = (
        [0, 0, 0.001, 0, 0, 0.001],
        [1, 1, 10, x_norm[-1] * 2, 1, 10],
    )

    try:
        popt, pcov = curve_fit(
            double_logistic, x_norm, y, p0=p0, bounds=bounds, maxfev=10000
        )
        a, b, c, d, e, f = popt

        # Compute fitted values
        y_fitted = double_logistic(x_norm, *popt)

        # R²
        ss_res = np.sum((y - y_fitted) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0

        # SOS: inflection point of green-up (where second derivative = 0)
        # For logistic: inflection at x = d
        sos = d + x[0]

        # EOS: inflection point of senescence
        # Approximate: where curve drops to same level as SOS
        eos = d + x[0] + (x_norm[-1] - d) * 0.5  # Simplified

        # Peak
        peak_val = b
        peak_date = d + x[0]

        return {
            "sos": float(sos),
            "eos": float(eos),
            "los": float(eos - sos),
            "peak_value": float(peak_val),
            "peak_date": float(peak_date),
            "amplitude": float(b - a),
            "baseline": float(a),
            "greenup_rate": float(c),
            "senescence_rate": float(f),
            "r_squared": float(r_squared),
            "fitted_params": popt.tolist(),
            "fitted_values": y_fitted.tolist(),
        }

    except Exception as e:
        print(f"WARNING: Logistic fitting failed: {e}")
        return {
            "error": str(e),
            "sos": None,
            "eos": None,
            "los": None,
        }


# ─── Core processing ─────────────────────────────────────────────────────────

def load_timeseries(input_path: str, date_col: str, value_col: str) -> pd.DataFrame:
    """Load time series from CSV."""
    df = pd.read_csv(input_path)

    if date_col not in df.columns:
        raise ValueError(f"Date column '{date_col}' not found. Available: {list(df.columns)}")
    if value_col not in df.columns:
        raise ValueError(f"Value column '{value_col}' not found. Available: {list(df.columns)}")

    # Parse dates
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.sort_values(date_col).reset_index(drop=True)

    # Remove NaN
    df = df.dropna(subset=[value_col])

    if len(df) < 5:
        raise ValueError(f"Insufficient data points ({len(df)}). Need at least 5.")

    return df


def compute_integral(dates, values):
    """Compute integral (area under curve) using trapezoidal rule."""
    x = np.array(dates, dtype=np.float64)
    y = np.array(values, dtype=np.float64)
    # Normalize x to numeric
    x_numeric = (x - x[0])
    trapz_fn = getattr(np, "trapezoid", None) or getattr(np, "trapz", None)
    if trapz_fn is None:
        # Fallback: manual trapezoid
        return float(np.sum((y[1:] + y[:-1]) * np.diff(x_numeric) / 2.0))
    return float(trapz_fn(y, x_numeric))


def extract_phenology(df: pd.DataFrame, date_col: str, value_col: str,
                      method: str, threshold_ratio: float = 0.5) -> dict:
    """Extract phenology metrics using specified method."""

    dates = df[date_col].values
    values = df[value_col].values.astype(np.float64)

    # Convert dates to numeric (days since start)
    dates_numeric = (df[date_col] - df[date_col].iloc[0]).dt.total_seconds().values / 86400.0

    # Basic statistics
    peak_idx = np.nanargmax(values)
    peak_val = float(values[peak_idx])
    peak_date = dates[peak_idx]
    vmin = float(np.nanmin(values))
    vmax = float(np.nanmax(values))
    amplitude = vmax - vmin

    integral = compute_integral(dates_numeric, values)

    result = {
        "method": method,
        "n_observations": len(values),
        "date_range": [str(dates[0]), str(dates[-1])],
        "peak_value": peak_val,
        "peak_date": str(peak_date),
        "min_value": vmin,
        "max_value": vmax,
        "amplitude": amplitude,
        "integral": integral,
    }

    if method == "threshold":
        thresh_result = extract_threshold(dates_numeric, values, threshold_ratio)
        result.update(thresh_result)
    elif method == "derivative":
        deriv_result = extract_derivative(dates_numeric, values)
        result.update(deriv_result)
    elif method == "logistic":
        log_result = fit_logistic(dates_numeric, values)
        result.update(log_result)
    else:
        raise ValueError(f"Unknown method '{method}'. Choose from: {', '.join(VALID_METHODS)}")

    return result


# ─── Commands ────────────────────────────────────────────────────────────────

def cmd_extract(args):
    """Handle extract subcommand."""
    # Apply preset
    if getattr(args, "preset", None):
        ps = PRESETS[args.preset]
        print(f"[preset] {args.preset}: {ps['description']}")
        if args.method == "threshold" and ps["method"]:
            args.method = ps["method"]
        if args.value_col == "ndvi" and ps["value_col"]:
            args.value_col = ps["value_col"]
        if args.date_col == "date" and ps["date_col"]:
            args.date_col = ps["date_col"]

    if args.place:
        # Optional: just print the resolved place for context (we don't auto-fetch)
        try:
            info = _resolve_place(args.place)
            print(f"[place] {args.place} -> {info.resolved_name} (centroid={info.centroid}, bbox={info.bbox})")
            # Stash on args for the QA summary
            args.place_info = info.to_dict()
        except ValueError as e:
            print(f"WARN: {e}")
            args.place_info = None

    if not os.path.isfile(args.input):
        print(f"ERROR: Input file not found: {args.input}")
        sys.exit(1)

    df = load_timeseries(args.input, args.date_col, args.value_col)
    print(f"Loaded {len(df)} observations")
    print(f"Date range: {df[args.date_col].iloc[0]} to {df[args.date_col].iloc[-1]}")

    result = extract_phenology(
        df, args.date_col, args.value_col,
        method=args.method, threshold_ratio=args.threshold_ratio,
    )

    print(f"\nPhenology Metrics ({args.method} method):")
    for key, val in result.items():
        if key not in ("fitted_values", "fitted_params"):
            if isinstance(val, float):
                print(f"  {key}: {val:.4f}")
            else:
                print(f"  {key}: {val}")

    # Output
    if args.output:
        output_data = {k: v for k, v in result.items() if k not in ("fitted_values", "fitted_params")}
        # Resolve --format (new) vs --json (deprecated) vs suffix
        fmt = getattr(args, "fmt", None)
        if fmt is None:
            if getattr(args, "json", False):
                fmt = "json"
            else:
                fmt = "json" if args.output.endswith(".json") else "csv"
        if fmt == "json":
            with open(args.output, "w") as f:
                json.dump(output_data, f, indent=2, default=str)
        else:
            pd.DataFrame([output_data]).to_csv(args.output, index=False)
        print(f"\nSaved: {args.output} (format={fmt})")

        # QA summary (v0.2.0)
        if getattr(args, "qa", False):
            qa_path = os.path.splitext(args.output)[0] + ".qa.json"
            qa = {
                "input": args.input,
                "place": getattr(args, "place", None),
                "place_info": getattr(args, "place_info", None),
                "preset": getattr(args, "preset", None),
                "method": args.method,
                "value_col": args.value_col,
                "date_col": args.date_col,
                "n_observations": int(len(df)),
                "date_range": [str(df[args.date_col].iloc[0]), str(df[args.date_col].iloc[-1])],
                "metrics": output_data,
                "output": args.output,
                "format": fmt,
            }
            with open(qa_path, "w", encoding="utf-8") as f:
                json.dump(qa, f, indent=2, ensure_ascii=False)
            print(f"  QA summary: {qa_path}")

    if getattr(args, "json", False) and getattr(args, "fmt", None) is None:
        output_data = {k: v for k, v in result.items() if k not in ("fitted_values", "fitted_params")}
        print(json.dumps(output_data, indent=2, default=str))


def cmd_from_place(args):
    """One-line phenology: resolve --place via geoskill_core.aoi + fetch NDVI + extract.

    [PHASE 1+ 2026-07-26 REFACTOR]
    Step 1: _geoskill_core.aoi.resolve_place(place) → bbox
    Step 2: subprocess 调 landsat-download 拉场景
    Step 3: 调本 skill cmd_extract 计算物候指标
    """
    import os as _os
    import sys as _sys
    import subprocess as _sp

    skill_dir = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
    gk_dir = _os.path.join(skill_dir, "_geoskill_core")
    if not _os.path.isdir(gk_dir):
        print("ERROR: _geoskill_core not vendored. Run vendor.py.", file=sys.stderr)
        return 3
    if skill_dir not in _sys.path:
        _sys.path.insert(0, skill_dir)
    try:
        from _geoskill_core import aoi as _aoi
    except Exception as _e:
        print(f"ERROR: failed to import _geoskill_core.aoi: {_e}", file=sys.stderr)
        return 3
    try:
        m = _aoi.resolve_place(args.place, allow_nominatim=not args.no_nominatim, use_cache=False)
    except Exception as _e:
        print(f"ERROR: failed to resolve --place={args.place!r}: {_e}", file=sys.stderr)
        return 5
    bbox = m.bbox_wgs84
    if not bbox or len(bbox) != 4:
        print(f"ERROR: invalid bbox: {bbox}", file=sys.stderr)
        return 5
    print(f"[from-place] resolved {args.place!r} → bbox={bbox} (resolver={m.resolver})",
          file=sys.stderr)
    # Step 2: 调 landsat-download
    parent = _os.path.dirname(skill_dir)
    fetch_dir = _os.path.join(parent, "landsat-download")
    fetch_script = _os.path.join(fetch_dir, "landsat-download.py")
    if not _os.path.isfile(fetch_script):
        for cand in [_os.path.join(fetch_dir, "scripts", "landsat-download.py")]:
            if _os.path.isfile(cand):
                fetch_script = cand
                break
    if not _os.path.isfile(fetch_script):
        print(f"ERROR: landsat-download script not found at {fetch_dir}", file=sys.stderr)
        return 3
    out_dir = _os.path.dirname(args.output) or "."
    cache_dir = _os.path.join(out_dir, ".from_place_cache")
    _os.makedirs(cache_dir, exist_ok=True)
    start = getattr(args, "start_date", "2023-01-01")
    end = getattr(args, "end_date", "2023-12-31")
    cmd = [
        _sys.executable, fetch_script,
        "--bbox", str(bbox[0]), str(bbox[1]), str(bbox[2]), str(bbox[3]),
        "--start-date", start,
        "--end-date", end,
        "--output-dir", cache_dir,
    ]
    print(f"[from-place] invoking: {' '.join(cmd)}", file=sys.stderr)
    try:
        r = _sp.run(cmd, capture_output=True, text=True, timeout=900)
    except _sp.TimeoutExpired:
        print("ERROR: landsat-download timeout (900s)", file=sys.stderr)
        return 4
    except Exception as _e:
        print(f"ERROR: landsat-download failed: {_e}", file=sys.stderr)
        return 7
    if r.returncode != 0:
        print(f"ERROR: landsat-download exit {r.returncode}:\n{r.stderr[-500:]}",
              file=sys.stderr)
        return r.returncode
    tif_files = []
    for root, _, files in _os.walk(cache_dir):
        for f in files:
            if f.endswith(".tif") and "SR_B" in f.upper() and not f.endswith(".part"):
                tif_files.append(_os.path.join(root, f))
    if not tif_files:
        print(f"ERROR: no Landsat SR .tif produced in {cache_dir}", file=sys.stderr)
        return 5
    # Step 3: 调本 skill extract
    extract_args = argparse.Namespace(
        inputs=tif_files, output=args.output, method=getattr(args, "method", "double-logistic"),
        threshold=getattr(args, "threshold", 0.2),
        ndvi_csv=None,
    )
    return cmd_extract(extract_args)
    from rasterio.warp import reproject as _reproj, Resampling

    _shared_path = _os.path.join(
        _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))),
        "_shared", "from_stac.py",
    )
    if not _os.path.exists(_shared_path):
        print(f"ERROR: shared helper not found at {_shared_path}", file=sys.stderr)
        return 2
    spec = importlib.util.spec_from_file_location("from_stac", _shared_path)
    fs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fs)
    if not fs.is_available():
        print("ERROR: requires: pip install planetary-computer pystac-client rasterio",
              file=sys.stderr)
        return 2

    # Fetch 12 monthly windows (one per month of --year)
    year = int(args.year)
    rows = []
    for m in range(1, 13):
        start = f"{year}-{m:02d}-01"
        if m == 12:
            end = f"{year}-12-31"
        else:
            import calendar
            last_day = calendar.monthrange(year, m)[1]
            end = f"{year}-{m:02d}-{last_day}"
        try:
            meta = fs.fetch_scenes(
                place=args.place, start=start, end=end,
                dataset="sentinel-2-l2a",
                bands=["B04", "B08"],
                max_cloud=args.max_cloud,
                limit=1,
                output_dir=_os.path.join(args.cache_dir, f"{year}-{m:02d}"),
                no_nominatim=args.no_nominatim,
                buffer_deg=args.buffer_deg,
                quiet=True,
            )
        except Exception as e:
            print(f"WARNING: month {m} fetch failed: {e}", file=sys.stderr)
            continue
        # Compute mean NDVI for the month
        scene = meta["scenes"][0]
        b4 = scene["asset_paths"].get("B04")
        b8 = scene["asset_paths"].get("B08")
        if not (b4 and b8 and _os.path.exists(b4) and _os.path.exists(b8)):
            print(f"WARNING: month {m} missing B04/B08", file=sys.stderr)
            continue
        with rasterio.open(b4) as s4, rasterio.open(b8) as s8:
            red = s4.read(1).astype("float32")
            nir = s8.read(1).astype("float32")
            if s4.profile["transform"] != s8.profile["transform"]:
                nir2 = np.empty_like(nir)
                _reproj(nir, nir2, src_transform=s8.transform, src_crs=s8.crs,
                        dst_transform=s4.transform, dst_crs=s4.crs, resampling=Resampling.bilinear)
                nir = nir2
            with np.errstate(divide="ignore", invalid="ignore"):
                ndvi = (nir - red) / (nir + red)
            valid = ndvi[(nir + red) != 0]
            if valid.size == 0:
                continue
            rows.append({
                "date": pd.Timestamp(year=year, month=m, day=15),
                "ndvi": float(np.mean(valid)),
            })

    if not rows:
        print("ERROR: no monthly composites available", file=sys.stderr)
        return 1

    df = pd.DataFrame(rows).sort_values("date").reset_index(drop=True)
    out_path = args.output
    if args.json:
        out_path = out_path if out_path.endswith(".json") else out_path + ".json"
        df.to_json(out_path, orient="records", force_ascii=False)
    else:
        out_path = out_path if out_path.endswith(".csv") else out_path + ".csv"
        df.to_csv(out_path, index=False)
    print(f"[from-place] wrote {len(df)} monthly NDVI records to {out_path}", file=sys.stderr)

    # Now run cmd_extract on the output
    extract_args = argparse.Namespace(
        input=out_path, date_col="date", value_col="ndvi",
        method=args.method, threshold_ratio=0.5, place=args.place,
        preset=None, output=out_path + ".pheno.json" if not args.json else None,
        json=True, qa=args.qa,
    )
    try:
        return cmd_extract(extract_args)
    except SystemExit:
        return 0


def cmd_fit(args):
    """Handle fit subcommand — fit double logistic and output."""
    if not os.path.isfile(args.input):
        print(f"ERROR: Input file not found: {args.input}")
        sys.exit(1)

    df = load_timeseries(args.input, args.date_col, args.value_col)
    dates_numeric = (df[args.date_col] - df[args.date_col].iloc[0]).dt.total_seconds().values / 86400.0
    values = df[args.value_col].values.astype(np.float64)

    result = fit_logistic(dates_numeric, values)

    print(f"\nDouble Logistic Fit:")
    print(f"  R²: {result.get('r_squared', 'N/A')}")
    print(f"  Baseline: {result.get('baseline', 'N/A')}")
    print(f"  Peak: {result.get('peak_value', 'N/A')}")
    print(f"  Green-up rate: {result.get('greenup_rate', 'N/A')}")
    print(f"  Senescence rate: {result.get('senescence_rate', 'N/A')}")

    # Output
    if args.output:
        output_data = {k: v for k, v in result.items() if k != "fitted_values"}
        with open(args.output, "w") as f:
            json.dump(output_data, f, indent=2, default=str)
        print(f"\nSaved: {args.output}")

    # Plot data
    if args.plot_data and "fitted_values" in result:
        plot_df = pd.DataFrame({
            "date": df[args.date_col].values,
            "original": values,
            "fitted": result["fitted_values"],
        })
        plot_df.to_csv(args.plot_data, index=False)
        print(f"Plot data saved: {args.plot_data}")


def cmd_plot_data(args):
    """Handle plot-data subcommand — generate smooth curve data."""
    if not os.path.isfile(args.input):
        print(f"ERROR: Input file not found: {args.input}")
        sys.exit(1)

    df = load_timeseries(args.input, args.date_col, args.value_col)
    dates_numeric = (df[args.date_col] - df[args.date_col].iloc[0]).dt.total_seconds().values / 86400.0
    values = df[args.value_col].values.astype(np.float64)

    # Fit and generate smooth curve
    result = fit_logistic(dates_numeric, values)

    if "fitted_values" in result:
        plot_df = pd.DataFrame({
            "date": df[args.date_col].values,
            "original": values,
            "fitted": result["fitted_values"],
        })
        plot_df.to_csv(args.output, index=False)
        print(f"Plot data saved: {args.output}")
    else:
        print("ERROR: Fitting failed, cannot generate plot data.")
        sys.exit(1)


# ─── CLI Setup ───────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="phenology-metrics",
        description="Extract phenological metrics from NDVI/EVI time series",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Privacy: This tool processes all data locally. No data is sent to external servers.

Examples:
  %(prog)s extract -i ndvi.csv --date-col date --value-col ndvi --method threshold
  %(prog)s fit -i ndvi.csv --date-col date --value-col ndvi -o fit.json --plot-data curve.csv
  %(prog)s plot-data -i ndvi.csv --date-col date --value-col ndvi -o curve.csv
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # ── extract ──
    p_extract = subparsers.add_parser("extract", help="Extract phenology metrics")
    p_extract.add_argument("-i", "--input", required=True, help="Input CSV file")
    p_extract.add_argument("--date-col", default="date", help="Date column name")
    p_extract.add_argument("--value-col", default="ndvi", help="Value column name")
    p_extract.add_argument("--method", default="threshold", choices=VALID_METHODS,
                           help="Extraction method")
    p_extract.add_argument("--threshold-ratio", type=float, default=0.5,
                           help="Threshold ratio for threshold method (0-1)")
    p_extract.add_argument("--place", help="Place name (Chinese or English); for context only")
    p_extract.add_argument("--preset", choices=list(PRESETS.keys()),
                           help="Use a preset (phenology-ndvi, phenology-evi, phenology-threshold, phenology-fast)")
    p_extract.add_argument("-o", "--output", help="Output file (CSV or JSON)")
    p_extract.add_argument("--format", dest="fmt", choices=["csv", "json"], default=None,
                           help="Output format: csv (default) or json. "
                                "If omitted, inferred from --output suffix.")
    p_extract.add_argument("--json", action="store_true",
                           help="[deprecated] Shorthand for --format json (kept for backward compat)")
    p_extract.add_argument("--qa", action="store_true", help="Write QA summary JSON next to the output")
    p_extract.set_defaults(func=cmd_extract)

    # ── fit ──
    p_fit = subparsers.add_parser("fit", help="Fit double logistic curve")
    p_fit.add_argument("-i", "--input", required=True, help="Input CSV file")
    p_fit.add_argument("--date-col", default="date", help="Date column name")
    p_fit.add_argument("--value-col", default="ndvi", help="Value column name")
    p_fit.add_argument("-o", "--output", help="Output JSON file")
    p_fit.add_argument("--plot-data", help="Output fitted curve CSV for plotting")
    p_fit.set_defaults(func=cmd_fit)

    # ── plot-data ──
    p_plot = subparsers.add_parser("plot-data", help="Generate fitted curve data for plotting")
    p_plot.add_argument("-i", "--input", required=True, help="Input CSV file")
    p_plot.add_argument("--date-col", default="date", help="Date column name")
    p_plot.add_argument("--value-col", default="ndvi", help="Value column name")
    p_plot.add_argument("-o", "--output", required=True, help="Output CSV file")
    p_plot.set_defaults(func=cmd_plot_data)

    # ── from-place: 拉 S2 时序 → 算 NDVI → 物候提取 ──
    p_fp = subparsers.add_parser(
        "from-place",
        help="One-line phenology: --place + --year → fetch S2 monthly composites + compute NDVI + extract phenology. "
             "Requires: pip install planetary-computer pystac-client rasterio.",
    )
    p_fp.add_argument("--place", required=True, help="行政区名 (中文/English) → bbox")
    p_fp.add_argument("--year", required=True, type=int, help="Year (e.g. 2024)")
    p_fp.add_argument("--max-cloud", type=float, default=20.0, help="最大云量%% (default 20)")
    p_fp.add_argument("--buffer-deg", type=float, default=0.3, help="Buffer degrees (default 0.3°)")
    p_fp.add_argument("--cache-dir", default="./pheno_cache")
    p_fp.add_argument("--no-nominatim", action="store_true")
    p_fp.add_argument("--method", default="threshold", choices=["threshold", "derivative", "logistic"])
    p_fp.add_argument("--output", required=True, help="Output CSV (or JSON if --format json)")
    p_fp.add_argument("--format", dest="fmt", choices=["csv", "json"], default=None,
                      help="Output format: csv (default) or json. "
                           "If omitted, inferred from --output suffix.")
    p_fp.add_argument("--json", action="store_true",
                      help="[deprecated] Shorthand for --format json (kept for backward compat)")
    p_fp.add_argument("--qa", action="store_true")
    p_fp.set_defaults(func=cmd_from_place)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Lazy import of shared from-stac helper (only when from-place is used)
    if args.command == "from-place":
        cmd_from_place(args)
        return

    try:
        return args.func(args)
    except ValueError as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nAborted by user.")
        sys.exit(130)


if __name__ == "__main__":
    sys.exit(main())

