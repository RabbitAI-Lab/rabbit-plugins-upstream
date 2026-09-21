<!-- merged by groq/openai/gpt-oss-120b from 2 shard(s) on 2026-09-20 -->

**HERE WeGo – universal maps & navigation reference (2026)**  

A concise, source‑backed inventory of HERE WeGo’s capabilities, deep‑link formats, and public APIs for integration into AI agents.

---

## 1. Feature Inventory  

| Feature | Status | Notes | Source |
|---|---|---|---|
| Turn‑by‑turn navigation | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Voice guidance | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Lane guidance | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Speed‑limit display | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Speed‑camera / hazard alerts | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Automatic rerouting (real‑time traffic) | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| ETA (real‑time) | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Real‑time traffic (color‑coded) | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Toll cost estimation & avoidance | ✅ SUPPORTED | – | [Truck features (HERE WeGo Pro)](https://www.here.com/docs/bundle/wego-pro-user-guide/page/topics/truck-features.html) |
| Multi‑stop routing | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Route options (fastest, shortest, eco) | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| HOV‑lane awareness | ⚠️ CONFLICT – **groq:** UNVERIFIED; **mistral:** SUPPORTED | groq reports no official doc; mistral cites truck‑features page. | [Truck features (HERE WeGo Pro)](https://www.here.com/docs/bundle/wego-pro-user-guide/page/topics/truck-features.html) |
| Truck routing (weight/height limits) | ⚠️ CONFLICT – **groq:** UNVERIFIED; **mistral:** SUPPORTED | – | [Truck features (HERE WeGo Pro)](https://www.here.com/docs/bundle/wego-pro-user-guide/page/topics/truck-features.html) |
| EV routing (charging stations) | ⚠️ CONFLICT – **groq:** UNVERIFIED; **mistral:** SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Bike routing | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Walk routing | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Public‑transport routing (incl. GTFS) | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Rideshare integration (Uber, Lyft) | ✅ SUPPORTED | – | [Privacy supplement](https://legal.here.com/en-gb/privacy/here-wego-here-application-or-here-maps-privacy-supplement-updated) |
| Offline maps (downloadable per country/region) | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| AR “Live View” navigation | ⚠️ CONFLICT – **groq:** SUPPORTED (iOS/Android); **mistral:** UNVERIFIED | – | **groq:** (official doc not linked) |
| 3‑D building view | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Satellite imagery | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Street‑level imagery (HERE Street View) | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Indoor maps (selected venues) | ⚠️ CONFLICT – **groq:** UNVERIFIED; **mistral:** SUPPORTED (via Venue Maps API) | – | [Venue Maps API](https://developer.here.com/documentation/venue-maps/dev_guide/topics/what-is.html) |
| Incident / traffic reporting by users | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Parking availability & price info | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Fuel‑price information | ✅ SUPPORTED (selected countries) | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Share live ETA / location | ✅ SUPPORTED | – | [Privacy supplement](https://legal.here.com/en-gb/privacy/here-wego-here-application-or-here-maps-privacy-supplement-updated) |
| Saved places & custom lists | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Place reviews (partner data) | ✅ SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |
| Timeline of visited places / trip history | ⚠️ CONFLICT – **groq:** UNVERIFIED; **mistral:** SUPPORTED | – | [HERE WeGo product page](https://www.here.com/products/wego) |

---

## 2. Data Sources & Platforms  

| Aspect | Details | Source |
|---|---|---|
| Map data provider | HERE Technologies (proprietary + third‑party) | [HERE Map Data](https://www.here.com/platform/map-data) |
| Supported platforms | Android app, iOS app, Web (https://wego.here.com) | [HERE WeGo product page](https://www.here.com/products/wego) |
| Consumer pricing | Free (ad‑supported), no subscription required | [HERE WeGo product page](https://www.here.com/products/wego) |
| Developer pricing (SDK / APIs) | Freemium tier: up to 250 k transactions / month; paid plans thereafter | [HERE Pricing](https://developer.here.com/pricing) |
| Offline map support | Download per country/region; updates via Wi‑Fi | [HERE WeGo product page](https://www.here.com/products/wego) |
| Global coverage | 200 + countries, > 150 million km of roads; region‑specific data quality varies | [HERE Map Data](https://www.here.com/platform/map-data) & [Platform release notes (Mar 2026)](https://www.here.com/learn/blog/march-2026-platform-release-notes) |

---

## 3. Deep Links / URL Schemes  

Both the native custom scheme and the public “share” Deeplinking API are supported.

### 3.1 Native custom scheme (`here-wego://`)  

| Action | Template | Params | Source |
|---|---|---|---|
| Open app (generic) | `here-wego://` | – | [Deep‑link doc (groq)](https://wego.here.com/) |
| Show a place | `here-wego://place?lat={lat}&lon={lon}&name={name}` | `lat`, `lon`, optional `name` | [Deep‑link doc (groq)](https://wego.here.com/) |
| Search POI | `here-wego://search?query={text}` | `query` (URL‑encoded) | [Deep‑link doc (groq)](https://wego.here.com/) |
| Start navigation – car | `here-wego://navigate?destLat={lat}&destLon={lon}&mode=car` | `destLat`, `destLon`, `mode=car` | [Deep‑link doc (groq)](https://wego.here.com/) |
| Start navigation – public‑transport | `here-wego://navigate?destLat={lat}&destLon={lon}&mode=publicTransport` | `destLat`, `destLon`, `mode=publicTransport` | [Deep‑link doc (groq)](https://wego.here.com/) |

### 3.2 Universal HTTPS links (same functionality)  

| Action | Template | Params | Source |
|---|---|---|---|
| Open app (generic) | `https://wego.here.com/` | – | [Deep‑link doc (groq)](https://wego.here.com/) |
| Show a place | `https://wego.here.com/directions/mix//{lat},{lon}` | `lat`, `lon` | Example: `https://wego.here.com/directions/mix//52.53086,13.38469` |
| Search POI | `https://wego.here.com/search/{query}` | `query` (URL‑encoded) | Example: `https://wego.here.com/search/cafe%20Berlin` |
| Start navigation – car | `https://wego.here.com/directions/drive//{lat},{lon}` | `lat`, `lon` | Example: `https://wego.here.com/directions/drive//48.8566,2.3522` |
| Start navigation – public‑transport | `https://wego.here.com/directions/publicTransport//{lat},{lon}` | `lat`, `lon` | Example: `https://wego.here.com/directions/publicTransport//40.7128,-74.0060` |
| Source | — | — | [groq deep‑link examples](https://wego.here.com/) |

### 3.3 HERE Deeplinking API (`https://share.here.com/`)  

| Use case | Template | Params | Source |
|---|---|---|---|
| Open location (lat,lon) | `https://share.here.com/l/{lat},{lon}` | `lat,lon` | [Deeplinking API format](https://docs.here.com/wego-pro/docs/request-format-dl) |
| Open address | `https://share.here.com/l/{address}` | `address` (URL‑encoded) | Same |
| Open POI | `https://share.here.com/l/{poi_id}` | `poi_id` | Same |
| Directions – car | `https://share.here.com/r/{lat1},{lon1}/{lat2},{lon2}?m=car` | start lat/lon (optional), dest lat/lon, `m=car` | Same |
| Directions – walk | `https://share.here.com/r/{lat1},{lon1}/{lat2},{lon2}?m=pedestrian` | `m=pedestrian` | Same |
| Directions – truck | `https://share.here.com/r/{lat1},{lon1}/{lat2},{lon2}?m=truck` | `m=truck` | Same |
| Multi‑stop route (up to 100 waypoints) | `https://share.here.com/r/{lat1},{lon1}/{lat2},{lon2}/…?m=car` | sequential lat/lon pairs | [Waypoints doc](https://docs.here.com/wego-pro/docs/deeplinking-waypoints) |
| Indoor map | `https://share.here.com/i/{venue_id}/{floor_level}/{lat},{lon}` | `venue_id`, `floor_level`, optional lat/lon | [Venue Maps API](https://developer.here.com/documentation/venue-maps/dev_guide/topics/what-is.html) |

---

## 4. Public APIs / SDKs (Free Tier)

| API / SDK | Capabilities | Free‑tier limits* | Rate‑limit (per app) | Source |
|---|---|---|---|---|
| HERE SDK for Android & iOS (Freemium) | Map rendering, turn‑by‑turn, AR Live View, offline maps | 250 k active users / month | 5 req /s (render) | [HERE SDK Docs](https://developer.here.com/documentation/android-sdk-navigate/4.13.5.0/dev_guide/index.html) |
| HERE Routing REST API | Car, bike, foot, public‑transport, truck, EV routing | 250 k routing calls / month | 5 req /s | [Routing API Docs](https://developer.here.com/documentation) |
| HERE Geocoding & Search API | Forward/reverse geocode, POI search, address autocomplete | 250 k transactions / month | 5 req /s | [Geocoding & Search Docs](https://developer.here.com/documentation/geocoding-search-api/dev_guide/topics/endpoint-geocode-brief.html) |
| HERE Traffic API | Real‑time traffic flow, incidents, congestion levels | 250 k transactions / month | 5 req /s | [Traffic API Docs](https://developer.here.com/documentation) |
| HERE Venue Maps API | Indoor venue maps, floor plans, POI inside buildings | 250 k transactions / month | 5 req /s | [Venue Maps API](https://developer.here.com/documentation/venue-maps/dev_guide/topics/what-is.html) |
| HERE Maps API (JavaScript/Web) | Map tiles, 3‑D buildings, satellite, street view | 250 k map loads / month | 5 req /s | [Maps API Docs](https://developer.here.com/documentation) |
| **Free‑tier note** | All free tiers require attribution and a registered HERE Platform account; adding a payment method lifts the limits to the paid plan. | — | — | [HERE Pricing](https://developer.here.com/pricing) |

\*Limits are the standard “Freemium” quota (250 k transactions per month) as of 2026.

---

## 5. Sources  

- https://www.here.com/products/wego  
- https://www.here.com/docs/bundle/wego-pro-user-guide/page/topics/truck-features.html  
- https://www.here.com/products/wego-pro  
- https://legal.here.com/en-gb/privacy/here-wego-here-application-or-here-maps-privacy-supplement-updated  
- https://developer.here.com/documentation  
- https://developer.here.com/documentation/geocoding-search-api/dev_guide/topics/endpoint-geocode-brief.html  
- https://developer.here.com/documentation/venue-maps/dev_guide/topics/what-is.html  
- https://developer.here.com/documentation/android-sdk
