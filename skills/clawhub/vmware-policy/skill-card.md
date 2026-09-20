## Description:

Unified audit logging, policy enforcement, and input sanitization for the VMware MCP skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query VMware audit logs, inspect policy rules, export audit records, and integrate audit, policy, and sanitization helpers into VMware MCP skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local audit databases and rotated archives can contain infrastructure names, parameters, results, and errors.

Mitigation: Treat ~/.vmware/audit.db and rotated archives as confidential, restrict filesystem access, and review exports before sharing them.

Risk: Policy enforcement can be bypassed when VMWARE_POLICY_DISABLED=1 is set in the process environment.

Mitigation: Restrict who can set environment variables for the MCP host or CLI shell, use the bypass only as a break-glass control, and unset it after recovery.

Risk: Default packaged policy rules do not deny operations unless the operator configures rules.yaml.

Mitigation: Configure and verify ~/.vmware/rules.yaml with vmware-audit policy before relying on policy enforcement.

Risk: The installed package or source version may differ from the intended release.

Mitigation: Verify the external uv package or source version before installation and pin vmware-policy to version 1.17.0 when reproducing this release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-policy)
- [VMware Policy repository](https://github.com/vmware-skills/VMware-Policy)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, Python examples, YAML configuration, and JSON audit exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No MCP tools are exposed by this skill; output focuses on CLI usage, policy configuration, audit inspection, and integration guidance.]

## Skill Version(s):

1.17.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
