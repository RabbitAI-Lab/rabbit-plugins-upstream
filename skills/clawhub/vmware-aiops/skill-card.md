## Description:

Helps operators investigate VMware infrastructure and manage virtual machines, deployments, clusters, and vCenter alarms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to investigate vSphere and ESXi environments and perform VM lifecycle, deployment, cluster, and alarm operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: VMware control can alter or remove live infrastructure resources.

Mitigation: Use a dedicated least-privilege service account, prefer read-only access unless writes are necessary, and configure deny rules for production.

Risk: Guest command execution and file upload can run arbitrary code inside virtual machines.

Mitigation: Treat guest execution and upload as remote code execution; avoid root or other privileged guest credentials.

Risk: The skill handles sensitive VMware credentials.

Mitigation: Use trusted secret-manager injection instead of long-lived plaintext .env credentials where possible.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zw008/skills/vmware-aiops)
- [Project homepage listed in skill metadata](https://github.com/vmware-skills/VMware-AIops)
- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Investigation protocol](references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend actions affecting live VMware infrastructure.]

## Skill Version(s):

2.4.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
