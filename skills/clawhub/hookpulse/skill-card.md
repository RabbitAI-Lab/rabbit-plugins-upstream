## Description:

Helps agents set up and manage HookPulse monitoring for scheduled jobs, backups, webhooks, and GitHub Actions workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wrpbr](https://clawhub.ai/user/wrpbr)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to create monitors, send job check-ins, inspect missed or failed runs, and configure alerts for scheduled work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using HookPulse sends monitoring data to an external service.

Mitigation: Install only if using hookpulse.net as the monitoring backend is acceptable.

Risk: Exposed guest tokens, setup keys, or monitor IDs can compromise monitor access or check-ins.

Mitigation: Treat these values as credentials and keep them out of public logs and issues.

Risk: Creating many monitors or adding alert destinations may incur charges.

Mitigation: Review billing before expanding monitors or alerts; leave purchases to the user.

## Reference(s):

- [HookPulse skill on ClawHub](https://clawhub.ai/wrpbr/skills/hookpulse)
- [HookPulse API discovery](https://hookpulse.net/api/)
- [HookPulse full reference](https://hookpulse.net/llms-full.txt)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include monitor state and check-in results; redact credentials and monitor IDs from shared output.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
