# Examples

## 使用说明

本文件仅保存真实、脱敏并经过人工确认的路由案例。

## 案例一：单 Skill 即可解决

输入：

检查一份报价是否完整。

预期：

只推荐 QUOTE()。

## 案例二：客户意思不清并需要回复

预期路径：

INTENT_DECODE() → CLARIFY() → REPLY()

## 案例三：陌生产品询价

预期路径：

PRODUCT_BRIEF() → CLARIFY() → RFQ()

根据结果再决定是否进入 PRICE() 和 QUOTE()。

## 案例四：客诉退款

预期路径：

COMPLAINT() → RESPONSIBILITY() → RMA() → SOLUTION() → REPLY()

## 案例五：信息不足，应停止

当产品型号和需求范围均不明确时，应先停在 CLARIFY()，不得继续 PRICE() 或 QUOTE()。

## 案例六：避免过度编排

简单付款提醒只使用 PAYMENT()，不增加 KEYPOINT()、REPORT() 或 REPLY()。

## 案例七：明确周期性汇报

输入：

整理本月业务复盘和下月重点。

预期：

只推荐 MONTHLY_REPORT()，不增加 REPORT()。

## 案例八：汇报类型不明

输入：

帮我写个给领导看的汇报。

预期：

先推荐 REPORT() 做汇报类型、对象、目的和周期识别，不直接进入 DAILY_REPORT()、WEEKLY_REPORT()、MONTHLY_REPORT()、MIDYEAR_REPORT() 或 ANNUAL_REPORT()。

## 案例九：跨部门协同后对外回复

输入：

客户希望提前上线，销售想今天回复客户，但设计和技术都还没有确认。

预期：

先推荐 CROSS_FUNCTIONAL_COLLABORATION() 整理内部事实、待确认事项、过早承诺风险和协同文本；只有内部确认后，再进入 REPLY() 生成对外客户回复。
