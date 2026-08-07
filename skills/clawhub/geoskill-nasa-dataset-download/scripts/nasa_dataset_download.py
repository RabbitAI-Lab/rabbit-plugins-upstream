#!/usr/bin/env python
"""nasa-dataset-download — Download any NASA Earth observation dataset, end-to-end.

Phase 7.7 (2026-07-27).

Wraps the `earthaccess` library (NSIDC's official NASA Earthdata SDK) to
provide a one-command download experience:

  - ``search`` — list available granules for a dataset
  - ``download`` — bulk-download granules for a dataset (BBox + time window)
  - ``login`` — verify Earthdata credentials
  - ``urls`` — print all granule URLs (no download)
  - ``known`` — browse the bundled 52K offline catalog + alias map
  - ``info`` — show a dataset's CMR metadata + tip on how to download it

Credentials: resolved via vendored ``geoskill_core.credentials`` which
honours env vars / ~/.geoskill/secrets.json / ~/.netrc. Bearer token is
preferred (CMR + LP DAAC earthdata cloud + GES DISC); basic auth is the
fallback.

Built on top of the opengeos/NASA-Earth-Data 52,126-dataset catalog
(``known`` for browsing offline) and a curated 50-entry alias map so users
can search by description ("land surface temperature") instead of having
to memorise short_names (MOD11A1 etc.).

Exit codes (geoskill-core §2.2):
  0=success, 2=arg, 3=missing dep, 4=network, 5=no match,
  6=data validation, 7=processing, 130=interrupt.
"""
from __future__ import annotations

import argparse
import contextlib
import json
import os
import re
import sys
import time
import warnings
from pathlib import Path
from typing import Any

# earthaccess 0.18 emits FutureWarning every time we call g.size()
# (will be `g.size` attribute in 1.0).  We use it intentionally, so silence.
warnings.filterwarnings(
    "ignore",
    message=r".*DataGranule\.size.*",
    category=FutureWarning,
)
warnings.filterwarnings(
    "ignore",
    message=r".*DataCollection\.size.*",
    category=FutureWarning,
)

# Vendored geoskill-core helpers (also vendored via vendor.py)
_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))
try:
    from _geoskill_core.credentials import (  # type: ignore
        get_earthdata_token,
        get_earthdata_creds,
        describe_credentials,
    )
    from _geoskill_core.errors import GeoSkillError, to_exit_code as exit_code_for  # type: ignore
except ImportError:
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


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
DATA_DIR = SKILL_DIR / "data"
DEFAULT_CATALOG = DATA_DIR / "nasa_catalog.json"
ALIAS_PATH = DATA_DIR / "aliases.json"
OUTPUT_DIR = SKILL_DIR / "output"

# Mirror of nasa-dataset-catalog constants
CMR_SEARCH_URL = "https://cmr.earthdata.nasa.gov/search/granules.json"
EARTHDATA_LOGIN_URL = "https://urs.earthdata.nasa.gov"

__version__ = "0.2.0"
__phase__ = "Phase 7.7 (2026-07-27)"


# ---------------------------------------------------------------------------
# earthaccess wrapper
# ---------------------------------------------------------------------------


def _ensure_earthaccess():
    try:
        import earthaccess  # type: ignore
        return earthaccess
    except ImportError as e:
        raise GeoSkillError(
            "earthaccess not installed. Run: pip install earthaccess"
        ) from e


@contextlib.contextmanager
def _silence_earthaccess_warnings():
    """earthaccess 0.18's DataGranule.size() emits a FutureWarning that
    is harmless to us. Silence it for the duration of an operation.
    """
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message=r".*DataGranule\.size.*",
            category=FutureWarning,
        )
        warnings.filterwarnings(
            "ignore",
            message=r".*DataCollection\.size.*",
            category=FutureWarning,
        )
        yield


