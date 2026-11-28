---
name: bs-mono-designer-portfolio
description: "Build a monochrome graphic-design portfolio site on faint grid paper: a huge black display title beside a greyscale cut-out portrait, dark label chips, a two-by-four poster grid and generic tool tiles, with Home, About, Work, eight poster detail pages, Services and Contact. Every page is fully designed and linked, with work filters, a plus accordion and a demo brief form. Ideal for poster, print and illustration designers who want a quiet, print-like presence that lets the work carry all the colour."
---

# Mono Designer Portfolio

A portfolio site that behaves like a printed portfolio sheet. The ground is
a pale grey paper with a faint, slightly tilted grid; the type is one heavy
grotesk in near-black; section titles are white text on dark label chips;
the designer appears as a greyscale cut-out that fades into the page; and
the only colour anywhere comes from the posters themselves, hung in a
two-by-four grid with a soft paper shadow. Nothing competes with the work.

Output starts from `references/template.html`, a single self-contained
HTML file with a hash router, one `<section data-page>` per page, an
inline SVG icon sprite, reveal-on-scroll, a mobile menu, work filters, a
plus accordion and a demo form. The example in `examples/demo.html` shows
the finished result for a fictional poster designer.

## Workflow

### 1. Gather the content story

Ask for, or draft in the style's plain first-person voice:

- The designer's name, discipline line (for example "Graphic Design") and
  a city or studio name; three short facts for the hero chips (location,
  founding year, availability).
- A bio of three or four sentences with two or three bolded facts, plus a
  career path of three to five dated rows.
- Eight projects, each with a title, one category word (Event, Print,
  Illustration, Packaging, Music), a one-line summary, and a few sentences
  for Brief, Approach and Outcome, four deliverables and a palette.
- Four services with an includes list, a starting price and a turnaround;
  four process steps; four FAQ pairs.
- Contact details, all fictional in demos: `name@brand.example`,
  `+1 (555) 010-…`, an invented street.

If the user has nothing yet, write it for them in this register: short
declarative sentences, concrete nouns (paper stock, print runs, venues),
no marketing superlatives.

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

- Greyscale only in the interface: ink `#262626`, ground `#e9e9e9`, white,
  and their tints. Colour enters exclusively through poster artwork.
- The faint grid stays faint (white hairlines at roughly 70% opacity on
  the grey ground, tilted about nine degrees, fixed behind the page).
- One typeface, the humanist system stack, from 400 to 800; the hero title
  is the only element allowed above 90px.
- Section titles are white text on the dark `chip-label`, never plain
  headings.
- The portrait is greyscale, cut out on white, and fades to nothing at the
  bottom edge.
- Posters keep a 4:5 frame, a soft paper shadow, a mono index badge and a
  lift on hover; never rounded corners, never borders.

### 4. Plan the pages

Read [references/page-library.md](references/page-library.md). Home, About,
Work, eight poster detail pages, Services, Contact and Not found always
ship. Keep the canonical order of sections on Home (hero, about teaser plus
toolkit, poster grid, service rows, dark CTA band). To add a project, copy
one `data-page="work/…"` section, give it a unique slug, update both poster
grids (Home and Work), the footer "Recent work" list if wanted, and the
previous/next links of its neighbours.

### 5. Copy the template and fill every slot

Copy `references/template.html` to the output path. Every
`<!-- REPLACE: … -->` comment marks a content slot: wordmark, hero title
and name, hero chips, bio, tool tiles, each poster card, each detail
page, services, process, FAQ, contact details and footer. Fill all of
them, delete pages the user does not want (and every link to them), and
leave the router, reveal, stagger, filter, accordion and form scripts
intact. Remove every REPLACE comment before delivery.

### 6. Imagery

Images live in the hero portrait, the About photo frame, the eight poster
cards and the eight detail pages (the detail page reuses the card image at
full size). Generate artwork with your image generation tool: one portrait
of a fictional person on a clean white ground (it is converted to greyscale
by CSS) and eight portrait-format poster artworks, each in a different
medium (paper-cut, product photo, kawaii illustration, risograph, analogue
collage, chrome render, flat vector, screen print) with "no text, no
logos, no watermark". Embed them as WebP data URIs sized for 2x DPR (the
posters display at about 500px, so 1000px wide is enough; long edge never
above 2560; quality 95, lossless for anything with UI or small text) and
keep the whole file under 20 MB. Never hot-link, never use real photos of
real people, real products or real logos.

### 7. Set the icons

