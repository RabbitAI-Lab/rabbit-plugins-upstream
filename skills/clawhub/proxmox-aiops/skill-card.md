## Description:

Manage Proxmox VE virtual machines and containers, inspect cluster health, and perform lifecycle, storage, backup, and diagnostic operations through CLI or MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure administrators use this skill to inspect Proxmox VE environments and manage VM and container lifecycles, snapshots, backups, storage, and cluster health.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic guidance can lead to disruptive Proxmox changes without clear user approval.

Mitigation: Start with a dedicated read-only token; require explicit agent approval before granting write permissions or making infrastructure changes. CLI confirmations do not cover MCP calls, and audit logs or undo records may not recover every destructive operation.

## Reference(s):

- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Project homepage](https://github.com/AIops-tools/Proxmox-AIops)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Structured tool results and concise text or Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write operations may return asynchronous task identifiers that need polling.]

## Skill Version(s):

0.16.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
