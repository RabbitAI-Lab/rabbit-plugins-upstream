## Description:

Tender Search helps agents search and analyze tender, procurement, award, company, competitor, supplier, market, and price-trend data through the Zhiliaobiaoxun service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve tender and award notices, analyze companies and competitors, find expiring projects, identify suppliers, compare market participants, and inspect historical award pricing. It is intended for procurement, bidding, sales, sourcing, and market-analysis workflows that need structured tender data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First use can create or recover a device-linked trial account and store an API key under ~/.zlbx/config.json.

Mitigation: Review the auto-registration flow before installing, set ZLBX_API_KEY in advance to avoid that path, and inspect local configuration after use.

Risk: Account, recharge, and auto-login flows may be opened when quota is exhausted or account status is queried.

Mitigation: Confirm that billing or login links point to the expected Zhiliaobiaoxun domain before following them, and avoid sharing API keys in conversation.

Risk: Company contact results can include sensitive business contact data.

Mitigation: Use contact results only for appropriate business purposes, avoid bulk harvesting, and apply applicable privacy, platform, and procurement policies.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liu-jiapeng/skills/tender-search)
- [Tender Search API Reference](references/api-search.md)
- [Company Analysis API Reference](references/api-company.md)
- [Market Analysis API Reference](references/api-market.md)
- [Account API Reference](references/api-account.md)
- [Auto-Registration Flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Concise text or Markdown with structured API results, JSON request examples, and shell commands when setup is required.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses authenticated Zhiliaobiaoxun API responses; credentials should be read from ZLBX_API_KEY or local agent configuration and not displayed.]

## Skill Version(s):

2.1.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
