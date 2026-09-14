---
name: vendor-summit-report
slug: vendor-summit-report
displayName: Vendor Summit Report
version: 1.0.0
description: "Build an executive-oriented deep-dive report for a major data/AI vendor conference — Snowflake Summit, Databricks Data+AI Summit, Microsoft Build, Google Cloud Next, AWS re:Invent. Ships three aligned deliverables (light-theme HTML, full Markdown, enterprise-chat push version) across a fixed 8-section structure held to analyst-note standards — state-don't-instruct, vendor-data caveats, role-based buyer recommendations, and confidence-tagged planning assumptions. Use it when the user asks for a 深度专题报告 / 大会报告 / summit report on a named event, or wants a previous summit report's structure repeated for a new conference."
description_zh: "厂商大会深度专题报告生成器——面向企业决策者的三口径交付（淡色 HTML + 完整 Markdown + 企业 IM 速读版），固定 8 段结构，遵循分析师机构标准（只陈述不发指令、厂商数据加 caveat、分角色买方建议、带置信度与年份的预测）；可复用的是结构与版式，分析内容必须从本次大会重新提炼。触发词：深度专题报告、大会报告、厂商大会报告、summit report、vendor summit deep dive、conference report、按上次那个结构做报告。"
description_en: "Vendor summit deep-dive report"
license: MIT
read_when:
  - "user asks for a deep-dive 专题报告 / summit report on a vendor conference"
  - "user says 按上次那个结构做 / use the same structure as last time"
  - "user names a vendor event and wants an analyst-style written report with buyer guidance"
not_for:
  - "daily or weekly news briefings (use a daily-brief skill instead)"
  - "vendor marketing collateral, keynote scripts, or product launch copy"
  - "generic conference recaps with no analytical or buyer-facing requirement"
metadata:
  openclaw:
    tags:
      - industry-research
      - analyst-report
      - conference-analysis
      - competitive-intelligence
      - executive-briefing
      - html-report
      - content-production
tags: [industry-research, analyst-report, conference-analysis, competitive-intelligence, executive-briefing, html-report, content-production]
---

# Vendor Summit Report

Produce a deep-dive written report on a single vendor's flagship conference, aimed at an industry-insider /
executive reader, and ship it in three formats that share one set of facts: a light-theme HTML page, a full
Markdown master copy, and a short enterprise-chat push message.

The **structure and visual system are the reusable asset**. The **content — insights, analytical frameworks,
industry extension — must be derived fresh from the conference being reported on**. Never transplant a previous
report's analytical framing into a new vendor's report.

## When to use

Trigger when any of these hold:

- The user asks for a "深度专题报告" / "专题报告" / "summit report" / "大会报告" on a vendor event.
- The user says something like "等 X 大会过后用这个/这套做报告" or "按上次那个结构做".
- A prior report of this class exists and the user wants the same structure reproduced for a new conference.

Do not trigger for daily news briefings, marketing collateral, or generic recaps with no analytical requirement.

## Fixed 8-section structure

