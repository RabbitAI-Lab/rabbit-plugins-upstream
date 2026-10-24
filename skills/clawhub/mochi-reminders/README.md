# MochiLab 提醒与定时任务 · Reminders and Scheduled Tasks

`mochi-reminders` · v1.0.0 · MIT-0

用一句话安排一次或重复提醒，查看任务编号、执行时间和接收账号，随时调整或暂停。

Create one-time or recurring reminders, inspect job IDs, timing and delivery accounts, and update or pause schedules.

## 安装 / Install

将本目录放到当前 OpenClaw 助手工作区的 `skills/` 目录，运行 `openclaw skills info mochi-reminders`，再开始新对话。

Copy this folder into the active OpenClaw agent workspace's `skills/` directory, check readiness, then start a fresh conversation.

Node.js 24.16+ is required. Use the model already connected to your agent; this standalone Skill needs no MochiLab account key.

## 使用 / Use

Read [SKILL.md](SKILL.md), [input contract](references/input.md), and the samples before running the helper. Local records stay in the active agent workspace.

OpenClaw、已连接的模型、Node.js 24.16+、当前助手工作区的读写权限。OpenClaw 定时任务工具、运行中的 Gateway、当前聊天渠道的投递能力。首次使用会核对可用工具及账号路由。

OpenClaw, a connected model, Node.js 24.16+, and read/write access to the current agent workspace. OpenClaw scheduling tools, a running Gateway, and delivery support for the active chat channel. First use checks tool availability and the account route.

## 示例 / Examples

## 能帮你做什么

解析一次、间隔和周期提醒，明确时区与接收账号；通过 OpenClaw 定时任务能力创建、查看、调整和暂停任务，保存真实任务回执。

## 直接这样说

```text
每周五晚上八点提醒我交周报，按北京时间发到当前微信。
```

```text
列出我创建的提醒，把周报提醒改成晚上七点。
```

```text
每天早上七点准备一份当天简报，发到这个聊天。
```

## 保存与继续使用

结果保存在当前助手的工作区，后续可以按记录编号查找和继续处理。提醒以定时任务工具返回的任务编号及状态为准。

## 运行方式

安装后先核对 OpenClaw 的定时任务和聊天投递能力，确认时区、账号与接收位置，再创建任务。创建结果会显示任务编号和下次执行时间。


## What it does

Resolve one-time, interval and recurring requests with explicit timezones and recipients. Use OpenClaw scheduling to create, inspect, change and pause jobs, keeping actual scheduler receipts.

## Try it

```text
Remind me in this chat every Friday at 8 pm Asia/Shanghai to submit my weekly report.
```

```text
List my reminders and move the weekly report reminder to 7 pm.
```

```text
Prepare a daily brief at 7 am and deliver it to this conversation.
```

## Save and continue

Records stay in the active agent workspace and can be retrieved by their IDs. Scheduled reminders use the job ID and status returned by the scheduler.

## Scheduling

First use checks OpenClaw scheduling and chat delivery, resolves the timezone, account and recipient, then creates the job and shows its ID and next execution time.


Source: https://mochilab.bz/ · License: [MIT-0](LICENSE)
