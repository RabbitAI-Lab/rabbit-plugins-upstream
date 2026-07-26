---
slug: cron-assist
name: cron-assist
version: "1.0.0"
displayName: 定时助手
summary: 自然语言驱动的定时任务助手，内置模板库与成本优化，把口语意图秒变可靠调度。
license: MIT
description: |-
  定时助手是定时调度专家的"自然语言层"。用户说"每天早上9点发日报"，它解析意图、匹配模板、生成调度命令并执行，全程无需懂 cron 语法。内置高频场景模板（日报、健康检查、收件箱巡检、周报）与成本优化策略（批量合并、降级模型、超时熔断）。

  核心能力：自然语言意图解析、调度模板库、一键创建/暂停/恢复/删除、执行历史查询、成本优化建议、超时与模型降级配置、跨任务批量管理。

  适用场景：非技术用户快速建任务、高频场景模板复用、Agent 心跳成本控制、临时任务快速创建、团队调度批量管理。

  差异化：相比只暴露 CLI 的原始方案，本技能新增自然语言解析（"每两天下午3点"→`--every 2d --at 15:00`）、模板库（6 类高频场景一键套用）、成本优化器（分析任务频次建议合并/降频/换廉价模型）、批量操作（一键暂停所有、按标签管理）。定位为"易用层"，底层调度由 cron-scheduler-pro 引擎执行。

  触发关键词：定时助手, 自然语言, 调度, 模板, cron, 任务, 提醒, schedule, template, natural language, assist
tags:
- 自动化
- 定时调度
- 自然语言
tools:
- read
- exec
---

# 定时助手

让用户用大白话管理定时任务，把"每天早上9点发日报"这种口语秒变可靠调度。本技能解决四个核心痛点：**cron 语法难懂**（`0 9 * * *` 谁记得住）、**重复配置**（日报、健康检查等高频场景每次从零写）、**成本失控**（频繁跑昂贵任务烧 API）、**管理混乱**（任务一多就找不到、改不动）。

## 职责分层

本技能是"易用层"，底层调度由引擎执行：

| 层级 | 技能 | 职责 |
|:-----|:-----|:-----|
| 易用层 | **定时助手（本技能）** | NL 解析、模板、成本优化、批量管理 |
| 引擎层 | 定时调度专家 | 时区锁定、并发安全、自清理、熔断 |
| 守护层 | 定时守护 | 脚本可靠性、shell 陷阱防护 |
| 精通层 | 定时大师 | 平台级 cron 高级用法、推送策略 |

## 快速开始

### 自然语言创建任务

直接说人话，助手解析后生成命令：

```bash
# 用户说："每两小时检查一下收件箱"
cron-assist add "每两小时检查一下收件箱"
# 助手解析为:
#   skill-platform cron add --every "2h" --task "检查收件箱" --name "inbox-check"

# 用户说："每天早上9点发日报"
cron-assist add "每天早上9点发日报"
# 解析为:
#   skill-platform cron add --daily --at "09:00" --task "生成并发送日报" --name "daily-report"

# 用户说："工作日下午5点半提醒下班"
cron-assist add "工作日下午5点半提醒下班"
# 解析为:
#   skill-platform cron add --weekly Mon-Fri --at "17:30" --task "提醒下班" --name "off-work-reminder"
```

### 管理任务

```bash
cron-assist list                # 列出所有任务
cron-assist pause "inbox-check" # 按名称暂停
cron-assist resume "inbox-check"
cron-assist delete "inbox-check"
cron-assist logs "inbox-check"  # 查看执行历史
```

## 自然语言解析规则

助手识别以下口语模式并翻译为调度参数：

| 自然语言 | 解析结果 |
|:---------|:---------|
| 每 N 小时 | `--every "Nh"` |
| 每 N 分钟 | `--every "Nm"` |
| 每 N 天 | `--every "Nd"` |
| 每天上午/下午 X 点 | `--daily --at "HH:MM"` |
| 每周一/二...X 点 | `--weekly Mon --at "HH:MM"` |
| 工作日 X 点 | `--weekly Mon-Fri --at "HH:MM"` |
| 每月 N 号 | `--monthly --day N --at "HH:MM"` |
| X 分钟后 / X 小时后 | `--once --in "Xm"` / `--once --in "Xh"` |
| 明天 X 点 | `--once --at "明天 HH:MM"` |

