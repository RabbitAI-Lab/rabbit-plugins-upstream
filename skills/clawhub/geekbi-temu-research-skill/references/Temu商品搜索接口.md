# Temu 商品搜索接口

## 目录

- [脚本调用](#脚本调用)
- [基础参数](#基础参数)
- [关键词与类目策略](#关键词与类目策略)
- [站点解析](#站点解析)
- [金额、竞争与库存口径](#金额与币种口径)
- [排序与筛选参数](#排序字段)
- [响应与失败处理](#成功响应)

## 脚本调用

单页 `size` 最大为 200。

通过以下命令调用：

```bash
python3 scripts/temu_goods_search.py \
  --param "keyword=连衣裙" \
  --param "siteId=48" \
  --param "size=20" \
  --param "sort=monthSold" \
  --param "order=desc"
```

按类目查询时重复传入一个或多个类目 ID：

```bash
python3 scripts/temu_goods_search.py \
  --param "catIds=一级或二级类目ID" \
  --param "siteId=48" \
  --param "size=20" \
  --param "sort=monthSold" \
  --param "order=desc"
```

服务端要求暂停查询时，按 [查询暂停与恢复流程](查询暂停与恢复流程.md) 提示用户；恢复条件满足后再次运行同一命令。

## 基础参数

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `keyword` | string | 无 | 商品名称或品牌关键词，最长 300 个字符 |
| `catIds` | integer，可重复 | 无 | Temu 类目 ID；多个 ID 使用多个同名参数，匹配其中任一类目 |
| `siteId` | integer | `48` | 极鲸云站点 ID；美国站直接使用默认值，其他国家或地区先用 `scripts/temu_site_list.py` 实时解析 |
| `page` | integer | `1` | 页码 |
| `size` | integer | `20` | 每页数量，最大 200 |
| `sort` | string | 无 | 排序字段，取值见下方“排序字段” |
| `order` | string | `desc` | `asc` 或 `desc` |

## 关键词与类目策略

- 一般只使用 `keyword` 或 `catIds` 之一，不要默认混合。两者同时使用时必须同时满足关键词和类目条件，返回结果通常会明显减少。
- 已有可信的一级或二级类目 ID 时优先使用 `catIds`，用于检索较宽的品类范围。
- 对三级及更深的细分类目，优先将用户意图转换为简洁的 `keyword`，避免类目过细导致样本太少。
- 用户明确要求在某类目中搜索特定商品时，可以同时传 `catIds` 和 `keyword`，但要在数据口径中说明这是交叉筛选。
- 类目 ID 必须来自用户输入或本 Skill 的“Temu类目搜索”能力。不得根据类目名称猜测 ID；没有可信 ID 时先查类目，或对更细的商品意图直接使用关键词。
- 多个 `catIds` 之间是“匹配任一类目”的关系。脚本使用重复参数，例如 `--param "catIds=123" --param "catIds=456"`。

关键词统一使用接口内置的模糊搜索。即使同时指定排序字段，关键词仍然作为结果筛选条件生效。

用户要求热销榜、日销排行、新品、蓝海、新店或大卖选品时，先按 [Temu 商品榜单查询预设](Temu商品榜单预设.md) 选择一个主预设，再使用 `asc` 或 `desc` 生成本接口参数。

## 站点解析

- 未指定站点或指定美国站时，直接使用默认站点 ID `48`，不额外查询站点列表。
- 用户指定其他国家或地区时，运行 `python3 scripts/temu_site_list.py --country "国家或地区名"`，将唯一精确匹配的站点 ID 传给商品搜索。
- 脚本实时匹配服务端返回的中文名或英文名，不使用本地静态站点表，不按语言、币种或相似名称猜测。
- 无匹配时请用户确认国家或地区名；多个匹配时列出中文站点名请用户澄清，不自行选择。

## 金额与币种口径

- `supplyPrice`、`minSupplyPrice`、`medianSupplyPrice`、`maxSupplyPrice` 等供货价字段，以及供货价筛选区间，单位固定为人民币（CNY）。
- `minPrice`、`maxPrice` 等商品价格字段，以及商品价格筛选区间，使用当前查询站点的币种；美国站使用美元，其他站点使用实时站点列表返回的币种。
- 面向用户展示任何价格时都明确标注币种，不要把供货价误写成站点币种，也不要把商品价格默认写成人民币。
- 计算价差、毛利或利润前，先将商品价格和供货价换算为同一币种，并说明采用的汇率及日期；没有可靠汇率时只分别展示两种价格，不直接计算利润。

## 同款数（跟卖数）评估口径

- 同款数（跟卖数）表示销售同一款商品的同行数量。数值越大，同行越多、同质化竞争越强，通常核价通过概率也越低。
- 默认按以下区间评估：不超过 10 为优选区间，竞争相对较低；11 至 20 为中等竞争；超过 20 为高竞争，且数值继续增大时竞争压力通常进一步上升。
- 对非工厂型卖家，优先选择同款数不超过 10 的商品；超过 20 的候选默认降级或剔除，除非存在明确的价格、渠道、产品差异化或运营优势。
- 工厂型卖家可以凭成本、产能、交付或定制能力承受更高的同款竞争，但不能仅凭工厂身份判定值得进入，仍需验证利润空间和核价可行性。
- 将同款数作为重要竞争指标，但不要单独据此下结论；同时结合销量及增长、供货价、商品价格、评价、上架时间和卖家自身能力综合判断。
- 搜索低竞争或蓝海商品时，默认将同款数上限设为 10；样本不足时最多放宽至 20，并明确说明竞争标准已放宽。除非有其他强证据，不要把超过 20 的商品称为低竞争或蓝海机会。

## 库存口径

- 库存字段为 `quantity`。返回值大于 `0` 时，将其作为当前采集到的库存快照，不将快照等同于长期可售库存。
- 库存返回 `0` 时存在两种可能：真实零库存，或当前没有统计到库存。默认按“库存情况未知”处理，不直接写成“库存为 0”“缺货”或“已售罄”。
- 面向用户展示该值时写为“库存：暂未统计到（接口返回 0，需进一步核实）”；不要仅展示数字 `0`。
- 计算平均库存、库存总量、库存覆盖天数或缺货比例时，将库存为 `0` 的商品作为缺失样本，不纳入数值计算，并披露排除数量。
- 使用库存区间筛选低库存商品时设置大于 `0` 的下限，避免把未统计到库存的商品混入低库存样本。不能仅凭库存上限筛选结果判断断货。

## 排序字段

| 维度 | `sort` 可选值 |
| --- | --- |
| 销量 | `sold`、`daySold`、`weekSold`、`monthSold`、`mallSold` |
| 销量增长率 | `daySoldRate`、`weekSoldRate`、`monthSoldRate` |
| 销售额 | `sales`、`daySales`、`weekSales`、`monthSales` |
| 销售额增长率 | `daySalesRate`、`weekSalesRate`、`monthSalesRate` |
| 价格 | `minPrice`、`maxPrice`、`supplyPrice`、`minSupplyPrice`、`medianSupplyPrice`、`maxSupplyPrice` |
| 商品指标 | `quantity`、`goodsScore`、`reviewNum`、`similarNum` |
| 时间 | `onSaleTime`、`mallOpenTime` |

价格排序使用 `minPrice`。未指定 `sort` 时，接口不强制业务排序；需要可比较的调研结果时应同时明确 `sort` 和 `order`。

## 筛选参数

所有区间参数均可只传最小值或最大值。

| 维度 | 最小值参数 | 最大值参数 |
| --- | --- | --- |
| 总销量 | `soldMin` | `soldMax` |
| 日销量 | `daySoldMin` | `daySoldMax` |
| 周销量 | `weekSoldMin` | `weekSoldMax` |
| 月销量 | `monthSoldMin` | `monthSoldMax` |
| 日销量增长率 | `daySoldRateMin` | `daySoldRateMax` |
| 周销量增长率 | `weekSoldRateMin` | `weekSoldRateMax` |
| 月销量增长率 | `monthSoldRateMin` | `monthSoldRateMax` |
| 总销售额 | `salesMin` | `salesMax` |
| 日销售额 | `daySalesMin` | `daySalesMax` |
| 周销售额 | `weekSalesMin` | `weekSalesMax` |
| 月销售额 | `monthSalesMin` | `monthSalesMax` |
| 日销售额增长率 | `daySalesRateMin` | `daySalesRateMax` |
| 周销售额增长率 | `weekSalesRateMin` | `weekSalesRateMax` |
| 月销售额增长率 | `monthSalesRateMin` | `monthSalesRateMax` |
| 库存 | `quantityMin` | `quantityMax` |
| 店铺销量 | `mallSoldMin` | `mallSoldMax` |
| 同款数（跟卖数） | `similarNumMin` | `similarNumMax` |
| 价格 | `priceMin` | `priceMax` |
| 供货价 | `supplyPriceMin` | `supplyPriceMax` |
| 商品评分 | `goodsScoreMin` | `goodsScoreMax` |
| 评论数 | `reviewNumMin` | `reviewNumMax` |
| 上架时间 | `onSaleTimeMin` | `onSaleTimeMax` |
| 开店时间 | `mallOpenTimeMin` | `mallOpenTimeMax` |

时间参数使用 ISO 8601 日期时间。托管模式使用：

- `hostingMode`：托管模式，`1` 全托管、`2` 半托管。

## 成功响应

```json
{
  "code": 0,
  "data": {
    "total": 100,
    "list": []
  }
}
```

- `data.total` 是当前条件下的命中总数。
- `data.list` 是当前页商品列表，核心字段包括商品 ID、店铺 ID、标题、图片、类目、价格、供货价、销量、销售额、增长率、评分、评论数、库存、状态、托管模式和时间字段。
- 服务端会为每个商品返回 `linkUrl`，指向该商品在极鲸云的 Temu 商品详情页。
- 对用户展示商品时，必须将每个商品标题写成 `[商品标题](<linkUrl>)`。该要求覆盖列表、表格、排名、候选清单和正文，不因用户未主动要求链接、要求简洁回答或表格空间有限而省略；不得根据商品 ID 或站点 ID 自行拼接、猜测或补全链接。
- 评论分析使用 `reviewNum`。
- 商品标识包括 `isAd`、`isPresale`、`isCustom`；同款数（跟卖数）使用 `similarNum`。
- 库存使用 `quantity`；值为 `0` 时遵守上方“库存口径”，按暂未统计到处理并向用户备注。
- 所有商品价格和供货价的展示与分析均遵守上方“金额与币种口径”。

## 校验与失败处理

- 请求前记录站点、页码、页大小、排序和筛选条件。
- 服务端要求暂停查询时不是普通查询失败。按 [查询暂停与恢复流程](查询暂停与恢复流程.md) 展示提示，有跳转地址时再展示可点击链接；恢复条件满足后原样重跑命令。
- `code != 0`、HTTP 非 2xx、响应不是 JSON 或缺少 `data` 时，将本次查询视为失败。服务端提供一级 `msg` 时，脚本将其写入错误输出的 `msg`；面向用户只提示该中文文案，不展示整段错误 JSON。
- 使用页码分页。请求多页时逐页累计，明确已读取的页数和条数；没有完成全部分页时不得声称结果为全量。
