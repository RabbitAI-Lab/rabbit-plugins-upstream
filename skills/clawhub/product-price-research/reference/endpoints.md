# product-price-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**57 endpoints across 8 platform group(s).**

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

## eBay (6)

### `ebay_item`

- **HTTP:** `GET /ebay/item/{item_id}`
- **What:** Get eBay item details. Returns normalized details for a public eBay item listing.
- **Params:** `item_id` (string, **required**) — eBay item ID

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
