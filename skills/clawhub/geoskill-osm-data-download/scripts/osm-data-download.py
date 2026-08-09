#!/usr/bin/env python3
"""
osm-data-download: Download OpenStreetMap features via Overpass API.

Privacy Disclosure:
  - Bounding box coordinates are sent to the Overpass API server.
  - NO personal data, cookies, or identifiers are transmitted.
  - Query results are public OSM data (ODbL license).
  - Consider using a local Overpass instance for sensitive areas.

License: MIT-0 (Public Domain)
Data Source: OpenStreetMap via Overpass API (https://overpass-api.de/api/interpreter)
"""

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
import os
import re
import shutil
import sys
import time
import zipfile
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: requests is required. Install with: pip install requests>=2.28.0")
    sys.exit(1)

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(iterable, **kwargs):
        return iterable


# ─── Constants ───────────────────────────────────────────────────────────────

OVERPASS_URL = "https://overpass-api.de/api/interpreter"
OVERPASS_ENDPOINTS = [
    OVERPASS_URL,
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
]
NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
# Multiple Nominatim mirrors. The OSM-hosted one is rate-limited (1 req/s);
# try the OSM one first because it has the most complete data.
NOMINATIM_ENDPOINTS = [
    NOMINATIM_URL,
    "https://nominatim.openstreetmap.fr/search",
]
DEFAULT_TIMEOUT = 60
DEFAULT_RATE_DELAY = 1.0
USER_AGENT = "osm-data-download/0.3.0 (public geodata workflow)"

FEATURE_TAGS = {
    "highway": {
        "description": "Roads and streets",
        "values": ["motorway", "trunk", "primary", "secondary", "tertiary",
                   "residential", "service", "unclassified", "path", "footway"],
    },
    "building": {
        "description": "Buildings",
        "values": ["yes", "residential", "commercial", "industrial", "retail",
                   "apartments", "house", "school", "hospital"],
    },
    "amenity": {
        "description": "Amenities (POIs)",
        "values": ["restaurant", "cafe", "school", "hospital", "bank",
                   "pharmacy", "parking", "fuel", "police", "library"],
    },
    "shop": {
        "description": "Shops",
        "values": ["supermarket", "convenience", "mall", "bakery", "clothes"],
    },
    "tourism": {
        "description": "Tourism features",
        "values": ["hotel", "museum", "attraction", "viewpoint", "picnic_site"],
    },
    "landuse": {
        "description": "Land use",
        "values": ["residential", "commercial", "industrial", "forest",
                   "farmland", "grass", "meadow", "orchard"],
    },
    "natural": {
        "description": "Natural features",
        "values": ["water", "wood", "grassland", "wetland", "beach", "cliff"],
    },
    "waterway": {
        "description": "Waterways",
        "values": ["river", "stream", "canal", "ditch", "drain"],
    },
}

VALID_FORMATS = ["geojson", "shapefile"]
# Semantic presets — combine multiple tag filters in one query.
PRESETS = {
    "water": {
        "description": "Water bodies and waterways",
        "filters": [
            '["natural"="water"]',
            '["waterway"]',
            '["landuse"="reservoir"]',
            '["water"~"^(river|lake|pond|reservoir)$"]',
        ],
    },
    "building": {
        "description": "All buildings",
        "filters": ['["building"]'],
    },
    "road": {
        "description": "All roads and paths",
        "filters": ['["highway"]'],
    },
    "green": {
        "description": "Green spaces (parks, forests, grassland)",
        "filters": [
            '["leisure"="park"]',
            '["leisure"="garden"]',
            '["landuse"="forest"]',
            '["landuse"="grass"]',
            '["landuse"="meadow"]',
            '["natural"="wood"]',
            '["natural"="grassland"]',
            '["natural"="heath"]',
        ],
    },
}


class AmbiguousPlaceError(ValueError):
    """Raised when a place name cannot be resolved without guessing."""

    def __init__(self, place: str, candidates: list):
        self.place = place
        self.candidates = candidates
        summary = "; ".join(
            f"{c.get('display_name')} (relation {c.get('osm_id')})"
            for c in candidates[:8]
        )
        super().__init__(f"Place {place!r} is ambiguous. Candidates: {summary}")


# ─── Utility functions ───────────────────────────────────────────────────────

