## Description:

快樂刷牙俠，讓孩子愛上刷牙的歡樂計時器與打卡系統

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

Families and caregivers use this skill with children ages 2-6 to run a positive brushing timer, story or music mode, reminders, brushing logs, streaks, and sticker rewards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a child's brushing routine, nickname, reminder settings, and sticker history in local JSON files under ~/.bookshelf-plus/kids/.

Mitigation: Use a nickname instead of a real name and periodically delete ~/.bookshelf-plus/kids/ records when the history is no longer needed.

Risk: Recurring brushing reminders may be too broad or too frequent for a household's needs.

Mitigation: Narrow invocation phrases and review the generated reminder schedule before enabling recurring reminders.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xuan905/skills/happy-brushing-hero)
- [Publisher profile](https://clawhub.ai/user/xuan905)
- [README.md](README.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Terminal text, TTS-ready text, JSON records, and crontab command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes brushing logs, sticker records, reminder configuration, and reminder state under ~/.bookshelf-plus/kids/.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
