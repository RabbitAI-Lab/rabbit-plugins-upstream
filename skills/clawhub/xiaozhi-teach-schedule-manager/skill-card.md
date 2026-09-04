## Description:

A Chinese-language agent skill that helps independent teachers turn student availability into weekly schedules, check teacher and student time conflicts, and maintain course-hour ledgers with teacher confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to draft weekly lesson schedules, handle leave, makeup, and rescheduling workflows, and track course-hour package status from pseudonymous student availability and ledger records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may store or read student availability, lesson schedules, and course-hour counts.

Mitigation: Use pseudonymous student aliases, store only scheduling windows and course-hour quantities, and avoid real names, family details, contact information, school/class details, and payment data.

Risk: Unconfirmed schedule or ledger changes could create conflicts or inaccurate course-hour records.

Mitigation: Require teacher confirmation before writing schedule changes, report teacher and student availability conflicts, and leave actual lesson-unit consumption to teacher-confirmed lesson-log workflows.

Risk: The bundled crisis support references are tailored to mainland China.

Mitigation: Users outside mainland China should adapt emergency contacts and professional support channels to their local resources before relying on the guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [weekly-schedule-template.md](references/weekly-schedule-template.md)
- [leave-makeup-reschedule-forms.md](references/leave-makeup-reschedule-forms.md)
- [platform-conventions.md](shared/platform-conventions.md)
- [crisis-referral-protocol.md](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown schedule views, conflict reports, leave/makeup/reschedule forms, and teacher-confirmed schedule and course-hour ledger entries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses pseudonymous student records and requires teacher confirmation before writing schedule or ledger changes.]

## Skill Version(s):

2.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
