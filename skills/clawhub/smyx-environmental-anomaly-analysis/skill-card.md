## Description:

Combines livestock behavior in continuous barn videos with environmental sensor data (temperature, humidity, ammonia, etc.) to identify group stress responses caused by abnormal in-barn conditions. | 结合畜禽行为与环境传感器，识别温湿度异常时的群体应激反应。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock facility operators and their technical teams can use the skill to relate barn video behavior to temperature, humidity, ammonia, and other sensor readings, identify possible group stress responses, and retrieve prior analysis reports. The results support monitoring and inspection; they do not provide equipment control instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically enrolls accounts and stores credentials.

Mitigation: Review account enrollment and credential retention before use, and use a dedicated workspace and provider identity.

Risk: The --export-env-only option may still upload footage.

Mitigation: Do not rely on this option to prevent uploads; request a fix before using it for that purpose and review footage handling before submitting sensitive material.

Risk: The skill may suggest installing a separate payment skill.

Mitigation: Independently review and approve any suggested payment-skill installation.

## Reference(s):

- [API interface notes](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis reports, Markdown, JSON, Report links]

**Output Format:** [Structured analysis report; historical report lists are formatted as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports summarize observed behavior, environmental correlations, and a stress level. Results are for monitoring reference and contain no equipment control instructions.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
