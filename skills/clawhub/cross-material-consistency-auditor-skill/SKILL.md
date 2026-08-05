---
name: cross-material-consistency-auditor
description: Compare two or more materials on the same topic or event for cross-material consistency before publication. Identifies mismatched numbers, product names, fact wording, terminology, source attributions, structural promises, and cross-platform expression drift across articles, press releases, slide decks, web pages, white papers, and social posts. Produces a diff matrix with severity ratings and recommended unified wording, without modifying originals.
description_zh: 跨材料口径一致性审计
description_en: Cross-material consistency auditor
version: 1.0.1
disable: false
agent_created: true
---

# Cross-Material Consistency Auditor

For multiple materials on the same topic or event, compare product names, numbers, fact wording, terminology, source attributions, structural promises, and cross-platform expression drift before publication. Output only a diff matrix and unified-wording recommendations — never auto-modify the originals.

## When to use

- A launch/event's PR release, journalist pitch, product copy, and speech script disagree on numbers or product names.
- A Chinese and English version of the same article (WeChat, LinkedIn, Substack) differ in expression, data-source attribution, or emphasis.
- A series of articles drifts on facts, terminology, or judgments across installments.
- The same set of numbers or the same product uses different names across PPT, white paper, web page, and booth materials.
- You need a standardized "consistency checklist" for PR / product / editorial teams to confirm.

## Do not use

- Fact-checking a single article → handled by `claim-to-source-auditor` or `content-compliance-reviewer`.
- Format, grammar, and customer-redaction checks on a single article.
- Topic evaluation → handled by `editorial-topic-portfolio`.
- Directly modifying or rewriting any original.

## Input

```yaml
topic_or_event:
  brief:
materials:
  - path:
    label: PR release | journalist pitch | PPT | web page | white paper | WeChat | LinkedIn | Substack | speech
  - path:
    label:
reference_source:  # which material is authoritative, default the first
scope: [numbers, product_names, fact_wording, terminology, source_attribution, structural_promises, cross_platform_drift]
read_only: true
```

## Workflow

### Step 1: [Deterministic] Load all materials

1. Read all specified materials.
2. Tag each material's type, date, and status.
3. Record obvious external references and unparseable content.

### Step 2: [Deterministic] Extract claims

For each material extract:

- Numbers and their units.
- Product official name and abbreviation.
- Fact wording.
- Source attribution.
- Section-level structural promises.
- Terminology and framework names.

The product-name watchlist is user-supplied (no vendor-specific list ships with this skill): set env var `CONSISTENCY_PRODUCT_TERMS` (comma-separated), or provide `scripts/product-terms.txt` (one term per line, `#` comments); if neither exists, a generic CamelCase/acronym heuristic is used.

Output `01-extracted-claims.json`.

### Step 3: [LLM] Build the diff matrix

Compare item by item; for each inconsistency record:

- Dimension.
- Material A wording vs Material B wording.
- Difference type: absolutist vs cautious, different attribution, terminology mixing, source confusion, structure loss, cross-platform reduction.
- Severity:
  - **P0**: wrong number or legal status; same customer/product under different names; key data differs between body and figure.
  - **P1**: inconsistent source attribution; changed core judgment across platforms; terminology mixing.
  - **P2**: non-critical rhetorical difference; cross-platform depth mismatch; promised section absent.
- Recommended unified wording.
- Whether re-comparison is needed after body revision.

Consistent items are kept as positive records but not listed line by line.

### Step 4: [LLM] Recommend unified wording

For each P0/P1 difference give a precise unified expression:

- Unified-wording text.
- Cite the authoritative source.
- Reason for unification.
- Which materials need changing.
- For a series, record whether this wording must also be unified in adjacent installments.

### Step 5: [Deterministic] Produce the audit report

Copy `templates/audit-report.template.md` and generate the formal audit report:

