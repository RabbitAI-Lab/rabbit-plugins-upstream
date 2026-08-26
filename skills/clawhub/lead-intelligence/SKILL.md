---
name: lead-intelligence
description: Use when 用户需要按合规过滤器搜索企业或联系人、基于用户提交的可观察信号执行线索评分，或生成本地线索报告；需要 LEAD_INTELLIGENCE_API_KEY。
metadata: {"packageVersion":"1.0.0","openclaw":{"emoji":"🎯","homepage":"https://ai-skills.open-idea.net","primaryEnv":"LEAD_INTELLIGENCE_API_KEY","requires":{"env":["LEAD_INTELLIGENCE_API_KEY"]}}}
---

# Lead Intelligence

通过 AI Skills 平台执行企业/联系人搜索与本地线索评分。默认 API 根为
`https://ai-skills.open-idea.net/api/v1`；`AI_SKILLS_API_URL` 只能覆盖站点根。不要直连或
描述第三方 Provider 接口。

## 执行流程

1. 按 [API Key 配置](references/API-KEY.md)读取产品专属 Key，不回显完整值。
2. 从 [Operations 契约](references/OPERATIONS.md)选择 operation，并严格使用其白名单字段。
3. 按 [HTTP 请求与任务查询](references/HTTP-REQUESTS.md)为新逻辑请求生成 UUID 幂等键。
4. 通常同步读取结果；若返回 `202`，查询同 operation 的任务路径直到终态或有界上限。
5. 按 [隐私、评分与错误规则](references/BEHAVIOR-RULES.md)交付结果和计费头。

## 核心边界

- `company.search`、`people.search` 需要平台 Provider；`lead.score`、`report.create` 在平台
  本地运行，不需要 Provider 连接。
- 不接收 LinkedIn Cookie、账号、密码、session 或任意 Provider payload，不登录或抓取
  LinkedIn。
- `people.search` 不返回邮箱或电话号码，只可报告 `email_available`、
  `direct_phone_available` 布尔标记；不得据此猜测、拼接或购买联系方式，也不推断电话。
- 评分只反映用户提交的四类信号，不代表身份真实性、购买意愿或成交概率。

## 参考资料

- [API Key 配置](references/API-KEY.md)
- [Operations 契约](references/OPERATIONS.md)
- [HTTP 请求与任务查询](references/HTTP-REQUESTS.md)
- [隐私、评分与错误规则](references/BEHAVIOR-RULES.md)
