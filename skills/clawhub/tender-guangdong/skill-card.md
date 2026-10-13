## Description:

Helps users search and analyze procurement notices, companies, suppliers, and pricing, with Guangdong as the default search region unless the user chooses another scope.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and bidding professionals use this skill to find tender and award notices, track project stages, research companies and suppliers, and assess markets and historical prices. Guangdong is the default query scope, not a restriction.

### Deployment Geography for Use:

Global; Guangdong, China is the default search region, but users can request another region.

## Known Risks and Mitigations:

Risk: Optional account registration transmits platform, CPU architecture, and a hashed MAC address for trial-account de-duplication.

Mitigation: Request explicit consent before registration or device-data collection; offer manual sign-up instead.

Risk: The service may create or read an API key and store it locally.

Mitigation: Confirm the user is comfortable with local key storage and keep the key private.

Risk: Company-group searches or amount filters may produce misleading conclusions if query scope or units are misunderstood.

Mitigation: State the applied search scope and check monetary units before relying on results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-guangdong)
- [Product documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Company registry API reference](references/api-registry.md)
- [Optional registration and privacy details](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown with linked search results and summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [States the actual search scope and units; availability and contact detail depend on account access.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
