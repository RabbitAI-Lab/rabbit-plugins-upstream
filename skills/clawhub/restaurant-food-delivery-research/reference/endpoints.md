# restaurant-food-delivery-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**35 endpoints across 5 platform group(s).**

## DoorDash (12)

### `doordash_explore`

- **HTTP:** `GET /doordash/explore`
- **What:** Get DoorDash nearby stores explore feed. Returns DoorDash's location-based "nearby stores" browse feed from the Android mobile guest experience. Unlike search or autocomplete, no search query is required. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Consumer latitude; `longitude` (number, **required**) — Consumer longitude

### `doordash_feed`

- **HTTP:** `GET /doordash/feed`
- **What:** Get DoorDash store discovery feed. Returns nearby trending restaurants, grocery stores, and promotional offers from the Android mobile guest experience for a location. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Consumer latitude; `limit` (integer, optional) — Max stores to return; `longitude` (number, **required**) — Consumer longitude; `offset` (integer, optional) — Feed offset

### `doordash_search`

- **HTTP:** `GET /doordash/search`
- **What:** Search DoorDash pickup restaurants. Searches the Android mobile guest catalog for pickup restaurants near a location and supports optional result filters. No DoorDash account or caller-supplied token is required.
- **Params:** `asapOnly` (boolean, optional) — Keep only stores currently available ASAP; `dashPassOnly` (boolean, optional) — Keep only DashPass-eligible stores; `latitude` (number, **required**) — Consumer latitude; `longitude` (number, **required**) — Consumer longitude; `maxDistanceMiles` (number, optional) — Maximum displayed distance in miles, from 0 to 100; `pickupOnly` (boolean, optional) — Keep only pickup-enabled stores; `query` (string, **required**) — Restaurant, cuisine, or dish query; `tag` (string, optional) — Exact cuisine or store tag, case-insensitive

### `doordash_search_autocomplete`

- **HTTP:** `GET /doordash/search/autocomplete`
- **What:** Get DoorDash pickup search suggestions. Returns pickup restaurant matches from the Android mobile guest search experience near a location. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Consumer latitude; `longitude` (number, **required**) — Consumer longitude; `query` (string, **required**) — Partial restaurant, cuisine, or dish query

### `doordash_search_filters`

- **HTTP:** `GET /doordash/search/filters`
- **What:** Get DoorDash search filter options. Returns the cuisines and filter values supported by the Android mobile guest search experience for a location. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Consumer latitude; `longitude` (number, **required**) — Consumer longitude

### `doordash_search_items`

- **HTTP:** `GET /doordash/search/items`
- **What:** Search DoorDash dishes and items. Search for specific dishes or items across nearby merchants from the Android mobile guest experience. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Consumer latitude; `longitude` (number, **required**) — Consumer longitude; `query` (string, **required**) — Search text

### `doordash_store`

- **HTTP:** `GET /doordash/store/{store_id}`
- **What:** Get a DoorDash store. Returns location-aware DoorDash store metadata through the Android mobile guest flow. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Delivery latitude; `longitude` (number, **required**) — Delivery longitude; `store_id` (string, **required**) — Numeric DoorDash store ID

### `doordash_store_fulfillment`

- **HTTP:** `GET /doordash/store/{store_id}/fulfillment`
- **What:** Get DoorDash store fulfillment details. Returns store fulfillment methods, delivery fee info, and scheduling details from the Android mobile guest experience. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Delivery latitude; `longitude` (number, **required**) — Delivery longitude; `store_id` (string, **required**) — Numeric DoorDash store ID

### `doordash_store_info`

- **HTTP:** `GET /doordash/store/{store_id}/info`
- **What:** Get DoorDash store contact info. Returns a lightweight store info card (map coordinates, address, phone number) from the Android mobile guest experience. This is a distinct upstream contract from the full store endpoint and reliably includes address and coordinates. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Delivery latitude; `longitude` (number, **required**) — Delivery longitude; `store_id` (string, **required**) — Numeric DoorDash store ID

### `doordash_store_item`

- **HTTP:** `GET /doordash/store/{store_id}/item/{item_id}`
- **What:** Get DoorDash menu item details. Returns details for a specific menu item from the Android mobile guest experience. No DoorDash account or caller-supplied token is required.
- **Params:** `item_id` (string, **required**) — Menu item ID or name; `latitude` (number, **required**) — Delivery latitude; `longitude` (number, **required**) — Delivery longitude; `store_id` (string, **required**) — Numeric DoorDash store ID

### `doordash_store_menu`

- **HTTP:** `GET /doordash/store/{store_id}/menu`
- **What:** Get a DoorDash store menu. Returns the location-aware DoorDash mobile menu, grouped into sections with item names, descriptions, and displayed prices. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Delivery latitude; `longitude` (number, **required**) — Delivery longitude; `store_id` (string, **required**) — Numeric DoorDash store ID

### `doordash_store_reviews`

- **HTTP:** `GET /doordash/store/{store_id}/reviews`
- **What:** Get DoorDash store reviews. Returns store ratings and customer reviews from the Android mobile guest experience for a location. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Delivery latitude; `longitude` (number, **required**) — Delivery longitude; `store_id` (string, **required**) — Numeric DoorDash store ID

