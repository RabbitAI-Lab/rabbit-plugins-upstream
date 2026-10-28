# MochiLab 日常记账与预算 · Expense Tracker and Budgets

`mochi-expense-tracker` · v1.0.0 · MIT-0

对话记录收入、支出和退款，按币种与分类汇总，查看月度预算进度。

Log income, spending and refunds through conversation, summarize by currency and category, and track monthly budgets.

## 安装 / Install

将本目录放到当前 OpenClaw 助手工作区的 `skills/` 目录，运行 `openclaw skills info mochi-expense-tracker`，再开始新对话。

Copy this folder into the active OpenClaw agent workspace's `skills/` directory, check readiness, then start a fresh conversation.

Node.js 24.16+ is required. Use the model already connected to your agent; this standalone Skill needs no MochiLab account key.

## 使用 / Use

Read [SKILL.md](SKILL.md), [input contract](references/input.md), and the samples before running the helper. Local records stay in the active agent workspace.

OpenClaw、已连接的模型、Node.js 24.16+、当前助手工作区的读写权限。

OpenClaw, a connected model, Node.js 24.16+, and read/write access to the current agent workspace. 

## 示例 / Examples

## 能帮你做什么

以最小货币单位精确记账，收入、支出与退款分开保存；支持分类统计、月度预算和保留原因的作废更正。

## 直接这样说

```text
午饭三十二元，打车十八元，分别记一下。
```

```text
这个月餐饮预算一千二，看看用了多少。
```

```text
刚才那笔打车记错了，作废并补录二十元。
```

## 保存与继续使用

结果保存在当前助手的工作区，后续可以按记录编号查找和继续处理。


## What it does

Store exact minor-unit amounts, distinguish income, expenses and refunds, summarize categories, track monthly budgets and void incorrect entries with a reason.

## Try it

```text
Log CNY 32 for lunch and CNY 18 for a taxi as separate entries.
```

```text
Set this month’s dining budget to CNY 1200 and show progress.
```

```text
Void the incorrect taxi entry and record CNY 20 instead.
```

## Save and continue

Records stay in the active agent workspace and can be retrieved by their IDs.


Source: https://mochilab.bz/ · License: [MIT-0](LICENSE)
