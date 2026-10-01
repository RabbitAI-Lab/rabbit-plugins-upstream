## Description:

帮助中国语境下的中小学生记录学习时间、安排番茄钟、复盘分心情况，并在有足够记录时识别高效时段。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中小学生的中文学习时间管理：记录实际学习时长、规划专注时段、回顾分心，并在获得明确同意后积累可用于识别高效时段的记录。小学学段使用时需有家长或老师陪同。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 未成年人学习习惯与分心记录可能在长期保存或跨技能共享后暴露隐私。

Mitigation: 长期记忆、提醒和跨技能共享默认关闭并分别征得明确同意；较年幼学生的长期记录须有监护人参与，且只保存与专注相关的必要信息。

Risk: 缺乏计时或跨会话记录能力时，可能误报专注时长或高效时段。

Mitigation: 无法计时时改为学生自行报告开始与结束；无法跨会话统计时说明结果基于自报数据，不给出精确统计。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)
- [番茄钟状态与流程](references/pomodoro-statemachine.md)
- [专注力档案模板](references/focus-archives-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [中文对话及 Markdown 学习时间摘要]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [可选的专注记录、提醒请求及跨技能共享须分别获得明确同意。]

## Skill Version(s):

2.9.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
