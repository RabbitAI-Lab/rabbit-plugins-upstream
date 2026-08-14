## Description:

Nutanix AIops helps agents operate Nutanix Prism Central v4 estates for health checks, inventory, VM lifecycle, storage, networking, data protection, alerts, LCM upgrades, capacity forecasting, and RCA workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators, SREs, platform engineers, and agents use this skill to inspect and manage Nutanix Prism Central environments, including clusters, VMs, storage, networking, data protection, alerts, upgrades, capacity, and RCA workflows. It is intended for Nutanix Prism Central v4 estates and should not be used for non-Nutanix platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact Nutanix infrastructure changes without a built-in read-only mode or approval gate.

Mitigation: Start with a read-only Prism Central account and require an external approval process before allowing destructive, LCM, or DR actions.

Risk: Credentials and local audit state are stored under ~/.nutanix-aiops and may be exposed on shared machines or in automation logs.

Mitigation: Isolate the ~/.nutanix-aiops state directory, protect the master password, and avoid putting NUTANIX_AIOPS_MASTER_PASSWORD in shared shells or CI logs.

Risk: Destructive operations such as VM deletion, snapshot restore, PD failover, storage deletion, and LCM updates can affect production availability.

Mitigation: Use dry-run previews, CLI double confirmation where available, read-only accounts during evaluation, and operator review for high-risk actions.

## Reference(s):

- [Nutanix AIops ClawHub Skill](https://clawhub.ai/zw008/skills/nutanix-aiops)
- [Nutanix AIops Repository](https://github.com/AIops-tools/Nutanix-AIops)
- [Capabilities Reference](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup and Security Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured tool results with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Nutanix Prism Central operational summaries, RCA findings, task references, dry-run previews, and audit-oriented guidance.]

## Skill Version(s):

0.10.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
