## Description:

VMware AIops helps agents manage VMware/vSphere/ESXi VM lifecycle operations, deployments, guest actions, cluster tasks, alarms, and infrastructure triage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to let an agent manage VMware/vSphere/ESXi VM lifecycle, deployment, guest operation, triage, and alarm workflows. It is intended for environments where VMware permissions and operational guardrails have already been scoped.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad VMware write authority can change or delete infrastructure on the first MCP call.

Mitigation: Run the server with a dedicated least-privilege VMware service account, use read-only RBAC unless writes are required, and add deny rules before enabling MCP writes.

Risk: Guest operations can run commands or move files using the supplied guest account.

Mitigation: Avoid privileged guest credentials and pass the least-privilege guest account that can complete the task.

Risk: Webhook notifications can expose internal operational data such as host names, IP addresses, user names, alarms, events, and connection errors.

Mitigation: Keep webhooks disabled unless needed and treat configured webhook destinations as recipients of internal operational data.

## Reference(s):

- [VMware AIops source repository](https://github.com/vmware-skills/VMware-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aiops)
- [Setup Guide](artifact/references/setup-guide.md)
- [Capabilities Reference](artifact/references/capabilities.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)
- [Investigation Protocol](artifact/references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide VMware CLI or MCP operations that return structured status; write effects depend on configured VMware and guest account permissions.]

## Skill Version(s):

1.9.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
