## Description:

Unified audit logging, policy enforcement, and input sanitization for the VMware MCP skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect VMware audit activity, configure policy rules, export audit records, and integrate shared audit, policy, and sanitization controls into VMware skill workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Policy controls can fail open if local rules are missing or enforcement prerequisites are not in place.

Mitigation: Create and protect ~/.vmware/rules.yaml before relying on enforcement, then verify blocked operations through vmware-audit.

Risk: The VMWARE_POLICY_DISABLED setting can bypass policy checks across VMware skill workflows.

Mitigation: Use policy bypass only for controlled break-glass or testing cases and review ok_bypassed audit entries.

Risk: The local audit database and exported audit files may contain sensitive infrastructure records.

Mitigation: Restrict filesystem permissions for ~/.vmware/audit.db and handle exported audit files as sensitive records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-policy)
- [VMware Policy source homepage](https://github.com/vmware-skills/VMware-Policy)
- [Capabilities reference](references/capabilities.md)
- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline bash, YAML, JSON, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local policy and audit files under ~/.vmware when guiding setup, enforcement, or compliance export.]

## Skill Version(s):

1.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
