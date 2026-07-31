---
name: industry-deep-dive-pipeline
description: Turn a topic brief, research materials, vendor case, policy event, or industry question into a publish-ready single deep-dive article for technology, AI, data, cloud, or enterprise-software audiences. Runs source verification, originality and competition review, full editorial planning, two human decision gates, drafting, deterministic red-line checks, an eight-role review panel, revision, and final evidence packaging.
description_zh: 产业深度文章全流程编排
description_en: Industry deep-dive pipeline
version: 1.0.0
disable: false
agent_created: true
read_when:
  - industry deep dive
  - research article pipeline
  - 产业深度文章
  - 从选题到定稿
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
2. Judge article type, timeliness level, fact risk, and sensitivity.
3. Mark the user's existing judgments as hypotheses-to-verify, not conclusions.
4. Copy `templates/case-brief.template.md` to `00-case-brief.md`.
5. Run:

```bash
python scripts/validate_case_bundle.py --case-dir <case-dir> --stage input --enforce
```

Stop on input-gate failure and report missing items.

### Step 2: [LLM] Build fact table

1. Extract numbers, dates, companies, policies, product status, quotes, and causal claims.
2. Use search to discover sources; return to official sites, filings, papers, regulatory text, or official releases to verify key facts.
3. High-risk facts need at least dual-source confirmation, or confirmation from a primary authoritative source.
4. Record original date, verification date, status, source tier, usable phrasing, and expiry conditions.
5. Copy `templates/fact-table.template.md` to `01-fact-table.md`.
6. Read `references/evidence-and-originality.md` as needed.

### Step 3: [LLM] Review originality and competition

1. Break out core judgment, analytical framework, and signature expressions.
2. Search Chinese/English news coverage, same-topic analysis, and highly-similar arguments.
3. Separate public opinion, independent deepening, verifiable differences, and phrasing collisions.
4. Proactively find direct counter-arguments, historical counterexamples, and falsification variables.
5. Output `02-originality-review.md`.

Stop if: the core judgment is already well covered with no information gain; the argument depends on unverifiable facts; the topic can only stand on an inflated headline.

### Step 4: [LLM] Produce full planning brief

1. Copy `templates/planning-brief.template.md` to `03-planning-brief.md`.
2. Complete topic feasibility, competition level, reader segmentation, core judgment, argument chain, originality anchor, counter-arguments, title, structure, save-worthy载体, risk, and series relationship.
3. Keep only the decisions that genuinely need a human value judgment.

### Gate A: [Human] Confirm planning

Pause and confirm: core judgment, title direction, length and trade-offs, controversy handling, platform goal, and series relationship. Writing the body is forbidden before confirmation.

### Step 5: [LLM] Draft article

1. Use only the confirmed plan and fact table.
2. Lead with the judgment; then unfold evidence, counter-arguments, and boundaries.
3. Forbid introducing new numbers, dates, statuses, or strong conclusions absent from the fact table.
4. Forbid bringing task background, internal notes, publish info, or writing process into the body.
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

Check unregistered numbers, credentials, UUIDs, personal paths, meta-info, antithetical sentences, marketing words, colloquial buffers, and profile red-lines. On failure return to Step 5, revise, and re-run.

### Step 7: [LLM] Run eight-role review

Call `tech-content-review-panel`, reusing G1/G2, R1–R4, G3, and T1. Copy `templates/review-record.template.md` to `06-review-record.md`; classify opinions into must-fix, should-fix, optional, and tension items.

### Gate B: [Human] Resolve real tensions

Pause only when genuine tensions appear — reach vs professionalism, depth vs completion-rate, risk vs expression, series-consistency vs single-article-independence. Fact errors, missing sources, format errors, and clear red-lines are fixed directly by the flow, not pushed to the user.

### Step 8: [LLM] Revise to final

1. Address all must-fix and should-fix items.
2. Handle tension items per the Gate B decision.
3. Forbid accepting new, unverified facts that appear in the panel review.
4. Record unadopted opinions and reasons to avoid re-raising them.
5. Output `07-final.md`.

### Step 9: [Deterministic + LLM] Re-check

1. Re-verify facts, timeliness, and sources.
2. Re-run `scan_draft_gates.py` on `07-final.md`.
3. Human full read to catch AI-tone, logic jumps, and posture overreach that machines miss.
4. Against the plan, confirm judgment, scope, title, and tables are consistent.
5. Output `08-final-check.md`.
6. Run:

