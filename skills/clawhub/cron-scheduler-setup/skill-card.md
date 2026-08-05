## Description: <br>
Cron Scheduler Setup helps agents configure one-time reminders, recurring cron jobs, and background automation with optional chat or webhook delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and automation-focused agent users use this skill to create scheduled reminders, recurring tasks, and workflow jobs for SkillHub Gateway-style agent environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduled jobs can persist in the background and repeat actions after the initial setup. <br>
Mitigation: Confirm the schedule, task contents, and deletion or listing command before enabling each job. <br>
Risk: Scheduled outputs can be delivered to external channels such as Telegram, WhatsApp, or webhooks. <br>
Mitigation: Verify the destination, message contents, and privacy implications before enabling external delivery. <br>
Risk: Isolated-session jobs may summarize or process private email, calendar, account, or business data repeatedly. <br>
Mitigation: Avoid scheduling sensitive-data summaries unless the user explicitly intends repeated processing and delivery. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cron-scheduler-setup) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash command examples and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include scheduled job names, cron expressions, time zones, delivery destinations, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
