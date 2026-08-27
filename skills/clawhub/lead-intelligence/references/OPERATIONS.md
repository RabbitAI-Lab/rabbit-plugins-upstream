# Operations 契约

四个 operation 通常同步完成；POST 与对应任务 GET 使用相同 ability。

| operation | POST 路径 | 执行位置 | 主要结果 |
|---|---|---|---|
| `company.search` | `/api/v1/lead-intelligence/company.search` | Provider | `result.companies`、`result.pagination` |
| `people.search` | `/api/v1/lead-intelligence/people.search` | Provider | `result.people`、`result.pagination` |
| `lead.score` | `/api/v1/lead-intelligence/lead.score` | 本地、免费 | `result.leads` |
| `report.create` | `/api/v1/lead-intelligence/report.create` | 本地 | `result.report` |

任务查询固定为 `/api/v1/lead-intelligence/{operation}/tasks/{task_id}`。

## company.search

除分页外至少提供一个过滤条件：

| 字段 | 规则 |
|---|---|
| `company_name` | 可选字符串，最多 200 字符 |
| `domains` | 1–20 个域名；不接受 URL 或 IP |
| `locations`、`excluded_locations` | 各 1–10 项，每项最多 100 字符 |
| `employee_ranges` | 1–10 项，每项最多 30 字符，格式为 `最小值,最大值` 且最小值不大于最大值 |
| `technologies` | 1–20 个技术 UID，每项最多 100 字符，只含字母、数字、`_`、`-` |
| `keywords` | 1–10 项，每项最多 100 字符 |
| `organization_ids` | 1–20 项，每项最多 100 字符，只含字母、数字、`_`、`-` |
| `latest_funding_amount_min/max` | 可选非负整数，min 不大于 max |
| `latest_funding_date_min/max` | 可选 `YYYY-MM-DD`，min 不晚于 max |
| `active_job_count_min/max` | 0–1,000,000，min 不大于 max |
| `active_job_titles` | 1–10 项，每项最多 100 字符 |
| `page` | 1–500，默认 1 |
| `per_page` | 1–50，默认 20 |

示例：

```json
{"domains":["example.com"],"page":1,"per_page":20}
```

`companies[]` 只交付企业标识、名称、公开网站/域名、成立年份和公开企业资料 URL；忽略企业
电话号码等不必要联系方式。`pagination` 含 `page`、`per_page`、`total_entries`、
`total_pages`；`partial_results_only` 说明 Provider 仅返回部分集合。

## people.search

除 `include_similar_titles` 和分页外至少提供一个过滤条件：

| 字段 | 规则 |
|---|---|
| `titles` | 1–20 项，每项最多 100 字符 |
| `include_similar_titles` | 可选布尔值，默认 false |
| `keywords` | 可选字符串，最多 200 字符 |
| `locations`、`organization_locations` | 各 1–10 项，每项最多 100 字符 |
| `seniorities` | 1–11 项：`owner`、`founder`、`c_suite`、`partner`、`vp`、`head`、`director`、`manager`、`senior`、`entry`、`intern` |
| `organization_domains` | 1–20 个域名；不接受 URL 或 IP |
| `organization_ids` | 1–20 项，每项最多 100 字符，只含字母、数字、`_`、`-` |
| `employee_ranges` | 1–10 项，每项最多 30 字符，格式为 `最小值,最大值` |
| `technologies` | 1–20 个技术 UID，每项最多 100 字符，只含字母、数字、`_`、`-` |
| `active_job_titles` | 1–10 项，每项最多 100 字符 |
| `page` | 1–500，默认 1 |
| `per_page` | 1–50，默认 20 |

示例：

```json
{"titles":["销售总监"],"organization_domains":["example.com"],"include_similar_titles":false,"page":1,"per_page":20}
```

`people[]` 可含 `id`、`first_name`、脱敏的 `last_name_obfuscated`、`title`、
`last_refreshed_at`、`organization.name`、`email_available`、`direct_phone_available`。
不返回邮箱，不返回或推断电话；availability 只表示 Provider 声称可能可用，不是联系方式。

## lead.score

`leads` 必填 1–50 项，每项只允许：必填 `id`（最多 100）、`company_name`（最多 200）；
可选 `title`（最多 200）、`latest_funding_date`（`YYYY-MM-DD`）、`active_job_count`
（0–1,000,000）、`technologies`（最多 50 项，每项最多 100）。`target_titles` 与
`target_technologies` 各最多 50 项，每项最多 100 字符。

```json
{"leads":[{"id":"l1","company_name":"Example","title":"销售总监","latest_funding_date":"2026-07-01","active_job_count":3,"technologies":["salesforce"]}],"target_titles":["销售总监"],"target_technologies":["salesforce"]}
```

结果每项含 `id`、`company_name`、可选 `title`、`points`、`score`、`reasons`。本地执行且
免费，计费头仍是唯一账单依据。

## report.create

`leads` 必填 1–50 项，每项只允许：必填 `id`（最多 100 字符）、`company_name`（最多
200 字符）；可选 `person_name`、`title`、`location`（各最多 200 字符）；
`technologies` 最多 50 项且每项最多 100 字符；必填整数 `score`（0–100）；可选
`reasons` 最多 6 项且每项最多 100 字符。结果大小必须能放入平台 50,000 字节安全展示上限。

`result.report` 含 `lead_count`、`average_score`、`high_priority_count`、`score_bands` 和最多
10 条 `top_leads`。报告只是对提交线索的确定性排序汇总，不搜索新联系人。
