---
name: zayn-contact-strategy
description: 针对已人工确认的目标公司，根据客户类型和具体业务证据规划优先联系部门、岗位、联系人查找路径、首次开发角度、联系前准备与可信度标记；不批量猜邮箱、不自动发送邮件或执行外联。
---

# CONTACT_STRATEGY() 联系路径策略

Display Name：`CONTACT_STRATEGY()`  
Chinese Name：联系路径策略  
Project：WorkFn  
Version：v1.0.0

## 参数与最低运行条件

必需：已筛选公司、客户类型、产品/服务、匹配证据、开发目标。建议：官网、LinkedIn 公司页、业务场景、地区语言、已有联系人、历史沟通和限制。

公司主体、客户类型和开发目标明确后才规划；联系人或邮箱无法验证时只给查找路径和可信度，不虚构个人信息。

## 流程

1. 采购型优先采购、寻源、供应链和品类岗位。
2. 技术方案型优先技术负责人、方案架构、基础设施、产品和售前岗位。
3. 渠道型优先产品、商务拓展、商业、销售和采购岗位。
4. 小型公司可优先 Owner、Founder、General Manager、Sales Director 或 Operations Manager。
5. 依次检查官网 Contact、About、Team，LinkedIn 公司员工与岗位，Google 姓名+公司，授权联系人数据库，最后才考虑疑似邮箱格式或通用邮箱。
6. 结合公司具体证据提出首次开发角度和应准备的产品信息。

岗位映射至少覆盖：采购型的 Procurement Manager、Purchasing Manager、Sourcing Manager、Supply Chain Manager、Category Manager；技术方案型的 Technical Director、Solution Architect、Infrastructure Manager、Product Manager、Pre Sales Manager；渠道型的 Product Manager、Business Development Manager、Commercial Director、Sales Director、Purchasing Manager。根据公司规模与证据调整顺序，不机械套用。

## 输出

输出公司类型、优先部门、第一/第二优先岗位、不建议优先岗位、LinkedIn 与 Google 关键词、官网路径、可用数据库、通用邮箱适用性、首次切入角度、联系前准备与问题、联系人信息可信度。

## 边界与协作

邮箱格式推断必须标记“疑似”，不得写成已验证；不得批量发送或自动外联。策略确认后，具体沟通内容交 `zayn-followup`、`zayn-reply` 或 `zayn-relation`；是否值得投入交 `zayn-qualify`。
