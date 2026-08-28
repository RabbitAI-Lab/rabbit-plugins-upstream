# resale-secondhand-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**45 endpoints across 7 platform group(s).**

## Poshmark (8)

### `poshmark_brand`

- **HTTP:** `GET /poshmark/brand/{name}`
- **What:** Browse Poshmark listings by brand. Returns a page of normalized Poshmark listings for a given brand name (e.g. Nike), the same browsing view as Poshmark's own brand pages. Pass a previous response's next_max_id back as max_id to fetch the next page. Credential-free public data sourced from Poshmark's own server-rendered brand page and, for pages past the first, Poshmark's own JSON pagination API.
- **Params:** `max_id` (string, optional) — Opaque pagination cursor from a previous response's next_max_id. Omit for the first page; `name` (string, **required**) — Poshmark brand name, matching the path segment of a /brand/{name} URL

### `poshmark_brands`

- **HTTP:** `GET /poshmark/brands`
- **What:** Get the full Poshmark brand directory. Returns Poshmark's full brand directory: every brand Poshmark recognizes (name, slug, logo, known aliases), not just brands with active listings for a given search or category filter. Useful for resolving a brand name to the exact value the brand/search filters expect. Credential-free public data sourced from Poshmark's own server-rendered brand directory page.
- **Params:** _none_

### `poshmark_categories`

- **HTTP:** `GET /poshmark/categories`
- **What:** Get the Poshmark department/category browse taxonomy. Returns Poshmark's full department/category browse taxonomy (e.g. Women > Shoes, Men > Jackets & Coats). Each entry's path resolves directly against the category endpoint. This is reference data that changes rarely, so responses are cached. Credential-free public data sourced from Poshmark's own server-rendered category pages.
- **Params:** _none_

### `poshmark_category`

- **HTTP:** `GET /poshmark/category/{path}`
- **What:** Browse Poshmark listings by category. Returns a page of normalized Poshmark listings for a given category path (e.g. Women-Shoes, Men-Shirts), the same browsing view as Poshmark's own category pages. Pass a previous response's next_max_id back as max_id to fetch the next page. Credential-free public data sourced from Poshmark's own server-rendered category page and, for pages past the first, Poshmark's own JSON pagination API.
- **Params:** `max_id` (string, optional) — Opaque pagination cursor from a previous response's next_max_id. Omit for the first page; `path` (string, **required**) — Poshmark category path segment, e.g. Women-Shoes, Men-Shirts

### `poshmark_closet`

- **HTTP:** `GET /poshmark/closet/{username}`
- **What:** Get Poshmark seller closet (storefront). Returns a normalized Poshmark closet (seller storefront) page: the seller's public profile and reputation stats (followers, ratings, items sold) plus a first page of their currently available listings and total listing count. Pass a previous response's next_max_id back as max_id to fetch the next page of listings; paginated responses omit the seller profile to avoid a second upstream fetch, so fetch without max_id first to get seller fields. Credential-free public data sourced from Poshmark's own server-rendered closet page and, for pages past the first, Poshmark's own JSON pagination API.
- **Params:** `max_id` (string, optional) — Opaque pagination cursor from a previous response's next_max_id. Omit for the first page; `username` (string, **required**) — Poshmark seller username, the path segment of a /closet/{username} URL

### `poshmark_listing`

- **HTTP:** `GET /poshmark/listing/{id}`
- **What:** Get Poshmark listing detail. Returns a normalized Poshmark item-detail page: the full listing (description, all photos, size/brand/condition, inventory), its seller's profile, public comments, and similar listings Poshmark itself surfaces on the same page. Credential-free public data sourced from Poshmark's own server-rendered listing page.
- **Params:** `id` (string, **required**) — Poshmark listing id, the trailing id segment of a /listing/{slug}-{id} URL

### `poshmark_search`

- **HTTP:** `GET /poshmark/search`
- **What:** Search Poshmark listings. Searches Poshmark for clothing, shoes, and accessory listings, returning normalized listing summaries (title, price, brand, size, condition, seller, images) plus the total matching count and an opaque pagination cursor. Pass a previous response's next_max_id back as max_id to fetch the next page. Credential-free public data sourced from Poshmark's own server-rendered search page and, for pages past the first, Poshmark's own JSON pagination API.
- **Params:** `department` (string, optional) — Department filter, e.g. Women, Men, Kids; `max_id` (string, optional) — Opaque pagination cursor from a previous response's next_max_id. Omit for the first page; `query` (string, **required**) — Free-text keyword search

