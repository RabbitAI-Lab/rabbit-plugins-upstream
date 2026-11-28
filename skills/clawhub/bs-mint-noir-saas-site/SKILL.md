---
name: bs-mint-noir-saas-site
description: Build a dark product marketing website for an AI or SaaS tool, with near-black graphite surfaces, a single mint accent and italic serif highlight words inside bold headlines. You get five connected pages — Product, Pricing, Resources, Events and Changelog — each with working toggles, filters, search, countdowns and forms. Ideal for software teams launching an app who want a calm, premium site that looks like the product itself.
---

# Mint Noir SaaS Site

A five-page marketing site for a software product, drawn in one restrained
palette: a near-black graphite ground, soft off-white ink at stepped
opacities, hairline borders and exactly one accent — mint `#6ee7c8`. Every
headline is a tight, bold grotesk set in a white-to-sage gradient, with one
word swapped for a large italic serif in mint ("One AI team that *sells*.").
Labels and numbers run in a monospace. Depth comes from faint mint glows
behind heroes and featured cards, never from colour blocks.

The pages:

1. **Product** — announcement pill, two-line gradient headline, two pill
   CTAs, avatar trust row, then a large fake app window (sidebar, KPI
   tiles, revenue sparkline, key-finding note) fading into the page; an
   integrations strip; a three-card feature row; a bento grid (agent ID
   card, integrations tiles, model chips, approval card, schedule); a
   serif testimonial with proof stats; a glowing closing CTA card.
2. **Pricing** — monthly/yearly toggle, three plans with the middle one
   lifted by a mint glow, a compare table and a billing FAQ accordion.
3. **Resources** — help-centre hero with a glowing search field, six
   category cards, popular articles, levelled tutorials and a support card.
4. **Events** — featured live workshop with a running countdown and agenda,
   filterable upcoming sessions, replay cards and a newsletter form.
5. **Changelog** — release timeline with a glowing active node, release
   cards with tags, nested preview panels and check lists, and "load
   older releases".

`references/template.html` is the complete single-file template (hash
router, one `<section class="page" data-page>` per page, icon sprite,
reveal-on-scroll and every interaction). `examples/demo.html` in the
catalog is the same site filled for a fictional product.

## Workflow

### 1. Gather the product story

Ask for, or draft in a calm, specific product voice:

- Product name (one or two words) and a one-line category, e.g. "The AI
  business team for global commerce".
- The hero line, split so one word can become the serif accent, plus a
  two-line sub-headline and two CTA labels (primary + secondary).
- What the app window shows: four KPIs with deltas, a chart label, one
  "key finding" sentence, and four to six sidebar items.
- Integrations the product genuinely supports (only real ones).
- Three features, five bento claims, one testimonial with a fictional
  customer, four proof numbers.
- Three plans with monthly and yearly prices, includes lists, a compare
  matrix and four billing questions.
- Help categories and articles, upcoming events, release notes.

If the user has nothing, write it for them: short sentences, one concrete
number per claim, no superlatives. Every person, company and quote in a
demo is fictional; emails use `@company.example`.

### 2. Choose the target stack

Use the framework the user asks for. If they are working inside an existing
repository, detect the stack from its signals (`package.json` dependencies,
framework config, existing component folders) and build there in that
stack's idiom. With no repository and no preference, default to **Next.js
App Router with TypeScript**; ask one short question only when the signals
conflict. A standalone single HTML file is the right output only when the
user explicitly wants one file they can open directly.

Read [references/framework-adaptation.md](references/framework-adaptation.md).
The template is the visual source of truth: turn its pages into real routes,
its repeated blocks into components and its lists into typed data. Keep the
palette, type ratios, spacing, glows and interaction states identical in any
stack. Never wrap the template in an iframe or inject it as raw HTML.

### 3. Read the style guide

Read [references/style-guide.md](references/style-guide.md). Non-negotiables:

- One accent only. Mint is for the serif word, eyebrows, status dots,
  checks, active states and glows. No second brand colour, and never
  purple or violet anywhere. Amber, sky and red appear only as tiny status
  tags and negative deltas.
- Ink is one off-white (`#edf1f0`) used at fixed opacities (85 / 72 / 58 /
  50 / 40 %), not a range of greys.
- Surfaces are separated by 1px white hairlines at 6–14 % and `3–4 %`
  white fills. No drop-shadow cards except the hero app window.
- Headlines: Geist 600, negative tracking (-4 % display, -3 % section),
  gradient `#fff -> #a3b2b0`; the accent word is Instrument Serif italic at
  about 1.16× the headline size.
- Buttons are 999px pills: primary white with near-black text, ghost with a
  4 % fill and 14 % hairline.

### 4. Plan the pages

Read [references/page-library.md](references/page-library.md) for every
section, its slots and its interaction. Keep the five pages in the nav in
this order: Product, Pricing, Resources, Events, Changelog. Drop a page only
when the user asks; if you drop one, remove it from the nav, the footer and
every in-page link.

### 5. Set the icons

Read [references/icon-library.md](references/icon-library.md). All icons are
inline SVG from one sprite: Lucide strokes at 2px for UI (arrows on CTAs and
"N articles" links, checks in plan lists and release notes, plus/minus on
FAQ, search, play, RSS, download on the primary CTA, category tiles) and
monochrome brand marks only for the product's real integrations, always
next to a text label. No emoji, no Unicode arrows or ticks, no icon fonts.

### 6. Set the imagery

The style is mostly drawn in code — the app window, charts, glows and
video thumbnails are HTML/CSS/SVG. Photographs are only people: small round
avatars (28–40px) and one 3:4 portrait inside the bento "agent" ID card.

- Use the user's own photos when they have them; otherwise generate a
  consistent set with the host image tool: head-and-shoulders, plain dark
  graphite backdrop, soft warm key light, muted wardrobe (charcoal, sand,
  deep green). The agent card portrait uses a light grey studio backdrop
  so it reads as a printed ID card.
- Deliver as local WebP files sized at 2× their largest display size
  (avatars 96–192px, portrait about 540×720). In a single-file output embed
  them as WebP data URIs; never hotlink.
- Different people get different photos on the same page.

### 7. Copy the template and fill the slots

Copy `references/template.html` (or port it) and replace every fictional
value: the brand name and logo mark, all copy, people, numbers, prices,
events and releases. Portrait slots are `<img data-face>` / `<img data-img>`
placeholders without a source; point them at real image files. Keep the structure:
`.wrap` content width 1200px, 120px section rhythm, 69px sticky nav with a
blurred backdrop, the giant 6 % wordmark under the footer.

### 8. Keep the interactions real

Every visible control must do something: billing toggle recalculates
prices, filters filter, search searches, the countdown ticks, accordions
open, register/approve buttons change state, forms validate. Without a real
backend, give honest local feedback (a toast) instead of pretending to send.
Respect `prefers-reduced-motion`.

### 9. Check the result

Run `node scripts/validate-site.mjs <path-to-html>` on a single-file output
(it fails on emoji/dingbat icons, purple colours, external requests, missing
pages and unfilled slots). For a framework build, run the project's own
build and lint, then open every page at 1440px and 390px: no horizontal
scroll, grids stack, the app window scales down, the compare table scrolls
inside its own container.

## Output

Report the pages built, where the files are, which images were generated or
supplied, and any interaction that is simulated locally rather than
connected to a real service.
