# Google 账户分析报告

> 统计区间：`{startDate}` ~ `{endDate}`  
> 账户：`{mediaCustomerId}`

> **默认交付物**：一份可打开的、带 ECharts 图表的 **HTML 文件**（`google-period-report.html`）。  
> 用户**未指定格式**时一律走下方 **标准四步流程**；**禁止** Agent 手写/拼接 HTML（语法错误会导致报告无法显示）。  
> **用户明确要求 Excel / xlsx**（且非 OKKI / 询盘话术）时：在拉数步骤不变的前提下，**另 Read 全文** `report-templates/google-period-report-excel.md`，并**先读齐**各维度 `*.outline.txt` 再写脚本；禁止加载宿主第三方 xlsx Skill；**不要**调用 `google-analysis render`。

---

## 标准四步流程（默认 · 交付 HTML）

| 步骤             | 执行者       | 动作                                                                                                                                                                                                               |
| ---------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. 拉数**      | Agent 调 CLI | `google-analysis -a <id> --start <s> --end <e> --json-out ./snap-google --sections <见下方默认维度对应 CLI>`                                                                                                       |
| **2. 分析**      | Agent        | 用 **node/python 脚本**读落盘 JSON（勿用 Read 打开业务 `*.json`），完成筛选、聚合、排序与洞察                                                                                                                      |
| **3. 写 JSON**   | Agent        | 按 `assets/google-period-report.schema.json` 撰写 `google-period-report.json`：只写 `meta` + `narrative`（8 维度叙事）；`kpis`/`charts`/`tables` 留给步骤 4 的 `--snapshot-dir` 合并（合并后缺 KPI 会拒绝出 HTML） |
| **4. 渲染 HTML** | CLI          | `google-analysis render` — **校验 narrative 8 维度必含字段**，缺项报错不生成 HTML；**禁止** Agent 手写/拼接 HTML                                                                                                   |

```bash
# 步骤 1
siluzan-tso google-analysis -a <id> --start <s> --end <e> --json-out ./snap-google \
  --sections overview,daily-metrics,dimension-summary,campaigns,devices,geographic,keywords

# 步骤 4（步骤 2～3 完成后）
siluzan-tso google-analysis render \
  --data ./google-period-report.json \
  --snapshot-dir ./snap-google \
  --out ./google-period-report.html
```

`google-period-report.json` 顶层结构：

- `meta`：`accountId`（必填）/ `accountName` / `currency` / `startDate` / `endDate`；可省略由 `--snapshot-dir` 从 `overview` + manifest 自动合并。
- `kpis`：账户级 KPI（消耗/展示/点击/转化/CTR/CPC/CPA，含可选 `previousPeriod` 环比）；Agent 可省略，但 **render 合并后** `cost`/`impressions`/`clicks` 至少一项须为有效数字，否则拒绝出 HTML（避免执行摘要卡片全「—」）。本期 KPI 由 CLI 优先对 `campaigns` 全系列累加并重算比率；无 campaigns 时回退 `overview.currentPeriod`，再回退 `dimension-summary`。环比仍来自 `overview.previousPeriod`。
- `charts.dailyTrend`：每日趋势（`dates`/`cost`/`conversions`/`cpa`）；可省略由 `daily-metrics` 自动合并。
- `tables.{dimensionSummary,campaigns,devices,geographic,keywords}`：对应 §3～§7 表格数据；可省略由同名 `google-analysis` section 自动合并。
- `narrative`（**Agent 必填，唯一由 Agent 撰写的内容**）：
  - `executiveSummary[]`：≥1 段执行摘要
  - `sections.{overview,dailyTrend,dimensionSummary,campaigns,devices,geographic,keywords}`：每个维度各 `{analysis[]（≥2 条）, suggestions[]（≥1 条）}`，对应报告 §1～§7
  - `recommendations[]`：≥3 条跨维度优化建议，对应报告 §8

完整字段定义见 `assets/google-period-report.schema.json`。

**Excel 分支**（用户明确要 xlsx 时）：

1. 步骤 1～2 与 HTML 流程相同（拉数 → 分析）。
2. 改为 Agent 执行 node/python 脚本按 `google-period-report-excel.md` 写出 `.xlsx`（先读齐 `*.outline.txt`）。
3. **不要**调用 `google-analysis render`（除非用户同时要 HTML + Excel）。
4. **禁止**假设存在 `siluzan-tso … excel` 子命令。

模板源码：`report-templates/google-period-report.html`（结构与样式，ECharts 渲染逻辑已内联）。

`render` 会向输出目录写入 HTML，并注入 `window.__GOOGLE_PERIOD_REPORT__`。  
传 `--snapshot-dir` 时 CLI 自动从快照合并 KPI、每日趋势图表、周期汇总/系列/设备/地域/关键词表格：**数值一律以 CLI 快照覆盖**（`meta` 仅补空）。本期 KPI 优先 `campaigns` 累加。若 manifest 缺条目但磁盘上仍有对应 `*.json`，CLI 会按文件名自愈补齐。Agent 只写 `narrative`，勿自填 `kpis`/`tables`。

