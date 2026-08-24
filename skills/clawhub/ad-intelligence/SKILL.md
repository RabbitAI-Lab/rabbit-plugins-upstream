---
name: ad-intelligence
description: Use when 用户需要搜索公开广告素材、按名称分析广告主，或基于域名生成广告投放趋势报告；需要 AD_INTELLIGENCE_API_KEY。
metadata: {"packageVersion":"1.0.0","openclaw":{"emoji":"📣","homepage":"https://ai-skills.open-idea.net","primaryEnv":"AD_INTELLIGENCE_API_KEY","requires":{"env":["AD_INTELLIGENCE_API_KEY"]}}}
---

# Ad Intelligence

通过 AI Skills 平台检索广告透明度数据。默认 API 根为
`https://ai-skills.open-idea.net/api/v1`；`AI_SKILLS_API_URL` 只能覆盖站点根。不要直连、
描述或暴露第三方 Provider 接口和凭证。

## 执行流程

1. 按 [API Key 配置](references/API-KEY.md)读取产品专属 Key，禁止回显完整值。
2. 从 [Operations 契约](references/OPERATIONS.md)选择 operation，严格遵守地区二选一和字段禁令。
3. 按 [HTTP 请求与任务查询](references/HTTP-REQUESTS.md)生成 UUID 幂等键并提交 JSON。
4. 正常同步响应直接读取终态；若平台返回 `202`，查询同 operation 的任务路径。
5. 按 [行为、证据与错误规则](references/BEHAVIOR-RULES.md)交付 structured 结果和计费头。

## 交付边界

- 把素材、广告主规模与趋势称为特定来源和时间范围内的观察结果，保留 `source_url`、
  `first_seen_at`、`last_seen_at`。
- 空结果不证明广告从未存在；`partial` 不得补造缺失素材。
- 不推断未返回的受众、转化、预算、归因或广告主身份，不把素材链接当作使用授权。
- 不承诺固定价格、固定条数、实时性或上游成功；费用只引用规范响应头。

## 参考资料

- [API Key 配置](references/API-KEY.md)
- [Operations 契约](references/OPERATIONS.md)
- [HTTP 请求与任务查询](references/HTTP-REQUESTS.md)
- [行为、证据与错误规则](references/BEHAVIOR-RULES.md)
