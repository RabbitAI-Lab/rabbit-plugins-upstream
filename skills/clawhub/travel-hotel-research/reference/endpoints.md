# travel-hotel-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**49 endpoints across 7 platform group(s).**

## Booking (8)

### `booking_attractions_detail`

- **HTTP:** `GET /booking-attractions/detail`
- **What:** Booking.com attraction detail. Returns a Booking.com attraction's detail page.
- **Params:** `slug` (string, **required**) — Attraction slug, from a prior attraction search result

### `booking_attractions_reviews`

- **HTTP:** `GET /booking-attractions/reviews`
- **What:** Booking.com attraction reviews. Returns normalized guest reviews for a Booking.com attraction.
- **Params:** `limit` (integer, optional) — Reviews per page, 1-50, default 10; `page` (integer, optional) — 1-based result page, default 1; `product_id` (string, **required**) — Attraction product id, from a prior attraction search result

### `booking_attractions_search`

- **HTTP:** `GET /booking-attractions/search`
- **What:** Search Booking.com attractions. Returns normalized Booking.com attractions/things-to-do search results for a destination and date range, with an optional category/subcategory filter and a discoverable category taxonomy.
- **Params:** `category` (string, optional) — Optional top-level category tagname filter, from a prior response's categories; `end_date` (string, optional) — Availability end date, YYYY-MM-DD, defaults to start_date; `limit` (integer, optional) — Results per page, 1-30, default 15; `page` (integer, optional) — 1-based result page, default 1; `query` (string, **required**) — Destination name or city; `start_date` (string, **required**) — Availability start date, YYYY-MM-DD; `subcategory` (string, optional) — Optional subcategory tagname filter, from a prior response's categories

### `booking_flights_autocomplete`

- **HTTP:** `GET /booking-flights/autocomplete`
- **What:** Booking.com flight autocomplete. Returns Booking.com flight-search location suggestions (airports/cities) for a query string.
- **Params:** `origin` (string, optional) — Optional origin location code, biases results by proximity; `origin_type` (string, optional) — Origin location type; `query` (string, **required**) — City or airport name/code to search; `type` (string, optional) — Location role, default to

### `booking_flights_search`

- **HTTP:** `GET /booking-flights/search`
- **What:** Search Booking.com flights. Returns normalized round-trip or one-way flight offers between two Booking.com flight-search locations.
- **Params:** `adults` (integer, optional) — Number of adults, 1-9, default 1; `cabin_class` (string, optional) — Cabin class, default ECONOMY; `children` (integer, optional) — Number of children, 0-9; `depart` (string, **required**) — Departure date, YYYY-MM-DD; `from` (string, **required**) — Origin location id, e.g. SGN.AIRPORT, from a prior autocomplete result; `from_country` (string, optional) — Origin country code; `return` (string, optional) — Return date, YYYY-MM-DD, required when type is ROUNDTRIP; `sort` (string, optional) — Result sort order, default BEST; `to` (string, **required**) — Destination location id, same composite format as from; `to_country` (string, optional) — Destination country code; `type` (string, optional) — Trip type, default ROUNDTRIP

### `booking_hotel_detail`

- **HTTP:** `GET /booking/hotel-detail`
- **What:** Booking.com hotel detail. Returns a Booking.com hotel's core detail page: rating, facilities, highlights, house rules, cover photos, and rooms with their own photos.
- **Params:** `hotel_id` (integer, **required**) — Booking.com hotel id, from a prior search's property id

### `booking_reviews`

- **HTTP:** `GET /booking/reviews`
- **What:** Booking.com hotel reviews. Returns normalized guest reviews for a Booking.com hotel, with an optional free-text search over review content.
- **Params:** `destination_id` (integer, optional) — Destination id (ufi), from a prior search response; `hotel_country_code` (string, **required**) — Hotel's country code, from a prior search response; `hotel_id` (integer, **required**) — Booking.com hotel id, from a prior search's property id; `hotel_score` (number, optional) — Hotel's overall review score; `limit` (integer, optional) — Reviews per page, 1-25, default 10; `page` (integer, optional) — 1-based result page, default 1; `search_text` (string, optional) — Optional free-text search over review content

### `booking_search`

