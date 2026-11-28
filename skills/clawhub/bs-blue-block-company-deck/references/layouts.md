> Pages are built from the recipes in `references/style-kit.json`. The composition rules below describe what each recipe is for; any HTML snippets only illustrate geometry and proportions on the fixed 1280x720 page and are not a template to copy.

# Layout library

Ten archetypes share one stylesheet (the style kit's `contentCSS`; the example project shows all ten filled). The target is a calm consultancy or annual-review deck: few words, large type, lots of white space. Sizes below are given in px on the fixed 1280×720 page.

## Hard rules (check every slide)

1. **Word budget.** Headline ≤ 7 words (cover title ≤ 5). At most one supporting line ≤ 18 words. At most 3 items per slide; each item is a short label (≤ 3 words) plus at most one line ≤ 10 words, or a number plus a 2–4 word caption. No paragraphs, no text block longer than 2 lines, ≤ 45 words per slide excluding numbers. Detail goes into `slide.notes`.
2. **Chrome.** Only the small `.brand-mark` top-left on content slides. No pill or tag clusters, no date or section pills, no eyebrow labels (one small `.label` is allowed on the cover), no footers or folios. "Illustrative" disclaimers go into the notes; a slide that shows numbers may carry one `.note` of ≤ 6 words.
3. **Grid.** 12 columns, side margins 77px (`--m`), gutters 26px, column 70px; column n starts at `77 + (n-1) × 96` px (col 5 = 461px, col 7 = 653px, col 8 = 749px, col 12 ends at 1203px). Content starts at 79px from the top (`--top`) and ends at 634px (`--bot`). Blocks in a row share top, height and style. Keep at least 30% of the slide empty; at most 3 content blocks per slide.
4. **Pictures.** Never overlap two photos and never float a card over a photo. Use a framed photo on an offset blue or stone block, a clean half/half split, or one large photo. One corner radius for photos and cards: `--r: 0`.
5. **Cards.** Siblings share one style (all outlined or all filled). Highlight one at most, with the accent fill, same size. A card holds a label, one line and an optional number. Icons only where they add meaning, all the same size and stroke.
6. **Type.** Headlines `h1`/`h2` use `--font-display` (embedded Newsreader, weight 500, tracking −0.025 to −0.035em, line-height ~1.0). Body, labels and names use `--font-body` (embedded Inter Tight). Cover `h1` 95px, page `h2` 47px (sentence case, never uppercase), `.lead` 19px in `--muted`, body `p` 15–17px, `.label` 11px uppercase tracked +0.12em, big numbers `.num` (Newsreader, tabular lining figures) 72–90px. Keep lines under ~55 characters.
7. **Colour.** White pages with blue panels. Use the accent for one element per slide (a panel, a block, one highlighted card or one filled circle). Do not add dark full-page backgrounds.

## Shared parts

- `.brand-mark` (logo icon + wordmark) at left 77px, top 32px; use the `on-accent` variant on blue backgrounds.
- Offset blocks are non-editable decorative bars; each page positions its own bar behind the photo so the block peeks out from one edge, often bleeding off the page. `--stone` (#c5cbd1) is the grey block; `--soft` (#eef2f6) the pale card tint; `--line` the hairline rule.
- Heads with a side lede use a 12-column grid: `h2` spans columns 1–6, `.lead` columns 8–12, aligned on the last baseline.

## Archetypes

| # | Recipe / id | Composition | Use for |
| --- | --- | --- | --- |
| 1 | `cover` | Text column (cols 1–5) bottom-aligned: one `.label`, two-line `h1`, one lede. Framed photo cols 7–12 from top to content bottom, a blue block bleeding off the top-right and a stone block peeking from its lower-left edge. | Opening. |
| 2 | `introduction` | Half/half: blue `.intro-panel` (x 0–576px) with title and lede at the top and two `.metric`s (number + label, hairline above) at the bottom; framed photo cols 7–12. | Who we are + two headline numbers. |
| 3 | `foundation` | Wide framed photo across all 12 columns with a blue block peeking from the left; below, `.found-grid` of three columns: title, then two ruled articles (`.label`, serif `h3`, one line). | Mission / direction, two principles. |
| 4 | `capabilities` | Head on white; background splits white/blue at x 384px; three equal outlined `.service-card`s (icon, number label, serif `h3`, one line) straddle the split. | Three services or pillars. |
| 5 | `reach` (`audience-journey`) | Blue frame with inset white `.reach-card`; head with side lede; three `.circle-metric` rings (218px) left-aligned to columns 1/5/9, the first filled; one caption each; one `.note`. | Segment counts, market sizes. |
| 6 | `workflow` | Tall framed photo cols 1–5 on a blue block bleeding off the bottom-left; right column: title, lede, three ruled `.process` rows (serif number, label, one line) bottom-aligned. | Three-step method. |
| 7 | `scope` (`pilot-scope`) | Left cols 1–6: title and lede at the top, three `.bar`s bottom-aligned (first one accent, others `--soft`); framed photo cols 8–12 on a stone block bleeding off the right. | Deliverables, commitments, programmes. |
| 8 | `quality` (`quality-review`) | `.q-head` with an accent left rule on the title and a side lede; `.standards` table of three rows × three columns (serif first column, hairline rules, no zebra, no header fill). | Measures, comparisons, schedules. |
| 9 | `team` | Blue `.team-band` (top 307px) with title and side lede in white; three rectangular `.portrait`s (one per 4-column span) straddle the band edge; serif name and `.label` role. | People, leadership, contacts. |
| 10 | `closing` | Blue `.closing-card` filling the content area on two stone offset blocks; brand mark, two-line title and one action line inside; three-column `.contact-row` at the card's foot. | Call to action and contacts. |

## Rules

- One takeaway per page. If the content does not fit the word budget, split it across two pages or move it into the notes; do not shrink the type.
- When adding a page, reuse an archetype and its grid positions rather than inventing new spacing.
- Icons are inline Lucide-style SVG (`references/icon-library.md`); no emoji or glyph arrows.
- Check every page at 1280×720 for wrapping and collisions before delivery.
