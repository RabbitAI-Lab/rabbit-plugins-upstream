---
name: commerce-radar
description: Use when 用户需要商品搜索与价格证据、查看商品详情、分析公开店铺，或基于关键词生成电商竞争报告；需要 COMMERCE_RADAR_API_KEY。
metadata: {"packageVersion":"1.0.0","openclaw":{"emoji":"📡","homepage":"https://ai-skills.open-idea.net","primaryEnv":"COMMERCE_RADAR_API_KEY","requires":{"env":["COMMERCE_RADAR_API_KEY"]}}}
---

# Commerce Radar

调用 AI Skills 平台的 Commerce Radar 公共 API；不要直连或描述第三方 Provider。默认 API 根为
`https://ai-skills.open-idea.net/api/v1`，`AI_SKILLS_API_URL` 只能覆盖站点根。

## 执行流程

1. 按 [API Key 配置](references/API-KEY.md)检查产品专属 Key，禁止回显完整值。
2. 从 [Operations 契约](references/OPERATIONS.md)选择一个明确 operation，只发送列出的字段。
3. 按 [HTTP 请求与任务轮询](references/HTTP-REQUESTS.md)为每个新逻辑请求生成 UUID 幂等键。
4. `202` 后查询同一 operation 的任务路径，直到终态或达到有界等待上限。
5. 按 [行为与错误规则](references/BEHAVIOR-RULES.md)提取 structured 结果、产物与计费头。

## 交付边界

- 把商品、店铺和报告数据称为 Provider 在特定时间返回的观察结果，保留 `source_url` 等证据。
- 不把缺失商品、空结果或 pending 状态解释为事实不存在。
- 不接受内网、环回、带用户信息或非 HTTP(S) 的商品/店铺 URL；不自行抓取目标站点。
- 不承诺固定价格、结果数量、实时性或 Provider 成功；费用只引用响应头。

## 参考资料

- [API Key 配置](references/API-KEY.md)
- [Operations 契约](references/OPERATIONS.md)
- [HTTP 请求与任务轮询](references/HTTP-REQUESTS.md)
- [行为与错误规则](references/BEHAVIOR-RULES.md)
