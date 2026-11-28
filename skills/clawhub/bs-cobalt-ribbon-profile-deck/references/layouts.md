> Pages are built from the style kit's recipes (`references/style-kit.json`) through `plan.json` and `scripts/style-kit.py compose`; see compose.md. The HTML snippets below only illustrate each composition's geometry, hierarchy and proportions. They are not an editor template and are never copied into the output. Do not copy a legacy engine, UI stylesheet, state hook or exporter.

# Layout library (v3)

Ten archetypes; the example deck uses all ten. Pages are fixed 1280x720 cards, so the prose below gives geometry in px at that size; CSS inside the snippets keeps its original units.

## Restraint rules (read first)

- **Word budget.** Headline ≤ 7 words (cover title ≤ 5). At most one supporting line ≤ 18 words. At most 3 items per slide; an item is a label ≤ 3 words plus at most one line ≤ 10 words, or a number plus a 2-4 word caption. No paragraphs, no text block longer than 2 lines, ≤ 45 words per slide (numbers excluded). Detail goes into `slide.notes`.
- **Chrome.** Only the small `.brand-mark` top-left on content slides. No pills, date or section tags, eyebrow labels (one tiny label on the cover only), folios or footer captions. "Illustrative" goes into notes; a slide showing invented numbers may carry one footnote ≤ 6 words, ending above y 634px.
- **Grid.** 12 columns, 77px side margins, 26px gutters (column = 70px; column n starts at 77 + (n-1)·96 px). Content starts at y 79px and ends at y 634px. Every block aligns to column edges; siblings in a row share top, height and style. Keep at least 30% of the slide empty; at most 3 content blocks.
- **Pictures.** Never overlap two photos and never float a card over a photo. Use a full-height photo on one side (angled cut allowed), a bottom band, or one framed photo on a column span. One radius for every photo and card: 0. Each picture appears on one slide only.
- **Cards.** Siblings share one style (all filled `--soft` or all ruled). Highlight one card only, by accent fill, at the same size. A card holds a label, one line and an optional number. Icons only where they add meaning, all 24-unit line icons at one size.
- **Typography.** Schibsted Grotesk (display, weight 600, tracking -0.03em) and Instrument Sans (body), embedded as base64 `@font-face` in the style CSS; keep `--font-display` / `--font-body`. Cover `h1` 102-115px; page titles 54-72px (`.ribbon` 54px); lead 20px; body text at least 17px at line-height 1.45; `h3` 26-38px; labels about 11px uppercase tracked +0.12em; big numbers 72-92px with tabular figures.
- **Color.** Light pages only; the cover is the single cobalt page. One accent element per slide besides the ribbon and the bottom chevron band.

## Shared parts

- `.ribbon` — the signature angled cobalt title band. It is absolutely placed at the content top; its band bleeds from the left edge with the title text on the 77px margin, or (on right-column pages) starts on the column-6 edge: `.workflow .ribbon{left:49.5vw;padding-left:1.5vw}`.
- `.brand-mark` — `<div class="brand-mark"><i></i><span data-edit-id="brand">Name</span></div>`; add `.on-accent` on the cover and on the `.brand-tab` (`<div class="decor brand-tab" data-edit="off"></div>` before `.body-wrap`) used on full-height left-photo pages.
- `.frame-bars` decor with one `<i>` draws the chevron band on the bottom edge (hidden on the cover).
- `.label`, `.num`, `.lead`, `.note` are the only text helpers; `img.pic` is every picture.

## 1. Cover (`.cover`)

The only cobalt page. White brand mark top-left; copy column on cols 1-5 anchored to the bottom content line: one tiny label (the only eyebrow in the deck), `h1` 102-115px (max 5 words), lead ≤ 12 words. `.cover-art` bleeds top, right and bottom with the angled cut.

```html
<section class="slide cover" data-slide-id="cover">
<div class="decor frame-bars" data-edit="off"><i></i></div>
<img class="pic cover-art" data-edit-id="city-art" src="library:<id> or data:image/webp;base64,..." alt="Original distribution hub scene generated for the fictional Fieldpath Logistics example" />
<div class="body-wrap">
<div class="brand-mark on-accent"><i></i><span data-edit-id="brand">Fieldpath Logistics</span></div>
<div class="cover-copy">
<p class="label" data-edit-id="edition">Company overview 2026</p>
<h1 data-edit-id="title">Company<br>profile</h1>
<p class="lead" data-edit-id="lead">Reliable regional routes and progress every customer can see.</p></div></div></section>
```

