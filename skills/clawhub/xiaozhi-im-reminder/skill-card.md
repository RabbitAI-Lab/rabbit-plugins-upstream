## Description:

Schedules and combines consented study reviews and tasks into a daily reminder for students.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking students and their guardians use this skill to opt into scheduled reviews, study tasks, and a consolidated daily reminder. Without consent, it suggests a reminder plan rather than creating reminders.

### Deployment Geography for Use:

Mainland China; use elsewhere requires localization of curriculum, crisis resources, and minor-consent rules.

## Known Risks and Mitigations:

Risk: Unwanted reminders or sharing of a minor's learning information.

Mitigation: Require explicit student or guardian consent, limit cross-skill sharing to necessary information, and honor pause, deletion, and quiet-hour controls.

Risk: Mainland China-specific crisis resources and minor-consent assumptions may be inappropriate elsewhere.

Mitigation: Localize help resources, curriculum, language, and consent requirements before use outside Mainland China.

Risk: Reminders may not arrive when the platform lacks scheduled notifications.

Mitigation: Explain the limitation and offer reminders when the student next opens a conversation or suggest a phone reminder.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Spaced review schedule](references/ebbinghaus-schedule.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Chinese-language reminder messages and queue summaries; structured reminder handoffs where supported]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normally one combined daily summary and at most one immediate reminder, subject to consent and quiet hours.]

## Skill Version(s):

2.6.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