Read [references/icon-library.md](references/icon-library.md). Every
pictorial mark is an inline SVG from the sprite at the top of `<body>`,
used through `<use href="#i-…">`: `i-menu` and `i-x` for the menu toggle,
`i-arrow-right` on buttons and service rows, `i-arrow-up-right` on poster
hover badges and text links, `i-arrow-left` and `i-arrow-right` on detail
previous/next, `i-plus` on the accordion, `i-check` on include lists,
`i-mail`, `i-phone`, `i-map-pin` and `i-calendar` in the contact card,
`i-pen-tool`, `i-printer` and `i-clock` on the principles, `i-send` on the
form button and `i-arrow-up` for back-to-top. Lucide glyphs are for UI;
LobeHub monochrome marks are allowed only for genuine AI-integration
contexts with a visible text label. Never emoji, dingbats or icon fonts.
Tool tiles are two-letter text abbreviations on dark rounded squares, never
vendor logos.

### 8. Validate

Run `node scripts/validate-mono.mjs <output.html>` (add `--allow-replace`
only when checking the untouched template). It fails on remote resources,
storage or network APIs, emoji or dingbat icons, leftover REPLACE or image
tokens, Latin filler text, missing hash router, unresolved `#/` links and
missing style structure (grid-paper body, stagger hero title, portrait
cut-out, label chips, eight poster cards, tool tiles, work filters,
accordion, four-column footer).

### 9. Walk every route in a browser

Open the file and visit Home, About, Work, all eight detail pages,
Services, Contact and an unknown route. Check that the hero title stays on
one line at 1280 and 1920 and wraps cleanly at 390; that the portrait
fades out rather than ending in a hard edge; that poster shadows do not
clip at the grid edges; that the mobile menu opens, navigates and closes;
that the filter, accordion and form respond; and that nothing scrolls
horizontally at 390, 1280 or 1920.

## Catalog demo constraints

These file/sandbox/hash constraints apply to the catalog demo. Generated
websites follow the selected framework as described in step 2.

- Self-contained and sandbox-safe: no external scripts, styles, fonts or
  images; no fetch, storage, cookies, `window.open` or `target="_top"`.
- English by default; other languages only when the user asks.
- All names, clients, testimonials, prices, handles and contact details are
  fictional; domains end in `.example`.
- Palette discipline: greyscale interface, colour only inside artwork.
- Hash routing only; no top-level navigation.

## Files

- `references/template.html` — the engine with REPLACE slots and
  placeholder artwork.
- `references/style-guide.md` — tokens, type, signature moves, voice.
- `references/page-library.md` — every page and section, canonical order.
- `references/icon-library.md` — sprite ids and icon rules.
- `references/third-party-notices.md` — Lucide notice; everything else
  original.
- `scripts/validate-mono.mjs` — the validator described in step 8.
- `examples/demo.html`, `examples/preview-*.webp` — the finished example.

- `references/framework-adaptation.md` - stack selection, component mapping, image coverage and fidelity checks

## Updated visual and route inventory

Read references/visual-contract.md and references/route-inventory.md for
the current image coverage, tokens and connected pages. These supplement
the original page library. Use dedicated imagery for unrelated entities.


## Refinement v2

Use the monochrome grid-paper shell as a quiet exhibition frame. Keep biography and service descriptions concise; case studies use a short brief, approach and outcome. Display the eight selected posters at their full 2:3 ratio, including on mobile; never stretch or crop the artwork to fill a shallow card. Portfolio subjects can differ, but maintain consistent poster scale, frame and captions. The ten active assets include the grayscale designer portrait, eight posters and a monochrome studio photograph. Avoid unrelated product still lifes on case pages. Use authentic Photoshop, Illustrator and Figma marks for their software positions; drawing and printing use consistent line icons, not invented two-letter badges. Fields are 48px high, textareas at least 128px. Keep the mobile hero title on one line.


## Interior page depth

Read references/interior-pages.md. Preserve the complete page-specific content, image roles, selection states and contextual actions in the working template. Do not reduce inner pages to a heading and a few summary sentences.

---

## More from Skillry

This skill is a free open-source website template from [Skillry](https://skillry.dev).

- Explore the full catalog of creative design, presentation, video, and web skills at [skillry.dev](https://skillry.dev).
- Connect Skillry MCP or browse all 87 free skills: `npx --yes skillry-cli@latest mcp` · [github.com/yihui-dev/skillry-skills](https://github.com/yihui-dev/skillry-skills)
