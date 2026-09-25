## Description:

经学生或监护人同意后，汇总学习复习和任务提醒，按学段作息安排每日提醒，并提供暂停、删除及共享控制。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese K–12 students and their guardians use this skill to schedule and manage consent-based study reviews, error rechecks, and learning-task reminders. It combines due items into a daily summary rather than sending unsolicited messages.

### Deployment Geography for Use:

Chinese K–12 context; localize emergency resources, school-level assumptions, and consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: Unwanted reminders or disclosure of a minor's study information across skills.

Mitigation: Require explicit reminder and sharing consent; share only necessary fields and offer pause, deletion, export, and sharing controls.

Risk: Incorrectly timed or excessive reminders when platform scheduling is unavailable or the student is in quiet hours.

Mitigation: Respect age-based quiet hours and daily limits; without scheduling, disclose the limitation and offer reminders when the student returns to the conversation.

Risk: Emergency or child-safety guidance may be unsuitable outside the Chinese K–12 context.

Mitigation: Localize emergency resources, school-level assumptions, and minor-consent rules before deployment elsewhere; use the crisis referral guidance when safety concerns arise.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Spaced review schedule](references/ebbinghaus-schedule.md)
- [Age-based reminder and quiet-hour guidance](shared/grade-bands.md)
- [Reminder handover protocol](shared/handover-protocol.schema.json)
- [Crisis referral guidance](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language chat messages and text reminder summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consent-gated reminders, daily message limits, quiet hours, and text export of the reminder queue.]

## Skill Version(s):

2.4.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