def validate_bbox(bbox_str: str) -> tuple:
    """Validate and parse bounding box string."""
    try:
        parts = bbox_str.split(",")
        if len(parts) != 4:
            raise ValueError("Bounding box must have 4 values")
        lon_min, lat_min, lon_max, lat_max = [float(p.strip()) for p in parts]

        if not (-180 <= lon_min <= 180 and -180 <= lon_max <= 180):
            raise ValueError(f"Longitude out of range: {lon_min}, {lon_max}")
        if not (-90 <= lat_min <= 90 and -90 <= lat_max <= 90):
            raise ValueError(f"Latitude out of range: {lat_min}, {lat_max}")
        if lon_min >= lon_max:
            raise ValueError(f"lon_min ({lon_min}) must be < lon_max ({lon_max})")
        if lat_min >= lat_max:
            raise ValueError(f"lat_min ({lat_min}) must be < lon_max ({lat_max})")

        # Warn if bbox is very large
        area = (lon_max - lon_min) * (lat_max - lat_min)
        if area > 1.0:
            print(f"WARNING: Large bounding box ({area:.2f} sq degrees). Query may be slow.")

        return (lon_min, lat_min, lon_max, lat_max)

    except ValueError as e:
        raise ValueError(f"Invalid bbox format '{bbox_str}': {e}")


def build_overpass_query(bbox: tuple, feature: str, value: str = None,
                         output_format: str = "json", timeout: int = 60) -> str:
    """Build an Overpass QL query for features within a bbox."""
    lon_min, lat_min, lon_max, lat_max = bbox
    # Overpass bbox format: (lat_min,lon_min,lat_max,lon_max)
    bbox_str = f"({lat_min},{lon_min},{lat_max},{lon_max})"

    if value:
        tag_filter = f'["{feature}"="{value}"]'
    else:
        tag_filter = f'["{feature}"]'

    # Query nodes, ways, and relations
    query = f"""
[out:{output_format}][timeout:{timeout}];
(
  node{tag_filter}{bbox_str};
  way{tag_filter}{bbox_str};
  relation{tag_filter}{bbox_str};
);
out body;
>;
out skel qt;
"""
    return query


def build_preset_query(bbox: tuple, preset: str, timeout: int = 60) -> str:
    """Build one Overpass query covering every tag in a semantic preset."""
    if preset not in PRESETS:
        raise ValueError(
            f"Unknown preset {preset!r}; available: {', '.join(sorted(PRESETS))}"
        )
    lon_min, lat_min, lon_max, lat_max = bbox
    bbox_text = f"({lat_min},{lon_min},{lat_max},{lon_max})"
    statements = []
    for tag_filter in PRESETS[preset]["filters"]:
        for element_type in ("node", "way", "relation"):
            statements.append(f"  {element_type}{tag_filter}{bbox_text};")
    return (
        f"[out:json][timeout:{timeout}];\n(\n"
        + "\n".join(statements)
        + "\n);\nout body;\n>;\nout skel qt;"
    )


def _normalise_place(value: str) -> str:
    value = re.sub(r"\s+", "", (value or "").strip())
    if not value:
        raise ValueError("--place must not be empty")
    return value


def _place_context(place: str) -> dict:
    """Extract conservative province/city/county hints for Nominatim."""
    result = {"country": "中国"}
    province = re.search(r"(.+?(?:省|自治区))", place)
    municipality = re.match(r"(.+?市)", place)
    county = re.search(r"([^省市]+?(?:区|县|旗|市))$", place)
    if province:
        result["state"] = province.group(1)
    if municipality:
        result["city"] = municipality.group(1)
    if county:
        result["county"] = county.group(1)
    return result


def _nominatim_request(params: dict, timeout: int) -> list:
    """Call Nominatim with endpoint fallback. Returns parsed JSON list."""
    last_err = None
    for endpoint in NOMINATIM_ENDPOINTS:
        try:
            response = requests.get(
                endpoint,
                params=params,
                headers={"User-Agent": USER_AGENT, "Accept-Language": "zh-CN,zh;q=0.9"},
                timeout=timeout,
            )
            if response.status_code == 429:
                last_err = "429"
                continue
            if response.status_code >= 500:
                last_err = str(response.status_code)
                continue
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            last_err = f"{type(e).__name__}: {e}"
            continue
    raise RuntimeError(f"All Nominatim endpoints failed: {last_err}")


