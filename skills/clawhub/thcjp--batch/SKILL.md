---
slug: batch
name: batch
version: "1.0.0"
displayName: Batch
summary: Process multiple items with progress tracking, checkpointing, and failure
  recovery.
license: MIT
description: |-
  Process multiple items with progress tracking, checkpointing, and failure
  recovery.

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: items, progress, batch, multiple, process
tags:
- Automation
tools:
- read
- exec
---

# Batch

## Before Starting

1. **Dry run:** Test with 2-3 items first
2. **Count:** "Processing 47 items, ~2 min estimated"
3. **Confirm destructive ops:** "This will delete 200 files. Proceed?"

## During Processing

* **Progress every 10 items:** "23/47 complete (49%)"
* **Checkpoint every 10-50 items:** Save state to resume if interrupted
* **On error:** Log it, continue with rest (don't abort entire batch)

## After Completion

Always report:

```text
✅ 44 succeeded
❌ 3 failed (saved to failed.json for retry)
```

## Error Handling

| Error | Action |
| --- | --- |
| Timeout, rate limit | Retry 3x with backoff (1s, 2s, 4s) |
| Bad format, missing data | Skip, log, continue |
| Auth failed, disk full | Abort entire batch |

Check `strategies.md` for parallel vs sequential decision matrix.
Check `errors.md` for retry logic and rollback patterns.

---

**Related:** For delegating to sub-agents, see `delegate`.

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
