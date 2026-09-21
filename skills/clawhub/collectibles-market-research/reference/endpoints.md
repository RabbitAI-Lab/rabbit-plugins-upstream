# collectibles-market-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**54 endpoints across 7 platform group(s).**

## Alt (9)

### `alt_asset`

- **HTTP:** `GET /alt/asset`
- **What:** Get one card design's population report and recent sales. Returns one card design's identity, full population report (across every grading company and grade Alt tracks), and a recent raw sales feed -- the "is this card actually rare, and what does it sell for" data for a specific card design, independent of any single listing. asset_id comes from a prior alt-search/alt-sold-listings/alt-card-search result's asset_id field. recent_sales has no per-transaction grade breakdown -- Alt's own API does not expose one; see alt-sold-listings for per-grade sold prices on specific listings. Credential-free public data from Alt's own GraphQL API.
- **Params:** `asset_id` (string, **required**) — The card design's asset id, from a Search/SoldListings/CardSearch result's asset_id field

### `alt_auctions`

- **HTTP:** `GET /alt/auctions`
- **What:** Search Alt's own live 24/7 auctions. Searches Alt's own currently live auctions -- the same pool shown on alt.xyz/browse's "Auctions" tab filtered to the Alt source. Unlike alt-search, this never returns another source auction house's listings or Alt's own fixed-price items: it always uses a search key scoped server-side to Alt's own live auction pool. Credential-free public data from Alt's own search backend. See alt-categories for the accepted category/grading_company/sort values.
- **Params:** `category` (string, optional) — Comma-separated card category filter; `grading_company` (string, optional) — Comma-separated grading company filter; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 24, max 100; `q` (string, optional) — Free-text search across item name, subject, brand, and variety. Omit or pass * to browse every current Alt auction.; `sort` (string, optional) — Result order. Default recommended.

### `alt_card_search`

