# product-price-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**124 endpoints across 20 platform group(s).**

## Amazon (3)

### `amazon_product`

- **HTTP:** `GET /amazon/product/{asin}`
- **What:** Retrieve Amazon product details. Returns normalized product details for an Amazon ASIN on `amazon.com`, including pricing, availability, overview data, inline review samples, and descriptive content.
- **Params:** `asin` (string, **required**) — Amazon ASIN; `currency` (string, optional) — Amazon currency; `language` (string, optional) — Amazon language

### `amazon_search`

- **HTTP:** `GET /amazon/search`
- **What:** Search Amazon products. Returns normalized Amazon search result cards for `amazon.com`.
- **Params:** `k` (string, **required**) — Search keyword; `page` (integer, optional) — 1-based page number; `s` (string, optional) — Sort order

### `amazon_suggest`

- **HTTP:** `GET /amazon/suggest/{keyword}`
- **What:** Retrieve Amazon search suggestions. Returns typeahead keyword suggestions from Amazon's public suggestion API for `amazon.com`.
- **Params:** `keyword` (string, **required**) — Suggestion prefix

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

## Shopify (11)

### `shopify_collection_products`

- **HTTP:** `GET /shopify/collections/{handle}/products`
- **What:** List Shopify collection products. Returns normalized products from a public Shopify collection `/products.json` endpoint.
- **Params:** `handle` (string, **required**) — Collection handle; `limit` (integer, optional) — Maximum products, defaults to 50 and supports up to 250; `page` (integer, optional) — 1-based page, defaults to 1; `url` (string, **required**) — Shopify storefront URL

### `shopify_collections`

- **HTTP:** `GET /shopify/collections`
- **What:** List Shopify collections. Returns normalized collections from a public Shopify `/collections.json` endpoint. Valid empty result pages return `200` with an empty collections array.
- **Params:** `limit` (integer, optional) — Maximum collections, defaults to 50 and supports up to 250; `page` (integer, optional) — 1-based page, defaults to 1; `url` (string, **required**) — Shopify storefront URL

### `shopify_page`

- **HTTP:** `GET /shopify/pages/{handle}`
- **What:** Get Shopify page. Returns normalized page detail from Shopify's credential-free `/pages/{handle}.json` endpoint. Page body HTML is returned as cleaned text only.
- **Params:** `handle` (string, **required**) — Page handle; `url` (string, **required**) — Shopify storefront URL

### `shopify_pages`

- **HTTP:** `GET /shopify/pages`
- **What:** List Shopify pages. Returns normalized static pages from a public Shopify `/pages.json` endpoint. Page body HTML is returned as cleaned text only.
- **Params:** `limit` (integer, optional) — Maximum pages, defaults to 50 and supports up to 250; `page` (integer, optional) — 1-based page, defaults to 1; `url` (string, **required**) — Shopify storefront URL

### `shopify_product`

- **HTTP:** `GET /shopify/products/{handle}`
- **What:** Get Shopify product. Returns normalized product detail from Shopify's credential-free product handle `.js` endpoint.
- **Params:** `handle` (string, **required**) — Product handle; `url` (string, **required**) — Shopify storefront URL

### `shopify_product_recommendations`

- **HTTP:** `GET /shopify/products/{handle}/recommendations`
- **What:** List Shopify product recommendations. Returns normalized recommended products from Shopify's credential-free recommendations Ajax endpoint. The route handle is resolved to a Shopify product id before fetching recommendations.
- **Params:** `handle` (string, **required**) — Product handle; `intent` (string, optional) — Recommendation intent. Allowed values: related, complementary; `limit` (integer, optional) — Maximum products, defaults to 10 and supports up to 20; `url` (string, **required**) — Shopify storefront URL

### `shopify_products`

- **HTTP:** `GET /shopify/products`
- **What:** List Shopify products. Returns normalized products from a public Shopify `/products.json` endpoint. Valid empty result pages return `200` with an empty products array.
- **Params:** `limit` (integer, optional) — Maximum products, defaults to 50 and supports up to 250; `page` (integer, optional) — 1-based page, defaults to 1; `url` (string, **required**) — Shopify storefront URL

### `shopify_search_suggest`

- **HTTP:** `GET /shopify/search/suggest`
- **What:** Get Shopify search suggestions. Returns products, collections, and query suggestions from Shopify's credential-free predictive search Ajax endpoint.
- **Params:** `limit` (integer, optional) — Maximum results per type, defaults to 10 and supports up to 20; `q` (string, **required**) — Search query; `types` (string, optional) — Comma-separated suggestion types. Allowed values: product, collection, query; `url` (string, **required**) — Shopify storefront URL

### `shopify_sitemap_urls`

- **HTTP:** `GET /shopify/sitemap/urls`
- **What:** List Shopify sitemap URLs. Fetches capped URL entries from Shopify child sitemaps matching the requested type.
- **Params:** `limit` (integer, optional) — Maximum URL entries, defaults to 50 and supports up to 250; `type` (string, optional) — Sitemap type. Allowed values: all, products, collections, pages, blogs, agentic_discovery, other; `url` (string, **required**) — Shopify storefront URL

### `shopify_sitemaps`

- **HTTP:** `GET /shopify/sitemaps`
- **What:** List Shopify sitemaps. Returns child sitemap URLs from a public Shopify `/sitemap.xml` index with inferred sitemap types.
- **Params:** `url` (string, **required**) — Shopify storefront URL

### `shopify_store`

- **HTTP:** `GET /shopify/store`
- **What:** Get Shopify store metadata. Resolves a public Shopify storefront and returns normalized metadata from credential-free storefront JSON. If the vanity domain blocks `/products.json`, the service may fall back to a public `*.myshopify.com` domain discovered from the storefront page.
- **Params:** `url` (string, **required**) — Shopify storefront URL

## Shop.app (16)

### `shop_app_analysis`

- **HTTP:** `GET /shop-app/analysis`
- **What:** Analyze Shop.app query results. Returns a market snapshot derived from Shop.app search results, including price ranges, currencies, sale counts, discounts, and top shops. Limit defaults to 20 and accepts values up to 50.
- **Params:** `deep_search` (boolean, optional) — Enable Shop.app deep search mode; `in_stock` (boolean, optional) — Request in-stock products; `limit` (integer, optional) — Maximum products to analyze, defaults to 20 and supports up to 50; `on_sale` (boolean, optional) — Request sale products; `query` (string, **required**) — Search query

### `shop_app_categories`

- **HTTP:** `GET /shop-app/categories`
- **What:** List Shop.app categories. Returns public Shop.app product categories.
- **Params:** _none_

### `shop_app_collection_products`

- **HTTP:** `GET /shop-app/shops/{handle}/collections/{collection_id}/products`
- **What:** List Shop.app collection products. Returns public product cards from a Shop.app merchant collection. sort_by allowed values: MOST_SALES, PRICE_LOW_TO_HIGH, PRICE_HIGH_TO_LOW, RELEVANCE.
- **Params:** `collection_id` (string, **required**) — Collection id; `handle` (string, **required**) — Shop handle; `in_stock` (boolean, optional) — Request in-stock products; `limit` (integer, optional) — Maximum products, defaults to 30 and supports up to 60; `sort_by` (string, optional) — Sort mode

### `shop_app_product`

- **HTTP:** `GET /shop-app/products/{id}`
- **What:** Get Shop.app product. Returns normalized public product details from Shop.app.
- **Params:** `id` (string, **required**) — Product id; `variant_id` (string, optional) — Variant id

### `shop_app_product_related`

- **HTTP:** `GET /shop-app/products/{id}/related`
- **What:** List Shop.app related products. Returns related product cards from a public Shop.app product page.
- **Params:** `id` (string, **required**) — Product id; `limit` (integer, optional) — Maximum products, defaults to 20 and supports up to 50

### `shop_app_product_reviews`

