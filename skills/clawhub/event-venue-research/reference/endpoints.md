# event-venue-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Only the endpoints used by this workflow. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**14 endpoints across 2 platform group(s).**

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

## TicketWeb (3)

### `ticketweb_event`

- **HTTP:** `GET /ticketweb/event`
- **What:** Get a TicketWeb event. Returns normalized details for one TicketWeb event: venue, dates, age restriction, delivery methods, and per-tier ticket pricing (base price, fee breakdown, and total) when tickets are on sale. `has_tickets` is false and `sections` is empty for a free/RSVP event with no paid tickets, a sold-out event, or an access-code-gated event -- TicketWeb's own data does not reliably distinguish these three cases at this level, so the response reports the shared observable state (no purchasable sections) rather than guessing which applies.
- **Params:** `id` (string, **required**) — Numeric TicketWeb event id

### `ticketweb_search`

- **HTTP:** `GET /ticketweb/search`
- **What:** Search TicketWeb events. Searches TicketWeb events by artist, event, or venue. A zero count with an empty events list is a valid no-results response. availability is one of `in_stock`, `sold_out`, `unknown` per event.
- **Params:** `page` (integer, optional) — One-based result page, 1-50; `q` (string, **required**) — Artist, event, or venue query

### `ticketweb_venue`

- **HTTP:** `GET /ticketweb/venue`
- **What:** Get a TicketWeb venue. Returns one TicketWeb venue's detail (name, address) plus one page of its upcoming events. A zero count with an empty events list on page 1 is a valid "no upcoming events" response.
- **Params:** `id` (string, **required**) — Numeric TicketWeb venue id; `page` (integer, optional) — One-based page of upcoming events, 1-50