def resolve_place(place: str, timeout: int = 30) -> dict:
    """Resolve an administrative place without silently choosing ambiguity."""
    normalised = _normalise_place(place)
    base = {
        "format": "jsonv2",
        "polygon_geojson": 1,
        "addressdetails": 1,
        "namedetails": 1,
        "countrycodes": "cn",
        "limit": 10,
    }
    attempts = []
    attempts.append({**base, "q": normalised})
    context = _place_context(normalised)
    if "county" in context or "city" in context:
        attempts.append({**base, **context})
    if normalised != place.strip():
        attempts.append({**base, "q": place.strip()})

    merged = {}
    for params in attempts:
        for candidate in _nominatim_request(params, timeout):
            key = (candidate.get("osm_type"), candidate.get("osm_id"))
            merged[key] = candidate
        if merged:
            break

    candidates = [
        item for item in merged.values()
        if item.get("osm_type") == "relation"
        and isinstance(item.get("geojson"), dict)
        and item["geojson"].get("type") in {"Polygon", "MultiPolygon"}
    ]
    if not candidates:
        raise ValueError(
            f"No administrative polygon found for {place!r}. "
            "Add province/city context or use a more specific name."
        )

    def score(item):
        display = re.sub(r"\s+", "", item.get("display_name", ""))
        address = item.get("address") or {}
        exact = normalised in display
        admin = item.get("category") == "boundary" or item.get("type") == "administrative"
        country = address.get("country_code") == "cn"
        return (100 if exact else 0) + (20 if admin else 0) + (10 if country else 0)

    candidates.sort(key=score, reverse=True)
    best_score = score(candidates[0])
    tied = [item for item in candidates if score(item) == best_score]
    if len(tied) > 1:
        exact_names = [
            item for item in tied
            if normalised == re.sub(r"\s+", "", (item.get("name") or ""))
        ]
        if len(exact_names) == 1:
            tied = exact_names
        else:
            raise AmbiguousPlaceError(place, tied)

    chosen = tied[0]
    bbox = chosen.get("boundingbox") or []
    if len(bbox) != 4:
        raise ValueError(f"Nominatim returned no usable bbox for {place!r}")
    return {
        "query": place,
        "normalised_query": normalised,
        "display_name": chosen.get("display_name"),
        "name": chosen.get("name") or chosen.get("display_name"),
        "osm_type": chosen.get("osm_type"),
        "osm_id": chosen.get("osm_id"),
        "admin_level": (chosen.get("extratags") or {}).get("admin_level"),
        "bbox": [float(bbox[2]), float(bbox[0]), float(bbox[3]), float(bbox[1])],
        "geometry": chosen["geojson"],
        "source": "OpenStreetMap Nominatim",
    }


def send_overpass_query(query: str, timeout: int = 60) -> dict:
    """Send query to Overpass API and return parsed JSON.

    Tries primary endpoint first, then fallbacks on connection / 5xx errors.
    """
    last_error = None
    for endpoint in OVERPASS_ENDPOINTS:
        try:
            response = requests.post(
                endpoint,
                data={"data": query},
                timeout=timeout + 30,  # Add buffer for network
                headers={"User-Agent": USER_AGENT},
            )

            if response.status_code == 429:
                # Rate-limited — try the next endpoint before giving up.
                print(f"WARNING: 429 rate limited on {endpoint}; trying next endpoint.")
                last_error = "429"
                continue

            if response.status_code == 504:
                print(f"WARNING: 504 gateway timeout on {endpoint}; trying next endpoint.")
                last_error = "504"
                continue

            if response.status_code != 200:
                print(f"WARNING: {endpoint} returned status {response.status_code}")
                last_error = str(response.status_code)
                continue

            return response.json()

        except requests.exceptions.Timeout:
            print(f"WARNING: timeout on {endpoint}; trying next endpoint.")
            last_error = "timeout"
            continue
        except requests.exceptions.ConnectionError as e:
            print(f"WARNING: connection error on {endpoint}: {e}")
            last_error = "connection"
            continue

    # All endpoints failed
    if last_error == "429":
        print("ERROR: All Overpass endpoints are rate-limited. Wait and try again.")
    elif last_error == "504":
        print("ERROR: All Overpass endpoints timed out. Try a smaller bbox.")
    else:
        print(f"ERROR: All Overpass endpoints failed (last status: {last_error}).")
    sys.exit(1)


