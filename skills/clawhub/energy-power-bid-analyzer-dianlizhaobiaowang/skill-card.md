## Description:

Analyzes energy and power procurement data from Dianlizhaobiaowang for grid, power, renewable energy, photovoltaic, energy storage, and wind-power bid searches, company lookups, market aggregation, and award concentration analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement analysts, and developers use this skill to query Chinese energy and power bidding data, compare purchasers and suppliers, inspect company tender histories, and summarize market concentration for specific equipment or project categories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create a free account by sending device characteristics when no API key is configured.

Mitigation: Require explicit user consent before automatic registration, and allow users to avoid this flow by preconfiguring ZLBX_API_KEY or ~/.zlbx/config.json.

Risk: The skill stores an API key locally in ~/.zlbx/config.json after automatic registration.

Mitigation: Protect the local credential file, avoid displaying API keys in chat output, and review local credential handling before deployment.

Risk: The skill can query project contact data and may expose contact details depending on account level.

Mitigation: Display contact data exactly as returned, respect masked contact responses, and avoid using external search to reconstruct masked phone numbers.

Risk: Recharge and auto-login links are part of the account flow.

Mitigation: Review account linkage and payment workflows before installation, especially for enterprise-managed environments.

## Reference(s):

- [Skill overview and tool list](artifact/SKILL.md)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Automatic registration reference](artifact/references/auto-register.md)
- [ClawHub skill page](https://clawhub.ai/thuanlynham-stack/skills/energy-power-bid-analyzer-dianlizhaobiaowang)
- [Dianlizhaobiaowang API base endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool_name})
- [Manual account and recharge portal](https://ai.zhiliaobiaoxun.com/?ch=s38)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with tables, JSON request examples, API result summaries, and occasional shell or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read ZLBX_API_KEY or ~/.zlbx/config.json; first-run automatic registration requires user consent before collecting device characteristics.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
