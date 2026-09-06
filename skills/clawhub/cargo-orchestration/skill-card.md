## Description:

Cargo Orchestration helps agents run Cargo connector actions, workflows, batches, AI-agent messages, node diagrams, and runtime SQL queries through the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to discover Cargo resources, execute single-record or batch workflows, message Cargo AI agents, inspect orchestration state, and generate workflow diagrams before approving changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can start runs, create batches, change live workflows, and trigger actions against connected systems.

Mitigation: Use it only with trusted agents and confirm the target workspace, action, workflow, destination system, filters, record counts, and expected cost before execution.

Risk: Large batches or empty filters can apply actions to many records and consume unexpected credits.

Mitigation: Sample 10-20 records first, report observed cost and hit rate, and get explicit approval with the full record count and credit estimate before full enrollment.

Risk: Using the latest Cargo CLI package can change behavior as the CLI evolves.

Mitigation: Consider pinning the Cargo CLI version for controlled deployments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/cargo-orchestration)
- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Cargo CLI - Orchestration](SKILL.md)
- [Action examples](references/examples/actions.md)
- [AI agent examples](references/examples/agents.md)
- [Play examples](references/examples/plays.md)
- [Orchestration query examples](references/examples/queries.md)
- [Segment data examples](references/examples/segments.md)
- [Orchestration templates](references/examples/templates.md)
- [Tool examples](references/examples/tools.md)
- [Filter syntax](references/filter-syntax.md)
- [Diagramming a node graph](references/node-diagram.md)
- [Prefer built-in actions + expressions over code/HTTP nodes](references/node-selection.md)
- [Creating nodes](references/nodes.md)
- [Async polling reference](references/polling.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Cargo CLI commands, SQL queries, workflow node JSON, polling instructions, diagrams, and approval guidance.]

## Skill Version(s):

1.11.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
