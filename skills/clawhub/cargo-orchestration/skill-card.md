## Description:

Cargo Orchestration helps agents execute Cargo actions and workflows, trigger batches and plays, message AI agents, build or inspect node graphs, and query orchestration runtime tables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run and inspect Cargo platform automations, including connector actions, workflow runs, batch enrollments, segment-driven plays, AI agent messages, node graph diagrams, and orchestration history queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install metadata uses @cargo-ai/cli@latest, so installing later can fetch a different CLI build than the reviewed release.

Mitigation: Pin and review the Cargo CLI version before use, especially in shared or production workspaces.

Risk: The skill can run high-impact Cargo automations such as workflow changes, batch enrollment, production runs, record exports, and agent messages.

Mitigation: Test on small samples first, validate node graphs, confirm record counts and credit estimates, and get explicit approval before bulk or production changes.

Risk: Authentication tokens, webhook secrets, exported CSVs, and signed URLs may expose sensitive workspace data if handled casually.

Mitigation: Prefer OAuth or protected environment secrets over command-line tokens, avoid shell history exposure, and treat exported files and signed links as sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-orchestration)
- [Cargo publisher profile](https://clawhub.ai/user/cargo-ai)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Action examples](references/examples/actions.md)
- [Tool examples](references/examples/tools.md)
- [Play examples](references/examples/plays.md)
- [AI agent examples](references/examples/agents.md)
- [Orchestration query examples](references/examples/queries.md)
- [Segment data examples](references/examples/segments.md)
- [Orchestration templates](references/examples/templates.md)
- [Creating nodes](references/nodes.md)
- [Diagramming a node graph](references/node-diagram.md)
- [Node selection guidance](references/node-selection.md)
- [Filter syntax](references/filter-syntax.md)
- [Async polling reference](references/polling.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON snippets, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Cargo CLI commands that execute actions, create runs or batches, update workflow drafts, query orchestration history, or generate node diagrams.]

## Skill Version(s):

1.11.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
