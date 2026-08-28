## Description:

Look up concert setlists and live-music history via setlist.fm for artists, tours, venues, cities, and dates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and call the setlist MCP server for concert setlist, artist, venue, city, country, and user lookup workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended install target may expose under-disclosed setlist.fm account or session write capabilities.

Mitigation: Use a pinned package version, avoid SETLIST_SESSION_COOKIE or browser-bridge access unless attendance changes are intended, and prefer configurations that expose only read-only lookup tools.

Risk: The skill depends on a setlist.fm API key and live third-party data.

Mitigation: Keep SETLIST_API_KEY private, cite setlist.fm result URLs, avoid persistent caching, and treat responses as point-in-time data.

## Reference(s):

- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp)
- [setlist-mcp declared source link](https://github.com/chrischall/setlist-mcp)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include setlist.fm source URLs and MCP configuration snippets; requires SETLIST_API_KEY for server use.]

## Skill Version(s):

0.9.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
