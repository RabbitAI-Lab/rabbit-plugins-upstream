## Description:

Yingmi MCP helps agents use the OOMOL oo CLI to discover and call Yingmi MCP financial data, research, and advisory tools with live schemas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Yingmi MCP tool schemas and run Yingmi MCP actions through an OOMOL-connected account. It is useful for financial data, research, and advisory workflows that require schema-aware MCP tool calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup guidance includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Install the oo CLI only from a trusted OOMOL distribution path and prefer pinned, signed, or checksum-verified releases before running installer commands.

Risk: Live Yingmi MCP tool schemas and behavior annotations can change over time.

Mitigation: Inspect the live schema before constructing payloads and require explicit confirmation for write or destructive actions.

Risk: The skill depends on an OOMOL-connected account and external Yingmi MCP availability.

Mitigation: Confirm the user is signed in, the Yingmi MCP connection is active, and billing or scope errors are resolved before retrying failed actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-yingmi-mcp)
- [Yingmi MCP homepage](https://qieman.com/mcp/mcp-market)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from Yingmi MCP actions when the oo CLI is run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
