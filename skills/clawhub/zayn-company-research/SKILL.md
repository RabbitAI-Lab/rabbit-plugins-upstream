---
name: zayn-company-research
description: 调查潜在客户、供应商、合作伙伴或竞争对手的公开企业信息，包括主体身份、公司背景、产品业务、规模信号、管理团队、认证和近期动态；先确认主体，再区分事实、信号、推断与待验证信息。用于企业真实性、背景和实力信号调查，不直接决定是否合作。
---

# COMPANY_RESEARCH() 企业公开信息调查

Display Name：`COMPANY_RESEARCH()`  
Chinese Name：企业公开信息调查  
Project：WorkFn  
Version：v1.0.0

## 运行边界

只收集、整理和分析公开事实，不直接给出合作决定。需要公开数据源或用户提供资料；无法联网或来源需登录时，列出待授权来源和补充材料。历史询价、订单、付款、发货和售后行为由 `zayn-customer-profile` 处理。

## 参数与最低运行条件

必需参数：目标公司名称、国家或地区、官网/域名或注册线索、调查目的、时间范围、重点方向。参数状态只使用：已命中、部分命中、缺失、冲突、待验证。

正式研究前确认：公司名称明确；国家或地区明确；至少有一个高区分度主体线索；调查目的明确；同名主体可基本区分。不满足时只输出主体候选、参数状态和补问。

## 工作流

1. 读取 `../shared/entity_resolution.md` 确认主体。
2. 读取 `../shared/research_workflow.md` 制定研究问题和来源计划。
3. 按 `../shared/source_quality.md` 收集注册、官网、产品、团队、市场、认证和近期动态。
4. 按 `../shared/evidence_rules.md` 与 `../shared/freshness_rules.md` 分类证据并核对日期。
5. 按 `../shared/citation_rules.md` 形成可追溯输出。

## 输出

依次输出：参数状态表、主体识别结果、基本信息、业务与产品、规模与经营信号、管理团队、市场与客户类型、认证资质、近期动态、已确认事实、待验证信息、信息缺口、核验动作、来源清单。

## 禁止事项

不得依据网站设计判断实力；不得把 LinkedIn 员工数、招聘信息或官网自述直接视为独立事实；不得混入关联公司信息；不得编造营收、员工数或客户名单；不得直接决定合作。

## 协作

公开研究后可交给 `zayn-business-risk`、`zayn-social-listening` 和 `zayn-company-fit`。内部业务历史由 `zayn-customer-profile` 补充，资格和优先级由 `zayn-qualify`、`zayn-priority` 判断。