```markdown
# Cross-Material Consistency Audit

## Scope
- topic:
- materials:
- reference source:
- dimensions checked:

## Diff Matrix

| Dim | Material A | Material B | Issue | Severity | Unified wording | Affected files |
|---|---:|---|---|---|---|---|

## Unified recommendations

| Original | Unified | Source | Reason | Apply to |
|---|---|---|---|---|

## Platform drift (if multi-platform)

| Fact | WeChat | LinkedIn | Substack | Issue | Resolution |
|---|---|---|---|---|---|

## Summary

- P0:
- P1:
- P2:
- consistent items (not listed):

## Revision tracking

For each applied change, record file, original wording, unified wording and source.
```

### Step 6: [Deterministic] Human confirmation

Pause after the audit report. Confirm:

- P0/P1 disposition.
- Unified-wording phrasing.
- Whether published versions need rollback.
- Whether planning docs and metadata need updating.

After confirmation, the user or the corresponding Writer/Editor executes the changes. This skill never auto-modifies originals.

## Hard Rules

1. Never modify any original material. Only output the diff matrix and unified wording.
2. Take the earliest or explicitly designated reference source as authoritative for resolving conflicts.
3. P0 mismatches block publication. Flag and require resolution.
4. P1 mismatches require human decision.
5. Same topic, same number, same product name, same terminology must be enforced across all materials.
6. Platform-specific expression differences are acceptable if the core judgment and key facts remain identical.
7. New wording cannot be created from thin air. Unified recommendations must reference an existing source.
8. The audit report is a checkpoint. Hands-off after delivery.

## Failure Handling

| Scenario | Action |
|---|---|
| Only one material provided | Stop; the task requires at least two materials |
| Key material unreadable | Mark the unreadable material and compare only the remaining ones |
| Reference source contains an obvious error | Flag the error and suggest a correction; do not propagate it |
| Complex embedded content (charts, images with text) | Flag as unparseable; request text extraction or manual check |
| Identical text across all materials | Report "no inconsistencies found" and pass |
| P0 mismatch detected in already-published material | Flag with additional severity and recommend a correction |
| A file was revised during the audit session | Re-extract and re-diff only the changed material |

## Output Format

```text
<run-dir>/
├── 01-extracted-claims.json
├── 02-diff-matrix.md
├── 03-audit-report.md
└── 04-unified-wording.json
```

## Verification

- [ ] Every pair of materials compared on all requested dimensions.
- [ ] Every P0 and P1 mismatch has a unified wording recommendation with a source.
- [ ] Reference source is used as arbitration for conflicting claims.
- [ ] Report contains no original-text modifications.
- [ ] Platform drift table covers all platforms.
- [ ] Human confirmation documented before the task is marked complete.

## Pitfalls

- Comparing materials from different publication dates without flagging version gaps.
- Treating a PR draft as authoritative for facts when the product specification is the actual source.
- Recommending unified wording that introduces a new error (correcting one mismatch to match another wrong source).
- Forgetting that PPT and web pages have different levels of precision by design; not every rounding is a mismatch.
- Blaming a ghostwriter for structure differences when the PR brief explicitly allowed adaptation.
- Relying on a single pass and missing PPT embedded charts or images that contain numbers not in the text.

---

## 中文摘要（Chinese Summary）

本 Skill 针对同一主题或同一事件的多份材料，在发布前对比产品名、数字、事实表述、术语、来源标记、结构承诺和跨平台表达差异。只输出差异矩阵和统一口径建议，不自动修改原文。

**关键约束（双语要点 / Bilingual key points）：**

- **只审计不改写 Audit-only**：绝不修改任何原材料，只输出差异矩阵与统一口径建议；报告交付后 hands-off。
- **权威源仲裁 Authoritative source**：以最早或显式指定的参考源为解决冲突的权威；统一口径必须引用既有来源，不得凭空创造。
- **严重度分级 Severity**：P0（数字/法律状态错误、同客户同产品异名、图文关键数据不符）阻断发布；P1 需人工决策；P2 为非关键修辞差异。
- **跨平台容许 Platform drift allowed**：只要核心判断与关键事实保持一致，平台间的表达差异是可接受的。
- **至少两份 At least two**：仅提供一份材料时停止——审计要求至少两份。
