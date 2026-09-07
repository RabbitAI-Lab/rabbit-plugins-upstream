# Mercado Libre 店铺接口

## 店铺搜索

运行 `scripts/mercadolibre_mall_search.py`，支持：

- `siteId`、`keyword`；
- `goodsNumMin/Max`、`followerNumMin/Max`、`mallSoldMin/Max`、`mallStarMin/Max`；
- `mallOpenTimeMin/Max`，使用含时区的 ISO 8601；
- `sort`：`updateTime`、`goodsNum`、`followerNum`、`mallSold`、`mallStar`、`mallOpenTime`；
- `order=asc|desc`、`page`、`size`，最多访问前 200 条。

返回字段可包含店铺 ID、名称、Logo、商品数、粉丝数、累计销量、信誉评分/等级、Power Seller 标签、卖家类型、推算开店时间和更新时间。

## 店铺详情

运行 `scripts/mercadolibre_mall_info.py --mall-id <店铺ID> --site-id <站点ID>`。响应包含 `mall` 和 `site`；不存在时不猜测或跨站点替代。
