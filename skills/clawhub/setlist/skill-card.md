## Description:

Looks up concert setlists and live-music history through setlist.fm using the setlist-mcp integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer live-music questions about artists, venues, tours, dates, and specific concert setlists. It helps agents resolve setlist.fm artist, venue, city, country, user, and setlist records and present sourced results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm package or source installation path.

Mitigation: Before installing, confirm the setlist-mcp package or source repository is trusted.

Risk: The setlist.fm API key is a credential required for operation.

Mitigation: Keep SETLIST_API_KEY private and avoid exposing it in prompts, logs, or responses.

Risk: setlist.fm data and API terms impose attribution, caching, and commercial-use obligations.

Mitigation: Cite followable setlist.fm source links, avoid persistent local caching, and obtain permission for commercial API use when required.

## Reference(s):

- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp)
- [setlist-mcp source](https://github.com/chrischall/setlist-mcp)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown or text responses with sourced setlist.fm links and optional configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only setlist.fm lookups require a SETLIST_API_KEY and registered setlist MCP server.]

## Skill Version(s):

0.9.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