def login(strategy: str = "environment") -> Any:
    """Authenticate with NASA Earthdata.

    Strategies (in order of preference):
      - "environment" (default): use $EARTHDATA_USERNAME/$EARTHDATA_PASSWORD or $EARTHDATA_TOKEN
      - "netrc": use ~/.netrc
      - "interactive": prompt for credentials
    """
    ea = _ensure_earthaccess()
    # earthaccess 0.18+ login reads env vars directly; ensure they're set
    tok = get_earthdata_token()
    if tok and not os.environ.get("EARTHDATA_TOKEN"):
        os.environ["EARTHDATA_TOKEN"] = tok
    if not tok:
        u, p = get_earthdata_creds()
        if u and p:
            os.environ.setdefault("EARTHDATA_USERNAME", u)
            os.environ.setdefault("EARTHDATA_PASSWORD", p)
    try:
        auth = ea.login(strategy=strategy)
        return auth
    except Exception as e:
        raise GeoSkillError(f"Earthdata login failed: {e}") from e


def search_granules(
    short_name: str,
    *,
    version: str | None = None,
    temporal: tuple[str, str] | None = None,
    bbox: tuple[float, float, float, float] | None = None,
    count: int = 100,
    cloud_hosted: bool = False,
) -> list[Any]:
    """Search NASA CMR for granules using earthaccess.

    Args:
        short_name: e.g. 'MOD11A1', 'GPM_3IMERGHH', 'SENTINEL-1A_SLC'
        version: e.g. '061'
        temporal: (start, end) in 'YYYY-MM-DD' format
        bbox: (W, S, E, N) in WGS84
        count: max results
        cloud_hosted: if True, also fetch s3:// links (for AWS-hosted datasets)
    """
    ea = _ensure_earthaccess()
    kwargs: dict[str, Any] = {"short_name": short_name, "count": count}
    if version:
        kwargs["version"] = version
    if temporal:
        kwargs["temporal"] = temporal
    if bbox:
        kwargs["bounding_box"] = bbox
    # earthaccess 0.18 入口
    try:
        with _silence_earthaccess_warnings():
            results = ea.search_data(**kwargs)  # type: ignore
    except AttributeError:
        # 0.18+ 可能用 search_granules
        try:
            with _silence_earthaccess_warnings():
                results = ea.search_granules(**kwargs)  # type: ignore
        except Exception as e:
            raise GeoSkillError(f"search failed: {e}") from e
    return list(results)


def granule_info(g: Any) -> dict[str, Any]:
    """Extract the displayable fields from a DataGranule in a way that
    works with earthaccess 0.18 and is forward-compatible with 1.0.

    Returns a dict with: granule_id, size_mb, day_night, production_dt,
    temporal, data_links, cloud_hosted, umm.
    """
    out: dict[str, Any] = {
        "granule_id": "",
        "size_mb": None,
        "day_night": "",
        "production_dt": "",
        "temporal": "",
        "data_links": [],
        "cloud_hosted": False,
    }
    # granule_id (CMR GranuleUR) — earthaccess 0.18 stores it in g['umm']
    try:
        umm = g["umm"] if hasattr(g, "__getitem__") else {}
        if isinstance(umm, dict):
            out["granule_id"] = umm.get("GranuleUR", "") or ""
            dg = umm.get("DataGranule")
            if isinstance(dg, list):
                dg = dg[0] if dg else {}
            if isinstance(dg, dict):
                out["production_dt"] = dg.get("ProductionDateTime", "") or ""
                out["day_night"] = dg.get("DayNightFlag", "") or ""
                ids = dg.get("Identifiers") or []
                if ids and isinstance(ids[0], dict):
                    out["granule_id"] = out["granule_id"] or ids[0].get("Identifier", "")
            te = umm.get("TemporalExtent")
            if isinstance(te, dict):
                rng = te.get("RangeDateTime") or {}
                out["temporal"] = (
                    f"{rng.get('BeginningDateTime', '')}/{rng.get('EndingDateTime', '')}"
                )
    except Exception:
        pass
    # size — earthaccess 0.18 g.size() returns MB; 1.0 will be g.size attribute
    try:
        sz = g.size()  # type: ignore
        if isinstance(sz, (int, float)):
            out["size_mb"] = round(float(sz), 2)
    except Exception:
        # Future-compatible: 1.0 may use attribute
        try:
            sz = g.size
            if isinstance(sz, (int, float)):
                out["size_mb"] = round(float(sz), 2)
        except Exception:
            pass
    # data_links — earthaccess 0.18 returns list[str]
    try:
        links = g.data_links()  # type: ignore
        if isinstance(links, list):
            out["data_links"] = [str(u) for u in links]
        else:
            out["data_links"] = [str(links)]
    except Exception:
        pass
    # cloud_hosted
    try:
        out["cloud_hosted"] = bool(g.cloud_hosted)
    except Exception:
        pass
    return out


