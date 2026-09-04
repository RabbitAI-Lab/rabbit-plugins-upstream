## Description:

帮学生把学习时间记成账、找出黄金时段、用番茄钟稳住专注，并积累分心规律。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students use this skill to track actual study time, run Pomodoro-style focus sessions, identify productive time windows, and review distraction patterns. Agents use it to provide time-use coaching while deferring study planning, error analysis, and comprehension checks to other skills.

### Deployment Geography for Use:

Global; review localization before use outside Chinese-language, mainland-China-oriented student support settings.

## Known Risks and Mitigations:

Risk: Crisis guidance is China-specific while the release does not clearly restrict geography.

Mitigation: Localize emergency contacts and referral language before real student use outside Chinese-language, mainland-China-oriented environments.

Risk: The skill can accumulate focus records, reminders, and cross-skill summaries about students.

Mitigation: Enable memory, reminders, and cross-skill sharing only with clear student or guardian consent, and honor pause, export, correction, and deletion requests.

Risk: Focus and distraction coaching can encounter self-harm, safety, bullying, or severe distress signals.

Mitigation: Stop the coaching flow, avoid recording incident details, and follow the crisis exception protocol with referral to trusted adults or emergency services.

## Reference(s):

- [Focus archive template](artifact/references/focus-archives-template.md)
- [Pomodoro state machine](artifact/references/pomodoro-statemachine.md)
- [Grade bands](artifact/shared/grade-bands.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Learning DNA profile schema](artifact/shared/dna-profile.schema.json)
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured text snippets and JSON-compatible archive fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose focus records, Pomodoro state, reminders, and cross-skill handoffs only when user consent is present.]

## Skill Version(s):

2.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
