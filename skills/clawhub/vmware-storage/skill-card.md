## Description:

vmware-storage helps agents manage VMware storage tasks including datastore browsing and image scans, iSCSI target configuration, and vSAN health and capacity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect VMware datastores, scan for deployable images, manage iSCSI storage targets, and check vSAN health and capacity in vSphere or ESXi environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform state-changing storage operations against production vSphere or ESXi targets.

Mitigation: Require dry-run previews and explicit human approval for iSCSI changes, especially target removal.

Risk: Weak TLS settings could expose vCenter or ESXi connections to interception.

Mitigation: Set verify_ssl: true for real vCenter or ESXi targets and review certificate handling before installation.

Risk: Local credential and audit files may contain sensitive operational data.

Mitigation: Protect ~/.vmware-storage/.env and ~/.vmware/audit.db with least-privilege filesystem access and avoid storing plaintext secrets where possible.

Risk: Optional webhook configuration may disclose operational events outside the local environment.

Mitigation: Leave webhook settings empty or remove them unless outbound notifications are intentionally approved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-storage)
- [VMware Storage Homepage](https://github.com/vmware-skills/VMware-Storage)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Capabilities](references/capabilities.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured tool-output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CLI commands, MCP tool guidance, datastore or vSAN summaries, and configuration checks.]

## Skill Version(s):

1.8.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
