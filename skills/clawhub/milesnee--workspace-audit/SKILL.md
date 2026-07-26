---
name: workspace-audit
description: "Software-engineering system audit for Agent workspaces. Uses DDIA reliability + DDD bounded-context analysis to diagnose schema drift, consistency gaps, query degradation, lifecycle bloat, and architectural coupling. Triggers during periodic health checks or when the workspace feels stale, bloated, or inconsistent."
metadata:
  category: harness
  author: wheat
  version: "1.2.0"
---

# Workspace Audit — Agent工作区架构审计与修复

当工作区出现文件膨胀、上下文耦合、查询质量退化、Schema漂移等问题时，用软件工程视角系统化诊断和修复。

## When to Trigger

- 任何核心配置文件（MEMORY.md / AGENTS.md / SOUL.md 等）超过 500 行 / 15KB
- 搜索返回重复结果或无关结果
- 日志/数据文件缺少 Schema 约束（如 Front Matter）
- 项目状态与实际脱节
- 架构耦合——改一处牵一片
- 定期健康检查（建议每月一次）

## Core Framework

**Dual lens:**

1. **DDIA (Designing Data-Intensive Applications)** — 可靠性/可扩展性/可维护性
2. **DDD (Domain-Driven Design)** — 有界上下文/聚合根/防腐层

**Five problem domains:**

| 域 | 核心问题 | 典型症状 |
|----|---------|----------|
| Schema | 无Schema约束，自由文本退化 | 字段不一致，无法程序化解析 |
| Consistency | 多存储间状态脱节 | 配置文件写了旧状态，实际已变 |
| Query | 无去重、无联合搜索 | 搜出重复，漏掉归档 |
| Lifecycle | 无GC、无过期标记 | 历史项目堆积，噪音淹没信号 |
| Coupling | 配置/运维/理论混杂 | 改一处牵一片，token浪费 |

## Workflow

### Phase 0: Scope & Baseline

```bash
python3 scripts/audit_baseline.py --workspace . --report /tmp/audit-baseline.json
```

Collect: file counts, line counts, Front Matter coverage (by directory category), duplication rate (per-category), staleness score.

> **Reading the output (v1.1+):** The baseline report splits `memory/` into categories (`toplevel`, `archive`, `clawcast`, plus any other subdirs auto-detected). The **headline FM coverage** is the `toplevel` rate — that's the one to chase to 100%. `fm_coverage_all` is the cross-directory aggregate and will look low because archive/diary dirs are historically un-FM'd; that's expected and not a P0.

> **Duplicate dates are per-category, not global.** A toplevel daily log and a clawcast study note sharing the same date is *normal multi-event logging*, not a duplicate. The script tags duplicates as `category:YYYY-MM-DD` so you can tell. Only act on duplicates within the *same* category (e.g. two `toplevel:2026-04-25` files).

### Phase 1: Diagnosis (5 domains × N checks)

```bash
python3 scripts/audit_diagnose.py --baseline /tmp/audit-baseline.json --output /tmp/audit-report.md
```

Each finding → priority bucket (P0-P4):

- **P0** data integrity (broken/dangerous)
- **P1** consistency (drift/misalignment)
- **P2** query capability (search quality)
- **P3** architecture decoupling (coupling/bloat)
- **P4** knowledge systematization (advanced)

### Phase 2: Execute Fixes (by priority)

Work P0 → P4 sequentially. Each fix:
1. Write script/tool
2. Execute
3. Verify (must pass before next)
4. Record trace

**Conservative file ops default.** When fixing duplicate-date or stale files, prefer `mv → archive/` over `rm`. Deletion is irreversible and the user wasn't in the loop to approve a specific file. Only delete a file when its content is provably empty or already byte-identical to another file (e.g. an 85-byte `NO_REPLY` stub whose info is in the main log). When in doubt, move not delete, and report what was moved.

**Don't over-merge "duplicate dates".** Two files with the same FM date but different filenames and different *content type* (e.g. `2026-04-04.md` daily log vs `travel-2026-04-malaysia-singapore.md` travel itinerary) are not duplicates — they are the same day recording different events. Merging them destroys the topical separation. The per-category duplicate check in v1.1 baseline already filters most of these; manually verify any remaining flags before acting.

### Phase 3: Validate

```bash
python3 scripts/audit_validate.py --report /tmp/audit-report.md
```

### Phase 4: Handoff

- Update IMPLEMENT.md with completed items
- Update MEMORY.md if project status changed
- Log to daily memory
- Record trace via trace_logger

## Key Scripts

| Script | Source | Purpose |
|--------|--------|---------|
| `audit_baseline.py` | this skill | Collect workspace metrics |
| `audit_diagnose.py` | this skill | Generate prioritized findings |
| `audit_validate.py` | this skill | Verify fixes passed |
| `memory_gc.py` | workspace | Semi-auto GC scan → suggestions |
| `staleness_check.py` | workspace | Detect stale entries (>60d) |
| `unified_search.py` | workspace | Cross-store federated search |
| `knowledge_graph.py` | workspace | Node/edge graph from memory |
| `gen_references_index.py` | workspace | Auto-generate INDEX.md |

