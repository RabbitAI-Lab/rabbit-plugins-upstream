# travel-accommodation-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**24 endpoints across 4 platform group(s).**

## Airbnb (7)

### `airbnb_host`

- **HTTP:** `GET /airbnb/host/{id}`
- **What:** Get Airbnb host profile. Returns a normalized Airbnb public host profile — display name, Superhost and identity-verification status, location, bio, hosting tenure, total guest-review count, and total listing count.
- **Params:** `id` (string, **required**) — Host id (numeric)

### `airbnb_host_listings`

- **HTTP:** `GET /airbnb/host/{id}/listings`
- **What:** Get Airbnb host listings. Returns the listings an Airbnb host manages, paginated. Page 1 comes from the host profile; deeper pages page through the host's full portfolio.
- **Params:** `id` (string, **required**) — Host id (numeric); `page` (integer, optional) — 1-based page

### `airbnb_host_reviews`

- **HTTP:** `GET /airbnb/host/{id}/reviews`
- **What:** Get Airbnb host reviews. Returns reviews guests left for an Airbnb host, paginated, including the reviewer name and location.
- **Params:** `id` (string, **required**) — Host id (numeric); `page` (integer, optional) — 1-based page

### `airbnb_room`

- **HTTP:** `GET /airbnb/room/{id}`
- **What:** Get Airbnb room. Returns normalized Airbnb public room details.
- **Params:** `id` (string, **required**) — Room id

### `airbnb_room_calendar`

- **HTTP:** `GET /airbnb/room/{id}/calendar`
- **What:** Get Airbnb room calendar. Returns public calendar month hints parsed from Airbnb room bootstrap data.
- **Params:** `id` (string, **required**) — Room id

### `airbnb_room_reviews`

- **HTTP:** `GET /airbnb/room/{id}/reviews`
- **What:** Get Airbnb room reviews. Returns normalized Airbnb public review snippets.
- **Params:** `id` (string, **required**) — Room id; `page` (integer, optional) — 1-based page

### `airbnb_search`

- **HTTP:** `GET /airbnb/search`
- **What:** Search Airbnb stays. Returns normalized Airbnb public web search results.
- **Params:** `adults` (integer, optional) — Adult guests; `check_in` (string, optional) — Check-in date; `check_out` (string, optional) — Check-out date; `currency` (string, optional) — Currency for bounded map search; `location` (string, **required**) — Location; `ne_lat` (number, optional) — Northeast latitude for bounded map search; `ne_lng` (number, optional) — Northeast longitude for bounded map search; `page` (integer, optional) — 1-based page; `sw_lat` (number, optional) — Southwest latitude for bounded map search; `sw_lng` (number, optional) — Southwest longitude for bounded map search; `zoom` (integer, optional) — Map zoom for bounded map search

## Agoda (8)

### `agoda_activities_search`

- **HTTP:** `GET /agoda/activities/search`
- **What:** Search Agoda activities. Returns Agoda activities (tours, attractions, experiences) matching a free-text keyword and/or a city. When keyword is omitted, the resolved city's name is used instead to return a general listing of activities in that city. Callers may supply a known Agoda city id or a free-text city name for the city filter; when both are supplied city_id takes precedence. Credential-free public data from Agoda's own destination search.
- **Params:** `city` (string, optional) — Free-text city name, used directly as the search text when keyword is omitted, and to resolve a city id filter.; `city_id` (integer, optional) — Numeric Agoda city id to filter results to. Optional if keyword is supplied; city_id takes precedence over city when both are supplied.; `keyword` (string, optional) — Free-text activity search keyword. When omitted, the resolved city's name is used instead.

### `agoda_activity_detail`

- **HTTP:** `GET /agoda/activities/{activity_id}`
- **What:** Get Agoda activity detail. Returns full activity detail from Agoda: title, description, stated duration, categories, and content images. Credential-free public data from Agoda's own activity content source.
- **Params:** `activity_id` (string, **required**) — Numeric Agoda activity id, from a prior activities search call's activity_id field

### `agoda_flights_itinerary_amenities`

- **HTTP:** `POST /agoda/flights/itinerary-amenities`
- **What:** Get Agoda flight segment amenities. Returns real-content amenities (aircraft type, seat layout, meals, entertainment, wifi) for one or more flight segments. Copy the segments straight from a flight search response's own segment fields. Credential-free public data from Agoda's own flight content service.
- **Params:** `body` (object, **required**) — One or more flight segments to fetch amenities for
- **REST body:** Send the value of the MCP argument `body` directly as the JSON body; do not wrap it in a `body` property.

### `agoda_flights_search`

