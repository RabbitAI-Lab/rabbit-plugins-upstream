---
name: geekbi-ozon-category-search-skill
description: 使用极鲸云查询 Ozon 当前支持站点已同步类目树、类目详情、父链、商品店铺规模、销量销售额、均价和历史，并结合真实商品样本研究品类机会。用户提到 Ozon 类目、类目 ID、类目树、赛道分析、市场规模或类目选品时使用。不把当前数据覆盖当作平台全量。
---

# 极鲸云 Ozon 类目研究

- 未指定站点时默认俄罗斯站 `siteId=1`；指定其他市场时先运行 `ozon_site_list.py`，再从 `ozon_category_list.py` 下钻或搜索并核验父链。
- 只使用确认过的 `catId`，不按名称猜测；商品样本运行 `ozon_goods_search.py`。
- 按 [类目接口](references/Ozon类目接口.md) 和 [类目研究](references/Ozon类目研究.md) 解释指标与覆盖范围。
- 最多访问前 200 条商品；空结果不等于平台不存在。
- 经营判断读取 [运营与政策口径](references/Ozon运营与政策口径.md)；暂停按 [查询暂停与恢复流程](references/查询暂停与恢复流程.md)。