| # | Section | Content | Visual form |
|---|---------|---------|-------------|
| 01 | Core judgment | One-sentence thesis + strategic premise + 4 takeaways + key-figure strip + **data-provenance note** (one vendor caveat sentence) | verdict card + takeaway grid + fact strip + `.note` |
| 02 | Specific observations | 4-5 **pure insights** (how to read it / what it means), no product parameters, no imperative or preachy sentences | `.card` × N: `.card-num` ("Observation 01…N") + `.card-h` judgment headline + `.lead` + `.pts`, conclusion line as `.pull` |
| 03 | Product panorama | 5 strategic products with numbers, each tagged GA / Public Preview / Private Preview / planned + remaining announcements in a collapsible table + product-stack layering | `.card` (`.badges` status chips + `.card-h` + `.lead` + `.pts` + `.lim`) + `<details>` table + `.layer-stack` |
| 04 | Customer evidence | 4-5 production cases, section head tagged "(vendor/customer-reported)" + analyst note | `.customer-grid` + `.info-box` analyst note containing `.pts` |
| 05 | Competitive landscape | Comparison table + convergence judgment + **home turf vs away game** + strengths and risks | `.cmp-table` + `.comp-row` (strengths/risks as a `.swot` two-column block) |
| 06 | **Buyer recommendations (the So-What)** | **Role-based** actionable judgments: data platform lead / AI platform lead / procurement / competing vendors | `.buyer-grid` × 4 (`.brole` + `.bjudg` judgment line + `.pts`) |
| 07 | Industry extension | The **industry-level question this conference actually raised** (angle varies by event) + 2-4 open questions | `.pull-lead` + `.pts` + `.judg` + `.cmp-table` or `.layer-stack` as the proposition requires + `.q-item` (qnum + qh + p) |
| 08 | Summary | One-screen wrap-up + short / medium / long-term judgments + **one Strategic Planning Assumption with a year and a confidence level** | `.summary-hero` + `.pts` + `.pull` + `.judgment` grid + `.spa` |

Two rules that are easy to get wrong:

- **Sections 05 and 07 carry content, not template.** A framework such as a "data gravity" thesis or a "multi-layer
  governance stack" belongs to the conference that produced it. For a different vendor, discard the old framing and
  derive a new extension angle from what this conference actually proposed. A different angle beats a forced fit.
- **Section 05 must include a "home turf ≠ away game" layer.** A vendor's advantage in its home market does not
  transfer to another market without additional evidence. Without this layer the section degenerates into restating
  the vendor's own positioning as a conclusion.

## Analyst-house standards

These four turn a conference recap into an analyst research note. Missing any one of them drops the report back to
vendor-friendly coverage.

1. **State, don't instruct.** No imperative or preachy sentences; do not coach the reader on how to read.
   - Bad: "发布与规划必须分清" / "评估这套叙事需先分清" / "must be distinguished first"
   - Good (declarative): "Three announcements land now; the platform roadmap item lands later. The two have
     different delivery horizons."
   - Also strip meta-commentary and thinking traces: "the first thing to clarify…", "this is the most easily
     overlooked / strategically highest statement", "the evidentiary basis for the observations above",
     "this confirms: …" (that one makes the judgment for the reader). Give the conclusion and the evidence; let the
     facts carry it.
2. **Vendor data needs a caveat.** Any performance or scale figure (2-6x, 67%, millions of QPS, account counts)
   sourced from the vendor or its customers must be marked `vendor-reported` / `customer-reported` plus
   "not independently validated", with a recommendation to verify on the buyer's own workload. Never quote an
   official "significantly better than competitor X" bare. Put a one-sentence data-provenance note in the core
   judgment area, tag the customer-evidence section head "(vendor/customer-reported)", and add an analyst note.
3. **The So-What is mandatory.** A dedicated "Buyer recommendations" section with role-based, actionable
   judgments: data platform lead / AI platform lead / procurement / competing vendors. Typical judgments: don't
   put non-GA capabilities on a production critical path, run a POC first; select interfaces by cross-platform
   standard to avoid single-vendor lock-in; require reproducible benchmarks in the contract; when competing head-on
   is uneconomic, attack a dimension where the other side has not built a moat.
4. **Forecasts carry a confidence level and a year.** Ban absolutes ("inevitably", "certainly", "unshakeable",
   "logically consistent", "decisively narrowing"). Use a **Strategic Planning Assumption**: "By 20XX, the share of
   Y in scenario X rises; confidence: medium-high." Place one explicit SPA in the summary.

## Reading layout contract

Most of a report's value depends on whether the reader actually reads it. This section turns layout from an
aesthetic preference into a checkable contract.

### Three-part entry (every item must satisfy it)

**Judgment headline + lead + bullet points.** If one of the three is missing, the item is not finished.

