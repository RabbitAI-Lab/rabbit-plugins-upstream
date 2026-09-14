---
name: geekbi-coupang-category-search-skill
description: 使用极鲸云查询 Coupang 韩国站全量展示类目树和类目父链，并结合真实商品样本研究价格、近 28 日销量与浏览量、评分和竞争。用户提到 Coupang 类目、展示类目 ID、展示类目编码、类目树、品类研究、赛道分析或类目选品时使用。类目接口可用于确认研究筛选条件，但不替代刊登所需的官方类目元数据与合规校验。
---

# 极鲸云 Coupang 类目研究

## 原则与流程

- 当前仅支持韩国站 `siteId=1`、KRW；运行 `scripts/coupang_site_list.py` 核验。
- 从 `parentId=0` 运行 `scripts/coupang_category_list.py` 逐层下钻；已有类目 ID 时运行 `scripts/coupang_category_info.py` 核验父链。
- 类目树来自 `coupangshuju-java` 的全量类目服务；区分导航用 `displayItemCategoryId` 与刊登/筛选相关的 `displayItemCategoryCode`。
- 按 [类目接口](references/Coupang类目接口.md) 将确认过的根、叶子或路径用于 `scripts/coupang_goods_search.py`；不根据名称猜 ID。
- 按 [类目研究](references/Coupang类目研究.md) 分析商品样本；最多访问前 200 条并说明样本范围和更新时间。
- 涉及刊登或合规时读取 [运营与政策口径](references/Coupang运营与政策口径.md)。
- 服务端要求暂停时按 [查询暂停与恢复流程](references/查询暂停与恢复流程.md) 处理。

## 边界

- 类目树是全量导航数据，类目商品研究仍受极鲸云商品收录和前 200 条限制。
- 没有类目级官方 GMV、流量、搜索量、广告、佣金或竞争度。
- 类目商品少不等于蓝海；缺失值显示 `-`。

输出默认包含：类目路径、类目 ID/编码、商品样本口径、关键数据、机会、风险和下一步验证。
