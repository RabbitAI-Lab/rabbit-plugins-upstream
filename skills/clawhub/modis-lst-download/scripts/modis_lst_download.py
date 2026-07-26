#!/usr/bin/env python3
"""
MODIS Land Surface Temperature Download CLI
============================================
Search and download MODIS LST products from NASA LAADS DAAC.

Privacy Notice:
- This tool sends ONLY the following data to NASA servers:
  * Bounding box coordinates
  * Date range
  * Product name
- If Earthdata auth is configured, credentials are sent to urs.earthdata.nasa.gov
  for authentication only.
- NO personal data beyond credentials is sent.
- All data is processed locally except the API request itself.

License: MIT-0 (Public Domain)
Data: NASA MODIS, Public Domain
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: 'requests' package is required. Install with: pip install requests>=2.28.0")
    sys.exit(1)

try:
    from tqdm import tqdm
except ImportError:
    tqdm = None

# Local place-resolver (offline-first place name -> bbox lookup, batch3 v0.2.0+)
try:
    from place_resolver import (
        resolve_place,
        get_preset,
        list_presets,
        format_bbox,
        PlaceNotFoundError,
        PRESETS,
    )
except ImportError as _exc:
    print(
        f"Warning: place_resolver.py not found ({_exc}). "
        "--place/--preset will be unavailable. Re-install the skill.",
        file=sys.stderr,
    )
    PRESETS = {}

    def resolve_place(*args, **kwargs):
        raise RuntimeError("place_resolver.py missing — --place not available")

    def get_preset(name):
        raise ValueError(f"Unknown preset: {name} (place_resolver missing)")

    def list_presets():
        return "(place_resolver.py missing)"

    def format_bbox(b):
        return f"{b[0]} {b[1]} {b[2]} {b[3]}"

    class PlaceNotFoundError(ValueError):
        pass

# ── Constants ──────────────────────────────────────────────────────────────────
CMR_STAC_URL = "https://cmr.earthdata.nasa.gov/stac/LAADS"
EARTHDATA_AUTH_URL = "https://urs.earthdata.nasa.gov"
CONFIG_DIR = Path.home() / ".config" / "modis-lst-download"
CONFIG_FILE = CONFIG_DIR / "config.json"

__version__ = "0.2.0"
USER_AGENT = f"modis-lst-download/{__version__} (+https://clawhub.ai)"

PRODUCTS = {
    "MOD11A1": {
        "name": "MODIS/Terra Land Surface Temperature/Emissivity Daily L3 Global 1km",
        "satellite": "Terra",
        "temporal": "Daily",
        "resolution": "1km",
        "collection": "6.1",
        "daynight": ["Day", "Night"],
    },
    "MOD11A2": {
        "name": "MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km",
        "satellite": "Terra",
        "temporal": "8-day",
        "resolution": "1km",
        "collection": "6.1",
        "daynight": ["Day", "Night"],
    },
    "MYD11A1": {
        "name": "MODIS/Aqua Land Surface Temperature/Emissivity Daily L3 Global 1km",
        "satellite": "Aqua",
        "temporal": "Daily",
        "resolution": "1km",
        "collection": "6.1",
        "daynight": ["Day", "Night"],
    },
    "MYD11A2": {
        "name": "MODIS/Aqua Land Surface Temperature/Emissivity 8-Day L3 Global 1km",
        "satellite": "Aqua",
        "temporal": "8-day",
        "resolution": "1km",
        "collection": "6.1",
        "daynight": ["Day", "Night"],
    },
}

LAYERS = {
    "LST_Day_1km": "Daytime Land Surface Temperature (1km)",
    "LST_Night_1km": "Nighttime Land Surface Temperature (1km)",
    "QC_Day": "Daytime Quality Control",
    "QC_Night": "Nighttime Quality Control",
    "LST_Day_6km": "Daytime Land Surface Temperature (6km)",
    "LST_Night_6km": "Nighttime Land Surface Temperature (6km)",
    "Emis_31": "Band 31 Emissivity",
    "Emis_32": "Band 32 Emissivity",
    "Clear_day_cov": "Day clear-sky coverage",
    "Clear_night_cov": "Night clear-sky coverage",
}

# ── Config Management ──────────────────────────────────────────────────────────
def load_config():
    """Load configuration from file."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_config(config):
    """Save configuration to file."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)
    # Set restrictive permissions on config file
    try:
        os.chmod(CONFIG_FILE, 0o600)
    except OSError:
        pass

def get_earthdata_creds():
    """Get Earthdata credentials from env or config."""
    username = os.environ.get("EARTHDATA_USERNAME")
    password = os.environ.get("EARTHDATA_PASSWORD")

    if username and password:
        return username, password

    config = load_config()
    if "earthdata_username" in config:
        username = config["earthdata_username"]
        password = config.get("earthdata_password", "")
        return username, password if password else None

    return None, None

# ── Validation ─────────────────────────────────────────────────────────────────
def validate_bbox(bbox):
    """Validate bounding box: west, south, east, north."""
    if len(bbox) != 4:
        raise ValueError("Bounding box must have 4 values: west south east north")
    west, south, east, north = bbox
    if not (-90 <= south <= 90) or not (-90 <= north <= 90):
        raise ValueError("Latitude must be between -90 and 90")
    if not (-180 <= west <= 180) or not (-180 <= east <= 180):
        raise ValueError("Longitude must be between -180 and 180")
    if south >= north:
        raise ValueError(f"South ({south}) must be less than North ({north})")
    if west >= east:
        raise ValueError(f"West ({west}) must be less than East ({east})")
    return west, south, east, north

def validate_date_range(start_str, end_str, product=None):
    """Validate date range."""
    try:
        start = datetime.strptime(start_str, "%Y-%m-%d")
        end = datetime.strptime(end_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Dates must be in YYYY-MM-DD format")

    if end < start:
        raise ValueError("End date must be >= start date")

    # FIRMS NRT limited to 7 days
    if product and product.upper() == "NRT":
        max_range = timedelta(days=7)
        if (end - start) > max_range:
            raise ValueError("NRT product limited to 7-day range")
    elif product and product.upper() == "STANDARD":
        max_range = timedelta(days=365)
        if (end - start) > max_range:
            print(f"Warning: Standard product range > 1 year. Request may be large.")
    else:
        max_range = timedelta(days=365)
        if (end - start) > max_range:
            print(f"Warning: Date range > 1 year. Search may be slow or truncated.")

    return start, end

def validate_product(product):
    """Validate product name."""
    product = product.upper()
    if product not in PRODUCTS:
        raise ValueError(f"Unknown product: {product}. Valid: {', '.join(PRODUCTS.keys())}")
    return product

# ── CMR-STAC Search ────────────────────────────────────────────────────────────
def search_cmr(product, start, end, bbox):
    """Search CMR-STAC for available granules."""
    product_info = PRODUCTS[product]
    collection = f"C{product_info['collection'].replace('.', '')}*{product}"

    # Build CMR-STAC search request
    search_url = f"{CMR_STAC_URL}/search"

    payload = {
        "collections": [product],
        "datetime": f"{start.strftime('%Y-%m-%d')}T00:00:00Z/{end.strftime('%Y-%m-%d')}T23:59:59Z",
        "bbox": list(bbox),
        "limit": 200,
    }

    try:
        resp = requests.post(search_url, json=payload, timeout=60)
        resp.raise_for_status()
    except requests.exceptions.Timeout:
        raise RuntimeError("Search request timed out. Try a smaller date range.")
    except requests.exceptions.ConnectionError:
        raise RuntimeError("Connection error. Check your internet connection.")
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Search HTTP error {resp.status_code}: {resp.text[:300]}")

    results = resp.json()
    features = results.get("features", [])

    granules = []
    for feature in features:
        properties = feature.get("properties", {})
        granule = {
            "id": feature.get("id"),
            "datetime": properties.get("datetime", ""),
            "start_datetime": properties.get("start_datetime", ""),
            "end_datetime": properties.get("end_datetime", ""),
            "bbox": feature.get("bbox", []),
        }

        # Extract download links
        links = feature.get("links", [])
        for link in links:
            if link.get("rel") == "self":
                granule["self_link"] = link.get("href")
            elif "data" in link.get("rel", "") or link.get("href", "").endswith(".hdf"):
                granule["download_url"] = link.get("href")

        granules.append(granule)

    return granules

def get_download_urls(granule):
    """Get download URLs for a granule."""
    urls = []
    self_link = granule.get("self_link")
    if self_link:
        try:
            resp = requests.get(self_link, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            for link in data.get("links", []):
                href = link.get("href", "")
                if href.endswith((".hdf", ".tif", ".tiff")):
                    urls.append(href)
        except Exception:
            pass

    if granule.get("download_url"):
        urls.append(granule["download_url"])

    return urls

# ── Download Functions ─────────────────────────────────────────────────────────
def download_file(url, output_path, auth=None):
    """Download a file with progress bar."""
    try:
        with requests.get(url, stream=True, auth=auth, timeout=120) as resp:
            resp.raise_for_status()
            total_size = int(resp.headers.get("content-length", 0))

            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, "wb") as f:
                if tqdm and total_size > 0:
                    with tqdm(total=total_size, unit="B", unit_scale=True,
                              desc=output_path.name) as pbar:
                        for chunk in resp.iter_content(chunk_size=8192):
                            f.write(chunk)
                            pbar.update(len(chunk))
                else:
                    for chunk in resp.iter_content(chunk_size=8192):
                        f.write(chunk)

        return True
    except Exception as e:
        print(f"  Download failed: {e}")
        if Path(output_path).exists():
            Path(output_path).unlink()
        return False

# ── CLI Commands ───────────────────────────────────────────────────────────────
def resolve_args_to_bbox(args) -> tuple:
    """Resolve --place / --preset / --bbox in priority order:
    1. --bbox if user provided 4 floats
    2. --place (offline hardcoded + Nominatim fallback)
    3. --preset (preset's bbox)

    Returns (bbox, source_label) where source_label is for diagnostic prints.
    """
    # 1) --bbox wins
    if getattr(args, "bbox", None) and len(args.bbox) == 4:
        return validate_bbox(args.bbox), f"--bbox {format_bbox(args.bbox)}"

    # 2) --place (best for "北京市")
    if getattr(args, "place", None):
        try:
            bbox = resolve_place(args.place)
            return bbox, f"--place '{args.place}' → {format_bbox(bbox)}"
        except PlaceNotFoundError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            sys.exit(2)

    # 3) --preset (which has its own bbox + product + layers defaults)
    if getattr(args, "preset", None):
        p = get_preset(args.preset)
        bbox = p["bbox"]
        # Apply preset defaults to the args (only if not user-set)
        for k, v in p.items():
            if k in ("description", "bbox"):
                continue
            if not getattr(args, k, None):
                setattr(args, k, v)
        return bbox, f"--preset '{args.preset}' → {format_bbox(bbox)}"

    raise ValueError(
        "No spatial extent given. Provide one of: --bbox W S E N, "
        "--place '北京市', or --preset <name>."
    )


def cmd_search(args):
    """Search for available MODIS LST data."""
    # Apply preset defaults to args first (so --product may be filled in)
    bbox, source_label = resolve_args_to_bbox(args)
    if not args.product:
        print("Error: --product is required (or set via --preset).", file=sys.stderr)
        sys.exit(2)
    if not (args.start and args.end):
        print("Error: --start and --end are required (no preset covers dates).", file=sys.stderr)
        sys.exit(2)
    product = validate_product(args.product)
    start, end = validate_date_range(args.start, args.end)

    print(f"Searching {product} ({PRODUCTS[product]['name']})")
    print(f"  Period: {args.start} to {args.end}")
    print(f"  BBox:   {bbox}  (from {source_label})")

    granules = search_cmr(product, start, end, bbox)

    if not granules:
        print("No granules found for the given criteria.")
        return

    print(f"\nFound {len(granules)} granule(s):\n")
    print(f"{'#':<4} {'Date':<12} {'ID'}")
    print("-" * 70)
    for i, g in enumerate(granules, 1):
        date_str = g.get("datetime", "")[:10]
        print(f"{i:<4} {date_str:<12} {g['id']}")

    if args.json:
        print()
        print(json.dumps(
            {
                "product": product,
                "period": {"start": args.start, "end": args.end},
                "bbox": list(bbox),
                "extent_source": source_label,
                "granules": [
                    {"id": g["id"], "datetime": g.get("datetime", "")} for g in granules
                ],
            },
            ensure_ascii=False,
            indent=2,
        ))

    # Save search results
    results_file = CONFIG_DIR / "last_search.json"
    results_file.parent.mkdir(parents=True, exist_ok=True)
    with open(results_file, "w") as f:
        json.dump({"product": product, "granules": granules}, f, indent=2)
    print(f"\nSearch results saved to {results_file}")


def cmd_download(args):
    """Download MODIS LST data."""
    # Apply preset defaults to args first (so --product / --layers may be filled in)
    bbox, source_label = resolve_args_to_bbox(args)
    # Phase 2 round 2: --year/--season → --start/--end
    _apply_year_season(args)
    if not args.product:
        print("Error: --product is required (or set via --preset).", file=sys.stderr)
        sys.exit(2)
    if not (args.start and args.end):
        print("Error: --start and --end are required (no preset covers dates).", file=sys.stderr)
        sys.exit(2)
    if not args.layers:
        args.layers = "LST_Day_1km,QC_Day"
    product = validate_product(args.product)
    start, end = validate_date_range(args.start, args.end)

    # Get Earthdata credentials
    username, password = get_earthdata_creds()
    auth = (username, password) if username and password else None

    if not auth and not args.list_only and not args.list_urls:
        print("Warning: No Earthdata credentials found.")
        print("Set EARTHDATA_USERNAME and EARTHDATA_PASSWORD environment variables,")
        print("or run: python scripts/modis_lst_download.py configure")
        print("Will attempt to list download URLs only.\n")

    # Search for granules
    print(f"Searching {product}...")
    print(f"  Period: {args.start} to {args.end}")
    print(f"  BBox:   {bbox}  (from {source_label})")
    granules = search_cmr(product, start, end, bbox)

    if not granules:
        print("No granules found.")
        sys.exit(1)

    print(f"Found {len(granules)} granule(s).")

    # --list-urls: write to a JSON file instead of printing
    if args.list_urls:
        url_list_path = Path(args.list_urls)
        url_list_path.parent.mkdir(parents=True, exist_ok=True)
        rows = []
        for g in granules:
            urls = get_download_urls(g)
            for u in urls:
                rows.append({
                    "granule_id": g["id"],
                    "datetime": g.get("datetime", ""),
                    "url": u,
                })
        with open(url_list_path, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
        print(f"\n{len(rows)} download URLs written to {url_list_path}")
        return

    if args.list_only:
        print("\nDownload URLs:")
        for g in granules:
            urls = get_download_urls(g)
            date_str = g.get("datetime", "")[:10]
            print(f"\n  {date_str} - {g['id']}:")
            for url in urls:
                print(f"    {url}")
        return

    # Download
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    success_count = 0
    for g in granules:
        urls = get_download_urls(g)
        if not urls:
            print(f"  No download URL for {g['id']}")
            continue

        date_str = g.get("datetime", "")[:10]
        for url in urls:
            filename = url.split("/")[-1]
            output_path = output_dir / filename

            if output_path.exists():
                print(f"  Skipping {filename} (already exists)")
                success_count += 1
                continue

            print(f"  Downloading {filename}...")
            if download_file(url, output_path, auth):
                success_count += 1

    print(f"\nDownloaded {success_count} file(s) to {output_dir}")

    # Phase 2 round 2: write QA
    if getattr(args, "qa", None):
        _write_qa(args, bbox, source_label, len(granules), success_count)


# ── Phase 2 round 2 helpers ──
import calendar as _cal_modis

SEASON_MONTHS_MODIS = {
    "spring": (3, 5), "summer": (6, 8), "autumn": (9, 11),
    "fall": (9, 11), "winter": (12, 2),
}


def _apply_year_season(args):
    """Apply --year/--season to args.start/args.end (low priority: do not override user input)."""
    if args.season and not args.year:
        print("ERROR: --season 必须配合 --year", file=sys.stderr)
        sys.exit(2)
    if not (args.year or args.season):
        return
    if args.season and args.year and not args.start:
        s = args.season.lower()
        if s not in SEASON_MONTHS_MODIS:
            print(f"ERROR: --season must be one of {list(SEASON_MONTHS_MODIS.keys())}", file=sys.stderr)
            sys.exit(2)
        m1, m2 = SEASON_MONTHS_MODIS[s]
        y = args.year
        if m1 <= m2:
            args.start = f"{y}-{m1:02d}-01"
            last_day = _cal_modis.monthrange(y, m2)[1]
            args.end = f"{y}-{m2:02d}-{last_day}"
        else:
            args.start = f"{y}-{m1:02d}-01"
            last_day = _cal_modis.monthrange(y + 1, m2)[1]
            args.end = f"{y + 1}-{m2:02d}-{last_day}"
    elif args.year and not args.start:
        y = args.year
        args.start = f"{y}-01-01"
        args.end = f"{y}-12-31"


def _write_qa(args, bbox, source_label, granule_count, success_count):
    """Write QA JSON for the modis-lst-download invocation."""
    qa = {
        "skill": "modis-lst-download",
        "version": "0.2.0",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "user_agent": USER_AGENT,
        "command": "download",
        "args": vars(args),
        "query": {
            "product": args.product,
            "start": args.start, "end": args.end,
            "bbox": list(bbox) if bbox else None,
            "bbox_source": source_label,
            "layers": args.layers,
            "year": getattr(args, "year", None),
            "season": getattr(args, "season", None),
            "preset": getattr(args, "preset", None),
            "place": getattr(args, "place", None),
        },
        "granules_found": granule_count,
        "downloaded": success_count,
        "output": args.output,
    }
    qa_p = Path(args.qa)
    qa_p.parent.mkdir(parents=True, exist_ok=True)
    with open(qa_p, "w", encoding="utf-8") as f:
        json.dump(qa, f, ensure_ascii=False, indent=2, default=str)
    print(f"[modis-lst-download] wrote QA to {args.qa}", file=sys.stderr)


def cmd_configure(args):
    """Configure Earthdata credentials."""
    import getpass

    config = load_config()

    if args.username:
        config["earthdata_username"] = args.username
    else:
        config["earthdata_username"] = input("Earthdata username: ").strip()

    password = getpass.getpass("Earthdata password: ")
    config["earthdata_password"] = password

    save_config(config)
    print(f"Configuration saved to {CONFIG_FILE}")
    print("You can also set EARTHDATA_USERNAME and EARTHDATA_PASSWORD environment variables.")


def cmd_list_presets(args):
    """List available --preset names and their defaults."""
    print(list_presets())


def cmd_list_regions(args):
    """List the offline-baked region catalog (HARDCODED_BBOXES keys)."""
    try:
        from place_resolver import HARDCODED_BBOXES
    except ImportError:
        print("place_resolver.py missing", file=sys.stderr)
        return
    print(f"Offline region catalog ({len(HARDCODED_BBOXES)} entries):\n")
    for key in sorted(HARDCODED_BBOXES.keys()):
        bbox = HARDCODED_BBOXES[key]
        print(f"  {key:<24} {format_bbox(bbox)}")

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        prog="modis-lst-download",
        description="Search and download MODIS Land Surface Temperature data from NASA LAADS DAAC",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples (with natural language place names + presets — batch3 v0.2.0+):

  # Preset: city-uhi = Beijing 8-day MOD11A2 LST
  %(prog)s download --preset city-uhi --start 2023-07-01 --end 2023-07-30 --list-only

  # --place: just say "北京市" instead of --bbox
  %(prog)s search --product MOD11A1 --start 2023-06-01 --end 2023-06-30 --place 北京

  # --bbox still works (highest priority)
  %(prog)s search --product MOD11A1 --start 2023-06-01 --end 2023-06-30 \\
    --bbox 116.0 39.5 116.8 40.2

  # Save download URLs to a file (no auth needed)
  %(prog)s download --preset china-lst --start 2023-08-01 --end 2023-08-07 \\
    --list-urls urls.json

  %(prog)s configure --username your_earthdata_username
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Search command
    s = subparsers.add_parser("search", help="Search for available LST data")
    s.add_argument("--product", choices=list(PRODUCTS.keys()),
                   help="MODIS LST product (preset can fill this in)")
    s.add_argument("--start", help="Start date (YYYY-MM-DD)")
    s.add_argument("--end", help="End date (YYYY-MM-DD)")
    s.add_argument("--bbox", nargs=4, type=float,
                   metavar=("W", "S", "E", "N"),
                   help="Bounding box (W S E N). Conflicts with --place/--preset.")
    s.add_argument("--place",
                   help="Place name (e.g. '北京市', '长江流域'). Offline-baked or Nominatim.")
    s.add_argument("--preset", choices=list(PRESETS.keys()),
                   help="Apply a named preset (e.g. city-uhi, china-lst).")
    s.add_argument("--json", action="store_true",
                   help="Also emit a JSON dump of the search result.")
    s.set_defaults(func=cmd_search)

    # Download command
    dl = subparsers.add_parser("download", help="Download LST data")
    dl.add_argument("--product", choices=list(PRODUCTS.keys()),
                    help="MODIS LST product (preset can fill this in)")
    dl.add_argument("--start", help="Start date (YYYY-MM-DD)")
    dl.add_argument("--end", help="End date (YYYY-MM-DD)")
    dl.add_argument("--bbox", nargs=4, type=float,
                    metavar=("W", "S", "E", "N"),
                    help="Bounding box (W S E N). Conflicts with --place/--preset.")
    dl.add_argument("--place",
                    help="Place name (e.g. '北京市').")
    dl.add_argument("--preset", choices=list(PRESETS.keys()),
                    help="Apply a named preset (e.g. city-uhi).")
    dl.add_argument("--output", default="./modis_lst/",
                    help="Output directory (default: ./modis_lst/)")
    dl.add_argument("--layers", default=None,
                    help="Comma-separated layer names (default: LST_Day_1km,QC_Day)")
    dl.add_argument("--list-only", action="store_true",
                    help="Only list download URLs, do not download")
    dl.add_argument("--list-urls", metavar="FILE",
                    help="Write a JSON list of download URLs to FILE (no auth needed)")
    dl.add_argument("--username", help="Earthdata username (or set EARTHDATA_USERNAME)")
    # Phase 2 round 2: --year / --season / --qa (mirror landsat-download v0.2.0)
    dl.add_argument("--year", type=int, default=None,
                    help="Shortcut: --year 2024 → --start 2024-01-01 --end 2024-12-31")
    dl.add_argument("--season", choices=["spring", "summer", "autumn", "fall", "winter"],
                    default=None,
                    help="Northern-Hemisphere season（需配合 --year）")
    dl.add_argument("--qa", metavar="PATH", default=None,
                    help="Write a JSON QA summary to PATH")
    dl.set_defaults(func=cmd_download)

    # Configure command
    cfg = subparsers.add_parser("configure", help="Configure Earthdata credentials")
    cfg.add_argument("--username", help="Earthdata username")
    cfg.set_defaults(func=cmd_configure)

    # List-presets
    lp = subparsers.add_parser("list-presets", help="List available --preset names")
    lp.set_defaults(func=cmd_list_presets)

    # List-regions
    lr = subparsers.add_parser("list-regions", help="List offline-baked region names")
    lr.set_defaults(func=cmd_list_regions)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        return args.func(args)
    except ValueError as e:
        print(f"Validation error: {e}")
        sys.exit(1)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        sys.exit(130)

if __name__ == "__main__":
    sys.exit(main())
