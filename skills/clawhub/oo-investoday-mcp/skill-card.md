## Description:

Investoday MCP (data-api.investoday.net) helps agents search and read Investoday financial market data through the OOMOL-connected Investoday MCP connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Investoday MCP action schemas, query China market datasets, retrieve quotes and fundamentals, generate charts, and search research or announcement data through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The oo CLI installer is invoked with a pipe-to-shell pattern that the security evidence flags as unverified.

Mitigation: Review the installer source first or use a safer verified installation path before installing the CLI.

Risk: The generic call_tool dispatcher may exceed the stated read-only scope if a live Investoday MCP tool has unclear or state-changing behavior.

Mitigation: Inspect the live schema and behavior annotations before use, and require explicit user approval for tools that write, delete, post, modify account data, or have unclear effects.

## Reference(s):

- [Investoday MCP homepage](https://data-api.investoday.net/mcp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-investoday-mcp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON data with execution metadata.]

## Skill Version(s):

1.0.1 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
