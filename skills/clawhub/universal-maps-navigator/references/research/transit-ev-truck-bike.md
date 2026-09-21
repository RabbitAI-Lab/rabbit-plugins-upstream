<!-- merged by groq/openai/gpt-oss-120b from 2 shard(s) on 2026-09-20 -->

**Universal maps & navigation skill – consolidated free/open data & API reference (transit | EV | truck | bike)**  

---

### 1️⃣ Public‑Transit (GTFS / GTFS‑RT)

| Feature | Endpoint / File | Params / Notes | Free‑tier / Limits | Source |
|---------|----------------|----------------|-------------------|--------|
| GTFS static feeds | `*.txt` files in a ZIP (e.g., `stops.txt`, `trips.txt`) | – | Open, no auth; any agency can host | [src](https://developers.google.com/transit/gtfs) |
| GTFS‑Realtime | `tripUpdates.pb`, `vehiclePositions.pb`, `serviceAlerts.pb` (HTTP GET) | – | Open, many agencies require API keys; many publish free feeds | [src](https://developers.google.com/transit/gtfs-realtime) |
| Mobility Database (catalogue of GTFS/GTFS‑RT) | `GET https://mobilitydatabase.org/v1/feeds` (JSON) | searchable, read‑only | Free, rate‑limited ≈ 10 req /s per IP | [src](https://mobilitydatabase.org/) |
| Mobility Database – feed count | ≈ 2 M feeds | – | – | [src](https://mobilitydatabase.org/) |
| **⚠️ CONFLICT** – Mobility Database feed count (shard 2 reports “≈ 6 000+ feeds”) | – | – | – | [src](https://mobilitydatabase.org/) |
| Transitland API v2 – feed metadata | `GET https://api.transit.land/v2/feed_versions` | – | Free API key (sign‑up), 10 k req / day | [src](https://transit.land/documentation/api/v2/) |
| Transitland API v2 – vehicle positions (realtime) | `GET https://api.transit.land/v2/vehicle_positions` | – | Free API key, 10 k req / day | [src](https://transit.land/documentation/api/v2/) |
| OpenTripPlanner public demo | `GET /otp/routers/default/plan?...` (JSON) | multimodal (transit + walk/bike) | Public demo servers (e.g., https://otp.sandbox) – rate‑limited, no SLA | [src](https://docs.opentripplanner.org/en/latest/) |
| Navitia (free tier) | `GET https://api.navitia.io/v1/journeys?...` | requires free API key | 10 k calls / month, 1 req /s | [src](https://doc.navitia.io/) |
| Navitia (self‑hosted) | Open‑source engine – ingest GTFS/GTFS‑RT | – | No hosted free tier; self‑hosted | [src](https://www.navitia.io/) |

---

### 2️⃣ EV‑aware Routing & Charging‑Station Data

| Data / Feature | Endpoint / Tag | Routing Params | Free‑tier / Limits | Source |
|----------------|----------------|----------------|-------------------|--------|
| OpenChargeMap (global EVSE catalogue) | `GET https://api.openchargemap.io/v3/poi/?output=json&countrycode=…` (requires free API key) | – (routing done by caller) | Free key, 10 req /s per IP | [src](https://openchargemap.org/develop/api) |
| OSM charging‑station tags | Overpass API query `amenity=charging_station` | `capacity`, `operator`, `socket:type2`, `voltage`, `max_power_kW` | Public Overpass endpoint – 2 req /s per IP, no auth | [src](https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcharging_station) |
| OpenRouteService EV profile | `POST https://api.openrouteservice.org/v2/directions/driving-electric` | `range`, `range_type`, `charging_strategy`, `avoid_features` | Free tier: 2 500 req / day, 40 req /min | [src](https://openrouteservice.org/dev/#/api-docs/v2/directions/{profile}/post) |
| Valhalla EV costing (self‑hosted) | `POST /route` with `"costing":"electric_vehicle"` | `battery_capacity_kWh`, `initial_charge_percent`, `charge_speed_kW` | No hosted free tier – self‑hosted | [src](https://github.com/valhalla/valhalla/blob/master/docs/api.md) |
| HERE Routing API – EV | `GET https://router.hereapi.com/v8/routes?transportMode=car&ev[range]=…` | `ev[range]`, `ev[charge]`, `ev[chargingStationIds]` | Freemium: 250 req / month | [src](https://developer.here.com/documentation/routing-api/8.13.0/dev_guide/topics/ev-routing.html) |
| Google Maps Directions – EV (beta) | `GET https://maps.googleapis.com/maps/api/directions/json?mode=driving&...&ev_charging=true` | `ev_charging` (boolean) | Free tier: $200 USD / month (≈ 40 k calls) – EV param only in beta | [src](https://developers.google.com/maps/documentation/directions/overview) |
| ORS Elevation API (separate) | `GET https://api.openrouteservice.org/elevation/line?format=geojson&points=…` | – | Same free tier as ORS routing | [src](https://openrouteservice.org/dev/#/api-docs/v2/elevation/line/get) |

---

### 3️⃣ Truck / HGV Routing

| Engine / Source | Endpoint | Routing Params (key) | Free‑tier / Limits | Source |
|-----------------|----------|----------------------|-------------------|--------|
| OpenRouteService – driving‑hgv | `POST https://api.openrouteservice.org/v2/directions/driving-hgv` | `height`, `width`, `weight`, `axleload`, `hazmat`, `length` (JSON body) | 2 500 req / day (same tier as ORS) | [src](https://openrouteservice.org/dev/#/api-docs/v2/directions/driving-hgv/post) |
| Valhalla – truck costing (self‑hosted) | `POST /route` with `"costing":"truck"` | `truck_type`, `height`, `width`, `length`, `weight`, `axle_load`, `hazmat`, `tunnel_category` | Self‑hosted (open source) | [src](https://github.com/valhalla/valhalla/blob/master/docs/costing.md#truck) |
| GraphHopper – truck profile | `GET https://graphhopper.com/api/1/route?profile=truck` | `vehicle_height`, `vehicle_width`, `vehicle_weight`, `vehicle_axle_weight`, `hazmat`, `toll_avoidance` | Free tier: 2 500 req / day, 5 req /s | [src](https://www.graphhopper.com/docs/) |
| HERE Routing – truck | `GET https://router.hereapi.com/v8/routes?transportMode=truck&truck[height]=…` | `truck[height]`, `truck[width]`, `truck[weight]`, `truck[axleWeight]`, `truck[hazmat]`, `truck[trailers]` | Freemium: 250 req / month | [src](https://developer.here.com/documentation/routing-api/8.13.0/dev_guide/topics/truck-routing.html) |

---

### 4️⃣ Bicycle / Scooter / Pedestrian Routing

| Engine | Profile(s) | Endpoint / Template | Important Params | Free‑tier / Limits | Source |
|--------|------------|---------------------|------------------|-------------------|--------|
| OSRM | `bike` / `bicycle`, `foot` | `GET https://router.project-osrm.org/route/v1/{profile}/{lon1},{lat1};{lon2},{lat2}?…` | `exclude=toll,ferry`, `alternatives`, `steps` | Public demo – 10 req /s, no auth | [src](http://project-osrm.org/docs/v5.24.0/api/#route-service) |
| OpenRouteService | `cycling-regular`, `cycling-mountain`, `cycling-electric`, `foot-hiking` | `POST https://api.openrouteservice.org/v2/directions/{profile}` | `elevation=true`, `preference=shortest|fastest`, `avoid_features` (e.g., `ferry`) | 2 500 req / day | [src](https://openrouteservice.org/dev/#/api-docs/v2/directions/{profile}/post) |
| GraphHopper | `bike`, `foot`, `scooter` | `GET https://graphhopper.com/api/1/route?profile=bike&…` | `elevation=true`, `point_hint`, `avoid` (e.g., `ferry`) | 2 500 req / day | [src](https://www.graphhopper.com/docs/) |
| Valhalla | `bicycle`, `pedestrian`, `scooter` | `POST /route` with `"costing":"bicycle"` etc. | `elevation=true`, `exclude` (e.g., `toll,ferry`) | Self‑hosted (open source) | [src](https://github.com/valhalla/valhalla/blob/master/docs/api.md#bicycle) |
| ORS Elevation API (line) | – | `GET https://api.openrouteservice.org/elevation/line?format=geojson&points=…` | – | Same free tier as ORS routing | [src](https://openrouteservice.org/dev/#/api-docs/v2/elevation/line/get) |

---

### 5️⃣ Toll & Ferry Avoidance (common across engines)

| Engine | Avoid Toll | Avoid Ferry | Parameter Example | Source |
|--------|------------|------------|-------------------|--------|
| OpenRouteService | Yes | Yes | `"avoid_features": ["ferries","tollways"]` | [src](https://giscience.github.io/openrouteservice/api-reference/endpoints/directions/routing-options) |
| Valhalla | Yes | Yes | `"avoid_toll": true` or `"toll_booth_penalty"` | [src](https://valhalla.github.io/valhalla/api/route/api-reference/) |
| GraphHopper | Yes | Yes | `"avoid": ["tolls","ferries"]` | [src](https://discuss.graphhopper.com/t/how-to-avoid-toll-roads-and-ferries-with-gh-3-0/6684) |

---

### 6️⃣ Live Traffic (free/open sources)

| Provider | Free Tier | Coverage | Docs / URL |
|----------|-----------|----------|------------|
| TomTom Traffic API | 2 500 req / day | Global | [src](https://developer.tomtom.com/intermediate-traffic-service/documentation) |
| HERE Traffic API | 25 000 req / month | Global | [src](https://developer.here.com/documentation) |
| Waze (partner feeds) | **UNVERIFIED** – only for partners | Select cities | [src](https://www.waze.com/forum) |
| OSM traffic tags | None (no live data) | – | [src](https://wiki.openstreetmap.org/wiki/Traffic_data) |

*How major consumer apps obtain traffic:* Google Maps (crowdsourced Android/iOS + partners), Apple Maps (anonymous iPhone GPS + partners), Waze (crowdsourced), TomTom/HERE (device & fleet data).

---

### 7️⃣ Summary of Engine Feature Coverage

| Engine | Transit | EV‑routing | Truck/HGV | Bicycle/Scooter | Pedestrian | Toll/Ferry Avoid | Live Traffic |
|--------|---------|------------|-----------|-----------------|------------|------------------|--------------|
| OpenRouteService | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ (needs external traffic feed) |
| Valhalla | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ (external) |
| GraphHopper | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ (external) |
| OSRM | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ |
| HERE Routing API | ✅ (via separate service) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (included in freemium) |
| Google Maps Directions | ✅ (transit) | ✅ (beta) | ✅ (truck via separate API) | ✅ | ✅ | ✅ | ✅ |

---

## Sources

- <https://developers.google.com/transit/gtfs>
- <https://developers.google.com/transit/gtfs-realtime>
- <https://mobilitydatabase.org/>
- <https://transit.land/documentation/api/v2/>
- <https://docs.opentripplanner.org/en/latest/>
- <https://doc.navitia.io/>
- <https://openchargemap.org/develop/api>
- <https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcharging_station>
- <https://openrouteservice.org/dev/#/api-docs/v2/directions/{profile}/post>
- <https://github.com/valhalla/valhalla/blob/master/docs/api.md>
- <https://router.hereapi.com/v8/routes?transportMode=car&ev[range]>
- <https://developer.here.com/documentation/routing-api/8.13.0/dev_guide/topics/ev-routing.html>
- <https://developers.google.com/maps/documentation/directions/overview>
- <https://openrouteservice.org/dev/#/api-docs/v2/directions/driving-hgv/post>
- <https://github.com/valhalla/valhalla/blob/master/docs/costing.md#truck>
- <https://www.graphhopper.com/docs/>
- <https://router.hereapi.com/v8/routes?transportMode=truck&truck[height]>
- <https://developer.here.com/documentation/routing-api/8.13.0/dev_guide/topics/truck-routing.html>
- <http://project-osrm.org/docs/v5.24.0/api/#route-service>
- <https://github.com/Project-OSRM/osrm-backend/blob/master/docs/profiles.md>
- <https://giscience.github.io/openrouteservice/api-reference/endpoints/directions/routing-options>
- <https://valhalla.github.io/valhalla/api/route/api-reference/>
- <https://discuss.graphhopper.com/t/how-to-avoid-toll-roads-and-ferries-with-gh-3-0/6684>
- <https://developer.tomtom.com/intermediate-traffic-service/documentation>
- <https://developer.here.com/documentation>
- <https://www.waze.com/forum>
- <https://wiki.openstreetmap.org/wiki/Traffic_data>
- <https://gtfs.org/resources/sharing-data/>
- <https://openchargemap.org/develop/api>
- <https://openrouteservice.org/dev/#/api-docs/v2/elevation/line/get>
