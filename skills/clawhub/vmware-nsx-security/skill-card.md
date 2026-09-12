## Description:

Helps agents manage VMware NSX security tasks including distributed firewall policies and rules, security groups, VM tags, Traceflow diagnostics, and IDS/IPS status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure, network security, and platform engineers use this skill to inspect and operate NSX distributed firewall controls, security groups, VM tags, Traceflow diagnostics, and IDS/IPS status through an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan verdict is suspicious because the install path is not reproducible enough for a skill that can access credentials and change firewall state.

Mitigation: Review the exact PyPI and GitHub release before installing, pin and hash-check dependencies where possible, and deploy only after source and package verification.

Risk: Incorrect firewall or security group changes can permit or block production traffic.

Mitigation: Use a dedicated least-privilege NSX account, keep dry-run and audit controls enabled for writes, and confirm all state-changing operations before execution.

Risk: Credential exposure or weakened TLS verification could compromise NSX Manager access.

Mitigation: Store per-target credentials outside config files, keep local secret files owner-only, and keep TLS verification enabled outside isolated lab environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-nsx-security)
- [Project Homepage](https://github.com/vmware-skills/VMware-NSX-Security)
- [Capabilities Reference](references/capabilities.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with inline shell commands, configuration snippets, and structured tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce operational recommendations and command sequences for high-impact NSX security changes that require review before execution.]

## Skill Version(s):

1.11.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
