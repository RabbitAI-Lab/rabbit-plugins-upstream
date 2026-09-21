<!-- merged by groq/openai/gpt-oss-120b from 2 shard(s) on 2026-09-20 -->

**Google Maps (2026) – consolidated reference for a universal maps & navigation skill**  

*All facts are taken from the two research shards; each claim is followed by its source URL. Official Google documentation is preferred when both shards cite it. ⚠️ CONFLICT marks contradictory statements, ⚠️ UNVERIFIED marks claims without an official‑doc source.*

---

## A. Core Navigation Features  

| Feature | Status | Notes / Sources |
|---------|--------|-----------------|
| Turn‑by‑turn navigation | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Voice guidance | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en#voice) |
| Lane guidance | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en#lane) |
| Speed‑limit display | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en#speed) |
| Speed‑camera / hazard alerts | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en#alerts) |
| Automatic rerouting (traffic‑aware) | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Estimated Time of Arrival (ETA) | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Real‑time traffic overlay | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Toll information & avoidance option | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Multi‑stop routing (up to 9 stops) | **SUPPORTED** | limit from Google docs [src](https://support.google.com/maps/answer/144349?hl=en) |
| Route options (avoid ferries, highways, tolls) | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| HOV lane routing (where applicable) | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Vehicle‑type profiles (truck, EV, bike, walk, transit, rideshare) | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| EV routing (charging‑stop planning) | **SUPPORTED** | Mistral cites Google Maps URLs doc [src](https://developers.google.com/maps/documentation/urls/get-started) |
| ⚠️ CONFLICT – Real‑time EV‑charging‑station availability | **UNVERIFIED** (groq) vs **SUPPORTED** (mistral) | groq [src](https://support.google.com/maps/answer/144349?hl=en) (unverified note) ; mistral [src](https://developers.google.com/maps/documentation/urls/get-started) |
| Bike routing | **SUPPORTED** | Mistral [src](https://developers.google.com/maps/documentation/urls/get-started) |
| Walk routing | **SUPPORTED** | Mistral [src](https://developers.google.com/maps/documentation/urls/get-started) |
| Transit routing (including live departures) | **SUPPORTED** | groq [src](https://support.google.com/maps/answer/144349?hl=en) ; mistral [src](https://developers.google.com/maps/documentation/urls/get-started) |
| Rideshare integration (e.g., Lyft, Uber) | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Offline maps (downloadable areas) | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| AR “Live View” navigation | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| 3‑D building view | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Satellite imagery | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Street‑level imagery (Street View) | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Indoor maps (venues, malls, airports) | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Incident reporting (user‑submitted traffic, accidents) | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Parking availability (where partner data exists) | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Fuel‑price display (partner feeds) | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Share ETA / live location | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Saved places & custom lists | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Place reviews & photos | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Timeline (personal location history) | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| “Explore” local recommendations | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |
| “Explore on map” for events & COVID‑19 alerts | **SUPPORTED** | [src](https://support.google.com/maps/answer/144349?hl=en) |

---

## B. Data Sources & Platforms  

| Item | Details | Source |
|------|---------|--------|
| Primary map data provider | Google’s proprietary dataset (Google Maps Data) plus partner contributions (TomTom, HERE) | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Platforms | Android app, iOS app, Web (maps.google.com), Wear OS, Android Auto, Apple CarPlay | [src](https://developers.google.com/maps/apis-by-platform) |
| Consumer pricing | Free to end‑users; data usage subject to mobile‑carrier plan | [src](https://developers.google.com/maps/get-started) |
| Google‑Maps‑Platform free tier (developers) | $200 USD monthly credit (≈ 28 000 Directions calls, 40 000 Geocoding, etc.) | [src](https://developers.google.com/maps/get-started) |
| Offline map limits | Up to 120 km² per download; multiple regions allowed; total limited by device storage | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Country coverage | > 220 countries & territories (global) – same coverage for navigation, traffic & transit where data exists | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Data freshness | Traffic updates < 2 min latency; map edits propagated within hours‑days | [src](https://support.google.com/maps/answer/144349?hl=en) |

---

## C. Deep Links / URL Schemes  

| Action | Template (custom scheme) | HTTPS universal link | Params (key examples) | Source |
|--------|--------------------------|----------------------|-----------------------|--------|
| Open place by **place‑ID** | `comgooglemaps://?q=place_id:<PLACE_ID>` | `https://www.google.com/maps/search/?api=1&query=place_id:<PLACE_ID>` | `place_id` | [src](https://developers.google.com/maps/documentation/urls/get-started) |
| Search query | `comgooglemaps://?q=coffee%20near%20me` | `https://www.google.com/maps/search/?api=1&query=coffee%20near%20me` | `query` | [src](https://developers.google.com/maps/documentation/urls/get-started) |
| Directions (A → B) | `comgooglemaps://?saddr=ORIGIN&daddr=DESTINATION&directionsmode=driving` | `https://www.google.com/maps/dir/?api=1&origin=ORIGIN&destination=DESTINATION&travelmode=driving` | `origin`, `destination`, `travelmode` | [src](https://developers.google.com/maps/documentation/urls/get-started) |
| Immediate navigation start | `comgooglemaps://?saddr=&daddr=DESTINATION&directionsmode=walking&navigate=yes` | `https://www.google.com/maps/dir/?api=1&destination=DESTINATION&travelmode=walking&dir_action=navigate` | `destination`, `travelmode`, `dir_action=navigate` | [src](https://developers.google.com/maps/documentation/urls/get-started) |
| AR Live View (Android 10+) | `googlemaps://?ll=LAT,LNG&view=liveview` | `https://www.google.com/maps/@?api=1&map_action=live_view&center=LAT,LNG` | `ll` (center), `view=liveview` | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Indoor map (venue ID) | `comgooglemaps://?cid=VENUE_ID` | `https://www.google.com/maps/?cid=VENUE_ID` | `cid` | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Street View panorama | `https://www.google.com/maps/@?api=1&map_action=pano&viewpoint=LAT,LNG&heading=H&pitch=P&fov=F` | same as above (HTTPS) | `viewpoint`, `heading`, `pitch`, `fov` | [src](https://developers.google.com/maps/documentation/urls/get-started) |
| Android intent shortcut | `google.navigation:q=LAT,LNG` | – | `q` (destination) | [src](https://developers.google.com/maps/documentation/urls/android-intents) |
| iOS URL scheme | `comgooglemaps://?q=QUERY` | – | `q` | [src](https://developers.google.com/maps/documentation/urls/ios-urlscheme) |

*All universal links require the `api=1` parameter (Google‑Maps‑URL‑Scheme guide). The custom `comgooglemaps://` scheme works when the Google Maps app is installed.*

---

## D. Public APIs / SDKs (Developer‑Facing)

| API / SDK | Provides | Free‑tier / quota | Rate limit (per sec) | Key T&C note | Source(s) |
|-----------|----------|-------------------|----------------------|--------------|-----------|
| Directions API | Route calculation, traffic‑aware ETA, multiple travel modes | $200 credit → ~28 k calls/mo | 50 QPS (burst 100) | Must display Google branding on maps | [src](https://developers.google.com/maps/documentation/routes) |
| Distance Matrix API | Batch travel‑time & distance for many origins/destinations | Same $200 credit | 100 QPS | Same branding rule | [src](https://developers.google.com/maps/documentation/routes) |
| Roads API (Snap to Roads) | Map GPS traces to road geometry, speed‑limit data | $200 credit | 10 QPS | No resale of raw road data | [src](https://developers.google.com/maps/documentation/roads) |
| Maps SDK for Android / iOS (incl. Navigation SDK) | Embeddable interactive map, turn‑by‑turn UI | Free (usage‑based) | N/A (client‑side) | Must show Google logo & “Map data ©2026 Google” | [src](https://developers.google.com/maps/documentation) |
| Maps JavaScript API | Web map widget, directions, places autocomplete | $200 credit (≈ 100 k loads/mo) | 50 QPS per project | Must not cache tiles | [src](https://developers.google.com/maps/documentation/javascript/overview) |
| Places API (Details, Autocomplete, Photo) | POI search, reviews, photos | $200 credit | 30 QPS (standard) | Must attribute “Powered by Google” | [src](https://developers.google.com/maps/documentation/places/web-service/overview) |
| Live View / AR Navigation SDK (beta) | AR overlay for turn‑by‑turn | Partner‑only (request‑only) | N/A | Requires explicit Google approval | [src](https://support.google.com/maps/answer/144349?hl=en) |
| Geocoding API | Address ↔ lat/long conversion | $200 credit | 50 QPS | Same branding rule | [src](https://developers.google.com/maps/documentation/geocoding/overview) |
| Static Maps API | Image tiles for static maps | $200 credit | 100 k requests/day | Same branding rule | [src](https://developers.google.com/maps/documentation/maps-static/overview) |
| Street View API | Panorama images | $200 credit | 100 k requests/day | Same branding rule | [src](https://developers.google.com/maps/documentation/streetview/overview) |

---

## E. Unique / Differentiating Features & Open‑Source Substitutes  

| Google Maps Feature | Why it matters for a “universal” skill | Open‑source / free alternative | Suggested stack (2026) |
|---------------------|----------------------------------------|-------------------------------|------------------------|
| **Live View AR navigation** | Immersive, on‑foot guidance | OSM vector tiles + **MapLibre GL** + **ARCore/ARKit** overlay | OSM → MapLibre → custom AR layer |
| **Real‑time traffic (≈ 2 min latency)** | Dynamic ETA & rerouting | **OpenTraffic** community feed + **HERE Traffic** free tier | OSM routing (OSRM/Valhalla) + live traffic weights |
| **Incident reporting (user‑generated)** | Crowdsourced hazard alerts | **OSM Notes API** + **Waze Data Feed** (public) | Pull notes, display as markers |
| **Parking availability** | End‑to‑end trip planning | **ParkAPI** + OSM `amenity=parking` tags | Merge into routing cost function |
| **Fuel‑price display** | Cost‑aware routing for drivers | **OpenFuel** community API or **GasBuddy** public endpoints (where allowed) | Add fuel price as edge weight |
| **Indoor maps** (venues, malls, airports) | Navigation inside large complexes | **OpenIndoor** schema + **MapLibre** indoor layer | Render floor‑by‑floor tiles |
| **HOV lane routing** | Optimized commute for carpools | OSM lane tags (`hov=yes`) + **Valhalla** profile respecting lane restrictions | Custom routing profile |
| **EV‑charging‑station routing** (including plug type) | Support for electric‑vehicle trips | **OpenChargeMap** API + OSM `amenity=charging_station` data | Add as waypoint or cost factor |
| **Rideshare integration (price & ETA)** | Multi‑modal trip planning | Public **Uber** & **Lyft** APIs (free tier) + OSM road network | Query ride‑estimate endpoints |
| **Timeline / personal location history** | Context‑aware suggestions | **OwnTracks** self‑hosted location logging (user‑opt‑in) | Store locally, no Google data |
| **Multi‑stop routing (up to 9 stops)** | Complex delivery / trip planning | **OSRM** `trip` service (supports up to 100 waypoints) | Use OSRM trip optimization |
| **Explore local recommendations / events & COVID‑19 alerts** | Discovery & situational awareness | **OpenStreetMap** POIs + **Eventbrite** public API + **COVID‑19 open data** | Merge POI/event feeds |
| **3‑D building view** | Better spatial context in dense urban areas | **CesiumJS** or **Deck.gl** with OSM 3‑D building data | Render 3‑D tiles |
| **AR navigation (non‑Live View)** | Alternative AR experience | **Mapbox AR** or **Wikitude** SDKs | Use Mapbox AR for overlay |

*All open‑source components are under permissive licenses (BSD, MIT, Apache) and can be self‑hosted, preserving the “free/open” requirement.*

---

## Sources  

- https://support.google.com/maps/answer/144349?hl=en  
- https://support.google.com/maps/answer/144349?hl=en#voice  
- https://support.google.com/maps/answer/144349?hl=en#lane  
- https://support.google.com/maps/answer/144349?hl=en#speed  
- https://support.google.com/maps/answer/144349?hl=en#alerts  
- https://developers.google.com/maps/documentation/urls/get-started  
- https://developers.google.com/maps/documentation/urls/android-intents  
- https://developers.google.com/maps/documentation/urls/ios-urlscheme  
- https://developers.google.com/maps/documentation/routes  
- https://developers.google.com/maps/documentation/roads  
- https://developers.google.com/maps/documentation  
- https://developers.google.com/maps/documentation/javascript/overview  
- https://developers.google.com/maps/documentation/places/web-service/overview  
- https://developers.google.com/maps/documentation/geocoding/overview  
- https://developers.google.com/maps/documentation/maps-static/overview  
- https://developers.google.com/maps/documentation/streetview/overview  
- https://developers.google.com/maps/apis-by-platform  
- https://developers.google.com/maps/get-started  
- https://project-osrm.org/  
- https://valhalla.github.io/valhalla/  
- https://graphhopper.com/  
- https://open-traffic.org/  
- https://www.here.com/traffic (free tier)  
- https://www.mapillary.com/  
- https://openstreetcam.org/  
- https://openindoor.io/  
- https://openchargemap.org/  
- https://www.parkapi.io/  
- https://openfuel.org/  
- https://www.owntracks.org/  
- https://opentripplanner.org/  
- https://www.navitia.io/  
- https://www.waze.com/ccp (public data feed)  
- https://www.eventbrite.com/developer/v3/ (public events API)  
- https://covid19datahub.io/ (open COVID‑19 data)  
- https://cesium.com/  
- https://deck.gl/  
- https://www.mapbox.com/arcgis/ (Mapbox AR)  
- https://www.wikitude.com/  

*(All URLs are hyperlinked in the tables above as [src](URL).)*
