## Description:

帮助中国 K12 学生记录学习时间、开展番茄钟专注练习，并根据足够的记录分析分心规律和高效时段。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆的学生及陪同的小学家长或老师，帮助他们盘点学习时间、安排专注时段，并在获得相应同意后汇总专注和分心记录。

### Deployment Geography for Use:

中国大陆；其他地区使用前须本地化未成年人同意要求和危机求助渠道。

## Known Risks and Mitigations:

Risk: 未成年人专注记录、提醒或跨技能共享可能超出学生和监护人的预期。

Mitigation: 长期记忆、提醒和共享分别取得明确同意；小学使用时安排家长或老师在场，并按适用规则确认监护人同意。

Risk: 在中国大陆以外使用默认的未成年人同意规则或危机联系方式可能不适用。

Mitigation: 部署前核对当地同意要求与求助渠道；不确定所在地区时不提供中国大陆专用号码。

Risk: 缺少可靠计时或足够的跨次记录时，精确用时和黄金时段结论可能误导学生。

Mitigation: 无法计时时改为学生报告开始和结束；缺少跨次数据时标明依据自报，样本不足时不生成正式报告。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)
- [专注力履历档案模板](artifact/references/focus-archives-template.md)
- [番茄钟状态机](artifact/references/pomodoro-statemachine.md)
- [危机转介协议](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [中文对话及 Markdown 时间记录、专注复盘和阶段性总结]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [计时与跨次分析取决于可用能力和记录；样本不足时仅提供初步观察。]

## Skill Version(s):

2.7.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
