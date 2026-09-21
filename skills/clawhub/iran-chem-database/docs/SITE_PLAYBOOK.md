# Per-Site Navigation & Fetch Playbook — v2.35.0

**Read this before crawling anything.** v2.35.0 ships a measured profile for
every configured seed (`data/site_profiles.json`): per host — the method
chain that actually answers, the catalogue family, the pagination mechanics
found in real pages, which Persian/English nav controls exist, whether the
catalogue is login-gated, and entry-point endpoints with live row counts.
The adaptive selector already turns those profiles into per-site method
plans; this document tells the **agent** what to do with the rest: how to
enumerate each family, what "next" means there, and what a chemical row looks
like on it.

## 0. The algorithm (always)

1. Look up the host in `data/site_profiles.json` (or
   `python3 -m src.crawler.adaptive_selector --explain <host>`).
   The `chain` decides *how to fetch*; `family` + `pagination` decide
   *how to enumerate*.
2. Enumerate URLs cheapest-first: structured API → sitemap → listing pages.
   Never start with HTTrack if a REST/sitemap path exists.
3. Fetch with the profiled method; the engine demotes/defers on saturation —
   if you run manual probes, obey §5.
4. On each listing page, follow **only** the family's pagination pattern
   (§2), stop on: empty page / page > declared total / **content-hash
   repeat** (pager dead-end: same body as previous page ⇒ stop, mark tail).
5. A row counts as a catalogue row only if §3's chemical-shape test passes;
   news/blog/category pages are structure, not data.
6. Stamp freshness exactly as the engine does (`live` / `relay_or_archive` /
   `cached@<date>`). An archived or translate-proxy copy is never "today's
   stock".

## 1. Families (counts from the 2026-09-21 profile run below)

### A · WooCommerce REST stores — `family: woocommerce` / profile `woo_rest`
- Enumeration: `GET /wp-json/wc/store/v1/products?per_page=100&page=N`
  until `[]`; `X-WP-TotalPages` header gives the bound. Categories:
  `/wp-json/wc/store/v1/products/categories` (join products→categories as
  the catalogue tree). Prices: `prices.price` is the minor unit (÷100) and
  `currency_code` tells IRR/Toman vs EUR; `is_in_stock` is the shop's own
  flag — copy it, don't interpret.
- Next/prev buttons are irrelevant here — page parameter only; the HTML pager
  («بعدی») exists but re-parses what REST already gives structured.
- Product identity: `id`, `sku` (often the supplier code, NOT CAS),
  `permalink` `/product/<slug>/`. CAS/purity live in `description` — the
  parser's job, not the API's.
- Fallback if `/wp-json` is blocked: `/product-sitemap.xml` (root `<loc>` =
  product pages) → fetch product pages via the profiled method.

### B · WordPress without Store API — `sitemap_wp`
- `sitemap_index.xml` → pick child sitemaps whose URL/name contains
  product|shop|catalog|محصول → count `<loc>` ≈ catalogue size; fetch those
  URLs only (never site-wide crawl).
- Each product page: JSON-LD (`application/ld+json`, `@type: Product`,
  `identifier`/`sku`), else the DOM block `class~"woocommerce-product"` is
  the data zone; everything outside it (widgets/related) belongs to another
  page's inventory — do not scrape it as this supplier's own stock.
- Pagination where listings exist: `/page/N/` path style or `?product-page=N`;
  «بعدی» link class `next page-numbers`; stop when absent.

### C · Static HTML catalogues — `static_html` (the biggest family)
- Listing URLs carry `?cat=`, `?cid=`, `?p=`/`?page=`, `?start=`/`?offset=`
  or `/list-<n>.html`. Grab row links via `<a href>` matching
  `product|item|goods|prod?=`; row anchors inside `<table>`/`<ul>` with
  classes containing product/item/goods.
- Pager anatomy: `<a class="next">بعدی</a>` / `صفحه بعد`, numbered
  `<a>?page=(\d+)` — take **max page number adjacent to current** (a "12"
  next to "2" is the tail; "999" is usually junk) and walk, don't jump.
- «نمایش بیشتر / بارگذاری بیشتر» (load more) = AJAX GET on the same URL with
  `&page=N+1` (or `&start=N+50`): replay it, don't click it — the button
  handler is `$.get(..., append)`; the plain request is the canonical form.
