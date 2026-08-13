## Description:

Interact with the Cargo platform via CLI. Use when the user wants to execute an action, run a workflow, trigger a batch, message an AI agent, query orchestration runtime tables (runs/batches/spans/records) with SQL, fetch segment records, resolve an action's output schema, or inspect a model schema.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to direct Cargo CLI orchestration tasks, including running actions, workflows, batches, AI agent messages, orchestration SQL queries, segment fetches, output schema inspection, and model schema inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cargo operations can trigger costly remote workflows, upload data, or write to connected systems.

Mitigation: Use the skill only in authorized workspaces, confirm scope and cost before mutating or large-batch actions, and prefer samples, sandbox connectors, and least-privilege credentials.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-orchestration)
- [Action examples](references/examples/actions.md)
- [AI agent examples](references/examples/agents.md)
- [Play examples](references/examples/plays.md)
- [Orchestration query examples](references/examples/queries.md)
- [Segment data examples](references/examples/segments.md)
- [Orchestration templates](references/examples/templates.md)
- [Tool examples](references/examples/tools.md)
- [Prefer built-in actions + expressions over code/HTTP nodes](references/node-selection.md)
- [Creating nodes](references/nodes.md)
- [Async polling reference](references/polling.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-directed Cargo CLI procedures and command arguments; commands may trigger remote workflows, uploads, or writes to connected systems when executed.]

## Skill Version(s):

1.6.1 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
