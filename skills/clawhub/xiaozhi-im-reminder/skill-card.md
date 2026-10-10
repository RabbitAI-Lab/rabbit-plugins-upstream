## Description:

Schedules and combines student-approved study reviews and task reminders into a daily message, with controls to pause or cancel reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students use this skill to receive consent-based reminders for reviews, practice questions, and planned learning tasks. Guardians and educators should oversee use by younger students.

### Deployment Geography for Use:

Mainland China (default; localize crisis resources before use elsewhere)

## Known Risks and Mitigations:

Risk: Younger students may enable persistent reminders without verifiable guardian consent.

Mitigation: Require the platform to verify guardian consent for elementary and younger junior-high users before scheduling reminders or accepting reminder handovers; do not rely on a boolean consent flag alone.

Risk: Cross-skill reminders may expose a student's learning data beyond the intended task.

Mitigation: Require explicit permission for each sharing purpose, pass only the minimum necessary fields, and provide controls to pause, cancel, and disable sharing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Spaced review schedule](references/ebbinghaus-schedule.md)
- [Grade-specific reminder windows](shared/grade-bands.md)
- [Reminder handover schema](shared/handover-protocol.schema.json)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational reminders and daily queue summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Without consent, offers a suggested reminder plan instead of scheduling messages.]

## Skill Version(s):

2.11.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
