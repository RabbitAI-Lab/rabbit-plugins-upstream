# ARI CLI 与 API 参考

仅在需要命令参数、响应字段或错误处理时读取本文件。

API 默认地址：`https://ari.funewa.com`（开发环境可用 `ARI_BASE_URL` 覆盖）。
认证头：`Authorization: Bearer ari_live_...`。统一 JSON 信封为
`{success, code, message, data, error, meta}`；SSE 分析由 CLI 聚合为同类 JSON。

## 用户入口

- API Key：<https://ari.funewa.com/zh/account?ui=d47626f#api-keys>
- 充值/套餐：<https://ari.funewa.com/zh/billing>
- 产品管理：<https://ari.funewa.com/zh/products>
- 报告中心：<https://ari.funewa.com/zh/reports>

## CLI 命令

| 命令 | API | 是否可能扣点 |
|---|---|---|
| `configure` | 本地保存 Key | 否 |
| `check` | user/me + credits/balance | 否 |
| `products` | asins | 否 |
| `collect` | billing/pricing + collection/submit | 是；必须 `--confirm` |
| `status` | collection/status/{taskId} | 否 |
| `reviews` | reviews | 否 |
| `charts` | charts/stars·trend·keywords·flow | 否 |
| `quote` | analysis/quote | 否 |
| `analyze` | analysis/voc·insight·trend·variant·compare | 是；必须 `--confirm` |
| `deepdive` | products + charts + reviews + reports + VOC quote/analysis | 默认否；`--confirm` 才分析 |
| `reports` / `report` | reports | 否 |

运行 `python ari.py <命令> --help` 查看完整参数。

## 采集

`collect --asin B0... --site amz_us --pages 3` 只返回报价；确认后追加
`--confirm --wait`。请求字段：`asin, site, pageCount, filterByStar, sortBy, alias`。

- `pages`: 1–10，每页约 10 条。
- `filterByStar`: `all_stars|critical|positive|one_star|two_star|three_star|four_star|five_star`。
- `sortBy`: `recent|helpful`。
- US 以外站点只能使用付费积点。

## 分析

先调用 `quote --type ...`。报价字段：
`type, basePrice, price, sampledReviews, totalReviews, balance, sufficient`。

- `voc`: Markdown VOC 报告，SSE 聚合后在 `data.content`，并归档。
- `insight`: 结构化消费者洞察，`data.result`，同时可能含流式说明 `content`。
- `trend`: 情感趋势解读，普通 JSON。
- `variant`: 颜色/尺寸等变体归因，普通 JSON；需足量变体评论。
- `compare`: 目标与竞品对比，双方均需已订阅且至少 10 条评论。

SSE 聚合结果字段：`meta, content, result, reportId, creditsUsed`。

## 免费数据字段

- `products`: `asins[], count, limit`；元素含 `asin, site, alias, collectionStatus,
  lastCollectedAt, reviewCount, variantCount`。
- `reviews`: `reviews[], total, page, pageSize`；每条含标题、正文、星级、日期、
  verifiedPurchase、helpfulCount、attributes。
- `charts stars`: `stars[1★..5★], total, avgStar`。
- `charts trend`: 按月评论数、平均星级、低星数。
- `charts keywords`: `keywords[]`。
- `charts flow`: 场景/问题等流向结构；为空时不要补造。

## 错误处理

| 状态/错误码 | 动作 |
|---|---|
| 401 / `ARI_UNAUTHENTICATED` | Key 无效或已撤销；去用户中心重建 |
| 402 / `ARI_INSUFFICIENT_CREDITS` | 停止付费操作；展示已有结果并引导充值 |
| 403 / `ARI_EMAIL_NOT_VERIFIED` | 去用户中心验证邮箱 |
| `ARI_INSUFFICIENT_REVIEWS` | 先增加采集页数；不把小样本包装成确定结论 |
| `ARI_FORBIDDEN` | 检查该 ASIN 是否属于当前账户；API Key 无账户/支付/后台权限 |
| 429 / `ARI_RATE_LIMITED` | 等待后再试；不要并发轰炸 |

CLI 网络错误和 HTTP 错误均返回结构化 JSON，不应从报错文本臆测业务数据。
