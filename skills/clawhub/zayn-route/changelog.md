# Changelog

## v0.1.5

1. 新增 `AI_TASK_DIAGNOSIS()` 路由，建立与 `ROUTE()`、`PLAN()` 和 `FOCUS()` 的职责边界。
2. 新增目标市场客户开发 5 个 Skill 的阶段选择规则。
3. 明确 `MARKET_OPPORTUNITY()`、`TARGET_CUSTOMER_PROFILE()`、`SEARCH_STRATEGY()`、`COMPANY_SCREENING()` 和 `CONTACT_STRATEGY()` 与既有市场、客户画像、企业研究及客户沟通 Skill 的边界。
4. 增加人工搜索、人工确认、候选公司材料不足及禁止自动外联的停止条件。
5. 新增 4 个路由示例和 10 个测试案例。

## v0.1.4

1. 新增 `ACCOUNT_WATCH()` 客户动态跟踪与商机信号分析路由。
2. 建立与 `COMPANY_RESEARCH()`、`SOCIAL_LISTENING()`、`OPPORTUNITY()`、`FOLLOWUP()` 和 `REPLY()` 的职责边界。
3. 增加账户动态单 Skill 路由及 ACCOUNT_WATCH → OPPORTUNITY → FOLLOWUP → REPLY 分阶段链路。
4. 增加无历史基线、招聘、参展和弱信号不得升级为明确商机的停止条件。
5. 新增 4 个路由示例和 4 个测试案例。

## v0.1.3

1. 新增 7 个市场与商业情报 Skill 的选择和编排规则。
2. 建立企业公开调查、合作风险、舆情、匹配、竞争、市场研究和选品的职责边界。
3. 增加潜在客户调查和竞争市场选品两条分阶段路由。
4. 增加主体冲突、辖区缺失、市场边界不足、匿名评论和“未找到”信息的停止条件。
5. 新增 4 个路由示例和 7 个测试案例。

## v0.1.2

1. 新增 `UPWARD_COMMUNICATION()` 上级沟通与管理沟通路由。
2. 建立 `REQUEST()`、`DECISION()`、`ESCALATE()` 与 `UPWARD_COMMUNICATION()` 的边界。
3. 增加请假、领导决策、重大升级和平级内部请求路由案例。
4. 增加 5 个上级沟通相关路由测试和 1 个信息不足停止测试。

## v0.1.1

1. 增加周期性汇报路由说明，覆盖日报、周报、月报、年中报告和年度报告。
2. 补充明确周期时直达专项汇报 Skill、类型不明时先用 REPORT() 的示例。
3. 增加路由测试案例，避免把明确月报、年中报告或年度报告过度编排。
4. 增加跨部门协同到客户回复的路由示例。

## v0.1

1. 新增 ROUTE() Skill 路由与编排
2. 建立单 Skill 优先原则
3. 建立多 Skill 调用链规则
4. 建立参数传递规则
5. 建立停止条件
6. 当前等待真实案例测试
