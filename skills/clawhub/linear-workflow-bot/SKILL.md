---
slug: linear-workflow-bot
name: linear-workflow-bot
version: "1.0.0"
displayName: Linear工作流机器人
summary: 解决Webhook易断、免费额度烧光、多服务配置混乱痛点，打造可自愈的Linear任务流水线
license: MIT
description: |-
  把 Linear 任务自动接入"通知-执行-回写-Git 同步"流水线。面向独立开发者与一人公司，
  解决免费自动化平台额度紧张、Webhook 触发不可靠、多服务配置散乱、Git 同步冲突四大痛点。

  核心能力:
  - 三层自动化平台选型：Make.com（免费首选）/ Pipedream（即时触发）/ Zapier（付费兜底）
  - Webhook 健康检查与自愈：心跳探活、失败重投、死信队列
  - 任务处理闭环：确认 → DM 通知 → 状态流转 → 执行 → 回写评论 → Git 同步
  - 配置中心化：单一 JSON 管理团队/状态/Discord/Git 四类配置
  - 免费额度监控：每月 ops 消耗看板，临近上限自动降级到低频模式

  适用场景:
  - 个人开发者把 Linear 作为任务中枢，自动分发到 Discord/Git
  - 小团队需要任务到达即通知、即执行、即归档
  - 研究/内容/代码任务的自动化产出与版本化归档
  - 预算敏感场景下榨干免费额度

  差异化:
  - 平台选型决策表 + 免费额度看板，原版只罗列限制
  - Webhook 自愈流程（心跳/重投/死信），原版仅给排错条目
  - 配置中心化 schema，原版散落多个文件
  - 任务处理闭环含失败补偿，原版是单向流程无回滚

  触发关键词: linear, webhook, discord, make, pipedream, zapier, 自动化, 任务流水线, git sync
tags:
- 自动化
- 项目管理
- 通知集成
tools:
- read
- exec
---

# Linear 工作流机器人

自动化流水线：**Linear → Webhook 平台 → 通知通道 → 任务执行 → Git 同步**

在 Linear 创建的任务自动触发处理，实时通知、执行、回写结果并同步到 Git 仓库。

## 平台选型决策表

| 平台 | 免费额度 | 触发延迟 | Webhook 支持 | 推荐场景 |
|:-----|:---------|:---------|:-------------|:---------|
| **Make.com** | 1000 ops/月 | 15 min（免费） | 是 | **免费首选**，额度最宽裕 |
| **Pipedream** | ~100 credits | 即时 | 是 | 需要实时性，能接受额度快速消耗 |
| **Zapier** | 100 tasks/月 | 15 min 轮询 | 否（需付费） | 已有付费账号的团队 |
| **自建** | 无限 | 即时 | 是 | 有服务器、不想被额度卡脖子 |

选型规则：
- 预算敏感 + 任务量 < 1000/月 → Make.com
- 任务量 > 1000/月 或需即时 → 自建 webhook 接收器（Node/Python 单文件）
- 已有 Zapier 付费 → Zapier

## 快速开始

5 步完成首次接入：

1. **配置 Linear API** — 在 `~/.linearbot/linear.env` 写入 `LINEAR_API_KEY`
2. **获取团队/状态 ID** — `./scripts/linear-api.sh teams` 与 `states`
3. **写配置中心** — 编辑 `~/.linearbot/config.json`（schema 见下文）
4. **接 Webhook 平台** — 按选型表选一个，按对应章节配置
5. **跑健康检查** — `./scripts/linearbot doctor` 验证全链路

## 配置中心 schema

替代原版散落多文件，单一 JSON 管理：

```json
{
  "$schema": "linearbot/v1",
  "linear": {
    "teamId": "team-uuid",
    "states": {
      "todo": "state-uuid",
      "inProgress": "state-uuid",
      "done": "state-uuid",
      "canceled": "state-uuid"
    },
    "watchFilter": "state.name = \"Todo\" AND assignee.id = \"<your-id>\""
  },
  "notify": {
    "channel": "discord",
    "discord": {
      "botToken": "${DISCORD_BOT_TOKEN}",
      "notifyUserId": "discord-user-id",
      "taskChannelId": "channel-id",
      "allowBots": true
    }
  },
  "git": {
    "repo": "/path/to/repo",
    "autoPush": true,
    "commitPrefix": "task:",
    "branch": "main",
    "conflictStrategy": "rebase"
  },
  "quota": {
    "platform": "make",
    "monthlyLimit": 1000,
    "warningThreshold": 0.8,
    "degradeStrategy": "batch-daily"
  }
}
```