- **HTTP:** `GET /shop-app/products/{id}/reviews`
- **What:** List Shop.app product reviews. Returns public product reviews from a Shop.app product page.
- **Params:** `id` (string, **required**) — Product id; `limit` (integer, optional) — Maximum reviews, defaults to 20 and supports up to 50

### `shop_app_product_shop`

- **HTTP:** `GET /shop-app/products/{id}/shop`
- **What:** Get the Shop.app shop for a product. Resolves the public Shop.app merchant profile for a product id.
- **Params:** `id` (string, **required**) — Product id

### `shop_app_product_variant`

- **HTTP:** `GET /shop-app/products/{id}/variant`
- **What:** Get a Shop.app product variant by selected options. Returns the exact public product variant matching selected options. selected_options must be a JSON object when provided. Repeated option filters may also be sent as option.Name=value or option[Name]=value.
- **Params:** `id` (string, **required**) — Product id; `selected_options` (string, optional) — Selected options JSON object

### `shop_app_product_variants`

- **HTTP:** `GET /shop-app/products/{id}/variants`
- **What:** List Shop.app product variants. Returns adjacent variants for a Shop.app product. selected_options must be a JSON object when provided. Repeated option filters may also be sent as option.Name=value or option[Name]=value.
- **Params:** `id` (string, **required**) — Product id; `limit` (integer, optional) — Maximum variants, defaults to 50 and supports up to 100; `selected_options` (string, optional) — Selected options JSON object

### `shop_app_search`

- **HTTP:** `GET /shop-app/search`
- **What:** Search Shop.app products. Searches Shop.app product results using the credential-free public web search flow. Limit defaults to 20 and accepts values up to 50.
- **Params:** `deep_search` (boolean, optional) — Enable Shop.app deep search mode; `in_stock` (boolean, optional) — Request in-stock products; `limit` (integer, optional) — Maximum products, defaults to 20 and supports up to 50; `on_sale` (boolean, optional) — Request sale products; `query` (string, **required**) — Search query

### `shop_app_shop`

- **HTTP:** `GET /shop-app/shops/{handle}`
- **What:** Get Shop.app shop. Returns public Shop.app merchant profile details.
- **Params:** `handle` (string, **required**) — Shop handle

### `shop_app_shop_locations`

- **HTTP:** `GET /shop-app/shops/{handle}/locations`
- **What:** List Shop.app shop locations. Returns public retail locations for a Shop.app merchant profile.
- **Params:** `handle` (string, **required**) — Shop handle; `limit` (integer, optional) — Maximum locations, defaults to 10 and supports up to 50

### `shop_app_shop_products`

- **HTTP:** `GET /shop-app/shops/{handle}/products`
- **What:** List Shop.app shop products. Returns public product cards from a Shop.app merchant profile. sort_by allowed values: MOST_SALES, PRICE_LOW_TO_HIGH, PRICE_HIGH_TO_LOW, RELEVANCE.
- **Params:** `handle` (string, **required**) — Shop handle; `in_stock` (boolean, optional) — Request in-stock products; `limit` (integer, optional) — Maximum products, defaults to 30 and supports up to 60; `sort_by` (string, optional) — Sort mode

### `shop_app_shop_reviews`

- **HTTP:** `GET /shop-app/shops/{handle}/reviews`
- **What:** List Shop.app shop reviews. Returns public reviews for a Shop.app merchant profile.
- **Params:** `handle` (string, **required**) — Shop handle; `limit` (integer, optional) — Maximum reviews, defaults to 20 and supports up to 50

### `shop_app_shop_typeahead`

- **HTTP:** `GET /shop-app/shops/{handle}/typeahead`
- **What:** Suggest products and collections inside a Shop.app shop. Returns public store typeahead suggestions for a Shop.app merchant profile.
- **Params:** `handle` (string, **required**) — Shop handle; `limit` (integer, optional) — Maximum suggestions, defaults to 20 and supports up to 20; `query` (string, **required**) — Typeahead query

### `shop_app_suggestions`

- **HTTP:** `GET /shop-app/suggestions`
- **What:** Suggest Shop.app searches. Returns Shop.app autocomplete suggestions. Limit defaults to 10 and supports up to 20.
- **Params:** `limit` (integer, optional) — Maximum suggestions, defaults to 10 and supports up to 20; `query` (string, **required**) — Search query

## Target (7)

### `target_categories`

- **HTTP:** `GET /target/categories`
- **What:** List all Target categories. Returns Target's current top-level category menu and the complete grouped shop-all directory, including category ids and canonical URLs.
- **Params:** _none_

### `target_category_products`

- **HTTP:** `GET /target/category-products`
- **What:** Browse Target category products. Returns paginated products for any category id from target-categories. Each response also contains every available dynamic filter group and option. Pass selected option ids through filter_ids as a comma-separated list. The sort enum accepts `relevance`, `featured`, `price-low`, `price-high`, `rating`, `bestselling`, and `newest`.
- **Params:** `category_id` (string, **required**) — Target category id; `filter_ids` (string, optional) — Comma-separated Target filter option ids; `page` (integer, optional) — One-based page (1-50); `sort` (string, optional) — Result order; `store_id` (integer, optional) — Target store id used for pricing

### `target_filter_options`

- **HTTP:** `GET /target/filter-options`
- **What:** List Target filter options. Returns every dynamic filter group and option for either a product query or category. Provide exactly one of q or category_id. Pass currently selected option ids through filter_ids to obtain the remaining context-aware options.
- **Params:** `category_id` (string, optional) — Target category id; mutually exclusive with q; `filter_ids` (string, optional) — Comma-separated selected Target filter option ids; `q` (string, optional) — Product search query; mutually exclusive with category_id; `store_id` (integer, optional) — Target store id used for pricing

### `target_product`

- **HTTP:** `GET /target/product`
- **What:** Get a Target product. Returns normalized product details for one Target item, including product content, images, price, rating, category, and availability flags for the selected store.
- **Params:** `store_id` (integer, optional) — Target store id used for pricing and availability; `tcin` (string, **required**) — Numeric Target item id (TCIN)

### `target_questions`

- **HTTP:** `GET /target/questions`
- **What:** List Target product questions and answers. Returns paginated product questions with their nested answers.
- **Params:** `page` (integer, optional) — Zero-based page; `per_page` (integer, optional) — Questions per page; `tcin` (string, **required**) — Numeric Target item id

### `target_reviews`

- **HTTP:** `GET /target/reviews`
- **What:** List Target product reviews. Returns paginated written reviews for a Target item. Pagination is zero-based and page 50 is the upstream maximum.
- **Params:** `page` (integer, optional) — Zero-based page; `per_page` (integer, optional) — Reviews per page; `tcin` (string, **required**) — Numeric Target item id

### `target_search`

- **HTTP:** `GET /target/search`
- **What:** Search Target products. Searches Target products and returns normalized products plus every filter group and option available for the current result set. Pass option ids back through filter_ids as a comma-separated list. A zero total with an empty products list is a valid no-results response. The sort enum accepts `relevance`, `featured`, `price-low`, `price-high`, `rating`, `bestselling`, and `newest`.
- **Params:** `filter_ids` (string, optional) — Comma-separated Target filter option ids; `page` (integer, optional) — One-based page (1-50); `q` (string, **required**) — Product search query; `sort` (string, optional) — Result order; `store_id` (integer, optional) — Target store id used for pricing

## Costco (6)

### `costco_categories`

- **HTTP:** `GET /costco/categories`
- **What:** Get Costco category facets. Returns Costco category slugs and product counts relevant to an optional search term, each slug usable directly with GET /costco/search's category filter. Public data sourced from Costco's own search backend.
- **Params:** `query` (string, optional) — Search text to scope the returned categories to, e.g. \

### `costco_product`

- **HTTP:** `GET /costco/product/{id}`
- **What:** Get a Costco product's detail. Returns a Costco product's detail: title, description, manufacturer, image, price, stock status, and rating. Public data sourced from Costco's own product backend.
- **Params:** `id` (string, **required**) — Costco product id, e.g. from a search result's id field or a product page URL's \

### `costco_product_availability`

