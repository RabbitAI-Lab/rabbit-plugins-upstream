## Description:

vmware-pilot helps agents design, approve, execute, and roll back complex multi-step VMware workflows across companion VMware skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and VMware operators use this skill to design and manage approval-gated workflows for incident response, clone-and-test changes, rolling maintenance, baseline checks, and other multi-step VMware operations. It is intended for workflows that need coordination across companion skills, human checkpoints, rollback planning, or auditability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approval and rollback behavior may be inconsistent for high-impact infrastructure workflows.

Mitigation: Require explicit human approval before any infrastructure-changing companion tool runs, review workflow plans before execution, and treat rollback as an operator-directed recovery action rather than a crash-safe guarantee.

Risk: Workflow, audit, and baseline files under ~/.vmware may contain sensitive operational data.

Mitigation: Restrict local file permissions, avoid sharing these files in prompts or logs, and handle audit exports as sensitive operational records.

Risk: Pilot tracks workflow state but does not itself prove that companion VMware tools changed infrastructure successfully.

Mitigation: Verify outcomes with the owning companion skill's read-only tools before reporting that infrastructure state has changed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-pilot)
- [VMware-Pilot homepage](https://github.com/vmware-skills/VMware-Pilot)
- [Setup Guide](references/setup-guide.md)
- [Workflow Design Guide](references/workflow-design.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Built-in Templates Reference](references/templates.md)
- [Cross-Skill Integration Patterns](references/integration-patterns.md)
- [CLI Reference](references/cli-reference.md)
- [Capabilities](references/capabilities.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and structured workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include workflow YAML templates, MCP tool names, approval checkpoints, rollback mappings, and audit guidance.]

## Skill Version(s):

1.8.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
