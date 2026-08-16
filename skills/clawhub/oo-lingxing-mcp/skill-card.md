## Description:

Lingxing MCP helps agents discover and run Lingxing ERP MCP tools through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to discover Lingxing ERP MCP tools and run Lingxing MCP actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can call Lingxing ERP tools through a generic action, and some available tools may create, update, delete, or overwrite ERP data.

Mitigation: Inspect the live tool schema before execution and require explicit user confirmation for any action that could change business records.

Risk: The skill's read-focused summary can understate the impact of actions exposed by the Lingxing ERP connector.

Mitigation: Treat the server security verdict and guidance as authoritative during review, and install the skill only when users are prepared to validate each selected tool and payload.

## Reference(s):

- [Lingxing MCP homepage](https://www.lingxing.com/help/article/mcp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub release page](https://clawhub.ai/oomol/skills/oo-lingxing-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from connector actions are returned as structured JSON with data and execution metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
