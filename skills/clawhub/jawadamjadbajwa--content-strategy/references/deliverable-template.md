# Deliverable template

Write in the user's own language and register (match how they write to you). Make it scannable: tables for comparisons, short paragraphs for reasoning. Cite ledger ids (E1, E2, ...) next to decisions. Mark guesses as **assumption**.

## Strategy document

1. **Summary.** The goal, the core bet in one sentence, the 3 most important decisions, and the first action this week.
2. **Assumptions and inputs.** What was given, what was assumed, and what data was unavailable (and what it would change).
3. **Niche snapshot.** Demand direction, seasonality, competitive density, saturation, monetization routes (with evidence ids).
4. **Audience personas.** 2 to 3 personas using the template in `frameworks.md`.
5. **Competitor benchmark.** Table: competitor, platform, posts per week, median views, outlier share, formats, top topics, weak spot. Then 3 takeaways.
6. **Content gaps.** Ranked list from the gap matrix: topic, demand evidence, supply evidence, class (gap, thin, contested), recommended angle.
7. **Content pillars.** Table: pillar, rubric score, share of posts, funnel stage, example topics, evidence ids.
8. **Funnel strategy.** Awareness, Engagement, Conversion: content types, CTAs, and the handoff between stages.
9. **Platform strategy.** One block per platform: role in the funnel, formats and lengths, cadence (range, minimum, stretch), posting days, what to repurpose from where.
10. **KPIs.** Table: KPI, stage, baseline, 90-day target, source, review rhythm.
11. **Calendar.** The first 4 weeks in detail (see columns below), then a monthly outline.
12. **Test-and-learn plan.** Experiments, sample size, metric, decision rule.
13. **Risks and next data to collect.** What could make the plan wrong and the cheapest way to check.
14. **Evidence appendix.** The ledger (or a link to `evidence.csv`) and the source list.

## Calendar columns

`date, weekday, week, platform, pillar, funnel_stage, format, topic, hook, evidence_id, cta, status`

`research_helper.py calendar` fills date, platform, pillar and funnel stage so ratios and cadence are exact; fill the rest per slot, with one evidence id per topic.

## Files to hand over

- the strategy document (a document artifact if the session offers one, otherwise a markdown file)
- `calendar.csv`
- `evidence.csv`
- raw data files from the research scripts (CSV/JSON), if the user wants to inspect them

## Length

The document should be readable in about 10 minutes. Put raw data in the CSVs, keep the document to decisions and the evidence behind them. End with one sentence naming the single best next step.
