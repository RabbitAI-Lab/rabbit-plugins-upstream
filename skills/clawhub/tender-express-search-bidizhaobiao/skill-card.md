## Description:

Searches regional Chinese procurement notices by location and returns recent results with dates, budgets, and source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and other users search province- or city-specific Chinese tender notices and review budgets, dates, and source links. The integration also offers company, contact, market, and account information when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration accesses company intelligence and contact data beyond regional tender search.

Mitigation: Install only if the broader data access is needed; limit queries to the user's request and avoid exporting or reconstructing masked contact details.

Risk: Automatic account registration collects device features and persists an API key locally.

Mitigation: Review and consent to registration first; prefer a user-supplied API key through the platform's secret mechanism where available and protect local credentials.

Risk: Some data requests consume account credits, and the integration can provide recharge links.

Mitigation: Check account terms and request costs; avoid unrequested follow-up searches or pagination and confirm before purchasing credits.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/liu-jiapeng/skills/tender-express-search-bidizhaobiao)
- [Provider skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Business registry API reference](artifact/references/api-registry.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Registration and credential setup](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and result tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include publication dates and budgets; contact details may be masked by account tier.]

## Skill Version(s):

2.0.6 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
