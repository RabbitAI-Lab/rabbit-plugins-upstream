## Description:

A Chinese-language English vocabulary coach that schedules spaced reviews, prepares upcoming words, and creates one daily card of due words.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and educators use this Chinese-language assistant to collect English vocabulary, practice with spaced-repetition cards, and preview words for upcoming lessons. With consent, it can retain learner progress and queue a daily review card.

### Deployment Geography for Use:

Mainland China; localize curriculum, minor-data consent, and crisis-support contacts before use elsewhere.

## Known Risks and Mitigations:

Risk: Storing a minor's vocabulary progress or sharing it beyond the session without permission.

Mitigation: Require learner-profile and cross-skill-sharing consent before saving or transferring progress; allow viewing, correction, deletion, and pausing.

Risk: Unwanted review reminders or promises of reminders where scheduling is unavailable.

Mitigation: Queue reminders only with explicit reminder consent; otherwise offer review on the learner's next visit and do not promise proactive messages.

Risk: Mainland China curriculum and crisis-support defaults may be inappropriate in another region.

Mitigation: Before deployment elsewhere, adapt curriculum, minor-data requirements, and local crisis contacts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-vocabulary-dna)
- [High-school vocabulary reference](references/english-hs-vocabulary.md)
- [Vocabulary preview topics](references/vocabulary-radar-topics.md)
- [Platform capabilities and regional adaptation](shared/platform-conventions.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Chinese-language vocabulary guidance and daily review cards; structured profile and reminder handoffs when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [At most one due-word card per day; reminders require consent and a supported reminder service.]

## Skill Version(s):

2.7.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
