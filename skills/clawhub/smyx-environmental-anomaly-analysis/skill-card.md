## Description:

Combines livestock behavior in continuous barn videos with environmental sensor data such as temperature, humidity, and ammonia to identify group stress responses caused by abnormal in-barn conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, livestock technicians, and agents use this skill to correlate barn video with environmental sensor data and produce anomaly reports for group stress monitoring. It can also retrieve cloud-hosted historical reports for the same workspace identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn media, sensor data, and historical report queries are processed by a remote service.

Mitigation: Use the skill only with data approved for remote processing and confirm retention and deletion expectations before handling sensitive operational records.

Risk: The skill may automatically create or reuse a local workspace identity.

Mitigation: Prefer explicit account setup and review the workspace identity state before use in shared or regulated environments.

Risk: Authentication tokens may be stored in a local SQLite database.

Mitigation: Apply local token storage controls, restrict workspace access, and clear stored credentials when the skill is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-environmental-anomaly-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Environmental anomaly API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report export links and historical report listings.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
