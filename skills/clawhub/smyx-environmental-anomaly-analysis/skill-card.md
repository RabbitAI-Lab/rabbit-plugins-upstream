## Description:

Combines livestock behavior in continuous barn videos with environmental sensor data such as temperature, humidity, and ammonia to identify group stress responses caused by abnormal in-barn conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, livestock facility teams, and agricultural monitoring developers use this skill to correlate barn camera footage with environmental sensor readings, identify likely environment-linked group stress, and retrieve historical anomaly reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn media, URLs, sensor data, and account-linked report history may be sent to or retrieved from remote services.

Mitigation: Review the publisher, endpoint configuration, and data handling requirements before installation; avoid sensitive footage or real credentials unless the deployment has approved production HTTPS endpoints and documented account controls.

Risk: The skill silently creates or reuses an internal identity and can store remote tokens locally.

Mitigation: Require review of the identity flow and local token storage before operational use, and confirm credentials are protected according to the deployment environment's security policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-environmental-anomaly-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Environmental Anomaly API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [markdown, json, shell commands, guidance]

**Output Format:** [Markdown reports and JSON analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes behavior-environment correlation findings, stress level labels, report links, and historical report tables.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
