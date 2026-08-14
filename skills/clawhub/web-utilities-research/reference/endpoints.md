# web-utilities-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**19 endpoints across 6 platform group(s).**

## Numbeo (8)

### `numbeo_cost_of_living_city`

- **HTTP:** `GET /numbeo/cost-of-living/city/{slug}`
- **What:** Get a Numbeo city's cost-of-living prices. Returns itemized cost-of-living prices for one city (restaurants, markets, transportation, utilities, rent, and more), grouped by category. Credential-free public Numbeo data (numbeo.com).
- **Params:** `slug` (string, **required**) — Numbeo city slug

### `numbeo_cost_of_living_country`

- **HTTP:** `GET /numbeo/cost-of-living/country`
- **What:** Get a Numbeo country's cost-of-living prices. Returns aggregate itemized cost-of-living prices for a country, plus the headline cost-of-living indices for every city Numbeo tracks there. Credential-free public Numbeo data (numbeo.com).
- **Params:** `country` (string, **required**) — Country name as Numbeo spells it

### `numbeo_cost_of_living_rankings`

- **HTTP:** `GET /numbeo/cost-of-living/rankings`
- **What:** Get the global Numbeo cost-of-living city ranking. Returns the global cost-of-living city ranking (Cost of Living, Rent, Cost of Living Plus Rent, Groceries, Restaurant Price, and Local Purchasing Power indices), either the continuously-updated current index or a historical periodic snapshot. Credential-free public Numbeo data (numbeo.com).
- **Params:** `period` (string, optional) — Required when scope=historical, e.g. 2026-mid or 2025; `scope` (string, optional) — current (default) or historical

### `numbeo_cost_of_living_rankings_by_country`

- **HTTP:** `GET /numbeo/cost-of-living/rankings-by-country`
- **What:** Get the global Numbeo cost-of-living country ranking. Returns the global country-level cost-of-living ranking (Cost of Living, Rent, Cost of Living Plus Rent, Groceries, Restaurant Price, and Local Purchasing Power indices). Credential-free public Numbeo data (numbeo.com).
- **Params:** _none_

### `numbeo_indices_city`

- **HTTP:** `GET /numbeo/indices/city/{slug}`
- **What:** Get a Numbeo city's data for an index family. Returns one city's data for a Numbeo index family (quality of life, crime, health care, pollution, traffic, or property investment): headline indices, and (depending on the family) titled sub-index sections and/or itemized prices. Credential-free public Numbeo data (numbeo.com).
- **Params:** `index` (string, **required**) — Index family; `slug` (string, **required**) — Numbeo city slug

### `numbeo_indices_country`

- **HTTP:** `GET /numbeo/indices/country`
- **What:** Get a Numbeo country's data for an index family. Returns one country's aggregate data for a Numbeo index family, plus every city Numbeo tracks there with its index breakdown. Credential-free public Numbeo data (numbeo.com).
- **Params:** `country` (string, **required**) — Country name as Numbeo spells it; `index` (string, **required**) — Index family

### `numbeo_indices_rankings`

- **HTTP:** `GET /numbeo/indices/rankings`
- **What:** Get the global Numbeo city ranking for an index family. Returns the global city ranking for a Numbeo index family, either the continuously-updated current index or a historical periodic snapshot. Credential-free public Numbeo data (numbeo.com).
- **Params:** `index` (string, **required**) — Index family; `period` (string, optional) — Required when scope=historical, e.g. 2026-mid or 2025; `scope` (string, optional) — current (default) or historical

### `numbeo_indices_rankings_by_country`

- **HTTP:** `GET /numbeo/indices/rankings-by-country`
- **What:** Get the global Numbeo country ranking for an index family. Returns the global country-level ranking for a Numbeo index family. Credential-free public Numbeo data (numbeo.com).
- **Params:** `index` (string, **required**) — Index family

## Geocoding (3)

### `geocoding_lookup`

