> Pages are built from the recipes in `references/style-kit.json` (SKILL.md Workflow step 4); every page is a fixed 1280x720 card in the shared editor. The HTML snippets below only illustrate geometry, hierarchy and proportions; they are not an editor template and are never written into the deck by hand. Do not copy a legacy engine, UI stylesheet, state hook or exporter.

# Layout library (v3)

Nine archetypes, each with a recipe in `style-kit.json` and styled by the kit's `contentCSS`. Every page is a fixed 1280x720 card; positions and sizes below are given in px on that page.

## Restraint rules (apply to every slide)

1. **Word budget.** Headline ≤ 7 words (cover title ≤ 5). At most one supporting line ≤ 18 words. At most 3 items per slide; each item is a ≤ 3-word label plus at most one line ≤ 10 words, or a number plus a 2–4 word caption. No paragraphs, no text block longer than 2 lines, whole slide ≤ 45 words excluding numbers. Detail goes into `slide.notes`.
2. **Chrome.** Content slides carry only the small brand mark top-left. No pill or tag clusters, no date or section pills, no eyebrow labels (one tiny eyebrow on the cover only), no footer captions or folios. "Illustrative" disclaimers go in the speaker notes.
3. **Grid.** 12 columns, 77px side margins, 26px gutters (column 70px; column n starts at 77 + (n−1) × 96 px). Content starts at the top content line (y 79px) and ends on the bottom content line (86px from the bottom, y 634px). Blocks align to column edges; siblings in a row share top, height and style. At most 3 content blocks per slide; keep at least 30% of the slide calm.
4. **Pictures.** Never overlap two photos. Use a full-bleed photo with text on a clean side, a clean split, or one framed photo. The only card-over-photo overlap is the `workflow` figure card. One corner radius (`--r`, about 15px) for every photo and card; the arch is the only other shape.
5. **Cards.** Siblings share one style; highlight one card only, via the navy fill, at the same size. A card holds a label, one line and an optional number. Icons only when they add meaning, all the same size and stroke.
6. **Type.** Manrope (OFL, embedded as a base64 `@font-face`, ~25 KB) for display and body through `--font-display` / `--font-body`; keep it offline, never link a font CDN. Headlines weight 500, tracking −0.035em, line-height ~1.05: cover 110px, page `h2` 59–69px. Body and row lines 17px, `.lead` 19–23px, labels `.label` about 10px uppercase +0.14em, big numbers 56–115px (`.num`, lining figures; tabular in ruled lists).
7. **Colour.** One accent element per slide (a highlighted number, the navy focus card, or the filled ring). Light pages use `--paper` with soft contours; only `introduction` and `workflow` are dark. Do not add dark pages.

## Shared blocks

Start every slide with the contour decor, and every content slide with the brand mark, both supplied by the style kit's recipes:

```html
<svg class="decor contours" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true" data-edit="off">…two contour paths…</svg>
<div class="brand-mark" data-edit="off"><svg class="icon" …lucide waves…/><span>Service Playbook</span></div>
```

In the skeletons below, `<!--DECOR-->` and `<!--BRAND-->` stand for those blocks, `<svg class="icon" …lucide…/>` for an inline icon from `icon-library.md`, and `IMAGE_DATA_URI` for an embedded picture (or `library:<id>` before running the embed script). Shared helpers: `.label`, `.lead`, `.num`, `.photo` (absolute, cover-fit, `--r` radius) and `.rows > .row` (ruled label + line rows; set `--key` for the label column width).

## 1. Cover — diagonal edge-bleed photo (`cover`)

`.cover-copy` spans columns 1–6 and is vertically centred between the top and bottom content lines: one tiny `.label` eyebrow (the only eyebrow in the deck), `h1` at 110px on up to three short lines, `.lead` 23px. `.cover-art` bleeds off the top, right and bottom edges (666px wide) with a diagonal left edge (`clip-path`). The dot grid is shown only here. Cover title ≤ 5 words.

