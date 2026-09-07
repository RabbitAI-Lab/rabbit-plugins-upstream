## Description:

Analyzes Xinchuang, domestic IT, and digital-government procurement data by querying Zhiliaobiaoxun bid, company, market, pricing, and account APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sales, market-intelligence, and public-sector IT teams use this skill to search Chinese bid notices, compare suppliers and brands, inspect company procurement histories, identify opportunities, and summarize market trends for domestic IT selection decisions.

### Deployment Geography for Use:

Global (focused on China procurement and bid data)

## Known Risks and Mitigations:

Risk: Procurement queries are sent to an external vendor API.

Mitigation: Use the skill only with data that is approved for that vendor service and avoid submitting confidential procurement or sourcing details without internal approval.

Risk: The optional trial registration flow sends a MAC-derived device hash.

Mitigation: Configure ZLBX_API_KEY manually or decline auto-registration when device fingerprinting is not acceptable.

Risk: The optional registration flow can save an API key locally.

Mitigation: Manage the local credential file as a secret, restrict file access, and rotate or remove the key when no longer needed.

Risk: Contact data may be masked or governed by account limits.

Mitigation: Preserve service-provided masking, do not attempt to reconstruct hidden contact details, and follow the account's usage limits.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/xinchuang-it-procurement-analyzer)
- [Publisher Profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Bid Search API Reference](references/api-search.md)
- [Company Analysis API Reference](references/api-company.md)
- [Market Analysis API Reference](references/api-market.md)
- [Account API Reference](references/api-account.md)
- [Auto-Registration Flow](references/auto-register.md)
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Manual Account and Recharge Entry](https://ai.zhiliaobiaoxun.com/?ch=s57)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with tables, concise prose, JSON request examples, and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based trial registration; calls external Zhiliaobiaoxun APIs and may surface masked contact data depending on account status.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
