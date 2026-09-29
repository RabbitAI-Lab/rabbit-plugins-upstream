## Description:

帮助学生记录实际学习时间、安排番茄钟，并根据已同意保存的记录分析专注时段和分心规律。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国 K12 学生的学习时间管理：记录学习时段、引导专注与休息，并在获准保存记录后回顾分心规律和适合学习的时段。

### Deployment Geography for Use:

China (mainland); localize crisis contacts, school norms and minor-consent practices before use elsewhere

## Known Risks and Mitigations:

Risk: Crisis contacts, school practices, and consent expectations may not fit users outside the intended Chinese K12 context.

Mitigation: Use in the intended context or localize language, crisis contacts, school norms, and minor-consent rules first.

Risk: Saving focus records or sending reminders or details to other skills without appropriate consent may expose a student's information.

Mitigation: Keep these features off by default and enable each only with the student's explicit agreement and guardian agreement when required.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)
- [专注力履历档案模板](references/focus-archives-template.md)
- [智能番茄钟状态机](references/pomodoro-statemachine.md)
- [学段参数表](shared/grade-bands.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and structured study-time summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Session-only by default; longer-term trends require consent and enough observations.]

## Skill Version(s):

2.7.1 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
