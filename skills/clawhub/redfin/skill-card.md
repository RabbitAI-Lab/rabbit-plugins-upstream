## Description:

Look up real-estate listings, property details, market reports, and your saved homes/searches on Redfin via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Redfin listings, property records, market reports, mortgage calculations, and signed-in saved Redfin homes or searches through an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved-home and saved-search tools use the user's signed-in Redfin browser session and can retrieve account-specific Redfin information.

Mitigation: Use saved-data tools only when the user explicitly wants account-specific Redfin information retrieved.

Risk: The skill depends on the third-party redfin-mcp package and fetchproxy Chrome extension.

Mitigation: Install only after reviewing and accepting those dependencies and their browser-session behavior.

Risk: Redfin private endpoints, browser challenges, or session state can affect availability or returned data.

Mitigation: Verify important property, market, or financial details against Redfin or another authoritative source before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp source](https://github.com/chrischall/redfin-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with structured Redfin listing details and setup snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact responses strip most image URLs; full responses can return upstream Redfin payloads.]

## Skill Version(s):

1.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
