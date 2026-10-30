# MochiLab 菜谱与买菜清单 · Meal Planner and Grocery List

`mochi-meal-planner` · v1.0.0 · MIT-0

按人数、预算、忌口和现有食材安排菜谱，合并用量并整理买菜清单。

Plan meals around servings, budget, exclusions and pantry ingredients, then merge quantities into a grocery list.

## 安装 / Install

将本目录放到当前 OpenClaw 助手工作区的 `skills/` 目录，运行 `openclaw skills info mochi-meal-planner`，再开始新对话。

Copy this folder into the active OpenClaw agent workspace's `skills/` directory, check readiness, then start a fresh conversation.

Node.js 24.16+ is required. Use the model already connected to your agent; this standalone Skill needs no MochiLab account key.

## 使用 / Use

Read [SKILL.md](SKILL.md), [input contract](references/input.md), and the samples before running the helper. Local records stay in the active agent workspace.

OpenClaw、已连接的模型、Node.js 24.16+、当前助手工作区的读写权限。

OpenClaw, a connected model, Node.js 24.16+, and read/write access to the current agent workspace. 

## 示例 / Examples

## 能帮你做什么

先确认人数、餐次和饮食偏好，生成可执行的菜谱；按食材和单位汇总采购量，扣除现有库存，保存每次方案。

## 直接这样说

```text
两个人，一周晚餐，预算三百元，尽量少洗锅。
```

```text
冰箱里有半公斤番茄，帮我安排三天晚饭并列买菜清单。
```

```text
不吃花生，把这周的午餐换一版。
```

## 保存与继续使用

结果保存在当前助手的工作区，后续可以按记录编号查找和继续处理。


## What it does

Confirm servings, meals and preferences, propose practical menus, aggregate ingredient quantities by compatible units, deduct pantry stock and save each plan.

## Try it

```text
Plan a week of dinners for two, with a CNY 300 budget and easy cleanup.
```

```text
I have half a kilogram of tomatoes; plan three dinners and list what to buy.
```

```text
Replace this week’s lunches and exclude peanuts.
```

## Save and continue

Records stay in the active agent workspace and can be retrieved by their IDs.


Source: https://mochilab.bz/ · License: [MIT-0](LICENSE)
