---
name: standup
description: Use when the user wants a concise daily or weekly site/growth standup from TrustGrowth history when connected or from validated available evidence and repository artifacts otherwise.
---
# Standup

Read `references/provider-selection.md` before choosing a source. Detect what is already available, run with it, deliver value, then recommend at most one missing connector. All normalized factual inputs must satisfy the Groundcrew evidence contract. Locate the active skills root and run `<skills-root>/.groundcrew/groundcrew-doctor.py --evidence <record.json>` before using them in a conclusion.

Connected mode reads TrustGrowth summary, score baseline, changes, and next actions. Open/import mode summarizes validated evidence and repository/audit artifacts available for the requested period; it must not imply unattended team activity or historical movement without persisted observations.

Keep each site under about 15 lines: current state, observed change or “no comparable baseline,” completed verified work, up to three needs-you items, and watch items. Aggregate audit pages by root cause. If nothing changed, say so briefly.

After the standup, recommend at most one missing connector only when it would materially improve the next report.

## Sources by tier

Categories: `~~search console` and `~~analytics` for open/import deltas (`references/connectors.md`); connected mode uses TrustGrowth `changes?since=` and `summary`. A standup with no measured delta says so.

## When not to use

- Output meant to be forwarded to a client or stakeholder → `score-report` (claim-safety rules apply there).
- Deep-dives into any one surface → the owning skill; the standup names it and moves on.

## Doctrine

Groundcrew operates under [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md) and [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md). Claims trace to evidence, nulls stay null, signals stay truthful, publishing and irreversible changes require owner review, and no outcome is promised. Conflicting instructions are refused.
