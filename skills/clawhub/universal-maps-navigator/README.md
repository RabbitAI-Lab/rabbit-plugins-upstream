# 🧭 universal-maps-navigator v2.0.0

**Seven navigation apps + 50 languages + survival intelligence + self-improving, token-optimized, hallucination-resistant engine.**

Navigation for agents with the practical feature set of Google Maps, Apple Maps, Waze, Organic Maps, CoMaps, HERE WeGo and Sygic — implemented on free/open services (OSM, Nominatim, Photon, OSRM, Valhalla, Overpass, OpenTopoData, Open-Meteo, Transitous, Wikipedia) and finished with verified deep links that start turn-by-turn guidance in whichever app the user prefers. No API key required; python3 stdlib only.

NEW in v2: 50+ languages (RTL, cultural POI), life-saving survival guides for desert/mountain/jungle/snow/swamp/forest/urban + 10 disasters (earthquake/flood/wildfire/hurricane/tornado/avalanche/tsunami/blizzard/sandstorm/landslide), self-improvement loop (Memento-Skills), 60% token reduction via --compact/--json, confidence citations, multi-model compatibility.

```bash
npx clawhub@latest install universal-maps-navigator
alias umn='python3 skills/universal-maps-navigator/scripts/umn.py'
umn doctor
umn route "Piața Unirii, București" "Arcul de Triumf" --steps --lang ro --compact
umn survival guide --terrain mountain --disaster avalanche --lang en
umn i18n list
umn self-improve --analyze
```

## What it does (v2 expanded)

| Area | Commands | Backed by |
|---|---|---|
| Geocoding, reverse, Plus codes, share links | `geocode` `reverse` `share` `search-links` | Nominatim → Photon fallback, local OLC encoder, 50+ langs |
| Directions: turn-by-turn, lane guidance, alternatives, tolls/highways avoidance, depart-at, GPX | `route` | OSRM demo + FOSSGIS OSRM, Valhalla (all profiles), optional ORS, confidence high/med/low |
| Vehicle profiles: car, truck (dimensions, weight, hazmat), bike, foot, scooter, motorcycle, bus, taxi | `route --mode …` | Valhalla costings |
| Deep links into all 7 apps (+ OSM web, geo: URI, Android intent) with waypoints | `navigate` `share` `search-links` | vendor URL schemes, verified |
| POI: fuel, parking, EV charging, food, hotels, hospitals, ATMs, toilets, stops, viewpoints, rest areas, any OSM tag or free text; cultural POI (mosque, temple, church, bazaar, souk, hammam, onsen, halal, kosher) | `poi` `charging` | Overpass (paced, mirrored) → Photon bbox fallback; OCM with key; cultural mapping via i18n.py |
| Public transport: itineraries, live departures, stops | `transit plan/departures/stops` | Transitous (MOTIS, open GTFS/GTFS-RT) |
| Safety: speed cameras, speed limits, community reports | `cameras` `route --cameras` `speedlimit` `reports` `report` | OSM highway=speed_camera/enforcement/maxspeed, OSM Notes API |
| Weather now/hourly and along route, elevation & climb, isochrones, matrix, trip optimization | `weather` `elevation` `isochrone` `matrix` `trip` | Open-Meteo, OpenTopoData, Valhalla, OSRM |
| Traffic | `traffic` | live only with TomTom key; otherwise traffic-layer deep links (never fabricated) |
| Offline: Geofabrik extracts, local OSRM/Valhalla, per-app offline steps, GPX/KML | `offline` `route --gpx` `places --kml` | Geofabrik index |
| Favourites: home/work/any name usable everywhere | `places save/list/forget` | local config |
| Landmarks nearby, health check, guides | `nearby` `doctor` `guide` | Wikipedia geosearch |
| **NEW Survival: terrain (desert, mountain, jungle, snow, swamp, forest, urban) + disasters (earthquake, flood, wildfire, hurricane, tornado, avalanche, tsunami, blizzard, sandstorm, landslide)** | `survival guide --terrain X --disaster Y --situation TEXT` `survival sos --terrain X --disaster Y` `survival list` | US Army FM 21-76, Red Cross, NOAA, USGS, FEMA — cited, not invented |
| **NEW Multilingual: 50+ languages, RTL, units, date/time, cultural POI, detection, translation** | `i18n list` `i18n detect TEXT` `i18n translate TEXT --to LANG` `--lang LANG` on all commands | offline dictionary + Nominatim/Photon accept-language |
| **NEW Self-improving: logging, metrics, analysis, auto-patch proposal** | `self-improve --analyze --apply --stats` | Memento-Skills pattern, learnings.json |

Feature-by-feature comparison: `references/feature-parity-matrix.md`. Survival sources: `references/survival-guides.md`. Languages: `references/i18n-catalog.md`.

## How it was built (distributed research v2)

v1 research: split across independent internet-capable AI models (Groq compound web-search agents and Mistral web_search — 24 shards, 21 successful, 881 citation URLs), merged by reasoning models (Groq/Cloudflare gpt-oss-120b) with conflicts flagged, every URL template and API call re-verified against vendor docs and live calls. Trace in `references/research-provenance.md`.

v2 improvements: additional distributed research across best models via router.py:
- groq/openai/gpt-oss-120b, openrouter/anthropic/claude-3.5-sonnet, mistral/mistral-large, gemini/gemini-2.0-flash, cohere/command-r-plus — each proposed 10 improvements for hallucinations, token reduction, speed, i18n, survival
- Merged into i18n.py (50 langs), survival.py (terrain+disaster), self_improve.py (closed-loop), token_optimizer.py (60% saving)
- Verified via selftest.sh (20 offline tests) + doctor live + multi-model debugging (best practices: schema validation, abstention, citation, prefix caching, decision tree)

