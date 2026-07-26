---
slug: obsidian-1-0-0
name: obsidian-1-0-0
version: "1.0.0"
displayName: Obsidian 1.0.0
summary: Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli.
license: MIT-0
description: |-
  Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli.

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 1.0.0, vaults, plain, obsidian
tags:
- Automation
tools:
- read
- exec
---

# Obsidian 1.0.0

Obsidian vault = a normal folder on disk.

Vault structure (typical)

* Notes: `*.md` (plain text Markdown; edit with any editor)
* Config: `.obsidian/` (workspace + plugin settings; usually don’t touch from scripts)
* Canvases: `*.canvas` (JSON)
* Attachments: whatever folder you chose in Obsidian settings (images/PDFs/etc.)

## Find the active vault(s)

Obsidian desktop tracks vaults here (source of truth):

* `~/Library/Application Support/obsidian/obsidian.json`

`obsidian-cli` resolves vaults from that file; vault name is typically the **folder name** (path suffix).

Fast “what vault is active / where are the notes?”

* If you’ve already set a default: `obsidian-cli print-default --path-only`
* Otherwise, read `~/Library/Application Support/obsidian/obsidian.json` and use the vault entry with `"open": true`.

Notes

* Multiple vaults common (iCloud vs `~/Documents`, work/personal, etc.). Don’t guess; read config.
* Avoid writing hardcoded vault paths into scripts; prefer reading the config or using `print-default`.

## obsidian-cli quick start

Pick a default vault (once):

* `obsidian-cli set-default "<vault-folder-name>"`
* `obsidian-cli print-default` / `obsidian-cli print-default --path-only`

Search

* `obsidian-cli search "query"` (note names)
* `obsidian-cli search-content "query"` (inside notes; shows snippets + lines)

Create

* `obsidian-cli create "Folder/New note" --content "..." --open`
* Requires Obsidian URI handler (`obsidian://…`) working (Obsidian installed).
* Avoid creating notes under “hidden” dot-folders (e.g. `.something/...`) via URI; Obsidian may refuse.

Move/rename (safe refactor)

* `obsidian-cli move "old/path/note" "new/path/note"`
* Updates `[[wikilinks]]` and common Markdown links across the vault (this is the main win vs `mv`).

Delete

* `obsidian-cli delete "path/note"`

Prefer direct edits when appropriate: open the `.md` file and change it; Obsidian will pick it up.

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
