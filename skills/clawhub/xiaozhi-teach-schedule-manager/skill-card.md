## Description:

帮助独立教师生成周课表、检查时间冲突，并在教师确认后登记排课与课时包信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向使用简体中文、按中国大陆 K12 教学方式工作的独立教师，提供排课、调课、请假及补课建议，并查看课时包剩余与到期情况。

### Deployment Geography for Use:

Mainland China (Simplified Chinese K12 teaching workflows)

## Known Risks and Mitigations:

Risk: 课表与学员时间信息可能暴露个人安排。

Mitigation: 使用学员化名，仅记录可上课时间段；不要记录真实姓名、联系方式或家庭安排原因。

Risk: 错误排课或课时包记录可能影响教师安排。

Mitigation: 先检查时间冲突并请教师确认，再保存课表；课时扣减交由课后记录流程确认。

Risk: 课时余额与到期提示可能被误当作财务结算或家长通知。

Mitigation: 将金额与退费交给独立记账工具，家长沟通由教师决定并在其他工具中处理。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-schedule-manager)
- [周课表与课时包模板](references/weekly-schedule-template.md)
- [请假、补课与调课登记模板](references/leave-makeup-reschedule-forms.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration]

**Output Format:** [中文课表、时间冲突提示和待确认的调课或补课建议；确认后更新课表与课时包记录]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [不扣减课时、不处理金额或退款、不代发家长消息。]

## Skill Version(s):

2.9.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
