## Description:

A Chinese K12 time and focus coach that helps students track study time, run consent-gated Pomodoro sessions, review distraction patterns, and identify productive study windows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in Chinese K12 settings use this skill to start focus sessions, record study time, review distraction patterns, and build consent-gated focus summaries. Deployments use its boundaries to manage student consent, reminder behavior, data deletion/export, and crisis referral handling.

### Deployment Geography for Use:

China mainland by default; other regions require localization of crisis-support channels, school-stage assumptions, and minor consent rules.

## Known Risks and Mitigations:

Risk: Minor students' focus records or reminders could be retained or shared without valid consent.

Mitigation: Keep long-term memory, reminders, and cross-skill sharing disabled unless the student and, where required, a guardian explicitly consent; confirm each record before writing it.

Risk: Crisis-support channels, school-stage defaults, and consent expectations may be wrong outside the intended China mainland K12 setting.

Mitigation: Localize emergency referrals, grade-band assumptions, and minor-consent rules before deploying to other regions.

Risk: Timer, reminder, or cross-session statistics claims could mislead users if the host platform lacks those capabilities.

Mitigation: Confirm platform support before enabling those workflows; otherwise use self-reported start and end times, local alarms, and current-session-only summaries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)
- [Focus archive template](artifact/references/focus-archives-template.md)
- [Pomodoro state machine](artifact/references/pomodoro-statemachine.md)
- [Platform capability conventions](artifact/shared/platform-conventions.md)
- [Grade-band parameters](artifact/shared/grade-bands.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)
- [Focus profile schema](artifact/shared/dna-profile.schema.json)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese conversational coaching text with optional structured focus-record and reminder handoff payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional long-term records, reminders, and cross-skill sharing are disabled until explicitly consented to.]

## Skill Version(s):

2.1.12 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
