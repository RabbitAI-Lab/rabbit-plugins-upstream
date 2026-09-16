## Description:

vmware-nsx helps agents inspect and manage VMware NSX networking through NSX Manager, including segments, Tier-0 and Tier-1 gateways, NAT, static routes, BGP, IP pools, inventory, health, and troubleshooting workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, infrastructure engineers, and NSX operators use this skill to inspect NSX state, troubleshoot connectivity, and perform explicitly requested network changes with audit and policy controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can use NSX credentials that may permit high-impact network changes.

Mitigation: Use read-only or least-privilege NSX service accounts, inject production secrets through a secret manager when possible, and verify the package source before installation.

Risk: MCP write tools execute directly after an agent calls them and do not provide their own confirmation step.

Mitigation: Require explicit human approval before any write, prefer CLI dry-runs for change previews, and use production deny rules in ~/.vmware/rules.yaml.

Risk: Disabling TLS verification can expose NSX Manager credentials or allow connection to the wrong endpoint.

Mitigation: Keep verify_ssl enabled for real environments and trust private CAs through SSL_CERT_FILE; use verify_ssl false only for isolated labs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-nsx)
- [VMware NSX Source Homepage](https://github.com/vmware-skills/VMware-NSX)
- [Capabilities](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CLI or MCP-oriented operational steps; state-changing actions require explicit user approval and should use dry-run, policy, and audit controls where available.]

## Skill Version(s):

1.9.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
