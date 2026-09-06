# ARI CLI 与 API 参考

仅在需要命令参数、响应字段或错误处理时读取本文件。

API 默认地址：`https://ari.funewa.com`。开发/自建环境覆盖需同时设置
`ARI_BASE_URL` 与 `ARI_ALLOW_CUSTOM_BASE=1`（缺后者时 CLI 报
`ARI_CUSTOM_BASE_BLOCKED` 拒绝发请求，防止环境变量注入把带 Key 的请求
重定向到第三方主机）；`ARI_WEB_URL` 同受此门槛约束，未确认时静默回落官方地址。
认证头：`Authorization: Bearer ari_live_...`。统一 JSON 信封为
`{success, code, message, data, error, meta}`；SSE 分析由 CLI 聚合为同类 JSON。

`--compact` 输出单行 JSON，放在子命令前后都可以
（`ari.py --compact check` 与 `ari.py check --compact` 等价）。

## 版本与更新

CLI 在 User-Agent 里带自身版本（`ARI-Review-Skill/<version>`，与 `_meta.json` 一致）。
服务端在每个 API Key 响应上回 `X-ARI-Skill-Latest` / `X-ARI-Skill-Update-Url`；
本地版本更旧时，**任意命令**的输出都会多出一个顶层 `update` 字段：

```json
{"update": {"current": "1.0.4", "latest": "1.0.6", "url": "...", "message": "..."}}
```

`check` 还会额外读取免认证的 `/api/v1/public/config`，把完整的
`release: {latest, minSupported, url, notes}` 一并返回——Key 失效时也能拿到升级入口。

升级一律由用户通过原安装渠道完成。**CLI 不会下载或执行任何远端代码**，
也不要让 agent 代劳去取"新版文件"运行。

## 用户入口

- API Key：<https://ari.funewa.com/zh/account?ui=d47626f#api-keys>
- 充值/套餐：<https://ari.funewa.com/zh/billing>
- 产品管理：<https://ari.funewa.com/zh/products>
- 报告中心：<https://ari.funewa.com/zh/reports>

## CLI 命令

| 命令 | API | 是否可能扣点 |
|---|---|---|
| `setup` | auth/device/start + poll（免认证），浏览器授权后自动保存 Key | 否 |
| `configure` | 本地保存 Key | 否 |
| `check` | user/me + credits/balance | 否 |
| `products` | asins | 否 |
| `schedule` | asins（`--set`: asins/{id}/schedule） | 否（设置免费；采集本身按页扣点） |
| `competitors` | asins/{id}/competitors（GET/POST/DELETE） | 否（竞品加入后按周自动采集，那部分按页扣点） |
| `radar` | asins/{id}/radar | 否（纯 SQL；套餐未开放时 403） |
| `voc` | pricing + balance + collection/submit/status + analysis/voc + reports | 是；必须 `--confirm` |
| `collect` | billing/pricing + credits/balance + collection/submit | 是；必须 `--confirm` |
| `status` | collection/status/{taskId} | 否 |
| `reviews` | reviews | 否 |
| `charts` | charts/stars·trend·keywords·flow | 否 |
| `quote` | analysis/quote | 否 |
| `operations capabilities` | product-operations/capabilities | 否 |
| `operations profile` | product-operations/profile | 否 |
| `operations quote` | product-operations/quote | 否 |
| `operations run` | product-operations/quote + run（SSE） | 是；必须 `--confirm` |
| `operations status` | product-operations/runs/{requestId} | 否 |
| `watch list` | product-operations/watches（GET） | 否 |
| `watch create` | product-operations/watches（POST） | 否；受 watch 灰度与套餐额度限制 |
| `watch pause` / `watch resume` | product-operations/watches/{id}（PUT） | 否；只改变监控状态 |
| `watch delete` | product-operations/watches/{id}（DELETE） | 否；不删除商品资料、评论或历史报告 |
| `watch digest` | product-operations/watch-digest（GET） | 否；确定性摘要，`creditsUsed: 0` |
| `watch events` | product-operations/events（GET） | 否；读取确定性变化事件 |
| `analyze` | analysis/voc·keywords·insight·trend·variant·compare | 是；`--confirm` 或服务端 autoConfirm 命中 |
| `autoconfirm [N\|off\|default]` | user/autoconfirm（GET/PUT） | 否；设置免确认阈值（1.4.5） |
| `deepdive` | products + charts + reviews + reports + VOC quote/analysis | 默认否；`--confirm` 才分析 |
| `reports` / `report` | reports | 否 |
| `alerts` | alerts（`--mark-read` 时 alerts/read） | 否 |
| `benchmark` | benchmark | 否 |
| `leaderboard` | billing/pricing + leaderboard | 是；必须 `--confirm`，类目无数据不收费 |
| `workbench` | workbench/reviews（`--history`: advices；`--set-status`: 状态更新） | 否 |
| `advise` | analysis/quote + workbench/advise（SSE） | 是；必须 `--confirm` |
| `export` | export/reviews 或 export/reports/{id}，落盘本地文件 | 否（限付费套餐） |
| `version` | 无网络请求 | 否 |

