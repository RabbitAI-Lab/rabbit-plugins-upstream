#!/usr/bin/env python3
"""
Open-Elevation CLI — Batch elevation lookup via the Open-Elevation public API.

Privacy Notice:
    This tool sends ONLY latitude/longitude coordinates to
    api.open-elevation.com. No personal data, cookies, or
    identifiers are transmitted.

Data Source:
    Open-Elevation API (https://open-elevation.com/)
    Public domain, no API key required.

License: MIT-0
Author: ruiduobao
Version: 0.1.0
"""

import argparse
import csv
import json
import sys
import os
from typing import List, Dict, Any, Optional

try:
    import requests
except ImportError:
    print("ERROR: 'requests' is required. Install with: pip install requests>=2.28.0")
    sys.exit(1)

try:
    from tqdm import tqdm
except ImportError:
    tqdm = None  # type: ignore

API_URL = "https://api.open-elevation.com/api/v1/lookup"
# Public mirrors / fallbacks
API_ENDPOINTS = [
    API_URL,
]
MAX_CHUNK = 100
TIMEOUT = 30
USER_AGENT = "open-elevation/0.2.0 (public geodata workflow)"

# Nominatim fallback chain (mirrors osm-data-download / nasa-power-download / soilgrids-download)
NOMINATIM_ENDPOINTS = [
    "https://nominatim.openstreetmap.org/search",
]


def validate_lat(lat: float) -> bool:
    return -90.0 <= lat <= 90.0


def validate_lon(lon: float) -> bool:
    return -180.0 <= lon <= 180.0


def query_elevation(locations: List[Dict[str, float]]) -> Optional[List[Dict[str, Any]]]:
    """Query elevation for a list of {latitude, longitude} dicts."""
    payload = {"locations": locations}
    last_err = None
    for endpoint in API_ENDPOINTS:
        try:
            resp = requests.post(endpoint, json=payload, timeout=TIMEOUT,
                                 headers={"User-Agent": USER_AGENT})
            if resp.status_code == 429 or resp.status_code >= 500:
                last_err = f"HTTP {resp.status_code}"
                continue
            resp.raise_for_status()
            data = resp.json()
            return data.get("results", [])
        except requests.exceptions.Timeout:
            last_err = "timeout"
            continue
        except requests.exceptions.ConnectionError:
            last_err = "connection"
            continue
        except requests.exceptions.HTTPError as e:
            last_err = f"HTTP {e.response.status_code}: {e.response.text[:100]}"
            continue
        except json.JSONDecodeError:
            last_err = "invalid JSON"
            continue
    print(f"ERROR: All Open-Elevation endpoints failed ({last_err}).", file=sys.stderr)
    return None


def _nominatim_search(query: str, timeout: int = 30):
    last_err = None
    params = {"q": query, "format": "jsonv2", "limit": 1, "addressdetails": 1}
    for endpoint in NOMINATIM_ENDPOINTS:
        try:
            r = requests.get(endpoint, params=params,
                headers={"User-Agent": USER_AGENT, "Accept-Language": "zh-CN,zh;q=0.9"},
                timeout=timeout)
            if r.status_code == 429 or r.status_code >= 500:
                last_err = f"HTTP {r.status_code}"
                continue
            r.raise_for_status()
            return r.json()
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            last_err = str(e)
            continue
    raise RuntimeError(f"All Nominatim endpoints failed for {query!r}: {last_err}")


def resolve_place(place: str) -> dict:
    """Resolve place name to (lat, lon, display_name, osm_id)."""
    import re
    normalised = re.sub(r"\s+", "", place.strip())
    if not normalised:
        raise ValueError("--place must not be empty")
    candidates = _nominatim_search(normalised)
    if not candidates:
        raise ValueError(f"No results for {place!r}")
    c = candidates[0]
    return {
        "query": place,
        "display_name": c.get("display_name"),
        "lat": float(c.get("lat")),
        "lon": float(c.get("lon")),
        "osm_id": c.get("osm_id"),
        "osm_type": c.get("osm_type"),
    }


