## Description:

帮助独立教师生成周课表、检查排课冲突，并在教师确认后维护课表与课时包台账。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

独立教师用它根据学员可上课时段编排周课表、处理请假与补课建议，并查看课时包剩余量和到期提醒；课表变更须由教师确认。

### Deployment Geography for Use:

Mainland China; localize crisis contacts and minor-consent requirements before use elsewhere.

## Known Risks and Mitigations:

Risk: Scheduling errors or unintended schedule changes

Mitigation: Check teacher and student availability, then obtain teacher confirmation before changing the schedule.

Risk: Misleading remaining lesson hours when entries await confirmation

Mitigation: Show pending confirmations alongside the balance and leave lesson-hour deductions to the separate post-lesson workflow.

Risk: Disclosure of minors' personal or scheduling information

Mitigation: Use student aliases and authorized availability only, confirm sharing consent, and adapt minor-consent rules to the deployment location.

Risk: Incorrect crisis referral information outside mainland China

Mitigation: Localize emergency contacts before deployment and confirm the user's location when it is unknown.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [Weekly schedule and lesson-hour templates](references/weekly-schedule-template.md)
- [Leave, makeup, and rescheduling forms](references/leave-makeup-reschedule-forms.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language weekly schedules, conflict reports, and lesson-hour summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Schedule and ledger updates require teacher confirmation; no payment handling or lesson-hour deduction.]

## Skill Version(s):

2.8.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
