## Description:

Look up real-estate listings, property details, market reports, and saved homes/searches on Redfin via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Redfin listing data, property details, market reports, mortgage calculations, and saved Redfin homes or searches through an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run unpinned external code and load an unpacked browser extension into a signed-in Chrome session.

Mitigation: Use a pinned and reviewed redfin-mcp version and fetchproxy commit, inspect extension permissions, and run the extension in a dedicated Chrome profile.

Risk: Saved homes and saved searches can expose personal Redfin account data.

Mitigation: Invoke saved-home and saved-search tools only when explicitly requested and treat returned account data as personal information.

Risk: Redfin does not publish a public consumer API, so private endpoint behavior, WAF challenges, or authenticated session state may affect reliability.

Mitigation: Review the MCP behavior before deployment and expect users to resolve browser challenges or session authentication issues in the bridged Chrome profile.

## Reference(s):

- [ClawHub redfin skill page](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp source](https://github.com/chrischall/redfin-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return compact or full Redfin payload views depending on the invoked MCP tool; saved-home and saved-search tools require a signed-in Redfin browser session.]

## Skill Version(s):

0.13.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
