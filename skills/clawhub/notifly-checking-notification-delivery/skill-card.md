## Description:

Checks Notifly activity and subscriber channels to explain whether a notification was triggered and how it was delivered, skipped, or failed without sending anything.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Support staff and developers use this skill to investigate a subscriber's missing notification across email, SMS, push, chat, or in-app channels using Notifly activity records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Subscriber and delivery records may contain personal or internal information.

Mitigation: Share only details needed to explain delivery status and omit internal identifiers unless requested.

Risk: Checking the wrong authorized environment or too narrow an activity window can lead to a misleading absence of events.

Mitigation: Confirm the selected environment and page through relevant activity before concluding no event was triggered.

Risk: Triggering a workflow during troubleshooting could send an unintended notification.

Mitigation: Use read-only inspection tools only; do not trigger workflows to test delivery.

## Reference(s):

- [Notifly: Checking Notification Delivery on ClawHub](https://clawhub.ai/bsalaeddin/skills/notifly-checking-notification-delivery)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-language delivery status summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes trigger time, workflow, channel statuses, and relevant subscriber channel availability; does not send notifications.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
