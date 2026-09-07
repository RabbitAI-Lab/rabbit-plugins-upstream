---
name: geekbi-ozon-keyword-search-skill
description: 使用极鲸云查询和分析 Ozon 当前支持站点的真实关键词数据，包括原始词和中文词、搜索量、销量销售额、商品店铺供给、平均价格、类目、日周月变化和历史。用户提到 Ozon 搜索词、关键词趋势、热词、蓝海词、需求或供给竞争时使用。仅依据极鲸云真实返回数据。
---

# 极鲸云 Ozon 关键词搜索

- 未指定站点时默认俄罗斯站 `siteId=1`；指定其他市场时先运行 `ozon_site_list.py`，再运行 `ozon_keyword_search.py` / `ozon_keyword_info.py`。
- 保留原始俄文或用户原词，按 [关键词接口](references/Ozon关键词接口.md) 传最少条件。
- 按 [关键词研究](references/Ozon关键词研究.md) 交叉搜索量、销量销售额、商品数、店铺数、均价、类目、历史和来源。
- 最多访问前 200 条；高搜索量、低商品数只是候选信号。
- 经营判断读取 [运营与政策口径](references/Ozon运营与政策口径.md)；暂停按 [查询暂停与恢复流程](references/查询暂停与恢复流程.md)。
