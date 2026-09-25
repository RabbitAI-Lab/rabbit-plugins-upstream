## Description:

帮助中国 K12 学生记录学习时间、开展番茄钟专注练习，并根据已有记录分析高效时段与分心规律。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in a Chinese K12 study-support setting use this skill to review study time, run consent-based focus sessions, and identify productive times and distraction patterns. Younger students may need guardian consent and elementary students need adult supervision.

### Deployment Geography for Use:

Mainland China; localize language, emergency contacts, school assumptions, and minor-consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: A minor's focus records or reminders could be retained or shared without their intended consent.

Mitigation: Keep memory, reminders, and cross-skill sharing off by default; request separate explicit consent, obtain guardian consent when required, and confirm each record before saving.

Risk: Time estimates and golden-hour conclusions may mislead when timing or historical records are unavailable.

Mitigation: Use self-reported start and end times if precise timing is unavailable, avoid invented historical totals, and label conclusions based on limited or self-reported data.

Risk: Emergency advice or minor-consent assumptions may not fit use outside the intended Chinese K12 setting.

Mitigation: Localize emergency contacts, school context, language, and guardian-consent rules before deployment elsewhere.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)
- [Pomodoro state machine](references/pomodoro-statemachine.md)
- [Focus archive template](references/focus-archives-template.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Markdown]

**Output Format:** [Conversational text and Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focus-session prompts, study-time summaries, and optional focus-record exports; historical analysis depends on available, consented records.]

## Skill Version(s):

2.4.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
