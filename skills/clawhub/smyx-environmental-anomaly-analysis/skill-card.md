## Description:

Combines livestock behavior in continuous barn videos with environmental sensor data (temperature, humidity, ammonia, etc.) to identify group stress responses caused by abnormal in-barn conditions. | 结合畜禽行为与环境传感器，识别温湿度异常时的群体应激反应。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, animal welfare reviewers, and agricultural monitoring developers use this skill to correlate livestock group behavior with barn sensor readings and produce environment-linked stress and anomaly reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn media or submitted URLs are sent to an external analysis service.

Mitigation: Review deployment data-flow and use the skill only with media and URLs approved for external processing.

Risk: The skill can query account-linked cloud history and stores identity and token data in a local SQLite database.

Mitigation: Deploy only where account linkage and local credential storage are acceptable, and require clear retention and deletion controls from the publisher.

Risk: Security evidence reports under-scoped remote services and private development HTTP endpoints.

Mitigation: Review service endpoints before installation and require the publisher to remove private development endpoints from release artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-environmental-anomaly-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Environmental anomaly API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Structured JSON or Markdown report text, including report links for history queries when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis output may include behavior features, environment correlations, stress level, and report export links.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
