## Description:

Searches local Chinese procurement and tender notices by province, city, county, amount, and date, returning recent announcements and budget amounts in reverse chronological order.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement or business-development teams use this skill to find location-specific tender opportunities, inspect tender details, and summarize buyer, supplier, company, market, and account information from the Zhiliaobiaoxun APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The vendor receives tender queries and account usage requests made through the skill.

Mitigation: Install and use the skill only for workflows where sharing those queries with the vendor is acceptable.

Risk: If no API key is configured, trial registration can collect a consent-gated device fingerprint derived from platform, CPU architecture, and a MAC hash.

Mitigation: Prefer configuring ZLBX_API_KEY yourself, or decline auto-registration if MAC-derived device identification is not acceptable.

Risk: The skill exposes broader company, market, contact, and referral behavior than a narrow local tender search requires.

Mitigation: Use contact lookup, company analysis, market analysis, and referral flows only when those capabilities are intended for the workflow.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/liu-jiapeng/skills/tender-express-search-bidizhaobiao)
- [Tender Search API Reference](references/api-search.md)
- [Company Analysis API Reference](references/api-company.md)
- [Market Analysis API Reference](references/api-market.md)
- [Account API Reference](references/api-account.md)
- [Auto-Registration Flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON or HTTP examples and concise tender result tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-gated auto-registration; uses REST APIs and may return masked contact data on free accounts.]

## Skill Version(s):

2.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
