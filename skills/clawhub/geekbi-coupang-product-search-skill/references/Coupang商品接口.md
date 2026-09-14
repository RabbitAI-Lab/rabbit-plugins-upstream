# Coupang 商品接口

## 商品搜索

运行 `scripts/coupang_goods_search.py`，查询条件以重复 `--param 名称=值` 传入。

| 条件 | 含义 |
| --- | --- |
| `siteId` | 固定 `1`，韩国站 |
| `keyword` | 匹配商品名、`productId`、品牌或制造商 |
| `categoryId` | 精确匹配采集到的商品类目 ID |
| `categoryPath` | 精确匹配完整类目路径 |
| `categoryPathPrefix` | 按已核验类目名称路径前缀匹配 |
| `leafCategoryCode` | 精确匹配叶子展示类目编码 |
| `rootCategoryCode` | 精确匹配根展示类目编码 |
| `displayDeliveryMethod` | `NORMAL`、`ROCKET`、`ROCKET_MERCHANT`、`COUPANG_GLOBAL`、`ROCKET_FRESH` |
| `priceMin/Max` | 商品规格价格区间有交集；单位 KRW |
| `ratingMin/Max` | 商品评分区间，0–5 |
| `ratingCountMin/Max` | 评分数量区间 |
| `pvLast28DayMin/Max` | 极鲸云收录的近 28 日浏览量区间 |
| `salesLast28dMin/Max` | 极鲸云收录的近 28 日销量区间 |
| `onSaleTimeMin/Max` | 估算上架时间，含时区的 ISO 8601 |
| `createTimeMin/Max` | 极鲸云首次建档时间，含时区的 ISO 8601 |
| `updateTimeMin/Max` | 极鲸云更新时间，含时区的 ISO 8601 |
| `sort` | `updateTime`、`minItemPrice`、`maxItemPrice`、`itemCount`、`sellerCount`、`rating`、`ratingCount`、`pvLast28Day`、`salesLast28d`、`createTime` |
| `order` | `asc` 或 `desc` |
| `page` / `size` | 从 1 开始；`size` 最大 100，只能访问前 200 条 |

响应包含 `data.total`、`data.list` 和韩国站 `data.site`。商品字段可包含商品 ID、名称、品牌、制造商、图片源路径、类目、规格价格区间、评分、评分数、近 28 日浏览量和销量、规格数、卖家数、配送展示标记及时间。

`estimatedOnSaleTime` 由最早评论时间、主图修改时间中的较早者再提前 10 天得出，只能作为估算筛选口径。

## 商品详情

运行 `scripts/coupang_goods_info.py --product-id <商品ID>`。可加 `--item-id <规格ID>`。

- 未传 `itemId`：返回当前商品、最多 100 个规格和最多近 31 条商品历史。
- 传入 `itemId`：只返回该规格，并增加最多近 31 条规格历史。
- 规格字段可包含顾客价、Buy Box 获胜价、竞争卖家数、属性和 vendor item ID；不返回卖家明细。
- 历史按时间正序返回，不做插值；空数组表示当前未取得历史。
