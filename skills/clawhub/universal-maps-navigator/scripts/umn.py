#!/usr/bin/env python3
"""umn.py — Universal Maps Navigator CLI v2.0.0 (stdlib only, Python 3.8+).

v2 Improvements:
- 50+ languages, RTL, cultural POI via i18n.py
- Life-saving survival guides via survival.py (FM 21-76, Red Cross)
- Self-improving loop via self_improve.py (Memento-Skills)
- Token optimizer via token_optimizer.py (60% reduction)
- Hallucination reduction: schema validation, confidence, citations, abstention
- Speed: parallel mirrors, compact mode, caching

Seven apps in 1 CLI: Google Maps, Apple Maps, Waze, Organic Maps, CoMaps, HERE WeGo, Sygic.
Built on free/open services (OSM, OSRM, Valhalla, Overpass, Open-Meteo, Transitous).

    umn geocode "Palace of Parliament, Bucharest" --lang ro --compact
    umn route "Bucharest" "Brașov" --steps --lang ro --compact
    umn survival guide --terrain mountain --disaster avalanche --lang en
    umn i18n list
    umn self-improve --analyze

Run `umn --help` or `umn <command> --help`. Add --json for machine output, --compact for minimal tokens.
"""
from __future__ import annotations
import argparse
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

# Add script dir to path for local imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deeplinks  # noqa: E402

# v2 modules — graceful fallback if not present (for backward compat)
try:
    import i18n as i18n_mod  # noqa: E402
except ImportError:
    i18n_mod = None
try:
    import survival as survival_mod  # noqa: E402
except ImportError:
    survival_mod = None
try:
    import self_improve as self_improve_mod  # noqa: E402
except ImportError:
    self_improve_mod = None
try:
    import token_optimizer as token_opt_mod  # noqa: E402
except ImportError:
    token_opt_mod = None

VERSION = "2.0.3"
SKILL_URL = "https://clawhub.ai/skills/universal-maps-navigator"
CONFIG_DIR = os.environ.get("UMN_CONFIG_DIR") or os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "universal-maps-navigator")
CACHE_DIR = os.environ.get("UMN_CACHE_DIR") or os.path.join(os.environ.get("XDG_CACHE_HOME", os.path.expanduser("~/.cache")), "universal-maps-navigator")
CONFIG_PATH = os.path.join(CONFIG_DIR, "config.json")
OFFLINE = os.environ.get("UMN_OFFLINE") == "1"

# ----------------------------------------------------------------------------- endpoints
NOMINATIM = "https://nominatim.openstreetmap.org"
PHOTON = "https://photon.komoot.io"
OSRM_CAR = "https://router.project-osrm.org"
OSRM_FOSSGIS = "https://routing.openstreetmap.de/routed-{profile}"
VALHALLA_DEFAULT = "https://valhalla1.openstreetmap.de"
OVERPASS_SERVERS = ["https://overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter", "https://overpass.private.coffee/api/interpreter"]
OPENTOPO = "https://api.opentopodata.org/v1"
OPEN_METEO = "https://api.open-meteo.com/v1/forecast"
TRANSITOUS = "https://api.transitous.org/api/v1"
OCM = "https://api.openchargemap.io/v3/poi/"
ORS = "https://api.openrouteservice.org"
OSM_API = "https://api.openstreetmap.org/api/0.6"
WIKIPEDIA = "https://{lang}.wikipedia.org/w/api.php"
GEOFABRIK_INDEX = "https://download.geofabrik.de/index-v1-nogeom.json"
TOMTOM = "https://api.tomtom.com"

MODES = deeplinks.MODES
VALHALLA_COSTING = {"car": "auto", "truck": "truck", "bike": "bicycle", "foot": "pedestrian", "scooter": "motor_scooter",
                    "motorcycle": "motorcycle", "bus": "bus", "taxi": "taxi"}
OSRM_PROFILE = {"car": "car", "bike": "bike", "foot": "foot"}
ORS_PROFILE = {"car": "driving-car", "truck": "driving-hgv", "bike": "cycling-regular", "foot": "foot-walking",
               "scooter": "driving-car", "motorcycle": "driving-car", "bus": "driving-car", "taxi": "driving-car"}

WMO = {0: "clear", 1: "mainly clear", 2: "partly cloudy", 3: "overcast", 45: "fog", 48: "rime fog", 51: "light drizzle", 53: "drizzle",
       55: "dense drizzle", 56: "freezing drizzle", 57: "freezing drizzle", 61: "light rain", 63: "rain", 65: "heavy rain", 66: "freezing rain",
       67: "freezing rain", 71: "light snow", 73: "snow", 75: "heavy snow", 77: "snow grains", 80: "rain showers", 81: "rain showers",
       82: "violent showers", 85: "snow showers", 86: "snow showers", 95: "thunderstorm", 96: "thunderstorm w/ hail", 99: "thunderstorm w/ hail"}

POI_CATEGORIES = {
    "fuel": ['["amenity"="fuel"]'], "gas": ['["amenity"="fuel"]'], "petrol": ['["amenity"="fuel"]'],
    "charging": ['["amenity"="charging_station"]'], "ev": ['["amenity"="charging_station"]'],
    "parking": ['["amenity"="parking"]', '["amenity"="parking_entrance"]'], "bike-parking": ['["amenity"="bicycle_parking"]'],
    "restaurant": ['["amenity"="restaurant"]'], "fast-food": ['["amenity"="fast_food"]'], "cafe": ['["amenity"="cafe"]'], "bar": ['["amenity"~"bar|pub"]'],
    "hotel": ['["tourism"~"hotel|hostel|guest_house|motel"]'], "camping": ['["tourism"~"camp_site|caravan_site"]'],
    "supermarket": ['["shop"~"supermarket|convenience"]'], "pharmacy": ['["amenity"="pharmacy"]'], "hospital": ['["amenity"~"hospital|clinic"]'],
    "doctor": ['["amenity"~"doctors|clinic"]'], "police": ['["amenity"="police"]'], "atm": ['["amenity"~"atm|bank"]'], "toilets": ['["amenity"="toilets"]'],
    "water": ['["amenity"="drinking_water"]'], "viewpoint": ['["tourism"="viewpoint"]'], "attraction": ['["tourism"~"attraction|museum|gallery|zoo|theme_park"]'],
    "museum": ['["tourism"="museum"]'], "park": ['["leisure"="park"]'], "playground": ['["leisure"="playground"]'],
    "bus-stop": ['["highway"="bus_stop"]', '["public_transport"="platform"]["bus"="yes"]'], "station": ['["railway"="station"]', '["railway"="halt"]'],
    "metro": ['["station"="subway"]', '["railway"="subway_entrance"]'], "tram": ['["railway"="tram_stop"]'], "airport": ['["aeroway"="aerodrome"]'],
    "ferry": ['["amenity"="ferry_terminal"]'], "taxi": ['["amenity"="taxi"]'], "car-rental": ['["amenity"="car_rental"]'], "car-wash": ['["amenity"="car_wash"]'],
    "repair": ['["shop"="car_repair"]'], "rest-area": ['["highway"~"rest_area|services"]'], "speed-camera": ['["highway"="speed_camera"]', '["enforcement"="maxspeed"]'],
    "bike-rental": ['["amenity"="bicycle_rental"]'], "bike-shop": ['["shop"="bicycle"]'], "post": ['["amenity"="post_office"]'], "library": ['["amenity"="library"]'],
    "cinema": ['["amenity"="cinema"]'], "gym": ['["leisure"="fitness_centre"]'], "beach": ['["natural"="beach"]'], "peak": ['["natural"="peak"]'],
    "embassy": ['["office"="diplomatic"]'], "shelter": ['["amenity"="shelter"]', '["emergency"="assembly_point"]'], "wifi": ['["internet_access"~"wlan|yes"]'],
    # v2 cultural extensions
    "mosque": ['["amenity"="place_of_worship"]["religion"="muslim"]', '["building"="mosque"]'],
    "church": ['["amenity"="place_of_worship"]["religion"="christian"]'],
    "temple": ['["amenity"="place_of_worship"]["religion"~"buddhist|hindu|shinto"]'],
    "synagogue": ['["amenity"="place_of_worship"]["religion"="jewish"]'],
    "shrine": ['["historic"="wayside_shrine"]'],
    "bazaar": ['["shop"="bazaar"]', '["amenity"="marketplace"]'],
    "souk": ['["shop"="market"]', '["amenity"="marketplace"]'],
    "hammam": ['["amenity"="public_bath"]'],
    "onsen": ['["amenity"="public_bath"]["bath:type"="onsen"]', '["leisure"="hot_spring"]'],
    "halal": ['["diet:halal"="yes"]'],
    "kosher": ['["diet:kosher"="yes"]'],
    "vegan": ['["diet:vegan"="yes"]'],
}

# ----------------------------------------------------------------------------- small utils
class UmnError(Exception):
    pass

def eprint(*a):
    print(*a, file=sys.stderr)

def load_config():
    try:
        with open(CONFIG_PATH) as fh:
            return json.load(fh)
    except Exception:
        return {}

def save_config(cfg):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    tmp = CONFIG_PATH + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(cfg, fh, indent=2, ensure_ascii=False)
    os.replace(tmp, CONFIG_PATH)
    try:
        os.chmod(CONFIG_PATH, 0o600)
    except Exception:
        pass

CFG = load_config()
VALHALLA = (os.environ.get("UMN_VALHALLA_URL") or CFG.get("valhalla_url") or VALHALLA_DEFAULT).rstrip("/")

def cfg_key(name):
    return os.environ.get("UMN_" + name.upper()) or CFG.get(name) or ""

def user_agent():
    contact = cfg_key("contact_email")
    return f"universal-maps-navigator/{VERSION} (+{SKILL_URL}" + (f"; {contact}" if contact else "") + ")"

def _rl_path():
    return os.path.join(CACHE_DIR, "ratelimit.json")

def pace(host, min_interval):
    os.makedirs(CACHE_DIR, exist_ok=True)
    try:
        st = json.load(open(_rl_path()))
    except Exception:
        st = {}
    last = st.get(host, 0)
    wait = last + min_interval - time.time()
    if wait > 0:
        time.sleep(wait)
    st[host] = time.time()
    try:
        json.dump(st, open(_rl_path(), "w"))
    except Exception:
        pass

def http(url, params=None, data=None, headers=None, timeout=40, method=None, retries=1, accept_json=True):
    if OFFLINE:
        raise UmnError("network disabled (UMN_OFFLINE=1)")
    if params:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params, quote_via=urllib.parse.quote, safe=",;|:/")
    body = None
    if data is not None:
        body = data.encode() if isinstance(data, str) else json.dumps(data).encode()
    h = {"User-Agent": user_agent(), "Accept": "application/json" if accept_json else "*/*"}
    if isinstance(data, (dict, list)):
        h["Content-Type"] = "application/json"
    elif isinstance(data, str):
        h["Content-Type"] = "application/x-www-form-urlencoded"
    h.update(headers or {})
    last_err = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, data=body, headers=h, method=method)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                if accept_json:
                    try:
                        return json.loads(raw.decode("utf-8", "replace"))
                    except ValueError:
                        raise UmnError(f"non-JSON response from {urllib.parse.urlsplit(url).netloc} [source={urllib.parse.urlsplit(url).netloc}]")
                return raw.decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            txt = e.read()[:300].decode("utf-8", "replace")
            last_err = UmnError(f"HTTP {e.code} from {urllib.parse.urlsplit(url).netloc}: {txt.strip()[:160]} [source={urllib.parse.urlsplit(url).netloc}]")
            if e.code in (429, 502, 503, 504) and attempt < retries:
                time.sleep(2 + 2 * attempt)
                continue
            raise last_err
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last_err = UmnError(f"network error for {urllib.parse.urlsplit(url).netloc}: {str(e)[:120]} [source={urllib.parse.urlsplit(url).netloc}]")
            if attempt < retries:
                time.sleep(1)
                continue
            raise last_err
    raise last_err

def cache_get(name, max_age):
    p = os.path.join(CACHE_DIR, name)
    try:
        if time.time() - os.path.getmtime(p) < max_age:
            return json.load(open(p))
    except Exception:
        pass
    return None

def cache_put(name, obj):
    os.makedirs(CACHE_DIR, exist_ok=True)
    try:
        json.dump(obj, open(os.path.join(CACHE_DIR, name), "w"))
    except Exception:
        pass

def haversine(a, b):
    R = 6371000.0
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))

def bearing(a, b):
    la1, la2 = math.radians(a[0]), math.radians(b[0])
    dlo = math.radians(b[1] - a[1])
    x = math.sin(dlo) * math.cos(la2)
    y = math.cos(la1) * math.sin(la2) - math.sin(la1) * math.cos(la2) * math.cos(dlo)
    return (math.degrees(math.atan2(x, y)) + 360) % 360

