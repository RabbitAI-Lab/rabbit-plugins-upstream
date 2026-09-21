#!/usr/bin/env python3
"""deeplinks.py — pure, offline deep-link builder for 7 navigation apps + open fallbacks.

Every template below was checked against the vendor's own documentation
(see references/deep-links.md for the source of each line).  No network access.

Apps: Google Maps, Apple Maps, Waze, Organic Maps, CoMaps, HERE WeGo, Sygic,
plus OpenStreetMap web, RFC 5870 geo: URIs and the Android navigation intent.

Usage as a module:
    from deeplinks import navigate_links, place_links, search_links
Usage as a CLI (JSON out):
    python3 deeplinks.py navigate 48.8584 2.2945 --name "Eiffel Tower" --mode bike
"""
from __future__ import annotations
import argparse
import json
import sys
from urllib.parse import quote, urlencode

APPS = ["google", "apple", "waze", "organic", "comaps", "here", "sygic", "osm", "geo", "android"]
MODES = ["car", "truck", "bike", "foot", "transit", "scooter", "motorcycle", "bus", "taxi"]

# --- per-app travel-mode vocabularies (verified against vendor docs) ---------
GOOGLE_MODE = {"car": "driving", "truck": "driving", "bike": "bicycling", "foot": "walking",
               "transit": "transit", "scooter": "two-wheeler", "motorcycle": "two-wheeler",
               "bus": "transit", "taxi": "driving"}
GOOGLE_ANDROID_MODE = {"car": "d", "truck": "d", "bike": "b", "foot": "w", "transit": "t",
                       "scooter": "l", "motorcycle": "l", "bus": "t", "taxi": "d"}
APPLE_MODE = {"car": "d", "truck": "d", "bike": "c", "foot": "w", "transit": "r",
              "scooter": "d", "motorcycle": "d", "bus": "r", "taxi": "d"}
OM_MODE = {"car": "vehicle", "truck": "vehicle", "bike": "bicycle", "foot": "pedestrian",
           "transit": "transit", "scooter": "vehicle", "motorcycle": "vehicle", "bus": "transit", "taxi": "vehicle"}
OM_V2_MODE = {"car": "drive", "truck": "drive", "bike": "bike", "foot": "walk", "transit": "transit",
              "scooter": "drive", "motorcycle": "drive", "bus": "transit", "taxi": "drive"}
HERE_MODE = {"car": "d", "truck": "tr", "bike": "b", "foot": "w", "transit": "pt",
             "scooter": "d", "motorcycle": "d", "bus": "pt", "taxi": "t"}
SYGIC_MODE = {"car": "drive", "truck": "drive", "bike": "drive", "foot": "walk", "transit": "walk",
              "scooter": "drive", "motorcycle": "drive", "bus": "drive", "taxi": "drive"}
OSM_ENGINE = {"car": "fossgis_osrm_car", "truck": "fossgis_valhalla_car", "bike": "fossgis_osrm_bike",
              "foot": "fossgis_osrm_foot", "transit": "fossgis_osrm_car", "scooter": "fossgis_osrm_car",
              "motorcycle": "fossgis_osrm_car", "bus": "fossgis_osrm_car", "taxi": "fossgis_osrm_car"}


def _ll(p):
    """Format a (lat, lon[, name]) tuple as 'lat,lon' with 6 decimals."""
    return f"{float(p[0]):.6f},{float(p[1]):.6f}"


def _name(p, default=""):
    return (p[2] if len(p) > 2 and p[2] else default) or ""


