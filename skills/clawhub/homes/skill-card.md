## Description:

Look up real-estate listings, property details, price and tax history, market reports, saved homes, and photo galleries on homes.com through the homes-mcp MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent query homes.com property listings, property records, price and tax history, market reports, saved account items, and photo galleries through homes-mcp.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing this skill runs external npm package code and depends on a separate browser extension connected to a signed-in homes.com session.

Mitigation: Review homes-mcp and the fetchproxy extension before installing, and pin exact package versions or commits where possible.

Risk: Saved homes and saved searches can expose account-specific homes.com data to the agent.

Mitigation: Use a dedicated browser profile when appropriate, and request saved homes or saved searches only when that account data should be shared with the agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [homes-mcp source link from artifact](https://github.com/chrischall/homes-mcp)
- [fetchproxy setup link from artifact](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with MCP tool guidance and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only homes.com data; compact responses strip image URLs except for the photo-gallery tool.]

## Skill Version(s):

1.4.5 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