## 2. Contents (`.contents`)

Ribbon title, three numbered entries (label ≤ 3 words + one line) stretched from y 243px to the bottom content line; `.contents-art` fills the right 589px with a cut bottom-left corner. Group sections into three parts; never list eight rows.

```html
<section class="slide contents" data-slide-id="contents">
<div class="decor frame-bars" data-edit="off"><i></i></div>
<img class="pic contents-art" data-edit-id="office-art" src="library:<id> or data:image/webp;base64,..." alt="Original dispatch office scene generated for the fictional Fieldpath Logistics example" />
<div class="body-wrap">
<div class="brand-mark"><i></i><span data-edit-id="brand">Fieldpath Logistics</span></div>
<h2 class="ribbon" data-edit-id="title">Contents</h2>
<ol class="toc">
<li>
<span class="num">01</span>
<h3 data-edit-id="item-1">Who we are</h3>
<p data-edit-id="item-1-body">Our teams, mission and services.</p></li>
<li>
<span class="num">02</span>
<h3 data-edit-id="item-2">How we work</h3>
<p data-edit-id="item-2-body">One daily routine shared by every hub.</p></li>
<li>
<span class="num">03</span>
<h3 data-edit-id="item-3">Proof and pilot</h3>
<p data-edit-id="item-3-body">Quarterly signals and a clear next step.</p></li></ol></div></section>
```

## 3. Introduction (`.introduction`)

Full-height photo on the left 557px with the cobalt `.brand-tab` holding a white brand mark; headline + one lead on cols 7-12 at the top, three figures (number + 2-3 word label) on the bottom content line.

```html
<section class="slide introduction" data-slide-id="introduction">
<div class="decor frame-bars" data-edit="off"><i></i></div>
<img class="pic intro-art" data-edit-id="desk-art" src="library:<id> or data:image/webp;base64,..." alt="Original route planning scene generated for the fictional Fieldpath Logistics example" />
<div class="decor brand-tab" data-edit="off"></div>
<div class="body-wrap">
<div class="brand-mark on-accent"><i></i><span data-edit-id="brand">Fieldpath Logistics</span></div>
<div class="intro-copy">
<h2 data-edit-id="title">Routes you<br>can rely on</h2>
<p class="lead" data-edit-id="lead">Progress stays visible from the first plan to the final doorstep.</p></div>
<div class="metric-row">
<div class="metric">
<strong class="num" data-edit-id="m1">11</strong>
<span class="label" data-edit-id="m1-label">Delivery teams</span></div>
<div class="metric">
<strong class="num" data-edit-id="m2">7</strong>
<span class="label" data-edit-id="m2-label">Dispatch hubs</span></div>
<div class="metric">
<strong class="num" data-edit-id="m3">4</strong>
<span class="label" data-edit-id="m3-label">Service areas</span></div></div></div></section>
```

## 4. Mission band (`.foundation`)

Ribbon title, two statements (tiny label + one `h3` sentence ≤ 8 words) in two halves, photo band on the bottom edge with the notched top. No body paragraphs.

```html
<section class="slide foundation" data-slide-id="foundation">
<div class="decor frame-bars" data-edit="off"><i></i></div>
<img class="pic band-art" data-edit-id="desk-art" src="library:<id> or data:image/webp;base64,..." alt="Original operations floor scene generated for the fictional Fieldpath Logistics example" />
<div class="body-wrap">
<div class="brand-mark"><i></i><span data-edit-id="brand">Fieldpath Logistics</span></div>
<h2 class="ribbon" data-edit-id="title">Mission and direction</h2>
<div class="found-grid">
<article>
<p class="label" data-edit-id="mission-title">Mission</p>
<h3 data-edit-id="mission">One shared plan for every shift.</h3></article>
<article>
<p class="label" data-edit-id="direction-title">Direction</p>
<h3 data-edit-id="direction">Visibility from first route to final update.</h3></article></div></div></section>
```

## 5. Services (`.capabilities`)

Ribbon title and three service rows on cols 1-6 (icon + label + one line), one framed photo on cols 8-12 from the top to the bottom content line.

