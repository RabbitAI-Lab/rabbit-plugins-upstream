## Description:

为独立教师生成周课表、检查师生时间冲突，并维护课时包余额与到期信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

独立教师可用此技能安排、调整和补排课程，检查教师与学员的可用时间冲突，并查看课时包剩余量及到期提示。排课建议须经教师确认后才写入课表。

### Deployment Geography for Use:

中国大陆（须遵守适用的校外培训规定）

## Known Risks and Mitigations:

Risk: Schedule records may contain student information.

Mitigation: Use student aliases and avoid recording unnecessary identifying details.

Risk: The bundled workspace schema omits some consent controls described by the skill.

Mitigation: Confirm the platform enforces the relevant consent and record controls before using shared student records.

Risk: A proposed schedule change could be incorrect or conflict with a student's availability.

Mitigation: Review conflict checks and approve each proposed change before it is written to the schedule.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [Weekly schedule and lesson-package template](artifact/references/weekly-schedule-template.md)
- [Leave, makeup, and rescheduling forms](artifact/references/leave-makeup-reschedule-forms.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration]

**Output Format:** [Markdown schedules and tables, plus structured schedule and lesson-package record updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Schedule changes are proposals until the teacher reviews and approves them.]

## Skill Version(s):

2.12.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
