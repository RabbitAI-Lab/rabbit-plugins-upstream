## Description:

Helps users search Chinese procurement and bidding notices, research companies and suppliers, and analyze purchasing trends through the Zhiliaobiaoxun service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, sales teams, and analysts use this skill to find Chinese tender opportunities, review company bidding history, identify suppliers and competitors, and summarize market activity.

### Deployment Geography for Use:

Global (focused on Chinese procurement data)

## Known Risks and Mitigations:

Risk: Procurement searches, company names, and account-linked requests are sent to Zhiliaobiaoxun.

Mitigation: Review the data you submit and configure your own ZLBX_API_KEY intentionally before use.

Risk: First-time setup can collect a device hash and save a generated API key locally.

Mitigation: Review the registration flow and consent before proceeding; choose manual key setup if preferred.

Risk: The skill can make a free account balance and update check using configured credentials.

Mitigation: Review this behavior before installation and monitor account-linked API use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/china-national-bidding-zhongguozhaobiao)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Procurement search API](references/api-search.md)
- [Company analysis API](references/api-company.md)
- [Company registry API](references/api-registry.md)
- [Market analysis API](references/api-market.md)
- [Account API](references/api-account.md)
- [Automatic registration process](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search filters and amounts are labeled in results; available account information may be summarized on request.]

## Skill Version(s):

1.0.9 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
