## Description:

Provides unified audit logging, configurable policy checks, and input sanitization for the VMware MCP skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

VMware operators and developers use this skill to inspect audit trails, configure policy rules, and integrate logging and sanitization into other VMware skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local audit records and exports can expose sensitive inventory, configuration, parameters, and results.

Mitigation: Restrict access to ~/.vmware or OPS_HOME and review exports before sharing.

Risk: The shipped policy baseline denies no operations unless the operator configures rules.

Mitigation: Configure deny rules where enforcement is needed and verify the active policy with vmware-audit policy.

Risk: Setting VMWARE_POLICY_DISABLED=1 bypasses policy checks in the host process.

Mitigation: Restrict who controls the host environment and unset the bypass after use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-policy)
- [Project homepage](https://github.com/vmware-skills/VMware-Policy)
- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Capabilities](references/capabilities.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with inline shell, YAML, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide JSON audit exports; exported records can contain sensitive operational data.]

## Skill Version(s):

1.21.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
