## Description:

Helps independent teachers prepare weekly schedules, check availability and conflicts, and maintain lesson-package counts and expiry details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to draft weekly lesson schedules, find teacher or student availability conflicts, handle leave and makeup proposals, and review lesson-package balances. Teachers confirm schedule changes before they are written.

### Deployment Geography for Use:

China mainland

## Known Risks and Mitigations:

Risk: Student schedule and lesson-package records can expose personal information.

Mitigation: Use aliases and limit records to the scheduling details needed; omit family reasons and identifying details.

Risk: The security baseline is missing and the bundled schema lacks consent fields.

Mitigation: Before storing student records, verify the host's consent, sharing, and deletion controls.

Risk: A proposed schedule change may be incorrect or conflict with availability or timing constraints.

Mitigation: Review conflicts and applicable timing limits, then confirm each change before writing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [Weekly schedule and lesson-package templates](artifact/references/weekly-schedule-template.md)
- [Leave, makeup, and reschedule forms](artifact/references/leave-makeup-reschedule-forms.md)
- [Off-campus training guidance](artifact/shared/off-campus-training.md)
- [Grade-band timing guidance](artifact/shared/grade-bands.md)
- [Workspace data schema](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Scheduling guidance]

**Output Format:** [Chinese-language schedule drafts, conflict summaries, lesson-package status, and structured workspace records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses student aliases; schedule changes and ledger updates require teacher confirmation.]

## Skill Version(s):

2.12.6 (source: server-resolved release; artifact frontmatter agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
