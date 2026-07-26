---
name: skill-manager
display_name: "Skill 管理器"
version: "1.0.0"
description: >
  WorkBuddy Skill 全生命周期管理器。列出/查看/创建/删除/搜索/审计/打包/安装技能，
  一站管理本地和内置市场的所有 Skill。触发词：技能管理, skill管理, 管理技能,
  skill manager, 列出技能, 技能列表, 审计技能, 技能审计, 删除技能,
  创建技能, 技能健康检查, 清理技能, 技能打包, 重复技能检测。
agent_created: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - WebFetch
  - Skill
  - TaskCreate
  - TaskUpdate
  - TaskList
  - TaskGet
  - AskUserQuestion
  - Agent
  - DeferExecuteTool
  - ToolSearch
metadata:
  emoji: "🗂"
  tags: ["skill", "management", "meta", "admin", "tooling"]
  category: "developer-tools"
---

# Skill Manager — Skill 全生命周期管理器

一站式管理 WorkBuddy 本地和内置市场的所有 Skill。覆盖列表、查看、创建、删除、搜索、审计、打包、安装八大核心功能。

## 何时触发

当用户表达以下意图时使用此技能：
- "管理技能" "管理skill" "skill manager" "列出所有技能" "技能列表"
- "审计技能" "检查技能" "技能健康" "清理技能" "重复技能"
- "创建技能" "新建skill" "删除技能" "移除skill"
- "打包技能" "打包skill" "发布技能"
- "搜索技能" "查找技能" "有没有XX技能"
- "安装XX技能" — 仅当用户已在 skill-manager 上下文中，否则让 marketplace-skill-installer 处理

## Skill 存储位置

| 类型 | 路径 | 作用域 |
|------|------|--------|
| 用户 Skill | `~/.workbuddy/skills/<name>/` | 全局可用 |
| 项目 Skill | `<project>/.workbuddy/skills/<name>/` | 当前项目 |
| 内置市场 Skill | 同用户 Skill，附带 `_skillhub_meta.json` 或 `_knot_meta.json` | 全局可用 |
| 内置 Skill | 系统目录，只读 | 全局可用 |

## 核心操作

### 1. 列出所有技能 (`--list`)

触发：用户说"列出技能""技能列表""list skills""有哪些技能"。

执行步骤：
1. 同时扫描用户目录和当前项目目录
2. 对于每个 skill，读取 SKILL.md 的 YAML frontmatter（前 5 行），提取 `name`、`version`、`description`（截取前 80 字）、`agent_created`、`metadata.emoji`
3. 判断来源：本地（有 agent_created）→ "自建"，来自市场（有 `_skillhub_meta.json`）→ "市场"，其他 → "未知"
4. 输出带编号的表格，列：序号、名称、版本、来源、简述、是否有脚本/资源
5. 输出统计：总数、自建数、市场安装数、项目级数

表格格式示例：
```
## 📦 已安装 Skill 列表 (共 42 个：自建 35 | 市场 5 | 项目 2)

| # | 名称 | 版本 | 来源 | 简述 | 资源 |
|---|------|------|------|------|------|
| 1 | agent-decision | 1.0.0 | 自建 | AI Agent开发决策辅助系统... | 📜 |
| 2 | agentmail | "1.0" | 市场 | Email inbox for AI agents... | 📜🔧 |
```

### 2. 查看技能详情 (`--view <name>`)

触发：用户说"查看XX技能""skill详情""看看XX技能"。

执行步骤：
1. 读取 SKILL.md 完整内容
2. 解析 frontmatter，展示结构化信息框（名称、版本、描述、来源、标签）
3. 展示目录结构（是否有 scripts/references/assets）
4. 如果用户加了 `--full` 或"看完整内容"，则展示 Markdown 全文
5. 如果是市场安装的，检查 `_skillhub_meta.json` 看是否有更新可用

### 3. 创建技能 (`--create <name>`)

触发：用户说"创建技能""新建skill""add skill"。

