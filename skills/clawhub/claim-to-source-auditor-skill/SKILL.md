---
name: claim-to-source-auditor
description: Audit, fact-check, verify, or cross-check an article, report, draft, or series. Extracts verifiable claims, traces them to L0 primary or L1 reliable secondary sources, marks each as pass/partial-support/missing-evidence/wrong/judgment, and produces a structured audit report with P0-P2 severity. Supports cross-platform version comparison and regression gold-set re-runs.
description_zh: 审稿核验器
description_en: Claim-to-Source Auditor
version: 1.0.1
disable: false
agent_created: true
---

# Claim-to-Source Auditor

## When to use

Use this skill when the user wants to:

- Fact-check a long-form article, report, or analysis before publication.
- Verify that claims in a published piece still hold against current sources.
- Check whether the same facts are consistent across multiple platform versions of the same article.
- Audit academic citations, regulatory claims, financial numbers, internal data, or direct quotes.
- Build a regression gold set so future revisions can be checked for fact-regression.
- Validate that external incidents are attributed correctly across event facts, platform statements, and author judgments.

## Do not use

- For style editing, structure critique, or argument-strength assessment — this skill only audits factual claims and their source support.
- For cross-material wording/number consistency across sibling materials → use `cross-material-consistency-auditor`.
- For full pre-publish compliance review of a marketing draft → use a dedicated compliance-review skill if one is installed.

## Architecture

Default to a fixed workflow running in shadow mode — read output, compare to sources, produce an audit table. Do not modify the source article unless the user explicitly asks for revision. Always separate audit from editing.

Target: 30–50 high-risk claims per article batch. High-risk means: specific numbers, dates, percentages, dollar amounts, regulatory conclusions, named individuals, institution affiliations, direct quotes, paper details, and incident attributions.

## Evidence hierarchy

Assign every source used to one of three levels:

| Level | Definition | Examples |
|---|---|---|
| L0 primary | Original, verifiable, unfiltered | Court judgments, official regulatory text, company filings, raw operational logs, author's original social-media post, arXiv pre-print |
| L1 reliable secondary | Trusted reporting with named sources | Bloomberg, Reuters, The Register, Fortune, a peer-reviewed journal article with a DOI |
| L2 supplementary | Indirect or unverified | Aggregated media summaries, a research archive that cites but does not quote the original, an LLM-generated summary of a paper |

- A claim can pass only when supported by L0 or L1.
- L2 can support partial-pass or help explain a gap; it cannot make a claim pass on its own.
- If L0 and L1 disagree, surface both and flag the conflict.

## Workflow

### Step 1: [LLM] Extract high-risk claims

Read the article body and extract every claim that falls into one or more of these categories:

1. Specific numbers or percentages.
2. Dates, time ranges, and timelines.
3. Direct quotes attributed to a named person.
4. Dollar, euro, or other currency amounts.
5. Regulatory conclusions.
6. Academic paper details.
7. Named institutions, roles, or affiliations.
8. Incident summaries that assign cause or blame.

For each claim, record: claim text, category, line or section reference, and whether it is a fact or the author's own judgment.

### Step 2: [Deterministic] Collect available evidence

For each claim, identify available local sources: research databases, internal operational logs, prior fact-check reports, and clean gold-set records from earlier audits.

For claims requiring external verification, search for: official judgments, company announcements, regulatory texts, original social-media posts, and trusted media reports.

### Step 3: [LLM] Classify each claim

Assign one of five statuses (Chinese labels retained for backward compatibility with reports; English gloss in parentheses):

| Status (状态) | Criteria |
|---|---|
| 通过 (pass) | L0 or L1 source directly supports the exact claim as written |
| 部分支持 (partial-support) | Core event or number exists, but the text overstates scope, causation, precision, or legal meaning |
| 缺证 (missing-evidence) | No L0 or L1 source found; only L2 or no source at all |
| 错误 (wrong) | L0 or L1 source directly contradicts the claim |
| 判断 (judgment) | Reasonable author analysis that no single source can prove or disprove |

Assign a severity:

- P0: must be corrected before next publication (wrong author, wrong number, fabricated or uncitable quote, wrong regulatory claim).
- P1: should be tightened or sourced (overstated scope, missing attribution, imprecise date or currency, inference presented as fact).
- P2: acceptable as-is with minor sourcing notes.

### Step 4: [LLM] Cross-platform verification

When the same article exists in multiple languages or platforms, check every high-risk claim across all versions:

- Are numbers, dates, and people's names identical?
- Are source annotations present in every version?
- Are regulatory conclusions translated without adding or losing meaning?

Mark each item as 一致 (consistent) / 近似 (approximate) / 偏差 (deviation) / 错误 (wrong).

### Step 5: [LLM] Separate layers in incident attribution

When an article describes a real-world incident, split it into three layers:

1. What is agreed to have happened.
2. How the platform or parties involved described it.
3. How the author interprets it.

Only layer 1 can pass as a verified fact. Layers 2 and 3 cannot be written as if they are the same thing.

