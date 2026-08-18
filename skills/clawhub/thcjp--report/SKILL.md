---
name: report
slug: report
displayName: "Report"
version: "1.0.3"
summary: "配置自定义定期报告,用户定义数据源,技能负责调度与格式化,自动化报表生成"
description: "配置自定义定期报告,用户定义数据源,技能负责调度与格式化,自动化报表生成。Configure custom recurring reports。User defines data sources, skill。触发关键词: custom, report, configure, recurring, reports。"
license: "MIT"
tools:
  - read
---

> **核心功能**: 本技能提供化报表生成等能力。


# Report

## Data Storage

```text
~/report/
├── memory.md               # Index + preferences
├── {name}/
│   ├── config.md           # Report configuration
│   ├── data.jsonl          # Historical data
│   └── generated/          # Past reports
```

Create on first use: `mkdir -p ~/report`

## Scope

This skill:

* ✅ Stores report configurations in ~/report/
* ✅ Generates reports on schedule
* ✅ Delivers via channels user configures

**User-driven model:**

* User defines WHAT data to include
* User grants access to any needed sources
* User provides API keys if external data needed
* Skill handles SCHEDULING and FORMATTING

This skill does NOT:

* ❌ Access APIs without user-provided credentials
* ❌ Pull data from sources user hasn't specified
* ❌ Store credentials (user provides via environment)

## Environment Variables

**No fixed requirements.** User provides API keys as needed:

```bash
export STRIPE_API_KEY="${API_KEY:?请设置环境变量}"

export GITHUB_TOKEN="[REDACTED]"
```

Config references env var name, never the value.

## Delivery Security

External delivery (Telegram/webhook/email) sends report content off-device.

* User explicitly configures each channel
* User responsible for trusting destination
* `file` delivery stays local (~/report/{name}/generated/)

## Quick Reference

| Task | File |
| --- | --- |
| Configuration schema | `schema.md` |
| Output formats | `formats.md` |
| Delivery options | `delivery.md` |

## Core Rules

### 1. User Defines Data Sources

When creating a report:

1. User specifies what data to track
2. If external API needed, user provides credentials
3. Credentials stored as env var references, not values

Example:

```text
User: "Weekly report on my Stripe revenue"
Agent: "I'll need Stripe API access. Please set
        STRIPE_API_KEY in your environment."
User: "Done"
→ Config stored with "source": {"type": "api", "env": "STRIPE_API_KEY"}
```

### 2. Report Configuration

In ~/report/{name}/config.md:

```yaml
name: weekly-revenue
schedule: "0 9 * * 1"  # Monday 9am
sources:
  - type: api
    env: STRIPE_API_KEY  # User provides
format: chat
delivery: telegram
```

### 3. Scheduling

| Frequency | Cron | Example |
| --- | --- | --- |
| Daily | `0 9 * * *` | 9am daily |
| Weekly | `0 9 * * 1` | Monday 9am |
| Monthly | `0 9 1 * *` | 1st of month |
| On-demand | - | When user asks |

### 4. Delivery Channels

User configures in config.md:

* `chat` — Reply in conversation
* `telegram` — Send to Telegram (user provides chat ID)
* `file` — Save to ~/report/{name}/generated/
* `email` — Send via user's configured mail

### 5. Managing Reports

```text
"List my reports" → Read ~/report/memory.md
"Pause X report" → Update config
"Run X now" → Generate on-demand
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent( Code / Cursor / Codex /  CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+execute(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Configure custom recurring reports
- User defines data sources, skill
  handles scheduling and forma
- 触发关键词: custom, report, configure, recurring, reports

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Report？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Report有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制

* **数据量限制**：Report技能能够处理的数据量受限于Agent平台的内存和存储资源。对于大规模数据源，可能需要分批处理或使用更强大的数据处理工具。
* **数据格式限制**：技能目前支持JSON Lines (.jsonl) 格式的数据文件，对于其他格式的数据，需要用户进行转换。
* **API调用限制**：对于需要API调用的数据源，技能的调用频率受到API提供商的限制，用户需要遵守这些限制。

### 性能边界

* **处理速度**：Report技能的执行速度取决于数据源的大小和复杂性，以及Agent平台的性能。
* **并发处理**：技能不支持同时处理多个报告，每次只能处理一个报告。

### 兼容性约束

* **操作系统**：技能在Windows、macOS和Linux操作系统上运行，但可能存在特定版本的兼容性问题。
* **Agent平台**：技能依赖于支持SKILL.md的AI Agent平台，不同平台的实现细节可能有所不同。
* **外部API**：技能依赖于外部API提供的数据，如果API发生变更或不可用，技能的功能可能会受到影响。

### 其他限制

* **实时数据处理**：Report技能不适用于实时流数据处理，它更适合处理定期生成的数据。
* **复杂逻辑处理**：技能不支持复杂的逻辑处理，对于需要复杂逻辑的场景，可能需要用户自行编写脚本或使用其他工具。
