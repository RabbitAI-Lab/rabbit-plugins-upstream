## Description:

Provides audit logging, policy checks, and input sanitization for VMware-family agent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and developers use this skill to inspect VMware-family audit trails, configure policy rules, and integrate audit and policy checks into related skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default policy rules do not deny risky changes.

Mitigation: Configure explicit deny rules or require approval before production changes.

Risk: Setting VMWARE_POLICY_DISABLED bypasses policy evaluation.

Mitigation: Leave it unset except during controlled break-glass recovery.

Risk: Local audit records and rotated archives can disclose infrastructure details.

Mitigation: Treat audit databases and archives as confidential and restrict access.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zw008/skills/vmware-policy)
- [Project homepage (listed in skill metadata)](https://github.com/vmware-skills/VMware-Policy)
- [Capabilities](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with command, YAML, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audit queries may return tabular summaries or JSON exports.]

## Skill Version(s):

1.24.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
