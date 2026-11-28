---
name: bs-green-pharmacy-storefront
description: A multi-page online pharmacy storefront with a lime-green hero, upload-prescription card, pastel category tiles, deal grids, tabbed trending products, brand row, promo tiles, FAQ accordion and a dark-green footer, plus catalog, product detail, cart, checkout, consultation, prescriptions, brands, FAQ, about and contact pages. Every page is fully designed with fictional products, brands and pharmacists, and the cart, filters and forms work in the browser. Ideal for pharmacies, wellness shops and health-delivery services that want a bright, trustworthy store ready to fill with their own range.
---

# Green Pharmacy Storefront

Build a bright, trustworthy online pharmacy or health shop in the green
pharmacy style: a 32px-radius lime hero frame holding a giant navy display
word, uppercase support copy, a pharmacist portrait rising from the bottom
edge and a white upload-prescription card; six square pastel category tiles;
calm grey product cards with white photo wells and yellow deal pills; a
yellow-and-peach service duo; monogram brand discs; a tabbed trending grid;
pastel promo tiles with masked figures; an aqua feature banner with flavour
bars; grey FAQ pills that turn lime when open; and a forest-green footer that
ends in a lime band with a giant wordmark. Every output starts from
`references/template.html`, which already contains the router, cart, filter,
tab, accordion and form engine plus a REPLACE slot for every piece of content.

## Workflow

1. **Gather the content story.** Ask for the shop name and city, the delivery
   promise, the services offered (consultation, prescriptions, membership), a
   product list with categories, prices, discounts and short descriptions,
   the brands to feature, a few customer quotes and contact details. If the
   buyer has nothing yet, draft a fictional range in the style's plain, warm
   voice: specific product names, two-decimal prices, three benefits and a
   usage line per product, and honest safety notes. Never use real
   pharmaceutical brands, real product names or real people.

2. **Choose the target stack.**

   Use the framework or starter explicitly requested by the user: Vue, React,
   Astro, Next.js, a TypeScript starter, or another named stack. When the user
   does not specify a stack, default to **Next.js App Router with TypeScript**.
   Do not ask the user to choose a stack merely because no preference was given.
   Inspect the target repository before writing; preserve unrelated files and
   put the requested output in a suitable isolated directory if the existing
   application uses a different stack. Never silently migrate that application.

   Read [references/framework-adaptation.md](references/framework-adaptation.md).
   Use this Skill's template and style guide as the visual source of truth.
   Translate sections into real components, data collections and framework
   routes. Preserve the palette, typography ratios, spacing, image treatment,
   section order and interaction states. Do not wrap the HTML in an iframe or
   inject the entire document as raw HTML to pretend it is a framework port.
   The single-file hash router belongs only to the catalog demo; actual websites
   use the selected framework's routing and state conventions.
3. **Read the style guide** at [references/style-guide.md](references/style-guide.md).
   Non-negotiables:
   - Lime is a surface and navy is the voice: headings on lime are navy, and
     lime never carries text under 12px.
   - One pastel per tile, never two adjacent tiles in the same pastel, never
     a new accent hue.
   - Product cards are grey with a white photo well; deals wear a yellow pill
     with a struck-through old price.
   - A single grotesk system stack; the hero word is 800 weight at
     `clamp(64px, 10.5vw, 184px)` with `-.05em` tracking.
   - Fictional brands are two-letter monogram discs, never logos.
   - Every icon is an inline SVG from the sprite; no emoji, dingbats or icon fonts.

4. **Plan the pages** with [references/page-library.md](references/page-library.md).
   Home, catalog, one detail page per product, cart, checkout, consultation,
   prescriptions, brands, FAQ, about, contact, account, app, privacy, terms
   and not-found always ship. Keep the canonical home order (hero, category
   tiles, deals, service duo, brands, trending tabs, promo tiles, baby row,
   feature banner, testimonials, perk duo, FAQ, app duo, footer) and drop
   whole sections rather than thinning them. To add a product, add its card
   to the catalog grid, its `data-page="product/<id>"` section following the
   detail anatomy, and its entry in the script's `PRODUCTS` list so the cart
   can price it. Every link must land on a real page; no `href="#"`.

