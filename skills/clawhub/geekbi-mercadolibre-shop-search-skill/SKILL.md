---
name: geekbi-mercadolibre-shop-search-skill
description: 使用极鲸云查询和分析 Mercado Libre（美客多）真实店铺数据，支持按站点、店铺名称或 ID、商品数、粉丝数、累计销量、信誉等级和开店时间筛选排序。用户提到美客多店铺、卖家、竞店、头部店铺、新店、信誉、Power Seller 或店铺规模时使用。只依据极鲸云返回数据，不代表卖家中心完整经营报表。
---

# 极鲸云 Mercado Libre 店铺搜索

## 原则与流程

- 指定市场时先运行 `scripts/mercadolibre_site_list.py`；未指定时默认 `siteId=1`（墨西哥）。
- 店铺搜索运行 `scripts/mercadolibre_mall_search.py`，详情运行 `scripts/mercadolibre_mall_info.py`。
- 按 [店铺接口](references/MercadoLibre店铺接口.md) 传最少必要条件，按 [店铺研究](references/MercadoLibre店铺研究.md) 比较规模、销量、粉丝、信誉和生命周期。
- `mallOpenTime` 是依据已收录商品最早上架时间推算，不等同于平台官方注册时间。
- `mallStar`、`reputationLevelText` 和 `powerSellerStatusText` 是采集快照，不能还原全部信誉考核明细。
- 最多访问前 200 条，说明站点、条件、排序、页码、样本量和更新时间。
- 服务端要求暂停时按 [查询暂停与恢复流程](references/查询暂停与恢复流程.md) 处理。

## 边界

- 不提供利润、广告、流量、转化率、退货率、投诉明细或卖家后台操作。
- 店铺销量和商品量仅按极鲸云当前数据口径解释；热销店铺不等于适合跟卖。
- 涉及信誉、跨境或履约判断时读取 [运营与政策口径](references/MercadoLibre运营与政策口径.md)。

输出默认包含：结论、查询口径、店铺证据、风险和下一步验证。