def osm_to_geojson(osm_data: dict) -> dict:
    """Convert Overpass JSON response to GeoJSON."""
    elements = osm_data.get("elements", [])

    # Build node lookup for ways
    nodes = {}
    ways = []
    relations = []

    for elem in elements:
        if elem["type"] == "node":
            nodes[elem["id"]] = elem
        elif elem["type"] == "way":
            ways.append(elem)
        elif elem["type"] == "relation":
            relations.append(elem)

    features = []

    # Convert nodes to Point features
    for node_id, node in nodes.items():
        if "tags" in node:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [node["lon"], node["lat"]]
                },
                "properties": {
                    "osm_id": node_id,
                    "osm_type": "node",
                    **node.get("tags", {})
                }
            }
            features.append(feature)

    # Convert ways to LineString/Polygon features
    for way in ways:
        if "tags" not in way:
            continue
        node_ids = way.get("nodes", [])
        coords = []
        for nid in node_ids:
            if nid in nodes:
                coords.append([nodes[nid]["lon"], nodes[nid]["lat"]])

        if len(coords) < 2:
            continue

        # Determine geometry type
        tags = way.get("tags", {})
        is_polygon = (
            coords[0] == coords[-1] or  # Closed way
            tags.get("building") or
            tags.get("landuse") or
            tags.get("natural") == "water" or
            tags.get("waterway")
        )

        if is_polygon and len(coords) >= 4:
            geom_type = "Polygon"
            coords = [coords]  # Polygon needs outer array
        else:
            geom_type = "LineString"

        feature = {
            "type": "Feature",
            "geometry": {
                "type": geom_type,
                "coordinates": coords
            },
            "properties": {
                "osm_id": way["id"],
                "osm_type": "way",
                **tags
            }
        }
        features.append(feature)

    return {
        "type": "FeatureCollection",
        "features": features,
        "metadata": {
            "generator": "osm-data-download",
            "osm_elements": len(elements),
            "osm_nodes": len(nodes),
            "osm_ways": len(ways),
        }
    }


def clip_features_to_boundary(geojson: dict, boundary_geom: dict) -> dict:
    """Clip features in a FeatureCollection to a boundary polygon.

    Drops features fully outside, clips polygons/linestrings to the boundary.
    Requires shapely.
    """
    try:
        from shapely.geometry import shape, mapping
    except ImportError:
        print("WARNING: shapely not installed; skipping boundary clipping.")
        return geojson

    boundary = shape(boundary_geom)
    if not boundary.is_valid:
        boundary = boundary.buffer(0)
    if boundary.is_empty:
        return geojson

    clipped_features = []
    for feat in geojson.get("features", []):
        try:
            geom = shape(feat["geometry"])
        except Exception:
            clipped_features.append(feat)
            continue

        if not geom.is_valid:
            geom = geom.buffer(0)

        # Empty / invalid after fixup → drop
        if geom.is_empty:
            continue

        if boundary.contains(geom):
            clipped_features.append(feat)
        elif boundary.intersects(geom):
            inter = boundary.intersection(geom)
            if inter.is_empty:
                continue
            # Keep only polygon / line / point outputs
            if inter.geom_type in (
                "Polygon", "MultiPolygon",
                "LineString", "MultiLineString",
                "Point", "MultiPoint",
            ):
                clipped_features.append({
                    **feat,
                    "geometry": mapping(inter),
                })
        # else: feature is fully outside, drop it
    return {
        **geojson,
        "features": clipped_features,
    }