- **Judgment headline** (`.card-h`): must stand on its own and be a judgment, not a noun phrase. No trailing period.
  - Good: "The only thing localized was the storyteller, not the data foundation"
  - Bad: "Product panorama" / "Competitive landscape" / "On the ontology architecture"
- **Lead** (`.lead`): background and facts, 2-4 lines, lighter weight.
- **Bullet points** (`.pts li`): one to two lines each, scannable. Use a list for parallel points; never pack them
  into a run-on paragraph.

### Component inventory

| Component | Class | Purpose | When |
|-----------|-------|---------|------|
| Item card | `.card` (with `.card-num`) | Shared skeleton for observation, product and buyer items | When a judgment stands as its own entry |
| Judgment headline | `.card-h` | Conclusion first | Reading the headline alone gives the full judgment |
| Lead | `.lead` | Background and facts | Opening of an entry |
| Bullet points | `.pts > li` | Parallel facts / evidence, square markers | Scannable at a glance |
| Numeric emphasis | `.num` | Tabular-nums, bold | Product and fact layer only |
| Pull block | `.pull` / `.pull-lead` | The single sentence carrying the judgment; `.pull-lead` for a section opener | The entry's conclusion |
| Standalone judgment line | `.judg` | A judgment not attached to a card | Section-closing conclusion |
| Boundary strip | `.lim` + `.lim-t` | Limits, risks, scope caveats | When a qualification must be explicit |
| Footnote | `.note` | Data provenance, non-comparability statements | Where caveats cluster |
| Status chips | `.badges > .badge` (`.b-ga` / `.b-prev` / `.b-arch`) | GA / preview / architecture layer | Replaces parenthetical prefixes |
| Flow strip | `.flow > .flow-step` + `.flow-arrow` | Steps, ladder, pipeline | When order or progression matters |
| Strengths vs risks | `.swot` + `.swot-col.pro` / `.con` | Two-column contrast | Turns a comma-spliced sentence into items |
| Layer stack | `.layer-stack > .layer` | Layers with an **inclusion or dependency** relation | See the criteria below |
| SPA block | `.spa` | Forecast with year and confidence | One per report, in the summary |

### Component criteria (the two that get misused)

- **`.layer-stack` boundary.** Use it only when the layers have an **inclusion or dependency** relation (an upper
  layer depends on what the lower layer provides). When the participants are **parallel or competing**, use
  `.cmp-table` or `.swot` instead. If a cross-vendor ecosystem layering is the analyst's own synthesis rather than
  the vendor's own description, say so in the same passage.
- **`.pull` vs `.judg`.** `.pull` belongs to a specific entry and states that entry's conclusion. `.judg` is a
  section-level judgment that belongs to no single entry. Do not stack both in the same block.

### Anti-patterns (any of these means rework)

- A bare paragraph longer than ~200 Chinese characters.
- A `.card-h` written as a noun phrase.
- Turning every item in a section into a card, producing a wall of cards; with fewer than three items, use a
  paragraph plus bullet points.
- A `.num` carrying a product figure inside the observation layer.
- A bullet point longer than two lines (it should be split, or moved into the lead).

## Workflow

### Step 1: [Deterministic] Confirm the event and the window

- Identify the exact conference, its host vendor, its date(s), and the reporting window.
- If two events of the same class fall in the window, confirm with the user which one this report covers.

### Step 2: [LLM] Research

Collect, using web search and page fetches:

1. Every product announcement, with GA / preview status verified one by one.
2. Financial backdrop: the vendor's most recent reported quarter.
3. Customer cases with business-outcome numbers, recording whether each figure is vendor-reported or
   customer-reported.
4. Competitor moves in the same period.
5. Analyst-house commentary.

Press-report discipline: verify each item's original publication date falls inside the window; cross-verify
single-source claims. **Prefer on-site coverage over pre-event previews** — a preview often blurs "next-generation
version" into vagueness, while the on-site talk draws the line between "shipped" and "on the roadmap". A preview may
name a future major version while the keynote clarifies that the current minor release is the shipped one and the
major is planned.