### `poshmark_trend`

- **HTTP:** `GET /poshmark/trend/{id}`
- **What:** Browse a Poshmark trend/showroom collection. Returns a page of normalized Poshmark listings for a curated trend/showroom collection (e.g. "Vintage Celine Handbags"), the same browsing view as Poshmark's own trend pages. Pass a previous response's next_max_id back as max_id to fetch the next page. Credential-free public data sourced from Poshmark's own server-rendered trend page and, for pages past the first, Poshmark's own JSON pagination API.
- **Params:** `id` (string, **required**) — Poshmark trend/showroom id, the trailing id segment of a /trend/{slug}-{id} URL; `max_id` (string, optional) — Opaque pagination cursor from a previous response's next_max_id. Omit for the first page

## Etsy (7)

### `etsy_listing`

- **HTTP:** `GET /etsy/listing/{id}`
- **What:** Get Etsy listing detail. Returns Etsy listing detail: title, price, images, materials, tags, and shop.
- **Params:** `id` (string, **required**) — Numeric Etsy listing id

### `etsy_listing_reviews`

- **HTTP:** `GET /etsy/listing/{id}/reviews`
- **What:** Get Etsy listing reviews. Returns buyer reviews for an Etsy listing.
- **Params:** `id` (string, **required**) — Numeric Etsy listing id; `offset` (integer, optional) — 0-based review offset; `sort` (string, optional) — Review sort order

### `etsy_search`

- **HTTP:** `GET /etsy/search`
- **What:** Search Etsy listings. Returns Etsy product search results across shops for a keyword query.
- **Params:** `limit` (integer, optional) — Page size (default 36, max 100); `offset` (integer, optional) — 0-based result offset; `q` (string, **required**) — Search keywords

### `etsy_shop`

- **HTTP:** `GET /etsy/shop/{id}`
- **What:** Get Etsy shop profile. Returns an Etsy shop profile: seller, headline, rating, and sold count. Accepts a numeric shop id or a shop name.
- **Params:** `id` (string, **required**) — Numeric Etsy shop id or shop name

### `etsy_shop_listings`

- **HTTP:** `GET /etsy/shop/{id}/listings`
- **What:** Get an Etsy shop's listings. Returns a shop's listing catalog, optionally filtered by keyword. Accepts a numeric shop id or a shop name.
- **Params:** `id` (string, **required**) — Numeric Etsy shop id or shop name; `limit` (integer, optional) — Page size (default 24); `offset` (integer, optional) — 0-based listing offset; `q` (string, optional) — Keyword filter within the shop's own catalog

### `etsy_shop_reviews`

- **HTTP:** `GET /etsy/shop/{id}/reviews`
- **What:** Get Etsy shop reviews. Returns buyer reviews for an Etsy shop. Accepts a numeric shop id or a shop name.
- **Params:** `id` (string, **required**) — Numeric Etsy shop id or shop name; `limit` (integer, optional) — Page size (default 14); `offset` (integer, optional) — 0-based review offset

### `etsy_shop_search`

- **HTTP:** `GET /etsy/shop/search`
- **What:** Search Etsy shops. Returns Etsy shops matching a keyword.
- **Params:** `limit` (integer, optional) — Max shops to return (default 10); `q` (string, **required**) — Shop search keyword

## Vinted (7)

### `vinted_brand`

- **HTTP:** `GET /vinted/brand`
- **What:** Vinted listings for a brand. Returns Vinted listings for a specific brand, with optional price filtering and sort order. `order` values: `relevance`, `newest_first`, `price_high_to_low`, `price_low_to_high`. Public data, sourced from Vinted's own server-rendered brand page.
- **Params:** `id` (string, **required**) — Numeric Vinted brand ID, from a /vinted/item result's brand link; `order` (string, optional) — Sort order. Allowed values: relevance, newest_first, price_high_to_low, price_low_to_high; `page` (integer, optional) — Page number, starting at 1; `price_from` (number, optional) — Minimum price; `price_to` (number, optional) — Maximum price

### `vinted_brands`

