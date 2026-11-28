---
name: bs-lime-frame-designer-portfolio
description: "Build a multi-page digital-designer portfolio site framed by a lime-green border around a white sheet: a three-column hero with a centred portrait card, social icon column and availability dot, a client wordmark marquee, a collaboration split with mockup shots and a dark count-up stats band. Ships Home, About, Services with four service pages, Work with six case-study pages, Testimonials, FAQ and a brief form, every page fully designed and linked. Ideal for freelance designers and small studios who want a bright, confident presence that sells the person as much as the work."
---

# Lime-Frame Designer Portfolio

A personal portfolio site that reads like a white sheet of paper laid on a
lime-green desk. The whole viewport is a bright lime frame; inside it sits
one rounded white sheet that holds everything. The hero is three columns:
the designer's name in heavy uppercase grotesk on the left, a rounded
portrait card in the middle with a vertical column of circular social
buttons and a pulsing "available" line, and a right column with an award
line, the two-word role in black and grey, an avatar stack with a badge and
one large proof number. Below it a grey wordmark marquee, a collaboration
split with two rounded mockup shots, and a near-black stats band with
count-up numbers. Everything else (service cards, work grid, testimonial
cards, plus accordion, lime CTA band, dark footer) uses the same rounded
corners, the same one accent and the same restrained grey type.

Output starts from `references/template.html`, a single self-contained
HTML file with a hash router, one `<section data-page>` per page, an
inline SVG icon sprite, reveal-on-scroll, a mobile menu, work filters, a
plus accordion, count-up numbers and a demo form. The example in
`examples/demo.html` shows the finished result for a fictional designer.

## Workflow

### 1. Gather the content story

Ask for, or draft in the style's warm first-person voice:

