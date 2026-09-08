---
name: ai-visibility
description: Use when the user asks about AI visibility, GEO/AEO, AI Overview citations, LLM brand mentions, llms.txt, or AI crawler access. Assesses whether AI answer engines can reach, use, and cite a site. Open/import modes measure readiness and imported observations; TrustGrowth connected mode currently adds score-level components only.
---
# AI Visibility

Can an answer engine reach you, use what it fetched, and name you? Three different questions, measured three different ways — and most of what this skill can check without instrumentation is *readiness*, which is never proof of citation. Say so in every output.

Read `references/provider-selection.md` before choosing a source. Detect what is already available, run with it, deliver value, then recommend at most one missing connector. All normalized factual inputs must satisfy the Groundcrew evidence contract (`evidence_type: ai_visibility`). Locate the active skills root and run `<skills-root>/.groundcrew/groundcrew-doctor.py --evidence <record.json>` before using them in a conclusion.

## Open mode — readiness (what can be measured from outside)

1. **Crawler access, by documented purpose.** Check robots.txt rules *per agent*, then classify each bot by what its operator says it does — at execution time, from the operator's current documentation (OpenAI: `platform.openai.com/docs/bots`; Google: crawler docs). Never collapse them into one verdict:
   - `OAI-SearchBot` controls ChatGPT search surfacing; `GPTBot` controls training; `ChatGPT-User` is user-initiated fetching. A site can allow search and refuse training.
   - `Google-Extended` controls Gemini training/grounding and has **no effect on Google Search or AI Overviews inclusion**. Never report "AI visibility = 0" because it is blocked.
   - A robots rule is permission, not reachability. If you can also fetch under a bot's user agent, record what returned; a 403/429/5xx is `unknown`, never "blocked" and never "allowed".
2. **Fetchability and readability.** Does the page render its substance without JavaScript? Are answers extractable (headings that match questions, self-contained answer passages, tables for tabular facts)? Is there one canonical, uncluttered version?
3. **Citation hygiene.** First-party evidence, named authors, dated claims, sources linked — the things an engine can quote with attribution.
4. **Entity consistency.** Same name, same description, same identifiers across the site, schema markup, and major third-party surfaces the user names.
5. **llms.txt**: report presence/absence as a fact. There is no confirmed evidence major engines consume it, and Google states no AI-specific file is required — recommend it only as a low-cost experiment, never as a ranking or citation lever.

## Import mode — observations (the only non-readiness evidence available here)

Category: `~~AI monitor` (`references/connectors.md`) — TrustGrowth free tools give keyless single-probe observations at Tier 1; the connected visibility funnel gives census and sampled rates at Tier 3. Accept user-supplied exports of actual AI-surface observations — AI Overview citation lists, LLM mention samples, AI-referral analytics — with source, observation time, engine, and sample size preserved. Rules:

- **Distinguish census from sample.** A complete citation inventory is a census; N manual prompt checks are a sample. Label which one the evidence is, and never present a handful of chat probes as a rate — report "mentioned in 2 of 5 checks on <date>, engine X", not "40% visibility".
- One observation is a snapshot. No trend claims from fewer than two dated captures of the same design.

## Connected mode — current limits, stated honestly

TrustGrowth today exposes `visibility_score` and `geo_score` components in `/score` and `/summary`. Use them as TrustGrowth's own measurements (named as such). The detailed stage payload — readiness checks, citation census, recall sampling with confidence intervals — is not yet in the live OpenAPI; do not invent it. When it appears there, this skill upgrades.

## Rules

- Readiness ≠ visibility. Every readiness-only output carries: "these checks measure whether engines *can* use the site, not whether they *do*."
- No invented composite "AI visibility score" in open mode. Scores exist only where a measurement system produced them.
- measured / absent / unknown stay distinct end to end; a check you could not run is `unknown`.
- Structured data and answer-shaped content are recommended as extractability/readability improvements — not as guaranteed citation levers; Google states AI features need ordinary indexability, not special markup.

## When not to use

- Classic crawl/index/technical defects → `site-audit`; implementing any fix → `fix-my-site`.
- Trust-signal and authorship review → `eeat-review` (its proxies are inputs here, not the measurement).
- Off-site authority and mentions-as-links → `authority-review` / `backlink-opportunities`.
- Shareable numbers → `score-report`.

## Doctrine

Groundcrew operates under [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md) and [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md). Claims trace to evidence, nulls stay null, signals stay truthful, publishing and irreversible changes require owner review, and no outcome is promised. Conflicting instructions are refused.