def download_files(
    granules: list[Any],
    out_dir: Path,
    *,
    max_files: int | None = None,
    verbose: bool = True,
) -> list[Path]:
    """Download granule files to out_dir.

    The optional ``max_files`` slices the *granule list* before calling
    earthaccess so we never download more than the user asked for.
    """
    if max_files is not None:
        granules = granules[:max_files]
    ea = _ensure_earthaccess()
    out_dir.mkdir(parents=True, exist_ok=True)
    with _silence_earthaccess_warnings():
        paths = ea.download(granules, local_path=str(out_dir))  # type: ignore
    if isinstance(paths, (list, tuple)):
        out = [Path(p) for p in paths]
    elif isinstance(paths, set):
        out = [Path(p) for p in sorted(paths)]
    else:
        out = [Path(p) for p in paths]
    if verbose:
        total_bytes = sum(p.stat().st_size for p in out if p.is_file())
        print(f"  downloaded {len(out)} file(s) totaling {total_bytes:,} bytes to {out_dir}")
    return out


# ---------------------------------------------------------------------------
# Catalog (offline) - same as nasa-dataset-catalog
# ---------------------------------------------------------------------------


def load_catalog(path: Path = DEFAULT_CATALOG) -> list[dict]:
    """Load the offline NASA catalog (52,126 records from opengeos/NASA-Earth-Data)."""
    if not path.is_file():
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        return []


def search_catalog(
    catalog: list[dict],
    keyword: str,
    *,
    provider: str | None = None,
    limit: int = 20,
) -> list[dict]:
    """Search the offline catalog by keyword (multi-word AND)."""
    tokens = [t.lower().strip() for t in re.split(r"[\s,]+", keyword) if t.strip()]
    if not tokens:
        return []
    results: list[dict] = []
    for rec in catalog:
        sn = (rec.get("ShortName") or "").strip()
        title = (rec.get("EntryTitle") or "").strip()
        creator = (rec.get("Creator") or "").strip()
        publisher = (rec.get("Publisher") or "").strip()
        provider_id = (rec.get("provider-id") or "").strip()
        if provider and provider_id.lower() != provider.lower():
            continue
        hay = " ".join([sn, title, creator, publisher]).lower()
        # AND match: every token must appear (substring)
        if all(tok in hay for tok in tokens):
            results.append({
                "short_name": sn,
                "title": title,
                "provider": provider_id,
                "version": (rec.get("Version") or "").strip(),
                "doi": (rec.get("DOI") or "").strip(),
            })
            if len(results) >= limit:
                break
    return results


def load_aliases(path: Path = ALIAS_PATH) -> dict[str, list[str]]:
    """Load the alias map (description phrase -> [short_names])."""
    if not path.is_file():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            return {}
        # Drop meta keys starting with _
        return {k.lower().strip(): list(v) for k, v in data.items() if not k.startswith("_") and isinstance(v, list)}
    except (OSError, json.JSONDecodeError):
        return {}


def resolve_alias(keyword: str, aliases: dict[str, list[str]] | None = None) -> list[str] | None:
    """If `keyword` matches an alias phrase (full or prefix), return the
    short_name list.  Returns None when no alias matched so callers can
    fall back to literal short_name search.
    """
    if aliases is None:
        aliases = load_aliases()
    if not keyword:
        return None
    k = keyword.lower().strip()
    if k in aliases:
        return aliases[k]
    # Try the longest prefix match (e.g. "MODIS land surface temperature"
    # matches the "land surface temperature" alias when "MODIS" is the
    # first token).
    tokens = k.split()
    for n in range(len(tokens), 0, -1):
        candidate = " ".join(tokens[-n:])  # tail n tokens
        if candidate in aliases:
            return aliases[candidate]
    return None


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------