变量引用 `${VAR}` 从环境变量读取，避免明文 secrets 入库。

## Webhook 平台配置

### Make.com（推荐）

1. 新建 scenario → 添加 Linear "Watch Issues" 触发器
2. 加 filter：`state.name = "Todo"`（与配置中心 watchFilter 对齐）
3. 加 "Webhook" 动作 → 指向你的任务执行端点
4. 加 "Discord" 动作发通知（可选，避免与执行端重复）
5. 启用 scenario，记录 scenario ID 用于额度监控

### Pipedream（需即时）

1. 新建 workflow，HTTP webhook 触发器
2. 在 Linear 配置 webhook 指向 Pipedream URL
3. 加 "Send Message" 步骤到 Discord
4. 消息模板：

```
<@BOT_ID>
New task: {{steps.trigger.event.data.title}}
Status: {{steps.trigger.event.data.state.name}}
ID: {{steps.trigger.event.data.identifier}}
URL: {{steps.trigger.event.data.url}}
```

### 自建 webhook 接收器（无额度限制）

```python
# receiver.py - 单文件 Flask 接收器
from flask import Flask, request
import subprocess
app = Flask(__name__)

@app.route("/linear", methods=["POST"])
def linear():
    event = request.json
    if event.get("action") == "create":
        subprocess.Popen(["./scripts/handle-task.sh", event["data"]["identifier"]])
    return "", 200
```

部署到任意 VPS，配合 systemd 守护。

## 任务处理闭环

任务到达通道后的处理流程，**每步都有失败补偿**：

| 步骤 | 动作 | 失败补偿 |
|:-----|:-----|:---------|
| 1. 确认 | 在通道回复收到 | 失败重试 3 次，仍失败则写入死信 |
| 2. DM 通知 | 给配置的用户发私信 | 用户 ID 错则回退到通道 @mention |
| 3. 状态流转 | `linear-api.sh start <id>` | Linear API 失败则走鉴权自愈 |
| 4. 执行任务 | 调子 Agent 或本地脚本 | 超时 30 min 则标记 "Stalled" |
| 5. 回写评论 | `linear-api.sh comment <id> "<summary>"` | 评论过长则改用文件附件 |
| 6. 完成流转 | `linear-api.sh done <id>` | 失败则保持 In Progress 并告警 |
| 7. Git 同步 | `git add/commit/push` | 冲突按 `conflictStrategy` 处理 |

### 状态机

```
Todo ──(收到)──> In Progress ──(成功)──> Done
                       │
                       ├──(超时)──> Stalled ──(用户介入)──> In Progress / Canceled
                       │
                       └──(失败)──> In Progress + 评论告警
```

## Webhook 自愈流程

```
每小时心跳：
 ├─ 调 Make/Pipedream API 查 scenario 最近运行
 ├─ 30 min 无运行 → 发测试 webhook 探活
 ├─ 探活失败：
 │   ├─ 重投最近 5 条历史任务（去重）
 │   ├─ 通知用户 webhook 异常
 │   └─ 切换到备用平台（若配置了 fallback）
 └─ 死信队列：3 次失败的任务进 DLQ，等用户手动处理
```

## 免费额度监控

```bash
# 每日检查 Make.com 用量
./scripts/linearbot quota-check
# 输出：本月已用 823/1000 ops (82%)，临近阈值，启用降级
```

降级策略（`degradeStrategy`）：
- `batch-daily`：把即时触发改为每日 22:00 批量处理
- `drop-low-priority`：丢弃低优先级标签的任务
- `switch-platform`：自动切到备用平台

## 脚本参考

`scripts/linear-api.sh` 命令：

| 命令 | 说明 |
|:-----|:-----|
| `teams` | 列团队与 ID |
| `states` | 列工作流状态 |
| `get <id>` | 取任务详情 |
| `pending` | 列待办任务 |
| `start <id>` | 标记 In Progress |
| `done <id>` | 标记 Done |
| `cancel <id>` | 标记 Canceled |
| `comment <id> "text"` | 加评论 |
| `comment-file <id> path.md` | 用文件加评论（长文本） |

`scripts/linearbot` 命令：

| 命令 | 说明 |
|:-----|:-----|
| `doctor` | 全链路健康检查 |
| `quota-check` | 查额度用量 |
| `replay <id>` | 重放指定任务 |
| `dlq list` | 列死信队列 |
| `dlq ack <id>` | 确认死信已处理 |

## 任务类型与产出归档

