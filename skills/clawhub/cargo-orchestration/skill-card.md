## Description:

Cargo Orchestration helps agents run and inspect Cargo CLI workflows, connector actions, batches, AI agent messages, node graphs, diagrams, and runtime SQL queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, operations teams, and developers use this skill to operate Cargo workspaces through the Cargo CLI: execute actions, run or batch workflows, message AI agents, build and validate node graphs, draw workflow diagrams, and query orchestration history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run, deploy, and mutate high-impact Cargo automations.

Mitigation: Install it only for users authorized to operate the target Cargo workspace and confirm the active workspace, connector accounts, and destination systems before running commands.

Risk: Batch and connector operations can affect many records, consume credits, or send personal and customer data to enrichment, CRM, or AI providers.

Mitigation: Use samples and narrow filters first, report record counts and credit estimates, and require explicit approval before full batches or deployments.

Risk: Segment removal and broad workflow changes can delete or reroute business automation state.

Mitigation: Avoid segment removal unless the intended deletion is clear, and validate or diagram workflow changes before execution.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
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
- [Prefer built-in actions and expressions over code/HTTP nodes](references/node-selection.md)
- [Filter syntax](references/filter-syntax.md)
- [Async polling reference](references/polling.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON payload examples, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs often include Cargo CLI commands and JSON request or response shapes for workspace operations.]

## Skill Version(s):

1.9.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
