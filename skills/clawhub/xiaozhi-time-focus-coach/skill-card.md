## Description:

Helps students track study time, identify productive periods, use focus sessions, and review distraction patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking K–12 students use the skill to plan and review study time, run focus sessions, and understand distraction patterns. Guardians and educators can support younger students using its consent controls.

### Deployment Geography for Use:

Chinese-speaking K–12 contexts; localize safety contacts, curriculum assumptions, and minor-consent rules before use in other regions.

## Known Risks and Mitigations:

Risk: A student's study and distraction records could be kept or shared without informed consent.

Mitigation: Keep long-term records, reminders, and cross-skill sharing off by default; obtain separate affirmative consent and guardian consent when required.

Risk: Safety contacts and consent expectations may not fit another region.

Mitigation: Localize crisis contacts, curriculum assumptions, and minor-consent rules before deployment outside the intended context.

Risk: Focus-session timing and long-term trends may be inaccurate without platform timing or record access.

Mitigation: Use student-confirmed start and end times when timing is unavailable, and describe trends as self-reported when persistent records are unavailable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)
- [Focus record template](references/focus-archives-template.md)
- [Pomodoro session rules](references/pomodoro-statemachine.md)
- [Age-group guidance](shared/grade-bands.md)
- [Crisis response guidance](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and structured study-time summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Session-only by default; persistent records, reminders, and sharing each require separate consent.]

## Skill Version(s):

2.11.2 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
