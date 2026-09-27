## Description:

Helps Chinese K12 students turn classroom notes into Cornell-style cue questions and summaries, then find relevant notes for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in upper elementary school, middle school, and high school use the skill to organize photographed or typed class notes, retrieve notes by topic, and review with cue questions. Upper-elementary students use a simplified version with an adult present.

### Deployment Geography for Use:

China (Chinese K12 context); localize curriculum, consent rules, and crisis resources before use elsewhere.

## Known Risks and Mitigations:

Risk: Student notes and usage history may contain sensitive learning information.

Mitigation: Enable the profile only with required consent, honor pause or deletion requests, and share only aggregate note counts and recurring gaps across skills.

Risk: Chinese K12 curriculum, consent assumptions, and crisis resources may be inappropriate in other locales.

Mitigation: Localize these elements before deployment elsewhere and use location-appropriate crisis referral guidance.

Risk: Unwanted persistent reminders could interrupt students or expose their study topics.

Mitigation: Send review reminders only after explicit consent and allow reminders to be paused.

## Reference(s):

- [Cornell note format and subject templates](references/cornell-format-guide.md)
- [Grade-band guidance](shared/grade-bands.md)
- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-cornell-notes)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language Cornell notes with cue questions and a one-sentence summary; optional note retrieval and usage reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Note storage, sharing, and reminders require applicable consent; without persistent memory, notes stay in the current conversation.]

## Skill Version(s):

2.7.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