### Step 3: [LLM] Core judgment

- Answer in one sentence: what is this vendor betting on?
- Produce four takeaways.
- Add a one-sentence **data-provenance note** in the core judgment area (conference performance and scale figures
  are vendor- or customer-reported and not independently validated).

### Step 4: [LLM] Observations

- Write 4-5 observations. Each carries one insight, stated as a judgment, stripped of product parameters.
- Each observation also needs its **judgment headline** (standalone-readable) plus lead and bullet points.
- **State, don't instruct.** No "must be distinguished", "must first clarify", "should note", and no meta-commentary
  or thinking traces.

### Step 5: [LLM] Product panorama

- Pick 5 strategic products and write them up with numbers; tag each with GA / Public Preview / Private Preview /
  planned using `.badges` chips rather than a parenthetical prefix.
- Remaining announcements go into a collapsible table.
- If a genuine inclusion relation exists between stack layers, render it with `.layer-stack`.

### Step 6: [LLM] Buyer recommendations

- Cover the four roles: data platform lead, AI platform lead, procurement, competing vendors.
- Content follows the actual conference, but the recurring logic holds: no production commitment on non-GA
  capabilities; select interfaces by common standard to avoid lock-in; require reproducible benchmarks in the
  contract; for competitors, attack a dimension where the other side has not built a moat.
- Each role opens with a judgment line (`.bjudg`) followed by 2-4 bullet points.

### Step 7: [LLM] Industry extension

- Ask: what industry-level question did this conference actually raise? A standards contest, a paradigm shift, an
  ecosystem land grab, or some capability becoming a new threshold? Extend along that line.
- Use `.layer-stack` only when the proposition really is a layered structure with dependencies. For parallel or
  competing participants use `.cmp-table` or `.swot`.
- Add 2-4 open questions that stay genuinely open.

### Step 8: [LLM] Summary and SPA

- One-screen wrap-up plus short / medium / long-term judgments.
- One Strategic Planning Assumption with a year and a confidence level. Ban absolutes.

### Step 9: [Deterministic] Generate the three deliverables

- Start from `templates/report-template.html`, replace content, keep the CSS, navigation logic, reveal script and
  the full set of reading components.
- Start from `templates/report-template.md` for the full Markdown master copy.
- Start from `templates/wecom-template.md` for the push version.
- **Three-format sync law:** finishing the Markdown does not mean the facts agree. At the end of every revision
  round, run a cross-file key-string count comparison — `<h1>` title and subtitle, hero subtitle, deck line, key
  facts table, table figures, caveat sentences — counting the same string in all three files. A mismatch means a
  missed edit.

### Step 10: [LLM] Layout pass on the HTML

- Split the finished prose per the reading layout contract: identify each judgment sentence and promote it to
  `.card-h`; background facts to `.lead`; parallel evidence to `.pts`; the conclusion sentence to `.pull`; caveats
  to `.lim` or `.note`.
- **This step only splits and emphasizes. It does not rewrite text.**
- After the pass, run two checks: (a) structure balance — for each of `section` / `div` / `article` / `ul` / `li` /
  `p` / `table` / `tr` / `td` / `strong` / `b` / `span` / `details` / `h3`, opening count equals closing count;
  (b) zero content loss — dump a plain-text snapshot before the pass, diff character-level after, and classify every
  difference into one of four buckets: quote normalization, punctuation adjusted by re-blocking, new structural
  tags, known corrections. A fifth bucket means roll back and investigate.

### Step 11: [Deterministic] Mechanical review

- Check the observation layer for product figures that leaked out of the product layer.
- Check for meta-commentary, imperative sentences and absolutes.
- Check that every vendor figure carries a caveat, the buyer-recommendations section exists, and the SPA carries a
  confidence level.
