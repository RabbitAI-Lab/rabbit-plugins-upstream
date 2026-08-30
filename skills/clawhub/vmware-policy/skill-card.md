## Description:

Unified audit logging, policy enforcement, and input sanitization for the entire VMware MCP skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query VMware-family audit logs, review denied operations, configure policy rules, export audit data, and integrate audit, policy, and sanitization helpers into VMware MCP skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Policy enforcement can be bypassed globally with VMWARE_POLICY_DISABLED=1.

Mitigation: Allow bypass only under documented break-glass procedures, monitor bypassed audit entries, and review the setting before production use.

Risk: Audit exports and the local audit database may contain sensitive operational details.

Mitigation: Treat audit exports as sensitive and restrict permissions on ~/.vmware and audit database files.

Risk: Missing or permissive policy rules can leave operations allowed by default.

Mitigation: Configure explicit ~/.vmware/rules.yaml policy rules, verify PyYAML is installed, and review rules before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-policy)
- [Project homepage](https://github.com/vmware-skills/VMware-Policy)
- [VMware Policy -- Capabilities](references/capabilities.md)
- [VMware Policy -- CLI Reference](references/cli-reference.md)
- [VMware Policy -- Setup Guide](references/setup-guide.md)
- [vmware-policy and local / small models](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, Python, YAML, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local audit exports, policy rules, and ~/.vmware configuration paths.]

## Skill Version(s):

1.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
