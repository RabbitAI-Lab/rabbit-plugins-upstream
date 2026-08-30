## Description:

Helps agents manage VMware NSX networking, including segments, Tier-0 and Tier-1 gateways, NAT rules, static routes, IP pools, network health checks, and connectivity troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operators, platform engineers, and developers use this skill to inspect and change VMware NSX networking resources, diagnose connectivity issues, and prepare CLI or tool-based workflows for NSX environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change important VMware NSX network settings.

Mitigation: Install only for operators who should manage NSX networking, prefer dry-run and explicit approvals for writes, and consider production deny rules.

Risk: Credentials and audit logs can expose sensitive operational access or history if poorly protected.

Mitigation: Use least-privilege NSX accounts and protect ~/.vmware-nsx/.env and ~/.vmware/audit.db with strict permissions.

Risk: Weak TLS settings can reduce protection for production NSX Manager connections.

Mitigation: Set verify_ssl: true with a trusted CA for production environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-nsx)
- [Project homepage](https://github.com/vmware-skills/VMware-NSX)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run recommendations, approval prompts, and verification steps for NSX network changes.]

## Skill Version(s):

1.8.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
