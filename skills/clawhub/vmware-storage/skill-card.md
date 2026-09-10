## Description:

Helps agents manage VMware storage tasks across datastores, iSCSI targets, and vSAN clusters, including datastore browsing, deployable image scans, iSCSI configuration, and vSAN health and capacity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and platform engineers use this skill to inspect VMware storage inventory, find deployable datastore images, manage iSCSI adapter targets, and review vSAN health and capacity. It is intended for storage-focused VMware operations rather than VM lifecycle, NSX networking, Kubernetes, or load-balancing tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect and change VMware storage configuration.

Mitigation: Install it only for agents expected to manage VMware storage, use least-privilege vSphere accounts, and require operator approval for state-changing workflows.

Risk: Stored target credentials may expose vCenter or ESXi access if file permissions are weak.

Mitigation: Keep ~/.vmware-storage/.env at owner-only permissions and prefer injected secrets for production deployments.

Risk: Audit logs can reveal infrastructure names, targets, parameters, and operation history.

Mitigation: Protect ~/.vmware/audit.db with appropriate local filesystem controls and operational retention practices.

Risk: Production vSphere connections may be vulnerable to trust issues if TLS verification is disabled.

Mitigation: Enable per-target TLS certificate verification for production targets where valid certificates are available.

Risk: Removing an iSCSI send target can make dependent LUNs and VMs inaccessible.

Mitigation: Use dry-run previews, verify no LUNs behind the target are in active use, and require explicit confirmation before removal.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-storage)
- [Project homepage](https://github.com/vmware-skills/VMware-Storage)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured VMware storage results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON-like tool results for datastore, iSCSI, and vSAN queries.]

## Skill Version(s):

1.8.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
