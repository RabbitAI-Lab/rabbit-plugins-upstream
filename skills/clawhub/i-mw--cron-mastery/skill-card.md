## Description: <br>
Master OpenClaw's timing systems. Use for scheduling reliable reminders, setting up periodic maintenance (janitor jobs), and understanding when to use Cron vs Heartbeat for time-sensitive tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[i-mw](https://clawhub.ai/user/i-mw) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, agent operators, and OpenClaw users use this skill to schedule reliable reminders, recurring jobs, and maintenance tasks with cron instead of heartbeat-based polling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ready-to-copy examples include hard-coded external delivery targets. <br>
Mitigation: Replace all Telegram IDs and external delivery settings with user-approved destinations before scheduling jobs. <br>
Risk: Recurring task examples can read email or send summaries externally. <br>
Mitigation: Require explicit user approval before any scheduled job accesses email or sends summaries outside the current session. <br>
Risk: Maintenance and recovery guidance can remove cron jobs or cron state. <br>
Mitigation: Run cleanup with a preview or narrow scope, and back up cron state before any manual jobs.json deletion. <br>


## Reference(s): <br>
- [Cron Examples & Templates](references/templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, code] <br>
**Output Format:** [Markdown guidance with JSON cron job examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Examples may include delivery targets, email access, and maintenance actions that should be reviewed before use.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
