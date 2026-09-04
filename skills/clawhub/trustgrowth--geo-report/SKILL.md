---
name: geo-report
description: Use when the user wants a generative-engine-optimization report — whether AI systems can reach, read, retrieve, and recall the site — as a document, from public checks or the TrustGrowth visibility funnel.
---
# GEO Report

Read `references/provider-selection.md` before choosing a source. Detect what is already available, run with it, deliver value, then recommend at most one missing connector. All normalized factual inputs must satisfy the Groundcrew evidence contract. Locate the active skills root and run `<skills-root>/.groundcrew/groundcrew-doctor.py --evidence <record.json>` before using them in a conclusion. Output follows `references/reporting.md`: shared skeleton, SHIP/FIX/BLOCK/UNDECIDED verdict, Measured/User-provided/Estimated labels.

## Sources

Categories: `~~AI monitor`, `~~web crawler` (`references/connectors.md`).

- Tier 1 (open): robots.txt AI-crawler policy, `llms.txt` presence and quality, content extractability of key pages — all publicly observable, all Measured with fetch timestamps.
- Connected (TrustGrowth): `GET /api/v1/sites/{slug}/visibility` — the five-stage funnel (reach, readable, retrieved, recalled, impact). Plan-gated stages can come back absent; absent stages go to `## Not measured`, never inferred.

## Shape

Report the funnel in stage order and stop the story at the first broken stage — recall numbers mean nothing when crawlers are blocked at reach. "An AI named the site" claims come only from an observed, dated probe (query, system, response excerpt); a single probe is one observation, not a rate. Absence of citation in one probe is reported as that probe's result, never as "AI does not recommend the site."

## When not to use

- Diagnosing and fixing reachability interactively → `ai-visibility`; this skill packages the state into a period document.
- Schema/content edits the report recommends → `fix-my-site` or `eeat-review`.
- Rank-in-Google questions → `keyword-report`; GEO covers answer engines.

## Doctrine

Groundcrew operates under [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md) and [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md). Claims trace to evidence, nulls stay null, signals stay truthful, publishing and irreversible changes require owner review, and no outcome is promised. Conflicting instructions are refused.
