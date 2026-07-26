---
name: tiktok-shop-search
description: "Extract product search results from TikTok Shop by keyword and country region — returns product id, title, price, currency, seller, shop, rating, review count, sold count, images, SKU variants, brand, and product URL. Use when user mentions TikTok Shop, tiktok shop scraper, tiktok shop search, tiktokshop, shop.tiktok.com, tiktok e-commerce, tiktok marketplace, tiktok products, tiktok shop keyword search, tiktok shop product data, tiktok shop competitor research, tiktok shop trending items, tiktok social commerce, tiktok shop listing, tiktok shop pricing, tiktok shop seller data, tiktok shop reviews count, tiktok shop sold count, scrape tiktok shop, extract tiktok shop products, tiktok shop by country, tiktok shop us, tiktok shop uk, tiktok shop by keyword. Also applies to social commerce market research, dropshipping product discovery, tiktok product trend spotting, seller performance monitoring on tiktok, price and discount tracking across the tiktok shop catalog, and building tiktok shop product datasets from a list of search queries."
---

# TikTok Shop — Search Results

> Input a keyword and a country code → output a paginated list of matching TikTok Shop products with prices, sellers, ratings, sold counts, images and SKU variants.

## Language

All process output to user (progress updates, process notifications) follows the user's language.

## Objective

Retrieve TikTok Shop search result products for a given keyword under a specific country region, extracting complete listing data (title, price, currency, seller, shop, rating, sold count, images, SKUs) for market research, competitor tracking and dropshipping product discovery.

## Prerequisites

- Target page is already open in the browser: `https://shop.tiktok.com/{country_code_lower}/s?q={keyword}` (e.g. `https://shop.tiktok.com/us/s?q=lipstick`)
- No login required. The keyword search page renders products server-side and is publicly accessible

## Pre-execution Checks

### 1. Tool Readiness

If browser-act has been confirmed available in the current session → skip this step.

Invoke `browser-act` via Skill tool to load usage. If installation or configuration issues arise, follow its guidance to resolve then retry.

## Capability Components

> This Skill's operational boundary = what the user can manually do in their browser. It only reads data already displayed to the user on the page, never bypassing authentication or access controls. Its role is equivalent to copy-pasting on the user's behalf — the data is already on screen, automation merely saves time. JS code is encapsulated in Python files under the `scripts/` directory, invoked via `eval "$(python scripts/xxx.py {params})"`. `$(...)` is bash syntax; it is recommended to use the bash tool for execution.

Below are all atomic capabilities discovered and verified during the exploration phase, listed by command template with parameters. Simply invoke them as needed — no need to read `scripts/*.py` source code or re-verify. Only inspect scripts when execution fails for troubleshooting. Combine freely as needed during execution.

### Network Capture: get search result products (parameters injected via URL navigation)

The search page renders products into the HTML server-side inside a `__MODERN_ROUTER_DATA__` JSON script. Business parameters (keyword, country region, page) are injected via URL; product data is extracted from the SSR script via DOM.

1. `navigate https://shop.tiktok.com/{country_code_lower}/s?q={keyword}&page={page}`
   - `{country_code_lower}` is the lowercase 2-letter region code (e.g. `us`, `gb`, `de`)
   - `{keyword}` must be URL-encoded (spaces become `%20` or `+`)
   - `{page}` is optional; omit for the first result set (15 products), pass `2`, `3`, ... to request more (server may return up to 30 products with `has_more=true`)
2. `wait stable`
3. `eval "$(python scripts/extract-search-results.py --country_code {country_code_upper})"`
   - `{country_code_upper}` is the uppercase form written back into each product record

Endpoint characteristic: SSR data lives in `<script id="__MODERN_ROUTER_DATA__" type="application/json">`; the search feed is at `loaderData['(region)/(route_page_name)/page'].page_config.components_map[?].component_name === 'feed_list_search_word'`.

Error handling:
- Response returns `{"error": true, "message": "SSR data script __MODERN_ROUTER_DATA__ not found..."}` — the URL was redirected (e.g. to a captcha or region-blocked page). Take a `screenshot` to inspect. If a slider/puzzle captcha is present, use `remote-assist` to have the user complete verification, then retry
- Response returns `{"error": true, "message": "Search feed component (feed_list_search_word) not found..."}` — this typically happens when the country region has no TikTok Shop coverage from the current IP or when the search returned no products. Confirm with `get title` (title should contain the keyword) and `screenshot` (page should show product cards); if the page shows "No results found", the search legitimately has no matches
- `count == 0` with `has_more == false` — legitimate no-results outcome

