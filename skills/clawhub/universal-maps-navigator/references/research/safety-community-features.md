<!-- merged by groq/openai/gpt-oss-120b from 1 shard(s) on 2026-09-20 -->

**Summary:** This reference consolidates open‑data tags, API endpoints, licensing, limits, and standards for community‑safety and navigation features (parking, fuel prices, ETA/live‑location sharing, and wheelchair‑accessible routing) that can be used by a universal maps & navigation skill.

---

## 1. Parking – OpenStreetMap (OSM) & Parkopedia

### 1.1 OSM Parking Tags  

| Tag | Description | Example Value |
|-----|-------------|---------------|
| `amenity=parking` | Public parking lot/facility (area or node) | – |
| `parking` | Surface type / structure | `surface`, `underground`, `multi-storey`, `street_side` |
| `access` | Access restriction | `public`, `private`, `customers` |
| `fee` | Fee status | `yes`, `no`, `free` |
| `capacity` | Number of spaces | `250` |
| `supervised` | Presence of staff | `yes`, `no` |
| `maxstay` | Maximum stay time | `2h` |
| `opening_hours` | Opening hours string | `Mo-Fr 08:00-20:00` |
| `amenity=parking_space` | Individual parking space (rare) | – |
| `wheelchair` | Accessibility of the lot/space | `yes`, `no`, `limited` |

**Example OSM XML**

```xml
<way id="12345">
  <tag k="amenity" v="parking"/>
  <tag k="parking" v="surface"/>
  <tag k="capacity" v="250"/>
  <tag k="fee" v="no"/>
  <tag k="wheelchair" v="yes"/>
</way>
```

**Sources**: [OSM Wiki: Tag:amenity=parking][src1] • [OSM Wiki: Parking][src2]

### 1.2 Parkopedia API (Proprietary)

| Feature | Endpoint (relative to base URL) | Method | Required Params | Notes |
|---------|--------------------------------|--------|----------------|-------|
| Search parking facilities | `/api/parking/search` | GET | `lat`, `lon`, optional `radius`, `filters` (price, availability) | Real‑time availability & pricing |
| Availability details | `/api/parking/availability` | GET | `parking_id` | Returns current occupancy, price tiers |
| Authentication | – | – | `api_key` (header or query) | Registration required |

- **Coverage:** ≈ 90 million spaces in 90+ countries.  
- **Licensing:** Proprietary commercial licence (widely used by OEMs).  
- **Rate limits:** Not publicly disclosed; contact sales for details.

**Sources**: [Parkopedia Business][src3] • [Parkopedia FAQ][src4]

---

## 2. Fuel Prices – Open Data APIs

| Country | Provider | Endpoint Template | Method | Params | License | Update Frequency |
|---------|----------|-------------------|--------|--------|---------|-------------------|
| Germany | Tankerkönig | `https://creativecommons.tankerkoenig.de/json/prices.php?ids={ids}&apikey={key}` | GET | `ids` (comma‑separated station IDs), `apikey` | CC BY 4.0 (commercial use allowed) | 4–10 min |
| Germany | Tankerkönig (station details) | `https://creativecommons.tankerkoenig.de/json/detail.php?id={id}&apikey={key}` | GET | `id`, `apikey` | CC BY 4.0 | 4–10 min |
| France | prix‑carburants.gouv.fr | `https://data.economie.gouv.fr/api/records/1.0/search/?dataset=prix-des-carburants-en-france-flux-instantane-v2&...` | GET | Standard Opendata query params (e.g., `q`, `rows`) | Open License (Etalab) | 10 min |
| Other (e.g., Spain, Italy, Australia) | National/open‑data portals | Varies | Varies | Varies | Varies (usually open) | Varies |

**Sources**: [Tankerkönig API][src5] • [prix‑carburants.gouv.fr Open Data][src6]

---

## 3. ETA & Live‑Location Sharing Standards

