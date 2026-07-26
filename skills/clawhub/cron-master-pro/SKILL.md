---
slug: cron-master-pro
name: cron-master-pro
version: "1.0.0"
displayName: 定时大师
summary: 平台级定时系统精通指南，heartbeat 与 cron 决策矩阵、推送策略、自唤醒规则全覆盖。
license: MIT
description: |-
  定时大师是平台级定时系统的深度使用指南，解决"何时用心跳、何时用 cron""推送还是静默""怎么跨回合等待"等高阶决策问题。它提供 heartbeat 与 cron 的决策矩阵、payload 类型选择（agentTurn 推送 vs systemEvent 静默）、严格指令模板、自唤醒规则、时区锁定规范与历史模式迁移指南。

  核心能力：heartbeat/cron 决策矩阵、推送通知策略（agentTurn+announce）、静默日志策略（systemEvent）、严格指令模板（防 AI 啰嗦）、跨回合自唤醒、时区锁定规范、历史遗留模式迁移、网关超时排查。

  适用场景：需要精确提醒（手机推送）、跨回合等待、平台级定时系统治理、遗留 cron 任务迁移、可靠性要求高的周期任务。

  差异化：相比原始方案，本技能把零散经验整理为可执行的决策矩阵与检查清单，新增推送/静默选型决策树、严格指令模板（解决"AI 加了多余寒暄"问题）、自唤醒三档规则（交互/短等待/长等待）、历史模式迁移对照表与网关超时分级处置。定位为"精通层"，解决高阶可靠性问题，不重复基础调度（那是定时调度专家的职责）。

  触发关键词：定时大师, heartbeat, 心跳, 推送, agentTurn, systemEvent, 自唤醒, 时区, 迁移, mastery, precise, reminder, push
tags:
- 自动化
- 定时调度
- 平台精通
tools:
- read
- exec
---

# 定时大师

**第一法则：心跳会漂移，cron 才精确。**

本技能是平台级定时系统的深度使用指南。它不重复基础调度（那是定时调度专家的职责），而是解决高阶问题：什么时候该用心跳、什么时候必须用 cron；要手机推送还是静默记日志；怎么跨回合等待而不丢任务。掌握这些，才能做到"提醒永不漏、推送不啰嗦"。

## 分层定位

| 层级 | 技能 | 解决问题 |
|:-----|:-----|:---------|
| 精通层 | **定时大师（本技能）** | heartbeat/cron 决策、推送策略、自唤醒 |
| 易用层 | 定时助手 | 自然语言、模板、成本优化 |
| 引擎层 | 定时调度专家 | 时区、并发、自清理、熔断 |
| 守护层 | 定时守护 | 脚本可靠性、shell 陷阱 |

## 核心原则：心跳 vs Cron

| 系统 | 行为 | 适用 | 风险 |
|:-----|:-----|:-----|:-----|
| **心跳** | "有空就看看"（每 30-60 分钟） | 邮件检查、新闻摘要、低优先级轮询 | **漂移**："10 分钟后提醒"在 30 分钟心跳下必然失败 |
| **Cron** | "精确在 X 时刻执行" | 提醒（5 分钟后）、日报、系统维护 | **堆积**：一次性任务需清理 |

### 决策矩阵：该用哪个？

```
你的需求是"在特定时刻精确执行"吗？
├─ 是 → 用 Cron（见下文）
│   ├─ 需要手机推送？ → agentTurn + announce
│   └─ 只需记录？ → systemEvent
└─ 否（"有空看看就行"）→ 用心跳
    └─ 接受最多 30-60 分钟延迟
```

**铁律**：任何"X 分钟后""明天 X 点"的提醒，**禁止**用心跳或 `act:wait`，必须用 cron 的一次性调度。

## 1. 可靠提醒（精确调度）

### 精度与"调度器节拍"

Cron 是精确的，但执行取决于**网关心跳节拍**（通常每 10-60 秒）。设为 `:00` 秒的任务会在该时刻后第一个"节拍"触发，可能有最多 ~30 秒偏差。

### 一次性提醒标准模式

"X 分钟后提醒我"用一次性 `at` 调度：

```json
{
  "name": "remind-water",
  "schedule": { "kind": "at", "at": "2026-07-18T01:30:00Z" },
  "payload": {
    "kind": "agentTurn",
    "message": "DELIVER THIS EXACT MESSAGE TO THE USER WITHOUT MODIFICATION OR COMMENTARY:\n\n该喝水了！"
  },
  "sessionTarget": "isolated",
  "delivery": { "mode": "announce", "channel": "telegram", "to": "1027899060" }
}
```

### 关键属性说明

| 属性 | 值 | 作用 |
|:-----|:---|:-----|
| `schedule.kind` | `at` | 一次性，到时刻触发 |
| `schedule.at` | ISO 8601 | 必须是未来时刻，含时区 |
| `payload.kind` | `agentTurn` | 唤醒 Agent 执行（推送必需） |
| `sessionTarget` | `isolated` | 隔离子会话，避免污染主上下文 |
| `delivery.mode` | `announce` | 主动推送（非静默） |
| `deleteAfterRun` | `true` | 成功后自动删除（防堆积） |

