## Description:

VMware AIops helps agents manage VMware vSphere and ESXi virtual machine lifecycle, deployment, guest operations, cluster changes, alarms, and investigation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators, platform engineers, and agent developers use this skill to perform VMware VM lifecycle operations, deploy lab or workload VMs, triage cluster health, investigate VM, host, and datastore issues, and manage alarms with approval gates for state-changing work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform powerful VMware infrastructure administration actions, including deletes, snapshot reverts, cluster changes, guest commands, and batch operations.

Mitigation: Use a dedicated least-privilege VMware account, configure policy deny rules for production writes, and require explicit human approval before these operations.

Risk: Production connections can be weakened if TLS verification is disabled.

Mitigation: Keep TLS verification enabled for production and reserve verify_ssl=false only for isolated lab environments with self-signed certificates.

Risk: Webhook notifications can send operational alert metadata to configured destinations.

Mitigation: Review webhook destinations before enabling them and keep notifications limited to user-controlled endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aiops)
- [VMware AIops source homepage](https://github.com/vmware-skills/VMware-AIops)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Investigation protocol](references/investigation-protocol.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and MCP tool-call recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce offline HTML snapshots through the vmware-aiops CLI when users request report output.]

## Skill Version(s):

1.8.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
