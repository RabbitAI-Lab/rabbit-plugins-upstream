---
slug: "calendar-reminder-free"
name: "calendar-reminder-free"
version: 1.0.1
displayName: "日历提醒(免费版)"
summary: "每晚22点扫描明日Outlook日历,基础飞书提醒,支持手动运行与cron注册。"
license: "MIT"
description: |-
  面向个人开发者的 Outlook 日历提醒 Skill 免费版。每晚 22:00 扫描明日 Outlook 日历,
  将上午日程与下午日程分别按"提前 2 小时"和"当天 12:00 统一"两种基础策略推送飞书提醒.
  基于 owa-outlook skill 提供的 owa_calendar.py 读取日历数据,通过 skill-platform CLI 注册 cron.
  适用于个人每日日程前置提醒的基础场景。高级特性(跨时区处理、团队群共享、安静时段、
  多渠道通知)请升级付费版.
tags:
  - 通用办公
  - Automation
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
pricing_tier: "L1-入门级"
suggested_price: "9.9 CNY/per_use"

---
# Calendar Reminder Free 日历提醒(免费版)

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 日历提醒(免费版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 概述

Calendar Reminder Free 是日历提醒 Skill 的免费版本,提供基础的每晚 22:00 扫描明日 Outlook 日历并按上下午时段推送飞书提醒的能力。适合个人开发者快速搭建每日日程提醒工作流.
## 核心能力

### 1. 每晚 22:00 扫描明日日历
在每晚 22:00(Asia/Shanghai 时区)自动拉取明日 Outlook 日历的全部日程,包括会议主题、开始时间、结束时间、组织者、地点等基础字段。扫描完成后立即发送一条汇报消息到飞书.
**输入**: 用户提供每晚 22:00 扫描明日日历所需的指令和必要参数.
**输出**: 返回每晚 22:00 扫描明日日历的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`每晚 22:00 扫描明日日历`的配置文档进行参数调优
### 2. 上下午差异化提醒
- **上午日程(开始时间 < 12:00)**:提前 2 小时飞书提醒.
- **下午日程(开始时间 >= 12:00)**:当天 12:00 统一汇总提醒.
**处理**: 解析上下午差异化提醒的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回上下午差异化提醒的处理结果,包含执行状态码、结果数据和执行日志.
### 3. Cron 定时任务注册
通过 `skill-platform cron add` 命令注册每日扫描任务,任务持久化在 skill-platform 中.
**输入**: 用户提供Cron 定时任务注册所需的指令和必要参数.
**处理**: 解析Cron 定时任务注册的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Cron 定时任务注册的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`Cron 定时任务注册`的配置文档进行参数调优
### 输出格式

完成响应以Markdown格式返回,包含任务状态(成功/失败)、解析摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。- 验证返回数据的完整性和格式正确性
- 参考`输出格式`的配置文档进行参数调优
#
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 适用场景

### 场景一：个人开发者每日晨会提醒

- **输入**: 配置飞书 open_id 后,每晚 22:00 自动触发
- **输出**: 次日 07:30 收到飞书提醒"09:30 晨会",12:00 收到下午日程汇总
- **价值**: 避免早晨匆忙错过晨会

### 场景二：基础日程预览

- **输入**: 明日有 3 场会议
- **输出**: 22:00 收到飞书汇报"明日共 3 场会议,上午 1 场,下午 2 场"
- **价值**: 睡前掌握明日安排

## 使用流程

### 步骤一：确认依赖

```bash
python3 --version  # 需要 3.9+
skill-platform --version
```

### 步骤二：配置飞书 open_id

编辑 `calendar_reminder.py` 中 `send_feishu` 函数,将 `target` 改为你的飞书 open_id:

```python
"--target", "user:ou_xxxxxxxxxxxxxxxx",
```

### 步骤三：注册 cron 任务

```bash
skill-platform cron add \
  --name "calendar-daily-scan" \
  --cron "0 22 * * *" \
  --tz "Asia/Shanghai" \
  --session main \
  --system-event "CALENDAR_SCAN: 请立即运行 python3 ~/.skill-platform/workspace/skills/calendar-reminder/calendar_reminder.py 并等待完成" \
  --description "每晚22:00扫描明天日历并设置提醒"
```

### 步骤四：手动验证

```bash
python3 ~/.skill-platform/workspace/skills/calendar-reminder/calendar_reminder.py
```

检查飞书是否收到扫描汇报消息.
#
## 案例展示

### 案例1:个人开发者的晨会提醒

**背景**: 开发者每日 09:30 有站会,经常因早晨处理事务错过.
**运行数据**:
- 22:00 扫描启动,拉取明日 3 条日程
- 22:02 飞书收到汇报:"明日共 3 场会议,上午 1 场(09:30 站会),下午 2 场"
- 次日 07:30 飞书提醒:"09:30 站会即将开始(提前 2 小时提醒)"
- 次日 12:00 飞书汇总:"下午 2 场会议:14:00 代码评审 / 16:00 周会"

**效果**: 开发者 07:30 收到提醒后提前准备站会内容.
### 案例2:明日无日程的静默处理

**背景**: 周末明日无任何日程.
**运行数据**:
- 22:00 扫描启动,拉取明日 0 条日程
- 22:01 飞书收到汇报:"明日无日程安排,扫描已完成"

**效果**: 用户确认扫描正常运行,无需担心任务失效.
## 异常处理

### 1. owa_calendar.py 调用失败

**原因**: `owa-outlook` skill 未安装或 Outlook 凭据过期.
**处理**: 执行 `python3 -c "import owa_calendar; owa_calendar.list_events()"` 验证 skill 可用;若凭据过期,重新运行 owa-outlook 登录流程刷新 token;网络问题检查代理配置后检查网络连接和配置后重试.
### 2. 飞书消息推送失败

**原因**: open_id 格式错误或机器人 token 过期.
**处理**: 检查 target 是否以 `user:` 前缀开头;若返回 token 错误码,重新获取 tenant_access_token;建议对飞书 API 失败做 3 次检查网络连接和配置后重试.
### 3. zoneinfo 模块导入失败

**原因**: Python 版本低于 3.9 或 Linux 未安装 tzdata.
**处理**: 升级 Python 到 3.9+;在 Debian/Ubuntu 执行 `sudo apt install tzdata`;macOS 通常已内置.
### 4. cron 任务未触发

**原因**: skill-platform 服务未运行或时区配置错误.
**处理**: 执行 `skill-platform cron list` 确认任务存在;检查 `--tz` 参数使用 IANA 时区名(如 Asia/Shanghai);手动触发 `skill-platform cron trigger calendar-daily-scan` 验证.
### 5. 扫描结果中日程缺失

**原因**: Outlook 部分日程为"私有"标记或存在多个日历文件夹.
**处理**: 在 owa-outlook 配置中开启拉取私有事件;在脚本中明确指定要扫描的日历名称,避免 Holidays 等系统日历干扰.
## 常见问题

### Q1: 如何将提醒从个人飞书改为其他渠道?

免费版仅内置飞书推送。若需钉钉、企业微信等渠道,请升级付费版,付费版支持多渠道通知后端切换.
### Q2: 明日没有日程时还会推送消息吗?

会推送一条"明日无日程安排"的汇报消息,确保用户知道扫描已正常执行。若希望静默,可在脚本中增加 `if not events: return` 跳过推送.
### Q3: 如何调整上午/下午的分界时间?

在 `calendar_reminder.py` 中找到 `afternoon_threshold` 变量,修改为目标时间(如 13:00)。免费版需同时手动调整下午统一提醒的 cron 时间.
### Q4: 如何临时禁用某一天的扫描?

执行 `skill-platform cron pause calendar-daily-scan` 暂停,假期结束后执行 `skill-platform cron resume calendar-daily-scan` 恢复.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接和配置后重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 仅支持 Outlook 日历,不支持 Google Calendar、Apple Calendar
- 提醒策略固定为"上午提前 2 小时 / 下午 12:00 汇总",不支持按优先级差异化
- 不支持跨时区日程的智能识别与安静时段判断
- 仅支持飞书推送,不支持团队群共享与多渠道通知
- 依赖 skill-platform cron,服务停止则扫描不执行

## 升级提示

当前为免费版本,提供基础的日历扫描与飞书提醒功能。升级到付费版可获得以下高级特性:

- **跨时区日程智能处理**:自动识别 UTC 时间并正确换算本地提醒时间
- **团队群共享提醒**:支持配置群 chat_id,全员共享明日日程
- **安静时段保护**:凌晨 23:00-07:00 不推送,延后合并提醒
- **全天事件单独处理**:避免全天事件被误判为上午日程
- **多渠道通知**:支持钉钉、企业微信、Slack 等渠道切换
- **扫描结果增强汇报**:标注重点会议、组织者、会议链接

请访问 skill 商城升级到 `calendar-reminder` 付费版获取完整能力.