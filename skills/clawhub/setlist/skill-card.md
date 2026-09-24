## Description:

Setlist helps agents look up concert setlists and live-music history through the setlist.fm MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and music researchers use this skill to find artist, venue, city, tour, date, and user setlist information. It also guides agents through setlist.fm attribution, API-key setup, batching, pagination, and interpretation of live-performance data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The attendance tools can change the user's setlist.fm account state.

Mitigation: Confirm explicit user intent before marking or unmarking attendance.

Risk: The skill requires a setlist.fm API key and MCP server setup before lookups work.

Mitigation: Install it only when setlist.fm access is intended, keep SETLIST_API_KEY private, and verify connectivity with the healthcheck tool.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist)
- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires setlist-mcp server registration and SETLIST_API_KEY; setlist.fm results should preserve attribution links.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
