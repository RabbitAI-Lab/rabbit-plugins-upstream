## Description:

Helps agents identify server changes and check system health, Docker, backups, and Proxmox through Homebutler.

This skill is ready for commercial/non-commercial use.

## Publisher:

[higangssh](https://clawhub.ai/user/higangssh)

### License/Terms of Use:

MIT-0

## Use Case:

Server administrators and developers use this skill to review changes and health across configured servers, inspect Docker and backups, and request scoped maintenance or Proxmox actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server scans and diagnostic results may expose hostnames, internal addresses, ports, or log contents.

Mitigation: Limit reads to the requested hosts, seek approval for broad scans, and summarize sensitive results instead of sharing raw output.

Risk: Write, restore, purge, service, and Proxmox power actions can change or delete operational data.

Mitigation: Require explicit operator approval for the specific target and action before execution; review configuration and backups first.

Risk: Configured SSH access and tokens can grant control over monitored servers and Proxmox guests.

Mitigation: Review Homebutler configuration, tokens, and SSH access before installation and use.

## Reference(s):

- [Homebutler on ClawHub](https://clawhub.ai/higangssh/skills/homebutler)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with optional structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarized changes, findings, and suggested actions; command results can be requested as JSON.]

## Skill Version(s):

2.4.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
