## Description:

A Chinese-language English vocabulary tutor for K–12 learners that schedules spaced review, assembles daily vocabulary cards, and prepares students for upcoming lessons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-reading K–12 students use this skill to collect English vocabulary, review due words with adaptive cards, preview upcoming lessons, and inspect their learning progress. Younger students should use it with a parent or teacher present.

### Deployment Geography for Use:

Mainland China (localize language, curriculum, and crisis-help contacts before use elsewhere)

## Known Risks and Mitigations:

Risk: Storing a minor's vocabulary history or sharing progress without appropriate permission.

Mitigation: Confirm profile, cross-skill, and parent-sharing consent before saving or sharing; honor access, correction, deletion, export, and pause requests.

Risk: Unwanted or excessive study reminders.

Mitigation: Require reminder consent, combine due words into one daily card, and pause reminders after repeated non-response.

Risk: Mainland China crisis contacts or curriculum assumptions may not fit users elsewhere.

Mitigation: Localize curriculum, language, and crisis-help contacts before deployment outside Mainland China; ask the user's region when uncertain.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-vocabulary-dna)
- [Vocabulary radar topic templates](references/vocabulary-radar-topics.md)
- [High-school vocabulary guidance](references/english-hs-vocabulary.md)
- [Vocabulary review and consent rules](shared/vocab.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language vocabulary cards, study prompts, and progress summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [At most one due-vocabulary card per day; proactive reminders require consent and a reminder-capable integration.]

## Skill Version(s):

2.9.0 (source: skill frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