5. **Copy the template and fill every REPLACE slot.** Brand name and mark,
   hero word and copy, category tiles, each product card and detail page,
   service cards, brand discs, promo tiles, feature banner, testimonials,
   perks, FAQ items, pharmacist roster, stats, contact channels and footer
   blurb. Delete pages and products the buyer does not need. Keep the router,
   reveal observer, cart, catalog, tabs, accordion and form handlers intact;
   they are generic and read everything from data attributes.

6. **Imagery.** The style needs a pharmacist portrait on flat lime, a
   pointing pharmacist on peach, a courier on yellow, six category photos of
   people or hands on flat pastels, three promo figures on peach, aqua and
   yellow, white-background product photos, and one hero product on aqua.
   Generate artwork with your image generation tool using prompts that name
   the flat background colour, the framing (waist-up, centred, or right half
   of the frame) and "no text, no logos, no watermark". Look at each result
   before using it. Convert to WebP (q95, lossless for anything with UI or
   small text), size at 2x the displayed width with the long edge at or
   below 2560px, keep the total under 20 MB, and embed as data URIs. Never
   hot-link, and never use real photos of real people, real products or
   real logos.

7. **Set the icons** from [references/icon-library.md](references/icon-library.md):
   `i-cross` for the brand mark and footer band, `i-arrow-right` on every
   CTA, `i-plus`/`i-minus` on add-to-cart pills and steppers, `i-check` on
   benefits and confirmations, `i-star` for ratings, `i-truck`/`i-clock`/
   `i-rotate-ccw` for delivery facts, `i-file-text`/`i-upload` on the
   prescription cards, `i-stethoscope` on the services pill,
   `i-chevron-down` on FAQ toggles, `i-shopping-bag` on the cart. Lucide
   grammar for UI; LobeHub monochrome marks only in real AI-integration
   contexts with visible labels; never emoji, dingbats or icon fonts.

8. **Validate** with `node scripts/validate-pharmacy.mjs <file>` (add
   `--allow-replace` for the unfilled template). It rejects remote
   resources, external scripts, storage and network APIs, top-level
   navigation, emoji and dingbat icons, leftover REPLACE or image tokens,
   placeholder filler copy, dead hash links and unreachable pages, and it requires the
   style's structure: hero frame with display word, upload card, six
   category tiles, product card grammar, catalog filters and sort, at least
   six product detail pages, cart lines with summary, FAQ accordion and the
   footer band.

9. **Open it in a browser and walk every route.** Check the hero at 1920,
   1280 and 390px (word fully visible, portrait bottom-aligned, card and
   button aligned right), the mobile menu, category tiles, tab filtering,
   add-to-cart count and toast, cart quantity and removal, promo code,
   checkout confirmation, catalog filters, sort and empty state, the FAQ
   accordion, every form's confirmation, the not-found page, and that no
   page scrolls horizontally. Fix overlapping text, cropped portraits, low
   contrast on pastel tiles and unbalanced grids before delivering.

## Catalog demo constraints

These file/sandbox/hash constraints apply to the catalog demo. Generated
websites follow the selected framework as described in step 2.

- Self-contained single file for standalone delivery: no external scripts,
  styles, fonts or images; no fetch, storage, cookies, `window.open` or
  `target="_top"`; must run from `file://` and inside a sandboxed iframe.
- English by default; translate only when asked.
- Fictional entities only: shop, brands, products, pharmacists, customers,
  addresses, phone numbers in the `+1 (555) 010-…` range and `.example`
  domains.
- Palette discipline: the locked tokens and pastel set only; no new hues.
- Cart, forms and uploads are demonstrations inside the page; never claim
  they process real orders or data.
- No top-level navigation; every link is a hash route inside the page.

## Files