- **HTTP:** `GET /geocoding/lookup`
- **What:** Lookup Nominatim OSM ids. Returns typed Nominatim JSONv2 places for comma-separated OSM ids such as W34633854,N123,R456.
- **Params:** `accept_language` (string, optional) — Preferred result language, forwarded to Nominatim; `addressdetails` (boolean, optional) — Include address details, defaults to true; `extratags` (boolean, optional) — Include OSM extra tags; `namedetails` (boolean, optional) — Include multilingual name details; `osm_ids` (string, **required**) — Comma-separated OSM ids such as W34633854,N123,R456

### `geocoding_reverse`

- **HTTP:** `GET /geocoding/reverse`
- **What:** Reverse geocode coordinates. Returns the nearest typed Nominatim JSONv2 place for latitude and longitude.
- **Params:** `accept_language` (string, optional) — Preferred result language, forwarded to Nominatim; `addressdetails` (boolean, optional) — Include address details, defaults to true; `extratags` (boolean, optional) — Include OSM extra tags; `lat` (number, **required**) — Latitude; `lon` (number, **required**) — Longitude; `namedetails` (boolean, optional) — Include multilingual name details; `zoom` (integer, optional) — Nominatim address zoom, defaults to 18

### `geocoding_search`

- **HTTP:** `GET /geocoding/search`
- **What:** Search Nominatim places. Returns typed Nominatim JSONv2 forward geocoding results. Use either q or structured fields, not both.
- **Params:** `accept_language` (string, optional) — Preferred result language, forwarded to Nominatim; `addressdetails` (boolean, optional) — Include address details, defaults to true; `city` (string, optional) — Structured city; `country` (string, optional) — Structured country; `countrycodes` (string, optional) — Comma-separated ISO 3166-1 alpha-2 country filters; `county` (string, optional) — Structured county; `extratags` (boolean, optional) — Include OSM extra tags; `limit` (integer, optional) — Maximum results, defaults to 10 and clamps to 20; `namedetails` (boolean, optional) — Include multilingual name details; `postalcode` (string, optional) — Structured postal code; `q` (string, optional) — Free-text search query; `state` (string, optional) — Structured state; `street` (string, optional) — Structured street or house number

## Web (3)

### `extract`

- **HTTP:** `POST /extract`
- **What:** Extract schema-conforming JSON from a URL. Scrapes a public URL into clean Markdown, then returns data that strictly conforms to the supplied bounded JSON Schema.
- **Params:** `extractOption` (object, **required**) — Extraction options

### `web_scrape`

- **HTTP:** `POST /web/scrape`
- **What:** Scrape a URL into markdown, HTML, links or metadata. Fetches a single public URL and returns clean content in the requested formats (markdown, html, raw_html, links, metadata). With render=auto the request starts as a fast HTTP fetch and escalates to a real browser when the page is blocked or rendered with JavaScript. only_main_content (default true) strips navigation, headers, footers and other boilerplate before conversion. Only public pages are supported; respect each site's terms of use and robots directives.
- **Params:** `scrapeOption` (object, **required**) — Scrape options

### `web_techstack`

