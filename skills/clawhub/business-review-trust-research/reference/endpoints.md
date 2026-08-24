# business-review-trust-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**41 endpoints across 6 platform group(s).**

## ProductHunt (11)

### `producthunt_about`

- **HTTP:** `GET /producthunt/product/{id}/about`
- **What:** Retrieve Product Hunt product about page. Returns the richer Product Hunt about-page payload, including launch, forum, review tags, and media data.
- **Params:** `id` (string, **required**) — Product Hunt slug

### `producthunt_alternatives`

- **HTTP:** `GET /producthunt/product/{id}/alternatives`
- **What:** Retrieve Product Hunt product alternatives. Returns paginated alternatives, tags, and related discussions for a Product Hunt product.
- **Params:** `cursor` (string, optional) — Pagination cursor; `first` (integer, optional) — Page size; `id` (string, **required**) — Product Hunt slug; `order` (string, optional) — Sort order; `tags` (string, optional) — Comma-separated tag slugs

### `producthunt_category`

- **HTTP:** `GET /producthunt/category/{slug}`
- **What:** Retrieve Product Hunt category details. Returns the category page payload for a Product Hunt category slug.
- **Params:** `slug` (string, **required**) — Product Hunt category slug

### `producthunt_category_products`

- **HTTP:** `GET /producthunt/category/{slug}/products`
- **What:** Retrieve Product Hunt category products. Returns the products in a Product Hunt category (now backed by Product Hunt topics), cursor-paginated. Pass the `cursor` from a previous response's `end_cursor` to page; `page_size` controls the batch size. `page`, `featured_only`, `order` and `tags` are accepted for compatibility but no longer affect the result.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous response's end_cursor; `featured_only` (boolean, optional) — Accepted for compatibility; no longer affects results; `order` (string, optional) — Accepted for compatibility; no longer affects results; `page` (integer, optional) — Accepted for compatibility; use cursor to paginate; `page_size` (integer, optional) — Page size (number of products); `slug` (string, **required**) — Product Hunt category slug; `tags` (string, optional) — Accepted for compatibility; no longer affects results

### `producthunt_customers`

- **HTTP:** `GET /producthunt/product/{id}/customers`
- **What:** Retrieve Product Hunt product customers. Returns paginated customer products for a Product Hunt product using Product Hunt's ProductCustomersPage GraphQL operation.
- **Params:** `id` (string, **required**) — Product Hunt slug; `order` (string, optional) — Product Hunt customers order; `page` (integer, optional) — Page number; `page_size` (integer, optional) — Results per page

### `producthunt_launches`

- **HTTP:** `GET /producthunt/product/{id}/launches`
- **What:** Retrieve Product Hunt product launches. Returns paginated launch posts for a Product Hunt product using Product Hunt's ProductPageLaunches GraphQL operation.
- **Params:** `cursor` (string, optional) — Pagination cursor; `id` (string, **required**) — Product Hunt slug; `order` (string, optional) — Product Hunt launch order

### `producthunt_leaderboard`

- **HTTP:** `GET /producthunt/leaderboard`
- **What:** Retrieve Product Hunt leaderboard. Fetches Product Hunt leaderboard data for daily, weekly, monthly, or yearly scopes via Product Hunt GraphQL.
- **Params:** `cursor` (string, optional) — Pagination cursor; `date` (string, optional) — Anchor date in YYYY-MM-DD format. Used to derive missing year/month/day/week values.; `day` (integer, optional) — Daily day override; `featured` (boolean, optional) — Featured products only; `month` (integer, optional) — Daily/monthly month override; `order` (string, optional) — Ranking order override. Defaults to scope rank enum.; `scope` (string, optional) — Leaderboard scope: daily, weekly, monthly, yearly; `week` (integer, optional) — Weekly ISO week override; `year` (integer, optional) — Leaderboard year override

### `producthunt_makers`

- **HTTP:** `GET /producthunt/product/{id}/makers`
- **What:** Retrieve Product Hunt product makers. Returns maker items for a Product Hunt product.
- **Params:** `cursor` (string, optional) — Pagination cursor; `id` (string, **required**) — Product Hunt slug

