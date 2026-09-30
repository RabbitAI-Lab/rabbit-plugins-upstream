---
name: scrapebadger
description: Web scraping platform — Twitter/X data, TikTok data, YouTube data, Vinted marketplace, Amazon marketplace, eBay marketplace, Realtor real-estate (realtor.com + realtor.ca), Apartments.com US rentals with unit-level pricing, Idealista real estate, Immobiliare.it real estate (Italy, Spain, Greece, Luxembourg), ChatGPT and Perplexity answers with cited sources and brand visibility (AEO/GEO), Baidu web/news/image search, DuckDuckGo privacy-first web/image/news/video search, and general web scraping API
version: 1.4.0
requires:
  env:
    - SCRAPEBADGER_API_KEY
tags:
  - twitter
  - tiktok
  - youtube
  - vinted
  - amazon
  - ebay
  - realtor
  - idealista
  - immobiliare
  - real-estate
  - chatgpt
  - perplexity
  - llm
  - aeo
  - brand-visibility
  - web-scraping
  - scraping
  - social-media
  - marketplace
  - e-commerce
  - api
  - data
  - apartments
  - walmart
  - rentals
  - baidu
  - duckduckgo
  - search-engine
---

# ScrapeBadger — Web Scraping Platform

ScrapeBadger provides REST APIs for three products. Use the `web_fetch` tool to call these endpoints.

## Authentication

Every request needs the `SCRAPEBADGER_API_KEY` environment variable.
Include it as an HTTP header: `X-API-Key: $SCRAPEBADGER_API_KEY`

## Base URL

```
https://scrapebadger.com
```

---

## Twitter/X API

### Users

**Get user profile by username:**
```
GET /v1/twitter/users/{username}/by_username
```

**Get user profile by numeric ID:**
```
GET /v1/twitter/users/{user_id}/by_id
```

**Batch get users by usernames (comma-separated):**
```
GET /v1/twitter/users/batch_by_usernames?usernames=elonmusk,OpenAI
```

**Batch get users by IDs (comma-separated):**
```
GET /v1/twitter/users/batch_by_ids?user_ids=44196397,1230113324
```

**Search users:**
```
GET /v1/twitter/users/search_users?query=AI+agents
```

**Get followers:**
```
GET /v1/twitter/users/{username}/followers
```

**Get following:**
```
GET /v1/twitter/users/{username}/followings
```

**Get mentions:**
```
GET /v1/twitter/users/{username}/mentions
```

**Get subscriptions:**
```
GET /v1/twitter/users/{user_id}/subscriptions
```

**Get user articles:**
```
GET /v1/twitter/users/{user_id}/articles
```

### Tweets

**Get tweet by ID:**
```
GET /v1/twitter/tweets/tweet/{tweet_id}
```

**Get multiple tweets by IDs:**
```
GET /v1/twitter/tweets/?tweets=123,456,789
```

**Advanced search:**
```
GET /v1/twitter/tweets/advanced_search?query=web+scraping&query_type=Latest&count=20
```

**Get replies:**
```
GET /v1/twitter/tweets/tweet/{tweet_id}/replies
```

**Get quotes:**
```
GET /v1/twitter/tweets/tweet/{tweet_id}/quotes
```

**Get retweeters:**
```
GET /v1/twitter/tweets/tweet/{tweet_id}/retweeters
```

**Get favoriters (likes):**
```
GET /v1/twitter/tweets/tweet/{tweet_id}/favoriters
```

**Get similar tweets:**
```
GET /v1/twitter/tweets/tweet/{tweet_id}/similar
```

**Get edit history:**
```
GET /v1/twitter/tweets/tweet/{tweet_id}/edit_history
```

**Get community notes:**
```
GET /v1/twitter/tweets/tweet/{tweet_id}/community_notes
```

**Get article:**
```
GET /v1/twitter/tweets/article/{article_id}
```

### Communities

**Get community:**
```
GET /v1/twitter/communities/{community_id}
```

**Get community tweets:**
```
GET /v1/twitter/communities/{community_id}/tweets
```

**Search communities:**
```
GET /v1/twitter/communities/search?query=AI
```

### Lists

**Get list details:**
```
GET /v1/twitter/lists/{list_id}/detail
```

**Get list tweets:**
```
GET /v1/twitter/lists/{list_id}/tweets
```

**Search tweets in list:**
```
GET /v1/twitter/lists/{list_id}/search_tweets?query=keyword
```

### Trends

**Get trending topics:**
```
GET /v1/twitter/trends/
```

**Get trends by location (WOEID):**
```
GET /v1/twitter/trends/place/{woeid}
```

### Geo

**Search places:**
```
GET /v1/twitter/geo/search?query=New+York
```

**Get place details:**
```
GET /v1/twitter/geo/places/{place_id}
```

### Spaces

**Get Space details:**
```
GET /v1/twitter/spaces/{space_id}
```

**Get broadcast details:**
```
GET /v1/twitter/spaces/broadcast/{broadcast_id}
```

---

## Vinted Marketplace API

**Search items:**
```
GET /v1/vinted/search?query=nike+shoes&market=fr&page=1&per_page=20
```
Optional params: `price_from`, `price_to`, `brand_ids`, `order`

**Get item details:**
```
GET /v1/vinted/items/{item_id}?market=fr
```

**Get user profile:**
```
GET /v1/vinted/users/{user_id}?market=fr
```

**Get user's items:**
```
GET /v1/vinted/users/{user_id}/items?market=fr
```

**Search brands:**
```
GET /v1/vinted/brands?keyword=nike&market=fr
```

**List colors:**
```
GET /v1/vinted/colors?market=fr
```

