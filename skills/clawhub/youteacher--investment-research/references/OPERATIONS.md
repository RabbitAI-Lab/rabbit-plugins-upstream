# Operations 契约

| operation | POST 路径 | 行为 | 主要结果 |
|---|---|---|---|
| `filing.search` | `/api/v1/investment-research/filing.search` | 通常同步、需平台 Provider | `result.filings` |
| `company.facts` | `/api/v1/investment-research/company.facts` | 通常同步、需平台 Provider | `result.facts` |
| `risk.analyze` | `/api/v1/investment-research/risk.analyze` | 本地同步、固定模板 | `result.risks` |
| `report.create` | `/api/v1/investment-research/report.create` | 本地同步、固定模板 | `result.report` |

对应任务 GET 为 `/api/v1/investment-research/{operation}/tasks/{task_id}`。四个 operation/ability
均返回 structured 结果；HTTP `202` 时按任务查询恢复。

## filing.search

`cik` 必填 1–10 位数字，平台补齐为 10 位。可选 `forms` 最多 10 项，每项最多 20 字符并
规范为大写；`filed_from`/`filed_to` 为 `YYYY-MM-DD` 且起始不晚于结束；`limit` 1–20，
默认 20。不要传 host、URL、path、排序或 User-Agent。

```json
{"cik":"320193","forms":["10-K","10-Q"],"limit":20}
```

读取 `cik`、`company_name` 及 `filings[]`：`accession`、`filed`、`report_date`、`form`、
`primary_document`、`description`、`source`、`observed_at`。空数组仅表示本次查询无结果。

## company.facts

`cik` 规则同上。可选 `taxonomies` 最多 5 项（每项 64）、`tags` 最多 20 项（每项 256）、
`units` 最多 10 项（每项 64），以及同样的日期范围和 `limit` 1–20。

```json
{"cik":"320193","taxonomies":["us-gaap"],"tags":["Revenue","NetIncomeLoss"],"units":["USD"],"limit":20}
```

读取 `cik`、`company_name` 及 `facts[]`：`taxonomy`、`tag`、`unit`、`value`、`period`、
`start`、`end`、`fy`、`fp`、`form`、`filed`、`accession`、`frame`、`source`、
`observed_at`。数值可能是整数或为保留精度而返回的字符串，不自行转浮点数；不同 unit 或
period 不合并。平台保留每个 taxonomy/tag/unit/period 的最新申报事实。

## risk.analyze 与 report.create

两者只接受一个字段：`source_task_ids`，必填 1–2 个互异 UUID。ID 必须来自当前用户在本
产品中真实成功或 `partial` 的 `filing.search`/`company.facts` 任务；来源结果不能截断、篡改
或超过合计 40 条证据。

```json
{"source_task_ids":["11111111-1111-4111-8111-111111111111","22222222-2222-4222-8222-222222222222"]}
```

示例 UUID 只说明格式，实际必须使用查询响应的 `task_id`。`risk.analyze` 返回 `risks[]` 与
顶层 `disclaimer`；每项包含 `category`、`conclusion`、`filed`、`evidence[]`。
`report.create` 返回固定 `title`、`conclusion_count`、`conclusions[]`、`disclaimer`。
两者不调用 LLM、不访问上游、不接受 title/company_name/category/conclusion/summary/evidence/source
等客户端自由文本。