### `producthunt_product`

- **HTTP:** `GET /producthunt/product/{id}`
- **What:** Retrieve Product Hunt product details. Returns the core Product Hunt product details.
- **Params:** `id` (string, **required**) — Product Hunt slug or numeric ID

### `producthunt_reviews`

- **HTTP:** `GET /producthunt/product/{id}/reviews`
- **What:** Retrieve Product Hunt product detailed reviews. Returns detailed review items for a Product Hunt product.
- **Params:** `id` (string, **required**) — Product Hunt slug

### `producthunt_search`

- **HTTP:** `GET /producthunt/search`
- **What:** Search for products, users, or launches on Product Hunt. Performs a full-text Product Hunt search and returns matching products, users, or launches.
- **Params:** `featured` (boolean, optional) — Launch search only: featured launches only; `page` (integer, optional) — Page number (1-based); `query` (string, **required**) — Search keywords; `topics` (string, optional) — Launch search only: comma-separated topic slugs; `type` (string, optional) — Result type: **product** (default), **user**, or **launch**

## TrustMRR (7)

### `trustmrr_acquire`

- **HTTP:** `GET /trustmrr/acquire`
- **What:** Get TrustMRR acquisition listings. Returns the for-sale startups rendered on the public TrustMRR /acquire marketplace page, with deal metrics (asking price, revenue, multiple, growth). Verified revenue figures come from supported payment providers.
- **Params:** _none_

### `trustmrr_categories`

- **HTTP:** `GET /trustmrr/categories`
- **What:** Get TrustMRR categories. Returns the TrustMRR startup category directory (slug, label, description, and keywords for each category).
- **Params:** _none_

### `trustmrr_category`

- **HTTP:** `GET /trustmrr/category/{slug}`
- **What:** Get TrustMRR category detail. Returns a single TrustMRR category page and the startups listed under it, with verified revenue and MRR figures.
- **Params:** `slug` (string, **required**) — TrustMRR category slug

### `trustmrr_leaderboard`

- **HTTP:** `GET /trustmrr/leaderboard`
- **What:** Get TrustMRR revenue leaderboard. Returns the top 100 startups ranked by the selected metric from the public TrustMRR leaderboard. Revenue and MRR figures are verified through supported payment providers.
- **Params:** `metric` (string, optional) — Leaderboard metric to rank by (default mrr)

### `trustmrr_marketplace`

- **HTTP:** `GET /trustmrr/marketplace`
- **What:** Get TrustMRR marketplace snapshot. Returns the public TrustMRR marketplace snapshot: the 25 most recently listed startups for sale and the current 25 best deals ranked by TrustMRR's recency-aware deal score. Revenue figures are verified through supported payment providers.
- **Params:** _none_

### `trustmrr_startup`

- **HTTP:** `GET /trustmrr/startup/{slug}`
- **What:** Get TrustMRR startup detail. Returns the full verified profile for a single TrustMRR startup by slug: revenue and MRR, growth, asking price and marketplace status, tech stack, marketing channels, and TrustMRR's AI-generated business summary.
- **Params:** `slug` (string, **required**) — TrustMRR startup slug

### `trustmrr_startups`

- **HTTP:** `GET /trustmrr/startups`
- **What:** List all TrustMRR startups. Returns a paginated list of every startup in the TrustMRR directory, discovered from the site's public sitemap. Each entry is a slug you can pass to /trustmrr/startup/{slug} for the full verified profile — together these two endpoints let you enumerate and scrape the entire directory without the authenticated marketplace API.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `page_size` (integer, optional) — Items per page (default 100, max 1000)

## Trustpilot (7)

### `trustpilot_business`

- **HTTP:** `GET /trustpilot/business/{slug}`
- **What:** Get Trustpilot business profile. Returns a summary Trustpilot business profile parsed from the public business page.
- **Params:** `slug` (string, **required**) — Trustpilot business slug

### `trustpilot_business_related`

- **HTTP:** `GET /trustpilot/business/{slug}/related`
- **What:** Get Trustpilot related businesses. Returns related company cards from Trustpilot's public business page rails.
- **Params:** `slug` (string, **required**) — Trustpilot business slug

