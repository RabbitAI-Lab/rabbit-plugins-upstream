## Description:

Analyzes meal videos to assess eating habits and dietary patterns, then provides structured reports and nutrition suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing their eating habits can submit a meal video or URL for an assessment of eating speed, habits, and food choices, or retrieve earlier reports from the cloud service. Results are for general dietary guidance, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meal videos or video URLs are sent to an external cloud service for analysis.

Mitigation: Get consent before sending sensitive footage and review the service's retention and deletion terms.

Risk: The skill automatically creates or reuses an internal user identity and queries cloud report history.

Mitigation: Check account-recovery and history-access expectations before sharing a workspace or using personal reports.

Risk: Service tokens are stored in the local workspace.

Mitigation: Protect workspace access and avoid sharing stored credentials.

## Reference(s):

- [Diet analysis API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-diet-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured dietary analysis report or Markdown history table; JSON output is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links or save results to a file]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