```html
<section class="slide capabilities" data-slide-id="capabilities">
<div class="decor frame-bars" data-edit="off"><i></i></div>
<img class="pic services-art" data-edit-id="service-art" src="library:<id> or data:image/webp;base64,..." alt="Original loading bay handover scene generated for the fictional Fieldpath Logistics example" />
<div class="body-wrap">
<div class="brand-mark"><i></i><span data-edit-id="brand">Fieldpath Logistics</span></div>
<h2 class="ribbon" data-edit-id="title">Services that connect</h2>
<div class="service-list">
<article class="service-card"><svg class="icon"><!-- 24-unit icon from icon-library.md --></svg>
<h3 data-edit-id="svc-1">Route planning</h3>
<p data-edit-id="svc-1-body">Daily routes built around customer commitments.</p></article>
<article class="service-card"><svg class="icon"><!-- 24-unit icon from icon-library.md --></svg>
<h3 data-edit-id="svc-2">Dispatch</h3>
<p data-edit-id="svc-2-body">Every job gets one owner and a next update.</p></article>
<article class="service-card"><svg class="icon"><!-- 24-unit icon from icon-library.md --></svg>
<h3 data-edit-id="svc-3">Live tracking</h3>
<p data-edit-id="svc-3-body">Progress and delays in one shared view.</p></article></div></div></section>
```

## 6. Key figures (`.reach`)

Plain cobalt headline with a lead on cols 8-12, three equal filled cards (number about 90px + 2-4 word caption). Highlight one card only with the accent fill. One footnote ≤ 6 words, ending above y 634px.

```html
<section class="slide reach" data-slide-id="audience-journey">
<div class="decor frame-bars" data-edit="off"><i></i></div>
<div class="body-wrap">
<div class="brand-mark"><i></i><span data-edit-id="brand">Fieldpath Logistics</span></div>
<div class="reach-head">
<h2 data-edit-id="title">Network at a glance</h2>
<p class="lead" data-edit-id="lead">A compact network run on one shared playbook.</p></div>
<div class="reach-grid">
<article class="goal-card">
<strong class="num" data-edit-id="num-1">11</strong>
<h3 data-edit-id="goal-1">Regional delivery teams</h3></article>
<article class="goal-card">
<strong class="num" data-edit-id="num-2">7</strong>
<h3 data-edit-id="goal-2">Dispatch hubs</h3></article>
<article class="goal-card accent">
<strong class="num" data-edit-id="num-3">95%</strong>
<h3 data-edit-id="goal-3">On-time handover target</h3></article></div>
<p class="note" data-edit-id="caption">Illustrative figures.</p></div></section>
```

## 7. Process (`.workflow`)

Angled photo on the left with `.brand-tab`; the ribbon starts on the column-6 edge; three numbered steps (cobalt squares) on cols 7-12.

```html
<section class="slide workflow" data-slide-id="workflow">
<div class="decor frame-bars" data-edit="off"><i></i></div>
<img class="pic process-art" data-edit-id="city-art" src="library:<id> or data:image/webp;base64,..." alt="Original warehouse handover scene generated for the fictional Fieldpath Logistics example" />
<div class="decor brand-tab" data-edit="off"></div>
<div class="body-wrap">
<div class="brand-mark on-accent"><i></i><span data-edit-id="brand">Fieldpath Logistics</span></div>
<h2 class="ribbon" data-edit-id="title">How work flows</h2>
<div class="process-list">
<article class="process"><span class="process-no">01</span>
<h3 data-edit-id="step-1">Plan</h3>
<p data-edit-id="step-1-body">Map the day and give each route one owner.</p></article>
<article class="process"><span class="process-no">02</span>
<h3 data-edit-id="step-2">Hand over</h3>
<p data-edit-id="step-2-body">Share open exceptions before the next shift.</p></article>
<article class="process"><span class="process-no">03</span>
<h3 data-edit-id="step-3">Review</h3>
<p data-edit-id="step-3-body">Weekly outcomes improve the next plan.</p></article></div></div></section>
```

## 8. Chart (`.performance`)

Ribbon title, two headline figures on cols 1-4, a bar chart on cols 6-12 with legend, axis and value labels. Footnote "Illustrative example data." under the figures when numbers are invented.

