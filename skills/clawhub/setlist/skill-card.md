## Description: <br>
Looks up concert setlists and live-music history through setlist.fm, including artists, shows, tours, venues, cities, and dates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to answer concert setlist, tour, venue, artist, city, date, and live-performance history questions with setlist.fm-backed results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a user-provided setlist.fm API key. <br>
Mitigation: Use an API key intended for this integration, keep it in environment configuration, and avoid exposing it in prompts or outputs. <br>
Risk: Free setlist.fm API access may not be permitted for commercial workflows. <br>
Mitigation: Confirm setlist.fm permission before using free API access in commercial contexts. <br>
Risk: Setlist data is live and may include empty stubs or point-in-time results. <br>
Mitigation: Cite setlist.fm source links, surface stub status when relevant, and avoid treating responses as a persistent local datastore. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist) <br>
- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp) <br>
- [setlist.fm API settings](https://www.setlist.fm/settings/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown answers with source links and inline JSON or shell configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only setlist.fm lookups; requires a user-provided SETLIST_API_KEY and source citation for setlist.fm results.] <br>

## Skill Version(s): <br>
0.9.3 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
