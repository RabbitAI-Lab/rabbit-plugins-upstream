## Description:

Searches Chinese tender and award notices and analyzes upcoming opportunities, companies, suppliers, and historical prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and business analysts use the skill to find Chinese bidding opportunities, review award histories, compare prices, and identify potential suppliers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Without an API key, trial registration sends device-derived attributes to the provider.

Mitigation: Request informed consent before registration; set ZLBX_API_KEY manually to skip device registration.

Risk: Automatic registration writes an API key to a local configuration file.

Mitigation: Review local credential storage before opting in and avoid sharing or displaying the API key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/liu-jiapeng/skills/bidding-search-jianyu)
- [Search API reference](artifact/references/api-search.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Company data API reference](artifact/references/api-company.md)
- [Account registration and privacy](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries, tables, and links to source notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results state search filters and monetary units; availability depends on the provider API and account credits.]

## Skill Version(s):

2.0.5 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
