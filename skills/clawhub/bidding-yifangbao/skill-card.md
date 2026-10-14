## Description:

Helps bidders search tender and award notices, assess competitors and suppliers, and summarize pricing and market trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Bidders and procurement analysts use this skill to find Chinese tender opportunities, review company bidding records, compare competitors, and assess historical award prices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bid queries, company and contact lookups, and account information are sent to the Zhiliaobiaoxun service.

Mitigation: Review the information to be shared before querying, and avoid submitting sensitive data without authorization.

Risk: Optional auto-registration can send a hashed device identifier and save an API key locally.

Mitigation: Prefer a manually configured API key; use auto-registration only after informed consent and protect any stored key.

Risk: Some credentialed request and acknowledgement directions are embedded in source comments.

Mitigation: Review the skill before installation and confirm credentialed actions and user-visible notices before enabling them.

Risk: Company registry lookups can consume paid credits.

Mitigation: Query only requested records and pages, and check the applicable credit cost before paid lookups.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/liu-jiapeng/skills/bidding-yifangbao)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Company registry API reference](references/api-registry.md)
- [Account API reference](references/api-account.md)
- [Optional registration flow](references/auto-register.md)
- [Skill setup documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown tables and concise narrative findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available service records; trial-account contact numbers may be masked.]

## Skill Version(s):

2.0.6 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
