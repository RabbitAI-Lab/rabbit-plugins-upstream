"""
Transit Jakarta API Client
API base: https://transit.oyenza.com
"""
import json, time, hashlib, pathlib, requests, os
from typing import Optional

BASE = "https://transit.oyenza.com"
CACHE_DIR = pathlib.Path(__file__).parent / "cache"
CACHE_DIR.mkdir(exist_ok=True)
STATIC_META_FILE = CACHE_DIR / "meta.json"
STATIC_DATA_FILE = CACHE_DIR / "static.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Accept": "application/json",
    "Referer": "https://transit.oyenza.com/",
}

_session = requests.Session()


def _get(path: str, params=None, timeout=10):
    r = _session.get(BASE + path, params=params, headers=HEADERS, timeout=timeout)
    r.raise_for_status()
    return r.json()


def get_meta():
    """Ambil metadata: static version, feed status."""
    return _get("/api/meta")


def get_stats():
    """Statistik semua bus aktif."""
    return _get("/api/stats")


def get_arrivals(halte_id: str):
    """Arrival times untuk satu halte."""
    return _get(f"/api/halte/{halte_id}")


def get_bus(bus_id: str):
    """Detail satu bus (position + next halte)."""
    return _get(f"/api/bus/{bus_id}")


def get_static_data(force_refresh=False):
    """Ambil + cache GTFS static data."""
    meta = get_meta()
    version = meta.get("static", "")

    # Check cache
    cached_meta = {}
    if STATIC_META_FILE.exists():
        cached_meta = json.loads(STATIC_META_FILE.read_text())

    needs_refresh = (
        force_refresh
        or not STATIC_DATA_FILE.exists()
        or cached_meta.get("static") != version
    )

    if not needs_refresh:
        return json.loads(STATIC_DATA_FILE.read_text()), meta

    # Fetch fresh
    url = meta.get("staticUrl") or "/data/static-latest.json"
    data_url = BASE + url if url.startswith("/") else url
    r = _session.get(data_url, headers=HEADERS, timeout=45)
    r.raise_for_status()
    data = r.json()

    # Save cache
    STATIC_META_FILE.write_text(json.dumps(meta))
    STATIC_DATA_FILE.write_text(json.dumps(data))

    return data, meta


def search_halte(query: str, limit=8):
    """Fuzzy search halte by name. Returns list of (halte_id, name, routes)."""
    data, _ = get_static_data()
    q = query.lower().strip()
    results = []
    for h in data.get("halte", []):
        name = h.get("name", "")
        if q in name.lower():
            results.append({
                "id": h.get("id"),
                "name": name,
                "routes": h.get("r", []),
                "lat": h.get("lat"),
                "lng": h.get("lng"),
                "brt": h.get("brt", False),
            })
    return results[:limit]


def search_route(query: str, limit=8):
    """Search route by short or long name."""
    data, _ = get_static_data()
    q = query.lower().strip()
    results = []
    for r in data.get("routes", []):
        short = r.get("short", "")
        long = r.get("long", "")
        if q in short.lower() or q in long.lower():
            results.append({
                "id": r.get("id"),
                "short": short,
                "long": long,
                "kind": r.get("kind"),
                "color": r.get("color"),
            })
    return results[:limit]


def get_halte_by_id(halte_id: str):
    """Get halte details by ID."""
    data, _ = get_static_data()
    for h in data.get("halte", []):
        if h.get("id") == halte_id:
            return {
                "id": h.get("id"),
                "name": h.get("name"),
                "routes": h.get("r", []),
                "lat": h.get("lat"),
                "lng": h.get("lng"),
                "brt": h.get("brt", False),
            }
    return None


def get_routes_for_halte(halte_id: str):
    """Get all routes serving a halte."""
    data, _ = get_static_data()
    route_map = {r.get("id"): r for r in data.get("routes", [])}
    halte = get_halte_by_id(halte_id)
    if not halte:
        return {}
    result = {}
    for rid in halte.get("routes", []):
        if rid in route_map:
            result[rid] = route_map[rid]
    return result


def nearest_halte(lat: float, lng: float, limit=5):
    """Find nearest halte to coordinates. Returns list sorted by distance."""
    import math
    data, _ = get_static_data()
    def dist(h):
        dlng = (h.get("lng", 0) - lng) * math.cos(math.radians((lat + h.get("lat", 0)) / 2))
        dlat = h.get("lat", 0) - lat
        return math.sqrt(dlng**2 + dlat**2) * 6371008  # meters

    halte_list = [h for h in data.get("halte", []) if h.get("lat") and h.get("lng")]
    halte_list.sort(key=dist)
    return [
        {
            "id": h.get("id"),
            "name": h.get("name"),
            "routes": h.get("r", []),
            "dist_m": round(dist(h)),
            "lat": h.get("lat"),
            "lng": h.get("lng"),
        }
        for h in halte_list[:limit]
    ]


def format_eta(eta_min: int) -> str:
    """Format ETA minutes to human readable."""
    if eta_min <= 0:
        return "Tiba sekarang ⭐"
    elif eta_min < 60:
        return f"{eta_min} menit"
    else:
        hours = eta_min // 60
        mins = eta_min % 60
        return f"{hours}j {mins}m" if mins else f"{hours} jam"


def format_age(age_s: int) -> str:
    """Format age seconds to human readable."""
    if age_s < 60:
        return f"{age_s} dtk lalu"
    elif age_s < 3600:
        return f"{age_s // 60} mnt lalu"
    else:
        return f"{age_s // 3600} jam lalu"


KIND_LABELS = {
    "brt": "BRT",
    "integrasi": "Non-BRT",
    "mikrotrans": "Mikrotrans",
    "jabodetabek": "Transjabodetabek",
    "royal": "Royaltrans",
    "rusun": "Rusun",
    "wisata": "Wisata",
    "other": "Lainnya",
}
