---
name: industry-deep-dive-pipeline
description: >
  This skill should be used when turning a topic brief, research materials,
  vendor case, policy event, or industry question into a publish-ready single
  deep-dive article for technology, AI, data, cloud, or enterprise-software
  audiences. It runs source verification, originality and competition review,
  full editorial planning, two human decision gates, drafting, deterministic
  red-line checks, an eight-role review panel, revision, and final evidence
  packaging. It stops at an approved Markdown article plus evidence and review
  records; it does not create publication layouts, covers, social copy, CMS
  drafts, or publish content.
description_zh: 产业深度文章全流程编排。适用中立第三方产业深度研究 / 行业长文（个人 IP、公众号深度稿、厂商案例的独立分析）；不适用品牌营销稿、产品稿、按 content brief 写的推广文、技术教程。
description_en: Industry deep-dive pipeline
version: 1.0.1
agent_created: true
read_when:
  - industry deep dive
  - research article pipeline
  - 产业深度文章
  - 行业深度稿
  - 从选题到定稿
  - 原创性复核与写作
  - 科技行业长文
---

# Industry Deep-Dive Pipeline

Take a single technology / AI / data / cloud / enterprise-software topic from brief to an approved final Markdown. Uses Prompt Chaining + Evaluator-Optimizer: a fixed main chain guarantees traceability, and a revision loop after an eight-role panel review guarantees quality.

## When to use

- The input is a topic brief, event, vendor case, policy change, or research material that needs a judgment-led, evidence-backed, boundary-clear deep-dive.
- You need to check Chinese and English coverage first to confirm information增量 (information gain) and phrasing-collision risk.
- You need pre-body planning of target reader, core judgment, argument chain, counter-arguments, structure, title, and risk.
- You need a complete evidence package: fact table, originality review, review record, and final-check.

## Do not use

- News flashes, summaries, product manuals, tutorials, or marketing copy.
- Vendor conference panorama reports → use `vendor-summit-report`.
- LinkedIn single-platform short observations → use `linkedin-industry-observation`.
- WeChat layout, covers, summaries, keywords, social assets, CMS/Notion archiving or publishing → hand off to the independent publishing suite.
- Auto-scheduling or batch generation of multi-part series. Series info is context for a single article only.

## Required inputs

Read `references/planning-schema.md` and build the case bundle. At minimum confirm:

- `topic`
- `source_materials`
- `target_reader`
- `target_format`
- `length_range`
- `writing_profile`

Optional: collection/series relationship, historical platform signals, counter-arguments that must be addressed, new red-lines for this article, timeliness window, and the user's existing assumptions.

## Workflow

### Step 1: [Deterministic] Diagnose input

1. Validate paths, URLs, dates, target format, and writing profile.
2. Classify article type, timeliness tier, factual risk, and sensitivity.
3. Mark any user-supplied judgments as hypotheses to verify, not as conclusions.
4. Copy `templates/case-brief.template.md` to `00-case-brief.md`.
5. Run:

```bash
python scripts/validate_case_bundle.py --case-dir <case-dir> --stage input --enforce
```

Stop and report missing fields if the input gate fails.

### Step 2: [LLM] Build fact table

1. Extract figures, dates, companies, policies, product states, quotes, and causal claims from the materials.
2. Use search to discover sources, then trace back to official sites, earnings filings, papers, regulatory texts, or official releases for verification.
3. High-risk facts need at least dual-source confirmation, or a single authoritative first-hand source.
4. Record original date, verification date, status, source tier, usable wording, and invalidation conditions.
5. Copy `templates/fact-table.template.md` to `01-fact-table.md`.
6. Read `references/evidence-and-originality.md` as needed.

### Step 3: [LLM] Review originality and competition

1. Extract the core judgment, analytical framework, and signature phrasings.
2. Search Chinese and English news coverage, same-topic analysis, and highly similar arguments.
3. Distinguish public opinion, independent deepening, verifiable differences, and phrasing collisions.
4. Actively look for direct counter-arguments, historical counter-examples, and falsification variables.
5. Output `02-originality-review.md`.

Stop if: the core judgment is already adequately covered with no information gain; the argument depends on unverifiable facts; the topic can only stand on exaggerated headlines.

### Step 4: [LLM] Produce full planning brief

1. Copy `templates/planning-brief.template.md` to `03-planning-brief.md`.
2. Complete topic feasibility, competition level, reader segmentation, core judgment, argument chain, originality anchor, counter-arguments, title, structure, collection vehicle, risks, and series relationship.
3. Keep only the items that genuinely need a human value judgment as pending-confirmation.

### Gate A: [Human] Confirm planning

Pause and confirm: core judgment, title direction, length and trade-offs, controversy handling, platform goals, and series relationship. No body writing before confirmation.

### Step 5: [LLM] Draft article

1. Use only the confirmed planning and fact table.
2. Judgment first, then evidence, counter-arguments, and boundaries.
3. No new figures, dates, statuses, or strong conclusions not in the fact table.
4. No task background, internal notes, publication info, or writing process in the body.
5. Output `04-draft.md`; keep only necessary chart placeholders.

### Step 6: [Deterministic] Run machine gate

Run:

