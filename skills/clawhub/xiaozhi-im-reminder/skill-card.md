## Description:

Schedules and combines consented study reviews and tasks into a daily reminder for Chinese-speaking students.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and guardians in mainland China's K12 setting use this skill to schedule and manage consented study reminders for review, practice, and planned tasks. Without consent, it offers a suggested reminder plan rather than scheduling notifications.

### Deployment Geography for Use:

Mainland China (Simplified Chinese K12); localize crisis contacts, curriculum, guardian-consent rules, and language before use elsewhere.

## Known Risks and Mitigations:

Risk: Unwanted notifications or sharing of a minor's study information.

Mitigation: Obtain explicit student or guardian consent, share only the minimum necessary information, and honor pause, cancellation, and sharing controls.

Risk: Excessive or ill-timed reminders may pressure students or disturb sleep.

Mitigation: Respect grade-specific quiet hours, combine routine items into one daily digest, and pause a reminder type after repeated nonresponse.

Risk: Mainland China crisis referrals and school assumptions may be inappropriate in other regions.

Mitigation: Localize crisis contacts, curriculum, consent rules, and language before deployment outside mainland China.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Spaced review schedule](references/ebbinghaus-schedule.md)
- [Grade-band reminder limits](shared/grade-bands.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language reminder messages and daily summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offers reminder controls and a review queue; requires scheduling support for proactive delivery.]

## Skill Version(s):

2.11.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