- **HTTP:** `GET /costco/product/{id}/availability`
- **What:** Get a Costco product's delivery estimate. Returns a Costco product's stock and estimated-delivery status for a delivery destination. Public data sourced from Costco's own fulfillment backend.
- **Params:** `id` (string, **required**) — Costco product id; `postal_code` (string, **required**) — US destination ZIP code; `state` (string, **required**) — US destination two-letter state code

### `costco_product_reviews`

- **HTTP:** `GET /costco/product/{id}/reviews`
- **What:** Get a Costco product's reviews. Returns a page of a Costco product's reviews: title, text, rating, author, and recommendation for each. Public data sourced from Costco's own review platform.
- **Params:** `id` (string, **required**) — Costco product id, e.g. from a search result's id field

### `costco_search`

- **HTTP:** `GET /costco/search`
- **What:** Search Costco products. Returns public Costco products matching a text query and/or a category slug: title, brand, model, image, and rating for each result. Public data sourced from Costco's own search backend.
- **Params:** `category` (string, optional) — Costco category slug, e.g. the last path segment of a category page URL; `query` (string, optional) — Search text

### `costco_warehouses`

- **HTTP:** `GET /costco/warehouses`
- **What:** Find nearby Costco warehouses. Returns Costco warehouses near a latitude/longitude, sorted by distance: name, address, and distance for each. Public data sourced from Costco's own warehouse locator backend.
- **Params:** `latitude` (number, **required**) — Latitude; `longitude` (number, **required**) — Longitude

## Zalando (5)

### `zalando_category`

- **HTTP:** `GET /zalando/category`
- **What:** Browse a Zalando category or brand. Browses a Zalando category or brand listing by URL slug (e.g. shoes, womens-dresses, on-running) and returns the same normalized result cards as zalando-search, plus the category's upstream total_count. Category slugs are market-specific (each storefront uses its own local-language slug, e.g. "shoes" on de/gb, "chaussures" on fr, "scarpe" on it) — take them from that market's own site navigation or a product's url field. market is required (there is no default storefront) and accepts 25 country storefronts — see zalando-markets for the full current list with domains.
- **Params:** `category` (string, **required**) — Zalando category or brand URL slug, in the target market's own language; `market` (string, **required**) — Zalando country storefront

### `zalando_markets`

- **HTTP:** `GET /zalando/markets`
- **What:** List supported Zalando country storefronts. Returns the Zalando country storefronts currently supported by the required market parameter on zalando-search, zalando-category, and zalando-product, with each market's domain. Static, credential-free metadata with no upstream request.
- **Params:** _none_

### `zalando_product`

- **HTTP:** `GET /zalando/product`
- **What:** Get a Zalando product. Returns normalized product details for one Zalando product, including brand, description, images, and per-size price/availability/GTIN. Pass the sku returned by zalando-search or zalando-category; Zalando's own site search resolves the sku to its canonical product page. market is required and must match the storefront the sku was found in (there is no default, and a sku is generally only listed for sale on the market(s) that carry it) — see zalando-markets for the full reference list.
- **Params:** `market` (string, **required**) — Zalando country storefront the sku was found in; `sku` (string, **required**) — Zalando product SKU (article number) from zalando-search or zalando-category

### `zalando_search`

- **HTTP:** `GET /zalando/search`
- **What:** Search Zalando products. Searches a Zalando country storefront by keyword and returns normalized result cards with price, brand, and image. Returns the first page of results as rendered by Zalando plus the upstream total_count; deeper pagination is not yet supported. market is required (there is no default storefront) and accepts 25 country storefronts — see zalando-markets for the full current list with domains.
- **Params:** `market` (string, **required**) — Zalando country storefront; `q` (string, **required**) — Product search keyword

### `zalando_suggest`

- **HTTP:** `GET /zalando/suggest`
- **What:** Autocomplete a Zalando search query. Returns Zalando's own search-box query completions for a partial keyword, e.g. "running sho" -> "running shoes", "running shoes nike". market is required (there is no default storefront) and accepts 25 country storefronts — see zalando-markets for the full current list with domains.
- **Params:** `market` (string, **required**) — Zalando country storefront; `q` (string, **required**) — Partial search text to complete

## Walmart (3)

### `walmart_product`

- **HTTP:** `GET /walmart/product/{item_id}`
- **What:** Get a Walmart product. Returns a normalized Walmart product: price, availability, brand, images, rating, seller, description, highlights, specifications, and variants. Credential-free public Walmart data, rendered from the product page through proxied browser renderers.
- **Params:** `item_id` (string, **required**) — Walmart item id (the numeric id in a /ip/{id} URL)

### `walmart_product_reviews`

- **HTTP:** `GET /walmart/product/{item_id}/reviews`
- **What:** Get Walmart product reviews. Returns the reviews snapshot embedded in a Walmart product page: average rating, total review count, the per-star rating breakdown, the recommended percentage, the top positive and top negative review, and a sample of recent reviews. This is a single on-page snapshot, not a full paginated feed. A product that exists but has no reviews returns zero counts and an empty reviews list. Credential-free public Walmart data, rendered from the product page through proxied browser renderers.
- **Params:** `item_id` (string, **required**) — Walmart item id (the numeric id in a /ip/{id} URL)

### `walmart_search`

- **HTTP:** `GET /walmart/search`
- **What:** Search Walmart products. Returns Walmart search results: item id, title, brand, price, image, availability, seller, and rating per product. Credential-free public Walmart data, rendered from the search page through proxied browser renderers.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `q` (string, **required**) — Search query; `sort` (string, optional) — Sort order

## H&M (5)

### `hm_categories`

- **HTTP:** `GET /hm/categories`
- **What:** Browse H&M's storefront category navigation. Returns H&M's own storefront category navigation, department by department: every direct nav item and subcategory currently shown in the site's own menu, with its display name and storefront URL. Where this build has separately verified the value against hm-listing's own category_id parameter, that id is included too; category_id is omitted for entries not yet verified rather than guessed, since the visible category label is confirmed NOT a reliable way to derive H&M's real listing category ids for every category. department, when given, filters the result to one department.
- **Params:** `department` (string, optional) — Filter to one storefront department

### `hm_listing`

- **HTTP:** `GET /hm/listing`
- **What:** Browse an H&M category's product listing. Returns one H&M category's product listing page: normalized products with pricing, images, colors, and per-size stock, sourced from H&M's own app-backend listing data. category_id is an H&M category slug (e.g. ladies_newarrivals_all, men_newarrivals_all, ladies_jeans) -- this build does not expose a category/nav-tree discovery endpoint, so category_id values are currently sourced from known H&M storefront paths rather than a lookup call. Pagination is page-based and real: requesting a page beyond the category's real last page returns a normal response with an empty products array rather than an error.
- **Params:** `category_id` (string, **required**) — H&M category slug; `is_new` (boolean, optional) — Optional filter for newly added items only; `page` (integer, optional) — Page number, one-based, defaults to 1; `page_size` (integer, optional) — Results per page, 1 to 72, defaults to 36; `sort` (string, optional) — Sort order, defaults to RELEVANCE

### `hm_product`

- **HTTP:** `GET /hm/product/{product_id}`
- **What:** Get an H&M product's full detail. Returns one H&M product's full detail: every purchasable color grouped with its own per-size price and live availability, plus an aggregate rating and real customer reviews (author label, date, body, rating, and any fit-feedback tags the reviewer left, such as "True to Size") when the product has any. This data is not available from hm-listing or hm-search, which only carry one representative price and a per-color stock count. product_id is the numeric id from a listing/search result's id field or its url field's productpage.<id>.html segment. An unrecognized product_id returns 404.
- **Params:** `product_id` (string, **required**) — Numeric H&M product id, from a listing/search result's id field

### `hm_search`

