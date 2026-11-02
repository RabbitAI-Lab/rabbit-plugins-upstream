## Description:

Schedules, combines, and sends consent-based study reminders for review and learning tasks when a student explicitly asks to manage reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students use this skill to set, review, pause, and manage consent-based study reminders, including combined daily summaries. Elementary-school users need an accompanying adult.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expect scheduling-only behavior despite occasional practice questions.

Mitigation: Set expectations about reminder content before enabling the skill.

Risk: The host may not support scheduled messages or persistent storage.

Mitigation: Confirm host support before enabling reminders; use the documented session-entry fallback when scheduling is unavailable.

Risk: Reminder sharing and timing require user permission and clear boundaries.

Mitigation: Choose reminder times and sharing permissions before enabling reminders, and retain the available pause and cancellation controls.

Risk: Elementary-school use requires adult accompaniment.

Mitigation: Ensure a parent or teacher is present during use.

## Reference(s):

- [Ebbinghaus review schedule](references/ebbinghaus-schedule.md)
- [Reminder handover protocol schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Conversational reminder plans and messages, plus structured reminder handoff data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reminder content is concise and governed by user consent and notification limits.]

## Skill Version(s):

2.12.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
