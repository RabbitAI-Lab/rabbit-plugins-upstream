## Description: <br>
定时大师 is a platform-level scheduling guide that helps agents choose between heartbeat and cron scheduling, configure push or silent payloads, use strict reminder templates, manage self-wake behavior, lock time zones, and migrate legacy cron patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agent builders use this skill to design reliable scheduled reminders, background logs, self-wake flows, and cron migration patterns on platforms that expose cron-style agent tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents with local shell or scheduler-admin access could alter persistent cron state while following scheduler maintenance guidance. <br>
Mitigation: Use the skill only for explicit scheduling work, prefer supported platform recovery tools, and require a backup before any direct `jobs.json` cleanup. <br>
Risk: Reminder delivery can target the wrong recipient or time if delivery fields or time zones are not confirmed. <br>
Mitigation: Confirm recipients, channels, and time zones before creating reminders, and use ISO 8601 timestamps with explicit time-zone context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cron-master-pro) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces scheduling decisions, payload templates, checklist guidance, and troubleshooting steps; it does not directly execute scheduler changes by itself.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
