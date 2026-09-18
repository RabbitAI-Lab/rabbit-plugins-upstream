## Description:

Runs Cargo orchestration operations such as connector actions, workflows, batches, AI agent messages, node graphs, diagrams, and runtime SQL queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to discover and run Cargo orchestration actions, workflows, batches, plays, tools, AI agent messages, and runtime queries while preserving approval and sampling gates for high-impact operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install metadata uses a mutable Cargo CLI package, so installed behavior can change over time.

Mitigation: Review before production installation and prefer a pinned, trusted Cargo CLI version.

Risk: Bulk executions, all-row batches, deploys, and workflow writes can affect workspace data or spend credits at scale.

Mitigation: Confirm the active workspace, sample a small batch first, quote record counts and credit estimates, and require explicit approval before full execution.

Risk: Shell examples can accidentally expose API tokens or webhook secrets if real credentials are pasted into commands.

Mitigation: Use secure credential handling and avoid placing real tokens or webhook secrets directly in shell commands.

Risk: Result-download operations may expose workspace data.

Mitigation: Use the designated analytics workflow for downloading result files.

## Reference(s):

- [Cargo Orchestration Skill Page](https://clawhub.ai/cargo-ai/skills/cargo-orchestration)
- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Action examples](references/examples/actions.md)
- [Tool examples](references/examples/tools.md)
- [Play examples](references/examples/plays.md)
- [AI agent examples](references/examples/agents.md)
- [Orchestration query examples](references/examples/queries.md)
- [Creating nodes](references/nodes.md)
- [Diagramming a node graph](references/node-diagram.md)
- [Node selection guidance](references/node-selection.md)
- [Async polling reference](references/polling.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Cargo CLI commands that execute or inspect workflows, batches, agent messages, node graphs, and orchestration queries.]

## Skill Version(s):

1.12.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