- **HTTP:** `GET /agoda/flights/search`
- **What:** Search Agoda one-way flights. Returns bookable one-way flight itineraries between two IATA airport codes for a departure date, including per-segment flight number, airline, times, layovers, aircraft type, and price. Resolve free-text city/airport names to codes first via the flight destination search endpoint. Credential-free public data from Agoda's own flight search.
- **Params:** `adults` (integer, optional) — Adult passengers (age 12+), defaults to 1; `cabin_class` (string, optional) — Cabin class, defaults to Economy; `children` (integer, optional) — Child passengers (age 2-11), defaults to 0; `departure_date` (string, **required**) — Departure date, YYYY-MM-DD; `destination` (string, **required**) — Destination IATA airport code; `infants` (integer, optional) — Infant passengers (under age 2), defaults to 0; `origin` (string, **required**) — Origin IATA airport code; `page` (integer, optional) — 1-indexed result page, defaults to 1

### `agoda_flights_search_locations`

- **HTTP:** `GET /agoda/flights/search-locations`
- **What:** Search Agoda flight destinations/airports. Resolves a free-text city or airport name into IATA airport codes for flight search, with each city's direct and nearby airports. Credential-free public data from Agoda's own flight destination search.
- **Params:** `keyword` (string, **required**) — Free-text city or airport name

### `agoda_homes_search`

- **HTTP:** `GET /agoda/homes/search`
- **What:** Search Agoda Homes & Apartments by city. Returns Homes & Apartments results for an Agoda city: full listing detail for every matching property whose accommodation type is Apartment, drawn from the same city search as hotel search and filtered to non-hotel accommodation types. Callers may supply a known Agoda city id or a free-text city name; when both are supplied city_id takes precedence. Credential-free public data from Agoda's own hotel/home search.
- **Params:** `city` (string, optional) — Free-text city name, resolved to a numeric city id via Agoda's own destination search. Ignored when city_id is also supplied.; `city_id` (integer, optional) — Numeric Agoda city id, e.g. 9395 for Bangkok. Either city_id or city is required; city_id takes precedence when both are supplied.; `limit` (integer, optional) — Candidate listings fetched per page before filtering to homes/apartments, defaults to 10, maximum 50; `page` (integer, optional) — 1-indexed result page over the underlying city search, defaults to 1

### `agoda_hotel_detail`

- **HTTP:** `GET /agoda/hotels/{property_id}`
- **What:** Get Agoda hotel detail. Returns full hotel detail from Agoda: identity (name, any former name), an accommodation type code, address (street address, postal code, city, country), guest rating, a main photo, room count, hotel chain id, a long and short description, and short-form policy statements (minimum age, adult/child definitions, extra-bed and additional-room booking policy). Credential-free public data from Agoda's own hotel content source.
- **Params:** `property_id` (string, **required**) — Numeric Agoda property id, from a prior search call's property_id field or the id embedded in an Agoda hotel URL

### `agoda_hotels_search`

- **HTTP:** `GET /agoda/hotels/search`
- **What:** Search Agoda hotels by city. Returns hotel search results for an Agoda city: the matching property ids for that city plus a direct link to each property's listing page. Callers may supply a known Agoda city id or a free-text city name; when both are supplied city_id takes precedence. Credential-free public data from Agoda's own hotel search.
- **Params:** `city` (string, optional) — Free-text city name, resolved to a numeric city id via Agoda's own destination search. Ignored when city_id is also supplied.; `city_id` (integer, optional) — Numeric Agoda city id, e.g. 9395 for Bangkok. Either city_id or city is required; city_id takes precedence when both are supplied.; `limit` (integer, optional) — Results per page, defaults to 10, maximum 50; `page` (integer, optional) — 1-indexed result page, defaults to 1

## Hotels.com (7)

### `hotels_autocomplete`

- **HTTP:** `GET /hotels/autocomplete`
- **What:** Get Hotels.com destination suggestions. Returns anonymous Hotels.com search-box suggestions for a partial destination or property name. Availability and prices are not included.
- **Params:** `q` (string, **required**) — Partial destination or property name

### `hotels_offers`

- **HTTP:** `POST /hotels/offers`
- **What:** Get Hotels.com room offers. Returns the public room/unit offer summaries shown for one Hotels.com property and date range, including room labels and non-transactional offer messages. Booking, checkout, payment, and reservation tokens are never returned. property_id is the numeric global property id from a Search response.
- **Params:** `request` (object, **required**) — Room offers request
- **REST body:** Send the value of the MCP argument `request` directly as the JSON body; do not wrap it in a `request` property.

### `hotels_property`

