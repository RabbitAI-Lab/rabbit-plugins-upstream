---
slug: linear-cli-pro
name: linear-cli-pro
version: "1.0.0"
displayName: Linear CLI专家
summary: 解决JSON解析难、内联转义炸、批量操作慢、鉴权易失效痛点，让Linear CLI在Agent中稳跑
license: MIT
description: |-
  面向在 Agent（Claude Code / Codex / Cursor 等）中调用 `linear` CLI 的开发者。
  聚焦 v3 执行模型下的稳定 JSON 契约、预演式写入、Markdown 安全传参、批量操作与鉴权自愈。

  核心能力:
  - Agent 优先执行循环：capabilities 发现 → 读 → dry-run 预览 → 写 → 校验 receipt/error.details
  - Markdown 内容强制走 `--*-file` 或 stdin，杜绝 `\n` 字面量与 shell 转义炸裂
  - 批量操作模板（issue 批量创建/状态流转/标签同步），含并发与限速策略
  - 鉴权自愈：token 过期自动触发 `linear auth refresh`，失败时降级到环境变量
  - Schema 检索工作流：先 grep 本地转储，再决定是否拉取线上 schema，节省 80% 流量

  适用场景:
  - AI Agent 自动化处理 Linear 任务（创建、流转、批量整理）
  - 把 Slack/邮件/PR 信封转化为 Linear issue 的 source-adjacent 接入
  - 大规模 backlog 清理、跨团队标签/状态同步
  - git/jj 工作流与 Linear 双向联动（提交信息回写、PR 关联）

  差异化:
  - 原版只列命令清单；本版给出"读→预览→写→校验"的 Agent 闭环
  - 内置 Markdown 安全传参决策表，原版散落在示例中
  - 批量操作模板 + 并发限速策略，原版无批量场景指引
  - 鉴权自愈流程，原版仅给安装链接

  触发关键词: linear, cli, issue, cycle, project, graphql, agent, backlog, 看板, 任务追踪
tags:
- 自动化
- 项目管理
- 开发者工具
tools:
- read
- exec
---

# Linear CLI 专家

在 Agent 运行时中安全、稳定地操作 Linear。所有写操作遵循"预览-执行-校验"闭环，所有 Markdown 内容走文件/stdin 而非内联，批量操作有并发与限速保护。

## 前置检查

```bash
linear --version          # 必须可用
linear auth status        # 鉴权状态
linear capabilities       # 命令能力清单（机器可读）
```

未安装时，按官方文档安装 `linear` CLI 并运行 `linear auth login`。Agent 检测到 `command not found` 应直接告知用户安装步骤，不要继续后续流程。

## Agent 推荐执行循环

按此顺序执行，**写操作必须先 dry-run**：

1. **发现能力**：`linear capabilities`（旧消费者用 `--compat v1`）
2. **读状态**：默认 JSON 输出或显式 `--json`
3. **预演写入**：`--dry-run --json`（命令支持时）
4. **执行写入**：在机器可读通道上执行，然后检查 `operation`、`receipt`、`error.details`
5. **校验结果**：查退出码与 `error.details`，**不要**解析带样式的终端文本

人/调试模式是次要且显式的：`--profile human-debug --interactive`。Agent 默认使用 `--profile agent-safe`（旧自动化兼容）。

当上游工具传入 Slack/工单信封时：优先 `--context-file`，若信封已含确定性 team/state/label 提示则加 `--apply-triage`，需要 suggest-only 或 preview-required 暂存时显式选 `--autonomy-policy`。

## Markdown 安全传参决策表

| 场景 | 推荐方式 | 反模式（禁用） |
|:-----|:---------|:---------------|
| 已有 .md 文件作为描述 | `issue create --description-file path.md` | `--description "$(cat file)"` |
| 已有 .md 文件作为评论 | `comment add --body-file path.md` | `--body "$(cat file)"` |
| 流式生成的 Markdown | `cat desc.md \| linear issue create --title "..."` | 内联 `--description "多行\n文本"` |
| 单行简单内容 | 内联 `--description "一句话"` | 仍用文件（过度工程） |

**为什么禁止大段内联**：
- Linear Web UI 中格式错乱
- shell 转义破坏换行与特殊字符
- 字面量 `\n` 出现在 markdown 中
- 脚本/管道中多行内容难维护

