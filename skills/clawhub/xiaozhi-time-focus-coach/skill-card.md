## Description:

帮助中国 K12 学生记录学习时间、启动专注时段、分析黄金时段和分心规律，并在明确同意后保存专注档案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and supporting adults use this skill in Chinese K12 study contexts to run focus sessions, review actual study time, and build consent-based focus records. It is intended for time-use and focus coaching, not subject planning, answer checking, or mental-health support.

### Deployment Geography for Use:

Global; use outside the intended Chinese K12 context requires localization of language, emergency-help channels, school-stage assumptions, and minor-consent rules.

## Known Risks and Mitigations:

Risk: The skill is intended for Chinese K12 learners and can involve minors, reminders, memory, and cross-skill sharing.

Mitigation: Use it only in the intended context unless localized, and confirm the required student and guardian permissions before enabling memory, reminders, or sharing.

Risk: Long-term focus records could expose a student's study habits or distraction patterns.

Mitigation: Keep records opt-in, neutral, and limited to focus fields; preserve pause, delete, export, and sharing controls.

Risk: Crisis, self-harm, abuse, or severe distress signals exceed the skill's focus-coaching purpose.

Mitigation: Stop the focus workflow and refer the student to trusted adults and local emergency-help channels according to the crisis protocol.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)
- [智能番茄钟 · 状态机定义](references/pomodoro-statemachine.md)
- [专注力履历档案模板](references/focus-archives-template.md)
- [危机转介协议](shared/crisis-referral-protocol.md)
- [危机例外处理](shared/crisis-exception.md)
- [学段与默认专注时长](shared/grade-bands.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Conversational Chinese guidance with optional Markdown summaries and JSON-shaped focus records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose consent-gated reminders, cross-skill handoffs, and focus archive entries; long-term records remain opt-in.]

## Skill Version(s):

2.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
