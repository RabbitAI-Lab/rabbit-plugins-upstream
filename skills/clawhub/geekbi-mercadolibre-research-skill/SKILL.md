---
name: geekbi-mercadolibre-research-skill
description: 通过极鲸云查询和组合分析 Mercado Libre（美客多）真实商品、店铺、类目和评论数据，完成跨境选品、市场调研、竞品分析、价格带、销量与口碑研究。用户提出美客多综合选品、市场机会、竞品店铺、类目赛道、跨境或 FULL 履约分析，且需要多类数据形成经营判断时使用。只依据极鲸云真实返回数据，不提供图搜、关键词趋势、利润或卖家中心操作。
---

# 极鲸云 Mercado Libre 综合研究

## 能力路由

- 商品筛选、详情和历史：读取 [商品接口](references/MercadoLibre商品接口.md)，运行 `mercadolibre_goods_search.py` / `mercadolibre_goods_info.py`。
- 店铺搜索和详情：读取 [店铺接口](references/MercadoLibre店铺接口.md)，运行 `mercadolibre_mall_search.py` / `mercadolibre_mall_info.py`。
- 类目路径和类目商品样本：读取 [类目接口](references/MercadoLibre类目接口.md)，运行 `mercadolibre_category_list.py` / `mercadolibre_category_info.py`。
- 商品评论：读取 [评论接口](references/MercadoLibre评论接口.md)，运行 `mercadolibre_review_search.py`。
- 指定市场时先运行 `mercadolibre_site_list.py`；未指定时默认 `siteId=1`（墨西哥）。

## 工作流

1. 明确站点、研究对象、指标、时间和输出目标。
2. 只调用回答问题所需的最少接口；需要类目时先确认真实 `catId`。
3. 先宽筛商品或店铺，再对少量候选查详情、历史、店铺和评论。
4. 分别按商品、店铺、类目和评论研究文档分析，再交叉验证结论。
5. 输出站点、币种、筛选、排序、页码、总命中上限、实际样本量和更新时间。
6. 服务端要求暂停时按 [查询暂停与恢复流程](references/查询暂停与恢复流程.md) 处理。

## 关键边界

- `isFull` 与 `isCrossBorder` 是两个独立字段，不互相推导。
- 类目树只覆盖当前 ES 商品样本中已出现的路径，不是平台全量类目。
- 商品与店铺最多访问前 200 条；热销不等于低竞争，样本不能外推成全市场。
- 当前没有图搜、搜索词趋势、流量、转化率、广告、佣金、物流、退货和利润数据。
- 极鲸云指标不称为 Mercado Libre 卖家中心官方数据；缺失值保持 `-`。
- 涉及平台经营判断时必须读取 [运营与政策口径](references/MercadoLibre运营与政策口径.md)。

默认输出：结论、数据口径、关键证据、机会、风险、置信度和下一步验证。面向业务用户不展示脚本或原始 JSON。
