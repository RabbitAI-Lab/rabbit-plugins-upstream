## Description:

setlist helps agents look up concert setlists and live-music history via setlist.fm for artist, venue, city, tour, date, and year questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer live-music questions by finding setlists, artists, venues, tours, cities, and user concert history through a registered setlist.fm MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setlist.fm API key could be exposed or stored somewhere inappropriate.

Mitigation: Store SETLIST_API_KEY only in trusted MCP configuration or environment storage, and do not include the key in prompts, logs, or shared outputs.

Risk: Attendance tools can change the user's setlist.fm account when marking or unmarking shows.

Mitigation: Require explicit confirmation before using attendance tools and verify the target setlist before submitting the action.

Risk: setlist.fm terms include attribution, non-commercial API-key limits, and restrictions on persistent caching.

Mitigation: Cite returned setlist.fm source URLs, avoid building local persistent copies, and confirm permission before commercial use of setlist.fm API data.

Risk: Live setlist data can be incomplete, ambiguous, or point-in-time.

Mitigation: Disambiguate with artist, date, city, and venue when possible, skip empty stub setlists unless relevant, and label tour-reference results as representative rather than exact-show data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist)
- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and MCP tool usage instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires setlist-mcp registration and SETLIST_API_KEY; setlist.fm results should include source URLs.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
