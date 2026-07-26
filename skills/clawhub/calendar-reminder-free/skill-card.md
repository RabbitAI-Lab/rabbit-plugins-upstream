## Description: <br>
Calendar Reminder Free helps personal developers scan tomorrow's Outlook calendar each night, schedule Feishu reminders for morning and afternoon events, and register the workflow with skill-platform cron. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal developers use this skill to preview the next day's Outlook schedule and receive basic Feishu reminders before morning meetings and at midday for afternoon events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uses tomorrow's Outlook meeting details to create Feishu reminders, which may expose private calendar information to the configured reminder channel. <br>
Mitigation: Install only for calendars and Feishu targets where this data sharing is acceptable, and review the configured recipient before enabling scheduled reminders. <br>
Risk: A daily persistent cron job can continue running after the user no longer wants reminders. <br>
Mitigation: Pause, remove, or audit the registered cron task when the workflow is no longer needed. <br>
Risk: A generic API_KEY setting could be configured unnecessarily and broaden credential exposure. <br>
Mitigation: Do not configure a generic API_KEY unless the actual agent setup requires it for this workflow. <br>


## Reference(s): <br>
- [Calendar Reminder Free on ClawHub](https://clawhub.ai/thcjp/skills/calendar-reminder-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns task status, schedule summary, execution logs, error details, and setup guidance for cron and Feishu reminder configuration.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