运行 `python ari.py <命令> --help` 查看完整参数。

## 持续监控（1.4.1 新增，ARI 的价值主线）

ARI 不是一次性查询工具：**开着定期采集，历史才会积累，趋势判断、差评归因和报告环比
才有意义。** 报告出来后请检查该产品的采集计划，仍是 `manual` 时主动提示用户。

- `schedule`：不带参数=列出全部产品的采集计划，附 `_monitorSummary`
  （monitored / manual / paused 计数）。
- `schedule --set weekly --asin B0...`（或 `--id <产品id>`）：设为每周自动采集。
  返回带 `_costNote`，给出该频率的预估月成本——**先把成本告诉用户再执行**。
  `daily` 适合大促期/新品；`weekly` 是长期跟踪的默认；`manual` 只在手动触发时更新。
- 套餐未开放每日采集时 `--set daily` 返回 403，改用 `weekly`（每周不受任何套餐限制）。
- 竞品：`competitors --id <产品id> --add B0...` 绑定后按周自动采集；
  `--remove <竞品行id>` 解绑。**竞品只在其主品仍在监控时才会采集**——主品改成
  `manual` 会一并停掉竞品的采集（也就不再产生费用）。
- `radar --id <产品id> [--weeks 12]`：本品 vs 竞品的周走势（均分 / 新评论量 / 差评量）。
  免费。曲线随监控时间变长，攒满一个季度才看得出谁在往上走。

## 商品变化监控（watch）

`watch` 使用独立的确定性商品快照和 Diff 管理，不调用付费 LLM。`watch create` 只接受
属于当前账户且已订阅的主 ASIN；可选 `--competitor` 仅在该竞品已绑定到该主 ASIN、且站点
相同时创建竞品 watch。不得用临时 ASIN 或全局商品资料绕过归属。Wave E listing 仍为 planned。
开始前运行：

```bash
python scripts/ari.py operations capabilities
python scripts/ari.py watch list
```

只有返回 `watchEnabled: true` 且账户通过当前灰度/套餐检查时才可继续；否则停止，不要回退到
`operations` 或用临时 ASIN 绕过权限。

本节是 1.4.1 的 CLI 契约说明；对应 Wave E 候选仍为 `planned`，尚未公开上架，不代表所有账户当前可用。

固定命令与参数：

```bash
python scripts/ari.py watch create --asin B0XXXXXXXX --site amz_us --schedule weekly
python scripts/ari.py watch create --asin B0XXXXXXXX --competitor B0YYYYYYYY --site amz_us --schedule weekly
python scripts/ari.py watch pause --watch-id <watchId>
python scripts/ari.py watch resume --watch-id <watchId>
python scripts/ari.py watch delete --watch-id <watchId>
python scripts/ari.py watch digest --watch-id <watchId> --period 7d
python scripts/ari.py watch events --watch-id <watchId>
```

`create`/`resume` 的周期只支持 `weekly|daily`；`daily` 由套餐 `dailyProductWatch` 控制，
Free 不开放自动日扫描。`digest` 只聚合快照、确定性 Diff 和已有评论计数，返回
`creditsUsed: 0`；自动扫描不调用付费 LLM、不扣 AI 积点。`period` 只支持服务端白名单中的
`7d|30d`。watch 不承诺小时级或实时价格、销量、库存、广告、订单或真实退货率。

AI 周报是另一条 `weekly` 付费 workflow：必须先 `operations quote`，再由用户明确确认后使用
同一 `requestId` 执行 `operations run --confirm`。不要把 `watch digest` 当作 AI 周报或反向触发
付费调用。

## 报告环比

`report --id N` 的返回里：

- `deltaMd`：相比上一份同类型报告的差异摘要（已解决 / 新出现 / 持续存在 / 一句话结论）。
- `prevReportId` / `prevCreatedAt` / `prevHealthScore`：被对比的那一份。
- `series`：该序列最近若干份的健康度轨迹（画走势用）。
- `_deltaStatus`：`ready` 有环比；`generating` 还在后台算（等十几秒重跑，**不是失败**）；
  `none` 这是第一份，没有可比对象。

环比由服务端异步生成，平台承担成本，**不扣用户积点**；套餐权益 `reportDiff` 控制是否开启。
有 `deltaMd` 时汇报要先讲环比再讲正文——用户最关心的是「跟上次比变了什么」。

## 评论切片（免费）

