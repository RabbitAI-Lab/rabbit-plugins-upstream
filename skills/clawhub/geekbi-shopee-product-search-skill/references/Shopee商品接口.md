# Shopee 商品接口

## 商品搜索

运行 `scripts/shopee_goods_search.py`，查询条件以重复 `--param 名称=值` 传入。

| 条件 | 含义 |
| --- | --- |
| `siteId` | 站点 ID；指定市场时先用站点列表实时解析，未传时服务端默认 `1` |
| `keyword` | 匹配商品名、商品 ID 或店铺 ID |
| `catId` | 精确匹配商品类目 ID |
| `monthSoldMin/Max` | 月销量区间 |
| `monthSalesMin/Max` | 月销售额区间 |
| `totalSoldMin/Max` | 总销量区间 |
| `totalSalesMin/Max` | 总销售额区间 |
| `priceMin/Max` | 最低价格区间 |
| `goodsScoreMin/Max` | 商品评分区间 |
| `reviewNumMin/Max` | 评论数区间 |
| `onSaleTimeMin/Max` | 上架时间区间，使用含时区的 ISO 8601 时间 |
| `mallOpenTimeMin/Max` | 店铺开店时间区间，使用含时区的 ISO 8601 时间 |
| `isCross` | 是否跨境商品，`true` 或 `false` |
| `sort` | `monthSold`、`monthSales`、`totalSold`、`totalSales`、`goodsScore`、`reviewNum`、`onSaleTime` 或 `mallOpenTime` |
| `order` | `asc` 或 `desc` |
| `page` / `size` | 从 1 开始分页；`size` 最大 200，且只能访问前 200 条 |

成功响应包含 `data.total`、`data.list` 和 `data.site`。每个商品可包含价格、销量/销售额、增长率、评分、评论数、点赞、库存、类目、SKU、店铺 ID 与更新时间；字段可能缺失。

## 商品详情

运行 `scripts/shopee_goods_info.py --goods-id <商品ID> --site-id <站点ID>`。

成功响应包含：

- `goods`：当前商品快照及类目；
- `history`：按时间正序排列的最近最多 31 条历史；
- `mall`：存在关联店铺数据时返回；
- `site`：本次查询站点。

接口未提供前台商品链接时，不自行拼接 URL。历史字段异常跳变必须单独标记，不用插值修补。
