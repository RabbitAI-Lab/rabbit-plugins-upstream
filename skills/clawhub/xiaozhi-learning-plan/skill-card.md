## Description:

帮助中国大陆小学高段至高中学生把学习目标拆解为可执行的周计划或 30 天计划，并根据反馈调整安排。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆小学高段、初中和高中学生及其陪同的监护人或教师，制定备考、日常学习和弱项巩固计划。学生可以复盘执行情况并调整任务；家长看板和提醒安排须分别取得同意。

### Deployment Geography for Use:

中国大陆；其他地区使用前须本地化课程、未成年人同意要求及危机求助渠道。

## Known Risks and Mitigations:

Risk: 未成年人学习档案或计划完成情况可能在未经同意时被读取或共享。

Mitigation: 档案读取、家长看板和提醒任务保持默认关闭，分别确认学生及必要时监护人的同意；家长看板只展示任务和完成情况。

Risk: 其他地区直接使用中国大陆课程安排、未成年人同意规则或危机求助渠道可能不适用。

Mitigation: 限定于中国大陆中文 K12 场景；跨地区使用前核对课程、同意规则，并替换当地求助渠道。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [学习计划模板](artifact/references/plan-templates.md)
- [学段与作息指南](artifact/shared/grade-bands.md)
- [危机情况处理指南](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [中文 Markdown 学习计划、复盘建议和可选的家长任务看板]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [初中及高中提供 30 天计划；小学高段提供周计划。档案读取、家长看板和提醒任务分别征得同意。]

## Skill Version(s):

2.10.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