- **HTTP:** `GET /vinted/brands`
- **What:** Vinted popular-brands directory. Returns Vinted's "Popular brands" directory. This is Vinted's own curated list, not an exhaustive list of every brand in its catalog. Each entry's `id` is usable directly as the `id` query parameter to /vinted/brand. Public data, sourced from Vinted's own server-rendered brands page.
- **Params:** _none_

### `vinted_catalog`

- **HTTP:** `GET /vinted/catalog`
- **What:** Vinted listing search. Returns Vinted resale listings matching a text search, with optional price filtering and sort order. `order` values: `relevance`, `newest_first`, `price_high_to_low`, `price_low_to_high`. Public data, sourced from Vinted's own server-rendered catalog page.
- **Params:** `order` (string, optional) — Sort order. Allowed values: relevance, newest_first, price_high_to_low, price_low_to_high; `page` (integer, optional) — Page number, starting at 1; `price_from` (number, optional) — Minimum price; `price_to` (number, optional) — Maximum price; `search_text` (string, **required**) — Search text

### `vinted_categories`

- **HTTP:** `GET /vinted/categories`
- **What:** Vinted top-level catalog categories. Returns Vinted's top-level catalog categories (e.g. Women, Men, Kids, Home, Electronics, Sports, Entertainment, Hobbies & collectibles). This is the root level only -- Vinted's full category tree goes several levels deeper on the live site, but deeper levels aren't server-rendered so aren't covered here. Each entry's `id` is usable directly as the `id` query parameter to /vinted/category. Public data, sourced from Vinted's own server-rendered catalog navigation.
- **Params:** _none_

### `vinted_category`

- **HTTP:** `GET /vinted/category`
- **What:** Vinted listings for a category. Returns Vinted listings for a specific category, with optional price filtering and sort order. `order` values: `relevance`, `newest_first`, `price_high_to_low`, `price_low_to_high`. Public data, sourced from Vinted's own server-rendered category page.
- **Params:** `id` (string, **required**) — Numeric Vinted category ID, from a /vinted/item result's categories breadcrumb link; `order` (string, optional) — Sort order. Allowed values: relevance, newest_first, price_high_to_low, price_low_to_high; `page` (integer, optional) — Page number, starting at 1; `price_from` (number, optional) — Minimum price; `price_to` (number, optional) — Maximum price

### `vinted_item`

- **HTTP:** `GET /vinted/item`
- **What:** A single Vinted listing's detail. Returns a single Vinted listing's detail: title, description, brand, size, condition, material, color, price, category breadcrumb, and photos. Public data, sourced from Vinted's own server-rendered item page.
- **Params:** `id` (string, **required**) — Numeric Vinted item ID, from a /vinted/catalog result's id field

### `vinted_member`

- **HTTP:** `GET /vinted/member`
- **What:** A Vinted seller's public storefront profile. Returns a Vinted seller's public storefront profile: username, self-disclosed coarse location, rating, and follower/following counts. Deliberately excludes online-presence and activity data (last-seen timestamps, upload-frequency badges) present on the live page. Public data, sourced from Vinted's own server-rendered member page.
- **Params:** `id` (string, **required**) — Numeric Vinted member ID, from a /vinted/item result's seller link

## StockX (5)

### `stockx_brands`

- **HTTP:** `GET /stockx/brands`
- **What:** Get StockX brand catalog. Returns StockX's full brand catalog (name and URL slug for every brand in its own brand directory), suitable for building GET /stockx/search's brand parameter or GET /stockx/search's model parameter's required single-brand context. Credential-free public data from the same navigation API backing StockX's own site menu.
- **Params:** _none_

### `stockx_categories`

- **HTTP:** `GET /stockx/categories`
- **What:** Get StockX category/subcategory taxonomy. Returns StockX's full category/subcategory reference: the 7 top-level categories accepted by GET /stockx/search's category parameter, each with its subcategories (e.g. Shoes -> Boots, Cleats, Clogs). Credential-free public data from the same navigation API backing StockX's own site menu.
- **Params:** _none_

### `stockx_product`

- **HTTP:** `GET /stockx/product/{slug}`
- **What:** Get StockX product detail. Returns a normalized StockX product: identity (title, brand, model, colorway, style id, retail price, release date, description, image), current market data (lowest ask, highest bid, last sale, trailing average price/sales count, delivery-speed ask tiers), individual seller listings (price, condition, size), related-product recommendations (other colorways/siblings StockX surfaces on the product page), and any promotional badges. Credential-free public data from StockX's own product-page GraphQL API.
- **Params:** `slug` (string, **required**) — StockX product URL slug (the urlKey), the path segment of a https://stockx.com/{slug} product page

