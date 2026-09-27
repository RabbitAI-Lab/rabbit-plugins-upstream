## Description:

为中文初高中学生提供元素符号、化合价、化学式和化学方程式书写与配平的分级练习和纠错指导。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中文初高中学生和辅导者，按掌握程度练习化学符号、化学式及方程式书写与配平，并针对错误给出逐步提示。

### Deployment Geography for Use:

中国大陆；其他地区须先调整课程标准、未成年人同意要求和危机求助渠道。

## Known Risks and Mitigations:

Risk: 中国大陆课程、未成年人授权规则和求助渠道不适合直接用于其他地区。

Mitigation: 面向其他地区学生部署前，核对当地课程与同意规则并替换危机求助联系方式。

Risk: 学习档案或提醒可能在学生不知情时保存或发送。

Mitigation: 默认仅进行会话内练习；明确征得相应同意后再启用档案、共享或提醒，并保留暂停和删除入口。

Risk: 生成的化学式、配平结果或练习题可能出错。

Mitigation: 发布练习前核对化学式及原子守恒；学生指出错误时重新验算并纠正。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-notation-coach)
- [化学用语规则手册](artifact/references/chemistry-notation-rules.md)
- [化学错因维度表](artifact/shared/chemistry-error-dimension-table.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [中文对话文本及 Markdown 练习反馈]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [可按学生确认记录学习进度或安排回顾提醒；默认仅在当前会话练习。]

## Skill Version(s):

2.7.0 (source: ClawHub release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
