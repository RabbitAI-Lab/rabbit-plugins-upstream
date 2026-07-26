## Description: <br>
Calendar Reminder scans Outlook calendar events each night, schedules time-based Feishu reminders for the next day, and reports the scan results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers use this skill to automate daily Outlook calendar scanning and send Feishu reminders for upcoming meetings, cross-time-zone events, and team schedule summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads Outlook meeting metadata and sends reminders or summaries to a configured Feishu user or group. <br>
Mitigation: Confirm that the selected Feishu recipient is appropriate for private or customer meetings, and use the narrowest practical target. <br>
Risk: The skill can keep running after setup through a scheduled cron job. <br>
Mitigation: Verify the cron schedule before deployment and document how to list, pause, resume, or remove the reminder job. <br>
Risk: The generated workflow depends on a separate calendar_reminder.py implementation that is not included in the artifact evidence. <br>
Mitigation: Review the actual script implementation before deployment, especially calendar access, Feishu delivery, error handling, and credential handling. <br>
Risk: Early morning events can produce reminders during quiet hours if the fixed two-hour lead time is used directly. <br>
Mitigation: Add or confirm quiet-hour handling so overnight reminders are delayed or bundled into an acceptable morning notification. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/calendar-reminder) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON result examples, code snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May register recurring cron jobs and send Feishu notifications based on Outlook calendar metadata.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter lists 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
