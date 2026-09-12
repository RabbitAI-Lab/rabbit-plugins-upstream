## Description:

vmware-aiops helps agents manage VMware vSphere and ESXi VM lifecycle, deployment, guest operations, cluster tasks, alarms, and triage workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and platform engineers use this skill to let an agent perform VMware VM lifecycle actions, deployments, guest operations, alarm handling, and health triage with operational guardrails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can make destructive VMware infrastructure changes when the configured vCenter or ESXi account is authorized to do so.

Mitigation: Use a dedicated least-privilege service account, use read-only RBAC for monitoring-only deployments, and add explicit deny rules for production targets.

Risk: Guest operations can run broad commands inside VMs and guest passwords passed through MCP are visible to the agent transcript.

Mitigation: Use least-privilege guest accounts, avoid guest administrator credentials unless required, and review the exact VM, command, and file paths before guest execution or upload.

Risk: Some write operations act immediately over MCP without enforced confirmation or dry-run.

Mitigation: Require human review in the calling workflow before write tools and rely on platform RBAC as the enforcement boundary.

Risk: Webhook notifications can include operational details such as host names, IP addresses, user names, alarm text, events, or connection errors.

Mitigation: Keep webhooks disabled unless needed and send notifications only to approved destinations that are allowed to receive operational data.

Risk: Server-resolved provenance is unavailable for this version.

Mitigation: Review the packaged source or verify release integrity before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aiops)
- [Project homepage](https://github.com/vmware-skills/VMware-AIops)
- [Capabilities reference](references/capabilities.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Investigation protocol](references/investigation-protocol.md)
- [CLI reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and operational summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or direct creation of local files such as offline HTML snapshots through documented CLI workflows.]

## Skill Version(s):

1.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