def navigate_links(dest, origin=None, via=(), mode="car", apps=("all",), avoid=(), truck=None, utm="universal-maps-navigator"):
    """Build navigation deep links.

    dest/origin/via items are tuples (lat, lon[, name]).  origin=None means
    "current location" in every app that supports it.  `avoid` may contain
    tolls/highways/ferries (Google & HERE honour it).  `truck` is an optional
    dict with height/width/length/weight (metres / tonnes) — only HERE WeGo
    Pro understands truck attributes via URL, Sygic Truck ignores them.
    Returns {app: {"label", "url", "scheme"?, "notes": [...]}}.
    """
    if mode not in MODES:
        raise ValueError(f"unknown mode {mode!r}; choose from {MODES}")
    want = set(APPS) if ("all" in apps) else set(apps)
    out = {}
    dll, dname = _ll(dest), _name(dest)
    oll = _ll(origin) if origin else None
    via = list(via or [])
    avoid = [a for a in avoid if a in ("tolls", "highways", "ferries")]

    # ---- Google Maps (Maps URLs; no API key needed; api=1 mandatory) --------
    if "google" in want:
        q = {"api": "1", "destination": dll, "travelmode": GOOGLE_MODE[mode], "dir_action": "navigate"}
        if oll:
            q["origin"] = oll
        if via:
            q["waypoints"] = "|".join(_ll(v) for v in via[:9])
        if avoid:
            q["avoid"] = ",".join(avoid)
        url = "https://www.google.com/maps/dir/?" + urlencode(q, safe="", quote_via=quote)
        notes = ["Universal link: opens the app on iOS/Android, the website elsewhere.",
                 "Max 9 waypoints (3 on mobile browsers); 2048-char limit."]
        if mode == "truck":
            notes.append("Google Maps has no truck routing – falls back to car.")
        ios = "comgooglemaps://?" + urlencode({"daddr": dll, **({"saddr": oll} if oll else {}),
                                               "directionsmode": GOOGLE_MODE[mode] if mode in ("car", "bike", "foot", "transit") else "driving"}, safe=",", quote_via=quote)
        out["google"] = {"label": "Google Maps", "url": url, "ios_scheme": ios,
                         "android_intent": f"google.navigation:q={dll}&mode={GOOGLE_ANDROID_MODE[mode]}", "notes": notes}

    # ---- Apple Maps (MapLinks) ----------------------------------------------
    if "apple" in want:
        q = {"daddr": dll, "dirflg": APPLE_MODE[mode]}
        if dname:
            q["daddr"] = f"{dll}"  # Apple prefers coordinates in daddr; name goes via q on place links
        if oll:
            q["saddr"] = oll
        url = "https://maps.apple.com/?" + urlencode(q, safe=",", quote_via=quote)
        notes = ["Opens Apple Maps on iOS/macOS; falls back to the Apple Maps website (beta) elsewhere.",
                 "Only one destination per link – no waypoints in the URL scheme."]
        if mode == "bike":
            notes.append("dirflg=c (cycling) is documented by third parties; official archive lists d/w/r.")
        if mode == "truck":
            notes.append("Apple Maps has no truck routing – falls back to car.")
        out["apple"] = {"label": "Apple Maps", "url": url, "ios_scheme": "maps://?" + urlencode(q, safe=",", quote_via=quote), "notes": notes}

    # ---- Waze -----------------------------------------------------------------
    if "waze" in want:
        q = {"ll": dll, "navigate": "yes", "zoom": "17"}
        if utm:
            q["utm_source"] = utm
        url = "https://waze.com/ul?" + urlencode(q, safe=",", quote_via=quote)
        notes = ["Waze is driving-only; other modes are ignored.", "Origin is always the current position.",
                 "Waypoints are not supported in the deep link."]
        out["waze"] = {"label": "Waze", "url": url, "app_scheme": "waze://?" + urlencode(q, safe=",", quote_via=quote), "notes": notes}

    # ---- Organic Maps ---------------------------------------------------------
    if "organic" in want:
        q = {"dll": dll, "daddr": dname or "Destination", "type": OM_MODE[mode]}
        if oll:
            q = {"sll": oll, "saddr": _name(origin, "Start"), **q}
        route_q = urlencode(q, safe=",", quote_via=quote)
        v2 = {"origin": oll or "currentLocation", "destination": dll, "mode": OM_V2_MODE[mode]}
        if via:
            v2["waypoints"] = "|".join(_ll(v) for v in via)
            v2["waypoint_names"] = "|".join(_name(v, "Via") for v in via)
        v2_q = urlencode(v2, safe=",|", quote_via=quote)
        out["organic"] = {"label": "Organic Maps", "url": "https://omaps.app/route?" + route_q,
                          "app_scheme": "om://route?" + route_q, "app_scheme_v2_nav": "om://v2/nav?" + v2_q,
                          "notes": ["om://route accepts start+destination; om://v2/nav adds waypoints and starts guidance.",
                                    "Works fully offline once the region map is downloaded."]}

    # ---- CoMaps (Organic Maps fork, same API, cm:// scheme) ------------------
    if "comaps" in want:
        q = {"dll": dll, "daddr": dname or "Destination", "type": OM_MODE[mode]}
        if oll:
            q = {"sll": oll, "saddr": _name(origin, "Start"), **q}
        route_q = urlencode(q, safe=",", quote_via=quote)
        out["comaps"] = {"label": "CoMaps", "url": "https://comaps.at/route?" + route_q,
                         "app_scheme": "cm://route?" + route_q, "alt_scheme": "comaps://route?" + route_q,
                         "notes": ["Same parameters as Organic Maps; offline-first."]}

    # ---- HERE WeGo (share.here.com) -------------------------------------------
    if "here" in want:
        pts = []
        pts.append(oll if oll else "mylocation")
        for v in via:
            pts.append(_ll(v) + ("," + quote(_name(v)) if _name(v) else "") + ",p")  # pass-through waypoint
        pts.append(dll + ("," + quote(dname) if dname else ""))
        q = {"m": HERE_MODE[mode]}
        if avoid:
            q["a"] = ",".join({"tolls": "tollroad", "highways": "motorway", "ferries": "boatFerry"}[a] for a in avoid)
        if truck and mode == "truck":
            # HERE WeGo Pro truck attributes (cm / kg)
            if truck.get("height"):
                q["vdh"] = str(int(float(truck["height"]) * 100))
            if truck.get("width"):
                q["vdw"] = str(int(float(truck["width"]) * 100))
            if truck.get("length"):
                q["vdl"] = str(int(float(truck["length"]) * 100))
            if truck.get("weight"):
                q["vw"] = str(int(float(truck["weight"]) * 1000))
            if truck.get("hazmat"):
                q["hmr"] = ",".join(truck["hazmat"]) if isinstance(truck["hazmat"], (list, tuple)) else str(truck["hazmat"])
        q["ref"] = utm or "umn"
        url = "https://share.here.com/r/" + "/".join(pts) + "?" + urlencode(q, safe=",", quote_via=quote)
        notes = ["2–100 waypoints; first = origin ('mylocation' allowed), last = destination.",
                 "m=tr (truck) needs HERE WeGo Pro – free app falls back to car."]
        out["here"] = {"label": "HERE WeGo", "url": url, "notes": notes}

    # ---- Sygic (com.sygic.aura://) --------------------------------------------
    if "sygic" in want:
        parts = ["coordinate"]
        for v in via:  # via points precede the destination, each as LON|LAT
            parts += [f"{float(v[1]):.6f}", f"{float(v[0]):.6f}"]
        parts += [f"{float(dest[1]):.6f}", f"{float(dest[0]):.6f}", SYGIC_MODE[mode]]
        raw = "com.sygic.aura://" + "|".join(parts)
        out["sygic"] = {"label": "Sygic GPS Navigation", "url": raw, "ios_url": raw.replace("|", "%7C"),
                        "notes": ["Sygic takes LONGITUDE before LATITUDE.", "Modes: drive | walk (truck profile comes from the app's vehicle settings).",
                                  "On iOS percent-encode the pipe as %7C."]}

    # ---- OpenStreetMap web directions (FOSSGIS OSRM / Valhalla) --------------
    if "osm" in want:
        pts = ([oll] if oll else []) + [_ll(v) for v in via] + [dll]
        url = f"https://www.openstreetmap.org/directions?engine={OSM_ENGINE[mode]}&route=" + ";".join(pts)
        out["osm"] = {"label": "OpenStreetMap (web)", "url": url,
                      "notes": ["Needs an origin; if omitted the site asks for one.", "Engines: fossgis_osrm_car|bike|foot, fossgis_valhalla_*"]}

    # ---- RFC 5870 geo: URI (any installed map app) ---------------------------
    if "geo" in want:
        label = quote(dname) if dname else dll
        out["geo"] = {"label": "geo: URI (any map app)", "url": f"geo:{dll}?q={dll}({label})",
                      "notes": ["Android/Linux pick the default map app; iOS ignores geo: unless a browser translates it."]}

    if "android" in want:
        out["android"] = {"label": "Android navigation intent", "url": f"google.navigation:q={dll}&mode={GOOGLE_ANDROID_MODE[mode]}",
                          "notes": ["Launches turn-by-turn immediately (Google Maps for Android)."]}
    return out