文件优先示例：

```bash
cat > /tmp/description.md <<'EOF'
## Summary
- 第一项
- 第二项

## Details
这是带格式的详细描述。
EOF

linear issue create --title "My Issue" --description-file /tmp/description.md
linear issue comment add ENG-123 --body-file /tmp/comment.md
```

## 命令速查

| 命令 | 用途 |
|:-----|:-----|
| `linear auth` | 鉴权管理（login / status / token / refresh） |
| `linear issue` | issue 增删改查、批量操作 |
| `linear team` / `linear project` / `linear cycle` / `linear milestone` | 团队/项目/周期/里程碑 |
| `linear initiative` / `linear initiative-update` | 举措与时间线帖 |
| `linear label` / `linear project-label` | issue 标签与项目标签 |
| `linear document` | Linear 文档 |
| `linear notification` / `linear webhook` | 通知与 webhook |
| `linear workflow-state` / `linear user` | 工作流状态与用户 |
| `linear config` | 交互式生成 `.linear.toml` |
| `linear schema` | 输出 GraphQL schema 到 stdout |
| `linear api` | 原始 GraphQL 请求（兜底） |
| `linear capabilities` | Agent 命令面描述 |
| `linear resolve` | 不变更地解析引用 |

任何命令加 `--help` 查看子命令与 flag。机器可读发现：`linear capabilities` 或 `linear capabilities --compat v1`。

## 批量操作模板

### 模板1：批量创建 issue（CSV → Linear）

```bash
# issues.csv: title,team,description
# 用 xargs 控制并发为 4，避免触发速率限制
tail -n +2 issues.csv | xargs -P 4 -I {} bash -c '
  IFS=, read -r title team desc <<< "{}"
  echo "$desc" > /tmp/desc_$$.md
  linear issue create --title "$title" --team "$team" --description-file /tmp/desc_$$.md --json
  rm -f /tmp/desc_$$.md
'
```

并发上限默认 4，超过 8 易触发 Linear API 速率限制（每分钟 1500 请求/工作区）。

### 模板2：批量状态流转

```bash
# backlog-to-in-progress.sh
linear issue list --status Backlog --json \
  | jq -r '.data[].identifier' \
  | xargs -P 4 -I {} linear issue update {} --status "In Progress" --dry-run --json \
  | tee /tmp/preview.json

# 预览无误后去掉 --dry-run 重跑
```

### 模板3：跨团队标签同步

```bash
# 把 ENG 团队的 "bug" 标签复制到 WEB 团队
linear label list --team ENG --json | jq -r '.data[].name' | while read label; do
  linear label create --team WEB --name "$label" --dry-run
done
```

## 鉴权自愈流程

```
检测到 401/403 或 "unauthorized"
 ├─ linear auth status          # 看当前状态
 ├─ linear auth refresh         # 尝试刷新 token
 ├─ 仍失败？
 │   ├─ 检查环境变量 LINEAR_API_KEY 是否存在 → 用 linear auth login --token "$LINEAR_API_KEY"
 │   └─ 提示用户重新登录：linear auth login
 └─ 成功 → 重试原命令（最多 3 次，指数退避）
```

## GraphQL 兜底工作流

**优先用 CLI**。仅当 CLI 未覆盖时用 `linear api`。

### Schema 检索（节省流量）

```bash
# 首次：转储 schema 到本地，后续只 grep
linear schema -o "${TMPDIR:-/tmp}/linear-schema.graphql"
grep -i "cycle" "${TMPDIR:-/tmp}/linear-schema.graphql"
grep -A 30 "^type Issue " "${TMPDIR:-/tmp}/linear-schema.graphql"
```

仅当本地转储超过 7 天或查询字段不存在时才重新拉取。

### GraphQL 请求

含 `!` 非空标记的查询必须用 heredoc stdin，避免转义问题：

```bash
linear api --variable teamId=abc123 <<'GRAPHQL'
query($teamId: String!) { team(id: $teamId) { name } }
GRAPHQL

linear api --variables-json '{"filter": {"state": {"name": {"eq": "In Progress"}}}}' <<'GRAPHQL'
query($filter: IssueFilter!) { issues(filter: $filter) { nodes { title } } }
GRAPHQL
```