### `stockx_releases`

- **HTTP:** `GET /stockx/releases`
- **What:** Get StockX upcoming release calendar. Returns a date-ordered page (release date ascending) of StockX's upcoming release calendar: new and restocked products releasing on or after the given date, with normalized product summaries, headline pricing, and each item's published release date. Credential-free public data from the same GraphQL API backing StockX's own releases page.
- **Params:** `from` (string, optional) — Only include releases on or after this date (YYYY-MM-DD, UTC). Defaults to today; `limit` (integer, optional) — Results per page, defaults to 20, maximum 100; `page` (integer, optional) — 1-indexed result page, defaults to 1

### `stockx_search`

- **HTTP:** `GET /stockx/search`
- **What:** Search/browse StockX products. Browses StockX's product catalog by category with optional free-text keyword search and facet filters (gender, brand, color, shoe height, activity, availability), returning normalized product summaries with headline pricing plus the total matching count. Credential-free public data from the same GraphQL API backing StockX's own category browse pages.
- **Params:** `activity` (string, optional) — Filter by activity, comma-separated for multiple values; `available_now` (boolean, optional) — Only include products with at least one active ask; `below_retail` (boolean, optional) — Only include products currently trading below original retail price; `brand` (string, optional) — Filter by one or more brand slugs, comma-separated, e.g. jordan,nike; `category` (string, **required**) — StockX top-level category; `color` (string, optional) — Filter by color, comma-separated for multiple values; `gender` (string, optional) — Filter by gender, comma-separated for multiple values; `limit` (integer, optional) — Results per page, defaults to 20, maximum 100; `model` (string, optional) — Filter by a single model slug, e.g. air-force-1. Requires exactly one value in brand; `page` (integer, optional) — 1-indexed result page, defaults to 1; `query` (string, optional) — Free-text keyword search within the category, e.g. a model name or colorway; `shoe_height` (string, optional) — Filter by shoe height, comma-separated for multiple values; `sort` (string, optional) — Result sort order, defaults to featured; `xpress_ship` (boolean, optional) — Only include products with StockX Xpress Ship availability

## Mercari (5)

### `mercari_autocomplete`

- **HTTP:** `GET /mercari/autocomplete`
- **What:** Mercari search autocomplete. Returns Mercari's own search-suggestion list for a partial keyword, in the upstream's own relevance order. An empty suggestion list is a normal outcome for obscure or gibberish input. Credential-free public data sourced from Mercari's own mobile-app API using an anonymous, login-free session.
- **Params:** `query` (string, **required**) — Partial keyword to get suggestions for

### `mercari_home`

- **HTTP:** `GET /mercari/home`
- **What:** Get Mercari home feed. Returns Mercari's own curated home-feed recommendations: normalized listing summaries (title, price, thumbnail, condition, seller). Credential-free public data sourced from Mercari's own mobile-app API using an anonymous, login-free session.
- **Params:** _none_

### `mercari_item`

- **HTTP:** `GET /mercari/item/{id}`
- **What:** Get Mercari item detail. Returns a normalized Mercari item-detail page: description, all photos, price, condition, category, hashtags, the shipping origin state, and a "similar items" carousel of related listings. Credential-free public data sourced from Mercari's own mobile-app API using an anonymous, login-free session.
- **Params:** `id` (string, **required**) — Mercari item id, e.g. from a search result's id field

### `mercari_master`

- **HTTP:** `GET /mercari/master`
- **What:** Get Mercari full taxonomy (categories, brands, sizes). Returns Mercari's full reference taxonomy in one call: every category (with parent linkage), every recognized brand, and every clothing/shoe/apparel size. Large (tens of thousands of brand entries) and effectively static -- cache this response rather than polling it. Credential-free public data sourced from Mercari's own mobile-app API using an anonymous, login-free session.
- **Params:** _none_

### `mercari_search`

- **HTTP:** `GET /mercari/search`
- **What:** Search Mercari listings. Searches Mercari's live resale marketplace by free-text keyword, returning normalized listing summaries (title, price, thumbnail, condition, seller) plus the total matching count. Credential-free public data sourced from Mercari's own mobile-app API using an anonymous, login-free session.
- **Params:** `query` (string, **required**) — Free-text keyword search

