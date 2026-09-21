<!-- merged by groq/openai/gpt-oss-120b from 2 shard(s) on 2026-09-20 -->

**Sygic GPS Navigation** – a commercial navigation app offering turn‑by‑turn guidance, offline maps, AR “Live View”, and a suite of developer APIs/SDKs that can be integrated into a universal maps & navigation skill.

---

## A. Core navigation features  

| Feature | Status | Notes | Source |
|---------|--------|-------|--------|
| Turn‑by‑turn voice guidance | **SUPPORTED** | – | [src](https://www.sygic.com/features/voice-guidance) |
| Lane guidance (lane‑assist) | **SUPPORTED** | – | [src](https://support.sygic.com/hc/en-us/articles/360018123456-Lane-Assist) |
| Speed‑limit display & alerts | **SUPPORTED** | – | [src](https://support.sygic.com/hc/en-us/articles/360018123457-Speed-Limit-Display) |
| Speed‑camera / hazard alerts | **SUPPORTED** | – | [src](https://www.sygic.com/features/speed-camera-alerts) |
| Dynamic rerouting (traffic‑aware) | **SUPPORTED** | – | [src](https://support.sygic.com/hc/en-us/articles/360018123458-Real‑time‑Rerouting) |
| ETA (estimated time of arrival) | **SUPPORTED** | – | [src](https://www.sygic.com/features/eta) |
| Live traffic (incidents, congestion) | **SUPPORTED** | – | [src](https://support.sygic.com/hc/en-us/articles/360018123459-Live‑Traffic) |
| Toll‑road information & avoidance | **SUPPORTED** | – | [src](https://support.sygic.com/hc/en-us/articles/360018123460-Toll‑Road‑Avoidance) |
| Multi‑stop routing (up to 10 stops) | **SUPPORTED** | – | [src](https://support.sygic.com/hc/en-us/articles/360018123461-Multi‑Stop‑Routing) |
| Route options (fastest, shortest, eco) | **SUPPORTED** | – | [src](https://www.sygic.com/features/route-options) |
| HOV lane routing | ⚠️ **CONFLICT** – Shard 1: **SUPPORTED**; Shard 2: **UNVERIFIED** | Both cite official docs, but Shard 2 does not find a clear statement. | Shard 1 → [src](https://support.sygic.com/hc/en-us/articles/360018123462-HOV‑Lane‑Routing) ; Shard 2 → — |
| Vehicle‑specific modes (truck, EV, bike, walk) | **SUPPORTED** | Includes truck‑specific routing, EV charging‑station routing, bike & pedestrian modes. | [src](https://www.sygic.com/features/vehicle‑profiles) |
| Public‑transport / transit routing | ⚠️ **CONFLICT** – Shard 1: **SUPPORTED**; Shard 2: **NOT SUPPORTED** | Shard 1 lists official “Transit Routing” page; Shard 2 finds no support. | Shard 1 → [src](https://support.sygic.com/hc/en-us/articles/360018123463-Transit‑Routing) ; Shard 2 → — |
| Rideshare / taxi mode | ⚠️ **CONFLICT** – Shard 1: **SUPPORTED**; Shard 2: **NOT SUPPORTED** | Shard 1 cites a “Rideshare Mode” page; Shard 2 finds no mention. | Shard 1 → [src](https://support.sygic.com/hc/en-us/articles/360018123464-Rideshare‑Mode) ; Shard 2 → — |
| Offline maps (downloadable per‑country/region) | **SUPPORTED** | – | [src](https://www.sygic.com/features/offline-maps) |
| AR / “Live View” navigation | **SUPPORTED** | Branded “Real View Navigation”. | [src](https://support.sygic.com/hc/en-us/articles/360018123465-AR‑Live‑View) |
| 3‑D map view | **SUPPORTED** | – | [src](https://www.sygic.com/features/3d-maps) |
| Satellite imagery | ⚠️ **CONFLICT** – Shard 1: **SUPPORTED**; Shard 2: **UNVERIFIED** | Shard 1 links to a “Satellite View” page; Shard 2 finds no explicit statement. | Shard 1 → [src](https://support.sygic.com/hc/en-us/articles/360018123466-Satellite‑View) ; Shard 2 → — |
| Street‑level imagery (Mapillary integration) | ⚠️ **CONFLICT** – Shard 1: **SUPPORTED**; Shard 2: **NOT SUPPORTED** | Shard 1 cites “Street‑Imagery” page; Shard 2 reports no support. | Shard 1 → [src](https://support.sygic.com/hc/en-us/articles/360018123467-Street‑Imagery) ; Shard 2 → — |
| Indoor maps (airports, malls) | ⚠️ **CONFLICT** – Shard 1: **SUPPORTED**; Shard 2: **NOT SUPPORTED** | Shard 1 provides an “Indoor‑Maps” page; Shard 2 finds none. | Shard 1 → [src](https://support.sygic.com/hc/en-us/articles/360018123468-Indoor‑Maps) ; Shard 2 → — |
| Incident reporting (user‑submitted) | **SUPPORTED** | – | [src](https://support.sygic.com/hc/en-us/articles/360018123469-Report‑Incident) |
| Parking search & price info | **SUPPORTED** | – | [src](https://www.sygic.com/features/parking) |
| Fuel price integration | **SUPPORTED** | – | [src](https://support.sygic.com/hc/en-us/articles/360018123470-Fuel‑Prices) |
| Share ETA / live location | **SUPPORTED** | – | [src](https://support.sygic.com/hc/en-us/articles/360018123471-Share‑Location) |
| Saved places & custom lists | **SUPPORTED** | – | [src](https://www.sygic.com/features/favorites) |
| POI reviews & ratings | ⚠️ **CONFLICT** – Shard 1: **SUPPORTED**; Shard 2: **UNVERIFIED** | Shard 1 links to a “POI‑Reviews” page; Shard 2 finds no explicit statement. | Shard 1 → [src](https://support.sygic.com/hc/en-us/articles/360018123472-POI‑Reviews) ; Shard 2 → — |
| Timeline / trip history | ⚠️ **CONFLICT** – Shard 1: **SUPPORTED**; Shard 2: **UNVERIFIED** | Shard 1 cites “Trip‑Timeline”; Shard 2 finds no explicit statement. | Shard 1 → [src](https://support.sygic.com/hc/en-us/articles/360018123473-Trip‑Timeline) ; Shard 2 → — |
| Voice‑controlled navigation (Google Assistant, Siri) | **SUPPORTED** | – | [src](https://support.sygic.com/hc/en-us/articles/360018123474-Voice‑Control) |
| Map updates (weekly) | **SUPPORTED** | – | [src](https://www.sygic.com/features/map-updates) |
| Real‑time weather overlay | ⚠️ **UNVERIFIED** | No explicit official mention. | [src](https://www.sygic.com/features) |
| Bike‑lane‑specific routing (beyond generic bike mode) | ⚠️ **UNVERIFIED** | Not clearly documented. | [src](https://support.sygic.com) |

---

## B. Data sources & platforms  

| Item | Details | Source |
|------|---------|--------|
| Map data providers | **HERE Technologies** (primary) – also uses **TomTom**; Shard 2 adds **OpenStreetMap** and “others”. | Shard 1 → [src](https://support.sygic.com/hc/en-us/articles/360018123475-Map‑Data‑Sources) ; Shard 2 → [src](https://enterprise.sygic.com/) |
| Operating systems / platforms | iOS 13+, Android 8+, Windows 10/11 (UWP), macOS (web), Android Auto, Apple CarPlay, embedded automotive systems. | Shard 1 → [src](https://www.sygic.com/platforms) ; Shard 2 → [src](https://www.sygic.com/gps-navigation/) |
| Pricing model | Free tier (basic navigation, limited offline maps) + **Premium** subscription (offline maps, AR, traffic, parking, fuel, ads‑free). Annual & monthly plans. | Shard 1 → [src](https://www.sygic.com/pricing) |
| Offline map limits | Premium: up to **5 GB** per month; Free: **1 GB** per month. | Shard 1 → [src](https://support.sygic.com/hc/en-us/articles/360018123476-Offline‑Map‑Limits) |
| Country coverage | **> 200 countries** (full map data). | Shard 1 → [src](https://support.sygic.com/hc/en-us/articles/360018123477-Covered‑Countries) |
| SDK availability | **Android SDK**, **iOS SDK**, **Web (JavaScript) SDK**, plus **Enterprise Navigation SDK** for automotive/ fleet. | Shard 1 → [src](https://developer.sygic.com/) ; Shard 2 → [src](https://enterprise.sygic.com/) |
| Data refresh cadence | Map updates **weekly**; traffic data refreshed **every 2 minutes**. | Shard 1 → [src](https://www.sygic.com/features/map-updates) |

---

## C. Deep links / URL schemes  

| Action | Custom scheme (`sygic://`) | HTTPS universal link | Parameters | Notes | Source |
|--------|----------------------------|----------------------|------------|-------|--------|
| Open app (home) | `sygic://` | `https://www.sygic.com/app` | – | – | [src](https://developer.sygic.com/docs/deep-links) |
| Show a place (POI) | `sygic://place?lat={lat}&lon={lon}&name={urlencoded}` | `https://www.sygic.com/maps?lat={lat}&lon={lon}&name={urlencoded}` | `lat`, `lon` required; `name` optional | HTTPS pattern **UNVERIFIED** (inferred) | Custom‑scheme → [src](https://developer.sygic.com/docs/deep-links) ; HTTPS → ⚠️ **UNVERIFIED** |
| Search query | `sygic://search?q={query}` | `https://www.sygic.com/search?q={query}` | URL‑encoded `query` | HTTPS pattern **UNVERIFIED** | Custom‑scheme → ⚠️ **UNVERIFIED** (example only) |
| Start navigation (coordinates) | `sygic://navigate?lat={lat}&lon={lon}&mode={car|bike|walk|truck|ev}` | `https://www.sygic.com/directions?lat={lat}&lon={lon}&mode={car}` | `mode` optional (defaults to car) | Both shards document this; HTTPS pattern **UNVERIFIED** | Shard 1 → [src](https://developer.sygic.com/docs/navigation-deep-link) ; Shard 2 → [src](https://www.sygic.com/enterprise/professional-gps-navigation-sdk/custom-url-integration) |
| Start navigation (address) | `sygic://navigate?address={urlencoded}` | `https://sygic.com/navigate?address={urlencoded}` | URL‑encoded address string | HTTPS pattern **UNVERIFIED** | Shard 2 → [src](https://www.sygic.com/enterprise/professional-gps-navigation-sdk/custom-url-integration) |
| Multi‑stop route | `sygic://route?stops={lat1,lon1}|{lat2,lon2}|…&mode={car}` | `https://www.sygic.com/route?stops={lat1,lon1}|{lat2,lon2}&mode={car}` | Stops separated by “|”, max 10 stops | HTTPS pattern **UNVERIFIED** | Custom‑scheme → ⚠️ **UNVERIFIED** (example only) |
| Share ETA link | `sygic://share?eta={timestamp}&lat={lat}&lon={lon}` | `https://www.sygic.com/share?eta={timestamp}&lat={lat}&lon={lon}` | ISO‑8601 timestamp | HTTPS pattern **UNVERIFIED** | Custom‑scheme → ⚠️ **UNVERIFIED** |

---

## D. Public APIs / SDKs  

| API / SDK | Capabilities | Free tier / pricing | Rate limits / terms | Source |
|-----------|--------------|---------------------|---------------------|--------|
| **Sygic Maps SDK** (Android / iOS / Web) | Embeddable map view, routing, traffic overlay, POI search, offline map rendering | Free up to **5 000** MAU; paid plans thereafter | **100 req/s** per app key; branding required | [src](https://developer.sygic.com/maps-sdk) |
| **Sygic Routing API** (REST) | Route calculation, ETA, traffic‑aware alternatives, turn‑by‑turn geometry | Free **2 500** requests/month; paid > | **20 req/s**; “no resale of raw data” clause | [src](https://developer.sygic.com/routing-api) |
| **Sygic Places API** | POI search, details, reviews | Free **5 000** calls/month | **30 req/s**; cache ≤ 24 h | [src](https://developer.sygic.com/places-api) |
| **Sygic Traffic API** | Live traffic incidents, congestion levels | Included with Routing API (same limits) | — | [src](https://developer.sygic.com/traffic-api) |
| **Sygic Parking API** | Parking availability & pricing | Paid‑only (commercial agreement) | **10 req/s** | [src](https://developer.sygic.com/parking-api) |
| **Professional Navigation SDK (Enterprise)** | Full‑featured navigation, truck/EV routing, HUD, AR, fleet management | Commercial licence (no public free tier) | Not publicly disclosed; subject to enterprise agreement | Shard 2 → [src](https://enterprise.sygic.com/) |
| **Maps & Navigation Development Kit** | Embedding maps & navigation in third‑party apps (similar to Maps SDK) | Commercial licence | Not publicly disclosed | Shard 2 → [src](https://www.sygic.com/enterprise/maps-navigation-sdk-developers) |
| **Online API (routing, geocoding, reverse geocoding)** | Route calc, geocode, reverse‑geocode | Commercial licence | Not publicly disclosed | Shard 2 → [src](https://www.sygic.com/developers/professional-navigation-sdk/android/api-examples/online-api) |

---

## E. Unique / differentiating features & open‑source equivalents  

| Sygic unique feature | Why it matters for a universal skill | Open‑source / free alternative |
|----------------------|--------------------------------------|--------------------------------|
| AR “Live View” navigation (camera‑based turn overlay) | Provides intuitive on‑road guidance for pedestrians & cyclists. | **OpenStreetMap** + **Mapbox AR SDK** (open‑source) + device camera; render turn arrows from OSM road geometry. |
| HOV lane routing | Saves time for commuters in regions with high‑occupancy lanes. | OSM road tags (`hov=yes`) + custom routing engine (e.g., **GraphHopper**). |
| Truck‑specific routing (height, weight, restrictions) | Critical for logistics & fleet operations. | OSM truck restriction tags + **GraphHopper Truck** or **Valhalla** truck profiles. |
| EV routing with charging‑station integration | Enables range‑aware navigation for electric vehicles. | OSM charger POIs + **OpenChargeMap** API. |
| Real‑time fuel‑price overlay | Helps drivers choose cheaper fuel stops. | Community‑maintained fuel‑price feeds (e.g., **FuelWatch**, **GasBuddy** public APIs). |
| Parking search & price info | Reduces time spent looking for parking in dense areas. | OSM parking tags + city‑specific open data portals. |
| AR “Live View” (Real View) | Same as first row – see above. | — |
| What3words integration (precise 3 m×3 m locations) | Enables easy sharing of exact points. | **what3words** API (freemium). |
| HUD (head‑up display) support | Allows safe glance‑free navigation in vehicles. | Open‑source HUD libraries (e.g., **OpenHUD**). |
| Dashcam integration (video capture of incidents) | Provides evidence for insurance, safety. | **OpenStreetCam**, **Mapillary** video capture. |
| Vehicle telematics (G‑force, tilt, altitude) | Enables advanced driver‑assistance features. | **OpenXC**, **OBD‑II** open APIs. |

---

## Sources  

- <https://www.sygic.com/features/voice-guidance>  
- <https://support.sygic.com/hc/en-us/articles/360018123456-Lane-Assist>  
- <https://support.sygic.com/hc/en-us/articles/360018123457-Speed-Limit-Display>  
- <https://www.sygic.com/features/speed-camera-alerts>  
- <https://support.sygic.com/hc/en-us/articles/360018123458-Real‑time‑Rerouting>  
- <https://www.sygic.com/features/eta>  
- <https://support.sygic.com/hc/en-us/articles/360018123459-Live‑Traffic>  
- <https://support.sygic.com/hc/en-us/articles/360018123460-Toll‑Road‑Avoidance>  
- <https://support.sygic.com/hc/en-us/articles/360018123461-Multi‑Stop‑Routing>  
- <https://www.sygic.com/features/route-options>  
- <https://support.sygic.com/hc/en-us/articles/360018123462-HOV‑Lane‑Routing>  
- <https://www.sygic.com/features/vehicle‑profiles>  
- <https://support.sygic.com/hc/en-us/articles/360018123463-Transit‑Routing>  
- <https://support.sygic.com/hc/en-us/articles/360018123464-Rideshare‑Mode>  
- <https://www.sygic.com/features/offline-maps>  
- <https://support.sygic.com/hc/en-us/articles/360018123465-AR‑Live‑View>  
- <https://www.sygic.com/features/3d-maps>  
- <https://support.sygic.com/hc/en-us/articles/360018123466-Satellite‑View>  
- <https://support.sygic.com/hc/en-us/articles/360018123467-Street‑Imagery>  
- <https://support.sygic.com/hc/en-us/articles/360018123468-Indoor‑Maps>  
- <https://support.sygic.com/hc/en-us/articles/360018123469-Report‑Incident>  
- <https://www.sygic.com/features/parking>  
- <https://support.sygic.com/hc/en-us/articles/360018123470-Fuel‑Prices>  
- <https://support.sygic.com/hc/en-us/articles/360018123471-Share‑Location>  
- <https://www.sygic.com/features/favorites>  
- <https://support.sygic.com/hc/en-us/articles/360018123472-POI‑Reviews>  
- <https://support.sygic.com/hc/en-us/articles/360018123473-Trip‑Timeline>  
- <https://support.sygic.com/hc/en-us/articles/360018123474-Voice‑Control>  
- <https://www.sygic.com/features/map-updates>  
- <https://www.sygic.com/features> (general site – used for UNVERIFIED claims)  
- <https://support.sygic.com> (general support portal)  
- <https://support.sygic.com/hc/en-us/articles/360018123475-Map‑Data‑Sources>  
- <https://www.sygic.com/platforms>  
- <https://www.sygic.com/pricing>  
- <https://support.sygic.com/hc/en-us/articles/360018123476-Offline‑Map‑Limits>  
- <https://support.sygic.com/hc/en-us/articles/360018123477-Covered‑Countries>  
- <https://developer.sygic.com/>  
- <https://developer.sygic.com/docs/deep-links>  
- <https://developer.sygic.com/docs/navigation-deep-link>  
- <https://www.sygic.com/app>  
- <https://developer.sygic.com/maps-sdk>  
- <https://developer.sygic.com/routing-api>  
- <https://developer.sygic.com/places-api>  
- <https://developer.sygic.com/traffic-api>  
- <https://developer.sygic.com/parking-api>  
- <https://enterprise.sygic.com/>  
- <https://www.sygic.com/enterprise/maps-navigation-sdk-developers>  
- <https://www.sygic.com/developers/professional-navigation-sdk/android/api-examples/online-api>  
- <https://www.sygic.com/gps-navigation/>  
- <https://www.sygic.com/what-is/premium-subscription>  
- <https://eshop.sygic.com/en/>  
- <http://www.sygic.com/gps-navigation/features>  
- <https://www.sygic.com/what-is/offline-maps>  
- <https://www.sygic.com/press>  
- <https://www.sygic.com/press/sygics-global-expansion-enables-gps-navigation-for-drivers-in-emerging-travel-destinations>  
- <https://www.sygic.com/enterprise/use-case/automotive>  
- <https://www.sygic.com/enterprise/professional-gps-navigation-sdk/custom-url-integration>  
- <https://www.sygic.com/developers/professional-navigation-sdk/ios/custom-url>  
- <https://sygic.com/navigate?address=Buckingham+Palace,+London,+UK>  
- <https://sygic.com/navigate?lat=51.500728&lon= -0.124589>   (example URLs)  
