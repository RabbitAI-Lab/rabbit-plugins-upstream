## Description:

Analyzes plant images or videos to identify growth stages and provide structured reports for agricultural decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Agricultural producers and advisers use plant images or videos to identify growth stages, review analysis reports, and inform crop-management decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or supplied URLs are sent to the lifeemergence cloud service for analysis.

Mitigation: Submit only media and URLs approved for sharing with that service.

Risk: The skill silently creates or reuses a local identity and persists tokens, linking analyses and report history.

Mitigation: Review and clear the workspace data database and tokens if persistent identity or report linkage is unwanted.

## Reference(s):

- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis reports and Markdown history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include growth-stage findings, recommendations, and report links.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release; bundled SKILL.md lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
