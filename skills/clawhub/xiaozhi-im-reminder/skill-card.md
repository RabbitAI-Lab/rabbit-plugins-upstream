## Description:

Schedules and combines consented study-review and task reminders into a daily summary for Chinese-speaking students.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking K–12 students and their caregivers use this skill to schedule and manage opted-in review, practice, and learning-task reminders. It combines due items into a daily digest and offers controls to view, change, pause, or delete reminders.

### Deployment Geography for Use:

Mainland China; localize school stages, consent, quiet hours, and crisis contacts before use elsewhere.

## Known Risks and Mitigations:

Risk: Unsolicited or excessive reminders may disrupt students.

Mitigation: Require explicit student or guardian consent, respect school-stage quiet hours and daily limits, and provide pause and deletion controls.

Risk: Sharing students' learning details across skills may expose more data than needed.

Mitigation: Share only the minimum reminder details when cross-skill sharing is authorized; do not expose a full learning profile.

Risk: Mainland-China school, consent, and crisis-contact defaults may be inappropriate elsewhere.

Mitigation: Before deployment outside mainland China, localize school-stage assumptions, consent requirements, quiet hours, and crisis-help contacts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Spaced-review schedule](references/ebbinghaus-schedule.md)
- [School-stage quiet hours](shared/grade-bands.md)
- [Crisis-response guidance](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Chinese-language reminder messages and text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scheduled delivery requires platform timer support; without it, due items can be summarized when the student next starts a conversation.]

## Skill Version(s):

2.8.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
