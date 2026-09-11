---
name: geekbi-ozon-shop-search-skill
description: 使用极鲸云查询和分析 Ozon 当前支持站点的真实店铺数据，支持按店铺、主体、国家、品牌、类目、商品规模、粉丝、销量销售额、评分、评论和开店时间筛选排序。用户提到 Ozon 店铺、卖家、竞店、头部店铺、新店、中国卖家、品牌矩阵或店铺趋势时使用。只依据极鲸云返回数据。
---

# 极鲸云 Ozon 店铺搜索

- 未指定站点时默认俄罗斯站 `siteId=1`；指定其他市场时先运行 `ozon_site_list.py`，再运行 `ozon_mall_search.py` / `ozon_mall_info.py`。
- 按 [店铺接口](references/Ozon店铺接口.md) 传最少条件，按 [店铺研究](references/Ozon店铺研究.md) 比较规模、销量、粉丝、评分、品牌、类目和生命周期。
- `chinaFlag`、主体国别、等级和排名只按来源字段解释；缺失不能反推。
- 最多访问前 200 条；报告筛选、排序、样本、历史时间和聚合来源。
- 经营判断读取 [运营与政策口径](references/Ozon运营与政策口径.md)；暂停按 [查询暂停与恢复流程](references/查询暂停与恢复流程.md)。