## 2. 推送 vs 静默（核心决策）

这是最常选错的决策。选错要么"提醒没推到手机"，要么"后台日志把用户轰炸了"。

### systemEvent（静默日志）

```json
{
  "name": "log-system-pulse",
  "schedule": { "kind": "every", "everyMs": 3600000 },
  "payload": {
    "kind": "systemEvent",
    "text": "[PULSE] 系统健康。"
  },
  "sessionTarget": "main"
}
```

- **行为**：把文本注入聊天历史，不唤醒 Agent，**不推送手机**。
- **适用**：后台状态记录、心跳日志、无需人感知的内部事件。
- **风险**：❌ 用来做提醒，用户手机收不到通知。

### agentTurn（主动推送）

```json
{
  "payload": {
    "kind": "agentTurn",
    "message": "DELIVER THIS EXACT MESSAGE...:\n\n内容"
  },
  "delivery": { "mode": "announce", "channel": "telegram", "to": "用户ID" }
}
```

- **行为**：唤醒 Agent 交付消息，**推送手机**通知。
- **适用**：所有需要用户感知的提醒。
- **风险**：❌ 不加严格指令，Agent 会加"你好，这是您的提醒～"等废话。

### 决策树

```
需要用户在手机上看到通知吗？
├─ 需要 → agentTurn + announce
│         （必须用严格指令模板）
└─ 不需要 → systemEvent
            （后台静默记录）
```

## 3. 严格指令模板（防 AI 啰嗦）

用 `agentTurn` 时，子 Agent 容易"热情过头"，在提醒前后加寒暄。用严格指令模板杜绝：

```
DELIVER THIS EXACT MESSAGE TO THE USER WITHOUT MODIFICATION OR COMMENTARY:

<你的提醒内容>
```

**关键点**：
- 大写 `DELIVER THIS EXACT MESSAGE` 起强调作用。
- `WITHOUT MODIFICATION OR COMMENTARY` 禁止添加任何评论。
- 换行后直接放消息内容。
- 子 Agent 应原样输出，不加"好的""提醒您"等前缀。

错误示例（子 Agent 啰嗦）：
```
你好！我收到了一条定时提醒，现在转达给您：
该喝水了！
希望您身体健康～
```

正确示例（严格指令效果）：
```
该喝水了！
```

## 4. 并发与死锁（已稳定但仍需注意）

历史遗留的"先 add 再 update"模式曾导致死锁。虽然网关已修复，最佳实践仍是**单步创建**：所有参数（含 `wakeMode: "now"`）在首次 `cron.add` 时一次传入，不要先 add 再 update。

```json
// 正确：单步创建
{
  "name": "remind",
  "schedule": { "kind": "at", "at": "..." },
  "payload": { "kind": "agentTurn", "message": "..." },
  "wakeMode": "now",
  "deleteAfterRun": true
}

// 错误：两步操作（已废弃）
// step1: cron.add { name, schedule }
// step2: cron.update { payload, wakeMode }  ← 曾导致死锁
```

## 5. 跨回合等待：自唤醒规则

**问题**：Agent 说"我等 30 秒"然后结束回合，就睡着了，自己无法醒来。

**规则三档**：

| 等待时长 | 方式 | 说明 |
|:---------|:-----|:-----|
| < 1 分钟 | `act:wait`（保持工具循环开启） | 交互式等待，不结束回合 |
| > 1 分钟 | Cron + `wakeMode: "now"` | 调度一次性任务唤醒自己 |
| 跨天/定期 | Cron 周期任务 | 长期调度 |

```json
// 等 30 分钟后继续
{
  "name": "self-wake-30m",
  "schedule": { "kind": "at", "at": "<30分钟后的ISO时刻>" },
  "payload": { "kind": "agentTurn", "message": "继续执行之前暂停的任务：XXX" },
  "wakeMode": "now",
  "deleteAfterRun": true
}
```

**铁律**：禁止用 `act:wait` 等待超过 1 分钟，会占用工具循环资源。长等待必须用 cron 自唤醒。

## 6. 时区锁定规范

Cron 要可靠，Agent **必须**知道自己的时间。

### 时区写入记忆

```bash
# 在 MEMORY.md 中记录
Timezone: Asia/Shanghai (UTC+8)
```

### 时区确认流程

用户说"9 点提醒我"时，Agent 必须确认：

```
用户: 9点提醒我开会
Agent: 9点是指 Asia/Shanghai 时区的晚上9点吗？
用户: 对
Agent: 已创建提醒：今晚 21:00 CST 开会提醒
```

### 验证清单

- [ ] MEMORY.md 中有时区记录
- [ ] 创建任务前确认时区
- [ ] `schedule.at` 使用含时区的 ISO 8601（如 `2026-07-18T21:00:00+08:00`）
- [ ] 跨时区用户单独指定时区

## 7. 一次性任务清理

网关已内置维护语义，自动清理卡住的任务并修复损坏的调度。手动清理仅在以下情况需要：

- 一次性任务以 `deleteAfterRun: false` 创建（旧模式）
- 不再需要的过期周期任务

### 清理策略