- Check that every `.card-h` is a judgment and no bare long paragraph remains.
- Check section numbering: the HTML comment number and the visible `.sec-no` must match.
- Preview in a browser: the first screen is the core judgment, not navigation.
- Grep for leftovers, e.g. `必须分清|需先分清|印证：|必然|难撼|逻辑自洽|决定性`.
- Red-line quotas per report: em-dash `——` at most 5 occurrences; "不是…而是" / "而非" contrast constructions at
  most 3. Note that in HTML these dashes often sit next to `</strong>` or `</span>`, so Markdown and HTML cannot
  share one set of plain-text replacement anchors — dump the hits per file and decide each one individually.

### Step 12: [LLM] Reader-fit review (recommended)

Mechanical review guarantees "nothing is violated"; reader-fit guarantees "the reader actually understands".

- **Positioning lock first**: genre / primary reader / reading task / central proposition / deliberately excluded
  material / depth. This lock is the basis for grading later.
- Choose 3-4 representative roles. For this class, **exclude** investors, media editors and general readers as
  incompatible with the positioning. Prefer: enterprise decision-maker, domain expert, runtime and governance
  engineer, cross-domain industry reader.
- Put the same five questions to each: (1) What is the central proposition in one sentence? (2) Which passage did
  you skip first? (3) Which claim felt under-evidenced? (4) Which number would you not cite? (5) What will you do
  after reading, if anything?
- Grade by positioning compatibility: must-fix (leaving it makes the reader adopt a wrong belief; usually a
  positioning risk) / suggested / optional / reject-park (incompatible with the positioning, parked with a stated
  reason).
- Record conflicts explicitly rather than splitting the difference.
- Limit the revision scope: fix must-fix and suggested only. **Revisions may not rewrite content** — only split,
  emphasize, reorder, or add caveats.
- Priority order: factual correctness → positioning integrity → core comprehension → technical depth → elegance →
  distribution preference.
- Recurring consensus blockers seen in practice: the assertion strength in tables and headings exceeds the wording
  in the body and observations, and readers adopt the harder side; when multiple formats ship in parallel the caveat
  lives in only one of them; a competitive section that only restates vendor positioning gets read as a conclusion.
- Save the review document next to the report.

### Step 13: [Deterministic] Deliver

- Deliver the three files, HTML first.
- If the workspace already has a publish or delivery script, reuse its pattern rather than writing a new one.
- Deploy the HTML to a dedicated path so it does not overwrite other routes on the same site.
- **Confirm the target channel with the user before pushing to any live group or public page.**

## Hard Rules

> These cannot be violated.

1. **Structure is reusable; content is not.** Never carry a previous report's analytical framework into a new
   vendor's report. Derive the extension angle from the conference being covered.
2. **Observation layer and product layer are strictly separated.** The observation layer states how to read
   something and carries no product figures; figures live only in the product layer.
3. **Every vendor- or customer-sourced figure carries a caveat** — vendor/customer-reported plus not-independently-
   validated — with no bare "significantly better than competitor X".
4. **The buyer-recommendations section is mandatory** and must cover the four roles.
5. **Forecasts carry a year and a confidence level.** No absolutes.
6. **No meta-commentary, no imperative or preachy sentences.** No "our report", "this report argues", "must first
   clarify", "this confirms".
7. **No bare paragraph longer than ~200 characters.** Every entry uses judgment headline + lead + bullet points.
8. **Three formats must agree** on the same figures, the same cases and the same caveats, verified by a cross-file
   key-string count.
9. **Section numbering must be self-consistent** — HTML comment number equals visible `.sec-no`.
10. **The push version must never drop the buyer recommendations.** When over budget, cut the customer evidence
    first, then the open questions.

## Failure Handling

