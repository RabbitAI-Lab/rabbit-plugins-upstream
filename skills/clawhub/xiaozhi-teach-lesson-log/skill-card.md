## Description:

帮助独立教师将课后观察整理为经确认的结构化教学记录、学习轨迹和下节课衔接建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆中文 K12 场景的独立教师：按学员化名和上课日期整理五维度课后记录、分知识点掌握情况、学习轨迹及下节课建议；记录和课时变更均须教师确认。

### Deployment Geography for Use:

中国大陆；其他地区使用前须本地化课程、未成年人数据规则及危机求助渠道。

## Known Risks and Mitigations:

Risk: 课后记录或课时台账可能包含不准确的观察或扣减。

Mitigation: 教师保存前核对每条记录，并逐项确认课时台账变更。

Risk: 未获授权的学员信息或课堂情绪观察可能被转给家长。

Mitigation: 使用化名，核对家长沟通和情绪分享授权；家长摘要仅供教师内部审定，不自动发送。

Risk: 中国大陆以外的课程、隐私要求或危机求助渠道可能不适用。

Mitigation: 在其他地区使用前核对当地课程与法律要求，并替换求助渠道。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-log)
- [课后记录与学习轨迹模板](references/lesson-log-template.md)
- [独立教师工作空间数据结构](shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Markdown, Structured records, Guidance]

**Output Format:** [中文课后记录草稿、结构化学员记录与待确认课时条目]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [记录经教师预览确认后才保存；家长摘要仅为内部草稿，不自动发送。]

## Skill Version(s):

2.4.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
