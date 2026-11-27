---
name: content-strategy
description: Build a complete, evidence-backed content strategy for a brand, creator or business, covering audience personas, niche analysis, competitor analysis, content gaps, content pillars, platform-specific plans, funnel (Awareness, Engagement, Conversion), formats, posting frequency, KPIs and a weekly or monthly calendar. Pulls real data (YouTube Data API, Google Trends exports, search autocomplete, optional SEO connectors such as Semrush or Ubersuggest, plus WebSearch/WebFetch) so every recommendation traces back to evidence instead of guesses. Use this skill whenever the user asks for a content strategy, content plan or calendar, content pillars, audience or niche analysis, competitor content analysis, content gaps, keyword or SEO content opportunities, posting frequency, or "what should I post", even if they only say "plan my content", "social media strategy" or "make my content plan".
---

# Content Strategy

Goal: produce a strategy the user can execute and *defend*. The difference from brainstorming: every pillar, platform choice, cadence and KPI points to an evidence item (a number, a source, a date) or is openly marked as an assumption to test. Ideas without evidence are hypotheses, and the plan says so.

## Inputs

Collect briefly, assume sensibly where missing, and list the assumptions at the top of the deliverable:

- business or brand, offer, and the one goal that matters (leads, sales, subscribers, authority, awareness)
- audience guess, region and language
- platforms already used or wanted (default: pick from evidence)
- capacity: people, hours per week, budget, production skill
- existing assets: current channels, past top posts, customer questions, site (if they have Search Console or analytics data, that outranks everything below)

Ask only when the business itself is unclear. Never stall on a questionnaire.

## Evidence first: the ledger

Keep an **evidence ledger** (`evidence.csv`, columns in `references/data-sources.md`): one row per finding with an id (E1, E2, ...), source, claim, metric, date pulled and confidence. The final strategy cites ledger ids next to each decision. This is what stops the output from becoming generic advice, and it lets the user verify or update any claim later.

Read `references/data-sources.md` before collecting. It maps each question to the best source, what to do when a source is unavailable, and how to label confidence.

## Workflow

1. **Scope and plan the research.** Decide the 3 to 7 competitors or reference creators, 5 to 10 seed topics, the platforms and the time window.
2. **Collect demand data** (what people want): `scripts/research_helper.py suggest` for autocomplete keyword expansion, `trends-csv` to read Google Trends exports the user downloads, WebSearch for Reddit/forum questions, and any connected SEO tool (Semrush, Ubersuggest) for real search volume.
3. **Collect supply data** (what exists): `scripts/yt_competitors.py` for competitor channels (cadence, median views, formats, outlier share) and `scripts/yt_research.py` for top-performing videos in the niche. Use WebSearch/WebFetch for competitors' sites, blogs and other platforms.
4. **Analyze.** Follow `references/frameworks.md`: niche analysis, evidence-based personas, competitor benchmark, and the **gap matrix** (`scripts/research_helper.py gap` compares demand keywords against competitor titles).
5. **Build the strategy.** Pillars scored with the rubric, funnel mapping, platform roles, format and cadence choices derived from capacity plus competitor benchmarks, KPIs with baselines and targets.
6. **Plan the calendar.** `scripts/research_helper.py calendar` lays out slots so pillar ratios and cadence match the plan exactly; then fill topics, hooks and evidence ids per slot.
7. **Deliver** using `references/deliverable-template.md`, with a test-and-learn plan so the strategy gets corrected by results.

If the `viral-content-research` skill is available, use it for the "what is outperforming right now" lane; otherwise `yt_research.py search` covers it.

## Commands

```bash
# demand: autocomplete expansion (relative signal, not volume)
python scripts/research_helper.py suggest "seed topic" "second seed" --source youtube --gl PK --out research/demand
# demand: Google Trends CSV exports the user downloaded
python scripts/research_helper.py trends-csv trends1.csv trends2.csv --out research/trends
# supply: competitor channels (needs YOUTUBE_API_KEY; ~4 quota units per channel)
python scripts/yt_competitors.py @handle1 @handle2 --uploads 30 --out research/competitors
# supply: top performers in the niche
python scripts/yt_research.py search -q "query" --days 90 --region PK --out research/niche
# gap matrix: demand keywords vs competitor titles
python scripts/research_helper.py gap --demand research/demand.csv --supply research/competitors_videos.csv research/niche.csv --out research/gaps
# calendar: print a plan template, edit it, then generate
python scripts/research_helper.py calendar --example > plan.json
python scripts/research_helper.py calendar --plan plan.json --out calendar
```

Run any script with `--help` for all flags.

## Decision rules (why the strategy holds up)

- **Pillars (3 to 5)** must each pass three tests: audience need (evidence from searches, comments or questions), business relevance (it can lead to the goal), and a viable gap or edge. Score them with the rubric in `references/frameworks.md`; drop the lowest.
- **Cadence** comes from capacity first, competitor benchmark second, platform norms third. Recommend a range the user can sustain for 90 days, not the theoretical best. A realistic weekly rhythm beats a plan that collapses in week three.
- **Formats** follow the funnel stage and the platform, and are checked against what actually outperforms in the data (for example, short-form share of competitors' outliers).
- **KPIs** are tied to the goal and the funnel stage, with a baseline, a target and the measurement source. Vanity metrics only appear as supporting signals.
- **Benchmarks** from general knowledge are labelled as benchmarks (confidence: low), never presented as facts about this niche.

## Honesty rules

- Never invent volumes, rates or competitor numbers. Missing data stays blank, and the report says what would fill it.
- State the confidence of each source: verified (API or connected tool), page-visible (fetched page with date), estimated (autocomplete-based signals, Trends index), or assumption.
- Autocomplete and Trends values are *relative signals*, not search volume. Say so wherever they appear.
- Paraphrase sources; keep quotes under 15 words.
- Say plainly when a data source could not be reached (network blocked, no API key, no connector) and what the plan loses because of it.

## If something fails

- **No YouTube key:** see `references/data-sources.md` for how to get one; continue with web research and mark competitor numbers unverified.
- **Scripts cannot reach the network** (sandbox allowlist): say so in one line, continue with WebSearch/WebFetch, and give the user the exact command to run locally; the scripts also read files the user exports.
- **Google Trends has no public API** (only an invite-only alpha at the time of writing), so ask the user to export CSVs from the Trends site and run `trends-csv`.
- **No paid SEO tool:** real search volume is unavailable; use autocomplete rank, Trends and YouTube performance as proxies, and label them as such.

## References

- `references/data-sources.md`: question-to-source map, tool options and costs, evidence ledger format.
- `references/frameworks.md`: personas, niche analysis, pillar rubric, gap matrix, funnel, KPIs, cadence and format logic.
- `references/deliverable-template.md`: the strategy document structure and calendar columns.