执行步骤：
1. 询问：技能名、简述、用户级还是项目级？
2. 如果用户明确说了名字，直接创建；否则先确认
3. 运行内置 init 脚本：
   ```bash
   python "/d/Program Files (x86)/WorkBuddy/resources/app.asar.unpacked/resources/builtin-skills/skill-creator/scripts/init_skill.py" <name> --path <目录>
   ```
   如果 `--path` 省略，默认用户级 (`~/.workbuddy/skills/`)。
4. 打开 SKILL.md 让用户编辑或让用户说需求后自动填充
5. 确认创建成功，显示目录结构

### 4. 删除技能 (`--delete <name>`)

触发：用户说"删除XX技能""移除XX"。

执行步骤：
1. ⚠️ **必须确认**：先展示技能详情（名称、描述、来源），然后用 `AskUserQuestion` 二次确认
2. 仅删除 `agent_created: true` 的技能（自建技能），拒绝删除内置系统技能
3. 市场技能：提示用户市场安装的 skill 可通过 WorkBuddy UI 的【技能管理】面板卸载
4. 自建技能：用 Bash 执行 `rm -rf` 删除整个目录
5. 确认删除成功

### 5. 审计技能 (`--audit`)

触发：用户说"审计技能""技能审计""技能健康检查""检查技能""clean up skills""整理技能"。

这是最核心的功能。运行审计脚本进行全量检查，或手动执行以下检查项：

#### 检查清单

| 检查项 | 严重度 | 说明 |
|--------|--------|------|
| 缺少 SKILL.md | 🔴 P0 | 目录存在但无 SKILL.md — 损坏的安装 |
| 重复 Skill（同名） | 🔴 P0 | 同一名称出现多次（如 storage-clean 和 storage-clean.backup） |
| 遗留 .zip 文件 | 🟡 P1 | skills 根目录有 .zip 打包产物 |
| 缺失 `agent_created` | 🟡 P1 | 无此标记可能导致后续无法管理 |
| 数字 ID 目录名 | 🟡 P1 | 市场安装的 skill（如 skill_2053078990332825600），名称不友好 |
| .backup 后缀目录 | 🟡 P1 | 疑似手动备份，可能与主版本冲突 |
| 缺少 description | 🟢 P2 | frontmatter 缺少 description |
| 版本号异常 | 🟢 P2 | 版本号格式不规范 |
| 空目录 | 🟢 P2 | 完全没有内容的目录 |

#### 执行方式

**优先使用审计脚本**：
```bash
python ~/.workbuddy/skills/skill-manager/scripts/audit.py --user ~/.workbuddy/skills/ [--project .workbuddy/skills/]
```

**手动执行**（脚本不可用时）：

1. 用 `ls` 和 `for` 循环扫描所有 skill 目录
2. 对每个目录检查 SKILL.md 是否存在
3. 读取 frontmatter 提取 metadata
4. 检查重复名称：`ls ~/.workbuddy/skills/ | sort | uniq -d`
5. 检查 .zip 文件：`ls ~/.workbuddy/skills/*.zip`
6. 检查 .backup 目录：`ls -d ~/.workbuddy/skills/*backup*`
7. 检查数字 ID 目录：`ls -d ~/.workbuddy/skills/skill_*`

#### 审计输出格式

以彩色分级报告形式展示：
```
## 🔍 Skill 审计报告

### 🔴 P0 严重问题
- storage-clean ↔ storage-clean.backup：重复 Skill，建议删除 .backup 版本

### 🟡 P1 警告
- skills/ 目录下发现 3 个 .zip 文件：aioom.zip, contract-review.zip, mbti-test.zip
- 5 个市场 Skill 使用数字 ID 目录名（不便于识别）

### 🟢 P2 建议
- xxx 缺少 description
- yyy 版本号为空

### 📊 统计
- 总数: 42 | P0: 1 | P1: 8 | P2: 3 | ✅ 正常: 30
```

### 6. 清理/修复 (`--fix`)

触发：用户说"修复技能""清理技能""fix skills"。

审计后提供一键修复选项：
1. 删除遗留 .zip 文件：`rm ~/.workbuddy/skills/*.zip`
2. 删除 .backup 重复目录（需确认）
3. 补充缺失的 `agent_created: true`（需确认）
4. 补充缺失的 description

