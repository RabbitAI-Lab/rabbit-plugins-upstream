#!/usr/bin/env python3
"""Generate one self-contained-ish HTML detail page per workout, plus an
index. Charts/stats are inline SVG (offline); the route map uses Leaflet +
Esri World Imagery satellite tiles loaded from CDNs, so it needs internet
access to render (everything else on the page works offline).
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.query import query
from lib import svg
from lib.geo import haversine_m, douglas_peucker, km_splits

REPORTS_DIR = Path(__file__).parent / "reports" / "workouts"

HTML_HEAD = """<!doctype html>
<html><head><meta charset="utf-8"><title>Workout — {title}</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<style>
  :root {{ color-scheme: dark; }}
  body {{ background:#10121a; color:#e6e9f0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
          margin:0; padding:24px; }}
  a {{ color:#5ec8f8; }}
  h1 {{ font-size:20px; margin:0 0 4px; }}
  .sub {{ color:#8890a0; font-size:13px; margin-bottom:20px; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(320px,1fr)); gap:16px; }}
  .card {{ background:#181b24; border:1px solid #2a2f3a; border-radius:10px; padding:16px; }}
  .card h2 {{ font-size:14px; text-transform:uppercase; letter-spacing:.05em; color:#8890a0; margin:0 0 12px; }}
  .headline {{ display:flex; flex-wrap:wrap; gap:20px; margin-bottom:20px; }}
  .stat {{ min-width:110px; }}
  .stat .v {{ font-size:22px; font-weight:600; }}
  .stat .l {{ font-size:11px; color:#8890a0; text-transform:uppercase; }}
  .tiles {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(150px,1fr)); gap:10px; }}
  .tile {{ background:#10121a; border-radius:8px; padding:8px; }}
  .tile .l {{ font-size:11px; color:#8890a0; }}
  .tile .v {{ font-size:14px; font-weight:600; margin-bottom:4px; }}
  .note {{ color:#8890a0; font-size:12px; margin-top:8px; }}
  table {{ width:100%; border-collapse:collapse; font-size:13px; }}
  th, td {{ text-align:left; padding:4px 8px; border-bottom:1px solid #2a2f3a; }}
  th {{ color:#8890a0; font-weight:500; text-transform:uppercase; font-size:11px; }}
  #map {{ height:420px; border-radius:8px; }}
</style></head><body>
<div class="sub"><a href="index.html">&larr; All workouts</a></div>
<h1>{title}</h1>
<div class="sub">{sub}</div>
"""


def slugify(name):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", name.lower())).strip("-")


def fmt(v, unit="", digits=1):
    if v is None:
        return "–"
    return f"{v:,.{digits}f}{unit}"


def fmt_duration(seconds):
    if seconds is None:
        return "–"
    h, rem = divmod(int(seconds), 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def fmt_pace(min_per_km):
    if min_per_km is None or min_per_km <= 0:
        return "–"
    m = int(min_per_km)
    s = round((min_per_km - m) * 60)
    if s == 60:
        m, s = m + 1, 0
    return f"{m}:{s:02d}/km"


def fetch_workouts():
    return query("SELECT id, date::VARCHAR AS date, name, duration_s, is_indoor, location, "
                 "temperature_c, humidity_pct, intensity, distance_km, avg_hr, min_hr, max_hr, "
                 "avg_speed, max_speed, elevation_up_m, active_energy_kj, total_energy_kj, "
                 "step_cadence, flights_climbed FROM workouts ORDER BY date DESC")


def fetch_route(workout_id):
    return query(f"SELECT seq, strftime(ts, '%H:%M:%S') AS ts_label, epoch(ts) AS ts_epoch, "
                 f"lat, lon, altitude, speed FROM workout_route "
                 f"WHERE workout_id='{workout_id}' ORDER BY seq")


def fetch_hr(workout_id):
    return query(f"SELECT strftime(ts, '%H:%M') AS ts_label, epoch(ts) AS ts_epoch, "
                 f"min, avg, max FROM workout_hr WHERE workout_id='{workout_id}' ORDER BY ts_epoch")


def fetch_hr_recovery(workout_id):
    return query(f"SELECT seq, min, avg, max FROM workout_hr_recovery "
                 f"WHERE workout_id='{workout_id}' ORDER BY seq")


def downsample(seq, n=200):
    if len(seq) <= n:
        return seq
    stride = len(seq) / n
    idx = sorted({min(len(seq) - 1, int(i * stride)) for i in range(n)})
    return [seq[i] for i in idx]


def cumulative_km(route):
    cum, out = 0.0, [0.0]
    for prev, cur in zip(route, route[1:]):
        cum += haversine_m(prev["lat"], prev["lon"], cur["lat"], cur["lon"]) / 1000
        out.append(cum)
    return out


def build_stat_tiles(w):
    tiles = []

    def tile(label, value):
        tiles.append((label, value))

    if w["distance_km"] is not None:
        tile("Distance", fmt(w["distance_km"], " km"))
    if w["avg_hr"] is not None:
        tile("Avg HR", fmt(w["avg_hr"], " bpm", 0))
    if w["max_hr"] is not None:
        tile("Max HR", fmt(w["max_hr"], " bpm", 0))
    if w["avg_speed"] is not None:
        tile("Avg Speed", fmt(w["avg_speed"], " km/h"))
    if w["max_speed"] is not None:
        tile("Max Speed", fmt(w["max_speed"], " km/h"))
    if w["elevation_up_m"] is not None:
        tile("Elevation Gain", fmt(w["elevation_up_m"], " m", 0))
    if w["active_energy_kj"] is not None:
        tile("Active Cal", fmt(w["active_energy_kj"] / 4.184, " kcal", 0))
    if w["total_energy_kj"] is not None:
        tile("Total Cal", fmt(w["total_energy_kj"] / 4.184, " kcal", 0))
    if w["step_cadence"] is not None:
        tile("Cadence", fmt(w["step_cadence"], " spm", 0))
    if w["flights_climbed"] is not None:
        tile("Flights", fmt(w["flights_climbed"], "", 0))
    if w["temperature_c"] is not None:
        tile("Temp", fmt(w["temperature_c"], "°C", 0))
    if w["humidity_pct"] is not None:
        tile("Humidity", fmt(w["humidity_pct"], "%", 0))
    if w["intensity"] is not None:
        tile("Intensity", fmt(w["intensity"], "", 1))
    if w["location"] is not None:
        tile("Location", w["location"])
    return tiles


def render_workout(w):
    is_cycling = "cycling" in w["name"].lower()
    route = fetch_route(w["id"])
    hr = fetch_hr(w["id"])
    hr_recovery = fetch_hr_recovery(w["id"])

    html = [HTML_HEAD.format(title=w["name"], sub=f'{w["date"]} &middot; {fmt_duration(w["duration_s"])}')]

    html.append('<div class="headline">')
    html.append(f'<div class="stat"><div class="v">{fmt_duration(w["duration_s"])}</div><div class="l">Duration</div></div>')
    if w["distance_km"] is not None:
        html.append(f'<div class="stat"><div class="v">{fmt(w["distance_km"], " km")}</div><div class="l">Distance</div></div>')
    if w["avg_hr"] is not None:
        html.append(f'<div class="stat"><div class="v">{fmt(w["avg_hr"], "", 0)}</div><div class="l">Avg HR (bpm)</div></div>')
    if w["active_energy_kj"] is not None:
        html.append(f'<div class="stat"><div class="v">{fmt(w["active_energy_kj"]/4.184, "", 0)}</div><div class="l">Active kcal</div></div>')
    html.append("</div>")

    html.append('<div class="grid">')

    # Map card
    if route:
        simplified = douglas_peucker([(p["lat"], p["lon"]) for p in route], epsilon_m=8.0)
        html.append('<div class="card" style="grid-column:1/-1"><h2>Route</h2><div id="map"></div>')
        html.append(f'<div class="note">{len(route):,} GPS points simplified to {len(simplified):,} for the route line. '
                    f'Requires internet to load the satellite map tiles.</div></div>')
        html.append('<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>')
        html.append('<script>')
        html.append(f'const route = {json.dumps(simplified)};')
        html.append("""
const map = L.map('map');
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
  attribution: 'Tiles &copy; Esri', maxZoom: 19
}).addTo(map);
if (route.length) {
  const poly = L.polyline(route, {color:'#5ec8f8', weight:3}).addTo(map);
  map.fitBounds(poly.getBounds(), {padding:[20,20]});
  L.circleMarker(route[0], {color:'#4ade80', radius:6, fillColor:'#4ade80', fillOpacity:1}).addTo(map).bindTooltip('Start');
  L.circleMarker(route[route.length-1], {color:'#f87171', radius:6, fillColor:'#f87171', fillOpacity:1}).addTo(map).bindTooltip('End');
} else {
  map.setView([0,0], 2);
}
""")
        html.append('</script>')
    elif w["is_indoor"]:
        html.append('<div class="card"><h2>Route</h2><div class="note">Indoor workout — no GPS route.</div></div>')

    # Elevation + speed/pace charts from route
    if route:
        cum = cumulative_km(route)
        indexed = list(zip(cum, route))
        sampled = downsample(indexed, 200)
        elev_vals = [(f"{c:.1f}", p["altitude"]) for c, p in sampled]
        html.append('<div class="card"><h2>Elevation</h2>')
        html.append(svg.line_chart(elev_vals, color=svg.PALETTE["accent2"], y_fmt=lambda v: f"{v:.0f}m"))
        html.append('<div class="note">Altitude (m) vs. distance (km)</div></div>')

        if is_cycling:
            speed_vals = [(f"{c:.1f}", p["speed"] * 3.6) for c, p in sampled]
            html.append('<div class="card"><h2>Speed</h2>')
            html.append(svg.line_chart(speed_vals, y_fmt=lambda v: f"{v:.0f}"))
            html.append('<div class="note">Speed (km/h) vs. distance (km)</div></div>')
        else:
            pace_vals = [(f"{c:.1f}", 60 / (p["speed"] * 3.6) if p["speed"] and p["speed"] > 0.1 else None)
                         for c, p in sampled]
            html.append('<div class="card"><h2>Pace</h2>')
            html.append(svg.line_chart(pace_vals, y_fmt=lambda v: f"{v:.0f}'"))
            html.append('<div class="note">Pace (min/km) vs. distance (km)</div></div>')

        # Splits table, GPS workouts >= 1km only
        if w["distance_km"] and w["distance_km"] >= 1:
            splits = km_splits([{"lat": p["lat"], "lon": p["lon"], "ts": p["ts_epoch"]} for p in route])
            if splits:
                html.append('<div class="card"><h2>Splits</h2><table><tr><th>Km</th><th>Split</th><th>Pace</th></tr>')
                for s in splits:
                    html.append(f'<tr><td>{s["km"]}</td><td>{fmt_duration(s["split_seconds"])}</td>'
                                f'<td>{fmt_pace(s["pace_min_per_km"])}</td></tr>')
                html.append('</table></div>')

    # HR chart
    if hr:
        hr_vals = [(r["ts_label"], r["avg"]) for r in hr]
        html.append('<div class="card"><h2>Heart Rate</h2>')
        html.append(svg.line_chart(hr_vals, color=svg.PALETTE["accent2"], y_fmt=lambda v: f"{v:.0f}"))
        html.append('<div class="note">Avg bpm per minute</div></div>')

    # HR recovery
    if hr_recovery:
        rec_vals = [r["avg"] for r in hr_recovery]
        html.append('<div class="card"><h2>HR Recovery</h2>')
        html.append(svg.sparkline(rec_vals, width=280, height=60))
        html.append(f'<div class="note">{fmt(hr_recovery[0]["avg"], " bpm", 0)} &rarr; '
                    f'{fmt(hr_recovery[-1]["avg"], " bpm", 0)} over {len(hr_recovery)} min post-workout</div></div>')

    # Summary stat tiles
    html.append('<div class="card"><h2>Summary</h2><div class="tiles">')
    for label, value in build_stat_tiles(w):
        html.append(f'<div class="tile"><div class="v">{value}</div><div class="l">{label}</div></div>')
    html.append('</div></div>')

    html.append('</div></body></html>')

    out_path = REPORTS_DIR / f'{w["date"]}-{slugify(w["name"])}.html'
    out_path.write_text("".join(html))
    return out_path


INDEX_HEAD = """<!doctype html>
<html><head><meta charset="utf-8"><title>Workouts</title>
<style>
  :root { color-scheme: dark; }
  body { background:#10121a; color:#e6e9f0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
         margin:0; padding:24px; }
  a { color:#5ec8f8; text-decoration:none; }
  a:hover { text-decoration:underline; }
  h1 { font-size:20px; margin:0 0 20px; }
  table { width:100%; max-width:720px; border-collapse:collapse; font-size:14px; }
  th, td { text-align:left; padding:8px; border-bottom:1px solid #2a2f3a; }
  th { color:#8890a0; font-weight:500; text-transform:uppercase; font-size:11px; }
</style></head><body>
<h1>Workouts</h1>
<table><tr><th>Date</th><th>Type</th><th>Duration</th><th>Distance</th><th>Cal</th></tr>
"""


def render_index(workouts):
    html = [INDEX_HEAD]
    for w in workouts:
        link = f'{w["date"]}-{slugify(w["name"])}.html'
        cal = fmt(w["active_energy_kj"] / 4.184, "", 0) if w["active_energy_kj"] is not None else "–"
        dist = fmt(w["distance_km"], " km") if w["distance_km"] is not None else "–"
        html.append(f'<tr><td><a href="{link}">{w["date"]}</a></td><td>{w["name"]}</td>'
                    f'<td>{fmt_duration(w["duration_s"])}</td><td>{dist}</td><td>{cal}</td></tr>')
    html.append('</table></body></html>')
    (REPORTS_DIR / "index.html").write_text("".join(html))


def main(force=False, out_dir=None):
    global REPORTS_DIR
    if out_dir:
        REPORTS_DIR = Path(out_dir)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    workouts = fetch_workouts()
    if not workouts:
        print("No workouts ingested yet.")
        return

    rendered = 0
    for w in workouts:
        out_path = REPORTS_DIR / f'{w["date"]}-{slugify(w["name"])}.html'
        if out_path.exists() and not force:
            continue
        render_workout(w)
        rendered += 1

    render_index(workouts)
    print(f"rendered {rendered} workout page(s), wrote index.html ({len(workouts)} total)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="Re-render all workout pages, not just missing ones")
    ap.add_argument("--out-dir", "-o", help="Directory to write workout pages + index.html into (default: reports/workouts/)")
    args = ap.parse_args()
    main(args.force, args.out_dir)
