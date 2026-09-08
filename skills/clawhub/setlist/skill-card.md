## Description:

Look up concert setlists and live-music history via setlist.fm for artists, venues, tours, cities, dates, and users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to answer live-music questions, resolve concert setlists, inspect venue or artist performance history, and prepare setlist.fm-backed responses with source attribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a setlist.fm API key and external setlist-mcp package/source.

Mitigation: Verify the package/source before installation and keep SETLIST_API_KEY private.

Risk: Attendance mark and unmark tools can change a user's setlist.fm account state.

Mitigation: Run attendance actions only after explicit user confirmation.

Risk: setlist.fm free API keys are documented for non-commercial use and commercial use may require permission.

Mitigation: Confirm setlist.fm API terms before using the integration in commercial workflows.

Risk: Some setlists may be stubs or tour-reference fallbacks rather than exact show song lists.

Mitigation: Surface hasSongs, song counts, and tourReference labels so users can tell exact results from references.

## Reference(s):

- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text responses with optional JSON snippets and shell or configuration blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should preserve setlist.fm source links, avoid exposing SETLIST_API_KEY, and distinguish exact setlists from tour-reference fallbacks.]

## Skill Version(s):

0.11.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
