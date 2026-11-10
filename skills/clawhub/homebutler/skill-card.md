## Description:

Tells an agent what changed on a server since it last looked - plus status, Docker, backups, Proxmox. Every tool is classed read, write or destructive, so an agent can tell a look from a change before it makes the call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[higangssh](https://clawhub.ai/user/higangssh)

### License/Terms of Use:

MIT-0

## Use Case:

System administrators and operators use this skill to review changes and health across servers, Docker workloads, backups, and Proxmox, then carry out requested management actions with their effects clearly classified.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server reads can expose internal addresses, listening ports, usernames, host paths, and log contents; management actions can change services or data.

Mitigation: Limit reads to the requested hosts and summarize sensitive results. Confirm the specific target and requested change before write actions, and require explicit operator authorization for destructive actions.

Risk: The security review reports capabilities for application management, server trust, service installation, and deployment, and notes that several local references were unavailable for full assessment.

Mitigation: Review the targets, credentials, and effects of these operations before enabling them, and assess the missing references as part of installation review.

## Reference(s):

- [Homebutler on ClawHub](https://clawhub.ai/higangssh/skills/homebutler)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Text summaries and structured JSON, with shell commands and configuration guidance for supported operations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include server status, change reports, findings, suggested actions, and management commands.]

## Skill Version(s):

2.7.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
