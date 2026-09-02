## Description:

Helps agents manage VMware NSX security and vDefend tasks, including distributed firewall policies and rules, security groups, VM tags, Traceflow diagnostics, and IDS/IPS status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

External infrastructure and security operators use this skill to inspect, plan, and apply VMware NSX distributed firewall, microsegmentation, VM tagging, Traceflow, and IDS/IPS workflows. It is intended for authorized NSX administration, with read-only inspection and approval-gated write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make live firewall, security group, and tag changes that may permit, block, or reroute operational security decisions.

Mitigation: Install it only for authorized NSX security operators, use explicit approval practices for writes, and avoid making production the default target unless intentional.

Risk: Broad NSX credentials could expand the impact of an incorrect agent action.

Mitigation: Prefer a dedicated least-privilege NSX account and use read-only RBAC for inspection-only deployments.

Risk: Persisted credentials in local environment files can be exposed if file permissions or workstation controls are weak.

Mitigation: Use a secret manager or injected environment variables when possible, and keep local configuration and .env files owner-readable only.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-nsx-security)
- [Project Homepage](https://github.com/vmware-skills/VMware-NSX-Security)
- [Capabilities Reference](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe NSX MCP or CLI actions; write operations should remain approval-gated and audited according to the release evidence.]

## Skill Version(s):

1.9.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
