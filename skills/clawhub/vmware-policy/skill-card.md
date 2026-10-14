## Description:

Provides audit-log guidance, policy-rule management, and input-sanitization integration for the VMware MCP skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

VMware administrators and developers use this skill to inspect audit activity, configure policy rules, and integrate audit and sanitization behavior with VMware tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local audit logs may contain sensitive tool parameters and results despite best-effort redaction.

Mitigation: Restrict access to ~/.vmware and review audit exports before sharing them.

Risk: Without operator-defined deny rules, production or destructive operations may not be blocked by this policy layer.

Mitigation: Configure deny rules for production and destructive actions, then confirm the active policy.

Risk: Leaving VMWARE_POLICY_DISABLED=1 set bypasses policy checks.

Mitigation: Limit who can set the variable and remove it after any authorized temporary bypass.

## Reference(s):

- [Project homepage (listed in skill metadata)](https://github.com/vmware-skills/VMware-Policy)
- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Capabilities](references/capabilities.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with CLI commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide local audit-log queries and JSON exports.]

## Skill Version(s):

1.18.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
