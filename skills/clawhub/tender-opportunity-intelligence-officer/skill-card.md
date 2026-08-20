## Description:

招投标商机情报与竞对动态分析助手，帮助销售与商务团队发现临期续约项目、追踪竞争对手中标动态、识别潜在客户和供应商。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, business development, and market intelligence users use this skill to query tender data, find expiring renewal opportunities, analyze competitors, identify likely suppliers, and summarize procurement-market signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic trial-account creation can collect a hashed MAC-based device identifier when no API key is configured.

Mitigation: Require explicit user consent before registration or device-data collection, and prefer a preconfigured ZLBX_API_KEY for managed environments.

Risk: The skill can write an API key to ~/.zlbx/config.json for later use.

Mitigation: Tell users where the credential is stored, avoid displaying the key in chat or logs, and apply local file-permission controls where possible.

Risk: Quota handling can generate recharge or auto-login links for the publisher service.

Mitigation: Generate billing or login links only after confirming the API-key source, and make clear that the link leads to the third-party publisher service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/tender-opportunity-intelligence-officer)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON/API examples and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use tender-data API calls, local API-key configuration, and recharge or login links when account state requires it.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
