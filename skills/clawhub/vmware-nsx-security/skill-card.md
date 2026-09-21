## Description:

Manages VMware NSX and VMware vDefend security tasks, including distributed firewall policies, security groups, VM tags, Traceflow diagnostics, and IDS/IPS status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure, network security, and platform engineers use this skill to inspect and administer NSX/vDefend security controls for microsegmentation, firewall rule management, security groups, VM tags, Traceflow troubleshooting, and IDS/IPS checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer high-impact NSX security controls, including firewall, tag, group, and delete operations.

Mitigation: Install only for agents intended to administer NSX security, use a least-privilege NSX account, and review previews before approving firewall, tag, group, or delete operations.

Risk: Credentials and configuration files could expose NSX access if stored with broad local permissions.

Mitigation: Prefer secret-manager or process-level environment injection for production, and keep config and environment files owner-only.

Risk: Incorrect distributed-firewall changes can silently permit or block traffic.

Mitigation: Use dry runs or delete previews, keep management access rules explicit, verify tags and group membership before enforcement, and use Traceflow to validate proposed rule behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-nsx-security)
- [Project homepage](https://github.com/vmware-skills/VMware-NSX-Security)
- [Capabilities Reference](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing NSX operations require explicit approval or preview review, and outputs may include current NSX policy, rule, group, tag, Traceflow, and IDPS data.]

## Skill Version(s):

1.13.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
