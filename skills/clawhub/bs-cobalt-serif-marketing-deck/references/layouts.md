> Pages are built from the style kit's recipes (`references/style-kit.json`) through `plan.json` and `scripts/style-kit.py compose`; see compose.md. The HTML snippets below only illustrate each composition's geometry, hierarchy and proportions. They are not an editor template and are never copied into the output. Do not copy a legacy engine, UI stylesheet, state hook or exporter.

# Layout library (layout v3)

All ten archetypes are recipes in `style-kit.json` and are shown filled in the example deck. Pick a recipe in `plan.json` and change its copy; the class names below are the ones the kit's `contentCSS` uses. Pages are fixed 1280x720 cards, so the prose gives geometry in px at that size. Every page is dark (`.slide.dark`); never add light pages.

## Hard rules (read first)

1. **Word budget.** Headline ≤ 7 words (cover title ≤ 5). At most one supporting line ≤ 18 words. At most 3 items per page; an item is a short label (≤ 3 words) plus at most one line ≤ 10 words, or a number plus a 2–4 word caption. No paragraphs, no text block longer than 2 lines. Whole page ≤ 45 words excluding numbers. Everything else goes into `slide.notes`.
2. **Chrome.** Each page carries only the brand mark top-left (`.topline > .brand`: small cobalt disc-and-crescent + name). No pill or tag clusters, date pills, section pills, footer captions, page numbers or meta rows; at most one tiny `.label` eyebrow on the cover. "Illustrative" or "fictional" disclaimers go in the notes; a page that shows numbers may carry one `.footnote` of ≤ 6 words, ending above y 634px.
3. **Grid.** 12 columns, side margins 77px, gutters 26px, column 70px (column n starts at 77 + 96·(n−1) px; cols 1–4 = x 77–435px, 5–8 = 461–819px, 9–12 = 845–1203px; cols 1–6 end at 627px, col 7 starts at 653px). Content runs from y 79px to 634px. Blocks align to column edges; blocks in one row share top, height and style. At most 3 content blocks per page; keep about a third of the page empty.
4. **Pictures.** Never overlap two pictures. Photos either bleed off one edge at full height on a clean half (`.photo.bleed-r` from col 7, `.photo.bleed-l` up to col 6) or sit in portrait circles. The deck's one signature move, a cobalt `.card.hi` inset inside a photo, is used on at most 2 pages (the demo uses it once, on `contact`). Every card uses the one radius `--r` (about 12px); portrait circles echo the cobalt discs.
5. **Cards.** Siblings share one style (filled `.card`); highlight one with `.card.hi` (cobalt) at the same size. A card holds a number or label, a title and one line — no icons, no tick lists.
6. **Type.** Embedded **Newsreader** (variable serif) for headlines, card titles and numbers; embedded **Geist** for body copy and labels. `.display` 128px (closing 108px) / 500 / −0.04em / 0.96; `.heading` 61px / 500 / −0.03em / 1.04; `h3` 24–38px; `.lead` 19px at 0.72 opacity (max 563px wide); `.line` 17px; `.label` 12px uppercase +0.12em; `.footnote` 14px; big numbers 44–84px with tabular lining figures. Keep `--font-display` / `--font-body` as the variables the style reads.
7. **Colour.** One cobalt accent element per page: a `.card.hi`, the first roadmap dot, one chart bar, one table number, or the crescent discs on cover and closing.

## Building blocks

`.topline .brand` (brand mark), `.text-col` (absolute flex column, 20px gap) holding `h2.heading` + `p.lead`, `.row` (absolute grid) of `.item`s (hairline top rule; `h3` or `.label` + `p.line`), `.card` / `.card.hi`, `.photo` with `img.case-image`, `.num`, `.label`, `.footnote`, `.decor` (non-editable art such as the disc SVG, timeline line and dots).

## Archetypes

