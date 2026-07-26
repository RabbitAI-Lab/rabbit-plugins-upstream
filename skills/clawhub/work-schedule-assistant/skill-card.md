## Description: <br>
Automatically saves work schedules, meetings, tasks, and related attachments into a persistent local schedule ledger and generates daily work reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liqiang12689](https://clawhub.ai/user/liqiang12689) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and professionals use this skill to capture work commitments from chat, maintain a local schedule ledger with attachments, query upcoming or overdue items, and receive daily reminders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Work schedule records and copied attachments are retained in a local ledger. <br>
Mitigation: Confirm the local storage location before use, configure WORK_SCHEDULE_HOME when needed, and avoid storing credentials or sensitive identity documents in schedule items. <br>
Risk: Daily reminders can announce schedule information to a configured chat or channel. <br>
Mitigation: Only run reminder setup after confirming the intended channel, recipient, time, and timezone. <br>
Risk: Attachments may include untrusted files or links. <br>
Mitigation: Keep attachments as copied files or HTTP/HTTPS links only; do not execute, unzip, or automatically open attached content. <br>


## Reference(s): <br>
- [Work Schedule Assistant ClawHub release page](https://clawhub.ai/liqiang12689/skills/work-schedule-assistant) <br>
- [Attachment handling guide](references/attachment-handling.md) <br>
- [Daily reminder setup guide](references/setup-reminder.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Markdown and plain text responses with JSON and Markdown files managed by helper scripts and shell commands for schedule operations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Persists schedule.json, 工作日程.md, history.jsonl, and optional attachment copies under the configured local schedule directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
