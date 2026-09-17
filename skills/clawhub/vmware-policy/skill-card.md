## Description:

Unified audit logging, policy enforcement, and input sanitization for the VMware MCP skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to query VMware skill audit logs, inspect policy rules, export audit data, and integrate audit, policy, and sanitization helpers into related VMware skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release depends on an external vmware-policy package and VMware skill-family trust boundary.

Mitigation: Install only when the package source and publisher are trusted, and verify release metadata before deployment.

Risk: Audit rows may contain infrastructure details in the local ~/.vmware audit database and rotated archives.

Mitigation: Protect ~/.vmware with restrictive permissions and review audit exports before sharing them.

Risk: Default policy does not replace VMware RBAC, and sanitize() is not a complete safety boundary.

Mitigation: Use least-privilege VMware accounts, configure explicit production deny rules, and treat sanitization as one layer of defense.

Risk: VMWARE_POLICY_DISABLED=1 bypasses policy evaluation for the process while leaving auditing enabled.

Mitigation: Restrict who can set MCP host environment variables and avoid leaving VMWARE_POLICY_DISABLED enabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-policy)
- [VMware Policy homepage](https://github.com/vmware-skills/VMware-Policy)
- [VMware Policy capabilities](references/capabilities.md)
- [VMware Policy CLI reference](references/cli-reference.md)
- [VMware Policy setup guide](references/setup-guide.md)
- [VMware Policy agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No MCP tools are exposed directly; outputs focus on CLI use, policy configuration, audit review, and integration guidance.]

## Skill Version(s):

1.16.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
