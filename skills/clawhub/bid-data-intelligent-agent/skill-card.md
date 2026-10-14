## Description:

Helps agents search and analyze Chinese procurement notices, company records, market trends, and historical award prices through the 知了标讯 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can find tender and award notices, review company procurement activity, identify buyers and suppliers, and summarize market or pricing trends using the service's data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration can send a hashed device-derived identifier to an external service and create an account.

Mitigation: Require informed user consent before registration; supply an existing ZLBX_API_KEY if automatic registration is not wanted.

Risk: Credentialed requests reach zhiliaobiaoxun.com, and automatic setup can store an API key locally.

Mitigation: Use a trusted secret mechanism for ZLBX_API_KEY, limit access to the local credential file, and approve external requests before use.

Risk: Operational instructions in HTML comments may be missed during review.

Mitigation: Review the complete skill source, including comments, before deployment.

Risk: Optional extra or repeated data queries may consume paid API credits.

Mitigation: Request only necessary endpoints and pages, and confirm scope before additional billable lookups.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/bid-data-intelligent-agent)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](artifact/references/api-search.md)
- [Company API reference](artifact/references/api-company.md)
- [Market API reference](artifact/references/api-market.md)
- [Registration and credential setup](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Natural-language answers, tables, and structured reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested API queries and available service data.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