def write_qa_summary(out_path: str, *, source: str, count: int, query_meta: dict) -> str:
    """Write a QA summary JSON next to the output."""
    qa = {
        "source": source,
        "count": count,
        "crs": "EPSG:4326 (WGS84)",
        **query_meta,
        "output": out_path,
    }
    qa_path = os.path.splitext(out_path)[0] + ".qa.json"
    try:
        with open(qa_path, "w", encoding="utf-8") as f:
            json.dump(qa, f, ensure_ascii=False, indent=2)
        print(f"QA: {qa_path}")
    except Exception as e:
        print(f"WARNING: failed to write QA summary: {e}")
    return qa_path


def _resolve_format(args, default: str = "csv") -> str:
    """Resolve --format (new) vs --json (deprecated alias)."""
    fmt = getattr(args, "fmt", None)
    if fmt is None:
        if getattr(args, "json", False):
            fmt = "json"
        else:
            fmt = default
    return fmt


def cmd_lookup(args: argparse.Namespace) -> int:
    """Handle the 'lookup' subcommand."""
    place_info = None
    if args.place:
        try:
            place_info = resolve_place(args.place)
        except (ValueError, RuntimeError) as e:
            print(f"ERROR: could not resolve --place: {e}", file=sys.stderr)
            return 1
        lat, lon = place_info["lat"], place_info["lon"]
        print(f"Resolved {args.place!r} → {place_info['display_name']}")
    else:
        lat, lon = args.lat, args.lon
    if lat is None or lon is None:
        print("ERROR: provide either --place or both --lat/--lon", file=sys.stderr)
        return 1
    if not validate_lat(lat):
        print(f"ERROR: latitude {lat} out of range [-90, 90].", file=sys.stderr)
        return 1
    if not validate_lon(lon):
        print(f"ERROR: longitude {lon} out of range [-180, 180].", file=sys.stderr)
        return 1

    results = query_elevation([{"latitude": lat, "longitude": lon}])
    if results is None:
        return 1

    fmt = _resolve_format(args, default="csv")
    if fmt == "json":
        print(json.dumps(results[0], indent=2, ensure_ascii=False))
    else:
        r = results[0]
        # CSV-style: "lat,lon,elevation" on one line
        print(f"{r['latitude']},{r['longitude']},{r['elevation']}")

    if args.qa:
        qa_meta = {
            "place": place_info,
            "query": {"lat": lat, "lon": lon},
            "endpoint": API_URL,
            "format": fmt,
        }
        # default output to a json next to nothing
        out = args.output or f"elevation_{lat:.4f}_{lon:.4f}.json"
        write_qa_summary(out, source="open-elevation", count=1, query_meta=qa_meta)
    return 0


def detect_columns(headers: List[str]) -> tuple:
    """Detect lat/lon column names from CSV headers."""
    headers_lower = [h.strip().lower() for h in headers]
    lat_col = None
    lon_col = None
    for h in headers_lower:
        if h in ("lat", "latitude", "y"):
            lat_col = h
        if h in ("lon", "lng", "long", "longitude", "x"):
            lon_col = h
    return lat_col, lon_col


