## Description:

Look up concert setlists and live-music history via setlist.fm for artist, venue, city, date, tour, and live-performance questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and music researchers use this skill to answer natural-language questions about concert setlists, live-performance history, venues, tours, and attended shows using setlist.fm data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the referenced current MCP package can modify a user's setlist.fm attended-show list if write tools are invoked with confirmation.

Mitigation: For read-only setlist lookup use, provide only SETLIST_API_KEY and avoid enabling session-cookie or browser-bridge access.

Risk: The skill depends on a user-provided setlist.fm API key.

Mitigation: Keep SETLIST_API_KEY in environment or local configuration only, and do not include it in prompts, outputs, logs, or shared files.

Risk: setlist.fm API terms require attribution and restrict persistent caching of fetched data.

Mitigation: Include followable setlist.fm links in user-facing answers and treat results as live, point-in-time data rather than building a local datastore.

## Reference(s):

- [setlist ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist)
- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with setlist.fm source links, JSON configuration snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should cite followable setlist.fm source links, avoid exposing SETLIST_API_KEY, and treat returned live data as point-in-time.]

## Skill Version(s):

0.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
