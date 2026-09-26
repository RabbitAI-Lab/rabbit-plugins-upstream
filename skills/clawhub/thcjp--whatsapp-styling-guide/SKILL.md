---
name: whatsapp-styling-guide
slug: whatsapp-styling-guide
displayName: "WhatsApp Styler"
version: "1.0.0"
summary: "确保发往WhatsApp的消息遵循平台特定格式语法(社区下载版)"
description: "确保发往WhatsApp的消息遵循平台特定格式语法(社区下载版)。Skill to ensure all messages sent to WhatsApp follow the platform's。触发关键词: ensure, whatsapp, sent, styling, guide, styler, messages, skill'。"
license: "MIT"
tools:
  - read
---

# WhatsApp Styler

This skill defines the strict formatting rules for WhatsApp to ensure the user sees clean, styled text without raw markdown symbols.

## Core Syntax Rules

1. *Bold*: Use single asterisks around text: `*texto*`. NEVER use double asterisks `**`.
2. *Italic*: Use single underscores around text: `_texto_`.
3. ~~Strikethrough~~: Use tildes around text: `~texto~`.
4. `Monospace`: Use triple backticks: `texto` (good for code or technical IDs).
5. *Bullet Lists*: Use a single asterisk followed by a space: `* Item`.
6. *Numbered Lists*: Use standard numbers: `1. Item`.
7. *Quotes*: Use the angle bracket: `> texto`.

## Prohibited Patterns (Do NOT use)

* No headers (`#`, `##`, `###`). Use *BOLD CAPS* instead.
* No markdown tables. Use bullet lists for structured data.
* No horizontal rules (`---`). Use a line of underscores if needed `__________`.
* No nested bold/italic symbols if it risks showing raw characters.

## Goal

The goal is a "Human-to-Human" look. Technical but clean.

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

- Skill to ensure all messages sent to WhatsApp follow the platform's
  specific formatting syntax
- 触发关键词: ensure, whatsapp, sent, styling, guide, styler, messages, skill'

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

### Q1: 如何开始使用WhatsApp Styler？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: WhatsApp Styler有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **文本长度**: WhatsApp Styler能够处理的消息长度有限制，通常不超过WhatsApp平台的消息长度限制。超过该长度的文本将被截断，并且格式可能无法完全保留。
- **特殊字符**: 输入中包含的特殊字符可能会影响格式化结果。例如，某些特殊字符在Markdown中具有特殊含义，可能会被错误地格式化。

### 性能边界
- **处理速度**: 对于大量消息的批量处理，WhatsApp Styler可能会受到性能限制，处理速度可能会降低。
- **并发处理**: WhatsApp Styler可能不支持高并发处理大量消息，这可能会影响消息的实时发送。

### 兼容性约束
- **平台兼容性**: WhatsApp Styler主要针对WhatsApp平台设计，可能不适用于其他即时通讯平台。
- **设备兼容性**: WhatsApp Styler的运行依赖于支持SKILL.md的AI Agent，不同设备的兼容性可能存在差异。

### 其他限制
- **外部API限制**: 如果WhatsApp Styler依赖于外部API，那么这些API的限制也会影响到技能的使用。
- **复杂格式处理**: 对于复杂的Markdown格式，WhatsApp Styler可能无法地转换成WhatsApp的格式，需要用户手动调整。
