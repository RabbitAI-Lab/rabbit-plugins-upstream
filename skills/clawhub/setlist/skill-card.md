## Description:

Look up concert setlists and live-music history via setlist.fm, including artist, venue, city, date, and tour searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for setlist.fm concert history, resolve artist, venue, city, date, and tour queries, and configure the setlist MCP server when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags an unpinned npm-based MCP install path.

Mitigation: Use a pinned, trusted version of setlist-mcp or a reviewed commit before installing.

Risk: The skill requires a setlist.fm API key.

Mitigation: Store the API key in user-scoped environment configuration and avoid committing it to shared project files.

Risk: Attendance tools can change the user's setlist.fm account attendance history.

Mitigation: Only enable or invoke attendance write tools after explicit confirmation from the account owner.

Risk: setlist.fm results are live third-party data subject to API terms.

Mitigation: Show setlist.fm source links with results, avoid persistent caching, and confirm commercial API permission where required.

## Reference(s):

- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with setlist.fm links, JSON MCP configuration snippets, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call setlist.fm through setlist-mcp; compact view strips media and avatar URLs by default.]

## Skill Version(s):

0.11.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