- **HTTP:** `GET /booking/search`
- **What:** Search Booking.com hotels. Returns normalized Booking.com hotel search results for a destination and date range.
- **Params:** `adults` (integer, optional) — Number of adults, 1-9, default 2; `checkin` (string, **required**) — Check-in date, YYYY-MM-DD; `checkout` (string, **required**) — Check-out date, YYYY-MM-DD; `children` (integer, optional) — Number of children, 0-9; `page` (integer, optional) — 1-based result page, default 1; `query` (string, **required**) — Destination name or city; `rooms` (integer, optional) — Number of rooms, 1-8, default 1

## Expedia (7)

### `expedia_activities_search`

- **HTTP:** `POST /expedia/activities/search`
- **What:** Search Expedia activities. Returns normalized Expedia Things To Do (activities/tours) search results for a free-text destination and date range.
- **Params:** `option` (object, **required**) — Activity search payload

### `expedia_flights_search`

- **HTTP:** `POST /expedia/flights/search`
- **What:** Search Expedia flights. Returns normalized Expedia Flights search results (departing-leg offers) for an origin/destination IATA pair and date range.
- **Params:** `option` (object, **required**) — Flights search payload

### `expedia_locations_search`

- **HTTP:** `POST /expedia/locations/search`
- **What:** Search Expedia destinations. Returns normalized destination/property typeahead suggestions (cities, airports, neighborhoods, hotels) for a free-text term.
- **Params:** `option` (object, **required**) — Location search payload

### `expedia_properties_detail`

- **HTTP:** `POST /expedia/properties/detail`
- **What:** Expedia Stays property detail. Returns a hotel's detail summary (name, star rating, address/coordinates, top amenities) for a known property id.
- **Params:** `option` (object, **required**) — Property detail payload

### `expedia_properties_filters`

- **HTTP:** `POST /expedia/properties/filters`
- **What:** Expedia search filters. Returns the sort and filter facets (amenities, star rating, neighborhood, nightly price range, sort options) available for a Stays search.
- **Params:** `option` (object, **required**) — Property filters payload

### `expedia_properties_reviews`

- **HTTP:** `POST /expedia/properties/reviews`
- **What:** Expedia Stays property guest reviews. Returns a hotel's overall rating and highlighted/recent guest reviews (reviewer, date, rating, message) for a known property id.
- **Params:** `option` (object, **required**) — Property reviews payload

### `expedia_properties_search`

- **HTTP:** `POST /expedia/properties/search`
- **What:** Search Expedia Stays properties. Returns normalized Expedia Stays (hotel) search results for a free-text destination and date range.
- **Params:** `option` (object, **required**) — Property search payload

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

## TripAdvisor (6)

### `tripadvisor_autocomplete`

- **HTTP:** `GET /tripadvisor/autocomplete`
- **What:** Autocomplete TripAdvisor locations and places. Returns normalized TripAdvisor public typeahead candidates from the credential-free GraphQL endpoint.
- **Params:** `limit` (integer, optional) — Maximum results; `locale` (string, optional) — TripAdvisor locale; `q` (string, **required**) — Autocomplete query; `route_uid` (string, optional) — Optional captured route uid; `scope_geo_id` (integer, optional) — Optional scoped geo id; `search_session_id` (string, optional) — Optional captured search session id; `type` (string, optional) — Optional result type hint; `typeahead_id` (string, optional) — Optional captured typeahead id

### `tripadvisor_enums`

- **HTTP:** `GET /tripadvisor/enums`
- **What:** Get TripAdvisor enum metadata. Returns supported TripAdvisor enum values for place/listing filters, including locales, currencies, languages, listing types, filters, amenities, and category ids.
- **Params:** _none_

### `tripadvisor_hotels`

- **HTTP:** `GET /tripadvisor/hotels`
- **What:** Search TripAdvisor hotels. Returns normalized TripAdvisor hotel listing results from public credential-free GraphQL listing data.
- **Params:** `amenities` (array, optional) — Amenity filter ids; `class` (integer, optional) — Hotel class filter; `currency` (string, optional) — Currency code; `filter_id` (string, optional) — Optional filter id such as class or ufe; `geo_id` (integer, **required**) — TripAdvisor geo id; `limit` (integer, optional) — Maximum results; `offset` (integer, optional) — Zero-based result offset; `price_max` (integer, optional) — Maximum price filter; `price_min` (integer, optional) — Minimum price filter; `pricing_mode` (string, optional) — Pricing mode; `sort` (string, optional) — Sort value; `travelers_choice` (boolean, optional) — Filter Travelers' Choice properties; `travelers_choice_botb` (boolean, optional) — Filter Best of the Best properties