简单查询可内联：`linear api '{ viewer { id name email } }'`。

### curl 兜底（需完全 HTTP 控制时）

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: $(linear auth token)" \
  -d '{"query": "{ viewer { id } }"}'
```

## 真实场景示例

### 场景1：把 Slack 工单信封转成 Linear issue

```bash
# 信封已含 team/state/label 提示
linear issue create \
  --context-file /tmp/slack-envelope.json \
  --apply-triage \
  --autonomy-policy preview-required \
  --dry-run --json | tee /tmp/preview.json

# 用户确认后
linear issue create --context-file /tmp/slack-envelope.json --apply-triage --json
```

### 场景2：清理 6 个月未更新的 backlog

```bash
linear issue list --status Backlog --json \
  | jq -r --arg cutoff "$(date -d '6 months ago' +%Y-%m-%d)" \
      '.data[] | select(.updatedAt < $cutoff) | .identifier' \
  | xargs -I {} linear issue update {} --status Canceled --dry-run
```

### 场景3：PR 合并自动关 issue

```bash
# git hook 中调用
PR_TITLE=$(git log -1 --pretty=%B)
ISSUE_IDS=$(echo "$PR_TITLE" | grep -oE '[A-Z]+-[0-9]+')
for id in $ISSUE_IDS; do
  linear issue update "$id" --status Done --comment-file /tmp/pr-merge.md
done
```

## FAQ

**Q1: `--dry-run` 不是所有命令都支持怎么办？**
A: 不支持 dry-run 的命令（如 `label create`）改用"先 list 确认不存在 → 再创建"的预检模式。写操作前永远先读。

**Q2: 大量 issue 创建时频繁 429？**
A: 并发降到 2，并在每次请求间加 `sleep 0.5`。Linear 速率限制按工作区计，跨工作区不会累计。

**Q3: JSON 输出字段不稳定？**
A: 用 `linear capabilities --compat v1` 获取稳定契约。字段名变更时优先看 `error.details`，它给出字段路径。

**Q4: heredoc 在 Windows PowerShell 报错？**
A: PowerShell 不支持 heredoc。改用文件：把查询写入 `.graphql` 文件，用 `linear api --query-file query.graphql`（如 CLI 不支持该 flag，则用 `Get-Content query.graphql -Raw | linear api`）。

**Q5: token 存哪里？**
A: `linear auth login` 交互式登录后存于 `~/.config/linear/credentials.json`。CI 环境用 `LINEAR_API_KEY` 环境变量，不要写入代码仓库。

## 故障排查

| 现象 | 排查路径 |
|:-----|:---------|
| `command not found: linear` | 未安装 → 按 README 安装 → 重开终端 |
| 401 Unauthorized | 走"鉴权自愈流程" |
| 429 Too Many Requests | 降并发到 2 → 加 sleep → 检查是否有其他自动化在跑 |
| `error.details` 显示字段路径 | 用 `linear schema` grep 该类型定义 → 按定义修正查询 |
| dry-run 通过但实写失败 | 检查是否有 webhook/automation 在写时触发副作用 → 查 Linear 审计日志 |
| Markdown 中出现字面 `\n` | 检查是否用了内联 `--description` → 改为 `--description-file` |
| `--context-file` 报格式错 | 信封必须为 JSON 且含 `source`、`title`、`description` 字段 |

## 依赖说明

### 运行环境
- **Agent 平台**: 任意支持 SKILL.md 的 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux（Windows 下避免 heredoc，用文件传参）
- **Shell**: bash / zsh 推荐；PowerShell 需用文件传参替代 heredoc

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| `linear` CLI（v3） | 命令行工具 | 必需 | 官方仓库安装 |
| `jq` | JSON 处理 | 强烈推荐 | 系统包管理器 |
| `curl` | HTTP 兜底 | 可选 | 系统自带 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 交互式：`linear auth login`（浏览器 OAuth）
- CI/自动化：环境变量 `LINEAR_API_KEY`（Personal API Key，从 Linear → Settings → API 获取）
- 凭证存储：`~/.config/linear/credentials.json`（勿提交到仓库）

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 必须通过 exec 执行 `linear` CLI 命令）
- **说明**: 基于自然语言指令驱动 Agent 通过 CLI 操作 Linear，所有写操作走预演-执行-校验闭环
