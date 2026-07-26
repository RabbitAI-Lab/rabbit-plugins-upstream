## Description: <br>
Fix common cron job failures in Clawdbot/Moltbot, including message delivery issues, tool timeouts, timezone bugs, and model fallback problems. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[promadgenius](https://clawhub.ai/user/promadgenius) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and Clawdbot/Moltbot operators use this skill to diagnose scheduled messaging failures and create more reliable cron jobs with explicit timezones, isolated sessions, delivery flags, and debugging checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shell commands can create, run, remove, or alter live scheduled bot jobs. <br>
Mitigation: Review commands before execution and confirm job names, schedules, timezones, recipients, messages, and delivery channels. <br>
Risk: Troubleshooting commands may expose private operational details in log output. <br>
Mitigation: Treat cron and gateway logs as private and avoid sharing sensitive chat IDs, recipients, or message contents. <br>
Risk: Gateway restart and cron removal commands can interrupt active bot behavior. <br>
Mitigation: Run restart or removal commands deliberately, preferably after identifying the affected job and expected service impact. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/promadgenius/skills/ez-cronjob) <br>
- [Clawdbot Cron Documentation](https://docs.molt.bot/tools/cron) <br>
- [Timezone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) <br>
- [Cron Expression Generator](https://crontab.guru/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes cron flags, troubleshooting checks, working examples, and operational cautions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