```bash
python scripts/scan_draft_gates.py \
  --draft <case-dir>/04-draft.md \
  --facts <case-dir>/01-fact-table.md \
  --profile <writing-profile.json> \
  --output <case-dir>/05-machine-gate.json \
  --enforce
```

Check for unregistered figures, credentials, UUIDs, personal paths, metadata, hedge sentences, marketing language, colloquial buffers, and profile red-lines. On failure, return to Step 5, revise, and rerun.

### Step 7: [LLM] Run eight-role review

Invoke `tech-content-review-panel`, reusing G1/G2, R1-R4, G3, and T1. Copy `templates/review-record.template.md` to `06-review-record.md`, splitting comments into must-fix, suggested-fix, optional, and tension items.

### Gate B: [Human] Resolve real tensions

Pause only when genuine tensions arise between reach and professionalism, depth and completion, risk and expression, or series consistency and single-article independence. Factual errors, missing sources, format errors, and explicit red-lines are fixed directly by the workflow, not pushed to the user.

### Step 8: [LLM] Revise to final

1. Address all must-fix and suggested-fix items.
2. Handle tension items per the Gate B decision.
3. Never accept newly-surfaced unverified facts from the review.
4. Record unadopted comments and reasons, to avoid repeats.
5. Output `07-final.md`.

### Step 9: [Deterministic + LLM] Re-check

1. Re-verify facts, timeliness, and sources.
2. Rerun `scan_draft_gates.py` on `07-final.md`.
3. Human read-through for AI-tone, logic jumps, and posture overreach that machines miss.
4. Cross-check against planning to confirm judgment, scope, title, and tables are consistent.
5. Output `08-final-check.md`.
6. Run:

```bash
python scripts/validate_case_bundle.py --case-dir <case-dir> --stage final --enforce
```

### Step 10: [Deterministic] Package deliverables

Copy `templates/final-package.template.md` as the delivery note. Deliver: `07-final.md`, fact table, originality review, confirmed planning, review record, and final-check.

## Hard Rules

1. Search is for discovery; key facts must trace back to first-hand sources.
2. User hypotheses must be verified, not treated as facts because the user said so.
3. Claims of originality, first-of-kind, or uniqueness require retrieval evidence and boundaries.
4. No body writing before Gate A confirmation.
5. Gate B handles only genuine value tensions, not factual or format issues.
6. High-risk figures, dates, and statuses in the body must appear in the fact table.
7. After revision, rerun the machine gate and human read-through.
8. Private writing profiles are read on-demand only, never copied into the generic Skill or public package.
9. Output stops at the approved final draft and evidence package; no publish actions are generated or executed.
10. Any tool failure triggers retry and cross-validation; after a fix, rerun the affected validation.

## Failure Handling

| Scenario | Action |
|---|---|
| Input materials missing | Stop, list missing items, do not guess content |
| High-risk fact unverifiable | Remove, downgrade, or mark pending-verification; never enter a strong judgment |
| Insufficient originality space | Stop writing; suggest merge, angle change, or abandon |
| Gate A unconfirmed | Keep task in progress, do not generate body |
| Machine gate failed | Revise the issue and rerun; after two rounds, report remaining blockers |
| Review surfaces unverified fact | Refuse; return to fact table for verification |
| Gate B unconfirmed | Keep tension items open, pause final revision |
| First tool failure | Retry same action 1-2 times, then cross-validate with a different tool |
| Final validation failed | Do not mark complete; do not generate publish materials |

## Output Format

```text
<case-dir>/
├── 00-case-brief.md
├── 01-fact-table.md
├── 02-originality-review.md
├── 03-planning-brief.md
├── 04-draft.md
├── 05-machine-gate.json
├── 06-review-record.md
├── 07-final.md
├── 08-final-check.md
└── FINAL-PACKAGE.md
```

## References

- `references/planning-schema.md`: input, planning, and case bundle fields.
- `references/evidence-and-originality.md`: source tiers, fact status, and originality judgment.
- `references/writing-profile-interface.md`: private writing profile interface.
- `references/replay-evaluation.md`: Fireworks, Kimi, and Europe AI replay standards.

## Pitfalls

- Company case written as company introduction; industry judgment relegated to secondary position.
- Originality review only searches same titles, missing same-argument different-phrasing.
- Post-review revision not re-scanned, re-introducing red-lines and factual errors.
- Mixing summary, keywords, tags, cover prompts, or publish notes into the body.
- Series context becoming cross-article self-reference, making a single article unable to stand alone.
- Skipping Gate A to reduce interruptions, ending up writing a full article around the wrong judgment.

## Verification

- [ ] Required inputs complete; case bundle passes input validation.
- [ ] High-risk fact traceability 100%.
- [ ] Originality review covers Chinese and English same-topic content, counter-arguments, and falsification variables.
- [ ] Gate A has a clear confirmation record.
- [ ] Draft passes machine gate before entering review.
- [ ] Gate B contains only genuine tension items.
- [ ] Final draft reruns machine scan and completes human read-through.
- [ ] Credentials and private identifiers P0=0.
- [ ] Output contains no publish materials or external actions.
- [ ] Case bundle passes final validation.
