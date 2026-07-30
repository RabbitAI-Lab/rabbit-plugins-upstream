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