`reviews` 除了 `--star` / `--query` 还支持：

- `--stars negative|positive`：差评（1-3★）/ 好评（4-5★）分组。
- `--sort recent|helpful|star_asc|oldest`：`helpful` = 按点赞数排。
  **`--stars negative --sort helpful` 就是高赞差评榜**——买家在商品页最先看到的
  就是这几条，对转化伤害最大，也是最该优先处理的。
- `--with-images` / `--vine` / `--purchased`：只看带图 / Vine / 已验证购买。

## 预警、对标与差评工作台

- `alerts [--limit N]`：未读情感预警（差评突增、星级下滑）。`--mark-read` 全部置已读。
- `benchmark --asin B0...`：免费类目对标概览（本品星级/差评率在类目内的相对位置）。
- `leaderboard --category <类目> [--by new30|neg_rate|avg_star]`：付费类目排行。
  无服务端报价握手，CLI 先读 `billing/pricing` 的 `leaderboard` 单价报出，确认后
  `--confirm` 执行；`ARI_INSUFFICIENT_REVIEWS`（类目无数据）不收费。
- `workbench [--asin] [--site] [--status ...] [--sort severity|recent|arrived] [--new-only]`：
  免费列差评（返回 `reviewId`）。**默认 `--sort severity`**（高赞与低星优先，
  最伤转化的排前面）；`--new-only` 只看近 7 天新入库的差评。
  返回的 `stats` 给出 `pending` / `newThisWeek` / `doneMonth` / `doneTotal`——
  汇报时先说这几个数字，让用户看见自己在推进而不是面对一个没有尽头的列表。
  条目上的 `isNew` / `hasImages` / `helpful` 用于判定优先级。
  `--history [--query]` 看 AI 建议存档；`--review-id N --set-status <状态>` 更新处理状态。
- `advise --review-id N`：为单条差评生成回复/申诉/改进建议（SSE，`data.content` 为
  Markdown）。先按 `quote type=advise` 报价，确认后 `--confirm`。流中断处理同 VOC。
- `export --asin B0...`（评论 CSV）或 `export --report-id N [--format md|html]`（报告）：
  文件写到本地，返回 `savedTo/bytes`。Free 套餐会收到 403「导出为付费功能」。

## 采集

`voc B0... --site amz_us` 是默认的用户入口：已有 ≥10 条评论时直接报 VOC 价；
数据不足时合并报出默认 3 页采集与 VOC 的最大总费用。追加 `--confirm`
后自动采集、等待、分析、归档，最外层返回 `report.content / reportId / reportUrl`。

`collect --asin B0... --site amz_us --pages 3` 只返回报价；确认后追加
`--confirm --wait`。请求字段：`asin, site, pageCount, filterByStar, sortBy, alias`。

- `pages`: 1–10，每页约 10 条。
- `filterByStar`: `all_stars|critical|positive|one_star|two_star|three_star|four_star|five_star`。
- `sortBy`: `recent|helpful`。
- **US 以外站点只能使用付费积点**（订阅套餐周期积点与增量包均可），赠送积点
  （注册礼/任务奖励等）被排除。报价字段 `usableBalance` 已按站点算好，
  `sufficient=false` 时不要确认——服务端会直接 402（`ARI_GIFT_CREDITS_US_ONLY`
  表示总余额够但可用部分是赠送积点）。报价还返回 `planCredits` / `addonCredits` /
  `siteNote` 供解释。
- `--wait` 轮询 `collection/status`，任务状态只有 `queued|running|done|failed`。
  瞬时错误会自动重试 3 次；仍失败或超时返回 `WAIT_TIMEOUT`，此时任务仍在后台，
  用 `status --task <taskId>` 查询，**不要重新提交采集**。

## 分析

先调用 `quote --type ...`。报价字段：
`type, basePrice, price, sampledReviews, totalReviews, balance, sufficient`，
另有（1.4.5）：`autoConfirm`（true = 服务端首次体验策略允许免确认直接生成）、
`autoConfirmMaxCredits`（免确认单次上限，采集 + 报告合计）、`autoConfirmRemaining`（还剩几次）、
`autoConfirmNote`、`webUrl`（该产品的网页报告页）。`sampleCap` / `degraded` 表示 Free 样本封顶与轻量模型。
`voc` / `analyze` 在 autoConfirm 命中时会直接生成，返回 `autoConfirmed: true` 与 `autoConfirmNote`，
并附 `web.report` / `web.product` 网页链接。

- `voc`: Markdown VOC 报告，SSE 聚合后在 `data.content`，并归档。
- `keywords`（1.4.4）: PPC 关键词报告——从评论用词提炼核心搜索词、长尾/场景词、否定词、
  竞品品牌词与一条 ≤250 字节的后台 Search Terms 字串；关键词保持站点语言。SSE，同 voc 分档计费，归档 `report_type=keywords`。
