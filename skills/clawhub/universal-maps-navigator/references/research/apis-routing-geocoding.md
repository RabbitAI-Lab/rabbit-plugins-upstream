<!-- merged by cloudflare/@cf/openai/gpt-oss-120b from 2 shard(s) on 2026-09-20 -->

**Universal Maps & Navigation – consolidated free/open‑web API reference (HTTPS, no SDK).**  

---

### 1️⃣ API catalogue (key facts)

| API | Base URL | API‑key? | Example endpoint template* | Rate limits / usage policy | Attribution required | Docs |
|-----|----------|----------|----------------------------|----------------------------|----------------------|------|
| **Nominatim** (OSM geocoder) | `https://nominatim.openstreetmap.org/` | No | `search?format=json&q={query}&limit=1`  <br> `reverse?format=json&lat={lat}&lon={lon}` | ⚠️ **CONFLICT** – shard 1: ≤ 1 req /s per IP (policy [1])  <br> shard 2: 1 req /s **and** 30 req /h per IP (policy [1]) | “© OpenStreetMap contributors” (display on every result page) | [1] https://operations.osmfoundation.org/policies/nominatim/ |
| **Photon** (Komoot) | `https://photon.komoot.io/` (also `https://photon.komoot.de/`) | No | `api/?q={query}&limit=1`  <br> `reverse?lat={lat}&lon={lon}` | ⚠️ **CONFLICT** – shard 1: recommends ≤ 1 req /s (policy [2])  <br> shard 2: no official limit, “polite usage” (docs [2]) | “© OpenStreetMap contributors” | [2] https://photon.komoot.io/ |
| **OSRM** (public demo) | `https://router.project-osrm.org/` | No | `route/v1/{profile}/{lon1},{lat1};{lon2},{lat2}?overview=full&geometries=geojson` (profile = driving | biking | foot) | ⚠️ **CONFLICT** – shard 1: **UNVERIFIED** (low‑volume testing only, no SLA) [3]  <br> shard 2: “no strict limit, avoid heavy usage” (docs [4]) | “© OpenStreetMap contributors” | [3] https://github.com/Project-OSRM/osrm-backend/wiki/FAQ#how-can-i-use-the-public-demo-server  <br> [4] http://project-osrm.org/docs/v5.24/api/ |
| **Valhalla** (public instance) | `https://valhalla1.openstreetmap.de/` | No | `route?json={"locations":[{"lat":{lat1},"lon":{lon1}},{"lat":{lat2},"lon":{lon2}}],"costing":"auto"}`  <br> `isochrone?json={...}` | No explicit limit; “reasonable use” advised (both shards) | “© OpenStreetMap contributors” | [5] https://github.com/valhalla/valhalla/wiki/Valhalla-API |
| **OpenRouteService** (ORS) | `https://api.openrouteservice.org/` | Yes (free API key) | `v2/directions/{profile}?api_key={key}&start={lon1},{lat1}&end={lon2},{lat2}`  <br> `v2/isochrones/{profile}?api_key={key}&locations={lon},{lat}&range={seconds}`  <br> `v2/matrix/{profile}?api_key={key}&...` | ⚠️ **CONFLICT** – shard 1: 2 000 req / day, 40 req / min (free tier) [6]  <br> shard 2: 20 req / min, 40 k req / month (free tier) [7] | “© OpenStreetMap contributors, © OpenRouteService” | [6] https://openrouteservice.org/sign-up/ (rate‑limit section)  <br> [7] https://openrouteservice.org/dev/#/api-docs |
| **GraphHopper** | `https://graphhopper.com/api/1/` | Yes (free key) | `route?key={key}&point={lat1},{lon1}&point={lat2},{lon2}&vehicle=car&format=json`  <br> `isochrone?key={key}&point={lat},{lon}&vehicle=bike&time_limit=600` | ⚠️ **CONFLICT** – shard 1: 2 500 req / day, burst 10 req / s [8]  <br> shard 2: 50 req / day (free tier) [9] | “© OpenStreetMap contributors, © GraphHopper” | [8] https://docs.graphhopper.com/#section/Rate-Limits  <br> [9] https://www.graphhopper.com/api/1/docs/ |
| **Overpass API** (POI) | `https://overpass-api.de/api/` | No | `interpreter?data=[out:json];node[amenity=restaurant]({south},{west},{north},{east});out;` | ⚠️ **CONFLICT** – shard 1: 2 req / min per IP [10]  <br> shard 2: “no strict limit, avoid heavy usage” (docs [11]) | “© OpenStreetMap contributors” | [10] https://overpass-api.de/faq.html  <br> [11] https://overpass-turbo.eu/ |
| **Open‑TopoData / Open‑Elevation** | `https://api.opentopodata.org/v1/` (e.g. `eudem25m`) | No | `{dataset}?locations={lon1},{lat1}|{lon2},{lat2}` | ⚠️ **CONFLICT** – shard 1: 1 req /s, 10 000 req / day [12]  <br> shard 2: 100 req / day (free tier) [13] | “© OpenTopoData” | [12] https://opentopodata.org/ (terms & limits)  <br> [13] https://opentopodata.org/ |
| **Open‑Meteo** (weather) | `https://api.open-meteo.com/v1/` | No | `forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation&timezone=auto` | shard 1: Unlimited for non‑commercial; reasonable use ≤ 10 req /s [14]  <br> shard 2: “no strict limit, avoid heavy usage” [15] | Recommended “Data source: Open‑Meteo” (no legal requirement) | [14] https://open-meteo.com/en/docs  <br> [15] https://open-meteo.com/en/docs |
| **OSM Tile Server** (raster) | `https://tile.openstreetmap.org/{z}/{x}/{y}.png` | No | `…/13/3556/2256.png` | ⚠️ **CONFLICT** – shard 1: ≤ 2 req /s per IP; heavy use → own tiles [16]  <br> shard 2: “no strict limit, avoid heavy usage” [17] | “© OpenStreetMap contributors” | [16] https://operations.osmfoundation.org/policies/tiles/  <br> [17] https://operations.osmfoundation.org/policies/tiles/ |
| **Wikidata / Wikipedia** (geosearch) | `https://www.wikidata.org/w/api.php` <br> `https://en.wikipedia.org/w/api.php` | No | `action=wbsearchentities&search={query}&language=en&format=json` (Wikidata)  <br> `action=query&list=geosearch&gscoord={lat}|{lon}&gsradius=1000&format=json` (Wikipedia) | ⚠️ **CONFLICT** – shard 1: 200 req / sec per IP (MediaWiki limits) [18]  <br> shard 2: “no strict limit, avoid heavy usage” [19] | “CC‑BY‑SA 3.0” (both) | [18] https://www.mediawiki.org/wiki/API:Etiquette  <br> [19] https://www.mediawiki.org/wiki/API:Etiquette |
| **Transitland / OpenTripPlanner** (public transit) | `https://api.transit.land/v1/` | No | `stops?lat={lat}&lon={lon}&radius=500`  <br> `routes?bbox={lon1},{lat1},{lon2},{lat2}` | ⚠️ **CONFLICT** – shard 1: 60 req / min per IP [20]  <br> shard 2: “no strict limit, avoid heavy usage” [21] | “© OpenStreetMap & GTFS providers” (see dataset) | [20] https://transit.land/documentation/api/  <br> [21] https://transit.land/documentation/api/ |
| **Mapbox** (free tier) | `https://api.mapbox.com/` | Yes (access token) | `geocoding/v5/mapbox.places/{search}.json?access_token={token}`  <br> `directions/v5/mapbox/driving/{lon1},{lat1};{lon2},{lat2}?access_token={token}` | 100 000 req / month free; burst 600 req / min [22] | “© Mapbox, © OpenStreetMap contributors” | [22] https://docs.mapbox.com/api/overview/ |
| **HERE** (Freemium) | Routing: `https://router.hereapi.com/v8/` <br> Geocode: `https://geocode.search.hereapi.com/v1/geocode` | Yes (API key) | `geocode?q={query}&apiKey={key}`  <br> `routes?transportMode=car&origin={lat1},{lon1}&destination={lat2},{lon2}&apiKey={key}` | 250 000 req / month free; 5 req / s per app [23] | “© HERE Technologies” (+ OSM where used) | [23] https://developer.here.com/documentation |
| **TomTom** (Freemium) | Geocode: `https://api.tomtom.com/search/2/` <br> Routing: `https://api.tomtom.com/routing/1/calculateRoute/` | Yes (key) | `geocode/JSON?query={query}&key={key}`  <br> `routing/1/calculateRoute/{lon1},{lat1}:{lon2},{lat2}/json?key={key}` | 2 500 req / day free; burst 5 req / s [24] | “© TomTom” (+ OSM where mixed) | [24] https://developer.tomtom.com/ |
| **Google Maps Platform** (Free credit) | `https://maps.googleapis.com/maps/api/` | Yes (API key + billing) | `geocode/json?address={query}&key={key}`  <br> `directions/json?origin={lat1},{lon1}&destination={lat2},{lon2}&key={key}` | $200 USD credit / month → ≈ 28 000 req / day (geocode); 40 req / s per project [25] | “© Google” (logo required) | [25] https://developers.google.com/maps/documentation/urls/guide |
| **TravelTime** (freemium) | `https://api.traveltime.com/v4/` (shard 1) <br> `https://api.traveltimeapp.com/v4/` (shard 2) | Yes (API key) | `time-map?json={...}` (isochrone / matrix) | ⚠️ **CONFLICT** – shard 1: 5 000 req / month free; 1 req / s [26]  <br> shard 2: 100 req / day free (≈ 3 000 / month) [27] | “© TravelTime” | [26] https://traveltime.com/docs/  <br> [27] https://docs.traveltime.com/api/v4/time-map |

