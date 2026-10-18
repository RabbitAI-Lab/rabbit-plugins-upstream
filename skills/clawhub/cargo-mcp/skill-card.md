## Description:

Guides agents in connecting to Cargo's hosted MCP server, selecting and pricing actions, running single or batch jobs, and reading workspace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to connect an MCP client to Cargo, confirm their workspace, discover and run priced actions, monitor batches, and query workspace models. It also helps route platform administration and reusable workflows to the CLI instead.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A token can expose or modify data in the wrong workspace.

Mitigation: Use workspace-scoped tokens stored in environment variables and confirm the workspace before acting.

Risk: Batch actions can spend credits or affect connected business systems.

Mitigation: Check action pricing, test a small batch, and obtain explicit approval before a full run.

Risk: Actions involving people can misuse personal data or send unwanted outreach.

Mitigation: Check lawful basis, suppression status, and relevance before sourcing, enriching, or contacting people.

## Reference(s):

- [Cargo MCP skill on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-mcp)
- [Cargo hosted MCP endpoint](https://mcp.getcargo.io/mcp)
- [Cargo skills homepage (listed in skill metadata; import provenance unavailable)](https://github.com/getcargohq/cargo-skills)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands]

**Output Format:** [Markdown with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Model queries return at most 50 rows; action execution may consume credits.]

## Skill Version(s):

1.1.0 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
