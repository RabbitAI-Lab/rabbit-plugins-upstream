<!-- merged by groq/openai/gpt-oss-120b from 1 shard(s) on 2026-09-20 -->

**Organic Maps – Open‑source, offline‑first maps & navigation (as of Sept 2026)**  

---

## 1. Core Navigation Feature Inventory  

| Feature | Status | Notes | Source |
|---|---|---|---|
| Turn‑by‑turn navigation (walking, cycling, car) | SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Voice guidance (TTS) | SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Lane guidance | SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Speed limits | SUPPORTED | Conditional limits added Mar 2026 | [Mar 2026 update](https://organicmaps.app/news/2026-03-12/conditional-speed-limits-more-detailed-isolines-for-china-splitsmaller-tanzania-regions-leather-shops-and-more-in-the-march-organic-maps-update/) |
| Speed‑camera / hazard alerts | SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Dynamic rerouting | SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| ETA (estimated time of arrival) | SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Live traffic | NOT SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Toll / avoidance options | SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Multi‑stop routing | SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Route options (fastest, shortest, eco, …) | SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| HOV lane support | NOT SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Travel modes (walk, bike, car, transit) | SUPPORTED | Transit added Jun 2026 | [Jun 2026 update](https://organicmaps.app/news/2026-06-29/satellite-imagery-public-transport-routes-alternate-routes-new-search-and-route-planning-interface-for-android-large-accessibility-fonts/) |
| Offline maps (full offline) | SUPPORTED | 100 % offline operation | [Organic Maps homepage](https://organicmaps.app/) |
| AR / Live View | NOT SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| 3‑D maps | SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Satellite imagery | SUPPORTED (experimental) | Custom raster tile server | [Jun 2026 update](https://organicmaps.app/news/2026-06-29/satellite-imagery-public-transport-routes-alternate-routes-new-search-and-route-planning-interface-for-android-large-accessibility-fonts/) |
| Street imagery | NOT SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Indoor maps | NOT SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Incident reporting | SUPPORTED | Via OSM editing | [Map editing FAQ](https://organicmaps.app/faq/editing/organic-maps-map-editing/) |
| Parking locations & info | SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Fuel price data | NOT SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Share ETA / location | SUPPORTED | Added Aug 2026 | [Aug 2026 update](https://organicmaps.app/news/2026-08-31/multi-selection-bookmarks-tracks-carplay-dashboard-hiding-tracks-share-links-august-2026/) |
| Saved places / lists | SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Wikipedia‑sourced reviews | SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |
| Track history / timelines | SUPPORTED |  | [Organic Maps homepage](https://organicmaps.app/) |

---

## 2. Data Sources & Platform Coverage  

| Category | Details | Source |
|---|---|---|
| Map data provider | OpenStreetMap (OSM) | [Organic Maps homepage](https://organicmaps.app/) |
| Supported platforms | Android, iOS, Huawei AppGallery, F‑Droid, Accrescent, Obtainium | [News page](https://organicmaps.app/news/) |
| Pricing model | Free, no ads, no tracking | [Organic Maps homepage](https://organicmaps.app/) |
| Offline capability | Full map tiles & routing offline | [Organic Maps homepage](https://organicmaps.app/) |
| Geographic coverage | Global (as far as OSM data exist) | [Organic Maps homepage](https://organicmaps.app/) |

---

## 3. Deep‑Link / URL Scheme Reference  

| Action | URL Template | Parameters (key = value) | Notes |
|---|---|---|---|
| Search | `https://omaps.app/search?query=…`  <br> `https://organicmaps.app/?query=…` | `query` – free‑text search term | Official docs not published; pattern observed in Apr 2026 update |
| Directions (open navigation) | `omaps://directions?to=lat,lon`  <br> `https://omaps.app/directions?to=lat,lon` | `to` – destination coordinates (lat,lon) <br> `mode` – optional travel mode (`car`, `bike`, `walk`, `transit`) | ⚠️ UNVERIFIED – parameter names inferred from app behavior |
| Show place | `omaps://place?lat=…&lon=…`  <br> `https://omaps.app/place?lat=…&lon=…` | `lat`, `lon` – coordinates | ⚠️ UNVERIFIED |
| Travel mode (when combined with directions) | `…?to=lat,lon&mode=car` | `mode` – `car`, `bike`, `walk`, `transit` | ⚠️ UNVERIFIED |

*Source for observed patterns:* [Apr 2026 update](https://organicmaps.app/news/2026-04-07/hiking-cycling-routes-elevation-charts-us-address-search-antimeridian-map-wrapping-april-2026-organic-maps-update/)

---

## 4. Public APIs / SDKs  

| API / SDK | Functionality | Rate limits / quotas | Access terms | Source |
|---|---|---|---|---|
| Organic Maps “open‑app” API | Allows external apps to launch OM for search, directions, place view | Not specified | Requires OM app installed on device | [Mar 2026 update](https://organicmaps.app/news/2026-03-12/conditional-speed-limits-more-detailed-isolines-for-china-splitsmaller-tanzania-regions-leather-shops-and-more-in-the-march-organic-maps-update/) |
| Android SDK (in development) | Embedding OM map tiles & routing into third‑party Android apps | Not specified | Contact Organic Maps team | [News page](https://organicmaps.app/news/) |
| Bookmarks / Tracks export API | Export / import of user bookmarks & GPX/GeoJSON tracks | Not specified | Requires OM app installed | [Jan 2026 update](https://organicmaps.app/news/2026-01-26/faster-cross-country-and-cross-region-routes-in-january-26-organic-maps-update/) |

---

## 5. Differentiating / Unique Features  

| Feature | How it’s realized | Open data / APIs used | Notes |
|---|---|---|---|
| Full offline maps | Pre‑downloaded OSM tiles + routing graphs stored on device | OpenStreetMap | Enables 100 % offline navigation |
| Privacy‑first design | No ads, no telemetry, open‑source code | N/A | Emphasised on homepage |
| Public‑transport routing (subway, bus, tram, train) | Uses OSM + GTFS feeds; experimental as of Jun 2026 | OSM, GTFS | Feature listed in Jun 2026 news |
| Satellite imagery (experimental) | Custom raster tile server delivering satellite tiles | Any XYZ/WMS source can be swapped | Added Jun 2026 |
| Hiking & cycling routes with elevation charts | OSM ways + elevation data (e.g., Open‑Topo) | OpenStreetMap, Open‑Meteo (elevation) | Highlighted Apr 2026 |
| Antimeridian map wrapping | Correct handling of longitude ±180° | OSM geometry | Apr 2026 update |
| Conditional speed limits | Reads OSM conditional tags | OpenStreetMap | Mar 2026 update |
| Multi‑selection for bookmarks / tracks | Bulk actions inside the app | N/A | Aug 2026 update |
| CarPlay dashboard integration | Shows navigation on CarPlay | N/A | Aug 2026 update |

---

## 6. Sources  

- https://organicmaps.app/  
- https://organicmaps.app/news/  
- https://organicmaps.app/faq/  
- https://organicmaps.app/faq/editing/organic-maps-map-editing/  
- https://organicmaps.app/news/2026-03-12/conditional-speed-limits-more-detailed-isolines-for-china-splitsmaller-tanzania-regions-leather-shops-and-more-in-the-march-organic-maps-update/  
- https://organicmaps.app/news/2026-04-07/hiking-cycling-routes-elevation-charts-us-address-search-antimeridian-map-wrapping-april-2026-organic-maps-update/  
- https://organicmaps.app/news/2026-06-29/satellite-imagery-public-transport-routes-alternate-routes-new-search-and-route-planning-interface-for-android-large-accessibility-fonts/  
- https://organicmaps.app/news/2026-08-31/multi-selection-bookmarks-tracks-carplay-dashboard-hiding-tracks-share-links-august-2026/  
- https://organicmaps.app/news/2026-01-26/faster-cross-country-and-cross-region-routes-in-january-26-organic-maps-update/  
- https://omaps.app/search?query=Pizza  
- https://omaps.app/directions?to=51.5074,0.1278  
- https://omaps.app/place?lat=51.5074&lon=0.1278  
- https://omaps.app/directions?to=51.5074,0.1278&mode=car
