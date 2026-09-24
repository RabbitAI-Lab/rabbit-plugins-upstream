## Description:

排课与课时管理 helps independent teachers turn memory-based scheduling into visible weekly lesson schedules, conflict checks, and course-hour ledgers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to draft and confirm weekly schedules, detect teacher and student time conflicts, manage leave/makeup/reschedule workflows, and track course-hour package status. It keeps parent communication, lesson-hour deduction, and financial handling outside this skill's scope.

### Deployment Geography for Use:

Global, with locale review recommended for use outside China-mainland Chinese teaching workflows.

## Known Risks and Mitigations:

Risk: The skill handles student aliases, availability, schedule entries, and course-hour counts, which can become sensitive if mixed with real names, contact details, family reasons, or financial data.

Mitigation: Use aliases and time availability only, keep parent communication and money/refund handling outside this skill, and follow the evidence security guidance to avoid storing real names, contact details, family reasons, or financial details.

Risk: Schedule proposals or makeup/reschedule suggestions could be written before all parties have confirmed them.

Mitigation: Treat outputs as teacher-facing proposals and require teacher confirmation before writing lessonSchedule entries or course-package ledger updates.

Risk: The workflow is designed for China-mainland Chinese K12 independent-teacher use and may not fit other locales without review.

Mitigation: Review locale, language, emergency-contact, and education-practice assumptions before deploying outside the intended Chinese teaching workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [周课表与课时台账模板](references/weekly-schedule-template.md)
- [请假/补课/调课登记模板](references/leave-makeup-reschedule-forms.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured text with schedule tables, conflict checks, confirmation prompts, and workspace field guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces teacher-facing proposals; schedule writes and course-hour ledger changes require teacher confirmation.]

## Skill Version(s):

2.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
