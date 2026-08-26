# real-estate-autos-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**20 endpoints across 5 platform group(s).**

## CarMax (7)

### `carmax_search`

- **HTTP:** `GET /carmax/search`
- **What:** Search CarMax vehicle listings. Searches CarMax for used car listings, returning normalized vehicle summaries (make, model, trim, year, mileage, colors, engine, fuel economy, pricing, store, images), available search facets with live counts, and the total matching count. Credential-free public data sourced from CarMax's own mobile-app search API.
- **Params:** `make` (string, optional) — CarMax make, e.g. honda, Toyota, BMW (case-insensitive); `max_mileage` (integer, optional) — Maximum odometer mileage; `max_price` (integer, optional) — Maximum price in US dollars; `max_year` (integer, optional) — Maximum model year; `min_price` (integer, optional) — Minimum price in US dollars; `min_year` (integer, optional) — Minimum model year; `model` (string, optional) — CarMax model, e.g. civic (case-insensitive). Does not require make; `page` (integer, optional) — 1-indexed result page, defaults to 1. CarMax returns 48 results per page; `sort` (string, optional) — Sort order: bestmatch, distance-asc, price-asc, price-desc, mileage-asc, mileage-desc, year-desc, year-asc, newarrival. Defaults to bestmatch; `zip` (string, optional) — 5-digit US ZIP code to bias results toward CarMax's nearest store

### `carmax_search_suggestions`

- **HTTP:** `GET /carmax/search/suggestions`
- **What:** Get CarMax search autocomplete suggestions. Returns autocomplete suggestions for a partial search term (make/model/trim), typo-tolerant by default. Credential-free public data sourced from CarMax's own mobile-app API.
- **Params:** `exact_match` (boolean, optional) — Disable fuzzy/typo-tolerant matching -- require an exact prefix match. Defaults to false; `search` (string, **required**) — Free-text partial search term to get autocomplete suggestions for

### `carmax_shop_by_brand`

- **HTTP:** `GET /carmax/shop-by-brand`
- **What:** Get CarMax's "shop by brand" make taxonomy. Returns CarMax's full make taxonomy for browsing by brand: every make, a display image, and CarMax's own display order. Credential-free public data sourced from CarMax's own mobile-app API.
- **Params:** _none_

### `carmax_store`

- **HTTP:** `GET /carmax/store/{id}`
- **What:** Get CarMax store (physical location) detail. Returns a normalized CarMax store: name, full address, phone numbers, coordinates, opening hours, and store-type flags (car buying center, microstore). Credential-free public data sourced from CarMax's own server-rendered store page.
- **Params:** `id` (string, **required**) — CarMax store id, the numeric path segment of a /stores/{id} URL

### `carmax_stores`

- **HTTP:** `GET /carmax/stores`
- **What:** Search CarMax store (physical location) locations. Searches CarMax's physical store locations by ZIP code or free-text keyword, returning normalized stores with full address, every published phone number, opening hours, and (for a ZIP-based search) live driving distance in miles. Credential-free public data sourced from CarMax's own mobile-app store-locator API.
- **Params:** `keyword` (string, optional) — Free-text match against store name or city; `take` (integer, optional) — Maximum number of stores to return, defaults to 10, capped at 300; `zip` (string, optional) — 5-digit US ZIP code to search near. Triggers a live geo-distance sort. Provide this or keyword; zip takes precedence if both are given

### `carmax_vehicle`

- **HTTP:** `GET /carmax/vehicle/{stock_number}`
- **What:** Get CarMax vehicle listing detail. Returns a normalized CarMax vehicle listing: full vehicle spec (make, model, trim, mileage, colors, engine, transmission, fuel economy, pricing), equipment features, labeled specifications, warranty coverage, accident/owner history, and CarMax's return guarantee terms. Credential-free public data sourced primarily from CarMax's own mobile-app API, backfilled with the website's server-rendered page for accident/owner history and warranty terms the mobile API doesn't expose.
- **Params:** `stock_number` (string, **required**) — CarMax stock number, the numeric path segment of a /car/{stock_number} URL; `store_id` (string, optional) — Optional CarMax store id for pricing/transfer-fee display context. Defaults to a fixed CarMax store when omitted

### `carmax_vehicle_recommendations`

