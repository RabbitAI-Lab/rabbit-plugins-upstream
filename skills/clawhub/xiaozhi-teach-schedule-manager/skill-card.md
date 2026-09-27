## Description:

帮助独立教师生成周课表、检查师生时间冲突，并在教师确认后维护排课与课时包台账。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to draft weekly class schedules, check availability and conflicts, arrange leave or make-up lessons, and track lesson-package balances and expiry dates. Scheduling changes require teacher confirmation; lesson deductions and financial transactions are outside its scope.

### Deployment Geography for Use:

Mainland China; adapt language, curriculum, consent rules, and crisis-help channels before use elsewhere.

## Known Risks and Mitigations:

Risk: Incorrect availability or unconfirmed schedule changes could cause double-booking.

Mitigation: Check teacher and student time conflicts and obtain teacher confirmation before writing schedules.

Risk: Schedule and lesson-package records may expose student information or be retained against user preferences.

Mitigation: Use student aliases, check consent before sharing or saving, and honor delete, pause, and sharing controls.

Risk: Chinese-language, curriculum, consent, and crisis-help assumptions may not fit other regions.

Mitigation: Localize these elements before use outside Mainland China.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [Weekly schedule and lesson-package templates](references/weekly-schedule-template.md)
- [Leave, make-up lesson, and rescheduling forms](references/leave-makeup-reschedule-forms.md)

## Skill Output:

**Output Type(s):** [Scheduling guidance, Markdown, Text]

**Output Format:** [Text or Markdown schedules, conflict reports, rescheduling options, and lesson-package summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposed schedule changes await teacher confirmation; no automatic lesson deductions or financial advice.]

## Skill Version(s):

2.7.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
