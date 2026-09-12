## Description:

Unified audit logging, policy enforcement, and input sanitization for the entire VMware MCP skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and VMware platform engineers use this skill to query audit logs, manage local policy rules, export audit data, and provide shared audit, policy, and sanitization support for other VMware MCP skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local audit database can contain sensitive operational details.

Mitigation: Protect ~/.vmware/audit.db and rotated archives as confidential data, restrict filesystem access, and review exports before sharing them.

Risk: Default packaged policy rules do not deny operations unless the operator configures rules.

Mitigation: Create and verify ~/.vmware/rules.yaml before using write-capable VMware skills, and use vmware-audit policy to confirm the active rule source.

Risk: VMWARE_POLICY_DISABLED=1 bypasses local policy checks for the running process.

Mitigation: Use the environment variable only for controlled break-glass cases, restrict who can set it, and unset it after the issue is resolved.

## Reference(s):

- [VMware Policy source repository](https://github.com/vmware-skills/VMware-Policy)
- [VMware Policy ClawHub page](https://clawhub.ai/zw008/skills/vmware-policy)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can also guide use of the vmware-audit CLI for JSON audit exports.]

## Skill Version(s):

1.13.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
