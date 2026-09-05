## Description:

Manages VMware NSX/vDefend security operations for distributed firewall policies and rules, security groups, VM tags, Traceflow diagnostics, and IDS/IPS status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and security operators use this skill to inspect and change VMware NSX/vDefend distributed firewall policy, microsegmentation, group membership, VM tags, Traceflow diagnostics, and IDS/IPS posture from an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect and change high-impact NSX firewall and security objects.

Mitigation: Install it only where agent-driven NSX security administration is intended, use a dedicated least-privilege NSX account, and keep write operations behind dry-run and approval gates.

Risk: Credentials and target configuration can expose NSX Manager access if local files are readable by other users.

Mitigation: Keep config and .env files owner-readable only, prefer a secret manager for production credentials, and use authenticated doctor checks as the normal validation path.

Risk: Firewall and tag changes can silently permit or block production traffic.

Mitigation: Use the skill's double-confirmation, audit logging, dependency checks, Traceflow verification, and explicit approval workflow before applying write operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-nsx-security)
- [Project Homepage](https://github.com/vmware-skills/VMware-NSX-Security)
- [VMware NSX Security Setup Guide](references/setup-guide.md)
- [VMware NSX Security Capabilities Reference](references/capabilities.md)
- [VMware NSX Security CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with command examples, configuration snippets, and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or execute read and write NSX security operations; write operations require appropriate approval, credentials, and audit controls.]

## Skill Version(s):

1.10.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
