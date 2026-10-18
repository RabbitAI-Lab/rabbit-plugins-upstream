## Description:

Helps operators inspect, diagnose, and manage Proxmox VE virtual machines, containers, storage, and clusters through CLI and MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and developers use this skill to inspect Proxmox VE health and carry out VM, container, backup, and storage operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable tools can change or delete Proxmox workloads without an internal approval gate.

Mitigation: Require external approval before enabling writes against important workloads; use read-only permissions unless writes are necessary.

Risk: Broad credentials or exposed local configuration could permit unintended infrastructure changes.

Mitigation: Use a dedicated least-privilege Proxmox API token, avoid broad root@pam credentials, and protect ~/.proxmox-aiops/.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/proxmox-aiops)
- [Project homepage (skill metadata)](https://github.com/AIops-tools/Proxmox-AIops)
- [Setup guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Capabilities](artifact/references/capabilities.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline commands and tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read operations report cluster and guest status; write operations may return asynchronous task identifiers.]

## Skill Version(s):

0.15.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