- Infinite scroll markers (`lazyload|waypoint|infinite`): same replay via
  `X-Requested-With: XMLHttpRequest`; if the endpoint isn't discoverable,
  demote this host to `httrack` full-mirror and dedupe by URL.

### D · Legacy ASP.NET catalogs — `aspnet` (kimyapardazan-style sites)
- Listings are `GridView`s; pager emits
  `__doPostBack('ctl$…$Pager','Page$N')`. Enumeration = POST the listing
  page back to itself, replaying `__VIEWSTATE` + `__EVENTVALIDATION`
  verbatim with `__EVENTARGUMENT=Page$N` (viewstate is per-page — re-GET,
  don't cache across pages).
- Trap: these sites serve `<title>404</title>` error pages as HTTP 200 —
  reject any page < 1.5 kB or containing `aspxerrorpath` (they pollute
  mirrors; profile notes already say `zero-files`).
- Tables: rows `td` order is typically نام محصول | کد | گرید | بسته‌بندی |
  وضعیت; **no prices** — they sell by استعلام (inquiry) → price field stays
  null, availability from "موجود/ناموجود" cell only.

### E · JS-rendered shops — `profile: playwright_js`
- Skip the DOM scroll loop unless API replay fails: open DevTools-network
  equivalent — the SPA calls `/api/products?page=`, `/graphql`, or livewire
  `update()`; replay that GET/POST with the observed query — 10× cheaper
  than rendering. Only if no API emerges: `playwright` scroll-to-bottom until
  the «نمایش بیشتر» button is absent (that's the terminator).
- These hosts frequently 404 on direct and answer via `translate_goog`
  (AMP/JS shells render server-side there) — trust the profile's chain.

### F · Telegram storefronts — handled by `social_crawl`
- No HTTP crawl: mirror with `t.me/s/<channel>` backward pagination
  (already the skill engine). This playbook only matters when the same
  seller also has a website — cross-link via `forwarded from` harvest so a
  channel post and a `/product/…` page dedupe to one identity (CAS anchor).

### G · Everything geo-refused — relay-chain hosts (majority of `chain`
heads are `translate_goog`)
- The fetch goes through the public copy (translate/amp/jina/wayback/
  commoncrawl/arquivo) — enumeration rules from A–E still apply **on the
  relay's body**; translate.goog rewrites links but keeps `href` targets, so
  strip its `/-/translate/` prefix before following (jina keeps raw URLs;
  wayback needs `id_` flag to get the untouched HTML).
- Wayback/CC are the fallback *enumerators* too: `cdx?url=<host>&
  matchType=domain&collapse=urlkey&filter=statuscode:200` lists the whole
  archived catalogue; snapshot fetch `/web/<ts>id_/<url>`.

## 2. Universal pager lexicon (what the buttons actually say)

| control | English | Persian (RTL) | selector reality |
|---|---|---|---|
| next | Next › / next | بعدی / صفحه بعد | `a.next`, `a[rel=next]`, `[aria-label=next]` |
| prev | ‹ Prev | قبلی / صفحه قبل | `a.prev` — only for gap-filling |
| load more | Load more | نمایش بیشتر / بارگذاری بیشتر / مشاهده بیشتر | button→AJAX `page++` |
| tail | last « | آخرین / عدد بزرگ کنار صفحه فعلی | max adjacent number |
| in stock | in stock | موجود / آماده ارسال | row flag |
| out of stock | out of stock | ناموجود / تمام شده | row flag — keep the row, stock=false |
| price on request | — | استعلام قیمت / تماس بگیرید | price=null, keep offer flag |

## 3. "What am I looking at" — the chemical row test

A node is catalogue data iff **URL smells product** (`/product`, `/shop`,
`?prod`, `list?item`, `goods/`) or the block carries a `product|item` class,
**and** at least one identity token: a CAS with valid checksum
(`\b[1-9]\d{0,6}-\d{2}-\d\b`), an InChIKey, or name+purity shape —
`(9[59](\.\d)?%|≥9\d%|GR|AR|HPLC|Merck|Sigma|مولود|شیمی‌ران)` next to a
Persian/Latin product name. Otherwise it's a news/blog/SEO page —
**never** counted toward coverage. Units: `کیلوگرم/kg`, `گرم/g`, `لیتر/L`,
`تن`; Toman = 10⁴ IRR — keep the supplier's literal string in
`price_raw`, normalised value separately. Known Iranian-brand spellings that
must survive normalization: Kimia, Kimia Pars (کیمیا), Dana (دانا), Ibnsina,
Zagros, Karaj, Nouri, Mobarakeh.

## 4. Speed rules (this is what "no timers, no bugs" means here)

- **No global sleeps.** Politeness is per-(host, method) token bucket — the
  profiler and selector enforce it; crawl up to 12 hosts in parallel.
- Cheapest enumeration first (§0 step 2): one REST/sitemap fetch replaces
  hundreds of HTML pages. `X-WP-Total` / `<loc>` counts give you the size
  bound **before** downloading anything.
- Hard byte caps: profile 200 kB, catalogue pages 1 MB; streaming abort, not
  full-read-then-check.
- Dead-relay skip: `tools/relay_liveness.py --write-config` before a long
  crawl — a dead hop used to cost `timeout_seconds` per blocked host.
- Race for unknown hosts: `ICDB_RELAY_RACE=1` (staggered 900 ms, first
  gate-passing body wins).
- Stop conditions are data, not timers: empty page, > declared total, or
  content-hash repeat.

## 5. Saturation contract (agent + engine)

When the method you're pushing saturates for a site (429/503 streak, or
budget exhausted: origin 60 rpm / 600 kB·min⁻¹, relays 90 rpm / 3 MB·min⁻¹
fleet-wide) → the selector **demotes it for that host with an escalating
cooldown (60→120→300 s) and switches to the next-best sanctioned method of
that same site** (`data/site_profiles.json` chain). When all options are
saturated, the host is **deferred** (revisit at the cooldown expiry) — the
crawl keeps flowing on other hosts. Escalation in any form is out of
policy: no fingerprint/UA spoofing against a refusing origin, no origin-IP
hunting, no residential relays, no paywall/gate bypass (gated catalogues are
`gated:true` in profiles → contact lead only, `nav_found` never justifies a
login attempt). Public copies (wayback/commoncrawl/arquivo) stay usable while
an origin is cooling — that's the pressure valve, by design.

