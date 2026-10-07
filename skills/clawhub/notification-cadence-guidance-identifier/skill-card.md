## Description:

Choose a notification cadence and deduplication key for an operations update stream.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams and their agents use this skill to choose a digest cadence and deduplication key for recurring updates before composing notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsupported timezone names can fall back to UTC, yielding a delivery hour different from the intended local time.

Mitigation: Check the returned timezone and local delivery hour before applying the cadence to a notification workflow.

## Reference(s):

- [Notification Cadence Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/notification-cadence-guidance-identifier)
- [wxt-ai publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object with a cadence_mode string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes a digest cadence and deduplication rule; does not send notifications.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
