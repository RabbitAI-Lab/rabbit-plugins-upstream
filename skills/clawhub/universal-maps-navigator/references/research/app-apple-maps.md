<!-- merged by groq/openai/gpt-oss-120b from 2 shard(s) on 2026-09-20 -->

**Apple Maps (2026) – capabilities, deep‑link formats, and public APIs for a universal maps & navigation skill**  

---

### A. Core Navigation Feature Inventory  

| Feature | Status | Notes | Source |
|---|---|---|---|
| Turn‑by‑turn navigation | SUPPORTED | Driving, walking, transit, cycling modes | [src](https://support.apple.com/en-us/HT207025) |
| Voice guidance (Siri‑driven) | SUPPORTED | Integrated with turn‑by‑turn | [src](https://support.apple.com/en-us/HT207025) |
| Lane guidance | SUPPORTED (iOS 15+) | Shows lane recommendations during navigation | [src](https://support.apple.com/en-us/HT212045) |
| Speed‑limit display | SUPPORTED (iOS 15) | Shown on highways & major roads where available | [src](https://support.apple.com/en-us/HT212045) |
| Speed‑camera / hazard alerts | SUPPORTED (iOS 16) | Alerts for speed cameras & road hazards | [src](https://www.apple.com/newsroom/2022/06/apple-maps-adds-speed-camera-alerts/) |
| Real‑time traffic & congestion | SUPPORTED | Aggregated from multiple sources | [src](https://support.apple.com/en-us/HT207025) |
| Automatic / dynamic rerouting | SUPPORTED | Re‑routes around traffic & incidents | [src](https://support.apple.com/en-us/HT207025) |
| Estimated Time of Arrival (ETA) | SUPPORTED | Continuously updated | [src](https://support.apple.com/en-us/HT207025) |
| Toll road info & avoidance | SUPPORTED | “Avoid Tolls” option in route settings | [src](https://support.apple.com/en-us/HT212045) |
| Multi‑stop routing (up to 10 stops) | ⚠️ **CONFLICT** – Shard 1: **SUPPORTED** (iOS 16) ; Shard 2: **UNVERIFIED** (no official doc) | Shard 1 cites up to 10 waypoints; Shard 2 finds no confirmation | [src 1](https://support.apple.com/en-us/HT212045) |
| Route options (fastest, avoid highways, avoid ferries) | SUPPORTED | User‑selectable preferences | [src](https://support.apple.com/en-us/HT212045) |
| HOV lane information | ⚠️ **CONFLICT** – Shard 1: **SUPPORTED** (select US metros) ; Shard 2: **UNVERIFIED** | — | [src 1](https://support.apple.com/en-us/HT212045) |
| Truck‑specific routing | ⚠️ **CONFLICT** – Shard 1: **NOT SUPPORTED** ; Shard 2: **UNVERIFIED** (no doc) | No dedicated truck profile in MapKit | — |
| EV‑charging station search & routing | ⚠️ **CONFLICT** – Shard 1: **SUPPORTED** (iOS 16) ; Shard 2: **UNVERIFIED** | Shard 1 references 2022 newsroom release | [src 1](https://www.apple.com/newsroom/2022/06/apple-maps-adds-ev-charging-station-search/) |
| Bike routing | SUPPORTED (iOS 16) | Includes elevation & trail data in select regions | [src](https://support.apple.com/en-us/HT212045) |
| Walk routing | SUPPORTED | Global coverage | [src](https://support.apple.com/en-us/HT207025) |
| Public‑transit routing | SUPPORTED (iOS 13+) | Schedules & real‑time updates where available | [src](https://support.apple.com/en-us/HT207025) |
| Rideshare integration (Uber, Lyft) | ⚠️ **CONFLICT** – Shard 1: **SUPPORTED** (in‑app booking) ; Shard 2: **UNVERIFIED** | — | [src 1](https://support.apple.com/en-us/HT212045) |
| Offline maps (downloadable) | ⚠️ **CONFLICT** – Shard 1: **NOT SUPPORTED** (only temporary caching) ; Shard 2: **SUPPORTED** (downloadable in select regions) | Apple introduced limited offline download in 2024 for certain areas | — |
| AR “Live View” walking directions | SUPPORTED (iOS 16) | Augmented‑reality overlay for pedestrian navigation | [src](https://www.apple.com/newsroom/2022/06/apple-maps-brings-ar-walking-directions-to-more-cities/) |
| 3‑D building rendering | SUPPORTED | 3‑D models in supported cities | [src](https://support.apple.com/en-us/HT207025) |
| Satellite imagery | SUPPORTED | Global coverage | [src](https://support.apple.com/en-us/HT207025) |
| “Look Around” street‑level imagery | SUPPORTED (select cities) | High‑resolution street view | [src](https://support.apple.com/en-us/HT212045) |
| Indoor maps (airports, malls, IMDF) | SUPPORTED (select venues) | Uses Apple’s Indoor Mapping Data Format | [src](https://support.apple.com/en-us/HT212045) |
| Incident / road‑hazard reporting by users | ⚠️ **CONFLICT** – Shard 1: **UNVERIFIED** (report UI exists, no public feed) ; Shard 2: **SUPPORTED** (users can report issues) | — | — |
| Parking availability info | SUPPORTED (select US cities) | Shows availability; some regions include price | [src](https://support.apple.com/en-us/HT212045) |
| Fuel‑price display at gas stations | ⚠️ **CONFLICT** – Shard 1: **UNVERIFIED** ; Shard 2: **SUPPORTED** (prices shown where data exists) | — | — |
| Share ETA / location (Messages, Mail, etc.) | SUPPORTED | One‑tap sharing | [src](https://support.apple.com/en-us/HT207025) |
| Saved places / “Favorites” & Collections | SUPPORTED | User‑created lists | [src](https://support.apple.com/en-us/HT212045) |
| Business reviews & ratings | SUPPORTED (Apple‑sourced) | — | [src](https://support.apple.com/en-us/HT212045) |
| Timeline / travel‑history view | ⚠️ **CONFLICT** – Shard 1: **UNVERIFIED** (private “Significant Locations”) ; Shard 2: **SUPPORTED** (encrypted visited‑places view) | — | — |
| Voice‑controlled routing via Siri | SUPPORTED | “Hey Siri, give me directions to …” | [src](https://support.apple.com/en-us/HT207025) |

---

### B. Data Sources & Platform Coverage  

| Item | Details | Source |
|---|---|---|
| Primary map data providers | Apple‑built data, supplemented by TomTom, OpenStreetMap, and numerous third‑party partners (e.g., Getchee, Hexagon AB, IGN, etc.) | [src](https://www.apple.com/maps/) |
| Supported platforms | iOS, iPadOS, macOS, watchOS, visionOS, CarPlay (Apple Maps app), and Apple Maps on the web | [src](https://developer.apple.com/documentation/mapkit) |
| Consumer pricing | Free for end‑users | [src](https://support.apple.com/en-us/HT207025) |
| Global coverage | >200 countries & territories (Apple claims “world‑wide coverage”) | [src](https://support.apple.com/en-us/HT207025) |
| Offline support | See conflict entry in Section A | — |

---

### C. Deep Links & URL Schemes  

| Action | Custom‑scheme (`maps://` or `http://maps.apple.com/`) | Universal HTTPS (`https://maps.apple.com/`) | Parameters (exact names) | Source |
|---|---|---|---|---|
| Show a place / free‑text search | `maps://?q=PLACE` | `https://maps.apple.com/?q=PLACE` | `q` = query string | [src](https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/MapLinks/MapLinks.html) |
| Show coordinates | `maps://?ll=LAT,LON` | `https://maps.apple.com/?ll=LAT,LON` | `ll` = latitude,longitude | same |
| Directions (driving) | `maps://?daddr=LAT,LON&saddr=LAT,LON&dirflg=d` | `https://maps.apple.com/?daddr=LAT,LON&saddr=LAT,LON&dirflg=d` | `daddr` destination, `saddr` source, `dirflg` = `d` (driving) | same |
| Directions (walking) | `maps://?daddr=LAT,LON&dirflg=w` | `https://maps.apple.com/?daddr=LAT,LON&dirflg=w` | `dirflg` = `w` (walking) | same |
| Directions (transit) | `maps://?daddr=LAT,LON&dirflg=r` | `https://maps.apple.com/?daddr=LAT,LON&dirflg=r` | `dirflg` = `r` (transit) | same |
| Directions (bicycling) | `maps://?daddr=LAT,LON&dirflg=b` | `https://maps.apple.com/?daddr=LAT,LON&dirflg=b` | `dirflg` = `b` (bicycling) | same |
| Directions with multiple stops | `maps://?daddr=STOP1,STOP2,STOP3&dirflg=d` | `https://maps.apple.com/?daddr=STOP1,STOP2,STOP3&dirflg=d` | `daddr` = comma‑separated list of waypoints | same |
| Avoid highways (example) | `maps://?daddr=DEST&dirflg=d&avoid=highways` | `https://maps.apple.com/?daddr=DEST&dirflg=d&avoid=highways` | `avoid` = `highways` (optional) | same |
| Map type selection | `maps://?t=TYPE` | `https://maps.apple.com/?t=TYPE` | `t` = `k` (standard), `h` (hybrid), `s` (satellite), `r` (Look Around where available) | same |
| Show specific POI by Apple ID | `maps://?id=POI_ID` | `https://maps.apple.com/?id=POI_ID` | `id` = Apple Maps place identifier | same |

*All parameter values must be URL‑encoded; parameter names are case‑sensitive.*

---

### D. Public APIs / SDKs  

| API / SDK | Capabilities | Free tier / limits | Key terms / restrictions | Source |
|---|---|---|---|---|
| **MapKit (iOS / macOS)** | Embed Apple Maps, perform routing, search, geocoding, annotations, display 3‑D & Look Around (read‑only) | Unlimited for apps on Apple platforms (subject to App Store Review) | Must obey Apple Developer Program License Agreement | [src](https://developer.apple.com/documentation/mapkit) |
| **MapKit JS** | Interactive web maps, geocoding, directions, search, basic Look Around (limited coverage) | 250 k map loads / month free; paid tiers thereafter | Requires Apple Developer account; must respect Apple Maps Service Terms | [src](https://developer.apple.com/documentation/mapkitjs) |
| **Apple Maps Server API** | REST endpoints for geocoding, search, ETA, routing (no public “Look Around” endpoint) | Free for all developers (rate limits not publicly disclosed) | Use must follow Apple Maps Service Terms; no redistribution of raw map data | [src](https://developer.apple.com/documentation/applemapsserverapi) |
| **SiriKit “Ride Booking”** | Launch Uber/Lyft booking from Maps via Siri | Free (partner‑specific agreements) | Follow SiriKit guidelines; rideshare partners must be authorized | [src](https://developer.apple.com/documentation/sirikit) |
| **Look Around (Web)** | Read‑only street‑level imagery via MapKit JS (no public API for bulk download) | No public API – only via MapKit JS rendering | Not available for third‑party commercial redistribution | [src](https://developer.apple.com/documentation/mapkitjs) |
| **Apple Maps “Search” (REST)** | ⚠️ **UNVERIFIED** – No official public REST endpoint documented | — | — | — |

---

### E. Differentiating Features & Open‑Source Emulation  

| Apple Maps feature | Why it matters for a universal skill | Open‑source / free data or APIs that could emulate it |
|---|---|---|
| AR Live View walking directions | Immersive, step‑by‑step guidance in the physical world | **OpenStreetMap** + **MapLibre GL** for map rendering + **ARCore/ARKit** (open wrappers) |
| Look Around street‑level imagery | Photo‑realistic context for navigation | **Mapillary**, **KartaView**, **OpenStreetCam** (CC‑BY imagery) |
| HOV lane & toll‑avoidance data | Enables compliance with local traffic rules & cost‑saving routing | OSM tags (`hov:lane`, `toll`) + **OpenTraffic** live feeds |
| EV‑charging station search & routing | Supports electric‑vehicle drivers | **OpenChargeMap**, **PlugShare** public APIs; OSM `amenity=charging_station` |
| Flyover / 3‑D city tours | High‑quality 3‑D visual experience | **CesiumJS** + OSM 3‑D building data (OSM‑Buildings) |
| Indoor maps (IMDF) | Navigation inside airports, malls, large venues | **OpenIndoor**, **OSM indoor** tags, custom IMDF conversion |
| Curated local guides & recommendations | Enhances discovery beyond pure navigation | **Wikidata**, **OpenStreetMap** POI tags, community‑curated lists |
| Parking availability & pricing | Reduces search time for drivers | **Parkopedia** public feeds, OSM `amenity=parking` + price tags |
| Fuel‑price display | Helps drivers choose cheaper stations | **FuelAPI**, community‑maintained price feeds |
| Timeline / visited‑places (privacy‑focused) | Personal travel history without cloud exposure | Local encrypted storage; no public API needed |
| Multi‑stop routing (up to 10) | Complex trip planning | MapKit routing (official) or **OpenRouteService** (free tier) supporting up to 50 waypoints |
| Rideshare in‑app booking | Seamless transition from navigation to ride request | Deep‑link to Uber/Lyft SDKs; no Apple‑only API needed |

---

## Sources  

- Apple Support – Turn‑by‑turn & navigation basics: https://support.apple.com/en-us/HT207025  
- Apple Support – Advanced navigation options (lanes, speed limits, tolls, etc.): https://support.apple.com/en-us/HT212045  
- Apple Newsroom – Speed‑camera alerts (2022): https://www.apple.com/newsroom/2022/06/apple-maps-adds-speed-camera-alerts/  
- Apple Newsroom – EV‑charging station search (2022): https://www.apple.com/newsroom/2022/06/apple-maps-adds-ev-charging-station-search/  
- Apple Newsroom – AR Live View (2022): https://www.apple.com/newsroom/2022/06/apple-maps-brings-ar-walking-directions-to-more-cities/  
- Apple Maps homepage (data sources): https://www.apple.com/maps/  
- MapKit documentation (iOS/macOS SDK): https://developer.apple.com/documentation/mapkit  
- MapKit JS documentation: https://developer.apple.com/documentation/mapkitjs  
- Apple Maps URL Scheme reference: https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/MapLinks/MapLinks.html  
- SiriKit Ride Booking guide: https://developer.apple.com/documentation/sirikit  
- Apple Maps Server API documentation: https://developer.apple.com/documentation/applemapsserverapi  
- Apple Newsroom – 2026 feature announcement: https://www.apple.com/newsroom/2026/06/apple-unveils-innovative-features-and-intelligence-experiences-across-services/  
- Apple Newsroom – 2024 web launch: https://www.apple.com/newsroom/2024/07/apple-maps-on-the-web-launches-in-beta/  
- Apple Support – Location & map view guide (iOS): https://support.apple.com/guide/iphone/set-your-location-and-map-view-iph10d7bdf26/ios  
- Apple App Store description (general feature list): https://apps.apple.com/hu/app/apple-t%C3%A9rk%C3%A9pek/id915056765  
- Apple Maps developer resources page: https://developer.apple.com/maps/resources/  
- Apple Maps legal & privacy pages: https://www.apple.com/legal/privacy/data/en/apple-maps/ ; https://www.apple.com/legal/internet-services/maps/legal-en.html  
- Apple Developer forums & discussions (used for verification attempts): https://developer.apple.com/forums/thread/67656 ; https://discussions.apple.com/thread/255104167  
- WWDC 2025 session on Apple Maps (overview of new capabilities): https://developer.apple.com/videos/play/wwdc2025/204/  
