# AliExpress 店铺接口

## 店铺详情

运行 `scripts/aliexpress_mall_info.py --mall-id <店铺ID> --site-id <站点ID>`。

成功响应包含 `site` 和 `mall`。店铺可能返回：店铺 ID、名称、Logo、评分、评论数、粉丝数、商品数、总/月/周/日销量与销售额、平均价格、类目、开店时间、`hostingMode`、各周期商品数及增长率。

字段是否返回取决于采集快照。`hostingMode` 缺少明确枚举说明时只原样展示。不得把缺失值写成 0，也不得把极鲸云指标称为 AliExpress 卖家中心官方结算或账号健康数据。

## 店铺商品

当前没有独立店铺商品接口。用 `scripts/aliexpress_goods_search.py` 将 `mallId` 作为 `keyword` 查询，并在结果中只保留 `mallId` 完全相同的商品。

关键词也会匹配商品名和商品 ID，因此不做精确过滤会混入无关结果。商品接口最多访问前 200 条。

当前不支持按店铺名称搜索。只有店铺名称时需补充店铺 ID 或代表商品 ID。