### Step 6: [Deterministic] Save a regression gold set

After every audit, save the claim list and verdicts as a CSV. When the article is revised, re-run the same claims to check for regression. A gold-set item that was previously 通过 (pass) and now fails counts as a regression event.

### Step 7: [LLM] Produce the audit report

Output a structured report containing:

- Article name, platform, and audit date.
- Summary counts: total claims, 通过/部分支持/缺证/错误/判断 (pass/partial-support/missing-evidence/wrong/judgment) by severity.
- P0 list with required corrections.
- Cross-platform comparison (if applicable).
- Regression check against any prior gold set.
- Source register with URLs.

## Hard rules

1. Only L0 or L1 sources can make a claim pass. L2 is supplementary only.
2. Papers, court judgments, and regulatory texts must never be silently altered. Mark any paraphrase, translation, or correction explicitly. Never present a paraphrase as a direct quotation.
3. Published articles may be revised directly when the user accepts a change. Every change to a paper citation, judgment, or regulatory reference must carry an annotation.
4. Separate event facts, platform/party attributions, and author interpretation — do not compress them into a single sentence.
5. Regulatory materials define jurisdiction-specific requirements. Do not compress them into universal prohibitions.
6. A prior fact-check report is a regression oracle, not proof that the current version is clean. Compare every historical P0/P1 item against the current text.
7. The default for any claim without a verifiable source is 缺证 (missing-evidence), not 通过 (pass).
8. Never invent evidence to fill a gap. If a source cannot be found, report it as a gap.

## Pitfalls

- Do not infer that a local file is unpublished merely because the folder is named `drafts`. The user, a CMS record, or a publication log is authoritative.
- A direct quote in an article that cannot be found in the reported source is a P0, even if the surrounding story is true.
- Near-miss numbers are still mismatches. An audit that reports 5810 when the source says 5817 must flag the difference.
- Cross-platform periods are high-risk. If one version reads "2024" and the other "2025", the different year is an error, not a paraphrase.
- Regulatory documents exist in specific jurisdictions. Never write "FDA, EU MDR, and China's regulations all say the same thing" without checking the governing text.

## Failure handling

| Scenario | Action |
|---|---|
| Source is behind a paywall or blocked | Mark the claim as 缺证 (missing-evidence); note the source is unavailable |
| Primary source and secondary source disagree | Surface both with verbatim quotes; flag the conflict |
| Claim involves a future prediction | Mark as 判断 (judgment); do not treat it as a fact |
| Foreign-language regulatory text | Use an official translation if available; otherwise mark as 部分支持 (partial-support) and flag language limitation |
| Internal operational log unavailable | Mark the claim as 部分支持 (partial-support); note which specific log is missing |
| Previously verified claim now fails | Flag as gold-set regression; escalate to P0 review |

## Verification

Before delivering, verify:

- Every P0 has a specific source that contradicts or fails to support the claim.
- The cross-platform audit table covers the same claims on every platform.
- The gold-set CSV loads cleanly and has the same number of rows as the current audit.
- Paper authors, journal names, case numbers, and years are checked against the original source, not against an intermediary archive.
- The audit report states which claims could not be verified and why.

## Output format

1. **Audit-problems CSV**: one row per claim, columns for claim-id, article, claim-text, status, severity, evidence-summary, and required-action.
2. **Audit report**: structured Markdown containing the summary table, P0 list, P1 summary, cross-platform comparison, regression check, source register, and final pass/fail/conditional decision.
3. **Gold-set CSV** (optional, for regression): one row per claim with the verdict from the most recent audit.

Lead with the decision, then evidence, boundaries, and next-stage actions.

---

## 中文摘要（Chinese Summary）

本 Skill 用于审稿 / 事实核验 / 来源追溯 / 跨平台一致性检查。提取可核验主张，溯源至 L0 一手或 L1 可靠二手来源，逐条标记为 通过 / 部分支持 / 缺证 / 错误 / 判断，并输出带 P0–P2 严重度的结构化审计报告；支持跨平台版本比对与回归 gold-set 重跑。只审计事实与来源，不改写风格或论证结构。

**关键约束（双语要点 / Bilingual key points）：**

- **证据分级 Evidence tiers**：仅 L0 一手或 L1 可靠二手可使主张通过；L2 仅补充，不能单独支撑通过；L0 与 L1 冲突时同时呈现并标红。
- **五状态 Five statuses**：通过 / 部分支持 / 缺证 / 错误 / 判断（保留中文标签以兼容既有报告，英文对照见正文表格）。
- **缺证默认 Missing-by-default**：无可核验来源的主张默认判 缺证，而非 通过；绝不编造证据填补缺口。
- **事故三层分离 Incident layers**：仅「公认发生的事实」层可作为已核验事实，平台表述层与作者解读层不得混写。
- **回归 gold-set Regression oracle**：每次审计留存主张与结论 CSV；修订后重跑同一批主张，曾 通过 现失败即记为回归事件并升级 P0。
