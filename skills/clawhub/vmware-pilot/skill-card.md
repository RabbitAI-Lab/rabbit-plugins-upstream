## Description:

VMware Pilot designs, approves, executes, and tracks rollback-aware multi-step VMware workflows across companion VMware skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, infrastructure engineers, and SREs use this skill to plan and coordinate VMware workflows that span multiple companion skills, with human approval gates before destructive operations and explicit rollback handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow plans can coordinate high-impact changes through companion VMware skills.

Mitigation: Use least-privileged companion skill accounts and review generated workflows before approval.

Risk: Kubeconfig-returning workflow steps can expose live credentials.

Mitigation: Keep those steps behind approval gates, write credentials only to owner-restricted files, and avoid printing tokens into chat or logs.

Risk: Local workflow, audit, and baseline files may reveal infrastructure details.

Mitigation: Protect or expire those files and keep generated baselines out of shared chat or logs.

Risk: The uvx fallback may re-resolve packages at launch time and is less suitable for production environments.

Mitigation: Prefer the installed vmware-pilot entry point for production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-pilot)
- [Project homepage from ClawHub metadata](https://github.com/vmware-skills/VMware-Pilot)
- [Capabilities](artifact/references/capabilities.md)
- [Workflow Design Guide](artifact/references/workflow-design.md)
- [Built-in Templates Reference](artifact/references/templates.md)
- [Cross-Skill Integration Patterns](artifact/references/integration-patterns.md)
- [Setup Guide](artifact/references/setup-guide.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with workflow plans, MCP tool-call parameters, shell commands, YAML configuration, and JSON status or validation data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include approval-gated workflow steps, rollback previews, audit guidance, and references to local workflow or baseline files.]

## Skill Version(s):

1.12.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
