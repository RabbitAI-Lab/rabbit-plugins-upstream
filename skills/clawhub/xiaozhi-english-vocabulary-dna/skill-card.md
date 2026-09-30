## Description:

帮助中国 K12 学生按间隔重复复习英语词汇，生成每日到期词卡、课前预热内容和词汇学习报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, families, and educators use the skill to save English vocabulary, practice due words with one daily card, prepare for upcoming lessons, and review learning progress.

### Deployment Geography for Use:

Mainland China; other regions require localization of curriculum, consent, reminder windows, and crisis-referral channels before use.

## Known Risks and Mitigations:

Risk: Vocabulary profiles and daily reminders may expose a minor's learning activity or send unwanted messages.

Mitigation: Require consent before storing or sharing vocabulary and before reminders; allow viewing, deletion, and pausing, and limit reminders to one consolidated daily card.

Risk: China-specific curriculum, consent practices, reminder windows, and crisis contacts may be inappropriate elsewhere.

Mitigation: Deploy in a Chinese K12 context only, or localize those settings and referral channels before student use.

## Reference(s):

- [Vocabulary radar topic templates](artifact/references/vocabulary-radar-topics.md)
- [High-school vocabulary levels](artifact/references/english-hs-vocabulary.md)
- [Spaced review scheduling](artifact/shared/ebbinghaus-schedule.md)
- [Vocabulary consent and reminder conventions](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language vocabulary cards, lesson previews, and progress reports in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [At most one consolidated due-word card per day; reminders and vocabulary-profile storage require the relevant consent.]

## Skill Version(s):

2.8.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