```json
// 创建时始终开启自动清理
{ "deleteAfterRun": true }

// 清理历史遗留的未清理任务
// 用 sessionTarget: "main" 让主 Agent 执行清理（子 Agent 权限不足）
{
  "name": "janitor",
  "schedule": { "kind": "every", "everyMs": 86400000 },
  "payload": { "kind": "systemEvent", "text": "执行 cron 清理：删除已完成的一次性任务" },
  "sessionTarget": "main"
}
```

### 为什么用 sessionTarget: "main"？

子 Agent（`isolated`）通常有受限的工具策略，无法调用 `gateway` 或删除其他 cron 任务。系统维护类任务**必须**通过 `systemEvent` 指向 `main` 会话，让有完整工具权限的主 Agent 执行清理。

## 8. 历史模式迁移指南

如果你有旧 cron 任务，按下表迁移：

| 旧模式（已废弃） | 新模式（推荐） |
|:------------------|:---------------|
| `"schedule": {"kind": "at", "atMs": 1234567890}` | `"schedule": {"kind": "at", "at": "2026-02-06T01:30:00Z"}` |
| `"deliver": true`（payload 内） | 不需要，`announce` 模式处理投递 |
| `"sessionTarget": "main"`（默认） | `"sessionTarget": "isolated"`（隔离，更安全） |
| 手动清理幽灵任务 | 一次性任务 `deleteAfterRun: true` 自动清理 |
| `cron.update` 跟在 `cron.add` 后 | 单步 `cron.add` 传入所有属性 |
| 无 `wakeMode` | 显式 `"wakeMode": "now"` |

迁移检查清单：
- [ ] 所有 `atMs` 改为 ISO 8601 `at`
- [ ] 移除 payload 中的 `deliver`
- [ ] 非维护类任务 `sessionTarget` 改为 `isolated`
- [ ] 一次性任务加 `deleteAfterRun: true`
- [ ] 合并 add+update 为单步 add
- [ ] 显式设置 `wakeMode: "now"`

## 故障排查

### "提醒没触发"

1. `cron.list` 查看任务是否存在
2. 确认 `at` 时间是未来时刻（ISO 8601 格式）
3. 确认 `wakeMode: "now"` 已设置
4. 检查时区是否匹配

### "网关超时 (10000ms)"

cron 工具响应过慢，通常是任务列表过大或文件锁冲突。

- **处置 1**：手动清理 `~/.skill-platform/state/cron/jobs.json`（先备份），重启网关
- **处置 2**：运行清理减少任务数量
- **处置 3**：检查是否有遗留的文件锁

### "任务跑了但没收到消息"

99% 是 payload 类型选错。需要推送却用了 `systemEvent`（静默）。

- **修复**：改为 `agentTurn` + `announce` 模式
- **验证**：确认 `delivery.channel` 和 `delivery.to` 正确

### "提醒消息带多余寒暄"

子 Agent 没遵守严格指令。

- **修复**：使用严格指令模板 `"DELIVER THIS EXACT MESSAGE... WITHOUT MODIFICATION OR COMMENTARY:\n\n<内容>"`
- **验证**：检查 payload.message 是否包含该模板前缀

## FAQ

**Q：心跳和 cron 能混用吗？**
A：能，且推荐。心跳做轻量轮询（"有没有任务到期"），cron 做精确执行。不要在心跳里做昂贵操作。

**Q：agentTurn 和 systemEvent 能在一个任务里同时用吗？**
A：不能，payload.kind 只能选一个。需要"既推送又记日志"时，拆成两个任务。

**Q：跨时区团队怎么管？**
A：每个用户在 MEMORY.md 锁定自己的时区。任务 `at` 用 UTC，由 Agent 转换显示。

**Q：一次性任务失败后会自动重试吗？**
A：默认不会（一次性任务失败即结束）。需要重试则用周期任务，或配合定时调度专家的熔断重试。

**Q：严格指令模板对中文有效吗？**
A：有效。模板是英文是为了强约束，消息内容可以是中文。子 Agent 会原样输出中文内容。

**Q：wakeMode 还有别的值吗？**
A：`"now"`（立即唤醒）最常用。其他值取决于网关版本，未明确时用 `now`。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 cron 工具与 SKILL.md 的 AI Agent 平台（需具备 agentTurn/systemEvent 能力）
- **操作系统**：Linux / macOS / Windows
- **网关**：支持 cron 调度的 Agent 网关（2026.2.15+ 推荐版本）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| 平台 cron 工具 | 内置工具 | 必需 | 平台内置 |
| cron-scheduler-pro | 关联技能 | 推荐 | 作为本地引擎补充 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本技能本身无需 API Key。
- 推送通知依赖平台的 delivery 配置（如 Telegram bot token、WhatsApp 等），在平台层配置。
- 任务执行消耗 LLM 额度，由平台账户承担。

### 可用性分类
- **分类**：MD（纯 Markdown 指南，通过 Agent 调用平台 cron 工具执行）
- **说明**：本技能是决策与规范指南，Agent 依据本指南选择正确的 payload 类型、调度模式与指令模板，实际调度由平台 cron 工具执行。
