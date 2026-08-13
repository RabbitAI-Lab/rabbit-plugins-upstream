## Description:

truenas-aiops helps agents operate TrueNAS SCALE storage through governed diagnostics, read workflows, and controlled write actions for pools, datasets, snapshots, disks, alerts, services, replication, and cloud-sync tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Storage administrators, developers, and operators use this skill to triage TrueNAS SCALE appliances, inspect ZFS health and capacity, manage snapshots and datasets, review alerts, and run selected governed maintenance actions. It is intended for explicitly TrueNAS SCALE contexts and excludes other NAS, backup, hypervisor, container, and network-device operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact TrueNAS storage writes and evidence.security reports no enforced read-only mode or approval gate.

Mitigation: Install only when agent access to a TrueNAS API key is acceptable; use a least-privilege or read-only TrueNAS account by default and enable write permissions only for intentional maintenance sessions.

Risk: Credential exposure could affect the configured TrueNAS appliance.

Mitigation: Use the encrypted secret store, migrate legacy plaintext environment keys, avoid long-lived master passwords in shell environments, and keep API keys scoped to the minimum required privileges.

Risk: Snapshot deletion and some service actions can disrupt storage operations.

Mitigation: Use dry-run previews and explicit operator review for write actions, especially snapshot deletion, dataset creation, scrubs, service restart, and undo operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/truenas-aiops)
- [TrueNAS AIops homepage](https://github.com/AIops-tools/TrueNAS-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI examples and MCP tool-call outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational guidance for TrueNAS SCALE and may direct governed CLI or MCP actions.]

## Skill Version(s):

0.10.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
