## Description:

英语词汇复习：按间隔重复排到期日，每天把到期的词合并成一张词卡。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in Chinese K12 English study contexts, with appropriate guardian or teacher involvement for younger learners, use this skill to save vocabulary, schedule spaced reviews, receive a single daily due-word card, and preview upcoming lesson vocabulary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can maintain a vocabulary profile and queue daily review cards when relevant consents are enabled.

Mitigation: Confirm profile, cross-skill sharing, reminder, sharing, and deletion choices before saving, enqueueing, sharing, or deleting vocabulary data.

Risk: Broad study triggers could be mistaken for permission to save new words or schedule reminders.

Mitigation: Pair broad triggers with a clear confirmation step before any profile write, reminder enqueue, sharing, or deletion action.

Risk: The skill is designed around Chinese K12 curriculum assumptions and default crisis resources.

Mitigation: Localize curriculum, consent-age rules, and crisis referral channels before deployment outside the intended Chinese K12 context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-vocabulary-dna)
- [Vocabulary radar topics](artifact/references/vocabulary-radar-topics.md)
- [Unified vocabulary and consent terms](artifact/shared/vocab.md)
- [Spaced review schedule](artifact/shared/ebbinghaus-schedule.md)
- [Platform capability conventions](artifact/shared/platform-conventions.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown-style study prompts, vocabulary review cards, profile writeback proposals, and reminder enqueue proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consent-gated vocabulary profile updates and at most one daily due-vocabulary card queued through the reminder system.]

## Skill Version(s):

2.3.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
