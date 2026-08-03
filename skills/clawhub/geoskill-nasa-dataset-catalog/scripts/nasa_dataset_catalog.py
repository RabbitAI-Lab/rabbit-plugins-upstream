#!/usr/bin/env python
"""nasa-dataset-catalog — Search, browse, and download 52K+ NASA Earth science datasets.

Phase 7.5 (2026-07-27).

Bridges the curated offline catalog from
https://github.com/opengeos/NASA-Earth-Data (52,126 records) with live
NASA services (CMR, LP DAAC earthdata cloud, GES DISC) so users can:

  - ``search`` — find datasets by keyword (offline catalog or live CMR)
  - ``info``   — show detailed metadata for a short_name
  - ``granules`` — list granules for a dataset in space/time
  - ``download`` — pull a single granule (or batch from --list-urls)
  - ``stats``  — show catalog coverage by provider / year / collection

Credentials: resolved via vendored ``geoskill_core.credentials`` which
honours env vars / ~/.geoskill/secrets.json / ~/.netrc. Bearer token is
preferred for CMR / LP DAAC / GES DISC; basic auth is the fallback.

Exit codes (geoskill-core convention §2.2):
  0=success, 2=arg error, 3=missing dep, 4=network/rate-limit,
  5=no match, 6=data validation, 7=processing, 130=user interrupt.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Iterable

# ---------------------------------------------------------------------------
# Vendored geoskill-core helpers
# ---------------------------------------------------------------------------
_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))
import os as _os
if _os.environ.get("NDCLI_DEBUG"):
    print(f"DEBUG: __file__={__file__}", file=__import__("sys").stderr)
    print(f"DEBUG: _HERE={_HERE}", file=__import__("sys").stderr)
    print(f"DEBUG: _HERE.parent={_HERE.parent}", file=__import__("sys").stderr)
    print(f"DEBUG: sys.path[0]={sys.path[0]}", file=__import__("sys").stderr)
    print(f"DEBUG: _geoskill_core/ exists={(_HERE.parent / '_geoskill_core').is_dir()}", file=__import__("sys").stderr)
try:
    from _geoskill_core.credentials import (  # type: ignore
        get_earthdata_token,
        get_earthdata_creds,
        describe_credentials,
    )
    from _geoskill_core.errors import GeoSkillError, to_exit_code as exit_code_for  # type: ignore
    if _os.environ.get("NDCLI_DEBUG"):
        print("DEBUG: real import OK", file=__import__("sys").stderr)
except ImportError:
    if _os.environ.get("NDCLI_DEBUG"):
        print(f"DEBUG: fallback (ImportError: {sys.exc_info()[1]})", file=__import__("sys").stderr)
    # fall back to stdlib
    def get_earthdata_token() -> str:
        return os.environ.get("EARTHDATA_TOKEN", "")

    def get_earthdata_creds() -> tuple[str, str]:
        return (
            os.environ.get("EARTHDATA_USERNAME", ""),
            os.environ.get("EARTHDATA_PASSWORD", ""),
        )

    def describe_credentials() -> dict:
        return {}

    class GeoSkillError(Exception):
        pass

    def exit_code_for(exc: BaseException) -> int:
        return 7

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
DATA_DIR = SKILL_DIR / "data"
DEFAULT_CATALOG = DATA_DIR / "nasa_catalog.json"
OUTPUT_DIR = SKILL_DIR / "output"

CMR_SEARCH_URL = "https://cmr.earthdata.nasa.gov/search/granules.json"
CMR_COLLECTIONS_URL = "https://cmr.earthdata.nasa.gov/search/collections.json"
EARTHDATA_LOGIN_URL = "https://urs.earthdata.nasa.gov"

__version__ = "0.1.0"
__phase__ = "Phase 7.5 (2026-07-27)"

# ---------------------------------------------------------------------------
# Catalog loading
# ---------------------------------------------------------------------------


def _strip(s: Any) -> str:
    """Strip whitespace/newlines from a field, return '' for None."""
    if s is None:
        return ""
    if not isinstance(s, str):
        return str(s)
    return s.strip()


def load_catalog(path: Path = DEFAULT_CATALOG) -> list[dict]:
    """Load the offline NASA catalog (52K records from opengeos/NASA-Earth-Data)."""
    if not path.is_file():
        raise GeoSkillError(
            f"offline catalog not found at {path}. "
            f"Re-download from https://github.com/opengeos/NASA-Earth-Data"
        )
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise GeoSkillError(f"catalog at {path} is not a JSON list")
    return data


def normalize_record(rec: dict) -> dict:
    """Clean the opengeos catalog record: strip whitespace on ShortName etc."""
    return {
        "short_name": _strip(rec.get("ShortName")),
        "title": _strip(rec.get("EntryTitle")),
        "doi": _strip(rec.get("DOI")),
        "concept_id": _strip(rec.get("concept-id")),
        "provider": _strip(rec.get("provider-id")),
        "s3_links": _strip(rec.get("s3-links")),
        "bbox_crs": _strip(rec.get("bbox-crs")),
        "bbox": rec.get("bbox") if isinstance(rec.get("bbox"), list) else [],
        "horizontal_res": _strip(rec.get("horizontal_res")),
        "start_time": _strip(rec.get("start-time")),
        "end_time": _strip(rec.get("end-time")),
        "creator": _strip(rec.get("Creator")),
        "publisher": _strip(rec.get("Publisher")),
        "version": _strip(rec.get("Version")),
        "linkage": _strip(rec.get("Linkage")),
    }


def search_catalog(
    catalog: list[dict],
    keyword: str,
    *,
    provider: str | None = None,
    limit: int = 20,
) -> list[dict]:
    """Search the offline catalog by keyword (matches short_name / title / creator)."""
    keyword_lower = keyword.lower().strip()
    if not keyword_lower:
        return []
    results: list[dict] = []
    for rec in catalog:
        norm = normalize_record(rec)
        if provider and norm["provider"].lower() != provider.lower():
            continue
        hay = " ".join(
            [norm["short_name"], norm["title"], norm["creator"], norm["publisher"]]
        ).lower()
        if keyword_lower in hay:
            results.append(norm)
            if len(results) >= limit:
                break
    return results


# ---------------------------------------------------------------------------
# Live CMR
# ---------------------------------------------------------------------------


def _session_with_token() -> Any:
    """Build a requests.Session with bearer token if available."""
    try:
        import requests  # type: ignore
    except ImportError as e:
        raise GeoSkillError("requests library required: pip install requests") from e
    sess = requests.Session()
    token = get_earthdata_token()
    if token:
        sess.headers["Authorization"] = f"Bearer {token}"
    return sess


def cmr_search_collections(
    keyword: str, *, limit: int = 10, provider: str | None = None
) -> list[dict]:
    """Live CMR collection search (returns dataset-level metadata)."""
    sess = _session_with_token()
    params = {
        "keyword": keyword,
        "page_size": str(limit),
    }
    if provider:
        params["provider"] = provider
    r = sess.get(CMR_COLLECTIONS_URL, params=params, timeout=30)
    r.raise_for_status()
    return r.json().get("feed", {}).get("entry", [])


def cmr_search_granules(
    short_name: str,
    *,
    version: str | None = None,
    temporal: str | None = None,
    bbox: list[float] | None = None,
    limit: int = 20,
) -> list[dict]:
    """Live CMR granule search.

    Args:
        short_name: dataset short name (e.g. 'MOD11A1')
        version: dataset version (e.g. '061')
        temporal: 'YYYY-MM-DD,YYYY-MM-DD' (inclusive) or
                  'YYYY-MM-DDTHH:MM:SSZ,YYYY-MM-DDTHH:MM:SSZ'
        bbox: [W, S, E, N]
        limit: max results
    """
    sess = _session_with_token()
    params: dict[str, str] = {
        "short_name": short_name,
        "page_size": str(limit),
    }
    if version:
        params["version"] = version
    if temporal:
        params["temporal"] = temporal
    if bbox and len(bbox) == 4:
        params["bounding_box"] = ",".join(str(v) for v in bbox)
    r = sess.get(CMR_SEARCH_URL, params=params, timeout=30)
    r.raise_for_status()
    return r.json().get("feed", {}).get("entry", [])


def granule_download_url(entry: dict) -> str | None:
    """Extract a downloadable URL from a CMR granule entry."""
    for link in entry.get("links", []):
        rel = link.get("rel", "")
        if "data#" in rel or "enclosure" in rel:
            return link.get("href")
    return None


def download_granule(
    url: str,
    out_path: Path,
    *,
    chunk: int = 64 * 1024,
    max_bytes: int | None = None,
) -> int:
    """Download a single granule to ``out_path`` using the bearer token.

    Returns the number of bytes downloaded. Honors ``max_bytes`` for
    testing (e.g. download only first 1MB).
    """
    sess = _session_with_token()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    written = 0
    headers = {}
    if max_bytes is not None:
        headers["Range"] = f"bytes=0-{max_bytes - 1}"
    with sess.get(url, headers=headers, timeout=120, stream=True) as r:
        r.raise_for_status()
        with open(out_path, "wb") as f:
            for chunk_data in r.iter_content(chunk_size=chunk):
                if not chunk_data:
                    continue
                f.write(chunk_data)
                written += len(chunk_data)
                if max_bytes is not None and written >= max_bytes:
                    break
    return written


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------


def catalog_stats(catalog: list[dict]) -> dict:
    """Summarize the offline catalog: by provider, by year, etc."""
    by_provider: dict[str, int] = {}
    by_year: dict[str, int] = {}
    by_short_name: dict[str, int] = {}
    with_bbox = 0
    with_doi = 0
    for rec in catalog:
        norm = normalize_record(rec)
        by_provider[norm["provider"] or "UNKNOWN"] = by_provider.get(norm["provider"] or "UNKNOWN", 0) + 1
        if norm["bbox"]:
            with_bbox += 1
        if norm["doi"]:
            with_doi += 1
        if norm["start_time"]:
            m = re.match(r"^(\d{4})", norm["start_time"])
            if m:
                year = m.group(1)
                by_year[year] = by_year.get(year, 0) + 1
        if norm["short_name"]:
            by_short_name[norm["short_name"]] = by_short_name.get(norm["short_name"], 0) + 1
    return {
        "total_records": len(catalog),
        "with_bbox": with_bbox,
        "with_doi": with_doi,
        "top_providers": dict(sorted(by_provider.items(), key=lambda x: -x[1])[:15]),
        "year_distribution": dict(sorted(by_year.items())),
        "unique_short_names": len(by_short_name),
    }


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------


def emit_json(obj: Any, indent: int = 2) -> str:
    return json.dumps(obj, indent=indent, ensure_ascii=False)


def write_qa(path: Path, command: str, args: dict, **extras) -> None:
    """Write a JSON run-summary sidecar to ``path``.

    Mirrors the Phase 5 ``--qa`` convention so nasa-dataset-catalog joins
    the 38/40 ``--qa`` coverage.
    """
    if path is None:
        return
    # Convert Path / non-serializable args to str
    safe_args: dict = {}
    for k, v in (args or {}).items():
        if k == "func" or k == "command":
            # argparse 把 func 引用 / subcommand name 也塞进 args
            continue
        if isinstance(v, Path):
            safe_args[k] = str(v)
        elif callable(v):
            continue
        elif isinstance(v, (list, tuple)):
            safe_args[k] = [
                str(x) if isinstance(x, Path) else x for x in v
            ]
        elif isinstance(v, dict):
            safe_args[k] = {kk: (str(vv) if isinstance(vv, Path) else vv)
                           for kk, vv in v.items()}
        else:
            safe_args[k] = v
    payload = {
        "skill": "nasa-dataset-catalog",
        "version": __version__,
        "command": command,
        "args": safe_args,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "credentials": describe_credentials(),
        **extras,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(emit_json(payload), encoding="utf-8")


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------


def cmd_search(args: argparse.Namespace) -> int:
    """Search offline catalog + live CMR."""
    offline_results: list[dict] = []
    live_entries: list[dict] = []
    cmr_error: str | None = None
    if args.offline or not args.live:
        if not DEFAULT_CATALOG.is_file():
            print(f"  offline catalog not found: {DEFAULT_CATALOG}", file=sys.stderr)
            return 3
        if args.format != "json":
            print(f"Loading offline catalog ({DEFAULT_CATALOG.name})...")
        catalog = load_catalog()
        if args.format != "json":
            print(f"  {len(catalog):,} records loaded.")
        offline_results = search_catalog(
            catalog, args.keyword, provider=args.provider, limit=args.limit
        )
        if args.format != "json":
            print(f"\n[offline] Found {len(offline_results)} match(es) for keyword={args.keyword!r}:")
            for r in offline_results:
                print(
                    f"  - {r['short_name']:30s} | {r['provider']:18s} | "
                    f"{r['title'][:60]}"
                )
                if r["doi"]:
                    print(f"      DOI: https://doi.org/{r['doi']}")
    if args.live:
        if args.format != "json":
            print(f"\n[live] Searching CMR collections for {args.keyword!r}...")
        try:
            live_entries = cmr_search_collections(
                args.keyword, limit=args.limit, provider=args.provider
            )
        except Exception as e:
            cmr_error = str(e)
            if args.format != "json":
                print(f"  CMR error: {e}", file=sys.stderr)
        else:
            if args.format != "json":
                print(f"  {len(live_entries)} collection(s):")
                for e in live_entries:
                    print(f"  - {e.get('short_name', ''):30s} | {e.get('entry_title', '')[:60]}")
    if args.format == "json":
        print(emit_json({
            "offline": offline_results,
            "live_cmr": live_entries,
            "cmr_error": cmr_error,
        }))
    elif cmr_error:
        return 4
    if args.qa:
        write_qa(Path(args.qa), "search", vars(args))
    return 0


def cmd_info(args: argparse.Namespace) -> int:
    """Show detailed info for a short_name (offline first, then live CMR)."""
    info: dict = {}
    if DEFAULT_CATALOG.is_file():
        catalog = load_catalog()
        for rec in catalog:
            norm = normalize_record(rec)
            if norm["short_name"].lower() == args.short_name.lower():
                info["offline"] = norm
                break
    if args.live or not info:
        try:
            entries = cmr_search_collections(args.short_name, limit=3)
            if entries:
                e = entries[0]
                info["live_cmr"] = {
                    "short_name": e.get("short_name", ""),
                    "entry_title": e.get("entry_title", ""),
                    "summary": e.get("summary", ""),
                    "concept_id": e.get("id", ""),
                    "provider": e.get("provider", ""),
                }
        except Exception as e:
            print(f"  CMR error: {e}", file=sys.stderr)
    if not info:
        print(f"  No info found for short_name={args.short_name!r}", file=sys.stderr)
        return 5
    if args.format == "json":
        print(emit_json(info))
    else:
        for src, payload in info.items():
            print(f"\n=== {src} ===")
            if isinstance(payload, dict):
                for k, v in payload.items():
                    if k in ("s3_links",) and not v:
                        continue
                    print(f"  {k}: {v if not isinstance(v, list) else v}")
            else:
                print(f"  {payload}")
    if args.qa:
        write_qa(Path(args.qa), "info", vars(args), short_name=args.short_name, info=info)
    return 0


def cmd_granules(args: argparse.Namespace) -> int:
    """List granules for a short_name in a given temporal / bbox window."""
    try:
        entries = cmr_search_granules(
            args.short_name,
            version=args.version,
            temporal=args.temporal,
            bbox=args.bbox,
            limit=args.limit,
        )
    except Exception as e:
        print(f"  CMR error: {e}", file=sys.stderr)
        return 4
    rows = []
    for e in entries:
        url = granule_download_url(e)
        row = {
            "id": e.get("id", ""),
            "title": e.get("title", ""),
            "time_start": e.get("time_start", ""),
            "time_end": e.get("time_end", ""),
            "size_mb": e.get("granule_size", ""),
            "url": url,
        }
        rows.append(row)
        if args.format != "json":
            print(
                f"  - {row['title'][:80]:80s} | {row['time_start']} | "
                f"{row['size_mb']:>10} MB"
            )
            if url:
                print(f"      {url[:120]}")
    if args.list_urls and rows:
        out = Path(args.list_urls)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(emit_json(rows), encoding="utf-8")
        print(f"\n{len(rows)} URL(s) written to {out}")
    if args.format == "json":
        print(emit_json(rows))
    if args.qa:
        write_qa(Path(args.qa), "granules", vars(args), n_granules=len(rows))
    return 0


def cmd_download(args: argparse.Namespace) -> int:
    """Download a single granule by URL (or first match for short_name+bbox+temporal)."""
    url = args.url
    if not url and args.short_name:
        # find first granule
        try:
            entries = cmr_search_granules(
                args.short_name,
                version=args.version,
                temporal=args.temporal,
                bbox=args.bbox,
                limit=1,
            )
        except Exception as e:
            print(f"  CMR error: {e}", file=sys.stderr)
            return 4
        if not entries:
            print(f"  No granule found for short_name={args.short_name}", file=sys.stderr)
            return 5
        url = granule_download_url(entries[0])
        if not url:
            print(f"  Granule has no data# link: {entries[0].get('title')}", file=sys.stderr)
            return 5
    if not url:
        print("  Either --url or --short_name is required.", file=sys.stderr)
        return 2
    out_path = Path(args.output) if args.output else OUTPUT_DIR / url.rsplit("/", 1)[-1]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    max_bytes = args.max_bytes
    print(f"Downloading: {url}")
    print(f"  -> {out_path} (max_bytes={max_bytes})")
    t0 = time.time()
    try:
        size = download_granule(url, out_path, max_bytes=max_bytes)
    except Exception as e:
        print(f"  Download error: {e}", file=sys.stderr)
        return 4
    elapsed = time.time() - t0
    print(f"  done: {size:,} bytes in {elapsed:.1f}s ({size/1024/elapsed:.1f} KB/s)")
    if args.qa:
        write_qa(
            Path(args.qa), "download", vars(args),
            url=url, output=str(out_path), size_bytes=size, elapsed_s=elapsed,
        )
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    """Show catalog coverage stats."""
    if not DEFAULT_CATALOG.is_file():
        print(f"  offline catalog not found: {DEFAULT_CATALOG}", file=sys.stderr)
        return 3
    catalog = load_catalog()
    stats = catalog_stats(catalog)
    if args.format == "json":
        print(emit_json(stats))
    else:
        print(f"Offline catalog: {DEFAULT_CATALOG}")
        print(f"  total records       : {stats['total_records']:,}")
        print(f"  with bbox           : {stats['with_bbox']:,}")
        print(f"  with DOI            : {stats['with_doi']:,}")
        print(f"  unique short_names  : {stats['unique_short_names']:,}")
        print(f"\nTop providers (by record count):")
        for prov, n in list(stats["top_providers"].items())[:10]:
            print(f"  {prov:30s} : {n:>6,}")
        print(f"\nYear distribution (start_time year):")
        by_year = stats["year_distribution"]
        if by_year:
            years = sorted(by_year.keys())
            print(f"  earliest: {years[0]}, latest: {years[-1]}, distinct years: {len(years)}")
            for y in years[-15:]:
                print(f"  {y}: {by_year[y]:>6,}")
    if args.qa:
        write_qa(Path(args.qa), "stats", vars(args), stats=stats)
    return 0


def cmd_auth(args: argparse.Namespace) -> int:
    """Show current credential state (source only, never plaintext)."""
    info = describe_credentials()
    print(f"NASA Earthdata credential state:")
    for k, v in info.items():
        mark = "OK" if v["available"] else "--"
        print(f"  [{mark}] {k:25s} source={v['source']:12s} available={v['available']}")
        if not v["available"]:
            print(f"         hint: {v['hint']}")
    print(f"\nHint: write your token + profile to ~/.geoskill/secrets.json")
    return 0


# ---------------------------------------------------------------------------
# Argparse
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="nasa-dataset-catalog",
        description=(
            "Search, browse, and download 52K+ NASA Earth science datasets. "
            "Combines the opengeos/NASA-Earth-Data offline catalog with live "
            "CMR / LP DAAC earthdata cloud / GES DISC endpoints."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG,
                   help=f"Offline catalog JSON path (default: {DEFAULT_CATALOG})")
    p.add_argument("--version", action="version", version=f"nasa-dataset-catalog {__version__} ({__phase__})")
    sub = p.add_subparsers(dest="command", required=True)

    def add_common(sp: argparse.ArgumentParser) -> None:
        sp.add_argument("--format", choices=["text", "json"], default="text",
                       help="Output format (default text)")
        sp.add_argument("--qa", metavar="PATH", default=None,
                       help="Write a JSON run-summary sidecar to PATH (e.g. --qa run.qa.json)")

    # auth
    sp = sub.add_parser("auth", help="Show current credential state")
    add_common(sp)
    sp.set_defaults(func=cmd_auth)

    # search
    sp = sub.add_parser("search", help="Search by keyword (offline catalog and/or live CMR)")
    sp.add_argument("keyword", help="Keyword to search (matches short_name/title/creator)")
    sp.add_argument("--offline", action="store_true", default=True,
                   help="Search offline catalog (default on)")
    sp.add_argument("--live", action="store_true", default=False,
                   help="Search live CMR collections (network required)")
    sp.add_argument("--provider", help="Filter by provider-id (e.g. LPDAAC, GES_DISC)")
    sp.add_argument("--limit", type=int, default=20, help="Max results (default 20)")
    add_common(sp)
    sp.set_defaults(func=cmd_search)

    # info
    sp = sub.add_parser("info", help="Show metadata for a short_name")
    sp.add_argument("short_name", help="Dataset short name (e.g. MOD11A1)")
    sp.add_argument("--live", action="store_true", default=False,
                   help="Also fetch live CMR entry (network required)")
    add_common(sp)
    sp.set_defaults(func=cmd_info)

    # granules
    sp = sub.add_parser("granules", help="List granules for a short_name")
    sp.add_argument("short_name", help="Dataset short name (e.g. MOD11A1)")
    sp.add_argument("--version", help="Dataset version (e.g. 061)")
    sp.add_argument("--temporal", help="YYYY-MM-DD,YYYY-MM-DD or ISO 8601 range")
    sp.add_argument("--bbox", type=float, nargs=4, metavar=("W", "S", "E", "N"),
                   help="Bounding box")
    sp.add_argument("--limit", type=int, default=20)
    sp.add_argument("--list-urls", metavar="FILE",
                   help="Write JSON of granule URLs to FILE (no download)")
    add_common(sp)
    sp.set_defaults(func=cmd_granules)

    # download
    sp = sub.add_parser("download", help="Download a single granule")
    sp.add_argument("--url", help="Direct download URL (overrides short_name search)")
    sp.add_argument("--short-name", help="Dataset short name (e.g. MOD11A1)")
    sp.add_argument("--version", help="Dataset version")
    sp.add_argument("--temporal", help="YYYY-MM-DD,YYYY-MM-DD")
    sp.add_argument("--bbox", type=float, nargs=4, metavar=("W", "S", "E", "N"))
    sp.add_argument("--output", "-o", help="Output file path")
    sp.add_argument("--max-bytes", type=int, default=None,
                   help="Stop after N bytes (testing/demo)")
    add_common(sp)
    sp.set_defaults(func=cmd_download)

    # stats
    sp = sub.add_parser("stats", help="Show catalog coverage stats")
    add_common(sp)
    sp.set_defaults(func=cmd_stats)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except KeyboardInterrupt:
        return 130
    except GeoSkillError as e:
        print(f"  error: {e}", file=sys.stderr)
        return exit_code_for(e)
    except Exception as e:
        print(f"  unexpected: {type(e).__name__}: {e}", file=sys.stderr)
        return 7


if __name__ == "__main__":
    sys.exit(main())
