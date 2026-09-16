## Description:

Governed TrueNAS SCALE storage operations for health checks, diagnostics, ZFS pool and dataset inspection, snapshots, disks, alerts, services, replication, cloud-sync tasks, and audited write actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers, storage operators, and agents use this skill to triage and operate a TrueNAS SCALE appliance through guided CLI or MCP workflows. It is intended for TrueNAS-specific pool health, capacity, dataset, snapshot, disk, alert, service, replication, and cloud-sync tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact TrueNAS storage writes, including irreversible snapshot deletion and service restarts.

Mitigation: Use a dedicated least-privilege or read-only TrueNAS API key where possible, confirm identifiers from list tools before writes, and use dry-run and CLI double confirmation for destructive operations.

Risk: The security review notes reliance on external package code and account or prompt controls rather than an enforced in-tool approval gate.

Mitigation: Review package provenance before deployment, restrict the connected account's permissions, and keep write authorization policy in the agent or operating workflow.

Risk: API keys and the master password can be exposed if pasted into shell history or long-lived environments.

Mitigation: Prefer the interactive secret prompt, avoid placing secrets directly in commands, and use the encrypted local secret store described by the setup guide.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/truenas-aiops)
- [Project Homepage](https://github.com/AIops-tools/TrueNAS-AIops)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup and Security Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool-use guidance, dry-run recommendations, and risk-aware operational steps.]

## Skill Version(s):

0.11.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