| Standard | URI / Code Format | Typical Use | Key Docs |
|----------|-------------------|-------------|----------|
| **geo: URI** (RFC 5870) | `geo:lat,lon;u=uncertainty` (e.g., `geo:52.5163,13.3779`) | Deep‑linking to map apps, SMS, web | [RFC 5870][src7] • [Wikipedia][src8] |
| **Open Location Code (Plus Codes)** | Full: `8FVC9G8F+6W` • Short: `8FVC9G8F` | Voice/text sharing where addresses missing | [Open Location Code Spec][src9] |
| **what3words** | `word.word.word` (3‑word address) | Emergency, logistics, precise location | [what3words API Docs][src10] |
| **Maidenhead Locator** | 6‑character grid `JO62QA` | Amateur radio, outdoor activities | [Maidenhead Locator System][src11] |

- **what3words free tier**: 10 requests / sec for autosuggest; higher tiers available.  
- **Libraries** for OLC are available in Python, JavaScript, etc. (no official endpoint needed).

**Sources**: [RFC 5870][src7] • [OSM Wiki: Geo URI scheme][src12] • [Open Location Code Spec][src9] • [what3words API Docs][src10] • [Maidenhead Locator System][src11]

---

## 4. Accessibility (Wheelchair) Routing

### 4.1 OSM Tags for Wheelchair Accessibility  

| Tag | Meaning | Example |
|-----|---------|---------|
| `wheelchair` | General accessibility | `yes` / `no` / `limited` |
| `wheelchair:description` | Textual description (e.g., “ramp”, “eurokey”) | `ramp` |
| `smoothness` | Surface smoothness | `good`, `bad`, `very_bad` |
| `surface` | Surface material | `asphalt`, `cobblestone`, `grass` |
| `width` | Minimum width (meters) | `1.5m` |
| `incline` | Gradient (percent or angle) | `5%` |
| `kerb` | Curb height | `lowered`, `raised` |

**Example OSM XML**

```xml
<way id="12345">
  <tag k="highway" v="footway"/>
  <tag k="wheelchair" v="yes"/>
  <tag k="smoothness" v="good"/>
  <tag k="width" v="2m"/>
</way>
```

**Sources**: [OSM Wiki: Key:wheelchair][src13] • [OSM Wiki: Wheelchair routing][src14]

### 4.2 Open‑Source Routing Engines

| Engine | Wheelchair Profile | Request Example | Notes |
|--------|-------------------|----------------|-------|
| **OpenRouteService (ORS)** | `profile=wheelchair` | `POST https://api.openrouteservice.org/v2/directions/wheelchair`<br>Headers: `Authorization: YOUR_API_KEY`, `Content-Type: application/json`<br>Body: `{"coordinates":[[8.681495,49.41461],[8.687872,49.420318]]}` | Considers incline, surface, curb, width |
| **Valhalla** | Use `costing=pedestrian` with custom `wheelchair` options | `POST https://valhalla.example.com/route` (payload includes `"costing":"pedestrian"` and wheelchair‑specific parameters) | No dedicated wheelchair profile; requires custom costing options |

**Sources**: [ORS Wheelchair Routing Help][src15] • Valhalla docs (implicit from open‑source repo)

---

## 5. Deep‑Link / Action Templates

