---
slug: cron
name: cron
version: "1.0.0"
displayName: Cron
summary: Local-first recurring schedule engine for reminders, repeated tasks, and
  time-based execution pla...
license: MIT-0
description: |-
  Local-first recurring schedule engine for reminders, repeated tasks,
  and time-based execution pla...

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: schedule, local, engine, cron, recurring
tags:
- Automation
tools:
- read
- exec
---

# Cron

Turn recurring intentions into structured local schedules.

## Core Philosophy

1. Repetition should be captured once, then trusted.
2. A schedule is not just a reminder — it is an execution contract over time.
3. The system should make recurrence visible, editable, and pausable.
4. Users should always know what runs next.

## Runtime Requirements

* Python 3 must be available as `python3`
* No external packages required

## Storage

All data is stored locally only under:

* `~/.skill-platform/workspace/memory/cron/jobs.json`
* `~/.skill-platform/workspace/memory/cron/runs.json`
* `~/.skill-platform/workspace/memory/cron/stats.json`

No external sync. No cloud storage. No third-party cron service.

## Job Status

* `active`: schedule is live
* `paused`: temporarily disabled
* `archived`: no longer active, kept for history

## Schedule Types

* `daily`
* `weekly`
* `monthly`
* `interval`

## Key Workflows

* **Capture recurring job**: `add_job.py`
* **See what runs next**: `next_run.py`
* **Pause or resume**: `pause_job.py`, `resume_job.py`
* **Inspect one job**: `show_job.py`
* **Review all jobs**: `list_jobs.py`

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
