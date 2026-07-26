# The Document Head — Metadata, Previews, Icons

Everything a machine reads before a human sees anything: the parser, the crawler, the link unfurler, the installer. Order matters here more than anywhere else in the document.

**Contents:** [Canonical Order](#canonical-order) · [The Three That Change Parsing](#the-three-that-change-parsing) · [Title and Description](#title-and-description) · [Canonical URLs](#canonical-urls) · [Open Graph and Cards](#open-graph-and-cards) · [Favicons and the Install Surface](#favicons-and-the-install-surface) · [Structured Data](#structured-data) · [Meta That Does Something](#meta-that-does-something) · [Meta That Does Nothing](#meta-that-does-nothing) · [The Boilerplate](#the-boilerplate)

**Before writing a canonical URL, an `hreflang` set, or an absolute `og:`/`twitter:` URL**, read `~/Clawic/data/domains/domains.md` for the canonical host already agreed for that site. Two pages that disagree on `www` are two pages as far as every crawler and unfurler is concerned.

## Canonical Order

The parser acts on the head top to bottom, and the preload scanner starts fetching before your first stylesheet is applied. Emit in this order:

1. `<meta charset="utf-8">` — first, always
2. `<meta name="viewport" content="width=device-width, initial-scale=1">`
3. `<title>`
4. `<meta name="color-scheme" content="light dark">` — it decides the UA background and control painting, so it belongs above anything that fetches
5. `<link rel="preconnect">` for origins the LCP resource lives on (`performance.md`)
6. `<link rel="preload">` for the fonts and the LCP image, if any
7. Stylesheets
8. `<script defer>` / `<script type="module">`
9. Everything descriptive: description, canonical, `og:`, icons, manifest, `theme-color`, JSON-LD

Rule of thumb: anything that changes *how the rest of the document is parsed or laid out* goes above anything that merely describes the page.

## The Three That Change Parsing

| Tag | Rule | Failure when wrong |
|---|---|---|
| `<meta charset="utf-8">` | Must appear within the **first 1024 bytes** of the document | The parser guesses, then restarts on discovering the real encoding; accented text renders as `Ã©`, `â€™` (`internationalization.md`) |
| `<meta name="viewport">` | `width=device-width, initial-scale=1` | Mobile browsers assume a ~980px viewport and shrink the page; every media query is evaluated against the wrong width |
| `<!DOCTYPE html>` | Literal first bytes of the file — before it, not even a comment or a BOM-visible blank line | Quirks mode (`parsing.md`) |

Never add `maximum-scale=1` or `user-scalable=no` to the viewport: it blocks pinch zoom, which is a WCAG 1.4.4 failure and the accommodation low-vision users reach for most.

## Title and Description

- `<title>` is the tab, the bookmark, the search result, the shared-link fallback, and the first thing a screen reader announces on page load. Front-load the unique part: `Invoice 4821 — Billing — Acme`, not `Acme | Billing | Invoice 4821`.
- Practical ceiling ~60 characters before search results truncate; there is no hard limit and the full string still matters for tabs and bookmarks.
- `<meta name="description">` does not affect ranking; it is the snippet, and search engines rewrite it when it does not match the query. ~155 characters is where truncation typically starts. Ranking strategy is `seo`.
- One `<title>` per document. A second one is ignored, which is how a template that emits both a default and a page title ships the wrong one.

## Canonical URLs

```html
<link rel="canonical" href="https://example.com/pricing">
```

- **Self-referencing on every page**, absolute, with the scheme and the agreed host. A relative canonical works but re-introduces the ambiguity it exists to remove.
- Canonical is a hint, not a directive — it loses to conflicting signals (a `noindex`, a redirect, an inconsistent sitemap). Make the canonical, the internal links, the sitemap and the redirects agree on one host and one trailing-slash style.
- Parameterized URLs (`?utm_source=`, `?sort=`) canonicalize to the clean URL. Paginated lists canonicalize to *themselves*, not to page 1 — pointing page 2 at page 1 drops page 2's contents from the index.
- Never emit a canonical from JS: unfurlers and many crawlers never run it.

## Open Graph and Cards

```html
<meta property="og:type" content="website">
<meta property="og:title" content="Pricing — Acme">
<meta property="og:description" content="…">
<meta property="og:url" content="https://example.com/pricing">
<meta property="og:image" content="https://example.com/og/pricing.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Three pricing tiers">
<meta name="twitter:card" content="summary_large_image">
```

- `og:*` uses `property`; `twitter:*` uses `name`. Swapping them is the most common reason a card is half-populated. X falls back to Open Graph for everything except `twitter:card`, so the Twitter block is two lines, not a duplicate set.
- **The image URL must be absolute and publicly fetchable.** A relative path, a staging host behind auth, or a bot-blocked CDN all produce a blank preview with no error anywhere.
- 1200×630 (1.91:1) is the safe size for the large card; supply `width`/`height` so the unfurler can lay out before it downloads. Under 300×157 many platforms downgrade to the small card.
- `twitter:card` values are a closed set: `summary`, `summary_large_image`, `app`, `player`. Anything else silently falls back to `summary`.
- Previews are cached hard per platform. After changing an image, expect the old one until the platform's cache expires or the URL changes — versioning the filename (`og/pricing-v2.png`) is the reliable fix.
- Messaging apps often fetch **only the first ~100 KB** of the HTML before giving up; metadata buried below a large inline script may never be seen.

## Favicons and the Install Surface

The minimum modern set, and what each one is actually for:

| File | Tag | Serves |
|---|---|---|
| `favicon.ico` (32×32 + 16×16) | none needed at the root path | Legacy browsers, bookmark bars, some crawlers |
| `icon.svg` | `<link rel="icon" href="/icon.svg" type="image/svg+xml">` | Every current browser, any DPI, and dark mode via a `prefers-color-scheme` media query *inside* the SVG |
| `apple-touch-icon.png` 180×180 | `<link rel="apple-touch-icon" href="/apple-touch-icon.png">` | iOS home screen — no transparency, no rounding (iOS masks it) |
| `manifest.webmanifest` | `<link rel="manifest" href="/site.webmanifest">` | Android install, name, theme color, 192 and 512 px icons |

- `<meta name="theme-color">` colors the browser UI on Android and in installed windows; give it a `media="(prefers-color-scheme: dark)"` twin or it fights dark mode.
- A maskable icon (`"purpose": "maskable"` in the manifest) needs its content inside the central 80% safe zone, or Android crops it.

## Structured Data

Emit in the format `structured_data` names — JSON-LD by default, because it is a single block that survives templating and does not entangle markup with vocabulary.

```html
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Product","name":"…","offers":{"@type":"Offer","price":"29.00","priceCurrency":"USD"}}
</script>
```

- Every claim in structured data must be visible on the page. Prices, ratings and availability that disagree with the rendered content are the standard trigger for a structured-data manual action.
- `@type` must be one schema.org type; a made-up type is ignored wholesale, and one syntax error kills the whole block, not the bad property.
- Microdata (`itemscope`/`itemprop`) is the alternative when the CMS cannot inject a script block. Never ship both for the same entity — duplicates get merged unpredictably.
- Which types earn rich results, and the eligibility rules, belong to `seo`. What belongs here is that the markup is valid, matches the page, and is emitted server-side.

## Meta That Does Something

| Tag | Effect |
|---|---|
| `<meta name="robots" content="noindex,nofollow">` | Page-level indexing control; `noindex` on a page that is also `Disallow`ed in robots.txt is never seen, because the crawler never fetches it |
| `<meta name="referrer" content="strict-origin-when-cross-origin">` | Document-wide referrer policy; the browser default already matches this in current versions |
| `<meta name="color-scheme" content="light dark">` | Opts the UA stylesheet — form controls, scrollbars, default background — into dark mode |
| `<meta http-equiv="Content-Security-Policy" …>` | A real CSP, with limits: `frame-ancestors`, `report-uri` and `sandbox` are **ignored** in meta form and only work as a header (`security.md`) |
| `<meta name="format-detection" content="telephone=no">` | Stops iOS auto-linking number strings that are not phone numbers |
| `<base href>` | Rebases every relative URL in the document, including ones you did not intend; almost always a mistake outside email and generated documents |

## Meta That Does Nothing

Delete on sight, and say why once: `<meta name="keywords">` (unused by every major engine since the 2000s), `<meta name="author">` and `<meta name="generator">` for ranking purposes, `<meta name="revisit-after">`, `<meta http-equiv="X-UA-Compatible">` (dead with IE), `<meta http-equiv="refresh">` for redirects — it is a WCAG 2.2.1 failure and search engines treat it as a weak 301; use a server redirect.

## The Boilerplate

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page — Site</title>
  <meta name="color-scheme" content="light dark">
  <link rel="stylesheet" href="/app.css">
  <script type="module" src="/app.js"></script>
  <meta name="description" content="…">
  <link rel="canonical" href="https://example.com/page">
  <!-- og: block -->
  <link rel="icon" href="/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#ffffff">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  …
</body>
</html>
```

The order is Canonical Order, line for line: parsing and painting first, then the render-blocking stylesheet and the module script, then the descriptive block. Templates that emit the descriptive block first delay the CSS request by however many tags precede it — keep the whole head well inside the ~100 KB an unfurler will read.

`lang` comes from `document_lang`. The skip link is the first focusable element in the body, not a decoration (`accessibility.md`).

**After agreeing a canonical host, a `www`-versus-apex choice, or a locale→hostname map**, write it to `~/Clawic/data/domains/domains.md` in the same turn — one row per hostname, updated in place (`memory-template.md`). **When a `<head>` block is settled for a site**, save it to `~/Clawic/data/html/artifacts/head-<site>.md` with the reason each line is there, and add its `## Boxes` line: rebuilding it from memory next quarter is how the canonical and the og image drift apart.
