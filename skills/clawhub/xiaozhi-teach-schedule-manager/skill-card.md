## Description:

把独立教师凭记忆排课的流程转成可见的周课表、冲突检测、补课调课建议和课时包台账。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to plan weekly lessons, detect teacher or student time conflicts, manage leave or makeup scheduling, and track lesson-package balances. It is intended to produce draft scheduling and ledger updates that teachers review before records are written.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Schedule or lesson-package records may be changed without adequate teacher review.

Mitigation: Use the skill only in workflows where the teacher confirms draft schedule, makeup, leave, and ledger changes before they are written.

Risk: Student privacy may be weakened if real identities, family details, contact information, or school/class details are entered into scheduling records.

Mitigation: Keep scheduling records limited to aliases, availability time windows, lesson events, and lesson-package quantities.

Risk: Financial handling could be confused with lesson-package tracking.

Mitigation: Keep amounts, prices, payments, arrears, refunds, and compensation outside this skill and use a separate accounting process.

Risk: Missing consent or data-control review could make the shared workspace unsuitable for deployment.

Mitigation: Review consent and data-control settings before installation and make sure teachers understand what workspace records the skill reads and writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [weekly-schedule-template.md](artifact/references/weekly-schedule-template.md)
- [leave-makeup-reschedule-forms.md](artifact/references/leave-makeup-reschedule-forms.md)
- [solo-teacher-workspace.schema.json](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese-language Markdown guidance, schedule tables, conflict reports, and workspace record proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires teacher confirmation before schedule writes; avoids lesson-content records, financial details, and parent-message drafting.]

## Skill Version(s):

2.2.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
