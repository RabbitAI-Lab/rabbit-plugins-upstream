## Description:

Drive Cargo from its hosted MCP server at https://mcp.getcargo.io/mcp: connect a client, discover and price an action, run it over one record or a batch, poll it, and read workspace models, with no CLI install.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to Cargo's hosted MCP server, choose the right Cargo surface, discover and price actions, execute single-record or batch actions, poll runs, and read workspace models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can operate against the wrong Cargo workspace if the connected token is not the intended workspace.

Mitigation: Open each session with whoami and name the resolved workspace before reading data or spending credits.

Risk: Batch or enrichment actions can spend credits and may produce uncertain hit rates.

Mitigation: Confirm the expected record count, run a small sample when appropriate, report observed cost and hit rate, and obtain approval before full execution.

Risk: Actions may touch personal or account data through third-party integrations.

Mitigation: Confirm permitted data use, lawful basis, suppression checks, and job relevance before sourcing, enriching, or contacting people.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-mcp)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo hosted MCP server](https://mcp.getcargo.io/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Cargo MCP tool-selection guidance, workspace checks, cost and batch execution guidance, and summarized run results.]

## Skill Version(s):

1.0.2 (source: frontmatter, skill-metadata.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
