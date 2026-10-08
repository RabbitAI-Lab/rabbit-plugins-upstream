## Description:

为语文教师提供现代文文本解读、阅读策略和分层阅读任务的教学设计指导。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

语文教师使用本技能设计小学高段至高中现代文阅读课，包括文本解读、阅读策略练习、群文阅读和班级阅读能力记录；教学草稿由教师复核后使用。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 班级阅读记录可能包含学生敏感信息，或未经同意向家长和其他技能共享。

Mitigation: 在教师控制的中国 K12 场景中使用学生别名，并在跨技能或家长共享前确认同意。

Risk: 班级记录写入权限过宽可能修改评估生成的字段。

Mitigation: 将写权限限制到声明的 x-skill-scope 字段，不允许更新 stubbornCount 等评估衍生字段。

Risk: 未经核查的生成练习或受版权保护的教材内容可能被直接用于课堂。

Mitigation: 教师在使用前复核生成内容；教材原文和教辅题只保存出处索引，不复制正文。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chinese-reading-guide)
- [文本三解模板](references/text-three-solve.md)
- [阅读六大策略卡](references/six-strategies-card.md)
- [群文阅读设计模板](references/group-text-design.md)
- [高中语文学习任务群课程地图](references/hs-task-group-map.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [中文文本或 Markdown 教学设计与阅读记录草稿]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [阅读速度和阅读量须由教师或学生填报；面向学生或家长的内容须经教师复核。]

## Skill Version(s):

2.11.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
