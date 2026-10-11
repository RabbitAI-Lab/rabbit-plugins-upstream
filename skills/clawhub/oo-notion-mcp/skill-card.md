## Description:

Helps agents search and read connected Notion pages, comments, and account information through OOMOL's Notion MCP connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents with an OOMOL-connected Notion account use this skill to find and read pages and comments, identify the connected user, and check available tool access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup suggests running an unverified remote installer script.

Mitigation: Install the CLI manually from a trusted source and verify it before use; do not let an agent run the remote installer automatically.

Risk: OOMOL mediates access to connected Notion data.

Mitigation: Use the connector only if that data-access arrangement is acceptable for the information involved.

## Reference(s):

- [Notion MCP skill release](https://clawhub.ai/oomol/skills/oo-notion-mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Notion MCP connection](https://console.oomol.com/app-connections?provider=notion_mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include page metadata, search results, comments, and tool-access notices.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
