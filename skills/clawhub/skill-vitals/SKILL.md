---
name: skill-vitals
description: Audit installed Agent Skills across Claude Code, Codex, OpenClaw, Hermes, and Tencent WorkBuddy. Use when users ask how many skills are installed or active, why a skill did not trigger, which skills can be removed, how much context they consume, whether copies conflict, or whether a skill looks unsafe. 体检已安装 Skills，检查清单、运行时可见性、上下文成本、冲突、触发失败、清理建议与安全风险。
---

# Skill Vitals

Audit an installed skill library and produce an evidence-aware cost-versus-value report with concrete actions.

Keep measured facts, host evidence, estimates, and model judgment separate. Never turn an unavailable field into a guessed value.

For a complete Chinese version of this workflow, read [references/guide.zh-CN.md](references/guide.zh-CN.md) when the user requests Chinese instructions or when Chinese terminology would improve the report.

## 1. Select one host

Run one report per runtime. Never combine context budgets or conflicts across hosts.

```bash
python3 scripts/scan.py --host claude-code --json /tmp/skill-scan.json
python3 scripts/scan.py --host codex --json /tmp/skill-scan.json
python3 scripts/scan.py --host openclaw --json /tmp/skill-scan.json
python3 scripts/scan.py --host hermes --json /tmp/skill-scan.json
python3 scripts/scan.py --host workbuddy --json /tmp/skill-scan.json
```

Use `--path <directory>` when the reported inventory is clearly incomplete. Use `--all` only to diagnose installed copies; do not present its aggregate cost as the active context cost.

### Host evidence

- Claude Code: read plugin state and lifetime per-skill usage from `~/.claude.json`.
- Codex: use the app-server runtime catalog for enabled state, scope, interface, and dependencies. Treat its 2% / 8,000-character fallback budget as an official estimate, not measured prompt usage.
- OpenClaw: use `skills list --eligible --json` for per-instance eligibility, model visibility, source, disabled/allowlist state, and missing dependencies. Include workspace, plugin, shared, and npm-bundled roots. If the CLI fails, report only filesystem candidates.
- WorkBuddy: derive active top-level Skills from the builtin manifest, installed cache version, and welcome mode. Do not promote plugin internals or connector catalog entries to top-level Skills.
- Hermes: use configured and filesystem roots. Mark runtime state and trigger counts unavailable unless the host exposes stronger evidence.

For OpenClaw, use `openclaw_instances` as the grouping authority. Never report a cross-instance duplicate as a shadowing conflict.

## 2. Interpret the scan

The scanner measures deterministic properties. You must judge semantic overlap, likely value, and recommended action.

### Disk is not context

Distinguish:

- installed: a copy exists on disk;
- discoverable: the host can consider it;
- loaded/runtime verified: an authoritative host source confirms visibility or enabled state.

Run budget, conflict, and zombie analysis over the effective host scope. Do not count disabled cache or marketplace copies as active.

### 2.1 Description budget

Report the used amount, assumed/configured limit, percentage, scope, and counted Skills only when the host provides a meaningful budget. Label estimates as estimates.

For Claude Code, explain that bundled Skills may not exist as standalone files and can make actual use higher than the filesystem estimate. For Codex, report the official policy and fallback. For OpenClaw, report its configurable Skill prompt cap when available.

If over budget, recommend both immediate relief and a durable fix:

1. Increase the relevant host limit only as temporary relief.
2. Shorten long descriptions, remove confirmed dead Skills, and sharpen overlapping trigger boundaries.

### 2.2 Context cost

Choose the emphasis by library size:

- 40 or more active Skills: emphasize Tier 1 resident metadata.
- Fewer than 40: emphasize Tier 2 load-on-trigger cost.

Keep these fields distinct:

- `tier2_core_tokens`: body loaded on trigger;
- `tier2_refs_tokens`: references loaded on demand;
- `tier2_max_tokens`: worst case if all references are read.

Splitting a Skill lowers average load cost, not necessarily worst-case cost.

### 2.3 Semantic overlap

Read descriptions and identify Skills that could compete for the same realistic request. For each overlap, provide:

