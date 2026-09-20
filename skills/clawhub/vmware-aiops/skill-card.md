## Description:

vmware-aiops helps agents manage VMware vSphere and ESXi VM lifecycle, deployment, guest operations, cluster administration, alarms, and operational triage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators, platform engineers, and developers use this skill to let an agent operate VMware VM lifecycle workflows, deployments, guest operations, cluster changes, alarm handling, and investigation-driven remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer VMware resources and may change infrastructure state.

Mitigation: Install it only for intended VMware administration use and run it with a dedicated least-privilege vCenter or ESXi service account; use read-only RBAC unless writes are required.

Risk: MCP guest exec and upload operations can run commands inside VMs or move local files using credentials visible to the agent.

Mitigation: Use least-privilege guest accounts, avoid high-privilege guest credentials, and treat guest exec/upload as high-risk operations.

Risk: Some write paths have limited enforced approval and can act on the first call.

Mitigation: Configure deny rules before production use, require human review of blast-radius previews, and keep audit logging available for operational review.

Risk: Secrets and VMware credentials may be exposed if stored casually.

Mitigation: Store secrets in a real secret manager when possible and avoid passing or persisting high-privilege credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aiops)
- [Project homepage](https://github.com/vmware-skills/VMware-AIops)
- [Capabilities Reference](artifact/references/capabilities.md)
- [Setup Guide](artifact/references/setup-guide.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Investigation Protocol](artifact/references/investigation-protocol.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands, operational checklists, and MCP tool-call recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide tools that return structured JSON and may generate local configuration or audit-oriented workflows.]

## Skill Version(s):

1.11.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