- **HTTP:** `GET /hm/search`
- **What:** Search H&M product listings by free-text keyword. Runs a free-text keyword search against H&M's own app-backend search data and returns normalized products with pricing, images, colors, and per-size stock, plus search-quality metadata (a spelling-correction suggestion, related searches, and a content-filter flag). Unlike category browsing, an obscure or nonsense keyword returns a genuine empty result (zero products) rather than a fallback set. Pagination is page-based and real: requesting a page beyond the real last page returns a normal response with an empty products array rather than an error.
- **Params:** `page` (integer, optional) — Page number, one-based, defaults to 1; `page_size` (integer, optional) — Results per page, 1 to 72, defaults to 36; `query` (string, **required**) — Free-text search keyword

### `hm_stores`

- **HTTP:** `GET /hm/stores`
- **What:** Find nearby H&M physical stores. Returns H&M physical retail store locations near a point: name, phone, full address, and coordinates. Either search, or both lat and lng, is required. search is a free-text zip code or place name that is first resolved to coordinates; if it does not resolve to any location, a well-formed empty result is returned rather than an error. lat and lng, when given directly, skip that resolution step. radius_meters is optional (1000 to 50000, defaults to 10000). A location with no stores within the radius returns a well-formed empty result rather than an error.
- **Params:** `lat` (number, optional) — Latitude, requires lng; `lng` (number, optional) — Longitude, requires lat; `radius_meters` (integer, optional) — Search radius in meters, 1000 to 50000, defaults to 10000; `search` (string, optional) — Free-text zip code or place name to resolve to coordinates

## Kohl's (4)

### `kohls_category`

- **HTTP:** `GET /kohls/category`
- **What:** Browse a Kohl's category or curated campaign page. Returns a Kohl's category or curated campaign page's product grid (page 1 only), with normalized products (title, image, colors, pricing, rating, availability) and facets for discovering further category values. category is Kohl's own catalog taxonomy string, e.g. "Room:Dorm" or "Department:Kitchen & Dining" -- combine multiple dimensions with a literal "+", percent-encoded as "%2B" so it survives as "+" rather than being decoded to a space (e.g. "Room%3ADorm%2BDepartment%3ABedding"). Every facets[].options[].category value in a response is a ready-to-use category string for a follow-up call, so a caller can discover the full taxonomy by starting from a known category (e.g. "Room:Dorm") and following facets. A category value Kohl's does not recognize returns a 404 rather than an unfiltered listing; a recognized dimension with no matching products returns a genuine zero-result response instead.
- **Params:** `category` (string, **required**) — Kohl's catalog taxonomy string, e.g. \

### `kohls_product_reviews`

- **HTTP:** `GET /kohls/product/reviews`
- **What:** Browse a Kohl's product's customer reviews. Returns one page of a Kohl's product's normalized customer reviews (title, text, rating, secondary ratings such as quality/durability/value/style, reviewer name and location, submission date, and photo URLs). web_id is the same identifier a GET /kohls/category response's products[].web_id field carries. A web_id with zero reviews returns a genuine zero-result response rather than an error.
- **Params:** `page` (integer, optional) — Page number, 10 reviews per page (default 1); `web_id` (string, **required**) — Kohl's product web id, e.g. from a GET /kohls/category response's products[].web_id

### `kohls_stores`

- **HTTP:** `GET /kohls/stores`
- **What:** Find nearby Kohl's store locations. Returns physical Kohl's store locations near a free-text location (city/state, zip code, or address): address, phone, weekly hours, distance, and store badges/services. A search with no results returns a genuine empty list rather than an error.
- **Params:** `search` (string, **required**) — Free-text location: city/state, zip code, or address

### `kohls_suggest`

- **HTTP:** `GET /kohls/suggest`
- **What:** Kohl's search-box typeahead suggestions. Returns Kohl's own search-box typeahead result for a partial query: a flat list of suggested search phrases (no product data). A nonsense query returns a genuine, well-formed empty list rather than an error.
- **Params:** `query` (string, **required**) — Partial search text, e.g. \

## Lululemon (5)

### `lululemon_categories`