- the competing names;
- one concrete user request that could trigger both;
- an action: merge, narrow boundaries, or add an explicit exclusion.

Do not reduce this to lexical similarity.

### 2.4 Copy and precedence conflicts

Use only conflicts emitted inside the same `conflict_domain`. Distinguish:

- `shadowed_newer`: a newer copy loses to an older effective copy;
- `intentional_override`: a higher-priority copy appears intentional;
- `redundant`: byte-identical copies.

Before recommending deletion, explain which copy is effective and provide both paths.

### 2.5 Trigger evidence

Use real host counters only. For Claude Code, `skillUsage` is lifetime data, not a rolling 30-day window. If trigger data is unavailable, say so and omit zombie claims.

Apply the age gate before calling a zero-trigger Skill a zombie. Treat recently installed Skills as too new to judge. Never substitute install time or mtime for usage.

Use `scripts/probe_logs.py --host openclaw --deep` only for hosts without a native usage source. It deduplicates observed `read` calls to `SKILL.md`, but those reads may come from inspection or debugging rather than automatic activation. Report them as indirect `observed_skill_reads`; never copy them into `usage_count` or use them alone for zombie decisions.

### 2.6 Structure

Prioritize:

- missing or invalid frontmatter;
- missing name or description;
- excessively long descriptions;
- oversized core bodies that should route to references;
- large data corpora that should remain on-demand.

Give a specific refactor boundary instead of saying only “split this Skill.”

### 2.7 Security

Review every flagged line manually. The scanner uses heuristics and can both miss attacks and flag defensive examples.

Explain findings in plain language:

- adversarial instruction: attempts to override prior instructions or hide actions;
- pipe/base64 execution: remote or encoded content executed directly by a shell;
- raw-IP fetch: content downloaded from an unverified numeric endpoint;
- password archive: an archive that may evade inspection;
- hardcoded secret: credentials embedded in files;
- credential read: access to `.env`, AWS, SSH, or similar secrets.

Treat `cited=true` only as a review-order hint. It must never suppress or downgrade a finding. Include file paths, line numbers, and short snippets for serious findings.

## 3. Recommend actions

Order recommendations as follows:

1. Fix blocking visibility, budget, overlap, and precedence problems.
2. Review security findings.
3. Reduce expensive Skill bodies and descriptions.
4. Remove only Skills supported by real inactivity evidence and sufficient age.
5. Improve output quality only after confirming the effective Skill is actually selected.

Do not delete or disable Skills unless the user explicitly asks.

When evaluating quality, build validation cases from real usage. Do not invent expected outputs. Preserve a holdout set and check newly introduced failures after each change.

## 4. Report format

Lead with the conclusion, then evidence:

```markdown
# Skill health report

## Critical finding
Only include this first when budget overflow, a high-severity conflict, or a serious security finding exists.

## Overview
Host and instance · installed N · active/runtime-verified M · estimated Tier 1 cost · evidence availability

## Immediate actions
1. Concrete action with Skill name and path

## Context cost
Highest-cost Skills with core/reference/worst-case distinctions

## Conflicts and semantic overlap
Effective copy, shadowed copies, and realistic competing prompts

## Usage evidence
Measured counters or an explicit unavailable statement

## Security and structure
Reviewed findings with file and line evidence

## Recommended disposition
Keep · revise · merge · disable/delete after confirmation
```

Every recommendation must be executable and name the affected Skill. Mark token counts as estimates, trigger counters as measurements, and semantic overlap as model judgment.

## Limitations

- Token counts are estimates and differ from the host tokenizer.
- Runtime catalogs prove visibility or eligibility, not output quality or actual invocation history.
- Codex, OpenClaw, Hermes, and WorkBuddy currently lack an equivalent to Claude Code's per-Skill lifetime counter.
- OpenClaw CLI failure leaves only filesystem candidates; do not call them loaded.
- WorkBuddy activity is inferred from manifest/cache/mode evidence, not invocation records.
- Security rules are heuristic and cannot establish that a Skill is safe.
- Files outside recognized reference directories may be classified as corpus data.
- Filesystem creation age can be inaccurate, especially on Linux.
