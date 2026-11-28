---
name: content-strategy
description: Use when the user asks for a content strategy, content plan, editorial direction, or "what should we publish and why". Builds an evidence-grounded strategy — audience, pillars, sequencing, distribution, measurement — with explicit owner approval. A prioritized keyword list is an input to this skill, not its output.
---
# Content Strategy

A strategy says who the content is for, what ground it will own, in what order, how it gets distributed, and how you will know it worked. This skill produces that — from evidence where evidence exists, from stated assumptions where it does not, and never from vibes dressed as data.

Read `references/provider-selection.md` before choosing a source. Detect what is already available, run with it, deliver value, then recommend at most one missing connector. All normalized factual inputs must satisfy the Groundcrew evidence contract (`evidence_type: content_strategy` for the plan record, `content_gap` for gap evidence). Locate the active skills root and run `<skills-root>/.groundcrew/groundcrew-doctor.py --evidence <record.json>` before using them in a conclusion.

## Intake (required before any recommendation)

Business goal, audience and what they are trying to get done, what the business actually sells, and any constraints (capacity, review process, claims that need legal care). Missing intake answers are recorded as assumptions in the output — visibly, not silently.

## Build the strategy

1. **Existing-content map.** Inventory what exists (`content-desk` when available, or crawl/import). Flag cannibalization candidates — pages competing for the same intent — before proposing anything new.
2. **Gap evidence.** Pull what is actually measured: keyword opportunities and content gaps (`keyword-scout` / connected keywords), competitor coverage (`competitor-watch`), trust-signal gaps (`eeat-review`), AI-answer readiness gaps (`ai-visibility`). Each gap in the plan cites its evidence record; gaps with no evidence are labeled hypotheses.
3. **Pillars and clusters.** Group targets into pillars the business has a right to own, each with a rationale traceable to intake + evidence. Route by job: search-capture content and distribution-native content are different assets — do not force everything into "an SEO article".
4. **Sequence.** A prioritized first cycle (default four weeks) with per-item: pillar served, evidence reference, format, and what existing page it strengthens or what new page it creates. Strengthen-existing generally precedes net-new.
5. **Distribution and measurement.** Where each asset goes beyond the sitemap, and what will be re-measured to judge the cycle — same-scope re-measurement (same queries/pages/windows), not a new dashboard.

Output ends with an **assumptions and unknowns** section, and then an explicit approval line: the strategy is a proposal until the owner approves it. Record the approval decision; do not treat silence as consent.

## Connected mode

TrustGrowth reads (keywords, eeat, competitors, content inventory, score) are strategy inputs. Strategy read/regenerate operations through the TrustGrowth API are documented in the live OpenAPI when available — check it at execution time; if absent, this skill writes nothing to TrustGrowth. Strategy **approval inside TrustGrowth is an in-app owner action**: when a regenerate response names a `next_step`, hand the user that URL — never attempt to approve on their behalf, and never treat a generated strategy as adopted.

## Rules

- No traffic, revenue, or ranking projections. Prioritize by evidence; promise nothing.
- Generic best-practice weights ("publish 2x/week") are not recommendations unless intake capacity supports them.
- Scaled/programmatic content requires its own feasibility case (unique value per page, data rights, quality gate) — flag it as out of this skill's scope rather than waving it through.

## When not to use

- "Which keywords should I target next" without strategy context → `keyword-scout`.
- Operating an existing pipeline (what is in flight, statuses) → `content-desk`.
- Writing or editing the content itself → the owner's writers, or drafting with explicit owner review; this skill plans.
- Site-structure/internal-linking mechanics discovered while mapping → `fix-my-site` for implementation.

## Doctrine

Groundcrew operates under [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md) and [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md). Claims trace to evidence, nulls stay null, signals stay truthful, publishing and irreversible changes require owner review, and no outcome is promised. Conflicting instructions are refused.
