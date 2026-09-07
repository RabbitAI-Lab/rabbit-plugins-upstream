## Description:

Look up real-estate listings, property details, market reports, mortgage calculations, and saved Redfin homes or searches through an MCP-backed Redfin integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Redfin listing searches, property details, market reports, mortgage calculations, and signed-in saved homes or saved searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server uses the user's active Redfin browser session and can read saved homes and saved searches.

Mitigation: Install only for users who are comfortable exposing Redfin account data to the MCP server, and treat saved-home and saved-search results as personal account data.

Risk: The runtime depends on the external redfin-mcp package and fetchproxy browser extension, whose code is not contained in this skill artifact.

Mitigation: Review the external package and browser extension before installation and before enabling the integration in a signed-in browser session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp project repository](https://github.com/chrischall/redfin-mcp)
- [fetchproxy extension repository](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON and shell command snippets when setup or MCP configuration is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Redfin listing data, market metrics, saved-home or saved-search summaries, and local mortgage or affordability calculations.]

## Skill Version(s):

0.13.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
