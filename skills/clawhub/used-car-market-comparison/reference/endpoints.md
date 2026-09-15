# used-car-market-comparison — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Only the endpoints used by this workflow. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**8 endpoints across 3 platform group(s).**

## CarMax (4)

### `carmax_search`

- **HTTP:** `GET /carmax/search`
- **What:** Search CarMax vehicle listings. Searches CarMax for used car listings, returning normalized vehicle summaries (make, model, trim, year, mileage, colors, engine, fuel economy, pricing, store, images), available search facets with live counts, and the total matching count. Credential-free public data sourced from CarMax's own mobile-app search API.
- **Params:** `make` (string, optional) — CarMax make, e.g. honda, Toyota, BMW (case-insensitive); `max_mileage` (integer, optional) — Maximum odometer mileage; `max_price` (integer, optional) — Maximum price in US dollars; `max_year` (integer, optional) — Maximum model year; `min_price` (integer, optional) — Minimum price in US dollars; `min_year` (integer, optional) — Minimum model year; `model` (string, optional) — CarMax model, e.g. civic (case-insensitive). Does not require make; `page` (integer, optional) — 1-indexed result page, defaults to 1. CarMax returns 48 results per page; `sort` (string, optional) — Sort order: bestmatch, distance-asc, price-asc, price-desc, mileage-asc, mileage-desc, year-desc, year-asc, newarrival. Defaults to bestmatch; `zip` (string, optional) — 5-digit US ZIP code to bias results toward CarMax's nearest store

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

## Autotrader (2)

### `autotrader_search`

- **HTTP:** `GET /autotrader/search`
- **What:** Search Autotrader vehicle listings. Searches Autotrader for new and used car listings, returning normalized vehicle summaries (make, model, trim, year, mileage, pricing, images) plus the total matching count. Credential-free public data sourced from Autotrader's own server-rendered search page.
- **Params:** `body_style` (string, optional) — Body style. Allowed values: convertible, coupe, hatchback, sedan, suv, truck, van, wagon; `condition` (string, optional) — Listing condition. Allowed values: new, used, certified, 3p_cert; `make` (string, optional) — Autotrader make code, e.g. TOYOTA, HONDA, BMW; `max_mileage` (integer, optional) — Maximum odometer mileage; `max_price` (integer, optional) — Maximum price in US dollars; `max_year` (integer, optional) — Maximum model year; `min_price` (integer, optional) — Minimum price in US dollars; `min_year` (integer, optional) — Minimum model year; `model` (string, optional) — Autotrader model code, e.g. CAMRY. Requires make; `page` (integer, optional) — 1-indexed result page, defaults to 1. Autotrader returns 24 results per page; `query` (string, optional) — Free-text keyword search; `radius` (integer, optional) — Search radius in miles around zip; `seller_type` (string, optional) — Seller type. Allowed values: dealer, private; `trim` (string, optional) — Autotrader trim code. Requires make and model; `zip` (string, optional) — 5-digit US ZIP code to search around

### `autotrader_vehicle`

- **HTTP:** `GET /autotrader/vehicle/{id}`
- **What:** Get Autotrader vehicle listing detail. Returns a normalized Autotrader vehicle listing: full vehicle spec (make, model, trim, mileage, colors, transmission, fuel type, engine, images, pricing), the full listing description, and seller detail (dealership or private seller). Credential-free public data sourced from Autotrader's own server-rendered vehicle detail page.
- **Params:** `id` (string, **required**) — Autotrader listing id, the numeric path segment of a /cars-for-sale/vehicle/{id} URL

## Cars.com (2)

### `carsdotcom_search`

- **HTTP:** `GET /carsdotcom/search`
- **What:** Search Cars.com vehicle listings. Searches Cars.com for new and used car listings, returning normalized vehicle summaries (make, model, trim, year, mileage, exterior color, drivetrain, fuel type, pricing, seller, images) plus the total matching count. Credential-free public data sourced directly from Cars.com's own public search API.
- **Params:** `page` (integer, optional) — 1-indexed result page, defaults to 1. Cars.com returns 24 results per page; `radius` (integer, optional) — Search radius in miles around zip; `stock_type` (string, optional) — Listing condition. Allowed values: new, used, cpo, all; `zip` (string, optional) — 5-digit US ZIP code to search around

### `carsdotcom_vehicle`

- **HTTP:** `GET /carsdotcom/vehicle/{listing_id}`
- **What:** Get Cars.com vehicle listing detail. Returns a normalized Cars.com vehicle listing: full vehicle spec (make, model, trim, mileage, colors, engine, transmission, fuel economy, a key-specs table), Cars.com's own deal-fairness rating and predicted fair price, categorized equipment features, an AutoCheck-derived vehicle history report, Cars.com's own price-change history, the seller's notes, dealer detail (name, rating, address, website, phones, hours) or private-seller detail for a for-sale-by-owner listing, and certified-pre-owned/manufacturer-program detail when applicable. Credential-free public data sourced directly from Cars.com's own public GraphQL API.
- **Params:** `listing_id` (string, **required**) — Cars.com listing id (a UUID), the path segment of a /vehicledetail/{listing_id}/ URL
