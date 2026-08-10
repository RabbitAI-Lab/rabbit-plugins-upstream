## Description:

Interact with the Cargo platform via CLI. Use when the user wants to execute an action, run a workflow, trigger a batch, message an AI agent, query orchestration runtime tables (runs/batches/spans/records) with SQL, fetch segment records, resolve an action's output schema, or inspect a model schema.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run and inspect Cargo orchestration workflows, actions, batches, agents, runtime queries, segments, templates, and model schemas from an agent-assisted CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide live Cargo workflow, batch, segment, file, CRM, and webhook operations with real workspace authority.

Mitigation: Use a test workspace or least-privilege account where possible, verify every workflow, segment, connector, and model UUID, and require explicit confirmation before deploy, cancel, segment removal, CRM write, or external webhook operations.

Risk: Large batches can create broad data changes or unexpected credit spend.

Mitigation: Run a 10-20 record sample first, report observed cost and hit rate, estimate full enrollment cost from the real record count, and wait for explicit user approval before processing the full set.

Risk: File uploads, webhook secrets, OAuth tokens, and API tokens can expose sensitive data if handled casually.

Mitigation: Avoid uploading sensitive files unless approved, keep webhook secrets and tokens out of shell history, and verify the authenticated session with cargo-ai whoami before running commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-orchestration)
- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Cargo CLI orchestration entrypoint](SKILL.md)
- [Action examples](references/examples/actions.md)
- [AI agent examples](references/examples/agents.md)
- [Play examples](references/examples/plays.md)
- [Orchestration query examples](references/examples/queries.md)
- [Segment data examples](references/examples/segments.md)
- [Orchestration templates](references/examples/templates.md)
- [Tool examples](references/examples/tools.md)
- [Filter syntax](references/filter-syntax.md)
- [Node selection guidance](references/node-selection.md)
- [Creating nodes](references/nodes.md)
- [Async polling reference](references/polling.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON payload examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the cargo-ai CLI and a Cargo account authenticated by browser OAuth or API token.]

## Skill Version(s):

1.6.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