| Scenario | Action |
|----------|--------|
| The conference date or host vendor is ambiguous | Stop and ask which event is in scope before researching |
| GA / preview status cannot be verified from a primary source | Do not guess; either label it as unconfirmed in the report or drop the item |
| A key figure appears in only one secondary source | Cross-verify; if unverifiable, attribute it inline and add a caveat, or omit it |
| A vendor figure has no test conditions disclosed | Keep the figure but add an explicit caveat that the conditions were not published and the number is not reproducible |
| The observation layer has absorbed product figures | Move the figures to the product layer; the observation layer states the judgment only |
| The HTML was regenerated and a tag count is unbalanced | Roll back to the last balanced version and redo the layout pass; do not patch by hand |
| The layout pass changed wording | Restore the original wording; the pass may only split and emphasize |
| The push version exceeds the byte budget | Cut in this order: customer evidence, then open questions. Never cut buyer recommendations |
| Two formats disagree on a figure or a caveat | Re-run the cross-file key-string count, fix the stale file, then re-verify |
| The reader-fit review reports a positioning-level conflict | Resolve at the positioning level, not by adding disclaimers |

## Output Format

Three files per report, one shared set of facts.

### 1. HTML (primary, light theme)

- Single self-contained page, light background with white cards and a blue accent, optional secondary accents.
- Fixed top navigation with two-character labels; compact hero; no large table-of-contents card.
- Scroll-reveal animation and active-section highlighting.
- All reading components from the layout contract available in the stylesheet.
- Status chips instead of parenthetical status prefixes.
- Collapsible tables folded by default.

### 2. Markdown (master copy)

- Same 8 sections, same order, same figures.
- Judgment headline plus bullet points, expressed with Markdown primitives (bold judgment line, then a list).
- Tables where the HTML uses them.

### 3. Push version (short read)

- Plain-text title plus short paragraphs. No emoji, no decorative symbols, no horizontal rules, no keycap numbers,
  no star ratings.
- Section marker: `▍`.
- Separator is a full-width colon `：`; never a vertical bar `｜`.
- No Markdown bold syntax — write complete sentences.
- Byte budget by content density, hard ceiling 4,096 bytes, measured as
  `len(text.encode('utf-8'))`, not character count:
  - single-launch event or one product line: ≤ 2,500 bytes
  - typical conference, two product lines or one strategic concept: ≤ 3,500 bytes
  - very high density (multiple product lines + multiple cases + role-based buyer recommendations): 3,500-3,900 bytes
- Over budget, cut in this order: customer evidence, then open questions. Never cut buyer recommendations.
- Role-based recommendations are the byte sink: keep each role to 40-60 characters; anything longer belongs in the
  HTML.
- Required sections: core judgment (with vendor caveat), observations, product panorama, competitive landscape,
  **buyer recommendations**, open questions, summary (with SPA). Sections may be merged or compressed but not
  deleted.
- Final line is fixed: "完整报告见 HTML 附件。"

## Templates

- `templates/report-template.html` — full light-theme HTML template: CSS variables, fixed navigation, fact strip,
  verdict card, the complete reading-component set, layer stack, scroll reveal, active-nav script. Its header
  comment carries four blocks: reuse list, mandatory replacements, reading contract, component criteria.
- `templates/report-template.md` — the Markdown master copy, 8 sections.
- `templates/wecom-template.md` — the push version, `▍` section markers, full-width colon separator, byte-budget
  tiers.

The three templates are a completed report used as a **structural and visual worked example**. Reuse the CSS, the
reading components, the section skeleton, the navigation logic and the writing discipline. Replace every vendor
name, product, figure, case and insight, plus the analytical frameworks of sections 05, 06 and 07.

## Pitfalls

- **Forcing an old framework** (most serious): transplanting a previous report's analytical framing into a different
  vendor's report to fill section 07. That framing is content, not template.
- **Observation and product layers repeating**: the most common defect. If the observation writes the figures, the
  product section writes them again, and the reader reads it twice.
- **Wall-of-text**: a continuous 200-300 character paragraph. This is the main reason a report looks professional
  and nobody finishes it.
- **Judgment headline written as a noun phrase**: wastes the line most likely to be read.
- **Section numbering off by one**: after any restructure, verify each section's comment number against the visible
  `.sec-no`.
