## Description:

Chinese-language English vocabulary review skill that stores learner vocabulary with consent, schedules spaced repetition, queues one daily review card, and supports pre-class vocabulary warmups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and education agents use this skill to manage English vocabulary review for upper-primary and middle-school students, including word intake, spaced review cards, vocabulary warmups, and vocabulary-library health reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can keep a long-term learner vocabulary profile and coordinate cross-skill sharing or reminders.

Mitigation: Confirm profile storage, cross-skill sharing, reminder consent, and parent-sharing settings before use, especially for minors.

Risk: Emergency contact and learner-support guidance may be jurisdiction-specific.

Mitigation: Review and replace local emergency or guardian-contact guidance before deployment outside the release's expected context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-vocabulary-dna)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Vocabulary radar topics](artifact/references/vocabulary-radar-topics.md)
- [Vocabulary contract](artifact/shared/vocab.md)
- [Platform capability conventions](artifact/shared/platform-conventions.md)
- [Ebbinghaus schedule guidance](artifact/shared/ebbinghaus-schedule.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese-language Markdown and structured handoff guidance for vocabulary cards, profile updates, and reminder queue entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires platform memory, reminder, OCR, and cross-session statistics capabilities for full behavior; falls back to manual text input, in-session review, or user-managed reminders when those capabilities are unavailable.]

## Skill Version(s):

2.1.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