### `tripadvisor_place`

- **HTTP:** `GET /tripadvisor/place`
- **What:** Get TripAdvisor place. Returns a rich normalized TripAdvisor place profile. Destination and bookable tour/experience pages resolve through a faster dedicated lookup; everything else comes from public place HTML, using configured browser fallbacks when direct HTML is blocked.
- **Params:** `id` (string, optional) — TripAdvisor location id fallback; `url` (string, optional) — TripAdvisor place URL

### `tripadvisor_reviews`

- **HTTP:** `GET /tripadvisor/reviews`
- **What:** Get TripAdvisor reviews. Returns normalized TripAdvisor public reviews from credential-free GraphQL review data. Pass either id or url.
- **Params:** `do_machine_translation` (boolean, optional) — Enable upstream machine translation; `id` (string, optional) — TripAdvisor location id; `language` (string, optional) — Review language; `limit` (integer, optional) — Maximum reviews; `page` (integer, optional) — 1-based review page; `photos_per_review_limit` (integer, optional) — Maximum photos per review; `ratings` (array, optional) — Rating filters; `sort_by` (string, optional) — Review sort field; `sort_type` (string, optional) — Review sort type; `url` (string, optional) — TripAdvisor place URL

### `tripadvisor_search`

- **HTTP:** `GET /tripadvisor/search`
- **What:** Search TripAdvisor places. Returns normalized TripAdvisor place listings for hotels, restaurants, attractions, and supported attraction category types.
- **Params:** `amenities` (array, optional) — Hotel amenity filter ids; `class` (integer, optional) — Hotel class filter; `currency` (string, optional) — Currency code; `establishment_types` (array, optional) — Restaurant establishment type ids; `filter_id` (string, optional) — Optional hotel filter id; `geo_id` (integer, **required**) — TripAdvisor geo id; `limit` (integer, optional) — Maximum results; `locale` (string, optional) — TripAdvisor locale; `offset` (integer, optional) — Zero-based result offset; `online_options` (array, optional) — Restaurant online option ids; `price_max` (integer, optional) — Maximum hotel price filter; `price_min` (integer, optional) — Minimum hotel price filter; `pricing_mode` (string, optional) — Hotel pricing mode; `restaurant_date` (string, optional) — Restaurant availability date; `restaurant_guests` (integer, optional) — Restaurant guest count; `restaurant_time` (string, optional) — Restaurant availability time; `sort` (string, optional) — Sort value; `travelers_choice` (boolean, optional) — Filter Travelers' Choice hotels; `travelers_choice_botb` (boolean, optional) — Filter Best of the Best hotels; `type` (string, **required**) — Listing type

## Trip.com (2)

### `tripcom_hotel_detail`

- **HTTP:** `GET /tripcom/hotels/{id}`
- **What:** Get Trip.com hotel detail. Returns a normalized Trip.com hotel-detail page: identity (name, local name, star rating, city/province/country), location (address, zone, latitude/longitude, nearby-transport description), guest rating (overall score plus cleanliness/amenities/location/service breakdown), images, description, check-in/check-out and child policy summaries, and popular facilities. Credential-free public data sourced from Trip.com's own server-rendered hotel-detail page. Pricing is not included: Trip.com's detail page only returns per-night rates alongside check-in/check-out dates, which this endpoint does not take as input -- use the search endpoint for a city's current display prices.
- **Params:** `id` (string, **required**) — Trip.com hotel id, from a prior search call's hotel_id field; `slug` (string, optional) — Optional slug segment for a nicer canonical source URL (e.g. the district/city slug from a search result's url). Not required and not validated by Trip.com.

### `tripcom_hotels_search`

- **HTTP:** `GET /tripcom/hotels/search`
- **What:** Search Trip.com hotels by city. Returns Trip.com's own top-hotels page for a city: normalized hotel summaries (name, location, star rating, guest rating, review count, image, display price) for the hotels Trip.com features on that city's hotel-list page. Trip.com does not expose a credential-free free-text city search, so callers supply the exact city_slug and city_id pair from a known Trip.com hotel-list URL of the form https://www.trip.com/hotels/{city_slug}-hotels-list-{city_id}/. Credential-free public data sourced from Trip.com's own server-rendered hotel-list page.
- **Params:** `city_id` (string, **required**) — Trip.com numeric city id, the trailing number of a /hotels/{city_slug}-hotels-list-{city_id}/ URL; `city_slug` (string, **required**) — Trip.com city slug, the text segment of a /hotels/{city_slug}-hotels-list-{city_id}/ URL

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

