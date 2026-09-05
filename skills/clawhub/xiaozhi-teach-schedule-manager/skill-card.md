## Description:

帮助独立教师生成周课表、检查老师和学员时间冲突，并在老师确认后维护课表与课时包台账。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to turn availability, lesson events, makeup requests, reschedules, and course-package balances into a visible weekly schedule and lesson-hour ledger. The workflow produces scheduling suggestions and records only after teacher confirmation.

### Deployment Geography for Use:

China mainland by default; deployments in other regions require localization of K12 assumptions, safety contacts, and applicable minor-data rules.

## Known Risks and Mitigations:

Risk: The bundled workspace schema exposes broader lesson-log data than the scheduling workflow needs.

Mitigation: Deploy with field-level access limited to the exact scheduling fields, or remove lessonLogs unless the platform enforces the documented scope.

Risk: Scheduling or course-hour proposals may be wrong if they are written before teacher review or based on stale availability.

Mitigation: Require teacher confirmation before writing lessonSchedule entries, registering makeup or reschedule records, or acting on remaining-hour warnings.

Risk: The skill operates around K12 student scheduling records and may encounter sensitive minor data.

Mitigation: Use aliases, avoid real names and contact or family details, respect consent controls, and localize China-specific safety contacts before use outside China mainland.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [Publisher profile: qizhitang](https://clawhub.ai/user/qizhitang)
- [Weekly schedule and course-hour ledger template](artifact/references/weekly-schedule-template.md)
- [Leave, makeup, and reschedule forms](artifact/references/leave-makeup-reschedule-forms.md)
- [Solo teacher workspace schema](artifact/shared/solo-teacher-workspace.schema.json)
- [Platform conventions and localization guidance](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured schedule, conflict-check, makeup/reschedule, and course-package ledger entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires teacher confirmation before schedule writes, makeup/reschedule records, or course-hour ledger changes.]

## Skill Version(s):

2.1.6 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
