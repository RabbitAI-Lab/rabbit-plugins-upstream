## Description:

Searches Chinese healthcare procurement notices to identify hospital purchasers, winning suppliers, and leading suppliers for a given hospital.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and healthcare-market analysts use this skill to find Chinese medical tenders and awards, compare hospital suppliers, and examine related company and market records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Without an existing API key, trial registration uses operating-system and CPU details plus a hashed MAC address.

Mitigation: Require informed consent before collecting device details; configure an API key manually to skip device-based registration.

Risk: Automatic registration stores an API key in a local configuration file for later use.

Mitigation: Review local credential storage and protect access to the configuration file; use a preconfigured API key if persistence is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pkuycl/skills/medical-health-bid-radar-yiliaozhaobiaocaigouwang)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Business registry API reference](references/api-registry.md)
- [Account API reference](references/api-account.md)
- [Account registration reference](references/auto-register.md)
- [Provider skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with links to procurement notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include purchaser, winning supplier, amount, date, and region; availability depends on the API account.]

## Skill Version(s):

1.0.9 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
