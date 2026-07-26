---
slug: node-red-manager
name: node-red-manager
version: "1.0.0"
displayName: Node Red Manager
summary: Manage Node-RED instances via Admin API or CLI. Automate flow deployment,
  install nodes, and trou...
license: MIT
description: |-
  Manage Node-RED instances via Admin API or CLI. Automate flow deployment,
  install nodes, and trou...

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: node, red, admin, manager, manage, instances, automate
tags: '[''Automation'', ''Operations'']'
tools: '[read, exec]'
---

# Node Red Manager

## Setup

1. Copy `.env.example` to `.env`.
2. Set `NODE_RED_URL`, `NODE_RED_USERNAME`, and `NODE_RED_PASSWORD` in `.env`.
3. The script automatically handles dependencies on first run.

## Infrastructure

* **Stack Location**: `deployments/node-red`
* **Data Volume**: `deployments/node-red/data`
* **Docker Service**: `mema-node-red`
* **URL**: `https://flow.glassgallery.my.id`

## Usage

### Flow Management

```bash
scripts/nr list-flows

scripts/nr get-flow <flow-id>

scripts/nr deploy --file assets/flows/watchdog.json

scripts/nr update-flow <flow-id> --file updated-flow.json

scripts/nr delete-flow <flow-id>

scripts/nr get-flow-state

scripts/nr set-flow-state --file state.json
```

### Backup & Restore

```bash
scripts/nr backup
scripts/nr backup --output my-backup.json

scripts/nr restore node-red-backup-20260210_120000.json
```

### Node Management

```bash
scripts/nr list-nodes

scripts/nr install-node node-red-contrib-http-request

scripts/nr get-node node-red-contrib-http-request

scripts/nr enable-node node-red-contrib-http-request
scripts/nr disable-node node-red-contrib-http-request

scripts/nr remove-node node-red-contrib-http-request
```

### Runtime Information

```bash
scripts/nr get-settings

scripts/nr get-diagnostics
```

### Context Management

```bash
scripts/nr get-context flow my-key
scripts/nr get-context global shared-data

scripts/nr set-context flow my-key '"value"'
scripts/nr set-context global counter '42'
scripts/nr set-context global config '{"key": "value"}'
```

## Docker Operations

```bash
cd deployments/node-red && docker compose restart

docker logs mema-node-red --tail 100

docker logs -f mema-node-red
```

## Environment Variables

* `NODE_RED_URL`: Node-RED API endpoint (default: `http://localhost:1880`)
* `NODE_RED_USERNAME`: Admin username
* `NODE_RED_PASSWORD`: Admin password

Legacy variable names (`NR_URL`, `NR_USER`, `NR_PASS`) are supported for backward compatibility.

## API Reference

See `references/admin-api.md` for complete Admin API endpoint documentation.

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
