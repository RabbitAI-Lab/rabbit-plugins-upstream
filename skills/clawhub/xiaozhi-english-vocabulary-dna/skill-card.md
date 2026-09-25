## Description:

帮助中小学生收集英语词汇、安排间隔复习，并生成每日词卡、课前预热内容及词汇学习报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese primary and middle school learners use the skill to build an English vocabulary list, review due words with spaced-repetition cards, and prepare for upcoming lessons. Younger learners use it with a parent or teacher present.

### Deployment Geography for Use:

China mainland by default; use elsewhere requires adapting school standards, privacy practices, and crisis contacts to the local context.

## Known Risks and Mitigations:

Risk: A learner's vocabulary history or learning profile could be stored or shared without authorization.

Mitigation: Obtain learner or guardian consent before profile storage or cross-skill sharing, and honor viewing, correction, deletion, and sharing controls.

Risk: Reminders or OCR imports could be used without the learner's or guardian's consent.

Mitigation: Enable reminders and photo-based import only with consent; otherwise use in-session review and pasted or typed word lists.

Risk: School standards, privacy expectations, or crisis contacts may be inappropriate outside China mainland.

Mitigation: Localize curricula, privacy requirements, and emergency resources before deployment in other regions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-vocabulary-dna)
- [Vocabulary radar topic templates](references/vocabulary-radar-topics.md)
- [Spaced review schedule](shared/ebbinghaus-schedule.md)
- [Vocabulary and consent conventions](shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language text and Markdown vocabulary cards, practice prompts, and progress summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One consolidated due-word card per day; reminders depend on consent and a separate reminder service.]

## Skill Version(s):

2.4.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