## Depop (10)

### `depop_brands`

- **HTTP:** `GET /depop/brands`
- **What:** Depop's full brand directory. Returns Depop's full brand directory (id, name, slug), not just brands with active listings for a given search -- resolves the search endpoint's otherwise-opaque brand_ids filter to human-readable names. Public data sourced from Depop's own brand-directory API.
- **Params:** _none_

### `depop_categories`

- **HTTP:** `GET /depop/categories`
- **What:** Get Depop's category taxonomy. Returns Depop's full department, category, and subcategory taxonomy -- every value usable with /depop/search's and /depop/shop/{username}'s category/subcategory filters. Tries a live refresh from Depop's own category-filter API first and falls back to a static snapshot on any failure, so this never errors.
- **Params:** _none_

### `depop_item`

- **HTTP:** `GET /depop/item/{slug}`
- **What:** Get Depop item detail. Returns a normalized Depop item-detail page: description, all photos, price, condition, brand, size, seller info, and a "similar items" carousel when the page has one. Public data sourced from Depop's own item pages.
- **Params:** `slug` (string, **required**) — Depop item URL slug, e.g. from a search result's id field

### `depop_item_similar`

- **HTTP:** `GET /depop/item/{slug}/similar`
- **What:** Get Depop items similar to a listing. Returns items similar to a given Depop listing, via Depop's dedicated similar-items API -- richer and paginated (up to 150 per page) compared to the small, non-paginated "similar items" carousel already included in item detail. Public data sourced from Depop's own similar-items API.
- **Params:** `after` (string, optional) — Opaque pagination cursor from a previous response's next_cursor field. Omit for the first page.; `limit` (integer, optional) — Max results per page, 1-150; `slug` (string, **required**) — Depop item URL slug, e.g. from a search result's id field

### `depop_search`

