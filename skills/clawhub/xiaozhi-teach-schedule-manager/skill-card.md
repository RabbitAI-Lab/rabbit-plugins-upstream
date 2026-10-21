## Description:

帮助独立教师生成周课表、检查时间冲突，并管理课时包台账与补课调课安排。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking independent K–12 teachers use this skill to draft and confirm weekly lessons, identify scheduling conflicts, handle leave and makeup lessons, and track remaining lesson units and expiry dates.

### Deployment Geography for Use:

Mainland China; localize language, crisis resources, school-calendar assumptions, and compliance rules before use elsewhere.

## Known Risks and Mitigations:

Risk: A mistaken schedule change could affect a teacher or student.

Mitigation: Check registered availability and conflicts, then require teacher confirmation before writing the schedule.

Risk: Schedule and lesson-unit records persist in a shared teacher workspace.

Mitigation: Use student aliases and registered time windows only; respect consent and access controls for shared records.

Risk: Mainland China-specific language, crisis resources, school calendars, and compliance assumptions may not fit another location.

Mitigation: Use for the intended Mainland China K–12 workflow or localize these assumptions before deployment elsewhere.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [Weekly schedule template](references/weekly-schedule-template.md)
- [Leave, makeup, and rescheduling forms](references/leave-makeup-reschedule-forms.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown schedules and conflict reports; structured lesson schedules and lesson-unit ledger records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher confirmation is required before schedule changes; the skill does not deduct lesson units or handle payments.]

## Skill Version(s):

2.11.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
