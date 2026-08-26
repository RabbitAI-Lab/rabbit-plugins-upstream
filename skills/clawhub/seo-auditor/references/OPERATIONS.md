# Operations 契约

| operation | POST 路径 | 行为 | 主要结果 |
|---|---|---|---|
| `keyword.research` | `/api/v1/seo-auditor/keyword.research` | 通常同步、需要 Provider | `result.metrics` |
| `page.audit` | `/api/v1/seo-auditor/page.audit` | 异步、需要 Provider | `result.findings` |
| `competitor.gap` | `/api/v1/seo-auditor/competitor.gap` | 通常同步、需要 Provider | `result.metrics` |
| `report.create` | `/api/v1/seo-auditor/report.create` | 本地同步、不需要 Provider | `result.report` |

对应任务 GET 为 `/api/v1/seo-auditor/{operation}/tasks/{task_id}`。

## keyword.research

`keywords` 必填 1–100 项，每项最多 80 字符且最多 10 个空白分隔词。可选正整数
`location_code` 和最多 12 字符的 `language_code`。

```json
{"keywords":["seo","laravel"],"location_code":2840,"language_code":"en"}
```

`metrics[]` 可含 `keyword`、`search_volume`、`cpc`、`competition`、
`competition_level`、`source`、`observed_at`。空值保持 null，不推断指标。

## page.audit

仅接受一个字段：`url`，必填公开 HTTP(S) URL，最多 220 字符。禁止用户名/密码、非标准
端口、localhost、IP 字面量、私网或保留地址。平台会保存解析证据并在执行前重新解析；DNS
变化或重绑定导致任务安全失败。

```json
{"url":"https://example.com"}
```

`findings[]` 可含 `severity`、`field`、`current_value`、`evidence_url`、
`recommendation`、`source`、`observed_at`；聚合发现使用 `affected_pages` 而不是伪造单页
`evidence_url`。

## competitor.gap

`site_domain` 必填域名，最多 253 字符；`competitor_domains` 必填且恰好 1 个域名，每项最多
253 字符。可选正整数 `location_code`、最多 12 字符 `language_code`、整数 `limit` 1–20。
这里的域名只是受控 Provider 查询参数，Skill 不直接访问目标主机。

```json
{"site_domain":"example.com","competitor_domains":["competitor.example"],"location_code":2840,"language_code":"en","limit":20}
```

结果读取 `metrics[]`，并保留每项来源与观察时间。

## report.create

可选 `title` 最多 200 字符。必须提供非空 `findings` 或 `metrics`；最多 50 个 findings 和
100 个 metrics，最终 structured 结果不得超过平台安全展示上限。

Finding 字段：

- `severity` 必填：`critical`、`high`、`medium`、`low`、`info`。
- `field` 必填，最多 100；`recommendation` 必填，最多 1000。
- `source` 必填，最多 2048；`observed_at` 必填 ISO 8601 时区时间。
- 单页证据提供 HTTP(S) `evidence_url`（最多 2048）和可选 `current_value`（最多 1000）。
- 聚合证据改用正整数 `affected_pages`，不能同时传 `evidence_url` 或 `current_value`。

Metric 字段：`keyword` 必填最多 80，`source` 和 `observed_at` 必填；可选非负整数
`search_volume`、非负 `cpc`、0–1 `competition`、最多 20 字符 `competition_level`。

```json
{"title":"SEO 对比报告","metrics":[{"keyword":"seo","search_volume":1000,"cpc":2.5,"competition":0.7,"competition_level":"HIGH","source":"provider:keyword-metrics","observed_at":"2026-08-11T10:00:00+08:00"}]}
```

报告读取 `title`、`finding_count`、`metric_count`、`severity_counts`、`findings`、`metrics`。
不要传 task ID、任意旧响应或没有真实来源的本地猜测。
