## Description: <br>
Look up concert setlists and live-music history via setlist.fm. Use when the user asks what songs an artist played at a show, their tour setlists, what was performed at a venue or on a date, or wants to find concerts by artist, venue, city, or year. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and music researchers use this skill to query setlist.fm for concert setlists, artists, venues, cities, countries, tours, and public user activity through a registered MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The npm MCP package may expose authenticated attendance-changing tools even though the skill text describes the workflow as read-only. <br>
Mitigation: Review the package version before running it and avoid providing SETLIST_SESSION_COOKIE or browser-cookie access unless account-changing features are intended. <br>
Risk: The skill requires a setlist.fm API key. <br>
Mitigation: Keep SETLIST_API_KEY private and avoid exposing it in prompts, logs, shared configuration, or returned results. <br>
Risk: Use of setlist.fm data is subject to setlist.fm API terms, including attribution and commercial-use requirements. <br>
Mitigation: Cite returned setlist.fm source URLs and confirm permission before commercial use of setlist.fm API data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist) <br>
- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp) <br>
- [setlist-mcp source repository](https://github.com/chrischall/setlist-mcp) <br>
- [setlist.fm API key settings](https://www.setlist.fm/settings/api) <br>
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON configuration examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include setlist.fm URLs, song lists, venue and artist identifiers, pagination details, and batch resolution status.] <br>

## Skill Version(s): <br>
0.9.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