def cmd_login(args: argparse.Namespace) -> int:
    """Authenticate with Earthdata and report credential state."""
    info = describe_credentials()
    print("NASA Earthdata credential state:")
    for k, v in info.items():
        mark = "OK" if v["available"] else "--"
        print(f"  [{mark}] {k:25s} source={v['source']:12s} available={v['available']}")
        if not v["available"]:
            print(f"         hint: {v['hint']}")
    print()
    print("Attempting live login with earthaccess.login()...")
    try:
        auth = login()
        print(f"  OK: earthaccess.authenticated={getattr(auth, 'authenticated', '?')}")
    except GeoSkillError as e:
        print(f"  ERR: {e}")
        return 3
    if args.qa:
        write_qa(Path(args.qa), "login", vars(args))
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    """List available granules for a dataset.

    If `--alias-resolve` is on (default) and the user passed a description
    like "land surface temperature" instead of a short_name, we look it
    up in the alias map and print a hint suggesting the canonical
    short_name(s) to use.
    """
    short_name = args.short_name
    if args.alias_resolve and not args.version:
        aliases = load_aliases()
        hit = resolve_alias(short_name, aliases)
        if hit:
            print(
                f"  hint: '{short_name}' matched the alias map; "
                f"try the canonical short_name(s): {', '.join(hit)}",
                file=sys.stderr,
            )
    print(f"Searching {short_name} (version={args.version or 'latest'})...")
    temporal = (args.temporal_start, args.temporal_end) if args.temporal_start else None
    bbox = tuple(args.bbox) if args.bbox else None
    try:
        granules = search_granules(
            short_name,
            version=args.version,
            temporal=temporal,
            bbox=bbox,
            count=args.count,
        )
    except GeoSkillError as e:
        print(f"  error: {e}", file=sys.stderr)
        return 5
    print(f"  found {len(granules)} granule(s)")
    if not granules:
        _print_no_match_hint(short_name, args.temporal_start, args.temporal_end, args.bbox)
        if args.qa:
            write_qa(Path(args.qa), "search", vars(args), n_granules=0)
        return 5
    if args.format == "json":
        out = [granule_info(g) for g in granules]
        print(json.dumps(out, indent=2, default=str))
    else:
        for i, g in enumerate(granules):
            info = granule_info(g)
            gid = info["granule_id"] or "(no-id)"
            sz = f"{info['size_mb']:.1f}MB" if info["size_mb"] is not None else "?MB"
            dn = info["day_night"] or "-"
            print(f"  [{i+1:3d}] {gid:48s}  {sz:>8s}  {dn:5s}  {info['temporal']}")
    if args.qa:
        write_qa(Path(args.qa), "search", vars(args), n_granules=len(granules))
    return 0


def _print_no_match_hint(short_name: str, ts: str | None, te: str | None, bbox) -> None:
    """Print a friendly hint when search returns 0 results."""
    aliases = load_aliases()
    print("  no granules found. Possible causes:", file=sys.stderr)
    print(f"    - '{short_name}' may be a description, not a short_name", file=sys.stderr)
    if ts and te and ts == te:
        print(f"    - the date {ts} may be out of range for this dataset", file=sys.stderr)
    if not ts:
        print("    - no temporal window given; some datasets require one", file=sys.stderr)
    if bbox:
        print(f"    - bbox {bbox} may not intersect the dataset's coverage", file=sys.stderr)
    if short_name.lower() in aliases:
        canon = ", ".join(aliases[short_name.lower()][:3])
        print(
            f"    - '{short_name}' IS an alias. Use the canonical short_name instead, e.g.: {canon}",
            file=sys.stderr,
        )
    else:
        print(
            f"    - try `nasa-dataset-download known \"{short_name}\"` to find a similar short_name",
            file=sys.stderr,
        )
        print(
            f"    - or check spelling: e.g. MOD11A1 (not MOD11A-1), GPM_3IMERGHH (not IMERG)",
            file=sys.stderr,
        )


