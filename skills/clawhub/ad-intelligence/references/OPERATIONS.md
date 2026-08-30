# Operations 契约

三个 operation 通常同步完成；POST 与对应任务 GET 使用相同 ability。

| operation | POST 路径 | 主要结果 |
|---|---|---|
| `creative.search` | `/api/v1/ad-intelligence/creative.search` | `result.creatives` |
| `advertiser.analyze` | `/api/v1/ad-intelligence/advertiser.analyze` | `result.analysis`、`result.advertisers` |
| `trend.report` | `/api/v1/ad-intelligence/trend.report` | `result.report`、`result.creatives` |

对应查询路径固定为 `/api/v1/ad-intelligence/{operation}/tasks/{task_id}`。

## 共同地区规则

必须且只能二选一：

- 指定正整数 `location_code`；或
- 明确发送 `"all_regions": true`。

不能同时提供，也不能同时省略。`language_code` 在全部三个 operation 中都被禁止。

## creative.search

`query` 必须是域名，最多 253 字符；不接受 URL、IP 或不合法域名。可选参数：

| 字段 | 规则 |
|---|---|
| `depth` | 整数 1–120，默认 40 |
| `platform` | `all`、`google_play`、`google_maps`、`google_search`、`google_shopping`、`youtube` |
| `format` | `all`、`text`、`image`、`video` |

素材可含 `advertiser`、`creative_text`、`format`、`first_seen_at`、`last_seen_at`、
`regions`、`source_url`。深度只是请求范围，不保证返回相同数量；素材搜索按请求批次计费，
具体金额仍只以响应头为准。

## advertiser.analyze

`query` 为必填广告主关键词，最多 700 字符。除地区二选一外，禁止发送 `depth`、
`platform`、`format`、`language_code`。`result.analysis` 可含 `advertiser_count`、
`approx_ads_count`；`result.advertisers[]` 可含广告主名称、地区和 `source_url`。不要仅凭同名
结果断言法律实体身份。

## trend.report

输入规则与 `creative.search` 相同：域名 `query`、地区二选一，以及可选的 `depth`、
`platform`、`format`。不要传前序任务 ID 或客户端计算结果。`result.report` 可含
`requested_depth`、`creative_count`、`first_seen_at`、`last_seen_at`、`formats`、
`advertisers`、`regions`、`generated_at`；底层证据在 `result.creatives`。