**歧义消解**：遇到"9点"未说明上午/下午时，助手主动确认："9点是指上午9点还是晚上9点？"

## 调度模板库（核心差异化）

高频场景开箱即用，避免每次从零配置：

### 模板 1：每日日报

```bash
cron-assist template daily-report --apply
# 等价于:
# skill-platform cron add \
#   --daily --at "09:00" \
#   --task "汇总昨日工作、今日计划，生成日报" \
#   --name "daily-report" \
#   --model "cheap" --timeout "120"
```

### 模板 2：收件箱巡检

```bash
cron-assist template inbox-check --interval 2h --apply
```

### 模板 3：API 健康检查

```bash
cron-assist template health-check \
  --endpoint "https://api.example.com/health" \
  --interval 5m --apply
```

### 模板 4：周报生成

```bash
cron-assist template weekly-report --day Friday --at 17:00 --apply
```

### 模板 5：数据备份

```bash
cron-assist template backup \
  --source "/data" --dest "/backup" --schedule "daily 02:00" --apply
```

### 模板 6：社交媒体提及监控

```bash
cron-assist template social-monitor --interval 1h --apply
```

查看所有模板：

```bash
cron-assist template list
```

```
可用模板:
  daily-report      每日日报（09:00, 廉价模型, 120s超时）
  inbox-check       收件箱巡检（每2h, 廉价模型, 60s超时）
  health-check      API健康检查（每5m, 30s超时, 失败告警）
  weekly-report     周报生成（周五17:00, 180s超时）
  backup            数据备份（每日02:00, 300s超时）
  social-monitor    社媒监控（每1h, 60s超时）
```

## 成本优化器（核心差异化）

频繁运行任务会烧 API 额度。本助手分析任务并给出优化建议：

```bash
cron-assist optimize
```

```
成本优化分析
═══════════════════════════════════════════════════
当前任务: 8 个 | 预估日消耗: $4.20

建议优化:
1. [合并] inbox-check(每2h) + social-monitor(每1h)
   → 合并为 social-inbox(每1h), 一次调用处理两者
   → 预估节省: $1.80/天

2. [降频] health-check(每5m) → 每10m
   → 多数 API 5分钟检查过于频繁
   → 预估节省: $0.40/天

3. [降级模型] daily-report 用的是 gpt-4
   → 日报生成用 gpt-3.5 足够
   → 预估节省: $0.90/天

4. [加超时] weekly-report 无超时限制
   → 建议加 --timeout 180 防止卡死烧钱

总计可节省: $3.10/天 (74%)
```

### 成本控制参数

```bash
skill-platform cron add \
  --every "2h" \
  --task "检查收件箱" \
  --model "cheap"        # 用廉价模型
  --timeout 60           # 60秒超时
  --max-retries 2        # 最多重试2次
```

| 参数 | 作用 | 推荐值 |
|:-----|:-----|:-------|
| `--model` | 指定模型（cheap/best/specific） | 巡检类用 cheap |
| `--timeout` | 单次执行超时秒数 | 30-180 |
| `--max-retries` | 失败重试次数 | 2-3 |
| `--cooldown` | 失败后冷却时间 | 300s |

## 批量管理（核心差异化）

任务多了逐个管理很累。本助手支持批量操作：

```bash
# 按标签批量管理（创建时打标签）
cron-assist add "每天9点日报" --tag "report"
cron-assist add "每周五周报" --tag "report"

# 批量暂停某类任务
cron-assist pause --tag "report"
cron-assist resume --tag "report"

# 批量暂停所有（假期模式）
cron-assist pause --all
cron-assist resume --all

# 按状态过滤
cron-assist list --status paused
cron-assist list --failing   # 列出最近失败的任务
```

## 心跳优化模式

不要在心跳里做昂贵检查，改用定时任务。这是最常见的成本浪费：

```bash
# 错误：每 30 分钟心跳都检查收件箱（昂贵）
# 正确：用定时任务精确调度
cron-assist add "每2小时检查收件箱" --model cheap
```

心跳只做轻量判断："有没有任务到期了？"

```bash
# 心跳里的轻量调用
skill-platform cron due-now   # 只返回到期的任务
```

