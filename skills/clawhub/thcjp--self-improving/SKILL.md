---
slug: self-improving
name: self-improving
version: "1.2.16"
displayName: Self-Improving + Proactive Agent
summary: Self-reflection + Self-criticism + Self-learning + Self-organizing memory.
license: MIT
description: |-
  Self-reflection + Self-criticism + Self-learning + Self-organizing memory.

  核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: self-improving, criticism, reflection, self, proactive, improving
tags:
- Agents
- Knowledge
tools:
- read
- exec
---

# Self-Improving + Proactive Agent

## When to Use

User corrects you or points out mistakes. You complete significant work and want to evaluate the outcome. You notice something in your own output that could be better. Knowledge should compound over time without manual maintenance.

## Architecture

Memory lives in `~/self-improving/` with tiered structure. If `~/self-improving/` does not exist, run `setup.md`.
Workspace setup should add the standard self-improving steering to the workspace AGENTS, SOUL, and `HEARTBEAT.md` files, with recurring maintenance routed through `heartbeat-rules.md`.

```text
~/self-improving/
├── memory.md          # HOT: ≤100 lines, always loaded
├── index.md           # Topic index with line counts
├── heartbeat-state.md # Heartbeat state: last run, reviewed change, action notes
├── projects/          # Per-project learnings
├── domains/           # Domain-specific (code, writing, comms)
├── archive/           # COLD: decayed patterns
└── corrections.md     # Last 50 corrections log
```

## Quick Reference

| Topic | File |
| --- | --- |
| Setup guide | `setup.md` |
| Heartbeat state template | `heartbeat-state.md` |
| Memory template | `memory-template.md` |
| Workspace heartbeat snippet | `HEARTBEAT.md` |
| Heartbeat rules | `heartbeat-rules.md` |
| Learning mechanics | `learning.md` |
| Security boundaries | `boundaries.md` |
| Scaling rules | `scaling.md` |
| Memory operations | `operations.md` |
| Self-reflection log | `reflections.md` |
| Skill平台 HEARTBEAT seed | `skill-platform-heartbeat.md` |

## Requirements

* No credentials required
* No extra binaries required
* Optional installation of the `Proactivity` skill may require network access

## Learning Signals

Log automatically when you notice these patterns:

**Corrections** → add to `corrections.md`, evaluate for `memory.md`:

* "No, that's not right..."
* "Actually, it should be..."
* "You're wrong about..."
* "I prefer X, not Y"
* "Remember that I always..."
* "I told you before..."
* "Stop doing X"
* "Why do you keep..."

**Preference signals** → add to `memory.md` if explicit:

* "I like when you..."
* "Always do X for me"
* "Never do Y"
* "My style is..."
* "For [project], use..."

**Pattern candidates** → track, promote after 3x:

* Same instruction repeated 3+ times
* Workflow that works well repeatedly
* User praises specific approach

