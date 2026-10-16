## Description:

Helps operators inspect and manage VMware NSX distributed firewall policies and rules, security groups, VM tags, traceflow diagnostics, and IDS/IPS status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

NSX security administrators and infrastructure engineers use this skill to review firewall enforcement, investigate traffic paths, and make approved changes to distributed firewall rules, security groups, and VM tags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Firewall and security-group writes can change which traffic is permitted or blocked.

Mitigation: Restrict installation to authorized NSX security operators, use least-privilege service accounts, and expose only read-only tools unless writes are needed.

Risk: Persisted NSX credentials could be disclosed.

Mitigation: Prefer secret-manager injection over persistent .env passwords in production.

Risk: Disabling certificate verification can expose NSX management traffic.

Mitigation: Keep TLS verification enabled for NSX connections.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-nsx-security)
- [Project homepage](https://github.com/vmware-skills/VMware-NSX-Security)
- [Setup guide](references/setup-guide.md)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can inspect NSX security state and perform approved firewall or security-group changes.]

## Skill Version(s):

1.17.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
