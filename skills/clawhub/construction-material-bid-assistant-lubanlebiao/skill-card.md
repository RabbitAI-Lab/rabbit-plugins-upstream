## Description:

施工建材采招助手-鲁班乐标 helps agents query construction-material procurement data, including price trends, Top brands, historical unit prices, and major supplier lists for materials such as steel, pipes, machinery, and specific building-material models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer construction procurement questions, search bid notices, analyze companies, compare purchasers, suppliers, brands, and retrieve material price history from Lubanlebiao APIs.

### Deployment Geography for Use:

Global; the covered procurement data and workflows focus on China construction markets.

## Known Risks and Mitigations:

Risk: The skill can read or write ~/.zlbx/config.json and store API credentials locally.

Mitigation: Prefer setting ZLBX_API_KEY directly, review local credential storage before installation, and never ask users to paste API keys into chat.

Risk: Automatic registration can collect a hashed MAC address and create a trial account after user consent.

Mitigation: Require explicit consent before auto-registration, send only the documented hashed device feature, and allow users to bypass the flow by configuring ZLBX_API_KEY or ~/.zlbx/config.json.

Risk: Recharge auto-login links may provide account access if shared broadly.

Mitigation: Only produce auto-login links in the documented quota-exhaustion case and treat them as user-specific account links.

Risk: Company contact queries can return sensitive contact data or masked phone numbers.

Mitigation: Display contact data as returned, do not supplement masked numbers from other sources, and avoid bulk exporting contacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thuanlynham-stack/skills/construction-material-bid-assistant-lubanlebiao)
- [标讯搜索类工具 API 详情](artifact/references/api-search.md)
- [企业分析类工具 API 详情](artifact/references/api-company.md)
- [市场分析类工具 API 详情](artifact/references/api-market.md)
- [账户查询类工具 API 详情](artifact/references/api-account.md)
- [SKILL 自动注册详细流程](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown answers with result tables, JSON request examples, API-derived data, and occasional shell command or configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a local ~/.zlbx/config.json API key; contact details may be masked according to account tier.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
