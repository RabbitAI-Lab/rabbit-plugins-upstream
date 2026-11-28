> Pages are built from the style kit's recipes in `references/style-kit.json` (SKILL.md Workflow step 4); keep the composition rules in this file as design guidance. The HTML snippets below only illustrate each archetype's geometry and hierarchy; do not paste them as slides. Their `<section>` wrappers and `data-*` attributes come from the retired hand-written format and are not required.

# Layout library (layout v3)

All nine archetypes are recipes in `style-kit.json`, and the kit's `contentCSS` styles them. Follow the rules below on every page. Measurements are in px on the 1280x720 page.

## Hard rules (read first)

1. **Word budget.** Headline ≤ 7 words (cover title ≤ 5). At most one supporting line ≤ 18 words. At most 3 items per page; an item is a label (≤ 3 words) plus at most one line ≤ 10 words, or a number plus a 2–4 word caption. No paragraphs, nothing longer than 2 lines. Whole page ≤ 45 words excluding numbers. Detail goes into `slide.notes`.
2. **Chrome.** Content pages carry only the brand mark top-left (`.topline > .brand`). No pill or tag clusters, date pills, section pills, footer captions or page numbers; at most one small `.label` eyebrow on the cover. "Illustrative" or "fictional" disclaimers go in the notes; a page that shows numbers may carry one `.footnote` of ≤ 6 words above 634px.
3. **Grid.** 12 columns, side margins 77px, gutters 26px, column 70px (column n starts at 77 + 96·(n−1) px; 4 columns = 358px, 5 = 454px, 6 = 550px). Content runs from 79px to 634px. Blocks align to column edges; blocks in one row share top, height and style. At most 3 content blocks; keep about a third of the page empty.
4. **Pictures.** Never overlap two pictures. The signature move — a violet glass card sitting inside a photo, inset 26px / 22px from the photo's edge — is used on at most 2 pages (the demo uses it on `solution` and `closing`). Otherwise use a framed photo beside text, a clean split, or a full-bleed art page. One radius (`--r`, about 14px) for every photo and card.
5. **Cards.** Siblings share one style (light glass `.card`); highlight one with `.violet-card` at the same size. A card holds a label, one line and an optional number — no tick lists, no icons unless they carry meaning.
6. **Type.** Embedded Geist (display + body) and Geist Mono (labels, axes). `h1` 123px / 500 / −0.045em; `h2` 54px / 500 / −0.035em / 1.04; `h3` 20px; `.lede` 19px at 0.78 opacity; body 16px; `.label` 10px mono uppercase +0.1em; numbers use `.num` (tabular). Keep `--font-display` / `--font-body` / `--font-mono` as the font variables.
7. **Colour.** One accent element per page (a violet card, the chart card, or one accent number). Dark pages stay `cover`, `opportunity`, `roadmap`; never add more dark pages.

## Building blocks

`.text-col` (flex column, 19px gap), `.image-window` (rounded photo frame) with `img.art`, `.card` / `.card.violet-card`, `.row` of `.item`s (hairline top rule; label/h3 + one line), `.stat` (`.big.num` with optional `<small>` unit and `.cap`), `.label`, `.footnote`, `.stage` (absolute picture layer), `.decor` (non-editable art).

## Archetypes

