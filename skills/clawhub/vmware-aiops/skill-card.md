## Description:

Use this skill to manage VMware, vSphere, and ESXi VM lifecycle operations, deployments, guest operations, clusters, alarms, and investigation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and infrastructure engineers use this skill to operate VMware environments from an agent, including VM lifecycle work, deployment, cluster changes, guest commands, alarm handling, and triage before remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform infrastructure-changing VMware operations, and some write actions can run without a built-in confirmation step.

Mitigation: Install with a dedicated least-privilege VMware service account, add deny rules before production use, and require operator review for writes such as reconfigure, clone, deploy, cluster changes, alarm reset, and plan apply.

Risk: Guest execution and upload operations can run commands or copy files with the supplied guest credentials.

Mitigation: Use least-privilege guest accounts, avoid root or administrator credentials unless necessary, and review the exact command, file path, and target VM before approving execution.

Risk: Destructive or broad-scope actions such as power-off, delete, migration, snapshot changes, TTL deletion, and alarm reset can affect availability or clear more than one object.

Mitigation: Inspect preview or blast-radius output when available, confirm target names and scopes, and re-check final state after execution.

Risk: Webhook notifications and diagnostics may expose operational metadata such as host names, IP addresses, user names, alarm text, event messages, or connection errors.

Mitigation: Enable webhooks only to trusted destinations and treat notifications as operational data.

Risk: Disabling TLS verification can expose connections to interception outside isolated lab environments.

Mitigation: Keep TLS verification enabled in production and use CA-signed certificates for vCenter or ESXi endpoints.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-aiops)
- [Project Homepage](https://github.com/vmware-skills/VMware-AIops)
- [Capabilities Reference](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to call VMware CLI or MCP tools that read or change infrastructure state.]

## Skill Version(s):

1.12.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
