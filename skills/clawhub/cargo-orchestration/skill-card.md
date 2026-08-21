## Description:

Guides an agent through Cargo CLI orchestration tasks, including running connector actions and workflows, managing batches and plays, messaging AI agents, drawing node graphs, and querying runtime execution tables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and go-to-market teams use this skill to run and inspect Cargo workflows, batches, plays, connector actions, and agent messages while checking schemas, diagrams, status, cost, and errors before live execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger live batches, connector actions, CRM updates, and data downloads in a Cargo workspace.

Mitigation: Confirm the active workspace, connector targets, data sensitivity, record count, and cost estimate before live execution.

Risk: Large batch or segment runs can apply the same workflow to many records and incur unexpected cost or broad data changes.

Mitigation: Run a 10-20 record sample first, report observed cost and hit rate, then require explicit approval for the full enrollment.

Risk: Workflow edits or deployments can fail or behave differently than intended if node graphs are invalid or hard to review.

Mitigation: Validate node graphs and render a diagram before deployment so routing, paid steps, and fallbacks are visible.

## Reference(s):

- [Cargo Orchestration on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-orchestration)
- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Cargo CLI - Orchestration](artifact/SKILL.md)
- [Action Examples](artifact/references/examples/actions.md)
- [Tool Examples](artifact/references/examples/tools.md)
- [Play Examples](artifact/references/examples/plays.md)
- [AI Agent Examples](artifact/references/examples/agents.md)
- [Orchestration Templates](artifact/references/examples/templates.md)
- [Orchestration Query Examples](artifact/references/examples/queries.md)
- [Segment Data Examples](artifact/references/examples/segments.md)
- [Creating Nodes](artifact/references/nodes.md)
- [Diagramming a Node Graph](artifact/references/node-diagram.md)
- [Node Selection](artifact/references/node-selection.md)
- [Filter Syntax](artifact/references/filter-syntax.md)
- [Async Polling Reference](artifact/references/polling.md)
- [Response Shapes](artifact/references/response-shapes.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline Cargo CLI commands, JSON payloads, SQL queries, and diagram text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create or inspect Cargo runs, batches, draft releases, node diagrams, agent messages, and read-only orchestration queries.]

## Skill Version(s):

1.8.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
