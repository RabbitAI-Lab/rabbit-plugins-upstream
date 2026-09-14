# Mercado Libre 商品接口

## 商品搜索

运行 `scripts/mercadolibre_goods_search.py`，查询条件以重复 `--param 名称=值` 传入。

| 条件 | 含义 |
| --- | --- |
| `siteId` | 站点 ID；默认 `1`（墨西哥），指定市场时先实时解析 |
| `keyword` | 匹配商品名、商品 ID、产品 ID 或店铺 ID |
| `catId` | 精确匹配已确认的类目 ID |
| `totalSoldMin/Max` | 累计销量区间 |
| `totalSalesMin/Max` | 累计销售额区间 |
| `priceMin/Max` | 当前价格区间 |
| `goodsScoreMin/Max` | 商品评分区间 |
| `reviewNumMin/Max` | 评论数区间 |
| `mallSoldMin/Max` | 关联店铺累计销量区间 |
| `onSaleTimeMin/Max` | 商品上架时间，含时区的 ISO 8601 |
| `mallOpenTimeMin/Max` | 推算店铺开店时间，含时区的 ISO 8601 |
| `shippedFrom` | 发货地文本 |
| `full` | `true/false`，FULL/Fully Managed 履约标记 |
| `crossBorder` | `true/false`，跨境标记 |
| `sort` | `updateTime`、`daySold`、`totalSold`、`totalSales`、`price`、`goodsScore`、`reviewNum`、`onSaleTime`、`mallOpenTime`、`mallSold` |
| `order` | `asc` 或 `desc` |
| `page` / `size` | 从 1 开始；`size` 最大 200，只能访问前 200 条 |

响应包含 `data.total`、`data.list` 和 `data.site`。商品字段可包含商品/产品/父产品 ID、店铺、价格、币种、日周月和累计销量、销售额、评分、评论数、库存、品牌、发货地、跨境/FULL 标记、类目路径和时间。

## 商品详情

运行 `scripts/mercadolibre_goods_info.py --goods-id <商品ID> --site-id <站点ID>`。

响应包含当前 `goods`、最多近 31 条按时间正序的 `history`、可用时的关联 `mall` 及 `site`。历史不做插值；字段为空时保持为空。
