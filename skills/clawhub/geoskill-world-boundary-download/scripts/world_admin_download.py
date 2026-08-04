"""CLI entry point for the world-boundary-download skill.

Examples
--------

    # List which admin levels are available for China on the default source:
    python world_admin_download.py levels --iso CHN

    # Show metadata + bbox + area for China ADM1:
    python world_admin_download.py info --iso CHN --level ADM1

    # Download China ADM1 as a zipped Shapefile:
    python world_admin_download.py country --iso CHN --level ADM1 --format shp --out ./chn_adm1.zip

    # Download the United States ADM2 as GeoJSON, clipped to a bbox:
    python world_admin_download.py region --iso USA --level ADM2 --bbox -125,24,-66,49 --format geojson --out ./usa_south.geojson

    # Search for a country by Chinese / English name:
    python world_admin_download.py search 美利坚

    # Force a specific source (skip the fallback chain):
    python world_admin_download.py country --iso CHN --level ADM0 --source gadm --format shp --out ./chn_gadm.zip
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Optional

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from core import (
    cache as cache_mod,
    format as fmt_mod,
    geoboundaries,
    geometry,
    gadm,
    natural_earth,
    sources,
)
from core.exceptions import (
    DataSourceError,
    FormatError,
    NetworkError,
    ResolutionError,
    WorldBoundryError,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _emit(payload: Any, *, plain: bool) -> int:
    if plain and not isinstance(payload, (list, dict)):
        print(payload)
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def _err(msg: str, *, code: int = 1) -> int:
    print(f"error: {msg}", file=sys.stderr)
    return code


__version__ = "0.1.0"
USER_AGENT = f"world-boundary-download/{__version__}"


def write_qa_summary(qa_path, *, skill, command, args, payload):
    """Write a JSON run-summary sidecar to qa_path (Phase 5 optimization).

    The payload is the dict we would normally emit via _emit(); we copy it
    and add timestamp / version / command so the sidecar is self-contained
    for QA / regression testing.
    """
    import json as _json
    from datetime import datetime as _dt, timezone as _tz

    summary = dict(payload) if isinstance(payload, dict) else {"result": payload}
    summary.setdefault("skill", skill)
    summary["command"] = command
    summary["version"] = __version__
    summary["user_agent"] = USER_AGENT
    summary["timestamp"] = _dt.now(_tz.utc).isoformat()
    # Add any input flags the QA consumer might want.
    for flag in ("iso", "name", "level", "format", "source", "simplified",
                 "bbox", "isos", "out", "expand_km", "no_cache"):
        if hasattr(args, flag):
            summary.setdefault(flag, getattr(args, flag))
    qa_p = Path(qa_path)
    qa_p.parent.mkdir(parents=True, exist_ok=True)
    with open(qa_p, "w", encoding="utf-8") as f:
        _json.dump(summary, f, ensure_ascii=False, indent=2)
    return qa_p


def _resolve_iso(args) -> str:
    """Resolve --name / --iso into a 3-letter ISO code, raising on failure."""

    if args.iso:
        iso = args.iso.strip()
        if len(iso) == 2:
            # Convert alpha-2 -> alpha-3 via pycountry.
            from core.iso_resolver import _pycountry_lookup
            m = _pycountry_lookup(iso)
            if not m:
                raise ResolutionError(f"unknown alpha-2 code: {iso}")
            return m.iso3
        if len(iso) == 3:
            return iso.upper()
        # Fall through to name resolution.
    if args.name:
        from core.iso_resolver import resolve
        return resolve(args.name).iso3
    raise ResolutionError("must provide --iso or --name")


def _build_cache(args) -> cache_mod.HttpCache:
    if args.cache_dir:
        return cache_mod.HttpCache(Path(args.cache_dir))
    return cache_mod.HttpCache()


def _format_arg(args) -> str:
    return fmt_mod.normalize_format(args.format)


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------

def cmd_search(args) -> int:
    from core.iso_resolver import search

    try:
        results = search(args.keyword, limit=args.limit)
    except Exception as e:
        return _err(str(e))
    out = [
        {**m.to_dict(), "score": round(m.score, 3)}
        for m in results
    ]
    return _emit({"count": len(out), "results": out}, plain=args.plain)


def cmd_resolve_iso(args) -> int:
    from core.iso_resolver import get_display, resolve

    try:
        if args.iso:
            m = get_display(args.iso)
        else:
            m = resolve(args.name)
    except ResolutionError as e:
        return _err(str(e))
    return _emit({**m.to_dict(), "score": m.score}, plain=args.plain)


def cmd_list_sources(args) -> int:
    out = []
    for name, src in sources.REGISTRY.items():
        out.append(
            {
                "name": name,
                "description": src.description,
            }
        )
    return _emit({"sources": out, "default_chain": sources.DEFAULT_FALLBACK_CHAIN}, plain=args.plain)


def cmd_levels(args) -> int:
    try:
        iso = _resolve_iso(args)
    except ResolutionError as e:
        return _err(str(e))
    cache = _build_cache(args)

    if args.source:
        try:
            src = sources.get_source(args.source)
            levels = src.list_levels(iso, cache=cache)
        except DataSourceError as e:
            return _err(str(e))
        return _emit(
            {"iso3": iso, "source": args.source, "levels": levels}, plain=args.plain
        )

    # All sources
    out: dict[str, list[str]] = {}
    for name, src in sources.REGISTRY.items():
        try:
            out[name] = src.list_levels(iso, cache=cache)
        except Exception as e:
            out[name] = [f"error: {e}"]
    return _emit({"iso3": iso, "levels_by_source": out}, plain=args.plain)


def cmd_info(args) -> int:
    try:
        iso = _resolve_iso(args)
    except ResolutionError as e:
        return _err(str(e))
    cache = _build_cache(args)

    if args.source and args.source != "geoboundaries":
        # For non-default sources we don't have rich metadata; return basic.
        try:
            levels = sources.get_source(args.source).list_levels(iso, cache=cache)
        except DataSourceError as e:
            return _err(str(e))
        return _emit(
            {
                "iso3": iso,
                "level": args.level,
                "source": args.source,
                "available": args.level.upper() in [l.upper() for l in levels],
                "license": "see source",
            },
            plain=args.plain,
        )

    # Default: geoboundaries.
    try:
        meta = geoboundaries.fetch_metadata(iso, args.level, cache=cache)
    except DataSourceError as e:
        return _err(str(e))
    if meta is None:
        return _err(
            f"geoBoundaries has no {args.level} boundary for {iso}",
        )

    flat = geoboundaries.flatten_meta(meta)
    # Optional bbox + area.
    try:
        import geopandas as gpd
        path = geoboundaries.download_zip(iso, args.level, cache=cache)
        with _open_zip_gdf(path) as gdf:
            bb = geometry.bbox_of_gdf(gdf)
            flat["bbox_wgs84"] = list(bb)
            if args.expand_km and args.expand_km > 0:
                bb_exp = geometry.expand_bbox(bb, args.expand_km)
                flat["bbox_wgs84_expanded"] = list(bb_exp)
            flat["area_km2"] = round(geometry.area_km2(gdf), 3)
            if args.expand_km and args.expand_km > 0:
                # Compute expanded area by creating a bbox polygon and clipping.
                from shapely.geometry import box as _box
                expanded = gdf.clip(_box(*bb_exp))
                flat["area_km2_expanded"] = round(geometry.area_km2(expanded), 3)
            flat["feature_count"] = int(len(gdf))
    except Exception as e:
        flat["bbox_wgs84_error"] = str(e)
    return _emit(flat, plain=args.plain)


def cmd_bbox(args) -> int:
    try:
        iso = _resolve_iso(args)
    except ResolutionError as e:
        return _err(str(e))
    cache = _build_cache(args)
    try:
        path = geoboundaries.download_zip(iso, args.level, cache=cache)
    except DataSourceError as e:
        return _err(str(e))

    with _open_zip_gdf(path) as gdf:
        bb = geometry.bbox_of_gdf(gdf)
        out: dict[str, Any] = {"iso3": iso, "level": args.level, "bbox_wgs84": list(bb)}
        if args.expand_km and args.expand_km > 0:
            bb_exp = geometry.expand_bbox(bb, args.expand_km)
            out["bbox_wgs84_expanded"] = list(bb_exp)
        out["area_km2"] = round(geometry.area_km2(gdf), 3)
    return _emit(out, plain=args.plain)


def cmd_country(args) -> int:
    try:
        iso = _resolve_iso(args)
    except ResolutionError as e:
        return _err(str(e))
    cache = _build_cache(args)
    try:
        result = sources.fetch(
            iso,
            args.level,
            cache=cache,
            source=args.source,
            simplified=args.simplified,
        )
    except DataSourceError as e:
        return _err(str(e))

    out_path = _resolve_out_path(args, iso, args.level, source=result.source)
    return _convert_and_report(
        result.path,
        out_path,
        args,
        extra={"iso3": iso, "level": args.level, "source": result.source},
        command="country",
    )


def cmd_region(args) -> int:
    """Like country, but clips the boundary to a bbox before saving."""

    try:
        iso = _resolve_iso(args)
        bbox = geometry.parse_bbox(args.bbox)
    except (ResolutionError, ValueError) as e:
        return _err(str(e))
    cache = _build_cache(args)
    try:
        result = sources.fetch(
            iso,
            args.level,
            cache=cache,
            source=args.source,
            simplified=args.simplified,
        )
    except DataSourceError as e:
        return _err(str(e))

    # Read the input into a GDF, clip, write.
    fmt = _format_arg(args)
    out_path = _resolve_out_path(args, iso, args.level, suffix_extra="_clipped", source=result.source)
    try:
        gdf = fmt_mod.read_input(result.path)
        from core.geometry import clip_gdf
        gdf = clip_gdf(gdf, bbox)
        if len(gdf) == 0:
            return _err(f"no features in bbox {bbox} for {iso} {args.level}")
        written = fmt_mod.write_output(gdf, out_path, fmt)
    except (FormatError, ValueError) as e:
        return _err(str(e))

    payload = {
        "ok": True,
        "saved": str(written),
        "size_bytes": written.stat().st_size,
        "format": fmt,
        "source": result.source,
        "iso3": iso,
        "level": args.level,
        "bbox": list(bbox),
        "feature_count": int(len(gdf)),
    }
    if getattr(args, "qa", None):
        write_qa_summary(args.qa, skill="world-boundary-download", command="region",
                         args=args, payload=payload)
        payload["qa_path"] = str(args.qa)
    return _emit(payload, plain=args.plain)


def cmd_multi(args) -> int:
    """Download the same ADM level for several countries, concatenate into one file."""

    cache = _build_cache(args)
    isos = [x.strip().upper() for x in args.isos.split(",") if x.strip()]
    if not isos:
        return _err("--isos must list at least one ISO 3 code (comma-separated)")

    fmt = _format_arg(args)
    gdfs = []
    used_sources: list[str] = []
    failures: list[str] = []
    for iso in isos:
        try:
            result = sources.fetch(iso, args.level, cache=cache, source=args.source)
            used_sources.append(f"{iso}:{result.source}")
            gdf = fmt_mod.read_input(result.path)
            gdf["source_iso3"] = iso
            gdfs.append(gdf)
        except Exception as e:
            failures.append(f"{iso}: {e}")

    if not gdfs:
        return _err(f"all countries failed: {failures}")

    combined = _concat(gdfs)

    out_path = _resolve_out_path(args, "multi", args.level, suffix_extra="_" + "-".join(isos), source=args.source)
    try:
        written = fmt_mod.write_output(combined, out_path, fmt)
    except FormatError as e:
        return _err(str(e))

    payload = {
        "ok": True,
        "saved": str(written),
        "size_bytes": written.stat().st_size,
        "format": fmt,
        "level": args.level,
        "countries": isos,
        "sources": used_sources,
        "feature_count": int(len(combined)),
        "failures": failures,
    }
    if getattr(args, "qa", None):
        write_qa_summary(args.qa, skill="world-boundary-download", command="multi",
                         args=args, payload=payload)
        payload["qa_path"] = str(args.qa)
    return _emit(payload, plain=args.plain)


def cmd_all_levels(args) -> int:
    """Download every available ADM level for a country."""

    try:
        iso = _resolve_iso(args)
    except ResolutionError as e:
        return _err(str(e))
    cache = _build_cache(args)

    if args.source:
        chain = [args.source]
    else:
        chain = sources.DEFAULT_FALLBACK_CHAIN

    saved = []
    errors = []
    for src_name in chain:
        try:
            src = sources.get_source(src_name)
            levels = src.list_levels(iso, cache=cache)
        except Exception as e:
            errors.append(f"{src_name}: list failed: {e}")
            continue
        for level in levels:
            try:
                path = src.fetch(iso, level, cache=cache, simplified=args.simplified)
                fmt = _format_arg(args)
                out_path = _resolve_out_path(args, iso, level, suffix_extra=f"_{src_name}")  # noqa: already includes source
                written = fmt_mod.convert(path, out_path, fmt)
                saved.append({"level": level, "source": src_name, "saved": str(written)})
            except Exception as e:
                errors.append(f"{src_name} {level}: {e}")
        if saved:
            break  # first source that produced something wins
    if not saved:
        return _err(f"no level could be downloaded: {errors}")

    payload = {"ok": True, "iso3": iso, "saved": saved, "errors": errors}
    if getattr(args, "qa", None):
        write_qa_summary(args.qa, skill="world-boundary-download", command="all-levels",
                         args=args, payload=payload)
        payload["qa_path"] = str(args.qa)
    return _emit(payload, plain=args.plain)


def cmd_cache_clear(args) -> int:
    cache = _build_cache(args)
    n = cache.clear()
    return _emit({"cleared_files": n}, plain=args.plain)


def cmd_cache_info(args) -> int:
    cache = _build_cache(args)
    return _emit(
        {
            "root": str(cache.root),
            "cached_items": len(cache._index),
            "size_bytes": cache.size_bytes(),
        },
        plain=args.plain,
    )


# ---------------------------------------------------------------------------
# Helpers used by subcommands
# ---------------------------------------------------------------------------

def _open_zip_gdf(path: Path):
    """Context-manager-like helper: returns a GeoDataFrame for a zip/geojson path."""

    gdf = fmt_mod.read_input(path)
    return _NullContext(gdf)


class _NullContext:
    """Tiny stand-in for contextlib.nullcontext that returns a value from __enter__."""

    def __init__(self, value):
        self.value = value

    def __enter__(self):
        return self.value

    def __exit__(self, *args):
        return False


def _concat(gdfs):
    import pandas as pd
    import geopandas as gpd
    return gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True), crs="EPSG:4326")


def _resolve_out_path(
    args,
    iso: str,
    level: str,
    *,
    suffix_extra: str = "",
    source: Optional[str] = None,
) -> Path:
    """Resolve --out into a concrete path with the correct extension.

    If the caller passed --out, that path is authoritative (we still
    append the right extension if the user did not provide one).

    Otherwise we build a default name of the form
    ``<iso>_<level>[_<extra>][_<source>].<ext>``. Including the source
    in the default name avoids silent overwrites when the same ISO/level
    is downloaded from different data sources in a single session.
    """

    suffix = fmt_mod.OUTPUT_SUFFIX[fmt_mod.normalize_format(args.format)]

    if args.out:
        p = Path(args.out)
        # --out is a directory? write into it.
        if p.is_dir():
            base = f"{iso}_{level}{suffix_extra}"
            if source and source != "geoboundaries":
                base = f"{base}_{source}"
            return p / (base + suffix)
        # No suffix provided? add the right one.
        if not p.suffix:
            return p.with_name(p.name + suffix)
        return p

    # No --out: build a deterministic default name.
    base = f"{iso}_{level}{suffix_extra}"
    if source and source != "geoboundaries":
        base = f"{base}_{source}"
    return Path(base + suffix)


def _convert_and_report(in_path: Path, out_path: Path, args, *, extra: dict, command: str = "country") -> int:
    fmt = _format_arg(args)
    try:
        if args.format and args.format.lower() in ("shp", "shapefile", "shape", "shp.zip"):
            # Special-case: if the input is already a zip with the SHP set,
            # just copy it instead of round-tripping through geopandas.
            if _input_already_shp_zip(in_path):
                out_path = out_path.with_suffix(".zip")
                out_path.parent.mkdir(parents=True, exist_ok=True)
                import shutil
                shutil.copy2(in_path, out_path)
                payload = {
                    "ok": True,
                    "saved": str(out_path),
                    "size_bytes": out_path.stat().st_size,
                    "format": "shp",
                    "passthrough": True,
                    **extra,
                }
                if getattr(args, "qa", None):
                    write_qa_summary(args.qa, skill="world-boundary-download", command=command,
                                     args=args, payload=payload)
                    payload["qa_path"] = str(args.qa)
                return _emit(payload, plain=args.plain)
        written = fmt_mod.convert(in_path, out_path, fmt)
    except (FormatError, ValueError) as e:
        return _err(str(e))

    payload = {
        "ok": True,
        "saved": str(written),
        "size_bytes": written.stat().st_size,
        "format": fmt,
        **extra,
    }
    if getattr(args, "qa", None):
        write_qa_summary(args.qa, skill="world-boundary-download", command=command,
                         args=args, payload=payload)
        payload["qa_path"] = str(args.qa)
    return _emit(payload, plain=args.plain)


def _input_already_shp_zip(p: Path) -> bool:
    if not p.suffix.lower() == ".zip":
        return False
    try:
        import zipfile
        with zipfile.ZipFile(p) as zf:
            return any(n.lower().endswith(".shp") for n in zf.namelist())
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="world_admin_download",
        description="Download administrative boundary vector data for any country.",
    )
    p.add_argument("--cache-dir", help="override cache root")
    p.add_argument(
        "--source",
        choices=list(sources.REGISTRY),
        help="pin a data source (skips fallback chain)",
    )
    p.add_argument(
        "--format",
        default="shp",
        help="output format: shp (default), geojson, gpkg, topojson",
    )
    p.add_argument(
        "--out",
        help="output path (file or directory); suffix auto-appended if missing",
    )
    p.add_argument(
        "--simplified",
        action="store_true",
        help="use the simplified geometry (geoBoundaries only; smaller files)",
    )
    p.add_argument(
        "--no-cache",
        action="store_true",
        help="force re-download (skip cache lookup)",
    )
    p.add_argument(
        "--expand-km",
        type=float,
        default=0.0,
        help="expand bbox by N km (info / bbox only)",
    )
    p.add_argument(
        "--plain",
        action="store_true",
        help="print non-JSON as plain text (for human reading)",
    )

    sub = p.add_subparsers(dest="cmd", required=True)

    # search
    sp = sub.add_parser("search", help="fuzzy search countries by name")
    sp.add_argument("keyword")
    sp.add_argument("--limit", type=int, default=10)
    sp.set_defaults(func=cmd_search)

    # resolve-iso
    sp = sub.add_parser("resolve-iso", help="resolve a country name to ISO 3")
    g = sp.add_mutually_exclusive_group(required=True)
    g.add_argument("--name", help="country name (English / Chinese / alias)")
    g.add_argument("--iso", help="ISO 3 or 2 letter code")
    sp.set_defaults(func=cmd_resolve_iso)

    # list-sources
    sp = sub.add_parser("list-sources", help="list available data sources")
    sp.set_defaults(func=cmd_list_sources)

    # levels
    sp = sub.add_parser("levels", help="list available ADM levels for a country")
    sp.add_argument("--iso", help="ISO 3 / 2 letter code")
    sp.add_argument("--name", help="country name (English / Chinese / alias)")
    sp.set_defaults(func=cmd_levels)

    # info
    sp = sub.add_parser("info", help="metadata + bbox + area for one boundary")
    sp.add_argument("--iso", help="ISO 3 / 2 letter code")
    sp.add_argument("--name", help="country name")
    sp.add_argument("--level", required=True, help="ADM0..ADM5")
    sp.set_defaults(func=cmd_info)

    # bbox
    sp = sub.add_parser("bbox", help="show bbox + area only (no metadata)")
    sp.add_argument("--iso", help="ISO 3 / 2 letter code")
    sp.add_argument("--name", help="country name")
    sp.add_argument("--level", required=True)
    sp.set_defaults(func=cmd_bbox)

    # country
    sp = sub.add_parser("country", help="download a country's boundary at a level")
    sp.add_argument("--iso", help="ISO 3 / 2 letter code")
    sp.add_argument("--name", help="country name")
    sp.add_argument("--level", required=True, help="ADM0..ADM5")
    sp.add_argument("--qa", metavar="PATH", default=None,
                    help="Write a JSON run-summary sidecar to PATH (Phase 5).")
    sp.set_defaults(func=cmd_country)

    # region
    sp = sub.add_parser("region", help="download a country boundary clipped to a bbox")
    sp.add_argument("--iso", help="ISO 3 / 2 letter code")
    sp.add_argument("--name", help="country name")
    sp.add_argument("--level", required=True, help="ADM0..ADM5")
    sp.add_argument("--bbox", required=True, help="'W,S,E,N' in WGS84 degrees")
    sp.add_argument("--qa", metavar="PATH", default=None,
                    help="Write a JSON run-summary sidecar to PATH (Phase 5).")
    sp.set_defaults(func=cmd_region)

    # multi
    sp = sub.add_parser("multi", help="download one ADM level for several countries, concat")
    sp.add_argument("--isos", required=True, help="comma-separated ISO 3 codes")
    sp.add_argument("--level", required=True, help="ADM0..ADM5")
    sp.add_argument("--qa", metavar="PATH", default=None,
                    help="Write a JSON run-summary sidecar to PATH (Phase 5).")
    sp.set_defaults(func=cmd_multi)

    # all-levels
    sp = sub.add_parser("all-levels", help="download every available ADM level for a country")
    sp.add_argument("--iso", help="ISO 3 / 2 letter code")
    sp.add_argument("--name", help="country name")
    sp.add_argument("--qa", metavar="PATH", default=None,
                    help="Write a JSON run-summary sidecar to PATH (Phase 5).")
    sp.set_defaults(func=cmd_all_levels)

    # cache
    sp = sub.add_parser("cache-clear", help="delete every cached file")
    sp.set_defaults(func=cmd_cache_clear)
    sp = sub.add_parser("cache-info", help="show cache size and root")
    sp.set_defaults(func=cmd_cache_info)

    return p


# ---------------------------------------------------------------------------
# Entry
# ---------------------------------------------------------------------------

def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except WorldBoundryError as e:
        return _err(str(e))
    except KeyboardInterrupt:
        return _err("interrupted")
    except Exception as e:  # pragma: no cover - defensive
        return _err(f"unexpected error: {e}")


if __name__ == "__main__":
    sys.exit(main())
