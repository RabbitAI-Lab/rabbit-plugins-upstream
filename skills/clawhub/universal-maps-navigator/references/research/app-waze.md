<!-- merged by groq/openai/gpt-oss-120b from 2 shard(s) on 2026-09-20 -->

**Waze – Universal Maps & Navigation Skill (2026)** – Real‑time, crowd‑sourced driving navigation with live‑traffic, incident reporting and deep‑link integration; no official offline maps, truck/EV routing, or indoor navigation.

---

## 1. Core Navigation Feature Inventory  

| Feature | Status / Notes | Source |
|---------|----------------|--------|
| Turn‑by‑turn navigation | **SUPPORTED** | [src](https://support.google.com/waze/answer/6132259) |
| Voice guidance (spoken directions) | **SUPPORTED** | [src](https://support.google.com/waze/answer/6132259) |
| Lane guidance (visual lane arrows) | **SUPPORTED** | [src](https://support.google.com/waze/answer/7357394) |
| Real‑time speed limits | **SUPPORTED** | [src](https://support.google.com/waze/answer/7357394) |
| Speed‑camera / hazard alerts (user‑reported) | **SUPPORTED** | [src](https://support.google.com/waze/answer/7357395) |
| Automatic rerouting (traffic‑aware) | **SUPPORTED** | [src](https://support.google.com/waze/answer/6132259) |
| ETA & arrival‑time updates | **SUPPORTED** | [src](https://support.google.com/waze/answer/6132259) |
| Live traffic overlay (congestion colors) | **SUPPORTED** | [src](https://support.google.com/waze/answer/7357394) |
| Toll road avoidance (settings) | **SUPPORTED** | [src](https://support.google.com/waze/answer/7357394) |
| Multi‑stop routing (add stops) | **SUPPORTED** | [src](https://support.google.com/waze/answer/7357394) |
| Route options (alternative routes preview) | **SUPPORTED** | [src](https://support.google.com/waze/answer/7357394) |
| HOV lane routing | ⚠️ **CONFLICT** – Shard 1: **UNVERIFIED** (no UI documented) | Shard 1 [src](https://support.google.com/waze/answer/7357394)  • Shard 2 **SUPPORTED** [src](https://www.waze.com/) |
| Truck‑specific routing (weight/height) | ⚠️ **CONFLICT** – Shard 1: **NOT SUPPORTED** | Shard 1 [src](https://support.google.com/waze/answer/7357394)  • Shard 2 **SUPPORTED** [src](https://www.waze.com/) |
| EV‑specific routing (charging stations) | ⚠️ **CONFLICT** – Shard 1: **NOT SUPPORTED** | Shard 1 [src](https://support.google.com/waze/answer/7357394)  • Shard 2 **SUPPORTED** [src](https://www.waze.com/) |
| Bike / pedestrian / transit modes | **NOT SUPPORTED** | [src](https://support.google.com/waze/answer/7357394) |
| Rideshare mode (Waze Carpool – separate app) | **NOT SUPPORTED** (core navigation) | [src](https://www.waze.com/carpool) |
| Offline maps (pre‑download) | **NOT SUPPORTED** | [src](https://support.google.com/waze/answer/7357394) |
| AR “Live View” (on‑screen navigation) | ⚠️ **CONFLICT** – Shard 1: **SUPPORTED** | Shard 1 [src](https://support.google.com/waze/answer/7357394)  • Shard 2 **UNVERIFIED** [src](https://www.waze.com/) |
| 3‑D map view | ⚠️ **CONFLICT** – Shard 1: **NOT SUPPORTED** | Shard 1 [src](https://support.google.com/waze/answer/7357394)  • Shard 2 **SUPPORTED** [src](https://www.waze.com/) |
| Satellite imagery | ⚠️ **CONFLICT** – Shard 1: **NOT SUPPORTED** | Shard 1 [src](https://support.google.com/waze/answer/7357394)  • Shard 2 **SUPPORTED** [src](https://www.waze.com/) |
| Street‑level imagery (Street View‑like) | ⚠️ **CONFLICT** – Shard 1: **NOT SUPPORTED** | Shard 1 [src](https://support.google.com/waze/answer/7357394)  • Shard 2 **SUPPORTED** [src](https://www.waze.com/) |
| Indoor navigation | **NOT SUPPORTED** | [src](https://support.google.com/waze/answer/7357395) |
| Incident reporting (traffic, police, hazards) | **SUPPORTED** | [src](https://support.google.com/waze/answer/7357395) |
| Parking availability (community‑reported) | ⚠️ **CONFLICT** – Shard 1: **UNVERIFIED** (pilot pilots) | Shard 1 [src](https://support.google.com/waze/answer/7357395)  • Shard 2 **SUPPORTED** [src](https://www.waze.com/) |
| Fuel‑price reporting (user‑submitted) | **SUPPORTED** | [src](https://support.google.com/waze/answer/7357395) |
| Share ETA / live location | **SUPPORTED** | [src](https://support.google.com/waze/answer/7357395) |
| Saved places / “Favorites” lists | **SUPPORTED** | [src](https://support.google.com/waze/answer/7357395) |
| Place reviews / star ratings | ⚠️ **CONFLICT** – Shard 1: **NOT SUPPORTED** | Shard 1 [src](https://support.google.com/waze/answer/7357395)  • Shard 2 **SUPPORTED** [src](https://www.waze.com/) |
| Timeline / travel history | **NOT SUPPORTED** | [src](https://support.google.com/waze/answer/7357395) |
| Voice‑controlled navigation (Google Assistant) | **SUPPORTED** | [src](https://support.google.com/waze/answer/7357394) |
| Map style customization (night / day) | **SUPPORTED** | [src](https://support.google.com/waze/answer/7357394) |

---

## 2. Data Sources & Platform Details  

| Item | Details | Source |
|------|---------|--------|
| Map data provider | **Shard 1:** Crowd‑sourced map built by Waze users (no OSM). <br>**Shard 2:** Mix of user‑generated data, US TIGER government data, and commercial sources. | [src 1](https://www.waze.com/about/features) • [src 2](https://www.waze.com//wiki/USA/Basemap) |
| Supported platforms | iOS (App Store), Android (Google Play), Web “Live Map” (waze.com/live) | [src 1](https://apps.apple.com/app/waze-navigation-live-traffic/id323229106) • [src 1](https://play.google.com/store/apps/details?id=com.waze) |
| Pricing for end‑users | Free download, ad‑supported (non‑intrusive) | [src](https://support.google.com/waze/answer/7357394) |
| Country coverage | **Shard 1:** > 190 countries. <br>**Shard 2:** 180+ countries & territories. | [src 1](https://support.google.com/waze/answer/7357394#countries) • [src 2](https://wiki.waze.com/wiki/Countries_and_Languages) |
| Offline support | No offline map download; requires data connection for routing. | [src](https://support.google.com/waze/answer/7357394) |

---

## 3. Deep Links / URL Schemes  

| Action | Template (example) | Parameters (key) | Source |
|--------|-------------------|------------------|--------|
| Open map centered on lat/lon (custom scheme) | `waze://?ll=37.7749,-122.4194` | `ll` = lat,lon | [src 1](https://developers.google.com/waze/deeplinks) |
| Start navigation to lat/lon (custom scheme) | `waze://?ll=37.7749,-122.4194&navigate=yes` | `ll`, `navigate` = `yes`/`no`, optional `z` = zoom, `mode` = `driving` (default) | [src 1](https://developers.google.com/waze/deeplinks) |
| Search address & center map (custom scheme) | `waze://?q=1600+Amphitheatre+Parkway` | `q` = URL‑encoded address | [src 2](https://www.waze.com/forum/viewtopic.php?f=18&t=31443) |
| Search address & start navigation (custom scheme) | `waze://?q=1600+Amphitheatre+Parkway&navigate=yes` | `q`, `navigate` | [src 2](https://www.waze.com/forum/viewtopic.php?f=18&t=31443) |
| Set zoom level (custom scheme) | `waze://?z=12` | `z` = zoom level (integer) | [src 2](https://www.waze.com/forum/viewtopic.php?f=18&t=31443) |
| Universal HTTPS navigation link | `https://waze.com/ul?ll=37.7749,-122.4194&navigate=yes` | `ll`, `navigate` | [src 1](https://developers.google.com/waze/deeplinks) |
| Universal HTTPS address search | `https://waze.com/ul?q=1600+Amphitheatre+Parkway` | `q` | [src 2](https://www.waze.com/discuss/t/deep-link-to-navigate-by-address/337725) |
| Universal HTTPS address search + navigation | `https://waze.com/ul?q=1600+Amphitheatre+Parkway&navigate=yes` | `q`, `navigate` | [src 2](https://www.waze.com/discuss/t/deep-link-to-navigate-by-address/337725) |

*All parameters are case‑sensitive and must be URL‑encoded.*

---

## 4. Public APIs / SDKs  

| API / SDK | Availability | Rate Limits / Terms | Source |
|-----------|--------------|---------------------|--------|
| Waze Deep Links (custom scheme & HTTPS) | Public, free | No published rate limits; attribution required | [src 1](https://developers.google.com/waze/deeplinks) |
| Waze Transport SDK | Partner‑only (application required) | Not public | [src 2](https://www.waze.com/sdk) |
| Waze Map Editor JavaScript SDK | Public (for community map editors) | Not public | [src 2](https://www.waze.com/editor/sdk/index.html) |
| Waze for Cities API (traffic/incident data) | Partner‑only (city/municipality partners) | Not public | [src 2](https://www.waze.com/wazeforcities/) |

---

## 5. Unique / Differentiating Features  

| Waze Feature | Emulation Suggestion (Open‑source) | Open Data / API Alternative |
|--------------|------------------------------------|------------------------------|
| Crowdsourced traffic & hazard alerts | Pull community‑reported incidents from OSM + local traffic feeds | OSM + Overpass API, Open‑Meteo, city traffic APIs |
| Real‑time incident reporting | Provide UI for user submissions to a public endpoint | OSM + custom incident API |
| Community map editing | Allow users to edit map data via an editor | OpenStreetMap |
| EV charging station routing (if supported) | Use OSM charging‑station tags | OpenChargeMap |
| Truck‑specific routing (if supported) | Use Valhalla or OSRM with truck profiles | Valhalla, OSRM |
| Fuel‑price comparison | Aggregate fuel‑price feeds | GlobalPetrolPrices, local APIs |

---

## Sources  

- https://support.google.com/waze/answer/6132259  
- https://support.google.com/waze/answer/7357394  
- https://support.google.com/waze/answer/7357395  
- https://www.waze.com/carpool  
- https://www.waze.com/about/features  
- https://apps.apple.com/app/waze-navigation-live-traffic/id323229106  
- https://play.google.com/store/apps/details?id=com.waze  
- https://support.google.com/waze/answer/7357394#countries  
- https://developers.google.com/waze/deeplinks  
- https://waze.com/ul?ll=37.7749,-122.4194  
- https://www.waze.com/  
- https://www.waze.com/wazeforcities/  
- https://www.waze.com//wiki/USA/Basemap  
- https://wiki.waze.com/wiki/Countries_and_Languages  
- https://www.waze.com/forum/viewtopic.php?f=18&t=31443  
- https://www.waze.com/discuss/t/deep-link-to-navigate-by-address/337725  
- https://www.waze.com/sdk  
- https://www.waze.com/editor/sdk/index.html  
