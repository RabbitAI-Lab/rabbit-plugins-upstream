## Description:

Helps agents execute Cargo connector actions, run workflows and batches, message AI agents, build or edit node graphs, and query orchestration runtime tables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Cargo workspace operators use this skill to run and monitor Cargo orchestration tasks, including single actions, multi-step workflows, segment or file batches, AI agent messages, node graph drafts, and SQL queries over run and batch data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bulk batches, CRM updates, enrichment, webhooks, or outreach workflows can affect many records, consume credits, or use third-party data.

Mitigation: Confirm the active workspace, test on a small sample, review affected record counts and credit cost, and ensure third-party data use is approved before full execution.

Risk: Workflow or node graph changes may trigger live operations against connected Cargo tools and integrations.

Mitigation: Prefer built-in actions and template expressions, inspect output schemas before wiring downstream steps, and review a node diagram before deploying or approving a workflow.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Cargo CLI - Orchestration](SKILL.md)
- [Action examples](references/examples/actions.md)
- [Tool examples](references/examples/tools.md)
- [Play examples](references/examples/plays.md)
- [AI agent examples](references/examples/agents.md)
- [Orchestration templates](references/examples/templates.md)
- [Orchestration query examples](references/examples/queries.md)
- [Segment data examples](references/examples/segments.md)
- [Creating nodes](references/nodes.md)
- [Diagramming a node graph](references/node-diagram.md)
- [Node selection guidance](references/node-selection.md)
- [Filter syntax](references/filter-syntax.md)
- [Async polling reference](references/polling.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Cargo CLI commands and operational guidance; command results are JSON when executed by the CLI.]

## Skill Version(s):

1.7.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
