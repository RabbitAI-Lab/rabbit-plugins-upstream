## Description:

Guides agents through Cargo CLI orchestration: executing connector actions, running workflows and batches, messaging AI agents, building or diagramming node graphs, and querying runtime tables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to make an agent operate Cargo workflows through the Cargo CLI, including discovering actions, running single-record or batch jobs, composing node graphs, messaging agents, and querying runtime status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents toward high-impact Cargo operations such as real runs, bulk batches, workflow deployments, connector calls, and data export paths.

Mitigation: Confirm the active workspace, use test or sandbox connectors where possible, and require explicit user approval before full-batch, workflow-changing, download, or export actions.

Risk: Broad or empty filters can process more records than intended.

Mitigation: Sample 10 to 20 records first, report observed cost and hit rate, quote the full record count and credit estimate, and avoid empty filters unless all records are intentionally in scope.

Risk: Unpinned CLI behavior may differ from the skill's documented command behavior.

Mitigation: Pin or verify the Cargo CLI version and refresh the CLI when documented commands are unavailable.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Action examples](references/examples/actions.md)
- [AI agent examples](references/examples/agents.md)
- [Play examples](references/examples/plays.md)
- [Orchestration query examples](references/examples/queries.md)
- [Segment data examples](references/examples/segments.md)
- [Orchestration templates](references/examples/templates.md)
- [Tool examples](references/examples/tools.md)
- [Filter syntax](references/filter-syntax.md)
- [Diagramming a node graph](references/node-diagram.md)
- [Prefer built-in actions and expressions over code or HTTP nodes](references/node-selection.md)
- [Creating nodes](references/nodes.md)
- [Async polling reference](references/polling.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Cargo CLI commands that execute runs, batches, workflow changes, connector calls, and runtime queries.]

## Skill Version(s):

1.12.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
