## Description:

Queries and analyzes Chinese healthcare tender and award notices, project opportunities, supplier records, and procurement trends through Zhiliaobiaoxun.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, bidders, and market analysts use this skill to find healthcare tenders, track project stages, research suppliers and company records, and summarize award prices and market activity. Healthcare is the default search focus, but user-specified industries and regions take precedence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentialed queries send tender and company search terms to Zhiliaobiaoxun, including possible background calls.

Mitigation: Use this skill only when sharing the queries and API key with that service is acceptable; review requested searches and configure ZLBX_API_KEY deliberately.

Risk: Auto-registration sends platform, CPU architecture, and a hashed MAC-derived identifier and saves an API key in ~/.zlbx/config.json.

Mitigation: Require informed consent before auto-registration; configure ZLBX_API_KEY manually to avoid device registration, and protect the saved credential.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-medical)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Zhiliaobiaoxun homepage](https://ai.zhiliaobiaoxun.com/?ch=s154)
- [Tender search API reference](artifact/references/api-search.md)
- [Company registry API reference](artifact/references/api-registry.md)
- [Auto-registration and credential setup](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports applied search filters; source results and account credit balance depend on the external service.]

## Skill Version(s):

1.0.4 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
