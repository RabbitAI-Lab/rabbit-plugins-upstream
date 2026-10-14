## Description:

Helps users analyze Chinese tender and award records, companies, competitors, purchasing trends, and potential bidding opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, suppliers, and market analysts use the skill to search Chinese procurement notices, review company bidding histories, identify potential suppliers and competitors, and summarize market opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional account registration collects device-derived identifiers and creates a vendor account.

Mitigation: Preconfigure ZLBX_API_KEY through a trusted secret mechanism, or require explicit consent before registration and device-feature collection.

Risk: Automatic registration persists an API key in a home-directory configuration file.

Mitigation: Prefer a managed secret for the API key and review local credential storage before enabling automatic registration.

Risk: Account-related requests may occur in addition to the requested tender analysis.

Mitigation: Review the account workflow and authorize only the requests needed for the task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/ai-tender-bid-analyst)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Business registry API reference](references/api-registry.md)
- [Account API reference](references/api-account.md)
- [Optional account registration workflow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports query filters, record counts, and monetary units; available contact details depend on account access.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