- **HTTP:** `POST /web/techstack`
- **What:** Tech stack — detect what a website is built with. Fetches a public URL and fingerprints the web technologies it is built with — a BuiltWith / Wappalyzer-style detector. Returns a list of detected `technologies`, each with its `categories`, a `confidence` (`high`, `medium`, `low`), an optional `version`, and the `evidence` that matched. Covers JavaScript frameworks and libraries (React, Vue.js, Angular, Svelte, jQuery), web frameworks / static site generators (Next.js, Nuxt.js, Gatsby, Remix, SvelteKit, Astro, Hugo), CMS and website builders (WordPress, Drupal, Joomla, Ghost, Wix, Squarespace, Webflow), e-commerce (Shopify, WooCommerce, Magento, BigCommerce), analytics, ad pixels, and tag managers (Google Analytics, Google Tag Manager, Meta Pixel, LinkedIn, Bing, TikTok/Pinterest/Reddit pixels, Segment, Hotjar, Microsoft Clarity), CDNs, UI frameworks and fonts, payments (Stripe, PayPal, Klarna), live chat, marketing automation, A/B testing, consent management, CAPTCHAs (reCAPTCHA, hCaptcha, Turnstile), video, and search. It also inspects response headers (from a plain HTTP fetch) to identify the web server (nginx, Apache, IIS), the CDN / hosting provider (Cloudflare, CloudFront, Fastly, Vercel, Netlify), and the server-side language / framework (PHP, ASP.NET, Ruby on Rails, Django, Laravel, Express). Results are directional, not exhaustive. The `render` fetch strategy is one of `browser` (headless browser that executes JavaScript — the default, so client-injected scripts like analytics, tag managers and pixels are detected), `auto` (Chrome-impersonated HTTP, escalating to a real browser only when blocked or JS-rendered), or `http` (HTTP only, no JavaScript — fastest, but sees only the server HTML); defaults to `browser`. Only public pages are supported; respect each site's terms of use and robots directives.
- **Params:** `request` (object, **required**) — Target URL (and optional render strategy)

## ImportYeti (2)

### `importyeti_company`

- **HTTP:** `GET /importyeti/company`
- **What:** Get an ImportYeti company report. Returns a normalized ImportYeti company report: identity, headline US customs shipment-volume metrics (total shipments, average TEU, last shipment date, estimated shipping spend), its supplier list, and recent bill-of-lading shipment activity. Credential-free public data, rendered from the company report page through proxied browser renderers.
- **Params:** `slug` (string, **required**) — ImportYeti company slug, the last path segment of a /company/{slug} URL

### `importyeti_search`

- **HTTP:** `GET /importyeti/search`
- **What:** Search ImportYeti companies and suppliers by name. Searches ImportYeti for companies and suppliers matching a name, returning each match's kind (company or supplier), slug, country, address, and headline shipment stats. A "company" result's slug chains into GET /importyeti/company. Credential-free public data, sourced from ImportYeti's own JSON search API (distinct from its human-facing /search results page, which does not render due to a client-side bug in ImportYeti's own app).
- **Params:** `page` (integer, optional) — 1-indexed result page, defaults to 1; `q` (string, **required**) — Company or supplier name to search for

## SimilarWeb (2)

### `similarweb_search`

- **HTTP:** `GET /similarweb/search`
- **What:** Search SimilarWeb Info. Returns SimilarWeb data for a given query (typically a domain).
- **Params:** `q` (string, **required**) — Domain or keyword to search

### `similarweb_web`

- **HTTP:** `GET /similarweb/web/{domain}`
- **What:** Get SimilarWeb Web Info. Returns traffic and engagement data from SimilarWeb for a specific domain.
- **Params:** `domain` (string, **required**) — Domain to fetch SimilarWeb data for

## Brand (1)

### `brand_retrieve`

- **HTTP:** `GET /brand/retrieve`
- **What:** Retrieve brand data by domain. Fetches a domain's homepage and Web App Manifest and extracts a normalized brand profile (title, description, brand colors normalized to hex, logos and icons ranked best-first, backdrops, socials, links, and any schema.org organization data). Enrichment-only fields that are not present in the page markup are returned as null.
- **Params:** `domain` (string, **required**) — Domain to retrieve brand data for, e.g. context.dev; `force_language` (string, optional) — Accepted for compatibility; not applied in HTML-only mode; `maxAgeMs` (integer, optional) — Cache freshness window in milliseconds, clamps to 1 day..1 year; `maxSpeed` (boolean, optional) — Optimize for speed by skipping schema.org and footer-link extraction; `timeoutMS` (integer, optional) — Upstream fetch timeout in milliseconds, clamps to 1000..300000