def save_geojson(geojson_data: dict, output_path: str) -> str:
    """Save GeoJSON to file. Returns the path written."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(geojson_data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {output_path} ({len(geojson_data['features'])} features)")
    return output_path


def save_shapefile(geojson_data: dict, output_path: str) -> str:
    """Save GeoJSON as Shapefile using fiona. Returns the path written.

    Mixed geometry types are split into one shapefile per type
    (e.g. base_Point.shp, base_LineString.shp, base_Polygon.shp).
    On import / write failure, falls back to GeoJSON next to the .shp path.
    """
    try:
        import fiona
        from fiona.crs import CRS
    except ImportError as e:
        print(f"WARNING: Shapefile output requires fiona: {e}")
        print("  Install with: pip install fiona shapely")
        # Fallback to GeoJSON
        geojson_path = str(Path(output_path).with_suffix(".geojson"))
        save_geojson(geojson_data, geojson_path)
        print(f"  Fallback: saved as GeoJSON instead: {geojson_path}")
        return geojson_path

    try:
        features = geojson_data.get("features", [])
        if not features:
            # Empty FeatureCollection — still create an empty shapefile
            shp = Path(output_path)
            with fiona.open(
                str(shp), "w",
                driver="ESRI Shapefile",
                crs=CRS.from_epsg(4326),
                schema={"geometry": "Point", "properties": {"osm_id": "str"}},
            ) as dst:
                pass
            _write_cpg(shp)
            print(f"Saved: {output_path} (0 features)")
            return output_path

        # Collect all property keys
        all_keys = []
        seen = set()
        for feat in features:
            for key in feat.get("properties", {}).keys():
                if key not in seen:
                    seen.add(key)
                    all_keys.append(key)
        schema_props = {k: "str" for k in all_keys}

        # Group by geometry type
        groups = {}
        for feat in features:
            gtype = feat["geometry"]["type"]
            groups.setdefault(gtype, []).append(feat)

        written_paths = []
        if len(groups) == 1:
            # Single geometry type — write to requested path
            gtype, feats = next(iter(groups.items()))
            _write_shapefile_one(
                output_path, gtype, feats, schema_props, CRS.from_epsg(4326)
            )
            written_paths.append(output_path)
        else:
            # Mixed — write one shapefile per geometry type with suffix
            base = Path(output_path)
            for gtype, feats in groups.items():
                sub = str(base.with_name(f"{base.stem}_{gtype}.shp"))
                _write_shapefile_one(sub, gtype, feats, schema_props, CRS.from_epsg(4326))
                written_paths.append(sub)
            print(
                f"NOTE: features split by geometry type → {len(groups)} shapefiles"
            )

        print(f"Saved: {', '.join(written_paths)} ({len(features)} features)")
        return written_paths[0] if len(written_paths) == 1 else written_paths

    except Exception as e:
        print(f"WARNING: Shapefile write failed: {e}")
        geojson_path = str(Path(output_path).with_suffix(".geojson"))
        save_geojson(geojson_data, geojson_path)
        return geojson_path


def _write_cpg(shp_path) -> None:
    """Write a UTF-8 .cpg sidecar so QGIS/ArcGIS pick UTF-8 for Chinese names."""
    cpg_path = shp_path.with_suffix(".cpg")
    try:
        with open(cpg_path, "w", encoding="ascii") as f:
            f.write("UTF-8\n")
    except OSError:
        pass


def _write_shapefile_one(output_path, gtype: str, feats: list,
                        schema_props: dict, crs) -> None:
    """Write a single shapefile with one geometry type."""
    import fiona
    # Ensure UTF-8 encoding is used for the .dbf so Chinese names survive.
    # This must be set before opening the file for writing.
    os.environ.setdefault("SHAPE_ENCODING", "UTF-8")
    with fiona.open(
        str(output_path), "w",
        driver="ESRI Shapefile",
        crs=crs,
        schema={"geometry": gtype, "properties": schema_props},
        encoding="utf-8",
    ) as dst:
        for feat in feats:
            props = {}
            for k in schema_props:
                v = feat.get("properties", {}).get(k)
                if v is None:
                    v = ""
                elif not isinstance(v, (str, int, float)):
                    v = str(v)
                props[k] = v
            dst.write({
                "geometry": feat["geometry"],
                "properties": props,
            })
    _write_cpg(Path(output_path))


def zip_shapefile_bundle(shp_path_or_paths, zip_stem: str = None) -> str:
    """Zip shapefile components into a single .zip.

    Accepts either a single .shp path (legacy) or a list of paths (when
    the data was split by geometry type). The zip filename defaults to
    the first shapefile's stem, but can be overridden with `zip_stem`
    to give a cleaner name (e.g. include the original base name).
    """
    if isinstance(shp_path_or_paths, str):
        paths = [shp_path_or_paths]
    else:
        paths = list(shp_path_or_paths)
    if not paths:
        raise ValueError("No shapefile paths provided to zip")

    shp_list = [Path(p) for p in paths]
    for p in shp_list:
        if not p.exists():
            raise FileNotFoundError(str(p))

    # Zip filename
    first = shp_list[0]
    parent = first.parent
    zip_name = zip_stem if zip_stem else first.stem
    zip_path = parent / f"{zip_name}.zip"

    # Common shapefile extensions
    extensions = (
        ".shp", ".shx", ".dbf", ".prj", ".cpg",
        ".sbn", ".sbx", ".fbn", ".fbx",
        ".ain", ".aih", ".atx", ".ixs", ".mxs", ".qix", ".qpj",
    )
    files_to_zip = []
    for shp in shp_list:
        stem = shp.stem
        files_to_zip.append(shp)
        for ext in extensions[1:]:
            candidate = parent / f"{stem}{ext}"
            if candidate.exists():
                files_to_zip.append(candidate)

    with zipfile.ZipFile(str(zip_path), "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in files_to_zip:
            zf.write(str(f), arcname=f.name)
    print(f"Zipped: {zip_path} ({len(files_to_zip)} files)")
    return str(zip_path)


def write_qa_summary(qa: dict, output_path: str) -> str:
    """Write QA summary as JSON next to outputs. Returns the path."""
    out = Path(output_path)
    qa_path = out.with_name(out.stem + ".qa.json")
    with open(qa_path, "w", encoding="utf-8") as f:
        json.dump(qa, f, ensure_ascii=False, indent=2)
    print(f"QA: {qa_path}")
    return str(qa_path)


def build_qa_summary(geojson: dict, *, bbox: tuple, query: str, formats: list,
                     place: dict = None, preset: str = None, feature: str = None,
                     value: str = None, clipped: bool = False,
                     extra: dict = None) -> dict:
    """Build a structured QA summary dictionary."""
    features = geojson.get("features", [])
    geom_counter = Counter(f["geometry"]["type"] for f in features)
    property_keys = set()
    for f in features:
        property_keys.update((f.get("properties") or {}).keys())

    qa = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generator": "osm-data-download",
        "feature_count": len(features),
        "geometry_types": dict(geom_counter),
        "property_keys": sorted(property_keys),
        "bbox": list(bbox),
        "crs": "EPSG:4326 (WGS84)",
        "query": {"overpass_query": query.strip()},
        "output_formats": formats,
    }
    if place is not None:
        qa["place"] = {
            "query": place.get("query"),
            "display_name": place.get("display_name"),
            "osm_type": place.get("osm_type"),
            "osm_id": place.get("osm_id"),
            "admin_level": place.get("admin_level"),
            "bbox": place.get("bbox"),
            "clipped_to_boundary": clipped,
        }
    if preset:
        qa["preset"] = {"name": preset, "filters": PRESETS[preset]["filters"]}
    if feature:
        qa["feature"] = {"key": feature, "value": value} if value else {"key": feature}
    if extra:
        qa.update(extra)
    return qa


def parse_format_list(text: str) -> list:
    """Parse a comma-separated format list, e.g. 'geojson,shapefile'."""
    if not text:
        return []
    out = []
    for item in text.split(","):
        item = item.strip().lower()
        if not item:
            continue
        if item not in VALID_FORMATS:
            raise ValueError(
                f"Unknown format {item!r}; valid: {', '.join(VALID_FORMATS)}"
            )
        if item not in out:
            out.append(item)
    return out


# ─── Commands ────────────────────────────────────────────────────────────────

def cmd_download(args):
    """Handle download subcommand."""
    bbox = validate_bbox(args.bbox)
    feature = args.feature.lower().strip()
    value = args.value.lower().strip() if args.value else None

    if feature not in FEATURE_TAGS:
        print(f"ERROR: Unknown feature type '{feature}'")
        print(f"  Available: {', '.join(FEATURE_TAGS.keys())}")
        sys.exit(1)

    print(f"Downloading OSM data:")
    print(f"  Feature: {feature}" + (f"={value}" if value else " (all)"))
    print(f"  BBox: {bbox}")
    print(f"  Format: {args.format}")

    # Build query
    query = build_overpass_query(bbox, feature, value, timeout=args.timeout)
    print(f"  Query built (timeout: {args.timeout}s)")

    # Send request
    print(f"  Sending to Overpass API...")
    osm_data = send_overpass_query(query, args.timeout)

    elements = osm_data.get("elements", [])
    print(f"  Received {len(elements)} elements")

    if not elements:
        print("  No features found. Check bbox and feature type.")
        return

    # Convert to GeoJSON
    geojson_data = osm_to_geojson(osm_data)

    # Save
    if args.format == "shapefile":
        save_shapefile(geojson_data, args.output)
    else:
        save_geojson(geojson_data, args.output)

    # Rate limiting
    time.sleep(args.rate_delay)


def cmd_query(args):
    """Handle query subcommand — custom Overpass QL."""
    print(f"Running custom Overpass query...")
    print(f"  Timeout: {args.timeout}s")

    osm_data = send_overpass_query(args.query, args.timeout)

    elements = osm_data.get("elements", [])
    print(f"  Received {len(elements)} elements")

    if not elements:
        print("  No results found.")
        return

    geojson_data = osm_to_geojson(osm_data)

    if args.output:
        ext = Path(args.output).suffix.lower()
        if ext == ".shp":
            save_shapefile(geojson_data, args.output)
        else:
            save_geojson(geojson_data, args.output)
    else:
        # Print summary to stdout
        print(f"\nResults: {len(geojson_data['features'])} features")
        print(json.dumps(geojson_data["metadata"], indent=2))

    time.sleep(args.rate_delay)


def cmd_list_tags(args):
    """Handle list-tags subcommand."""
    print("\nCommon OSM Feature Tags")
    print("=" * 60)

    for tag, info in FEATURE_TAGS.items():
        print(f"\n  {tag}: {info['description']}")
        print(f"    Values: {', '.join(info['values'])}")

    print(f"\n{'=' * 60}")
    print(f"Usage: --feature <tag> --value <value>")
    print(f"  Omit --value to get all features with that tag.")
    print(f"\nSemantic presets:")
    for name, info in PRESETS.items():
        print(f"  {name}: {info['description']}")
    print(f"\nData: © OpenStreetMap contributors (ODbL)")


def cmd_download_place(args):
    """Download features for a named administrative place.

    Resolves place via Nominatim, then queries Overpass using either
    --preset (semantic) or --feature/--value (raw tag) within the
    administrative bbox, optionally clipping to the admin polygon.
    """
    if not args.preset and not args.feature:
        raise ValueError("download-place requires either --preset or --feature")

    print(f"Resolving place: {args.place}")
    place = resolve_place(args.place, timeout=args.timeout)
    bbox = tuple(place["bbox"])
    print(f"  → {place['display_name']} (OSM {place['osm_type']}/{place['osm_id']})")
    print(f"  bbox: {bbox}")

    # Build the Overpass query
    if args.preset:
        if args.preset not in PRESETS:
            raise ValueError(
                f"Unknown preset {args.preset!r}; "
                f"available: {', '.join(sorted(PRESETS))}"
            )
        query = build_preset_query(bbox, args.preset, timeout=args.timeout)
        print(f"  Preset: {args.preset} ({len(PRESETS[args.preset]['filters'])} tag groups)")
    else:
        feature = args.feature.lower().strip()
        if feature not in FEATURE_TAGS:
            raise ValueError(
                f"Unknown feature {feature!r}; "
                f"available: {', '.join(FEATURE_TAGS.keys())}"
            )
        value = args.value.lower().strip() if args.value else None
        query = build_overpass_query(bbox, feature, value, timeout=args.timeout)
        print(f"  Feature: {feature}" + (f"={value}" if value else " (all)"))

    print(f"  Querying Overpass (timeout {args.timeout}s)...")
    osm_data = send_overpass_query(query, args.timeout)
    elements = osm_data.get("elements", [])
    print(f"  Received {len(elements)} elements")

    if not elements:
        print("  No features found in this area. Try a larger or different preset.")
        # Still emit QA so users can see the place resolved but empty
        if args.qa:
            qa = build_qa_summary(
                {"features": []},
                bbox=bbox, query=query, formats=parse_format_list(args.formats) or ["geojson"],
                place=place, preset=args.preset, feature=args.feature, value=args.value,
            )
            qa_path = write_qa_summary(qa, args.output)
        return

    geojson_data = osm_to_geojson(osm_data)

    clipped = False
    if not args.no_clip:
        before = len(geojson_data["features"])
        geojson_data = clip_features_to_boundary(geojson_data, place["geometry"])
        after = len(geojson_data["features"])
        if after != before:
            clipped = True
        print(f"  Clipped to boundary: {before} → {after} features")
    else:
        print("  Skipping boundary clipping (--no-clip)")

    # Determine output path and formats
    formats = parse_format_list(args.formats)
    if not formats:
        formats = [args.format]  # fall back to legacy --format

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    written = []
    shp_paths_for_zip = []
    for fmt in formats:
        if fmt == "shapefile":
            shp_path = str(output_path.with_suffix(".shp"))
            w = save_shapefile(geojson_data, shp_path)
            if isinstance(w, list):
                written.extend(w)
                shp_paths_for_zip.extend(w)
            else:
                written.append(w)
                if w.endswith(".shp"):
                    shp_paths_for_zip.append(w)
        else:
            gj_path = str(output_path.with_suffix(".geojson"))
            w = save_geojson(geojson_data, gj_path)
            written.append(w)

    if args.zip_shapefile and shp_paths_for_zip:
        z = zip_shapefile_bundle(shp_paths_for_zip, zip_stem=output_path.stem)
        written.append(z)

    if args.qa:
        qa = build_qa_summary(
            geojson_data, bbox=bbox, query=query,
            formats=formats, place=place,
            preset=args.preset, feature=args.feature, value=args.value,
            clipped=clipped,
            extra={"output_files": written},
        )
        write_qa_summary(qa, args.output)

    time.sleep(args.rate_delay)


# ─── CLI Setup ───────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="osm-data-download",
        description="Download OpenStreetMap features via Overpass API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Privacy: Bounding box coordinates are sent to Overpass API. No personal data is transmitted.

Examples:
  %(prog)s download --bbox "116.0,39.5,116.8,40.2" --feature highway -o roads.geojson
  %(prog)s download --bbox "116.3,39.8,116.5,40.0" --feature building -o buildings.geojson
  %(prog)s download-place --place "北京市朝阳区" --preset water --formats geojson,shapefile --zip-shapefile --qa -o chaoyang_water
  %(prog)s download-place --place "成都市" --feature highway -o chengdu_roads.geojson
  %(prog)s query --query '[out:json][timeout:60];(node["amenity"="restaurant"](39.8,116.3,40.0,116.5););out body;'
  %(prog)s list-tags
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # ── download ──
    p_dl = subparsers.add_parser("download", help="Download features by bbox and tag")
    p_dl.add_argument("--bbox", required=True, help="Bounding box: lon_min,lat_min,lon_max,lat_max")
    p_dl.add_argument("--feature", required=True, choices=list(FEATURE_TAGS.keys()),
                      help="Feature type (OSM tag key)")
    p_dl.add_argument("--value", help="Specific tag value (omit for all values)")
    p_dl.add_argument("-o", "--output", required=True, help="Output file path")
    p_dl.add_argument("--format", default="geojson", choices=VALID_FORMATS,
                      help="Output format")
    p_dl.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT,
                      help=f"API timeout in seconds (default: {DEFAULT_TIMEOUT})")
    p_dl.add_argument("--rate-delay", type=float, default=DEFAULT_RATE_DELAY,
                      help=f"Delay between requests (default: {DEFAULT_RATE_DELAY}s)")
    p_dl.set_defaults(func=cmd_download)

    # ── download-place ── (NEW)
    p_dp = subparsers.add_parser(
        "download-place",
        help="Download features for an administrative place (resolves bbox + optional clipping)",
    )
    p_dp.add_argument("--place", required=True, help="Administrative place name (e.g. 北京市朝阳区)")
    p_dp.add_argument("--preset", choices=sorted(PRESETS.keys()),
                      help="Semantic preset (water/road/building/green)")
    p_dp.add_argument("--feature", choices=list(FEATURE_TAGS.keys()),
                      help="Feature key (alternative to --preset)")
    p_dp.add_argument("--value", help="Specific tag value (with --feature)")
    p_dp.add_argument("-o", "--output", required=True,
                      help="Output file base path (extensions auto-set per format)")
    p_dp.add_argument("--format", default="geojson", choices=VALID_FORMATS,
                      help="Single output format (legacy; prefer --formats)")
    p_dp.add_argument("--formats", default=None,
                      help=f"Comma-separated formats: {','.join(VALID_FORMATS)}")
    p_dp.add_argument("--zip-shapefile", action="store_true",
                      help="When shapefile is in --formats, also write a .zip bundle")
    p_dp.add_argument("--no-clip", action="store_true",
                      help="Do not clip features to the admin boundary (default: clip)")
    p_dp.add_argument("--qa", action="store_true",
                      help="Write a QA summary JSON next to the outputs")
    p_dp.add_argument("--clip-to-boundary", action="store_true",
                      help="(alias of default behaviour; kept for explicitness)")
    p_dp.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT,
                      help=f"API timeout in seconds (default: {DEFAULT_TIMEOUT})")
    p_dp.add_argument("--rate-delay", type=float, default=DEFAULT_RATE_DELAY,
                      help=f"Delay between requests (default: {DEFAULT_RATE_DELAY}s)")
    p_dp.set_defaults(func=cmd_download_place)

    # ── query ──
    p_q = subparsers.add_parser("query", help="Run custom Overpass QL query")
    p_q.add_argument("--query", required=True, help="Overpass QL query string")
    p_q.add_argument("-o", "--output", help="Output file path")
    p_q.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT,
                     help=f"API timeout (default: {DEFAULT_TIMEOUT}s)")
    p_q.add_argument("--rate-delay", type=float, default=DEFAULT_RATE_DELAY,
                     help=f"Delay after request (default: {DEFAULT_RATE_DELAY}s)")
    p_q.set_defaults(func=cmd_query)

    # ── list-tags ──
    p_lt = subparsers.add_parser("list-tags", help="List common OSM feature tags and presets")
    p_lt.set_defaults(func=cmd_list_tags)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        return args.func(args)
    except ValueError as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    except AmbiguousPlaceError as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nAborted by user.")
        sys.exit(130)


if __name__ == "__main__":
    sys.exit(main())
