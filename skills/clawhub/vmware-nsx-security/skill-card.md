## Description:

VMware NSX Security helps agents manage NSX and vDefend distributed firewall policies, security groups, VM tags, traceflow diagnostics, and IDS/IPS status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure and security engineers use this skill to inspect, create, and maintain VMware NSX distributed firewall controls, security groups, VM tags, traceflow checks, and IDS/IPS posture through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change high-impact NSX security controls, including distributed firewall rules and security group membership.

Mitigation: Review proposed changes before execution, use dry-run previews where available, require explicit approval for writes, and keep audit logging enabled.

Risk: Credential examples and persistent .env files can expose NSX credentials if used casually in production.

Mitigation: Use least-privilege NSX service accounts, restrict file permissions, and inject production secrets from a secret manager instead of storing them persistently.

Risk: Disabling TLS verification or trusting unreviewed package sources can weaken deployment integrity.

Mitigation: Keep TLS verification enabled with a trusted CA and review the upstream package source for the exact release before installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-nsx-security)
- [Project Homepage](https://github.com/vmware-skills/VMware-NSX-Security)
- [Capabilities Reference](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include NSX object listings, proposed firewall changes, setup steps, and approval-gated write actions.]

## Skill Version(s):

1.11.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
