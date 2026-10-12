## Description:

Helps Chinese-speaking teams manage a local task ledger and generate workday-aware reminder guidance, with scheduling and delivery handled by an external integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[djoldwang](https://clawhub.ai/user/djoldwang)

### License/Terms of Use:

MIT-0

## Use Case:

Teams use this skill to create, update, search, archive, and export tasks in a local ledger and to prepare reminders against a China workday calendar. A trusted integration must handle identity, permissions, scheduling, and notification delivery.

### Deployment Geography for Use:

Global; default workday calendar covers mainland China for 2025–2026.

## Known Risks and Mitigations:

Risk: Task and backup data persist on disk and could be exposed by overly broad file access.

Mitigation: Restrict writes to one trusted local task directory and a separately designated calendar directory.

Risk: The skill does not authenticate team members or authorize notification recipients.

Mitigation: Enforce identity, task permissions, and delivery authorization in the trusted integration.

Risk: Built-in workday calendars cover mainland China only for 2025–2026, and reminder text is currently Chinese.

Mitigation: Maintain missing calendar years from official announcements and use a trusted localization layer where needed.

## Reference(s):

- [ClawHub release](https://clawhub.ai/djoldwang/skills/team-tasks)
- [Safe storage and integration](artifact/references/storage.md)
- [Reminder adapter contract](artifact/references/reminder-adapters.md)
- [Annual calendar maintenance](artifact/references/calendar-maintenance.md)
- [2025 China holiday schedule source](https://www.forestry.gov.cn/c/www/szxx/594663.jhtml)
- [2026 China holiday schedule source](https://www.beijing.gov.cn/zhengce/zhengcefagui/202511/t20251104_4258873.html)

## Skill Output:

**Output Type(s):** [Text, JSON, CSV, Guidance]

**Output Format:** [Chinese-language text and structured task or reminder data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task changes persist locally; reminders are prepared but not sent by this skill.]

## Skill Version(s):

1.5.1 (source: skill metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
