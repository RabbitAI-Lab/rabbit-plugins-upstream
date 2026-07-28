# Storefront — Speed, Search and the Pages Themselves

The storefront's job is to let a decided customer buy and an undecided one find. Both are lost by the same three things: **slow pages, weak site search, and navigation that hides the catalog**.

**Before optimizing**, read `## Metrics` for the store's own mobile conversion rate and any performance baseline recorded. Optimizing without a before-number produces improvements nobody can defend later.

## Core Web Vitals, and What Moves Them in a Store

Targets (the "good" thresholds): **LCP under 2.5 s · INP under 200 ms · CLS under 0.1**, measured at the 75th percentile of real users on mobile. INP replaced FID as the responsiveness metric in 2024, and it is the one most stores fail, because it measures the cost of their scripts.

| Metric | Store-specific cause | Fix |
|---|---|---|
| LCP | The hero or product image: unoptimized, lazy-loaded when it should not be, or waiting on a font | Serve modern formats, size to the viewport, preload the LCP image, never lazy-load above the fold |
| LCP | Render-blocking app scripts in the head | Defer everything not needed for first paint; audit what each app injects |
| INP | Third-party tags: chat widgets, reviews, personalization, analytics, consent banners | Load on interaction or after idle; the number of apps *is* the metric |
| CLS | Images without dimensions, banners injected late, fonts swapping | Reserve space with width/height or aspect-ratio; preload fonts, `font-display: swap` with a matched fallback |
| All three | Theme code that queries the full catalog to render a menu | Cache the menu; paginate everything |

- **Measure field data (real users), not only lab scores.** A perfect lab score with a bad field score means the tested conditions are not the customers' conditions.
- Test on a mid-range Android on a throttled connection. A storefront that is fast on the developer's phone has been tested by nobody (`checkout.md`).
- The app-count discipline is the highest-leverage performance work in hosted stores: each app is script weight on every page. Removing three unused apps beats most image work.

## Images

- Modern formats (AVIF/WebP) with a fallback, responsive `srcset` sized to real breakpoints, and compression tuned per category — product detail shots need more quality than lifestyle backgrounds.
- One canonical source image per product at high resolution; every derivative generated, never hand-uploaded. Hand-uploaded derivatives are how a store ends up with a 4 MB thumbnail (`catalog.md`).
- Zoom and gallery scripts load after the main image, not before it.
- Alt text describes the product for a buyer who cannot see it — that serves accessibility, image search and feeds at once.

## Site Search

Searchers convert several times better than browsers, which makes search failures unusually expensive.

| Failure | Fix |
|---|---|
| Zero results for a real product | Synonyms and misspelling tolerance; review the zero-result report weekly (`## Due`) |
| Results ignore stock status | Sort in-stock first, never hide out-of-stock silently |
| Searching a SKU or model number returns nothing | Index SKU, GTIN and MPN fields (`catalog.md`) |
| Category names return nothing | Index collections as results, not only products |
| No results for a competitor or a nickname customers use | Synonym dictionary, built from the search log itself |
| Search results page has no filters | Facets on search results, same as a collection page |

The search log is the cheapest product-research tool in the store: the top zero-result queries are either a catalog gap or a naming gap, and both are worth money.

## Navigation, Collections and Filters

- Depth over breadth fails on mobile: a customer should reach any product family in two taps. A mega-menu that lists everything is a menu nobody reads.
- Filters must come from structured attributes that exist on every product in the collection; a filter that hides valid products is a silent revenue leak (`catalog.md`).
- Sort defaults matter: "featured" should be a curated, margin-aware order, not creation date. Newest-first as a default buries your best sellers.
- **Facet indexation is a decision, not an accident**: pick the one or two commercially valuable facet types to index, canonicalize the rest, and write the rule down. Unmanaged facets generate thousands of near-duplicate URLs that consume crawl budget (`acquisition.md`).
- Pagination: infinite scroll must still produce crawlable, linkable pages, and must not break the back button — the most common cause of "I lost the product I was looking at".

## Caching and Delivery

- Static assets on a CDN with long cache lifetimes and content-hashed filenames; HTML cached carefully — a cached page showing another customer's cart is the classic personalization bug.
- **Never cache anything keyed to a session** at the CDN. Cart, account and checkout are always dynamic; the cart badge belongs to a client-side call.
- Prices change: cached collection pages must be invalidated on price and availability changes, or the store advertises a price it will not honour (SKILL.md Rule 1).
- Third-party scripts are the tail that wags the storefront. Keep an inventory of every tag with its owner and its purpose, and delete the orphans quarterly (`analytics.md`).

## Accessibility

Not optional, and not only ethical: accessibility legislation now applies to consumer-facing digital services in a growing number of markets, and the same fixes improve conversion for everyone.

- Keyboard-navigable everywhere, including variant selectors, filters, modals and the cart drawer.
- Contrast that survives on a phone in daylight; never colour alone to convey availability or errors.
- Labelled form fields with error messages tied to the field, announced to screen readers — the same fix that reduces checkout abandonment (`checkout.md`).
- Alt text on product images, and no critical information delivered only in an image.
- Focus states visible; skip-to-content link present; motion reduced when the user asks for it.

## Errors, 404s and Out-of-Stock Pages

| Page | Should do |
|---|---|
| 404 | Search box, top collections, and the nearest match — never a dead end |
| Discontinued product | Stay live, say it is discontinued, and offer the replacement or the category (`catalog.md`) |
| Out of stock | Take an email for restock notification; that list is the cheapest demand signal a store gets |
| Checkout error | Preserve the entered data and say which field failed (`checkout.md`) |
| Maintenance | A real page with an expected return time, not a blank 503 |

**Write after storefront work**: performance baselines (LCP, INP, CLS at p75, mobile) into `## Metrics` with their `as of` date; the app inventory and any app removed for performance into `## Store`; a zero-result search pattern that revealed a catalog gap into `## Pain Points`; the facet indexation rule, the tag inventory and any theme decision into `artifacts/<kebab-name>.md`; and the search-log and tag-audit cadences into `## Due` — each with its `## Boxes` line in the same turn (`memory-template.md`).