def cmd_batch(args: argparse.Namespace) -> int:
    """Handle the 'batch' subcommand."""
    input_path = args.input
    output_path = args.output
    chunk_size = args.chunk

    if not os.path.isfile(input_path):
        print(f"ERROR: Input file '{input_path}' not found.", file=sys.stderr)
        return 1
    if chunk_size < 1 or chunk_size > MAX_CHUNK:
        print(f"ERROR: --chunk must be between 1 and {MAX_CHUNK}.", file=sys.stderr)
        return 1

    # Read CSV
    rows = []
    try:
        with open(input_path, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                print("ERROR: CSV file is empty or has no headers.", file=sys.stderr)
                return 1
            lat_col, lon_col = detect_columns(list(reader.fieldnames))
            if not lat_col or not lon_col:
                print(
                    f"ERROR: Could not detect lat/lon columns. Headers: {reader.fieldnames}",
                    file=sys.stderr,
                )
                print("Expected columns: lat/latitude and lon/lng/longitude.", file=sys.stderr)
                return 1
            for row in reader:
                try:
                    lat = float(row[lat_col])
                    lon = float(row[lon_col])
                    rows.append((lat, lon))
                except (ValueError, KeyError):
                    continue
    except Exception as e:
        print(f"ERROR: Failed to read input file: {e}", file=sys.stderr)
        return 1

    if not rows:
        print("ERROR: No valid coordinate pairs found in input file.", file=sys.stderr)
        return 1

    print(f"Read {len(rows)} coordinate pairs. Querying in chunks of {chunk_size}...")

    # Query in chunks
    all_results: List[Dict[str, Any]] = []
    chunks = [rows[i : i + chunk_size] for i in range(0, len(rows), chunk_size)]
    iterator = tqdm(chunks) if tqdm else chunks

    for chunk in iterator:
        locations = [{"latitude": lat, "longitude": lon} for lat, lon in chunk]
        results = query_elevation(locations)
        if results is None:
            print("ERROR: Batch query failed. Partial results discarded.", file=sys.stderr)
            return 1
        all_results.extend(results)

    # Write output
    try:
        fmt = _resolve_format(args, default="csv")
        # If --format not given, infer from suffix
        if getattr(args, "fmt", None) is None and not getattr(args, "json", False):
            if output_path.lower().endswith(".json"):
                fmt = "json"
            else:
                fmt = "csv"
        if fmt == "json":
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(all_results, f, indent=2, ensure_ascii=False)
        else:
            with open(output_path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["latitude", "longitude", "elevation"])
                writer.writeheader()
                writer.writerows(all_results)
        print(f"Wrote {len(all_results)} results to {output_path} (format={fmt})")
    except Exception as e:
        print(f"ERROR: Failed to write output file: {e}", file=sys.stderr)
        return 1

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="open-elevation",
        description="Query elevation data from the Open-Elevation public API.",
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcommand")

    # lookup
    p_lookup = subparsers.add_parser("lookup", help="Single-point elevation lookup")
    p_lookup.add_argument("--place", help="Place name (e.g. '北京市朝阳区'); resolved via Nominatim")
    p_lookup.add_argument("--lat", type=float, help="Latitude (-90 to 90)")
    p_lookup.add_argument("--lon", type=float, help="Longitude (-180 to 180)")
    p_lookup.add_argument("--format", dest="fmt", choices=["csv", "json"], default=None,
                          help="Output format: csv (default) or json")
    p_lookup.add_argument("--json", action="store_true",
                          help="[deprecated] Shorthand for --format json (kept for backward compat)")
    p_lookup.add_argument("--qa", action="store_true",
                          help="Write a QA summary JSON")
    p_lookup.add_argument("--output", help="Path used as the basis for the QA summary file")

    # batch
    p_batch = subparsers.add_parser("batch", help="Batch elevation lookup from CSV")
    p_batch.add_argument("--input", required=True, help="Input CSV file path")
    p_batch.add_argument("--output", required=True, help="Output file path")
    p_batch.add_argument("--format", dest="fmt", choices=["csv", "json"], default=None,
                          help="Output format: csv (default) or json. "
                               "If omitted, inferred from --output suffix.")
    p_batch.add_argument("--json", action="store_true",
                         help="[deprecated] Shorthand for --format json (kept for backward compat)")
    p_batch.add_argument(
        "--chunk", type=int, default=100, help=f"Points per API call (max {MAX_CHUNK}, default 100)"
    )

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "lookup":
        return cmd_lookup(args)
    elif args.command == "batch":
        return cmd_batch(args)
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
