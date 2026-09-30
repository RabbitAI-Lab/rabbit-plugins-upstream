## Description:

Helps Chinese-speaking students track study time, identify productive periods, run focused study sessions, and reflect on distractions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking K–12 students use this skill to review study-time patterns, plan realistic focus sessions, and identify productive times. Younger students need the specified guardian or teacher involvement.

### Deployment Geography for Use:

Mainland China; localize the guidance and crisis resources for use elsewhere.

## Known Risks and Mitigations:

Risk: A student's study and distraction records may be retained or shared without informed consent.

Mitigation: Keep long-term memory, reminders, and cross-skill sharing off by default; obtain separate explicit consent, including guardian consent where required.

Risk: Chinese K–12 guidance and crisis contacts may be unsuitable in another locale.

Mitigation: Confirm the intended audience and localize the content and crisis resources before deployment elsewhere.

Risk: Time estimates may appear precise when live timing or cross-session history is unavailable.

Mitigation: Use student-reported start and end times and label estimates as self-reported rather than claiming background timing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)
- [Focus archive template](references/focus-archives-template.md)
- [Pomodoro session state machine](references/pomodoro-statemachine.md)
- [Grade-band guidance](shared/grade-bands.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Conversational text and Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide study-time summaries and an exportable focus record; persistent records, reminders, and cross-skill sharing require separate opt-in.]

## Skill Version(s):

2.8.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
