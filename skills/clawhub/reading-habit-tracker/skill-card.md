## Description:

閱讀習慣追蹤系統：目標設定（年目標/書單/頁數/時長）、進度追蹤、每週/每月分析報告、落後預警、視覺化統計。與 reading_progress.py（專注打卡）差異化：目標導向、計劃管理、深度數據分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage reading goals, book lists, reading sessions, progress dashboards, periodic reports, and alerts from a local command-line workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reading goals, book titles, notes, page counts, and session history are stored locally on the user's machine.

Mitigation: Install and use the skill only when local storage of this reading data is acceptable; review files under ~/.bookshelf-plus/habit_tracker/ as needed.

Risk: The suggested cron reminder can create recurring local agent activity.

Mitigation: Treat cron setup as opt-in and review the schedule and message before enabling it.

Risk: Remove and delete commands can alter local reading records, and some deletions may not ask for confirmation.

Mitigation: Use delete and remove commands carefully and keep backups of local tracker data when records matter.

## Reference(s):

- [Server-resolved source repository](https://github.com/xuan905/reading-habit-tracker)
- [ClawHub skill release page](https://clawhub.ai/xuan905/skills/reading-habit-tracker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and local text reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores goals, sessions, book lists, and generated reports locally under ~/.bookshelf-plus/habit_tracker/.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
