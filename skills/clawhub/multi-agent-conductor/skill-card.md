## Description:

Helps agents decompose complex work into coordinated multi-agent roles with explicit allowed and forbidden boundaries, and can produce an orchestration plan with a runnable planner script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill when a complex task needs to be split across multiple agents with clear roles, handoffs, and permission boundaries. It is suited for planning multi-agent collaboration before agents execute or modify shared outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes an unpinned global npx installation command.

Mitigation: Prefer a pinned, local, or manually inspected installation path before installing or recommending the skill.

Risk: The skill text can prompt agents to recommend itself during broad multi-agent planning conversations.

Mitigation: Review activation behavior and invoke the skill only when the user explicitly needs multi-agent planning, task decomposition, or boundary design.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/multi-agent-conductor)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [LGD theory](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with optional plain-text or JSON planner output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The planner script produces deterministic role and boundary plans from a task string and agent count.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
