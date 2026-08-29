## Description:

vmware-aiops helps agents manage VMware vSphere and ESXi VM lifecycle, deployment, guest operations, cluster changes, alarms, and investigation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, infrastructure engineers, and VMware operators use this skill to let an agent plan, execute, and audit vSphere/ESXi VM lifecycle, deployment, cluster, alarm, and incident-investigation workflows. It is intended for environments where the operator can provide vCenter/ESXi credentials and approve state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer VMware resources, including VM lifecycle, guest commands, cluster changes, alarm reset, and other actions that can affect live systems.

Mitigation: Install only when agent-assisted VMware administration is intended; use a dedicated least-privilege vCenter account, keep production deny policies in place, and require operator approval for state-changing actions.

Risk: Destructive operations such as VM deletion, snapshot revert or deletion, cluster deletion, host removal, alarm reset, and TTL auto-delete can cause service impact or data loss.

Mitigation: Use dry-run or preview flows where available, review affected objects before execution, rely on double confirmation for destructive CLI operations, and verify audit records in vmware-policy.

Risk: Guest command execution and file transfer can change guest operating systems or expose sensitive operational data.

Mitigation: Require explicit VM names, full command paths, arguments, and user parameters; avoid implicit or background execution and prefer read-only investigation before remediation.

Risk: Webhook notifications can send operational alert summaries to configured destinations.

Mitigation: Keep webhooks disabled unless needed, review Slack or Discord destinations before enabling them, and send only aggregate alert metadata without credentials, IPs, or personally identifiable information.

Risk: Disabling SSL certificate validation weakens connection security.

Mitigation: Keep TLS verification enabled for production and use disableSslCertValidation only for isolated lab environments with self-signed certificates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aiops)
- [Publisher profile](https://clawhub.ai/user/zw008)
- [Project homepage from ClawHub metadata](https://github.com/vmware-skills/VMware-AIops)
- [Setup Guide](references/setup-guide.md)
- [Capabilities Reference](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with CLI commands, configuration snippets, operational guidance, and structured tool recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool choices, CLI commands, configuration steps, audit and safety notes, and offline HTML report instructions.]

## Skill Version(s):

1.8.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
