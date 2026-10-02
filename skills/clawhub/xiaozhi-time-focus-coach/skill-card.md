## Description:

帮助中文 K12 学生记录学习用时、安排番茄钟，并根据专注记录分析高效时段与分心规律。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆中文 K12 学生及陪同使用的家长或老师，提供学习时间盘点、番茄钟引导和专注习惯复盘。

### Deployment Geography for Use:

China (mainland); localize crisis resources, curriculum assumptions, and guardian-consent rules before use elsewhere

## Known Risks and Mitigations:

Risk: Crisis guidance, curriculum assumptions, and guardian-consent rules are tailored to Chinese-speaking K12 use in mainland China.

Mitigation: Localize crisis resources, curriculum assumptions, and consent rules before deploying elsewhere.

Risk: Enabling long-term memory, reminders, or cross-skill sharing can persist a student's focus history.

Mitigation: Keep each feature off by default, obtain separate explicit consent, and confirm each record before storing it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)
- [专注力履历档案模板](artifact/references/focus-archives-template.md)
- [番茄钟状态机](artifact/references/pomodoro-statemachine.md)
- [学段参数表](artifact/shared/grade-bands.md)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Text]

**Output Format:** [Conversational text and structured focus summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long-term focus records, reminders, and cross-skill sharing require separate explicit consent.]

## Skill Version(s):

2.10.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
