## Description:

帮助初高中学生按六类生物错因分析错题、定位薄弱环节，并在学生请求时生成弱项报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中文初高中学生，分析生物错题的概念、结构与功能、图表、实验、表述及遗传计算错误，帮助制定针对性的练习，并按授权维护弱项档案。

### Deployment Geography for Use:

中国大陆中文 K12；其他地区使用前须本地化课程、危机求助渠道和未成年人同意规则。

## Known Risks and Mitigations:

Risk: 未授权存储或共享未成年学生的错题弱项信息。

Mitigation: 确认平台执行建档、跨技能共享、家长可见性、暂停和删除的同意控制，再启用档案更新。

Risk: 在中国大陆以外沿用不适用的课程假设或危机求助方式。

Mitigation: 部署前本地化课程、未成年人同意要求和求助渠道；提供危机联系方式前确认所在地。

Risk: 将学习分析误当作医疗或心理诊断，或在危机情境继续出题。

Mitigation: 不提供诊断或治疗建议；出现危机信号时停止学习流程，指引联系可信成年人及当地专业援助。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-biology-error-dna)
- [生物错因维度表](references/biology-error-dimension-table.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [中文文本或 Markdown 弱项报告；授权时提供结构化 JSON 交接与档案更新内容]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [不自行计算历史错题次数；样本不足时标注限制，档案更新须经学生同意。]

## Skill Version(s):

2.10.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