```html
<section class="slide cover" data-slide-id="cover"><!--DECOR--><div class="decor dot-grid" data-edit="off"></div><div class="body-wrap"><div class="cover-copy"><p class="label" data-edit-id="eyebrow">Front office training</p><h1 data-edit-id="title">Service<br>Desk<br>Playbook</h1><p class="lead" data-edit-id="lead">A consistent welcome, every shift.</p></div><img class="cover-art" data-edit-id="service-art" src="IMAGE_DATA_URI" alt="A guest with a suitcase arriving at a calm hotel front desk" /></div></section>
```

## 2. Photo + statement + three figures (dark) (`introduction`)

`.intro-art` bleeds off the left and bottom edges from the top content line to column 6 (one rounded top-right corner). Columns 7–12 hold `h2` + `.lead` at the top and `.metrics` (three ruled rows: 56px number + 2–4 word caption) on the bottom content line. Highlight only the first number.

```html
<section class="slide introduction dark" data-slide-id="introduction"><!--DECOR--><div class="body-wrap"><!--BRAND--><img class="photo intro-art" data-edit-id="service-art" src="IMAGE_DATA_URI" alt="A desk teammate greeting an arriving guest across the counter" /><div class="intro-copy"><h2 data-edit-id="title">The service<br>standard</h2><p class="lead" data-edit-id="lead">Every guest leaves the desk welcomed, informed and looked after.</p></div><div class="metrics"><div class="metric"><strong class="num" data-edit-id="m1-value">60s</strong><span data-edit-id="m1-label">To acknowledge each arrival</span></div><div class="metric"><strong class="num" data-edit-id="m2-value">3</strong><span data-edit-id="m2-label">Everyday desk habits</span></div><div class="metric"><strong class="num" data-edit-id="m3-value">1</strong><span data-edit-id="m3-label">Named owner per request</span></div></div></div></section>
```

## 3. Three checks + framed photo on a navy panel (`foundation`)

Columns 1–6: `h2`, `.lead`, and `.rows` (three ruled rows: check icon + ≤ 3-word label, one line) on the bottom content line. Columns 8–12: one framed `.found-art` photo from the top to the bottom content line, over a navy `.found-panel` that bleeds off the right edge (from x 1024px to the edge).

```html
<section class="slide foundation" data-slide-id="foundation"><!--DECOR--><div class="body-wrap"><!--BRAND--><div class="found-panel" aria-hidden="true"></div><div class="found-copy"><h2 data-edit-id="title">Ready for the<br>first shift</h2><p class="lead" data-edit-id="lead">Ten minutes of preparation makes the next eight hours calmer.</p></div><div class="rows"><div class="row"><h3 data-edit-id="c1-title"><svg class="icon" …lucide check…/>Walk the desk</h3><p data-edit-id="c1-text">Test the phone line and key printer.</p></div><div class="row"><h3 data-edit-id="c2-title"><svg class="icon" …lucide check…/>Read the log</h3><p data-edit-id="c2-text">Open requests and today’s priorities.</p></div><div class="row"><h3 data-edit-id="c3-title"><svg class="icon" …lucide check…/>Know escalation</h3><p data-edit-id="c3-text">Tonight’s duty manager and contacts.</p></div></div><img class="photo found-art" data-edit-id="desk-art" src="IMAGE_DATA_URI" alt="A prepared front desk with notebook, lamp and screen" /></div></section>
```

## 4. Three equal cards (`capabilities`)

`h2` + `.lead` top-left (columns 1–8). `.service-grid` is three equal cards spanning columns 1–4, 5–8 and 9–12 from y 301px to the bottom content line. Each card: a 64px `.num`, then `h3` + one line at the bottom. Exactly one card `.is-focus` (navy fill); the others share the outlined style. Put any fourth item in the notes.

