## Description:

Combines livestock behavior in continuous barn videos with environmental sensor data (temperature, humidity, ammonia, etc.) to identify group stress responses caused by abnormal in-barn conditions. | 结合畜禽行为与环境传感器，识别温湿度异常时的群体应激反应。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and livestock operations teams use this skill to analyze barn images, video, optional sensor data, and historical reports for environment-linked group stress signals. It produces structured findings on behavior features, environmental correlations, stress level, and report links for pre-alert monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn media, sensor files, and public video URLs may be sent to external lifeemergence.com/open.lifeemergence.com services.

Mitigation: Install only where that transfer is acceptable, and avoid sensitive media or sensor files unless the deployment owner has approved the data flow.

Risk: The skill can create or reuse a local identity, store authentication tokens in a workspace SQLite database, and query cloud report history.

Mitigation: Use a non-sensitive workspace, review local state retention expectations, and clear the local data directory when retained state is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-environmental-anomaly-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Environmental anomaly API documentation](references/api_doc.md)
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports, with optional shell commands and saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior feature lists, environment correlation results, stress level, historical report tables, and report links.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
