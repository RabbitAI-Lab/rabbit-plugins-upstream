> Pages are built from the style kit's recipes in `references/style-kit.json` (SKILL.md Workflow step 4); keep the composition rules in this file as design guidance. The HTML snippets below only illustrate each archetype's geometry and hierarchy; do not paste them as slides. Their `<section>` wrappers and `data-*` attributes come from the retired hand-written format and are not required.

# Mint Marker layout library (v3)

## Hard rules (read first)

1. **Word budget.** Headline at most 7 words (cover title at most 5). At most one supporting line of 18 words or fewer. At most 3 items per slide; an item is a label of 3 words or fewer plus at most one line of 10 words or fewer, or a number plus a 2 to 4 word caption. No paragraphs, no text block longer than 2 lines, at most 45 words per slide excluding numbers. Put detail in `slide.notes`.
2. **Chrome.** Only the small `.brand` mark top-left on every page. No pill or tag clusters, date pills, section labels, eyebrows, folios or footer captions. Put "illustrative" or "fictional" disclaimers in the notes; a page with numbers may carry one footnote of 6 words or fewer above 634px (`.metrics-note`).
3. **Grid.** 12 columns, 77px side margins (`--mx`), 26px gutters (`--gut`), content from 79px (`--top`) to 634px (`--floor` = 86px from the bottom). Blocks align to grid edges; siblings in a row share top, height and style. Leave at least 30% of most pages empty. At most 3 content blocks per page (headline, picture, one group).
4. **No collage.** Never overlap two pictures and never float a card over a photo. Use a bleeding illustration, a clean half split or one large picture. One corner radius for the deck: 0.
5. **Cards and items.** Siblings share one style (all ruled, or all filled). Highlight one with the accent fill only, at the same size (`.phase.two`). Items hold a label, one line and an optional number. Icons only where they add meaning, all at `.ico` size and stroke.
6. **Type.** Display: Bricolage Grotesque 700, uppercase, tracking -0.035em, line height 0.94. Body: Figtree 450 to 650. Both are embedded as base64 `@font-face` in the style (`style-source.css`, carried in the kit's `contentCSS`; about 61 KB, SIL OFL 1.1); keep the `--font-display` / `--font-body` variables. Sizes on the 1280x720 page: cover title 154px, page headlines 64 to 82px, closing title 123px, ledes 19 to 20px, item labels 19px, item lines 17px (never below 17px), labels 12px tracked +0.08em, big numbers 64 to 102px with tabular figures.
7. **Color.** One accent element per paper page (the headline usually is it). Accent `.mint` pages use ink headlines. Two to four accent pages per ten slides; no dark pages.
8. **Pictures.** Every picture on at most one page; crop with `object-fit` / `object-position` only.

Pictures are `img.doodle.case-illustration.decor` (illustrations) or `img.photo-half` (photo). The example sequence is cover, statement, split, strategy, timeline, photo split, challenge, roles, targets, closing; each is a recipe in `style-kit.json`. Reorder and repeat recipes to fit the story. Every page carries the small `.brand` mark top-left.

## Cover

`.cover` (Headline in front) and the alternative `.cover-above` class (Headline above).
- `.cover-art` is a top band (358px to 1229px, 0 to 475px). `.cover-title` 154px, one line, bottom edge at 634px. `.cover-subtitle` is one `.lede` line under the brand mark (top 79px, 243px wide).
- `.cover-above` puts the title at 79px and the art below it (259 to 634px); the subtitle moves top-right.

```html
<section class="slide cover" data-slide-id="cover" data-variant="a" data-variant-label="Headline in front"><p class="brand" data-edit-id="brand">Neighborhood Lab</p><p class="lede cover-subtitle" data-edit-id="subtitle">A shared workshop for the neighborhood.</p><img class="doodle cover-art case-illustration decor" data-edit-id="case-cover" src="data:image/webp;base64,..." alt="Three neighbors building a small shelf around a shared table"><h1 class="display cover-title" data-edit-id="title">MAKE ROOM</h1></section>
```

## Statement

`.intro`: purpose or problem.
- `.intro-title` 82px, up to three lines, top-left. `.intro-art` is a full-height portrait window bleeding off the right edge (486px).
- `.intro-foot` holds one `.lede` line under a 2px rule, bottom edge at 634px, 589px wide.
- Without a picture, use `<div class="doodle intro-art image-frame decor" data-edit="off">`.

```html
<section class="slide intro" data-slide-id="why" ><p class="brand" data-edit-id="brand">Neighborhood Lab</p><h2 class="display intro-title" data-edit-id="title">GOOD IDEAS<br>NEED A PLACE<br>TO GROW.</h2><img class="doodle intro-art case-illustration decor" data-edit-id="case-why" src="data:image/webp;base64,..." alt="A neighbor with a toolbox looking into an empty room with one long work table"><div class="intro-foot"><p class="lede" data-edit-id="copy">One vacant room becomes a shared workshop for a six-week pilot.</p></div></section>
```

## Split

`.split` (Illustration left); the alternative `.split-reverse` class mirrors it.
- `.split-art` bleeds off the left edge (0 to 666px, 79 to 634px, cover crop).
- `.split-copy` column from 742px to the right margin: headline 64px at the top, `.split-points` two equal ruled items at the bottom (accent `.num` 33px, label, one line).

```html
<section class="slide split" data-slide-id="goals" data-variant="a" data-variant-label="Illustration left"><p class="brand" data-edit-id="brand">Neighborhood Lab</p><img class="doodle split-art case-illustration decor" data-edit-id="case-goals" src="data:image/webp;base64,..." alt="Neighbors presenting a repaired lamp and a completed shelf"><div class="split-copy"><h2 class="display" data-edit-id="title">A COMMON<br>GOAL.<br>ROOM TO TRY.</h2><div class="split-points"><div class="item"><p class="num" data-edit-id="num-1">01</p><h3 data-edit-id="label-1">Easy first visit</h3><p data-edit-id="copy-1">A clear welcome and someone to help.</p></div><div class="item"><p class="num" data-edit-id="num-2">02</p><h3 data-edit-id="label-2">Learn by making</h3><p data-edit-id="copy-2">A fixed lamp is a reason to return.</p></div></div></div></section>
```

## Strategy (accent page)

`.mint.strategy`: method, way of working, principles.
- `.strategy-copy` column on the left (77px to 563px): headline 72px at the top, `.item-list` of three ruled items pinned to the bottom (Lucide `.ico`, label, one line).
- `.strategy-art` fills the right side; generate it on flat mint so it merges with the page.

```html
<section class="slide mint strategy" data-slide-id="working-together" ><p class="brand" data-edit-id="brand">Neighborhood Lab</p><img class="doodle strategy-art case-illustration decor" data-edit-id="case-working-together" src="data:image/webp;base64,..." alt="A host and first-time visitor using a shared planning board"><div class="strategy-copy"><h2 class="display" data-edit-id="title">MAKE IT<br>TOGETHER.</h2><ul class="item-list"><li class="item"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true" data-edit="off"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M19 8v6M22 11h-6"/></svg><div><h3 data-edit-id="habit-1-title">Pair with a host</h3><p data-edit-id="habit-1-copy">Every newcomer works beside someone who has done it.</p></div></li><li class="item"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true" data-edit="off"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 7v7M12 7v4M16 7v9"/></svg><div><h3 data-edit-id="habit-2-title">One shared board</h3><p data-edit-id="habit-2-copy">Decisions and next steps stay visible to all.</p></div></li><li class="item"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true" data-edit="off"><path d="M2 3h20"/><path d="M21 3v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V3"/><path d="m7 21 5-5 5 5"/></svg><div><h3 data-edit-id="habit-3-title">Show and tell</h3><p data-edit-id="habit-3-copy">Five minutes to share what was made.</p></div></li></ul></div></section>
```

## Timeline

`.timeline`: phases, milestones, agenda.
- `.timeline-title` 67px top-left; `.timeline-sketch` top-right (717 to 1203px, 50 to 338px).
- `.phase-grid` three equal boxes from 374px to 634px: top rule, big `.num` (64px), label and one line at the bottom. `.phase.two` is the single accent-filled box at the same size; move the class to the phase that matters most.

```html
<section class="slide timeline" data-slide-id="timeline" ><p class="brand" data-edit-id="brand">Neighborhood Lab</p><h2 class="display timeline-title" data-edit-id="title">ONE ROOM.<br>THREE SIMPLE<br>PHASES.</h2><img class="doodle timeline-sketch case-illustration decor" data-edit-id="case-timeline" src="data:image/webp;base64,..." alt="A facilitator explaining three unlabeled workshop phases"><div class="phase-grid"><div class="phase item one"><p class="display num" data-edit-id="phase-01-number">01</p><h3 data-edit-id="phase-01-title">Listen · Week 1</h3><p data-edit-id="phase-01-copy">Ask what neighbors would actually use.</p></div><div class="phase item two"><p class="display num" data-edit-id="phase-02-number">02</p><h3 data-edit-id="phase-02-title">Make · Weeks 2–5</h3><p data-edit-id="phase-02-copy">One open workshop, every week.</p></div><div class="phase item three"><p class="display num" data-edit-id="phase-03-number">03</p><h3 data-edit-id="phase-03-title">Learn · Week 6</h3><p data-edit-id="phase-03-copy">Decide what to keep, change, or stop.</p></div></div></section>
```

## Photo split (accent page)

`.mint.photo`: resources, setting, proof.
- `.photo-copy` column on mint (77px to 563px): headline 64px at the top, three ruled items at the bottom (no icons).
- `.photo-half` is the photo, full-bleed on the right half (640px x 720px). Nothing overlaps it.

```html
<section class="slide mint photo" data-slide-id="resources" ><p class="brand" data-edit-id="brand">Neighborhood Lab</p><div class="photo-copy"><h2 class="display photo-title" data-edit-id="title">A FEW TOOLS.<br>A LOT OF<br>POSSIBILITY.</h2><ul class="item-list"><li class="item"><div><h3 data-edit-id="item-1-title">One work table</h3><p data-edit-id="item-1-copy">Six seats and a basic hand-tool kit.</p></div></li><li class="item"><div><h3 data-edit-id="item-2-title">Reusable materials</h3><p data-edit-id="item-2-copy">Offcuts, spare parts and donated supplies.</p></div></li><li class="item"><div><h3 data-edit-id="item-3-title">A safety routine</h3><p data-edit-id="item-3-copy">A two-minute walkthrough before any tool.</p></div></li></ul></div><img class="photo-half" data-edit-id="workshop-photo" src="data:image/webp;base64,..." alt="Hands collaborating on an unbranded community workshop project"></section>
```

## Challenge and response

`.challenges`: problem/response, before/after, risk/mitigation.
- `.challenge-art` top-left (0 to 666px). `.challenge-columns` two equal ruled items top-right (742px to the margin), accent label and one line at 20px.
- `.challenge-title` 90px, two lines, bottom edge at 634px.

```html
<section class="slide challenges" data-slide-id="challenges" ><p class="brand" data-edit-id="brand">Neighborhood Lab</p><img class="doodle challenge-art case-illustration decor" data-edit-id="case-challenges" src="data:image/webp;base64,..." alt="A host waving a newcomer into a calm workshop while another visitor watches"><div class="challenge-columns"><div class="challenge-card item"><span class="label" data-edit-id="left-label">The challenge</span><p data-edit-id="left-copy">A busy room feels hard to enter.</p></div><div class="challenge-card item response"><span class="label" data-edit-id="right-label">Our response</span><p data-edit-id="right-copy">A short first task. Watching counts as joining.</p></div></div><h2 class="display challenge-title" data-edit-id="title">LESS FRICTION.<br>MORE CONNECTION.</h2></section>
```

## Roles

`.objectives`: team, audiences, roles.
- Headline 67px top-left, `.gathering-art` wide across the content width (166 to 504px), `.role-grid` three equal ruled items from 518px to 634px with accent labels.

```html
<section class="slide objectives" data-slide-id="objectives" ><p class="brand" data-edit-id="brand">Neighborhood Lab</p><h2 class="display objectives-title" data-edit-id="title">EVERYONE<br>HAS A PART.</h2><img class="doodle gathering-art case-illustration decor" data-edit-id="case-objectives" src="data:image/webp;base64,..." alt="Five neighbors contributing different roles in a workshop circle"><div class="role-grid"><div class="role item"><h3 data-edit-id="role-1-title">Hosts</h3><p data-edit-id="role-1-copy">Open the door and welcome people.</p></div><div class="role item"><h3 data-edit-id="role-2-title">Makers</h3><p data-edit-id="role-2-copy">Share a skill, lead one small task.</p></div><div class="role item"><h3 data-edit-id="role-3-title">Visitors</h3><p data-edit-id="role-3-copy">Watch, ask, and try when ready.</p></div></div></section>
```

## Targets (accent page)

`.mint.metrics`: numbers, targets, results.
- Headline 72px top-left. `.metric-grid` three equal ruled columns from 382px: a 102px number and a 2 to 4 word caption. `.metrics-note` is the one short footnote, bottom edge at 634px.

```html
<section class="slide mint metrics" data-slide-id="pilot-targets" ><p class="brand" data-edit-id="brand">Neighborhood Lab</p><h2 class="display metrics-title" data-edit-id="title">SMALL START.<br>CLEAR SIGNALS.</h2><div class="metric-grid"><div class="metric"><p class="display" data-edit-id="metric-0-number">4</p><h3 data-edit-id="metric-0-title">Open workshops</h3></div><div class="metric"><p class="display" data-edit-id="metric-1-number">30</p><h3 data-edit-id="metric-1-title">First-time visitors</h3></div><div class="metric"><p class="display" data-edit-id="metric-2-number">1</p><h3 data-edit-id="metric-2-title">Shared next step</h3></div></div><p class="metrics-note" data-edit-id="note">Planning targets, not results.</p></section>
```

## Closing

`.closing`: invitation, call to action.
- `.closing-title` 123px, three stacked lines, top-left. `.closing-art` fills the right side (538px to the edge).
- `.closing-copy` one `.lede` line under a 2px rule, bottom edge at 634px.

```html
<section class="slide closing" data-slide-id="closing" ><p class="brand" data-edit-id="brand">Neighborhood Lab</p><img class="doodle closing-art case-illustration decor" data-edit-id="case-closing" src="data:image/webp;base64,..." alt="Three neighbors greeting visitors with a finished shelf"><h2 class="display closing-title" data-edit-id="title">LET'S<br>MAKE<br>ROOM.</h2><div class="closing-copy"><p class="lede" data-edit-id="copy">Bring one idea. Invite one neighbor.</p></div></section>
```
