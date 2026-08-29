# ebay-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**10 endpoints across 1 platform group(s).**

## eBay (10)

### `ebay_item`

- **HTTP:** `GET /ebay/item/{item_id}`
- **What:** Get eBay item details. Returns normalized details for a public eBay item listing.
- **Params:** `item_id` (string, **required**) — eBay item ID

### `ebay_live_stream`

- **HTTP:** `GET /ebay/live/streams/{id}`
- **What:** Get an eBay Live stream. Returns normalized detail for a single eBay Live stream/event, including each host's feedback summary for the last 365 days.
- **Params:** `id` (string, **required**) — eBay Live stream/event id

### `ebay_live_stream_items`

- **HTTP:** `GET /ebay/live/streams/{id}/items`
- **What:** List an eBay Live stream's featured items. Returns the currently featured/auction items for an eBay Live stream, including live bidding state.
- **Params:** `id` (string, **required**) — eBay Live stream/event id

### `ebay_live_streams`

- **HTTP:** `GET /ebay/live/streams`
- **What:** List eBay Live streams. Returns currently live and upcoming eBay Live streams for a category channel.
- **Params:** `category` (string, optional) — eBay Live category channel, defaults to explore; `request_number` (integer, optional) — Pagination cursor from a previous response's next_request_number, defaults to 0; `session_id` (string, optional) — Pagination session id from a previous response's session_id

### `ebay_live_streams_batch`

- **HTTP:** `GET /ebay/live/streams/batch`
- **What:** Get multiple eBay Live streams. Returns normalized summaries for multiple eBay Live streams/events in one call, up to 9 ids per request.
- **Params:** `ids` (string, **required**) — One or more eBay Live stream/event ids, up to 9. Comma-separated or repeated query values are both accepted.

### `ebay_search`

- **HTTP:** `POST /ebay/search`
- **What:** Search eBay listings. Returns normalized eBay search results.
- **Params:** `option` (object, **required**) — eBay search payload

### `ebay_seller`

- **HTTP:** `GET /ebay/seller/{seller}`
- **What:** Get eBay seller profile. Returns normalized details for a public eBay seller profile.
- **Params:** `seller` (string, **required**) — eBay seller username

### `ebay_seller_about`

- **HTTP:** `GET /ebay/seller/{seller}/about`
- **What:** Get eBay seller about details. Returns normalized seller about information from the public eBay store about tab, including seller stats, top-rated status, optional location/member-since fields, and cleaned store categories.
- **Params:** `seller` (string, **required**) — eBay seller username

### `ebay_seller_feedback`

- **HTTP:** `GET /ebay/seller/{seller}/feedback`
- **What:** Get eBay seller feedback. Returns normalized seller feedback summary, detailed ratings, and recent review cards from the public eBay seller feedback tab.
- **Params:** `page` (integer, optional) — Feedback page number; `per_page` (integer, optional) — Reviews per page; `seller` (string, **required**) — eBay seller username

### `ebay_seller_shop`

- **HTTP:** `GET /ebay/seller/{seller}/shop`
- **What:** Get eBay seller shop listings. Returns normalized listings from the public eBay seller shop tab, with pagination backed by the store odtRefresh response.
- **Params:** `page` (integer, optional) — Shop page number; `seller` (string, **required**) — eBay seller username
