## Description:

Audit/harden OpenClaw hosts: SSH, firewall, updates, exposure, backups, disk encryption, gateway security.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to audit OpenClaw host posture and plan staged hardening for SSH, firewall, updates, exposure, backups, disk encryption, and gateway security.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect SSH, firewall, disk encryption, update, or scheduled-audit changes can affect remote access or system behavior.

Mitigation: Review proposed changes carefully, confirm the active access path, and approve exact state-changing actions before execution.

Risk: Host audit outputs may reveal sensitive system configuration if shared broadly.

Mitigation: Keep reports scoped to the operator and avoid printing or exposing secrets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/healthcheck)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only checks are presented before any state-changing hardening steps; exact write actions require user approval.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
