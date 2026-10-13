## Description:

Analyzes construction tender and award records, including project amounts, winning bidders, company qualifications, and past performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Construction procurement teams and analysts use this skill to search tender notices, compare project awards, and summarize winning companies and market activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: If no API key is configured, trial registration sends a hashed device identifier to the provider and stores the returned key locally.

Mitigation: Require informed consent before registration; configure an API key manually to avoid device-based trial registration.

Risk: The skill uses a third-party service API and may lead users to account or payment links.

Mitigation: Review the service and account links before use, and limit access to the API key and locally stored credentials.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pkuycl/skills/construction-tender-analyzer-jianshetong)
- [Service API](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Account registration guidance](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tender and award summaries with project amounts, winning bidders, company details, and links to available records.]

## Skill Version(s):

1.0.8 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
