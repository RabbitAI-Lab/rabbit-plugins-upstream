## Description:

Audit/harden OpenClaw hosts: SSH, firewall, updates, exposure, backups, disk encryption, gateway security.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw operators use this skill to review a host's security posture and receive evidence-based, staged hardening recommendations tailored to its operating system and access context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some ordinary OpenClaw doctor commands may migrate state or copy legacy configuration, and even read-only checks may create incidental logs or cache bookkeeping.

Mitigation: Use the documented read-only checks, interpret doctor --lint findings from its report, and reserve ordinary doctor commands and repairs for explicit approval.

Risk: Changes to SSH, firewall rules, or remote access could interrupt the operator's access to the host.

Mitigation: Confirm the access path first, recommend only when identity or role is unknown, and get approval for each exact state-changing action with rollback notes.

## Reference(s):

- [healthcheck on ClawHub](https://clawhub.ai/hillstreet-ph/skills/healthcheck)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Guidance]

**Output Format:** [Markdown report with findings, recommendations, and inline shell or PowerShell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and recommendations are tailored to confirmed host context and desired security posture.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