```html
<section class="slide capabilities" data-slide-id="capabilities"><!--DECOR--><div class="body-wrap"><!--BRAND--><div class="cap-head"><h2 data-edit-id="title">Everyday desk habits</h2><p class="lead" data-edit-id="lead">Three habits, in the same order, on every shift.</p></div><div class="service-grid"><article class="service-card is-focus"><p class="num">01</p><div><h3 data-edit-id="h1-title">Greet</h3><p data-edit-id="h1-text">Acknowledge every arrival, even while on a call.</p></div></article><article class="service-card"><p class="num">02</p><div><h3 data-edit-id="h2-title">Verify</h3><p data-edit-id="h2-text">Confirm details from the screen, never aloud.</p></div></article><article class="service-card"><p class="num">03</p><div><h3 data-edit-id="h3-title">Guide</h3><p data-edit-id="h3-text">Explain the next step and how long it takes.</p></div></article></div></div></section>
```

## 5. Journey track — three rings (`audience-journey`)

Centred `.center-head`. `.journey` is three equal columns; 141px `.stage-ring` icons sit on a thin navy line that bleeds edge to edge; `h3` 28px and one line below. Mark at most one stage `.is-focus` (filled ring). Show the three stages that matter most; list the rest in the notes.

```html
<section class="slide reach" data-slide-id="audience-journey"><!--DECOR--><div class="body-wrap"><!--BRAND--><div class="center-head"><h2 data-edit-id="title">The guest journey</h2><p class="lead" data-edit-id="lead">Every stage has an owner, even on a quiet night.</p></div><div class="journey"><article class="stage"><span class="stage-ring"><svg class="icon" …lucide…/></span><h3 data-edit-id="s1-title">Arrival</h3><p data-edit-id="s1-text">Welcome, verify and guide.</p></article><article class="stage"><span class="stage-ring"><svg class="icon" …lucide…/></span><h3 data-edit-id="s2-title">Stay</h3><p data-edit-id="s2-text">Respond with clarity and pace.</p></article><article class="stage is-focus"><span class="stage-ring"><svg class="icon" …lucide…/></span><h3 data-edit-id="s3-title">Follow-up</h3><p data-edit-id="s3-text">Close every promise made.</p></article></div></div></section>
```

## 6. Three steps + full-height photo + one figure card (dark) (`workflow`)

Columns 1–5: `h2`, `.lead`, and `.rows` (number, label, one line) on the bottom content line. `.flow-art` bleeds off the top, right and bottom from x 653px. The `.flow-stat` card (number + 2–5 word caption) sits on the photo at columns 8–10, resting on the bottom content line. This card-over-photo is the deck's one signature overlap: use it on this page only.

```html
<section class="slide workflow dark" data-slide-id="workflow"><!--DECOR--><div class="body-wrap"><!--BRAND--><div class="flow-copy"><h2 data-edit-id="title">A handover<br>that travels</h2><p class="lead" data-edit-id="lead">Information should cross the shift change intact.</p></div><div class="rows"><div class="row"><span class="num">01</span><div><h3 data-edit-id="p1-title">Read the log</h3><p data-edit-id="p1-text">Open requests and today’s priorities.</p></div></div><div class="row"><span class="num">02</span><div><h3 data-edit-id="p2-title">Name the owners</h3><p data-edit-id="p2-text">One person for each next action.</p></div></div><div class="row"><span class="num">03</span><div><h3 data-edit-id="p3-title">Close the loop</h3><p data-edit-id="p3-text">Confirm the next teammate understood.</p></div></div></div><img class="photo flow-art" data-edit-id="service-art" src="IMAGE_DATA_URI" alt="Two desk teammates reviewing the handover log together" /><div class="metric flow-stat"><strong class="num" data-edit-id="stat-value">10 min</strong><span data-edit-id="stat-label">Overlap at every shift change</span></div></div></section>
```

## 7. Avoid vs. say instead (`concern-scenario`)

