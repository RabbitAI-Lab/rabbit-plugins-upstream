## Description:

Guides an agent through Cargo orchestration tasks: executing actions, running workflows and batches, messaging agents, building or diagramming node graphs, and querying runtime tables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Cargo users, operators, and developers use this skill to discover orchestration resources, run individual actions or multi-step workflows, trigger batches and plays, query runtime status, and draft or inspect node graphs. It is intended for agent-assisted Cargo operations where live runs, costs, and workspace changes need explicit review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent toward high-impact Cargo operations, including live automation, workspace mutation, cancellations, exports, and third-party connector writes.

Mitigation: Confirm the active workspace, start with sandbox or narrow test data, and require explicit user approval before bulk runs, exports, deploys, CRM writes, syncs, cancellations, or segment deletion.

Risk: Bulk batches can multiply mistakes and costs across many records.

Mitigation: Run a 10-20 record sample first, report the observed cost and hit rate, quote the full record count and credit estimate, and wait for explicit approval before full enrollment.

Risk: Incorrect node configuration, routing, or missing output paths can produce successful runs with wrong or empty downstream results.

Mitigation: Validate node graphs, draw the graph before deployment, inspect runContext and computed configs when debugging, and prefer built-in actions and expressions over custom code or raw HTTP nodes where possible.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-orchestration)
- [Cargo CLI Orchestration](SKILL.md)
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

**Output Type(s):** [guidance, markdown, shell commands, configuration, SQL queries, diagrams]

**Output Format:** [Markdown with Cargo CLI commands, JSON payloads, SQL examples, and ASCII or Mermaid diagrams.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may propose live Cargo operations that create runs, batches, workflow releases, segments, records, or agent messages.]

## Skill Version(s):

1.11.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
