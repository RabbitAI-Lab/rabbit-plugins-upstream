---
slug: obsidian-notesmd-cli
name: obsidian-notesmd-cli
version: "1.0.0"
displayName: Obsidian via notesmd-cli (obsidian-cli)
summary: Work with Obsidian vaults (plain Markdown notes) and automate via notesmd-cli.
license: MIT-0
description: |-
  Work with Obsidian vaults (plain Markdown notes) and automate via notesmd-cli.

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: via, obsidian, notesmd, vaults, plain, notesmd-cli, (obsidian-cli), cli
tags:
- Automation
tools:
- read
- exec
---

# Obsidian via notesmd-cli (obsidian-cli)

Obsidian vault = a normal folder on disk.

Vault structure (typical)

* Notes: `*.md` (plain text Markdown; edit with any editor)
* Config: `.obsidian/` (workspace + plugin settings; usually don’t touch from scripts)
* Canvases: `*.canvas` (JSON)
* Attachments: whatever folder you chose in Obsidian settings (images/PDFs/etc.)

## Find the active vault(s)

Obsidian desktop tracks vaults here (source of truth):

* `~/Library/Application Support/obsidian/obsidian.json`

`notesmd-cli` resolves vaults from that file; vault name is typically the **folder name** (path suffix).

Fast “what vault is active / where are the notes?”

* If you’ve already set a default: `notesmd-cli print-default --path-only`
* Otherwise, read `~/Library/Application Support/obsidian/obsidian.json` and use the vault entry with `"open": true`.

## notesmd-cli quick start

Pick a default vault and open behavior (once):

* `notesmd-cli set-default "<vault-folder-name>"`
* `notesmd-cli set-default --open-type editor` (Sets default to use your terminal/GUI `$EDITOR` instead of opening the Obsidian app)
* `notesmd-cli print-default` / `notesmd-cli print-default --path-only`

Search

* `notesmd-cli search` (Interactive fuzzy search for notes; respects Obsidian's excluded files)
* `notesmd-cli search-content "query"` (Searches inside notes; shows snippets + lines)

Create

* `notesmd-cli create "Folder/New note" --content "..."`
* `notesmd-cli create "New note" --open` (Opens in Obsidian, or `$EDITOR` if `--editor` flag is passed)
* **Note:** Works directly on disk (headless supported); Obsidian does *not* need to be running. Reads `.obsidian/app.json` for default new file locations.

Daily Notes

* `notesmd-cli daily` (Creates or opens today's daily note directly on disk)
* Automatically reads your `.obsidian/daily-notes.json` for folder, format, and template configurations.

Frontmatter (YAML Metadata)

* `notesmd-cli frontmatter "NoteName" --print`
* `notesmd-cli frontmatter "NoteName" --edit --key "status" --value "done"`
* `notesmd-cli frontmatter "NoteName" --delete --key "draft"`

Move/rename (safe refactor)

* `notesmd-cli move "old/path/note" "new/path/note"`
* Updates `[[wikilinks]]` and common Markdown links across the vault (this is the main win vs standard `mv`).

Delete

* `notesmd-cli delete "path/note"`

Prefer direct edits when appropriate: open the `.md` file in any editor (`notesmd-cli open "note" --editor`) and change it; Obsidian will automatically pick it up.

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
