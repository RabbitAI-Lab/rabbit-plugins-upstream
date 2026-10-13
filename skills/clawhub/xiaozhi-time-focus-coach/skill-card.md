## Description:

Helps Chinese-speaking K12 students track study time, run focus sessions, and identify productive periods and distraction patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking K12 students use the skill to review study-time logs, plan consent-based focus sessions, and see patterns in their attention and productive hours. Persistent records, reminders, and sharing require separate consent.

### Deployment Geography for Use:

Mainland China (Chinese-language K12); other regions require localization of crisis contacts and minor-consent rules.

## Known Risks and Mitigations:

Risk: Crisis contacts and consent expectations may not fit students outside mainland China.

Mitigation: Localize emergency channels and minor-consent rules before deployment in other countries or school systems.

Risk: Focus records and sharing could expose a student's study and distraction data.

Mitigation: Keep long-term storage, reminders, and cross-skill sharing off until separately authorized; require confirmation before saving records.

Risk: Time and focus trends can be misleading when logs are sparse or reliable timing is unavailable.

Mitigation: Label self-reported or limited data, avoid precise historical claims without records, and defer formal golden-hour reports until enough data exists.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)
- [Focus archive template](artifact/references/focus-archives-template.md)
- [Pomodoro state machine](artifact/references/pomodoro-statemachine.md)
- [Grade-band guidance](artifact/shared/grade-bands.md)
- [Crisis referral guidance](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Markdown]

**Output Format:** [Chinese-language conversational text and structured Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Study-time summaries, focus-session check-ins, and optional consented focus records; timing and historical analysis depend on available platform capabilities.]

## Skill Version(s):

2.11.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
