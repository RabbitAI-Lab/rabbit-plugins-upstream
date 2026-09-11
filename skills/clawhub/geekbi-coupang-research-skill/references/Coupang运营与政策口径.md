# Coupang 运营与政策口径

本 Skill 的经营解释参考 Coupang 官方资料，但筛选和数据结论只使用极鲸云返回字段。政策可能更新，实际刊登前必须回查官方页面。

- 极鲸云当前数据集仅覆盖韩国站。Coupang 卖家 Open API 文档中出现韩国、台湾等适用市场，不代表本 Skill 同时提供这些市场的数据。
- `productId` 是极鲸云收录的前台商品 ID，不应直接当作卖家 Open API 的 `sellerProductId` 或 `vendorItemId`。官方区分了注册商品 ID、商品 ID和规格 ID：[商品查询](https://developers.coupangcorp.com/hc/en-us/articles/360033644994-Querying-product)。
- 刊登需要正确的展示类目编码，并按类目元数据填写购买选项、认证、告知和材料；本 Skill 的类目研究不替代刊登校验：[类目元数据查询](https://developers.coupangcorp.com/hc/en-us/articles/360034035713-Category-Metadata-Query)。
- Coupang 已公告自 2026 年 8 月 1 日起逐步强制品牌、GTIN/型号和必填购买选项。研究结果不代表商品满足发布要求：[商品信息政策更新](https://developers.coupangcorp.com/hc/en-us/articles/58875696282905-Product-Information-Policy-Update-Mandatory-Brand-GTIN-Model-Number-and-Purchase-Option-Fields-Published-on-May-21-2026)。
- `ROCKET_MERCHANT` 等值来自商品页展示标记。火箭成长/卖家火箭相关徽章与曝光还会受价格竞争力、政策遵守等条件影响，配送时间也因商品和地区而异：[Rocket Growth](https://marketplace.coupang.com/rocket-growth)。
- `COUPANG_GLOBAL` 只说明观察到跨境配送展示标记，不等于卖家国籍、进口合规、利润或跨境资格。
- 上架前仍需核对禁限售、知识产权、认证、商品信息、税务、物流和售后要求；本 Skill 不执行发布、定价或 WING 后台操作。
