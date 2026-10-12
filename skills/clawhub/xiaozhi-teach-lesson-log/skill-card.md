## Description:

帮助独立教师将课后观察整理为经教师确认的结构化课堂记录、学习轨迹与下节课衔接建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向独立教师：课后整理化名学员的课堂内容、分知识点掌握度和进步证据，预览确认后保存记录，并生成待确认课时条目及下一节课的教学衔接建议。

### Deployment Geography for Use:

中国大陆；其他地区使用前需调整危机求助渠道、课程假设和合规要求。

## Known Risks and Mitigations:

Risk: 课后记录包含未成年人的学习和课堂观察信息，跨技能共享或家长摘要可能超出授权范围。

Mitigation: 使用化名并核验学员授权；记录与课时变更先供教师确认，家长摘要仅在授权后生成内部草稿，由教师决定是否发送。

Risk: 中国大陆的危机联系方式、课程与合规假设在其他地区可能不适用。

Mitigation: 仅在适用的教学场景使用；跨地区部署前由教师核对并本地化危机转介、课程和法律指引。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-log)
- [课后记录模板](references/lesson-log-template.md)
- [危机例外处置](shared/crisis-exception.md)
- [独立教师工作空间数据结构](shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [教师可预览的结构化课后记录和文字建议]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [含逐知识点掌握度、学习轨迹摘要、待确认课时条目；家长事实摘要仅为经授权的内部草稿，不自动发送。]

## Skill Version(s):

2.11.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
