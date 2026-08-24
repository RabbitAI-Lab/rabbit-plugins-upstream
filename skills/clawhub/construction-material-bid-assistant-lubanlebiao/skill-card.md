## Description:

施工建材采招助手-鲁班乐标 helps agents query construction-material bidding intelligence, including historical unit prices, top brands, suppliers, purchasers, bid records, company profiles, contacts, and competitor analysis through the ZLBX API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, construction, sourcing, and sales-intelligence users can use this skill to search bid notices, analyze companies and competitors, identify major purchasers or suppliers, and compare construction-material brand and model pricing. The skill is especially intended for product or material queries where historical bid prices and supplier lists help purchasing or market-analysis decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan verdict is suspicious because the skill acts as a broad procurement-intelligence assistant rather than only a construction-material price checker.

Mitigation: Review whether broad bid search, company analysis, competitor intelligence, and contact lookup are appropriate for the intended deployment before enabling the skill.

Risk: The skill may read or write ~/.zlbx/config.json and can create a trial account from device-derived identifiers when no API key is configured.

Mitigation: Prefer a user-provided ZLBX_API_KEY, require explicit user consent before trial registration, and verify local credential-storage behavior in the target agent environment.

Risk: The skill can access account usage data, company contacts, and competitor intelligence.

Mitigation: Limit use to authorized accounts and contexts where exposing procurement contacts, consumption details, and competitive analysis is acceptable.

## Reference(s):

- [Skill release page](https://clawhub.ai/thuanlynham-stack/skills/construction-material-bid-assistant-lubanlebiao)
- [Account setup guide](references/account-setup.md)
- [Account API details](references/api-account.md)
- [Company analysis API details](references/api-company.md)
- [Market analysis API details](references/api-market.md)
- [Bid search API details](references/api-search.md)
- [ZLBX API base endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名})
- [ZLBX account portal](https://ai.zhiliaobiaoxun.com/?ch=s35)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with API request examples, retrieved bid or company data summaries, and occasional shell commands for account setup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a local ~/.zlbx/config.json API key; first-use trial account setup may write local credential configuration after user consent.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
