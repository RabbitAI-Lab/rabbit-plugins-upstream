## Description:

建筑工程标讯洞察-筑龙标事 helps agents search construction bid notices, analyze companies and markets, identify expiring projects, and recommend potential bidders for infrastructure and large engineering opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents working with construction-market intelligence use this skill to retrieve bid notices, analyze buyers and suppliers, find competitors and potential bidders, and summarize bid-market opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create and manage a third-party trial account using a persistent device identifier and a saved API key.

Mitigation: Prefer a manually configured ZLBX_API_KEY, and approve trial account creation only when comfortable with the vendor workflow and hashed MAC-derived identifier.

Risk: Auto-created accounts can later produce an auto-login recharge link when quota is exhausted.

Mitigation: Review recharge links before using them, and avoid sharing account or API-key details in chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/architecture-bid-insight-zhulongbiaoshi)
- [API search reference](references/api-search.md)
- [API company reference](references/api-company.md)
- [API market reference](references/api-market.md)
- [API account reference](references/api-account.md)
- [Trial account setup reference](references/account-setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown responses with JSON API payloads and concise bid-analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a user-consented trial account setup; API responses use JSON with data, error, and meta fields.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
