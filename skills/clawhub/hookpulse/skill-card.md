## Description:

Helps agents monitor scheduled jobs and backups with HookPulse, configure alerts, and review check-ins and monitor status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wrpbr](https://clawhub.ai/user/wrpbr)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure HookPulse monitors for cron jobs, backups, webhooks, and scheduled workflows, signal run outcomes, and inspect alerts and check-ins.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creating or deleting monitors or sending check-ins without approval can change alerting behavior.

Mitigation: Confirm with the user before creating, deleting, or signaling monitors.

Risk: Exposed guest tokens or monitor IDs can let others access or falsely check in monitors.

Mitigation: Keep guest tokens and monitor IDs out of public logs and shared messages.

Risk: Using remote monitoring for unrelated cron or backup troubleshooting can cause unintended external activity.

Mitigation: Use this skill for such tasks only when the user wants remote monitoring.

## Reference(s):

- [HookPulse API reference](https://hookpulse.net/llms-full.txt)
- [HookPulse API discovery](https://hookpulse.net/api/)
- [HookPulse skill release](https://clawhub.ai/wrpbr/skills/hookpulse)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide monitor setup steps, check-in commands, and status summaries.]

## Skill Version(s):

1.0.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