- `insight`: 结构化消费者洞察，`data.result`，同时可能含流式说明 `content`。
- `trend`: 情感趋势解读，普通 JSON。
- `variant`: 颜色/尺寸等变体归因，普通 JSON；需足量变体评论。
- `compare`: 目标与竞品对比，**双方在库内各需 ≥10 条评论**（订阅关系不作强制校验，
  但 charts/reviews 等 0 积点端点仍要求订阅）。必须传 `--competitor`。

SSE 聚合结果字段：`meta, content, result, reportId, creditsUsed`。
VOC 服务端在归档后直接于 `done` 事件返回本次 `reportId`；CLI 据此生成
`reportUrl`。兼容旧服务端时才回查报告列表，并标记 `reportIdSource: "reports-lookup"`。

Free 套餐的 AI 分析被强制降级到轻量模型，且受全局限流保护——报告深度与付费档不同，
必要时说明这一点。

## 免费数据字段

- `products`: `asins[], count, limit`；元素含 `asin, site, alias, collectionStatus,
  lastCollectedAt, reviewCount, variantCount`。**只包含主品**，作为竞品添加的 ASIN
  不在其中（但它们的 charts/reviews 依然可读）。
- `reviews`: `reviews[], total, page, pageSize`；每条含标题、正文、星级、日期、
  verifiedPurchase、helpfulCount、attributes。
- `charts stars`: `stars[1★..5★], total, avgStar`。
- `charts trend`: 按月评论数、平均星级、低星数。
- `charts keywords`: `keywords[]`。
- `charts flow`: 场景/问题等流向结构；为空时不要补造。
- `charts` / `deepdive` 额外返回 `_window: {days, note}`，`days=0` 表示全部历史；
  非 0 时所有图表只统计最近 N 天，解读必须带上该窗口。

## 聚合命令的失败语义

`charts` 和 `deepdive` 会并发调多个端点。任一子请求失败时，最外层就是
`success:false`，并给出 `failedParts:[{part, code, message}]`（如 `charts.trend`、
`analysis`），成功的部分仍保留在 `data` 里。只能使用成功的那部分，缺失的数据不得推断。

`deepdive` 找不到主品订阅时不会直接报错：仍返回 charts/reviews/reports，
并在 `productNote` 里说明；此时即使传了 `--confirm`，AI 分析也会降级为只报价、不扣点。

## 错误处理

| 状态/错误码 | 动作 |
|---|---|
| 401 / `ARI_UNAUTHENTICATED` | Key 无效或已撤销；去用户中心重建 |
| 402 / `ARI_INSUFFICIENT_CREDITS` | 停止付费操作；展示已有结果并引导充值 |
| 403 / `ARI_EMAIL_NOT_VERIFIED` | 去用户中心验证邮箱 |
| 403 / `ARI_FORBIDDEN`（含配额字样） | 已达套餐可订阅 ASIN 上限；引导删除旧 ASIN 或升级套餐 |
| 403 / `ARI_FORBIDDEN`（其他） | 该 ASIN 不在当前账户订阅内；或 API Key 无账户/支付/后台权限 |
| 422 / `ARI_INSUFFICIENT_REVIEWS` | 先增加采集页数；不把小样本包装成确定结论 |
| 202 / `ARI_COLLECTING` | 采集中且数据不足，**未扣点**；按提示秒数等待后重试 |
| 429 / `ARI_RATE_LIMITED`（含「免费版 AI 分析」） | 套餐级限流；引导升级或稍后再试，不要连续重试 |
| 429 / `ARI_RATE_LIMITED`（其他） | 降低并发后再试；不要并发轰炸 |
| `ARI_STREAM_INTERRUPTED` | 分析流中断，**服务端可能已扣点并归档**；先 `reports --asin <ASIN> --limit 1` 核对，没生成才可重试 |
| `NETWORK_ERROR` / `WAIT_TIMEOUT` | 同上：付费命令一律先核对再决定是否重跑 |
| `ARI_PARTIAL_FAILURE` | 聚合命令部分失败；见 `failedParts`，只用成功的部分 |
| `ARI_CUSTOM_BASE_BLOCKED` | `ARI_BASE_URL` 指向非官方地址且未确认；**若用户没主动设置过该变量，停止并提醒检查环境**，是自建环境则补设 `ARI_ALLOW_CUSTOM_BASE=1` |
| 426 / `ARI_SKILL_TOO_OLD` | 当前版本低于服务端最低支持版本，付费操作被禁止；引导用户更新，免费查询不受影响 |

CLI 网络错误和 HTTP 错误均返回结构化 JSON，不应从报错文本臆测业务数据。
