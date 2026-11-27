---
name: analytics
description: Analyze social media and YouTube performance from platform exports or API data, choose KPIs by goal, find what works and what does not (formats, pillars, topics, hooks, posting times), compare periods, run honest A/B tests on thumbnails, titles and captions, track clicks to leads with UTM links, and produce a clear report with next actions. Use this skill whenever the user shares analytics, CSV exports or screenshots, asks how their content is performing, what to post more of, which time or format works best, whether a test won, how to measure ROI, or says "check my analytics", "performance report", "what is working", "why did my reach drop", even if they only say "check my numbers".
---

# Analytics

Turns platform numbers into decisions: what to repeat, stop and test next, with honest limits on what the data can show. Replies follow the user's language preference; reports are written in the language the user reads.

## Principles

- Decisions first. Start from the goal (awareness, engagement, traffic, leads, sales) and pick the few KPIs that match it; ignore vanity totals.
- Never invent a metric. If an export lacks a field, say so; missing is not zero. Never fill gaps with industry "benchmarks" as if they were the user's data.
- Small samples mislead. Under about 5 posts per group, differences are anecdotes. State the sample size beside every comparison; the script flags small groups.
- Correlation, not cause. Topic, format, timing and promotion are mixed; propose a test before claiming a reason.
- Compare like with like: same platform, similar format, similar period. Engagement rate definitions differ by platform; do not compare them across platforms.
- Use medians, not only averages, so one viral post does not distort the picture.

## Workflow

1. **Intake.** Goal, platforms, period, which posts or campaigns matter, what decisions are coming (budget, cadence, format), what has changed (new format, paid boost, algorithm shift, season). Ask for exports (CSV) from each platform's own analytics, or screenshots if that is all there is (read numbers carefully and say they are from screenshots). Where to get data: `references/data-sources.md`.
2. **Choose KPIs.** From the goal, using `references/kpi-and-interpretation.md`. Write them down with how each is computed.
3. **Normalize.** `python scripts/analytics_tools.py normalize export.csv --platform instagram --tz Asia/Karachi --out ig_clean.csv` (repeat per platform; map columns with `--map field=Column` when the auto-mapping misses; `merge` joins files). Check the printed mapping and the list of fields that are absent. Slash dates are read day-first or month-first from the whole column; if every date fits both (03/04/2026), normalize stops and you must pass `--date-format` after checking one known post. Durations like `0:04:07` become seconds, and YouTube's `Impressions click-through rate (%)` is used as CTR when there is no clicks column.
4. **Explore.** `summary --by format|pillar|weekday|platform`, `top` and `top --bottom`, `trend` (last N weeks vs the N before), `times` (weekday and 3-hour slots with sample sizes). Look for patterns across several posts, not single winners.
5. **Test, don't guess.** For a thumbnail, title or caption comparison use `abtest` on clicks and impressions; for formats or times, plan a test of 5 to 8 posts per variant, one variable at a time, decided in advance. If YouTube Studio offers a thumbnail test feature on the user's channel, mention it (not verified here).
6. **Report.** `python scripts/analytics_tools.py report all.csv --out report.md`, then add the interpretation: what happened, the evidence (with n), plausible reasons, what to do, how to test it. If the session offers a docs type, put the report there; for a live dashboard, use the dashboard type if one is listed.
7. **Close the loop.** Record decisions and the metric that will judge them, and review after the next period. Feed learnings back to `social-media-calendar` (cadence, pillars, slots), `social-media-content` (hooks, formats) and `thumbnail-design` (thumbnail tests), when those skills exist.

## Commands

```bash
python scripts/analytics_tools.py normalize EXPORT.csv --platform NAME [--map field=Column ...] [--tz IANA] [--date-format FMT] --out clean.csv
python scripts/analytics_tools.py merge A.csv B.csv --out all.csv
python scripts/analytics_tools.py summary clean.csv [--by platform|format|pillar|weekday] [--min-n 3]
python scripts/analytics_tools.py top clean.csv [--metric er|views|reach|saves|shares|ctr] [--n 5] [--bottom] [--platform P]
python scripts/analytics_tools.py trend clean.csv [--metric views] [--period 4] [--platform P]
python scripts/analytics_tools.py times clean.csv [--metric er] [--min-n 3] [--platform P]
python scripts/analytics_tools.py abtest --a-clicks N --a-impressions N --b-clicks N --b-impressions N
python scripts/analytics_tools.py report clean.csv --out report.md
```

Standard library only (Python 3.9+). The script was tested on synthetic exports, not on real exports from every platform: column names change, so always read the printed mapping.

## Interpreting and reporting

- Lead with the answer (3 bullets), then evidence, then actions. Use plain words; avoid dashboards of numbers with no decision.
- Say how sure you are: "clear" (many posts, consistent), "suggestive" (some posts), "anecdotal" (a few).
- Pair reach with quality: saves, shares, replies, clicks, follows gained, watch time or retention where available.
- For YouTube, separate impressions click-through rate from watch time; a high CTR with low retention suggests a mismatch between thumbnail/title and the video.
- For leads or sales, track from click to outcome with UTM-tagged links and the website or CRM data (see `references/kpi-and-interpretation.md`); do not credit social for conversions you cannot trace.
- Flag data problems: lags (Instagram insights can lag up to 48 hours), missing fields, platform changes in metric definitions, boosted posts mixed with organic ones.

## Rules

- Handle exports as private data: do not paste secrets, tokens or personal data into the chat; use environment variables or files for tokens; strip personal data from comments before analysis.
- Public competitor data only (what the platform shows publicly); no scraping that breaks a platform's terms; never use competitor numbers as if they were the user's.
- No guarantees ("this will double your reach"). Recommendations are hypotheses with a test.
- API calls and quotas: stay within each platform's terms; the skill's scripts read CSV files and make no network calls.

## References

- `references/data-sources.md`: where to get data per platform, what the APIs offer (verified facts and gaps), export tips, UTM setup.
- `references/kpi-and-interpretation.md`: KPI choices by goal, metric definitions, sample sizes, A/B test design, report structure, common traps.