def cmd_download(args: argparse.Namespace) -> int:
    """Bulk-download granules to a local directory."""
    print(f"Logging in...")
    try:
        login()
    except GeoSkillError as e:
        print(f"  login error: {e}", file=sys.stderr)
        return 4
    print(f"Searching {args.short_name} (version={args.version or 'latest'})...")
    temporal = (args.temporal_start, args.temporal_end) if args.temporal_start else None
    bbox = tuple(args.bbox) if args.bbox else None
    try:
        granules = search_granules(
            args.short_name,
            version=args.version,
            temporal=temporal,
            bbox=bbox,
            count=args.count,
        )
    except GeoSkillError as e:
        print(f"  error: {e}", file=sys.stderr)
        return 5
    if not granules:
        print(f"  no granules found for {args.short_name}", file=sys.stderr)
        _print_no_match_hint(args.short_name, args.temporal_start, args.temporal_end, args.bbox)
        return 5
    planned = len(granules) if args.max_files is None else min(len(granules), args.max_files)
    print(f"  found {len(granules)} granule(s); will download {planned}")
    if args.dry_run:
        print("  --dry-run set; listing URLs only:")
        for g in granules[:planned]:
            info = granule_info(g)
            print(f"    {info['granule_id']}  {info['size_mb']}MB  {info['data_links'][0] if info['data_links'] else ''}")
        return 0
    out_dir = Path(args.output_dir) if args.output_dir else OUTPUT_DIR / args.short_name
    print(f"Downloading to {out_dir}...")
    t0 = time.time()
    try:
        paths = download_files(granules, out_dir, max_files=args.max_files)
    except Exception as e:
        print(f"  download error: {e}", file=sys.stderr)
        return 4
    elapsed = time.time() - t0
    total = sum(p.stat().st_size for p in paths if p.is_file())
    print(f"  done in {elapsed:.1f}s. {len(paths)} file(s), {total:,} bytes total")
    if args.qa:
        write_qa(
            Path(args.qa), "download", vars(args),
            n_granules=len(granules), n_files=len(paths),
            output_dir=str(out_dir), total_bytes=total, elapsed_s=elapsed,
        )
    return 0


def cmd_urls(args: argparse.Namespace) -> int:
    """Print all granule URLs without downloading."""
    print(f"Logging in...")
    try:
        login()
    except GeoSkillError as e:
        print(f"  login error: {e}", file=sys.stderr)
        return 4
    print(f"Searching {args.short_name}...")
    temporal = (args.temporal_start, args.temporal_end) if args.temporal_start else None
    bbox = tuple(args.bbox) if args.bbox else None
    try:
        granules = search_granules(
            args.short_name, version=args.version,
            temporal=temporal, bbox=bbox, count=args.count,
        )
    except GeoSkillError as e:
        print(f"  error: {e}", file=sys.stderr)
        return 5
    if not granules:
        _print_no_match_hint(args.short_name, args.temporal_start, args.temporal_end, args.bbox)
        return 5
    rows: list[dict] = []
    for g in granules:
        info = granule_info(g)
        rows.append(info)
        for u in info["data_links"]:
            print(f"  {u[:150]}")
    print(f"  {sum(len(r['data_links']) for r in rows)} URL(s) across {len(rows)} granule(s)")
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps({"short_name": args.short_name, "granules": rows}, indent=2, default=str),
            encoding="utf-8",
        )
        print(f"  saved to {out}")
    if args.qa:
        write_qa(Path(args.qa), "urls", vars(args), n_granules=len(rows), n_urls=sum(len(r['data_links']) for r in rows))
    return 0


def cmd_known(args: argparse.Namespace) -> int:
    """Browse the offline 52K catalog + alias map."""
    catalog = load_catalog()
    if not catalog:
        print(f"  offline catalog not found at {DEFAULT_CATALOG}", file=sys.stderr)
        return 3
    print(f"Loaded {len(catalog):,} records from {DEFAULT_CATALOG.name}")
    # Alias expansion first (so the user gets short_name hints)
    aliases = load_aliases()
    alias_hit = resolve_alias(args.keyword, aliases)
    if alias_hit:
        print(f"\n  alias match: '{args.keyword}' -> {', '.join(alias_hit)}")
    results = search_catalog(catalog, args.keyword, provider=args.provider, limit=args.limit)
    print(f"\n  {len(results)} match(es) for '{args.keyword}':")
    for r in results:
        print(f"  - {r['short_name']:30s} | {r['provider']:18s} | {r['title'][:60]}")
    if not results and alias_hit is None:
        print(
            f"  hint: try a shorter phrase (one or two keywords), e.g. "
            f"`known MODIS` or `known precipitation`",
            file=sys.stderr,
        )
    if args.qa:
        write_qa(
            Path(args.qa), "known", vars(args),
            n_results=len(results), alias_hit=alias_hit or [],
        )
    return 0


