## Description:

Unified audit logging, policy enforcement, and input sanitization for the entire VMware MCP skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and VMware platform engineers use this skill to audit VMware skill activity, configure local deny rules and maintenance windows, export audit trails, and integrate shared policy and sanitization hooks into other VMware skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local audit rows can contain sensitive inventory, configuration, parameters, results, user, agent, and timestamp data.

Mitigation: Protect ~/.vmware or OPS_HOME, keep local audit files restricted, and review exports before sharing them outside the operating team.

Risk: Policy enforcement depends on operator configuration; the packaged baseline denies nothing and VMWARE_POLICY_DISABLED=1 bypasses policy checks.

Mitigation: Configure deny rules and maintenance windows before relying on enforcement, verify them with vmware-audit policy, and avoid leaving VMWARE_POLICY_DISABLED=1 set in MCP host or CLI environments.

Risk: Installing the skill relies on a third-party package source.

Mitigation: Install only in environments where the vmware-policy package source and linked source homepage are trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-policy)
- [Source homepage](https://github.com/vmware-skills/VMware-Policy)
- [VMware Policy capabilities](references/capabilities.md)
- [VMware Policy setup guide](references/setup-guide.md)
- [VMware Policy CLI reference](references/cli-reference.md)
- [VMware Policy agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and CLI text with JSON export examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance and command examples around local audit and policy state; the skill itself exposes no MCP tools.]

## Skill Version(s):

1.16.0 (source: server release metadata and artifact setup examples)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
