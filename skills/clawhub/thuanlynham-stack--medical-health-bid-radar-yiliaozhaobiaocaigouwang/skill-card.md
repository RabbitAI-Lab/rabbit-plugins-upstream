## Description:

医疗大健康采招雷达-医疗招标采购网，当搜索词包含医院、医疗、卫生、体检时触发，重点提取采购方（医院）和中标方（医药公司/代理商），分析特定医院的Top供应商体系。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Chinese bidding and procurement data, with emphasis on healthcare-related hospital purchasers, suppliers, award history, market patterns, and account status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is broader than a strictly medical procurement radar.

Mitigation: Confirm the user's intended domain and apply healthcare keywords, purchaser types, or filters when medical-only coverage is required.

Risk: Automatic registration sends a MAC-derived device fingerprint.

Mitigation: Prefer a manually configured API key and use auto-registration only after explicit consent, especially on shared or managed machines.

Risk: The skill may persist an API key in ~/.zlbx/config.json.

Mitigation: Protect the local config file with user-only permissions and avoid exposing API keys in prompts, logs, or outputs.

Risk: Contact-related features can expose or encourage use of procurement contact data.

Mitigation: Use returned contact fields only as provided, do not attempt to recover masked phone numbers, and avoid bulk outreach.

Risk: The skill includes service referrals and recharge flows.

Mitigation: Treat referrals as optional next steps and keep them separate from the procurement facts returned to the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thuanlynham-stack/skills/medical-health-bid-radar-yiliaozhaobiaocaigouwang)
- [API search reference](references/api-search.md)
- [API company reference](references/api-company.md)
- [API market reference](references/api-market.md)
- [API account reference](references/api-account.md)
- [Auto-registration reference](references/auto-register.md)
- [Procurement API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Account and registration portal](https://ai.zhiliaobiaoxun.com/?ch=s36)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with tables, JSON request examples, REST API responses, and occasional shell commands for account setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a locally stored API key; results depend on the external procurement API and account quota.]

## Skill Version(s):

1.0.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
