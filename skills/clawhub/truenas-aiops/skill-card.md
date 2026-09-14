## Description:

truenas-aiops helps agents inspect and operate TrueNAS SCALE storage with health, diagnostic, ZFS pool, dataset, snapshot, disk, alert, service, replication, and cloud-sync workflows under audit and risk-tier controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers, storage administrators, and operations engineers use this skill to triage and operate a TrueNAS SCALE appliance through CLI or MCP workflows, including read-only diagnostics and governed write operations such as scrub starts, dataset creation, snapshot changes, service restarts, and undo application.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can exercise high-impact storage authority when connected with a TrueNAS account that has write permissions.

Mitigation: Use a read-only or least-privilege TrueNAS API key unless write operations are intentionally required.

Risk: Weak approval controls can allow an agent to attempt destructive or disruptive operations such as snapshot deletion or service restart.

Mitigation: Require explicit operator authorization in the calling agent, use dry-run previews, and rely on CLI double confirmation for supported destructive commands.

Risk: Credential handling and transport choices can expose NAS credentials if configured carelessly.

Mitigation: Keep TLS verification enabled in production, avoid long-lived plaintext master passwords in environment variables, and use the encrypted secret store.

Risk: Installing an unpinned or unverified package could place NAS credentials and destructive operations under unreviewed code.

Mitigation: Pin or verify the installed package version before trusting it with TrueNAS credentials or write-capable operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/truenas-aiops)
- [Project Homepage](https://github.com/AIops-tools/TrueNAS-AIops)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and tool-use instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe CLI commands, MCP tool usage, TrueNAS diagnostic findings, dry-run workflows, audit behavior, and setup configuration.]

## Skill Version(s):

0.11.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
