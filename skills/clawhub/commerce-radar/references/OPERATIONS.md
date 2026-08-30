# Operations 契约

所有创建接口都是异步操作，成功受理通常返回 HTTP `202`。每个 POST 与对应 GET 使用同一
ability。

| operation | POST 路径 | 用途 |
|---|---|---|
| `product.search` | `/api/v1/commerce-radar/product.search` | 搜索商品与价格证据 |
| `product.detail` | `/api/v1/commerce-radar/product.detail` | 查询一个商品详情 |
| `store.analyze` | `/api/v1/commerce-radar/store.analyze` | 汇总一个公开店铺的商品与价格带 |
| `report.create` | `/api/v1/commerce-radar/report.create` | 生成关键词竞争报告 |

对应任务路径固定为
`/api/v1/commerce-radar/{operation}/tasks/{task_id}`。

## product.search

| 字段 | 规则 |
|---|---|
| `query` | 必填字符串，最多 700 字符 |
| `location_code` | 可选正整数 |
| `language_code` | 可选字符串，最多 12 字符 |
| `limit` | 可选整数，1–40；默认 20 |

结果重点读取 `result.products[]`。单项可含 `title`、`price`、`currency`、`rating`、
`reviews`、`domain`、`source_url`、`image_url`、`product_id`、`data_docid`、`gid`。

## product.detail

至少提供 `product_id`、`product_url`、`data_docid`、`gid` 之一。三个标识字符串最多 255
字符且只能包含 `A-Za-z0-9_-`。`product_url` 必须是公开 HTTP(S) URL，路径为
`/shopping/product/{product_id}`，其中 product_id 是 5 至 255 位数字；URL 最多 2048 字符。
一般商品页 URL 不能替代标识，平台只把该路径中的数字派生为 `product_id`。可附正整数
`location_code` 和最多 12 字符的 `language_code`。结果读取 `result.product`，详情可含
`title`、`specifications` 与 `sellers`；卖家价格和币种是观察值，不代表持续有效报价。

## store.analyze

| 字段 | 规则 |
|---|---|
| `store_url` | 必填公开 HTTP(S) URL，最多 220 字符 |
| `query` | 必填字符串，最多 400 字符 |
| `location_code` | 可选正整数 |
| `language_code` | 可选字符串，最多 12 字符 |
| `limit` | 可选整数，1–40；默认 20 |

结果读取 `result.store` 与 `result.products`。店铺摘要可含 `sample_size`、平均/最低/最高
价格和币种分布；样本不等于完整店铺库存。

## report.create

`queries` 必填，1–10 个字符串，每项最多 40 字符。`store_urls` 可选且最多 1 个公开
HTTP(S) URL，每项最多 220 字符。可附正整数 `location_code` 和最多 12 字符的
`language_code`。结果读取 `result.report` 与 `result.products`；报告可含
`target_count`、`product_count`、`top_domains`、`generated_at`。

不要发送 `provider`、`market`、`category`、任意上游 payload 或结果 ID；它们不在平台
请求契约中。
