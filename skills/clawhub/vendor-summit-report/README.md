# Vendor Summit Report

Turn a vendor's flagship data/AI conference into an executive-grade deep-dive report — three aligned
deliverables, one shared set of facts, a fixed analytical structure, and a reading layout that people
actually finish.

Built for events like Snowflake Summit, Databricks Data+AI Summit, Microsoft Build, Google Cloud Next
and AWS re:Invent. The reusable asset is the **structure and the reading layout**; the analysis is
always derived fresh from the conference being reported on.

---

## What it produces

| Deliverable | Role | Format |
|-------------|------|--------|
| `report.html` | Primary reading experience | Single self-contained light-theme page, fixed nav, collapsible tables, scroll reveal |
| `report.md` | Master copy for archiving and reuse | Same 8 sections, same figures, Markdown primitives |
| `push.md` | Short read for enterprise chat | Plain text, `▍` section markers, byte-budgeted by content density |

All three must agree on the same figures, the same cases and the same caveats — enforced by a
cross-file key-string count at the end of every revision round, not by eye.

## Fixed 8-section structure

| # | Section | What goes in it |
|---|---------|-----------------|
| 01 | Core judgment | One-sentence thesis, strategic premise, four takeaways, key-figure strip, data-provenance note |
| 02 | Specific observations | 4–5 pure insights with no product parameters |
| 03 | Product panorama | Five strategic products with numbers and verified GA / preview status, plus a collapsible list of the rest |
| 04 | Customer evidence | 4–5 production cases, labelled vendor/customer-reported |
| 05 | Competitive landscape | Comparison table, convergence judgment, home turf vs away game, strengths and risks |
| 06 | Buyer recommendations | The So-What: role-based actionable judgments |
| 07 | Industry extension | The industry-level question this conference actually raised, plus open questions |
| 08 | Summary | One-screen wrap-up, short / medium / long-term judgments, one planning assumption |

Sections 05 and 07 carry **content, not template**. An analytical framework belongs to the conference
that produced it. For a different vendor, discard the old framing and derive a new one — a different
angle beats a forced fit.

## Analyst-house standards

These four are what separate an analyst note from a conference recap. Drop any one and the report falls
back to vendor-friendly coverage.

1. **State, don't instruct.** No imperative or preachy sentences, no meta-commentary, no thinking
   traces. Give the conclusion and the evidence; let the facts carry it.
2. **Vendor data carries a caveat.** Any performance or scale figure from the vendor or its customers
   is marked *vendor-reported / customer-reported* plus *not independently validated*, with a
   recommendation to verify on the buyer's own workload. Never quote an official "significantly better
   than competitor X" bare.
3. **The So-What is mandatory.** A dedicated buyer-recommendations section covering four roles: data
   platform lead, AI platform lead, procurement, competing vendors.
4. **Forecasts carry a year and a confidence level.** No absolutes. One explicit Strategic Planning
   Assumption in the summary.

## Reading layout contract

Layout here is a checkable contract, not a matter of taste. Every entry must satisfy the three-part
form — **judgment headline + lead + bullet points**:

- `.card-h` judgment headline — must stand alone as a judgment, not a noun phrase, no trailing period
- `.lead` — background and facts, two to four lines
- `.pts li` — parallel evidence, one to two lines each

Components: `.card` / `.card-num` / `.card-h` / `.lead` / `.pts` / `.num` / `.pull` / `.pull-lead` /
`.judg` / `.lim` / `.lim-t` / `.note` / `.badges .badge` (`.b-ga` / `.b-prev` / `.b-arch`) / `.flow` /
`.swot` / `.layer-stack` / `.buyer-grid` / `.spa` / `.q-item`.

Two criteria that get misused most often:

- **`.layer-stack`** is only for layers with an **inclusion or dependency** relation. Parallel or
  competing participants belong in `.cmp-table` or `.swot`.
- **`.pull` vs `.judg`** — `.pull` states one entry's conclusion, `.judg` is a section-level judgment.
  Do not stack both in the same block.

Anti-patterns that trigger rework: a bare paragraph over ~200 characters; a `.card-h` written as a noun
phrase; every item turned into a card; product figures leaking into the observation layer; a bullet
point longer than two lines.

## Workflow

13 steps, deterministic and LLM steps marked:

1. `[Deterministic]` Confirm the event and the reporting window
2. `[LLM]` Research — announcements, GA/preview status one by one, financial backdrop, customer cases, competitor moves, analyst commentary
3. `[LLM]` Core judgment plus data-provenance note
4. `[LLM]` Observations — 4–5 insights, stated not instructed
5. `[LLM]` Product panorama with status chips and a collapsible table
6. `[LLM]` Buyer recommendations across the four roles
7. `[LLM]` Industry extension plus open questions
8. `[LLM]` Summary and one Strategic Planning Assumption
9. `[Deterministic]` Generate the three deliverables, then run the cross-file sync check
10. `[LLM]` Layout pass on the HTML — split and emphasize only, never rewrite
11. `[Deterministic]` Mechanical review — layer separation, caveats, numbering, red-line quotas
12. `[LLM]` Reader-fit review with a positioning lock and 3–4 representative roles
13. `[Deterministic]` Deliver, with channel confirmation before any live push

## Installation

```bash
# ClawHub
clawhub install vendor-summit-report
```

Or copy the folder into your skills directory:

```
~/.workbuddy/skills/vendor-summit-report/
  SKILL.md
  templates/
    report-template.html
    report-template.md
    wecom-template.md
```

No binaries or external services required. Research uses ordinary web search and page fetches.

## Quick start

```
/vendor-summit-report
```

Or just describe the task in natural language:

- "Snowflake Summit 2026 的深度专题报告"
- "按上次那个结构，做一份 Databricks Data+AI Summit 的报告"
- "Use the same structure as last time for Google Cloud Next"

The skill will confirm the event and window first, then research, write, lay out, review and deliver.

## Repository layout

```
SKILL.md                       full workflow, standards, hard rules, verification checklist
templates/report-template.html light-theme HTML with the complete reading-component stylesheet
templates/report-template.md   Markdown master copy, 8 sections
templates/wecom-template.md    enterprise-chat push version with byte-budget tiers
```

The templates are a completed report used as a **structural and visual worked example**. Reuse the CSS,
the reading components, the section skeleton and the navigation logic. Replace every vendor name,
product, figure, case and insight, plus the analytical frameworks of sections 05, 06 and 07.

## Hard rules

1. Structure is reusable; content is not
2. Observation layer and product layer are strictly separated
3. Every vendor-sourced figure carries a caveat
4. Buyer recommendations are mandatory, covering four roles
5. Forecasts carry a year and a confidence level
6. No meta-commentary, no imperatives
7. No bare paragraph over ~200 characters
8. The three formats must agree, verified by a key-string count
9. Section numbering must be self-consistent
10. The push version never drops the buyer recommendations

## License

MIT