## Ticketmaster (11)

### `ticketmaster_attraction`

- **HTTP:** `GET /ticketmaster/attraction`
- **What:** Get a Ticketmaster attraction. Returns normalized details for one Ticketmaster artist, team, or other attraction.
- **Params:** `id` (string, **required**) — Numeric Ticketmaster attraction id

### `ticketmaster_attraction_events`

- **HTTP:** `GET /ticketmaster/attraction-events`
- **What:** List an attraction's Ticketmaster events. Returns upcoming Ticketmaster events for one attraction. The sort enum accepts `relevance` and `date`.
- **Params:** `id` (string, **required**) — Numeric Ticketmaster attraction id; `page` (integer, optional) — Zero-based page (0-49); `sort` (string, optional) — Result order

### `ticketmaster_discover_categories`

- **HTTP:** `GET /ticketmaster/discover-categories`
- **What:** List Ticketmaster discover categories. Lists every current Concerts, Sports, Arts & Theater, and Family category with pagination. Section accepts `all`, `concerts`, `sports`, `arts-theater`, and `family`.
- **Params:** `page` (integer, optional) — One-based page; `per_page` (integer, optional) — Categories per page; `section` (string, optional) — Discover section

### `ticketmaster_discover_category_events`

- **HTTP:** `GET /ticketmaster/discover-category-events`
- **What:** List events in a Ticketmaster discover category. Returns a zero-based paginated event feed for any category returned by ticketmaster-discover-categories.
- **Params:** `category_id` (string, **required**) — Ticketmaster discover category id; `page` (integer, optional) — Zero-based page

### `ticketmaster_discover_cities`

- **HTTP:** `GET /ticketmaster/discover-cities`
- **What:** List Ticketmaster discover cities. Lists Ticketmaster city discovery destinations for a country with pagination.
- **Params:** `country` (string, optional) — Two-letter country code; `page` (integer, optional) — One-based page; `per_page` (integer, optional) — Cities per page

### `ticketmaster_discover_city_events`

- **HTTP:** `GET /ticketmaster/discover-city-events`
- **What:** List events in a Ticketmaster discover city. Returns a zero-based paginated event feed for a city slug returned by ticketmaster-discover-cities.
- **Params:** `city` (string, **required**) — Ticketmaster discover city slug; `country` (string, optional) — Two-letter country code matching the selected city; `page` (integer, optional) — Zero-based page

### `ticketmaster_event`

- **HTTP:** `GET /ticketmaster/event`
- **What:** Get a Ticketmaster event. Returns normalized details for one Ticketmaster event, including its venue, attractions, timing, availability flags, and classification.
- **Params:** `id` (string, **required**) — Ticketmaster event id

### `ticketmaster_search_events`

- **HTTP:** `GET /ticketmaster/search-events`
- **What:** Search Ticketmaster events. Searches Ticketmaster events by artist, event, team, or venue. A zero total with an empty events list is a valid no-results response. The sort enum accepts `relevance` and `date`.
- **Params:** `page` (integer, optional) — Zero-based page (0-49); `q` (string, **required**) — Artist, event, team, or venue query; `sort` (string, optional) — Result order

### `ticketmaster_suggest`

- **HTTP:** `GET /ticketmaster/suggest`
- **What:** Suggest Ticketmaster artists, events, and venues. Returns autocomplete suggestions for a partial query.
- **Params:** `q` (string, **required**) — Partial artist, event, team, or venue query

### `ticketmaster_venue`

- **HTTP:** `GET /ticketmaster/venue`
- **What:** Get a Ticketmaster venue. Returns normalized details and visitor information for one Ticketmaster venue.
- **Params:** `id` (string, **required**) — Numeric Ticketmaster venue id

### `ticketmaster_venue_events`

- **HTTP:** `GET /ticketmaster/venue-events`
- **What:** List a venue's Ticketmaster events. Returns upcoming Ticketmaster events at one venue. The sort enum accepts `relevance` and `date`.
- **Params:** `id` (string, **required**) — Numeric Ticketmaster venue id; `page` (integer, optional) — Zero-based page (0-49); `sort` (string, optional) — Result order