### `trustpilot_business_reviews`

- **HTTP:** `GET /trustpilot/business/{slug}/reviews`
- **What:** Get Trustpilot business reviews. Returns paginated Trustpilot business reviews parsed from the public review page.
- **Params:** `date_from` (string, optional) — Date range start in YYYY-MM-DD; currently rejected by upstream; `date_to` (string, optional) — Date range end in YYYY-MM-DD; currently rejected by upstream; `language` (string, optional) — Review language code used by Trustpilot; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, optional) — Text search within reviews; `replied` (boolean, optional) — Filter to reviews with business replies; `slug` (string, **required**) — Trustpilot business slug; `stars` (integer, optional) — Filter by star rating from 1 to 5; `verified` (boolean, optional) — Filter to verified reviews

### `trustpilot_business_search`

- **HTTP:** `GET /trustpilot/business-units/search`
- **What:** Search Trustpilot business units. Returns normalized business-unit search results from Trustpilot's JSON business-unit search API.
- **Params:** `country` (string, optional) — Two-letter country code; defaults to US; `page` (integer, optional) — 1-based page number; defaults to 1; `page_size` (integer, optional) — Results per page; defaults to 20, maximum 100; `q` (string, **required**) — Search query

### `trustpilot_categories`

- **HTTP:** `GET /trustpilot/categories`
- **What:** Get Trustpilot categories. Returns the Trustpilot public category index grouped by top-level category.
- **Params:** _none_

### `trustpilot_category`

- **HTTP:** `GET /trustpilot/category/{slug}`
- **What:** Get Trustpilot category detail. Returns category metadata, company cards, and side rails from Trustpilot's public category page.
- **Params:** `page` (integer, optional) — 1-based page number; defaults to 1; `slug` (string, **required**) — Trustpilot category slug

### `trustpilot_category_search`

- **HTTP:** `GET /trustpilot/categories/search`
- **What:** Search Trustpilot categories. Returns normalized category search results from Trustpilot's JSON category search API.
- **Params:** `country` (string, optional) — Two-letter country code; defaults to US; `locale` (string, optional) — Locale in ll-CC format; defaults to en-US; `q` (string, **required**) — Search query; `size` (integer, optional) — Maximum number of categories; defaults to 20

## Capterra (3)

### `capterra_product`

- **HTTP:** `GET /capterra/product`
- **What:** Get a Capterra product. Returns a normalized Capterra product profile: name, description, category, and aggregate rating. Credential-free public Capterra data, rendered from the product page through proxied browser renderers.
- **Params:** `product_id` (string, **required**) — Capterra product id (the numeric id in a /p/{id}/{slug}/ URL)

### `capterra_reviews`

- **HTTP:** `GET /capterra/product/reviews`
- **What:** Get Capterra product reviews. Returns a page of normalized Capterra reviews (author, headline, rating) plus the product's aggregate rating. Credential-free public Capterra data, rendered from the reviews page through proxied browser renderers.
- **Params:** `page` (integer, optional) — Page number (default 1); `product_id` (string, **required**) — Capterra product id (the numeric id in a /p/{id}/{slug}/ URL)

### `capterra_search`

- **HTTP:** `GET /capterra/search`
- **What:** Search Capterra products. Returns Capterra search-result products (id, name, url, description, rating). Credential-free public Capterra data, rendered from the search page through proxied browser renderers. Note: Capterra renders a fallback product list even for queries with no genuine match, rather than a distinct empty-results page, so callers should treat low-relevance results as an upstream characteristic, not a bug.
- **Params:** `q` (string, **required**) — Search query

## BBB (9)

### `bbb_business`

- **HTTP:** `GET /bbb/business`
- **What:** Get a Better Business Bureau business profile. Returns a normalized bbb.org business profile: BBB rating letter grade and reasons, accreditation status and since-date, years in business, BBB file/incorporation dates, entity type, contact info, business categories, social media, and a short latest-reviews preview. Credential-free public Better Business Bureau data.
- **Params:** `url` (string, **required**) — BBB business profile URL, from a bbb-search result's url or hq_profile_url

### `bbb_business_complaints`

