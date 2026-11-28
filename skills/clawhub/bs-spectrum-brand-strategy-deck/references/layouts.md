> Pages are built from the recipes in `references/style-kit.json` (SKILL.md Workflow step 4); every page is a fixed 1280x720 card in the shared editor. The HTML snippets below only illustrate geometry, hierarchy and proportions; they are not an editor template and are never written into the deck by hand. Do not copy a legacy engine, UI stylesheet, state hook or exporter.

# Layout library (layout v3)

The style reference and migrated example project document these original compositions. Compose each page from its recipe in `style-kit.json`, replace the content with the user's, keep node IDs unique, and update `slide.notes` to match.

## Hard rules (read first)

1. **Word budget.** Headline ≤ 7 words (cover title ≤ 5). At most one supporting line ≤ 18 words. At most 3 items per page; an item is a label (≤ 3 words) plus at most one line ≤ 10 words, or a number plus a 2–4 word caption. No paragraphs, nothing longer than 2 lines. Whole page ≤ 45 words excluding numbers. Detail (fourth values, need lists, owners, dates, contact details) goes into `slide.notes`.
2. **Chrome.** Content pages carry only the brand mark top-left (`.topline > .brand`: four tiny spectrum tiles + name). No eyebrow pills, series labels, date or section tags, footer captions or page numbers; one small `.eyebrow` is allowed on the cover only. "Fictional" / "illustrative" disclaimers go in the notes; a page that shows numbers may carry one `.footnote` (≤ 6 words) at y 612px.
3. **Grid.** On the 1280x720 page: 12 columns, side margins 77px, gutters 26px, column 70px (column n starts at 77 + 96·(n−1) px; 4 columns = 358px, 6 = 550px). Content runs from y 79px to y 634px. Blocks align to column edges; blocks in one row share top, height and style. At most 3 content blocks per page; keep about a third of the page empty.
4. **Pictures.** Never overlap two pictures and never float a card over a picture. Use a framed picture in grid columns (`.frame`), or a picture bleeding off one page edge (`.bleed-left`, `.closing-art`). Each picture appears on one page only. One radius (`--r`, about 18px) for every framed picture and card.
5. **Cards and tiles.** Siblings share one style: dark `.card` surfaces. Highlight one card per page with a spectrum colour class (`.hl.t-green`, `.hl.t-blue`, `.t-orange`, `.t-yellow`) at the same size. A card holds a small label or number, a title and one line, or a big number and a caption. No icons, tick lists or chips inside cards.
6. **Type.** Embedded Bricolage Grotesque (display, weight 600) and Figtree (body). `.display` 133px / .92 / −0.045em (84px on the closing page); `.heading` 61px / 1.02 / −0.035em; `.lead` 20px at 0.78 opacity; body 17px / 1.45; card and row titles 27–36px; `.label` 11px uppercase +0.1em; big numbers `.num` 84px with tabular figures. Keep `--font-display` / `--font-body` as the font variables; never fall back to an Arial-only stack.
7. **Colour.** Every page is deep ink with cream type (no light pages). Use one spectrum accent per page: one highlighted tile, the yellow quote, the yellow numbered nodes, or one coloured row title. Pictures carry the rest of the colour.

## Building blocks

`.topline` + `.brand` (brand mark), `.heading` / `.display`, `.lead`, `.label`, `.frame` with `img.figure` (rounded picture window), `.row3` (three equal columns across columns 1–12), `.card` (+ `.hl` and a `.t-*` colour), `.rows > .item` (hairline rows: small label or number column + title and one line), `.node` (yellow numbered circle), `.quote` (yellow display quote), `.footnote`, `.decor` (non-editable art).

## Archetypes

1. **cover** — `.cover-text` cols 1–6, bottom-aligned at y 634px: optional `.eyebrow`, `.display` title (≤ 5 words), one `.lead`. `.frame.cover-art` cols 7–12, y 79–634px: a square 3D still life.
2. **promise** (three values) — `.pr-text` heading + one supporting line at the top; `.row3.pr-cards` three equal cards at y 360–634px (number label top, title + one line bottom), the middle one highlighted green.
3. **audience** (segments) — `.au-text` cols 1–5: heading at the top, supporting line at y 634px. `.rows.au-rows` cols 7–12, y 94–634px: three hairline rows (number, 36px segment name, one line); the segment to focus on first is coloured blue.
4. **positioning** (half-bleed picture) — `.bleed-left` portrait picture fills the left 557px edge to edge (no brand mark on this page). `.po-text` cols 7–12: heading + yellow `.quote`. `.rows.kv` three key/value rows pinned to y 634px.
5. **voice** (comparison) — heading at the top; `.vo-table` y 331–634px: three columns (principle in display type, "Write this" with a green label, "Avoid this" muted and struck through), three rows.
6. **touchpoints** — heading in cols 1–4; `.frame.tp-art` landscape picture cols 5–12, y 79–454px; `.row3.tp-steps` three steps (number, title, one line) under hairlines at y 511–634px.
7. **roadmap** — heading at the top; a hairline `.rm-rule` at y 403px with three yellow `.node`s at the column starts; under each: week `.label`, phase title, one "Exit:" line.
8. **measurement** (big numbers) — heading + one baseline line; `.row3.me-cards` three equal cards at y 338–598px (label top, `.num` + caption bottom), one highlighted blue; `.footnote` "Illustrative pilot targets" at y 612px.
9. **closing** — `.closing-art` landscape picture bleeds off the right edge with a soft left fade; `.display` (84px) at the top left; `.rows.cl-steps` three decisions with yellow `.node`s pinned to y 634px. Meeting times, owners and contact details go in the notes.

## Rules of thumb

- One focal point per page: the heading or the picture, then one block of items.
- Two-line headings on content pages; three lines only when the heading sits in a narrow column.
- Equal-height siblings in every row; whitespace should look intentional, not missing.
- Put text on the dark page or on solid tiles, never over a picture.
