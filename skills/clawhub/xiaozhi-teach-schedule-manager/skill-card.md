## Description:

帮助独立教师生成周课表、检测老师和学员时间冲突、维护课时包台账，并以老师确认为前提处理补课、请假和调课流程。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to make scheduling and lesson-hour management visible and traceable. It supports weekly schedule drafts, conflict checks, make-up or leave workflows, and course-package ledger reminders without handling lesson notes, financial records, refunds, or parent messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workspace schema appears broader than the skill's stated lesson-ledger write boundaries.

Mitigation: Enforce field-level ledger permissions and reject writes from this skill to usedUnits, remainingUnits, or pendingConfirmations.

Risk: Consent checks may be missing from the included workspace schema for profile creation, parent communication handoffs, or cross-skill sharing.

Mitigation: Treat missing consent fields as fail-closed and require review before installing in a real teacher workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [Weekly schedule and lesson-hour ledger template](references/weekly-schedule-template.md)
- [Leave, make-up, and reschedule forms](references/leave-makeup-reschedule-forms.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)
- [Platform conventions](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese conversational guidance, Markdown schedule tables, ledger summaries, conflict reports, and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires teacher confirmation before writing schedule or ledger entries; uses student aliases and excludes financial handling, lesson-note logging, and parent-message drafting.]

## Skill Version(s):

2.1.10 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