修复使用 `AskUserQuestion` 逐项确认，或用户说"全部修复"时批量处理。

### 7. 搜索技能 (`--search <keyword>`)

触发：用户说"搜索技能""查找XX"。

执行步骤：
1. 在用户级和项目级 skill 目录的 SKILL.md 中搜索关键词
2. Grep 搜索 frontmatter 中的 name 和 description 字段
3. 展示匹配项：名称、匹配内容摘要、所在路径
4. 如果没有匹配，搜索内置市场 (`workbuddy_marketplace_skill` search)

### 8. 打包技能 (`--package <name> [--output <dir>]`)

触发：用户说"打包技能""package skill""发布技能"。

执行步骤：
1. 确认技能存在且有效（有 SKILL.md）
2. 运行打包脚本：
   ```bash
   python "/d/Program Files (x86)/WorkBuddy/resources/app.asar.unpacked/resources/builtin-skills/skill-creator/scripts/package_skill.py" <skill-path> [output-dir]
   ```
3. 打包成功后展示 .zip 文件路径和大小

### 9. 从市场安装 (`--install <keyword>`)

触发：用户说"安装XX技能"。

委托给 `marketplace-skill-installer` 技能处理。仅当 skill-manager 已在上下文中时直接调用 `workbuddy_marketplace_skill`：
- search → 展示选项 → install

## SaaS 模式 (Dashboard)

除了 CLI 模式，skill-manager 还提供 Web Dashboard（SaaS 模式）。

### 启动 Dashboard

```bash
# 需要先安装依赖
pip install fastapi uvicorn

# 启动服务
python ~/.workbuddy/skills/skill-manager/server.py --port 8765
```

### Dashboard 功能

- 📊 **统计面板**：总数/P0/P1/P2/OK 实时卡片
- 📋 **技能列表**：搜索、过滤（来源/状态）、排序、分页
- 🩺 **审计报告**：Chart.js 饼图（健康分布 + 来源分布）+ 问题列表
- 🔍 **技能详情抽屉**：查看 SKILL.md 完整内容、元信息、文件列表
- 🗑️ **一键删除**：自建技能支持 Web 删除（需二次确认）
- 🔧 **一键修复**：自动清理 .zip 遗留文件
- 📥 **导出**：JSON 格式导出全量技能数据
- 📖 **API 文档**：FastAPI 自动生成的 Swagger UI (`/docs`)

### API 端点

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/health` | 健康检查 |
| GET | `/api/stats` | 统计摘要 |
| GET | `/api/skills` | 技能列表（支持 ?q=&source=&level=&sort=&page=） |
| GET | `/api/skills/{name}` | 技能详情（含 SKILL.md 全文） |
| GET | `/api/skills/{name}/raw` | 原始 SKILL.md 内容 |
| DELETE | `/api/skills/{name}?confirm=true` | 删除自建技能 |
| GET | `/api/audit` | 全量审计报告 |
| POST | `/api/audit/fix?confirm=true` | 自动修复 |

## 审计脚本

`scripts/audit.py` 是核心辅助工具，提供：
- 全量 skill 扫描
- YAML frontmatter 解析
- 重复检测（同名/.backup）
- 遗留文件检测
- 结构化 JSON 输出，便于后续处理
- 同时被 CLI 和 server.py 复用

当脚本存在时优先使用；当脚本不可用时，按手动方式逐项执行。

## 重要规则

1. **删除需确认**：任何删除操作必须经过用户二次确认，不得直接执行
2. **拒绝删除系统 Skill**：内置系统 skill 目录不可删除
3. **市场 Skill 建议 UI 操作**：市场安装的 skill 建议通过 WorkBuddy 技能管理面板操作
4. **优先使用脚本**：审计和打包操作优先使用现有脚本，减少重复工作
5. **结果完整性**：每次操作后输出简要摘要，大结果表格式呈现
6. **中文输出**：与用户交互全程中文，表格和报告使用中文列名
