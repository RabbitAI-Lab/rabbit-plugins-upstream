## Description:

英语词汇复习技能，按 SM-2 间隔重复维护单词到期日，并把到期词汇合并为每日一张词卡。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and learning-assistant operators use this skill to store English vocabulary, schedule review by performance, prepare upcoming lesson words, and produce consent-gated vocabulary cards and health reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores student vocabulary history and may queue long-term reminders.

Mitigation: Confirm profile, cross-skill sharing, and reminder consent before enabling storage or reminders.

Risk: The skill is written for a Mainland China Chinese K12 learning context.

Mitigation: Localize curriculum assumptions, guardian-consent rules, reminder windows, and crisis/help resources before using it in other regions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-vocabulary-dna)
- [Vocabulary Radar Topics](references/vocabulary-radar-topics.md)
- [Vocabulary Shared Contract](shared/vocab.md)
- [Ebbinghaus Schedule](shared/ebbinghaus-schedule.md)
- [English Error Dimension Table](shared/english-error-dimension-table.md)
- [Platform Conventions](shared/platform-conventions.md)
- [Crisis Referral Protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured handoff guidance for vocabulary cards, profile updates, reminders, and reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queues one merged daily vocabulary card when reminder consent is enabled; otherwise responds in-session.]

## Skill Version(s):

2.1.10 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
