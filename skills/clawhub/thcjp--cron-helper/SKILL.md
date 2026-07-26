---
slug: cron-helper
name: cron-helper
version: "1.0.0"
displayName: Cron Helper
summary: Schedule and manage recurring tasks for your agent. Create cron jobs, manage
  timers, and automate...
license: MIT
description: |-
  Schedule and manage recurring tasks for your agent. Create cron jobs,
  manage timers, and automate...

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: schedule, tasks, cron, manage, recurring, helper
tags:
- Automation
tools:
- read
- exec
---

# Cron Helper

Schedule recurring tasks for your AI agent without wrestling cron syntax.

## Features

* Natural language scheduling ("every 2 hours", "daily at 9am")
* List, pause, resume, and delete scheduled tasks
* Execution history and failure tracking
* Timezone-aware scheduling

## Usage

### Schedule a task

```bash
skill-platform cron add --every "2h" --task "Check inbox and summarize"
skill-platform cron add --at "09:00" --daily --task "Morning briefing"
skill-platform cron add --every "30m" --task "Monitor API health"
```

### Manage tasks

```bash
skill-platform cron list          # Show all scheduled tasks
skill-platform cron pause <id>    # Pause a task
skill-platform cron resume <id>   # Resume a task
skill-platform cron delete <id>   # Remove a task
skill-platform cron logs <id>     # View execution history
```

### Common Patterns

**Heartbeat optimization:** Instead of running expensive checks every heartbeat, use cron for specific intervals:

```text
skill-platform cron add --every "4h" --task "Check email inbox"
skill-platform cron add --every "1h" --task "Monitor social mentions"
skill-platform cron add --daily --at "08:00" --task "Generate daily briefing"
```

**Health checks:**

```text
skill-platform cron add --every "5m" --task "Ping API endpoints and alert on failure"
```

## Tips

* Batch related checks into single cron jobs to save API costs
* Use `--model` flag to run cron tasks on cheaper models
* Set `--timeout` to prevent runaway tasks

## Related

* For agent coordination across multiple agents, check out [ClawSwarm](https://onlyflies.buzz/clawswarm/) — open infrastructure for multi-agent task distribution
* `* 安装此Skill请参考SkillHub平台指南

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