- **HTTP:** `GET /carmax/vehicle/{stock_number}/recommendations`
- **What:** Get CarMax "similar vehicles" recommendations for a listing. Returns CarMax's own similar-vehicle recommendations for a listing: stock number, description, display mileage/price, store location, and image, for vehicles CarMax considers comparable. An empty list is a normal result, not an error. Credential-free public data sourced from CarMax's own mobile-app API.
- **Params:** `stock_number` (string, **required**) — CarMax stock number to find similar vehicles for, the numeric path segment of a /car/{stock_number} URL; `store_id` (string, **required**) — CarMax store id used as the recommendation's location context. See any search/vehicle/store response's store id field

## Redfin (5)

### `redfin_estimate`

- **HTTP:** `GET /redfin/estimate`
- **What:** Get Redfin Estimate. Returns the Redfin Estimate for a property, including the current estimate, property facts, and the monthly estimate history with city/county/postal comparatives. Faithful pass-through of Redfin's public avm + avmHistoricalData resources.
- **Params:** `property_id` (string, **required**) — Redfin property id

### `redfin_property`

- **HTTP:** `GET /redfin/property`
- **What:** Get Redfin property. Returns normalized Redfin public property details. Provide a listing url, or a property_id (optionally with listing_id) to use Redfin's public stingray detail API.
- **Params:** `listing_id` (string, optional) — Redfin listing id, improves completeness with property_id; `property_id` (string, optional) — Redfin property id, used when url is not provided; `url` (string, optional) — Redfin listing URL (primary key)

### `redfin_region_trends`

- **HTTP:** `GET /redfin/region-trends`
- **What:** Get Redfin region market trends. Returns Redfin's aggregate market trends for a region (median list/sale price, sale-to-list, offers, days on market, inventory, year-over-year). Faithful pass-through of Redfin's public aggregate-trends resource.
- **Params:** `region_id` (integer, **required**) — Redfin region id from autocomplete; `region_type` (integer, optional) — Redfin region type from autocomplete (defaults to 6, city)

### `redfin_search`

- **HTTP:** `GET /redfin/search`
- **What:** Search Redfin listings. Returns normalized Redfin public listing search results from Redfin's credential-free region CSV endpoint. Pass region_id/region_type from autocomplete to skip location resolution.
- **Params:** `location` (string, optional) — Display location; resolved via autocomplete when region_id is omitted; `max_price` (integer, optional) — Maximum price filter; `min_baths` (number, optional) — Minimum bathrooms filter; `min_beds` (integer, optional) — Minimum bedrooms filter; `min_price` (integer, optional) — Minimum price filter; `page` (integer, optional) — 1-based page; `region_id` (integer, optional) — Redfin region id from autocomplete; `region_type` (integer, optional) — Redfin region type from autocomplete (defaults to 6, city); `status` (string, optional) — Listing status: for_sale or sold

### `redfin_similar`

- **HTTP:** `GET /redfin/similar`
- **What:** Get Redfin comparable listings. Returns Redfin's comparable ("similar") listings for a property as normalized listing rows. Faithful pass-through of Redfin's public similars resource.
- **Params:** `property_id` (string, **required**) — Redfin property id

## Autotrader (3)

### `autotrader_dealer`

- **HTTP:** `GET /autotrader/dealer/{id}`
- **What:** Get Autotrader dealer profile. Returns a normalized Autotrader dealer profile (name, phone, address, rating, website) plus a first page of the dealer's own current inventory as normalized vehicle summaries and the dealer's total listing count. Credential-free public data sourced from Autotrader's own server-rendered dealer profile page.
- **Params:** `id` (string, **required**) — Autotrader dealer/owner id, the numeric path segment of a /car-dealers/{id} URL

### `autotrader_search`

- **HTTP:** `GET /autotrader/search`
- **What:** Search Autotrader vehicle listings. Searches Autotrader for new and used car listings, returning normalized vehicle summaries (make, model, trim, year, mileage, pricing, images) plus the total matching count. Credential-free public data sourced from Autotrader's own server-rendered search page.
- **Params:** `body_style` (string, optional) — Body style. Allowed values: convertible, coupe, hatchback, sedan, suv, truck, van, wagon; `condition` (string, optional) — Listing condition. Allowed values: new, used, certified, 3p_cert; `make` (string, optional) — Autotrader make code, e.g. TOYOTA, HONDA, BMW; `max_mileage` (integer, optional) — Maximum odometer mileage; `max_price` (integer, optional) — Maximum price in US dollars; `max_year` (integer, optional) — Maximum model year; `min_price` (integer, optional) — Minimum price in US dollars; `min_year` (integer, optional) — Minimum model year; `model` (string, optional) — Autotrader model code, e.g. CAMRY. Requires make; `page` (integer, optional) — 1-indexed result page, defaults to 1. Autotrader returns 24 results per page; `query` (string, optional) — Free-text keyword search; `radius` (integer, optional) — Search radius in miles around zip; `seller_type` (string, optional) — Seller type. Allowed values: dealer, private; `trim` (string, optional) — Autotrader trim code. Requires make and model; `zip` (string, optional) — 5-digit US ZIP code to search around

