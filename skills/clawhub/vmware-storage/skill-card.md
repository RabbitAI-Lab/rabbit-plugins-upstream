## Description:

VMware Storage helps agents manage VMware vSphere storage tasks, including datastore browsing, deployable-image discovery, iSCSI target configuration, and vSAN health and capacity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers, platform engineers, and VMware operators use this skill to inspect datastores, find deployment images, configure iSCSI storage, and review vSAN health and capacity through CLI or MCP workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write-capable VMware storage operations, including iSCSI target changes that may affect host storage availability.

Mitigation: Use dry-run previews, require explicit operator confirmation, and rely on the documented audit and policy controls before executing write actions.

Risk: The setup examples include disabled TLS certificate verification while using privileged vCenter or ESXi credentials.

Mitigation: Set verify_ssl to true with trusted certificates and use least-privilege VMware service accounts for production targets.

Risk: Persistent .env credential storage can expose VMware passwords if local file access is compromised.

Mitigation: Prefer a real secret manager or process-injected environment variables, keep .env permissions at 600, and avoid ESXi root or broad administrator accounts.

Risk: The security verdict is suspicious because privileged infrastructure access and write-capable storage operations require production review.

Mitigation: Review the vmware-storage and vmware-policy packages before installation and validate the configured policy rules before connecting to production infrastructure.

## Reference(s):

- [VMware Storage homepage](https://github.com/vmware-skills/VMware-Storage)
- [Agent Guardrails](references/agent-guardrails.md)
- [VMware Storage Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and structured CLI or MCP results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include VMware datastore, iSCSI, and vSAN operation results; write-capable workflows should use dry-run previews and explicit confirmation.]

## Skill Version(s):

1.9.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
