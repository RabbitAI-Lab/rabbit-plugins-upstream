---
name: geekbi-mercadolibre-product-search-skill
description: 使用极鲸云查询和分析 Mercado Libre（美客多）真实商品数据，包括商品搜索、商品详情、价格、日周月及累计销量、销售额、评分、评论数、上架时间、店铺指标、跨境和 FULL 履约标记。用户提到美客多商品、Mercado Libre 选品、爆品、新品、价格带、销量榜、跨境商品或单品趋势时使用。只依据极鲸云返回数据，不提供图搜、搜索词趋势、利润或卖家中心操作。
---

# 极鲸云 Mercado Libre 商品搜索

## 原则

- 指定市场时先运行 `scripts/mercadolibre_site_list.py`；未指定市场才使用默认 `siteId=1`，并说明对应墨西哥站。
- 搜索运行 `scripts/mercadolibre_goods_search.py`，详情与最多近 31 条历史运行 `scripts/mercadolibre_goods_info.py`。
- 只使用接口返回字段。销量、销售额、跨境和 FULL 标记属于极鲸云采集数据，不称为卖家中心官方数据。
- `isFull` 是 FULL/Fully Managed 履约标记，`isCrossBorder` 是跨境标记，两者不能互相替代。
- 最多访问前 200 条；输出说明站点、币种、筛选、排序、页码、实际样本量和更新时间。
- 服务端要求暂停时按 [查询暂停与恢复流程](references/查询暂停与恢复流程.md) 处理。

## 工作流

1. 明确站点、类目或关键词、价格/销量/评分区间及跨境或 FULL 条件。
2. 按 [商品接口](references/MercadoLibre商品接口.md) 生成最少条件并搜索。
3. 对少量候选查询详情，核验商品历史、店铺、类目路径、发货地和更新时间。
4. 按 [商品研究](references/MercadoLibre商品研究.md) 比较需求、价格、口碑、生命周期与供给风险。
5. 涉及经营决策时读取 [运营与政策口径](references/MercadoLibre运营与政策口径.md)。

## 边界

- 没有图搜、搜索量、流量、转化率、广告、成本、佣金、物流费用、退货率和利润数据。
- 类目为当前 ES 商品样本中观察到的路径，不代表平台完整类目树。
- 热销不等于低竞争；前 200 条不能外推成全市场。
- 缺失值显示 `-`，不自行估算或补齐。

输出默认包含：结论、查询口径、候选证据、风险和下一步验证。面向业务用户不展示脚本或原始 JSON。
