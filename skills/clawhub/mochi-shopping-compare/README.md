# MochiLab 购物比较助手 · Shopping Comparison

`mochi-shopping-compare` · v1.0.0 · MIT-0

对照商品规格、价格和使用成本，区分已确认信息与待补充信息，整理购买选择。

Compare product specifications, prices and usage costs, separating confirmed facts from missing information.

## 安装 / Install

将本目录放到当前 OpenClaw 助手工作区的 `skills/` 目录，运行 `openclaw skills info mochi-shopping-compare`，再开始新对话。

Copy this folder into the active OpenClaw agent workspace's `skills/` directory, check readiness, then start a fresh conversation.

Node.js 24.16+ is required. Use the model already connected to your agent; this standalone Skill needs no MochiLab account key.

## 使用 / Use

Read [SKILL.md](SKILL.md), [input contract](references/input.md), and the samples before running the helper. Local records stay in the active agent workspace.

OpenClaw、已连接的模型、Node.js 24.16+、当前助手工作区的读写权限。查询当前商品页面和价格时使用 OpenClaw 可用的联网浏览工具。

OpenClaw, a connected model, Node.js 24.16+, and read/write access to the current agent workspace. Current product-page and price research uses the browsing tools available to OpenClaw.

## 示例 / Examples

## 能帮你做什么

按用户用途建立比较标准，记录商品来源和查询日期，精确计算已知价格、数量、运费与优惠，分别展示各币种结果。

## 直接这样说

```text
比较这三款打印机，重点看一年耗材成本。
```

```text
预算两千元，这两台显示器哪个更适合写代码？
```

```text
把这几个商品的价格、运费和规格整理在一起。
```

## 保存与继续使用

结果保存在当前助手的工作区，后续可以按记录编号查找和继续处理。


## What it does

Use the buyer’s needs to define criteria, retain product sources and observation dates, and calculate known prices, quantities, shipping and discounts by currency.

## Try it

```text
Compare these three printers, including a year of consumables.
```

```text
Which of these monitors suits coding within a CNY 2000 budget?
```

```text
Organize these product prices, shipping costs and specifications.
```

## Save and continue

Records stay in the active agent workspace and can be retrieved by their IDs.


Source: https://mochilab.bz/ · License: [MIT-0](LICENSE)
