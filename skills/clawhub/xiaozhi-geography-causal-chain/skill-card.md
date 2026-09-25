## Description:

引导初高中学生逐步串联地理现象的起因、过程与结果，补全原因分析中的遗漏环节。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆中文初高中地理学习者，帮助学生通过逐环提问解释地球运动、气候、河流、板块运动和人地关系，并完善原因类题目的作答。

### Deployment Geography for Use:

中国大陆；其他地区使用前须本地化课程、学段及危机求助渠道。

## Known Risks and Mitigations:

Risk: 地理因果链可能遗漏中间环节、颠倒因果或偏离当地教材。

Mitigation: 逐环核对学生的解释，以适用教材和当地考试要求为准；生成练习题前先自检。

Risk: 学生档案、跨技能共享、家长可见内容或提醒可能涉及未成年人隐私。

Mitigation: 默认只在当前会话使用；仅在学生或监护人明确同意后启用记忆、共享、家长查看或提醒，并提供更正和删除入口。

Risk: 中国大陆的课程设定和危机求助号码不适用于其他地区。

Mitigation: 面向其他地区部署前本地化课程和求助渠道；地区不明时先询问，不直接提供中国大陆号码。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-geography-causal-chain)
- [地理成因链指南](artifact/references/causal-chain-guide.md)
- [地理错因维度表](artifact/shared/geography-error-dimension-table.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Markdown]

**Output Format:** [中文对话文本与分步成因链；可按学生确认提供文字档案或练习反馈]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [默认仅限当前会话；档案写入、跨技能共享和提醒须经同意。]

## Skill Version(s):

2.4.0 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
