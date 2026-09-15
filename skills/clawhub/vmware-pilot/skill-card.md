## Description:

vmware-pilot helps agents design, review, execute, and manage multi-step VMware workflows with approval gates, persistent workflow state, and explicit best-effort rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and VMware operators use this skill to coordinate multi-step infrastructure workflows such as clone-and-test changes, incident response, rolling maintenance, drift detection, and approval-gated remediation across companion VMware skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can coordinate production infrastructure changes through companion VMware skills.

Mitigation: Use least-privilege service accounts, configure vmware-policy rules for production, and require explicit operator approval for high-impact workflow steps.

Risk: The runtime package is external to the artifact and may be resolved at install or launch time.

Mitigation: Verify the package source and exact version before use, and prefer the installed entry point over uvx so runtime launch does not re-resolve the package.

Risk: Some delegated workflow steps can return live kubeconfig credentials or other sensitive operational data.

Mitigation: Keep credential-returning steps behind approval gates, write kubeconfigs only to owner-only files, and do not print tokens or sensitive results into chat or logs.

Risk: Rollback is explicit and best-effort, not automatic.

Mitigation: Ask the operator before undoing work, then call each recorded rollback tool last-first; document any step without a rollback mapping as not directly undoable.

Risk: Workflow databases and baseline inventories can contain sensitive infrastructure state.

Mitigation: Keep local state files owner-only and avoid copying workflow parameters, baseline inventories, or audit data into public channels.

## Reference(s):

- [VMware Pilot homepage](https://github.com/vmware-skills/VMware-Pilot)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-pilot)
- [Capabilities](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [Workflow Design Guide](references/workflow-design.md)
- [Cross-Skill Integration Patterns](references/integration-patterns.md)
- [Built-in Templates Reference](references/templates.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with MCP tool calls, YAML workflow examples, JSON snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce workflow plans, approval prompts, rollback instructions, audit guidance, and setup commands.]

## Skill Version(s):

1.11.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
