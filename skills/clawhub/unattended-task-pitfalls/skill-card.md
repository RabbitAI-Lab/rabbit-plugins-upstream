## Description:

Hardening playbook for AI agent unattended and scheduled tasks, covering background execution, artifact verification, isolated-session context limits, notification design, and self-healing retries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mowenqwq](https://clawhub.ai/user/mowenqwq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when designing, hardening, or debugging unattended agent jobs such as cron tasks, scheduled backups, auto-reports, and artifact pipelines. It helps agents turn operational lessons into enforceable checks for validation, retry behavior, notification quality, and context-sensitive scheduled decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Detached background commands can continue after a gateway or session timeout, so blind retries may duplicate destructive, publishing, upload, or deletion operations.

Mitigation: Before retrying, check process state, artifact timestamps, logs, and idempotency; add explicit stop procedures, time limits, and clear operator notification for detached jobs.

Risk: Scheduled artifact pipelines can propagate corrupt or partial files if they upload or mark success before validation completes.

Mitigation: Validate archives locally before upload, skip state updates on failure, verify existing artifacts before reuse, and leave failed runs eligible for the next scheduled retry.

Risk: Isolated scheduled sessions may make incorrect decisions when they assume access to the main agent conversation or memory context.

Mitigation: Ground scheduled decisions in available filesystem evidence, explicit exclusion rules for automatic artifacts, and documented time attribution rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mowenqwq/skills/unattended-task-pitfalls)
- [Publisher profile](https://clawhub.ai/user/mowenqwq)
- [verify_archive.py](scripts/verify_archive.py)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and Python reference code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational hardening recommendations and reusable validation patterns for scheduled agent workflows.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