```html
<section class="slide performance" data-slide-id="performance">
<div class="decor frame-bars" data-edit="off"><i></i></div>
<div class="body-wrap">
<div class="brand-mark"><i></i><span data-edit-id="brand">Fieldpath Logistics</span></div>
<h2 class="ribbon" data-edit-id="title">Performance by quarter</h2>
<div class="perf-stats">
<article>
<strong class="num" data-edit-id="ins-1">93%</strong>
<span class="label" data-edit-id="ins-1-body">On-time handovers in Q4</span></article>
<article>
<strong class="num" data-edit-id="ins-2">+20 pts</strong>
<span class="label" data-edit-id="ins-2-body">Same-day exception closure</span></article></div>
<p class="note" data-edit-id="caption">Illustrative example data.</p>
<div class="chart">
<div class="legend"><span><i></i>On-time handovers</span><span><i class="alt"></i>Exceptions closed same day</span></div>
<div class="plot">
<div class="yaxis"><span>0</span><span>20</span><span>40</span><span>60</span><span>80</span><span>100</span></div>
<div class="bars">
<div class="grid-lines"><i></i><i></i><i></i><i></i><i></i><i></i></div>
<div class="quarter">
<div class="bar" style="height:82%"><b>82</b></div>
<div class="bar alt" style="height:64%"><b>64</b></div><em>Q1</em></div>
<div class="quarter">
<div class="bar" style="height:86%"><b>86</b></div>
<div class="bar alt" style="height:71%"><b>71</b></div><em>Q2</em></div>
<div class="quarter">
<div class="bar" style="height:90%"><b>90</b></div>
<div class="bar alt" style="height:78%"><b>78</b></div><em>Q3</em></div>
<div class="quarter">
<div class="bar" style="height:93%"><b>93</b></div>
<div class="bar alt" style="height:84%"><b>84</b></div><em>Q4</em></div></div></div></div></div></section>
```

## 9. Table (`.quality`)

Ribbon title with a lead on cols 8-12, three rows by three columns: signal in cobalt display type, owner and cadence in muted body type. Header row = tracked labels over an ink rule; no filled header band.

```html
<section class="slide quality" data-slide-id="quality-review">
<div class="decor frame-bars" data-edit="off"><i></i></div>
<div class="body-wrap">
<div class="brand-mark"><i></i><span data-edit-id="brand">Fieldpath Logistics</span></div>
<h2 class="ribbon" data-edit-id="title">Review cadence</h2>
<p class="lead" data-edit-id="lead">Three signals, each with a named owner.</p>
<table class="standards">
<thead>
<tr><th>Signal</th><th>Owner</th><th>Cadence</th></tr></thead>
<tbody>
<tr><td data-edit-id="sig-1">Adoption</td><td data-edit-id="own-1">Hub coordinator</td><td data-edit-id="cad-1">Weekly</td></tr>
<tr><td data-edit-id="sig-2">Clarity</td><td data-edit-id="own-2">Dispatch lead</td><td data-edit-id="cad-2">Daily</td></tr>
<tr><td data-edit-id="sig-3">Reliability</td><td data-edit-id="own-3">Operations manager</td><td data-edit-id="cad-3">Monthly</td></tr></tbody></table></div></section>
```

## 10. Closing (`.closing`)

Headline ≤ 6 words and one action line on cols 1-5, two contact lines with small line icons, angled photo on the right. No call-out boxes.

```html
<section class="slide closing" data-slide-id="closing">
<div class="decor frame-bars" data-edit="off"><i></i></div>
<img class="pic closing-art" data-edit-id="abstract-art" src="library:<id> or data:image/webp;base64,..." alt="Original loading dock scene generated for the fictional Fieldpath Logistics example" />
<div class="body-wrap">
<div class="brand-mark"><i></i><span data-edit-id="brand">Fieldpath Logistics</span></div>
<div class="closing-copy">
<h2 data-edit-id="title">Build the next<br>route together.</h2>
<p class="lead" data-edit-id="lead">Choose a pilot hub and agree a six-week review.</p>
<ul class="contact">
<li><svg class="icon"><!-- 24-unit icon from icon-library.md --></svg><span data-edit-id="mail">hello@fieldpath.example</span></li>
<li><svg class="icon"><!-- 24-unit icon from icon-library.md --></svg><span data-edit-id="web">fieldpath.example</span></li></ul></div></div></section>
```

## Pace

Alternate picture pages with structured pages (figures, chart, table). Suggested order for 10 pages: cover, contents, introduction, mission band, services, key figures, process, chart, table, closing. For 8 pages drop contents and the table.
