## Description:

Look up real-estate listings, property details, market reports, and your saved homes/searches on Redfin via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query Redfin listings, property details, market reports, mortgage calculations, saved homes, and saved searches through the redfin-mcp server. It is useful when real-estate research should be grounded in Redfin data and the user can provide an authenticated browser session when account-specific activity is requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running unpinned third-party MCP code and a browser extension can introduce unexpected behavior after upstream changes.

Mitigation: Pin reviewed package versions or commits before use, and audit the browser extension permissions before installing or updating it.

Risk: The browser extension can operate with a signed-in Redfin session, including access to saved homes and saved searches.

Mitigation: Use a dedicated browser profile for Redfin and request saved account activity only when the user explicitly intends to share it.

## Reference(s):

- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp repository](https://github.com/chrischall/redfin-mcp)
- [fetchproxy repository](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Redfin listing details, property records, market metrics, saved account activity summaries, MCP setup snippets, and local mortgage or affordability calculations.]

## Skill Version(s):

0.13.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
