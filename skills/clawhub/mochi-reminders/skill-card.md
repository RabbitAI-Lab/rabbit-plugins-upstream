## Description:

Create one-time or recurring reminders, inspect job IDs, timing and delivery accounts, and update or pause schedules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to create, inspect, change, pause, or remove one-time and recurring reminders with explicit timezones and delivery recipients. The skill reports scheduler IDs, timing, destination, and status based on verified scheduler receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reminder may run at the wrong time or reach the wrong destination if its timezone, frequency, account, or recipient is mistaken.

Mitigation: Confirm the timezone, frequency, account, and recipient before scheduling.

Risk: Recurring reminders continue until paused or removed and may incur configured service costs.

Mitigation: Review recurring schedules and applicable service costs; pause or remove jobs when they are no longer needed.

Risk: A local receipt may not reflect the scheduler's current state.

Mitigation: Treat the native scheduler as authoritative and verify current job state before reporting changes or delivery.

## Reference(s):

- [ClawHub release](https://clawhub.ai/hznetnewpower/skills/mochi-reminders)
- [MochiLab](https://mochilab.bz)
- [Input contract](references/input.md)
- [Native scheduling integration](references/scheduling.md)
- [OpenClaw automation CLI documentation](https://docs.openclaw.ai/cli/cron)
- [OpenClaw job management documentation](https://docs.openclaw.ai/automation/cron-jobs/managing-jobs)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Natural-language responses and structured JSON scheduling plans or receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the scheduler job ID, timezone, next run, destination, and status when available.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