def place_links(lat, lon, name="", zoom=16, apps=("all",)):
    """Links that SHOW a place (no routing) in each app + share-friendly URLs."""
    want = set(APPS) if ("all" in apps) else set(apps)
    ll = _ll((lat, lon))
    out = {}
    if "google" in want:
        q = {"api": "1", "query": ll}
        out["google"] = {"label": "Google Maps", "url": "https://www.google.com/maps/search/?" + urlencode(q, safe=",", quote_via=quote),
                         "map_url": f"https://www.google.com/maps/@?api=1&map_action=map&center={ll}&zoom={zoom}",
                         "streetview_url": f"https://www.google.com/maps/@?api=1&map_action=pano&viewpoint={ll}",
                         "traffic_url": f"https://www.google.com/maps/@?api=1&map_action=map&center={ll}&zoom={max(zoom - 3, 3)}&layer=traffic",
                         "transit_layer_url": f"https://www.google.com/maps/@?api=1&map_action=map&center={ll}&zoom={zoom}&layer=transit"}
    if "apple" in want:
        q = {"ll": ll, "z": str(zoom)}
        if name:
            q["q"] = name
        out["apple"] = {"label": "Apple Maps", "url": "https://maps.apple.com/?" + urlencode(q, safe=",", quote_via=quote),
                        "satellite_url": "https://maps.apple.com/?" + urlencode({**q, "t": "k"}, safe=",", quote_via=quote)}
    if "waze" in want:
        out["waze"] = {"label": "Waze", "url": f"https://waze.com/ul?ll={ll}&zoom={min(zoom, 17)}",
                       "livemap_url": f"https://www.waze.com/live-map/directions?to=ll.{lat}%2C{lon}"}
    if "organic" in want:
        q = urlencode({"v": "1", "ll": ll, "n": name or ""}, safe=",", quote_via=quote)
        out["organic"] = {"label": "Organic Maps", "url": "https://omaps.app/map?" + q, "app_scheme": "om://map?" + q}
    if "comaps" in want:
        q = urlencode({"v": "1", "ll": ll, "n": name or ""}, safe=",", quote_via=quote)
        out["comaps"] = {"label": "CoMaps", "url": "https://comaps.at/map?" + q, "app_scheme": "cm://map?" + q}
    if "here" in want:
        out["here"] = {"label": "HERE WeGo", "url": f"https://share.here.com/l/{ll}" + ("," + quote(name) if name else "") + f"?z={zoom}&t=normal",
                       "traffic_url": f"https://share.here.com/l/{ll}?z={zoom}&t=traffic"}
    if "sygic" in want:
        out["sygic"] = {"label": "Sygic", "url": f"com.sygic.aura://coordinate|{float(lon):.6f}|{float(lat):.6f}|show"}
    if "osm" in want:
        out["osm"] = {"label": "OpenStreetMap", "url": f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map={zoom}/{lat}/{lon}",
                      "notes_layer_url": f"https://www.openstreetmap.org/#map={zoom}/{lat}/{lon}&layers=N"}
    if "geo" in want:
        out["geo"] = {"label": "geo: URI", "url": f"geo:{ll}?z={zoom}" + (f"&q={ll}({quote(name)})" if name else "")}
    return out