## Yelp (8)

### `yelp_business`

- **HTTP:** `GET /yelp/business/{id}`
- **What:** Get Yelp business detail. Looks up a single Yelp business by alias or encoded id via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id

### `yelp_business_menu`

- **HTTP:** `GET /yelp/business/{id}/menu`
- **What:** Get Yelp business menu. Fetches menu items for a Yelp business via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id

### `yelp_business_photos`

- **HTTP:** `GET /yelp/business/{id}/photos`
- **What:** Get Yelp business photos. Fetches the photo gallery for a Yelp business via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id; `limit` (integer, optional) — Max photos to return, 1-50; `offset` (integer, optional) — Pagination offset

### `yelp_business_review_highlights`

- **HTTP:** `GET /yelp/business/{id}/reviews/highlights`
- **What:** Get Yelp business review highlights. Fetches thematic review snippets (extracted talking points with a supporting quote) for a Yelp business via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id

### `yelp_business_reviews`

- **HTTP:** `GET /yelp/business/{id}/reviews`
- **What:** Get Yelp business reviews. Fetches reviews for a Yelp business via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id; `limit` (integer, optional) — Max reviews to return, 1-50; `offset` (integer, optional) — Pagination offset

### `yelp_business_reviews_search`

- **HTTP:** `GET /yelp/business/{id}/reviews/search`
- **What:** Search Yelp business reviews by keyword. Searches a Yelp business's reviews for a keyword via Yelp's real Android app backend, returning a highlighted excerpt per match. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id; `term` (string, **required**) — Keyword to search reviews for

### `yelp_geocode`

- **HTTP:** `GET /yelp/geocode`
- **What:** Geocode a free-form address. Resolves a free-form address into structured location data (coordinates, city, state, zip, county) via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller. Not business-scoped.
- **Params:** `address` (string, **required**) — Free-form address to geocode

### `yelp_search`

- **HTTP:** `GET /yelp/search`
- **What:** Search Yelp businesses. Searches Yelp's real Android app business-search backend for a term and location. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `limit` (integer, optional) — Max results to return, 1-50; `location` (string, **required**) — Neighborhood, city, state, or zip code; `offset` (integer, optional) — Pagination offset; `term` (string, **required**) — Search term

## UberEats (5)

### `ubereats_feed`

- **HTTP:** `GET /ubereats/feed`
- **What:** Browse UberEats location feed. Returns restaurants delivering to a specific location: name, rating, review count, delivery estimate, cuisine tags, and cover image. Credential-free public UberEats data.
- **Params:** `latitude` (number, **required**) — Delivery search center latitude; `limit` (integer, optional) — Number of restaurants to return, clamped to 50. Default 20; `longitude` (number, **required**) — Delivery search center longitude; `offset` (integer, optional) — Result offset for the location feed. Default 0

### `ubereats_search`

- **HTTP:** `GET /ubereats/search`
- **What:** Search UberEats restaurants. Returns restaurants delivering to a location: name, rating, review count, delivery estimate, cuisine tags, and image. Pass a keyword to search by name/cuisine/dish, or omit it to browse the general feed for that location. Credential-free public UberEats data.
- **Params:** `cursor` (string, optional) — Opaque pagination cursor from a previous keyword-search response; `latitude` (number, **required**) — Delivery search center latitude; `limit` (integer, optional) — Number of restaurants to return, clamped to 50. Default 20; `longitude` (number, **required**) — Delivery search center longitude; `offset` (integer, optional) — Result offset for the location feed (used only when query is omitted). Default 0; `query` (string, optional) — Keyword — restaurant name, cuisine, or dish

### `ubereats_store`

- **HTTP:** `GET /ubereats/store/{store_id}`
- **What:** Get an UberEats store. Returns a normalized UberEats store: address, phone, rating, cuisine tags, hours tagline, and the full menu (sections with items, descriptions, and prices). Credential-free public UberEats data.
- **Params:** `store_id` (string, **required**) — UberEats store UUID, as returned by the search endpoint's storeUuid field

### `ubereats_store_menu`

- **HTTP:** `GET /ubereats/store/{store_id}/menu`
- **What:** Get an UberEats store menu. Returns the full menu for an UberEats store: section titles, items, item descriptions, prices, and availability status. Credential-free public UberEats data.
- **Params:** `store_id` (string, **required**) — UberEats store UUID, as returned by the search endpoint's storeUuid field

### `ubereats_store_reviews`

- **HTTP:** `GET /ubereats/store/{store_id}/reviews`
- **What:** Get UberEats store reviews. Returns the reviews snapshot embedded in an UberEats store page: aggregate rating, review count, and a sample of recent reviews (reviewer name, text, and relative/absolute date). This is a single on-page snapshot, not a full paginated feed. A store with no written reviews returns an empty reviews list. Credential-free public UberEats data.
- **Params:** `store_id` (string, **required**) — UberEats store UUID, as returned by the search endpoint's storeUuid field

## Instacart (6)

### `instacart_departments`

