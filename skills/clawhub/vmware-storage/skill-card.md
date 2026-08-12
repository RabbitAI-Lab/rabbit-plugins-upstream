## Description:

Use this skill to manage VMware storage, including datastores, iSCSI targets, vSAN health and capacity, and deployable image discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect and administer VMware vSphere storage resources, including datastore browsing, iSCSI configuration, and vSAN health and capacity checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill administers VMware storage and can affect vCenter or ESXi storage configuration.

Mitigation: Install it only for agents that are intended to administer VMware storage and use a least-privilege vCenter or ESXi account.

Risk: TLS or authentication checks can be weakened during setup or diagnostics.

Mitigation: Use `verify_ssl: true` with trusted certificates in production and reserve `--skip-auth` for narrow diagnostic cases.

Risk: Storage operations may involve credentials and optional notification settings.

Mitigation: Store credentials through the documented environment-variable flow and confirm whether any webhook or notification setting is actually used before entering credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-storage)
- [Project homepage](https://github.com/vmware-skills/VMware-Storage)
- [Agent Guardrails](references/agent-guardrails.md)
- [VMware Storage Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run previews, audit-aware operational guidance, and configuration steps for local CLI or MCP use.]

## Skill Version(s):

1.8.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
