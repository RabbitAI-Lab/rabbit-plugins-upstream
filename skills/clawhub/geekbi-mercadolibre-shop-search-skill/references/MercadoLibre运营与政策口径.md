# Mercado Libre 运营与政策口径

本 Skill 的经营解释遵循 Mercado Libre 官方开发者文档，但实际筛选和结论只使用极鲸云返回字段。

- 卖家信誉按市场分别计算，并涉及投诉、卖家取消和处理时间等维度。极鲸云的 `mallStar`、`reputationLevelText`、`powerSellerStatusText` 只是采集快照，不能替代官方完整信誉面板。官方参考：[Seller Reputation](https://global-selling.mercadolibre.com/devsite/en_us/price-per-variation-cbt/seller-reputation-global-selling)。
- User Products 将产品定义与各站点商品销售条件分离；同一产品在不同站点仍可能有不同价格、库存和销售状态。因此不能仅凭标题或 `productId` 把跨站报价当成同一商品记录。官方参考：[User Products](https://global-selling.mercadolibre.com/devsite/en_us/deals-gs/user-products-cbt) 与 [Global Listing](https://global-selling.mercadolibre.com/devsite/en_us/sync-and-modify-listings-gs/global-listing)。
- FULL/Fully Managed 是履约模式，不天然等于跨境商品。分析时分别使用 `isFull` 和 `isCrossBorder`，不得互相推断。官方参考：[Fully Managed](https://global-selling.mercadolibre.com/devsite/en_us/manage-claims/fully-managed-product-publishing)。
- 上架前仍需按目标站点核对禁限售、资质、知识产权、商品信息、税务、物流和售后要求；本 Skill 不执行发布、定价或卖家后台操作。
