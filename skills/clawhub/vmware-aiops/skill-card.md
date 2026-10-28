## Description:

Helps agents administer VMware VMs and clusters, investigate infrastructure health, and manage vCenter alarms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to triage VMware environments and perform VM lifecycle, cluster, guest, and alarm operations through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can change infrastructure or delete VMs and clusters.

Mitigation: Review before production use; run with a dedicated least-privilege vCenter/ESXi account, prefer read-only access unless writes are needed, and configure production deny rules.

Risk: Guest commands can act with the supplied guest account's privileges.

Mitigation: Avoid root or administrator guest credentials and use a least-privilege guest account.

Risk: An exposed remote management endpoint can grant broad infrastructure access.

Mitigation: Do not expose the HTTPS MCP endpoint without strict tokens and role separation.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zw008/skills/vmware-aiops)
- [ClawHub publisher profile](https://clawhub.ai/user/zw008)
- [Project homepage listed in skill metadata (import provenance unavailable)](https://github.com/vmware-skills/VMware-AIops)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Investigation protocol](references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples and operational findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report results of VMware operations and health checks.]

## Skill Version(s):

2.4.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