def search_links(query, near=None, apps=("all",)):
    """Open a free-text search ("vegan restaurant") in each app, optionally near (lat, lon)."""
    want = set(APPS) if ("all" in apps) else set(apps)
    out = {}
    nll = _ll(near) if near else None
    if "google" in want:
        out["google"] = {"label": "Google Maps", "url": "https://www.google.com/maps/search/?" + urlencode({"api": "1", "query": query}, quote_via=quote)}
    if "apple" in want:
        q = {"q": query}
        if nll:
            q["sll"] = nll
        out["apple"] = {"label": "Apple Maps", "url": "https://maps.apple.com/?" + urlencode(q, safe=",", quote_via=quote)}
    if "waze" in want:
        out["waze"] = {"label": "Waze", "url": "https://waze.com/ul?" + urlencode({"q": query, "navigate": "yes"}, quote_via=quote)}
    if "organic" in want:
        q = {"query": query}
        if nll:
            q["cll"] = nll
        out["organic"] = {"label": "Organic Maps", "url": "https://omaps.app/search?" + urlencode(q, safe=",", quote_via=quote),
                          "app_scheme": "om://search?" + urlencode(q, safe=",", quote_via=quote)}
    if "comaps" in want:
        q = {"query": query}
        if nll:
            q["cll"] = nll
        out["comaps"] = {"label": "CoMaps", "url": "https://comaps.at/search?" + urlencode(q, safe=",", quote_via=quote),
                         "app_scheme": "cm://search?" + urlencode(q, safe=",", quote_via=quote)}
    if "here" in want:
        out["here"] = {"label": "HERE WeGo", "url": "https://share.here.com/s/" + quote(query) + (f"?at={nll}" if nll else "")}
    if "osm" in want:
        out["osm"] = {"label": "OpenStreetMap", "url": "https://www.openstreetmap.org/search?query=" + quote(query)}
    if "geo" in want:
        out["geo"] = {"label": "geo: URI", "url": "geo:0,0?q=" + quote(query)}
    return out