- **HTTP:** `GET /alt/card-search`
- **What:** Search Alt's reference card-design catalog. Searches Alt's reference card-design catalog -- a canonical catalog of card designs (one entry per year/brand/subject/card-number/variety combination), separate from live listings or sales. Useful for finding a card design's asset_id (to feed into alt-asset for a population report and recent sales) without already having a live listing or sale that references it. Credential-free public data from Alt's own search backend.
- **Params:** `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 24, max 100; `q` (string, optional) — Free-text search across card name, subject, brand, and variety

### `alt_categories`

- **HTTP:** `GET /alt/categories`
- **What:** List Alt search filter values. Returns every accepted value for alt-search/alt-auctions/alt-sold-listings' category, auction_house, grading_company, and listing_type params, plus the sort enum. category/auction_house/grading_company/listing_type are read live from Alt's own current search index via a facets-only query on every call, not a fixed taxonomy -- so this endpoint self-corrects if Alt's aggregator adds a new source auction house, grading company, or category. Credential-free public data from Alt's own search backend.
- **Params:** _none_

### `alt_listing`

- **HTTP:** `GET /alt/listing`
- **What:** Get one Alt listing's full public detail. One listing's full public detail -- title, description, price/bid state, grading info, and images -- normalized across Alt's own native listings and its aggregated external listings. id and listing_type come from a prior alt-search/alt-auctions result. Not every response field applies to every listing_type -- see the field-level notes in this endpoint's markdown doc.
- **Params:** `id` (string, **required**) — The listing's id, from a Search/Auctions result's id field; `listing_type` (string, **required**) — The listing's listing_type from the same Search/Auctions result

### `alt_market_trends`

- **HTTP:** `GET /alt/market-trends`
- **What:** Get Alt's card-market price-trend index. Returns Alt's own category-level price-trend index -- the same data alt.xyz's "Market Trends" page shows: a weekly/monthly/90-day change and a current index value per card category, built from Alt's own sold/valuation data. Credential-free public data from Alt's own GraphQL API.
- **Params:** `category` (string, optional) — Optional exact category filter -- must match one of the categories present in the live response (a subset of alt-categories' category list; Alt only publishes a trend index for its own tracked sports categories). Omit to get every tracked category.

### `alt_search`

- **HTTP:** `GET /alt/search`
- **What:** Search Alt's aggregated card marketplace. Searches Alt's universal aggregator index -- live auction and fixed-price listings from Alt itself and every other source auction house its search carries (eBay, Fanatics Collect, Pristine Auction, Goldin, CardHobby, Memory Lane) -- by free-text query, category, source auction house, grading company, and listing type, in a caller-selected sort order. Only currently-live listings are returned; see alt-sold-listings for completed sales. Credential-free public data from Alt's own search backend. See alt-categories for the accepted category/auction_house/grading_company/listing_type/sort values.
- **Params:** `auction_house` (string, optional) — Comma-separated source auction house filter; `category` (string, optional) — Comma-separated card category filter; `grading_company` (string, optional) — Comma-separated grading company filter; `listing_type` (string, optional) — Comma-separated listing type filter. Omit to search auctions and fixed-price listings from every source together.; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 24, max 100; `q` (string, optional) — Free-text search across item name, subject, brand, and variety. Omit or pass * to browse everything.; `sort` (string, optional) — Result order. Default recommended.

### `alt_sold_listings`

- **HTTP:** `GET /alt/sold-listings`
- **What:** Search Alt's completed sales archive. Searches Alt's global archive of completed card sales, aggregated across every source auction house its search carries -- the "market data" side of Alt's card-investment-marketplace positioning. This is a separate index from alt-search/alt-auctions, scoped to a rolling recent time window, not a filtered view of live listings. Pass auction_house=Alt to see only Alt's own completed auctions. Credential-free public data from Alt's own search backend. See alt-categories for the accepted category/auction_house/grading_company values.
- **Params:** `auction_house` (string, optional) — Comma-separated source auction house filter. Pass Alt to see only Alt's own completed auctions.; `category` (string, optional) — Comma-separated card category filter; `grading_company` (string, optional) — Comma-separated grading company filter; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 24, max 100; `q` (string, optional) — Free-text search across item name, subject, brand, and variety. Omit or pass * to browse the most recent sales.

### `alt_top_movers`

- **HTTP:** `GET /alt/top-movers`
- **What:** Get Alt's biggest card-market price movers. Returns Alt's biggest price-index movers -- either a cross-subject leaderboard (optionally scoped to one category) or, when subject is set, that one player/character's own trend broken out per category it appears in. category is not strictly validated against alt-categories' list -- this trend index's own category set is broader (e.g. it includes MULTI-SPORT_CARDS). Credential-free public data from Alt's own GraphQL API.
- **Params:** `category` (string, optional) — Optional category filter for the leaderboard. Ignored when subject is set. Omit to rank movers across every category.; `limit` (integer, optional) — Max results, default 10, max 50; `subject` (string, optional) — Optional exact player/subject name. Returns that subject's own trend per category instead of a leaderboard, and category is ignored.

## COMC (3)

### `comc_categories`

- **HTTP:** `GET /comc/categories`
- **What:** List COMC categories. Returns COMC's (comc.com) closed, top-level category/sport taxonomy -- the discovery endpoint for the search endpoint's `category` param. Every slug is the exact path segment comc.com's own site uses.
- **Params:** _none_

### `comc_listing`

- **HTTP:** `GET /comc/listing`
- **What:** Get COMC card listing detail. Returns one card+grade combination's full detail from COMC (comc.com): card identity and every seller's individual for-sale copy (owner, item id, price). handle is the value returned by comc_search's CardSummary.handle field (or the equivalent comc.com card URL path).
- **Params:** `handle` (string, **required**) — Required. The handle from a comc_search result (or the equivalent comc.com card URL path).

### `comc_search`

- **HTTP:** `GET /comc/search`
- **What:** Search COMC card listings. Searches or browses COMC's (comc.com) live consignment marketplace for graded and ungraded trading cards. Each result row is a distinct card+grade combination (COMC's own category/search grid aggregates every seller's copy under one row); chain a row's handle into the listing endpoint for the per-seller breakdown. At least one of category or query is typically useful, but both are optional -- omitting both searches all categories.
- **Params:** `attributes` (string, optional) — Optional, comma-separated. Allowed values: AUTO (Autographed), HOF (Hall of Fame), MEM (Memorabilia), PRC (Pre-Rookie Card), RC (Rookie Card), RR (Rookie Related), RY (Rookie Year), SN (Serial Numbered).; `category` (string, optional) — Optional. One of comc_categories' slug values. Omit to search all categories.; `condition` (string, optional) — Optional. Allowed values: aUngraded (Ungraded), aGraded (Graded), aAftermarketAuto (Aftermarket Auto), aAfterAutoGraded (Aftermarket Auto Graded).; `page` (integer, optional) — 1-based page, default 1.; `page_size` (integer, optional) — Optional. Allowed values: 6, 8, 10, 12, 14, 15, 16, 18, 20, 24, 30, 40, 50, 64, 100. Omit to use COMC's own default.; `query` (string, optional) — Optional free-text search query.; `sort` (string, optional) — Optional. Allowed values: r (Recently Added, default), c (Card #), o (Oldest), n (Newest), b (Highest SRP), h (Highest Price), l (Lowest Price), d (Biggest Discount), p (Highest Percent Off), q (Print Run), s (Least in Stock), m (Most in Stock), e (Ending Soonest).

## Fanatics Collect (7)

### `fanaticscollect_auctions`

- **HTTP:** `GET /fanaticscollect/auctions`
- **What:** List Fanatics Collect auction events. Returns Fanatics Collect's current and recent weekly and premier auction events -- the same short list the site's own header auction switcher and countdown banner show. This is the discovery endpoint for Search's auction_urn param: copy an event's urn value to browse every lot in that auction. A small, current/recent set (observed live: around 6 events), not a full historical archive -- older auctions' urn values found on a Search result or a GetListing response remain valid for Search even once they no longer appear here. Credential-free public data from Fanatics Collect's own GraphQL API.
- **Params:** _none_

### `fanaticscollect_categories`

- **HTTP:** `GET /fanaticscollect/categories`
- **What:** List Fanatics Collect search filter values. Returns every accepted value for GetListing's marketplace param -- WEEKLY, PREMIER, FIXED -- and for Search's marketplace, category_parent, sub_category, grading_service, status, and sort params. Discovery endpoint for those closed enums.
- **Params:** _none_

### `fanaticscollect_instant_rips_categories`

- **HTTP:** `GET /fanaticscollect/instant-rips/categories`
- **What:** Get Fanatics Collect Instant Rips categories. Returns every category Fanatics Collect's "Instant Rips" mystery-pack product (fanaticscollect.com/instant-rips) currently advertises on its homepage: id, name, and price range. Instant Rips is a "buy a randomized pack, a real graded card is revealed" product; each category's id is a real listing id, fetchable through GetListing with type=FIXED for that entry point's own full detail. This does not cover the individual pack-tier tiles within a category or the homepage's "Recently ripped" live feed -- both are hydrated client-side in a form this repo cannot reliably parse. Credential-free public data, server-rendered on Fanatics Collect's own page.
- **Params:** _none_

### `fanaticscollect_listing`

- **HTTP:** `GET /fanaticscollect/listing/{id}`
- **What:** Get Fanatics Collect listing detail. Returns full detail for a single Fanatics Collect listing: a weekly-auction lot, a premier-auction lot, or a fixed-price "buy now" item (including an Instant Rips pack). Fields include title, current bid/starting/asking price, bid count, auction window and status, images, description, completed sale history, and -- when the card is stored in Fanatics' vault -- grading/authentication metadata including a direct PSA cert-verification link. Credential-free public data from Fanatics Collect's own GraphQL API.
- **Params:** `id` (string, **required**) — Listing UUID; `type` (string, optional) — Listing type. Default: WEEKLY

### `fanaticscollect_search`

- **HTTP:** `GET /fanaticscollect/search`
- **What:** Search Fanatics Collect listings. Searches Fanatics Collect's full marketplace -- weekly auctions, premier auctions, and the fixed-price "Buy Now" marketplace -- by free-text query, category, grading service, price/year/grade range, and listing status, in a caller-selected sort order. Credential-free public data from Fanatics Collect's own public search index. See GetCategories for the accepted category, grading-service, status, and sort values.
- **Params:** `allow_offers` (boolean, optional) — Filter for listings the seller accepts offers on; `auction_urn` (string, optional) — Browse every lot in one specific weekly or premier auction event. Not a fixed enum; copy the exact value from a prior Search result's auction_urn field. Only WEEKLY/PREMIER listings carry one.; `brand` (string, optional) — Exact brand/subject facet value (case-insensitive), e.g. a player, character, or set name. Not a fixed enum; match a prior Search result's brand field.; `category_parent` (string, optional) — Top-level category; `certified_seller` (string, optional) — Exact seller/shop name (case-insensitive). Not a fixed enum -- match a name from a prior Search result's certified_seller field.; `grading_service` (string, optional) — Grading/authentication service; `great_price` (boolean, optional) — Filter for listings Fanatics Collect itself flags as a great price vs. guide value; `has_offers` (boolean, optional) — Filter for listings with at least one active offer pending; `marketplace` (string, optional) — Listing type. Omit to search all three.; `max_grade` (number, optional) — Maximum numeric grade, inclusive; `max_price` (number, optional) — Maximum current price/bid, inclusive; `max_year` (integer, optional) — Maximum card/item year, inclusive; `min_grade` (number, optional) — Minimum numeric grade, inclusive; `min_price` (number, optional) — Minimum current price/bid, inclusive; `min_year` (integer, optional) — Minimum card/item year, inclusive; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 24, max 100; `q` (string, optional) — Free-text search across title, brand, subject, and set; `seller_id` (string, optional) — Exact seller id (UUID) -- browse everything one seller has listed. Not a fixed enum; match a prior Search result's seller_id field.; `sort` (string, optional) — Result order. Default best_value.; `status` (string, optional) — Listing status. Default LIVE.; `sub_category` (string, optional) — A parent > child category path (or just the child name), e.g. \

### `fanaticscollect_sold_items`

- **HTTP:** `GET /fanaticscollect/sold-items`
- **What:** Search Fanatics Collect sold items. Searches Fanatics Collect's sales-history archive -- every completed sale across every marketplace, not just what the live search index currently surfaces. A separate product from Search, reached from the "View all sold items" link on every marketplace search page. Credential-free public data from Fanatics Collect's own public sales-history API. See GetCategories for the accepted category, grading-service, eye-appeal-grade, and sort values.
- **Params:** `category` (string, optional) — Item category; `eye_appeal_grade` (string, optional) — Eye-appeal grade; `grading_service` (string, optional) — Grading/authentication service, including ungraded for raw items; `max_price` (number, optional) — Maximum sold price, inclusive; `max_year` (integer, optional) — Maximum card/item year, inclusive; `min_price` (number, optional) — Minimum sold price, inclusive; `min_year` (integer, optional) — Minimum card/item year, inclusive; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 20, max 100; `sort` (string, optional) — Result order. Default sold_date_desc.; `title` (string, optional) — Free-text search across item title

### `fanaticscollect_trending_searches`

- **HTTP:** `GET /fanaticscollect/trending-searches`
- **What:** Get Fanatics Collect trending search terms. Returns Fanatics Collect's own currently trending search terms -- the same list shown in the site's own header search box before the visitor types anything. Credential-free public data from Fanatics Collect's own GraphQL API.
- **Params:** `limit` (integer, optional) — Number of terms to return, 1-50, default 8

## Fanatics Live (8)

### `fanaticslive_browse`

- **HTTP:** `GET /fanaticslive/browse`
- **What:** Browse Fanatics Live shows by league. Returns the live and upcoming shows currently listed under a Fanatics Live league: name, status, cover image, viewers, and the hosting channel/shop. Public data sourced from Fanatics Live's own GraphQL API.
- **Params:** `league` (string, **required**) — Fanatics Live league type code. See GET /fanaticslive/leagues for the full list.

### `fanaticslive_channel`

- **HTTP:** `GET /fanaticslive/channel/{id}`
- **What:** Get a Fanatics Live channel's detail page. Returns a Fanatics Live channel's own detail page: its parent shop, and a first page of its live/upcoming and past/replay shows. A shop can run several channels (e.g. a league-specific sub-feed) -- see /fanaticslive/shop/{slug} for a shop's full channel list and /fanaticslive/shop/{slug}/shows for cursor-paginated access to a full show history. Public data sourced from Fanatics Live's own GraphQL API.
- **Params:** `id` (string, **required**) — Fanatics Live channel id (a UUID), e.g. from a shop or show result's channel.id field

### `fanaticslive_instant_rips`

- **HTTP:** `GET /fanaticslive/show/{id}/instant-rips`
- **What:** Get a Fanatics Live show's current instant-rip state. Returns a Fanatics Live show's current break's digital-instant-rip state: spot claim/rip progress and the currently revealing item, when a rip is actively in progress. current_break is omitted when the show has no active break at request time. Public data sourced from Fanatics Live's own GraphQL API.
- **Params:** `id` (string, **required**) — Fanatics Live show id, the same id GET /fanaticslive/show/{id} takes

### `fanaticslive_leagues`

- **HTTP:** `GET /fanaticslive/leagues`
- **What:** Get Fanatics Live's league taxonomy. Returns Fanatics Live's full league/category list (e.g. "Pokemon", "NFL", "MTG"). Each entry's type is usable directly with /fanaticslive/browse's league filter. Public data sourced from Fanatics Live's own GraphQL API.
- **Params:** _none_

### `fanaticslive_shop`

- **HTTP:** `GET /fanaticslive/shop/{slug}`
- **What:** Get a Fanatics Live shop's public profile. Returns a Fanatics Live shop's public profile page: description, social links, follower count, and its channels and staffers. Public data sourced from Fanatics Live's own GraphQL API.
- **Params:** `slug` (string, **required**) — Fanatics Live shop slug, e.g. from a shops-list result's slug field

### `fanaticslive_shop_shows`

- **HTTP:** `GET /fanaticslive/shop/{slug}/shows`
- **What:** Get a Fanatics Live shop's own live or replay show list. Returns a Fanatics Live shop's own live/upcoming or past/replay show list -- distinct from /fanaticslive/browse, which lists shows across all shops filtered by league. status=replay is the only credential-free way to observe a COMPLETE-status show. Public data sourced from Fanatics Live's own GraphQL API.
- **Params:** `after` (string, optional) — Pagination cursor from a previous response's next_cursor; `limit` (integer, optional) — Max shows to return (default 24); `slug` (string, **required**) — Fanatics Live shop slug, e.g. from a shops-list result's slug field; `status` (string, **required**) — Which show list to return

### `fanaticslive_shops`

- **HTTP:** `GET /fanaticslive/shops`
- **What:** Get Fanatics Live's shop directory. Returns Fanatics Live's full public shop directory: every shop's id, name, slug, logo, and follower count. Each entry's slug is usable directly with /fanaticslive/shop/{slug}. Public data sourced from Fanatics Live's own GraphQL API.
- **Params:** _none_

### `fanaticslive_show`

- **HTTP:** `GET /fanaticslive/show/{id}`
- **What:** Get a Fanatics Live show's detail page. Returns a Fanatics Live live show's detail page: status, viewers, hosting channel/shop, its currently active break/lot, and its full break/lot list. Public data sourced from Fanatics Live's own GraphQL API.
- **Params:** `id` (string, **required**) — Fanatics Live show id, e.g. from a browse result's id field

## Goldin (5)

### `goldin_auctions`

- **HTTP:** `GET /goldin/auctions`
- **What:** List Goldin's full auction history. Goldin's complete auction event history, back to 2012 -- title, type, status, start/end window, and buyer's premium for every auction Goldin has run. Pass an auction's own id as auction_id to goldin-search to browse its lots.
- **Params:** `order` (string, optional) — asc (oldest first) or desc (newest first, default)

### `goldin_categories`

- **HTTP:** `GET /goldin/categories`
- **What:** List Goldin's search filter enums. Goldin's full filter-enum surface for goldin-search, scoped to one lot pool -- category, sub_category, certification, item_type, and the live auction list (each with its own id, name, and current lot count), plus the sort enum valid for that pool. category/sub_category/certification/item_type are read live from Goldin's own current inventory, not a fixed taxonomy, so results can shift over time. The Auction pool (default) and the Fixed Price "Private Sales" marketplace are disjoint item pools with different certification/item_type values and different sort enums -- pass the same auction_type here and to goldin-search.
- **Params:** `auction_type` (string, optional) — Auction (default) or Fixed_Price -- selects which lot pool to discover enums for

### `goldin_listing`

- **HTTP:** `GET /goldin/listing`
- **What:** Get one Goldin lot's full public detail. One lot's full public detail: title, description, current bid/starting price, auction window and status, grading info, images, and prev/next lot pointers within the same auction. slug is the meta_slug from a goldin-search result (or the trailing path segment of the lot's own goldin.co/item/{slug} page URL).
- **Params:** `slug` (string, **required**) — The lot's meta_slug, from a goldin-search result

### `goldin_search`

- **HTTP:** `GET /goldin/search`
- **What:** Search Goldin's lot auction inventory. Browse or search Goldin's current lot inventory by free-text keyword, category, sub_category, certification, item_type, and auction_id, in a caller-selected sort order. Every filter is optional and combines with AND semantics. All enum values come from goldin-categories -- pass the matching auction_type to both. The Auction pool (default) and the Fixed Price "Private Sales" marketplace are disjoint item pools with different certification/item_type values and different sort enums.
- **Params:** `auction_id` (string, optional) — One auction id from goldin-categories' auctions field -- only meaningful for auction_type Auction; `auction_type` (string, optional) — Auction (default) or Fixed_Price -- selects which lot pool to search; `category` (string, optional) — One value from goldin-categories' category field; `certification` (string, optional) — One value from goldin-categories' certification field; `item_type` (string, optional) — One value from goldin-categories' item_type field; `keyword` (string, optional) — Free-text search across lot titles/descriptions; `page` (integer, optional) — 1-based page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 24, capped at 96; `sort` (string, optional) — One value from goldin-categories' own sort field for the same auction_type. Auction pool: Featured (default), Ending_Soonest, Highest_Bids, Lowest_Bids, Most_Bids, Least_Bids, Most_Recent_Bids, Highest_Lot_Number, Recently_Started. Fixed Price pool: Recently_Created (default), Highest_Bids, Lowest_Bids; `sub_category` (string, optional) — One value from goldin-categories' sub_category field

### `goldin_suggest`

- **HTTP:** `GET /goldin/suggest`
- **What:** Get Goldin's search suggestions for a keyword. Goldin's own search-suggestions/autocomplete for a partial keyword, matching the site's own search box typeahead. keyword is optional -- when omitted, returns Goldin's current trending/popular searches instead of an error.
- **Params:** `keyword` (string, optional) — Partial search query, e.g. \; `limit` (integer, optional) — Max suggestions to return, defaults to 8, capped at 20

## PSA (19)

### `psa_autographfacts_categories`

- **HTTP:** `GET /psa/autographfacts/categories`
- **What:** List PSA AutographFacts categories. PSA AutographFacts' full subject-category list -- the discovery endpoint for the category_id parameter used to browse subjects. Categories span far beyond sports: Baseball, Basketball, Football, Boxing, Golf, Hockey, Soccer, Tennis, MMA, Miscellaneous Sports, Cycling, Olympics, Motorsports, Entertainment, Music, Writers/Authors/Artists, Space Exploration, U.S. Presidents, and Historical & Political Figures.
- **Params:** _none_

### `psa_autographfacts_gallery`

- **HTTP:** `GET /psa/autographfacts/gallery`
- **What:** Get a PSA AutographFacts subject's exemplar image gallery. One autograph subject's full exemplar image gallery: real, captioned examples of authenticated signed items PSA keeps on file for this subject (signed photos, cards, baseballs, letters, contracts, and more), used as authentication reference material. subject_id is the numeric id from a psa-autographfacts-subjects result.
- **Params:** `subject_id` (string, **required**) — Numeric subject id, from a psa-autographfacts-subjects result

### `psa_autographfacts_subject`

- **HTTP:** `GET /psa/autographfacts/subject`
- **What:** Get a PSA AutographFacts subject's profile and price guide. One autograph subject's full public reference page: PSA's own authentication notes (signing habits, forgery risk, signature evolution), a general biography, and a per-item-type price guide (e.g. 3x5/AP card, photo, check, letter, single-signed ball -- item types vary by subject). subject_id is the numeric id from a psa-autographfacts-subjects result.
- **Params:** `subject_id` (string, **required**) — Numeric subject id, from a psa-autographfacts-subjects result

### `psa_autographfacts_subjects`

- **HTTP:** `GET /psa/autographfacts/subjects`
- **What:** List PSA AutographFacts subjects in a category. Every autograph subject PSA AutographFacts lists for one category, each with the numeric subject_id to pass to psa-autographfacts-subject for that subject's full profile and price guide.
- **Params:** `category_id` (integer, **required**) — Category id, from psa-autographfacts-categories

### `psa_cardfacts_categories`

- **HTTP:** `GET /psa/cardfacts/categories`
- **What:** List PSA CardFacts categories. PSA CardFacts' full category list -- the discovery endpoint for the category_id parameter used to browse sets. Nine categories: Baseball, Basketball, Boxing, Football, Golf, Hockey, Misc Sports, Multi-Sport, and Non-Sports/TCG.
- **Params:** _none_

### `psa_cardfacts_checklist`

- **HTTP:** `GET /psa/cardfacts/checklist`
- **What:** Get a PSA CardFacts set's card checklist. One set's full card checklist: every card's name and printed number (number is empty for sets PSA lists without one, e.g. many autograph/player-only card sets). set_id is the numeric id from a psa-cardfacts-sets result.
- **Params:** `set_id` (string, **required**) — Numeric set id, from a psa-cardfacts-sets result

### `psa_cardfacts_sets`

- **HTTP:** `GET /psa/cardfacts/sets`
- **What:** List PSA CardFacts sets in a category. Every card set PSA CardFacts lists for one category, each with the numeric set_id to pass to psa-cardfacts-checklist for that set's full card checklist.
- **Params:** `category_id` (integer, **required**) — Category id, from psa-cardfacts-categories

### `psa_cert_lookup`

- **HTTP:** `GET /psa/cert-lookup`
- **What:** Verify a PSA certification number. Looks up PSA's own public Cert Verification record for one PSA-graded card by its certification number: item title, grade, label type, reverse cert/barcode flag, year, brand/title, subject, card number, category, PSA's own price estimate, and this-cert's-own population figures (population for this exact card+grade, and pop-higher). Scoped to PSA's trading-card department; a cert number issued under a different PSA division (autographs, tickets) returns a not-found error. PSA's full Population Report and Auction Prices Realized both require a PSA/Collectors account login and are not available through this endpoint.
- **Params:** `cert_number` (string, **required**) — PSA certification number, numeric, e.g. \

### `psa_price_guide_categories`

- **HTTP:** `GET /psa/price-guide/categories`
- **What:** List PSA Price Guide categories. PSA Price Guide's full category list -- the discovery endpoint for the category_path parameter used to browse or fetch a set's price table. Every category is a distinct collectible type (Baseball Cards, Basketball Cards, Boxing Cards, Football Cards, Golf Cards, Hockey Cards, Soccer Cards, Non-Sports/TCG Cards, Racing Cards, Sports Tickets, Tennis, Unopened Packs, Presidential Autographs, Sports Autographs, Professional Model/Game-Used Bats, Graded Baseballs).
- **Params:** _none_

### `psa_price_guide_search`

- **HTTP:** `GET /psa/price-guide/search`
- **What:** Search PSA Price Guide. Searches PSA Price Guide by free text (a player/subject name or set name), matching PSA's own site search box. Each result is a matching set with the query's matching cards/items inside it; use a result's category_path, set_path and set_id as the input to psa-price-guide-set to fetch that set's full price table.
- **Params:** `page` (integer, optional) — One-based result page, default 1; `page_size` (integer, optional) — Results per page, default 50, max 100; `query` (string, **required**) — Free-text search term, e.g. a player/subject name or set name

### `psa_price_guide_set`

- **HTTP:** `GET /psa/price-guide/set`
- **What:** Get a PSA Price Guide set's price table. Fetches one PSA Price Guide set's full grade-by-grade price table: every card in the set with PSA's own formatted price per grade column (the set's own grade columns vary -- a vintage set may carry more/lower grade tiers than a modern one). category_path, set_path and set_id together identify the set; use the matching fields from a psa-price-guide-search result, or category_path from psa-price-guide-categories combined with a set_path/set_id found by browsing PSA's own category page.
- **Params:** `category_path` (string, **required**) — Category URL path segment, from psa-price-guide-categories or a psa-price-guide-search result; `set_id` (string, **required**) — PSA's own numeric set id, from a psa-price-guide-search result; `set_path` (string, **required**) — Set URL path segment, from a psa-price-guide-search result

### `psa_probatfacts_categories`

- **HTTP:** `GET /psa/probatfacts/categories`
- **What:** List PSA ProBatFacts categories. PSA ProBatFacts' full player-category list -- the discovery endpoint for the category_id parameter used to browse players. Baseball-bat authentication only, split by Hall of Fame status: Hall of Fame Players, Star Players.
- **Params:** _none_

### `psa_probatfacts_gallery`

- **HTTP:** `GET /psa/probatfacts/gallery`
- **What:** Get a PSA ProBatFacts player's exemplar image gallery. One player's full exemplar image gallery: real, captioned examples of authenticated bats PSA keeps on file for this player, used as authentication reference material. subject_id is the numeric id from a psa-probatfacts-subjects result.
- **Params:** `subject_id` (string, **required**) — Numeric subject id, from a psa-probatfacts-subjects result

### `psa_probatfacts_subject`

- **HTTP:** `GET /psa/probatfacts/subject`
- **What:** Get a PSA ProBatFacts player's bat-authentication reference page. One player's full public reference page: PSA's own bat-authentication notes (professional models used, signature placement) and a general player biography. Unlike psa-autographfacts-subject, this carries no price guide. subject_id is the numeric id from a psa-probatfacts-subjects result.
- **Params:** `subject_id` (string, **required**) — Numeric subject id, from a psa-probatfacts-subjects result

### `psa_probatfacts_subjects`

- **HTTP:** `GET /psa/probatfacts/subjects`
- **What:** List PSA ProBatFacts subjects in a category. Every player PSA ProBatFacts lists for one category, each with the numeric subject_id to pass to psa-probatfacts-subject for that player's full bat-authentication reference page.
- **Params:** `category_id` (integer, **required**) — Category id, from psa-probatfacts-categories

### `psa_ticketfacts_categories`

- **HTTP:** `GET /psa/ticketfacts/categories`
- **What:** List PSA TicketFacts categories. PSA TicketFacts' full event-category list -- the discovery endpoint for the category_id parameter used to browse events. Spans NFL, MLB and NBA historic events: Super Bowl, World Series, MLB All Star Game, Historic Baseball Events, and Historic Basketball Events.
- **Params:** _none_

### `psa_ticketfacts_gallery`

- **HTTP:** `GET /psa/ticketfacts/gallery`
- **What:** Get a PSA TicketFacts event's exemplar image gallery. One event's full exemplar image gallery: real, captioned examples of authenticated tickets from this event PSA keeps on file, used as authentication reference material. subject_id is the numeric id from a psa-ticketfacts-subjects result.
- **Params:** `subject_id` (string, **required**) — Numeric subject id, from a psa-ticketfacts-subjects result

### `psa_ticketfacts_subject`

- **HTTP:** `GET /psa/ticketfacts/subject`
- **What:** Get a PSA TicketFacts event's ticket reference page. One event's full public ticket reference page: PSA's own historical writeup of the event and the ticket(s) involved. Unlike psa-autographfacts-subject, this carries no price guide. subject_id is the numeric id from a psa-ticketfacts-subjects result.
- **Params:** `subject_id` (string, **required**) — Numeric subject id, from a psa-ticketfacts-subjects result

### `psa_ticketfacts_subjects`

- **HTTP:** `GET /psa/ticketfacts/subjects`
- **What:** List PSA TicketFacts subjects in a category. Every event PSA TicketFacts lists for one category, each with the numeric subject_id to pass to psa-ticketfacts-subject for that event's full ticket reference page.
- **Params:** `category_id` (integer, **required**) — Category id, from psa-ticketfacts-categories

## Pristine Auction (3)

### `pristine_auction_categories`

- **HTTP:** `GET /pristine-auction/categories`
- **What:** Discover Pristine Auction's search enum values. Returns the whole value space for pristine-auction-search's category, auction_type, sort, and status params. categories[] is fetched live (with a current listing count per category, refreshed on every call); auction_types[], sort[], and statuses[] are pristineauction.com's own fixed, small search-form value sets.
- **Params:** _none_

### `pristine_auction_lot`

- **HTTP:** `GET /pristine-auction/lot/{lot_number}`
- **What:** Get a Pristine Auction lot's full detail. Returns one pristineauction.com lot's full detail: title, description, image gallery, price (current high bid, or realized/sold price once the auction has ended), auction end time, sport/collectible category, auction type, no-reserve flag, and view/watch/bid counts. lot_number comes from pristine-auction-search's results[].lot_number. Credential-free public data -- see the endpoint markdown for the transport used.
- **Params:** `lot_number` (integer, **required**) — A lot_number from pristine-auction-search's results

### `pristine_auction_search`

- **HTTP:** `GET /pristine-auction/search`
- **What:** Search Pristine Auction's live auction inventory. Browses or searches pristineauction.com's current sports card and memorabilia auction lots. term or category is required, matching pristineauction.com's own search form. All enum values (category, auction_type, sort, status) come from pristine-auction-categories. status=completed browses ended/sold lots (a prices-realized view); the default (all statuses) mirrors the site's own default. Every filter is optional and combines with AND semantics. Credential-free public data -- see the endpoint markdown for the transport used.
- **Params:** `auction_type` (string, optional) — Comma-separated auction-type filter. Omit to include every auction type.; `category` (string, optional) — One value from pristine-auction-categories' categories[].slug. term or category is required.; `max_price` (number, optional) — Maximum current bid price in USD, inclusive. Omit or 0 for no maximum.; `min_price` (number, optional) — Minimum current bid price in USD, inclusive. Omit or 0 for no minimum.; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page. pristineauction.com only accepts 15, 30, or 60; any other value is rejected. Default 30.; `sort` (string, optional) — Result order, default newly-listed.; `status` (string, optional) — Comma-separated auction-status filter. status=completed browses ended/sold lots. Omit to include every status.; `term` (string, optional) — Free-text search across lot titles. term or category is required.
