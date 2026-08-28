## Description:

Use this skill whenever the user needs to manage VMware NSX networking, including segments, gateways, NAT, routing, IP pools, and NSX network health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to inspect and manage VMware NSX networking resources, including segments, Tier-0 and Tier-1 gateways, NAT rules, static routes, IP pools, and health checks. It supports local CLI workflows and MCP-based agent workflows for NSX network operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production configuration examples may disable SSL certificate verification while the skill handles powerful NSX credentials.

Mitigation: Use certificate verification with a valid CA bundle for production targets and review any configuration that sets verify_ssl to false before deployment.

Risk: The skill can perform state-changing NSX network operations with credentials that may affect routing, NAT, segments, gateways, and IP pools.

Mitigation: Use least-privilege NSX accounts, require explicit approval for writes, prefer dry-run previews for CLI changes, and keep write operations covered by audit policy.

Risk: Local credential and audit files may expose sensitive operational context if filesystem permissions are weak.

Mitigation: Protect ~/.vmware-nsx/.env and ~/.vmware/audit.db with restrictive permissions and avoid storing reusable production secrets where possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-nsx)
- [Project Homepage](https://github.com/vmware-skills/VMware-NSX)
- [Setup Guide](artifact/references/setup-guide.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Capabilities](artifact/references/capabilities.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include NSX CLI commands, MCP tool-use guidance, dry-run recommendations, and setup or troubleshooting steps.]

## Skill Version(s):

1.8.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
