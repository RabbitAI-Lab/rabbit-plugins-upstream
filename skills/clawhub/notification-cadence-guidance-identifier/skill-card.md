## Description:

Choose a notification cadence and deduplication key for an operations update stream.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams use this skill to choose a digest schedule, grouping field, and deduplication key for recurring updates. It produces guidance for a later notification step rather than sending notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cadence guidance may default to UTC or leave requested cutoff and urgent-item rules unspecified.

Mitigation: Review the resulting schedule, timezone, cutoff, and urgent exceptions against the team's requirements before use.

## Reference(s):

- [Notification Cadence Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/notification-cadence-guidance-identifier)
- [wxt-ai publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [JSON object containing a cadence_mode string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local formatting only; does not send notifications or persist an artifact.]

## Skill Version(s):

1.1.0 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
