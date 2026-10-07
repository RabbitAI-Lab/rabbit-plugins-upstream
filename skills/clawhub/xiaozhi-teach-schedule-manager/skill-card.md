## Description:

帮助独立教师根据学员可上课时间生成周课表、发现排课冲突，并管理课时包与补课、请假和调课记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to draft weekly schedules, check availability conflicts, track remaining lesson units and expiry dates, and coordinate leave, makeup lessons, and rescheduling. Teachers confirm changes before they are saved.

### Deployment Geography for Use:

Mainland China as written; localize crisis contacts and consent guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: Incorrect availability or dates could produce conflicting lessons or inaccurate lesson-unit balances.

Mitigation: Check registered availability and pending lesson-unit confirmations, and require teacher approval before saving schedule changes.

Risk: Schedule and course-hour records could expose student or family information if shared or retained unnecessarily.

Mitigation: Use student aliases and availability windows only; obtain consent before profile persistence or sharing with other skills.

Risk: Mainland China crisis contacts and consent assumptions may not fit other regions.

Mitigation: Localize emergency contacts and consent guidance before using the skill outside Mainland China.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Weekly schedule template](artifact/references/weekly-schedule-template.md)
- [Leave, makeup, and rescheduling forms](artifact/references/leave-makeup-reschedule-forms.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown schedules, conflict reports, lesson-unit summaries, and proposed changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Schedule and ledger changes require teacher confirmation; financial transactions and post-lesson unit deductions are out of scope.]

## Skill Version(s):

2.10.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