**List statuses:**
```
GET /v1/vinted/statuses?market=fr
```

**List markets:**
```
GET /v1/vinted/markets
```

Supported markets: fr, de, uk, us, es, it, nl, be, at, pl, pt, cz, lt, and more.

---

## Amazon Marketplace API

The `domain` parameter is the marketplace TLD (`com`, `co.uk`, `de`, `fr`, `co.jp`, …), default `com`. It also sets the geo-matched residential proxy for correct price/availability.

**Search the catalog:**
```
GET /v1/amazon/search?query=mechanical+keyboard&domain=com&page=1
```
Optional params: `sort_by`, `category`, `min_price`, `max_price`, `zip`

**Keyword autocomplete:**
```
GET /v1/amazon/autocomplete?query=mechan&domain=com
```

**Get product detail (PDP) by ASIN:**
```
GET /v1/amazon/products/{asin}?domain=com
```
Optional params: `zip`, `language`. Returns variants, buybox, badges, A+ content, frequently-bought-together, also-bought.

**Get all seller offers + buybox:**
```
GET /v1/amazon/products/{asin}/offers?domain=com
```

**Get product reviews (featured public subset):**
```
GET /v1/amazon/products/{asin}/reviews?domain=com&page=1
```
Optional params: `sort_by` (helpful|recent), `star`, `verified_only`, `media_only`

**Best Sellers:**
```
GET /v1/amazon/bestsellers?domain=com&category={node}&page=1
```

**New Releases:**
```
GET /v1/amazon/new-releases?domain=com&category={node}&page=1
```