\*Templates show required placeholders; replace with URL‑encoded values.

---

### 2️⃣ Feature inventory (which free APIs support which capability)

| Capability | Supporting APIs (free tier) | Notes |
|------------|-----------------------------|-------|
| **Geocoding / reverse‑geocoding** | Nominatim, Photon, OpenRouteService, GraphHopper, Mapbox, HERE, TomTom, Google, Open‑Meteo (via `timezone`), Wikidata (entity search) | OSM‑based services need attribution; commercial services need logo. |
| **Routing (car, bike, foot)** | OSRM, Valhalla, OpenRouteService, GraphHopper, Mapbox, HERE, TomTom, Google | OSRM & Valhalla are public demos – low‑volume only. |
| **Isochrones / isodistances** | OpenRouteService, GraphHopper, Valhalla, Mapbox Isochrone API, HERE Reachability, TravelTime, TomTom (paid), Google (via Distance Matrix) | TravelTime offers public‑transport isochrones. |
| **Matrix / distance‑time table** | OpenRouteService, GraphHopper, HERE, TomTom, Google, TravelTime | Matrix endpoints often require POST with JSON payload. |
| **POI / feature search** | Overpass API, Nominatim (amenity filter), Photon, Wikidata, Transitland (stops), Mapbox (POI tiles), HERE (Places) | Overpass allows arbitrary OSM tag queries. |
| **Elevation** | Open‑TopoData / Open‑Elevation | Batch up to 100 locations per request (dataset‑dependent). |
| **Weather along a route** | Open‑Meteo (query per sampled coordinate) | No dedicated “weather‑along‑route” API; client must sample geometry. |
| **Public‑transit routing** | Transitland / OpenTripPlanner, HERE Transit, Google Transit, TomTom Transit (paid), OpenRouteService (limited) | Transitland provides raw GTFS data; HERE/Google give ready‑to‑use journeys. |
| **Map tiles** | OSM raster tile server, Mapbox (vector/raster), HERE (vector), TomTom (vector), Google (raster) | Free OSM tiles limited to ≤ 2 req /s; commercial providers have higher quotas. |

