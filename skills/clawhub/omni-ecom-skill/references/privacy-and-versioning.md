# 客户隔离、版本与修订

## 客户隔离

每次运行先建立 `client_scope`。最终回复、PDF、图表、文件名和示例只能出现本次范围明确授权的品牌/店铺。历史报告、记忆和模板只复用匿名结构；不得提及或暗示其他客户名称、案例数字、店铺 ID、私有路径或“沿用某品牌版式”。

## 版本标注

`omni-ecom v1.5.10` 是专家团能力版本；`R1/R2` 是本次报告修订号。标题、PDF 首页、摘要和最终回复都显示二者。版本差异至少说明：数据质量闸门、真实协作可见性、默认图表化 PDF、冻结复核、回执隔离、公域客户隔离、团队启动超时和安全续跑。

## 完成态

只有在数据闸门、角色参与、报告生成、PDF 渲染、客户范围扫描和交付复核均满足时，才可写“正式交付”。任何缺项必须返回对应状态：`collaboration_unavailable`、`collaboration_incomplete`、`collaboration_wait_timeout`、`pdf_delivery_unavailable`、`review_stale_blocked` 或 `client_scope_leak_blocked`。
