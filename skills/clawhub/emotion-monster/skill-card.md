## Description:

情緒小怪獸，幫助 2-6 歲孩童認識與表達情緒的互動工具。情緒卡片、情緒日記、情緒教練、情緒日曆，零責怪設計。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

Parents, caregivers, and child-facing agents use this skill to help children ages 2-6 recognize, name, record, and talk through emotions in Traditional Chinese. It provides emotion cards, a mood diary, an emotion first-aid coach, and an emotion calendar for guided emotional literacy activities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores sensitive child mood diary records locally at ~/.bookshelf-plus/kids/mood_diary.json without enough built-in privacy controls or deletion guidance.

Mitigation: Use it only on parent-controlled devices, restrict access to synced or backed-up folders, and manually delete diary records when they are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xuan905/skills/emotion-monster)
- [README.md](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Traditional Chinese terminal text with interactive prompts, ANSI-colored output, shell commands, and local JSON diary records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The mood diary stores records locally at ~/.bookshelf-plus/kids/mood_diary.json.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