**Deals (Today's / Lightning):**
```
GET /v1/amazon/deals?domain=com&category=...&page=1
```

**Browse a category by node:**
```
GET /v1/amazon/category?node={node}&domain=com&page=1
```
Optional param: `sort_by`

**Seller profile:**
```
GET /v1/amazon/sellers/{seller_id}?domain=com
```

**Seller storefront products:**
```
GET /v1/amazon/sellers/{seller_id}/products?domain=com&page=1
```

**Seller buyer feedback:**
```
GET /v1/amazon/sellers/{seller_id}/feedback?domain=com&page=1
```

**List markets (free):**
```
GET /v1/amazon/markets
```

**List categories (free):**
```
GET /v1/amazon/categories
```

Supported marketplaces (20): com, co.uk, de, fr, it, es, nl, se, pl, ca, com.mx, com.br, co.jp, in, com.au, sg, ae, sa, com.tr, eg.

---

## eBay Marketplace API

The `domain` parameter is the marketplace TLD (`com`, `co.uk`, `de`, `fr`, …), default `com`. It also sets the geo-matched residential proxy for correct price/availability. Aliases: `us`→`com`, `uk`/`gb`→`co.uk`, `au`→`com.au`.

**Search active listings:**
```
GET /v1/ebay/search?query=mechanical+keyboard&domain=com&page=1
```
Optional params: `category_id`, `per_page` (60|120|240), `sort_by` (best_match|ending_soonest|newly_listed|price_low_to_high|price_high_to_low), `condition` (new|open_box|refurbished|used|for_parts|graded|ungraded), `buying_format` (auction|buy_it_now|best_offer), `min_price`, `max_price`, `free_shipping`, `location` (domestic|worldwide). Returns results[] + facets + pagination.

**Search active listings by image (eBay's own visual search — 10 credits):**
```
POST /v1/ebay/search/by-image
{"image_url": "https://example.com/sneaker.jpg", "domain": "com"}
```
Send exactly one of `image_url` (a public http(s) URL we download) or `image_base64` (the image itself, JPEG or PNG, max 10 MB decoded; a `data:image/jpeg;base64,…` URL also works). Same optional filters as `/search` — `category_id`, `page`, `per_page`, `condition`, `buying_format`, `min_price`, `max_price`, `free_shipping`, `location`, `language` — and the same response shape, with `query: null`. There is no `sort_by`: eBay ignores sorting on a visual results page. An image eBay cannot read is a 400, never an empty result set.

**Search completed/sold listings (price research):**
```
GET /v1/ebay/completed?query=iphone+13+pro&domain=com&page=1
```
Optional params: `category_id`, `per_page`, `sort_by`, `condition` (incl. `graded`/`ungraded` for cards), `min_price`, `max_price`, `location` (`domestic` keeps only this marketplace's own country — foreign sales otherwise skew a national price series, and eBay shows their prices converted). Returns sold listings (sold=true).

**Keyword autocomplete:**
```
GET /v1/ebay/autocomplete?query=mechan&domain=com
```

**Get item detail by item ID:**
```
GET /v1/ebay/items/{item_id}?domain=com
```
Returns specifics, images, shipping, returns, and seller.

**Get item reviews:**
```
GET /v1/ebay/items/{item_id}/reviews?domain=com&page=1
```
Returns reviews[] + aggregate rating + histogram.

**Seller profile:**
```
GET /v1/ebay/sellers/{username}?domain=com
```

**Seller active listings:**
```
GET /v1/ebay/sellers/{username}/items?domain=com&page=1
```
Optional params: `query`, `per_page`.

**Seller buyer feedback:**
```
GET /v1/ebay/sellers/{username}/feedback?domain=com&page=1
```

**Browse a category by ID:**
```
GET /v1/ebay/categories/{category_id}/items?domain=com&page=1
```
Optional params: `per_page`, `sort_by`, `min_price`, `max_price`.

**List categories (free):**
```
GET /v1/ebay/categories
```

**List markets (free):**
```
GET /v1/ebay/markets
```

Supported marketplaces (18): com, co.uk, de, fr, it, es, com.au, ca, at, ch, be, ie, nl, pl, com.hk, com.sg, com.my, ph.

---

## Realtor Real-Estate API

Unified real-estate API over **realtor.com (US, USD)** and **realtor.ca (Canada, CAD)**. The `market` parameter (`us` or `ca`, default `us`) picks the portal and the geo-matched residential proxy. Rich datapoints: price + price/tax history, beds/baths/sqft/lot, coordinates, photos/videos/virtual tours, features/amenities, HOA, schools, open houses, agent/office/broker contacts, days-on-market, price-per-sqft.

**Search listings:**
```
GET /v1/realtor/search?location=Austin,+TX&market=us&status=for_sale
```
Required: `location` (free-text "Austin, TX" / ZIP / "Toronto, ON"; optional if a CA bbox is given). Optional params: `status` (for_sale|for_rent|sold|pending, default for_sale), `price_min`, `price_max`, `beds_min`, `baths_min`, `sqft_min`/`sqft_max` (US), `property_type` (US CSV: single_family,condos,townhomes,multi_family,mobile,land), `sort` (relevant|newest|price_low|price_high|photo_count), `page`, `limit` (1-200), `lat_min`/`lat_max`/`lng_min`/`lng_max` (CA bbox; realtor.ca caps ~600/box). Returns results[] of Property + total/count/page/total_pages.

**Get property detail by ID:**
```
GET /v1/realtor/properties/{property_id}?market=us
```
Returns a full PropertyDetail: price/tax history, schools, amenities, estimates, agents, open houses.

**Location autocomplete:**
```
GET /v1/realtor/autocomplete?query=austi&market=us
```
Optional param: `limit` (1-25, default 10). Returns suggestions[] (cities, ZIPs, neighborhoods, addresses).

**List markets (free):**
```
GET /v1/realtor/markets
```

Supported markets (2): us (realtor.com), ca (realtor.ca).
## Walmart API

Product, seller and store data from **walmart.com** (US only, USD, en-US). No Walmart account or developer key is needed. walmart.ca and walmart.com.mx run on different platforms and are not supported.

**Search products:**
```
GET /v1/walmart/search?query=laptop&sort=price_low&min_price=100&max_price=500
```
Required: `query`. Optional: `page` (1-10), `sort` (`best_match`|`best_seller`|`price_low`|`price_high`|`rating_high`|`new`), `min_price`, `max_price`, `facet` (Walmart's own syntax, e.g. `brand:HP`). Returns 40-60 organic products a page.

**Browse a category / deals:**
```
GET /v1/walmart/category?path=electronics/3944&page=2
GET /v1/walmart/deals
```
`path` comes from a `walmart.com/browse/...` or `/cp/...` URL. `/category` takes no `sort` — Walmart's browse pages silently ignore it, so it is not offered. `/deals` is the rollback/clearance feed; no other Walmart API exposes one.

**Product detail and reviews:**
```
GET /v1/walmart/products/5689919121
GET /v1/walmart/products/5689919121/reviews?page=1&sort=helpful
```
`item_id` is the numeric segment at the end of a `/ip/...` URL. The product carries UPC/GTIN, structured `specifications`, `variants`, per-method promised delivery dates, return policy, and a 10-review sample. The reviews endpoint adds the **full star histogram** (`one_star`..`five_star` counts and percentages) plus Walmart's own most-helpful positive and negative reviews. 10 reviews a page — Walmart's page size, not adjustable.

**Marketplace sellers:**
```
GET /v1/walmart/sellers/101040442
GET /v1/walmart/sellers/6907/products?query=camera
```
The seller id is the **numeric `catalog_seller_id`** found on a product — NOT the 32-character hex `seller_id`, which 404s. The profile endpoint has no product list because Walmart renders a storefront's grid client-side; `/products` goes through search with a `retailer_id` facet instead, which is why it **requires** a `query`.

**Stores:**
```
GET /v1/walmart/stores/100
```
Returns the store's address, geo, phone, weekly hours, and per-department services (pharmacy, deli, auto centre — each with its own phone and hours), plus ~30 nearby stores. Walmart has no working store-finder-by-ZIP page, so walk outward from a known store id.

**Autocomplete:**
```
GET /v1/walmart/autocomplete?query=lapt
```

**Gotchas that will bite you:**
- `total_results_reported` is Walmart's own claim (~14,000) and is **not reachable** — results dry up after page 10 (search) or 11 (browse), roughly 500 products a query. Use `has_more_pages`. To go deeper, segment by brand facet or price band rather than paging.
- Consecutive pages **overlap ~20%** because Walmart re-ranks between requests — deduplicate on `us_item_id`.
- Facets can be **applied** but not **enumerated**; Walmart renders the filter rail client-side.
- Searching by UPC does **not** work — Walmart returns zero results for a bare UPC, including a product's own.
- Prices are store-specific and Walmart resolves the store from the request IP. It cannot be pinned by a parameter, so every product returns a `location` block naming the store the prices actually came from.
- HTTP 422 is an anti-bot challenge: not billed, and retrying shortly succeeds.

Cost: 1 credit autocomplete; 5 credits search / category / deals / seller / seller products / store; 10 credits product detail and reviews. `markets` and `health` are free.

## DuckDuckGo API

Privacy-first search from **duckduckgo.com** — web, images, news and videos, plus autocomplete and Instant Answers. No DuckDuckGo account or API key is needed. Region is set with the `kl`/`l` code (`us-en`, `uk-en`, `de-de`, … `wt-wt` = all regions); `safesearch` is `on` | `moderate` | `off`.

**Web search:**
```
GET /v1/duckduckgo/search?query=privacy+tools&region=us-en&safesearch=moderate&timelimit=week&page=1
```
Required: `query`. Optional: `region` (default `wt-wt`), `safesearch` (default `moderate`), `timelimit` (`day`|`week`|`month`|`year`), `page` (1-25). Returns organic results (title, url, snippet, display_url, `is_ad`), the zero-click abstract box, and `has_next`.

**Image search:**
```
GET /v1/duckduckgo/images?query=northern+lights&size=Large&color=Blue&image_type=photo&layout=Wide&license=Public
```
Required: `query`. Optional: `region`, `safesearch`, `page` (1-10, 100 results a page), `size` (`Small`|`Medium`|`Large`|`Wallpaper`), `color`, `image_type` (`photo`|`clipart`|`gif`|`transparent`|`line`), `layout` (`Square`|`Tall`|`Wide`), `license` (`Any`|`Public`|`Share`|`ShareCommercially`|`Modify`).

**News search:**
```
GET /v1/duckduckgo/news?query=elections&region=us-en&timelimit=day&page=1
```
Required: `query`. Optional: `region`, `safesearch`, `timelimit` (`day`|`week`|`month`|`year`), `page` (1-10, 30 results a page). Each item carries `date_utc` (unix) and `date_at` (ISO), source, excerpt and image.

**Video search:**
```
GET /v1/duckduckgo/videos?query=guitar+lesson&duration=medium&resolution=high&page=1
```
Required: `query`. Optional: `region`, `safesearch`, `page` (1-10, 60 results a page), `duration` (`short`|`medium`|`long`), `resolution` (`high`|`standard`). Returns title, publisher, uploader, duration, views and thumbnails.

**Autocomplete:**
```
GET /v1/duckduckgo/autocomplete?query=pyth&region=us-en
```
Required: `query`. Optional: `region`. Returns `{ query, suggestions[] }`.

**Instant Answer:**
```
GET /v1/duckduckgo/instant?query=valley+forge
```
Required: `query`. DuckDuckGo's Instant Answer API — abstract, definition, direct answer and related topics.

**Regions:**
```
GET /v1/duckduckgo/regions
```
No params. Returns the full list of 64 DuckDuckGo `kl` region codes (`us-en`, `uk-en`, `de-de`, … `wt-wt` = all).

Cost: 1 credit autocomplete / instant; 5 credits search / images / news / videos. `regions` and `health` are free.

## Apartments.com Rentals API

US rental listings from **apartments.com** (US, USD, en-US) with **unit-level pricing** — not just a property's advertised range, but every individual rentable unit with its own rent, beds, baths, square footage and availability date. No apartments.com account is needed.

**Search listings:**
```
GET /v1/apartments/search?location=kansas-city-mo&beds=1&max_price=1500
```
Required: `location` — the apartments.com slug (`kansas-city-mo`, `new-york-ny`) or a ZIP (`64108`). Optional: `page` (1-28, 40 cards a page), `beds` (0=studio, 1-4), `min_price`, `max_price`. Returns `results[]` of cards plus `total_results` / `total_pages`.

Filters verified against live counts on `kansas-city-mo` (700 unfiltered): `beds=1` → 374, `beds=2` → 490, `beds=0` → 145, `max_price=1500` → 646, `beds=1&max_price=1500` → 320. apartments.com also renders a pet filter, but it returns the unfiltered total, so it is deliberately not exposed.

**Get property detail (unit-level):**
```
GET /v1/apartments/property?url=https%3A%2F%2Fwww.apartments.com%2Furbane-kansas-city-mo%2Fwcd6e5k%2F
GET /v1/apartments/properties/{slug}/{property_id}
```
Returns the property (name, split address, geo, phone, amenities, office hours, photos), its `floor_plans[]`, and a flattened `units[]` across all plans.

**IMPORTANT — use `rent`, not `max_term_rent`.** Every unit carries both. `rent` is the advertised monthly price the site shows a renter. `max_term_rent` is apartments.com's raw `data-maxrent` attribute, which measures roughly **twice** the advertised rent and appears to be an upper bound across lease terms. It is exposed unparsed for completeness only.

`available_text` is verbatim (`"Now"`, `"Sep 3"`); the site renders no year, so it is deliberately not a date. A floor plan with `units_available: 0` and valid beds/baths/rent/sqft is the site's own layout for properties that advertise plans rather than individual units — not missing data.

A search card is a **summary** with a rent/bed rollup; pass its `url` to the property endpoint for units.

**Do not use `render_js` for apartments.com** via the general Web Scraping API — the page is fully server-rendered, so JS rendering only forces the slow browser path (100+ s) and can exceed the CDN timeout with a 524.

Cost: 5 credits per search page and per property.

## Idealista Real Estate API

Real-estate listings from Idealista across 3 markets — Spain (`es`), Italy (`it`), Portugal (`pt`), all EUR. The `market` parameter defaults to `es`. No upstream Idealista key is needed; ScrapeBadger signs requests to Idealista's mobile API server-side. Search is keyed by **location codes**, not free text, so use the two-step flow: suggest → search → property detail.

**Suggest locations (free-text → location codes):**
```
GET /v1/idealista/suggest?query=sagrada+familia&market=es
```
Optional params: `operation` (sale|rent, default sale), `property_type` (homes|offices|premises|garages|bedrooms|newDevelopments|lands|storageRooms|buildings, default homes). Returns locations[] + total + market. Only entries with `type == "location"` carry a usable `locationId`.

**Search listings (by location code):**
```
GET /v1/idealista/search?location=0-EU-ES-28-07-001-079&operation=sale&market=es
```
Optional params: `property_type` (as above, excluding bedrooms), `page` (default 1), `max_items` (default 30, 1..50), `sort_by` (weigh|price|distance|publicationDate|modificationDate|size|floor|rooms|ratioeurm2|pricedown), `sort_order` (asc|desc, default desc), `min_price`, `max_price`, `min_size`, `max_size`, `min_rooms`, `max_rooms`. Returns elementList[] + total + totalPages + actualPage + itemsPerPage + summary[] + market.

**Full property detail (by property code):**
```
GET /v1/idealista/properties/{property_code}?market=es&locale=en
```
Optional params: `locale` (en|es|it|pt, default en). Returns property + market.

**List markets (free):**
```
GET /v1/idealista/markets
```

Supported markets (3): es (idealista.com), it (idealista.it), pt (idealista.pt).

---

## Immobiliare Real Estate API

Real-estate listings from the Immobiliare Group — Italy's #1 portal immobiliare.it plus its sister portals — across 4 markets: `it` (www.immobiliare.it), `es` (www.indomio.es), `gr` (www.indomio.gr), `lu` (www.immotop.lu), all EUR. The `market` parameter defaults to `it`. No upstream API key needed. Search accepts a free-text `location` (auto-resolved) or explicit `region_id`/`province_id`/`city_id` codes from `/autocomplete`.

**Location autocomplete (free-text → location IDs):**
```
GET /v1/immobiliare/autocomplete?query=milano&market=it
```
Returns suggestions[] — each `{id, label, type (nation|region|province|comune|zone), region_id, province_id, city_id, macrozone_ids[], url}`.

**Search listings:**
```
GET /v1/immobiliare/search?location=Milano&contract=sale&market=it
```
Optional params: `region_id`/`province_id`/`city_id` (instead of free-text `location`), `contract` (sale|rent), `category` (residential|commercial|garages|offices|land|buildings|warehouses), `price_min`, `price_max`, `surface_min`, `surface_max`, `rooms_min`, `rooms_max`, `bathrooms_min`, `sort` (relevance|price_asc|price_desc|newest|oldest|surface_desc|surface_asc), `page`. Returns listings[] + count + total_ads + current_page + max_pages + is_results_limit_reached + related_searches[].

**Get full listing detail:**
```
GET /v1/immobiliare/listings/{id}?market=it
```
Returns a full Listing: price + €/m², surface, rooms, baths, floor, energy class, GPS coordinates, all photos, virtual tours, agency + agent contacts, multi-unit properties[].

**Agency profile:**
```
GET /v1/immobiliare/agencies/{id}?market=it
```

**Agency listings:**
```
GET /v1/immobiliare/agencies/{id}/listings?market=it&page=1
```

**Market price insights (€/m² monthly time series):**
```
GET /v1/immobiliare/market-insights/prices?region_id=10&market=it
```
Required: `region_id`. Optional params: `province_id`, `city_id`, `contract` (sale|rent). Returns `{contract, unit: "EUR/m²", points[{label, value}]}`.

**List markets (free):**
```
GET /v1/immobiliare/markets
```

**Reference data — contracts/categories/sorts (free):**
```
GET /v1/immobiliare/reference
```

Supported markets (4): it (immobiliare.it), es (indomio.es), gr (indomio.gr), lu (immotop.lu).

---

## YouTube API

No YouTube Data API key, OAuth, or quota required. Data is fetched via YouTube's unauthenticated InnerTube JSON API (`youtubei/v1/*`) plus SSR-HTML fallback. The `gl` parameter (ISO 3166-1 alpha-2 content region, default `US`) and `hl` parameter (BCP-47 UI language, default `en`) steer the geo-matched residential proxy + locale. All list endpoints paginate via a `continuation` token (no page numbers); pass the returned token back as `continuation`. All datetime fields ship as both `*_utc` (Unix) and `*_at` (ISO 8601 UTC).

**Search videos / channels / playlists:**
```
GET /v1/youtube/search?query=machine+learning&gl=US&hl=en
```
Optional params: `type` (video|channel|playlist|movie|all), `sort_by` (relevance|date|views|rating), `upload_date` (hour|today|week|month|year), `duration` (short|medium|long), `features` (csv: hd,4k,360,vr180,3d,hdr,cc,subtitles,live,creative_commons,location,purchased), `continuation`. Returns results[] + continuation.

**Search autocomplete:**
```
GET /v1/youtube/autocomplete?query=machine+lea&gl=US&hl=en
```

**Get video detail (merged player+next):**
```
GET /v1/youtube/videos/{video_id}
```

**Related videos:**
```
GET /v1/youtube/videos/{video_id}/related?continuation=...
```

**Video comments and nested replies:**
```
GET /v1/youtube/videos/{video_id}/comments?sort_by=top&continuation=...
GET /v1/youtube/videos/{video_id}/comments/{comment_id}/replies?continuation=...
```

**Transcript (timed text + full text + SRT/VTT):**
```
GET /v1/youtube/videos/{video_id}/transcript?lang=en
```

**Captions / streams / live chat:**
```
GET /v1/youtube/videos/{video_id}/captions
GET /v1/youtube/videos/{video_id}/streams
GET /v1/youtube/videos/{video_id}/live_chat?continuation=...
```

**Batch video lookup (POST):**
```
POST /v1/youtube/videos/batch
{ "video_ids": ["dQw4w9WgXcQ", "..."] }
```

**Channel detail + tabs:**
```
GET /v1/youtube/channels/{channel_id}
GET /v1/youtube/channels/{channel_id}/videos?sort_by=newest&continuation=...
GET /v1/youtube/channels/{channel_id}/shorts?continuation=...
GET /v1/youtube/channels/{channel_id}/streams?continuation=...
GET /v1/youtube/channels/{channel_id}/playlists?continuation=...
GET /v1/youtube/channels/{channel_id}/community?continuation=...
GET /v1/youtube/channels/{channel_id}/about
GET /v1/youtube/channels/{channel_id}/subscriber_count
GET /v1/youtube/channels/{channel_id}/search?query=...&continuation=...
```

**Resolve a handle / custom URL to a channel_id:**
```
GET /v1/youtube/channels/resolve?handle=@GoogleDevelopers
```

**Playlists and mixes:**
```
GET /v1/youtube/playlists/{playlist_id}
GET /v1/youtube/playlists/{playlist_id}/items?continuation=...
GET /v1/youtube/mixes/{mix_id}
```

**Trending, hashtags, home feed:**
```
GET /v1/youtube/trending?gl=US&type=now&continuation=...
GET /v1/youtube/trending/shorts?gl=US&continuation=...
GET /v1/youtube/hashtags/{tag}?gl=US&continuation=...
GET /v1/youtube/home?gl=US&hl=en&continuation=...
```

**Shorts:**
```
GET /v1/youtube/shorts/{short_id}
GET /v1/youtube/shorts/by_sound/{sound_id}?continuation=...
```

**Community posts:**
```
GET /v1/youtube/posts/{post_id}
GET /v1/youtube/posts/{post_id}/comments?continuation=...
```

**YouTube Music search:**
```
GET /v1/youtube/music/search?query=...
```

**Reference (free):**
```
GET /v1/youtube/oembed?url=...
GET /v1/youtube/categories
GET /v1/youtube/languages
GET /v1/youtube/regions
GET /v1/youtube/markets
```

---

## TikTok API

No TikTok login required. The `region` parameter (ISO 3166-1 alpha-2, default `US`) steers the residential proxy geo + locale. `count` is 1–50. Most endpoints use a fast device-signed mobile path with deep cursor pagination. All datetime fields ship as both `*_utc` (Unix) and `*_at` (ISO 8601 UTC).

### Users

**Get user profile:**
```
GET /v1/tiktok/users/{username}
```

**Get user's videos (cursor pagination):**
```
GET /v1/tiktok/users/{username}/videos?count=30&cursor=...
```

**Get followers (403 if the account hides the list):**
```
GET /v1/tiktok/users/{username}/followers?count=20
```

**Get following (403 if private):**
```
GET /v1/tiktok/users/{username}/following?count=20
```

**Get liked videos (403 if private):**
```
GET /v1/tiktok/users/{username}/liked?count=20
```

**Get reposted videos:**
```
GET /v1/tiktok/users/{username}/reposts?count=20
```

### Videos

**Get video / photo detail:**
```
GET /v1/tiktok/videos/{video_id}
```
Optional param: `username`

**Get video comments:**
```
GET /v1/tiktok/videos/{video_id}/comments?count=20
```

**Get comment replies:**
```
GET /v1/tiktok/comments/{comment_id}/replies?item_id={video_id}&count=20
```

**Get related videos:**
```
GET /v1/tiktok/videos/{video_id}/related?count=20
```

**Get auto-caption transcript:**
```
GET /v1/tiktok/videos/{video_id}/transcript
```

**Get oEmbed metadata for a TikTok URL:**
```
GET /v1/tiktok/oembed?url=https://www.tiktok.com/@user/video/123
```

### Hashtags & Music

**Get hashtag / challenge detail:**
```
GET /v1/tiktok/hashtags/{name}
```

**Get videos for a hashtag:**
```
GET /v1/tiktok/hashtags/{name}/videos?count=20
```

**Get sound / music detail:**
```
GET /v1/tiktok/music/{music_id}
```

**Get videos using a sound:**
```
GET /v1/tiktok/music/{music_id}/videos?count=20
```

### Search

**General search (returns videos):**
```
GET /v1/tiktok/search?query=ai+agents&count=20
```

**Search videos:**
```
GET /v1/tiktok/search/videos?query=ai+agents&count=20
```

**Search hashtags:**
```
GET /v1/tiktok/search/hashtags?query=ai&count=20
```

**Search users:**
```
GET /v1/tiktok/search/users?query=charli&count=20
```

### Trending

**Trending videos (curated Explore feed):**
```
GET /v1/tiktok/trending/videos?region=US&count=20
```

**Trending hashtags (with view_count + creator counts):**
```
GET /v1/tiktok/trending/hashtags?region=US&count=20
```

**Trending songs (ranked by usage):**
```
GET /v1/tiktok/trending/songs?region=US&count=20
```

### Ad Library (EU only)

**Search the TikTok Commercial Content Library (EU-DSA ad transparency):**
```
GET /v1/tiktok/ads/search?query=sneakers&region=DE&days=30&count=20
```
Search by keyword (`query`) OR by advertiser (`advertiser_id`). Paginates via `offset` + `search_id`. EU regions only.

### Reference (free)

**List supported regions:**
```
GET /v1/tiktok/regions
```

Coverage notes: `following`/`liked` return 403 when the account hides those lists (most large accounts do). Trending creators and trending keywords are not available (TikTok deprecated the Creative Center trend lists). The Ad Library is EU-only.

---

## ChatGPT API

Sends a prompt to **the real chatgpt.com** (not the OpenAI API) and returns the answer as structured JSON, including the web sources ChatGPT cited. Anonymous — no OpenAI account or API key is involved. Measured latency **20-25s ungrounded, 30-70s with web search per call**, so set a generous client timeout and don't poll.

**Ask ChatGPT (20 credits):**
```
GET /v1/chatgpt/ask?prompt=best+open-source+vector+databases&country=US&web_search=auto
```
Required: `prompt` (max 4096 chars). Optional: `country` (ISO-3166 alpha-2 egress country, default `US`), `web_search` (`auto` | `force` | `off`, default `auto`). Also accepts POST with the same fields as a JSON body.

Returns: `prompt`, `answer`, `answer_markdown`, `citations[]`, `search_results[]`, `source_domains[]`, `web_search_triggered` (whether ChatGPT actually browsed), `reference_tokens[]`, `model`, `conversation_id`, `message_id`, `country`, `answer_length`, `citation_count`, `latency_ms`, `created_utc`/`created_at`.

Each `Citation` is `{url, title, snippet, domain, attribution, pub_date_utc, published_at, start_index, end_index, matched_text}` — `start_index`/`end_index` are char offsets into `answer`, so you can anchor a source to the exact sentence it supports. `search_results[]` is the FULL retrieved set (`{url, title, snippet, domain, attribution, pub_date_utc, published_at, ref_index, cited}`), including results ChatGPT retrieved but never cited.

**Brand visibility — AEO/GEO (25 credits):**
```
GET /v1/chatgpt/brand-visibility?prompt=best+CRM+for+startups&brand=Acme&domain=acme.com&competitors=Salesforce,HubSpot
```
Required: `prompt`, `brand`. Optional: `domain`, `aliases` (comma-separated on GET, `string[]` on POST), `competitors` (same), `country`, `web_search` (default `force`).

Returns the brand block plus the answer: `mentioned`, `mention_count`, `first_position` (char offset), `position_score` (1.0 = named at the very start, 0.0 = absent), `share_of_voice_pct` (brand mentions / brand+competitor mentions), `cited`, `cited_urls[]`, `citation_rank`, `competitors[]` (`{name, mentioned, mention_count, first_position, cited, cited_urls}`), `excerpt`, `answer`, `citations[]`, `web_search_triggered`, `model`, `country`, `latency_ms`, `created_utc`/`created_at`.

**List available models (1 credit):**
```
GET /v1/chatgpt/models?country=US
```
Returns `{models: [{slug, title, description, max_tokens, tags[]}], count}`. Informational only — `/ask` does not take a model parameter.

**Health (free):**
```
GET /v1/chatgpt/health
```

Errors come back as `{"detail": {"code", "message"}}` with codes `blocked` (422), `rate_limited` (429), `upstream_error`, `composer_not_found`, `empty_answer`, `render_failed`, `models_unavailable` (502). Non-2xx responses are never billed.

Not supported: multi-turn conversations, model selection, streaming, and image input.

---

## Perplexity API

Sends a prompt to **the real perplexity.ai** and returns the grounded answer as structured JSON, including the web sources Perplexity cited. Anonymous — no Perplexity account or API key is involved. Every answer is a live browse taking tens of seconds, so set a generous client timeout and don't poll.

**Ask Perplexity (20 credits):**
```
GET /v1/perplexity/ask?prompt=best+open-source+vector+databases&country=US&focus=web
```
Required: `prompt` (max 4096 chars). Optional: `country` (ISO-3166 alpha-2 egress country, default `US`), `focus` (`web` | `scholar` | `social`, default `web` — `scholar` grounds on academic sources, `social` on community sources). Also accepts POST with the same fields as a JSON body.

Returns: `prompt`, `answer`, `answer_markdown`, `citations[]`, `search_results[]`, `source_domains[]`, `related_questions[]`, `images[]`/`videos[]`, `web_search_triggered`, `truncated`, `search_queries[]` (Perplexity's own retrieval fan-out — the sub-queries it issued to its search backend, which no other vendor exposes), `focus`, `model`, `backend_uuid`, `country`, `answer_length`, `citation_count`, `latency_ms`, `created_utc`/`created_at`.

Each `Citation` is `{url, title, snippet, domain, source_type, pub_date_utc, published_at, last_updated, ref_index, start_index, end_index, matched_text}` — `start_index`/`end_index` are char offsets into `answer`, so you can anchor a source to the exact sentence it supports. `search_results[]` is the FULL retrieved set (`{url, title, snippet, domain, source_type, pub_date_utc, published_at, last_updated, ref_index, cited}`), including results Perplexity retrieved but never cited.

**Brand visibility — AEO/GEO (25 credits):**
```
GET /v1/perplexity/brand-visibility?prompt=best+CRM+for+startups&brand=Acme&domain=acme.com&competitors=Salesforce,HubSpot
```
Required: `prompt`, `brand`. Optional: `domain`, `aliases` (comma-separated on GET, `string[]` on POST), `competitors` (same), `country`.

Returns the brand block plus the answer: `mentioned`, `mention_count`, `first_position` (char offset), `position_score` (1.0 = named at the very start, 0.0 = absent), `share_of_voice_pct` (brand mentions / brand+competitor mentions), `cited`, `cited_urls[]`, `citation_rank`, `competitors[]` (`{name, mentioned, mention_count, first_position, cited, cited_urls}`), `excerpt`, `answer`, `citations[]`, `web_search_triggered`, `model`, `country`, `latency_ms`, `created_utc`/`created_at`.

**List available models (1 credit):**
```
GET /v1/perplexity/models?country=US
```
Returns `{models: [{slug, title, description, requires_account}], count}`. Informational only — `/ask` takes a `focus` parameter, not a model.

**Health (free):**
```
GET /v1/perplexity/health
```

Non-2xx responses are never billed.

Not supported: multi-turn conversations (a `backend_uuid` is returned but follow-up chaining is not exposed), model selection, streaming, and image input.

---

## Baidu API

Web search, news, images and autocomplete from **baidu.com** — China's #1 search engine (~60% CN market share). No Baidu account or developer key is needed. Chinese and English queries both work; there is no country parameter, Baidu is a single market.

**Web search (5 credits):**
```
GET /v1/baidu/search?query=咖啡机&page=1&num=20&language=zh-cn
GET /v1/baidu/search?query=site:zhihu.com+咖啡&time_from=1735689600&time_to=1767225600
```
Required: `query`. Optional: `page` (1-76), `num` (1-50), `language` (`all`|`zh-cn`|`zh-tw`), `time_from`/`time_to` (unix timestamps). Baidu's own operators — `site:`, `intitle:`, `inurl:`, `filetype:`, `"quoted phrases"` — work inside `query`. `page` is translated to Baidu's `pn` offset using `num`, so the two compose (`page=3&num=50` starts at result 101).

Each organic result carries the **real target URL** in `url` (from Baidu's `mu` attribute) alongside `baidu_url` (the `baidu.com/link?url=` tracking redirect competitors return on its own), plus `display_url`, `snippet`, `source`, `date` (Baidu's own string, e.g. `2026年8月1日` / `3天前`), `date_at` (ISO 8601 date), `thumbnail`, `tpl` (Baidu's result template id). The response also carries `total_results` and `related_searches[]`.

**News (5 credits):**
```
GET /v1/baidu/news?query=人工智能&sort=time
```
Required: `query`. Optional: `page` (1-76), `sort` (`relevance` default, or `time` for newest first). 10 articles a page; each has `title`, `url`, `baidu_url`, `snippet`, `source`, `date`, `date_at`, `thumbnail`.

**Images (5 credits):**
```
GET /v1/baidu/images?query=熊猫&page=1
```
Required: `query`. Optional: `page` (1-50). 30 images a page, each with `image_url` (full size), `thumbnail_url`, `middle_url`, `hover_url`, `width`, `height`, `type`, `from_url` and `from_title` (the page it was found on).

**Autocomplete (1 credit):**
```
GET /v1/baidu/autocomplete?query=咖啡
```

**Gotchas that will bite you:**
- `total_results` is Baidu's own claim (`百度为您找到相关结果约N个`) and is **not reachable** — pagination stops around page 76 regardless.
- Only organic results are returned. Baidu's own vertical blocks (Baike, Tieba, image grids) and ad shells are dropped, so `position` is organic rank.
- Baidu's SERP carries **no time-of-day**, so there is no `*_utc` float — only `date` (raw) and `date_at` (ISO date). A midnight timestamp would be fabricated precision.
- `url` is null when Baidu omits the `mu` attribute on a result; `baidu_url` is present either way.
- `language` and the time window are server-side Baidu filters, not post-filtering — they change which results Baidu returns.
- HTTP 422 is an anti-bot challenge: not billed, and retrying shortly succeeds.

Cost: 1 credit autocomplete; 5 credits search / news / images. `health` is free.

---

## Web Scraping API

**Scrape a URL:**
```
POST /v1/web/scrape
Content-Type: application/json

{"url": "https://example.com", "render_js": false, "return_format": "markdown"}
```
Optional fields: `render_js` (boolean), `wait_for` (CSS selector), `timeout_ms`, `proxy_country`, `return_format` (html/markdown/text)

**Detect anti-bot protection (1 credit):**
```
POST /v1/web/detect
Content-Type: application/json

{"url": "https://example.com"}
```

**Take screenshot:**
```
POST /v1/web/screenshot
Content-Type: application/json

{"url": "https://example.com", "full_page": true}
```

**Extract structured data:**
```
POST /v1/web/extract
Content-Type: application/json

{"url": "https://example.com", "ai_query": "What is the main product price?"}
```
Optional fields: `extract_rules` (CSS/XPath), `ai_extract_rules`, `ai_query`

**Submit batch job:**
```
POST /v1/web/batch
Content-Type: application/json

{"urls": ["https://example.com", "https://example.org"]}
```

**Check batch status:**
```
GET /v1/web/batch/{job_id}
```

---

## Pagination

Most list endpoints support cursor-based pagination. Pass the `cursor` query parameter from the previous response to get the next page.

## Credits

Each API call costs credits. Check your balance:
- Twitter endpoints: 1 credit per call
- Web scraping: 1-10 credits depending on complexity
- Vinted: 1 credit per call
- Amazon: autocomplete 1, seller profile/feedback 3, listings 5, offers 8, product detail & reviews 10; markets/categories free
- eBay: autocomplete 1; search/completed/item/seller/category 5; reviews/feedback 10; markets/categories free
- Realtor: autocomplete 2; search 8; property detail 10; markets free
- Idealista: suggest 2; search 5; property detail 10; markets free
- Immobiliare: autocomplete 2; search / agency profile / agency listings 5; listing detail & market price insights 10; markets/reference free
- YouTube: autocomplete/oembed 1; resolve/about/subscriber_count/captions 2; search/transcript/channel/playlist/trending/community/shorts/music 5; video detail & batch (per video) 10; streams 15; categories/languages/regions/markets free
- TikTok: oembed 2; profile/video/hashtag/music detail + search + trending + ads 5; list captures (user videos/reposts, comments, replies, related, hashtag/music videos) 8; followers/following/liked + transcript 10; regions free
- ChatGPT: models 1; ask 20; brand-visibility 25; health free
- Perplexity: models 1; ask 20; brand-visibility 25; health free
- Baidu: autocomplete 1; search/news/images 5; health free

## Rate Limits

Rate limits are per API key. Check the `X-RateLimit-*` response headers for current limits.

## More Information

- Documentation: https://docs.scrapebadger.com
- Dashboard: https://scrapebadger.com/dashboard?utm_source=openclaw-skill&utm_medium=referral
- MCP Server: https://mcp.scrapebadger.com/mcp
