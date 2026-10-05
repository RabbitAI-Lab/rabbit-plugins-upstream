## Description:

Guides Chinese-speaking students through weekly activities to distinguish fleeting likes from sustained interests, with optional consent-based tracking over time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in Chinese-language K–12 settings use guided weekly reflection to explore interests and observe how they respond to challenges. With appropriate student and guardian consent, the skill can track interest patterns across weeks; without consent, it supports a single unrecorded conversation.

### Deployment Geography for Use:

Mainland China; use elsewhere requires localizing safeguarding contacts, school context, and rules for minors' data and guardian consent.

## Known Risks and Mitigations:

Risk: Long-term interest records about minors could be kept or shared without informed consent.

Mitigation: Explain what is saved, who can see it, how long it remains, and how to delete it; obtain student and required guardian consent before tracking, and separate consent for parent or cross-skill sharing.

Risk: Reminders or sharing could expose a student's interests to others.

Mitigation: Enable reminders only with consent; limit parent summaries to facts the student approves and cross-skill sharing to the current exploration topic.

Risk: Mainland-China defaults may be unsafe or unsuitable in other regions.

Mitigation: Localize crisis referral contacts, school context, and guardian-consent requirements before offering the skill elsewhere.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-interest-explorer)
- [Interest exploration template](references/interest-exploration-template.md)
- [Platform and localization conventions](shared/platform-conventions.md)
- [Crisis response guidance](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and structured Markdown interest records or summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional weekly records, staged interest summaries, and student-approved parent-facing factual summaries.]

## Skill Version(s):

2.10.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
