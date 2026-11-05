## Description:

面向语文教师，提供现代文阅读教学设计与文本解读框架。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

语文教师用它为现代文、群文和名著阅读设计教学任务，并按文本三解、阅读策略和三阶阅读组织讨论与练习。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 班级阅读记录可能包含学生相关信息或错误更新。

Mitigation: 使用学生化名；由教师审阅拟议的记录变更，并确认平台支持文档所述的同意、暂停和删除控制。

Risk: 跨技能传递学生档案可能超出已审查的数据范围。

Mitigation: 在交接数据结构和接收技能完成审查前，避免可选的学生档案传递。

Risk: 生成的教学题目或讲解草稿可能有误，或输入未启用的考试材料。

Mitigation: 课堂使用前由教师核验生成内容；不要输入尚未启用的统考试题、答案或评分标准。

## Reference(s):

- [文本三解模板](artifact/references/text-three-solve.md)
- [阅读策略卡片](artifact/references/six-strategies-card.md)
- [群文阅读设计模板](artifact/references/group-text-design.md)
- [高中语文学习任务群地图](artifact/references/hs-task-group-map.md)
- [班级教学工作空间数据结构](artifact/shared/class-teaching-workspace.schema.json)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [中文文本与 Markdown 教学设计框架；可包含结构化班级阅读记录]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [输出为供教师审阅的草稿；不生成整本教材内容或未经确认的学生评价。]

## Skill Version(s):

2.12.5 (source: server-resolved release, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
