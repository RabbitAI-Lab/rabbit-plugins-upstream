## Description:

Look up concert setlists and live-music history via setlist.fm using a registered setlist MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query setlist.fm through a registered setlist MCP server for artist, venue, tour, city, date, and user setlist information. It supports live-music research workflows such as finding songs performed at a concert, locating shows at a venue, and resolving batches of concerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation frames the server as read-only while attendance tools can change a user's setlist.fm account state.

Mitigation: Treat setlist_mark_attended and setlist_unmark_attended as account-changing actions and require explicit user confirmation before use.

Risk: The recommended npx setup can run the setlist-mcp package without pinning a reviewed version.

Mitigation: Pin setlist-mcp to an audited package version or a specific reviewed source commit before deployment.

Risk: SETLIST_API_KEY is required for API access and could expose account access if mishandled.

Mitigation: Keep SETLIST_API_KEY private, scope it appropriately, and avoid printing or storing it in generated output.

Risk: setlist.fm data is live external data and may be incomplete, stale, rate-limited, or subject to attribution and usage terms.

Mitigation: Cite returned setlist.fm URLs, treat results as point-in-time, avoid persistent caching, and review setlist.fm terms for the intended use.

## Reference(s):

- [setlist skill page](https://clawhub.ai/chrischall/skills/setlist)
- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp)
- [setlist-mcp source link listed in artifact](https://github.com/chrischall/setlist-mcp)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON configuration snippets, shell commands, and natural-language guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include setlist.fm URLs for attribution and compact or full MCP response guidance.]

## Skill Version(s):

0.11.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
