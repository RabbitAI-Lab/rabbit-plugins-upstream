## Description:

Coordinates consent-based study reminders by combining due reviews and learning tasks into a daily summary for students.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and guardians use this Chinese-language skill to schedule, review, pause, and receive consolidated study reminders after giving consent.

### Deployment Geography for Use:

Global (China-mainland defaults require local adaptation)

## Known Risks and Mitigations:

Risk: Student reminders may be sent without appropriate consent or at unsuitable times.

Mitigation: Confirm student or guardian consent and reminder permissions, respect quiet hours, and allow reminders to be paused or deleted.

Risk: Study information could be shared across skills beyond what the student authorized.

Mitigation: Check cross-skill sharing settings and use only the minimum necessary information when sharing is enabled.

Risk: Defaults for minors and emergency support may not fit the deployment region.

Mitigation: Confirm the region and adapt guardian-consent requirements and local support contacts before student use.

## Reference(s):

- [Spaced-review schedule](references/ebbinghaus-schedule.md)
- [Reminder handover schema](shared/handover-protocol.schema.json)
- [Grade-based reminder and quiet-hour settings](shared/grade-bands.md)
- [Platform capabilities and fallback behavior](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Chinese-language reminder messages, daily summaries, and queue views]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposes a reminder plan rather than scheduling or sending messages without consent.]

## Skill Version(s):

2.9.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
