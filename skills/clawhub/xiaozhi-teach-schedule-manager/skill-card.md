## Description:

帮助独立教师生成周课表、核对时间冲突，并管理请假、补课及课时包台账。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

独立教师用它安排和查询课表、检查教师与学员的时间冲突，并准备请假、调课、补课和课时包到期提示；课表变更须由教师确认。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 共享记录中的学员时间和课时包数量可能暴露个人安排。

Mitigation: 仅记录化名、可上课时间和课时数量；不要录入真实姓名、联系方式、学校班级、家庭原因或付款信息。

Risk: 错误排课、台账变更或未经核对的导出、共享和删除可能影响教学安排。

Mitigation: 教师确认前检查时间冲突及课时余额，并复核每次课表、台账、导出、共享或删除操作。

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [周课表模板](references/weekly-schedule-template.md)
- [请假/补课/调课登记模板](references/leave-makeup-reschedule-forms.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [中文文本及 Markdown 课表、冲突提示和登记表]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [课表及台账更改需教师确认；不处理金额或自动扣减课时。]

## Skill Version(s):

2.4.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
