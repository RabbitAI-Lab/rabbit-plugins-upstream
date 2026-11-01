---
name: memory-audit
description: "Audit and repair agent memory systems using DDIA reliability + DDD bounded-context analysis. Triggers when memory feels stale, bloated, inconsistent, or during periodic health checks."
metadata:
  category: harness
  author: wheat
  version: "1.0.0"
---

# Memory Audit — 记忆系统架构审计与修复

当记忆系统出现膨胀、不一致、查询质量差、架构耦合等问题时，用软件工程视角系统化诊断和修复。

## When to Trigger

- MEMORY.md 或 AGENTS.md 超过 500 行 / 15KB
- 搜索返回重复结果或无关结果
- 日志文件缺少 Front Matter
- 项目状态与实际脱节
- 定期健康检查（建议每月一次）

## Core Framework

**Dual lens:**

1. **DDIA (Designing Data-Intensive Applications)** — 可靠性/可扩展性/可维护性
2. **DDD (Domain-Driven Design)** — 有界上下文/聚合根/防腐层

**Five problem domains:**

| 域 | 核心问题 | 典型症状 |
|----|---------|---------|
| Schema | 无Schema约束，自由文本退化 | 字段不一致，无法程序化解析 |
| Consistency | 多存储间状态脱节 | MEMORY.md写了旧模型，实际已换 |
| Query | 无去重、无联合搜索 | 搜出重复，漏掉归档 |
| Lifecycle | 无GC、无过期标记 | 历史项目堆积，噪音淹没信号 |
| Coupling | 配置/运维/理论混杂 | 改一处牵一片，token浪费 |

## Workflow

### Phase 0: Scope & Baseline

```bash
python3 scripts/audit_baseline.py --workspace . --report /tmp/audit-baseline.json
```

Collect: file counts, line counts, Front Matter coverage, duplication rate, staleness score.

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

This skill assumes an OpenClaw-style workspace:

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

For other layouts, adapt `audit_baseline.py` path constants.

## See Also

- [references/audit-checklist.md](references/audit-checklist.md) — Full 15-item checklist
- [references/ddia-ddd-mapping.md](references/ddia-ddd-mapping.md) — Theory mapping
- [assets/audit-report-template.md](assets/audit-report-template.md) — Report template
