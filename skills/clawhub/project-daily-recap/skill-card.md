## Description: <br>
Project Daily Recap sends a scheduled daily project recap reminder through OpenClaw to WeCom or WeChat without relying on an LLM. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lynnsudo](https://clawhub.ai/user/lynnsudo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and project teams use this skill to schedule a daily recap prompt for project progress, next-day planning, and configurable checklist reminders. It is aimed at industrial automation, manufacturing, and similar project workflows that need reliable scheduled messaging without AI API dependencies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer can add a persistent cron job that runs the reminder script on a schedule. <br>
Mitigation: Inspect the cron line before installation and confirm it points to the intended local skill directory and reminder schedule. <br>
Risk: Reminder messages may be sent to hardcoded or default messaging recipients that are not controlled by the installer. <br>
Mitigation: Edit reminder.sh and config before use so the channel, account, and recipient are explicitly yours. <br>
Risk: Project details in TODAY_PROGRESS or TOMORROW_PLAN may be delivered to the configured messaging destination. <br>
Mitigation: Avoid putting sensitive project information in recap fields unless the delivery endpoint has been verified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lynnsudo/skills/project-daily-recap) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Installs or runs shell scripts that create scheduled reminder messages and write local logs.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
