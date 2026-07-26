## Description: <br>
Look up concert setlists and live-music history via setlist.fm for questions about songs played at shows, tour setlists, venues, dates, artists, cities, and years. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to the setlist.fm MCP server for read-only concert, artist, venue, tour, city, country, and public user activity lookups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends concert lookup terms and public user lookup requests to setlist.fm. <br>
Mitigation: Use it only when that external API use is acceptable, and avoid public user lookups when they could expose activity tied to a setlist.fm account. <br>
Risk: The MCP server requires a setlist.fm API key. <br>
Mitigation: Store SETLIST_API_KEY in the MCP environment or local configuration and do not include it in prompts, logs, or responses. <br>
Risk: setlist.fm API terms limit free API keys to non-commercial use and restrict persistent caching. <br>
Mitigation: Confirm the applicable setlist.fm terms for the deployment, cite setlist.fm result URLs, and avoid building a local datastore from returned data. <br>
Risk: Installation uses npx or source code from a third-party package. <br>
Mitigation: Install only from trusted package and source locations, pin or review the package version when appropriate, and keep normal dependency review controls in place. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist-mcp) <br>
- [npm package](https://www.npmjs.com/package/setlist-mcp) <br>
- [Source repository](https://github.com/chrischall/setlist-mcp) <br>
- [setlist.fm API key settings](https://www.setlist.fm/settings/api) <br>
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown or text responses with source links and structured setlist details from setlist.fm] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only MCP tool calls require SETLIST_API_KEY and may return paginated or pending results for larger lookups.] <br>

## Skill Version(s): <br>
0.7.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