Output example:
```json
{
  "keyword": "lipstick",              // search keyword extracted from the page's route_info
  "country_code": "US",               // uppercase country code passed via --country_code
  "count": 30,                         // number of products in this page
  "has_more": true,                    // whether the server indicates more results exist
  "load_more_params": {                // opaque token for subsequent page requests (server-side only)
    "offset": 30,
    "page_token": "20260708104613F63F68A6F8279A03FF71",
    "api_source": 2
  },
  "products": [
    {
      "rank": 1,                       // 1-based position within this response
      "id": "1732349662666133893",   // product id
      "title": "Smooth Texture 12-Color Lip Cosmetic Set...",
      "keyword": "lipstick",
      "country_code": "US",
      "currency": "USD",
      "price": "$14.99",              // display price with currency symbol
      "min_price": 14.99,             // numeric sale price
      "max_price": 14.99,             // numeric sale price (equals min_price for single-price items)
      "origin_price": "$35.99",       // pre-discount price with symbol, null if not discounted
      "discount_format": "58%",       // percentage off, null if no discount
      "product_rating": 3,             // average rating 0-5, null if no reviews
      "review_count": 2,               // number of reviews, null if none
      "sold_count": 121,               // total sold quantity, null if hidden
      "sold_count_str": "121",         // formatted string (may contain K/M suffix)
      "seller_id": "7494497798489408901",
      "seller_name": "COCOBALA Comstics",
      "shop": {
        "shop_id": "7494497798489408901",
        "shop_name": "COCOBALA Comstics",
        "shop_logo": ["tos-alisg-i-.../5ba198ca...", "https://p16-oec-general.../..."]
      },
      "brand": null,                   // brand name or null
      "images": [                       // primary product image (uri then CDN url variants)
        "tos-useast5-i-.../dcad684...",
        "https://p16-oec-general-useast5.ttcdn-us.com/tos-useast5-i-.../dcad684...~tplv-.webp",
        "https://p19-oec-general-useast5.ttcdn-us.com/tos-useast5-i-.../dcad684...~tplv-.webp"
      ],
      "transparent_images": [          // transparent-background image variants (if provided)
        "tos-maliva-i-.../4af4dcb...",
        "https://p16-oec-general.ttcdn-us.com/tos-maliva-i-.../4af4dcb...~tplv-.webp"
      ],
      "product_url": "https://shop.tiktok.com/us/pdp/smooth-texture-12-color-lip-set-.../1732349662666133893",
      "slug": "smooth-texture-12-color-lip-set-matte-glossy-smudge-proof",
      "skus": [                         // SKU variants for this product
        {
          "sku_id": "1732349827825308037",
          "price": 14.99,
          "price_str": "$14.99",
          "currency": "USD",
          "origin_price": 35.99,
          "discount_format": "58%"
        }
      ]
    }
  ]
}
```

## Enum Parameters

[AI] `country_code`: TikTok Shop supports the following 2-letter region codes (uppercase used for output field, lowercase used inside URL path): `US`, `VN`, `TH`, `PH`, `MY`, `ID`, `GB`, `SG`, `ES`, `MX`, `DE`, `IT`, `FR`, `BR`, `JP`. Regions other than `US` require the browser's outbound IP to be inside (or accepted by) the target region; from a US IP, non-US regions typically return "No results found" or block the request.

## Pagination

**URL Pagination**: URL pattern `https://shop.tiktok.com/{country_code_lower}/s?q={keyword}&page={N}`. The first request (no `page` or `page=1`) returns up to 15 products; subsequent pages (`page=2`, `page=3`, ...) may return up to 30 products in one payload. Termination: `has_more == false` in the extracted output, or `count == 0`. The server caps how deep pagination can go — when `has_more` becomes `false`, stop; do not assume unlimited depth.

## Success Criteria

`response.error !== true && response.count >= 1 && response.products.every(p => p.id && p.title && p.currency)`

For legitimate "no results" outcomes (`count == 0 && has_more == false` without an `error` field), the capability is considered to have executed successfully with an empty result set.

## Known Limitations

- Non-US country regions require the browser's outbound IP to originate from (or be accepted by) the target region. From a US-based IP, `country_code` values other than `US` typically return "No results found" or trigger a captcha wall. To collect data for other regions, use a stealth browser bound to a matching country dynamic proxy
- The unauthenticated public search page returns a hard cap of ~30 products per URL request; deeper pagination beyond `has_more == false` is not supported through the SSR path
- First-time visits from a fresh IP may trigger a slider/puzzle captcha before the search page loads; auto-solve does not cover this widget, so `remote-assist` is required for the first request from a new IP
- Some fields exposed by the original inspiration source (`biz_type`, `commission_rate`, `first_time` / `last_time` timestamps, `week_sales`, `week_sold_count`, `total_sales`) are seller-back-office data and are NOT available from the public search page; those fields are intentionally omitted
- `min_price` and `max_price` both reflect the current sale price returned by the page; multi-SKU price ranges are represented via the `skus` array

## Execution Efficiency

- **Batch orchestration**: Write a bash script to loop through the command templates serially within a single session; do not parallelize within one browser (prone to triggering anti-scraping restrictions). Refer to rate information in "Known Limitations" above to add appropriate intervals. To increase throughput, open multiple stealth browser sessions and distribute work across them — each session has an independent fingerprint so rate limits apply per session
- **Test before batch execution**: After writing a batch script, you must first test with 1-2 items to verify the script runs correctly; only then run the full batch. Never skip testing and execute in batch directly
- **Reduce redundant pre-operations**: When multiple keywords need to run against the same country region, keep the same session open and only re-navigate; do not re-open the browser per keyword
- **Error resumption**: Save results item by item during batch processing; on failure, resume from the breakpoint rather than starting over

## Experience Notes

Path: `{working-directory}/browser-act-skill-forge-memories/tiktok-shop-search-scraper-tiktok-shop-search.memory.md` (working directory is determined by the Agent running the Skill, typically the project root or current working directory)

**Before execution**: If the file exists, read it first — it records unexpected situations encountered during past executions (e.g., a strategy has become ineffective); adjust strategy order accordingly.

**After execution**: If an unexpected situation is encountered (strategy became ineffective, page redesigned, anti-scraping upgraded, better path discovered), append a line:
`{YYYY-MM-DD}: {what happened} → {conclusion}`

Normal execution does not write to the file. Do not record what keywords were used or how many results were returned — those are task outputs, not experience.
