# MochiLab 工作日报与周报 · Daily and Weekly Work Reports

`mochi-work-reports` · v1.0.1 · MIT-0

根据真实工作记录整理进展、成果、阻碍与后续安排，保留事项来源和时间范围。

Turn actual work records into progress, completed work, blockers and next steps, retaining sources and reporting periods.

## 安装 / Install

将本目录放到当前 OpenClaw 助手工作区的 `skills/` 目录，运行 `openclaw skills info mochi-work-reports`，再开始新对话。

Copy this folder into the active OpenClaw agent workspace's `skills/` directory, check readiness, then start a fresh conversation.

Node.js 24.16+ is required. Use the model already connected to your agent; this standalone Skill needs no MochiLab account key.

## 使用 / Use

Read [SKILL.md](SKILL.md), [input contract](references/input.md), and the samples before running the helper. Local records stay in the active agent workspace.

OpenClaw、已连接的模型、Node.js 24.16+、当前助手工作区的读写权限。

OpenClaw, a connected model, Node.js 24.16+, and read/write access to the current agent workspace. 

## 示例 / Examples

## 能帮你做什么

积累带日期和依据的工作事项，按日或周筛选，分成已完成、进行中和待解决事项，再整理为适合接收人的报告。

## 直接这样说

```text
记录一下，今天完成登录页修改，依据是这份提交记录。
```

```text
按这周的工作记录整理周报，重点写进度和阻碍。
```

```text
把这份流水账改成适合发给主管的日报。
```

## 保存与继续使用

结果保存在当前助手的工作区，后续可以按记录编号查找和继续处理。


## What it does

Capture dated, evidenced work records, filter daily or weekly periods, group completed work, work in progress and blockers, and draft for the intended audience.

## Try it

```text
Record today’s login-page update using this commit as the source.
```

```text
Prepare a weekly report from my records, focusing on progress and blockers.
```

```text
Turn these work notes into a concise daily report for my manager.
```

## Save and continue

Records stay in the active agent workspace and can be retrieved by their IDs.


Source: https://mochilab.bz/ · License: [MIT-0](LICENSE)
