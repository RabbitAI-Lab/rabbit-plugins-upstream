# MochiLab 每日计划与复盘 · Daily Planner and Review

`mochi-daily-planner` · v1.0.0 · MIT-0

整理当天任务、优先级和可用时间，跟踪完成情况，把未完成事项安排到后续日期。

Organize daily priorities and available time, track completion and carry unfinished tasks to a later date.

## 安装 / Install

将本目录放到当前 OpenClaw 助手工作区的 `skills/` 目录，运行 `openclaw skills info mochi-daily-planner`，再开始新对话。

Copy this folder into the active OpenClaw agent workspace's `skills/` directory, check readiness, then start a fresh conversation.

Node.js 24.16+ is required. Use the model already connected to your agent; this standalone Skill needs no MochiLab account key.

## 使用 / Use

Read [SKILL.md](SKILL.md), [input contract](references/input.md), and the samples before running the helper. Local records stay in the active agent workspace.

OpenClaw、已连接的模型、Node.js 24.16+、当前助手工作区的读写权限。

OpenClaw, a connected model, Node.js 24.16+, and read/write access to the current agent workspace. 

## 示例 / Examples

## 能帮你做什么

记录任务预计用时和优先级，显示超出可用时间的部分；完成后更新状态，复盘时保留原日期并衔接下一天。

## 直接这样说

```text
今天有六件事，只有四小时，帮我排优先级。
```

```text
上午这两件已经做完了，更新一下。
```

```text
复盘今天，把没完成的事情安排到明天。
```

## 保存与继续使用

结果保存在当前助手的工作区，后续可以按记录编号查找和继续处理。


## What it does

Store task duration estimates and priorities, show work exceeding available time, record completions and carry open work forward while retaining the original day.

## Try it

```text
I have six tasks and four hours today; help me prioritize.
```

```text
These two tasks are done; update today’s plan.
```

```text
Review today and move unfinished tasks to tomorrow.
```

## Save and continue

Records stay in the active agent workspace and can be retrieved by their IDs.


Source: https://mochilab.bz/ · License: [MIT-0](LICENSE)
