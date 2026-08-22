## Description:

Choose a notification cadence and deduplication key for an operations update stream.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations, support, and communications teams use this skill to turn a cadence_request into a recurring update delivery rule that reduces repetitive messages while preserving time-sensitive items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A downstream composer or scheduler may send messages based on cadence_mode without its own controls.

Mitigation: Verify downstream composer and scheduler controls before using cadence_mode to send notifications.

Risk: A weak deduplication key can hide distinct events or allow repeated messages.

Mitigation: Use a stable event or case identifier, avoid free-form message text as the deduplication key, and state the cutoff for late items.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/notification-cadence-guidance-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Short string in cadence_mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cadence, local delivery hour, timezone, grouping field, deduplication key, and any urgent exception; sends no notification itself.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
