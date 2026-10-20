## Description:

Correlates livestock behavior in barn videos with environmental sensor readings to identify possible group stress responses to abnormal conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock operators and farm analysts use the skill to identify potential environmental stress in barn footage, correlate it with sensor data, and review cloud-hosted analysis reports. Results support monitoring rather than equipment-control decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn media, sensor data, or supplied URLs are sent to the lifeemergence.com service.

Mitigation: Install only if the service is trusted for these inputs; confirm its retention and cleanup practices before sending sensitive data.

Risk: The skill may create or reuse identity records and persist authentication tokens locally without clear disclosure.

Mitigation: Review account creation, local token storage, access controls, and removal procedures before installation.

Risk: Historical report queries can expose identity-linked cloud history.

Mitigation: Require user confirmation before querying history and limit access to authorized users.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-environmental-anomaly-analysis)
- [API interface documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured analysis results or JSON; historical reports as Markdown tables with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes observed behavior, associated environmental indicators, and group stress levels; results are advisory.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
