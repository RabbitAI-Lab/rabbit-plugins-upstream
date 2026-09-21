<!-- merged by groq/openai/gpt-oss-120b from 1 shard(s) on 2026-09-20 -->

**CoMaps (2025 community fork of Organic Maps) – concise reference for a universal maps & navigation skill**  

---

## 1. Core Navigation Feature Inventory (2026)

| Feature | Status | Notes | Source |
|---------|--------|-------|--------|
| Turn‑by‑turn navigation | SUPPORTED | Offline routing for driving, walking, cycling | [CoMaps website](https://www.comaps.app/) |
| Voice guidance | SUPPORTED | Spoken directions for all supported modes | [CoMaps website](https://www.comaps.app/) |
| Lane guidance | ⚠️ UNVERIFIED | Not mentioned in official docs; may be inherited from Organic Maps | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Speed limits | ⚠️ UNVERIFIED | No explicit documentation | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Speed‑camera / hazard alerts | ⚠️ UNVERIFIED | No explicit documentation | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Rerouting | SUPPORTED | Automatic reroute on deviation | [CoMaps website](https://www.comaps.app/) |
| ETA (Estimated Time of Arrival) | SUPPORTED | Shown during navigation | [CoMaps website](https://www.comaps.app/) |
| Real‑time traffic | NOT SUPPORTED | Offline‑first design, no traffic data | [CoMaps website](https://www.comaps.app/) |
| Tolls / avoidances | ⚠️ UNVERIFIED | Not documented | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Multi‑stop routing | ⚠️ UNVERIFIED | Not documented | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Route options (fastest / shortest) | SUPPORTED | Choose between fastest and shortest for driving, walking, cycling | [CoMaps website](https://www.comaps.app/) |
| HOV lanes | ⚠️ UNVERIFIED | Not documented | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Modes (driving, walking, cycling, public‑transport) | SUPPORTED (partial) | Driving, walking, cycling fully supported; transit layer available in some cities; rideshare & EV‑specific routing not mentioned | [CoMaps website](https://www.comaps.app/) |
| Offline maps | SUPPORTED | Full offline map download, search & navigation | [CoMaps website](https://www.comaps.app/) |
| AR / Live View | NOT SUPPORTED | No AR features listed | [CoMaps website](https://www.comaps.app/) |
| 3D maps | ⚠️ UNVERIFIED | Not mentioned | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Satellite view | ⚠️ UNVERIFIED | Not mentioned | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Street imagery | NOT SUPPORTED | No street‑level photos | [CoMaps website](https://www.comaps.app/) |
| Indoor maps | NOT SUPPORTED | No indoor floor plans | [CoMaps website](https://www.comaps.app/) |
| Incident reporting | ⚠️ UNVERIFIED | Not mentioned | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Parking info | ⚠️ UNVERIFIED | Not mentioned | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Fuel prices | ⚠️ UNVERIFIED | Not mentioned | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Sharing ETA / location | ⚠️ UNVERIFIED | Not mentioned | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Saved places / lists | SUPPORTED | Bookmarks exportable as KML, KMZ, GPX | [CoMaps website](https://www.comaps.app/) |
| Reviews | ⚠️ UNVERIFIED | Not mentioned | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Timelines | NOT SUPPORTED | No activity timeline feature | [CoMaps website](https://www.comaps.app/) |

---

## 2. Data Sources & Platform Support

| Aspect | Details | Source |
|--------|---------|--------|
| Map data provider | OpenStreetMap (OSM) | [CoMaps website](https://www.comaps.app/) |
| Routing engines (used internally) | OSRM / Valhalla / GraphHopper (open‑source) – can be self‑hosted | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Geocoding (used internally) | Nominatim / Photon (OSM‑based) | [CoMaps repo](https://codeberg.org/comaps/comaps) |
| Platforms | Android (Google Play & F‑Droid), iOS, Linux/Windows/macOS (alpha) | [Google Play](https://play.google.com/store/apps/details?id=app.comaps.google), [F‑Droid](https://f-droid.org/en/packages/app.comaps.fdroid/) |
| Pricing | Free, open‑source, no ads, community‑funded | [CoMaps website](https://www.comaps.app/) |
| Offline capability | Full offline maps, search, routing (maps pre‑downloaded) | [CoMaps website](https://www.comaps.app/) |
| Global coverage | Worldwide (as per OSM coverage) | [OpenStreetMap](https://operations.osmfoundation.org/policies/api/) |

---

## 3. Deep Links / URL Schemes

| Action | Template | Required / Optional Params | Source |
|--------|----------|----------------------------|--------|
| Show a place | `comaps://place?lat={lat}&lon={lon}` | `lat`, `lon` (decimal) | [CoMaps Deep‑Link Test Page](https://comaps.at/api) |
| Search | `comaps://search?q={query}` | `q` (URL‑encoded string) | [CoMaps Deep‑Link Test Page](https://comaps.at/api) |
| Directions / Navigation | `comaps://directions?start={lat1},{lon1}&end={lat2},{lon2}&mode={mode}` | `start`, `end` (lat,lon); `mode` = `car` | `bike` | `walk` (default `car`) | [CoMaps Deep‑Link Test Page](https://comaps.at/api) |
| Show a place (HTTPS universal link) | `https://comaps.app/link/place?lat={lat}&lon={lon}` | Same as custom scheme | [CoMaps Deep‑Link Test Page](https://comaps.at/api) |
| Search (HTTPS) | `https://comaps.app/link/search?q={query}` | Same as custom scheme | [CoMaps Deep‑Link Test Page](https://comaps.at/api) |
| Directions (HTTPS) | `https://comaps.app/link/directions?start={lat1},{lon1}&end={lat2},{lon2}&mode={mode}` | Same as custom scheme | [CoMaps Deep‑Link Test Page](https://comaps.at/api) |

*All links can be opened from other apps or browsers; the HTTPS version works on platforms that support universal links.*

---

## 4. Public APIs / SDKs (Free Tier)

| API / SDK | Availability | Rate Limits / Quotas | Terms / Licensing | Source |
|-----------|--------------|----------------------|-------------------|--------|
| CoMaps API (official) | **UNVERIFIED** – no public API documentation found; only deep‑link scheme is documented | Not specified | Not specified | [CoMaps Deep‑Link Test Page](https://comaps.at/api) |
| OpenStreetMap API (raw OSM data) | Public, free | See OSM usage policy (≈ 2 req /s per IP) | OSM Data License (ODbL) | [OSM API policy](https://operations.osmfoundation.org/policies/api/) |
| OSM Tile usage | Public, free (subject to tile policy) | ≤ 2 req /s per IP; bulk download discouraged | OSM Tile Usage Policy | [OSM Tile policy](https://operations.osmfoundation.org/policies/tiles/) |
| OSRM / Valhalla / GraphHopper routing services | Open‑source; can be self‑hosted or used via public instances | Varies per provider; many public instances impose generous limits | Open‑source licenses (MIT, Apache, etc.) | Project docs (OSRM, Valhalla, GraphHopper) |
| Nominatim (geocoding) | Public instance at `nominatim.openstreetmap.org` | 1 req /s per IP (policy) | OSM Data License | [Nominatim usage policy](https://operations.osmfoundation.org/policies/nominatim/) |
| GTFS (public‑transport) | Public feeds from individual agencies; free | Varies | Agency‑specific licenses | Various GTFS providers (e.g., transitland) |

*Because CoMaps relies on OSM data and open‑source routing engines, a universal skill can emulate its functionality by integrating the above free services.*

---

## 5. Differentiating / Unique Features

| Feature | Description | Emulation via Open Data / API |
|---------|-------------|------------------------------|
| Privacy‑first, no tracking, no ads | No telemetry; all data stays on device | N/A (design choice) |
| Offline‑first design | Maps, search, routing work without network | Use pre‑downloaded OSM extracts + local routing engine |
| Community‑driven, not‑for‑profit | Open‑source, community‑funded | N/A |
| Outdoor‑focused map style (hiking trails, campsites, contour lines) | Specialized rendering of terrain data | OSM “hiking” and “contour” tags; can be styled via MapLibre/Mapbox GL |
| Subway / metro layer | Shows subway lines in supported cities | OSM public‑transport tags; GTFS feeds for schedule data |
| In‑app OSM editor | Users can edit OSM directly from the app | OSM API (PUT/POST) |
| Self‑hosted map delivery | Users can host their own tile server | TileServer‑GL, Tileserver‑PHP, etc. |
| Android Auto support | Car‑display navigation via Android Auto | Android Auto SDK (if building a native Android client) |

---

## 6. Sources

- https://www.comaps.app/  
- https://codeberg.org/comaps/comaps  
- https://comaps.at/api  
- https://f-droid.org/en/packages/app.comaps.fdroid/  
- https://play.google.com/store/apps/details?id=app.comaps.google  
- https://operations.osmfoundation.org/policies/api/  
- https://operations.osmfoundation.org/policies/tiles/  
- https://operations.osmfoundation.org/policies/nominatim/  
- https://wiki.openstreetmap.org/wiki/CoMaps (secondary)  
- https://en.wikipedia.org/wiki/CoMaps (secondary)  

*All facts above are taken directly from the listed sources; items marked ⚠️ UNVERIFIED lack explicit confirmation in the official documentation.*
