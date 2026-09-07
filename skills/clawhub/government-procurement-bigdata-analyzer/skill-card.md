## Description:

Analyzes Chinese government procurement, tender, award, supplier, competitor, price, and market data through the Zhiliaobiaoxun API platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business-development, sales, procurement, and market-analysis users use this skill to search public procurement notices, identify upcoming opportunities, analyze buyers and suppliers, compare competitors, and summarize award and pricing trends.

### Deployment Geography for Use:

Global, with data coverage and practical use cases focused on China government procurement and state-owned enterprise purchasing.

## Known Risks and Mitigations:

Risk: Automatic trial signup can send a persistent MAC-derived device identifier to the provider.

Mitigation: Review the automatic registration flow before installation and prefer a manually created account or a preconfigured ZLBX_API_KEY if device fingerprinting is not acceptable.

Risk: The provider API key may be stored in a local plaintext configuration file.

Mitigation: Use environment-based secret management where possible and restrict local config file permissions when provider-managed key storage is used.

Risk: The skill may include promotional referrals for affiliated provider services.

Mitigation: Treat provider links as vendor referrals and review whether they are appropriate for the deployment context.

Risk: Procurement contact data can include sensitive business contact details, sometimes returned only in masked form.

Mitigation: Preserve provider-side masking, avoid trying to reconstruct hidden contact information, and avoid bulk exporting contacts unless approved for the use case.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/government-procurement-bigdata-analyzer)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration flow](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with API request guidance, result summaries, tables, and occasional shell commands or configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY or provider-managed local API key configuration for live API access.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
