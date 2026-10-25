## Description:

Helps agents and operators query VMware skill audit activity, configure policy rules, and integrate shared audit and sanitization safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and VMware operators use this skill to review audit trails, check denied actions, configure policy rules, and add shared safeguards to VMware skill tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default policy does not block risky operations until rules are configured.

Mitigation: Configure ~/.vmware/rules.yaml and confirm the active rules before relying on policy enforcement.

Risk: Local audit records and rotated archives can contain sensitive operational information.

Mitigation: Restrict access to the audit database and archives, and review exports before sharing.

Risk: Operators with control of the host environment can disable policy checks.

Mitigation: Restrict who can set VMWARE_POLICY_DISABLED or modify the MCP host environment.

## Reference(s):

- [VMware Policy project homepage (listed in release metadata)](https://github.com/vmware-skills/VMware-Policy)
- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Capabilities](references/capabilities.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with shell, YAML, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audit queries may report sensitive operational details; review exports before sharing.]

## Skill Version(s):

1.24.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