- **HTTP:** `GET /bbb/business/complaints`
- **What:** Get a Better Business Bureau business's complaint history. Returns a business's BBB complaint history: total complaint count, complaints closed in the last 12 months, and per-complaint detail (date, type, status, narrative text, and any business response / customer answer thread). A business with no filed complaints returns total_complaints 0 and an empty complaints list -- this is a normal result, not an error. Credential-free public Better Business Bureau data.
- **Params:** `url` (string, **required**) — BBB business profile URL, from a bbb-search result's url or hq_profile_url

### `bbb_business_more_info`

- **HTTP:** `GET /bbb/business/more-info`
- **What:** Get a Better Business Bureau business's full rating reasons and service area. Returns a business's full per-factor "Reasons for Rating" list and full service-area list, from the separate BBB business profile /more-info sub-page. The bbb-business endpoint's own rating_reasons field is read from the main profile page and typically holds only one generic boilerplate bullet regardless of actual rating; this endpoint fetches the richer, business-specific list instead. Service area is business-conditional -- some businesses render no service-area section at all, in which case service_areas is empty. Credential-free public Better Business Bureau data.
- **Params:** `url` (string, **required**) — BBB business profile URL, from a bbb-search result's url or hq_profile_url

### `bbb_business_reviews`

- **HTTP:** `GET /bbb/business/reviews`
- **What:** Get a Better Business Bureau business's customer reviews. Returns a business's full customer-review list (author, star rating, date, text, and any business response thread), paginated 10 per page, plus the average star rating and total review count. Credential-free public Better Business Bureau data. Unlike the other bbb-business-* endpoints, this one is fetched with browser impersonation rather than plain direct HTTP -- see the family's maintenance note for why.
- **Params:** `page` (integer, optional) — Result page (10 per page), default 1; `url` (string, **required**) — BBB business profile URL, from a bbb-search result's url or hq_profile_url

### `bbb_category`

- **HTTP:** `GET /bbb/category`
- **What:** Browse a Better Business Bureau category. Browses bbb.org businesses by category and location directly, without a free-text search query. Returns the same normalized business-result shape as bbb-search. Credential-free public Better Business Bureau data.
- **Params:** `page` (integer, optional) — Result page, default 1; `url` (string, **required**) — BBB category browse URL, from a bbb-search result's related_categories

### `bbb_scamtracker_detail`

- **HTTP:** `GET /bbb/scamtracker/{id}`
- **What:** Get a Better Business Bureau Scam Tracker report. Returns one normalized BBB Scam Tracker consumer scam report: description, dollars lost, targeted person's location, scammer location/email/phone/URL (when known), scam type, business name used, and date reported. Credential-free public Better Business Bureau data.
- **Params:** `id` (string, **required**) — BBB Scam Tracker report id, from a bbb-scamtracker-search result's id or url

### `bbb_scamtracker_search`

- **HTTP:** `GET /bbb/scamtracker/search`
- **What:** Search Better Business Bureau Scam Tracker reports. Searches bbb.org Scam Tracker's consumer-reported-scam database by free-text query, scam category, targeted-victim state/province, reported-scammer state/province, report-date range, and/or dollar-loss range, paginated 10 results/page. Omit every filter to browse the most-recent-first feed. Credential-free public Better Business Bureau data. This is a separate BBB dataset from the bbb-search/bbb-business/bbb-business-complaints business-rating family -- consumer-reported scam incidents, not business ratings.
- **Params:** `date_from` (string, optional) — Optional report-date range start (YYYY-MM-DD), inclusive. Must be set together with date_to; `date_to` (string, optional) — Optional report-date range end (YYYY-MM-DD), inclusive. Must be set together with date_from; `max_dollars_lost` (integer, optional) — Optional maximum reported dollar loss. Must be set together with min_dollars_lost; `min_dollars_lost` (integer, optional) — Optional minimum reported dollar loss. Must be set together with max_dollars_lost; `page` (integer, optional) — Result page (10 per page), default 1; `query` (string, optional) — Free-text search (phone number, website, email, business name, scam ID, description). Omit to browse the most-recent feed; `scam_type` (string, optional) — Scam category filter; `scammer_state` (string, optional) — Optional 2-letter reported-scammer state/province code (US state or Canadian province) -- where the scammer is reported to be, not the victim; `state` (string, optional) — Optional 2-letter targeted-victim state/province code (US state or Canadian province)