- `references/template.html` – the engine with REPLACE slots and placeholder art.
- `references/style-guide.md` – tokens, type, signature moves, motion, voice, do/don't.
- `references/page-library.md` – every page and section, canonical order, how to add products.
- `references/icon-library.md` – sprite ids, placements and icon rules.
- `references/third-party-notices.md` – Lucide ISC note, system fonts, original everything else.
- `scripts/validate-pharmacy.mjs` – the validator described in step 8.

- `references/framework-adaptation.md` - stack selection, component mapping, image coverage and fidelity checks

## Updated visual and route inventory

Read references/visual-contract.md and references/route-inventory.md for
the current image coverage, tokens and connected pages. These supplement
the original page library. Use dedicated imagery for unrelated entities.


## Current refinement standard

Preserve the lime hero, oversized two-word heading, delivery portrait, pastel category photos and forest-green footer. Reduce the homepage recommended grid to four visible products per selected category. Keep the full catalog and every product reachable.

Use short product names above the price; put strengths and pack details in the details table. Keep descriptions concise. Do not invent efficacy, dosage or verification claims for new products; use supplied product information. General navigation and purchase controls use the same line-icon family. Original Apple and Android marks identify platform buttons only; license and original SVGs are included under brand-icons/.

32 active images follow two roles: colorful studio portraits for categories and services, soft white-background pack shots for products. Show complete products with contain sizing inside square media frames. Keep the pharmacy interior on the about page; do not add unrelated staged skincare products to a specific product case.

Forms have 48px fields, 128px textareas and 16px radio controls, with a maximum 720px form card. Pair fields on desktop and stack on mobile. Checkout totals align labels left and amounts right. The mobile cart uses a compact thumbnail, clear quantity control and a separate remove action.

Cart thumbnails must read the live hydrated product image when rendering the cart. Do not cache an absent src before the image hydration script has run. Validate a populated cart, quantity changes, totals and mobile rendering. Respect the selected framework and default to Next.js App Router + TypeScript.



















<!-- reui:stack -->
#### Interface components come from ReUI

Every generic control in this template — buttons, text fields, selects,
radio groups, tabs, accordions, filter chips, the mobile menu panel — is a
[ReUI](https://reui.io) component, not a hand-written control. Keep it that
way in the generated project.

- Install from the official registry and use the real component source.
  ReUI is a React component system built on Radix primitives; in a
  Next.js/React project add components with the shadcn CLI
  (`npx shadcn@latest add @reui/button`, and so on) and import them from
  your `components/ui` directory. The MIT-licensed source also lives at
  https://github.com/keenthemes/reui.
- Do not substitute a native `<select>`, a hand-rolled popover, or a `div`
  with matching class names. If a control needs behaviour ReUI does not
  provide, build it explicitly and say so.
- Style through tokens, not forks. Point ReUI's custom properties
  (`--primary`, `--background`, `--border`, `--radius`, …) at this
  template's palette and keep its own control classes on the rendered
  elements. `references/reui-components.md` lists the mapping used here.
- In a non-React stack, check ReUI's real support before promising it.
  Astro can mount React islands; a Vue or Svelte project cannot use ReUI
  components directly — raise the conflict rather than switching stacks or
  silently swapping in another library.
<!-- /reui:stack -->

### Shopping bag entrance
Use a compact 44px icon-only shopping bag or cart button in the header. Do not render “Bag (0)”, “Cart (0)”, parentheses, or a text label. Hide the quantity badge for an empty cart; show and update it only for positive quantities. Preserve an accessible label and keyboard focus.


## Interior page depth

Read references/interior-pages.md. Preserve the complete page-specific content, image roles, selection states and contextual actions in the working template. Do not reduce inner pages to a heading and a few summary sentences.

---

## More from Skillry

This skill is a free open-source website template from [Skillry](https://skillry.dev).

- Explore the full catalog of creative design, presentation, video, and web skills at [skillry.dev](https://skillry.dev).
- Connect Skillry MCP or browse all 87 free skills: `npx --yes skillry-cli@latest mcp` · [github.com/yihui-dev/skillry-skills](https://github.com/yihui-dev/skillry-skills)
