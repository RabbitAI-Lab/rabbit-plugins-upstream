## Description:

Helps bidders search Chinese tender and award notices, analyze competitors and suppliers, and assess award prices for bidding decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Bidders and procurement analysts use the skill to find tender opportunities, examine award histories and competitors, compare prices, and identify potential partners or suppliers.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Automatic account creation sends a hashed device identifier to a third-party service.

Mitigation: Review the device-data collection and require informed user consent before registration; configure ZLBX_API_KEY manually to avoid automatic registration.

Risk: Automatic registration persists an API key in a plaintext home-directory configuration file.

Mitigation: Review local key-storage policy before enabling registration; configure ZLBX_API_KEY yourself and do not allow creation of ~/.zlbx/config.json if plaintext storage is prohibited.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/liu-jiapeng/skills/bidding-yifangbao)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Registry API reference](references/api-registry.md)
- [Account API reference](references/api-account.md)
- [Automatic registration guide](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Markdown with tables and optional charts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search findings and bidding insights depend on third-party data and API access.]

## Skill Version(s):

2.0.5 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