- **HTTP:** `GET /instacart/departments`
- **What:** Get Instacart store department taxonomy. Returns a store's department/category taxonomy (Produce, Dairy & Eggs, Bakery, ...) two levels deep -- department and subcategory. Metadata only, does not return products. Public data sourced from Instacart's own storefront navigation.
- **Params:** `postal_code` (string, **required**) — Postal code to localize the taxonomy for; `shop_id` (string, **required**) — Store's opaque shop id, from GET /instacart/stores; `store_slug` (string, **required**) — Store's retailer slug, from GET /instacart/stores

### `instacart_item`

- **HTTP:** `GET /instacart/item`
- **What:** Get Instacart product detail at a store. Returns a single product's detail at a specific Instacart store: name, size, brand, image, current pricing (with any sale/offer badge), availability, stock level, dietary labels, and nutrition facts. Public data sourced from Instacart's own storefront pages.
- **Params:** `postal_code` (string, **required**) — Postal code to price/localize the lookup for; `product_id` (string, **required**) — Instacart's opaque product id; `retailer_location_id` (string, **required**) — Store's opaque retailer location id, from GET /instacart/stores; `shop_id` (string, **required**) — Store's opaque shop id, from GET /instacart/stores; `store_slug` (string, **required**) — Store's retailer slug, from GET /instacart/stores

### `instacart_search`

- **HTTP:** `GET /instacart/search`
- **What:** Search Instacart product terms at a store. Returns Instacart's own search-term autosuggestions for a keyword within one store -- the same suggestion list shown in the site's own search box dropdown. This is term-level (matching search phrases plus a representative thumbnail), not a paginated product-results list. Public data sourced from Instacart's own storefront search.
- **Params:** `q` (string, **required**) — Free-text search term; `shop_id` (string, **required**) — Store's opaque shop id, from GET /instacart/stores; `store_slug` (string, **required**) — Store's retailer slug, from GET /instacart/stores

### `instacart_search_nearby`

- **HTTP:** `GET /instacart/search-nearby`
- **What:** Search Instacart product terms near a postal code. Returns Instacart's own search-term autosuggestions for a keyword across every retailer serving a postal code at once, rather than one specific store. Public data sourced from Instacart's own cross-retailer search.
- **Params:** `postal_code` (string, **required**) — US postal/ZIP code to search near; `q` (string, **required**) — Free-text search term

### `instacart_stores`

- **HTTP:** `GET /instacart/stores`
- **What:** Find Instacart stores near a postal code. Finds Instacart retailer storefronts (grocery stores, warehouse clubs, and other partner retailers) serving a US postal code, each with the identifiers needed to look up its items and search suggestions. Public data sourced from Instacart's own store-discovery API.
- **Params:** `postal_code` (string, **required**) — US postal/ZIP code to search near

### `instacart_trending`

- **HTTP:** `GET /instacart/trending`
- **What:** Get Instacart trending search terms near a postal code. Returns Instacart's own popular/trending search terms across every retailer serving a postal code -- the same blank-state suggestions shown before a user types anything into the search box. Public data sourced from Instacart's own cross-retailer search.
- **Params:** `postal_code` (string, **required**) — US postal/ZIP code to search near

## OpenTable (4)

### `opentable_restaurant`

- **HTTP:** `GET /opentable/restaurant`
- **What:** Get an OpenTable restaurant's profile and live availability. Returns a restaurant's profile (location, cuisines, hours, price band, review summary) plus real-time bookable timeslots for the given date/time and party size. Credential-free.
- **Params:** `date_time` (string, optional) — Reservation date/time, RFC3339-minute local format; defaults to now; `party_size` (integer, optional) — Party size, default 2; `restaurant_id` (string, **required**) — OpenTable restaurant id

### `opentable_restaurant_menus`

- **HTTP:** `GET /opentable/restaurant/menus`
- **What:** Get an OpenTable restaurant's menus. Returns a restaurant's menus (sections, items, prices). Credential-free.
- **Params:** `restaurant_id` (string, **required**) — OpenTable restaurant id

### `opentable_restaurant_reviews`

- **HTTP:** `GET /opentable/restaurant/reviews`
- **What:** Get a page of an OpenTable restaurant's diner reviews. Returns a page of diner reviews (author, text, per-category ratings) for a restaurant. Credential-free.
- **Params:** `page` (integer, optional) — Page number, default 1; `restaurant_id` (string, **required**) — OpenTable restaurant id; `size` (integer, optional) — Reviews per page, default 20

### `opentable_search`

- **HTTP:** `GET /opentable/search`
- **What:** Search OpenTable restaurants near a location. Searches restaurants by free-text term (cuisine, name, neighborhood) near a latitude/longitude, for a given date/time and party size, including inline live availability per result. Credential-free.
- **Params:** `date_time` (string, optional) — Reservation date/time, RFC3339-minute local format; defaults to now; `latitude` (number, **required**) — Search center latitude; `longitude` (number, **required**) — Search center longitude; `party_size` (integer, optional) — Party size, default 2; `size` (integer, optional) — Max results, default 10; `term` (string, **required**) — Free-text search term
