## Description:

Schedules and combines consented study-review and task reminders into a daily message for Chinese-speaking K–12 students.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking K–12 students and their guardians use this skill to request, view, pause, and manage study reminders. With consent, it combines due reviews and learning tasks into a daily summary instead of sending reminders automatically.

### Deployment Geography for Use:

Mainland China by default; localize emergency-contact guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: Unwanted reminders or sharing of a minor's learning information.

Mitigation: Confirm the platform enforces reminder and cross-skill sharing consent, plus pause, delete, and export controls, before enabling scheduling.

Risk: Mainland China emergency-contact guidance may be inappropriate in other regions.

Mitigation: Use only in the intended Chinese K–12 setting or localize crisis referrals and emergency contacts before deployment elsewhere.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Spaced-review schedule](references/ebbinghaus-schedule.md)
- [Reminder handover protocol](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language reminder messages, daily summaries, and text queue exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [At most one merged daily summary and one immediate reminder by default; users can pause or delete reminders.]

## Skill Version(s):

2.7.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