```bash
python scripts/validate_case_bundle.py --case-dir <case-dir> --stage final --enforce
```

### Step 10: [Deterministic] Package deliverables

Copy `templates/final-package.template.md` as the delivery note. Deliver: `07-final.md`, fact table, originality review, confirmed plan, review record, and final-check.

## Hard Rules

1. Search is for discovery; key facts return to primary sources.
2. User assumptions must be verified, not treated as facts just because the user raised them.
3. "Original / first / only" judgments must have search evidence and boundaries.
4. No body writing before Gate A confirmation.
5. Gate B only handles genuine value tensions; never push fact and format issues to the user.
6. High-risk numbers, dates, and statuses in the body must appear in the fact table.
7. After revision, re-run the machine gate and do a human full read.
8. The private writing profile is read on demand only; never copied into the generic skill or public package.
9. Output stops at approved final + evidence package; never generate or execute publish actions.
10. Any tool failure gets retry + cross-verification; re-run after fixing.

## Failure Handling

| Scenario | Action |
|---|---|
| Input material missing | Stop, list missing items, do not guess content |
| High-risk fact unverifiable | Delete, downgrade, or mark待核; forbid into strong judgment |
| Insufficient originality space | Stop writing, suggest merge / re-angle / abandon |
| Gate A unconfirmed | Keep task in progress, generate no body |
| Machine gate fails | Fix the issue and re-run; after 2 rounds report remaining blockers |
| Panel adds unverified fact | Reject inclusion, return to fact table for verification |
| Gate B unconfirmed | Keep tension items, pause final revision |
| Tool fails first try | Retry same op 1–2 times, then switch tool for cross-verification |
| Final verification fails | Do not mark complete, do not generate publish assets |

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

- `references/planning-schema.md`: input, planning, and case-bundle fields.
- `references/evidence-and-originality.md`: source tiers, fact status, originality judgment.
- `references/writing-profile-interface.md`: private writing-profile interface.
- `references/replay-evaluation.md`: Fireworks, Kimi, and European-AI replay standards.

## Pitfalls

- Writing a company case as a company intro, pushing the industry judgment to a secondary position.
- Originality review only searches the same title, missing same-argument different-phrasing.
- Post-panel revision skips re-scan, re-introducing red-lines and fact errors.
- Mixing summary, keywords, tags, cover prompts, or publish notes into the body.
- Series context becomes cross-article self-reference, making a single article unable to stand alone.
- Skipping Gate A to reduce interruptions, then writing a full article around the wrong judgment.

## Verification

- [ ] Required inputs complete; case bundle passes input validation.
- [ ] High-risk fact traceability 100%.
- [ ] Originality review covers Chinese/English same-topic content, counter-arguments, and falsification variables.
- [ ] Gate A has an explicit confirmation record.
- [ ] Draft enters panel review only after passing the machine gate.
- [ ] Gate B contains only genuine tension items.
- [ ] Final re-runs machine scan and completes human full read.
- [ ] Credentials and private identifiers P0 = 0.
- [ ] Output contains no publish assets or external actions.
- [ ] Case bundle passes final validation.

---

## 中文摘要（Chinese Summary）

本 Skill 将单篇科技 / AI / 数据 / 云 / 企业软件产业选题推进到审核通过的正式 Markdown。采用 Prompt Chaining + Evaluator-Optimizer：固定主链保证可追踪，八角色会审后的修订循环保证质量。

**关键约束（双语要点 / Bilingual key points）：**

- **双人类门禁 Two human gates**：Gate A 未确认不得写正文；Gate B 只处理真实价值张力，事实/格式问题由流程直接修正。
- **事实表 Fact table**：正文中的高风险数字、日期、状态必须出现在事实表，并回到一手来源双源确认。
- **原创性 Originality**：「原创/首创/唯一」类判断必须有检索证据与边界，否则停止写作。
- **私有 profile Private profile**：只按需读取，绝不复制进通用 Skill 或公开包。
- **止于定稿 Output stops at final**：只交付审核定稿与证据包，禁止生成或执行任何发布动作。
- **工具失败 Tool failure**：首次失败须重试 1–2 次并换工具交叉验证，修复后必须重跑。
