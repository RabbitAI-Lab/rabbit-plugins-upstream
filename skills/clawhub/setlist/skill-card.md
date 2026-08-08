## Description:

Look up concert setlists and live-music history via setlist.fm for artist, venue, city, tour, date, and user-attendance questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and query a read-only setlist.fm MCP server for concert setlists, live-music history, artist details, venue history, city and country lookup, and tour context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external npm MCP package or GitHub source that the user must trust before installation.

Mitigation: Install only from a trusted package/source and review the package before enabling it in an agent environment.

Risk: The setlist.fm API key is required and could be exposed if placed in prompts, logs, or shared configuration.

Mitigation: Store SETLIST_API_KEY as an environment secret and avoid including it in user-visible output.

Risk: setlist.fm API data is subject to attribution, non-commercial-use, and caching requirements.

Mitigation: Present followable setlist.fm source links with results, avoid persistent local caching, and obtain setlist.fm permission for commercial API use when required.

## Reference(s):

- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a registered setlist MCP server and SETLIST_API_KEY; setlist results should include followable setlist.fm source links.]

## Skill Version(s):

0.9.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