## 场景化指南

### 场景 A：非技术用户快速上手

```bash
用户: "帮我每天早上8点提醒我喝水"
助手: 已创建任务 "drink-water-reminder"
      每天上午8:00 提醒喝水
      要取消就说"暂停喝水提醒"

用户: "改成9点"
助手: 已更新，每天上午9:00 提醒喝水
```

### 场景 B：批量部署团队任务

```bash
# 一键部署团队标准任务集
cron-assist template daily-report --apply --tag "team-standard"
cron-assist template inbox-check --apply --tag "team-standard"
cron-assist template health-check --endpoint "$API" --apply --tag "team-standard"

# 团队放假，一键暂停
cron-assist pause --tag "team-standard"
```

### 场景 C：成本敏感的个人开发者

```bash
# 先分析现有成本
cron-assist optimize
# 按建议优化
cron-assist add "每4小时检查收件箱" --model cheap --timeout 60
```

### 场景 D：临时一次性提醒

```bash
cron-assist add "30分钟后提醒我关火"
# 解析为一次性任务，30分钟后触发，自动清理
```

## FAQ

**Q：自然语言识别不了我的说法怎么办？**
A：助手支持常见中文时间表达。若无法识别，它会询问"请用'每X小时'或'每天X点'格式说明"。也可直接用 `skill-platform cron add` 手动指定。

**Q：模板能自定义吗？**
A：能。把自定义模板写入 `~/.skill-platform/cron-assist/templates/`，格式参考内置模板。`cron-assist template create` 可交互式创建。

**Q：成本优化的预估准吗？**
A：基于任务频次 × 单次模型调用均价估算，仅供参考。实际消耗取决于任务复杂度。建议定期 `optimize` 复查。

**Q：批量暂停所有任务，定时提醒也会停吗？**
A：会。`pause --all` 暂停全部，包括一次性提醒。假期模式后记得 `resume --all`。

**Q：和定时调度专家有什么区别？**
A：本技能是"自然语言+模板+成本"的易用层；定时调度专家是"时区+并发+清理"的引擎层。两者配合使用：助手负责理解意图，引擎负责可靠执行。

**Q：任务失败了我怎么知道？**
A：`cron-assist list --failing` 查看失败任务。建议配合定时大师的推送通知策略，失败时主动通知。

## 故障排查

| 症状 | 可能原因 | 处置 |
|:-----|:---------|:-----|
| 自然语言无法解析 | 表达不标准 | 用模板或直接 CLI |
| 任务创建成功但不跑 | 底层引擎未启动 | 确认定时调度专家引擎运行 |
| 成本突然升高 | 任务频次过高或模型升级 | 运行 `optimize` 检查 |
| 模板应用失败 | 缺少必要参数 | 查看模板说明补全参数 |
| `list` 显示空 | 任务被归档 | `list --archived` 查看 |
| 批量操作无响应 | 标签拼写错误 | `list --tags` 查看已有标签 |

## 性能优化

1. **模板优先**：高频场景用模板，避免重复解析。
2. **廉价模型**：巡检类任务指定 `--model cheap`，省 80% 成本。
3. **合理超时**：设 `--timeout` 防止卡死任务无限烧钱。
4. **批量合并**：多个相关检查合并为一个任务，减少调用次数。
5. **降频**：多数任务 5 分钟一次没必要，适当降频。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent
- **操作系统**：Linux / macOS / Windows
- **底层依赖**：需配合定时调度专家引擎（cron-scheduler-pro）执行实际调度

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| skill-platform CLI | CLI | 必需 | 平台内置或安装 |
| cron-scheduler-pro | 关联技能 | 推荐 | 作为底层引擎 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| jq | CLI | 可选（成本分析） | 包管理器安装 |

### API Key 配置
- 本技能本身无需 API Key。
- 被调度的任务可能调用外部 API（由具体任务决定）。
- `--model` 参数控制任务执行用哪个 LLM 模型，费用由平台账户承担。

### 可用性分类
- **分类**：MD+EXEC（Markdown 指令 + CLI 执行）
- **说明**：Agent 通过自然语言驱动 CLI，助手负责解析、模板匹配与成本建议，底层调度委托给引擎层。
