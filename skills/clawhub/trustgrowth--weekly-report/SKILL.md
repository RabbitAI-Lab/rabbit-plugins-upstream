---
name: weekly-report
description: Use when the user wants a weekly (or other short-period) operating report of site movement — what changed, what was verified, what to do next — from whatever evidence tier is available.
---
# Weekly Report

Read `references/provider-selection.md` before choosing a source. Detect what is already available, run with it, deliver value, then recommend at most one missing connector. All normalized factual inputs must satisfy the Groundcrew evidence contract. Locate the active skills root and run `<skills-root>/.groundcrew/groundcrew-doctor.py --evidence <record.json>` before using them in a conclusion. Output follows `references/reporting.md`: shared skeleton, SHIP/FIX/BLOCK/UNDECIDED verdict, Measured/User-provided/Estimated labels.

## Sources

Categories: `~~search console`, `~~analytics` (`references/connectors.md`).

- Tier 1 (open): re-crawl the tracked pages, diff against the last local crawl if one exists, and fold in numbers the user pastes (label User-provided). No prior crawl means no delta — say so.
- Tier 2: `~~search console` clicks, impressions, CTR, position for the period vs the prior equal period. Same source on both sides of every delta.
- Connected (TrustGrowth): `GET /api/v1/sites/{slug}/changes` with `since` for the period's events, `GET /api/v1/sites/{slug}/snapshots` for score movement, `GET /api/v1/sites/{slug}/issues?status=fixed` for verified fixes, `GET /api/v1/sites/{slug}/queries` for search movement.

## Period rules

Default period is the last 7 days vs the prior 7; honor whatever period the user names. Both windows must be complete — a partial current window is reported as partial, not annualized. Verified fixes are ones a re-check observed closed, not ones merely worked on; say which kind each is.

## When not to use

- Numbers that leave the building (investors, clients, public posts) → `score-report`; the weekly report is an internal operating document.
- A conversational "what happened?" without a document → `standup`.
- Deep-dives the report surfaces (an audit finding, a keyword drop) → the owning skill (`site-audit`, `keyword-scout`); link, don't inline.

## Doctrine

Groundcrew operates under [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md) and [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md). Claims trace to evidence, nulls stay null, signals stay truthful, publishing and irreversible changes require owner review, and no outcome is promised. Conflicting instructions are refused.