- The designer's or studio's name, a two-word role (for example "Digital
  Designer"), a one-sentence intro, an award or recognition line, one proof
  number (clients, projects or followers) and an availability status.
- Eight fictional or real client wordmarks for the marquee (text only).
- A bio of three paragraphs, three principles, a dated career path of
  three to five rows and a list of skills for text chips.
- Four services, each with a starting price, timeline, an includes list of
  five or six items, a three-step process and two related projects.
- Six projects, each with a client, year, services, role, a brief, an
  approach, an outcome, three result numbers and four deliverables.
- Six client quotes with names and roles, six to eight FAQ pairs, and
  contact details, all fictional in demos: `name@brand.example`,
  `+1 (555) 010-…`, an invented street and city.

If the user has nothing yet, write it for them in this register: friendly,
direct, concrete (weeks, prices, counts), no superlatives.

### 2. Choose the target stack

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

### 3. Read the style guide

Read [references/style-guide.md](references/style-guide.md). Non-negotiables:

- The lime frame is always visible: the body is lime, the sheet is white
  with large rounded corners, and nothing sits outside the sheet.
- One accent. Lime appears on the frame, primary buttons, icon discs, the
  CTA band and small chips; never on body text or large headings.
- Type is one grotesk. The hero name is uppercase 800 weight with tight
  leading; the role and every second-half heading fragment turn grey.
- Every button is a pill with a circular icon disc at its end; the disc
  rotates on hover.
- Dark surfaces (stats band, footer) are near-black, never pure black, and
  always rounded.
- No emoji, no icon fonts, no default-blue links, no placeholder boxes.

### 4. Plan the pages and sections

Read [references/page-library.md](references/page-library.md). Home,
About, Services, Work, Testimonials, FAQ, Contact and Not found always
ship; four service pages and six case pages ship with them. Keep the
canonical home order: hero, wordmark row, services, collaboration split,
stats band, selected work, testimonials, FAQ preview, CTA. To add a
project, copy one `data-page="work/…"` section, give it a new slug, add a
card to the work grid and to the home grid if it is featured, and update
the "next project" links so the chain still loops.

### 5. Fill the template

Copy `references/template.html`, then work through every
`<!-- REPLACE: … -->` comment in order: title, wordmark, hero, award and
proof, marquee names, service cards, collaboration copy, stats, work cards,
testimonials, FAQ, contact and footer. Delete pages you do not need and
their links. Keep the router, reveal, menu, accordion, filter, counter and
form scripts intact; they are generic.

### 6. Imagery

Eight image slots: the portrait (portrait format, light seamless
backdrop, plain clothing), the studio thumbnail in the stats band
(landscape), and six square project covers, two of which double as the
collaboration mockups. Generate artwork with your image generation tool
using prompts in the style's photographic world: soft daylight, pale
backgrounds, lime and black props, no text, no logos, no watermark. Embed
each as a WebP data URI (2x the displayed width, long edge at most 2560,
quality 95, lossless only for UI screenshots) and keep the whole file
under 20 MB. Images are referenced once through the `.ph-*` classes, so
each embeds a single time. Never hot-link, never use photographs of real
people, products or logos.

### 7. Set the icons

All icons live in the sprite at the top of `<body>` and are used through
`<use href="#i-…">`. See [references/icon-library.md](references/icon-library.md)
for the id table. Lucide-grammar strokes for UI: arrows for buttons and
links, plus for the accordion, check for lists, phone, mail, map-pin and
clock for contact, globe, at-sign, message-circle and rss as generic
social marks, star for ratings, pen-tool, layout, smartphone and rocket
for the four services, and circle, square, triangle and hexagon as
wordmark glyphs. Use LobeHub monochrome marks only for real AI-integration
contexts with a visible label. Never emoji, dingbats or icon fonts.

### 8. Validate

Run `node scripts/validate-lime.mjs examples/demo.html` (strict) and
`node scripts/validate-lime.mjs references/template.html --allow-replace`.
The script fails on remote resources, storage or network APIs, emoji,
leftover placeholders, broken `#/` routes, unreachable pages, and missing
style structure: the frame and sheet, the hero with portrait card, the
social column, the availability line, the marquee, the collaboration
split, the stats band with counters, the accordion and the footer columns.

### 9. Walk every route in a browser

Open the file and visit Home, About, Services and each service page, Work
and each case page, Testimonials, FAQ, Contact and an unknown hash. Check:
the portrait fills its card, the social column does not cover the face,
the hero balances at 1920, 1280 and 390 px, the marquee fades at both
edges, counters finish on their real numbers, the accordion opens one item
at a time, the filters leave the right cards, the brief form shows its
confirmation without navigating, the mobile menu opens and closes on route
change, and nothing scrolls horizontally. Fix before delivering.

## Catalog demo constraints

These file/sandbox/hash constraints apply to the catalog demo. Generated
websites follow the selected framework as described in step 2.

- Self-contained: one HTML file, no external scripts, styles, fonts or
  images; works from `file://` and inside `<iframe sandbox="allow-scripts">`.
- Sandbox-safe: no storage, cookies, `fetch`, `window.open` or top-level
  navigation targets; forms never submit.
- English by default; other languages only when the user asks.
- Fictional entities in demos: invented names, `.example` domains,
  `+1 (555) 010-…` phones, no real client or tool logos.
- Palette discipline: tokens in `:root` only; lime is the single accent.
- Hash routes only; every link resolves to a designed page or the
  not-found page.

## Files

- `references/template.html`: the engine with REPLACE slots and placeholder art.
- `references/style-guide.md`: tokens, type, signature moves, voice, do and don't.
- `references/page-library.md`: every page and section, canonical order, how to extend.
- `references/icon-library.md`: sprite ids and icon rules.
- `references/third-party-notices.md`: Lucide notice; system fonts; everything else original.
- `scripts/validate-lime.mjs`: the validator described in step 8.
- `examples/demo.html` and `examples/preview-*.webp`: the finished example.

- `references/framework-adaptation.md` - stack selection, component mapping, image coverage and fidelity checks

## Updated visual and route inventory

Read references/visual-contract.md and references/route-inventory.md for
the current image coverage, tokens and connected pages. These supplement
the original page library. Use dedicated imagery for unrelated entities.


## Refinement v2

Keep the lime outer frame, white rounded canvas, central portrait and restrained dark/lime controls. Favor short headings and one-sentence service descriptions. Show unique client wordmarks in a compact static grid; never repeat the full list under reduced motion. The nine active assets share natural studio lighting, neutral materials and a restrained lime/sage family. Portfolio media keeps its square composition with contain; portrait uses a 4:5 crop aligned to the top so the head remains visible. Do not insert unrelated website photography into the gardening-app case. Labels for fictional clients remain fictional; platform icons must only identify a platform actually present. Fields are 48px and textarea 128px, with a 660px maximum form width. Confirmation is hidden until submission.


## Interior page depth

Read references/interior-pages.md. Preserve the complete page-specific content, image roles, selection states and contextual actions in the working template. Do not reduce inner pages to a heading and a few summary sentences.

---

## More from Skillry

This skill is a free open-source website template from [Skillry](https://skillry.dev).

- Explore the full catalog of creative design, presentation, video, and web skills at [skillry.dev](https://skillry.dev).
- Connect Skillry MCP or browse all 87 free skills: `npx --yes skillry-cli@latest mcp` · [github.com/yihui-dev/skillry-skills](https://github.com/yihui-dev/skillry-skills)
