## Description:

Helps agents search tender, procurement, and award notices, analyze suppliers and purchasers, and summarize market, competitor, company, and bid-history signals from the Zhiliaobiaoxun/Bilianwang APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sales, bid, sourcing, and market-analysis users can use this skill to find Chinese tender opportunities, inspect award history, research suppliers and customers, and compare competitor or market activity. It is also useful for agents that need structured procurement-data lookups before producing concise recommendations or summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement and company-research queries are sent to the third-party provider.

Mitigation: Install only when this data sharing is acceptable for the intended business workflow.

Risk: The skill can use a local API key file and persistent credentials.

Mitigation: Prefer a manually configured ZLBX_API_KEY when possible and protect ~/.zlbx/config.json as a secret.

Risk: Fallback registration may collect a MAC-derived device hash after user consent.

Mitigation: Review the consent prompt and skip auto-registration by configuring ZLBX_API_KEY or the local config file in advance.

Risk: Contact-phone features can expose business contact data returned by the provider.

Mitigation: Use contact lookup only for lawful business needs and do not attempt to reconstruct masked numbers.

Risk: Some answers may include promotional referral links.

Mitigation: Review generated responses for suitability before sharing them with end users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/enterprise-tender-search-bilianwang)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [API search reference](references/api-search.md)
- [API company reference](references/api-company.md)
- [API market reference](references/api-market.md)
- [API account reference](references/api-account.md)
- [Auto-registration reference](references/auto-register.md)
- [Manual registration and recharge portal](https://ai.zhiliaobiaoxun.com/?ch=s49)
- [Zhiliaobiaoxun agent](https://agent.zhiliaobiaoxun.com?utm_source=skill)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with tables, structured API request examples, and occasional shell commands for local credential setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include procurement records, company profiles, contact fields as returned by the provider, account status summaries, and links to provider pages; credentials should not be echoed.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
