# target-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**8 endpoints across 1 platform group(s).**

## Target (8)

### `target_categories`

- **HTTP:** `GET /target/categories`
- **What:** List all Target categories. Lists Target's top-level category menu in `categories`, plus the grouped shop-all directory in `groups`. Each category has an `id` (the one used by `/target/category-products`), name, canonical URL and, when Target supplies one, an image URL. The response also gives `count` and `group_count`. Takes no parameters.
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
- **What:** Get a Target product. Returns product details for one Target item, including product content, images, price, rating, category, and availability flags for the selected store.
- **Params:** `store_id` (integer, optional) — Target store id used for pricing and availability; `tcin` (string, **required**) — Numeric Target item id (TCIN)

### `target_questions`

- **HTTP:** `GET /target/questions`
- **What:** List Target product questions and answers. Lists customer questions for a Target item given by its numeric `tcin`, each with its text, author, submission time, helpful votes and nested answers. `page` is zero-based and `per_page` runs 1 to 25. The response gives `total_pages` and `count` for paging.
- **Params:** `page` (integer, optional) — Zero-based page; `per_page` (integer, optional) — Questions per page; `tcin` (string, **required**) — Numeric Target item id

### `target_reviews`

- **HTTP:** `GET /target/reviews`
- **What:** List Target product reviews. Lists written reviews for a Target item given by its numeric `tcin`. Each review has its rating, title, text, author, submission time, helpful votes, and verified and syndicated flags. `page` is zero-based and stops at 50; `per_page` runs 1 to 25. The response gives `total` and `total_pages`.
- **Params:** `page` (integer, optional) — Zero-based page; `per_page` (integer, optional) — Reviews per page; `tcin` (string, **required**) — Numeric Target item id

### `target_search`

- **HTTP:** `GET /target/search`
- **What:** Search Target products. Searches Target products and returns products plus every filter group and option available for the current result set. Pass option ids back through filter_ids as a comma-separated list. A zero total with an empty products list is a valid no-results response. The sort enum accepts `relevance`, `featured`, `price-low`, `price-high`, `rating`, `bestselling`, and `newest`.
- **Params:** `filter_ids` (string, optional) — Comma-separated Target filter option ids; `page` (integer, optional) — One-based page (1-50); `q` (string, **required**) — Product search query; `sort` (string, optional) — Result order; `store_id` (integer, optional) — Target store id used for pricing

### `target_stores`

- **HTTP:** `GET /target/stores`
- **What:** Find Target stores near a location. Returns Target's physical stores near a ZIP code, a free-text "city, state", or a "latitude,longitude" pair, including each store's store_id, status, distance, phone, address, service list, time zone, and two weeks of daily opening hours. Use the returned store_id values with the store_id parameter on target-search, target-category-products, target-filter-options, and target-product.
- **Params:** `limit` (integer, optional) — Maximum stores to return (1-20); `place` (string, **required**) — ZIP code, city/state, or latitude,longitude; `within` (integer, optional) — Search radius in miles (1-5000)
