## Description:

Unified audit logging, policy enforcement, and input sanitization for VMware MCP skill-family tools, including audit queries, policy rules, and the shared @vmware_tool wrapper.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform operators use VMware Policy to audit VMware skill activity, review denied operations, configure local policy rules, and integrate audit and sanitization controls into related VMware MCP skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Policy enforcement may fail open or be bypassed, so configured controls may not block operations unless the environment is prepared and protected.

Mitigation: Create and test ~/.vmware/rules.yaml, install PyYAML where required, and restrict who can set VMWARE_POLICY_DISABLED.

Risk: The local audit database can contain sensitive operational metadata, tool parameters, results, user, agent, and operation details.

Mitigation: Treat ~/.vmware/audit.db as sensitive, keep ~/.vmware owner-restricted, and use sensitive-parameter redaction when integrating tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-policy)
- [Project homepage](https://github.com/vmware-skills/VMware-Policy)
- [VMware Policy setup guide](references/setup-guide.md)
- [VMware Policy capabilities](references/capabilities.md)
- [VMware Policy CLI reference](references/cli-reference.md)
- [VMware Policy agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, YAML configuration examples, and Python code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local audit database and policy file paths used by VMware skill-family tooling.]

## Skill Version(s):

1.13.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