---

## 默认报告维度

生成报告时，**默认包含**以下 8 个维度：

| #   | 维度                                                                         | CLI                                                                                           |
| --- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| 1   | 执行摘要（消耗/展示/点击/转化/CTR/CPC/CPA 本期概览）                         | `google-analysis --sections overview`                                                         |
| 2   | 每日投放趋势（按日消耗/点击/转化曲线；金额/CPA **2 位小数**，转化/点击整数） | `google-analysis --sections daily-metrics`                                                    |
| 3   | 月度汇总（全周期汇总数据）                                                   | `google-analysis --sections dimension-summary`                                                |
| 4   | 广告系列表现（预算/出价策略/各系列消耗与效果）                               | `google-analysis --sections campaigns`                                                        |
| 5   | 设备分布（PC/移动/平板 消耗/点击/转化）                                      | `google-analysis --sections devices`                                                          |
| 6   | 地域分布（国家/地区 消耗占比）                                               | `google-analysis --sections geographic`                                                       |
| 7   | 关键词表现（词/消耗/CTR/CPC 排行）                                           | `google-analysis --sections keywords`（这个命令获取的关键词数据会来自多个系列，不能合并去重） |
| 8   | 优化建议（根据以上数据给出可执行改进建议）                                   | 不额外拉数，基于已有数据撰写                                                                  |

**在执行任何数据拉取之前**，先向用户展示以下可选维度，询问是否需要追加：

---

## 平台支持的全部可选维度

| 维度          | CLI                                             | 备注                                                              |
| ------------- | ----------------------------------------------- | ----------------------------------------------------------------- |
| 系列按小时    | `google-analysis --sections campaign-hour`      | 行在 `items[]`，含 `date`/`hour`/消耗与效果                       |
| 受众分布      | `google-analysis --sections audience`           | 可分 `SystemDefined` / `UserDefined`                              |
| 搜索词报告    | `google-analysis --sections search-terms`       | 高消耗搜索词；`queryTargetingStatusZh` 列（已添加/已排除/都没有） |
| 广告创意表现  | `google-analysis --sections ads`                | 广告标题/类型/到达网址                                            |
| 附加信息      | `google-analysis --sections extensions`         | 附加链接/电话/宣传信息等状态                                      |
| 图片/视频素材 | `google-analysis --sections materials`          | 图片 + 视频合并视图                                               |
| 账户落地页    | `google-analysis --sections final-urls`         | 主投放域名/落地页（不传日期）                                     |
| 黄金账户评分  | `google-analysis --sections gold-account`       | 健康度评分与各项达标状态                                          |
| 广告质量指标  | `google-analysis --sections ads-index`          | 质量得分汇总                                                      |
| 转化动作配置  | `google-analysis --sections conversion-actions` | 已配置的转化目标列表                                              |
| 账户结构统计  | `google-analysis --sections resource-counts`    | 系列/组/广告/词数量                                               |
| 广告系列类型  | `google-analysis --sections campaign-types`     | 系列类型分布（不传日期）                                          |

---

## 拉数顺序（默认 7 个维度）

**首选：用 `google-analysis --sections` 一次拉齐**（单进程复用 keep-alive，比逐个 spawn 快 3-7×；详见 `references/analytics/account-analytics.md` 的 `all` 子命令说明）：

```bash
mkdir -p ./snap-google
siluzan-tso google-analysis -a <id> --start <s> --end <e> --json-out ./snap-google \
  --sections overview,daily-metrics,dimension-summary,campaigns,devices,geographic,keywords
```

如果用户**追加**了维度（按上文「可选追加」表），把它们加入 `--sections` 即可；要全 21 维则省略 `--sections`。

> 仅在调试单个维度或需要传 `all` 暂未透传的特殊参数时，才回落到逐条 `siluzan-tso google-analysis <子命令> -a <id> …` 调用。

---

## 广告系列状态列（必读）

`campaigns-*.json` → `items[]` 每行含 CLI 注入的 **`campaignStatusDisplay`**（`投放中` / `已暂停` / `已移除`）。

| 正确                                                                              | 错误                                                                                      |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 直接展示 `row.campaignStatusDisplay`                                              | 读 `campaignStatus` 后自行 `MAP[s] \|\| '已移除'`（`Enabled` 未命中键时会全变「已移除」） |
| 需要英文枚举时读 `campaignStatus` 或 `campaignStatusV2`，展示前 `.upper()` 再映射 | 用 `stats` / `list-accounts` 的账户 `status` 充当系列状态                                 |

原始枚举为 PascalCase（`Enabled`），与 `ad campaigns` 的 `statusDisplay`（如 `Enabled·有效` / `Enabled·投放期已结束`）口径不同；周期报告「状态」列统一用 **`campaignStatusDisplay`**。
