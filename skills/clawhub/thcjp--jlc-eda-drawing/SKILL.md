---
slug: jlc-eda-drawing
name: jlc-eda-drawing
version: "0.1.0"
displayName: JLC EDA Drawing
summary: Advanced JLC EDA / EasyEDA circuit design agent for schematic and PCB-ready
  work. Use when the us...
license: MIT-0
description: |-
  Advanced JLC EDA / EasyEDA circuit design agent for schematic and PCB-ready
  work. Use when the us...

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: eda, circuit, easyeda, design, drawing, agent, jlc, advanced
tags:
- Automation
tools:
- read
- exec
---

# JLC EDA Drawing

Act as a circuit-design copilot, not just an API caller. Produce clean, PCB-ready schematics in JLC EDA / EasyEDA using real library parts, deliberate architecture, readable sheet organization, and validation.

## Core Model

Use three layers:

1. **Bridge layer**: connect Codex to the running EasyEDA client.
2. **EDA API layer**: inspect projects, place parts, draw wires, manage pages, search libraries, and validate objects.
3. **Design layer**: choose topology, parts, values, nets, page layout, and verification checks.

Prefer MCP tools when available. Use the official API bridge package only as fallback or for reference.

## Design Intake

Move decisively when the request is clear. Ask one concise question only when a decision changes the circuit materially:

* Input/output voltage or current is unknown for power designs.
* MCU/module variant is ambiguous and affects pins or footprint.
* Connector, package, or mounting style matters mechanically.
* Safety, mains voltage, battery charging, RF, high current, or precision analog is involved.

Otherwise choose conservative defaults and state assumptions at the end.

## Reference Files

Load only what the task needs:

* `references/bridge-api.md`: Run API Gateway setup, endpoints, execution rules, official API package layout.
* `references/design-standards.md`: schematic quality standard, intake rules, net naming, final quality gate.
* `references/parts-strategy.md`: part search patterns and selection rules.
* `references/circuit-blocks.md`: reusable USB-C, regulator, MCU, UART, I2C, SPI, LED block rules.
* `references/eda-code-patterns.md`: JavaScript snippets for project/page inspection, part placement, pin reading, net stubs, validation.
* `references/pcb-workflow.md`: PCB context, units, placement/routing heuristics, DRC workflow.
* `references/examples.md`: concrete user requests and which reference files to load.
* `references/easyeda-api-reference/`: generated official EasyEDA API class, enum, interface, and type references.
* `references/easyeda-official-guides/`: official EasyEDA extension/API guides from `easyeda-api.zip`.
* `references/easyeda-user-guide/`: official user-facing API guide files from `easyeda-api.zip`.
* `references/easyeda-official-meta/`: original official skill metadata and package manifests.
* `scripts/bridge-server.mjs`: bundled official Run API Gateway bridge server script.

## Default Flow

1. Use `references/bridge-api.md` if bridge state or API execution is uncertain.
2. Use `references/design-standards.md` before substantial schematic work.
3. Use `references/parts-strategy.md` when choosing real library parts.
4. Use `references/circuit-blocks.md` for common circuit topologies.
5. Use `references/eda-code-patterns.md` while writing `execute_in_eda` code.
6. Use `references/pcb-workflow.md` for PCB/layout tasks.
7. Use `references/examples.md` when trigger behavior or task shape is unclear.

## Official API References

The official EasyEDA API bundle is split by purpose instead of stored as one raw nested package.

Use it when:

* A method signature is uncertain.
* An enum/interface/type is needed.
* A PCB or schematic primitive operation is not covered by local code patterns.
* The user asks about EasyEDA extension development.
* The user explicitly wants official API behavior.

Lookup order:

1. `references/easyeda-api-reference/_quick-reference.md`
2. `references/easyeda-api-reference/_index.md`
3. Specific files under `references/easyeda-api-reference/classes/`
4. Specific enum/interface/type files under `references/easyeda-api-reference/enums/`, `interfaces/`, or `types/`
5. Extension and usage guides under `references/easyeda-official-guides/` and `references/easyeda-user-guide/`

Do not load the whole official reference set into context. Search it with `rg` and open only the relevant files.

## Quality Gate

Before final response:

* Correct page/document is active.
* Components were actually placed, not only text.
* Critical nets exist by sampling recent wires with `getState_Net()`.
* Power rails and grounds are labelled.
* IC power pins have nearby decoupling or documented assumptions.
* Connectors expose labelled nets.
* The schematic is zoomed to all primitives.

Final response should include:

* Page name.
* Main blocks created.
* Real parts used or notable substitutions.
* Verification performed.
* Any assumptions or risks that matter electrically.

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