---

### 3️⃣ Deep‑link templates (quick‑copy URLs for the agent)

| Action | URL template | Required parameters | Source |
|--------|--------------|---------------------|--------|
| **Geocode (OSM‑Nominatim)** | `https://nominatim.openstreetmap.org/search?format=json&q={query}&limit=1` | `query` (URL‑encoded) | [1] |
| **Reverse‑geocode (Nominatim)** | `https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}` | `lat`, `lon` | [1] |
| **Geocode (Photon)** | `https://photon.komoot.io/api?q={query}&limit=1` | `query` | [2] |
| **Route (OSRM, driving)** | `https://router.project-osrm.org/route/v1/driving/{lon1},{lat1};{lon2},{lat2}?overview=full&geometries=geojson` | `lon1,lat1,lon2,lat2` | [4] |
| **Route (Valhalla, auto)** | `https://valhalla1.openstreetmap.de/route?json={"locations":[{"lat":{lat1},"lon":{lon1}},{"lat":{lat2},"lon":{lon2}}],"costing":"auto"}` | `lat1,lon1,lat2,lon2` | [5] |
| **Route (OpenRouteService, car)** | `https://api.openrouteservice.org/v2/directions/driving-car?api_key={key}&start={lon1},{lat1}&end={lon2},{lat2}` | `key`, `lon1,lat1,lon2,lat2` | [6] |
| **Route (GraphHopper, car)** | `https://graphhopper.com/api/1/route?key={key}&point={lat1},{lon1}&point={lat2},{lon2}&vehicle=car&format=json` | `key`, `lat1,lon1,lat2,lon2` | [8] |
| **Isochrone (OpenRouteService)** | `https://api.openrouteservice.org/v2/isochrones/{profile}?api_key={key}&locations={lon},{lat}&range={seconds}` | `profile`, `key`, `lon,lat`, `seconds` | [6] |
| **Isochr
