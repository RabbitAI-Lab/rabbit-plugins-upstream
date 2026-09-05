## Description:

VMware AIops helps agents manage VMware, vSphere, and ESXi VM lifecycle operations, deployments, guest operations, cluster administration, alarm handling, and infrastructure triage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators, platform engineers, and developers use this skill to let an agent administer VMware environments, including VM lifecycle work, deployment, migration, snapshots, guest operations, cluster tasks, alarms, and guided triage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent high-impact control over VMware infrastructure through MCP without built-in confirmation gates.

Mitigation: Use dedicated least-privilege vCenter accounts, configure production deny rules, and expose the MCP server only to agents operating with explicit human review.

Risk: Guest operations can run commands inside VMs when guest credentials are supplied.

Mitigation: Avoid guest credentials unless required and scope any guest account to the minimum privileges needed for the task.

Risk: Monitoring-only needs can be over-permissioned if this administrative skill is used for read-only workflows.

Mitigation: Prefer read-only companion skills for monitoring and health checks when no infrastructure changes are intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aiops)
- [Project homepage](https://github.com/vmware-skills/VMware-AIops)
- [Capabilities Reference](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Investigation Protocol](references/investigation-protocol.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, analysis, API calls]

**Output Format:** [Markdown guidance with inline shell commands and structured tool-call results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce offline HTML snapshots for selected triage and investigation workflows.]

## Skill Version(s):

1.8.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
