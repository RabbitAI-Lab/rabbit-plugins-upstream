## Description:

Look up concert setlists and live-music history via setlist.fm for artist, venue, city, date, tour, and song-list questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to configure and operate a setlist.fm MCP server so an agent can answer concert setlist, venue, tour, and live-performance history questions. The skill also guides users to cite setlist.fm results and handle API-key-backed live data appropriately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server-resolved security summary says the recommended runtime package exposes account-attendance write tools and session-cookie use while the skill describes itself as read-only.

Mitigation: Pin and review the npm package version before use, and do not provide a setlist.fm session cookie or browser-cookie bridge unless the deployment intentionally allows attended-show marker management.

Risk: The skill depends on a setlist.fm API key and live third-party API responses.

Mitigation: Keep SETLIST_API_KEY scoped to setlist.fm, do not display or log the key in agent responses, cite returned setlist.fm URLs, and avoid persistent caching of setlist.fm data.

Risk: The artifact notes that free setlist.fm API keys cover non-commercial use and commercial use needs permission.

Mitigation: Confirm setlist.fm permission or licensing terms before using API-backed outputs in a commercial workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist)
- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses should cite setlist.fm result URLs, treat results as live point-in-time data, and avoid exposing the SETLIST_API_KEY value.]

## Skill Version(s):

0.9.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
