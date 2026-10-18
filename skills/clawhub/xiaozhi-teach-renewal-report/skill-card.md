## Description:

根据指定学员的真实学习记录起草可追溯的阶段报告、续课建议和家长沟通话术，由教师审核并自行发送。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

独立教师使用指定学员的课后记录、作业跟进和课时数据，编写事实、进步、计划三段式报告，并准备不施压的续课沟通草稿。

### Deployment Geography for Use:

中国大陆；其他地区使用前需本地化语言、法律参考和危机求助渠道。

## Known Risks and Mitigations:

Risk: 读取未指定或未经授权的未成年人学习记录，或向家长披露敏感内容。

Mitigation: 先指定一位学员并限制读取范围；生成家长可见内容前核实沟通及相关内容的授权，不写真实姓名和联系方式。

Risk: 不完整的学习数据可能造成夸大进步或误导续课决定。

Mitigation: 每项结论追溯原始记录；缺少逐知识点分数时仅作定性判断，由教师核对报告与建议。

Risk: 中国大陆 K12 的法律和危机求助假设在其他地区可能不适用。

Mitigation: 在其他地区使用前本地化法律参考、语言和危机求助渠道。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-renewal-report)
- [阶段报告模板](references/stage-report-templates.md)
- [续课沟通话术库](references/renewal-communication-scripts.md)
- [教学记录术语和授权位](shared/vocab.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [带记录依据的中文阶段报告和续课沟通草稿]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [需教师核实记录、授权和建议后自行发送；不会代发消息或变更学员档案。]

## Skill Version(s):

2.11.2 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
