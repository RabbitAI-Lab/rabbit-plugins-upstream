## Description: <br>
Schedule and manage recurring tasks with cron and systemd timers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operations engineers use this skill to write, manage, and debug recurring jobs with cron, systemd timers, one-off scheduling, timezone handling, monitoring, locking, and retry-safe patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduling examples can create persistent cron jobs, systemd timers, or queued one-off jobs that continue running after setup. <br>
Mitigation: Confirm the intended user or service account, periodically review active crontabs, timers, and queued jobs, and disable entries that are no longer needed. <br>
Risk: Crontab management commands can remove or replace existing schedules if copied without checking the current state. <br>
Mitigation: Back up existing crontabs before editing or installing new ones, and avoid destructive removal commands unless the goal is to delete all jobs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gitgoodordietrying/skills/cron-scheduling) <br>
- [Publisher profile](https://clawhub.ai/user/gitgoodordietrying) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash, cron, and systemd unit examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
