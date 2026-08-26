---
name: seo-auditor
description: Use when 用户需要研究关键词指标、审计公开网页、比较本站与竞品的关键词差距，或把带来源的发现和指标汇总为 SEO 审计报告；需要 SEO_AUDITOR_API_KEY。
metadata: {"packageVersion":"1.0.0","openclaw":{"emoji":"🔎","homepage":"https://ai-skills.open-idea.net","primaryEnv":"SEO_AUDITOR_API_KEY","requires":{"env":["SEO_AUDITOR_API_KEY"]}}}
---

# SEO Auditor

通过 AI Skills 平台执行有来源的 SEO 查询与页面审计。默认 API 根为
`https://ai-skills.open-idea.net/api/v1`；`AI_SKILLS_API_URL` 只能覆盖站点根。不要直连或
描述第三方 Provider endpoint。

## 执行流程

1. 按 [API Key 配置](references/API-KEY.md)读取产品专属 Key，不回显完整值。
2. 从 [Operations 契约](references/OPERATIONS.md)选择 operation，只发送白名单字段。
3. 按 [HTTP 请求与任务轮询](references/HTTP-REQUESTS.md)为新逻辑请求生成 UUID 幂等键。
4. `page.audit` 异步轮询；其余 operation 通常同步，若返回 `202` 也查询同 operation。
5. 按 [证据、安全与错误规则](references/BEHAVIOR-RULES.md)交付 structured 结果和计费头。

## 核心边界

- 页面审计目标必须是公开 HTTP(S) URL；平台执行两阶段 DNS 校验以阻断 SSRF 与 DNS 重绑定。
- 保留每项 `source`、`observed_at` 和适用的 `evidence_url`，不把缺少证据的建议写成事实。
- `report.create` 仅在平台本地汇总调用者提交的 findings/metrics，不读取旧任务或自行搜索。
- 不承诺排名、流量提升、数据实时性、固定价格或 Provider 成功。

## 参考资料

- [API Key 配置](references/API-KEY.md)
- [Operations 契约](references/OPERATIONS.md)
- [HTTP 请求与任务轮询](references/HTTP-REQUESTS.md)
- [证据、安全与错误规则](references/BEHAVIOR-RULES.md)
