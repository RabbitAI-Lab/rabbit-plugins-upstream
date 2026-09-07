## Description:

Helps independent teachers create weekly schedules, check teacher and student time conflicts, handle leave/makeup/reschedule requests, and maintain lesson-hour package ledgers with teacher confirmation before schedule writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent K12 teachers use this skill to plan weekly lessons, resolve time conflicts, track lesson-hour packages, and manage leave, makeup, and reschedule workflows. It is intended for Chinese-language solo-teacher operations where schedule changes and ledger updates remain subject to teacher confirmation.

### Deployment Geography for Use:

China mainland by default; localization review is needed before use in other regions.

## Known Risks and Mitigations:

Risk: The skill references consent checks for student data that the packaged schema does not let it read or enforce.

Mitigation: Install only where the platform supplies and enforces the required consent fields fail-closed, or keep cross-skill sharing and parent-facing processing disabled until consent can be verified.

Risk: Course-package and schedule edits can affect lesson entitlements even though this skill does not deduct used or remaining units.

Mitigation: Review schedule and course-package changes before applying them, and keep lesson-hour consumption under the separate lesson-log confirmation workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [Weekly schedule and lesson-hour ledger template](references/weekly-schedule-template.md)
- [Leave, makeup, and reschedule forms](references/leave-makeup-reschedule-forms.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)
- [Platform conventions and regional guidance](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured text for schedules, conflict checks, registration forms, and ledger guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires teacher confirmation before schedule writes; does not deduct lesson hours, process money, or contact parents directly.]

## Skill Version(s):

2.1.12 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
