> Pages are built from the recipes in `references/style-kit.json` (SKILL.md Workflow step 4); every page is a fixed 1280x720 card in the shared editor. The HTML snippets below only illustrate geometry, hierarchy and proportions; they are not an editor template and are never written into the deck by hand. Do not copy a legacy engine, UI stylesheet, state hook or exporter.

# Layout library

Ten archetypes share one stylesheet (the style kit's `contentCSS`), and `style-kit.json` carries a recipe for each. The target is a calm consultancy or annual-review profile: few words, large type, steel-blue framing and one arched picture per page. Positions and sizes below are given in px on the fixed 1280x720 page.

## Hard rules (check every slide)

1. **Word budget.** Headline ≤ 7 words (cover title ≤ 5). At most one supporting line ≤ 18 words. At most 3 items per slide; each item is a short label (≤ 3 words) plus at most one line ≤ 10 words, or a number plus a 2–4 word caption. No paragraphs, no text block longer than 2 lines, ≤ 45 words per slide excluding numbers. Detail goes into `slide.notes`.
2. **Chrome.** Only the small `.brand-mark` top-left (add `on-accent` on the steel field of framed pages; omit it on pages whose photo bleeds into the top-left corner). No pill or tag clusters, no date or section pills, no eyebrow labels (one small `.label` is allowed on the cover), no footers or folios. "Illustrative" disclaimers go into the notes.
3. **Grid.** 12 columns, side margins 77px, gutters 26px, column 70px; column n starts at `77 + (n-1) × 96` px (col 5 = 461px, col 7 = 653px, col 8 = 749px, col 12 ends at 1203px). Open pages: content from y 94px to y 634px. Framed pages: the white `.panel` runs 38px from the sides and from y 72px to y 670px; inside it, subtract 38px / 72px from page coordinates, and content runs from 50px below the panel top to 50px above the panel bottom. Blocks in a row share top, height and style. Keep at least 30% of the slide empty; at most 3 content blocks per slide.
4. **Pictures.** Never overlap two photos. Each photo is anchored to an edge or the panel and carries one arch corner (`--arch`, about 230px; about 128px for the paired team portraits) with an optional 4px steel stroke on the curved edges. The workflow `.overlap-card` is the deck's one card-on-photo move; align it to columns 1–4 and do not repeat it on more than one other page.
5. **Cards.** One corner radius `--r` (about 15px) for cards and the panel. Siblings share one style (soft fill or hairline rule). Highlight one at most (`.hi`: accent fill or accent rule), same size. A card holds a number or label, one title and one line. No icons inside cards.
6. **Type.** `--font-display` is embedded Manrope (600, tracking −0.035em, line-height ~1.04, sentence case, never uppercase); `--font-body` is embedded Hanken Grotesk. Cover `h1` 120px (second line in an accent `<span>`), page `h2` 59–64px, `.lead` 20px in `--muted`, body `p` 17px, `h3` 22–29px, `.label` 11px uppercase tracked +0.14em, big numbers `.num` (Manrope, tabular figures) 64–83px. Headings and leads use `text-wrap: balance`; keep lines under ~55 characters.
7. **Colour.** Steel `--accent` for the framed field, one top bar (`.frame-bars i`, 10px) on open pages and one highlighted element per slide. Headlines are `--deep` ink. Do not add dark pages.

## Shared parts

- `.brand-mark`: building icon + wordmark at left 77px, top 26px.
- `.dot-trio`: three small dots top-right at the brand-mark height, white on framed pages and on the cover photo.
- `.decor.frame-bars` holds one `<i>`: a thin accent bar on the top edge, positioned per archetype on the side opposite the photo.
- `.decor.chev`: the three-chevron SVG; use at most once in a deck as a quiet accent (commitments).
- `.head` (framed) / `.quality-head` (open): a two-column head row, `h2` in columns 1–6 and `.lead` in columns 8–12 on the last baseline.

## Archetypes

| # | Section class / id | Composition | Use for |
| --- | --- | --- | --- |
| 1 | `cover` | Soft field. `.cover-art` fills columns 7–12 to the right edge at full height with a 333px lower-left curve. `.cover-copy` (cols 1–6, top y 216px): one `.label`, two-line `h1`, one `.lead`. | Opening. |
| 2 | `introduction framed` | Panel: `.intro-copy` (cols 1–6) with `h2` and `.lead` at the top; `.metric-row` of three equal `.metric` cards (number + 2–3 word caption, first one `.hi`) at the panel base; `.intro-art` fills the panel from column 8 to its right edge with an arched top-left corner. | Who we are + three headline numbers. |
| 3 | `foundation` | `.arch-left` rises from the bottom-left (x 0–570px, from y 173px) with an arched top-right corner. `.found-copy` (cols 8–12): `h2` at the top, two ruled `.statement`s (`.label` + one display-weight line) at the bottom. | Mission / direction, two principles. |
| 4 | `capabilities framed` | `.head` row, then three equal soft `.service-card`s across the panel (cols 1–4, 5–8, 9–12): accent number at the top, `h3` and one line at the base. | Three services or pillars. |
| 5 | `reach` (`audience-journey`) | Left cols 1–6: `h2` + `.lead` at the top, `.reach-grid` of three `.reach-item`s (hairline rule, 82px number, short caption; the first `.hi` with an accent rule) at the bottom. `.arch-right` from column 8 to the right edge, from y 94px, arched top-left. | Segment counts, scope figures. |
| 6 | `workflow` | `.bleed-left` photo x 0–570px at full height with a steel right edge and the one `.overlap-card` (ink fill, big figure + one line) on cols 1–4 at the content bottom. Right cols 7–12: `h2` at the top, three ruled `.process` rows (accent number, `h3`, one line) at the bottom. | Three-step method. |
| 7 | `team framed` | `.head` row; bottom row (panel y 216px to base): two equal `.team-art` portraits (cols 1–3 and 4–6, outer corners arched) and a `.role-list` of three ruled roles (`h3` + one line) in cols 8–12, sharing the same top. | People and roles. |
| 8 | `quality` (`quality-review`) | `.quality-head` row; `table.standards` across all 12 columns: small uppercase header, three rows with a display-weight first column (first row `.hi` in accent), muted middle column, right-aligned cadence. Hairline rules only. | Measures, schedules, comparisons. |
| 9 | `pledge framed` (`commitments`) | Panel: `.pledge-copy` (cols 1–5) with `h2` + `.lead`; `.pill-stack` of three ruled rows filling cols 7–12 top to base (pale number, one display-weight promise line); `.decor.chev` at the panel's lower left. | Commitments, principles. |
| 10 | `closing` | `.closing-art` fills x 0–621px at full height with a 282px lower-right curve. Right cols 8–12: `h2` + `.lead` at the top, `.contact-row` of three ruled icon rows at the bottom. | Call to action and contacts. |

Common slide shell (open page), shown only to illustrate the structure the recipes produce:

```html
<section class="slide ARCHETYPE" data-slide-id="ID">
  <div class="brand-mark"><svg class="icon">…</svg><span>Company</span></div>
  <div class="decor frame-bars" data-edit="off"><i></i></div>
  <div class="body-wrap"> … </div>
</section>
```

Framed pages use `<div class="brand-mark on-accent">`, a `.dot-trio`, and put their blocks inside `.body-wrap > .panel`.

## Rules

- One takeaway per page. If the content does not fit the word budget, split it across two pages or move it into the notes; do not shrink the type.
- Alternate framed (steel) and open (white) pages; avoid two arch pages back to back where possible. Default sequence: cover, introduction, foundation, capabilities, reach, workflow, team, quality, commitments, closing.
- When adding a page, reuse an archetype and its grid positions rather than inventing new spacing.