1. **Cover** (`cover`, dark) — `.cover-art.decor` full-bleed glass art with `.cover-shade`; `.text-col.cover-text` (cols 1–6, bottom-aligned at 634px): optional `.label` eyebrow, `h1.cover-title`, one `.lede`.
2. **Overview** (`opportunity`, dark) — `.text-col.ov-text` (cols 1–5, bottom-aligned): `h2` + one line; one `.image-window.ov-photo` cols 7–12, 79–634px.
3. **Problem** (`problem`, light) — `.image-window.vis-photo` cols 1–5, 79–634px; `.text-col.vis-text` cols 7–12 at the top (h2 + one line); `.row.vis-stats` of two `.item.stat` pinned to 634px (Today / Tomorrow, one accent number).
4. **Solution** (`solution`, light) — `.text-col.mis-text` cols 1–6 (h2 + line), `.row.mis-steps` of two `.item`s (h3 + one line) pinned to 634px; `.image-window.mis-photo` cols 8–12 with the signature `.violet-card.stat.mis-card` inside it.
5. **Evidence** (`evidence`, light) — `.text-col.ch-text` cols 1–4 (h2, line, `.stat` pinned low, `.footnote`); `.violet-card.ch-card` chart cols 5–9; portrait `.image-window.ch-photo` cols 10–12. The chart is HTML: `.ch-legend`, `.chart` > `.y-axis`, `.plot` > `.group` > `.bar.s1/.s2` with heights `.h10`–`.h90`, `.x-axis`.
6. **Pricing** (`model`, light) — centred `.pr-head` (h2 + line); three equal `.card.pr-card` (`.pr-a`, `.pr-b` violet, `.pr-c`) cols 1–4 / 5–8 / 9–12, 274–634px: `.label`, `p.price`, `p.desc` (one line). Feature lists go in the notes.
7. **Roadmap** (`roadmap`, dark) — `.rm-art.decor` glass steps top-right (masked fade), `h2.rm-title` left, hairline `.rm-line` with `.rm-dot`s at 77 / 461 / 845px, three equal `.card.rm-card` (middle violet) at 432–634px: `.label` period, `h3` stage, `p.gate` one line.
8. **Team** (`team`, light) — `.tm-head` (h2 left, one `.lede` right, cols 8–12); three equal `.image-window.tm-photo` portraits (cols 1–4 / 5–8 / 9–12, 216–576px); `.tm-name` rows beneath (h3 name, mono role).
9. **Contact** (`closing`, light) — centred `h2.ct-title`; `.image-window.ct-band` cols 1–12, 187–562px, with the signature `.violet-card.ct-card` inside its lower right (cols 9–12, inset); one quiet `.ct-bar` contact line (two items, Lucide icons) at 590px.

## Skeletons

```html
<section class="slide dark" data-slide-id="opportunity"><div class="topline"><span class="brand">…</span></div><div class="text-col ov-text"><h2 data-edit-id="opportunity-title">One plan.<br>Less friction.</h2><p class="lede" data-edit-id="opportunity-copy">…</p></div><div class="stage"><div class="image-window ov-photo"><img class="art" alt="…" src="…"></div></div></section>

<section class="slide" data-slide-id="solution"><div class="topline">…</div><div class="text-col mis-text"><h2>…</h2><p class="lede">…</p></div><div class="row mis-steps"><div class="item"><h3>Collect</h3><p>…</p></div><div class="item"><h3>Decide</h3><p>…</p></div></div><div class="stage"><div class="image-window mis-photo"><img class="art" alt="…" src="…"></div></div><div class="card violet-card stat mis-card"><p class="big num">2<small>min</small></p><p class="cap">to read a full project</p></div></section>

<section class="slide dark" data-slide-id="roadmap"><div class="rm-art decor"><img class="art" alt="…" src="…"></div><div class="topline">…</div><h2 class="rm-title">…</h2><div class="rm-line decor"></div><div class="rm-dot decor" style="left:6vw"></div><div class="rm-dot decor" style="left:36vw"></div><div class="rm-dot decor" style="left:66vw"></div><div class="card rm-card rm-a"><p class="label">Weeks 1–4</p><h3>…</h3><p class="gate">…</p></div><!-- rm-b violet-card, rm-c --></section>

<section class="slide" data-slide-id="team"><div class="topline">…</div><div class="tm-head"><h2>The team</h2><p class="lede">…</p></div><div class="stage"><div class="image-window tm-photo tm-a"><img class="art" alt="…" src="…"></div><!-- tm-b, tm-c --></div><div class="tm-name tm-a"><h3>Name</h3><p>Role</p></div><!-- tm-b, tm-c --></section>
```

The evidence and contact pages follow the same pattern with the class names above. If copy does not fit its region, cut words; never shrink type or add a block.
