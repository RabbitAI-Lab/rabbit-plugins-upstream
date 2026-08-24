## Description:

Automatically selects, composes, executes, verifies, and recovers OpenClaw skills based on user intent without requiring the user to name skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to route tasks across relevant OpenClaw skills, compose an execution order, resolve conflicts, verify results, and recover when a selected path fails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to choose other skills, tools, plugins, and models with broad authority.

Mitigation: Require explicit user approval for high-risk actions, persistent memory or registry changes, plugin and tool fallback, and any skill disabling.

Risk: Automatic orchestration can hide routing choices from the user and make it harder to inspect why an action was taken.

Mitigation: Keep routing decisions reviewable and reversible, and constrain the skill to explain material changes in selected skills, tools, or execution order.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/auto-skill-orchestrator)
- [Publisher profile](https://clawhub.ai/user/pmuhammadagus-byte)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with workflow steps and optional commands or configuration for selected downstream skills]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces orchestration guidance rather than a standalone executable artifact.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
