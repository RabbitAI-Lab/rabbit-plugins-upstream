## Description:

Helps independent teachers draft weekly lesson schedules, check time conflicts, and track lesson-package balances and expiration dates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers in Chinese-language K–12 tutoring use this skill to prepare weekly timetables, review availability conflicts, manage absence and makeup requests, and monitor remaining lesson units. Schedule changes require teacher confirmation; lesson consumption and financial transactions are handled separately.

### Deployment Geography for Use:

Mainland China (localize language, legal assumptions, and crisis-help information before use elsewhere)

## Known Risks and Mitigations:

Risk: Persistent schedule and lesson-hour records may contain sensitive information about minors.

Mitigation: Confirm record retention and sharing are acceptable; use aliases and keep real names and financial data out.

Risk: Scheduling or crisis guidance may be inappropriate outside the mainland-China K–12 setting.

Mitigation: Localize language, legal assumptions, and crisis-help channels before using the skill elsewhere.

Risk: Incorrect availability or unconfirmed changes could result in conflicting lessons.

Mitigation: Check teacher and student availability and require teacher confirmation before writing schedules.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [Weekly schedule and lesson-package templates](references/weekly-schedule-template.md)
- [Absence, makeup, and rescheduling forms](references/leave-makeup-reschedule-forms.md)
- [Workspace data schema](shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language schedules, conflict reports, lesson-unit summaries, and proposed changes for teacher approval]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Confirmed schedules and lesson-package records may be retained; the skill does not deduct lesson units or handle payments.]

## Skill Version(s):

2.11.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
