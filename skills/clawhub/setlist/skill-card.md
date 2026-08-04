## Description: <br>
Looks up concert setlists and live-music history through setlist.fm for questions about songs played by artists, tour setlists, venues, cities, dates, and concerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to answer live-music questions by querying setlist.fm for artist, venue, tour, date, and city setlist data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The referenced MCP package may expose account-attendance write tools and browser or session-cookie handling that the skill file does not disclose. <br>
Mitigation: Review before installing, use only a setlist.fm API key for read-only lookup, avoid session-cookie or browser-cookie bridging, and pin or audit the package version when deploying. <br>
Risk: Using attendance-marking features would grant account-changing access beyond read-only setlist lookup. <br>
Mitigation: Use any account-changing feature only with explicit confirmation and separate review of the configured server capabilities. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist) <br>
- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp) <br>
- [setlist.fm API key settings](https://www.setlist.fm/settings/api) <br>
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with source links, setup snippets, and MCP tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results should cite setlist.fm URLs, require a setlist.fm API key, and avoid exposing credentials.] <br>

## Skill Version(s): <br>
0.9.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
