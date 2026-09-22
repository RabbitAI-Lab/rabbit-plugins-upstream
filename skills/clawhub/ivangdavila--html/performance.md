# Loading Performance Owned by Markup

Everything here happens before a line of application JS runs, and none of it is fixable in CSS or in a bundler config. The measurements belong to the page; the decisions belong to the head and to a handful of attributes.

**Contents:** [The Critical Path](#the-critical-path) · [Scripts](#scripts) · [Stylesheets](#stylesheets) · [The Preload Scanner](#the-preload-scanner) · [Resource Hints](#resource-hints) · [Fonts](#fonts) · [LCP](#lcp) · [CLS](#cls) · [INP at the Markup Layer](#inp-at-the-markup-layer) · [Deferring Below-Fold Work](#deferring-below-fold-work) · [Speculative Loading](#speculative-loading) · [Budget Table](#budget-table)

## The Critical Path

The browser cannot paint until it has the HTML, every render-blocking stylesheet, and every parser-blocking script above the content. Three questions, in order:

1. What blocks rendering? (stylesheets without a `media` filter; `<script src>` with no `defer`/`async`; inline `<script>` after a stylesheet, which waits for that stylesheet)
2. When is the LCP resource discovered? (its distance from the top of the HTML, and whether it is reachable by the preload scanner)
3. What shifts after paint? (unsized media, late fonts, injected banners)

## Scripts

| Form | Parsing | Execution | Order |
|---|---|---|---|
| `<script src>` | Blocks at that line | On arrival | Document order |
| `<script defer src>` | Never blocks | After parsing, before `DOMContentLoaded` | Document order preserved |
| `<script async src>` | Never blocks | As soon as it lands | **Non-deterministic** |
| `<script type="module">` | Never blocks | Deferred by default | Document order; `async` overrides |
| Inline `<script>` | Blocks | Immediately | Also waits for any preceding stylesheet |

- `defer` is the default choice. `async` only for scripts with no dependency on the DOM or on each other — a single analytics beacon qualifies; two interdependent libraries do not, and the failure appears only on slow networks.
- `type="module"` implies defer; adding `defer` is a no-op, adding `async` is a real change.
- `<script>` at the end of `<body>` is the pre-`defer` workaround: it still blocks the parser at that point, and it is discovered later. `defer` in the head is strictly better.
- An inline script placed after a stylesheet waits for the stylesheet to load before executing, and blocks the parser while it waits — the classic "why is my tiny inline script costing 400ms".
- `nomodule` for legacy fallbacks only under `browser_support: legacy`.

## Stylesheets

- A `<link rel="stylesheet">` blocks first paint. That is usually correct: unstyled content flashing is worse.
- `media="print"` and unmatched media queries load without blocking — the mechanism behind conditionally loading non-critical CSS.
- Inline the critical CSS only when it is small (a few kilobytes) and generated, never hand-maintained; otherwise the duplicate bytes cost more than the round trip saved.
- Number of stylesheets barely matters over HTTP/2; the amount of blocking CSS does.

## The Preload Scanner

While the main parser is blocked, a secondary scanner reads ahead in the raw HTML and starts fetching what it can see. Everything invisible to it is discovered late:

| Invisible to the scanner | Consequence |
|---|---|
| Images injected by JS | Discovered after the bundle parses and runs |
| CSS `background-image` | Discovered after CSSOM is built and the element matches |
| `srcset` chosen by a lying `sizes` | The wrong file is fetched early, which is worse than late |
| Fonts referenced only from CSS `@font-face` | Discovered after the stylesheet parses — the reason font preload exists |
| Anything behind a lazy-loaded parent | Intentional; wrong if it is the LCP element |

The scanner is why "just move it into JS" makes pages slower and why a plain `<img>` in the HTML beats every clever alternative for the hero image.

## Resource Hints

| Hint | Use | Budget |
|---|---|---|
| `<link rel="preconnect" href="https://cdn.example.com" crossorigin>` | Opens DNS + TCP + TLS early to an origin you *will* use | 2–4 origins; each one costs a connection whether or not it is used |
| `<link rel="dns-prefetch">` | Cheaper, DNS only; a fallback for origins used later | Several are harmless |
| `<link rel="preload" as="…">` | Fetch a late-discovered critical resource early | 1–3. Preloading everything reorders nothing and starves the real critical path |
| `<link rel="modulepreload">` | Module graph warm-up | Only for the entry module's direct dependencies |
| `<link rel="prefetch">` | Low-priority fetch for the *next* navigation | Wasted bytes if the guess is wrong |

Rules that decide correctness:

- `as` is mandatory on `preload`. Without it the resource is fetched twice, at the wrong priority.
- **Fonts require `crossorigin` on the preload even when same-origin** — font requests are CORS-mode, and a preload without it downloads a second copy.
- Preconnect to an origin you do not use within a few seconds is a wasted connection; the browser closes idle ones.
- A `preload` for a resource that is never used produces a console warning and pure waste — treat the warning as a bug.

## Fonts

- `font-display: swap` (CSS) plus a preload of the one or two files actually used above the fold. Subset the file; a full-language font is often 3–5× the size needed.
- Every self-hosted font preload: `<link rel="preload" as="font" type="font/woff2" href="/f.woff2" crossorigin>`.
- WOFF2 only; older formats are dead weight.
- Fallback metrics (`size-adjust`, `ascent-override`) reduce the layout shift when the web font swaps in — that shift is CLS, and it is the one most often missed because it happens after the images have settled.

## LCP

The largest contentful element in the first viewport — usually a hero image, a heading, or a background image. Markup-layer levers:

1. It must be a real `<img>` in the initial HTML, not a background and not JS-injected.
2. `loading="eager"` (never `lazy`) and `fetchpriority="high"`.
3. `preload` it only if it is discovered late (a `<picture>` behind a JS-driven wrapper, a CSS background); a plain `<img>` near the top does not need one.
4. Nothing render-blocking above it that is not essential.
5. If the LCP element is text, the font it uses is the critical resource.

Thresholds: LCP ≤ 2.5s is "good", 2.5–4.0s needs improvement. Measure at the 75th percentile of real users, not on a development machine.

## CLS

| Cause | Fix |
|---|---|
| Images and iframes without dimensions | `width`/`height` attributes (SKILL.md Rule 3) |
| Ads, embeds, and banners injected after paint | Reserve the box in the markup with a min-height matching the most common size |
| Late fonts with different metrics | Preload + `size-adjust` fallbacks |
| Content inserted above existing content | Insert below the fold, or reserve space |
| A cookie banner appended to the top of the body | Position it as an overlay, not in flow |

Thresholds: CLS ≤ 0.1 is "good", 0.1–0.25 needs improvement. A single 400px-tall unsized hero on a 800px viewport typically scores around 0.5 on its own.

## INP at the Markup Layer

Interaction responsiveness is mostly a JS concern, but markup contributes:

- Enormous DOMs are slow to style and lay out. Practical guidance: a few thousand elements is fine; tens of thousands is where interaction latency becomes structural. Paginate or virtualize.
- Deeply nested layout (dozens of levels) costs on every recalculation.
- Native elements handle their own interaction off the main thread's application code — a `<details>` toggle is free, a JS accordion is not.
- Hundreds of individually bound handlers on list rows: one delegated handler on the container instead.

## Deferring Below-Fold Work

- `loading="lazy"` on below-fold `<img>` and `<iframe>`. Never on anything in the first viewport.
- `content-visibility: auto` (CSS) with a `contain-intrinsic-size` estimate skips rendering work for off-screen sections; the intrinsic size estimate is what keeps the scrollbar honest.
- Facade pattern for heavy embeds: a poster image and a button that swaps in the real `<iframe>` on click (`media.md`).
- `decoding="async"` on long image lists.

## Speculative Loading

Speculation Rules prefetch or prerender a likely next page:

```html
<script type="speculationrules">
{"prerender":[{"where":{"href_matches":"/products/*"},"eagerness":"moderate"}]}
</script>
```

Chromium-only at present. Prerendering runs the target page for real — analytics fire, and anything with side effects runs early. Use `eagerness: "moderate"` (hover/pointerdown) rather than `eager`, and never prerender a URL that mutates state.

## Budget Table

Working numbers to state when recommending; verify against the project's own field data.

| Metric | Good | Needs improvement |
|---|---|---|
| LCP | ≤ 2.5 s | 2.5–4.0 s |
| CLS | ≤ 0.1 | 0.1–0.25 |
| INP | ≤ 200 ms | 200–500 ms |
| Render-blocking requests above the fold | ≤ 2 | — |
| `preconnect` origins | ≤ 4 | — |
| `preload` entries | ≤ 3 | — |
| HTML document, compressed | ≤ 100 KB | — |

**After measuring a page**, record the LCP element and any structural constraint against that template's row in `## Pages` of `~/Clawic/data/html/memory.md` — which element is the LCP, what blocks above it, which hints are deliberate (`memory-template.md`). Without it, the next session re-derives the critical path and re-adds a preload that was removed on purpose. **A performance decision with a rejected alternative** — a facade instead of the real embed, self-hosted fonts instead of a provider — goes to `artifacts/` with its numbers.
