## Description:

Use this skill when an agent needs to manage VMware NSX security and vDefend distributed firewall policies and rules, security groups, VM tags, Traceflow diagnostics, and IDPS status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and security administrators use this skill to inspect and change VMware NSX security controls, including distributed firewall policy and rule management, microsegmentation groups, VM tags, Traceflow diagnostics, and IDPS checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change NSX firewall rules, security groups, VM tags, and local audit records, which can disrupt access or weaken security posture if misused.

Mitigation: Use a dedicated least-privilege NSX account and require dry-run plus approval workflows before applying firewall, group, or tag changes.

Risk: NSX credentials and operational artifacts may be exposed if configuration, .env, or audit files are readable by unintended users.

Mitigation: Prefer secret-manager injection for production and keep config, .env, and audit files owner-readable only.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-nsx-security)
- [Project Homepage](https://github.com/vmware-skills/VMware-NSX-Security)
- [Capabilities Reference](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide CLI or MCP operations against configured NSX Manager targets; write operations should use dry-run and approval workflows.]

## Skill Version(s):

1.8.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