`h2` on two lines + one-line situation `.lead`. `.say-row` holds two equal cards (columns 1–6 and 7–12) from y 320px to the bottom content line: small icon + label at the top, a ≤ 10-word quote at 33px at the bottom. The better answer is the navy card. Full situation and the four recovery steps go in the notes.

```html
<section class="slide concern" data-slide-id="concern-scenario"><!--DECOR--><div class="body-wrap"><!--BRAND--><div class="concern-head"><h2 data-edit-id="title">When a guest<br>raises a concern</h2><p class="lead" data-edit-id="lead">22:40. A family booked twin beds and found one double.</p></div><div class="say-row"><article class="say-card avoid"><p class="say-top label"><svg class="icon" …lucide…/><span data-edit-id="avoid-label">Avoid</span></p><p class="quote" data-edit-id="avoid">“That’s how it was booked. Nothing I can do.”</p></article><article class="say-card better"><p class="say-top label"><svg class="icon" …lucide…/><span data-edit-id="better-label">Say instead</span></p><p class="quote" data-edit-id="better">“I’m sorry. A twin room, or a rollaway in fifteen minutes?”</p></article></div></div></section>
```

## 8. Big figure + three standards (`quality-review`)

Columns 1–5: `h2` + `.lead` at the top, `.quality-figure` (115px number + short caption) on the bottom content line. Columns 7–12: `.rows` with three equal ruled rows (label + one line) from y 224px to the bottom content line. No tables; put a full standards matrix in the notes or a handout.

```html
<section class="slide quality" data-slide-id="quality-review"><!--DECOR--><div class="body-wrap"><!--BRAND--><div class="quality-copy"><h2 data-edit-id="title">Quality you<br>can observe</h2><p class="lead" data-edit-id="lead">Each standard names what good looks like and who checks it.</p></div><div class="quality-figure"><strong class="num" data-edit-id="figure-value">3</strong><span data-edit-id="figure-label">Checks the shift lead runs weekly</span></div><div class="rows"><div class="row"><h3 data-edit-id="q1-title">Greeting</h3><p data-edit-id="q1-text">Acknowledged within sixty seconds.</p></div><div class="row"><h3 data-edit-id="q2-title">Handover</h3><p data-edit-id="q2-text">Every open item confirmed aloud.</p></div><div class="row"><h3 data-edit-id="q3-title">Follow-up</h3><p data-edit-id="q3-text">Closed in the agreed time and channel.</p></div></div></div></section>
```

## 9. Closing — arch window (`closing`)

Columns 1–6: `h2` 69px, a short `.lead`, and three `.rows` next steps on the bottom content line. Columns 8–12: `.closing-art` in an arch (radius = half its width) that bleeds off the bottom, with an offset `.arch-line` outline behind it.

```html
<section class="slide closing" data-slide-id="closing"><!--DECOR--><div class="body-wrap"><!--BRAND--><div class="closing-copy"><h2 data-edit-id="title">Make the next shift a good one.</h2><p class="lead" data-edit-id="lead">Prepare. Welcome. Follow through.</p></div><div class="rows"><div class="row"><h3 data-edit-id="n1-title">Before your shift</h3><p data-edit-id="n1-text">Read the log and tonight’s contacts.</p></div><div class="row"><h3 data-edit-id="n2-title">At the desk</h3><p data-edit-id="n2-text">Greet within a minute; name the next step.</p></div><div class="row"><h3 data-edit-id="n3-title">At handover</h3><p data-edit-id="n3-text">Confirm every open item aloud.</p></div></div><span class="arch-line" aria-hidden="true"></span><img class="photo closing-art" data-edit-id="service-art" src="IMAGE_DATA_URI" alt="A sunlit hotel lobby with a guest checking in at the desk" /></div></section>
```

## Composition checks

- Inspect every page at 1280x720: no clipping, no text over busy image areas, nothing with text below the bottom content line.
- Count words per slide (excluding notes and numbers): ≤ 45, and fewer is better.
- Each picture appears once; reuse a crop only via `object-position`.
