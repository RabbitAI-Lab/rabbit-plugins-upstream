# yuque-docs-skill

[English](#english) | [中文](#中文)

---

## 中文

**yuque-docs-skill** 是一个兼容多平台的 Agent Skill，通过语雀 OpenAPI 全面操作语雀知识库文档，支持创建、更新、删除、拉取、智能增量同步等。

### 功能

| 类别 | 能力 |
|------|------|
| **读** | 列出知识库所有文档、获取单篇文档详情、查看目录结构（TOC）、拉取云端文档到本地 Markdown 文件、状态对比（本地与云端差异） |
| **写** | 推送本地 Markdown 创建新文档（自动加入 TOC）、覆盖或追加更新已有文档、智能增量同步（只推送有改动的文档） |
| **管理** | 删除文档、智能 sync 状态管理（`.yuque-sync.json`）、layout 自动检测（flat / nested / frontmatter） |

所有操作通过本地 Python CLI 脚本完成，无需 MCP Server，Token 不会写入代码。

### 快速开始

**1. 安装 Skill**

**用户级安装**（推荐，所有项目均可使用）：

macOS / Linux：
```bash
git clone https://github.com/CPsean/yuque-docs-skill \
  ~/.claude/skills/yuque-docs-skill
```

Windows（PowerShell）：
```powershell
git clone https://github.com/CPsean/yuque-docs-skill `
  "$env:USERPROFILE\.claude\skills\yuque-docs-skill"
```

**项目级安装**（仅当前项目可用）：

```bash
git clone https://github.com/CPsean/yuque-docs-skill \
  .claude/skills/yuque-docs-skill
```

安装后重启 Claude Code 使 Skill 生效。

**2. 安装依赖**

```bash
pip install requests python-dotenv
```

**3. 配置凭据**

首次使用时，Skill 会引导你完成配置：

1. 打开你的语雀知识库，复制地址栏 URL（格式类似 `https://xxx.yuque.com/group/book`）
2. 前往 [语雀 Token 页面](https://www.yuque.com/settings/tokens) 创建 Token，授予目标知识库读写权限
3. 将 URL 和 Token 提供给 Claude，Skill 会自动运行：
   ```bash
   python scripts/yuque_cli.py setup --url "<URL>" --token "<token>"
   ```

**4.（可选）验证连接**

```bash
python scripts/yuque_cli.py list
```

### 使用示例

直接用自然语言和 Claude 对话即可：

- *"把 `docs/design.md` 推送到我的语雀知识库"*
- *"用本地最新版本更新语雀上的 PRD 文档"*
- *"列出我语雀知识库里的所有文档"*
- *"把语雀上的会议纪要拉取到本地"*
- *"同步本地所有改动到语雀"*
- *"查看语雀知识库的目录结构"*

### 工作流程

```
用户请求
  → Skill 激活（通过 description 触发词匹配）
  → 命令映射（create / update / sync / pull / delete ...）
  → 执行前确认（所有写操作需用户确认）
  → 语雀 OpenAPI
  → 返回结果：文档 ID + 标题 + slug
```

### 已知限制

| 限制项 | 详情 |
|---|---|
| **TOC 位置** | `create` 默认将文档追加到知识库根节点，无法通过 Skill 指定父节点或插入位置，需在语雀 Web 编辑器中手动调整。 |
| **Lake 格式** | 语雀 Lake 是私有富文本格式。始终使用 `--format markdown`，除非用户明确需要 Lake 格式。 |
| **远端草稿** | `sync` 基于已发布版本检测变更，不感知 Web 编辑器中的未发布草稿。如怀疑有草稿，先 `pull` 查看。 |
| **批量迁移** | 不支持跨知识库批量迁移，也不支持管理语雀团队成员或权限。 |

### 安全性

- API Token 仅写入项目根目录 `.env` 文件，**不会提交到版本控制**（setup 命令自动检查 `.gitignore`）
- Token 不会出现在任何命令输出或 Claude 的回复中
- 删除操作需要显式传 `--confirm` 且用户明确确认后才执行

### 文件结构

```
.claude/skills/yuque-docs-skill/
├── SKILL.md                  # Skill 入口（触发器 + 指令）
├── README.md                 # 本文件
├── evals/
│   ├── evals.json            # 任务执行测评
│   └── trigger-evals.json    # 触发边界测评
├── references/
│   └── yuque-cli.md          # CLI 命令速查表
├── scripts/
│   └── yuque_cli.py          # Python CLI 工具本体
└── tests/
    └── test_yuque_sync_fixes.py  # 功能测试
```

### 更新日志

#### 2025-07-12 迭代

- **标题提取优化**：`sync` 推送时标题优先级链改为 frontmatter `title` → H1 → 文件名 → slug，无 H1 时使用文件名而非英文 slug
- **标题同步**：`sync` 更新文档时同步传入标题字段
- **--force-title 参数**：新增 `--force-title` 标志，强制使用文件名作标题
- **标题回退告警**：`status` 输出新增 "Title fallback" 段落，列出回退到文件名/slug 的文档
- **文档间链接重写**：推送前自动将 `[文字](文件名.md)` 转为 `[文字](slug)`，未匹配链接保留并告警
- **反向链接转换**：`pull` 时自动将 slug 链接转回文件名格式
- **加粗格式修复**：推送前自动在 `**标签：**` 后插入空格以修复语雀渲染
- **frontmatter 剥离**：`create`/`update` 使用 `--body-file` 时自动剥离 YAML frontmatter
- **功能测试**：新增 `tests/test_yuque_sync_fixes.py` 覆盖全部 9 个需求

---

## English

**yuque-docs-skill** is a cross-platform Agent Skill for reading, pushing, syncing, and managing documents in a [Yuque](https://www.yuque.com) knowledge base via the Yuque OpenAPI.

### Features

| Category | Capabilities |
|----------|-------------|
| **Read** | List all documents, get document details, inspect TOC, pull cloud docs to local Markdown files, compare local vs. remote status |
| **Write** | Push local Markdown to create documents (auto-added to TOC), overwrite or append updates, smart incremental sync (push only changed docs) |
| **Manage** | Delete documents, sync state management (`.yuque-sync.json`), auto layout detection (flat / nested / frontmatter) |

All operations go through a local Python CLI script — no MCP server needed, no API keys in code.

### Quick Start

**1. Install the Skill**

**User-level install** (recommended — available across all projects):

macOS / Linux:
```bash
git clone https://github.com/CPsean/yuque-docs-skill \
  ~/.claude/skills/yuque-docs-skill
```

Windows (PowerShell):
```powershell
git clone https://github.com/CPsean/yuque-docs-skill `
  "$env:USERPROFILE\.claude\skills\yuque-docs-skill"
```

**Project-level install** (current project only):

```bash
git clone https://github.com/CPsean/yuque-docs-skill \
  .claude/skills/yuque-docs-skill
```

Restart Claude Code after installing to load the skill.

**2. Install dependencies**

```bash
pip install requests python-dotenv
```

**3. Configure credentials**

On first use, the skill will guide you through setup:

1. Open your Yuque knowledge base and copy the URL from the address bar (e.g. `https://xxx.yuque.com/group/book`)
2. Go to the [Yuque Token page](https://www.yuque.com/settings/tokens) and create a token with read/write access to your knowledge base
3. Paste the URL and token to Claude — the skill runs automatically:
   ```bash
   python scripts/yuque_cli.py setup --url "<URL>" --token "<token>"
   ```

**4. (Optional) Verify connection**

```bash
python scripts/yuque_cli.py list
```

### Usage Examples

Just talk to Claude naturally:

- *"Push `docs/design.md` to my Yuque knowledge base"*
- *"Update the PRD document on Yuque with the latest local version"*
- *"List all documents in my knowledge base"*
- *"Pull the meeting notes from Yuque to local"*
- *"Sync all local changes to Yuque"*
- *"Show the table of contents of my Yuque book"*

### How It Works

```
User request
  → Skill activation (matched by description trigger)
  → Command mapping (create / update / sync / pull / delete ...)
  → Pre-execution confirmation (for all write operations)
  → Yuque OpenAPI
  → Result: document ID + title + slug
```

### Known Limitations

| Limitation | Detail |
|---|---|
| **TOC position** | `create` appends documents to the knowledge base root — no way to specify a parent node or insert position via this skill. Reorder manually in the Yuque web editor. |
| **Lake format** | Yuque Lake is a proprietary rich-text format. Always use `--format markdown` unless the user explicitly needs Lake. |
| **Remote drafts** | `sync` detects changes based on the last published version and does not see unpublished web-editor drafts. Use `pull` to inspect first if in doubt. |
| **Batch migration** | Cross-repo migration, team member management, and permission management are out of scope. |

### Security

- API token is written only to the project-local `.env` file — **never committed to version control** (the setup command checks `.gitignore` automatically)
- Token never appears in command output or Claude's responses
- Delete operations require explicit `--confirm` flag and unambiguous user approval before execution

### File Structure

```
.claude/skills/yuque-docs-skill/
├── SKILL.md                  # Skill entry point (trigger + instructions)
├── README.md                 # This file
├── evals/
│   ├── evals.json            # Task execution evals
│   └── trigger-evals.json    # Trigger boundary evals
├── references/
│   └── yuque-cli.md          # CLI command reference
├── scripts/
│   └── yuque_cli.py          # Python CLI implementation
└── tests/
    └── test_yuque_sync_fixes.py  # Functional tests
```

### Changelog

#### 2025-07-12 Iteration

- **Title extraction**: Priority chain changed to frontmatter `title` → H1 → file name → slug; falls back to file name instead of English slug when no H1 is present
- **Title sync**: `sync` now passes the title field when updating documents
- **--force-title flag**: New `--force-title` flag forces using the file name as the title
- **Title fallback warning**: `status` output now includes a "Title fallback" section listing docs that fell back to file name/slug
- **Inter-document link rewriting**: `[text](file.md)` links are automatically converted to `[text](slug)` before push; unresolved links are kept and reported as warnings
- **Reverse link conversion**: `pull` now converts slug links back to file name format
- **Bold format fix**: Automatically inserts a space after `**label：**` to fix Yuque's bold rendering
- **Frontmatter stripping**: `create`/`update` with `--body-file` now strips YAML frontmatter before pushing
- **Functional tests**: Added `tests/test_yuque_sync_fixes.py` covering all 9 requirements

### License

MIT