- **Updating only one of the three formats**: the Markdown is fixed but the HTML `<h1>` subtitle, hero subtitle and
  table figures still hold the old wording. Always run the cross-file count at the end.
- **Table wording stronger than body wording**: the table says "integrated" while the body says "acquisition just
  closed", and the reader believes the table. Assertion strength must match across layers.
- **Navigation eating the first screen**: no standalone table-of-contents card, no tall hero.
- **Push version over the byte ceiling**: measure; do not eyeball. Cut in the stated order.
- **Vertical bar as separator in the push version**: use the full-width colon.
- **Product status guessed**: GA / Public Preview / Private Preview / Alpha must be verified one by one.
- **Vendor figures quoted bare**: credibility collapses.
- **Buyer recommendations missing**: the report falls back to being a conference recap.
- **Forecasts using absolutes**: downgrade to a year-and-confidence SPA.
- **Competitive section missing home turf vs away game**: the vendor's home-market advantage gets read as universal.
- **Competitive section duplicating the observations**: if the observations already covered data gravity or model
  commoditization, the competitive section must take a different angle (for instance, how the three vendors' data
  shapes differ).
- **Using `.layer-stack` for parallel relationships**: it implies architectural inheritance that does not exist.

## Verification

- [ ] Section order is judgment → observations → products → cases → competition → **buyer recommendations** →
      industry → summary (8 sections), with `.sec-no` 01-08 and no numbering off by one
- [ ] Section 07's framework comes from this conference, with no residue of a previous report's framing
- [ ] Section 05 includes a home turf vs away game layer
- [ ] Insights, propositions and cases are all from this conference, with no residue from a previous report
- [ ] The observation layer contains no product figures and no `.num`
- [ ] Layout contract met: every entry has judgment headline + lead + bullet points; every `.card-h` is a standalone
      judgment rather than a noun phrase; no bare paragraph over ~200 characters
- [ ] Components used correctly: statuses as `.badges`; `.layer-stack` only for inclusion or dependency relations;
      `.pull` and `.judg` not stacked
- [ ] Layout pass checks passed: tag counts balanced; character-level diff fully classified into the four buckets
- [ ] No meta-commentary, no imperative sentences, no absolutes
- [ ] Red-line quotas: `——` at most 5; contrast constructions at most 3
- [ ] Every vendor or customer figure carries a caveat; no bare "significantly better than competitor X"
- [ ] A standalone buyer-recommendations section exists with all four roles, each with a judgment line plus bullets
- [ ] The summary contains one SPA with a year and a confidence level
- [ ] The HTML first screen is the core judgment, not navigation
- [ ] The push version measures inside its density band, uses `▍` markers and a full-width colon, carries the vendor
      caveat and the buyer recommendations, and contains no imperative sentences or absolutes
- [ ] The three formats agree on figures, cases and caveats, confirmed by the cross-file key-string count
- [ ] If a reader-fit review was run, the review document is saved and every must-fix item is resolved, with parked
      items recorded
- [ ] Every product's GA / preview status verified
- [ ] HTML previews correctly: collapsible tables folded, reveal animation and active navigation working

## 中文说明

本 skill 面向厂商大会（Snowflake Summit、Databricks Data+AI Summit、Microsoft Build、Google Cloud Next、
AWS re:Invent 等）生成面向行业内参与高管视角的深度专题报告，一次产出三个口径一致的版本：淡色 HTML、
完整 Markdown、企业 IM 速读版。

复用的是**结构骨架、视觉风格与写作纪律**；**洞察、分析框架与行业延伸角度必须从本次大会的实际内容重新
推导**，不得把上一份报告的具体框架（例如某家的"数据重力论"或"多层治理生态"）硬塞进新报告。

四条分析师机构标准为硬性：只陈述不发指令、厂商数据必须加 caveat、必须有分角色买方建议、预测必须带年份
与置信度。
