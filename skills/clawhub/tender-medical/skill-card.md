## Description:

A Chinese-language agent skill for querying and analyzing medical and healthcare tender, bid-award, company, market, pricing, and account data from Zhi Liao Biao Xun services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement teams, sales teams, and bidding analysts use this skill to search healthcare-sector tender and bid-award notices, inspect company and market data, compare competitors, review historical winning prices, and check account usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts zhiliaobiaoxun.com services and requires use of a ZLBX API key for authenticated data queries.

Mitigation: Install only if this service dependency is acceptable, and prefer a manually configured ZLBX_API_KEY when users do not want automatic registration.

Risk: Automatic trial registration can send device-derived identifiers and persist an API key in ~/.zlbx/config.json.

Mitigation: Use the documented consent gate before registration, send only the minimized hashed device features described by the artifact, and choose manual API key setup if local config-file persistence is not desired.

Risk: Free or trial accounts may receive masked contact information in tender and company results.

Mitigation: Display returned contact fields as-is, explain masking once when present, and do not try to reconstruct or bulk export masked contact details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bailianai/skills/tender-medical)
- [Publisher profile](https://clawhub.ai/user/bailianai)
- [Zhi Liao Biao Xun account and API key page](https://ai.zhiliaobiaoxun.com/?ch=s154)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with tables, JSON request examples, links, and inline shell or HTTP commands when setup is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY or user-approved automatic trial registration before authenticated data queries.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
