## Description:

Look up real-estate listings, property details, photos, price history, and resolve addresses on Compass via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate researchers use this skill to query Compass listings, retrieve property records and media, compare listings, resolve addresses, and calculate affordability or mortgage payments through a configured MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run unpinned external code for the MCP server and browser extension.

Mitigation: Pin exact npm package versions and Git commits before installation, and review changes before updating.

Risk: The browser extension operates through a signed-in Compass session.

Mitigation: Use a dedicated Chrome profile for Compass with no unrelated signed-in accounts, and review the extension manifest and permissions before loading it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp)
- [compass-mcp source repository](https://github.com/chrischall/compass-mcp)
- [fetchproxy source repository](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command snippets plus structured MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Compass lookup outputs may include listing records, photo URLs, price history, property comparisons, mortgage or affordability calculations, session diagnostics, and per-target errors.]

## Skill Version(s):

0.14.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
