> Pages are built from the style kit's recipes in `references/style-kit.json` (SKILL.md Workflow step 4); keep the composition rules in this file as design guidance. The HTML snippets below only illustrate each archetype's geometry and hierarchy; do not paste them as slides. Their `<section>` wrappers and `data-*` attributes come from the retired hand-written format and are not required.

# Layout library (layout v3)

All ten archetypes are recipes in `style-kit.json`, and the kit's `contentCSS` styles them. Follow the rules below on every page. Measurements are in px on the 1280x720 page.

## Hard rules (read first)

1. **Word budget.** Headline ≤ 7 words (cover title ≤ 5). At most one supporting line ≤ 18 words. At most 3 items per page; an item is a label (≤ 3 words) plus at most one line ≤ 10 words, or a number plus a 2–4 word caption. No paragraphs, nothing longer than 2 lines. Whole page ≤ 45 words excluding numbers. Bios, detail and context go into `slide.notes`.
2. **Chrome.** Every page carries only the brand mark top-left (`.topline > .mark`). No section labels, date pills, eyebrows, footer captions or page numbers (no `.bottomline`). "Illustrative" or "fictional" disclaimers go in the notes; a page that shows numbers may carry one `.footnote` of ≤ 6 words with its foot at 634px.
3. **Grid.** 12 columns, side margins 77px, gutters 26px, column 70px. Column n starts at 77 + 96·(n−1) px (col 2 = 173, col 5 = 461, col 7 = 653, col 8 = 749, col 9 = 845); k columns span 96·k − 26 px (4 = 358px, 5 = 454px, 6 = 550px). Content runs from 86px to 634px. Blocks align to column edges; blocks in one row share top, height and style. At most 3 content blocks; keep about a third of the page empty.
4. **Pictures.** Never overlap two pictures. Photos bleed off an edge (cover, lead, partner, closing) or sit in a clean grid frame (`.frame`). The signature move — the white `.sig-card` with a violet tile, inside a photo at cols 7–12 with its foot at 634px — is used on at most 2 pages (the demo uses it on `lead` and `closing`). One radius for every photo and card: square corners.
5. **Cards.** Siblings share one style (white `.st-card`); highlight one with `.on` (violet) at the same size. A card holds a number, a label and one line — no lists, no icons.
6. **Type.** Embedded Schibsted Grotesk (display: headings, labels, numbers) and Inter (body). `h1` 133px cover / 90px closing, `h2` 67–74px, all uppercase, weight 600, tracking −0.03em, line-height 0.88–0.94; `h3` 19–31px uppercase 600; `.lede` 21px; body 17px at line-height 1.45; `.label` 11px uppercase +0.1em; numbers use `.num` (tabular). Keep `--font-display` / `--font-body` as the font variables.
7. **Colour.** One accent element per page (a violet tile, the `.on` card, or the bars). Dark pages stay `contents`, `team`, `achievements`; never add more dark pages.

## Building blocks

`.topline > .mark` (accent dot + studio name), `.frame` (absolute photo window, `img.portrait` / `img.team-photo` with `object-fit:cover`), `.arrow-tile.decor` (violet square with the Lucide arrow-up-right; size by width, it stays square), `.band` (h2 left, one `.lede` right, bottoms aligned), `.sig-card` (tile + `h3` + one line), `.items > .item` (ruled rows: `h3` label + one line), `.st-card`, `.hbar`, `.big-num`, `.label`, `.footnote`, `.decor` (non-editable art).

## Archetypes

| # | Page id (class) | Composition | Use for |
|---|---|---|---|
| 1 | `cover` (`cv-title`, `cv-lede`, `cv-photo`, `cv-tile`) | Three-line `h1` cols 1–6 from 94px, one `.lede` with its foot at 634px. Team photo bleeds cols 7–12 top to bottom; a 141px violet tile sits flush on its bottom-left corner. | Opening page. |
| 2 | `contents` dark (`ct-title`, `ct-rows`, `ct-row`) | Oversized "Contents" (102px) cols 1–6 anchored at 634px; three ruled chapter rows cols 7–12 ending at 634px (accent number + uppercase `h3` 38px). Three chapters, not a page list. | Agenda. |
| 3 | `overview` (`band`, `ov-tile`, `ov-photo`) | `.band` at 86px: two-line `h2` left, one line right (cols 8–12). Panoramic photo cols 2–12 from 288px to 634px; a col-1 violet tile at its top-left. | Overview, context, mission. |
| 4 | `lead` (`ld-photo`, `ld-text`, `sig-card`) | Close-up portrait full bleed (subject in the right half). `h2` + one line top-left (cols 1–5), signature card cols 7–12 inside the photo. | One featured person. |
| 5 | `team` dark (`band`, `tm-photo`, `tm-name`) | `.band` title row; three equal portraits cols 1–4 / 5–8 / 9–12 from 216px to 554px; name (`h3`) and role (`.label`) beneath. Max 3 people per page — split larger teams across pages. | Team roster. |
| 6 | `partner` (`pt-photo`, `pt-tile`, `pt-text`, `items`) | Clean split: portrait bleeds cols 1–6 (0–550px) top to bottom with a violet tile flush on its bottom-right corner. Cols 7–12: `h2` + one line at the top, three ruled `.item` rows ending at 634px. | One person and what they own, a service, a principle. |
| 7 | `structure` (`band`, `st-cards`, `st-card`) | `.band` title row; three equal white cards cols 1–4 / 5–8 / 9–12 from 331px to 634px (number top, `h3` + one line at the foot); the first card `.on`. | Process, how work moves, steps. |
| 8 | `achievements` dark (`band`, `ac-chart`, `hbar`, `ac-stat`, `ac-note`) | `h2` top-left; three horizontal bars cols 1–7 (274–576px) with values in the bar ends; one `.big-num` (95px) + caption centred in cols 9–12; `.footnote` "Illustrative figures." at 634px. | Outcomes, before and after. |
| 9 | `working-together` (`hb-head`, `hb-tile`, `hb-list`, `hb-row`) | Two-line `h2` cols 1–6 at the top, a 90px violet tile with its foot at 634px. Cols 8–12: three ruled rows (day `.label`, `h3`, one line) filling 86–634px. | Rituals, habits, principles. |
| 10 | `closing` (`cl-title`, `cl-lede`, `cl-photo`, `sig-card`) | Three-line `h1` (90px) cols 1–6 at the top, a two-line `.lede` with its foot at 634px. Portrait bleeds cols 7–12; signature card (CTA + contact address) inside it. | Closing and contact. |

## Rules

- One picture per semantic page; never repeat a photo on another page.
- Siblings in a row share top, height and style; the only highlight is `.on` or one accent element.
- Slide notes hold the detail the page leaves out.
- Bar widths use `.w56`, `.w68`, `.w80`; add classes in the same pattern for other values. Muted bars use `.op55` or `.op75`.
