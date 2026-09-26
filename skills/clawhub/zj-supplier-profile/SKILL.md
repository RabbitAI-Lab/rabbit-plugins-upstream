---
name: 浙江供应商资质业绩核验
slug: zj-supplier-profile
displayName: 浙江供应商资质业绩核验
display_name: 浙江供应商资质业绩核验
version: 1.0.4
summary: 浙江供应商资质业绩核验，一次查清一家企业是否在科技型中小企业名录、有没有工程中标业绩。当用户需要供应商资质核验、中标业绩查询、供应商入围筛选、投标对手摸底、供应商尽调、企业名录查询时使用。触发词 供应商核验、资质核验、中标业绩、入围筛选、投标摸底、供应商尽调、企业名录、浙江供应商、**招标公告、中标公告、招投标**。
description: 浙江供应商双证据核验，按企业名交叉核验资质（科技型中小企业名录）与业绩（工程中标记录）
description_zh: 输入企业名称，得到它在浙江省科技型中小企业名录的收录情况与工程中标记录（条数、金额档位与区间），并给出四类互斥结论与建议动作
description_en: Dual-evidence supplier check for Zhejiang: whether a company is in the technology-SME roster and what public-works contracts it has won, with four mutually exclusive verdicts.
allowed-tools: Bash(node scripts/run.mjs:*)
permissions:
  network: ["数据接口地址（HTTPS）"]
  files: ["~/.odf/combo-supplier-profile.json（仅本产品凭据与安装标识）"]
  note: 只运行本技能自带的 scripts/run.mjs；不安装依赖、不执行远程代码、不读其它本地文件
author: chenqingggong
category: business-ops
subCategories: [biz-sales, biz-growth]
tags: ["供应商", "资质", "业绩", "中标", "中标公告", "招标公告", "招投标", "名录", "浙江", "尽调"]
---

# 浙江供应商资质业绩核验

输入一家企业名称，得到**交叉结论**：它有没有科技型中小企业资质、有没有工程中标业绩。

## 你会得到

- **结论（四类互斥）**：双证据 / 只有资质 / 只有业绩 / 都没有，并给对应动作建议
- **资质证据**：是否在浙江省科技型中小企业名录（含本库收录量与最新批次）
- **业绩证据**：中标条数、可信金额合计与档位（只统计该类型合理区间，超出部分印出条数）
- **组合口径**：组合键（企业名称）、粒度（企业级）、整体时效（取最旧组件）

## 怎么用

用户问起某家供应商的资质或业绩时，**执行脚本取真实数据**（不要凭记忆作答、不要编造数字）：

```bash
node scripts/run.mjs "浙江求是工程咨询监理有限公司"
```

## 数据边界（请如实告知用户）

- 名录只含**已采集批次**（未命中 ≠ 不在名录）；合同库为历史区间（**不是实时行情**）；
- 未命中不等于不存在；建议用统一社会信用代码复核；
- 本产品提供公开记录整理，**不构成对企业信用的评价**。