### `bbb_scamtracker_state_stats`

- **HTTP:** `GET /bbb/scamtracker/state-stats`
- **What:** Get Better Business Bureau Scam Tracker state/province aggregate stats. Returns aggregate scam-report stats per US state and Canadian province for a given time window: report counts, dollar losses, per-capita rates, year-over-year change, and top scam-type breakdown. This calls the same JSON API the BBB Scam Tracker heatmap dashboard's own frontend uses -- not an HTML scrape. Credential-free public Better Business Bureau data.
- **Params:** `period` (string, optional) — Aggregation window, default 90

### `bbb_search`

- **HTTP:** `GET /bbb/search`
- **What:** Search Better Business Bureau businesses. Searches bbb.org for businesses by name or category near a location. Returns each business's BBB rating letter grade, accreditation status, categories, service areas, contact info, and profile URL. Credential-free public Better Business Bureau data.
- **Params:** `location` (string, **required**) — City and state (e.g. 'Austin, TX') or a ZIP code; `page` (integer, optional) — Result page, default 1; `query` (string, **required**) — Business name or category/service keyword

## Kickstarter (4)

### `kickstarter_comments`

- **HTTP:** `GET /kickstarter/comments`
- **What:** Get a Kickstarter campaign's comments. Returns the first page of one Kickstarter campaign's comments feed (Kickstarter's own server-rendered initial batch, typically 40-60 comments; total_count reports the feed's real total). Each comment includes the author, whether the author is the creator (a reply), the posted timestamp, and the comment text. creator and slug are the two path segments of the project URL, e.g. lookingglass and musubi for kickstarter.com/projects/lookingglass/musubi.
- **Params:** `creator` (string, **required**) — Creator path segment of the project URL; `slug` (string, **required**) — Project slug path segment of the project URL

### `kickstarter_discover`

- **HTTP:** `GET /kickstarter/discover`
- **What:** Browse or search Kickstarter's Discover surface. Returns one page of Kickstarter's own Discover results -- browse by category id and/or a free-text search term, sorted by magic/popularity/newest/end_date/most_funded, optionally filtered by campaign state and/or restricted to staff picks. Each result includes the campaign's funding snapshot (goal, pledged, percent funded, backers), category, location, creator, and cover photo.
- **Params:** `category_id` (integer, optional) — Kickstarter's own numeric category id (top-level or sub-category), e.g. 16 for Technology; `page` (integer, optional) — 1-based page number; `sort` (string, optional) — Result order; `staff_pick_only` (boolean, optional) — Restrict results to Kickstarter's own \; `state` (array, optional) — Repeatable campaign state filter; `term` (string, optional) — Free-text search query

### `kickstarter_project`

- **HTTP:** `GET /kickstarter/project`
- **What:** Get a Kickstarter campaign's detail. Returns one Kickstarter campaign's detail: funding snapshot (goal, pledged, percent funded, backers, state, dates), category, creator, cover photo, story text, risks & challenges, update/comment/FAQ counts, and reward/pledge tiers. creator and slug are the two path segments of the project URL, e.g. lookingglass and musubi for kickstarter.com/projects/lookingglass/musubi. Reward tiers are best-effort -- see the endpoint's documentation for when they may be omitted.
- **Params:** `creator` (string, **required**) — Creator path segment of the project URL; `slug` (string, **required**) — Project slug path segment of the project URL

### `kickstarter_updates`

- **HTTP:** `GET /kickstarter/updates`
- **What:** Get a Kickstarter campaign's updates feed. Returns one Kickstarter campaign's full updates feed: for each update, its number, title, author, whether the author is the creator, publish date, body text, and comment count. creator and slug are the two path segments of the project URL, e.g. lookingglass and musubi for kickstarter.com/projects/lookingglass/musubi.
- **Params:** `creator` (string, **required**) — Creator path segment of the project URL; `slug` (string, **required**) — Project slug path segment of the project URL