def _main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("navigate"); n.add_argument("lat", type=float); n.add_argument("lon", type=float)
    n.add_argument("--name", default=""); n.add_argument("--from", dest="origin", help="lat,lon")
    n.add_argument("--via", action="append", default=[], help="lat,lon (repeatable)")
    n.add_argument("--mode", default="car", choices=MODES); n.add_argument("--app", default="all")
    n.add_argument("--avoid", default="", help="tolls,highways,ferries")
    p = sub.add_parser("place"); p.add_argument("lat", type=float); p.add_argument("lon", type=float); p.add_argument("--name", default=""); p.add_argument("--zoom", type=int, default=16); p.add_argument("--app", default="all")
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("--near", help="lat,lon"); s.add_argument("--app", default="all")
    a = ap.parse_args(argv)
    apps = tuple(x.strip() for x in a.app.split(",") if x.strip())
    unknown = set(apps) - set(APPS) - {"all"}
    if unknown:
        ap.error(f"unknown app(s): {', '.join(sorted(unknown))} (choose from {', '.join(APPS)} or all)")
    if a.cmd == "navigate":
        origin = tuple(map(float, a.origin.split(","))) if a.origin else None
        via = [tuple(map(float, v.split(","))) for v in a.via]
        res = navigate_links((a.lat, a.lon, a.name), origin, via, a.mode, apps, avoid=[x for x in a.avoid.split(",") if x])
    elif a.cmd == "place":
        res = place_links(a.lat, a.lon, a.name, a.zoom, apps)
    else:
        near = tuple(map(float, a.near.split(","))) if a.near else None
        res = search_links(a.query, near, apps)
    json.dump(res, sys.stdout, indent=2, ensure_ascii=False); print()


if __name__ == "__main__":
    _main()
