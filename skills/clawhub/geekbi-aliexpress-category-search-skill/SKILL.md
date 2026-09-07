---
name: geekbi-aliexpress-category-search-skill
description: 使用极鲸云查询 AliExpress 类目列表、类目父链和可信类目 ID，并结合类目下商品样本研究销量、销售额、价格带、供给结构和品类机会。用户提到 AliExpress 类目树、类目 ID、品类研究、赛道分析或类目选品时使用。只依据极鲸云真实返回的数据，不把类目商品样本当作平台全量市场。
---

# 极鲸云 AliExpress 类目研究

## 原则

- 指定市场时先运行 `scripts/aliexpress_site_list.py` 实时解析；未指定市场才使用服务端默认 `siteId=1`，不能推断它对应哪个国家。
- 从 `parentCatId=0` 运行 `scripts/aliexpress_category_list.py` 逐层下钻；已有类目 ID 时运行 `scripts/aliexpress_category_info.py` 核验父链。
- 将确认过的 `catId` 交给 `scripts/aliexpress_goods_search.py` 获取类目商品样本。
- 不根据类目名称猜 ID，不把类目父级、叶子类目或其他站点 ID 混用。
- 商品接口最多访问前 200 条；输出必须说明筛选条件、样本量、总命中上限、站点和更新时间。
- 服务端要求暂停时，按 [查询暂停与恢复流程](references/查询暂停与恢复流程.md) 处理。

## 工作流

1. 按 [类目接口](references/AliExpress类目接口.md) 确认类目层级和父链。
2. 使用可信 `catId` 查询商品，可按销量、销售额、价格、评分和上架时间细分。
3. 按 [类目研究](references/AliExpress类目研究.md) 比较需求、价格带、头部集中、店铺分布、新品与增长样本。
4. 对样本外推保持克制；热销类目不等于低竞争或可合规进入。
5. 涉及实际上架时读取 [运营与政策口径](references/AliExpress运营与政策口径.md)，复核限售资质、商品信息和履约要求。

## 边界

- 当前没有类目级官方 GMV、流量、搜索量、广告和评论正文。
- 类目表本身不携带站点字段；当前站点由请求中的 `siteId` 确认，跨站点使用前必须实时核验可用站点与类目适用性。
- 接口未返回链接时不拼接 URL，缺失字段显示 `-`。
- 类目商品样本中的 `999999` 占位价和高于累计总量的周期指标视为无效。

输出默认包含：类目路径、样本口径、关键数据、机会与风险、下一步验证。
