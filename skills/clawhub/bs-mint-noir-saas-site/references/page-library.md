# Page library

Every page starts under the shared sticky nav and ends with the shared
footer (brand + tagline + seven social squares, four link columns, status
row, giant 6 % wordmark). Section order below is fixed; slots in brackets.

## Product (`home`)

| Section | Slots | Interaction |
| --- | --- | --- |
| Hero | announcement pill [tag, text]; two-line headline [serif word]; sub-headline; primary CTA (download icon) + ghost CTA (arrow); trust row [5 avatars, proof line] | CTAs route or toast |
| App window | sidebar [nav items, task list, user]; title + status pill; KPI tiles x4 [label, value, delta]; revenue sparkline; key finding | sidebar tasks swap the report; KPIs count up; sparkline draws in |
| Integrations strip | eyebrow; 6 real integration marks + names | hover brighten |
| Feature row | eyebrow "01 — …"; heading with serif word; side note; 3 cards [icon, index, title, text] | hover lift |
| Bento | agent card [3:4 portrait ID card, role chips]; integrations tile grid; model chips; approval card; schedule list | chips select; Approve flips state; schedule lights up in sequence |
| Testimonial | serif quote with mint phrase; author [avatar, name, role · shop · city]; 4 proof stats | stats count up |
| Closing CTA | eyebrow; headline with serif phrase; note; two CTAs | — |

## Pricing (`pricing`)

Hero with Monthly / Yearly toggle (savings badge) → three plan cards
(Starter, featured Pro with glow and "Most popular" tag, Team) with price,
billing note, CTA and includes list → trust row → compare table (Pro column
header in mint, checks and dashes) → billing FAQ accordion (first open).
The toggle recalculates every price and billing note.

## Resources (`resources`)

Hero with glowing search field (keyboard hint) and popular chips → 2×3
category cards [icon tile, title, text, "N articles" link] → two columns:
numbered popular articles and levelled tutorial cards (Beginner /
Intermediate / Advanced tags, author, read time) → support card with avatar
stack and "Contact support". Search filters categories and articles live.

## Events (`events`)

Hero → featured live workshop card (LIVE tag with pulsing dot, title with
serif word, mono date line, host, "Save my seat", registrant avatars,
4-box countdown, agenda 01–04) → upcoming sessions with type filter pills
and rows [big date, type tag, title, meta, host avatar, Register] → three
replay cards (gradient thumbnail, play button, duration) → newsletter card
with validated email field.

## Changelog (`changelog`)

Hero with "Subscribe to updates" and RSS → timeline: version + date column,
vertical line with nodes (the one nearest the viewport centre glows),
release cards [tags, title, text, optional preview panel, check list] →
"Load older releases" reveals hidden entries, then reports "all caught up".

## Adding content

- New plan: add a card and a compare-table column; keep the featured plan in
  the middle.
- New event: add a row with a `data-type` matching a filter pill.
- New release: add a timeline item at the top and move the glowing node.
- New page: add a `<section class="page" data-page="id">` (single file) or a
  route (framework), a nav link and a footer link.
