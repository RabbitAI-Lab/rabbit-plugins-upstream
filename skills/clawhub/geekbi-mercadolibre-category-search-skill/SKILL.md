---
name: geekbi-mercadolibre-category-search-skill
description: 使用极鲸云查询 Mercado Libre（美客多）当前商品样本中真实出现的类目列表和类目父链，并结合类目商品样本研究销量、价格带、口碑和品类机会。用户提到美客多类目、类目 ID、类目树、品类研究、赛道分析或类目选品时使用。不把样本类目覆盖或商品样本当作平台全量市场。
---

# 极鲸云 Mercado Libre 类目研究

## 原则与流程

- 指定市场时先运行 `scripts/mercadolibre_site_list.py`；未指定时默认 `siteId=1`（墨西哥）。
- 从 `parentCatId=0` 运行 `scripts/mercadolibre_category_list.py` 下钻；已有类目 ID 时运行 `scripts/mercadolibre_category_info.py` 核验父链。
- 类目接口从当前 ES 商品样本的 `catItems` 构建，只覆盖已收录商品实际出现的路径，不是 Mercado Libre 全量类目树。
- 使用确认过的 `catId` 运行 `scripts/mercadolibre_goods_search.py` 获取商品样本；不根据名称猜 ID。
- 按 [类目接口](references/MercadoLibre类目接口.md) 和 [类目研究](references/MercadoLibre类目研究.md) 执行。
- 最多访问前 200 条商品；说明站点、样本覆盖、筛选、页码、样本量和更新时间。
- 服务端要求暂停时按 [查询暂停与恢复流程](references/查询暂停与恢复流程.md) 处理。

## 边界

- 没有类目级官方 GMV、流量、搜索量、广告、佣金或竞争度。
- 空类目只说明当前样本未观察到，不代表平台不存在。
- 涉及经营政策时读取 [运营与政策口径](references/MercadoLibre运营与政策口径.md)。

输出默认包含：类目路径、样本口径、关键数据、机会、风险和下一步验证。
