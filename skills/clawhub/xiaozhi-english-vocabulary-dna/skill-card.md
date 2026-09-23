## Description:

Chinese K12 English vocabulary review skill that stores learner-selected words with consent, schedules spaced review due dates, prepares daily vocabulary cards, and supports lesson-preview vocabulary warmups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, parents, teachers, and education agents use this skill to help upper-primary and middle-school students maintain an English vocabulary review list, receive one consolidated due-word card, and preview upcoming lesson vocabulary. The skill is designed for consent-gated profile storage and reminder queueing in a Chinese K12 learning environment.

### Deployment Geography for Use:

China mainland by default; localize crisis referral numbers and consent practices before use in other regions.

## Known Risks and Mitigations:

Risk: The skill is intended for minors in a Chinese K12 learning environment and may store vocabulary progress when profile and sharing consent are enabled.

Mitigation: Review profile, sharing, reminder, parent-sharing, and guardian-consent settings before use, especially for younger students.

Risk: Crisis referral guidance includes China mainland emergency and youth-support channels that may not apply elsewhere.

Mitigation: Localize emergency contact guidance before deployments outside China mainland and ask for the user's region when location is unclear.

Risk: Over-frequent reminders could create pressure or notification fatigue for students.

Mitigation: Keep the artifact's one-card-per-day behavior and pause vocabulary reminders after repeated non-response.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-vocabulary-dna)
- [Vocabulary Radar Topics](artifact/references/vocabulary-radar-topics.md)
- [Unified Vocabulary Contract](artifact/shared/vocab.md)
- [Ebbinghaus Schedule Notes](artifact/shared/ebbinghaus-schedule.md)
- [Crisis Referral Protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Chinese conversational guidance, daily vocabulary-card markdown, and consent-gated profile or reminder records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal operation produces at most one daily vocabulary card contribution and avoids extra reminders.]

## Skill Version(s):

2.2.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