## 6. Regenerating profiles

```bash
python3 -m src.crawler.site_profiler            # all seeds, resumable
python3 -m src.crawler.site_profiler --hosts chemi,par --force
python3 -m src.crawler.site_profiler --selftest
```
One polite probe per (host × method); results merge into
`data/site_profiles.json`; the selector picks them up on next worker start.
Re-run weekly from beat — chains drift as relays/hosts change.

## 7. Measured run — 2026-09-21 (profiles shipped in this release)

All 251 seeds × every method, one pass from a live sandbox: **0 errors, 251
personal chains produced.**

| fact | value | what it changes |
|---|---|---|
| chain heads split | translate_goog 86 · jina 57 · wayback 55 · direct 39 · entry 14 | a single "best relay" is a myth — per-site plans are the whole point |
| families found | woocommerce 87 · static_listing 35 · aspnet 2 · unknown 12 · no-body-yet 115 | §1 recipes by family; for the 115, wayback domain-sweep IS the enumeration |
| wayback snapshot exists | **211/251 (84 %)** | archive-first default for unreachable hosts |
| median latency | direct 7164 ms (≈ all timeouts from this egress) · translate_goog 881 ms · jina 550 ms | live-origin attempts are the slowest step for most hosts — profiles front-load relays |
| jina returned STALE copies | **58 hosts (23 %)** got a `cached@date` snapshot | freshness tags are load-bearing coverage policy (v2.34 rule, now quantified) |
| pagination seen | load_more 18 · rel_next 7 · true infinite_scroll 9 (after regex tightening: image-`lazyload` false positives eliminated) | default enumeration = page/sitemap parameters, not scroll hacks |
| working entry-points | 14 hosts expose live REST/sitemap rows via declared entry_points | structured pull first wherever `entry:*` tops the chain |

Note `acidshop.ir`: its seed fingerprint (Aug) said translate_goog-primary; today's
measurement ranks `jina → wayback` (translate path degraded on it this run). This
drift is exactly why profiles **override** seed `free_access_methods` at plan time
while keeping them as the fallback universe. Weekly `site_profiler` from beat.