# ---------------------------------------------------------------------------
# QA + argparse
# ---------------------------------------------------------------------------


def write_qa(path: Path, command: str, args: dict, **extras) -> None:
    if path is None:
        return
    safe_args: dict = {}
    for k, v in (args or {}).items():
        if k in ("func", "command") or callable(v):
            continue
        if isinstance(v, Path):
            safe_args[k] = str(v)
        elif isinstance(v, (list, tuple)):
            safe_args[k] = [str(x) if isinstance(x, Path) else x for x in v]
        else:
            safe_args[k] = v
    payload = {
        "skill": "nasa-dataset-download",
        "version": __version__,
        "command": command,
        "args": safe_args,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "credentials": describe_credentials(),
        **extras,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def add_common(sp: argparse.ArgumentParser) -> None:
    sp.add_argument("--format", choices=["text", "json"], default="text")
    sp.add_argument("--qa", metavar="PATH", default=None,
                   help="Write a JSON run-summary sidecar to PATH")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="nasa-dataset-download",
        description=(
            "Download any NASA Earth observation dataset (HDF / NetCDF / GeoTIFF) "
            "using the official earthaccess library. Supports MODIS, VIIRS, GPM, "
            "Sentinel, SMAP, ASTER, etc."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--version", action="version",
                   version=f"nasa-dataset-download {__version__} ({__phase__})")
    sub = p.add_subparsers(dest="command", required=True)

    # login
    sp = sub.add_parser("login", help="Authenticate with Earthdata")
    add_common(sp)
    sp.set_defaults(func=cmd_login)

    # search
    sp = sub.add_parser("search", help="List available granules")
    sp.add_argument("short_name", help="Dataset short name (e.g. MOD11A1) — also accepts description like 'land surface temperature' (will print alias hint)")
    sp.add_argument("--version", help="Dataset version (e.g. 061)")
    sp.add_argument("--temporal-start", help="Start date YYYY-MM-DD")
    sp.add_argument("--temporal-end", help="End date YYYY-MM-DD")
    sp.add_argument("--bbox", type=float, nargs=4, metavar=("W", "S", "E", "N"))
    sp.add_argument("--count", type=int, default=20)
    sp.add_argument("--no-alias-resolve", dest="alias_resolve", action="store_false",
                   help="Disable alias-map hinting when short_name looks like a description")
    sp.set_defaults(alias_resolve=True)
    add_common(sp)
    sp.set_defaults(func=cmd_search)

    # download
    sp = sub.add_parser("download", help="Bulk-download granules")
    sp.add_argument("short_name", help="Dataset short name (e.g. MOD11A1)")
    sp.add_argument("--version", help="Dataset version")
    sp.add_argument("--temporal-start", help="Start date YYYY-MM-DD")
    sp.add_argument("--temporal-end", help="End date YYYY-MM-DD")
    sp.add_argument("--bbox", type=float, nargs=4, metavar=("W", "S", "E", "N"))
    sp.add_argument("--count", type=int, default=10)
    sp.add_argument("--max-files", type=int, default=None,
                   help="Max files to download (testing) — limits downloads, not just the report")
    sp.add_argument("--output-dir", "-o", help="Output directory")
    sp.add_argument("--dry-run", action="store_true",
                   help="Show what would be downloaded without actually downloading")
    add_common(sp)
    sp.set_defaults(func=cmd_download)

    # urls
    sp = sub.add_parser("urls", help="Print granule URLs (no download)")
    sp.add_argument("short_name")
    sp.add_argument("--version")
    sp.add_argument("--temporal-start")
    sp.add_argument("--temporal-end")
    sp.add_argument("--bbox", type=float, nargs=4, metavar=("W", "S", "E", "N"))
    sp.add_argument("--count", type=int, default=20)
    sp.add_argument("--out", help="Write JSON to file")
    add_common(sp)
    sp.set_defaults(func=cmd_urls)

    # known (offline catalog browse)
    sp = sub.add_parser("known", help="Browse 52K offline catalog")
    sp.add_argument("keyword", help="Keyword to search")
    sp.add_argument("--provider", help="Filter by provider")
    sp.add_argument("--limit", type=int, default=20)
    add_common(sp)
    sp.set_defaults(func=cmd_known)

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
