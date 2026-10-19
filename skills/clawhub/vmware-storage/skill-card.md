## Description:

Helps operators inspect VMware datastores, iSCSI storage, vSAN health, and Fibre Channel paths, with gated storage changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Storage administrators and engineers use this skill to inspect vSphere datastores, iSCSI targets, vSAN clusters, and Fibre Channel paths, and to perform approved iSCSI changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Storage changes could interrupt access to datastores or LUNs.

Mitigation: Restrict installation to storage administrators, use least-privilege vSphere accounts, prefer read-only access, and review and confirm writes before execution.

Risk: Stored vSphere credentials could be exposed.

Mitigation: Keep ~/.vmware-storage/.env out of backups and repositories; prefer secret-manager injection where possible.

Risk: Optional HTTPS MCP exposure could grant unauthorized storage access.

Mitigation: Do not expose HTTPS MCP without tokens, TLS, and network controls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-storage)
- [Project homepage (listed in skill metadata; provenance unverified)](https://github.com/vmware-skills/VMware-Storage)
- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples and storage findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only diagnostics and gated, audited iSCSI changes]

## Skill Version(s):

2.4.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
