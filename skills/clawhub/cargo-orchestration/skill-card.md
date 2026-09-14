## Description:

Guides an agent through Cargo CLI orchestration tasks, including executing actions, running workflows and batches, messaging AI agents, building or diagramming node graphs, and querying runtime tables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to safely discover Cargo resources, execute one-off or batch orchestration work, edit and validate workflows, inspect AI-agent interactions, and query run history. It is intended for live Cargo workspaces where CLI actions may create runs, batches, workflow changes, or external connector calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs an unpinned Cargo CLI package.

Mitigation: Pin a reviewed @cargo-ai/cli version before deployment and refresh only after review.

Risk: Commands can affect live workflows, batches, segments, CRM-style systems, and exported data.

Mitigation: Confirm the active workspace, use sandbox or test workspaces for workflow edits, and require explicit approval before full batches or deploys.

Risk: Connector actions or webhooks may transmit customer data outside the workspace.

Mitigation: Use trusted connectors and webhooks only, minimize submitted data, and review destinations before execution.

## Reference(s):

- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Cargo Orchestration Skill](https://clawhub.ai/cargo-ai/skills/cargo-orchestration)
- [Action examples](references/examples/actions.md)
- [Tool examples](references/examples/tools.md)
- [Play examples](references/examples/plays.md)
- [AI agent examples](references/examples/agents.md)
- [Orchestration query examples](references/examples/queries.md)
- [Segment data examples](references/examples/segments.md)
- [Orchestration templates](references/examples/templates.md)
- [Creating nodes](references/nodes.md)
- [Diagramming a node graph](references/node-diagram.md)
- [Prefer built-in actions and expressions over code or HTTP nodes](references/node-selection.md)
- [Filter syntax](references/filter-syntax.md)
- [Async polling reference](references/polling.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown with inline shell commands, JSON payloads, SQL snippets, and diagram source or ASCII diagrams]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or execute Cargo CLI commands that return JSON and can affect live workspace resources.]

## Skill Version(s):

1.11.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