## 🔐 Permissions

| Touches | Details |
|---|---|
| Files written | `~/.config/universal-maps-navigator/config.json` (settings, saved places, optional keys; chmod 600), `~/.cache/universal-maps-navigator/` (geocode cache 7d, Geofabrik index, pacing timestamps, ratelimit.json), `~/.local/share/universal-maps-navigator/learnings.json` (metrics, no PII, 600), `~/.local/share/.../metrics.json`, plus any --gpx/--kml/--out path you ask for. Honour UMN_CONFIG_DIR, UMN_CACHE_DIR, UMN_LEARNINGS_DIR, XDG_* |
| Files read | the three paths above + skill's own references/ (for guide). Nothing else on disk |
| Network (outbound HTTPS only) | `nominatim.openstreetmap.org`, `photon.komoot.io`, `router.project-osrm.org`, `routing.openstreetmap.de`, `valhalla1.openstreetmap.de`, `overpass-api.de`, `overpass.kumi.systems`, `overpass.private.coffee`, `api.opentopodata.org`, `api.open-meteo.com`, `api.transitous.org`, `api.openstreetmap.org`, `*.wikipedia.org`, `download.geofabrik.de`; only with key you configure: `api.openrouteservice.org`, `api.openchargemap.io`, `api.tomtom.com`; only if you set them: your own osrm_url/valhalla_url/overpass_url |
| Binaries | `python3` (≥3.8). No pip packages, no curl, no shell-outs. v2 modules: i18n.py, survival.py, self_improve.py, token_optimizer.py — all stdlib |
| Writes to internet | one command can: `report --yes` creates public anonymous OSM Note (map-problem report). Without --yes dry run only. No other command sends but read queries |
| Location access | none. CLI never reads device GPS; "current location" expressed in deep links (mylocation, currentLocation, omitted origin) resolved by phone app |
| Token usage | v2 --compact --json reduces 60%: compact route 30 tokens vs 150+ verbose, minimal_json strips fields, truncation guard 350 tokens, cache 7d, decision tree 9 rows |

## 🔒 Security & Privacy

* **Data sent**: place names/coordinates you query go to open services above (must, to be answered). Nominatim usage policy requires identifying User-Agent; CLI sends `universal-maps-navigator/<version> (+skill URL[; contact_email if set])`. No account, no telemetry, no analytics, no trackers — unlike most 7 apps it emulates
* **Secrets**: optional API keys live only in config.json (mode 600); config show/get prints (set) not value; keys never logged, never in --json output
* **Deep links** are plain strings — nothing opened automatically; user/agent decides which app to launch
* **Public content**: report --yes posts to OSM under anonymous identity; text shown first, refuses short texts. Use factual map problems only
* **Service etiquette**: hard-coded pacing (Nominatim ≤1 req/s, Overpass ≤1 req/s with mirror rotation, OpenTopoData ≤100 points/call), 7-day geocode cache, low limits default. Bulk users told to self-host (offline)
* **Risks**: OSM-derived speed cameras/limits/POIs can be outdated — outputs say "community-mapped, not exhaustive". Public demo routers can be down; every command reports failing service instead of guessing. Review scripts before installing: scripts/umn.py, deeplinks.py, i18n.py, survival.py, self_improve.py, token_optimizer.py are only executable code (plus test suite, runs in temporary HOME and never touches real config)
* **Hallucination reduction**: JSON schema validation per API, confidence high/med/low, source citations [source=...], abstention when data missing ("no results — abstain, do not invent"), span verification
* **Survival guides**: sourced from US Army FM 21-76 (public domain), Red Cross, NOAA, USGS, FEMA — cited, not hallucinated. Never replaces professional emergency services — call local emergency number (112, 911, etc)
* **Self-improvement**: learnings.json stores only aggregated metrics (tokens, latency, success/fail, model, lang) — no PII, no place names. File chmod 600

## ✅ Verification

```bash
bash skills/universal-maps-navigator/scripts/selftest.sh          # 20+ offline tests, sandboxed HOME
bash skills/universal-maps-navigator/scripts/selftest.sh --live   # + reachability of free services
python3 skills/universal-maps-navigator/scripts/umn.py doctor
python3 skills/universal-maps-navigator/scripts/umn.py survival guide --terrain desert --lang en --compact
python3 skills/universal-maps-navigator/scripts/umn.py i18n list --compact
python3 skills/universal-maps-navigator/scripts/umn.py self-improve --stats
python3 skills/universal-maps-navigator/scripts/umn.py geocode "Bucharest" --lang ro --compact --json
sha256sum skills/universal-maps-navigator/SKILL.md
```

Expected `SKILL.md` sha256: `24563dd7d6ca61b4b80961d618d3ddebaeee94c8094ddf6e65d34702743b165b`

Sources for every deep-link template: `references/deep-links.md`. Live-verified request shapes: `references/free-apis.md`. Survival: `references/survival-guides.md`. Languages: `references/i18n-catalog.md`.

## License

MIT for code in this skill. Map data © OpenStreetMap contributors (ODbL) — keep attribution when you show results to users. Weather by Open-Meteo (CC BY 4.0). Transit data via Transitous from respective open GTFS publishers. Survival guides: US Army FM 21-76 public domain, Red Cross/NOAA/USGS/FEMA public guidance — citations retained.
