# Free / open services used by `umn` — live-verified request shapes

All endpoints below were called successfully from the build sandbox on 2026-09-20/21 (ground truth beats
the ⚠️ CONFLICT rate-limit claims in `research/apis-routing-geocoding.md`). No key needed unless stated.
Attribution: everything OSM-based requires "© OpenStreetMap contributors".

| Capability | Service | Request shape (what the CLI sends) | Policy / notes |
|---|---|---|---|
| Geocode | **Nominatim** `https://nominatim.openstreetmap.org/search?q=…&format=jsonv2&limit=5&addressdetails=1[&countrycodes=ro]` | GET | ≤1 req/s, **identifying User-Agent mandatory** (a UA with a bogus contact such as `example.invalid` gets HTTP 403), cache results, no bulk |
| Reverse geocode | Nominatim `/reverse?lat=&lon=&format=jsonv2&zoom=18` | GET | same policy |
| Geocode fallback / autocomplete / bbox POI | **Photon** (komoot) `https://photon.komoot.io/api/?q=…&limit=&lat=&lon=[&bbox=minLon,minLat,maxLon,maxLat][&osm_tag=amenity:fuel]`, `/reverse?lat=&lon=` | GET | fair use, no hard limit published |
| Car routing, alternatives, turn-by-turn, **lane guidance**, table, trip, nearest, match | **OSRM demo** `https://router.project-osrm.org/{route,table,trip,nearest,match}/v1/driving/LON,LAT;LON,LAT?overview=full&geometries=geojson&steps=true&alternatives=true` | GET | demo server, low volume; lanes in `steps[].intersections[0].lanes` |
| Bike / foot routing (OSRM) | **FOSSGIS OSRM** `https://routing.openstreetmap.de/routed-{bike,foot,car}/route/v1/driving/…` | GET | same API as OSRM |
| Any-profile routing (auto, **truck** w/ dimensions & hazmat, bicycle, pedestrian, motor_scooter, motorcycle, bus, taxi), avoid tolls/highways/ferries, time-dependent, alternates | **Valhalla (FOSSGIS)** `https://valhalla1.openstreetmap.de/route` POST `{"locations":[{lat,lon}…],"costing":"truck","costing_options":{"truck":{"height":4.1,"width":2.6,"length":16.5,"weight":40,"hazmat":true,"use_tolls":0,"use_highways":0}},"directions_options":{"units":"kilometers","language":"en-US"},"alternates":2,"date_time":{"type":1,"value":"2026-09-22T08:00"}}` | POST JSON | shape = polyline **precision 6**; verified all 8 costings |
| Isochrones | Valhalla `/isochrone` `{"locations":[…],"costing":"pedestrian","contours":[{"time":10},{"time":20}],"polygons":true}` | POST | GeoJSON out |
| Matrix | Valhalla `/sources_to_targets` (any costing) · OSRM `/table/v1/driving/…?annotations=duration,distance` | POST/GET | |
| Multi-stop optimisation | Valhalla `/optimized_route` (any costing) · OSRM `/trip/v1/driving/…?source=first&destination=last&roundtrip=false` | POST/GET | |
| Elevation profile | Valhalla `/height` `{"range":true,"shape":[…]}` · **OpenTopoData** `https://api.opentopodata.org/v1/srtm90m?locations=LAT,LON|LAT,LON` (`aster30m` fallback) | GET | OpenTopoData: ≤100 locations/request, 1 req/s, 1000/day; **LAT,LON order** |
| POI search by tag / name / brand, speed cameras, parking, fuel, EV, stops | **Overpass API** `https://overpass-api.de/api/interpreter` POST `data=[out:json][timeout:25];(nwr["amenity"="fuel"](around:1500,LAT,LON););out center tags 45;` — corridor search: `around:80,lat1,lon1,lat2,lon2,…` | POST form | bursts get 429/504 → the CLI paces 1 req/s, retries mirrors (`overpass.kumi.systems`, `overpass.private.coffee`) and falls back to Photon |
| Posted speed limits | Overpass `way(around:40,LAT,LON)["highway"]["maxspeed"];out tags geom;` | POST | implicit values like `RO:urban` are translated |
| Weather now / hourly / along a route | **Open-Meteo** `https://api.open-meteo.com/v1/forecast?latitude=a,b&longitude=c,d&current=temperature_2m,precipitation,weather_code,wind_speed_10m,wind_gusts_10m,visibility&hourly=…&forecast_hours=6&timezone=auto` | GET | multi-point in one call; free non-commercial |
| **Public transport** routing, live departures, stop search | **Transitous (MOTIS)** `https://api.transitous.org/api/v1/plan?fromPlace=LAT,LON&toPlace=LAT,LON[&time=ISO-UTC][&arriveBy=true][&wheelchair=true][&maxTransfers=]&numItineraries=3` · `/geocode?text=…&type=STOP` · `/stoptimes?stopId=…&n=10[&time=]` · `/reverse-geocode?place=LAT,LON` | GET | community project aggregating open GTFS/GTFS-RT worldwide; coverage varies by city |
| Community map reports | **OSM Notes API** `https://api.openstreetmap.org/api/0.6/notes.json?bbox=W,S,E,N&closed=0&limit=20` · create: `POST /api/0.6/notes.json?lat=&lon=&text=` (anonymous allowed; the CLI dry-runs unless `--yes`) | GET/POST | public content — be factual |
| Landmarks / explore | **Wikipedia geosearch** `https://{lang}.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=LAT|LON&gsradius=1000&gslimit=10&format=json` | GET | CC BY-SA |
| Offline data | **Geofabrik** index `https://download.geofabrik.de/index-v1-nogeom.json` → `urls.pbf` per region | GET | feed to local OSRM/Valhalla/Nominatim; the CLI honours `osrm_url`, `valhalla_url`, `overpass_url` overrides |
| Plus codes | computed locally (Open Location Code) | — | e.g. Eiffel Tower `8FW4V75V+8Q` |

## Optional keys (unlock extra providers; never required)

| Key (`umn config set <key> …`) | Adds | Free tier (per vendor pages, may change) |
|---|---|---|
| `ors_key` | OpenRouteService directions (`driving-hgv` trucks, `cycling-*`, wheelchair) with `avoid_features`, alternative routes | ~2 000 directions/day |
| `openchargemap_key` | OpenChargeMap live network data (connector types, power, usage cost) instead of OSM tags | free key |
| `tomtom_key` | live traffic flow (`/traffic/services/4/flowSegmentData/absolute/10/json?point=`) + incidents (`/traffic/services/5/incidentDetails?bbox=`) | 2 500 req/day |

## Known dead ends (do not retry)
* `api.open-elevation.com` — TLS certificate expired at build time; OpenTopoData used instead.
* OpenChargeMap without key → 403; Transitland v2 without key → 401 (Transitous replaces it).
* No keyless live traffic API exists anywhere — `umn traffic` says so and links the apps' traffic layers.
