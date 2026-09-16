# retail-assortment-gap-analysis — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Only the endpoints used by this workflow. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**11 endpoints across 3 platform group(s).**

## Shopify (5)

### `shopify_collection_products`

- **HTTP:** `GET /shopify/collections/{handle}/products`
- **What:** List Shopify collection products. Returns normalized products from a public Shopify collection `/products.json` endpoint. `sortBy` and dynamic facet-filter query params (e.g. `fit`, `canonicalColour`) only take effect for headless storefronts served via the embedded-SSR-JSON fallback transport (`transport_mode: "ssr_embedded"`) and return an invalid-param error if supplied against a classic-transport store, since Shopify's classic public catalog JSON has no server-side sort or filter support.
- **Params:** `handle` (string, **required**) — Collection handle; `limit` (integer, optional) — Maximum products, defaults to 50 and supports up to 250; `page` (integer, optional) — 1-based page, defaults to 1; `sortBy` (string, optional) — SSR-fallback transport only (transport_mode ssr_embedded). Allowed values: sortLTH, sortHTL, newest. Omit for the storefront's default relevancy order. Rejected as an invalid param for classic-transport stores.; `url` (string, **required**) — Shopify storefront URL

### `shopify_collections`

- **HTTP:** `GET /shopify/collections`
- **What:** List Shopify collections. Returns normalized collections from a public Shopify `/collections.json` endpoint. Valid empty result pages return `200` with an empty collections array.
- **Params:** `limit` (integer, optional) — Maximum collections, defaults to 50 and supports up to 250; `page` (integer, optional) — 1-based page, defaults to 1; `url` (string, **required**) — Shopify storefront URL

### `shopify_product`

- **HTTP:** `GET /shopify/products/{handle}`
- **What:** Get Shopify product. Returns normalized product detail from Shopify's credential-free product handle `.js` endpoint.
- **Params:** `handle` (string, **required**) — Product handle; `url` (string, **required**) — Shopify storefront URL

### `shopify_products`

- **HTTP:** `GET /shopify/products`
- **What:** List Shopify products. Returns normalized products from a public Shopify `/products.json` endpoint. Valid empty result pages return `200` with an empty products array. `sortBy` and dynamic facet-filter query params (e.g. `fit`, `canonicalColour`) only take effect for headless storefronts served via the embedded-SSR-JSON fallback transport (`transport_mode: "ssr_embedded"`) and return an invalid-param error if supplied against a classic-transport store, since Shopify's classic public catalog JSON has no server-side sort or filter support.
- **Params:** `limit` (integer, optional) — Maximum products, defaults to 50 and supports up to 250; `page` (integer, optional) — 1-based page, defaults to 1; `sortBy` (string, optional) — SSR-fallback transport only (transport_mode ssr_embedded). Allowed values: sortLTH, sortHTL, newest. Omit for the storefront's default relevancy order. Rejected as an invalid param for classic-transport stores.; `url` (string, **required**) — Shopify storefront URL

### `shopify_store`

- **HTTP:** `GET /shopify/store`
- **What:** Get Shopify store metadata. Resolves a public Shopify storefront and returns normalized metadata from credential-free storefront JSON. If the vanity domain blocks `/products.json`, the service may fall back to a public `*.myshopify.com` domain discovered from the storefront page.
- **Params:** `url` (string, **required**) — Shopify storefront URL

## Target (3)

### `target_categories`

- **HTTP:** `GET /target/categories`
- **What:** List all Target categories. Returns Target's current top-level category menu and the complete grouped shop-all directory, including category ids and canonical URLs.
- **Params:** _none_

### `target_category_products`

- **HTTP:** `GET /target/category-products`
- **What:** Browse Target category products. Returns paginated products for any category id from target-categories. Each response also contains every available dynamic filter group and option. Pass selected option ids through filter_ids as a comma-separated list. The sort enum accepts `relevance`, `featured`, `price-low`, `price-high`, `rating`, `bestselling`, and `newest`.
- **Params:** `category_id` (string, **required**) — Target category id; `filter_ids` (string, optional) — Comma-separated Target filter option ids; `page` (integer, optional) — One-based page (1-50); `sort` (string, optional) — Result order; `store_id` (integer, optional) — Target store id used for pricing

### `target_product`

- **HTTP:** `GET /target/product`
- **What:** Get a Target product. Returns normalized product details for one Target item, including product content, images, price, rating, category, and availability flags for the selected store.
- **Params:** `store_id` (integer, optional) — Target store id used for pricing and availability; `tcin` (string, **required**) — Numeric Target item id (TCIN)

## IKEA (3)

### `ikea_category`

- **HTTP:** `GET /ikea/category`
- **What:** Browse an IKEA category. Returns one page of an IKEA category's product listing, with real offset/size pagination and sort. category is IKEA's own category key (e.g. 20649), taken from a category URL's trailing -{key}/ segment or a product's own category_path field.
- **Params:** `category` (string, **required**) — IKEA category key; `country` (string, optional) — Lowercase 2-letter IKEA site country code; `language` (string, optional) — Lowercase 2-letter IKEA site language code; `offset` (integer, optional) — Zero-based result offset; `size` (integer, optional) — Result count (1-100); `sort` (string, optional) — Result order

### `ikea_product`

- **HTTP:** `GET /ikea/product`
- **What:** Get an IKEA product's detail. Returns one IKEA item's full normalized detail: name, price, rating, every product image, quick facts, and category breadcrumb path. item_no is IKEA's own item number (8 digits, optionally prefixed with "s" for a combination/set article), taken from a search result's item_no field or an ikea.com product page's own URL.
- **Params:** `country` (string, optional) — Lowercase 2-letter IKEA site country code; `item_no` (string, **required**) — IKEA item number; `language` (string, optional) — Lowercase 2-letter IKEA site language code

### `ikea_search`

- **HTTP:** `GET /ikea/search`
- **What:** Search IKEA products. Searches IKEA products and returns normalized name, price, rating, images, colors, and variant data. q is a free-text query; an IKEA item number also resolves as its own single result. country and language select IKEA's per-country site (default us/en). A zero total with an empty products list is a valid no-results response.
- **Params:** `country` (string, optional) — Lowercase 2-letter IKEA site country code; `language` (string, optional) — Lowercase 2-letter IKEA site language code; `q` (string, **required**) — Free-text product search query; `size` (integer, optional) — Result count (1-100)