- **HTTP:** `GET /lululemon/categories`
- **What:** Browse lululemon's storefront category navigation. Returns lululemon's own storefront category navigation, flattened out of the site's shared header nav: every navigable category with its display name, breadcrumb path, and the exact category/cdp_hash pair lululemon-category's own parameters expect (read directly from the nav's own URL, not guessed from the display label). section, when given, filters the result to one top-level nav section.
- **Params:** `section` (string, optional) — Filter to one top-level storefront nav section

### `lululemon_category`

- **HTTP:** `GET /lululemon/category`
- **What:** Browse a lululemon category's product listing. Returns one lululemon category's product listing page: normalized products with pricing, sale detection, sizes, colors, and style numbers, sourced from lululemon's own app-backend category data. category and cdp_hash are the two path segments of a lululemon category URL (https://shop.lululemon.com/c/{category}/{cdp_hash}), e.g. women-new-styles and n14f1wz6o10 -- both are also available from lululemon-categories's own category and cdp_hash fields. Pagination is page-based and real: requesting a page beyond the category's real last page returns a normal response with an empty products array rather than an error. An unrecognized category/cdp_hash pair returns 404.
- **Params:** `category` (string, **required**) — lululemon category slug, from a category URL's first path segment; `cdp_hash` (string, **required**) — lululemon category id, from a category URL's second path segment; `page` (integer, optional) — Page number, one-based, defaults to 1; `page_size` (integer, optional) — Results per page, 1 to 100, defaults to 24

### `lululemon_outfit`

- **HTTP:** `GET /lululemon/outfit`
- **What:** Get lululemon's outfit/style recommendations for a product color. Returns lululemon's own curated outfit/style recommendations for one product color: every complementary item in each styled look, plus the anchor product itself. unified_id and color_code are lululemon-product's own unified_id response field and a color's code field (from lululemon-product's colors[] or lululemon-category's style_numbers-paired colors[]) -- not lululemon-product's own product_id, which is a different id space. Recommended items' own id is a separate, third-party catalog id (not lululemon-product's product_id) -- use each item's url to reach its product page. An unrecognized unified_id/color_code pair returns 404.
- **Params:** `color_code` (string, **required**) — lululemon color code, from a lululemon-product result's colors[].code field; `unified_id` (string, **required**) — lululemon product unified id, from a lululemon-product result's unified_id field

### `lululemon_product`

- **HTTP:** `GET /lululemon/product/{product_id}`
- **What:** Get a lululemon product's full detail. Returns one lululemon product's full detail: every purchasable color/size SKU with its own price, sale status, and live availability, plus an aggregate rating and real customer reviews when the product has any -- none of which lululemon-category exposes (it only carries one representative color/price per product). product_id is the id from a lululemon-category result's id field or a lululemon product URL's trailing path segment (https://shop.lululemon.com/p/{slug}/{product_id}) -- the slug itself is not needed. An unrecognized product_id returns 404.
- **Params:** `product_id` (string, **required**) — lululemon product id, from a lululemon-category result's id field

### `lululemon_stores`

- **HTTP:** `GET /lululemon/stores`
- **What:** Browse lululemon's physical store directory. Returns lululemon's own complete physical store directory (480 US and 86 Canada locations as of this endpoint's own research), including regular weekly hours and in-store amenities. All filters are optional and applied locally after fetching the full directory -- there is no live geo-search API on a credential-free host for this platform (see notes/lululemon-maintenance.md). country and state are free-text equality filters against the values this directory actually carries (2-letter codes, e.g. US/CA, NY/CA), not an enforced enum. lat and lng (both required together) filter to stores within radius_miles (1 to 500, defaults to 50), sorted nearest-first.
- **Params:** `country` (string, optional) — Filter to one country by its 2-letter code; `lat` (number, optional) — Latitude, requires lng; `lng` (number, optional) — Longitude, requires lat; `radius_miles` (number, optional) — Search radius in miles, 1 to 500, defaults to 50; `state` (string, optional) — Filter to one state/province by its 2-letter code

## Macy's (3)

### `macys_product`

- **HTTP:** `GET /macys/product/{productId}`
- **What:** Get a Macy's product's full detail. Returns one Macy's product's full detail: name, brand, description, department/division, category breadcrumb, pricing (with sale detection), availability, images, aggregate rating, and every purchasable color variant with its own price. productId is a numeric id, taken from a Macy's product page's ?ID= query parameter.
- **Params:** `productId` (string, **required**) — Numeric Macy's product id, from a product page's ?ID= query parameter

### `macys_product_reviews`

- **HTTP:** `GET /macys/product/reviews`
- **What:** Get a Macy's product's customer reviews. Returns one page of a Macy's product's normalized customer reviews, plus a site-wide rating summary (rating count, average rating, recommended ratio, rating histogram) for the product. Sourced from a separate review platform Macy's own product pages embed, distinct from the product catalog itself. product_id is a numeric id, the same one used by GET /macys/product/{productId}. A product with zero reviews, or a well-formed but unrecognized product_id, returns a normal, empty result rather than an error.
- **Params:** `page` (integer, optional) — Result page, 1-based, defaults to 1; `product_id` (string, **required**) — Numeric Macy's product id, from a product page's ?ID= query parameter

### `macys_suggest`

- **HTTP:** `GET /macys/suggest`
- **What:** Get Macy's search-box suggestions. Returns Macy's own search-box suggestions (typeahead) for a partial query: a flat list of suggested search phrases, no product data. A partial query with no real matches returns a normal, empty result rather than an error.
- **Params:** `query` (string, **required**) — Partial search query

## Nike (6)

### `nike_categories`

- **HTTP:** `GET /nike/categories`
- **What:** List Nike's category and subcategory taxonomy. Returns Nike's full Men/Women/Kids/Jordan category and subcategory taxonomy tree, sourced directly from Nike.com's own nav mega-menu. Each top-level entry (Men, Women, Kids, Jordan) breaks down into named groups (e.g. Shoes, Clothing, Accessories, Shop By Sport -- Women additionally carries a Shop by Color group, and Jordan is organized by Men/Women/Kids instead of by product type), each with its own subcategory entries. Every subcategory (and most groups) carries a slug usable as a future category-browse endpoint's path/slug input, and is directly browsable today at https://www.nike.com/w/<slug>. This mirrors the live nav exactly, including its seasonal/promotional groups (e.g. Limited Time, New & Featured) alongside the stable structural ones -- Nike's own markup does not distinguish the two.
- **Params:** _none_

### `nike_product`

- **HTTP:** `GET /nike/product`
- **What:** Get a Nike product. Returns normalized product-detail data for one color variant: title, description, pricing, images, every offered size, and every other available color. slug and style_color together reproduce Nike's own product page URL (nike.com/t/<slug>/<style_color>) and are both returned by nike-search's product colors[].slug and colors[].style_color fields.
- **Params:** `slug` (string, **required**) — Product-detail URL slug, from a search result's colors[].slug field; `style_color` (string, **required**) — Style-color id, from a search result's colors[].style_color field

### `nike_product_reviews`

- **HTTP:** `GET /nike/product/reviews`
- **What:** Get Nike product reviews. Returns one page of a Nike product's normalized customer reviews, plus an aggregate rating summary (average rating and a per-star rating breakdown) that Nike's own product-detail endpoint does not otherwise expose. slug and style_color are the same values nike-product accepts (from a search result's colors[].slug/colors[].style_color fields). A product with no reviews yet returns a well-formed empty result rather than an error. Requesting a page beyond the available result pages returns a not-found error.
- **Params:** `page` (integer, optional) — One-based page number, defaults to 1; `slug` (string, **required**) — Product-detail URL slug, from a search result's colors[].slug field; `style_color` (string, **required**) — Style-color id, from a search result's colors[].style_color field

### `nike_search`

- **HTTP:** `GET /nike/search`
- **What:** Search or browse Nike products. Searches Nike.com product listings by keyword, or browses a category/subcategory listing by slug, with real pagination. Exactly one of keyword or category is required. Returns normalized product groups with pricing, colorway images, and every purchasable color variant, plus filter and subcategory navigation data (facet_nav) already present on the same response -- both keyword search and a category listing's first page include filter groups (Gender, Color, Price, Size, and similar); only a category listing includes a breadcrumb trail and subcategory drill-down options, and only its first page (a category listing's later pages do not repeat navigation data). Keyword search is best-effort relevance, not a guaranteed keyword match: for an obscure or nonsense keyword, Nike's own search index falls back to its own recommended results instead of returning an empty list, and there is currently no reliable signal in the response to distinguish a true keyword match from that fallback behavior. A keyword Nike's own search router treats as structurally empty (for example a punctuation-only query) does return a genuine empty result. Category values come from nike-categories' own slug field, or from a prior response's own facet_nav navigation paths (with the leading /w/ stripped). Requesting a page beyond the available result pages returns a not-found error.
- **Params:** `category` (string, optional) — Category/subcategory browse slug, from nike-categories' own slug field or a prior response's facet_nav navigation. Exactly one of keyword or category is required.; `keyword` (string, optional) — Search keyword. Exactly one of keyword or category is required.; `page` (integer, optional) — One-based page number, defaults to 1

### `nike_stores`

- **HTTP:** `GET /nike/stores`
- **What:** Find nearby Nike stores. Searches Nike's physical retail store locator by coordinates and radius. Returns each nearby store's name, address, phone, coordinates, distance, and store page URL. A location with no nearby stores within the given radius returns a well-formed empty result.
- **Params:** `lat` (number, **required**) — Latitude, -90 to 90; `lng` (number, **required**) — Longitude, -180 to 180; `page` (integer, optional) — One-based page number, defaults to 1; `radius_miles` (integer, optional) — Search radius in miles, defaults to 50

### `nike_suggest`

- **HTTP:** `GET /nike/suggest`
- **What:** Get Nike search-box suggestions. Returns Nike's own search-box suggestions (typeahead) for a partial query, the same "Top Suggestions" list shown while typing into Nike's search box: a flat list of suggested search phrases, no product data.
- **Params:** `query` (string, **required**) — Partial search query

## Old Navy (7)

### `oldnavy_categories`

- **HTTP:** `GET /oldnavy/categories`
- **What:** List Old Navy storefront categories. Lists Old Navy's own storefront navigation as name/cid pairs, resolving the cid-discovery gap oldnavy-search, oldnavy-product, and oldnavy-category all document. Omit cid to list Old Navy's top-level divisions (e.g. Women, Men, Boys, Toddler). Pass a cid (a division's own, or any deeper category's) to list the related categories for that part of the storefront instead, in the same order the live storefront menu shows them -- this is section-level, not necessarily unique per leaf category. Currently only available for brand=on (Old Navy) -- Gap, Banana Republic, and Athleta render their storefront navigation as client-side-only JavaScript with no server-rendered category id to scrape.
- **Params:** `brand` (string, optional) — Storefront to list -- only on (Old Navy) is currently supported; `cid` (string, optional) — Category id to list related categories for; omit to list the top-level divisions

### `oldnavy_category`

- **HTTP:** `GET /oldnavy/category`
- **What:** Browse an Old Navy, Gap, Banana Republic, or Athleta category. Returns a category/browse listing for one storefront category id (cid). cid is an opaque Gap Inc category id assigned by the storefront's own navigation -- neither oldnavy-search nor oldnavy-category currently surface a category-id list, so find one from the storefront's own category page URLs (the cid query parameter on a /browse/... page) for now. Select the storefront with the brand parameter (`on` for Old Navy, `gap` for Gap, `br` for Banana Republic, `at` for Athleta; defaults to `on`) -- it must match the brand the cid was found under. Returns the category's subcategory breakdown, normalized product summaries with per-color inventory data, and available search facets with live counts.
- **Params:** `brand` (string, optional) — Storefront to browse; `cid` (string, **required**) — Category id, from a storefront category page's own cid query parameter; `page` (integer, optional) — One-based page

### `oldnavy_product`

- **HTTP:** `GET /oldnavy/product`
- **What:** Get an Old Navy, Gap, Banana Republic, or Athleta product. Returns normalized product-detail data for one color variant: name, description, images, aggregate rating, and every size offered in that color as a separate priced offer. pid is a color-specific product id, as returned by oldnavy-search's product colors[].id field (not the bare base product id). Select the storefront with the brand parameter (`on` for Old Navy, `gap` for Gap, `br` for Banana Republic, `at` for Athleta; defaults to `on`) -- it must match the brand the pid was found under.
- **Params:** `brand` (string, optional) — Storefront the pid belongs to; `pid` (string, **required**) — Color-specific product id, from a search result's colors[].id field

### `oldnavy_product_availability`

- **HTTP:** `GET /oldnavy/product/availability`
- **What:** Check in-store pickup stock for an Old Navy, Gap, Banana Republic, or Athleta product. Checks per-size, in-store pickup stock status for one color (pid) at one or more physical stores. pid matches oldnavy-product's own color-level id. Give store location either directly with store_id (one or more comma-separated store ids, e.g. from a prior call to this endpoint or a value you already have) or with zip or both lat and lng, which resolves the nearest stores automatically. Select the storefront with the brand parameter (`on` for Old Navy, `gap` for Gap, `br` for Banana Republic, `at` for Athleta; defaults to `on`). Each returned store lists every offered size's stock status: `in_stock`, `out_of_stock`, or `low_stock`.
- **Params:** `brand` (string, optional) — Storefront to check; `lat` (number, optional) — Latitude to resolve the nearest stores from (must be given together with lng); `lng` (number, optional) — Longitude to resolve the nearest stores from (must be given together with lat); `pid` (string, **required**) — Color-level Old Navy/Gap/Banana Republic/Athleta product id; `store_id` (string, optional) — One or more comma-separated numeric store ids; `zip` (string, optional) — Zip code to resolve the nearest stores from

### `oldnavy_product_reviews`

- **HTTP:** `GET /oldnavy/product/reviews`
- **What:** Get reviews for an Old Navy, Gap, Banana Republic, or Athleta product. Returns one page of a product's customer reviews (author, date, rating, headline, body, and verified-purchase flag), plus the product's overall rating summary (average rating, rating count, per-star histogram, and recommended ratio). pid is a color-specific product id, as returned by oldnavy-search's product colors[].id field (not the bare base product id) -- the same pid oldnavy-product accepts. Select the storefront with the brand parameter (`on` for Old Navy, `gap` for Gap, `br` for Banana Republic, `at` for Athleta; defaults to `on`) -- it must match the brand the pid was found under. A product with no reviews yet returns a well-formed empty result, not an error.
- **Params:** `brand` (string, optional) — Storefront the pid belongs to; `page` (integer, optional) — One-based page, 10 reviews per page; `pid` (string, **required**) — Color-specific product id, from a search result's colors[].id field

### `oldnavy_search`

- **HTTP:** `GET /oldnavy/search`
- **What:** Search Old Navy, Gap, Banana Republic, or Athleta products. Searches product listings across Old Navy, Gap, Banana Republic, and Athleta -- select the storefront with the brand parameter (`on` for Old Navy, `gap` for Gap, `br` for Banana Republic, `at` for Athleta; defaults to `on`). Returns normalized product summaries with pricing, review scores, and every purchasable color variant. This search is best-effort relevance, not a guaranteed keyword match: for an obscure or nonsense keyword the upstream search index falls back to its own recommended results instead of returning an empty list, and there is currently no reliable signal in the response to distinguish a true keyword match from that fallback behavior.
- **Params:** `brand` (string, optional) — Storefront to search; `keyword` (string, **required**) — Search keyword; `page` (integer, optional) — One-based page

### `oldnavy_stores`

- **HTTP:** `GET /oldnavy/stores`
- **What:** Find Old Navy, Gap, Banana Republic, or Athleta store locations. Searches physical store locations for one storefront by free-text search (zip code or city) and/or coordinates. Provide search, or both lat and lng. Select the storefront with the brand parameter (`on` for Old Navy, `gap` for Gap, `br` for Banana Republic, `at` for Athleta; defaults to `on`). Returns each nearby store's name, full address, phone number, coordinates, distance, and specialties (e.g. "In-Store Shopping", "Outlet"). This is location search only -- it does not report per-item, per-store stock levels; use oldnavy-product-availability for that.
- **Params:** `brand` (string, optional) — Storefront to search; `lat` (number, optional) — Latitude (must be given together with lng); `lng` (number, optional) — Longitude (must be given together with lat); `search` (string, optional) — Zip code or city to search near

## Sam's Club (5)

### `samsclub_category`

- **HTTP:** `GET /samsclub/category`
- **What:** Browse a Sam's Club category or collection. Returns a Sam's Club category or collection page's product grid, with real page-based pagination. id accepts a bare numeric category id (from a nav link's /browse/{id} URL) or a full /browse/{slug}/{id} URL copied from samsclub.com -- only the trailing id is used. Returns normalized products with name, brand, pricing, availability, rating, and image. An id samsclub.com does not recognize returns a genuine zero-result response rather than an error, matching upstream's own behavior.
- **Params:** `id` (string, **required**) — Sam's Club category id, or a /browse/{slug}/{id} URL; `page` (integer, optional) — Result page, 1-based, defaults to 1

### `samsclub_content`

- **HTTP:** `GET /samsclub/content/{id}`
- **What:** Get a Sam's Club curated content or landing page. Returns one Sam's Club curated content/landing page (e.g. a seasonal savings hub or a "New Arrivals" page) -- distinct data from GET /samsclub/category's flat, paginated product grid. id accepts a bare numeric content page id (from a nav link's /cp/{id} URL) or a full /cp/{slug}/{id} URL copied from samsclub.com -- only the trailing id is used. Returns a title, breadcrumb, named curated product shelves, and a category-navigation tile grid. There is no pagination -- a content page's shelves are a fixed, hand-curated set. An id samsclub.com does not recognize returns a 404, unlike GET /samsclub/category's zero-result response for the same situation.
- **Params:** `id` (string, **required**) — Numeric Sam's Club content page id, from a /cp/{slug}/{id} URL

### `samsclub_departments`

- **HTTP:** `GET /samsclub/departments`
- **What:** List Sam's Club departments and categories. Returns Sam's Club's full department/category taxonomy, as shown on its own "All Departments" page: every top-level department with its own subcategory list. Each link's type is "browse" (pairs directly with GET /samsclub/category), "cp" (a content/landing page that does not reliably carry a product grid), or empty (an unrecognized link shape).
- **Params:** _none_

### `samsclub_product`

- **HTTP:** `GET /samsclub/product/{id}`
- **What:** Get a Sam's Club product's full detail. Returns one Sam's Club product's full detail: name, brand, description, category breadcrumb, pricing, availability, images, aggregate rating and review count, and the club's own item number. id is the numeric product id from a Sam's Club product page's /ip/ URL.
- **Params:** `id` (string, **required**) — Numeric Sam's Club product id, from a product page's /ip/{slug}/{id} URL

### `samsclub_product_related`

- **HTTP:** `GET /samsclub/product/{id}/related`
- **What:** Get a Sam's Club product's related items. Returns the related-item carousels shown on a Sam's Club product page, each a named shelf (e.g. "Members also considered", "Items you may like") of normalized products with pricing, rating, and image. id is the numeric product id from a Sam's Club product page's /ip/ URL. This upstream source does not distinguish an unrecognized id from a known one -- an unrecognized id still returns generic fallback shelves rather than an error.
- **Params:** `id` (string, **required**) — Numeric Sam's Club product id, from a product page's /ip/{slug}/{id} URL

## Ulta Beauty (8)

### `ulta_categories`

- **HTTP:** `GET /ulta/categories`
- **What:** List Ulta Beauty storefront categories. Lists Ulta Beauty's own storefront category navigation: department, group, name, and a URL usable directly as GET /ulta/category's own category parameter. Closes the discovery gap of not already knowing a category path. department, if set, filters to just that department's entries. group is empty for a department's own top-level link or a group's own heading link, and set to that group's name for the leaf categories nested under it. The exact same real category can legitimately appear more than once under a different department/group when the site's own navigation cross-lists it.
- **Params:** `department` (string, optional) — Filter to one department

### `ulta_category`

- **HTTP:** `GET /ulta/category`
- **What:** Browse an Ulta Beauty category page. Browses an Ulta Beauty category page's product grid, with real page-based pagination and the category's own guided-navigation refinement options. category accepts a category path or full URL copied from Ulta's own site navigation (e.g. shop/makeup/eyes/mascara). filter narrows results using Ulta's own guided-navigation facet-code shape (e.g. BENEFIT--WATERPROOF, or a comma-joined combination of codes) -- discover valid codes for a category from that category's own response facets field, whose value is ready to use directly as this parameter. An unrecognized category returns 404.
- **Params:** `category` (string, **required**) — Ulta category path or URL; `filter` (string, optional) — Guided-navigation facet code(s), comma-joined for multiple; `page` (integer, optional) — Result page, 1-based, defaults to 1

### `ulta_product`

- **HTTP:** `GET /ulta/product/{productId}`
- **What:** Get an Ulta Beauty product's full detail. Returns one Ulta Beauty product's full detail: name, brand, description, category, pricing, rating, review count, images, and every purchasable color/shade variant. productId is taken from a search result's product_id field or a product page's URL (e.g. pimprod2020260). sku is optional and selects a specific color/shade variant; an omitted or invalid sku still resolves the base product using its own default variant. An unrecognized productId returns 404.
- **Params:** `productId` (string, **required**) — Ulta product id, from a search result's product_id field; `sku` (string, optional) — Numeric Ulta sku id selecting a specific color/shade variant

### `ulta_product_questions`

- **HTTP:** `GET /ulta/product/questions`
- **What:** Get an Ulta Beauty product's customer questions and answers. Returns one page of an Ulta Beauty product's normalized customer questions, each with every answer it received. product_id is taken from a search result's product_id field or a product page's URL. A product with zero questions, or a well-formed but unrecognized product_id, returns a normal, empty result rather than an error.
- **Params:** `page` (integer, optional) — Result page, 1-based, defaults to 1; `product_id` (string, **required**) — Ulta product id, from a search result's product_id field

### `ulta_product_reviews`

- **HTTP:** `GET /ulta/product/reviews`
- **What:** Get an Ulta Beauty product's customer reviews. Returns one page of an Ulta Beauty product's normalized customer reviews, plus the retailer's own site-wide rating summary (rating count, average rating, recommended ratio, rating histogram) for the product. product_id is taken from a search result's product_id field or a product page's URL. A product with zero reviews, or a well-formed but unrecognized product_id, returns a normal, empty result rather than an error.
- **Params:** `page` (integer, optional) — Result page, 1-based, defaults to 1; `product_id` (string, **required**) — Ulta product id, from a search result's product_id field

### `ulta_search`

- **HTTP:** `GET /ulta/search`
- **What:** Search Ulta Beauty products. Searches Ulta Beauty's product catalog by keyword, with real page-based pagination. Returns normalized products with brand, pricing, rating, and review count. An unrecognized/nonsense keyword returns a genuine empty result rather than a fallback set. Requesting a page beyond the available results returns a normal, empty result rather than an error.
- **Params:** `page` (integer, optional) — Result page, 1-based, defaults to 1; `query` (string, **required**) — Search keyword

### `ulta_stores`

- **HTTP:** `GET /ulta/stores`
- **What:** Find nearby Ulta Beauty physical stores. Returns Ulta Beauty physical retail store locations near a point: name, phone, full address, hours, services, and coordinates. Either search, or both lat and lng, is required. search is a free-text zip code, city, or address that is first resolved to coordinates; if it does not resolve to any location, a well-formed empty result is returned rather than an error. lat and lng, when given directly, skip that resolution step. radius_meters is optional (1000 to 50000, defaults to 25000). A location with no stores within the radius returns a well-formed empty result rather than an error.
- **Params:** `lat` (number, optional) — Latitude, requires lng; `lng` (number, optional) — Longitude, requires lat; `radius_meters` (integer, optional) — Search radius in meters, 1000 to 50000, defaults to 25000; `search` (string, optional) — Free-text zip code, city, or address to resolve to coordinates

### `ulta_suggest`

- **HTTP:** `GET /ulta/suggest`
- **What:** Get Ulta Beauty search suggestions. Returns Ulta Beauty's own search-suggestion (typeahead) result for a partial search term: suggested search terms, each with its own top product matches, plus a featured top result matching what a real user sees at the top of the dropdown. A partial term with no matches returns a normal, empty result rather than an error.
- **Params:** `query` (string, **required**) — Partial search term

## Wayfair (3)

### `wayfair_categories`

- **HTTP:** `GET /wayfair/categories`
- **What:** List Wayfair categories. Returns a page of Wayfair categories discovered from Wayfair's own published sitemap, closing the discovery gap where a category id otherwise has to be found elsewhere. Pair a returned id with GET /wayfair/category to browse that category's product grid. name is derived from the category's own URL slug (title-cased), not an authoritative site-provided label. q, if set, case-insensitively filters to categories whose derived name or department contains it.
- **Params:** `page` (integer, optional) — Result page, 1-based, defaults to 1; `page_size` (integer, optional) — Results per page, defaults to 100, max 1000; `q` (string, optional) — Case-insensitive substring filter on name or department

### `wayfair_category`

- **HTTP:** `GET /wayfair/category`
- **What:** Browse a Wayfair category. Returns a Wayfair category page's product grid, with real page-based pagination. category accepts a bare Wayfair category id ("478390"), a "c"-prefixed id ("c478390"), a category slug ("office-chairs-c478390"), or a full category URL copied from wayfair.com -- only the trailing category id is used. Returns normalized products with name, brand, pricing, and image.
- **Params:** `category` (string, **required**) — Wayfair category id, slug, or URL; `page` (integer, optional) — Result page, 1-based, defaults to 1

### `wayfair_product`

- **HTTP:** `GET /wayfair/product/{id}`
- **What:** Get a Wayfair product's full detail. Returns one Wayfair product's full detail: name, brand, price, stock status, aggregate rating with a 1-5 star breakdown, images, every selectable variant option (e.g. color, finish), and site-selected feature highlights. id is the product's own "W"-prefixed id (e.g. W100794312), taken from a category result's product_id field or a product page's URL. An unrecognized id returns 404.
- **Params:** `id` (string, **required**) — Wayfair product id, starting with W

## Wish (6)

### `wish_categories`

- **HTTP:** `GET /wish/categories`
- **What:** Get Wish's category and filter navigation tree. Returns Wish's own top navigation/category tree (e.g. "Popular", "Deals Hub", "Fashion", "Gadgets") plus each category's nested filter groups (e.g. Color, Rating) where present. This is a static, site-wide taxonomy -- it takes no input and its result does not vary by search term or category.
- **Params:** _none_

### `wish_product`

- **HTTP:** `GET /wish/product/{id}`
- **What:** Get a Wish product's full detail. Returns one Wish product's full detail: name, description, sold-out state, aggregate rating, image URLs, and every purchasable variation with its own price, currency, inventory, and merchant. id is taken from a search result's product_id field or a product page's URL. An unrecognized id returns 404.
- **Params:** `id` (string, **required**) — Wish product id, a 24-character hex id from a search result's product_id field

### `wish_product_related`

- **HTTP:** `GET /wish/product/{id}/related`
- **What:** Get a Wish product's related items. Returns a Wish product's related-item rails: shelves of similar products, grouped by rail (e.g. general similar items, a faster-shipping-eligible subset). id is taken from a search result's product_id field or a product page's URL. A faster-shipping rail with no eligible items, or a nonexistent id, returns a normal, empty result rather than an error.
- **Params:** `count` (integer, optional) — Number of items to return per rail, 1 to 70, defaults to 10; `id` (string, **required**) — Wish product id, a 24-character hex id from a search result's product_id field

### `wish_product_reviews`

- **HTTP:** `GET /wish/product/{id}/reviews`
- **What:** Get a Wish product's customer reviews. Returns a Wish product's normalized customer reviews. id is taken from a search result's product_id field or a product page's URL. A product with zero reviews returns a normal, empty result rather than an error. A caller wanting more reviews should re-request with a larger count -- this endpoint does not support an offset/cursor parameter, since the upstream source does not support one.
- **Params:** `count` (integer, optional) — Number of reviews to return, 1 to 200, defaults to 10; `id` (string, **required**) — Wish product id, a 24-character hex id from a search result's product_id field

### `wish_search`

- **HTTP:** `GET /wish/search`
- **What:** Search Wish products. Searches Wish's product catalog by keyword, with real offset-based pagination. Returns normalized products with price, currency, rating, review count, and merchant id. A query with no matches returns a normal, empty result rather than an error.
- **Params:** `count` (integer, optional) — Number of results per page, 1 to 70, defaults to 30; `offset` (integer, optional) — Result offset, 0-based, defaults to 0, must be an exact multiple of count up to 3 * count; `query` (string, **required**) — Search keyword

### `wish_suggest`

- **HTTP:** `GET /wish/suggest`
- **What:** Get Wish search suggestions. Returns Wish's own search-suggestion (typeahead) result for a partial search term: a flat list of suggested search terms, no product data. A partial term with no matches returns a normal, empty result rather than an error.
- **Params:** `query` (string, **required**) — Partial search term

## Zappos (5)

### `zappos_brand`

- **HTTP:** `GET /zappos/brand`
- **What:** Browse a Zappos brand. Returns a Zappos brand page's product grid, with real page-based pagination and per-field filter facets. brand accepts a full brand URL copied from zappos.com, the "slug/id.zso" path from that URL, or just the opaque id from a GET /zappos/brands result's own id field. An unrecognized brand returns 404.
- **Params:** `brand` (string, **required**) — Zappos brand URL, slug/id.zso path, or opaque id; `page` (integer, optional) — Result page, 1-based, defaults to 1

### `zappos_brands`

- **HTTP:** `GET /zappos/brands`
- **What:** List Zappos brands. Returns a page of Zappos brands discovered from Zappos's own published sitemap, closing the discovery gap where a brand id otherwise has to be found elsewhere. Pair a returned id or url with GET /zappos/brand to browse that brand's product grid. name is derived from the brand's own URL slug (title-cased), not an authoritative site-provided label. q, if set, case-insensitively filters to brands whose derived name or slug contains it.
- **Params:** `page` (integer, optional) — Result page, 1-based, defaults to 1; `page_size` (integer, optional) — Results per page, defaults to 100, max 1000; `q` (string, optional) — Case-insensitive substring filter on name or slug

### `zappos_product`

- **HTTP:** `GET /zappos/product/{productId}`
- **What:** Get a Zappos product's full detail. Returns one Zappos product's full detail: name, brand, description, category, breadcrumbs, pricing, images, aggregate rating with a 1-5 star breakdown, up to two featured customer reviews with real author/date/body/rating, reviewer-submitted fit feedback for size/width/arch (each response option's own share of respondents plus the most common answer), and every sibling color variant with its own price. productId is taken from a search result's product_id field or a product page's URL. colorId is optional and selects a specific color variant; an omitted or invalid colorId still resolves the base product using a real color variant rather than failing. An unrecognized productId returns 404.
- **Params:** `colorId` (string, optional) — Zappos color id selecting a specific color variant; `productId` (string, **required**) — Zappos product id, from a search result's product_id field

### `zappos_search`

- **HTTP:** `GET /zappos/search`
- **What:** Search Zappos products. Searches Zappos's product catalog by keyword, with real page-based pagination. Returns normalized products with brand, pricing, sale status, rating, and review count, plus filterable facets (gender, department, shoe size, and more) each with a live result count and its own drill-down URL. Requesting a page beyond the available results returns a normal, empty result rather than an error.
- **Params:** `page` (integer, optional) — Result page, 1-based, defaults to 1; `term` (string, **required**) — Search keyword

### `zappos_suggest`

- **HTTP:** `GET /zappos/suggest`
- **What:** Get Zappos search-box suggestions. Returns Zappos's own search-box suggestions (typeahead) for a partial query: a flat list of suggested search phrases, no product data. A partial query with no real matches returns a normal, empty result rather than an error.
- **Params:** `query` (string, **required**) — Partial search query

## Zara (6)

### `zara_categories`

- **HTTP:** `GET /zara/categories`
- **What:** List Zara's category and subcategory taxonomy. Returns Zara's full category and subcategory navigation tree for the US storefront (WOMAN, MAN, KID, and other top-level sections), sourced directly from Zara's own category navigation data. Each entry's id is the value to pass as categoryId to zara-category-products. Takes no query parameters.
- **Params:** _none_

### `zara_category_products`

- **HTTP:** `GET /zara/category/{categoryId}/products`
- **What:** Browse a Zara category's product listing. Returns a Zara category's full product listing: normalized products with pricing, images, and availability, sourced from Zara's own category browse data. categoryId is a numeric id from zara-categories. Zara does not paginate this data -- the response always contains the category's complete listing in one call, not one page of it. Each entry represents one purchasable color variant rather than a color-grouped product family, matching how Zara's own category data is structured.
- **Params:** `categoryId` (string, **required**) — Numeric Zara category id, from zara-categories' id field

### `zara_product`

- **HTTP:** `GET /zara/product/{productId}`
- **What:** Get a Zara product's full detail. Returns one Zara product's full detail: every purchasable color variant with its real marketing description, per-size stock, and full image gallery -- richer than the per-product summaries returned by zara-category-products and zara-search. productId is a numeric id, taken from a search/category result's url field (the digits after "-p" in the product-detail URL). An unrecognized productId returns 404.
- **Params:** `productId` (string, **required**) — Numeric Zara product id, from a search/category result's url field

### `zara_search`

- **HTTP:** `GET /zara/search`
- **What:** Search Zara products. Searches Zara product listings by keyword within one department section, with real offset-based pagination. Returns normalized products with pricing, images, availability, and every purchasable color variant, plus the upstream's own search facets. This search is best-effort relevance, not a guaranteed keyword match: for an obscure or nonsense keyword, Zara's own search falls back to a broader recommended result set instead of returning an empty list, and there is no reliable field in the response to distinguish a true keyword match from that fallback behavior. Requesting an offset beyond the available results returns a normal, empty result with is_last_page true rather than an error.
- **Params:** `limit` (integer, optional) — Results per request, 1 to 100, defaults to 24; `offset` (integer, optional) — Zero-based result offset, defaults to 0; `query` (string, **required**) — Search keyword; `section` (string, **required**) — Department section to search

### `zara_stores`

- **HTTP:** `GET /zara/stores`
- **What:** Find nearby Zara physical stores. Returns Zara physical retail stores near a location: name, full address, phone, coordinates, opening hours status, pickup/donation eligibility, and a canonical store page URL. lat and lng are both required -- this endpoint does not accept a free-text zip/city search. A location with no stores within the radius returns a normal response with an empty stores array rather than an error.
- **Params:** `donation_only` (boolean, optional) — Only return stores that accept clothing donations; `lat` (number, **required**) — Latitude; `lng` (number, **required**) — Longitude; `pickup_only` (boolean, optional) — Only return stores that support in-store pickup; `radius` (integer, optional) — Search radius in miles, 1 to 500, defaults to 30

### `zara_suggest`

- **HTTP:** `GET /zara/suggest`
- **What:** Get Zara search-box suggestions for a partial keyword. Returns Zara's own search-suggestion (typeahead) results for a partial keyword, the same suggestions shown while typing into Zara's search box. A nonsense query returns a normal response with an empty suggestions array rather than a fallback/recommended set.
- **Params:** `query` (string, **required**) — Partial search keyword