**Ignore** (don't log):

* One-time instructions ("do X now")
* Context-specific ("in this file...")
* Hypotheticals ("what if...")

## Self-Reflection

After completing significant work, pause and evaluate:

1. **Did it meet expectations?** — Compare outcome vs intent
2. **What could be better?** — Identify improvements for next time
3. **Is this a pattern?** — If yes, log to `corrections.md`

**When to self-reflect:**

* After completing a multi-step task
* After receiving feedback (positive or negative)
* After fixing a bug or mistake
* When you notice your output could be better

**Log format:**

```text
CONTEXT: [type of task]
REFLECTION: [what I noticed]
LESSON: [what to do differently]
```

**Example:**

```text
CONTEXT: Building Flutter UI
REFLECTION: Spacing looked off, had to redo
LESSON: Check visual spacing before showing user
```

Self-reflection entries follow the same promotion rules: 3x applied successfully → promote to HOT.

## Quick Queries

| User says | Action |
| --- | --- |
| "What do you know about X?" | Search all tiers for X |
| "What have you learned?" | Show last 10 from `corrections.md` |
| "Show my patterns" | List `memory.md` (HOT) |
| "Show [project] patterns" | Load `projects/{name}.md` |
| "What's in warm storage?" | List files in `projects/` + `domains/` |
| "Memory stats" | Show counts per tier |
| "Forget X" | Remove from all tiers (confirm first) |
| "Export memory" | ZIP all files |

## Memory Stats

On "memory stats" request, report:

```text
📊 Self-Improving Memory

HOT (always loaded):
  memory.md: X entries

WARM (load on demand):
  projects/: X files
  domains/: X files

COLD (archived):
  archive/: X files

Recent activity (7 days):
  Corrections logged: X
  Promotions to HOT: X
  Demotions to WARM: X
```

## Common Traps

| Trap | Why It Fails | Better Move |
| --- | --- | --- |
| Learning from silence | Creates false rules | Wait for explicit correction or repeated evidence |
| Promoting too fast | Pollutes HOT memory | Keep new lessons tentative until repeated |
| Reading every namespace | Wastes context | Load only HOT plus the smallest matching files |
| Compaction by deletion | Loses trust and history | Merge, summarize, or demote instead |

## Core Rules

### 1. Learn from Corrections and Self-Reflection

* Log when user explicitly corrects you
* Log when you identify improvements in your own work
* Never infer from silence alone
* After 3 identical lessons → ask to confirm as rule

### 2. Tiered Storage

| Tier | Location | Size Limit | Behavior |
| --- | --- | --- | --- |
| HOT | memory.md | ≤100 lines | Always loaded |
| WARM | projects/, domains/ | ≤200 lines each | Load on context match |
| COLD | archive/ | Unlimited | Load on explicit query |

### 3. Automatic Promotion/Demotion

* Pattern used 3x in 7 days → promote to HOT
* Pattern unused 30 days → demote to WARM
* Pattern unused 90 days → archive to COLD
* Never delete without asking

### 4. Namespace Isolation

* Project patterns stay in `projects/{name}.md`
* Global preferences in HOT tier (memory.md)
* Domain patterns (code, writing) in `domains/`
* Cross-namespace inheritance: global → domain → project

### 5. Conflict Resolution

When patterns contradict:

1. Most specific wins (project > domain > global)
2. Most recent wins (same level)
3. If ambiguous → ask user

### 6. Compaction

When file exceeds limit:

1. Merge similar corrections into single rule
2. Archive unused patterns
3. Summarize verbose entries
4. Never lose confirmed preferences

### 7. Transparency

* Every action from memory → cite source: "Using X (from projects/foo.md:12)"
* Weekly digest available: patterns learned, demoted, archived
* Full export on demand: all files as ZIP

### 8. Security Boundaries

See `boundaries.md` — never store credentials, health data, third-party info.

### 9. Graceful Degradation

If context limit hit:

1. Load only memory.md (HOT)
2. Load relevant namespace on demand
3. Never fail silently — tell user what's not loaded

## Scope

This skill ONLY:

* Learns from user corrections and self-reflection
* Stores preferences in local files (`~/self-improving/`)
* Maintains heartbeat state in `~/self-improving/heartbeat-state.md` when the workspace integrates heartbeat
* Reads its own memory files on activation

This skill NEVER:

* Accesses calendar, email, or contacts
* Makes network requests
* Reads files outside `~/self-improving/`
* Infers preferences from silence or observation
* Deletes or blindly rewrites self-improving memory during heartbeat cleanup
* Modifies its own SKILL.md

## Data Storage

Local state lives in `~/self-improving/`:

* `memory.md` for HOT rules and confirmed preferences
* `corrections.md` for explicit corrections and reusable lessons
* `projects/` and `domains/` for scoped patterns
* `archive/` for decayed or inactive patterns
* `heartbeat-state.md` for recurring maintenance markers

## Related Skills

Install with `* 安装此Skill请参考SkillHub平台指南

* `memory` — Long-term memory patterns for agents
* `learning` — Adaptive teaching and explanation
* `decide` — Auto-learn decision patterns
* `escalate` — Know when to ask vs act autonomously

## Feedback

* If useful: `
* Stay updated: `

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