- **HTTP:** `POST /hotels/property`
- **What:** Get Hotels.com property details. Returns public static metadata from one canonical Hotels.com property page, including name, address, rating, images, and amenities. Date-bound availability, prices, booking, and review content are excluded.
- **Params:** `request` (object, **required**) — Canonical Hotels.com property URL
- **REST body:** Send the value of the MCP argument `request` directly as the JSON body; do not wrap it in a `request` property.

### `hotels_rates`

- **HTTP:** `POST /hotels/rates`
- **What:** Get Hotels.com rates for one property. Returns one Hotels.com property's date-bound rates and availability: the same normalized property card Search returns, with the live per-night and per-stay prices Hotels.com shows for the requested dates. property_id is the numeric global property id from a Search response's properties[].id; it is distinct from the legacy /ho<id>/ URL id.
- **Params:** `request` (object, **required**) — Rates request
- **REST body:** Send the value of the MCP argument `request` directly as the JSON body; do not wrap it in a `request` property.

### `hotels_reviews`

- **HTTP:** `POST /hotels/reviews`
- **What:** Get Hotels.com guest reviews. Returns one Hotels.com property's review overview: the overall rating (0-10) with its descriptive label, the per-category sub-ratings (cleanliness, service, amenities, and so on), and a bounded set of highlighted guest reviews with reviewer, date, rating label, text, and verified-stay flag. property_id is the numeric global property id from a Search response's properties[].id. This mirrors the property page's Guest reviews section; the full paginated review archive is not exposed.
- **Params:** `request` (object, **required**) — Reviews request
- **REST body:** Send the value of the MCP argument `request` directly as the JSON body; do not wrap it in a `request` property.

### `hotels_reviews_archive`

- **HTTP:** `POST /hotels/reviews/archive`
- **What:** List Hotels.com guest reviews. Returns one page of public guest reviews for a Hotels.com property, including reviewer, date, traveler type, rating label, title, and message. Use page and page_size to walk the archive; the response reports whether another page is available. property_id is the numeric global property id from a Search response's properties[].id. Booking, account, and private review data are not included.
- **Params:** `request` (object, **required**) — Review archive request
- **REST body:** Send the value of the MCP argument `request` directly as the JSON body; do not wrap it in a `request` property.

### `hotels_search`

- **HTTP:** `POST /hotels/search`
- **What:** Search Hotels.com hotels. Returns a page of date-bound Hotels.com hotel search results for either a free-text destination or a numeric Hotels.com region_id: normalized property cards with per-night and per-stay prices, review score and count, location, thumbnail, amenities, and promotional badges. Provide exactly one of query or region_id; region_id skips destination typeahead resolution. Prices are the live rates Hotels.com shows for the requested check-in and check-out dates.
- **Params:** `request` (object, **required**) — Search request
- **REST body:** Send the value of the MCP argument `request` directly as the JSON body; do not wrap it in a `request` property.

## Trip.com (2)

### `tripcom_hotel_detail`

- **HTTP:** `GET /tripcom/hotels/{id}`
- **What:** Get Trip.com hotel detail. Returns a normalized Trip.com hotel-detail page: identity (name, local name, star rating, city/province/country), location (address, zone, latitude/longitude, nearby-transport description), guest rating (overall score plus cleanliness/amenities/location/service breakdown), images, description, check-in/check-out and child policy summaries, and popular facilities. Credential-free public data sourced from Trip.com's own server-rendered hotel-detail page. Pricing is not included: Trip.com's detail page only returns per-night rates alongside check-in/check-out dates, which this endpoint does not take as input -- use the search endpoint for a city's current display prices.
- **Params:** `id` (string, **required**) — Trip.com hotel id, from a prior search call's hotel_id field; `slug` (string, optional) — Optional slug segment for a nicer canonical source URL (e.g. the district/city slug from a search result's url). Not required and not validated by Trip.com.

### `tripcom_hotels_search`

- **HTTP:** `GET /tripcom/hotels/search`
- **What:** Search Trip.com hotels by city. Returns Trip.com's own top-hotels page for a city: normalized hotel summaries (name, location, star rating, guest rating, review count, image, display price) for the hotels Trip.com features on that city's hotel-list page. Trip.com does not expose a credential-free free-text city search, so callers supply the exact city_slug and city_id pair from a known Trip.com hotel-list URL of the form https://www.trip.com/hotels/{city_slug}-hotels-list-{city_id}/. Credential-free public data sourced from Trip.com's own server-rendered hotel-list page.
- **Params:** `city_id` (string, **required**) — Trip.com numeric city id, the trailing number of a /hotels/{city_slug}-hotels-list-{city_id}/ URL; `city_slug` (string, **required**) — Trip.com city slug, the text segment of a /hotels/{city_slug}-hotels-list-{city_id}/ URL
