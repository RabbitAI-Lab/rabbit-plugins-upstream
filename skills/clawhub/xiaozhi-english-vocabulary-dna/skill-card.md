## Description:

按间隔重复安排英语词汇复习，生成每日到期词卡，并支持课前词汇预热和按个人遗忘速度调整复习间隔。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向初中和高中英语学习者，用于收录词汇、按复习间隔生成每日词卡，并为新课词汇安排课前预热；小学高段学生须有家长或教师陪同。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved vocabulary and learning weaknesses are student learning records.

Mitigation: Keep record-saving and sharing off unless the student or guardian opts in; use the provided deletion and opt-out controls. Younger students require guardian involvement.

Risk: Companion storage and reminder services are outside this skill bundle.

Mitigation: Review those services separately before enabling their storage or reminder features.

## Reference(s):

- [English high school vocabulary reference](artifact/references/english-hs-vocabulary.md)
- [Vocabulary radar topics](artifact/references/vocabulary-radar-topics.md)
- [Spaced-repetition schedule](artifact/shared/ebbinghaus-schedule.md)
- [Vocabulary records and consent conventions](artifact/shared/vocab.md)
- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-vocabulary-dna)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese conversational text and Markdown vocabulary cards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized review prompts; reminders are consent-controlled and consolidated by the reminder service.]

## Skill Version(s):

2.12.6 (source: server release metadata, artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
