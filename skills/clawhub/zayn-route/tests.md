# Tests

## 测试原则

1. 是否先判断单 Skill 是否足够
2. 是否会推荐过多 Skill
3. 是否能识别正确调用顺序
4. 是否能说明每个 Skill 的作用
5. 是否能定义参数传递
6. 是否能设置停止条件
7. 是否会在信息不足时继续
8. 是否会把推测传成事实
9. 是否会重复询问已有信息
10. 是否明确最终输出 Skill
11. 是否会自己完成业务分析
12. 是否保持路由简洁

## 测试案例

| 编号 | 类型 | 场景 | 预期结果 |
|---|---|---|---|
| RT-01 | 正常 | 检查报价是否完整 | 只推荐 QUOTE() |
| RT-02 | 正常 | 客户意思不清并需要回复 | 推荐 INTENT_DECODE() → CLARIFY() → REPLY() |
| RT-03 | 正常 | 陌生产品询价 | 推荐 PRODUCT_BRIEF() → CLARIFY() → RFQ()，后续按结果决定是否报价 |
| RT-04 | 正常 | 客诉退款 | 推荐 COMPLAINT() → RESPONSIBILITY() → RMA() → SOLUTION() → REPLY() |
| RT-05 | 正常 | 明确本月复盘 | 只推荐 MONTHLY_REPORT() |
| RT-06 | 正常 | 上半年总结和下半年计划 | 只推荐 MIDYEAR_REPORT() |
| RT-07 | 正常 | 年度述职和明年计划 | 只推荐 ANNUAL_REPORT() |
| RT-08 | 边界 | 只说“写个汇报” | 推荐 REPORT() 先识别类型和补问 |
| RT-09 | 正常 | 跨部门确认后再回复客户 | 推荐 CROSS_FUNCTIONAL_COLLABORATION() → REPLY() |
| RT-10 | 边界 | 产品型号和需求范围均不明确 | 停在 CLARIFY()，不得继续 PRICE() 或 QUOTE() |
| RT-11 | 禁止 | 简单付款提醒 | 只使用 PAYMENT()，不增加 KEYPOINT()、REPORT() 或 REPLY() |
| RT-12 | 正常 | 信息明确的请假申请，需要发给直属主管 | 只推荐 UPWARD_COMMUNICATION() |
| RT-13 | 正常 | 需要经理在延期和按期上线之间选择并生成沟通提纲 | 推荐 DECISION() → UPWARD_COMMUNICATION() |
| RT-14 | 正常 | 重大系统故障，需要老板协调外部和内部资源 | 推荐 ESCALATE() → UPWARD_COMMUNICATION() |
| RT-15 | 边界 | 向平级财务同事索要付款记录 | 只推荐 REQUEST()，不使用 UPWARD_COMMUNICATION() |
| RT-16 | 边界 | 只说“帮我跟老板沟通”，未说明事项和目标 | 停止并补问事项、目的、期望动作和时限 |
| RT-17 | 正常 | 调查潜在客户公开背景、风险和匹配度 | COMPANY_RESEARCH() → BUSINESS_RISK() → COMPANY_FIT() |
| RT-18 | 正常 | 研究区域市场、比较对手并评估候选产品 | MARKET_RESEARCH() → COMPETITOR_ANALYSIS() → PRODUCT_SELECTION() |
| RT-19 | 边界 | 同名企业且无国家、域名或注册号 | 停在 COMPANY_RESEARCH()，不得归因或继续风险调查 |
| RT-20 | 边界 | 未找到诉讼记录 | 不得将“未找到”传递为“无风险” |
| RT-21 | 边界 | 市场范围和时间不明确 | 停在 MARKET_RESEARCH() 补问，不输出规模或进入建议 |
| RT-22 | 单 Skill | 已有研究和候选产品，只需判断验证优先级 | 只推荐 PRODUCT_SELECTION() |
| RT-23 | 边界 | 只有一条匿名差评 | SOCIAL_LISTENING() 标记线索，不进入重大风险结论 |
| RT-24 | 单 Skill | 有主体、来源和历史状态，只需扫描客户变化并更新监测状态 | 只推荐 ACCOUNT_WATCH() |
| RT-25 | 正常 | 客户公开新项目，需要判断机会、安排跟进并生成消息 | ACCOUNT_WATCH() → OPPORTUNITY() → FOLLOWUP() → REPLY() |
| RT-26 | 边界 | 第一次监测且无上次检查时间 | ACCOUNT_WATCH() 只做基线或近期扫描，不得声称新增 |
| RT-27 | 禁止 | 客户招聘采购岗位并参展，但无项目或需求证据 | ACCOUNT_WATCH() 标记线索，不直接进入 OPPORTUNITY() 或 REPLY() |

## 验收结果

待补充。
