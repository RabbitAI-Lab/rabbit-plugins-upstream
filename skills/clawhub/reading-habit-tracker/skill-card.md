## Description:

閱讀習慣追蹤系統：目標設定（年目標/書單/頁數/時長）、進度追蹤、每週/每月分析報告、落後預警、視覺化統計。與 reading_progress.py（專注打卡）差異化：目標導向、計劃管理、深度數據分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to set reading goals, manage a reading list, log sessions, and review weekly or monthly progress reports with lag alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create and update local reading-tracker JSON files under ~/.bookshelf-plus/habit_tracker/.

Mitigation: Review proposed commands before running state-changing actions such as setting goals, logging sessions, deleting records, or removing books.

Risk: The optional cron reminder can schedule recurring reading alerts.

Mitigation: Add the cron reminder only when scheduled prompts are desired, and adjust the timezone and message before enabling it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xuan905/skills/reading-habit-tracker)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and terminal text with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates local JSON reading-tracker files under ~/.bookshelf-plus/habit_tracker/ when state-changing scripts are run.]

## Skill Version(s):

1.0.1 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
