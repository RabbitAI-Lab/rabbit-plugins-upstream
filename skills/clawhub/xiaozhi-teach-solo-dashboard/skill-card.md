## Description:

只读汇总独立教师的课表、学员、作业、家长沟通与课时包记录，生成按优先级排列的每日工作台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆的独立教师，汇总现有教学记录，查看今日课表、待办、需关注的学员和最重要的三件事；不代替教师审核或更改记录。

### Deployment Geography for Use:

中国大陆

## Known Risks and Mitigations:

Risk: 日工作台汇总未成年学员和家长记录，转发可能泄露个人信息。

Mitigation: 仅在教师知情和适当授权下读取；分享给家长前核对同意范围，并仅用学员化名及必要的低敏信息。

Risk: 中国大陆以外的法律、课程或危机转介信息可能不适用。

Mitigation: 在其他地区使用前，本地化相关法律、课程和危机转介指引。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [日工作台模板](artifact/references/dashboard-template.md)
- [七区块输出模板](artifact/references/daily-dashboard-block-templates.md)
- [日工作台完整示例](artifact/references/daily-dashboard-full-sample.md)
- [独立教师工作空间数据结构](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [七区块日工作台，含基于记录的风险提示与三项优先待办；不写入记录或发送消息。]

## Skill Version(s):

2.11.0 (source: ClawHub release, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
