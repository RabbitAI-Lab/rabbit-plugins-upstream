## Description:

VMware AIops helps agents manage VMware vSphere and ESXi VM lifecycle, deployment, guest operations, clusters, alarms, triage, and investigation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to manage VMware VM lifecycle work, deployments, guest operations, cluster changes, alarm handling, and evidence-led triage or investigations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP write tools can change VMware infrastructure immediately, including VM deletion, cluster changes, migration, snapshots, and guest operations.

Mitigation: Run the skill with a dedicated least-privilege vCenter or ESXi service account, use read-only RBAC when writes are not required, and require external approval controls for production changes.

Risk: Guest-operation passwords passed over MCP are visible to the agent transcript even though audit rows redact credentials.

Mitigation: Avoid passing privileged guest credentials through MCP; use a least-privilege guest account and provide only the access needed for the requested operation.

Risk: Guest upload operations can read local files available to the server process and copy them into a VM.

Mitigation: Restrict the server process filesystem access and upload only files explicitly named and approved for the task.

Risk: The shipped policy baseline denies nothing and optional deny rules are guardrails rather than a replacement for platform RBAC.

Mitigation: Configure deny rules and maintenance windows before use, especially for production-labeled targets, while relying on VMware RBAC as the enforcement boundary.

Risk: Webhook notifications can include operational data such as host names, IP addresses, user names, alarms, event text, and connection errors.

Mitigation: Keep webhooks disabled unless needed and send them only to controlled destinations approved to receive operational infrastructure data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aiops)
- [ClawHub publisher profile](https://clawhub.ai/user/zw008)
- [Project homepage from ClawHub metadata](https://github.com/vmware-skills/VMware-AIops)
- [Capabilities Reference](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce MCP tool-use guidance, CLI commands, configuration steps, triage summaries, and investigation reports.]

## Skill Version(s):

1.9.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
