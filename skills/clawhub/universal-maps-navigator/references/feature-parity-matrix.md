# Feature-parity matrix — the 7 apps vs. what `umn` gives an agent

Legend: ✅ native · ⚠️ partial / paid / region-limited · ❌ absent.
The right-most column says how the skill delivers the capability (free/open service, deep link, or honest limitation).
Per-app detail and sources: `references/research/app-*.md` (merged from independent web-research shards).

| Capability | Google Maps | Apple Maps | Waze | Organic Maps | CoMaps | HERE WeGo | Sygic | **umn (this skill)** |
|---|---|---|---|---|---|---|---|---|
| Search / geocode | ✅ | ✅ | ✅ | ✅ offline | ✅ offline | ✅ | ✅ | `geocode`, `reverse` — Nominatim → Photon |
| Turn-by-turn directions | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | `route --steps` (OSRM/Valhalla instructions) + `navigate` deep links to start guidance in any of the 7 apps |
| Lane guidance | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | `route --steps` prints lane arrows where OSM has `turn:lanes` |
| Voice guidance | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | hand-off to the chosen app (`navigate`) |
| Alternatives | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | `route --alternatives` |
| Avoid tolls / highways / ferries | ✅ | ✅ | ✅ | ⚠️ (tolls/unpaved/ferries) | ⚠️ | ✅ | ✅ | `route --avoid …` (Valhalla) and passed into Google/HERE links |
| Walking | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | `--mode foot` |
| Cycling | ✅ | ✅ (regions) | ❌ | ✅ | ✅ | ✅ | ❌ | `--mode bike` |
| Public transport | ✅ | ✅ | ❌ | ⚠️ (subway lines) | ⚠️ | ✅ | ❌ | `transit plan / departures / stops` (Transitous, open GTFS) + transit deep links |
| Truck / RV routing | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ WeGo Pro | ✅ Sygic Truck | `--mode truck --truck-height/width/length/weight --hazmat` (Valhalla) + HERE Pro truck link params |
| Motorcycle / scooter | ✅ two-wheeler (regions) | ❌ | ✅ motorcycle | ❌ | ❌ | ⚠️ | ✅ | `--mode motorcycle` / `scooter` |
| Multi-stop & route optimisation | ✅ (≤9 stops, no optimisation) | ✅ (multi-stop) | ⚠️ (1 stop) | ✅ (waypoints) | ✅ | ✅ | ✅ | `route --via`, `trip` (optimal order) + multi-stop links (Google/HERE/Sygic/Organic) |
| Travel-time matrix / isochrones | ❌ (API only) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | `matrix`, `isochrone` — beyond any of the apps |
| Live traffic & ETA | ✅ | ✅ | ✅ crowd | ❌ | ❌ | ✅ | ✅ (licence) | `traffic` → live only with a TomTom key; otherwise traffic-layer deep links (honest) |
| Hazard / police / crash reports | ⚠️ | ⚠️ | ✅ crowd | ❌ | ❌ | ⚠️ | ⚠️ | `reports` (OSM Notes read), `report` (create a note, dry-run by default); crowd hazards stay in Waze |
| Speed-camera alerts | ✅ (regions) | ⚠️ | ✅ | ❌ | ❌ | ✅ | ✅ | `cameras`, `route --cameras` (OSM `highway=speed_camera` + `enforcement`) |
| Speed-limit display | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | `speedlimit` (OSM `maxspeed`, implicit codes translated) |
| Offline maps | ⚠️ areas, driving only | ⚠️ iOS 17+ | ❌ | ✅ full | ✅ full | ✅ | ✅ | `offline` → Geofabrik extracts + local OSRM/Valhalla + per-app instructions; `--gpx`/`--kml` exports for offline apps |
| POI along route / nearby (fuel, parking, EV, food…) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | `poi <category> --near`, `charging`, corridor search in code (`poi_search(polyline=)`) |
| EV charging & connector filters | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | `charging --min-kw` (OSM tags; OpenChargeMap with key) |
| Parking | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | `poi parking --near` |
| Weather | ⚠️ | ✅ | ✅ (hazard) | ❌ | ❌ | ❌ | ✅ | `weather <place>`, `weather A --route B` (Open-Meteo along the route) |
| Elevation / profile | ⚠️ (cycling) | ⚠️ (cycling) | ❌ | ✅ (hiking) | ✅ | ❌ | ❌ | `elevation`, `route --elevation` |
| Street View / Look Around | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | `share` gives the Google Street View URL |
| Satellite / terrain layers | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ⚠️ | `share` links with `basemap=satellite`, Apple `t=k`, HERE `t=satellite` |
| Saved places / favourites / home & work | ✅ | ✅ | ✅ | ✅ bookmarks | ✅ | ✅ | ✅ | `places save/list/forget`, `navigate home`, KML export |
| Share a location / plus code | ✅ | ✅ | ✅ | ✅ short links | ✅ | ✅ | ✅ | `share` (all app links + Plus code) |
| Explore / guides / landmarks | ✅ | ✅ | ❌ | ⚠️ (Wikipedia in place page) | ⚠️ | ⚠️ | ❌ | `nearby` (Wikipedia geosearch) |
| Privacy (no tracking) | ❌ | ⚠️ | ❌ | ✅ | ✅ | ⚠️ | ⚠️ | no account, no telemetry; only the queried coordinates reach the open services |
| CarPlay / Android Auto | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | via the app opened by `navigate` |

## Where the skill deliberately stops
* **Live crowd-sourced traffic, police & crash alerts** are proprietary probe networks (Waze/Google/HERE/TomTom/Sygic). No free API exists; `umn` never fakes it.
* **Voice guidance, AR walking, CarPlay** need a phone app — the skill hands off with a deep link instead of reinventing them.
* **Real-time transit** depends on whether the city publishes GTFS-RT feeds that Transitous ingests.
