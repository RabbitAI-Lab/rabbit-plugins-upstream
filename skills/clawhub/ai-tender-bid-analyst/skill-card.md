## Description:

AI 招投标分析师用自然语言检索和分析招中标、企业、市场和价格数据，帮助用户研判商机、竞对和投标决策。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business teams use this skill to analyze tender opportunities, procurement activity, supplier competition, market trends, company profiles, bid prices, and likely bidders from vendor bid-data APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create a vendor account and inspect local platform, CPU architecture, and hashed MAC address when no API key is configured.

Mitigation: Prefer a manually supplied ZLBX_API_KEY; require explicit user consent before device collection or automatic registration.

Risk: The skill can persist a vendor API key in ~/.zlbx/config.json.

Mitigation: Protect the config file, avoid displaying API keys, and rotate the key if it is exposed.

Risk: Quota handling can generate auto-login recharge links tied to the current API key.

Mitigation: Confirm the user wants billing guidance before presenting recharge links, and avoid sharing those links beyond the current user context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/ai-tender-bid-analyst)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown analysis with JSON API request and response snippets when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use vendor API data, local API-key configuration, and billing or recharge guidance when quota handling is needed.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
