## Description:

Correlates livestock behavior in barn images or video with environmental sensor data to identify possible group stress responses to abnormal conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and livestock monitoring teams use the skill to review barn footage and sensor readings for environmental anomalies and associated group stress, or to retrieve cloud-stored analysis reports. Its findings support early warning and inspection, not equipment-control decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn media or supplied URLs are sent to the configured cloud analysis service.

Mitigation: Confirm the service and obtain approval before submitting barn media or URLs.

Risk: The skill automatically creates or reuses an identity and persists report identity and session tokens locally.

Mitigation: Review or clear the workspace data directory when persistent identity or tokens are not wanted.

Risk: History queries can expose account-linked cloud reports in shared environments.

Mitigation: Avoid broad history requests unless account-linked report access is intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-environmental-anomaly-analysis)
- [Skill API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include stress levels, environmental correlations, and cloud report links.]

## Skill Version(s):

1.0.12 (source: ClawHub release; bundled SKILL.md lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
