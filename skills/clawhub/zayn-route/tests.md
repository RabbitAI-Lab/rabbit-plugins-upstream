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

## 验收结果

待补充。
