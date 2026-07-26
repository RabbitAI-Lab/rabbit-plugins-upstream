---
slug: cron-worker-guardrails
name: cron-worker-guardrails
version: "1.0.5"
displayName: Cron Worker Guardrails
summary: "Use when: hardening OpenClaw cron/background workers (POSIX shells: bash/sh)
  against brittle quot"
license: MIT
description: |-
  Use when: hardening OpenClaw cron/background workers (POSIX shells:
  bash/sh) against brittle quot...

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: hardening, background, cron, guardrails, openclaw, worker
tags:
- Automation
tools:
- read
- exec
---

# Cron Worker Guardrails

A reliability-first checklist for **Skill平台 cron workers** and any unattended automation.

## Scope (important)

* This skill is **POSIX-focused** (bash/sh examples).
* The *principles* are portable, but if you're on Windows/PowerShell you'll need equivalent patterns.

## The `NO_REPLY` convention

Many Skill平台 setups treat emitting exactly `NO_REPLY` as "silent success" (no human notification).

* If your runtime does not support `NO_REPLY`, interpret it as: **print nothing on success**.

## Quick Start

1. **Scripts-first:** move logic into a repo script (recommended: `tools/<job>.py` or `tools/<job>.sh`).
2. **One command in cron:** cron should run *one short command* (no multi-line `bash -lc '...'`).
3. **Deterministic cwd/env:** `cd` to the repo (or have the script do it), and document required env vars.
4. **Silent on success:** print nothing (or exactly `NO_REPLY`) when OK; only emit a short alert when broken.

Also see:

* `references/cron-agent-contract.md`
* `references/pitfalls.md`

## Why this skill exists

Cron failures are rarely "logic bugs". In practice they're often:

* brittle shell quoting (`bash -lc '...'` nested quotes)
* command substitution surprises (`$(...)`)
* one-liners that hide escaping bugs (`python -c "..."`)
* cwd/env drift ("works locally, fails in cron")
* pipelines that fail for the wrong reason (`pipefail` + `head` / SIGPIPE)

The fix is boring but effective: **scripts-first + deterministic execution + silent-on-success**.

## Portability rules (still apply)

Even on POSIX, do **not** hardcode deployment-specific absolute paths tied to one machine.

Prefer:

* repo-relative paths
* environment variables you document
* minimal wrappers that `cd` into the repo

## Common failure patterns -> fixes

### 1) `unexpected EOF while looking for matching ')'`

Likely causes:

* unclosed `$(...)` from command substitution
* broken nested quotes in `bash -lc ' ... '`

Fix pattern:

* Replace the whole multi-line shell block with a script.
* Cron calls exactly one short command, for example:
  + `python3 tools/<job>.py`

### 2) False failure from `pipefail` + `head` (SIGPIPE)

Symptom:

* command exits non-zero even though the output you wanted is fine

Fix pattern:

* avoid `pipefail` when piping into `head`
* or better: do the filtering in a script (read only what you need)

### 3) "Works locally, fails in cron"

Common causes:

* wrong working directory
* missing env vars
* different PATH

Fix pattern:

* `cd` into the repo (or have the script do it)
* keep dependencies explicit and documented

## Git footgun: `git push` rejected (non-fast-forward)

Symptom:

* `! [rejected] ... (non-fast-forward)` when automation pushes to a **long-lived PR/feature branch**.

Conservative fix (no force-push):

* On rejection, fetch the remote branch, transplant your new local commits onto it (cherry-pick), then retry push once.

## Copy/paste hardening header (portable)

Use this near the top of a cron prompt (2 lines, low-noise):

* **Hardening (MUST):** follow `references/cron-agent-contract.md` (scripts-first, deterministic cwd, silent-on-success).
* Also apply the `cron-worker-guardrails` skill. If parsing/multi-step logic is needed, write/run a small `tools/*.py` script.

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