| # | id | Key classes | Composition | Use for |
| --- | --- | --- | --- | --- |
| 1 | cover | `cover` + `.visual.decor` disc SVG, `.text-col.cover-text` | Glowing cobalt circle and two crescents bleed off the right; optional `.label` eyebrow, 128px serif title (≤ 5 words) and one lede, bottom-left | Opening |
| 2 | goals | `.text-col.goals-text`, `.row.goal-row` of `.card.goal-card` | Heading + lede top-left; three equal cards on cols 1–4 / 5–8 / 9–12 from y 331px to 619px: serif number at the top, title + one line anchored at the bottom; first card `.hi` | Three goals, pillars, principles |
| 3 | audience | `split` + `.photo.bleed-r` + `.text-col.split-text` + `.row.split-items` | Photo bleeds off the right edge from col 7; heading + lede top-left; two `.item`s (label + one line) at y 475px | Audience, need, positioning |
| 4 | roadmap | `.text-col.rm-text`, `.rm-line`/`.rm-dot` decor, `.row.rm-row` | Heading + lede; one hairline at y 374px with three dots (first cobalt) at x 77 / 461 / 845px; three phases beneath (y 410–619px): `.label` unit, 64px serif week numeral `.num.wk`, 33px serif name and one line anchored low | Timelines, phases |
| 5 | budget | `.text-col.bd-text`, `.bd-stat`, `.bd-chart` of `.bd-bar` | Heading cols 1–4 with one big total and caption low; quiet horizontal bar chart cols 6–12 (name, bar, value), one `.hi` bar in cobalt; `.footnote` | Budgets, splits, one key number |
| 6 | team | `.text-col.tm-text`, `.lead.tm-lede`, `.row.tm-row` of `.member` | Heading left, one lede right-aligned on cols 8–12; three 256px portrait circles with serif name and `.label` role | Team, owners |
| 7 | channels | `mirror` + `.photo.bleed-l` + `.text-col.split-text` + `.row.ch-list` | Photo bleeds off the left edge to col 6; heading + lede on cols 8–12; three hairline rows (name + one line) | Channels, options, workstreams |
| 8 | scorecard | `.text-col.sc-text`, `.lead.sc-lede`, `table.sc-table` | Heading left, lede right; a quiet three-row table across all columns: serif measure, today, big target (one in cobalt), owner; `.footnote` | Targets, KPIs, comparisons |
| 9 | contact | `contact` + `.photo.bleed-r` + `.text-col.ct-text` + `.row.ct-list` + `.card.hi.note-card` | Heading + lede top-left; three hairline contact rows; photo bleeds right from col 7 with the signature cobalt card inset (label, number, one line) | Contact, next review |
| 10 | closing | `closing cover` + disc SVG + `.text-col.cover-text` + `.row.cl-steps` | Discs on the right; 108px serif line (≤ 7 words), one lede, three numbered decisions on a hairline at y 504px | Closing ask |

## Skeletons

```html
<section class="slide dark" data-slide-id="goals" data-dark="true"><div class="topline"><span class="brand"><svg>…</svg><span data-edit-id="brand">Brand</span></span></div><div class="text-col goals-text"><h2 class="heading" data-edit-id="heading">Three goals.<br>One launch.</h2><p class="lead" data-edit-id="lead">…</p></div><div class="row goal-row"><article class="card goal-card hi"><p class="num">01</p><h3 data-edit-id="goal-1">…</h3><p class="line" data-edit-id="goal-1-line">…</p></article><!-- two more .card.goal-card --></div></section>

<section class="slide dark split" data-slide-id="audience" data-dark="true"><div class="topline">…</div><div class="photo bleed-r"><img class="figure case-image" data-edit-id="…" src="…" alt="…"></div><div class="text-col split-text"><h2 class="heading" data-edit-id="heading">…</h2><p class="lead" data-edit-id="lead">…</p></div><div class="row split-items"><div class="item"><h3>Who</h3><p class="line">…</p></div><div class="item"><h3>Barrier</h3><p class="line">…</p></div></div></section>

<section class="slide dark" data-slide-id="roadmap" data-dark="true"><div class="topline">…</div><div class="text-col rm-text"><h2 class="heading" data-edit-id="heading">…</h2><p class="lead" data-edit-id="lead">…</p></div><div class="rm-line decor"></div><div class="rm-dot decor on" style="left:6vw"></div><div class="rm-dot decor" style="left:36vw"></div><div class="rm-dot decor" style="left:66vw"></div><div class="row rm-row"><div class="item"><p class="label">Week</p><p class="num wk">1</p><h3>Listen</h3><p class="line">…</p></div><!-- two more --></div></section>

<section class="slide dark" data-slide-id="budget" data-dark="true"><div class="topline">…</div><div class="text-col bd-text"><h2 class="heading" data-edit-id="heading">…</h2></div><div class="bd-stat"><p class="num" data-edit-id="total">$12,000</p><p class="line">…</p></div><div class="bd-chart"><div class="bd-bar hi"><p class="name">Content</p><div class="track"><i class="fill" style="width:100%"></i></div><p class="num">$4.2k</p></div><!-- more .bd-bar, widths relative to the largest --></div><p class="footnote bd-note">Illustrative planning figures</p></section>
```

Bar widths are percentages of the largest value. Keep the chart to four or five bars and one cobalt bar.