| Action | URL Template | Required Params | Source |
|--------|--------------|----------------|--------|
| Search parking (Parkopedia) | `https://api.parkopedia.com/api/parking/search?lat={lat}&lon={lon}&radius={km}&key={api_key}` | `lat`, `lon`, optional `radius`, `api_key` | [Parkopedia API][src3] |
| Parking availability (Parkopedia) | `https://api.parkopedia.com/api/parking/availability?parking_id={id}&key={api_key}` | `parking_id`, `api_key` | [Parkopedia API][src3] |
| German fuel prices (Tankerkönig) | `https://creativecommons.tankerkoenig.de/json/prices.php?ids={ids}&apikey={key}` | `ids` (comma‑sep), `apikey` | [Tankerkönig API][src5] |
| German station detail (Tankerkönig) | `https://creativecommons.tankerkoenig.de/json/detail.php?id={id}&apikey={key}` | `id`, `apikey` | [Tankerkönig API][src5] |
| French fuel prices (prix‑carburants) | `https://data.economie.gouv.fr/api/records/1.0/search/?dataset=prix-des-carburants-en-france-flux-instantane-v2&...` | Opendata query params (e.g., `q`, `rows`) | [prix‑carburants Open Data][src6] |
| Geo URI (RFC 5870) | `geo:{lat},{lon}{;u={uncertainty}}` | `lat`, `lon`, optional `uncertainty` | [RFC 5870][src7] |
| Open Location Code | `https://plus.codes/{plus_code}` (web view) | `plus_code` | [Open Location Code Spec][src9] |
| what3words autosuggest | `https://api.what3words.com/v3/autosuggest?input={text}&key={api_key}` | `input`, `api_key` | [what3words API Docs][src10] |
| ORS wheelchair routing | `https://api.openrouteservice.org/v2/directions/wheelchair` (POST) | JSON body with `coordinates`, header `Authorization` | [ORS Wheelchair Routing Help][src15] |
| Valhalla wheelchair‑style route | `https://valhalla.example.com/route` (POST) | JSON with `costing":"pedestrian"` and wheelchair options | ⚠️ UNVERIFIED (derived from Valhalla docs, not explicitly cited) |

---

## 6. Feature Inventory Summary

| Feature | Open Data Source(s) | Open API / Standard | Licensing / Limits | Source |
|---------|---------------------|---------------------|--------------------|--------|
| Parking (basic) | OSM `amenity=parking` | Overpass API, Parkopedia REST | OSM ODbL; Parkopedia proprietary | [src1] • [src3] |
| Parking (real‑time) | – | Parkopedia `/search`, `/availability` | Proprietary (commercial) | [src3] |
| Fuel Prices (DE) | Tankerkönig | `prices.php`, `detail.php` | CC BY 4.0, free API key | [src5] |
| Fuel Prices (FR) | prix‑carburants.gouv.fr | Opendata portal / API console | Open License (Etalab), no key | [src6] |
| ETA / Live Location | – | geo: URI (RFC 5870), OLC, what3words, Maidenhead | Open standards; what3words free tier 10 req/s | [src7] • [src9] • [src10] |
| Wheelchair Routing | OSM wheelchair tags | ORS `profile=wheelchair`, Valhalla `costing=pedestrian` | OSM ODbL; ORS/Valhalla open source | [src13] • [src15] |
| Speed Cameras (reference only) | OSM `highway=speed_camera` | SCDB.info (paid) | OSM ODbL; SCDB CC BY‑NC 4.0 (personal) | [src16] |

---

## Sources

[src1]: https://wiki.openstreetmap.org/wiki/Tag:amenity=parking  
[src2]: https://wiki.openstreetmap.org/wiki/Parking  
[src3]: https://business.parkopedia.com/parking-data  
[src4]: https://api.parkopedia.com/faq/  
[src5]: https://creativecommons.tankerkoenig.de/  
[src6]: https://www.prix-carburants.gouv.fr/rubrique/opendata/  
[src7]: https://datatracker.ietf.org/doc/rfc5870/  
[src8]: https://en.wikipedia.org/wiki/Geo_URI_scheme  
[src9]: https://github.com/google/open-location-code/blob/main/Documentation/Specification/specification.md  
[src10]: https://developer.what3words.com/public-api/docs  
[src11]: https://en.wikipedia.org/wiki/Maidenhead_Locator_System  
[src12]: https://wiki.openstreetmap.org/wiki/Geo_URI_scheme  
[src13]: https://wiki.openstreetmap.org/wiki/Key:wheelchair  
[src14]: https://wiki.openstreetmap.org/wiki/Wheelchair_routing  
[src15]: https://wiki.openstreetmap.org/wiki/ORS_Wheelchair_Routing_Help  
[src16]: https://www.scdb.info/en/  

*(All URLs are listed in the order they appear in the tables above.)*
