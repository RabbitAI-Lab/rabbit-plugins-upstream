## Description:

VMware AIops helps agents manage VMware/vSphere/ESXi VM lifecycle, deployment, guest operations, cluster changes, alarms, and triage workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to investigate and operate VMware, vSphere, and ESXi environments, including VM lifecycle actions, deployments, guest operations, cluster administration, alarm handling, and health triage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP tools can immediately modify or delete VMware infrastructure when supplied credentials allow it.

Mitigation: Use a dedicated least-privilege service account, configure deny rules for production, avoid unattended exposure of MCP write tools, and prefer CLI dry-run and confirmation flows for destructive changes.

Risk: Guest command execution can run commands inside VMs with the supplied guest credentials.

Mitigation: Omit guest credentials unless guest operations are required and restrict guest accounts to the minimum permissions needed.

Risk: Monitoring or triage workflows may not require state-changing access.

Mitigation: Prefer vmware-monitor or read-only vCenter roles for monitoring-only use cases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aiops)
- [VMware AIops homepage](https://github.com/vmware-skills/VMware-AIops)
- [Setup Guide](references/setup-guide.md)
- [Capabilities Reference](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Investigation Protocol](references/investigation-protocol.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to execute CLI commands or MCP tools against configured VMware targets.]

## Skill Version(s):

1.8.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
