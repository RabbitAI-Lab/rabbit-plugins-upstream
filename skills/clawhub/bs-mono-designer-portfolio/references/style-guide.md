# Mono style guide

The page must read like a single sheet from a printed portfolio: grey
paper, a faint tilted grid, one heavy grotesk in near-black, and posters
hung with a soft shadow. The interface is greyscale; the work brings the
colour.

## Tokens (locked)

| Token | Value | Job |
| --- | --- | --- |
| `--ground` | `#e9e9e9` | page background |
| `--ground-2` | `#f2f2f2` | lighter panels |
| `--paper` | `#f8f8f8` | poster frames while loading |
| `--ink` | `#262626` | headings, buttons, chips, body emphasis |
| `--ink-2` | `#333333` | label chips, tool tiles, icon boxes |
| `--muted` | `#5c5c5c` | body copy |
| `--soft` | `#8a8a8a` | eyebrows, meta, captions |
| `--line` | `rgba(0,0,0,.09)` | hairlines, card borders |
| `--grid` | `rgba(255,255,255,.72)` | the grid-paper lines |
| `--shadow-poster` | long soft stack | resting poster cards |
| `--shadow-poster-hover` | deeper stack | lifted poster cards |
| `--r-tile` | `16px` | tool tiles and icon boxes only |
| `--font` | Avenir Next / Avenir / Segoe UI / system-ui | the only face |
| `--font-mono` | SF Mono / Menlo / Consolas | index badges, years, hex codes |
| `--wrap` | `1240px` | content width |

Rules:

- **No accent colour.** Buttons, chips, links and states are ink on
  ground or white on ink. If a colour is needed, it is inside an image.
- **Square corners** everywhere except the tool tiles and icon boxes
  (`--r-tile`) and the pulsing availability dot.
- **Hairlines, not boxes.** Rows and lists are separated by 1px lines;
  the only bordered surfaces are the translucent service and value cards.

## Ground

`body.grid-paper::before` draws two repeating linear gradients (120px
cells, 2px white lines at `--grid`), fixed, inset by minus 45 percent and
rotated minus nine degrees so the grid runs slightly uphill like the
reference sheet. `::after` adds a soft white radial highlight at the top
centre. Both are `pointer-events:none` and sit at z-index minus one and
two, so every section floats on the same paper.

## Type

- One family, weights 400 to 800. Never load web fonts.
- Hero title: 800 weight, `clamp(60px, 11.5vw, 164px)`, tracking
  `-0.05em`, line-height 0.9, `white-space: nowrap` (drops to 17vw on
  narrow phones). Each letter rises in with a 45ms stagger.
- Hero name: 600 weight, 26 to 46px, tracking `-0.025em`; discipline line
  400 weight in `--muted`.
- Page heads: 800 weight, 38 to 84px, tracking `-0.045em`, max 14ch.
- Section titles are `chip-label`: white 700 text on `--ink-2`, 20 to
  30px, padding `.42em .8em`.
- Eyebrows and form labels: 11px, 600, `.16em` tracking, uppercase, in
  `--soft`.
- Body: 15 to 17px in `--muted`, line-height 1.65; emphasis is 700 in
  `--ink`, never italics.

## Signature moves

- **Portrait cut-out.** A 2:3 figure, `object-fit: cover`, CSS
  `grayscale(1) contrast(1.08)`, `mix-blend-mode: multiply` so the white
  ground disappears into the paper, and a bottom mask that fades the last
  40 percent to nothing. It sits bottom-aligned beside the title.
- **Label chips.** Every section title is a dark chip. On Home the
  projects chip is centred; elsewhere chips align left.
- **Meta chips.** Hairline-bordered uppercase chips for location, year
  and availability; the availability chip carries a pulsing dot.
- **Poster grid.** Four columns at desktop, three at tablet, two on
  phones. Each card: 4:5 frame, cover image, mono index badge top-left,
  white arrow badge bottom-right that appears on hover, caption row with
  title left and category right. Hover lifts the frame 8px and scales the
  image 3.5 percent.
- **Tool tiles.** Two-letter abbreviations on dark rounded squares with a
  small label beneath; they tilt slightly on hover. Never vendor marks.
- **Service rows.** Number, name, one-liner and arrow on hairline rows;
  the row slides right on hover.
- **Dark CTA band.** Full-width ink band with a large headline, one white
  button and one ghost button, closing Home, About and Services.
- **Detail page.** Sticky full-height poster on the left; on the right the
  title, summary, four-cell meta list, Brief, Approach, Outcome,
  deliverables with check icons, hex swatches, and previous/next links.

## Motion

- Reveal-on-scroll: fade and 22px rise, 0.7s, with four delay steps.
- Hero letters: rise and un-rotate, staggered, replayed on each visit to
  Home.
- Hovers: 200 to 400ms on the cubic-bezier(.2,.7,.2,1) curve.
- `prefers-reduced-motion` removes all of it.

## Voice

- First person, plain and specific; short sentences; concrete nouns
  (stock, runs, venues, deadlines).
- Headlines state a stance ("I design posters that people keep"), not a
  category.
- Case studies follow Brief, Approach, Outcome with one modest number
  each; no awards language.
- Prices are shown as "From $650" with a turnaround beneath.
- Forms confirm in-page and say plainly that nothing was sent.

## Forbidden

Any accent hue in the interface; gradients other than the two ground
overlays; rounded buttons or cards; drop shadows on anything except
posters, tool tiles and the mobile menu; italics; emoji or dingbat icons;
vendor logos in the toolkit; photographs of real people; dark mode;
parallax; autoplaying media; Latin filler text.

## Icons

Inline SVG in the Lucide grammar only, defined once in the sprite and
referenced with `<use>`. See [icon-library.md](icon-library.md).


## Refinement v2

Use the monochrome grid-paper shell as a quiet exhibition frame. Keep biography and service descriptions concise; case studies use a short brief, approach and outcome. Display the eight selected posters at their full 2:3 ratio, including on mobile; never stretch or crop the artwork to fill a shallow card. Portfolio subjects can differ, but maintain consistent poster scale, frame and captions. The ten active assets include the grayscale designer portrait, eight posters and a monochrome studio photograph. Avoid unrelated product still lifes on case pages. Use authentic Photoshop, Illustrator and Figma marks for their software positions; drawing and printing use consistent line icons, not invented two-letter badges. Fields are 48px high, textareas at least 128px. Keep the mobile hero title on one line.


## Interior page depth

Read references/interior-pages.md. Preserve the complete page-specific content, image roles, selection states and contextual actions in the working template. Do not reduce inner pages to a heading and a few summary sentences.