### `autotrader_vehicle`

- **HTTP:** `GET /autotrader/vehicle/{id}`
- **What:** Get Autotrader vehicle listing detail. Returns a normalized Autotrader vehicle listing: full vehicle spec (make, model, trim, mileage, colors, transmission, fuel type, engine, images, pricing), the full listing description, and seller detail (dealership or private seller). Credential-free public data sourced from Autotrader's own server-rendered vehicle detail page.
- **Params:** `id` (string, **required**) — Autotrader listing id, the numeric path segment of a /cars-for-sale/vehicle/{id} URL

## Zillow (3)

### `zillow_autocomplete`

- **HTTP:** `GET /zillow/autocomplete`
- **What:** Autocomplete Zillow locations. Returns normalized Zillow public web autocomplete candidates. Semantic candidates may include region_id/region_type compatibility aliases plus region_ids/region_types arrays; prefer complete bounds metadata for Zillow search when present.
- **Params:** `limit` (integer, optional) — Maximum results, clamped to 20; `query` (string, **required**) — Location query; `status` (string, optional) — Search context. Allowed values: for_sale (aliases sale, for-sale), for_rent (aliases rent, for-rent), sold

### `zillow_property`

- **HTTP:** `GET /zillow/property/{zpid}`
- **What:** Get Zillow property. Returns normalized Zillow public property details using Zillow's public persisted GraphQL property payload, including optional typed sections for address parts, listing attribution, pricing, history, media, facts, schools, and nearby homes when present.
- **Params:** `zpid` (string, **required**) — Zillow property id

### `zillow_search`

- **HTTP:** `GET /zillow/search`
- **What:** Search Zillow listings. Returns normalized Zillow public listing search results. Callers must pass complete map bounds from autocomplete when available, or a region id fallback.
- **Params:** `east` (number, optional) — Map east bound from autocomplete; `location` (string, **required**) — Display location; `north` (number, optional) — Map north bound from autocomplete; `page` (integer, optional) — 1-based page; `region_id` (integer, optional) — Zillow region id from autocomplete, used when complete bounds are not provided; `region_type` (integer, optional) — Zillow region type from autocomplete, used with region_id fallback; `south` (number, optional) — Map south bound from autocomplete; `status` (string, optional) — Search context. Allowed values: for_sale (aliases sale, for-sale), for_rent (aliases rent, for-rent), sold; `west` (number, optional) — Map west bound from autocomplete

## Cars.com (2)

### `carsdotcom_search`

- **HTTP:** `GET /carsdotcom/search`
- **What:** Search Cars.com vehicle listings. Searches Cars.com for new and used car listings, returning normalized vehicle summaries (make, model, trim, year, mileage, exterior color, drivetrain, fuel type, pricing, seller, images) plus the total matching count. Credential-free public data sourced directly from Cars.com's own public search API.
- **Params:** `page` (integer, optional) — 1-indexed result page, defaults to 1. Cars.com returns 24 results per page; `radius` (integer, optional) — Search radius in miles around zip; `stock_type` (string, optional) — Listing condition. Allowed values: new, used, cpo, all; `zip` (string, optional) — 5-digit US ZIP code to search around

### `carsdotcom_vehicle`

- **HTTP:** `GET /carsdotcom/vehicle/{listing_id}`
- **What:** Get Cars.com vehicle listing detail. Returns a normalized Cars.com vehicle listing: full vehicle spec (make, model, trim, mileage, colors, engine, transmission, fuel economy, a key-specs table), Cars.com's own deal-fairness rating and predicted fair price, categorized equipment features, an AutoCheck-derived vehicle history report, Cars.com's own price-change history, the seller's notes, dealer detail (name, rating, address, website, phones, hours) or private-seller detail for a for-sale-by-owner listing, and certified-pre-owned/manufacturer-program detail when applicable. Credential-free public data sourced directly from Cars.com's own public GraphQL API.
- **Params:** `listing_id` (string, **required**) — Cars.com listing id (a UUID), the path segment of a /vehicledetail/{listing_id}/ URL