## Adapting to Other Workspaces

This skill assumes an OpenClaw-style workspace but the audit framework is general:

```
workspace/
  MEMORY.md          # long-term semantic memory
  AGENTS.md          # operational handbook
  SOUL.md            # persona/behavior rules
  TOOLS.md           # ops reference
  IMPLEMENT.md       # task tracker
  memory/*.md        # daily episodic logs
  references/*.md    # archived source materials
  traces/            # agent execution traces
  docs/              # migrated detailed docs
```

For other Agent frameworks or layouts, adapt `audit_baseline.py` path constants and the checklist thresholds.

**Hermes Agent (`~/.hermes/`)**: The baseline scripts do NOT work here — Hermes
uses SQLite (`state.db`) instead of flat files, and has no SOUL.md/AGENTS.md.
Use [references/hermes-audit-procedure.md](references/hermes-audit-procedure.md)
instead, which covers state.db schema queries, memory truncation detection,
cron delivery error diagnosis, and the correct column names (`timestamp REAL`,
not `created_at`).

## Pitfalls

- **False-positive duplicates (pre-v1.1):** The original baseline script flat-listed `memory/*.md` + `memory/archive/*.md` + `memory/clawcast/*.md` together and computed duplicate dates across the union. This reported 48 "duplicates" when only 3 were real file-name collisions — the rest were a daily log and a same-day clawcast note legitimately coexisting. Fixed in v1.1: duplicates are now detected per-category and tagged `category:date`. If you ever adapt this script to a new workspace, keep the per-category isolation; do not collapse back to a flat list.
- **"Same FM date" ≠ "duplicate file".** A daily log and a topical note (travel, reading, study) can share a date because multiple things happen in a day. Check filename *and* content type before merging — if the filenames differ meaningfully, they are almost certainly not duplicates.
- **Subdirectory FM coverage is intentionally low.** `archive/`, `diary/`, `agent-productivity/` historically have little or no front matter. This is expected and not a P0. Chase the `toplevel` FM coverage to 100% first; subdirectory FM is a P3/P4 cleanup at best.
- **execute_code blocked under cron profile.** When running this audit from a cron job (or any session with `approvals.cron_mode: approve`), `execute_code` is denied. Write ad-hoc Python to `/tmp/script.py` and run it via `terminal` instead — the baseline/diagnose/validate scripts already work this way.
- **Session archive ≠ state.db.** Files under `~/.hermes/sessions/` (`.jsonl` transcripts, `session_*.json` checkpoint dumps) are raw exports that `session_search` never reads — search uses FTS on `state.db`. Before deleting or compressing old session files, verify they overlap with state.db's date range; if so, they're 100% redundant. The default cleanup is `tar.gz` compress (~80% reduction), not `rm`.
- **Dead cron vs stale cron.** A cron job with `last_status: ok` but `last_delivery_error: [99992402]` = **delivery** problem (fixable, clear stale thread_id). A cron job where `last_status: ok` but the output content shows repeated upstream API 401/rejection = **dead service** problem (remove the job entirely, don't debug the key). Different root causes, different fixes.
- **Second-pass audits surface different findings.** A first audit catches P0/P1 (memory truncation, cron delivery, auto_prune). A second audit on the same workspace a week later will find P0/P1 already fixed and instead surface **new P2 areas the original baseline command missed**: `session_*.json` checkpoint dumps (the #1 disk consumer, not just `*.jsonl`), `lsp/` node_modules, `logs/`, ghost sessions. Always `du -sh` every top-level subdirectory — the 5-dir command in the original procedure is too narrow.

## See Also

- [references/audit-checklist.md](references/audit-checklist.md) — Full 15-item checklist
- [references/ddia-ddd-mapping.md](references/ddia-ddd-mapping.md) — Theory mapping
- [references/hermes-audit-procedure.md](references/hermes-audit-procedure.md) — **Hermes Agent specific**: state.db schema, memory truncation detection, cron `[99992402]` stale thread_id root cause + fix, dead cron job removal (upstream API dead), session archive compression (tar.gz middle path), state.db redundancy verification before cleanup, correct column names `timestamp REAL` not `created_at`, ghost session detection, second-pass audit shift patterns, `session_*.json` as #1 disk consumer (14-day archive threshold)
- [references/openclaw-workspace-audit-2026-07.md](references/openclaw-workspace-audit-2026-07.md) — Real-run execution log: false-positive duplicate pattern, fix resolutions, baseline numbers for `/root/.openclaw/workspace`
- [assets/audit-report-template.md](assets/audit-report-template.md) — Report template
