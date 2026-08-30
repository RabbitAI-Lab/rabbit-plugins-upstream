## Description:

VMware Pilot helps agents design, review, and coordinate multi-step VMware workflows across companion skills with approval gates, persisted state, and rollback support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to plan and coordinate VMware change, incident response, maintenance, and compliance workflows that require checkpoints or multiple companion skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may coordinate VMware workflows whose safety guarantees are weaker than its description suggests.

Mitigation: Review every generated step before execution and require approval before the first state-changing action in production workflows.

Risk: Workflow activity can involve sensitive operational context or secrets being returned into chat, logs, or local VMware files.

Mitigation: Avoid returning kubeconfig files or passwords into chat or logs, and secure or purge ~/.vmware audit, workflow, and baseline files under local data-handling rules.

Risk: The skill delegates actual infrastructure changes to companion VMware skills configured in the user's environment.

Mitigation: Install only in environments where the companion skills, permissions, and policy controls are approved for coordinated VMware change workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-pilot)
- [Homepage from ClawHub metadata](https://github.com/vmware-skills/VMware-Pilot)
- [Setup Guide](artifact/references/setup-guide.md)
- [Capabilities](artifact/references/capabilities.md)
- [Workflow Design Guide](artifact/references/workflow-design.md)
- [Built-in Templates Reference](artifact/references/templates.md)
- [Cross-Skill Integration Patterns](artifact/references/integration-patterns.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured MCP workflow guidance with inline shell and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces workflow plans, step descriptions, approval checkpoints, rollback guidance, and setup commands for an agent to review and dispatch.]

## Skill Version(s):

1.8.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
