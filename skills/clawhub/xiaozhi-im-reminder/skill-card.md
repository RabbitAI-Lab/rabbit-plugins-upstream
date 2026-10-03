## Description:

在学生或监护人同意后，将复习和学习任务合并排期，发送适度的中文学习提醒。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking K–12 students and their guardians use this skill to schedule, combine, and manage consent-based study reminders for review and planned activities.

### Deployment Geography for Use:

Mainland China by default; deployment elsewhere requires localized crisis-support resources.

## Known Risks and Mitigations:

Risk: Unwanted reminders or inappropriate sharing of minors' study information.

Mitigation: Confirm reminder consent, cross-skill sharing, guardian visibility, quiet hours, and pause or deletion controls before activation.

Risk: Mainland-China crisis contacts may be unsuitable in other regions.

Mitigation: Localize crisis-support resources before deployment elsewhere and confirm the user's location before providing contact numbers.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Spaced-review schedule](references/ebbinghaus-schedule.md)
- [Grade-band quiet hours](shared/grade-bands.md)
- [Reminder handover schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Chinese-language reminder messages and queue summaries; structured reminder status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consent-gated scheduling, daily message limits, quiet hours, and pause or deletion controls.]

## Skill Version(s):

2.10.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