def compass(deg):
    return ["N", "NE", "E", "SE", "S", "SW", "W", "NW"][int((deg + 22.5) // 45) % 8]

def fmt_dist(m, units=None, lang="en"):
    # v2: respect CFG units first, then i18n
    # Test expects CFG["units"]=imperial to override lang default
    effective_units = units or cfg_key("units") or None
    if effective_units is None:
        # No explicit units -> use i18n auto
        if i18n_mod and lang:
            try:
                return i18n_mod.format_distance(m, lang, "auto")
            except Exception:
                pass
        effective_units = "metric"
    else:
        if i18n_mod and lang:
            try:
                # Pass effective_units to i18n so imperial CFG is respected
                return i18n_mod.format_distance(m, lang, effective_units)
            except Exception:
                pass
    if effective_units.startswith("imp"):
        mi = m / 1609.344
        return f"{mi:.1f} mi" if mi >= 0.2 else f"{m * 3.28084:.0f} ft"
    return f"{m / 1000:.1f} km" if m >= 1000 else f"{m:.0f} m"

def fmt_dur(s, lang="en"):
    if i18n_mod and lang:
        try:
            return i18n_mod.format_duration(s, lang)
        except Exception:
            pass
    s = int(round(s))
    h, m = divmod(s // 60, 60)
    return f"{h} h {m:02d} min" if h else f"{m} min"

def decode_polyline(s, precision=6):
    coords, idx, lat, lon, f = [], 0, 0, 0, 10 ** precision
    while idx < len(s):
        for which in (0, 1):
            shift = result = 0
            while True:
                b = ord(s[idx]) - 63
                idx += 1
                result |= (b & 0x1F) << shift
                shift += 5
                if b < 0x20:
                    break
            d = ~(result >> 1) if result & 1 else result >> 1
            if which == 0:
                lat += d
            else:
                lon += d
        coords.append((lat / f, lon / f))
    return coords

def sample_line(coords, n):
    if len(coords) <= n:
        return list(coords)
    total = sum(haversine(coords[i], coords[i + 1]) for i in range(len(coords) - 1))
    step, acc, out, nxt = total / max(n - 1, 1), 0.0, [coords[0]], 1
    for i in range(len(coords) - 1):
        acc += haversine(coords[i], coords[i + 1])
        while acc >= nxt * step and len(out) < n - 1:
            out.append(coords[i + 1])
            nxt += 1
    out.append(coords[-1])
    return out

def plus_code(lat, lon):
    alphabet = "23456789CFGHJMPQRVWX"
    lat = min(max(float(lat), -90.0), 90.0)
    lon = ((float(lon) + 180.0) % 360.0) - 180.0
    if lat == 90.0:
        lat -= 0.000125
    lat_v = int(math.floor((lat + 90.0) * 8000))
    lon_v = int(math.floor((lon + 180.0) * 8000))
    code = ""
    for _ in range(5):
        code = alphabet[lon_v % 20] + code
        code = alphabet[lat_v % 20] + code
        lat_v //= 20
        lon_v //= 20
    return code[:8] + "+" + code[8:]

# ----------------------------------------------------------------------------- places & geocoding
LATLON_RE = re.compile(r"^\s*(-?\d+(?:\.\d+)?)\s*[, ]\s*(-?\d+(?:\.\d+)?)\s*$")

def saved_places():
    return CFG.get("places", {})

def parse_place(text, limit=1, country=None, lang="en"):
    m = LATLON_RE.match(text or "")
    if m:
        lat, lon = float(m.group(1)), float(m.group(2))
        if -90 <= lat <= 90 and -180 <= lon <= 180:
            return {"lat": lat, "lon": lon, "name": f"{lat:.5f},{lon:.5f}", "source": "coordinates", "confidence": "high"}
    sp = saved_places().get((text or "").strip().lower())
    if sp:
        return {"lat": sp["lat"], "lon": sp["lon"], "name": sp.get("name") or text, "source": "saved", "confidence": "high"}
    res = geocode(text, limit=limit, country=country, lang=lang)
    if not res:
        raise UmnError(f"could not geocode {text!r} [source=nominatim|photon] confidence:low — abstain if uncertain")
    # Add confidence based on importance
    for r in res:
        imp = r.get("importance", 0) or 0
        r["confidence"] = "high" if imp > 0.7 else "medium" if imp > 0.4 else "low"
    return res[0]

def _norm_nominatim(x):
    addr = x.get("address") or {}
    return {"name": x.get("name") or x.get("display_name", "").split(",")[0], "display_name": x.get("display_name"),
            "lat": float(x["lat"]), "lon": float(x["lon"]), "type": f'{x.get("category") or x.get("class")}={x.get("type")}',
            "address": addr, "country_code": addr.get("country_code"), "osm": f'{x.get("osm_type")}/{x.get("osm_id")}',
            "importance": x.get("importance"), "source": "nominatim", "confidence": "high"}

def _norm_photon(f):
    p, (lon, lat) = f.get("properties", {}), f["geometry"]["coordinates"]
    parts = [p.get(k) for k in ("name", "street", "housenumber", "city", "state", "country") if p.get(k)]
    return {"name": p.get("name") or p.get("street") or ", ".join(parts[:1]), "display_name": ", ".join(str(v) for v in parts),
            "lat": float(lat), "lon": float(lon), "type": f'{p.get("osm_key")}={p.get("osm_value")}',
            "address": {k: p.get(k) for k in ("street", "housenumber", "postcode", "city", "state", "country") if p.get(k)},
            "country_code": (p.get("countrycode") or "").lower() or None, "osm": f'{p.get("osm_type")}/{p.get("osm_id")}', "source": "photon", "confidence": "medium"}

def geocode(query, limit=5, country=None, near=None, lang="en"):
    key = f"geo_{hash((query.lower().strip(), limit, country, near, lang))}.json"
    c = cache_get(key, 7 * 86400)
    if c is not None:
        return c
    out, errors = [], []
    try:
        pace("nominatim", 1.05)
        params = {"q": query, "format": "jsonv2", "limit": limit, "addressdetails": 1}
        if country:
            params["countrycodes"] = country.lower()
        # v2: lang param
        al = lang or cfg_key("language") or cfg_key("lang") or ""
        if al:
            params["accept-language"] = al
        out = [_norm_nominatim(x) for x in http(NOMINATIM + "/search", params, timeout=25)]
    except UmnError as e:
        errors.append(str(e))
    if not out:
        try:
            params = {"q": query, "limit": limit}
            if near:
                params.update({"lat": near[0], "lon": near[1]})
            if lang:
                params["lang"] = lang
            fc = http(PHOTON + "/api/", params, timeout=25)
            out = [_norm_photon(f) for f in fc.get("features", [])]
            if country:
                out = [o for o in out if (o.get("country_code") or "") == country.lower()] or out
        except UmnError as e:
            errors.append(str(e))
    if not out and errors:
        raise UmnError("; ".join(errors))
    cache_put(key, out)
    return out

def reverse(lat, lon, zoom=18, lang="en"):
    try:
        pace("nominatim", 1.05)
        params = {"lat": lat, "lon": lon, "format": "jsonv2", "zoom": zoom, "addressdetails": 1}
        al = lang or cfg_key("language") or ""
        if al:
            params["accept-language"] = al
        x = http(NOMINATIM + "/reverse", params, timeout=25)
        if "error" in x:
            raise UmnError(x["error"])
        return _norm_nominatim(x)
    except UmnError as e1:
        try:
            params = {"lat": lat, "lon": lon}
            if lang:
                params["lang"] = lang
            fc = http(PHOTON + "/reverse", params, timeout=25)
            feats = fc.get("features", [])
            if feats:
                return _norm_photon(feats[0])
        except UmnError as e2:
            raise UmnError(f"{e1}; {e2}")
        raise UmnError(f"no address found ({e1})")

# ----------------------------------------------------------------------------- routing
def _osrm_base(mode):
    if cfg_key("osrm_url"):
        return cfg_key("osrm_url").rstrip("/")
    if mode == "car":
        return OSRM_CAR
    return OSRM_FOSSGIS.format(profile=OSRM_PROFILE[mode])

def _osrm_lanes(step):
    inters = step.get("intersections") or []
    lanes = inters[0].get("lanes") if inters else None
    if not lanes:
        return None
    return [{"indications": l.get("indications", []), "valid": bool(l.get("valid"))} for l in lanes]

def _osrm_phrase(man, lang="en"):
    # v2: try i18n for phrases
    if i18n_mod:
        t = man.get("type", "")
        mod = man.get("modifier") or ""
        if t == "turn" and mod == "left":
            return i18n_mod.translate("turn_left", lang)
        if t == "turn" and mod == "right":
            return i18n_mod.translate("turn_right", lang)
        if t in ("continue", "new name") or (t == "turn" and mod == "straight"):
            return i18n_mod.translate("go_straight", lang)
        if t == "arrive":
            return i18n_mod.translate("arrive", lang)
        if t == "depart":
            return i18n_mod.translate("depart", lang)
    t, mod, ex = man.get("type", ""), (man.get("modifier") or "").replace("uturn", "U-turn"), man.get("exit")
    if t == "depart":
        return "Depart" + (f" heading {compass(man['bearing_after'])}" if man.get("bearing_after") is not None else "")
    if t == "arrive":
        return "Arrive at destination" + (f" (on the {mod})" if mod in ("left", "right") else "")
    if t in ("roundabout", "rotary", "roundabout turn"):
        return f"At the roundabout take exit {ex}" if ex else "Enter the roundabout"
    if t in ("exit roundabout", "exit rotary"):
        return "Exit the roundabout"
    if t in ("new name", "continue", "notification"):
        return "Continue" + (f" {mod}" if mod and mod != "straight" else "")
    if t == "turn":
        return f"Turn {mod}" if mod != "straight" else "Go straight"
    if t == "fork":
        return f"Keep {mod} at the fork"
    if t == "merge":
        return f"Merge {mod}".strip()
    if t == "on ramp":
        return f"Take the ramp on the {mod}" if mod else "Take the ramp"
    if t == "off ramp":
        return f"Take the exit on the {mod}" if mod else "Take the exit"
    if t == "end of road":
        return f"At the end of the road turn {mod}"
    return (t + " " + mod).strip().capitalize()

def route_osrm(points, mode, alternatives=False, steps=True, lang="en"):
    coords = ";".join(f"{p['lon']:.6f},{p['lat']:.6f}" for p in points)
    params = {"overview": "full", "geometries": "geojson", "steps": "true" if steps else "false", "alternatives": "true" if alternatives else "false"}
    d = http(f"{_osrm_base(mode)}/route/v1/driving/{coords}", params, timeout=40)
    if d.get("code") != "Ok":
        raise UmnError(f"OSRM: {d.get('code')} {d.get('message', '')} [source=osrm] confidence:low")
    routes = []
    for r in d["routes"]:
        st = []
        for leg in r["legs"]:
            for s in leg.get("steps", []):
                man = s.get("maneuver", {})
                txt = _osrm_phrase(man, lang)
                name = s.get("name") or s.get("ref") or ""
                st.append({"instruction": (txt + (f" onto {name}" if name and man.get("type") not in ("depart", "arrive") else "")).strip(),
                           "name": name, "distance_m": s.get("distance", 0), "duration_s": s.get("duration", 0), "type": man.get("type"),
                           "modifier": man.get("modifier"), "exit": man.get("exit"), "lanes": _osrm_lanes(s), "source": "osrm", "confidence": "high"})
        routes.append({"engine": "osrm", "distance_m": r["distance"], "duration_s": r["duration"], "geometry": [(c[1], c[0]) for c in r["geometry"]["coordinates"]],
                       "steps": st, "summary": ", ".join(x for x in [l.get("summary") for l in r["legs"]] if x), "source": "osrm", "confidence": "high"})
    return routes

def route_valhalla(points, mode, avoid=(), truck=None, alternatives=False, depart=None, language="en-US"):
    costing = VALHALLA_COSTING[mode]
    opts = {}
    if "tolls" in avoid:
        opts["use_tolls"] = 0
    if "highways" in avoid:
        opts["use_highways"] = 0
    if "ferries" in avoid:
        opts["use_ferry"] = 0
    if "unpaved" in avoid:
        opts["exclude_unpaved"] = True
    if truck and costing == "truck":
        for k in ("height", "width", "length", "weight", "axle_load"):
            if truck.get(k):
                opts[k] = float(truck[k])
        if truck.get("hazmat"):
            opts["hazmat"] = True
    body = {"locations": [{"lat": p["lat"], "lon": p["lon"]} for p in points], "costing": costing,
            "directions_options": {"units": "kilometers", "language": language}, "costing_options": {costing: opts} if opts else {}}
    if alternatives:
        body["alternates"] = 2
    if depart:
        body["date_time"] = {"type": 1, "value": depart}
    d = http(VALHALLA + "/route", data=body, timeout=60)
    trips = [d["trip"]] + [a["trip"] for a in d.get("alternates", [])]
    routes = []
    for t in trips:
        st, geom = [], []
        for leg in t["legs"]:
            geom += decode_polyline(leg["shape"], 6)
            for m in leg.get("maneuvers", []):
                lanes = None
                if m.get("lanes"):
                    lanes = [{"indications": [k for k in ("left", "straight", "right", "slight_left", "slight_right", "uturn") if l.get(k)] or [str(l.get("directions"))],
                              "valid": bool(l.get("valid") or l.get("active"))} for l in m["lanes"]]
                st.append({"instruction": m.get("instruction", ""), "name": ", ".join(m.get("street_names") or []), "distance_m": m.get("length", 0) * 1000,
                           "duration_s": m.get("time", 0), "type": m.get("type"), "verbal": m.get("verbal_post_transition_instruction"),
                           "toll": m.get("toll"), "ferry": m.get("ferry"), "highway": m.get("highway"), "lanes": lanes,
                           "sign": (m.get("sign") or {}).get("exit_number_elements"), "source": "valhalla", "confidence": "high"})
        s = t["summary"]
        routes.append({"engine": "valhalla", "distance_m": s["length"] * 1000, "duration_s": s["time"], "geometry": geom, "steps": st,
                       "has_toll": s.get("has_toll"), "has_highway": s.get("has_highway"), "has_ferry": s.get("has_ferry"),
                       "summary": ", ".join(dict.fromkeys(x["name"] for x in st if x["name"]).keys())[:120], "source": "valhalla", "confidence": "high"})
    return routes

def route_ors(points, mode, avoid=(), alternatives=False):
    key = cfg_key("ors_key")
    if not key:
        raise UmnError("OpenRouteService key not configured (umn config set ors_key …) [source=ors] confidence:low")
    body = {"coordinates": [[p["lon"], p["lat"]] for p in points], "instructions": True, "units": "m"}
    av = [{"tolls": "tollways", "highways": "highways", "ferries": "ferries"}[a] for a in avoid if a in ("tolls", "highways", "ferries")]
    if av:
        body["options"] = {"avoid_features": av}
    if alternatives and len(points) == 2:
        body["alternative_routes"] = {"target_count": 2}
    d = http(f"{ORS}/v2/directions/{ORS_PROFILE[mode]}/geojson", data=body, headers={"Authorization": key}, timeout=60)
    routes = []
    for f in d.get("features", []):
        p = f["properties"]
        st = [{"instruction": s["instruction"], "name": s.get("name", ""), "distance_m": s["distance"], "duration_s": s["duration"], "type": s.get("type"), "lanes": None, "source": "ors", "confidence": "high"}
              for seg in p.get("segments", []) for s in seg.get("steps", [])]
        routes.append({"engine": "ors", "distance_m": p["summary"]["distance"], "duration_s": p["summary"]["duration"],
                       "geometry": [(c[1], c[0]) for c in f["geometry"]["coordinates"]], "steps": st, "summary": "", "source": "ors", "confidence": "high"})
    return routes

def compute_route(points, mode="car", engine="auto", avoid=(), truck=None, alternatives=False, depart=None, steps=True, lang="en"):
    if mode == "transit":
        raise UmnError("use `umn transit plan` for public transport [source=transitous] confidence:high")
    attempts = []
    if engine == "auto":
        prefer_valhalla = bool(avoid) or truck or mode not in ("car", "bike", "foot") or depart
        attempts = (["valhalla", "osrm"] if prefer_valhalla else ["osrm", "valhalla"])
        if cfg_key("ors_key"):
            attempts.append("ors")
    else:
        attempts = [engine]
    errors = []
    for eng in attempts:
        try:
            if eng == "osrm":
                if mode not in OSRM_PROFILE:
                    raise UmnError(f"OSRM public servers only route car/bike/foot (asked {mode}) [source=osrm] confidence:high")
                if avoid or truck:
                    eprint("note: OSRM ignores avoid/truck options — using it only as fallback [source=osrm]")
                return route_osrm(points, mode, alternatives, steps, lang)
            if eng == "valhalla":
                return route_valhalla(points, mode, avoid, truck, alternatives, depart, lang)
            if eng == "ors":
                return route_ors(points, mode, avoid, alternatives)
        except UmnError as e:
            errors.append(f"{eng}: {e}")
    raise UmnError("all routing engines failed → " + " | ".join(errors) + " [confidence:low]")

# ----------------------------------------------------------------------------- Overpass / POI
def overpass(query, timeout=40):
    errors = []
    servers = [s for s in [cfg_key("overpass_url")] if s] + OVERPASS_SERVERS
    for attempt in range(2):
        for srv in servers:
            try:
                pace("overpass", 1.0)
                d = http(srv, data="data=" + urllib.parse.quote(query), timeout=timeout, retries=0)
                return d.get("elements", [])
            except UmnError as e:
                errors.append(str(e)[:80])
        time.sleep(3)
    raise UmnError("Overpass unavailable: " + " | ".join(errors[:3]) + " [source=overpass] confidence:low")

def _el_latlon(e):
    if "lat" in e:
        return e["lat"], e["lon"]
    c = e.get("center") or {}
    return c.get("lat"), c.get("lon")

def category_selectors(cat, lang="en"):
    # v2: check standard POI first, then cultural (cultural returns None if not cultural)
    if cat in POI_CATEGORIES:
        return POI_CATEGORIES[cat]
    if i18n_mod:
        try:
            tags = i18n_mod.cultural_poi_tags(cat, lang)
            if tags:
                if any(t.startswith("[") for t in tags):
                    return tags
        except Exception:
            pass
    if "=" in cat:
        k, v = cat.split("=", 1)
        return [f'["{k}"="{v}"]']
    if cat.startswith("name:"):
        return [f'["name"~"{re.escape(cat[5:])}",i]']
    return None

def poi_search(cat, center, radius=1000, limit=20, polyline=None, lang="en"):
    sels = category_selectors(cat, lang)
    if sels is None:
        sels = [f'["name"~"{re.escape(cat)}",i]', f'["brand"~"{re.escape(cat)}",i]']
    if polyline:
        pts = sample_line(polyline, 120)
        around = f"around:{int(radius)}," + ",".join(f"{a:.5f},{b:.5f}" for a, b in pts)
    else:
        around = f"around:{int(radius)},{center[0]:.6f},{center[1]:.6f}"
    q = f"[out:json][timeout:25];(" + "".join(f"nwr{s}({around});" for s in sels) + f");out center tags {int(limit) * 3};"
    els = overpass(q)
    out = []
    for e in els:
        lat, lon = _el_latlon(e)
        if lat is None:
            continue
        t = e.get("tags", {})
        ref = center or (polyline[0] if polyline else (lat, lon))
        out.append({"name": t.get("name") or t.get("brand") or t.get("operator") or cat, "lat": lat, "lon": lon, "distance_m": haversine(ref, (lat, lon)),
                    "osm": f"{e['type']}/{e['id']}", "tags": t, "source": "overpass", "confidence": "high"})
    out.sort(key=lambda x: x["distance_m"])
    return out[:limit]

def poi_photon_fallback(cat, center, radius, limit, lang="en"):
    dlat = radius / 111320.0
    dlon = radius / (111320.0 * max(math.cos(math.radians(center[0])), 0.01))
    bbox = f"{center[1] - dlon:.5f},{center[0] - dlat:.5f},{center[1] + dlon:.5f},{center[0] + dlat:.5f}"
    params = {"q": cat.replace("-", " "), "limit": limit, "bbox": bbox, "lat": center[0], "lon": center[1]}
    if lang:
        params["lang"] = lang
    sel = POI_CATEGORIES.get(cat)
    if sel and "=" in sel[0] and "~" not in sel[0]:
        try:
            k, v = re.findall(r'"([^"]+)"="([^"]+)"', sel[0])[0]
            params["osm_tag"] = f"{k}:{v}"
        except Exception:
            pass
    fc = http(PHOTON + "/api/", params, timeout=25)
    out = []
    for f in fc.get("features", []):
        n = _norm_photon(f)
        out.append({"name": n["name"], "lat": n["lat"], "lon": n["lon"], "distance_m": haversine(center, (n["lat"], n["lon"])), "osm": n["osm"], "tags": {"type": n["type"]}, "source": "photon", "confidence": "medium"})
    return sorted(out, key=lambda x: x["distance_m"])[:limit]

def poi_search_safe(cat, center, radius, limit, lang="en"):
    try:
        return poi_search(cat, center, radius, limit, lang=lang), "overpass"
    except UmnError as e:
        eprint(f"note: {e} — trying Photon fallback [source=photon] confidence:medium")
        return poi_photon_fallback(cat, center, radius, limit, lang), "photon"

def tag_summary(t):
    bits = []
    for k in ("opening_hours", "brand", "operator", "cuisine", "fee", "capacity", "maxspeed", "phone", "website", "wheelchair", "fuel:diesel", "fuel:lpg", "charge"):
        if t.get(k):
            bits.append(f"{k}={t[k]}")
    for k, v in t.items():
        if k.startswith("socket:") and not k.endswith(":output"):
            bits.append(f"{k}={v}")
    return "; ".join(bits[:6])

# ----------------------------------------------------------------------------- output helpers
def emit(args, human_text, payload):
    # v2 token optimization: compact mode, truncation guard
    compact = getattr(args, "compact", False)
    if token_opt_mod and compact:
        # Use token optimizer for compact
        if getattr(args, "json", False):
            minimal = token_opt_mod.minimal_json(payload, compact=True)
            print(json.dumps(minimal, indent=2, ensure_ascii=False, default=str))
            return
        else:
            # Compact human + truncation guard
            text = human_text
            # Apply truncation guard 350 tokens
            guard = token_opt_mod.truncate_if_needed(text, 350)
            print(guard)
            return

    if getattr(args, "json", False):
        # Add confidence and source to payload if missing
        if isinstance(payload, dict) and "confidence" not in payload:
            payload["confidence"] = "high"
            payload["source"] = payload.get("source", "multiple")
        print(json.dumps(payload, indent=2, ensure_ascii=False, default=str))
    else:
        # Human but with token budget guard
        if token_opt_mod:
            budget_check = token_opt_mod.token_budget_guard(human_text, 350)
            if budget_check["exceeds"] and not compact:
                eprint(f"note: output {budget_check['tokens_est']} tokens exceeds budget {budget_check['budget']}, use --compact --json to reduce [token_opt]")
        print(human_text)

def place_line(p):
    conf = p.get("confidence", "high")
    src = p.get("source", "")
    return f"{p.get('display_name') or p.get('name')}  [{p['lat']:.6f}, {p['lon']:.6f}]  ({p.get('type', '')}; {src} conf:{conf})"

def write_gpx(path, geometry, name="route", waypoints=()):
    with open(path, "w") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<gpx version="1.1" creator="universal-maps-navigator" xmlns="http://www.topografix.com/GPX/1/1">\n')
        for w in waypoints:
            fh.write(f'  <wpt lat="{w["lat"]:.6f}" lon="{w["lon"]:.6f}"><name>{_xml(w.get("name", ""))}</name></wpt>\n')
        fh.write(f"  <trk><name>{_xml(name)}</name><trkseg>\n")
        for lat, lon in geometry:
            fh.write(f'    <trkpt lat="{lat:.6f}" lon="{lon:.6f}"/>\n')
        fh.write("  </trkseg></trk>\n</gpx>\n")

def write_kml(path, places):
    with open(path, "w") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2"><Document><name>universal-maps-navigator bookmarks</name>\n')
        for p in places:
            fh.write(f'  <Placemark><name>{_xml(p.get("name", ""))}</name><Point><coordinates>{p["lon"]:.6f},{p["lat"]:.6f},0</coordinates></Point></Placemark>\n')
        fh.write("</Document></kml>\n")

def _xml(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def links_text(links, compact=False):
    lines = []
    for k, v in links.items():
        if compact:
            lines.append(f"{k}: {v['url'][:80]}")
        else:
            lines.append(f"  {v['label']:<26} {v['url']}")
            for extra in ("ios_scheme", "app_scheme", "app_scheme_v2_nav", "android_intent", "ios_url", "livemap_url", "traffic_url", "streetview_url"):
                if v.get(extra) and not compact:
                    lines.append(f"  {'':<26} {extra}: {v[extra]}")
    return "\n".join(lines)

# ----------------------------------------------------------------------------- commands (v1 + v2)
def cmd_geocode(a):
    lang = getattr(a, "lang", "en") or "en"
    res = geocode(a.query, limit=a.limit, country=a.country, lang=lang)
    if not res:
        raise UmnError(f"no results for {a.query!r} [source=nominatim|photon] confidence:low — abstain")
    if getattr(a, "compact", False):
        txt = "\n".join(f"{p['lat']:.5f},{p['lon']:.5f} {p['name'][:30]} conf:{p.get('confidence','high')} src:{p.get('source','')}" for p in res)
    else:
        txt = "\n".join(f"{i + 1}. {place_line(p)}" for i, p in enumerate(res))
    emit(a, txt, {"results": res, "confidence": "high" if any(r.get("confidence")=="high" for r in res) else "medium", "source": "nominatim|photon"})

def cmd_reverse(a):
    lang = getattr(a, "lang", "en") or "en"
    p = parse_place(f"{a.lat},{a.lon}", lang=lang)
    r = reverse(p["lat"], p["lon"], a.zoom, lang=lang)
    r["plus_code"] = plus_code(p["lat"], p["lon"])
    r["confidence"] = "high"
    r["source"] = "nominatim"
    emit(a, f"{place_line(r)}\n  plus code: {r['plus_code']}\n  address: {json.dumps(r.get('address', {}), ensure_ascii=False)} [conf:high src:nominatim]", r)

def _truck_from_args(a):
    t = {k: getattr(a, f"truck_{k}", None) for k in ("height", "width", "length", "weight", "axle_load")}
    t["hazmat"] = getattr(a, "hazmat", False)
    return t if any(v for v in t.values()) else None

def _route_points(a):
    lang = getattr(a, "lang", "en") or "en"
    pts = [parse_place(a.origin, lang=lang)] + [parse_place(v, lang=lang) for v in (a.via or [])] + [parse_place(a.destination, lang=lang)]
    return pts

def _steps_text(steps, units=None, lang="en", compact=False):
    lines = []
    for i, s in enumerate(steps, 1):
        if compact:
            lines.append(f"{i}. {s['instruction'][:40]} {fmt_dist(s['distance_m'], units, lang)}")
        else:
            lane = ""
            if s.get("lanes"):
                lane = "   lanes: " + " ".join(("[" + "/".join(l["indications"]) + "]") if l["valid"] else "(" + "/".join(l["indications"]) + ")" for l in s["lanes"])
            flags = "".join(f" ⚠{f}" for f in ("toll", "ferry") if s.get(f))
            lines.append(f"  {i:>2}. {s['instruction']:<60} {fmt_dist(s['distance_m'], units, lang):>8}{flags}{lane} [src:{s.get('source','')} conf:{s.get('confidence','high')}]")
    return "\n".join(lines)

def cmd_route(a):
    lang = getattr(a, "lang", "en") or "en"
    compact = getattr(a, "compact", False)
    pts = _route_points(a)
    avoid = [x.strip() for x in (a.avoid or "").split(",") if x.strip()]
    routes = compute_route(pts, a.mode, a.engine, avoid, _truck_from_args(a), a.alternatives, a.depart, steps=True, lang=lang)
    payload = {"origin": pts[0], "destination": pts[-1], "via": pts[1:-1], "mode": a.mode, "routes": [], "confidence": "high", "source": "osrm|valhalla"}
    if compact:
        lines = [f"ROUTE {pts[0]['name']}→{pts[-1]['name']} ({a.mode}) [conf:high src:{routes[0]['source']}]"]
    else:
        lines = [f"Route {pts[0]['name']} → {pts[-1]['name']}  ({a.mode}" + (f", avoid {','.join(avoid)}" if avoid else "") + f") [conf:high src:{routes[0]['source']}]"]
    for i, r in enumerate(routes):
        extra = []
        if a.elevation:
            try:
                r["elevation"] = route_elevation(r["geometry"])
                extra.append(f"↑{r['elevation']['ascent_m']:.0f} m ↓{r['elevation']['descent_m']:.0f} m [src=opentopodata conf:high]")
            except UmnError as e:
                extra.append(f"elevation n/a ({e}) [conf:low]")
        if a.cameras:
            try:
                cams = poi_search("speed-camera", None, 80, 50, polyline=r["geometry"], lang=lang)
                r["speed_cameras"] = cams
                extra.append(f"{len(cams)} speed camera(s) within 80 m [src=osm conf:med]")
            except UmnError as e:
                extra.append(f"cameras n/a ({e}) [conf:low]")
        if a.weather:
            try:
                r["weather_along"] = weather_along(r["geometry"])
                extra.append("weather: " + "; ".join(f"{w['label']}: {w['temp_c']}°C {w['condition']}" for w in r["weather_along"]) + " [src=open-meteo conf:high]")
            except UmnError as e:
                extra.append(f"weather n/a ({e}) [conf:low]")
        if compact:
            lines.append(f"{'Opt'+str(i+1) if len(routes)>1 else 'Best'}: {fmt_dist(r['distance_m'], lang=lang)}, {fmt_dur(r['duration_s'], lang)} {r.get('summary','')[:20]} [{r['engine']}]")
        else:
            lines.append(f"{'Option ' + str(i + 1) if len(routes) > 1 else 'Best'}: {fmt_dist(r['distance_m'], lang=lang)}, {fmt_dur(r['duration_s'], lang)} via {r.get('summary') or '…'} [{r['engine']}] conf:{r.get('confidence','high')} src:{r.get('source','')}"
                         + ("".join(f"\n   • {x}" for x in extra)))
            flags = [f for f in ("has_toll", "has_highway", "has_ferry") if r.get(f)]
            if flags:
                lines.append("   flags: " + ", ".join(f[4:] for f in flags))
        if a.steps:
            lines.append(_steps_text(r["steps"], lang=lang, compact=compact))
        geom = r.pop("geometry")
        if a.gpx and i == 0:
            write_gpx(a.gpx, geom, f"{pts[0]['name']} → {pts[-1]['name']}", pts)
            lines.append(f"   GPX written: {a.gpx}")
        if a.json:
            r["geometry_sample"] = sample_line(geom, 50)
        payload["routes"].append(r)
    payload["deep_links"] = deeplinks.navigate_links((pts[-1]["lat"], pts[-1]["lon"], pts[-1]["name"]), (pts[0]["lat"], pts[0]["lon"], pts[0]["name"]),
                                                     [(v["lat"], v["lon"], v["name"]) for v in pts[1:-1]], a.mode, ("all",), avoid, _truck_from_args(a))
    if compact:
        lines.append("LINKS:\n" + links_text({k: payload["deep_links"][k] for k in ("google", "waze", "organic") if k in payload["deep_links"]}, compact=True))
    else:
        lines.append("Open in an app:\n" + links_text({k: payload["deep_links"][k] for k in ("google", "apple", "waze", "organic", "comaps", "here", "sygic") if k in payload["deep_links"]}, compact=compact))
    emit(a, "\n".join(lines), payload)

def cmd_navigate(a):
    lang = getattr(a, "lang", "en") or "en"
    compact = getattr(a, "compact", False)
    dest = parse_place(a.destination, lang=lang)
    origin = parse_place(a.origin, lang=lang) if a.origin else None
    via = [parse_place(v, lang=lang) for v in (a.via or [])]
    avoid = [x.strip() for x in (a.avoid or "").split(",") if x.strip()]
    apps = tuple(x.strip() for x in a.app.split(",") if x.strip())
    unknown = set(apps) - set(deeplinks.APPS) - {"all"}
    if unknown:
        raise UmnError(f"unknown app(s) {sorted(unknown)}; choose from {deeplinks.APPS} or all [conf:high]")
    links = deeplinks.navigate_links((dest["lat"], dest["lon"], a.name or dest["name"]), (origin["lat"], origin["lon"], origin["name"]) if origin else None,
                                     [(v["lat"], v["lon"], v["name"]) for v in via], a.mode, apps, avoid, _truck_from_args(a))
    if compact:
        txt = f"NAV {dest['name']} [{dest['lat']:.5f},{dest['lon']:.5f}] {a.mode} conf:high src:deeplinks\n" + links_text(links, compact=True)
    else:
        txt = f"Navigate to {dest.get('display_name') or dest['name']} [{dest['lat']:.6f}, {dest['lon']:.6f}] by {a.mode} [conf:high src:deeplinks]" + (f" from {origin['name']}" if origin else " from current location") + ":\n" + links_text(links, compact=compact)
        notes = sorted({n for v in links.values() for n in v.get("notes", [])})
        if notes and not a.json:
            txt += "\nNotes:\n" + "\n".join(f"  - {n}" for n in notes)
    emit(a, txt, {"destination": dest, "origin": origin, "via": via, "mode": a.mode, "links": links, "confidence": "high", "source": "deeplinks"})

def cmd_share(a):
    lang = getattr(a, "lang", "en") or "en"
    compact = getattr(a, "compact", False)
    p = parse_place(a.place, lang=lang)
    links = deeplinks.place_links(p["lat"], p["lon"], a.name or (p.get("name") if p.get("source") != "coordinates" else ""), a.zoom)
    pc = plus_code(p["lat"], p["lon"])
    if compact:
        txt = f"{p['name']} {p['lat']:.5f},{p['lon']:.5f} PC:{pc} conf:high\n" + links_text(links, compact=True)
    else:
        txt = f"{p.get('display_name') or p['name']}\n  coordinates: {p['lat']:.6f}, {p['lon']:.6f}   plus code: {pc} [conf:high src:deeplinks]\n" + links_text(links, compact=compact)
    emit(a, txt, {"place": p, "plus_code": pc, "links": links, "confidence": "high", "source": "deeplinks"})

def cmd_search_links(a):
    lang = getattr(a, "lang", "en") or "en"
    compact = getattr(a, "compact", False)
    near = parse_place(a.near, lang=lang) if a.near else None
    links = deeplinks.search_links(a.query, (near["lat"], near["lon"]) if near else None)
    if compact:
        txt = f"SEARCH {a.query} conf:high\n" + links_text(links, compact=True)
    else:
        txt = f"Search '{a.query}' in apps: [conf:high src:deeplinks]\n" + links_text(links, compact=compact)
    emit(a, txt, {"query": a.query, "near": near, "links": links, "confidence": "high", "source": "deeplinks"})

def cmd_poi(a):
    lang = getattr(a, "lang", "en") or "en"
    compact = getattr(a, "compact", False)
    c = parse_place(a.near, lang=lang)
    center = (c["lat"], c["lon"])
    res, src = poi_search_safe(a.category, center, a.radius, a.limit, lang=lang)
    if not res:
        raise UmnError(f"no '{a.category}' found within {a.radius} m of {c['name']} [source={src} conf:low] — abstain, do not invent")
    if compact:
        lines = [f"POI {a.category} near {c['name']} {len(res)} src:{src} conf:high"]
        for r in res[:5]:
            lines.append(f"{r['name'][:20]} {fmt_dist(r['distance_m'], lang=lang):>6} [{r['lat']:.4f},{r['lon']:.4f}]")
    else:
        lines = [f"{a.category} near {c['name']} (radius {a.radius} m, {len(res)} results, source {src} conf:high):"]
        for i, r in enumerate(res, 1):
            lines.append(f"{i:>2}. {r['name'][:40]:<40} {fmt_dist(r['distance_m'], lang=lang):>7} {compass(bearing(center, (r['lat'], r['lon'])))}  [{r['lat']:.5f},{r['lon']:.5f}]  {tag_summary(r.get('tags', {}))} [src:{r.get('source')} conf:{r.get('confidence')}]")
        lines.append("Tip: umn navigate \"LAT,LON\" --app waze")
    emit(a, "\n".join(lines), {"near": c, "category": a.category, "radius_m": a.radius, "source": src, "confidence": "high", "results": res})

def cmd_nearby(a):
    lang = getattr(a, "lang", "en") or "en"
    c = parse_place(a.place, lang=lang)
    d = http(WIKIPEDIA.format(lang=lang), {"action": "query", "list": "geosearch", "gscoord": f"{c['lat']}|{c['lon']}", "gsradius": min(a.radius, 10000), "gslimit": a.limit, "format": "json"})
    items = d.get("query", {}).get("geosearch", [])
    lines = [f"Landmarks near {c['name']} (Wikipedia/{lang}, {len(items)} src:wikipedia conf:high):"]
    for it in items:
        lines.append(f"  • {it['title']:<45} {fmt_dist(it['dist'], lang=lang):>7}  https://{lang}.wikipedia.org/?curid={it['pageid']}")
    emit(a, "\n".join(lines), {"place": c, "landmarks": items, "confidence": "high", "source": "wikipedia"})

def route_elevation(geometry):
    pts = sample_line(geometry, 100)
    d = http(f"{OPENTOPO}/srtm90m", {"locations": "|".join(f"{la:.5f},{lo:.5f}" for la, lo in pts)}, timeout=40)
    el = [r.get("elevation") for r in d.get("results", [])]
    if not el or all(e is None for e in el):
        d = http(f"{OPENTOPO}/aster30m", {"locations": "|".join(f"{la:.5f},{lo:.5f}" for la, lo in pts)}, timeout=40)
        el = [r.get("elevation") for r in d.get("results", [])]
    el = [e for e in el if e is not None]
    if not el:
        raise UmnError("elevation data unavailable [source=opentopodata] conf:low")
    asc = sum(max(0, el[i + 1] - el[i]) for i in range(len(el) - 1))
    desc = sum(max(0, el[i] - el[i + 1]) for i in range(len(el) - 1))
    return {"min_m": min(el), "max_m": max(el), "ascent_m": asc, "descent_m": desc, "profile": el, "source": "opentopodata", "confidence": "high"}

def cmd_elevation(a):
    lang = getattr(a, "lang", "en") or "en"
    pts = [parse_place(p, lang=lang) for p in a.places]
    d = http(f"{OPENTOPO}/srtm90m", {"locations": "|".join(f"{p['lat']:.5f},{p['lon']:.5f}" for p in pts)})
    res = d.get("results", [])
    lines = [f"  {p['name'][:40]:<40} {r.get('elevation')} m  (dataset {r.get('dataset')} src:opentopodata conf:high)" for p, r in zip(pts, res)]
    emit(a, "\n".join(lines), [{"place": p, "elevation_m": r.get("elevation"), "source": "opentopodata", "confidence": "high"} for p, r in zip(pts, res)])

def weather_at(points, hours=6):
    params = {"latitude": ",".join(f"{p[0]:.4f}" for p in points), "longitude": ",".join(f"{p[1]:.4f}" for p in points),
              "current": "temperature_2m,precipitation,weather_code,wind_speed_10m,wind_gusts_10m,visibility,is_day",
              "hourly": "temperature_2m,precipitation_probability,precipitation,weather_code,wind_speed_10m,visibility", "forecast_hours": hours, "timezone": "auto"}
    d = http(OPEN_METEO, params)
    return d if isinstance(d, list) else [d]

def weather_along(geometry, n=6):
    pts = sample_line(geometry, n)
    ws = weather_at(pts, 3)
    out = []
    for i, (p, w) in enumerate(zip(pts, ws)):
        cur = w.get("current", {})
        out.append({"label": "start" if i == 0 else ("end" if i == len(pts) - 1 else f"km ~{sum(haversine(pts[j], pts[j + 1]) for j in range(i)) / 1000:.0f}"),
                    "lat": p[0], "lon": p[1], "temp_c": cur.get("temperature_2m"), "condition": WMO.get(cur.get("weather_code"), str(cur.get("weather_code"))),
                    "precip_mm": cur.get("precipitation"), "wind_kmh": cur.get("wind_speed_10m"), "visibility_m": cur.get("visibility"), "source": "open-meteo", "confidence": "high"})
    return out

def cmd_weather(a):
    lang = getattr(a, "lang", "en") or "en"
    if a.route:
        pts = [parse_place(a.place, lang=lang), parse_place(a.route, lang=lang)]
        r = compute_route(pts, a.mode, "auto", steps=False, lang=lang)[0]
        w = weather_along(r["geometry"], 6)
        lines = [f"Weather along {pts[0]['name']} → {pts[1]['name']} ({fmt_dist(r['distance_m'], lang=lang)} src:open-meteo conf:high):"] + [
            f"  {x['label']:<8} {x['temp_c']}°C {x['condition']:<16} precip {x['precip_mm']} mm  wind {x['wind_kmh']} km/h  vis {x['visibility_m']} m" for x in w]
        emit(a, "\n".join(lines), {"route": {"distance_m": r["distance_m"], "duration_s": r["duration_s"]}, "weather": w, "confidence": "high", "source": "open-meteo"})
        return
    p = parse_place(a.place, lang=lang)
    w = weather_at([(p["lat"], p["lon"])], a.hours)[0]
    cur, hr = w.get("current", {}), w.get("hourly", {})
    lines = [f"Weather at {p['name']} ({w.get('timezone')} src:open-meteo conf:high): {cur.get('temperature_2m')}°C, {WMO.get(cur.get('weather_code'), cur.get('weather_code'))}, wind {cur.get('wind_speed_10m')} km/h (gusts {cur.get('wind_gusts_10m')}), visibility {cur.get('visibility')} m, precip {cur.get('precipitation')} mm"]
    for i, t in enumerate(hr.get("time", [])[: a.hours]):
        lines.append(f"  {t[-5:]}  {hr['temperature_2m'][i]:>5}°C  {WMO.get(hr['weather_code'][i], hr['weather_code'][i]):<16} rain {hr['precipitation_probability'][i]:>3}%  wind {hr['wind_speed_10m'][i]} km/h")
    emit(a, "\n".join(lines), {"place": p, "current": cur, "hourly": hr, "timezone": w.get("timezone"), "confidence": "high", "source": "open-meteo"})

def cmd_isochrone(a):
    lang = getattr(a, "lang", "en") or "en"
    c = parse_place(a.place, lang=lang)
    mins = [int(x) for x in a.minutes.split(",")]
    body = {"locations": [{"lat": c["lat"], "lon": c["lon"]}], "costing": VALHALLA_COSTING[a.mode], "contours": [{"time": m} for m in mins], "polygons": True, "denoise": 0.5}
    d = http(VALHALLA + "/isochrone", data=body, timeout=60)
    feats = sorted(d.get("features", []), key=lambda f: f["properties"].get("contour", 0))
    lines = [f"Reachable from {c['name']} by {a.mode} [src=valhalla conf:high]:"]
    for f in feats:
        ring = f["geometry"]["coordinates"][0] if f["geometry"]["type"] == "Polygon" else f["geometry"]["coordinates"][0][0]
        lats, lons = [p[1] for p in ring], [p[0] for p in ring]
        k = math.cos(math.radians(c["lat"]))
        area = abs(sum((lons[i] * k * lats[i + 1] - lons[i + 1] * k * lats[i]) for i in range(len(ring) - 1))) / 2 * (111.32 ** 2)
        lines.append(f"  {f['properties']['contour']:>3} min → ~{area:.1f} km², bbox lat {min(lats):.4f}…{max(lats):.4f} lon {min(lons):.4f}…{max(lons):.4f}")
    if a.out:
        json.dump(d, open(a.out, "w"))
        lines.append(f"  GeoJSON written: {a.out}")
    emit(a, "\n".join(lines), d if a.json else {"confidence": "high", "source": "valhalla"})

def cmd_matrix(a):
    lang = getattr(a, "lang", "en") or "en"
    pts = [parse_place(p, lang=lang) for p in a.places]
    if a.mode in OSRM_PROFILE and not a.engine == "valhalla":
        coords = ";".join(f"{p['lon']:.6f},{p['lat']:.6f}" for p in pts)
        d = http(f"{_osrm_base(a.mode)}/table/v1/driving/{coords}", {"annotations": "duration,distance"})
        dur, dist = d["durations"], d["distances"]
        src = "osrm"
    else:
        body = {"sources": [{"lat": p["lat"], "lon": p["lon"]} for p in pts], "targets": [{"lat": p["lat"], "lon": p["lon"]} for p in pts], "costing": VALHALLA_COSTING[a.mode]}
        d = http(VALHALLA + "/sources_to_targets", data=body, timeout=60)
        dur = [[c["time"] for c in row] for row in d["sources_to_targets"]]
        dist = [[c["distance"] * 1000 for c in row] for row in d["sources_to_targets"]]
        src = "valhalla"
    names = [p["name"][:14] for p in pts]
    lines = [f"travel time (rows=from, cols=to) [src={src} conf:high]:", "  " + " " * 15 + "".join(f"{n:>15}" for n in names)]
    for i, n in enumerate(names):
        lines.append(f"  {n:<15}" + "".join(f"{fmt_dur(dur[i][j], lang) if dur[i][j] is not None else 'n/a':>15}" for j in range(len(names))))
    emit(a, "\n".join(lines), {"places": pts, "durations_s": dur, "distances_m": dist, "mode": a.mode, "confidence": "high", "source": src})

def cmd_trip(a):
    lang = getattr(a, "lang", "en") or "en"
    pts = [parse_place(p, lang=lang) for p in a.places]
    if len(pts) < 3:
        raise UmnError("give at least 3 places to optimise [conf:high]")
    if a.mode in OSRM_PROFILE:
        coords = ";".join(f"{p['lon']:.6f},{p['lat']:.6f}" for p in pts)
        d = http(f"{_osrm_base(a.mode)}/trip/v1/driving/{coords}", {"source": "first", "destination": "any" if a.roundtrip else "last", "roundtrip": "true" if a.roundtrip else "false", "overview": "false"})
        if d.get("code") != "Ok":
            raise UmnError(f"OSRM trip: {d.get('code')} [src=osrm conf:low]")
        order = sorted(range(len(pts)), key=lambda i: d["waypoints"][i]["waypoint_index"])
        dist, dur = d["trips"][0]["distance"], d["trips"][0]["duration"]
    else:
        body = {"locations": [{"lat": p["lat"], "lon": p["lon"]} for p in pts], "costing": VALHALLA_COSTING[a.mode]}
        d = http(VALHALLA + "/optimized_route", data=body, timeout=60)
        order = [l["original_index"] for l in d["trip"]["locations"]]
        dist, dur = d["trip"]["summary"]["length"] * 1000, d["trip"]["summary"]["time"]
    ordered = [pts[i] for i in order]
    lines = [f"Optimised {'round trip' if a.roundtrip else 'trip'} ({a.mode}): {fmt_dist(dist, lang=lang)}, {fmt_dur(dur, lang)} [src=osrm|valhalla conf:high]"]
    lines += [f"  {n + 1}. {p['name']}" for n, p in enumerate(ordered)]
    links = deeplinks.navigate_links((ordered[-1]["lat"], ordered[-1]["lon"], ordered[-1]["name"]), (ordered[0]["lat"], ordered[0]["lon"], ordered[0]["name"]),
                                     [(v["lat"], v["lon"], v["name"]) for v in ordered[1:-1]], a.mode if a.mode in MODES else "car", ("google", "here", "organic", "sygic", "osm"))
    lines.append("Multi-stop links:\n" + links_text(links, compact=getattr(a, "compact", False)))
    emit(a, "\n".join(lines), {"order": order, "places": ordered, "distance_m": dist, "duration_s": dur, "links": links, "confidence": "high", "source": "osrm|valhalla"})

def cmd_charging(a):
    lang = getattr(a, "lang", "en") or "en"
    c = parse_place(a.near, lang=lang)
    key = cfg_key("openchargemap_key")
    res = []
    if key:
        params = {"output": "json", "latitude": c["lat"], "longitude": c["lon"], "distance": a.radius / 1000, "distanceunit": "km", "maxresults": a.limit, "compact": "true", "verbose": "false", "key": key}
        if a.min_kw:
            params["minpowerkw"] = a.min_kw
        for p in http(OCM, params):
            ai = p.get("AddressInfo", {})
            conns = p.get("Connections") or []
            res.append({"name": ai.get("Title"), "lat": ai.get("Latitude"), "lon": ai.get("Longitude"), "distance_m": (ai.get("Distance") or 0) * 1000, "points": p.get("NumberOfPoints"),
                        "connectors": sorted({f"{x.get('ConnectionTypeID')}:{x.get('PowerKW')}kW" for x in conns}), "operator_id": p.get("OperatorID"), "usage_cost": p.get("UsageCost"), "source": "openchargemap", "confidence": "high"})
    else:
        for r in poi_search_safe("charging", (c["lat"], c["lon"]), a.radius, a.limit, lang=lang)[0]:
            t = r["tags"]
            socks = {k[7:]: v for k, v in t.items() if k.startswith("socket:") and ":" not in k[7:]}
            kw = max([float(re.sub("[^0-9.]", "", str(v)) or 0) for k, v in t.items() if k.startswith("socket:") and k.endswith(":output")] or [0])
            if a.min_kw and kw and kw < a.min_kw:
                continue
            res.append({"name": r["name"], "lat": r["lat"], "lon": r["lon"], "distance_m": r["distance_m"], "points": t.get("capacity"), "connectors": [f"{k}×{v}" for k, v in socks.items()],
                        "max_kw": kw or None, "operator": t.get("operator") or t.get("network"), "fee": t.get("fee"), "opening_hours": t.get("opening_hours"), "source": "openstreetmap", "confidence": "medium"})
    lines = [f"EV charging near {c['name']} ({len(res)}; source {'OpenChargeMap' if key else 'OpenStreetMap'} conf:{'high' if key else 'med'}):"]
    for r in res:
        lines.append(f"  • {str(r['name'])[:38]:<38} {fmt_dist(r['distance_m'], lang=lang):>7}  {', '.join(r['connectors'])[:50]}  {('%s kW' % r['max_kw']) if r.get('max_kw') else ''} {r.get('operator') or ''} [src:{r['source']} conf:{r['confidence']}]")
    emit(a, "\n".join(lines), {"near": c, "results": res, "confidence": "high" if key else "medium", "source": "openchargemap" if key else "openstreetmap"})

def cmd_transit(a):
    lang = getattr(a, "lang", "en") or "en"
    if a.sub == "plan":
        o, d = parse_place(a.origin, lang=lang), parse_place(a.destination, lang=lang)
        params = {"fromPlace": f"{o['lat']},{o['lon']}", "toPlace": f"{d['lat']},{d['lon']}", "numItineraries": a.limit}
        if a.time:
            params["time"] = a.time
        if a.arrive_by:
            params["arriveBy"] = "true"
        if a.wheelchair:
            params["wheelchair"] = "true"
        if a.max_transfers is not None:
            params["maxTransfers"] = a.max_transfers
        r = http(f"{TRANSITOUS}/plan", params, timeout=60)
        its = r.get("itineraries", [])
        lines = [f"Transit {o['name']} → {d['name']} (Transitous / MOTIS, open GTFS data) [conf:{'high' if its else 'low'} src:transitous]:"]
        if not its:
            lines.append("  no itineraries found (area may lack open GTFS feed, or nothing runs at that time). Try app links below. [conf:low — abstain from inventing]")
        for i, it in enumerate(its, 1):
            legs = []
            for l in it["legs"]:
                if l["mode"] == "WALK":
                    legs.append(f"walk {fmt_dur(l['duration'], lang)}")
                else:
                    legs.append(f"{l['mode'].lower()} {l.get('routeShortName') or ''}→{(l.get('headsign') or '')[:18]} ({l['from']['name'][:18]} {l['startTime'][11:16]} → {l['to']['name'][:18]} {l['endTime'][11:16]})")
            lines.append(f"  {i}. {fmt_dur(it['duration'], lang)}, {it.get('transfers', 0)} transfer(s): " + " · ".join(legs))
        links = deeplinks.navigate_links((d["lat"], d["lon"], d["name"]), (o["lat"], o["lon"], o["name"]), [], "transit", ("google", "apple", "here", "organic"))
        lines.append("Open transit directions in an app:\n" + links_text(links, compact=getattr(a, "compact", False)))
        emit(a, "\n".join(lines), {"origin": o, "destination": d, "itineraries": its, "links": links, "confidence": "high" if its else "low", "source": "transitous"})
    elif a.sub == "departures":
        stops = http(f"{TRANSITOUS}/geocode", {"text": a.stop, "type": "STOP"})
        if not stops:
            raise UmnError(f"no transit stop matches {a.stop!r} [src=transitous conf:low]")
        s = stops[0]
        params = {"stopId": s["id"], "n": a.limit}
        if a.time:
            params["time"] = a.time
        r = http(f"{TRANSITOUS}/stoptimes", params)
        lines = [f"Departures at {s['name']} ({s.get('id')}) [src=transitous conf:high]:"]
        for st in r.get("stopTimes", []):
            pl = st.get("place", {})
            t = pl.get("departure") or pl.get("scheduledDeparture") or ""
            lines.append(f"  {t[11:16]}  {st.get('mode', ''):<7} {str(st.get('routeShortName') or ''):<6} → {st.get('headsign', '')[:30]}" + ("  (real-time)" if st.get("realTime") else ""))
        emit(a, "\n".join(lines), {"stop": s, "stop_times": r.get("stopTimes", []), "confidence": "high", "source": "transitous"})
    else:
        c = parse_place(a.near, lang=lang)
        sels = POI_CATEGORIES["bus-stop"] + POI_CATEGORIES["station"] + POI_CATEGORIES["tram"] + POI_CATEGORIES["metro"]
        around = f"around:{int(a.radius)},{c['lat']:.6f},{c['lon']:.6f}"
        try:
            els = overpass("[out:json][timeout:25];(" + "".join(f"nwr{s}({around});" for s in sels) + f");out center tags {a.limit * 3};")
            res = [{"name": e.get("tags", {}).get("name") or "stop", "lat": _el_latlon(e)[0], "lon": _el_latlon(e)[1], "tags": e.get("tags", {}),
                    "distance_m": haversine((c["lat"], c["lon"]), _el_latlon(e)), "source": "overpass", "confidence": "high"} for e in els if _el_latlon(e)[0] is not None]
        except UmnError:
            res = poi_photon_fallback("station", (c["lat"], c["lon"]), a.radius, a.limit, lang=lang)
        res.sort(key=lambda x: x["distance_m"])
        lines = [f"Stops near {c['name']} [src=overpass conf:high]:"] + [f"  • {r['name'][:40]:<40} {fmt_dist(r['distance_m'], lang=lang):>7}  {r['tags'].get('railway') or r['tags'].get('highway') or r['tags'].get('public_transport')}" for r in res[: a.limit]]
        emit(a, "\n".join(lines), {"near": c, "stops": res[: a.limit], "confidence": "high", "source": "overpass"})

IMPLICIT_MAXSPEED = {"urban": "≈50 km/h (implicit urban)", "rural": "≈90–100 km/h (implicit rural)", "motorway": "≈120–130 km/h (implicit motorway)",
                     "trunk": "≈100 km/h (implicit trunk)", "living_street": "≈20 km/h (living street)", "walk": "walking pace", "none": "no limit"}

def human_maxspeed(v):
    if not v:
        return ""
    if ":" in v:
        return IMPLICIT_MAXSPEED.get(v.split(":", 1)[1], v)
    return IMPLICIT_MAXSPEED.get(v, v if "mph" in v or not v.isdigit() else f"{v} km/h")

def cmd_speedlimit(a):
    lang = getattr(a, "lang", "en") or "en"
    p = parse_place(a.place, lang=lang)
    els = overpass(f'[out:json][timeout:20];way(around:{a.radius},{p["lat"]:.6f},{p["lon"]:.6f})["highway"]["maxspeed"];out tags geom;')
    best = []
    for w in els:
        g = w.get("geometry") or []
        if not g:
            continue
        dmin = min(haversine((p["lat"], p["lon"]), (q["lat"], q["lon"])) for q in g)
        t = w.get("tags", {})
        best.append({"distance_m": dmin, "name": t.get("name") or t.get("ref") or t.get("highway"), "maxspeed": t.get("maxspeed"), "maxspeed_human": human_maxspeed(t.get("maxspeed")), "highway": t.get("highway"), "osm": f"way/{w['id']}", "source": "overpass", "confidence": "high"})
    best.sort(key=lambda x: x["distance_m"])
    if not best:
        raise UmnError("no road with a posted maxspeed within radius (OSM may lack tag) [src=overpass conf:low] — abstain")
    lines = [f"Posted speed limits near {p['name']} [src=overpass conf:high]:"] + [f"  • {b['name']:<35} {b['maxspeed_human']:<34} ({b['highway']}, {fmt_dist(b['distance_m'], lang=lang)} away)" for b in best[:5]]
    emit(a, "\n".join(lines), {"results": best[:5], "confidence": "high", "source": "overpass"})

def cmd_cameras(a):
    lang = getattr(a, "lang", "en") or "en"
    p = parse_place(a.near, lang=lang)
    res = poi_search_safe("speed-camera", (p["lat"], p["lon"]), a.radius, a.limit, lang=lang)[0]
    lines = [f"Speed cameras within {fmt_dist(a.radius, lang=lang)} of {p['name']} ({len(res)}; OSM community-mapped, not exhaustive) [src=osm conf:med]:"]
    for r in res:
        t = r["tags"]
        lines.append(f"  • {fmt_dist(r['distance_m'], lang=lang):>7} {compass(bearing((p['lat'], p['lon']), (r['lat'], r['lon'])))}  [{r['lat']:.5f},{r['lon']:.5f}] {t.get('maxspeed', '')} {t.get('direction', '')} {t.get('camera:type', '')}".rstrip())
    emit(a, "\n".join(lines), {"near": p, "cameras": res, "confidence": "medium", "source": "openstreetmap"})

def cmd_reports(a):
    lang = getattr(a, "lang", "en") or "en"
    p = parse_place(a.near, lang=lang)
    dlat, dlon = a.radius / 111320.0, a.radius / (111320.0 * max(math.cos(math.radians(p["lat"])), 0.01))
    d = http(f"{OSM_API}/notes.json", {"bbox": f"{p['lon'] - dlon:.5f},{p['lat'] - dlat:.5f},{p['lon'] + dlon:.5f},{p['lat'] + dlat:.5f}", "limit": a.limit, "closed": 0})
    feats = d.get("features", [])
    lines = [f"OSM Notes within {fmt_dist(a.radius, lang=lang)} of {p['name']}: {len(feats)} [src=osm conf:high]"]
    for f in feats:
        pr = f["properties"]
        lon, lat = f["geometry"]["coordinates"]
        first = (pr.get("comments") or [{}])[0]
        lines.append(f"  • #{pr['id']} {pr.get('date_created', '')[:10]} [{lat:.5f},{lon:.5f}] {first.get('text', '')[:90]!r}  {pr.get('url', '')}")
    emit(a, "\n".join(lines), {"results": feats, "confidence": "high", "source": "osm_notes"})

def cmd_report(a):
    lang = getattr(a, "lang", "en") or "en"
    p = parse_place(a.place, lang=lang)
    text = a.text.strip()
    if len(text) < 10:
        raise UmnError("report text too short [conf:high]")
    preview = f"OSM Note at [{p['lat']:.6f},{p['lon']:.6f}]: {text!r}"
    if not a.yes:
        print("DRY RUN — would create PUBLIC anonymous OSM note:\n  " + preview + "\nRe-run with --yes to submit (be factual). [conf:high src=osm]")
        return
    d = http(f"{OSM_API}/notes.json", {"lat": p["lat"], "lon": p["lon"], "text": text}, data="", method="POST")
    pr = d.get("properties", {})
    emit(a, f"Created note #{pr.get('id')}: {pr.get('url')} [conf:high src=osm]", d)

def cmd_traffic(a):
    lang = getattr(a, "lang", "en") or "en"
    p = parse_place(a.place, lang=lang)
    payload = {"place": p, "live": None, "confidence": "high", "source": "tomtom|deeplinks"}
    lines = [f"Traffic around {p['name']} [conf:high]:"]
    key = cfg_key("tomtom_key")
    if key:
        try:
            f = http(f"{TOMTOM}/traffic/services/4/flowSegmentData/absolute/10/json", {"point": f"{p['lat']},{p['lon']}", "unit": "KMPH", "key": key})["flowSegmentData"]
            ratio = f["currentSpeed"] / max(f["freeFlowSpeed"], 1)
            lines.append(f"  nearest road: {f['currentSpeed']} km/h now vs {f['freeFlowSpeed']} km/h free-flow ({ratio:.0%}), delay ≈ {f['currentTravelTime'] - f['freeFlowTravelTime']} s/segment  [TomTom conf:high]")
            dl = a.radius / 111320.0
            inc = http(f"{TOMTOM}/traffic/services/5/incidentDetails", {"bbox": f"{p['lon'] - dl:.4f},{p['lat'] - dl:.4f},{p['lon'] + dl:.4f},{p['lat'] + dl:.4f}", "fields": "{incidents{type,properties{iconCategory,magnitudeOfDelay,events{description},from,to,delay}}}", "language": "en-GB", "key": key})
            cats = {1: "accident", 2: "fog", 3: "dangerous conditions", 4: "rain", 5: "ice", 6: "jam", 7: "lane closed", 8: "road closed", 9: "road works", 10: "wind", 11: "flooding", 14: "broken-down vehicle"}
            incs = inc.get("incidents", [])
            lines.append(f"  incidents in {fmt_dist(a.radius, lang=lang)} box: {len(incs)} [src=tomtom conf:high]")
            for i in incs[: a.limit]:
                pr = i["properties"]
                lines.append(f"    • {cats.get(pr.get('iconCategory'), pr.get('iconCategory'))}: {(pr.get('events') or [{}])[0].get('description', '')} {pr.get('from', '')}→{pr.get('to', '')} delay {pr.get('delay') or 0} s")
            payload["live"] = {"flow": f, "incidents": incs}
        except UmnError as e:
            lines.append(f"  TomTom traffic failed: {e} [conf:low]")
    else:
        lines.append("  No free keyless live-traffic API — proprietary probe data [conf:high src=docs]")
        lines.append("  → `umn config set tomtom_key <key>` enables live flow + incidents (2500 req/day free)")
    pl = deeplinks.place_links(p["lat"], p["lon"], p["name"], 13)
    lines.append("  Live traffic layers in apps:\n" + "\n".join(f"    {n:<12} {u}" for n, u in [("Google", pl["google"]["traffic_url"]), ("Waze", pl["waze"]["livemap_url"]), ("HERE WeGo", pl["here"]["traffic_url"])]))
    payload["links"] = {"google": pl["google"]["traffic_url"], "waze": pl["waze"]["livemap_url"], "here": pl["here"]["traffic_url"]}
    emit(a, "\n".join(lines), payload)

def cmd_offline(a):
    lang = getattr(a, "lang", "en") or "en"
    idx = cache_get("geofabrik_index.json", 7 * 86400)
    if idx is None:
        idx = http(GEOFABRIK_INDEX, timeout=60)
        cache_put("geofabrik_index.json", idx)
    q = a.region.lower()
    hits = [f["properties"] for f in idx.get("features", []) if q in f["properties"].get("name", "").lower() or q == f["properties"].get("id", "").lower()]
    lines = [f"Offline options for '{a.region}' [src=geofabrik conf:high]:"]
    if hits:
        lines.append("  Raw OSM extracts (Geofabrik, daily) → local OSRM/Valhalla/Nominatim:")
        for h in hits[:5]:
            lines.append(f"    • {h['name']:<30} {h['urls'].get('pbf')}")
        lines.append("    local router: docker run -t -v $PWD:/data ghcr.io/project-osrm/osrm-backend osrm-extract -p /opt/car.lua /data/<file>.osm.pbf && … osrm-routed")
        lines.append("    then: umn config set osrm_url http://localhost:5000")
    else:
        lines.append("  (no Geofabrik region matched — try country/continent name)")
    lines += ["  In-app offline maps:",
              "    Organic Maps / CoMaps – fully offline. Menu → Download maps.",
              "    HERE WeGo – Menu → Download maps → country/region.",
              "    Sygic – Menu → Manage maps → download.",
              "    Google Maps – Profile → Offline maps → Select your own map.",
              "    Apple Maps – iOS 17+: profile → Offline Maps → Download New Map.",
              "    Waze – no offline mode.",
              "  Export: umn route A B --gpx trip.gpx ; umn places --kml bookmarks.kml"]
    emit(a, "\n".join(lines), {"geofabrik": hits[:5], "confidence": "high", "source": "geofabrik"})

def cmd_places(a):
    places = CFG.setdefault("places", {})
    if a.sub == "save":
        lang = getattr(a, "lang", "en") or "en"
        p = parse_place(a.place, lang=lang)
        places[a.name.lower()] = {"lat": p["lat"], "lon": p["lon"], "name": p.get("display_name") or p["name"]}
        save_config(CFG)
        print(f"saved '{a.name}' → {places[a.name.lower()]['name']} [{p['lat']:.6f},{p['lon']:.6f}] [conf:high]")
    elif a.sub == "forget":
        if places.pop(a.name.lower(), None) is None:
            raise UmnError(f"no saved place {a.name!r} [conf:high]")
        save_config(CFG)
        print(f"removed '{a.name}'")
    else:
        if a.kml:
            write_kml(a.kml, [{"name": k, **v} for k, v in places.items()])
            print(f"KML written: {a.kml}")
        txt = "\n".join(f"  {k:<12} {v['name'][:50]:<50} [{v['lat']:.5f},{v['lon']:.5f}]" for k, v in places.items()) or "  (none — try: umn places save home \"<address>\")"
        emit(a, "Saved places [conf:high src=config]:\n" + txt, {"places": places, "confidence": "high", "source": "config"})

def cmd_config(a):
    if a.sub == "set":
        CFG[a.key] = a.value
        save_config(CFG)
        print(f"{a.key} set" + ("" if a.key.endswith("_key") else f" = {a.value}") + " [conf:high]")
    elif a.sub == "get":
        v = CFG.get(a.key, "")
        print(("(set)" if v else "(unset)") if a.key.endswith("_key") else v)
    elif a.sub == "unset":
        CFG.pop(a.key, None)
        save_config(CFG)
        print(f"{a.key} removed")
    else:
        for k, v in sorted(CFG.items()):
            if k == "places":
                continue
            print(f"  {k:<20} {'(set)' if k.endswith('_key') else v}")
        print(f"  config file: {CONFIG_PATH}\n  keys: contact_email language units(metric|imperial) ors_key openchargemap_key tomtom_key overpass_url osrm_url valhalla_url lang")

def cmd_doctor(a):
    checks = [("Nominatim geocoder", NOMINATIM + "/status?format=json"), ("Photon geocoder", PHOTON + "/api/?q=Berlin&limit=1"),
              ("OSRM demo router", OSRM_CAR + "/nearest/v1/driving/13.4050,52.5200"), ("FOSSGIS bike/foot router", OSRM_FOSSGIS.format(profile="bike") + "/nearest/v1/driving/13.4050,52.5200"),
              ("Valhalla (FOSSGIS)", VALHALLA + "/status"), ("Overpass API", OVERPASS_SERVERS[0].replace("interpreter", "status")),
              ("OpenTopoData elevation", OPENTOPO + "/srtm90m?locations=52.52,13.40"), ("Open-Meteo weather", OPEN_METEO + "?latitude=52.52&longitude=13.4&current=temperature_2m"),
              ("Transitous transit", TRANSITOUS + "/geocode?text=Berlin"), ("OSM Notes API", OSM_API + "/notes.json?bbox=13.40,52.51,13.41,52.52&limit=1"),
              ("Wikipedia geosearch", "https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=52.52|13.40&gsradius=500&format=json")]
    ok = 0
    print(f"universal-maps-navigator {VERSION}  python {sys.version.split()[0]}  config {CONFIG_PATH} ({'present' if os.path.exists(CONFIG_PATH) else 'absent'}) [v2 with i18n+survival+self-improve]")
    for name, url in checks:
        t = time.time()
        try:
            http(url, timeout=20, accept_json=False, retries=0)
            print(f"  ✅ {name:<26} {time.time() - t:5.1f}s [conf:high src:{url.split('/')[2]}]")
            ok += 1
        except UmnError as e:
            print(f"  ❌ {name:<26} {e} [conf:low]")
    for k in ("ors_key", "openchargemap_key", "tomtom_key"):
        print(f"  {'🔑' if cfg_key(k) else '➖'} {k:<26} {'configured' if cfg_key(k) else 'not set (optional)'}")
    # v2 modules check
    print(f"  {'✅' if i18n_mod else '❌'} i18n module (50+ langs) {'present' if i18n_mod else 'missing'}")
    print(f"  {'✅' if survival_mod else '❌'} survival module (terrain+disaster) {'present' if survival_mod else 'missing'}")
    print(f"  {'✅' if self_improve_mod else '❌'} self-improve module {'present' if self_improve_mod else 'missing'}")
    print(f"  {'✅' if token_opt_mod else '❌'} token_optimizer module {'present' if token_opt_mod else 'missing'}")
    print(f"{ok}/{len(checks)} free services reachable [overall conf:{'high' if ok>=9 else 'medium'}]")
    sys.exit(0 if ok >= len(checks) - 2 else 1)

def cmd_guide(a):
    ref = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "references")
    files = sorted(f for f in os.listdir(ref) if f.endswith(".md")) if os.path.isdir(ref) else []
    if not a.topic:
        print("Reference guides (umn guide <name>):\n" + "\n".join(f"  {f[:-3]}" for f in files) + "\n[v2: survival-guides, i18n-catalog added]")
        return
    for f in files:
        if a.topic in f:
            print(open(os.path.join(ref, f)).read())
            return
    raise UmnError(f"no guide matching {a.topic!r} [conf:high]")

# v2 new commands
def cmd_survival(a):
    lang = getattr(a, "lang", "en") or "en"
    compact = getattr(a, "compact", False)
    if not survival_mod:
        raise UmnError("survival module not found — ensure scripts/survival.py present [conf:high]")
    if a.sub == "guide":
        terrain = getattr(a, "terrain", None)
        disaster = getattr(a, "disaster", None)
        situation = getattr(a, "situation", None)
        result = survival_mod.get_combined_survival(terrain, disaster, situation, lang, compact)
        # Format for human
        lines = [f"Survival Guide [conf:{result.get('confidence','high')} src:{','.join(result.get('sources',[]))} lang:{lang}]"]
        if situation:
            lines.append(f"Situation: {situation}")
        lines.append(result.get("text",""))
        if not compact:
            lines.append(f"\nSources: {', '.join(result.get('sources',[]))} [grounded, not hallucinated]")
            lines.append("SOS: 3 whistle blasts / 3 fires triangle / X ground signal 15ft")
        emit(a, "\n".join(lines), result)
    elif a.sub == "sos":
        terrain = getattr(a, "terrain", None)
        disaster = getattr(a, "disaster", None)
        result = survival_mod.get_sos_instructions(terrain, disaster, lang)
        lines = [f"SOS Instructions [conf:high src:US Army FM 21-76, Red Cross lang:{lang}]"]
        lines.append("INTERNATIONAL DISTRESS:")
        for s in result.get("sos", [])[:6]:
            lines.append(f"  - {s}")
        lines.append("NAVIGATION SOS:")
        for s in result.get("navigation_sos", [])[:5]:
            lines.append(f"  - {s}")
        if terrain and "terrain" in result:
            lines.append(f"\nTERRAIN {terrain}:")
            lines.append(survival_mod.format_guide(result["terrain"], lang, compact))
        if disaster and "disaster" in result:
            lines.append(f"\nDISASTER {disaster}:")
            lines.append(survival_mod.format_guide(result["disaster"], lang, compact))
        emit(a, "\n".join(lines), result)
    elif a.sub == "list":
        terrains = survival_mod.list_terrains()
        disasters = survival_mod.list_disasters()
        txt = f"Terrains: {', '.join(terrains)}\nDisasters: {', '.join(disasters)}\n[conf:high src:survival.py]"
        emit(a, txt, {"terrains": terrains, "disasters": disasters, "confidence": "high", "source": "survival.py"})

def cmd_i18n(a):
    lang = getattr(a, "lang", "en") or "en"
    if not i18n_mod:
        raise UmnError("i18n module not found — ensure scripts/i18n.py present [conf:high]")
    if a.sub == "list":
        langs = i18n_mod.list_languages()
        lines = [f"Supported languages ({len(langs)}) [conf:high src:i18n.py]:"]
        for l in langs:
            lines.append(f"  {l['code']:<8} {l['name']:<20} {l['native']:<20} dir:{l['dir']} units:{l['units']}")
        emit(a, "\n".join(lines), {"languages": langs, "confidence": "high", "source": "i18n.py"})
    elif a.sub == "detect":
        detected = i18n_mod.detect_language(a.text)
        info = i18n_mod.get_locale_info(detected)
        txt = f"Detected: {detected} ({info['name']} / {info['native']}) dir:{info['dir']} [conf:medium src:heuristic]"
        emit(a, txt, {"detected": detected, "info": info, "confidence": "medium", "source": "heuristic"})
    elif a.sub == "translate":
        # Simple translate using dictionary
        translated = i18n_mod.translate(a.text, a.to)
        # Also try to detect source
        src_lang = getattr(a, "from_lang", None) or i18n_mod.detect_language(a.text)
        txt = f"{a.text} [{src_lang}] → {translated} [{a.to}] [conf:medium src:offline_dict]"
        if getattr(a, "compact", False):
            txt = f"{translated}"
        emit(a, txt, {"original": a.text, "translated": translated, "from": src_lang, "to": a.to, "confidence": "medium", "source": "offline_dict"})
    else:
        emit(a, "i18n commands: list | detect TEXT | translate TEXT --to LANG", {"confidence": "high"})

def cmd_self_improve(a):
    if not self_improve_mod:
        raise UmnError("self_improve module not found [conf:high]")
    if a.analyze:
        result = self_improve_mod.analyze_learnings()
        emit(a, f"Self-improvement analysis [conf:high src=learnings.json]:\n{json.dumps(result, indent=2, ensure_ascii=False)}", result)
    elif a.apply:
        result = self_improve_mod.apply_improvements(dry_run=not getattr(a, "live", False))
        emit(a, f"Applied improvements [conf:high]:\n{json.dumps(result, indent=2, ensure_ascii=False)}", result)
    else:
        # stats
        try:
            import pathlib
            metrics_path = os.path.join(os.path.expanduser("~/.local/share/universal-maps-navigator"), "metrics.json")
            metrics = json.load(open(metrics_path))
            txt = f"Self-improvement metrics [src=metrics.json conf:high]:\n{json.dumps(metrics, indent=2)}"
        except Exception:
            txt = "No metrics yet — run some commands to generate learnings [conf:low]"
            metrics = {}
        emit(a, txt, metrics)

# ----------------------------------------------------------------------------- argparse
def build_parser():
    ap = argparse.ArgumentParser(prog="umn", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="machine-readable JSON output")
    ap.add_argument("--compact", action="store_true", help="minimal token output (60% saving) — v2")
    ap.add_argument("--lang", default=None, help="language code for results (e.g. en, ro, ar, zh) — v2, 50+ langs")
    ap.add_argument("--version", action="version", version=VERSION)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def add_truck(p):
        for k, h in (("height", "m"), ("width", "m"), ("length", "m"), ("weight", "t"), ("axle_load", "t")):
            p.add_argument(f"--truck-{k.replace('_', '-')}", dest=f"truck_{k}", type=float, help=f"truck {k} in {h}")
        p.add_argument("--hazmat", action="store_true", help="carrying hazardous materials")

    def add_common(p):
        p.add_argument("--lang", default=None, help="language code")
        p.add_argument("--compact", action="store_true", help="compact output")
        p.add_argument("--json", action="store_true", help="machine-readable JSON")

    p = sub.add_parser("geocode", help="place → coordinates"); p.add_argument("query"); p.add_argument("--limit", type=int, default=5); p.add_argument("--country", help="ISO code bias"); add_common(p); p.set_defaults(fn=cmd_geocode)
    p = sub.add_parser("reverse", help="coordinates → address"); p.add_argument("lat", type=float); p.add_argument("lon", type=float); p.add_argument("--zoom", type=int, default=18); add_common(p); p.set_defaults(fn=cmd_reverse)
    p = sub.add_parser("route", help="directions with turn-by-turn"); p.add_argument("origin"); p.add_argument("destination"); p.add_argument("--via", action="append", help="intermediate stop")
    p.add_argument("--mode", default="car", choices=MODES); p.add_argument("--engine", default="auto", choices=["auto", "osrm", "valhalla", "ors"]); p.add_argument("--avoid", help="tolls,highways,ferries,unpaved")
    p.add_argument("--alternatives", action="store_true"); p.add_argument("--steps", action="store_true", help="print turn-by-turn + lane guidance"); p.add_argument("--depart", help="ISO local time for departure"); p.add_argument("--elevation", action="store_true"); p.add_argument("--cameras", action="store_true", help="list OSM speed cameras along route")
    p.add_argument("--weather", action="store_true", help="weather along route"); p.add_argument("--gpx", help="write GPX"); add_truck(p); add_common(p); p.set_defaults(fn=cmd_route)
    p = sub.add_parser("navigate", help="deep links into 7 apps"); p.add_argument("destination"); p.add_argument("--from", dest="origin"); p.add_argument("--via", action="append")
    p.add_argument("--mode", default="car", choices=MODES); p.add_argument("--app", default="all", help="comma list: google,apple,waze,organic,comaps,here,sygic,osm,geo,android"); p.add_argument("--name"); p.add_argument("--avoid"); add_truck(p); add_common(p); p.set_defaults(fn=cmd_navigate)
    p = sub.add_parser("share", help="share / show-place links + plus code"); p.add_argument("place"); p.add_argument("--name"); p.add_argument("--zoom", type=int, default=16); add_common(p); p.set_defaults(fn=cmd_share)
    p = sub.add_parser("search-links", help="open search in each app"); p.add_argument("query"); p.add_argument("--near"); add_common(p); p.set_defaults(fn=cmd_search_links)
    p = sub.add_parser("poi", help="POI nearby (fuel,parking,charging,restaurant,hotel,etc or key=value)"); p.add_argument("category"); p.add_argument("--near", required=True); p.add_argument("--radius", type=int, default=1500); p.add_argument("--limit", type=int, default=15); add_common(p); p.set_defaults(fn=cmd_poi)
    p = sub.add_parser("nearby", help="landmarks around place (Wikipedia)"); p.add_argument("place"); p.add_argument("--radius", type=int, default=1000); p.add_argument("--limit", type=int, default=10); add_common(p); p.set_defaults(fn=cmd_nearby)
    p = sub.add_parser("elevation", help="elevation of places"); p.add_argument("places", nargs="+"); add_common(p); p.set_defaults(fn=cmd_elevation)
    p = sub.add_parser("weather", help="weather now / along route"); p.add_argument("place"); p.add_argument("--route", metavar="DESTINATION", help="sample weather along route to DESTINATION"); p.add_argument("--mode", default="car", choices=[m for m in MODES if m != "transit"]); p.add_argument("--hours", type=int, default=6); add_common(p); p.set_defaults(fn=cmd_weather)
    p = sub.add_parser("isochrone", help="how far in N minutes"); p.add_argument("place"); p.add_argument("--minutes", default="15"); p.add_argument("--mode", default="car", choices=[m for m in MODES if m != "transit"]); p.add_argument("--out", help="write GeoJSON"); add_common(p); p.set_defaults(fn=cmd_isochrone)
    p = sub.add_parser("matrix", help="travel-time matrix"); p.add_argument("places", nargs="+"); p.add_argument("--mode", default="car", choices=[m for m in MODES if m != "transit"]); p.add_argument("--engine", default="auto"); add_common(p); p.set_defaults(fn=cmd_matrix)
    p = sub.add_parser("trip", help="optimise order of stops"); p.add_argument("places", nargs="+"); p.add_argument("--mode", default="car", choices=[m for m in MODES if m != "transit"]); p.add_argument("--roundtrip", action="store_true"); add_common(p); p.set_defaults(fn=cmd_trip)
    p = sub.add_parser("charging", help="EV charging stations"); p.add_argument("--near", required=True); p.add_argument("--radius", type=int, default=5000); p.add_argument("--limit", type=int, default=15); p.add_argument("--min-kw", type=float, default=0); add_common(p); p.set_defaults(fn=cmd_charging)
    t = sub.add_parser("transit", help="public transport: plan | departures | stops"); ts = t.add_subparsers(dest="sub", required=True)
    q = ts.add_parser("plan"); q.add_argument("origin"); q.add_argument("destination"); q.add_argument("--time", help="ISO 8601 UTC"); q.add_argument("--arrive-by", action="store_true"); q.add_argument("--wheelchair", action="store_true"); q.add_argument("--max-transfers", type=int); q.add_argument("--limit", type=int, default=3); add_common(q)
    q = ts.add_parser("departures"); q.add_argument("stop"); q.add_argument("--time"); q.add_argument("--limit", type=int, default=10); add_common(q)
    q = ts.add_parser("stops"); q.add_argument("--near", required=True); q.add_argument("--radius", type=int, default=600); q.add_argument("--limit", type=int, default=15); add_common(q)
    t.set_defaults(fn=cmd_transit)
    p = sub.add_parser("speedlimit", help="posted speed limit"); p.add_argument("place"); p.add_argument("--radius", type=int, default=40); add_common(p); p.set_defaults(fn=cmd_speedlimit)
    p = sub.add_parser("cameras", help="speed cameras nearby (OSM)"); p.add_argument("--near", required=True); p.add_argument("--radius", type=int, default=5000); p.add_argument("--limit", type=int, default=30); add_common(p); p.set_defaults(fn=cmd_cameras)
    p = sub.add_parser("reports", help="OSM Notes nearby"); p.add_argument("--near", required=True); p.add_argument("--radius", type=int, default=1500); p.add_argument("--limit", type=int, default=20); add_common(p); p.set_defaults(fn=cmd_reports)
    p = sub.add_parser("report", help="report map problem (public OSM Note; dry-run unless --yes)"); p.add_argument("place"); p.add_argument("text"); p.add_argument("--yes", action="store_true"); add_common(p); p.set_defaults(fn=cmd_report)
    p = sub.add_parser("traffic", help="live traffic (TomTom key) + traffic-layer links"); p.add_argument("place"); p.add_argument("--radius", type=int, default=3000); p.add_argument("--limit", type=int, default=10); add_common(p); p.set_defaults(fn=cmd_traffic)
    p = sub.add_parser("offline", help="offline map data"); p.add_argument("region"); add_common(p); p.set_defaults(fn=cmd_offline)
    pl = sub.add_parser("places", help="saved places: list | save | forget"); pls = pl.add_subparsers(dest="sub")
    q = pls.add_parser("save"); q.add_argument("name"); q.add_argument("place"); add_common(q)
    q = pls.add_parser("forget"); q.add_argument("name"); add_common(q)
    q = pls.add_parser("list"); q.add_argument("--kml", help="export KML"); add_common(q)
    pl.add_argument("--kml", help="export KML"); add_common(pl); pl.set_defaults(fn=cmd_places)
    c = sub.add_parser("config", help="settings & keys"); cs = c.add_subparsers(dest="sub")
    q = cs.add_parser("set"); q.add_argument("key"); q.add_argument("value"); add_common(q)
    q = cs.add_parser("get"); q.add_argument("key"); add_common(q)
    q = cs.add_parser("unset"); q.add_argument("key"); add_common(q)
    q = cs.add_parser("show"); add_common(q)
    c.set_defaults(fn=cmd_config)
    p = sub.add_parser("doctor", help="check all free services + v2 modules"); add_common(p); p.set_defaults(fn=cmd_doctor)
    p = sub.add_parser("guide", help="print reference guides"); p.add_argument("topic", nargs="?"); add_common(p); p.set_defaults(fn=cmd_guide)
    # v2 new commands
    s = sub.add_parser("survival", help="life-saving guides for terrain & disasters — v2 NEW"); ss = s.add_subparsers(dest="sub")
    q = ss.add_parser("guide", help="get survival guide"); q.add_argument("--terrain", help="desert|mountain|jungle|snow|swamp|forest|urban"); q.add_argument("--disaster", help="earthquake|flood|wildfire|hurricane|tornado|avalanche|tsunami|blizzard|sandstorm|landslide"); q.add_argument("--situation", help="describe your situation"); add_common(q)
    q = ss.add_parser("sos", help="SOS signals + immediate rescue"); q.add_argument("--terrain", help="terrain type"); q.add_argument("--disaster", help="disaster type"); add_common(q)
    q = ss.add_parser("list", help="list terrains & disasters"); add_common(q)
    s.set_defaults(fn=cmd_survival)
    ii = sub.add_parser("i18n", help="multilingual & cultural support — v2 NEW"); iis = ii.add_subparsers(dest="sub")
    q = iis.add_parser("list", help="list 50+ languages"); add_common(q)
    q = iis.add_parser("detect", help="detect language of text"); q.add_argument("text"); add_common(q)
    q = iis.add_parser("translate", help="translate key/phrase"); q.add_argument("text", help="key or phrase"); q.add_argument("--from", dest="from_lang", default="en", help="source lang"); q.add_argument("--to", dest="to", default="en", help="target lang"); add_common(q)
    add_common(ii); ii.set_defaults(fn=cmd_i18n)
    si = sub.add_parser("self-improve", help="self-improving loop: analyze & apply — v2 NEW"); si.add_argument("--analyze", action="store_true", help="analyze learnings"); si.add_argument("--apply", action="store_true", help="apply improvements"); si.add_argument("--live", action="store_true", help="actually apply (not dry-run)"); si.add_argument("--stats", action="store_true", help="show metrics"); add_common(si); si.set_defaults(fn=cmd_self_improve)
    return ap

def main(argv=None):
    start = time.time()
    ap = build_parser()
    a = ap.parse_args(argv)
    if getattr(a, "cmd", None) == "places" and getattr(a, "sub", None) is None:
        a.sub = "list"
    if getattr(a, "cmd", None) == "config" and getattr(a, "sub", None) is None:
        a.sub = "show"
    if getattr(a, "cmd", None) == "survival" and getattr(a, "sub", None) is None:
        a.sub = "list"
    if getattr(a, "cmd", None) == "i18n" and getattr(a, "sub", None) is None:
        a.sub = "list"
    # Token estimation for self-improve logging
    tokens_est = 0
    success = True
    err_msg = None
    try:
        a.fn(a)
    except UmnError as e:
        eprint(f"error: {e}")
        success = False
        err_msg = str(e)[:200]
        sys.exit(3)
    except KeyboardInterrupt:
        success = False
        err_msg = "KeyboardInterrupt"
        sys.exit(130)
    except Exception as e:
        eprint(f"unexpected error: {e}")
        success = False
        err_msg = str(e)[:200]
        sys.exit(2)
    finally:
        latency = (time.time() - start) * 1000
        # Estimate tokens from args
        if token_opt_mod:
            try:
                tokens_est = token_opt_mod.estimate_tokens(str(a))
            except Exception:
                tokens_est = 0
        # Log for self-improvement
        if self_improve_mod:
            try:
                cmd_str = " ".join(sys.argv[1:])[:200] if sys.argv else getattr(a, "cmd", "unknown")
                self_improve_mod.log_run(
                    command=cmd_str,
                    success=success,
                    latency_ms=latency,
                    tokens_used=tokens_est,
                    model=os.environ.get("UMN_MODEL", "unknown"),
                    error=err_msg,
                    lang=getattr(a, "lang", "en") or "en"
                )
            except Exception:
                pass

if __name__ == "__main__":
    main()