| 任务类型 | 执行方式 | 归档位置 |
|:---------|:---------|:---------|
| 研究 | 子 Agent 调研 | `research/<topic>.md` |
| 内容创作 | 生成草稿 | `content/<slug>.md` |
| 代码任务 | 写/改代码 + commit | 仓库对应目录 |
| 数据处理 | 跑脚本 | `output/<task-id>/` |
| 自定义 | 按 `outputPattern` 配置 | 配置指定 |

## 真实场景示例

### 场景1：研究类任务自动归档

```
Linear 任务 ENG-456 "调研 wasm 在边缘计算的应用"
1. 收到 → Discord 通知 + DM
2. start ENG-456
3. 子 Agent 调研，生成 research/wasm-edge-computing.md
4. comment ENG-456 "已完成，见 research/wasm-edge-computing.md"
5. done ENG-456
6. git add research/ && commit -m "task: ENG-456 wasm调研" && push
```

### 场景2：内容批量生产

```
Linear 任务 ENG-457 "写 5 篇产品文案"
1. 收到 → 通知
2. start
3. 子 Agent 按 5 个主题各生成一篇，存 content/
4. comment-file ENG-457 /tmp/summary.md（含 5 篇链接）
5. done + git push
```

### 场景3：Webhook 故障自愈

```
doctor 发现 Make scenario 30 min 无运行
1. 发测试 webhook → 失败
2. 重投最近 5 条任务到备用 Pipedream workflow
3. Discord 告警 "Make 异常，已切 Pipedream"
4. 用户收到通知后修复 Make，linearbot resume 回切
```

## FAQ

**Q1: 免费 1000 ops 会超吗？**
A: 单人日均任务 < 30 条基本够。每条任务平均消耗 2-3 ops（触发 + 通知）。超过 80% 阈值自动降级到 batch-daily。

**Q2: Git push 冲突怎么办？**
A: 按 `conflictStrategy`：`rebase`（默认，自动 rebase 后重试 3 次）、`merge`（生成 merge commit）、`abort`（放弃同步并告警）。

**Q3: 子 Agent 执行超时？**
A: 默认 30 min 超时标记 Stalled。可在 config 中调 `executionTimeout`。Stalled 任务不自动取消，等用户介入。

**Q4: 多个 Linear 团队怎么配？**
A: 配置中心支持 `teams` 数组，每个团队独立 watchFilter 与通知通道。Git 同步可按团队分仓库或分目录。

**Q5: 凭证安全？**
A: 所有 secrets 用 `${VAR}` 引用环境变量，不写入 config.json。`~/.linearbot/` 目录权限设为 600。

## 故障排查

| 现象 | 排查路径 |
|:-----|:---------|
| 任务不触发 | `linearbot doctor` → 查 webhook 平台 scenario 状态 → 查 watchFilter |
| Linear API 报 401 | 检查 `~/.linearbot/linear.env` → 重新生成 API Key |
| Discord 不通知 | 验证 botToken → 检查 bot 在频道权限 → `allowBots: true` |
| Git push 失败 | 检查 SSH key/credential → 查 remote → 按 conflictStrategy 处理 |
| 额度耗尽 | `quota-check` → 启用降级 → 或切自建接收器 |
| 死信堆积 | `linearbot dlq list` → 逐个 `replay` 或 `ack` |

## 依赖说明

### 运行环境
- **Agent 平台**: 任意支持 SKILL.md 的 AI Agent
- **操作系统**: Windows / macOS / Linux
- **Shell**: bash 推荐（脚本依赖）
- **Git**: 已配置 remote 与认证

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Linear 账号 | SaaS | 必需 | linear.app 注册 |
| Make.com / Pipedream / Zapier | 自动化平台 | 三选一（或自建） | 对应官网注册 |
| Discord 账号 + Bot | 通知通道 | 推荐（可替换为 Slack/Telegram） | Discord Developer Portal |
| Git 仓库 | 版本控制 | 可选（启用 Git 同步时必需） | 本地或 GitHub/GitLab |
| `jq` | JSON 处理 | 推荐 | 系统包管理器 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- `LINEAR_API_KEY`：Linear → Settings → API → Personal API keys
- `DISCORD_BOT_TOKEN`：Discord Developer Portal → Bot → Token
- Make/Pipedream API Token：对应平台账号设置
- 全部存于环境变量或 `~/.linearbot/*.env`（权限 600），勿入库

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 必须通过 exec 执行脚本与 webhook 调用）
- **说明**: 基于自然语言指令驱动 Agent 搭建并运维 Linear 任务流水线，含自愈与降级机制