- **HTTP:** `GET /depop/search`
- **What:** Search Depop listings. Searches Depop's resale-fashion marketplace by free-text keyword, with optional price, condition, colour, category, subcategory, gender, kids-department, brand, discount, and sort filters, returning normalized listing summaries (title, price, brand, condition, like count, photos, sizes), a pagination cursor, and the total matching count. Public data sourced from Depop's own search API.
- **Params:** `after` (string, optional) — Opaque pagination cursor from a previous response's next_cursor field. Omit for the first page.; `brand_ids` (string, optional) — Comma-separated Depop internal numeric brand ids. Not documented by Depop -- find a brand's id by browsing its depop.com/brands/<slug>/ page.; `category` (string, optional) — Depop category slug: tops, bottoms, dresses, coats-jackets, jumpsuit-and-playsuit, suits, footwear, accessories, nightwear, underwear, swim-beach-wear, fancy-dress, sleepsuits-and-bodysuits, bundles, beauty, face-masks, home, tech-accessories, film, art, books-and-magazine, music, party-supplies, sports-equipment-accesories, toys, umbrella. See GET /depop/categories for a machine-readable enumeration with names and subcategories.; `colours` (string, optional) — Comma-separated colour filter: black, grey, white, brown, tan, cream, yellow, red, burgundy, orange, pink, purple, blue, navy, green, khaki, multi; `condition` (string, optional) — Comma-separated condition filter: brand_new, used_like_new, used_excellent, used_good, used_fair; `gender` (string, optional) — Department filter: female, male; `is_kids` (boolean, optional) — Kids-department filter: true restricts results to kids items only, false excludes them, omitted returns both.; `on_sale` (boolean, optional) — Restrict results to discounted listings; `price_max` (number, optional) — Maximum listing price in USD; `price_min` (number, optional) — Minimum listing price in USD; `query` (string, **required**) — Free-text keyword search; `sizes` (string, optional) — Comma-separated Depop size composite ids (format {size_set_id}.{id}, e.g. \; `sort` (string, optional) — Sort order: relevance, price_low_to_high, price_high_to_low; `subcategory` (string, optional) — Comma-separated Depop subcategory slug(s), scoped within category. See GET /depop/categories for the full list per category.

### `depop_search_facets`

- **HTTP:** `GET /depop/search/facets`
- **What:** Depop search result-count breakdowns. Returns result-count breakdowns per department/category/subcategory for a search query, via Depop's dedicated aggregates API -- a distinct upstream call from search itself, not embedded in its response. Public data sourced from Depop's own search-aggregates API.
- **Params:** `query` (string, **required**) — Free-text keyword search

### `depop_search_sellers`

- **HTTP:** `GET /depop/search-sellers`
- **What:** Search Depop sellers by name. Finds Depop users/sellers by name or username. A matched result's username can be passed directly to GET /depop/shop/{username} for that seller's full shop. Public data sourced from Depop's own user-search API.
- **Params:** `query` (string, **required**) — Seller name or username to search for

### `depop_shop`

- **HTTP:** `GET /depop/shop/{username}`
- **What:** Get a Depop seller's shop. Returns a Depop seller's public shop: profile (rating, sold count, followers, bio) plus current listings, with optional price, condition, colour, category, subcategory, gender, discount, and sort filters. Public data sourced from Depop's own shop pages.
- **Params:** `category` (string, optional) — Depop category slug: tops, bottoms, dresses, coats-jackets, jumpsuit-and-playsuit, suits, footwear, accessories, nightwear, underwear, swim-beach-wear, fancy-dress, sleepsuits-and-bodysuits, bundles, beauty, face-masks, home, tech-accessories, film, art, books-and-magazine, music, party-supplies, sports-equipment-accesories, toys, umbrella. See GET /depop/categories for a machine-readable enumeration with names and subcategories.; `colours` (string, optional) — Comma-separated colour filter: black, grey, white, brown, tan, cream, yellow, red, burgundy, orange, pink, purple, blue, navy, green, khaki, multi; `condition` (string, optional) — Comma-separated condition filter: brand_new, used_like_new, used_excellent, used_good, used_fair; `gender` (string, optional) — Department filter: female, male; `on_sale` (boolean, optional) — Restrict results to discounted listings; `price_max` (number, optional) — Maximum listing price in USD; `price_min` (number, optional) — Minimum listing price in USD; `sizes` (string, optional) — Comma-separated Depop size composite ids (format {size_set_id}.{id}, e.g. \; `sort` (string, optional) — Sort order: relevance, price_low_to_high, price_high_to_low, recently_listed; `subcategory` (string, optional) — Comma-separated Depop subcategory slug(s), scoped within category. See GET /depop/categories for the full list per category.; `username` (string, **required**) — Depop seller username, e.g. from a shop page URL segment

### `depop_sizes`

- **HTTP:** `GET /depop/sizes`
- **What:** Get Depop's size taxonomy. Returns Depop's full, multi-region size taxonomy -- every composite id usable with /depop/search's and /depop/shop/{username}'s sizes filter. Public data sourced from Depop's own size-filter API.
- **Params:** _none_

### `depop_suggest`

- **HTTP:** `GET /depop/suggest`
- **What:** Depop search-box autocomplete. Returns Depop's own search-box autocomplete suggestions for a partial query, including the category a suggestion maps to when relevant. Public data sourced from Depop's own search-suggestions API.
- **Params:** `query` (string, **required**) — Partial search query to autocomplete

## Whatnot (3)

### `whatnot_browse`

- **HTTP:** `GET /whatnot/browse`
- **What:** Browse Whatnot live shows by category. Returns the live and upcoming shows currently listed under a Whatnot category: seller, title, status, start time, thumbnail, and tags. Public data sourced from Whatnot's own GraphQL API.
- **Params:** `category` (string, **required**) — Whatnot category slug. See GET /whatnot/categories for the full list.

### `whatnot_categories`

- **HTTP:** `GET /whatnot/categories`
- **What:** Get Whatnot's category list. Returns Whatnot's full top-level category list (e.g. "Trading Card Games", "Sneakers & Streetwear"). Each entry's slug is usable directly with /whatnot/browse's category filter. Public data sourced from Whatnot's own GraphQL API.
- **Params:** _none_

### `whatnot_live`

- **HTTP:** `GET /whatnot/live/{id}`
- **What:** Get a Whatnot live show's current shop feed. Returns a Whatnot live show's current shop feed: every product, auction, and giveaway listing currently visible in the show, each with its seller's rating. Public data sourced from Whatnot's own GraphQL API.
- **Params:** `id` (string, **required**) — Whatnot live show id, e.g. from a browse result's id field
